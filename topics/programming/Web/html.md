---
title: HTML 基础
tags:
  - programming
  - web
  - html
created: 2026-10-10
updated: 2026-10-10
---
# HTML 基础

> 面向对象：往前端方向入门的读者；目标是掌握**结构化标记 + 语义化**的思维方式，为 [[topics/programming/Web/css]]（样式）与 [[topics/programming/Web/javascript]]（行为）打底。
> 定位：单篇基础笔记，覆盖日常开发所需的 HTML 核心知识，不追求全集；HTTP / 网络基础按计划另立笔记。编程导航见 [[notes/MOC - programming]]。

## 1. HTML 是什么

HTML（HyperText Markup Language，超文本标记语言）描述页面的**结构与含义**，浏览器解析后生成 DOM 树，再由 CSS 装饰、JavaScript 操作。三层分工：

| 层 | 技术 | 负责的问题 | 类比 |
|----|------|-----------|------|
| 结构 | HTML | **是什么**（标题、段落、按钮） | 骨架 |
| 表现 | CSS | **长什么样**（颜色、布局、动画） | 皮肤 |
| 行为 | JavaScript | **做什么**（响应点击、请求数据） | 神经 |

写 HTML 的核心心智模型：**标记的是语义，不是外观**。"想让文字变大"不是用 `<big>`（已废弃），而是"这是标题"→ `<h2>`，大小交给 CSS。语义化是贯穿全篇的主线。

## 2. 文档基本结构

```html
<!DOCTYPE html>              <!-- 文档类型声明，触发标准模式 -->
<html lang="zh-CN">          <!-- lang 帮助翻译工具、读屏器发音 -->
<head>                       <!-- 给浏览器/搜索引擎看的元信息 -->
  <meta charset="UTF-8">     <!-- 字符编码，必须是 head 前 1024 字节内 -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>页面标题</title>     <!-- 浏览器标签页 + 搜索结果标题 -->
</head>
<body>                       <!-- 用户看到的内容 -->
  <!-- 内容写在这里 -->
</body>
</html>
```

要点：

- `<!DOCTYPE html>`：HTML5 的简化写法，没有它浏览器进入"怪异模式"（盒模型等行为会变，CSS 排版难以预测）。
- `<meta name="viewport">`：移动端适配的入口，没有它手机会以 980px 宽渲染再缩放。
- `<head>` 里的内容不直接显示（`<title>` 显示在标签页）；`<body>` 是可见内容。

## 3. 常用元素速览

### 3.1 文本级

| 元素 | 语义 | 备注 |
|------|------|------|
| `<h1>`–`<h6>` | 标题层级 | 每页一个 `<h1>`，不跳级 |
| `<p>` | 段落 | 块级，段落间距由 CSS 管 |
| `<strong>` / `<em>` | **重要** / *强调* | 有语义；`<b>`/`<i>` 只改外观无语义 |
| `<br>` / `<hr>` | 换行 / 主题分隔 | 空元素，无闭合标签 |
| `<span>` | 无语义行内容器 | 仅作 CSS/JS 钩子 |
| `<code>` / `<pre>` | 代码 / 预格式文本 | `pre` 保留空格换行 |
| `<blockquote>` / `<q>` | 块引用 / 行内引用 | `cite` 属性标来源 |

### 3.2 结构与语义容器

HTML5 语义标签替代"满屏 `<div>`"，是语义化的主战场：

```html
<body>
  <header>页头：logo、导航</header>
  <nav>导航链接组</nav>
  <main>               <!-- 每页唯一的主内容区 -->
    <article>          <!-- 独立成篇：一篇文章、一条评论、一张卡片 -->
      <h1>标题</h1>
      <section>        <!-- 文章内的章节，通常带标题 -->
        <h2>小节</h2>
      </section>
    </article>
    <aside>侧边栏、广告、相关链接</aside>
  </main>
  <footer>页脚：版权、联系方式</footer>
</body>
```

