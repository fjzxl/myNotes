---
title: "CSS 入门指南 · 第三阶段：盒模型与显示模式 —— 理解元素的空间占用"
tags:
  - programming
  - css
created: 2026-09-10
updated: 2026-10-01
---

# 第三阶段：盒模型与显示模式 —— 理解元素的空间占用

> 📚 本文是 [[topics/programming/Web/css|CSS 入门指南]] 的第 3 / 10 章。 上一章：[[topics/programming/Web/css/stage-02-text-styling|第二阶段：给文字"化妆"]] · 下一章：[[topics/programming/Web/css/stage-04-selectors|第四阶段：选择器]]


> 🎯 **本节目标**：理解显示模式与盒模型的关系，掌握两种盒模型的区别，会使用 `border-box`，理解 block/inline/inline-block 的差异，掌握 padding、border、margin 的用法。
>
> 盒模型和显示模式是 CSS 中**最重要的两个概念**。不理解它们，布局永远学不好。

### 3.1 显示模式（Display）：元素在页面中的"行为身份"

#### 为什么会有显示模式？

打开任何一个网页，你会看到有的元素独占一行（如标题、段落），有的元素并排显示（如链接、强调文字）。HTML 标签天生具有不同的"行为性格"，而 **`display` 属性就是用来定义这种行为的**。

> 🍎 **生活比喻**：教室里有的同学喜欢独占一张桌子（block），有的同学喜欢几个人挤在一张长桌上（inline）。`display` 就是在规定"你该怎么坐"。

#### 常见显示模式一览

| 值             | 是否独占一行 | 可设宽高  | 典型元素                      | 生活比喻               |
| -------------- | ------------ | --------- | ----------------------------- | ---------------------- |
| `block`        | ✅ 独占一行  | ✅ 可以   | `div`、`p`、`h1~h6`           | 一人一张桌子           |
| `inline`       | ❌ 共占一行  | ❌ 不可以 | `span`、`a`、`strong`、`em`   | 几人挤一张长桌         |
| `inline-block` | ❌ 共占一行  | ✅ 可以   | `input`、`button`、`textarea` | 长桌上每人有固定座位   |
| `none`         | —            | —         | —                             | 这个人请假了，不占位置 |
| `flex`         | ✅ 独占一行  | —         | —                             | 像军训排队，有队长指挥 |
| `grid`         | ✅ 独占一行  | —         | —                             | 像棋盘，横竖分明       |

#### 常见 HTML 元素的显示模式

HTML 标签天生就带有默认的 `display` 值。**不需要死记硬背所有标签**，只要记住最常用的几个，其他的遇到时查一下就行。

**🔵 块级元素（block）—— 独占一行**

> 最常见的：**`div`**、`p`、`h1~h6`、`ul`/`li`、`section`、`header`、`footer`

这些元素在页面上会自动换行，默认占满父容器的可用宽度（`width: auto`）。

```html
<!-- 浏览器中，这三个元素会垂直堆叠，每个独占一行 -->
<div>我是 div</div>
<p>我是段落</p>
<h3>我是标题</h3>
```

**🟢 行内元素（inline）—— 共占一行，宽高由内容撑开**

> 最常见的：**`span`**、`a`、`strong`、`em`、`label`

这些元素不会换行，你设置 `width` 和 `height` 也不生效。

```html
<!-- 浏览器中，这三个会在同一行并排显示 -->
<span>我是 span</span>
<a href="#">我是链接</a>
<strong>我是加粗</strong>
```

**🟡 行内块元素（inline-block）—— 既能并排，又能设宽高**

> 最常见的：**`input`**、`button`、`img`、`textarea`、`select`

这些元素可以像行内元素一样并排，又可以像块级元素一样设置宽高。

```html
<!-- 浏览器中，输入框和按钮并排，且可以设置宽高 -->
<input type="text" placeholder="输入框" />
<button>按钮</button>
<img src="photo.jpg" width="100" />
```

---

**⚠️ 初学者最容易混淆的两个元素**

