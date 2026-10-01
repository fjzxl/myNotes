---
title: "CSS 入门指南 · 第六阶段：布局系统 —— 让元素各就各位"
tags:
  - programming
  - css
created: 2026-09-10
updated: 2026-10-01
---

# 第六阶段：布局系统 —— 让元素各就各位

> 📚 本文是 [[topics/programming/Web/css|CSS 入门指南]] 的第 6 / 10 章。 上一章：[[topics/programming/Web/css/stage-05-backgrounds|第五阶段：背景与装饰]] · 下一章：[[topics/programming/Web/css/stage-07-responsive-design|第七阶段：响应式设计]]


> 🎯 **本节目标**：理解文档流、定位、Flexbox 和 Grid，能选择合适的布局方式。
>
> 布局是 CSS 最难也最重要的部分。学习顺序：**正常流 → 定位 → Flexbox → Grid**。
>
> 本节所有布局示例都基于下面这段统一的 HTML 骨架。你可以把不同的 CSS 应用到同一个结构上，观察各种布局效果：
>
> ```html
> <div class="page">
>   <header class="header">顶部导航栏</header>
>
>   <nav class="navbar">
>     <a href="#">首页</a>
>     <a href="#">文章</a>
>     <a href="#">关于</a>
>   </nav>
>
>   <div class="layout">
>     <aside class="sidebar">侧边栏</aside>
>     <main class="main">主内容区</main>
>   </div>
>
>   <div class="cards">
>     <div class="card">卡片 1</div>
>     <div class="card">卡片 2</div>
>     <div class="card">卡片 3</div>
>   </div>
>
>   <footer class="footer">页脚</footer>
> </div>
> ```

### 🍎 生活比喻：布局就像安排座位

- **正常文档流** = 大家随便坐，高个子（块级）一人占一排，矮个子（行内）挤在一起
- **相对定位 relative** = 从座位上站起来，但椅子还占着（原位置保留）
- **绝对定位 absolute** = 直接站到讲台角落（脱离队伍，不占原来的位置）
- **固定定位 fixed** = 站在门口（不管大家怎么动，他都不动）
- **Flexbox** = 军训排队，队长喊"向左看齐"（一维排列）
- **Grid** = 电影院座位，有行有列（二维排列）

### 6.1 正常文档流（Normal Flow）

默认情况下：

- **块级元素**：独占一行，从上到下排列
- **行内元素**：从左到右排列，满行后换行

```
正常文档流示意：
┌─────────────────┐
│     <div>       │  ← 块级：独占一行
│   块级元素       │
├─────────────────┤
│     <div>       │  ← 块级：独占一行
│   块级元素       │
├─────────────────┤
│ <span> <a>      │  ← 行内：并排排列
│  行内  行内      │
└─────────────────┘
```

### 6.2 定位系统（Position）

| 值         | 说明             | 定位参考                              | 生活比喻           |
| ---------- | ---------------- | ------------------------------------- | ------------------ |
| `static`   | 默认，正常文档流 | —                                     | 正常坐着           |
| `relative` | 相对定位         | 相对于自身原位置                      | 站起来但椅子还占着 |
| `absolute` | 绝对定位         | 相对于最近的定位祖先                  | 站到讲台角落       |
| `fixed`    | 固定定位         | 相对于视口（默认）                    | 站在门口不动       |
| `sticky`   | 粘性定位         | 滚动到阈值前像 relative，之后像 fixed | 粘在墙上的便利贴   |

```css
/* 相对定位：原位置保留，视觉偏移 */
.box {
  position: relative;
  top: 10px; /* 向下移 10px */
  left: 20px; /* 向右移 20px */
}

/* 绝对定位：脱离文档流，原位置不保留 */
/* ⚠️ 确保父元素设置了 position: relative，否则元素会飞到页面角落 */
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 0;
  right: 0;
}

/* 固定定位：滚动时不动 */
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
}
/* ⚠️ fixed 元素脱离文档流，下方内容会被遮挡，需要补偿 */
body {
  padding-top: 60px; /* header 的高度 */
}

/* 粘性定位：滚动到顶部时粘住 */
.section-header {
  position: sticky;
  top: 0; /* 滚动到视口顶部时粘住 */
  z-index: 100;
}
```

#### 🔴 重难点：定位上下文（Containing Block）

`absolute` 元素相对于最近的 **定位祖先**（`position` 为非 `static`）。