判断标准：`<article>` 拿出来单独发布仍然完整（RSS 里一条）；`<section>` 是主题分块；纯为了布局切分且无语义时才用 `<div>`。

### 3.3 列表

```html
<ul><li>无序列表</li></ul>          <!-- 导航、标签列表 -->
<ol><li>有序列表</li></ol>          <!-- 步骤、排行 -->
<dl><dt>术语</dt><dd>定义</dd></dl> <!-- 键值对：FAQ、参数表 -->
```

### 3.4 链接与图片

```html
<a href="https://example.com">外部链接</a>
<a href="/about">站内绝对路径</a>
<a href="#section-id">页内锚点</a>
<a href="mailto:a@b.com">邮件</a>
<a href="https://" target="_blank" rel="noopener noreferrer">新标签打开</a>

<img src="photo.jpg" alt="日落下的教学楼" width="800" height="600" loading="lazy">
```

要点：

- `target="_blank"` 必须配 `rel="noopener noreferrer"`：否则新页面能通过 `window.opener` 操纵原页面（安全 + 性能问题）。
- `alt` 是图片加载失败时的替代文本，也是读屏器朗读的内容；装饰性图片用 `alt=""`（空串）明确告知可跳过。
- `width`/`height` 写在标签上可以**预留空间**，避免图片加载引起布局抖动（CLS 指标）。
- 图片路径规范见仓库约定：资源统一放 `attachments/`，用 Markdown 路径或相对路径均可，但要与 Foam wikilink 区分。

### 3.5 表格

```html
<table>
  <caption>2026 年学习时长统计</caption>
  <thead>
    <tr><th>月份</th><th>小时</th></tr>
  </thead>
  <tbody>
    <tr><td>10 月</td><td>64</td></tr>
  </tbody>
</table>
```

- 表格只用于**二维数据**，不要拿来布局（上世纪做法）。
- `<th>` 自带"表头单元格"语义，读屏器会朗读列名，这是无障碍表格的关键。

## 4. 表单：交互的入口

表单是前端项目（登录、注册、搜索）的核心，也是 Vue 双向绑定的主要对象。

```html
<form action="/login" method="post">
  <label for="username">用户名</label>
  <input id="username" name="username" type="text" required minlength="3">

  <label for="pwd">密码</label>
  <input id="pwd" name="pwd" type="password" required>

  <label for="city">城市</label>
  <select id="city" name="city">
    <option value="">请选择</option>
    <option value="bj">北京</option>
  </select>

  <textarea id="bio" name="bio" rows="3" placeholder="一句话介绍自己"></textarea>

  <fieldset>
    <legend>订阅</legend>
    <label><input type="checkbox" name="news"> 新闻</label>
    <label><input type="radio" name="plan" value="m" checked> 月付</label>
    <label><input type="radio" name="plan" value="y"> 年付</label>
  </fieldset>

  <button type="submit">提交</button>
</form>
```

要点：

- **`<label>` 永远配 `id`**（或包裹控件）：点击文字也能聚焦，读屏器朗读字段名——无障碍与易用性双收益。
- `type` 决定键盘行为与校验：`email`/`number`/`date`/`tel` 在手机上调出对应键盘；`required`/`minlength`/`pattern` 提供原生校验（框架时代常被 JS 校验替代，但原生层值得保留）。
- `<button>` 不写 `type` 时默认 `submit`——**表单里放"取消"按钮必须写 `type="button"`**，否则点击就提交（高频坑）。
- `name` 是提交到服务端的键名，`id` 用于 label 关联与 JS 选择，两者职责不同。
- 单选框按 `name` 分组：同名互斥。

## 5. 多媒体与嵌入

```html
<video src="intro.mp4" controls muted poster="cover.jpg"></video>
<audio src="podcast.mp3" controls></audio>
<iframe src="https://player.example.com/x" title="视频播放器" allowfullscreen></iframe>
```

- `controls` 显示原生控制条；`muted`+`autoplay` 组合才允许自动播放（浏览器策略）。
- `iframe` 嵌入第三方页面（地图、播放器）时补 `title`，读屏器才有上下文。