| 元素     | 默认显示模式           | 为什么特殊                                                                          |
| -------- | ---------------------- | ----------------------------------------------------------------------------------- |
| `img`    | `inline`（可替换元素） | 虽然是 inline，但可以设置宽高——它的内容被图片"替换"了，所以不受普通 inline 规则限制 |
| `select` | `inline-block`         | 表单类控件大多默认是 inline-block，既能并排又能设置尺寸                             |

---

> 💡 **快速判断小技巧**：
>
> 1. 这个标签是用来装**一大块内容**的？→ 大概率是 `block`（div、p、h1~h6）
> 2. 这个标签是用来修饰**文字**的？→ 大概率是 `inline`（span、strong、a）
> 3. 这个标签是**表单控件或图片**？→ 大概率是 `inline-block`（input、button、img）
>
> 遇到不确定的，用浏览器开发者工具选中元素，查看 `display` 值即可。

```css
/* ========== 最常用的转换场景 ========== */

/* 场景1：让 span 独占一行 */
span {
  display: block;
}

/* 场景2：让链接变成按钮（设置宽高 + 并排） */
.nav-item {
  display: inline-block;
  width: 100px;
  height: 40px;
  line-height: 40px;
  text-align: center;
  background: #3498db;
  color: white;
}
```

#### 显示模式与盒模型的关系

这是初学者最容易忽略的关键点：**显示模式决定了"哪些盒模型属性会生效"**。

| 属性                           | `block` | `inline`                                          | `inline-block` |
| ------------------------------ | ------- | ------------------------------------------------- | -------------- |
| `width` / `height`             | ✅ 生效 | ❌ 不生效（由内容撑开）                           | ✅ 生效        |
| `margin-top` / `margin-bottom` | ✅ 生效 | ❌ 不生效                                         | ✅ 生效        |
| `margin-left` / `margin-right` | ✅ 生效 | ✅ 生效                                           | ✅ 生效        |
| `padding`                      | ✅ 生效 | ⚠️ 垂直 padding 延伸背景，但不影响行框高度        | ✅ 生效        |
| `border`                       | ✅ 生效 | ✅ 生效（垂直 border 延伸背景，但不影响行框高度） | ✅ 生效        |

> 🔑 **核心结论**：`display` 决定"怎么排"，盒模型决定"占多少地"。**`inline` 元素的盒模型是"打折版"的**——宽度和垂直方向的 margin 不生效，padding 和 border 虽然能设置，但不会影响上下文的行高。

```css
/* 初学者常见困惑 */
span {
  width: 200px; /* ❌ 不生效！span 是 inline */
  height: 50px; /* ❌ 不生效！ */
  margin-top: 20px; /* ❌ 不生效！ */
}

/* ✅ 正确做法：先改变显示模式 */
span {
  display: inline-block;
  width: 200px;
  height: 50px;
  margin-top: 20px; /* 现在生效了！ */
}
```

> ⚠️ **常见坑**：`inline-block` 元素之间会出现约 4px 的空白间隙
>
> 这个间隙来自 HTML 源码中的**换行符和空格**。浏览器会把它们解析为"匿名文本节点"，从而产生间隙。这是很多初学者在使用 `inline-block` 做导航栏时遇到的第一个坑。

**问题现象的代码和效果**：

```html
<!-- HTML 中的换行和空格会产生间隙 -->
<div class="nav">
  <a class="nav-item">首页</a>
  <a class="nav-item">文章</a>
  <a class="nav-item">关于</a>
</div>
```

```css
.nav-item {
  display: inline-block;
  width: 80px;
  height: 40px;
  background: #3498db;
  color: white;
  text-align: center;
  line-height: 40px;
}
```

**浏览器中实际显示的效果**：

```
┌────────┐    约4px间隙    ┌────────┐    约4px间隙    ┌────────┐
│  首页  │  ←—空格—→   │  文章  │  ←—空格—→   │  关于  │
└────────┘               └────────┘               └────────┘
         ↑                             ↑
      这不是 margin！是 HTML 换行符被解析成的文本空格
```

> 💡 **原因**：`<a>` 标签之间的换行和缩进，在浏览器看来就是一段空白文本，和文字之间的空格是一样的。

