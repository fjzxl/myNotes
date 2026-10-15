---
title: Calico 残留 iptables 规则导致云主机重启后 no route to host
tags:
  - programming
  - linux
  - kubernetes
  - network
aliases:
  - calico iptables 残留
  - k8s 重启后网络不通
  - no route to host 10250
  - kubectl logs no route to host
created: 2026-10-13
updated: 2026-10-15
---

# Calico 残留 iptables 规则导致云主机重启后 no route to host

> 实战案例（2026-10-13）：云主机重启后 k8s 拉起，calico 相关 pods 报错、ta-node2 上 CoreDNS 启动失败；排查中 `kubectl logs` 报 `dial tcp <node-ip>:10250: connect: no route to host`。根因是节点重启后 iptables 中残留的 calico 规则把入向流量 REJECT。日志见 [2026-10-13](../../../journal/daily/2026-10-13.md)。

## 集群与背景

- 3 节点集群：**ta-node1、ta-node2（172.26.190.131）、ta-node3**，网络插件 **Calico**。
- 本次 **ta-node2 与 ta-node3 两台重启**（ta-node1 一直在线），重启后集群自动拉起。

## 现象（时间线）

1. 节点重启后 k8s 组件恢复，但 **calico 相关 pods 启动报错**（未逐条细看日志）。
2. **ta-node2 上 CoreDNS 启动失败**。
3. 用 `kubectl logs` 抓 ta-node2 上故障 pod 的日志，**kubectl 本身报错**：

```text
$ kubectl logs -n kube-system <pod-name> -c calico-node --tail=50
Error from server: Get "https://ta-node2:10250/containerLogs/kube-system/calico-node-xxxxx/calico-node?tailLines=50":
dial tcp 172.26.190.131:10250: connect: no route to host
```

> **模式识别（本案例最有复用价值的一步）**：报错主体是 `Error from server: Get "https://<节点名>:10250/..."`——这是 **kube-apiserver → kubelet** 的取日志链路不通（10250 = kubelet 端口），**不是 pod 自身的日志**。看到它应立即把排查方向转向「该节点的入向网络被拦」，而不是继续盯着 CoreDNS / calico 的容器本身。

## 排查思路

### 本例实际路径（复盘）

1. kubectl 侧：发现 calico 相关 pods 报错、ta-node2 上 CoreDNS 启动失败。
2. 跨节点连通性探测：**`ping 172.26.190.131` 通；`telnet 172.26.190.131 10250` 超时；`curl https://172.26.190.131:10250` 超时**。
3. 读 pod 日志：`kubectl logs` 报 `Error from server: ... dial tcp 172.26.190.131:10250: no route to host`（apiserver → kubelet 链路）。
4. 检查防火墙 / iptables → 定位 calico 残留规则 → 清空 + 重启 calico → 恢复。

**每步证明了什么**：

- `ping` 通 → L3 正常：路由、链路、节点存活（ICMP 放行）；
- `telnet` / `curl` 超时 → TCP SYN 被静默丢弃（DROP 行为），**不是** `refused`（kubelet 在监听，只是流量到不了它）；
- **ping 通 + TCP 超时并存 = 端口级选择性拦截**——典型的 iptables 部分规则画像，可排除真·路由问题、整机宕机、安全组整体拦截；
- 细节：kubectl 报 `no route to host`（REJECT 特征）与手工探测超时（DROP 特征）**并存**，说明规则集处于「半成品」状态（不同链不同动作）；且此类故障中组件仍在自行恢复，**多次探测结果可能不同，记录时间点再对照**。

### 更优路径（在上述路径上的改进）

**第 0 步 · 读错误语义（零成本，最重要）**——内核报错类型直接暴露出问题的层：

| 报错 | 含义 | 第一嫌疑 |
|:---|:---|:---|
| `no route to host` | 有路由但被拒（EHOSTUNREACH） | iptables `REJECT --reject-with icmp-host-prohibited` |
| `connection refused` | 对端没监听 | kubelet 未启动 / 端口不符 |
| `i/o timeout` | 静默丢包 | iptables DROP / MTU / 安全组 |

**第 1 步 · kubectl 侧定位**：`kubectl -n kube-system get pods -o wide` 的 `NODE` 列把故障 pod 映射到节点；`kubectl get nodes` 注意 **Ready ≠ 节点网络正常**（kubelet 活着就报 Ready，CNI 坏不影响它）。

