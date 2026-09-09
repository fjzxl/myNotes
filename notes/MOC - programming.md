---
title: 编程 MOC
tags:
  - moc
  - programming
created: 2026-09-09
updated: 2026-09-09
---

# MOC · Programming（编程地图）

> 编程相关笔记的入口。所有编程主题的笔记都从这里跳转。

## 全景

编程笔记按 **语言 / 平台 / 工具** 三个维度组织：
- 语言层：Java / C++ / Python / Go / Rust ...
- 平台层：Web / Android / Linux / 嵌入式 ...
- 工具层：VSCode / Git / Docker / CI/CD ...

## 核心笔记

> 必读、最常翻

- [[topics/tools/VSCode]] —— 主编辑器配置与基础
- [[topics/tools/Markdown]] —— 写作工具链
- [[topics/tools/Foam]] —— 知识库管理
- [[topics/tools/marp-guide]] —— Marp 幻灯片（Markdown → PDF/PPT）

## 按语言分类

### Java

- [[topics/programming/Java/Servlet]]
- [[topics/programming/Java/vscode_Java_dev]]
- [[topics/programming/Java/vscode_Java_remote_dev]]
- [[topics/programming/Java/spring/spring_intro]]
- [[topics/programming/Java/spring/spring_lifecycle]]

> 📊 **Marp 幻灯片示例**（Java 实战）：[[topics/programming/Java/slides/Servlet-lifecycle]]

### C++

- [[topics/programming/cplusplus/into]]
- [[topics/programming/cplusplus/vscodec]]

### Web（前端三件套 + TypeScript）

- [[topics/programming/Web/css]]
- [[topics/programming/Web/es6]]
- [[topics/programming/Web/javascript]]
- [[topics/programming/Web/typescript/intro]]

## 按平台分类

### 移动端

- [[topics/programming/Android/Android_into]]

### 基础设施

- [[topics/programming/Linux/linux-kernel-4.9-build]]
- [[topics/programming/MySQL/ubuntu_mysql_install]]

## 按主题深度

### 配置 / 工具

- [[topics/programming/Linux/linux-kernel-4.9-build]] —— Linux 4.9 内核编译实战

## 待补充

- [ ] Python 学习笔记
- [ ] Go 学习笔记
- [ ] Rust 学习笔记
- [ ] 算法与数据结构
- [ ] 设计模式
- [ ] 架构设计
- [ ] 数据库进阶（索引、事务、锁）
- [ ] 操作系统（进程、线程、内存）
- [ ] 计算机网络（TCP/IP、HTTPS）
- [ ] Git 进阶（rebase、cherry-pick、submodule）

## Foam 图谱查询

> 在 Foam 图谱面板（`Ctrl+Shift+P` → `Foam: Open Graph`）里用：

```
tag:programming                       # 所有编程笔记
tag:programming AND tag:java          # Java 专题
tag:programming AND tag:linux         # Linux 专题
tag:programming AND -ORPHANS:false    # 已连接（不是孤立节点）的编程笔记
```

## 相关 MOC

- [[notes/MOC - ai]] —— AI（含 LLM、Agent）
- [[notes/MOC - math]] —— 数学（含算法基础）
- [[notes/MOC - history]] —— 历史

## 更新记录

- **2026-09-09** —— 初始创建（重构后）