## 6. 全局属性与 class/id

所有元素共享的常用属性：

| 属性 | 作用 | 场景 |
|------|------|------|
| `id` | 全文档唯一标识 | label 关联、锚点、`getElementById` |
| `class` | 样式/行为分组钩子 | CSS 选择器主力 |
| `style` | 行内样式 | 调试用，生产少写 |
| `hidden` | 隐藏元素 | 等价 `display:none` 的语义写法 |
| `data-*` | 自定义数据 | JS 读 `el.dataset.foo` |
| `title` | 悬停提示 | 补充说明，别当提示框滥用 |
| `tabindex` | 键盘焦点顺序 | `0` 可聚焦、`-1` 仅 JS 聚焦；**慎用正整数**（打乱自然顺序） |

## 7. head 里的 meta 与 SEO 基础

```html
<title>页面标题（搜索结果的第一行）</title>
<meta name="description" content="页面摘要，搜索结果第二行">
<link rel="icon" href="/favicon.ico">
<link rel="stylesheet" href="/style.css">
<script src="/app.js" defer></script>
<meta property="og:title" content="分享到社交平台时的标题">
```

- `<title>` 与 `description` 是 SEO 中唯二稳定可控的 HTML 层要素。
- `defer`：脚本并行下载、DOM 解析完再执行——`<script>` 放 head 里时几乎总该加（对比 `async`：下载完立即执行，顺序不保证，适合独立统计脚本）。
- Vue/React 项目里这些由框架（`useHead`、`react-helmet`）或构建配置管理，但原理相同。

## 8. 无障碍（a11y）最小集

语义化本身就是无障碍的基础。再加四条就覆盖大部分场景：

1. **图片有 `alt`**（装饰图空串）。
2. **表单控件有 label**。
3. **别删焦点样式**：写 CSS 时避免 `outline: none` 而不补替代样式。
4. **用语义标签代替 `<div onclick>`**：按钮就得是 `<button>`——回车/空格触发、焦点管理、读屏器角色全部免费获得。

```html
<!-- ❌ 假按钮：键盘用户无法触发 -->
<div class="btn" onclick="submit()">提交</div>
<!-- ✅ -->
<button type="submit" class="btn">提交</button>
```

## 9. 调试：DevTools

`F12` → Elements 面板：

- 查看实时 DOM（框架渲染后的真实结构）、hover 高亮盒模型；
- `Ctrl+F` 在面板内按选择器/CSS/XPath 搜节点；
- 强制 `:hover`/`:focus` 状态（`:hov` 面板）；
- 删掉可疑节点快速验证"是它导致的吗"。

## 10. 小结与下一步

- HTML 的价值在**语义**：选标签问"它是什么"，而不是"它长什么样"。
- 三件套分工：结构 → [[topics/programming/Web/css]]，行为 → [[topics/programming/Web/javascript]]（语言基础先行，ES6+ 见 [[topics/programming/Web/es6]]）。
- 工程化方向的下一步是让语义化为框架服务：Vue 单文件组件的 `<template>` 里写的就是这些标签；表单一节在 Vue 里对应 `v-model`，值得先在这里把原生行为（提交、校验、name/id）吃透。

### 自测

- [ ] 能默写最小 HTML5 文档骨架并说出 `DOCTYPE`、`viewport`、`charset` 各自的作用
- [ ] 能为一段含页头/导航/文章/侧栏/页脚的版面选出正确的语义标签
- [ ] 说得出 `<strong>` 与 `<b>`、`<article>` 与 `<section>`、`id` 与 `name` 的区别
- [ ] 知道表单里 `<button>` 默认 type 及其后果
- [ ] 能列出 4 条无障碍实践并说明理由

## 相关链接

- [[topics/programming/Web/css]] —— CSS（结构与表现的衔接）
- [[topics/programming/Web/javascript]] —— JavaScript（DOM 操作）
- [[topics/programming/Web/es6]] —— ES6+ 专题手册
- [[notes/MOC - programming]] —— 编程知识地图