**第 2 步 · 连通性矩阵（把 ping / telnet / curl 三连升级为三对照）**——两条命令、三个对照，每个回答一个问题、给一句判读依据：

```bash
nc -vz -w 2 172.26.190.131 10250                          # 代替 telnet：可设超时、可批量测多端口
curl -k --connect-timeout 2 https://172.26.190.131:10250/healthz
```

| 命令 / 对照 | 回答的问题 | 判读依据（一句） |
|:---|:---|:---|
| `ping <节点IP>` | L3 通不通（路由 / 链路 / 存活） | 通 → 排除真·路由问题与宕机（本例：通） |
| `nc -vz -w 2 <IP> 10250` | 该端口 TCP 能否建立 | `succeeded` 通；超时 = DROP；no route to host = REJECT；refused = 未监听 |
| `curl -k --connect-timeout 2 https://<IP>:10250/healthz` | 到 kubelet 的 HTTPS 是否可用 | 401/403 = 网络通且 kubelet 活着——**任何 HTTP 状态码都证明网络层是通的** |
| 对照健康节点（ta-node1:10250） | 单点还是全局 | 健康节点同样不通 → 全局问题（apiserver 侧 / 全节点防火墙）；只有本节点不通 → 锁定 ta-node2 |
| 对照其他端口（ta-node2:22） | 拦截的粒度 | 22 通 + 10250 不通 = **端口特定规则**（iptables 精确拦截，本例画像）；22 也不通 = **整机入向被拦**（firewalld / 安全组） |
| 对照本机（登 ta-node2 打 `localhost:10250`） | 网络拦还是服务挂 | 本机通 + 跨节点不通 = 入向被拦；本机也 refused / 超时 = kubelet 自身问题 |

> 两个细节：必须 `https` + `-k`（10250 是 TLS 端口，`http://` 会得到混乱响应）；`nc -w 2` 与 `--connect-timeout 2` 让失败快速返回，不傻等。

**第 3 步 · 节点上抓拦截规则（计数器法）**：

```bash
iptables -L INPUT -n -v --line-numbers   # 另一节点循环 curl，看哪条 REJECT 的 pkts 计数在涨
systemctl status firewalld                # 必查：云镜像重启后 firewalld 自启，
                                          # 默认 REJECT 产生一模一样的 no route to host
nft list ruleset | grep cali              # nft 后端的等价检查
```

**终极手段 · tcpdump 双端同抓**——计数器看不出方向时，在源与目标同时抓包，看包死在哪一跳：

```bash
tcpdump -ni any host <源IP> and port 10250   # 两边各跑一条，对照包的进 / 出
```

**第 4 步 · 绕过 apiserver 取日志**：apiserver → kubelet 断了时 `kubectl logs/exec/top` 全不可用，登节点直接：

```bash
crictl ps -a | grep -E 'calico|coredns'
crictl logs --tail 50 <container-id>
# 或 /var/log/pods/<ns>_<pod>_<uid>/<container>/*.log
```

**第 5 步 · 修复后按序验证**：`kubectl logs` 可读 → calico pods Ready → CoreDNS 起来 → 跨节点 Service 连通。

## 根因

- **直接原因**：ta-node2（及 ta-node3）重启后，宿主机 iptables 里残留的 calico 规则把入向流量 REJECT——10250（kubelet）首当其冲：apiserver 取不到日志，节点上 pod 的启动依赖（网络、探针）受阻，表现为 CoreDNS 等「启动失败」。
- **深层原因**：节点**非正常重启**时 Calico（Felix）不保证清理自家 iptables 规则；开机后 k8s 组件与 calico-node 竞争恢复，calico 未 Ready 之前节点网络处于「半配置」状态——旧规则拦路，新规则未就位。

## 修复（推荐顺序：从首选到兜底）

**① 先排除 firewalld**——若 `firewall-cmd --state` 显示运行中，本例问题可能根本不是 calico：

```bash
systemctl disable --now firewalld   # k8s 节点通常不应运行 firewalld
```

**② 首选：让 Calico 自己重写规则**——只重启故障节点的 calico-node，Felix 会把规则集同步回期望状态，不动其他组件：

```bash
kubectl -n kube-system delete pod --field-selector spec.nodeName=ta-node2 -l k8s-app=calico-node
```

