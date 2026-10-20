---
title: 编程 MOC
tags:
  - moc
  - programming
created: 2026-09-09
updated: 2026-10-11
---

# MOC · Programming（编程地图）

> 编程相关笔记的入口。所有编程主题的笔记都从这里跳转。

## 全景

编程笔记按 **语言 / 平台 / 工具** 三个维度组织：
- 语言层：Java / C++ / Python / Go / Rust ...
- 平台层：Web / Android / Linux / 嵌入式 ...
- 工具层：VSCode / Git / Docker / CI/CD ...

> 前端求职线（JS/TS → Vue/React → 作品集）与高数、软考并行的总排程，见 [笔记编撰计划](../projects/note-writing-plan.md)。

## 核心笔记

> 必读、最常翻

- [VSCode](../topics/tools/VSCode.md) —— 主编辑器配置与基础
- [Markdown](../topics/tools/Markdown.md) —— 写作工具链
- [Foam](../topics/tools/Foam.md) —— 知识库管理
- [marp-guide](../topics/tools/marp-guide.md) —— Marp 幻灯片（Markdown → PDF/PPT）
- [marp-screencast-script](../topics/tools/marp-screencast-script.md) —— Marp 5 分钟录屏脚本
- [Shortcuts](../topics/tools/Shortcuts.md) —— 顶层工具速查表（VS Code 快捷键、Markdown 工具）
- [foam-knowledge-base-guide](../topics/tools/foam-knowledge-base-guide.md) —— Foam 完整使用指南（按 foam-vscode 0.46.0 核对）

## 按语言分类

### Java

- [Servlet](../topics/programming/Java/Servlet.md)
- [vscode_Java_dev](../topics/programming/Java/vscode_Java_dev.md)
- [vscode_Java_remote_dev](../topics/programming/Java/vscode_Java_remote_dev.md)
- [spring_intro](../topics/programming/Java/spring/spring_intro.md)
- [spring_lifecycle](../topics/programming/Java/spring/spring_lifecycle.md)

> 📊 **Marp 幻灯片示例**（Java 实战）：[Servlet-lifecycle](../topics/programming/Java/slides/Servlet-lifecycle.md)

### C++

- [into](../topics/programming/cplusplus/into.md) —— C 入门：从源码到可执行文件（编译四阶段、gcc、make）
- [vscodec](../topics/programming/cplusplus/vscodec.md) —— VS Code C/C++ 环境配置（扩展、构建与调试）

### Web（前端三件套 + TypeScript）

- [html](../topics/programming/Web/html.md) —— HTML 基础（文档结构、语义化、表单、无障碍）
- [css](../topics/programming/Web/css.md) —— CSS 入门指南（按学习阶段拆分为 10 篇）
  - [一·初识 CSS](../topics/programming/Web/css/stage-01-getting-started.md) · [二·文字化妆](../topics/programming/Web/css/stage-02-text-styling.md) · [三·盒模型](../topics/programming/Web/css/stage-03-box-model.md) · [四·选择器](../topics/programming/Web/css/stage-04-selectors.md) · [五·背景装饰](../topics/programming/Web/css/stage-05-backgrounds.md)
  - [六·布局系统](../topics/programming/Web/css/stage-06-layout.md) · [七·响应式设计](../topics/programming/Web/css/stage-07-responsive-design.md) · [八·动画交互](../topics/programming/Web/css/stage-08-animation.md) · [九·现代特性](../topics/programming/Web/css/stage-09-modern-css.md) · [十·架构与工程化](../topics/programming/Web/css/stage-10-architecture.md)
- [javascript](../topics/programming/Web/javascript.md) —— JavaScript 语言与运行时基础（按章节拆分为 8 篇）
  - [一·语言基础](../topics/programming/Web/javascript/01-language-basics.md) · [二·引用类型](../topics/programming/Web/javascript/02-reference-types.md) · [三·核心机制](../topics/programming/Web/javascript/03-core-mechanisms.md) · [四·异步编程](../topics/programming/Web/javascript/04-asynchronous-programming.md)
  - [五·DOM 与浏览器 API](../topics/programming/Web/javascript/05-dom-and-browser-api.md) · [六·ES6+ 特性](../topics/programming/Web/javascript/06-es6-modern-features.md) · [七·错误处理](../topics/programming/Web/javascript/07-error-handling-and-debugging.md) · [八·工程化与最佳实践](../topics/programming/Web/javascript/08-engineering-and-best-practices.md)