**三种解决方案对比**：

**方案 1：父元素设置 `font-size: 0`（消除文本节点）**

```css
.nav {
  font-size: 0; /* 把匿名文本的字体大小设为 0，间隙就消失了 */
}
.nav-item {
  display: inline-block;
  font-size: 16px; /* 子元素必须重新设置字体大小！ */
  /* ... 其他样式不变 */
}
```

> ⚠️ **副作用**：如果子元素内有文字，必须重新设置 `font-size`，否则文字也会消失。

**方案 2：使用 Flexbox 布局（最推荐）**

```css
.nav {
  display: flex; /* 改用 Flex 布局，彻底避免间隙问题 */
  gap: 0; /* 间距由你精确控制，初始值 normal 在 Flex/Grid 中通常表现为 0 */
}
.nav-item {
  /* 不需要 display: inline-block 了 */
  width: 80px;
  height: 40px;
  /* ... 其他样式不变 */
}
```

> ✅ **优点**：没有 `font-size: 0` 的副作用，代码更简洁，且可以方便地通过 `gap` 控制间距。

**方案 3：HTML 标签连写（不推荐，但能让你理解原理）**

```html
<!-- 消除源码中的换行和空格，间隙自然消失 -->
<div class="nav">
  <a class="nav-item">首页</a><a class="nav-item">文章</a
  ><a class="nav-item">关于</a>
</div>
```

> ❌ **缺点**：HTML 可读性极差，实际项目中不要这样写。

> 🏆 **结论**：方案 2（Flexbox）是最优雅的解决方式。如果你还在用 `inline-block` 做横向布局，建议直接迁移到 Flexbox。

### 3.2 盒模型 —— 元素的空间构成

CSS 中，每个元素都被视为一个**矩形盒子**。这个盒子由四层组成，就像你收到的快递包裹：

```
┌─────────────────────────────────────────┐
│                                         │
│              margin（外边距）            │  ← 两个快递盒之间的距离
│           "快递盒与快递盒的间距"          │
│    ┌─────────────────────────────────┐  │
│    │                                 │  │
│    │          border（边框）          │  │  ← 纸箱的厚度
│    │          "纸箱的纸板厚度"        │  │
│    │   ┌─────────────────────────┐   │  │
│    │   │                         │   │  │
│    │   │       padding（内边距）  │   │  │  ← 气泡膜、填充物
│    │   │       "保护商品的海绵层"  │   │  │
│    │   │   ┌─────────────────┐   │   │  │
│    │   │   │                 │   │   │  │
│    │   │   │   content（内容）│   │   │  │  ← 杯子本身
│    │   │   │   "你买的商品"   │   │   │  │
│    │   │   │                 │   │   │  │
│    │   │   └─────────────────┘   │   │  │
│    │   │                         │   │  │
│    │   └─────────────────────────┘   │  │
│    │                                 │  │
│    └─────────────────────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
```

**四层记忆法**：

| 层次        | 作用                           | 背景色是否延伸 | 生活比喻             |
| ----------- | ------------------------------ | -------------- | -------------------- |
| **content** | 元素的实际内容（文字、图片等） | —              | 杯子本身             |
| **padding** | 内容与边框之间的内间距         | ✅ 会延伸      | 气泡膜、海绵         |
| **border**  | 边框线，分隔内外               | ✅ 会延伸      | 纸箱的纸板           |
| **margin**  | 元素与其他元素的外间距         | ❌ 不会延伸    | 两个快递盒之间的距离 |

> 💡 **记忆口诀**：
>
> - **padding** = **p**adding = **内**部填充（背景色会延伸到这）
> - **margin** = **m**argin = **外**部间距（与其他盒子的距离）
> - **border** = 边界线，分隔内外

### 🔴 重难点：两种盒模型对比

这是初学者**最容易混淆**的概念！理解它，你的 CSS 布局能力会提升一大截。

#### 为什么会有两种盒模型？

在 CSS 早期，**W3C 标准**和 **IE 浏览器**对 `width` 的定义不同：

