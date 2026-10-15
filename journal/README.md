---
title: Journal
tags:
  - journal
  - daily-notes
---

# 📔 Journal · 笔记日志

> 每日笔记、随笔。**日期即文件名**（如 `2026-10-12.md`），按时间顺序。

## 结构

- **`daily/`** —— 每日笔记主目录（按 `YYYY-MM-DD.md` 命名）
  - 用 Foam 扩展的 `Foam: Open Today's Note` 命令（默认快捷键 `Alt+D`）自动创建
  - 或者手动在 `daily/` 下新建
- **`weekly/`** —— 周复盘（每周日写当日计划的周复盘，如五十音冲刺的 10-18、10-25；目录暂未创建，首次写入时新建）

## 模板

参见 [daily-note](../templates/daily-note.md) 模板。

## 工具配合

```powershell
# VS Code 命令面板
Ctrl+Shift+P → "Foam: Open Today's Note"
```

或手动：
```
journal/daily/2026-10-12.md
```

## 复盘节奏

- 🌅 **每日** —— 写今日笔记
- 📅 **每周日** —— 写周复盘到 `weekly/`（与五十音等冲刺计划的周复盘联动）
- 📈 **每季度** —— 翻这季度，整理到 `topics/` 或 `notes/`
