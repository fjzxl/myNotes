---
title: Templates
tags:
  - templates
---

# 📋 Templates · 笔记模板

> 复用的笔记模板，统一管理。

## 使用方法

### 方法 1：直接复制

```powershell
# 复制到目标位置
Copy-Item templates\daily-note.md journal\daily\2026-09-09.md
```

### 方法 2：VS Code 片段（推荐）

`.vscode/foam.code-snippets` 里配置后，键入 `daily` → Tab 自动展开。

详见 [[topics/tools/Foam]]。

## 模板索引

### 笔记类

- [[templates/daily-note|daily-note]] —— 每日笔记（PARA 1）
- [[templates/cornell-note|cornell-note]] —— **康奈尔笔记**（上课/讲座/读书的 3 区笔记法）
- [[templates/permanent-note|permanent-note]] —— **Zettelkasten 永久笔记**（核心：原子化、概念化）
- [[templates/literature-note|literature-note]] —— 文献笔记（读书/读文章）
- [[templates/moc|moc]] —— Map of Content 索引页

### 项目 / 任务类

- [[templates/project|project]] —— 项目笔记（PARA 3）

### 附件类

- [[templates/code-snippet|code-snippet]] —— 代码片段（存档到 `attachments/code-snippets/`）

## 完整清单

| 模板 | 用途 | 关键 tag |
|------|------|----------|
| daily-note | 每天 | daily-note |
| **cornell-note** | **康奈尔笔记（3 区：线索/笔记/总结）** | **cornell-note, topic** |
| **cornell-marp** | **康奈尔 × Marp 混合（笔记转幻灯片）** | **marp, cornell-note** |
| permanent-note | 概念原子笔记 | permanent-note, topic |
| literature-note | 读书笔记 | literature-note, topic |
| moc | 主题索引 | moc, topic |
| project | 项目跟踪 | project |
| code-snippet | 重用代码 | code-snippet, language |

## 模板设计原则

1. **Frontmatter 必备**：tags + 关键元数据（date, source, status 等）
2. **明确"是什么"**：开篇 1-2 句话说清模板用途
3. **占位符用 `{{}}`**：方便搜索替换
4. **附"写作守则"**：每张模板末尾给使用提示