- **W3C 认为**：`width` 应该只包含内容区（content）
- **IE 认为**：`width` 应该包含内容 + 内边距 + 边框

后来 CSS3 引入 `box-sizing` 属性，让开发者可以自主选择：

| 属性值        | 含义                                    | 别名       |
| ------------- | --------------------------------------- | ---------- |
| `content-box` | `width` 只包含 content                  | 标准盒模型 |
| `border-box`  | `width` 包含 content + padding + border | IE 盒模型  |

#### 核心区别图解

假设都设置：`width: 200px; padding: 20px; border: 2px solid; margin: 10px`

**`box-sizing: content-box`（默认）**：

```
实际占用宽度 = width + padding×2 + border×2 + margin×2
           = 200 + 40 + 4 + 20
           = 264px

┌────────────────────────────────────────────────────────────┐
│ margin (10px)                                              │
│   ┌──────────────────────────────────────────────────┐     │
│   │ border (2px)                                     │     │
│   │   ┌──────────────────────────────────────────┐   │     │
│   │   │ padding (20px)                           │   │     │
│   │   │   ┌──────────────────────────────┐       │   │     │
│   │   │   │    content (200px)           │       │   │     │
│   │   │   │    "width 只算这里"          │       │   │     │
│   │   │   └──────────────────────────────┘       │   │     │
│   │   └──────────────────────────────────────────┘   │     │
│   └──────────────────────────────────────────────────┘     │
└────────────────────────────────────────────────────────────┘
```

**`box-sizing: border-box`**：

```
实际到 border 为止的宽度 = 200px（padding 和 border 被包含在内）
content 实际宽度 = 200 - 40 - 4 = 156px

┌────────────────────────────────────────────┐
│ margin (10px)                              │
│   ┌────────────────────────────────────┐   │
│   │ ┌──────────────────────────────┐   │   │
│   │ │ ┌────────────────────┐       │   │   │
│   │ │ │ content (156px)    │       │   │   │
│   │ │ │ "被压缩后的内容区"  │       │   │   │
│   │ │ └────────────────────┘       │   │   │
│   │ │      padding (20px)          │   │   │
│   │ └──────────────────────────────┘   │   │
│   │        border (2px)                │   │
│   │        "到 border 共 200px"        │   │
│   └────────────────────────────────────┘   │
└────────────────────────────────────────────┘
```

#### 生活比喻

| 盒模型        | 你说了什么        | 实际占地                        |
| ------------- | ----------------- | ------------------------------- |
| `content-box` | "我的杯子宽 10cm" | 10cm + 气泡膜 + 纸箱厚度 = 更大 |
| `border-box`  | "整个包裹宽 10cm" | 就是 10cm，内部自己压缩         |

#### 代码对比实例

```css
/* 两个盒子都设置相同的 width，但盒模型不同 */
.box1 {
  box-sizing: content-box; /* 默认，可省略 */
  width: 200px;
  padding: 20px;
  border: 2px solid red;
  margin: 10px;
  /* 实际到 border 为止的宽度：200 + 20×2 + 2×2 = 244px */
  /* 加上 margin 的总占用：244 + 10×2 = 264px */
}

.box2 {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 2px solid blue;
  margin: 10px;
  /* 实际到 border 为止的宽度：200px（就是 width 的值！） */
  /* 内部 content 实际只有：200 - 20×2 - 2×2 = 156px */
  /* 加上 margin 的总占用：200 + 10×2 = 220px */
}
```

> 💡 **直观对比**：
>
> - `content-box`：你设定的是"内容宽度"，但实际占地要心算
> - `border-box`：你设定的是"边框以内总宽度"，所见即所得

#### 为什么强烈推荐 `border-box`？

在实际布局中，我们通常更关心"这个元素在页面上占多少地方"，而不是"它的内容区有多宽"。

```css
/* 实际场景：两栏布局 */
.column {
  width: 50%;
  padding: 20px;
  border: 1px solid #ccc;
  float: left;
}

/* content-box 下：两个 50% 的栏会挤爆容器！
   因为实际宽度 = 50% + 20px×2 + 1px×2 > 50% */

/* border-box 下：两个 50% 的栏完美并排
   因为 padding 和 border 被包含在 50% 内 */
```

