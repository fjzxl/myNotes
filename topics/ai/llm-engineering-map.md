---
title: LLM 工程知识地图 · 待补项分层攻略
tags:
  - ai
  - ai/llm
  - ai/moc-candidate
  - ai/learning-path
---

# LLM 工程知识地图：18 个待补项的分层攻略

> MOC - ai「待补充」区的 18 个空项迁到此处分层管理：**每项一句话 + 资源锚点 + 解锁时机**，写完一篇在这里勾掉并回链 [MOC - ai](../../notes/MOC%20-%20ai.md)。
> 锚点纪律：只标注**已核验**的（书本结构来自 PDF 目录提取）；标注「待定位」的，读进去后再补——宁可空着，不编页码。
> 页码缩写：AE = [AI Engineering 导读](ai-engineering.md)（页码为书内页码）；SLP3 = ⑬；d2l = ⑫；UDL = ⑪；AAB = [深入理解 AI Agent](understanding-ai-agent.md)。

---

## 一、总览

| 层 | 项数 | 内容 | 解锁时机 |
|---|---|---|---|
| L1 模型基础 | 5 | Transformer / Attention / 位置编码 / 训练流程 / 推理优化 | 随时可攻坚（SLP3·d2l·UDL 三路资源齐备）；与理论线阶段二/三同行最佳 |
| L2 应用工程 | 6 | Prompt / RAG / Fine-tuning / 评估 / Function Calling / MCP | 16 周同步线 W5-W10（AE p.49-175） |
| L3 部署 | 1 | 本地部署 | W14-W16（AE p.255-384） |
| L4 Agent | 3 | ReAct 系模式 / Memory / 多智能体框架 | W11-W13（AE p.176-254）；[Agent 实操线](agent-practice-plan.md) 同期实操场 |
| L5 产品与对比 | 3 | LLM 对比 / AI 编程工具 / 国产调研 | 调研型，无书锚；求职季前集中做 |

## 二、L1 模型基础（5 项）

| 项 | 一句话 | 资源锚点 | 状态 |
|---|---|---|---|
| Transformer 架构 | 自注意力堆出的序列机器，一切 LLM 的骨架 | SLP3 Ch7；d2l Ch10；UDL Ch12；AE p.23-28 | ⬜ |
| Attention 机制（Self / MHA / MQA / GQA） | 让每个 token 决定看谁、怎么加权取信息 | SLP3 Ch7；d2l Ch10；MQA/GQA 变体细节待定位 | ⬜ |
| 位置编码（PE / RoPE / ALiBi） | 自注意力本身无序，位置要额外注入 | d2l Ch10（位置编码节）；RoPE / ALiBi 原论文待定位 | ⬜ |
| 训练流程（预训练 / SFT / RLHF / DPO） | 三阶段把原始模型变成助手 | SLP3 Ch7（预训练）+ Ch8（post-training）；AE p.18（from scratch）+ p.37（用 LLM 训 LLM）；AAB Ch8 | ⬜ |
| 推理优化（KV-Cache / 投机解码 / 量化） | 推理贵在记忆与带宽，三件套各砍一头 | KV-Cache：AE p.326、AAB Ch2；量化：AE p.306（模型压缩节，覆盖度读后确认）；投机解码：待定位 | ⬜ |

## 三、L2 应用工程（6 项，W5-W10 解锁）

