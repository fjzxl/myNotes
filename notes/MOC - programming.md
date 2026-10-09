---
title: 编程 MOC
tags:
  - moc
  - programming
created: 2026-09-09
updated: 2026-10-09
---

# MOC · Programming（编程地图）

> 编程相关笔记的入口。所有编程主题的笔记都从这里跳转。

## 全景

编程笔记按 **语言 / 平台 / 工具** 三个维度组织：
- 语言层：Java / C++ / Python / Go / Rust ...
- 平台层：Web / Android / Linux / 嵌入式 ...
- 工具层：VSCode / Git / Docker / CI/CD ...

> 前端求职线（JS/TS → Vue/React → 作品集）与高数、软考并行的总排程，见 [[projects/note-writing-plan|笔记编撰计划]]。

## 核心笔记

> 必读、最常翻

- [[topics/tools/VSCode]] —— 主编辑器配置与基础
- [[topics/tools/Markdown]] —— 写作工具链
- [[topics/tools/Foam]] —— 知识库管理
- [[topics/tools/marp-guide]] —— Marp 幻灯片（Markdown → PDF/PPT）
- [[topics/tools/marp-screencast-script]] —— Marp 5 分钟录屏脚本

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

- [[topics/programming/Web/css]] —— CSS 入门指南（按学习阶段拆分为 10 篇）
  - [[topics/programming/Web/css/stage-01-getting-started|一·初识 CSS]] · [[topics/programming/Web/css/stage-02-text-styling|二·文字化妆]] · [[topics/programming/Web/css/stage-03-box-model|三·盒模型]] · [[topics/programming/Web/css/stage-04-selectors|四·选择器]] · [[topics/programming/Web/css/stage-05-backgrounds|五·背景装饰]]
  - [[topics/programming/Web/css/stage-06-layout|六·布局系统]] · [[topics/programming/Web/css/stage-07-responsive-design|七·响应式设计]] · [[topics/programming/Web/css/stage-08-animation|八·动画交互]] · [[topics/programming/Web/css/stage-09-modern-css|九·现代特性]] · [[topics/programming/Web/css/stage-10-architecture|十·架构与工程化]]
- [[topics/programming/Web/javascript]] —— JavaScript 语言与运行时基础（按章节拆分为 8 篇）
  - [[topics/programming/Web/javascript/01-language-basics|一·语言基础]] · [[topics/programming/Web/javascript/02-reference-types|二·引用类型]] · [[topics/programming/Web/javascript/03-core-mechanisms|三·核心机制]] · [[topics/programming/Web/javascript/04-asynchronous-programming|四·异步编程]]
  - [[topics/programming/Web/javascript/05-dom-and-browser-api|五·DOM 与浏览器 API]] · [[topics/programming/Web/javascript/06-es6-modern-features|六·ES6+ 特性]] · [[topics/programming/Web/javascript/07-error-handling-and-debugging|七·错误处理]] · [[topics/programming/Web/javascript/08-engineering-and-best-practices|八·工程化与最佳实践]]
- [[topics/programming/Web/es6]] —— ES6+ 语法与平台特性
- [[topics/programming/Web/typescript/intro]] —— TS 入门与工程实践（建议先掌握 JS / ES6+）
- [[topics/programming/Web/typescript/interface]] —— 从 JavaScript 对象约定理解 TypeScript 接口
- [[topics/programming/Web/typescript/type-system]] —— TS 类型系统进阶（结构化类型、型变、条件类型与类型体操）

> **TypeScript 学习路线**：[[topics/programming/Web/javascript]] → [[topics/programming/Web/es6]] → [[topics/programming/Web/typescript/intro]] → [[topics/programming/Web/typescript/interface]] → [[topics/programming/Web/typescript/type-system]]。前两篇讲运行时语言与语法，后三篇依次介绍类型基础、接口契约和类型编程。

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

## 按标签查找

Foam 没有图谱查询语法。按标签筛选用左侧 **Tag Explorer** 面板，或 `Ctrl+Shift+P` → `Foam: Search Tag`；连接与孤立情况在 `Foam: Show Graph` 面板查看。

- `programming` —— 所有编程笔记
- `java` —— Java 专题
- `linux` —— Linux 专题

## 相关 MOC

- [[notes/MOC - ai]] —— AI（含 LLM、Agent）
- [[notes/MOC - math]] —— 数学（含算法基础）
- [[notes/MOC - history]] —— 历史

## 更新记录

- **2026-09-09** —— 初始创建（重构后）
- **2026-09-30** —— 索引维护：核心笔记纳入 [[topics/tools/marp-screencast-script]]；Web 分类新增 TypeScript 类型系统与接口专题，并补充 TS 学习路线
- **2026-10-01** —— 拆分超长教程：javascript（8 章）、css（10 阶段）各拆为总览导航页 + 章节笔记，原文件保留学习路线与术语表；全库主题笔记补齐 frontmatter；新增 `scripts/check_notes.py` 校验脚本
- **2026-10-09** —— 「全景」接入 [[projects/note-writing-plan|笔记编撰计划]]（前端求职线总排程，补全双向导航）