**全局设置（现代项目标配）**：

```css
/* 强烈推荐全局设置！ */
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

> ⚠️ **常见错误**：
>
> - 给 `span`、`a` 等行内元素设置 `width` 和 `height` 不生效（需要改为 `display: block` 或 `inline-block`）
> - 设置 `height: 100%` 不生效（需要**所有祖先元素**链路上都有确定高度，通常需要 `html, body { height: 100%; }`）

### 3.3 内容区（Content）

- `width`：设置内容宽度
- `height`：设置内容高度
- **只对块级元素和行内块元素生效**（`inline` 元素由内容撑开）

> ⚠️ **常见错误**：`height: 100%` 不生效，通常是因为父元素没有明确设定高度（父元素高度是 auto 由内容撑开）。解决方法是确保直接父元素有确定高度：
>
> ```css
> html,
> body {
>   height: 100%;
> } /* 逐级向上设置 */
> .parent {
>   height: 500px;
> } /* 或直接给父元素设定高度 */
> ```

### 3.4 内边距（Padding）

元素**内部**的间距，背景色会延伸到 padding 区域。

```css
/* 四个方向 */
padding: 10px; /* 上下左右都是 10px */
padding: 10px 20px; /* 上下 10px，左右 20px */
padding: 10px 20px 30px 40px; /* 上、右、下、左（顺时针） */

/* 单独设置 */
padding-top: 10px;
padding-right: 20px;
padding-bottom: 30px;
padding-left: 40px;
```

> 💡 **记忆口诀**：顺时针，上右下左，对称时可以简写。

### 3.5 边框（Border）

```css
/* 简写：宽度 样式 颜色 */
border: 1px solid #ccc;

/* 单独设置 */
border-width: 2px;
border-style: dashed; /* solid、dashed、dotted、double、none */
border-color: red;

/* 圆角 */
border-radius: 8px; /* 统一圆角 */
border-radius: 8px 16px; /* 左上+右下 / 右上+左下 */
border-radius: 50%; /* 正圆（元素宽高相等时） */
```

> 💡 **常用边框技巧**：
>
> - 细线边框：`border: 1px solid #e0e0e0`
> - 无边框但占位：`border: 1px solid transparent`
> - 三角形（利用边框）

##### 三角形是怎么画出来的？

这是 CSS 中最经典的技巧之一，核心原理是：**把元素的宽高设为 0，四个边框就会从中心点向四个角延伸，交汇成四个三角形**。

**第一步：一个普通盒子的边框**

```css
.box {
  width: 40px;
  height: 40px;
  border-top: 20px solid red;
  border-right: 20px solid green;
  border-bottom: 20px solid blue;
  border-left: 20px solid orange;
}
```

浏览器中显示的效果：

```
┌────────────────────────┐
│\        red           /│
│ \                    / │
│  ┌──────────────────┐  │
│  │     content      │  │
│  │     (40×40)      │  │
│  └──────────────────┘  │
│ /        blue        \ │
│/                      \│
└────────────────────────┘
```

注意观察四个角：每个角都是**两条边框斜向交汇**形成的（上边框为红色，右边框为绿色，下边框为蓝色，左边框为橙色；四个边框分别横跨顶部/底部、纵贯左侧/右侧，紧密包围着中间的内容区）。`border-top`（红色）和 `border-left`（橙色）在左上角交汇，自然形成了一个斜边。

> 🔴 **为什么是对角线？**
>
> 因为每个边框都是一块**矩形区域**（不是一条线）。在左上角：
>
> - 上边框的下内边缘是内容区的**顶边**（水平线）
> - 左边框的右内边缘是内容区的**左边**（垂直线）
> - 这两条线在内容区的角上相交成 90°
>
> 浏览器用一条对角线连接**外角**和**内角**，把中间的区域平分给两个边框：
>
> ```
>      外角
>        ●────────────────
>        │\     上边框     │
>        │ \               │
>        │  \              │
>        │   ●────────────
>        │   │ 内角（内容区左上角）
>        └───┘
> ```
>
> 当相邻两个边框宽度相等时（如都是 20px），这条对角线恰好是 **45°**。

