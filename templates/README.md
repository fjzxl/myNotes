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

### 方法 3：Foam 完整模板

`Ctrl+Shift+P` → `Foam: Create Note from Template`，从 `templates/` 选择模板；也可直接复制文件并替换 `{{...}}` 字段。

## 读书与技能学习怎么选

- **读完一本书做总结**：[[templates/book-note|book-note]]（`book` + Tab）。
- **读一章、提问题、闭卷回忆**：[[templates/book-chapter|book-chapter]]（`chapter` + Tab）；最后将重要结论汇入整本书笔记。
- **规划一项技能并定义验收标准**：[[templates/skill-learning|skill-learning]]（`skill` + Tab）。
- **记录一次练习、纠错与复测**：[[templates/practice-log|practice-log]]（`practice` + Tab）；结果回链到学习计划。

建议：读书 / 技能的主题知识放 `topics/` 对应主题，限期学习计划放 `projects/`，练习流水放 `journal/`，提炼后的原子概念放 `notes/`。新主题笔记记得加入相关 MOC。

三个新模板均为纯 Markdown，无特殊渲染依赖。空 `[[]]` 是待填写的关联笔记；实际链接使用工作区根相对路径。快捷片段是简版，存于本地被 Git 忽略的 `.vscode/foam.code-snippets`；跨设备可直接用完整模板。

## 模板索引

### 笔记类

- [[templates/daily-note|daily-note]] —— 每日笔记（PARA 1）
- [[templates/cornell-note|cornell-note]] —— **康奈尔笔记**（上课/讲座/读书的 3 区笔记法）
- [[templates/cornell-marp|cornell-marp]] —— **康奈尔 × Marp 混合**（笔记直接转幻灯片）
- [[templates/permanent-note|permanent-note]] —— **Zettelkasten 永久笔记**（核心：原子化、概念化）
- [[templates/literature-note|literature-note]] —— 文献笔记（读书/读文章）
- [[templates/book-note|book-note]] —— **读书笔记**（整本书的完整沉淀）
- [[templates/book-chapter|book-chapter]] —— 章节阅读（问题 / 论证 / 闭卷回忆 / 自测）
- [[templates/practice-log|practice-log]] —— 单次练习（尝试 / 反馈 / 纠错 / 复测）
- [[templates/moc|moc]] —— Map of Content 索引页

### 项目 / 任务类

- [[templates/project|project]] —— 项目笔记（PARA 3）
- [[templates/skill-learning|skill-learning]] —— 技能学习计划（能力拆解 / 练习安排 / 验收）

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
| **book-note** | **读书笔记（整本书：总结/逐章/金句/行动）** | **book-note, topic** |
| book-chapter | 章节阅读与主动回忆 | book-chapter, topic |
| skill-learning | 技能学习计划与能力验收 | skill-learning, topic |
| practice-log | 单次练习、纠错与复测 | practice-log, topic |
| moc | 主题索引 | moc, topic |
| project | 项目跟踪 | project |
| code-snippet | 重用代码 | code-snippet, language |

## 模板设计原则

1. **Frontmatter 必备**：tags + 关键元数据（date, source, status 等）
2. **明确"是什么"**：开篇 1-2 句话说清模板用途
3. **占位符用 `{{}}`**：方便搜索替换
4. **附"写作守则"**：每张模板末尾给使用提示
