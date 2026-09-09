---
title: Code Snippets
tags:
  - attachments
  - code-snippets
---

# 💾 Code Snippets · 代码片段

> **重用代码**的归档位置。从仓库里的 `README.md` 历史描述："Code_Snippet —— 使用过的代码，重要且会重复使用。有必要记录起来。"

## 组织方式

按语言/项目分：

```
code-snippets/
├── cpp/
├── java/
├── python/
├── shell/
├── js/
└── sql/
```

每个片段一个 `.snippet` 或 `.md` 文件，**带说明**（什么时候用、为什么这么写）。

## 建议

- 📌 优先记录"用了一次还会用第二次"的代码
- 🏷 用 Frontmatter 标 `tags: [language, purpose]`
- 📚 Foam wikilink：`[[attachments/code-snippets/xxx]]` 在笔记里直接引用

## 引用示例

```markdown
见 [[attachments/code-snippets/cpp/thread-pool]] 实现的线程池。
```