> ⚠️ **特殊陷阱**：如果祖先设置了 `transform`、`perspective`、`filter`（不为 `none`）或 `will-change: transform`，也会成为定位参考！这甚至会让 `fixed` 元素"失效"。
>
> - `fixed` 默认相对于视口，但若祖先有上述属性，会相对于该祖先。

> 🍎 **比喻理解**：就像小孩找家长——
>
> - 先问爸爸：`position: relative?` → 是的话，就以爸爸为参考
> - 爸爸不是？问爷爷：`position: relative/absolute/fixed?`
> - 一直问到 `html`（祖宗），总会找到一个
>
> ⚠️ **`overflow: hidden` 不一定裁剪 absolute 子元素**——只有当设置它的元素同时是该子元素的定位祖先（包含块）时，裁剪才会生效。

```css
/* 正确做法：父元素设置 relative 作为定位参考 */
.parent {
  position: relative;
}

.child {
  position: absolute;
  top: 10px;
  right: 10px;
}
```

> ⚠️ **常见错误**：
>
> - 给子元素设置 `absolute` 但父元素没有设置定位，导致元素飞到页面角落
> - `fixed` 元素宽度默认收缩为内容宽度，需要手动设置 `width`

**z-index**：控制层叠顺序，数值越大越在上层。只在同一个**层叠上下文**中比较。

> ⚠️ **常见陷阱**：z-index 只在同一层叠上下文中有效！如果父元素创建了新的层叠上下文（如设置了 `opacity: 0.9`、`transform`、`filter`、`isolation: isolate`），子元素的 `z-index: 9999` 也无法突破父元素的层级！
>
> - Flex/Grid 容器的子项即使 `position: static`，设置 `z-index`（非 `auto`）也会创建层叠上下文并生效。

```css
.modal {
  position: fixed;
  z-index: 1000; /* 弹窗要在最上层 */
}

.overlay {
  position: fixed;
  z-index: 999; /* 遮罩层在弹窗下面 */
}
```

### 6.3 浮动（Float）—— 了解即可

```css
float: left; /* 向左浮动 */
float: right; /* 向右浮动 */
```

浮动最初用于**文字环绕图片**，现代布局中已被 Flexbox 和 Grid 取代。了解清除浮动即可：

#### 清除浮动的作用和意义

**为什么要清除浮动？**

浮动元素会**脱离正常的文档流**（半脱离，仍占据位置），导致以下问题：

1. **父元素高度塌陷**：父元素无法感知浮动子元素的高度，导致自身高度变为 0，边框/背景无法正常包裹子元素
2. **后续元素布局混乱**：浮动元素后面的元素会跑上来，被浮动元素覆盖或环绕，破坏正常排版

```
未清除浮动的问题示意：

┌─ 父元素（高度塌陷为0）──────────┐
│ ┌─────┐ ┌─────┐               │
│ │ 浮动│ │ 浮动│ ← 脱离文档流   │
│ └─────┘ └─────┘               │
└───────────────────────────────┘
┌─ 后续元素（跑上来重叠了）────────┐
│ 内容被浮动元素遮挡/环绕...       │
└─────────────────────────────────┘
```

**清除浮动的意义**：

| 作用 | 说明 |
|:---|:---|
| 闭合浮动 | 让父元素重新"包裹"住浮动的子元素，恢复正常高度 |
| 隔离影响 | 阻止浮动对后续兄弟元素的影响，保证后续内容正常排列 |
| 维护文档流 | 让布局回归可预测状态，避免意外的重叠和环绕 |

