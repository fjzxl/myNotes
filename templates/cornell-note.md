---
title: "康奈尔笔记：{{topic}}"
tags:
  - cornell-note
  - {{topic}}
source: "{{source}}"
date: {{date}}
---

# 康奈尔笔记：{{topic}}

> **康奈尔笔记法**（Cornell Notes）—— 经典的两栏版式：左线索 / 右笔记 / 底总结。
> 模板位置：`templates/cornell-note.md`
> 适用：上课笔记、读书笔记、听讲座笔记
>
> **📌 渲染要求**：本文档使用 **HTML + 内联 CSS** 实现真正的两栏版式。
> 推荐用 **Markdown Preview Enhanced** 预览（VS Code 已推荐），效果最佳。
> 导出 PDF 用 **Marp** 插件（见 `README.md` 配置说明）。

## 元信息

| 字段 | 内容 |
|------|------|
| **课程/主题** | {{topic}} |
| **日期** | {{date}} |
| **来源** | {{source}}（书 / 视频 / 课 / 文章） |
| **章节/页码** |  |

---

<!-- Cornell 笔记核心区：HTML + CSS 两栏版式 -->
<style>
  .cornell-page {
    display: grid;
    grid-template-columns: 30% 70%;
    gap: 1.2rem;
    border: 1px solid #ccc;
    border-radius: 6px;
    padding: 1rem;
    margin: 1.5rem 0;
    background: rgba(127,127,127,0.03);
  }
  .cornell-cues {
    border-right: 2px solid #888;
    padding-right: 0.8rem;
  }
  .cornell-cues h3 { margin-top: 0; color: #d97706; }
  .cornell-notes {
    padding-left: 0.8rem;
  }
  .cornell-notes h3 { margin-top: 0; color: #2563eb; }
  .cornell-cues ul, .cornell-notes ul { margin: 0.3em 0; padding-left: 1.2em; }
  .cornell-cues li, .cornell-notes li { margin: 0.2em 0; }
  .cornell-summary {
    border: 1px solid #ccc;
    border-radius: 6px;
    padding: 0.8rem 1rem;
    margin: 1rem 0;
    background: rgba(34,197,94,0.05);
  }
  .cornell-summary h3 { margin-top: 0; color: #16a34a; }
  @media print {
    .cornell-page, .cornell-summary { page-break-inside: avoid; }
  }
</style>

<div class="cornell-page">

<div class="cornell-cues">

### 🔑 线索（Cues）

<!-- 课后补：关键词、问题、定义、对比 -->
- **概念 1**
- **概念 2**
- **问题：** 自问自答
- **定义：** ...
- **对比：** ...
- **疑问：** ...

</div>

<div class="cornell-notes">

### 📝 笔记（Notes）

<!-- 当场记：详细内容、公式、例子 -->

- 要点 1：详细展开
- 要点 2：详细展开
  - 子要点
  - 子要点
- 公式：`f(x) = ...`
- 例题：

  ```
  题目描述...
  解答...
  ```

- **关键引文**：> 原文 + 上下文
- **临时缩写**：符号约定

</div>

</div>

---

<div class="cornell-summary">

### 📋 总结（Summary）

> **24 小时内必填** —— 2-3 句话回答："这页讲了什么？我学到了什么？"

- **整页核心**：
- **学到的关键概念**：
- **还需深入的点**：

</div>

---

## 复盘（事后填）

### 24 小时内

- [ ] 整理线索栏（用关键词代替冗长句子）
- [ ] 写下总结
- [ ] 提出 3 个问题写在反向链接里

### 1 周内

- [ ] 复习一遍笔记
- [ ] 补充新理解
- [ ] 用 `[[wikilink]]` 链接到相关永久笔记

### 1 月内

- [ ] 转化为永久笔记（用 `perm` + Tab 模板）
- [ ] 归档或丢弃

## 相关笔记

- 永久笔记：[[]]
- 文献笔记：[[]]
- 项目笔记：[[]]

---

> 📌 **康奈尔笔记法要点**：
> 1. **先记右，再补左**：课堂或读书时**只**写笔记栏；线索栏课后整理时再补
> 2. **线索用词组不用句子**：每个线索 ≤ 5 个字
> 3. **总结 24h 内必写**：这是"提炼"的关键步骤
> 4. **3 次复盘节奏**：24h → 1w → 1m，配合 Zettelkasten 转化为永久笔记
> 5. **避免抄书**：用自己的话重述，理解 > 复制
>
> 💡 **导出选项**：
> - **PDF**：`Ctrl+Shift+P` → `Markdown Preview Enhanced: Open Preview` → 右上角 `⋯` → `Chrome (Puppeteer) PDF`
> - **HTML**：MPE 预览 → 右上角 `⋯` → `HTML`
> - **幻灯片**：Marp 插件（见 README）
