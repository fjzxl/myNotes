# Markdown配置

## vscode插件

Markdown Preview Enhanced \
Markdown All in One \
Markdownlint \
Local history \
Paste Image \
Marp \
Markmap

## 配置

```json
{
    "markdown.copyFiles.destination": {
        "*.md": "attachments/images/${relativeFileDirname}/${documentBaseName}-${fileName}"
    },
    "[markdown]": {
        "editor.defaultFormatter": "DavidAnson.vscode-markdownlint"
    },

    "markdown-preview-enhanced.codeBlockTheme": "github-dark.css",
    "markdown-preview-enhanced.previewTheme": "one-dark.css",
    "markdown-preview-enhanced.automaticallyShowPreviewOfMarkdownBeingEdited": true,
    "markdown-preview-enhanced.imageFolderPath": "attachments/images",
    "markdownlint.run": "onType",
}
```

> **路径变更说明**：自 2026-09 重构后，所有图片统一存放在 `attachments/images/`（旧路径 `attachments/images/` 已废弃）。

## 语法

```Markdown
# 一级标题

## 二级标题

### 三级标题

每写完一个段落要隔一行空行.

就像这样, 隔了一行空行.

---

分割线

**重点加粗**

*斜体*

~~删除线~~

---

列表:

* 无序列表
  * 嵌套无序列表
  * 嵌套无序列表
* 无序列表
* 无序列表

1. 有序列表 1
   1. 嵌套有序列表 1
   2. 嵌套有序列表 2
2. 有序列表 2
3. 有序列表 3

---

引用文本:

> 引用别人说的话
> 就这样写
> By. OrangeX4

---

这是 `行内代码` 语法.

代码块语法:

''' python
print("Hello, World!")
'''

请将 ' 替换成 `.

---

[超链接名称](链接地址)

![图片提示语](图片地址)

---

表格:

| 表头 | 表头 |
| ---- | ---- |
| 内容 | 内容 |
| 内容 | 内容 |

---

任务列表:

- [x] 已经完成的事 1
- [x] 已经完成的事 2
- [x] 已经完成的事 3
- [ ] 仍未完成的事 4
- [ ] 仍未完成的事 5

---

注释:

<!-- 你看不见我 -->
```

## 链接

* [VS Code 中用 Markdown 做「数字化」学习笔记](https://zhuanlan.zhihu.com/p/366596107)

## 知识管理（Foam 集成）

本目录的所有 Markdown 笔记可以直接作为 **Foam 知识库** 使用：

- 完整文档：[[topics/tools/foam-knowledge-base-guide]]
- 索引入口：[[topics/tools/Foam]]

**为什么 Markdown 工具链与 Foam 强相关**：

- Foam 的图谱、反向链接、wikilink 全部建立在纯 Markdown 之上
- Markdown All in One 的 `Ctrl+Shift+V` 预览才能看到反向链接面板
- Paste Image 配置好的图片存储路径，会被 Foam 自动识别为附件节点

**图片存储新路径**：`attachments/images/`（按主题分子目录）

## 相关链接

- [[topics/tools/VSCode]] —— VS Code 配置与基础
- [[topics/tools/Shortcuts]] —— 顶层工具速查表
- [[topics/tools/Foam]] —— 知识库管理工具索引
- https://zuizhinan.com/markdown/