**第二步：把宽高设为 0**

```css
.box {
  width: 0;
  height: 0;
  border-top: 20px solid red;
  border-right: 20px solid green;
  border-bottom: 20px solid blue;
  border-left: 20px solid orange;
}
```

中间的内容区消失了，只剩下四个三角形：

```
         ▼
        /│\      ← 上边框（红色朝下三角形）
       / │ \
      /  │  \
     /   │   \
    ▶   │    ◀      ← 左右边框（橙色朝右、绿色朝左）
     \   │   /
      \  │  /
       \ │ /
        \│/
         ▲
      下边框（蓝色朝上三角形）
```

**第三步：只保留一个三角形，其他三个变透明**

```css
.triangle {
  width: 0;
  height: 0;
  border: 10px solid transparent; /* 四个边框都是透明 */
  border-bottom-color: red; /* 只让下边框显示红色 */
}
```

浏览器最终只显示一个朝上的红色三角形（其余三个边框完全透明，不可见）：

```
       ▲
      /│\
     / │ \
    /  │  \
   /   │   \      ← 红色朝上三角形
  /    │    \        底边 20px，高 10px
 /     │     \
/────────────────\
```

> 💡 **本质理解**：`border` 不是一条线，而是一个**梯形区域**。当元素没有内容区（宽高为 0）时，梯形退化为**三角形**。

**不同方向的三角形代码**：

```css
/* 朝上 ▲ */
.triangle-up {
  width: 0;
  height: 0;
  border: 10px solid transparent;
  border-bottom-color: red;
}

/* 朝下 ▼ */
.triangle-down {
  width: 0;
  height: 0;
  border: 10px solid transparent;
  border-top-color: red;
}

/* 朝左 ◀ */
.triangle-left {
  width: 0;
  height: 0;
  border: 10px solid transparent;
  border-right-color: red;
}

/* 朝右 ▶ */
.triangle-right {
  width: 0;
  height: 0;
  border: 10px solid transparent;
  border-left-color: red;
}
```

> ⚠️ **为什么必须写 `width: 0; height: 0;`？**
> 如果不设，元素会有默认的宽高（或者由内容撑开），四个边框之间会有内容区隔开，就看不到三角形交汇的效果了。

### 3.6 外边距（Margin）

元素**外部**的间距，背景色不会延伸到这里。

```css
margin: 10px;
margin: 10px auto; /* 上下 10px，左右自动（水平居中常用） */
margin: 0 auto; /* 块级元素水平居中 */
```

> ⚠️ **居中前提**：`margin: 0 auto` 只对**设置了固定宽度**的块级元素生效。如果元素宽度是 100%（块级元素默认值），左右 auto 会被计算为 0，看不出居中效果。
>
> **为什么？**
>
> `auto` 的含义是"把剩余空间平分给我"。如果元素宽度是 100%，它已经占满了整行，**没有剩余空间**，左右 auto 自然就是 0。
>
> 只有当元素宽度**小于父容器**（如 200px、50%、800px 等），左右才会有"剩余空间"，auto 才能把这些空间平分成两半，实现居中。
>
> ```css
> /* ❌ 错误：没设宽度，默认 100%，auto = 0，不居中 */
> .box {
>   /* width 默认为 100%，不写也行 */
>   margin: 0 auto;
>   background: red;
> }
>
> /* ✅ 正确：设置了固定宽度，剩余空间被 auto 平分，完美居中 */
> .box {
>   width: 600px; /* 或 50%、max-width: 800px 等 */
>   margin: 0 auto;
>   background: green;
> }
> ```
>
> 💡 **快速验证**：在开发者工具中查看元素的 Computed 样式。如果左右 margin 都是 0，说明宽度太宽或没设宽度；如果左右 margin 有值且相等，说明居中生效。

#### 🔴 重难点：垂直外边距合并（Margin Collapse）

