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
        "*.md": "Source/pics/${relativeFileDirname}/${documentBaseName}-${fileName}"
    },
    "[markdown]": {
        "editor.defaultFormatter": "DavidAnson.vscode-markdownlint"
    },
   
    "markdown-preview-enhanced.codeBlockTheme": "github-dark.css",
    "markdown-preview-enhanced.previewTheme": "one-dark.css",
    "markdown-preview-enhanced.automaticallyShowPreviewOfMarkdownBeingEdited": true,
    "markdown-preview-enhanced.imageFolderPath": "Source/pics",
    "markdownlint.run": "onType",
}
```

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