- [es6](../topics/programming/Web/es6.md) —— ES6+ 语法与平台特性（专题手册；JS 教程第 6 章为导读，二者已互相交叉引用）
- [intro](../topics/programming/Web/typescript/intro.md) —— TS 入门与工程实践（建议先掌握 JS / ES6+）
- [interface](../topics/programming/Web/typescript/interface.md) —— 从 JavaScript 对象约定理解 TypeScript 接口
- [type-system](../topics/programming/Web/typescript/type-system.md) —— TS 类型系统进阶（结构化类型、型变、条件类型与类型体操）

> **前端三件套路线**：[html](../topics/programming/Web/html.md)（结构）→ [css](../topics/programming/Web/css.md)（表现）→ [javascript](../topics/programming/Web/javascript.md)（行为）。
> **TypeScript 学习路线**：[javascript](../topics/programming/Web/javascript.md) → [es6](../topics/programming/Web/es6.md) → [intro](../topics/programming/Web/typescript/intro.md) → [interface](../topics/programming/Web/typescript/interface.md) → [type-system](../topics/programming/Web/typescript/type-system.md)。前两篇讲运行时语言与语法，后三篇依次介绍类型基础、接口契约和类型编程。

## 按平台分类

### 移动端

- [Android_into](../topics/programming/Android/Android_into.md) —— Android 入门（平台架构、四大组件、开发环境与第一个项目）

### 基础设施

- [linux-kernel-4.9-build](../topics/programming/Linux/linux-kernel-4.9-build.md)
- [calico-iptables-stale-rules](../topics/programming/Linux/calico-iptables-stale-rules.md) —— Calico 残留 iptables 规则排查与修复（k8s 重启后网络不通）
- [ubuntu_mysql_install](../topics/programming/MySQL/ubuntu_mysql_install.md)

## 按主题深度

### 配置 / 工具

- [linux-kernel-4.9-build](../topics/programming/Linux/linux-kernel-4.9-build.md) —— Linux 4.9 内核编译实战
- [calico-iptables-stale-rules](../topics/programming/Linux/calico-iptables-stale-rules.md) —— iptables / Calico 实战案例

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

- `programming` —— 所有编程笔记（学科伞形，Tag Explorer 树的根）
- `programming/web/javascript` / `programming/web/css` / `programming/web/typescript` —— 前端三件套
- `programming/java` —— Java 专题
- `programming/linux`（含 `programming/linux/kernel`）—— Linux 专题

## 相关 MOC

- [MOC - ai](MOC%20-%20ai.md) —— AI（含 LLM、Agent）
- [MOC - math](MOC%20-%20math.md) —— 数学（含算法基础）
- [MOC - history](MOC%20-%20history.md) —— 历史

## 更新记录

- **2026-09-09** —— 初始创建（重构后）
- **2026-09-30** —— 索引维护：核心笔记纳入 [marp-screencast-script](../topics/tools/marp-screencast-script.md)；Web 分类新增 TypeScript 类型系统与接口专题，并补充 TS 学习路线
- **2026-10-01** —— 拆分超长教程：javascript（8 章）、css（10 阶段）各拆为总览导航页 + 章节笔记，原文件保留学习路线与术语表；全库主题笔记补齐 frontmatter；新增 `scripts/check_notes.py` 校验脚本
- **2026-10-09** —— 「全景」接入 [笔记编撰计划](../projects/note-writing-plan.md)（前端求职线总排程，补全双向导航）
- **2026-10-10** —— Web 分类新增 [HTML 基础](../topics/programming/Web/html.md)（补齐三件套，新增前端三件套路线）；es6 与 JS 教程第 6 章互加交叉引用明确分工；C++（[C 入门](../topics/programming/cplusplus/into.md)、[VS Code C/C++](../topics/programming/cplusplus/vscodec.md)）与 [Android 入门](../topics/programming/Android/Android_into.md) 由空壳扩充为完整笔记
- **2026-10-11** —— 「核心笔记」补齐工具类归属：新增 [Shortcuts](../topics/tools/Shortcuts.md) 与 [foam-knowledge-base-guide](../topics/tools/foam-knowledge-base-guide.md)（此前 7 篇工具笔记 5 篇有索引、2 篇遗漏）
