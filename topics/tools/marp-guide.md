---
title: Marp 使用指南
tags:
  - marp
  - slides
  - presentation
  - markdown
  - tools
aliases:
  - Marp Guide
  - Marp 幻灯片
---

# Marp 使用指南：Markdown 写 PPT

> 一份面向 VS Code 用户的 Marp 完整手册。读完你就能用纯 Markdown 写出漂亮的演示文稿，并一键导出 PDF / HTML / PPTX。

---

## 目录

1. [什么是 Marp](#1-什么是-marp)
2. [与同类工具对比](#2-与同类工具对比)
3. [安装](#3-安装)
4. [基本语法](#4-基本语法)
5. [Frontmatter 配置](#5-frontmatter-配置)
6. [主题与样式](#6-主题与样式)
7. [实战示例](#7-实战示例)
8. [导出](#8-导出)
9. [进阶技巧](#9-进阶技巧)
10. [常见问题](#10-常见问题)

---

## 1. 什么是 Marp

**Marp**（Markdown Presentation Ecosystem）是一套**用 Markdown 写幻灯片**的工具链。核心思想：

- **Markdown 是源文件**：所有内容是纯 `.md`，不是专有格式
- **可编程**：主题用 CSS 写，逻辑用指令（Directives）控制
- **多端输出**：一份源文件 → PDF / HTML / PPTX
- **可版本控制**：因为是文本，可用 Git 管理

一句话总结：**Marp = Markdown + Reveal.js + 极简主题系统**。

---

## 2. 与同类工具对比

| 工具 | 源格式 | 学习成本 | 美观度 | 代码高亮 | 数学公式 |
|------|--------|---------|--------|---------|---------|
| **PowerPoint** | 二进制 | 中 | ⭐⭐⭐⭐⭐ | 需手动 | 需手动 |
| **Keynote** | 二进制 | 中 | ⭐⭐⭐⭐⭐ | 需手动 | 需手动 |
| **Reveal.js** | HTML | 高 | ⭐⭐⭐⭐ | ✅ | ✅ |
| **Slidev** | Markdown | 中 | ⭐⭐⭐⭐ | ✅ | ✅ |
| **Marp** | Markdown | **低** | ⭐⭐⭐⭐ | ✅ | ✅（KaTeX） |

**结论**：
- 想要**最简单**：Marp（5 分钟上手）
- 想要**最花哨**：Reveal.js / Slidev
- 想要**Office 兼容**：导出 PPTX 给老板/老师

---

## 3. 安装

### 3.1 VS Code 扩展（推荐，已经在推荐列表）

工作区打开时会提示安装 `marp-team.marp-vscode`，或手动：

1. `Ctrl+Shift+X` → 搜 `Marp` → 安装
2. 打开任意 `.md` 文件
3. 点击右上角 🎁 **Marp 图标** 打开预览
4. 预览界面 **⚙️ 齿轮** → `Export Slide Deck` 导 PDF/PPTX/HTML

### 3.2 命令行工具（适合批量 / 自动化）

```powershell
# 用 npm 全局安装
npm install -g @marp-team/marp-cli

# 验证
marp --version
```

### 3.3 进阶：自定义主题

把 CSS 文件放在 `.vscode/` 或项目根目录，在 Frontmatter 里引用。

---

## 4. 基本语法

### 4.1 三横线分页（最基础）

```markdown
# 第一张幻灯片

内容

---

# 第二张幻灯片

内容
```

`---` 单独成行表示**换页**。

### 4.2 标准 Frontmatter

```markdown
---
marp: true          # 启用 Marp 模式
theme: default      # 主题：default / gaia / uncover
paginate: true      # 显示页码
title: 我的演讲
author: MiniMax151938
---
```

> ⚠️ **必须** 在文件**最顶部**用三横线包起来，且**第一行**就是 `marp: true`。

### 4.3 常用 Markdown 语法

幻灯片里支持所有标准 Markdown：

```markdown
# 标题（最大）

## 二级标题

正文段落

- 无序列表
- 无序列表

1. 有序列表
2. 有序列表

**加粗** *斜体* `代码`

[链接文本](https://example.com)

![图片](图片路径)

| 表头 | 表头 |
|------|------|
| 内容 | 内容 |
```

### 4.4 代码高亮

````markdown
```python
def hello():
    print("Hello, Marp!")
```
````

支持的语言和 VS Code 一致。

### 4.5 数学公式（KaTeX）

```markdown
行内：$E = mc^2$

块级：
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 4.6 背景图 / 背景色

```markdown
<!-- _backgroundColor: #123456 -->
<!-- _color: white -->

# 反色幻灯片
```

`_backgroundColor` / `_color` 用 `<!-- -->` HTML 注释写在每张幻灯片**最顶部**。

---

## 5. Frontmatter 配置

### 5.1 核心配置

```yaml
---
marp: true                # 必填，启用 Marp
theme: default            # 主题
paginate: true            # 显示页码
size: 16:9                # 比例：4:3 / 16:9 / 16:10
backgroundColor: #fff     # 默认背景
color: #333               # 默认文字色
header: '顶部文字'         # 顶部
footer: '底部文字'         # 底部
---
```

### 5.2 常用指令（Directives）

| 指令 | 作用 | 示例 |
|------|------|------|
| `theme` | 全局主题 | `theme: gaia` |
| `paginate` | 显示页码 | `paginate: true` |
| `size` | 比例 | `size: 16:9` |
| `header` / `footer` | 顶部/底部 | `header: 'My Talk'` |
| `title` | 演讲标题 | `title: 算法导论` |
| `author` | 作者 | `author: MiniMax151938` |
| `math: katex` | 数学公式 | `math: katex` |
| `style: \|` | 内联 CSS | 见下 |

### 5.3 单张幻灯片局部指令

```markdown
---
marp: true
theme: default
---

# 普通页

---

<!-- _class: lead -->

# 居中大标题（lead 风格）

---

<!-- _backgroundColor: black -->
<!-- _color: white -->

# 黑底白字

---

<!-- _paginate: false -->

# 这页不显示页码
```

---

## 6. 主题与样式

### 6.1 内置主题

| 主题 | 风格 | 适合 |
|------|------|------|
| `default` | 简洁白底 | 通用 |
| `gaia` | 深色蓝调 | 演讲 |
| `uncover` | 学术风 | 教学 |

切换主题：Frontmatter 里改 `theme: gaia`。

### 6.2 自定义主题

创建 `theme.css`：

```css
/* @theme my-theme */

section {
  background: #1a1a2e;
  color: #e0e0e0;
  font-family: 'JetBrains Mono', monospace;
}

h1 {
  color: #ff6b9d;
  text-align: center;
  font-size: 2.5em;
}

section.lead h1 {
  font-size: 3em;
}
```

引用：

```yaml
---
marp: true
theme: my-theme
themeStyle: |
  @import url('theme.css');
---
```

或者用 `style:` 直接写：

```yaml
---
marp: true
style: |
  section {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
  }
---
```

### 6.3 常用样式片段

**渐变背景**：
```css
section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

**分栏布局（用 grid）**：
```css
section.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}
```

**标题居中**：
```css
h1 {
  text-align: center;
}
```

---

## 7. 实战示例

### 示例 1：算法讲解（3 页）

```markdown
---
marp: true
theme: gaia
paginate: true
title: 二分查找
---

# 二分查找
## Binary Search

MiniMax151938 · 2026-09-09

---

## 问题

> 在**有序数组**中查找目标值

- 输入：`[1, 3, 5, 7, 9]`，target = 5
- 输出：2（索引）

时间复杂度：**O(log n)**

---

## 代码

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

<!-- 
提示：实际写时 ``` 不要有前导空格
-->
```

### 示例 2：考研数学复习

```markdown
---
marp: true
theme: default
paginate: true
math: katex
---

# 极限的定义

## $\epsilon$-$\delta$ 语言

---

## 定义

> $\displaystyle \lim_{x \to a} f(x) = L$ 成立
> 当且仅当：**$\forall \epsilon > 0$，$\exists \delta > 0$**
> 使得 $|x - a| < \delta$ 时 $|f(x) - L| < \epsilon$

---

## 直觉

- $\epsilon$：**精度要求**（你希望多接近 $L$）
- $\delta$：**响应精度**（需要多接近 $a$）
- 逻辑：**先给定精度，再给响应**

---

## 证明 $\lim_{x \to 2} (3x + 1) = 7$

**证**：对任意 $\epsilon > 0$，取 $\delta = \epsilon / 3$

当 $|x - 2| < \delta$ 时：
$$|3x + 1 - 7| = 3|x - 2| < 3 \cdot \frac{\epsilon}{3} = \epsilon$$

故原极限成立。$\blacksquare$
```

### 示例 3：康奈尔笔记版

如果用 [[cornell-note]] 模板，可以用 `<!-- _class: ... -->` 模拟两栏：

```markdown
---
marp: true
theme: default
size: 16:9
style: |
  section {
    display: grid;
    grid-template-columns: 30% 70%;
    gap: 1rem;
    text-align: left;
  }
  section.cornell-summary {
    display: block;
  }
---

<!-- _class: cornell-cues -->

## 🔑 线索
- 概念 1
- 问题
- 定义

<!-- _class: cornell-notes -->

## 📝 笔记

详细内容...

<!-- _class: cornell-summary -->

## 📋 总结

核心内容
```

### 示例 4：带图片 / 背景

```markdown
---
marp: true
theme: gaia
---

# 章节封面

![bg left:40%](cover.jpg)

## 副标题

作者：xxx
```

`![bg]` 是 Marp 的"背景图"语法，左/右/覆盖都可以。

---

## 8. 导出

### 8.1 VS Code 扩展导出（最简单）

1. 打开 `.md` 文件
2. 点击右上角 ⚙️ → `Export Slide Deck`
3. 选择格式：
   - **PDF** （推荐）
   - **HTML** （可交互）
   - **PPTX** （PowerPoint 兼容）
   - **PNG / JPEG** （单页图片）
4. 选择保存路径

### 8.2 命令行导出

```powershell
# 基础导出
marp my-talk.md --pdf
marp my-talk.md --html
marp my-talk.md --pptx

# 指定输出文件
marp my-talk.md -o my-talk.pdf

# 自定义主题
marp my-talk.md --theme my-theme.css --pdf

# 监视模式（文件变化自动重新导出）
marp my-talk.md --watch --pdf

# 允许本地 HTML 资源（图片等）
marp my-talk.md --pdf --allow-local-files
```

### 8.3 批量导出整个目录

```powershell
# 找到所有 .md（带 marp: true）并导出
Get-ChildItem -Recurse -Filter *.md | ForEach-Object {
  $c = Get-Content $_.FullName -TotalCount 5
  if ($c -match 'marp: true') {
    marp $_.FullName --pdf --allow-local-files
  }
}
```

---

## 9. 进阶技巧

### 9.1 用 `_class` 自定义单页

```markdown
<!-- _class: title-page -->

# 我的演讲

## 副标题
```

在 CSS 里：

```css
section.title-page {
  text-align: center;
  background: #000;
  color: #fff;
}
section.title-page h1 {
  font-size: 3em;
  margin-top: 30%;
}
```

### 9.2 演讲者备注（Speaker Notes）

```markdown
---
marp: true
---

# 第一页

<!--
这是给演讲者看的备注，幻灯片上不显示。
记得强调：先给定 ε，再构造 δ。
-->
```

### 9.3 嵌入 HTML（高级）

```markdown
<div style="display: flex; align-items: center; gap: 1rem;">
  <div style="flex: 1;">左栏内容</div>
  <div style="flex: 1;">右栏内容</div>
</div>
```

### 9.4 片段动画（Fragments）

Marp 不原生支持动画，但可以用 Marp Core 的 `_class` + CSS 模拟：

```yaml
---
marp: true
style: |
  section ul li {
    opacity: 0.3;
  }
  section.active ul li {
    opacity: 1;
  }
---
```

配合键盘翻页效果不完美但可用。

### 9.5 嵌入 Mermaid 图

需要 Mermaid 插件（不是 Marp 内置）：

```markdown
<mermaid>
graph LR
  A[用户] --> B[API]
  B --> C[数据库]
</mermaid>
```

Marp 配合 `markdown-it-mermaid` 插件可用。

---

## 10. 常见问题

### Q1：VS Code 预览不显示 Marp？

检查：
- 文件**第一行**是 `---`，里面包含 `marp: true`
- VS Code 装了 `marp-team.marp-vscode` 扩展
- 右上角 🎁 Marp 图标点击了
- 重启 VS Code

### Q2：导出的 PDF 中文乱码？

原因：字体不支持中文。解决：

```yaml
---
marp: true
style: |
  section {
    font-family: 'Microsoft YaHei', 'PingFang SC', sans-serif;
  }
---
```

### Q3：图片显示不出来？

- **相对路径**：图片放项目内，用相对路径
- **导 PDF 时**加 `--allow-local-files`

```powershell
marp my-talk.md --pdf --allow-local-files
```

### Q4：数学公式不渲染？

Frontmatter 加：

```yaml
math: katex
```

### Q5：代码不高亮？

Marp 默认用 Prism.js 高亮。语言标记要写对：

````markdown
```python
# 而不是 py
```
````

### Q6：能转成 PowerPoint 吗？

可以，但有限制：

```powershell
marp my-talk.md --pptx
```

⚠️ 复杂布局/字体可能丢失。**导 PDF 更稳**。

### Q7：怎么和 [[Foam]] 配合？

Marp 文档**可以**放 Foam 知识库：
- 放在 `topics/.../slides/` 子目录
- 用 `marp: true` 标记
- Foam 的 wikilink `[[]]` 在 Marp 渲染时会显示为纯文本（不影响）

### Q8：康奈尔笔记能转 Marp 幻灯片吗？

可以！[[cornell-note]] 模板本身是 HTML/Markdown，Marp 用 `style: |` 配 CSS Grid 模拟两栏即可。详见 [[#示例 3：康奈尔笔记版]]。

---

## 参考资源

- [Marp 官方文档](https://marpit.marp.app/)
- [Marp 主题集](https://github.com/marp-team/marp-core/tree/main/themes)
- [Marpit Directive 完整参考](https://marpit.marp.app/directives)
- [Marp CLI 文档](https://github.com/marp-team/marp-cli)
- [Awesome Marp](https://github.com/awesome-marp/awesome-marp)

---

## 相关笔记

- [[topics/tools/Markdown]] —— Markdown 基础
- [[topics/tools/Foam]] —— 知识库管理
- [[topics/tools/VSCode]] —— VS Code 配置
- [[templates/cornell-note]] —— 康奈尔笔记（可转 Marp）
- [[templates/cornell-marp]] —— **康奈尔 × Marp 混合模板**
- [[topics/tools/marp-screencast-script]] —— 5 分钟录屏脚本
- [[topics/programming/Java/slides/Servlet-lifecycle]] —— 实战示例（Servlet 生命周期）
- [[topics/tools/Shortcuts]] —— 工具速查
