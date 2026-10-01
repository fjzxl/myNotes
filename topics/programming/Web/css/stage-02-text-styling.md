---
title: "CSS 入门指南 · 第二阶段：给文字"化妆" —— 最直观的改变"
tags:
  - programming
  - css
created: 2026-09-10
updated: 2026-10-01
---

# 第二阶段：给文字"化妆" —— 最直观的改变

> 📚 本文是 [[topics/programming/Web/css|CSS 入门指南]] 的第 2 / 10 章。 上一章：[[topics/programming/Web/css/stage-01-getting-started|第一阶段：初识 CSS]] · 下一章：[[topics/programming/Web/css/stage-03-box-model|第三阶段：盒模型与显示模式]]


> 🎯 **本节目标**：能修改文字的颜色、大小、字体、对齐方式，实现文字溢出省略效果。
>
> 这是最容易有成就感的部分。改个颜色、换个字体，页面立刻不一样。

### 🍎 生活比喻：颜色就像调颜料

CSS 中的颜色设置就像画家调色：

- **颜色关键字** `red` = 直接拿预调好的颜料（"给我红色"）
- **十六进制** `#ff0000` = 精确的颜料配方（"红255，绿0，蓝0"）
- **RGB** `rgb(255, 0, 0)` = 用三原色光混合（就像舞台灯光调色）
- **RGBA** `rgba(255, 0, 0, 0.5)` = 加了透明度的颜料（就像半透明的彩色玻璃纸）
- **HSL** `hsl(0, 100%, 50%)` = 按色相/饱和度/亮度调色（更直观："红色，最纯，中等亮度"）

### 2.1 颜色（Color）

| 表示方式   | 示例                      | 说明               | 什么时候用           |
| ---------- | ------------------------- | ------------------ | -------------------- |
| 颜色关键字 | `red`、`blue`、`black`    | 147 个预定义颜色   | 快速测试、教学演示   |
| 十六进制   | `#ff0000`、`#f00`         | 最常用，#RRGGBB    | **日常开发首选**     |
| RGB        | `rgb(255, 0, 0)`          | 红绿蓝三通道       | 需要动态计算颜色时   |
| RGBA       | `rgba(255, 0, 0, 0.5)`    | 带透明度（0~1）    | **需要半透明时**     |
| HSL        | `hsl(0, 100%, 50%)`       | 色相、饱和度、亮度 | 主题色系统、调整深浅 |
| HSLA       | `hsla(0, 100%, 50%, 0.5)` | 带透明度的 HSL     | 需要透明度的主题色   |

**💡 记忆口诀**：

> 日常开发用 **十六进制**，
> 半透明用 **RGBA**，
> 调深浅用 **HSL**。

> ⚠️ **重点**：`#fff` 是 `#ffffff` 的简写，`#f00` 是 `#ff0000` 的简写，书写更简洁！

> ⚠️ **常见错误**：`opacity` 设置透明度会**影响整个元素及其所有子元素**，而 `rgba` 只影响**当前属性**（如只让背景半透明，文字保持不透明）！
>
> ```css
> /* 错误：子元素也会变透明 */
> .parent {
>   opacity: 0.5;
> }
>
> /* 正确：只有背景半透明，子元素不受影响 */
> .parent {
>   background: rgba(0, 0, 0, 0.5);
> }
> ```

### 2.2 字体样式（Font）

| 属性          | 作用         | 常用值                     | 生活比喻                    |
| ------------- | ------------ | -------------------------- | --------------------------- |
| `font-size`   | 字体大小     | `16px`、`1.2em`、`1rem`    | 字多大，就像字号            |
| `font-family` | 字体族       | `"Microsoft YaHei", Arial` | 用什么字体，就像选钢笔/毛笔 |
| `font-weight` | 字重（粗细） | `normal`(400)、`bold`(700) | 笔的粗细                    |
| `font-style`  | 字体样式     | `normal`、`italic`         | 正写还是斜写                |
| `line-height` | 行高         | `1.5`、`24px`              | 行与行的间距                |

