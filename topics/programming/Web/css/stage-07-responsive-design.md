---
title: "CSS 入门指南 · 第七阶段：响应式设计 —— 适配不同屏幕"
tags:
  - programming
  - css
created: 2026-09-10
updated: 2026-10-01
---

# 第七阶段：响应式设计 —— 适配不同屏幕

> 📚 本文是 [[topics/programming/Web/css|CSS 入门指南]] 的第 7 / 10 章。 上一章：[[topics/programming/Web/css/stage-06-layout|第六阶段：布局系统]] · 下一章：[[topics/programming/Web/css/stage-08-animation|第八阶段：动画与交互]]


> 🎯 **本节目标**：理解响应式设计概念，掌握媒体查询和常用断点，能写出移动优先的样式。

### 🍎 生活比喻：响应式就像"液体倒入不同容器"

同一瓶水，倒进杯子、碗、盆子里，形状会自适应容器——响应式设计就是让你的网页像水一样，在手机、平板、电脑上都能"自然流动"成合适的形状。

```
同一套代码：
┌──────────┐    ┌──────────────┐    ┌──────────────────┐
│   📱     │    │      📱      │    │        💻        │
│  手机    │ →  │    平板      │ →  │      桌面        │
│ 单列布局 │    │  两列布局    │    │    三列布局       │
│ 小字号   │    │  中等字号    │    │    大字号        │
└──────────┘    └──────────────┘    └──────────────────┘
```

> 响应式布局需要先在 HTML 中设置视口，然后基于相同的结构用媒体查询适配不同屏幕：
>
> ```html
> <!DOCTYPE html>
> <html lang="zh-CN">
>   <head>
>     <meta charset="UTF-8" />
>     <meta name="viewport" content="width=device-width, initial-scale=1.0" />
>     <title>响应式页面</title>
>     <link rel="stylesheet" href="style.css" />
>   </head>
>   <body>
>     <div class="container">
>       <div class="card">卡片 1</div>
>       <div class="card">卡片 2</div>
>       <div class="card">卡片 3</div>
>     </div>
>   </body>
> </html>
> ```

### 7.1 媒体查询（Media Queries）

```css
/* 语法 */
@media 媒体类型 and (条件) {
  /* 满足条件时生效的样式 */
}

/* 常见写法 */
@media (max-width: 767px) {
  /* 屏幕宽度 ≤ 767px 时生效 */
  .sidebar {
    display: none;
  }
}

@media (min-width: 768px) {
  /* 屏幕宽度 ≥ 768px 时生效 */
  .sidebar {
    display: block;
  }
}
```

> 🍎 **比喻理解**：媒体查询就像"条件判断"——
>
> - `@media (min-width: 768px)` = "如果屏幕宽度大于等于 768px，就执行这些样式"
> - 就像"如果房间大于 20 平米，就放一个大沙发"

#### 🔴 重难点：移动优先 vs 桌面优先

| 策略         | 写法                                | 比喻                       | 推荐度                         |
| ------------ | ----------------------------------- | -------------------------- | ------------------------------ |
| **移动优先** | 先写小屏样式，再用 `min-width` 叠加 | 先设计小房子，再扩建大房子 | ✅ **强烈推荐**（渐进增强）    |
| **桌面优先** | 先写大屏样式，再用 `max-width` 覆盖 | 先设计大房子，再拆成小房子 | ⚠️ 视场景而定（B端系统可考虑） |

```css
/* 移动优先写法（推荐） */
.card {
  /* 手机：全宽。块级元素默认就是 100%，此行可省略 */
  /* 如果显式设置 width: 100% 且有 padding，务必配合 box-sizing: border-box */
}

@media (min-width: 576px) {
  .card {
    width: 50%; /* 平板：半宽 */
  }
}

@media (min-width: 992px) {
  .card {
    width: 33.33%; /* 桌面：三分之一 */
  }
}
```

> 💡 **为什么推荐移动优先**：
>
> - 手机用户占比更高
> - CSS 默认就是无媒体查询的样式，从小屏开始写更自然
> - `min-width` 叠加比 `max-width` 覆盖更符合直觉

### 7.2 常用断点

| 名称           | 宽度范围       | 设备            | 比喻   |
| -------------- | -------------- | --------------- | ------ |
| 超小屏         | < 576px        | 手机竖屏        | 小口袋 |
| 小屏（平板）   | 576px - 767px  | 手机横屏/小平板 | 书包   |
| 中屏（笔记本） | 768px - 991px  | 大平板/小笔记本 | 公文包 |
| 大屏（桌面）   | 992px - 1199px | 普通桌面        | 行李箱 |
| 超大屏         | ≥ 1200px       | 大屏桌面        | 集装箱 |

> 💡 **提示**：断点数值参考 Bootstrap 5，常用组合是 `576px`、`768px`、`992px`、`1200px`。相邻断点首尾相接（如 576px-767px），没有重叠。

### 7.3 响应式布局技巧