**垂直外边距合并**是 CSS 中最让初学者困惑的概念之一。简单来说：当两个块级元素在**垂直方向**上相遇时，它们的 `margin-top` 和 `margin-bottom` 不会相加，而是**合并成一个外边距，取其中较大的那个值**。

##### 为什么会这样？

CSS 的设计者认为，外边距是用来控制**元素之间**的间距的。如果两个元素都想和对方保持距离，取最大值就足够了，叠加反而会让间距过大。

> 🍎 **生活比喻**：就像两个人排队，前面的人说"我要和后面的人保持 20cm"，后面的人说"我要和前面的人保持 30cm"——他们最终只会隔开 **30cm**，而不是 50cm。距离是共享的，不会叠加。

##### 三种会发生合并的情况

**情况 1：相邻兄弟元素**

两个垂直排列的块级元素，上元素的 `margin-bottom` 和下元素的 `margin-top` 会合并。

```css
.box1 {
  margin-bottom: 20px;
}
.box2 {
  margin-top: 30px;
}
/* ❌ 你以为间距是 50px */
/* ✅ 实际是 30px（取最大值） */
```

如果两个值相等（比如都是 20px），结果就是 20px；如果一个正数一个负数（比如 30px 和 -10px），结果是 **20px**（代数相加）。

**情况 2：父子元素之间（最容易踩坑！）**

当父元素没有上边框（`border-top`）、没有上内边距（`padding-top`）、没有 `overflow: hidden` 等"阻隔"时，子元素的 `margin-top` 会**穿过父元素**，和父元素的 `margin-top` 合并。

```css
.parent {
  /* 没有 border、没有 padding */
  background: lightblue;
}
.child {
  margin-top: 50px; /* 这个 margin 会"溢出"到父元素外面！ */
  background: pink;
}
```

显示效果示意：

```html
<!-- HTML 结构 -->
<div class="parent">
  <div class="child"></div>
</div>
```

**初学者常见困惑**：我给子元素加了 `margin-top: 50px`，想让它在父元素内部向下偏移，结果却是**父元素整体向下移动了 50px**！这就是因为父子之间的垂直 margin 发生了合并。

> 🎯 **形象理解**：想象父元素是一张没有边框的纸，子元素的 `margin-top` 就像是从纸的上方"漏"了出去，直接作用在父元素的外面。

**情况 3：空的块级元素**

如果一个块级元素没有内容、没有高度、没有边框、没有内边距，它的 `margin-top` 和 `margin-bottom` 也会合并。

```css
.empty-box {
  margin-top: 20px;
  margin-bottom: 30px;
  /* 没有 height、border、padding、content */
}
/* 这个空元素实际占据的垂直空间是 30px，不是 50px */
```

##### 如何防止外边距合并？

针对不同场景，有以下几种方法：

| 方法                   | 适用场景         | 原理                                 |
| ---------------------- | ---------------- | ------------------------------------ |
| 加 `border`            | 父子合并         | 边框像一堵墙，阻止 margin "漏"出去   |
| 加 `padding`           | 父子合并         | 内边距填充了空间，margin 有了"起点"  |
| `display: flow-root`   | 父子合并（推荐） | 创建新的 BFC，隔离内外 margin        |
| `overflow: hidden`     | 父子合并         | 同样创建 BFC，但可能裁切溢出内容     |
| 只给一个元素设 margin  | 兄弟合并         | 比如统一用 `margin-bottom` 控制间距  |
| 用 `gap` / `flex` 布局 | 兄弟合并         | Flex/Grid 布局中不会发生 margin 合并 |

```css
/* ✅ 推荐：现代浏览器，无副作用 */
.parent {
  display: flow-root;
}

/* ✅ 兼容旧浏览器，但会裁切溢出内容 */
.parent {
  overflow: hidden;
}

/* ✅ 简单直接，但会改变盒模型尺寸 */
.parent {
  padding-top: 1px; /* 1px 就够了！ */
}

/* ✅ 同样简单 */
.parent {
  border-top: 1px solid transparent; /* 透明边框，视觉上看不见 */
}
```

##### 什么时候不会合并？

记住这些例外情况，排查问题时很有用：