**现代清除浮动方法（推荐）**：

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
```

> 💡 **使用方式**：给浮动元素的父容器加上 `class="clearfix"` 即可。
>
> 原理：`::after` 伪元素在父元素末尾插入一个空块级元素，并设置 `clear: both`，这个元素会排到浮动元素下方，从而把父元素的高度"撑开"。
>
> 现代项目中，如果你可以控制结构，**优先用 Flexbox 替代 float**，就不再需要处理清除浮动了。

### 6.4 弹性布局（Flexbox）—— 一维布局

> Flexbox 是现代 CSS 布局的基石，**必须熟练掌握**。

#### 🍎 生活比喻：Flexbox 就像军训排队

- **容器（container）** = 教官
- **项目（items）** = 学生
- **主轴（Main Axis）** = 排队方向（默认横着排）
- **交叉轴（Cross Axis）** = 垂直于排队的方向（默认竖着）
- `justify-content` = 教官喊"沿主轴方向怎么对齐"
- `align-items` = 教官喊"沿交叉轴方向对齐（每行内部对齐）"

```
Flexbox 布局示意：
┌──────────────────────────────────────┐
│  flex container（容器 = 教官）        │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐     │
│  │ item│ │ item│ │ item│ │ item│     │ ← flex items（学生）
│  └─────┘ └─────┘ └─────┘ └─────┘     │
│  ←────── 主轴（Main Axis）──────→     │
│  ↑                                   │
│  交叉轴（Cross Axis）                 │
│  ↓                                   │
└──────────────────────────────────────┘
```

#### 容器属性

| 属性              | 作用                   | 常用值                                              | 比喻                 |
| ----------------- | ---------------------- | --------------------------------------------------- | -------------------- |
| `display: flex`   | 开启 flex 布局         | —                                                   | 教官开始指挥         |
| `flex-direction`  | 主轴方向               | `row`、`column`                                     | 横着排还是竖着排     |
| `justify-content` | 主轴对齐               | `flex-start`、`center`、`flex-end`、`space-between` | 沿主轴方向怎么对齐   |
| `align-items`     | 交叉轴对齐（每行内部） | `stretch`、`flex-start`、`center`                   | 沿交叉轴方向怎么对齐 |
| `align-content`   | 多行时行与行的对齐     | 同 justify-content                                  | 只有换行后才生效     |
| `flex-wrap`       | 是否换行               | `nowrap`、`wrap`                                    | 挤不下时换不换行     |
| `gap`             | 项目间距               | `10px`、`1rem`                                      | 学生之间的间距       |

**justify-content 图示**：

```
flex-start:    │▓▓  ▓▓  ▓▓        │
center:        │    ▓▓  ▓▓  ▓▓    │
flex-end:      │        ▓▓  ▓▓  ▓▓│
space-between: │▓▓        ▓▓      ▓▓│
space-around:  │ ▓▓  ▓▓  ▓▓ │
space-evenly:  │  ▓▓    ▓▓    ▓▓  │
```

> 💡 **记忆口诀**：
>
> - `justify-content` = **justify**（调整）**content**（内容）= 调整内容在主轴上的位置
> - `align-items` = **align**（对齐）**items**（项目）= 对齐项目在交叉轴上的位置
> - 想不清楚时记住：**justify 是主轴，align 是交叉轴**

#### 项目属性

| 属性          | 作用                                    | 比喻               |
| ------------- | --------------------------------------- | ------------------ |
| `flex-grow`   | 放大比例（剩余空间分配）                | 有多余空间时谁多长 |
| `flex-shrink` | 缩小比例（空间不足时）                  | 空间不够时谁先缩   |
| `flex-basis`  | 初始大小                                | 一开始占多大       |
| `flex`        | 简写，常用 `flex: 1`（等价于 `1 1 0%`） | 上面三个的缩写     |
| `align-self`  | 单独设置对齐方式                        | 某个学生搞特殊     |
| `order`       | 排列顺序                                | 插队顺序           |

#### 常见 Flexbox 布局

```css
/* 水平垂直居中（最常用） */
.center {
  display: flex;
  justify-content: center; /* 主轴居中 */
  align-items: center; /* 侧轴居中 */
}

/* 两端对齐的导航栏 */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 等分卡片 */
.cards {
  display: flex;
  flex-wrap: wrap; /* 避免窄屏幕溢出 */
  gap: 20px;
}
.card {
  flex: 1 1 300px; /* 基础宽度 300px，可 grow 也可 shrink */
  /* ⚠️ 如果只用 flex: 1（flex-basis: 0%），元素会平分宽度，空间不足时收缩 */
}