```css
/* 流式图片：不超出容器 */
img {
  max-width: 100%;
  height: auto;
}

/* 弹性容器 */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* 响应式文字：最小、首选、最大 */
h1 {
  font-size: clamp(1.5rem, 4vw, 3rem);
}

/* 响应式容器：防止 clamp 导致溢出 */
.container {
  width: min(100%, clamp(300px, 80vw, 1200px));
  box-sizing: border-box;
}

/* 响应式 Grid */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

/* 响应式 Flexbox */
.flex-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.flex-item {
  flex: 0 1 300px; /* 不 grow、可 shrink、基础 300px，避免换行后拉伸 */
}
```

#### 🔴 重难点：`clamp()` 函数

`clamp(最小值, 首选值, 最大值)` —— 响应式神器！

> 🍎 **比喻理解**：就像汽车的定速巡航——
>
> - 最快速度 120km/h（最大值）
> - 最慢速度 60km/h（最小值）
> - 中间根据路况自动调整（首选值）

```css
/* 字体大小：最小 18px，按视口 4% 缩放，最大不超过 32px */
h1 {
  font-size: clamp(18px, 4vw, 32px);
}

/* 容器宽度：最小 300px，按视口 80% 缩放，最大不超过 1200px */
.container {
  /* ⚠️ clamp() 计算出的宽度若大于父容器会溢出，配合 min() 更安全 */
  width: min(100%, clamp(300px, 80vw, 1200px));
  box-sizing: border-box;
}
```

### 7.4 视口设置

在 HTML `<head>` 中添加：

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

| 值                   | 含义                 | 比喻                   |
| -------------------- | -------------------- | ---------------------- |
| `width=device-width` | 视口宽度等于设备宽度 | 窗户多大房间就多大     |
| `initial-scale=1.0`  | 初始缩放比例为 1     | 正常大小，不放大不缩小 |

> ⚠️ **不加 viewport 的后果**：手机浏览器会按桌面宽度渲染页面，导致文字极小，需要手动缩放。就像把一张大海报强行塞进小相框！

### ✅ 本节回顾

- [x] 理解移动优先和桌面优先的区别，推荐移动优先
- [x] 会写 `@media (min-width: 768px)` 媒体查询
- [x] 知道常用断点范围
- [x] 会设置 viewport meta 标签
- [x] 会用 `clamp()` 实现响应式文字

### 📝 自测题

**1. 移动优先的媒体查询应该用什么条件？**

- A. `max-width`
- B. `min-width`
- C. `max-height`
- D. `min-height`

**2. `clamp(16px, 3vw, 24px)` 的含义是？**

- A. 固定 16px
- B. 固定 24px
- C. 最小 16px，按 3vw 缩放，最大 24px
- D. 最小 3vw，按 16px 缩放，最大 24px

**3. 不加 viewport meta 标签的后果是？**

- A. 页面无法加载
- B. 手机浏览器按桌面宽度渲染，文字很小
- C. CSS 不生效
- D. 没有影响

**4. 以下哪个断点范围对应"平板"？**

- A. < 576px
- B. 576px - 768px
- C. 768px - 992px
- D. > 1200px

<details>
<summary>点击查看答案</summary>

1. **B**（移动优先用 min-width 叠加）
2. **C**（clamp(最小, 首选, 最大)）
3. **B**（手机会按桌面宽度渲染）
4. **B**（576px-767px 是平板范围）

</details>

### ✏️ 动手练习

1. 创建一个卡片，手机全宽、平板两列、桌面三列（用媒体查询）
2. 用 `clamp()` 设置一个标题，手机 18px、桌面 32px、中间平滑过渡
3. 在浏览器开发者工具的设备模拟器中测试你的响应式页面

<details>
<summary>点击查看参考实现</summary>