- **水平方向**的 `margin-left` 和 `margin-right` **永远不会合并**
- **行内元素**（`display: inline`）的垂直 margin **不会合并**
- **浮动元素**（`float: left/right`）之间不会合并
- **绝对定位元素**（`position: absolute/fixed`）之间不会合并
- **Flex/Grid 布局的子元素**之间不会合并
- 两个 margin 之间有**边框、内边距、清除浮动**等阻隔时不会合并

> 💡 **给初学者的小建议**：在实际项目中，控制兄弟元素之间的垂直间距时，建议**只使用 `margin-bottom`**（或者统一使用 `margin-top`），而不是上下都用。这样可以避免大多数的外边距合并困扰。比如：
>
> ```css
> p {
>   margin-top: 0;
>   margin-bottom: 1em;
> }
> ```

### 3.7 `display: none` vs `visibility: hidden`

| 特性       | `display: none`      | `visibility: hidden`         |
| ---------- | -------------------- | ---------------------------- |
| 是否占空间 | ❌ 不占              | ✅ 占                        |
| 是否可见   | ❌ 不可见            | ❌ 不可见                    |
| 子元素状态 | 也消失               | 默认也隐藏（可单独设置可见） |
| 触发重排   | ✅ 会（性能开销大）  | ❌ 不会（性能更好）          |
| 生活比喻   | 这个人从世界上消失了 | 这个人隐形了，但位置还在     |

> ⚠️ **注意**：`display: none` 会让元素完全消失（不占空间），与 `visibility: hidden`（隐藏但占位）不同。

### ✅ 本节回顾

- [x] 理解 `block`、`inline`、`inline-block` 的区别和使用场景
- [x] 知道显示模式会影响哪些盒模型属性生效
- [x] 能用"快递盒"比喻解释盒模型的四层结构
- [x] 知道 `content-box` 和 `border-box` 的区别，理解为什么推荐 `border-box`
- [x] 会用简写设置四个方向的内边距/外边距
- [x] 知道 `margin: 0 auto` 的前提条件是块级元素 + 固定宽度
- [x] 理解垂直外边距合并的三种情况和解决方法

### 📝 自测题

**1. 设置 `box-sizing: border-box` 后，`width: 200px; padding: 20px; border: 2px` 的元素总宽度是多少？**

- A. 200px
- B. 244px
- C. 222px
- D. 242px

**2. `margin: 0 auto` 能实现水平居中的前提条件是？**

- A. 元素必须是块级元素且设置了宽度
- B. 任何元素都可以
- C. 父元素必须设置 `text-align: center`
- D. 元素必须是 `display: flex`

**3. 两个上下相邻的 `div`，分别设置 `margin-bottom: 30px` 和 `margin-top: 50px`，实际间距是？**

- A. 80px
- B. 30px
- C. 50px
- D. 20px

**4. `display: inline` 和 `display: inline-block` 的主要区别是？**

- A. 没有区别
- B. inline 不能设置宽高，inline-block 可以
- C. inline 独占一行，inline-block 不独占
- D. inline 是块级元素

**5. 以下哪个属性设置的是元素内部的间距（背景色会延伸到这）？**

- A. margin
- B. padding
- C. border
- D. width

<details>
<summary>点击查看答案</summary>

1. **A**（border-box 下 width 包含 content + padding + border）
2. **A**（需要是块级且设置宽度，否则默认 100% 看不出居中）
3. **C**（垂直外边距合并，取最大值 50px）
4. **B**（inline-block 可以设置宽高，inline 不行）
5. **B**（padding 是内边距）

</details>

### ✏️ 动手练习

1. 创建一个 `div`，设置宽高 200px，背景色浅灰，内边距 20px，边框 2px 蓝色实线，外边距 20px。分别用 `content-box` 和 `border-box` 观察总尺寸差异。
2. 创建两个上下排列的 `div`，分别设置 `margin-bottom: 30px` 和 `margin-top: 50px`，用开发者工具验证实际间距。
3. 创建一个 `span`，尝试设置宽高，观察是否生效。然后改为 `display: inline-block`，再次观察。