/* 侧边栏 + 主内容 */
.layout {
  display: flex;
}
.sidebar {
  width: 200px;
  flex-shrink: 0; /* 侧边栏不收缩 */
}
.main {
  flex: 1; /* 主内容占满剩余空间 */
  min-width: 0; /* ⚠️ 关键！允许 main 收缩到小于内容宽度，防止溢出 */
}
```

> 💡 **Flexbox 速查口诀**：
>
> - 主轴对齐用 `justify-content`
> - 侧轴对齐用 `align-items`
> - 子元素占满剩余空间用 `flex: 1`
> - 间距用 `gap`，不要再用 margin hack

### 6.5 网格布局（Grid）—— 二维布局

> Grid 用于同时控制**行和列**，适合整体页面布局和复杂网格。

#### 🍎 生活比喻：Grid 就像电影院座位

- **grid-template-columns** = 有多少列座位
- **grid-template-rows** = 有多少排座位
- **gap** = 座位之间的过道宽度
- **grid-area** = 某个区域占了几个座位（比如 VIP 区占了两列三排）
- **fr 单位** = 按比例分配剩余的座位空间

```
Grid 布局示意：
┌─────────┬─────────┬─────────┐
│  Cell   │  Cell   │  Cell   │  ← 单元格
├─────────┼─────────┼─────────┤
│  Cell   │         │         │  ← Area（合并多个单元格）
│         │  Area   │  Area   │
├─────────┼─────────┼─────────┤
│  Cell   │  Cell   │  Cell   │
└─────────┴─────────┴─────────┘
  ←────── 列轨道（Track）──────→
```

#### 常用单位与函数

```css
.container {
  /* 三列等宽 */
  grid-template-columns: 1fr 1fr 1fr;

  /* 重复：repeat(次数, 大小) */
  grid-template-columns: repeat(3, 1fr);

  /* 自动填充：repeat(auto-fill, minmax(200px, 1fr)) */
  /* 💡 auto-fill 会保留空轨道；auto-fit 会拉伸 item 填满空间 */
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));

  /* 固定 + 自适应 */
  grid-template-columns: 200px 1fr;
}
```

> 💡 **fr 单位**：Fraction（分数），分配剩余空间的比例。`1fr 2fr` 表示第二个占两份。
>
> 🍎 **比喻**：fr 就像分蛋糕——`1fr 1fr 1fr` 是三人平分，`1fr 2fr` 是第一个人 1/3，第二个人 2/3。

#### 常见 Grid 布局

```css
/* 经典页面布局 */
.layout {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-rows: 60px 1fr 40px;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  gap: 20px;
}

.header {
  grid-area: header;
}
.sidebar {
  grid-area: sidebar;
}
.main {
  grid-area: main;
}
.footer {
  grid-area: footer;
}

/* 移动端适配：侧边栏移到底部 */
@media (max-width: 767px) {
  .layout {
    grid-template-columns: 1fr;
    grid-template-areas:
      "header"
      "main"
      "sidebar"
      "footer";
  }
}

/* 响应式卡片网格 */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}
```

### 6.6 Flexbox vs Grid 怎么选？

| 场景                               | 选择              | 比喻                                        |
| ---------------------------------- | ----------------- | ------------------------------------------- |
| 一维排列（一行或一列）             | **Flexbox**       | 只排一队                                    |
| 二维网格（同时控制行列）           | **Grid**          | 排座位（有行有列）                          |
| 组件内部对齐（如按钮内图标和文字） | **Flexbox**       | 调整一个小组件内部                          |
| 整体页面布局                       | **Grid**          | 整个房间的座位安排                          |
| 两者也可以结合使用                 | 父 Grid + 子 Flex | 房间用 Grid，每个座位里的人用 Flex 调整姿势 |

```css
/* 结合使用示例 */
.page {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-rows: auto 1fr auto;
}

