---
title: Journal
tags:
  - journal
  - daily-notes
---

# 📔 Journal · 笔记日志

> 每日笔记、复盘、随笔。**日期即文件名**（如 `2026-09-09.md`），按时间顺序。

## 结构

- **`daily/`** —— 每日笔记主目录（按 `YYYY-MM-DD.md` 命名）
  - 用 Foam 扩展的 `Foam: Open Daily Note` 命令自动创建
  - 或者手动在 `daily/` 下新建

## 模板

参见 [[templates/daily-note]] 模板。

## 工具配合

```powershell
# VS Code 命令面板
Ctrl+Shift+P → "Foam: Open Daily Note"
```

或手动：
```
journal/daily/2026-09-09.md
```

## 复盘节奏

- 🌅 **每日** —— 写今日笔记
- 📅 **每周日** —— 翻这一周，写周复盘到 `journal/weekly/`
- 📆 **每月末** —— 翻这月，写月复盘到 `journal/monthly/`
- 📈 **每季度** —— 翻这季度，整理到 `topics/` 或 `notes/`