**字体栈写法**（从左到右依次回退）：

```css
body {
  font-family:
    "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei",
    sans-serif;
}
```

> 🍎 **比喻理解**：字体栈就像"点名优先级"——
>
> 1. 先叫 `"Helvetica Neue"`（Mac 优先字体）
> 2. 不在？叫 `Helvetica`
> 3. 不在？叫 `Arial`（Windows 英文字体）
> 4. 不在？叫 `"PingFang SC"`（Mac 中文字体）
> 5. 不在？叫 `"Microsoft YaHei"`（Windows 中文字体）
> 6. 都不在？用系统默认的 `sans-serif`（无衬线字体）

**常用 font 简写**（按顺序：style weight size/line-height family）：

```css
body {
  font:
    400 16px/1.5 "Microsoft YaHei",
    sans-serif;
}
```

> ⚠️ **注意**：简写时 `font-size` 和 `font-family` 是必填项，否则不生效。

### 2.3 文本排版（Text）

| 属性              | 作用       | 常用值                    | 比喻               |
| ----------------- | ---------- | ------------------------- | ------------------ |
| `text-align`      | 水平对齐   | `left`、`center`、`right` | 文字在横线上怎么排 |
| `text-decoration` | 文本装饰   | `none`、`underline`       | 加下划线、删除线   |
| `text-transform`  | 大小写转换 | `uppercase`、`lowercase`  | 全大写、全小写     |
| `letter-spacing`  | 字间距     | `2px`、`0.05em`           | 字与字的呼吸空间   |
| `word-spacing`    | 词间距     | `4px`                     | 英文单词间的距离   |
| `white-space`     | 空白处理   | `normal`、`nowrap`        | 换不换行           |

```css
/* 去掉链接下划线 */
a {
  text-decoration: none;
}

/* 标题大写 */
h1 {
  text-transform: uppercase;
  letter-spacing: 2px;
}

/* 文本两端对齐 */
.paragraph {
  text-align: justify;
}
```

### 2.4 文字溢出处理

```css
/* 单行省略 */
.single-line {
  white-space: nowrap; /* 不换行 */
  overflow: hidden; /* 超出隐藏 */
  text-overflow: ellipsis; /* 显示省略号 */
}

/* 多行省略（WebKit 浏览器） */
.multi-line {
  display: -webkit-box; /* 弹性盒模型 */
  -webkit-line-clamp: 3; /* 限制3行 */
  -webkit-box-orient: vertical; /* 垂直排列 */
  overflow: hidden;
}
```

> 💡 **记忆口诀**：单行省略三件套——**不换行、超出藏、省略号**。

> 🔴 **重难点**：`text-overflow: ellipsis` 必须配合 `white-space: nowrap` 和 `overflow: hidden` 才能生效，三者缺一不可！

### ✅ 本节回顾

- [x] 能用至少两种方式设置颜色
- [x] 会写字体栈，了解中文字体的回退策略
- [x] 掌握 `text-align`、`text-decoration`、`letter-spacing` 的用法
- [x] 能实现单行文字省略效果

### 📝 自测题

**1. 以下哪个颜色值带有透明度？**

- A. `#ff0000`
- B. `rgb(255, 0, 0)`
- C. `rgba(255, 0, 0, 0.5)`
- D. `red`

**2. 字体栈 `"Arial", "Microsoft YaHei", sans-serif` 的含义是？**

- A. 同时使用三种字体
- B. 优先用 Arial，没有就用微软雅黑，再没有就用系统默认无衬线字体
- C. 只有 Arial 生效
- D. 三种字体随机显示

**3. 判断正误：`text-overflow: ellipsis` 单独使用就能让文字显示省略号。**

- A. 正确
- B. 错误（需要配合 `white-space: nowrap` 和 `overflow: hidden`）

**4. 以下代码的效果是？**