.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
```

### ✅ 本节回顾

- [x] 理解 static、relative、absolute、fixed、sticky 的区别
- [x] 知道 absolute 的定位上下文是什么
- [x] 会用 Flexbox 实现水平垂直居中
- [x] 会用 Grid 创建响应式网格布局
- [x] 知道什么时候用 Flexbox，什么时候用 Grid

### 📝 自测题

**1. `position: absolute` 的定位参考是？**

- A. 视口
- B. 最近的非 static 定位的祖先元素
- C. 自身原位置
- D. 浏览器窗口

**2. Flexbox 中，控制主轴对齐的属性是？**

- A. `align-items`
- B. `justify-content`
- C. `flex-direction`
- D. `align-content`

**3. `grid-template-columns: 1fr 2fr` 表示？**

- A. 两列等宽
- B. 第二列是第一列的两倍宽
- C. 第一列宽 1px，第二列宽 2px
- D. 总共 3 列

**4. 以下哪种布局最适合做整体页面布局（header + sidebar + main + footer）？**

- A. Flexbox
- B. Grid
- C. Float
- D. Position

**5. `position: fixed` 和 `position: absolute` 的主要区别是？**

- A. 没有区别
- B. fixed 相对于视口，absolute 相对于定位祖先
- C. fixed 会保留原位置，absolute 不会
- D. absolute 随滚动移动，fixed 不动

<details>
<summary>点击查看答案</summary>

1. **B**（absolute 相对于最近的非 static 定位祖先）
2. **B**（justify-content 控制主轴对齐）
3. **B**（1fr 和 2fr 表示按比例分配，第二个占两份）
4. **B**（Grid 适合二维整体布局）
5. **B**（fixed 相对于视口，absolute 相对于定位祖先）

</details>

### ✏️ 动手练习

1. 用 Flexbox 实现一个水平垂直居中的登录框
2. 用 Grid 实现一个经典页面布局（header + sidebar + main + footer）
3. 创建一个响应式卡片列表，手机上一列，平板两列，桌面三列（用 Grid）
4. 实现一个固定在页面顶部的导航栏（`position: fixed`）

<details>
<summary>点击查看参考实现</summary>

**练习 1：Flexbox 水平垂直居中登录框**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .login-box {
      width: 360px;
      padding: 40px;
      background: white;
      border-radius: 12px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }

    .login-box h2 {
      text-align: center;
      margin-bottom: 30px;
      color: #333;
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      display: block;
      margin-bottom: 8px;
      color: #555;
      font-size: 14px;
    }

    .form-group input {
      width: 100%;
      padding: 12px 16px;
      border: 1px solid #ddd;
      border-radius: 6px;
      font-size: 14px;
      transition: border-color 0.3s;
    }

    .form-group input:focus {
      outline: none;
      border-color: #667eea;
    }

    .btn-login {
      width: 100%;
      padding: 14px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .btn-login:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
    }
  </style>
</head>
<body>
  <div class="login-box">
    <h2>登录</h2>
    <form>
      <div class="form-group">
        <label>用户名</label>
        <input type="text" placeholder="请输入用户名">
      </div>
      <div class="form-group">
        <label>密码</label>
        <input type="password" placeholder="请输入密码">
      </div>
      <button type="submit" class="btn-login">登 录</button>
    </form>
  </div>
</body>
</html>
```

