---
title: "CSS 入门指南 · 第五阶段：背景与装饰 —— 让页面更丰富"
tags:
  - programming
  - css
created: 2026-09-10
updated: 2026-10-01
---

# 第五阶段：背景与装饰 —— 让页面更丰富

> 📚 本文是 [[topics/programming/Web/css|CSS 入门指南]] 的第 5 / 10 章。 上一章：[[topics/programming/Web/css/stage-04-selectors|第四阶段：选择器]] · 下一章：[[topics/programming/Web/css/stage-06-layout|第六阶段：布局系统]]


> 🎯 **本节目标**：能设置背景色、背景图、阴影和渐变，让页面更有层次感。

> 本节示例基于以下 HTML 结构：

```html
<div class="hero">全屏背景图区域</div>

<div class="card">
  <h3>卡片标题</h3>
  <p>卡片内容文字</p>
  <button class="btn-gradient">渐变按钮</button>
</div>
```

### 🍎 生活比喻：背景就像房间装修

- **背景颜色** = 刷墙漆（`background-color: blue` = 刷蓝墙）
- **背景图片** = 贴壁纸（`background-image` = 贴一张图在墙上）
- **背景重复** = 壁纸怎么铺（`no-repeat` = 只贴一张，`repeat` = 铺满整个墙）
- **背景位置** = 挂画的位置（`center` = 挂在正中间）
- **阴影** = 物体投下的影子
- **渐变** = 从一种颜色平滑过渡到另一种颜色（就像日落时天空的颜色变化）

### 5.1 背景颜色

```css
background-color: #f5f5f5;
background-color: rgba(0, 0, 0, 0.5); /* 半透明黑色 */
```

> 💡 **半透明背景技巧**：用 `rgba(255,255,255,0.9)` 做毛玻璃感遮罩，比纯色更高级。

### 5.2 背景图片

```css
background-image: url("bg.jpg"); /* 路径相对于 CSS 文件，不是 HTML 文件 */
background-repeat: no-repeat; /* repeat、repeat-x、repeat-y */
background-position: center center; /* 水平 垂直 */
background-size: cover; /* cover、contain、具体宽高 */
background-attachment: fixed; /* 固定背景（视差效果） */
```

| `background-size` 值 | 效果                                   | 生活比喻                               |
| -------------------- | -------------------------------------- | -------------------------------------- |
| `cover`              | 等比缩放，完全覆盖容器（可能裁剪图片） | 把照片放大到铺满整个相框，边缘可能裁掉 |
| `contain`            | 等比缩放，图片完整显示（可能有留白）   | 把照片完整放进相框，留白边             |
| `100% 100%`          | 拉伸填满（可能变形）                   | 强行拉变形铺满                         |
| `auto`               | 保持原始尺寸                           | 原样展示                               |

> 🔴 **重难点**：`cover` 和 `contain` 的区别是初学者最常搞混的！
>
> - **cover** = 铺满容器，图片可能被裁剪（像放大的照片）
> - **contain** = 图片完整，容器可能有留白（像完整的小照片放进大框）

### 5.3 背景简写

```css
background: #f5f5f5 url("bg.jpg") no-repeat center/cover;
/*         颜色    图片           重复    位置/大小   */
```

> ⚠️ **注意**：简写时 `background-size` 必须紧跟在 `background-position` 后面，用 `/` 分隔。

### 5.4 阴影效果

```css
/* 盒子阴影：x偏移 y偏移 模糊半径 扩散半径 颜色 */
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
box-shadow:
  0 2px 4px rgba(0, 0, 0, 0.1),
  0 8px 16px rgba(0, 0, 0, 0.1); /* 多层阴影 */
box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1); /* 内阴影 */

/* 文字阴影 */
text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
```

> 🍎 **比喻理解**：`box-shadow` 的参数就像描述一个影子：
>
> - `0` = 影子在正下方（不左右偏）
> - `4px` = 影子向下偏移 4px
> - `8px` = 影子模糊程度（越大越模糊）
> - `rgba(0,0,0,0.1)` = 黑色的、很淡的影子

> 💡 **阴影层次感技巧**：
>
> - 轻微悬浮：`box-shadow: 0 2px 8px rgba(0,0,0,0.1)`
> - 明显悬浮：`box-shadow: 0 8px 24px rgba(0,0,0,0.15)`

### 5.5 渐变背景