```css
a {
  text-decoration: none;
}
```

- A. 链接文字变大
- B. 链接去掉下划线
- C. 链接变成斜体
- D. 链接变成红色

<details>
<summary>点击查看答案</summary>

1. **C**（RGBA 的 A 就是 Alpha 透明度通道）
2. **B**（字体栈是回退机制，从左到右依次尝试）
3. **B**（三件套缺一不可）
4. **B**（`text-decoration: none` 去掉下划线）

</details>

### ✏️ 动手练习

**练习 1：创建一个段落，设置文字颜色为深蓝 `#2c3e50`，字号 `18px`，行高 `1.8`**

```html
<p class="article">这是第一段练习文字，演示基本的文字样式设置。</p>
```

```css
.article {
  color: #2c3e50; /* 深蓝色 */
  font-size: 18px; /* 字号 */
  line-height: 1.8; /* 行高 */
}
```

**练习 2：给标题设置居中、大写、增加字间距**

```html
<h1 class="title">hello css</h1>
```

```css
.title {
  text-align: center; /* 居中对齐 */
  text-transform: uppercase; /* 全大写 */
  letter-spacing: 4px; /* 字间距 */
  font-size: 24px;
  color: #2c3e50;
}
```

**练习 3：实现一个固定宽度 200px 的容器，内部文字超出时显示省略号**

```html
<div class="card">
  <p class="card__title">这是一个非常非常长的标题文字，超出了容器的宽度</p>
</div>
```

```css
.card {
  width: 200px; /* 固定宽度 */
  background: #f5f5f5;
  padding: 16px;
  border-radius: 8px;
}

.card__title {
  /* 单行省略三件套 */
  white-space: nowrap; /* 不换行 */
  overflow: hidden; /* 超出隐藏 */
  text-overflow: ellipsis; /* 显示省略号 */
  margin: 0; /* 清除默认 margin */
}

/* 多行省略（适用于 WebKit 浏览器） */
.card__desc {
  display: -webkit-box;
  -webkit-line-clamp: 2; /* 限制2行 */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

**完整示例代码：**

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>第二阶段练习</title>
    <style>
      /* 全局盒模型设置 */
      *,
      *::before,
      *::after {
        box-sizing: border-box;
      }

      body {
        font-family: "Microsoft YaHei", sans-serif;
        padding: 20px;
        background: #f0f2f5;
      }

      /* 练习1：基本文字样式 */
      .article {
        color: #2c3e50;
        font-size: 18px;
        line-height: 1.8;
        margin-bottom: 20px;
      }

      /* 练习2：标题样式 */
      .title {
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 4px;
        font-size: 24px;
        color: #2c3e50;
        margin-bottom: 20px;
      }

      /* 练习3：单行省略 */
      .card {
        width: 200px;
        background: #fff;
        padding: 16px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
      }

      .card__title {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        margin: 0;
        font-size: 14px;
        color: #333;
      }

      /* 练习3扩展：多行省略 */
      .card__desc {
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        text-overflow: ellipsis;
        margin: 10px 0 0 0;
        font-size: 13px;
        color: #666;
        line-height: 1.5;
      }
    </style>
  </head>
  <body>
    <!-- 练习1 -->
    <p class="article">
      这是第一段练习文字，演示基本的文字样式设置。行高1.8让文字更易阅读。
    </p>

    <!-- 练习2 -->
    <h1 class="title">hello css</h1>

    <!-- 练习3 -->
    <div class="card">
      <p class="card__title">这是一个非常非常长的标题文字，超出了容器的宽度</p>
      <p class="card__desc">
        这是一段比较长的描述文字，可以显示两行省略效果，超过两行的部分会被隐藏并显示省略号。
      </p>
    </div>
  </body>
</html>
```

> 💡 **提示**：保存为 `.html` 文件直接在浏览器中打开，即可查看效果。尝试修改颜色、字号等数值，观察变化！