**练习 2：Grid 经典页面布局**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      min-height: 100vh;
      display: grid;
      grid-template-areas:
        "header header"
        "sidebar main"
        "footer footer";
      grid-template-columns: 200px 1fr;
      grid-template-rows: 60px 1fr 50px;
    }

    header {
      grid-area: header;
      background: #2c3e50;
      color: white;
      padding: 0 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .sidebar {
      grid-area: sidebar;
      background: #34495e;
      color: white;
      padding: 20px;
    }

    .sidebar nav a {
      display: block;
      color: #ecf0f1;
      text-decoration: none;
      padding: 12px 0;
      border-bottom: 1px solid #465c71;
    }

    .sidebar nav a:hover {
      background: #465c71;
      padding-left: 10px;
    }

    main {
      grid-area: main;
      padding: 20px;
      background: #f5f6fa;
      overflow-y: auto;
    }

    footer {
      grid-area: footer;
      background: #2c3e50;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
    }

    @media (max-width: 768px) {
      body {
        grid-template-areas:
          "header"
          "main"
          "footer";
        grid-template-columns: 1fr;
        grid-template-rows: 60px 1fr 50px;
      }

      .sidebar {
        display: none;
      }
    }
  </style>
</head>
<body>
  <header>
    <h1>我的网站</h1>
    <span>用户</span>
  </header>

  <aside class="sidebar">
    <nav>
      <a href="#">首页</a>
      <a href="#">文章</a>
      <a href="#">产品</a>
      <a href="#">关于</a>
    </nav>
  </aside>

  <main>
    <h2>欢迎回来</h2>
    <p>这是主内容区域。</p>
  </main>

  <footer>
    &copy; 2024 我的网站
  </footer>
</body>
</html>
```

**练习 3：响应式卡片列表**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
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

    .card-list {
      display: grid;
      gap: 20px;
      /* 默认一列（移动端） */
      grid-template-columns: 1fr;
    }

    /* 平板：两列 */
    @media (min-width: 576px) {
      .card-list {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    /* 桌面：三列 */
    @media (min-width: 992px) {
      .card-list {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .card {
      background: white;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s, box-shadow 0.3s;
    }

    .card:hover {
      transform: translateY(-4px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    }

    .card-image {
      height: 160px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 48px;
    }

    .card-content {
      padding: 20px;
    }

    .card-title {
      font-size: 18px;
      font-weight: bold;
      margin-bottom: 10px;
      color: #333;
    }

    .card-desc {
      font-size: 14px;
      color: #666;
      line-height: 1.6;
    }
  </style>
</head>
<body>
  <div class="card-list">
    <div class="card">
      <div class="card-image">📦</div>
      <div class="card-content">
        <h3 class="card-title">产品一</h3>
        <p class="card-desc">这是产品一的描述文字，介绍产品的特点和功能。</p>
      </div>
    </div>

    <div class="card">
      <div class="card-image">🎨</div>
      <div class="card-content">
        <h3 class="card-title">产品二</h3>
        <p class="card-desc">这是产品二的描述文字，介绍产品的特点和功能。</p>
      </div>
    </div>

    <div class="card">
      <div class="card-image">🚀</div>
      <div class="card-content">
        <h3 class="card-title">产品三</h3>
        <p class="card-desc">这是产品三的描述文字，介绍产品的特点和功能。</p>
      </div>
    </div>

    <div class="card">
      <div class="card-image">💡</div>
      <div class="card-content">
        <h3 class="card-title">产品四</h3>
        <p class="card-desc">这是产品四的描述文字，介绍产品的特点和功能。</p>
      </div>
    </div>

    <div class="card">
      <div class="card-image">⚡</div>
      <div class="card-content">
        <h3 class="card-title">产品五</h3>
        <p class="card-desc">这是产品五的描述文字，介绍产品的特点和功能。</p>
      </div>
    </div>

    <div class="card">
      <div class="card-image">🔥</div>
      <div class="card-content">
        <h3 class="card-title">产品六</h3>
        <p class="card-desc">这是产品六的描述文字，介绍产品的特点和功能。</p>
      </div>
    </div>
  </div>
</body>
</html>
```

**练习 4：固定顶部导航栏**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      /* 为固定导航栏留出空间 */
      padding-top: 70px;
      font-family: "Microsoft YaHei", sans-serif;
      background: #f5f6fa;
    }

    .navbar {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 70px;
      background: #2c3e50;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 30px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
      z-index: 1000;
    }

    .navbar-brand {
      font-size: 24px;
      font-weight: bold;
      color: white;
      text-decoration: none;
    }

    .navbar-menu {
      display: flex;
      gap: 30px;
      list-style: none;
    }

    .navbar-menu a {
      color: #ecf0f1;
      text-decoration: none;
      padding: 8px 16px;
      border-radius: 4px;
      transition: background 0.3s;
    }

    .navbar-menu a:hover {
      background: rgba(255, 255, 255, 0.1);
    }

    .content {
      max-width: 800px;
      margin: 0 auto;
      padding: 40px 20px;
    }

    .content h1 {
      margin-bottom: 20px;
      color: #2c3e50;
    }

    .content p {
      line-height: 1.8;
      color: #555;
      margin-bottom: 20px;
    }

    @media (max-width: 768px) {
      .navbar {
        padding: 0 15px;
      }

      .navbar-menu {
        gap: 15px;
      }

      .navbar-menu a {
        padding: 6px 10px;
        font-size: 14px;
      }
    }
  </style>
</head>
<body>
  <nav class="navbar">
    <a href="#" class="navbar-brand">我的网站</a>
    <ul class="navbar-menu">
      <li><a href="#">首页</a></li>
      <li><a href="#">文章</a></li>
      <li><a href="#">产品</a></li>
      <li><a href="#">关于</a></li>
    </ul>
  </nav>

  <main class="content">
    <h1>固定导航栏示例</h1>
    <p>这个导航栏使用 <code>position: fixed</code> 固定在页面顶部。</p>
    <p>向下滚动页面，导航栏会始终保持在视口顶部。</p>
    <p>注意 <code>body</code> 设置了 <code>padding-top: 70px</code>，为固定导航栏留出空间。</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
  </main>
</body>
</html>
```

**关键知识点回顾**：

| 练习 | 核心技术 |
|------|----------|
| 1 | `display: flex` + `justify-content: center` + `align-items: center` |
| 2 | Grid 布局 + `grid-template-areas` + 响应式适配 |
| 3 | Grid + 媒体查询 + `grid-template-columns: repeat(N, 1fr)` |
| 4 | `position: fixed` + `z-index` + `body { padding-top }` |

</details>
