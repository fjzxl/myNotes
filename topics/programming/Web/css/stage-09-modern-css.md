---
title: "CSS 入门指南 · 第九阶段：现代 CSS 进阶特性"
tags:
  - programming
  - css
created: 2026-09-10
updated: 2026-10-01
---

# 第九阶段：现代 CSS 进阶特性

> 📚 本文是 [[topics/programming/Web/css|CSS 入门指南]] 的第 9 / 10 章。 上一章：[[topics/programming/Web/css/stage-08-animation|第八阶段：动画与交互]] · 下一章：[[topics/programming/Web/css/stage-10-architecture|第十阶段：CSS 架构与工程化]]


> 🎯 **本节目标**：掌握 CSS 变量、常用函数和现代属性。
>
> 本节现代 CSS 特性示例基于以下 HTML 结构：
>
> ```html
> <button class="button">主题色按钮</button>
>
> <div class="card">
>   <h3>自适应标题</h3>
>   <p>这段文字在一个响应式容器中</p>
> </div>
>
> <div class="avatar">圆形裁剪</div>
> ```

### 🍎 生活比喻：CSS 变量就像"全局配色方案"

想象你负责装修一栋大楼：

- 如果没有变量 = 每间房间刷墙时都要说"用那个蓝色"——万一要换颜色，得一间一间重新刷
- 有了 CSS 变量 = 先定义"主题蓝 = #3498db"，所有房间引用这个名称——换颜色时只改定义处，全局生效

### 9.1 CSS 自定义属性（变量）

```css
/* 定义全局变量 */
:root {
  --primary-color: #3498db;
  --spacing-unit: 8px;
  --border-radius: 4px;
}

/* 使用变量 */
.button {
  background-color: var(--primary-color);
  padding: var(--spacing-unit) calc(var(--spacing-unit) * 2);
  border-radius: var(--border-radius);
}

/* 局部变量 */
.card {
  --card-padding: 20px;
  padding: var(--card-padding);
}

/* 备用值 */
.element {
  color: var(--undefined-var, black); /* 变量不存在时使用黑色 */
}
```

> 🍎 **比喻理解**：
>
> - `:root` = 大楼的总设计图（全局生效）
> - `.card` 里的 `--card-padding` = 某个房间的特殊要求（只在这个房间生效）
> - `var(--color, black)` = "如果有这个颜色就用，没有就用黑色兜底"

> 💡 **变量优势**：
>
> - 一处修改，全局生效（换主题色特别方便）
> - 可以在运行时通过 JS 修改
> - 遵循 CSS 级联规则，可局部覆盖

```js
// JavaScript 修改变量（实现换肤功能）
document.documentElement.style.setProperty("--primary-color", "#e74c3c");
```

### 9.2 CSS 函数

#### 函数详解

| 函数 | 说明 | 语法 | 参数说明 | 比喻 |
|------|------|------|----------|------|
| `calc()` | 四则运算 | `calc(expr)` | 支持 `+`、`-`、`*`、`/` 混合运算 | 计算器 |
| `min()` | 取最小值 | `min(a, b, ...)` | 从多个值中取最小的 | 选两个数中较小的 |
| `max()` | 取最大值 | `max(a, b, ...)` | 从多个值中取最大的 | 选两个数中较大的 |
| `clamp()` | 范围限制 | `clamp(min, ideal, max)` | 限制值在 min~max 范围内 | 限速器（不低于、不超过） |
| `minmax()` | Grid 轨道范围 | `minmax(min, max)` | 定义轨道尺寸的最小和最大值 | 区间范围 |
| `repeat()` | 重复轨道 | `repeat(n, value)` | 重复某个值 n 次 | 批量复制 |
| `var()` | CSS 变量 | `var(--name, fallback)` | 引用自定义属性，可选默认值 | 引用变量 |

#### calc() — 四则运算

> 场景：让子元素宽度比父容器少 40px（常用于固定宽度 sidebar + 自适应主内容）

```css
/* 计算父容器宽度减去固定值 */
width: calc(100% - 40px);

/* 固定高度减去上下 padding */
height: calc(100vh - 80px);

/* 混合运算：100% 减去左右各 20px，再除以 2 */
width: calc((100% - 40px) / 2);
```

> ⚠️ **注意**：`+` 和 `-` 运算符两侧必须留空格！
>
> ```css
> /* ✅ 正确：运算符两侧有空格 */
> width: calc(100% - 40px);
>
> /* ❌ 错误：减号两侧无空格会被解析为负数 */
> width: calc(100%-40px);
> ```

#### min() — 取最小值

> 场景：宽度最多 800px，在小屏幕上自动占满 100%

```css
/* 宽度取 100% 和 800px 中的较小值 */
/* 小屏幕(<800px)：占满屏幕 */
/* 大屏幕(>=800px)：固定 800px */
width: min(100%, 800px);
```

#### max() — 取最大值

> 场景：字体大小至少 16px，但随屏幕变大而增大

```css
/* 字号取 16px 和 2vw 中的较大的值 */
/* 小屏幕：至少 16px */
/* 大屏幕：随 vw 增大而增大 */
font-size: max(16px, 2vw);
```

