---
title: Tools
tags:
  - tools
  - readme
created: 2026-10-11
updated: 2026-10-11
---

# 🧰 Tools · 工具笔记

> 编辑器、写作工具链与演示导出相关笔记。工具笔记服务于**其他主题**（编程 / AI / 数学 / 考试 / 语言），本身不构成知识主题。

## 索引

- [Shortcuts](Shortcuts.md) —— 顶层工具速查表（VS Code 快捷键、Markdown 工具）**← 入口**
- [VSCode](VSCode.md) —— VS Code 配置、常用快捷键与插件清单
- [Markdown](Markdown.md) —— Markdown 写作环境（Foam 强依赖的工具链）
- [Foam](Foam.md) —— Foam 知识库工具索引
- [foam-knowledge-base-guide](foam-knowledge-base-guide.md) —— Foam 完整使用指南（按 foam-vscode 0.46.0 核对命令名与设置项）
- [marp-guide](marp-guide.md) —— Marp 完整使用指南（Markdown → PDF / PPT / HTML）
- [marp-screencast-script](marp-screencast-script.md) —— Marp 5 分钟录屏脚本

## 配置位置

| 文件 | 作用 | 是否入 Git |
|------|------|-----------|
| `.vscode/settings.json` | 工作区设置（编码 / 行尾 / 终端 / Foam 模板目录） | ❌ 含机器相关的解释器路径 |
| `.vscode/foam.code-snippets` | 笔记模板快捷片段（`daily` / `perm` / `wl` 等 + Tab） | ✅ 已跟踪（2026-10-12 起入 Git，跨设备克隆可得） |
| `.vscode/extensions.json` | 推荐扩展列表 | ✅ 已跟踪 |

> 快捷片段跨设备可用；完整模板在 `templates/`，用 `Ctrl+Shift+P` → `Foam: Create New Note From Template` 调起。

## 相关

- [MOC - programming](../../notes/MOC%20-%20programming.md) —— 编程知识地图
- [README](../../README.md) —— 仓库结构总览