```css
/* 线性渐变 */
background: linear-gradient(to right, red, blue);
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* 径向渐变 */
background: radial-gradient(circle at center, red, blue);

/* 重复渐变 */
background: repeating-linear-gradient(
  45deg,
  #f0f0f0,
  #f0f0f0 10px,
  #fff 10px,
  #fff 20px
);
```

> 🍎 **比喻理解**：线性渐变就像日落时天空的颜色变化——从左到右（`to right`）或者从左上到右下（`135deg`）。

> 💡 **渐变方向写法**：
>
> - `to right`：从左到右
> - `to bottom right`：从左上到右下
> - `135deg`：角度写法，0deg 是从下到上，顺时针增加

### ✅ 本节回顾

- [x] 会用 `background` 简写设置背景
- [x] 理解 `background-size: cover` 和 `contain` 的区别
- [x] 会写 `box-shadow` 和 `text-shadow`
- [x] 能创建线性渐变背景

### 📝 自测题

**1. `background-size: cover` 的效果是？**

- A. 图片完整显示，可能有留白
- B. 图片铺满容器，可能被裁剪
- C. 图片拉伸变形
- D. 保持原始尺寸

**2. `box-shadow: 2px 4px 6px rgba(0,0,0,0.3)` 中，第二个值 `4px` 表示？**

- A. 水平偏移
- B. 垂直偏移
- C. 模糊半径
- D. 扩散半径

**3. 以下哪个是线性渐变的正确写法？**

- A. `gradient(linear, red, blue)`
- B. `linear-gradient(to right, red, blue)`
- C. `background-gradient(red, blue)`
- D. `linear-color(red, blue)`

<details>
<summary>点击查看答案</summary>

1. **B**（cover 是铺满容器，可能裁剪）
2. **B**（四个值依次是：x偏移、y偏移、模糊半径、颜色）
3. **B**（`linear-gradient` 是正确语法）

</details>

### ✏️ 动手练习

1. 给卡片设置白色背景 + 轻微阴影，悬停时阴影加深
2. 创建一个全屏背景图，要求不变形且居中（用 `cover`）
3. 用渐变创建一个紫色到蓝色的按钮背景

**参考实现：**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CSS 动手练习</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Microsoft YaHei', sans-serif;
    }

    /* ========== 练习 1：卡片白色背景 + 阴影 + 悬停加深 ========== */
    .card {
      width: 300px;
      padding: 24px;
      margin: 40px auto;
      background-color: #fff;
      border-radius: 12px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
      transition: box-shadow 0.3s ease;
      text-align: center;
    }

    .card:hover {
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    }

    .card h3 {
      margin-bottom: 12px;
      color: #333;
    }

    .card p {
      color: #666;
      line-height: 1.6;
    }

    /* ========== 练习 2：全屏背景图 cover 居中 ========== */
    .hero {
      width: 100%;
      height: 100vh;
      background-image: url('https://picsum.photos/1920/1080');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .hero h1 {
      color: #fff;
      font-size: 48px;
      text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
    }

    /* ========== 练习 3：紫色到蓝色的渐变按钮 ========== */
    .btn-gradient {
      display: block;
      margin: 40px auto;
      padding: 14px 36px;
      font-size: 16px;
      color: #fff;
      border: none;
      border-radius: 25px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .btn-gradient:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }

    .btn-gradient:active {
      transform: translateY(0);
    }

    /* 分隔线 */
    .divider {
      height: 2px;
      background: #eee;
      margin: 20px 0;
    }
  </style>
</head>
<body>

  <!-- 练习 1：卡片 -->
  <div class="card">
    <h3>精美卡片</h3>
    <p>白色背景配合轻微阴影，鼠标悬停时阴影会加深，带来自然的层次感。</p>
  </div>

  <div class="divider"></div>

  <!-- 练习 2：全屏背景图 -->
  <div class="hero">
    <h1>全屏背景图</h1>
  </div>

  <div class="divider"></div>

  <!-- 练习 3：渐变按钮 -->
  <button class="btn-gradient">紫色渐变按钮</button>

</body>
</html>
```

**实现要点说明：**

| 练习 | 核心属性 | 说明 |
|:---|:---|:---|
| 卡片阴影 | `box-shadow` + `:hover` | 使用 `transition` 让阴影变化更平滑 |
| 全屏背景图 | `background-size: cover` | 配合 `background-position: center` 实现不变形居中 |
| 渐变按钮 | `linear-gradient(135deg, #667eea, #764ba2)` | 135° 对角线渐变，悬停时添加 glow 效果 |