| 项 | 一句话 | 资源锚点 | 状态 |
|---|---|---|---|
| Prompt Engineering | 不动参数，动上下文来改变行为 | AE Ch2 p.49-65；AAB Ch2 | ⬜ |
| RAG 系统设计 | 检索外部知识拼进上下文 | AE Ch4 p.105-145（分块 p.118、8 架构 p.126）；AAB Ch3；SLP3 Ch11（IR and RAG） | ⬜ |
| Fine-tuning 实操（LoRA / QLoRA） | 动一小块参数适配任务 | AE Ch3 p.66-104（LoRA from scratch p.78）；理论侧：W7 原子卡 [稳定性与正则化](../../notes/regularization-and-stability.md) | ⬜ |
| 模型评估与基准 | 把「好不好用」变成可比较的信号 | AE Ch9 p.331-357；AAB Ch7（14 实验）；理论侧：W6 原子卡 [交叉验证与过拟合](../../notes/cross-validation-and-overfitting.md) | ⬜ |
| Function Calling / Tool Use | 给模型一个可调用的外部动作接口 | AE p.281（MCP vs Function Calling）；AAB Ch4 | ⬜ |
| MCP 协议 | 工具接入的标准化层 | AE Ch7 p.264-303；AAB Ch4；[Agent 实操线](agent-practice-plan.md) 阶段 B 实操 | ⬜ |

## 四、L3 部署（1 项，W14-W16 解锁）

| 项 | 一句话 | 资源锚点 | 状态 |
|---|---|---|---|
| 本地部署（Ollama / vLLM / llama.cpp） | 把模型跑在自己可控的机器上 | AE p.40（本地运行四种方式，具体覆盖工具读后确认）+ p.361（vLLM）+ p.365（LitServe） | ⬜ |

## 五、L4 Agent（3 项，W11-W13 解锁）

| 项 | 一句话 | 资源锚点 | 状态 |
|---|---|---|---|
| ReAct / Reflexion / Plan-and-Execute | 思考-行动-观察的循环及其变体 | AE p.205（ReAct 从零实现）+ p.199（5 设计模式，变体覆盖度读后确认）；[Claude Code](Claude%20Code.md) 拓扑实战 | ⬜ |
| Memory 系统（短期 / 长期 / 向量） | 跨轮次与会话保持状态 | AE p.195；AAB Ch3；实操线阶段 B | ⬜ |
| Multi-agent 协作框架（AutoGen / CrewAI / LangGraph） | 多智能体的组织层 | AE p.242（多智能体 7 模式）；框架本体需调研（各自官方文档）；实操线阶段 E | ⬜ |

## 六、L5 产品与对比（3 项，调研型）

| 项 | 一句话 | 方法建议 | 状态 |
|---|---|---|---|
| 主流 LLM 对比（GPT / Claude / Gemini / 开源） | 选型与成本的现实坐标 | 快照式笔记：固定维度（能力 / 价格 / 上下文窗口 / 许可），每季度更新一次并注明数据日期与来源 | ⬜ |
| AI 编程工具对比（Copilot / Cursor / Claude Code） | 自己的生产工具链选型 | 以 [Claude Code](Claude%20Code.md) 心得为底座，补实测对比 | ⬜ |
| 国产 LLM 调研 | 国内生态与合规选项 | 同快照法；结合求职线看目标公司技术栈 | ⬜ |

## 七、使用规则

1. 写完一项：状态 ⬜ → ✅，并回链新笔记；新笔记是原子概念走 `notes/`（permanent-note 模板），是主题走 `topics/ai/`。
2. 锚点「待定位」的，读到就在地补上——本地图的价值在于**页码可信**。
3. 每季度扫一次 L5 快照的时效；L1-L4 锚点跟随 AE/书单版本更新（书单更新时核对章号）。

---

## 相关笔记

- [AI Engineering 导读](ai-engineering.md) —— 页码锚点的主要来源
- [机器学习书单与完整阅读计划](ml-booklist.md) —— 理论侧的对应（W5-W7 / W11-W13）
- [Agent 实操线](agent-practice-plan.md) —— L4 层的实操场
- [深入理解 AI Agent](understanding-ai-agent.md) —— AAB 锚点来源
- [MOC - ai](../../notes/MOC%20-%20ai.md) —— 本地图的上游索引

## 更新记录

- **2026-10-16** 初始创建：承接 MOC - ai「待补充」18 项，分 L1-L5 五层；资源锚点仅收录已核验项（书本结构经 PDF 目录提取），4 处未核验点如实标注「待定位」。