**练习 1：响应式卡片布局**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>响应式卡片</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      padding: 20px;
      background: #f0f2f5;
      font-family: "Microsoft YaHei", sans-serif;
    }

    h1 {
      text-align: center;
      margin-bottom: 30px;
      /* 练习2：clamp() 实现响应式字体 */
      font-size: clamp(18px, 4vw, 32px);
    }

    /* 卡片容器 - 移动优先 */
    .card-list {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
    }

    .card {
      /* 手机：默认全宽（100%） */
      width: 100%;
      background: white;
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s, box-shadow 0.3s;
    }

    .card:hover {
      transform: translateY(-4px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    }

    .card h3 {
      margin-bottom: 12px;
      color: #2c3e50;
    }

    .card p {
      color: #666;
      line-height: 1.6;
      font-size: 14px;
    }

    .card .tag {
      display: inline-block;
      padding: 4px 12px;
      background: #e8f4fd;
      color: #3498db;
      border-radius: 20px;
      font-size: 12px;
      margin-top: 12px;
    }

    /* 平板：两列 */
    @media (min-width: 576px) {
      .card {
        width: calc(50% - 10px); /* 50% 减去 gap 的一半 */
      }
    }

    /* 桌面：三列 */
    @media (min-width: 992px) {
      .card {
        width: calc(33.333% - 14px); /* 三等分减去两个 gap */
      }
    }
  </style>
</head>
<body>
  <h1>响应式卡片练习</h1>

  <div class="card-list">
    <div class="card">
      <h3>卡片一</h3>
      <p>这是卡片内容区域，可以放文字描述、产品介绍或任何内容。</p>
      <span class="tag">标签</span>
    </div>

    <div class="card">
      <h3>卡片二</h3>
      <p>这是卡片内容区域，可以放文字描述、产品介绍或任何内容。</p>
      <span class="tag">标签</span>
    </div>

    <div class="card">
      <h3>卡片三</h3>
      <p>这是卡片内容区域，可以放文字描述、产品介绍或任何内容。</p>
      <span class="tag">标签</span>
    </div>

    <div class="card">
      <h3>卡片四</h3>
      <p>这是卡片内容区域，可以放文字描述、产品介绍或任何内容。</p>
      <span class="tag">标签</span>
    </div>

    <div class="card">
      <h3>卡片五</h3>
      <p>这是卡片内容区域，可以放文字描述、产品介绍或任何内容。</p>
      <span class="tag">标签</span>
    </div>

    <div class="card">
      <h3>卡片六</h3>
      <p>这是卡片内容区域，可以放文字描述、产品介绍或任何内容。</p>
      <span class="tag">标签</span>
    </div>
  </div>
</body>
</html>
```

**练习 2：clamp() 响应式字体**

```css
/* clamp() 语法：clamp(最小值, 首选值, 最大值) */

/* 标题字体：最小 18px，最大 32px，中间根据视口宽度平滑过渡 */
.responsive-title {
  font-size: clamp(18px, 4vw + 1rem, 32px);
  /* 解释：
   * 18px = 最小值（屏幕很小时不再缩小）
   * 4vw + 1rem = 首选值（随视口宽度增加而增大）
   * 32px = 最大值（屏幕很大时不再增大）
   */
}

/* 另一种常见写法：只用 vw 来计算 */
.section-title {
  font-size: clamp(1.125rem, 2.5vw, 2rem);
  /* 1.125rem ≈ 18px, 2rem = 32px */
}

/* 段落文字也适用 */
.paragraph {
  font-size: clamp(14px, 1.5vw + 0.75rem, 18px);
  line-height: clamp(1.4, 2vw + 1.2, 1.8);
}
```

**完整示例（包含 clamp 字体）：**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>clamp() 响应式字体</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      padding: 20px;
      background: #f5f6fa;
      font-family: "Microsoft YaHei", sans-serif;
    }

    .container {
      max-width: 800px;
      margin: 0 auto;
    }

    /* clamp() 实现响应式标题 */
    .main-title {
      font-size: clamp(24px, 5vw + 1rem, 48px);
      font-weight: 700;
      color: #2c3e50;
      margin-bottom: 20px;
      text-align: center;
    }

    .subtitle {
      font-size: clamp(14px, 2vw + 0.5rem, 20px);
      color: #666;
      text-align: center;
      margin-bottom: 40px;
    }

    .card {
      background: white;
      border-radius: 12px;
      padding: clamp(16px, 3vw + 1rem, 32px);
      margin-bottom: 20px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }

    .card h2 {
      /* 卡片标题也用 clamp */
      font-size: clamp(16px, 2vw + 0.5rem, 24px);
      color: #2c3e50;
      margin-bottom: 12px;
    }

    .card p {
      /* 段落文字响应式 */
      font-size: clamp(13px, 1.5vw + 0.5rem, 16px);
      color: #555;
      line-height: 1.7;
    }

    .highlight {
      /* 强调文字使用 clamp */
      font-size: clamp(12px, 1.2vw + 0.5rem, 14px);
      color: #3498db;
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1 class="main-title">响应式字体练习</h1>
    <p class="subtitle">使用 clamp() 实现平滑过渡的响应式字体</p>

    <div class="card">
      <h2>什么是 clamp()</h2>
      <p>
        <code>clamp()</code> 是一个 CSS 函数，接收三个值：
        <code>clamp(最小值, 首选值, 最大值)</code>。
        当首选值在最小值和最大值之间时，元素会呈现首选值；
        当视口缩小到一定程度时，元素会固定在最小值；
        当视口放大时，元素会固定在最大值。
      </p>
      <p class="highlight">
        💡 clamp() 可以在不使用媒体查询的情况下实现响应式效果
      </p>
    </div>

    <div class="card">
      <h2>响应式布局</h2>
      <p>
        除了字体，clamp() 还可以用于任何支持长度的属性，
        如 padding、margin、border-radius 等。
        结合媒体查询使用效果更好。
      </p>
    </div>
  </div>
</body>
</html>
```

**练习 3：开发者工具设备模拟器使用**

1. 打开 Chrome 开发者工具（F12 或 Ctrl+Shift+I）
2. 点击左上角的 **设备切换按钮** 📱（或按 Ctrl+Shift+M）
3. 在顶部设备选择器中选择预设设备：
   - **iPhone SE** - 测试手机布局
   - **iPad** - 测试平板布局
   - **Desktop** - 测试桌面布局
4. 或者自定义设备：点击设备选择器旁的 "Edit" 按钮添加自定义设备
5. 拖动设备模拟器边缘调整视口宽度，观察布局变化

</details>