**③ 次选：定向清理 `cali-` 链**（机器上还有 Docker 等依赖 iptables 的组件时；`iptables -F` 会连它们一起清掉）。先备份，先摘挂载再删链，nat / mangle 表都要看：

```bash
iptables-save > /root/iptables.bak
iptables -S | grep -E '^-A .+ -j cali-' | sed 's/^-A /-D /' | while read -r r; do iptables $r; done
iptables -S | awk '/^(:|-N) cali-/ {print $2}' | sort -u | xargs -r -n1 iptables -F
iptables -S | awk '/^(:|-N) cali-/ {print $2}' | sort -u | xargs -r -n1 iptables -X
```

> `-X` 只能删除**空**链，所以必须先 `-F` 清空链内规则再删链（上面第二行）。nat / mangle 表同理：给三条命令各加 `-t nat` / `-t mangle` 再跑一遍。

**④ 兜底：`iptables -F`**——仅限「纯 k8s 节点、确认无其他 iptables 依赖」：

```bash
iptables -F
```

本例实际操作是 **多台节点 `iptables -F` + 重启 calico**（② + ④ 组合），能工作但杀面偏大；最小修复未做对照验证。

## 预防

- **k8s 节点禁用 firewalld**：云镜像重启后 firewalld 自启是 `no route to host` 的头号替身凶手。
- **计划内重启走标准流程**：`kubectl drain <node> --ignore-daemonsets` → `systemctl stop kubelet containerd` → 重启 → `kubectl uncordon`，让 calico 走正常清理 / 重建路径。
- **重启后 30 秒体检**：`iptables -S | grep -c cali-` 有无异常、`kubectl -n kube-system get ds calico-node` 就绪、CoreDNS endpoints 就绪、每节点 `curl -k https://localhost:10250/healthz`。
- **监控前移**：blackbox exporter 对每节点 10250 探测 + calico-node NotReady 告警，别等 CoreDNS 挂了才发现。
- **calico 保持较新版本**（旧版 Felix 的重启恢复路径修过多个 bug）。

## 同类 k8s 网络问题的通用排查框架

「到某节点 / 某端口不通」「pod 起不来疑似网络」这类问题，按四层定位，每层一个问题、一条命令：

**第 1 层 · 报错语义**：`no route to host`（REJECT）/ `timeout`（DROP）/ `refused`（未监听）——见上文三分法表。

**第 2 层 · 想清楚「谁 → 谁」**——k8s 里源-目标对决定链路，四类典型链路各有病根：

| 链路 | 典型症状 | 第一嫌疑 |
|:---|:---|:---|
| apiserver → kubelet 10250 | `kubectl logs/exec/top` 报 `:10250` | 节点入向 iptables / firewalld（本例） |
| pod → pod（跨节点） | PodCIDR 互 ping 不通 | CNI：calico BGP / VXLAN / IPinIP、节点路由表 |
| pod → Service | IP 直连通、Service 不通 | kube-proxy（iptables / ipvs 规则）、endpoints 为空 |
| pod → 外部域名 | IP 通、域名不通 | CoreDNS：副本数 / 上游 / ndots 五跳 |

**第 3 层 · 连通性矩阵（三对照）**：`nc -vz -w 2` 打「健康节点同端口 / 故障节点其他端口 / 本机 localhost」——区分端口特定拦截、整机拦截、服务未监听。

**第 4 层 · 定位到规则或组件**：iptables 计数器法 / firewalld 状态 / tcpdump 双端同抓；组件侧 `calico-node` Ready、`calicoctl node status`（BGP peer）、`ipvsadm -Ln`（Service 规则）、`kubectl -n kube-system get ep kube-dns`（CoreDNS endpoints）。

> 顺序原则：先用零成本的「读报错 + `kubectl get pods -o wide`」定向，再用带超时的探测划层，最后才上节点抓规则 / 抓包——每一步都缩小范围，不做重复测量。

## 关联

- [MOC - programming](../../../notes/MOC%20-%20programming.md) · Linux 专题
- 案例日志：[2026-10-13](../../../journal/daily/2026-10-13.md)

---

## 相关笔记

本篇在图谱里的邻居——从这里可以走到相关主题，也能被别人走回来。

- [MoE（负载均衡辅助损失 ↔ 这里的分布式限流，同一个别让某部分过载的思路）](../../ai/MoE.md)
- [Linux 4.9 内核编译（同一条 Linux 运维线）](linux-kernel-4.9-build.md)