#### clamp() — 范围限制（三参数）

> 场景：响应式字体，最小 1rem，最大 2rem，中间随屏幕缩放

```css
/* 语法：clamp(最小值, 首选值, 最大值) */
font-size: clamp(1rem, 2.5vw, 2rem);
```

**效果解析**：

| 屏幕宽度 | `2.5vw` 计算值 | 最终取值 | 说明 |
|----------|----------------|----------|------|
| 小屏幕（375px） | 9.375px | **1rem**（取最小值） | 不小于最小值 |
| 中屏幕（900px） | 22.5px | **22.5px**（取首选值） | 在范围内，用首选值 |
| 大屏幕（1440px） | 36px | **2rem**（取最大值） | 不超过最大值 |

> 💡 **记忆口诀**：`clamp(最小, 理想, 最大)` = "不要小于最小，也不要超过最大"

**常用场景**：

```css
/* 响应式宽度容器 */
width: clamp(300px, 80vw, 1200px);

/* 响应式内边距 */
padding: clamp(16px, 4vw, 48px);

/* 响应式圆角 */
border-radius: clamp(4px, 1vw, 16px);
```

#### minmax() — Grid 轨道范围（用于 Grid 布局）

> 场景：Grid 列宽最少 200px，最多 1fr（平分剩余空间）

```css
.grid {
  display: grid;
  /* 3 列，每列宽度在 200px ~ 1fr 之间 */
  grid-template-columns: repeat(3, minmax(200px, 1fr));
  gap: 20px;
}
```

**效果**：如果容器宽度 900px，三列平分各 300px；如果容器宽度 1200px，三列平分各 400px（始终 >= 200px）。

#### repeat() — 重复轨道（用于 Grid 布局）

> 场景：快速创建多列网格

```css
.grid {
  display: grid;
  /* 4 列，每列等宽 */
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

/* 配合 minmax：自动填充列，最小 200px，最大 1fr */
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}
```

> 💡 `auto-fill` vs `auto-fit`：
> - `auto-fill`：如果列数不足，空白区域留空
> - `auto-fit`：如果列数不足，列会自动拉伸填满空白区域

#### var() — CSS 变量

> 场景：定义主题色，全局引用，一处修改全部生效

```css
/* 定义 */
:root {
  --primary-color: #3498db;
  --spacing: 16px;
  --radius: 8px;
}

/* 使用 */
.button {
  background-color: var(--primary-color);
  padding: var(--spacing);
  border-radius: var(--radius);
}

/* 带默认值的引用（变量未定义时使用） */
.text {
  color: var(--text-color, #333); /* text-color 未定义时使用 #333 */
}
```

> 💡 **使用场景**：主题换肤、组件库 tokens、统一管理间距/颜色等设计决策。

### 9.3 裁剪与遮罩

```css
/* 裁剪路径 */
.clip-circle {
  /* 50% 是半径（基于元素宽/高较小者），非直径 */
  clip-path: circle(50%);
}
/* 正圆裁剪建议配合 aspect-ratio: 1 / 1 或等宽高容器使用 */
.clip-polygon {
  clip-path: polygon(0 0, 100% 0, 100% 80%, 0 100%);
}

/* 遮罩 */
.mask {
  -webkit-mask-image: linear-gradient(
    to bottom,
    black,
    transparent
  ); /* Safari 兼容 */
  mask-image: linear-gradient(to bottom, black, transparent);
}
```

> 🍎 **比喻理解**：
>
> - `clip-path` = 用剪刀把照片剪成特定形状（圆形、多边形）
> - `mask` = 给照片盖上一层纱布，默认根据遮罩层的 **alpha 通道**（透明度）决定显示程度——遮罩越不透明，照片显示越清晰；遮罩越透明，照片越被隐藏。设置 `mask-mode: luminance` 时才根据亮度（黑/白/灰）决定。

### ✅ 本节回顾

- [x] 会定义和使用 CSS 变量
- [x] 会用 `calc()`、`clamp()`、`min()`、`max()`
- [x] 了解 `clip-path` 的作用

### 📝 自测题

**1. CSS 变量的正确定义方式是？**

- A. `$primary-color: blue;`
- B. `--primary-color: blue;`
- C. `@primary-color: blue;`
- D. `var primary-color: blue;`

**2. 使用 CSS 变量的正确方式是？**

- A. `color: --primary-color;`
- B. `color: var(--primary-color);`
- C. `color: $(--primary-color);`
- D. `color: get(--primary-color);`

**3. `calc(100% - 40px)` 的作用是？**

- A. 报错，不能混合单位
- B. 计算宽度为父容器宽度的 100% 减去 40px
- C. 固定 60px
- D. 固定 100px

<details>
<summary>点击查看答案</summary>

1. **B**（CSS 变量以 `--` 开头）
2. **B**（用 `var()` 函数引用变量）
3. **B**（calc 支持混合单位计算）

</details>

### ✏️ 动手练习

1. 定义一套主题色变量（主色、辅色、文字色、背景色），应用到按钮和卡片上
2. 用 `clamp()` 实现一个响应式容器宽度（最小 300px，最大 1200px，中间 80vw）
