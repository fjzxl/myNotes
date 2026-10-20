---
title: PDFs
tags:
  - attachments
  - pdfs
---

# 📄 PDFs · PDF 文件

> 重要 PDF 文档的存放位置（电子书、论文、报告等）。附件总约定见仓库 [README](../../README.md)（目录结构）与 [AGENTS](../../AGENTS.md)（大体积 PDF 的 gitignore 规则）。

## 组织方式

本目录目前为空。按仓库约定（见 `AGENTS.md` 附件约定）分两类处理：

- **大体积教材 / 手册 PDF**：就地放在主题笔记旁并 gitignore（如 `topics/languages/japanese/*.pdf`、`topics/ai/*.pdf`）
- **小型通用 PDF**：放本目录，按主题分子目录：

```
pdfs/
├── programming/
├── ai/
├── math/
└── general/
```

## 引用

```markdown
详见 [effective-cpp.pdf](../attachments/pdfs/programming/effective-cpp.pdf)
```

或在 Markdown 里嵌入：

```markdown
<iframe src="../../../attachments/pdfs/..." ></iframe>
```

## 工具

- VS Code 装 `vscode-pdf` 扩展可直接打开
- Foam 也会把 PDF 当作节点显示在图谱里
