---
title: "CSS 入门指南 · 第四阶段：选择器 —— 精准选中要修改的元素"
tags:
  - programming
  - css
created: 2026-09-10
updated: 2026-10-01
---

# 第四阶段：选择器 —— 精准选中要修改的元素

> 📚 本文是 [[topics/programming/Web/css|CSS 入门指南]] 的第 4 / 10 章。 上一章：[[topics/programming/Web/css/stage-03-box-model|第三阶段：盒模型与显示模式]] · 下一章：[[topics/programming/Web/css/stage-05-backgrounds|第五阶段：背景与装饰]]


> 🎯 **本节目标**：掌握基础选择器、复合选择器、伪类和伪元素，理解优先级计算规则。
>
> 学完基础样式后，需要学会**精准选中**元素。选择器是 CSS 的"瞄准镜"。

### 🍎 生活比喻：选择器就像"点名找人"

想象你在一个教室里要找到特定的人并给他发衣服（样式）：

- **`*` 通配选择器** = "给教室里所有人发衣服"
- **`div` 标签选择器** = "给所有男生发衣服"
- **`.class` 类选择器** = "给所有穿红衣服的人发衣服"
- **`#id` ID 选择器** = "给学号为 001 的人发衣服"（唯一）
- **`nav a` 后代选择器** = "给坐在靠窗那一排的所有同学发衣服"
- **`ul > li` 子选择器** = "给第一组的小组长发衣服"（只选直接下属）
- **`:hover` 伪类** = "给正在举手的人发衣服"

> 本节所有选择器都基于下面这段 HTML 结构来演示：

```html
<!-- 基础选择器示例 -->
<div id="header" class="container">
  <h1 class="title">网站标题</h1>
  <p>这是一段介绍文字。</p>
</div>

<!-- 复合选择器示例 -->
<nav class="navbar">
  <a href="#">首页</a>
  <a href="#">文章</a>
  <a href="#">关于</a>
</nav>

<ul class="menu">
  <li>首页</li>
  <li>
    产品
    <ul>
      <li>产品 A</li>
      <li>产品 B</li>
    </ul>
  </li>
  <li>关于</li>
</ul>

<!-- 伪类示例 -->
<button class="button">提交</button>

<!-- 结构伪类示例 -->
<table>
  <tr>
    <td>第 1 行</td>
  </tr>
  <tr>
    <td>第 2 行</td>
  </tr>
  <tr>
    <td>第 3 行</td>
  </tr>
</table>

<!-- 伪元素示例 -->
<ul class="feature-list">
  <li>特性一</li>
  <li>特性二</li>
</ul>
```

**上述 HTML 对应的树形结构图**：

```
body
└── <div id="header" class="container">
    ├── <h1 class="title">网站标题</h1>
    └── <p>这是一段介绍文字。</p>

└── <nav class="navbar">
    ├── <a href="#">首页</a>
    ├── <a href="#">文章</a>
    └── <a href="#">关于</a>

└── <ul class="menu">
    ├── <li>首页</li>
    ├── <li>
    │   产品
    │   └── <ul>
    │       ├── <li>产品 A</li>
    │       └── <li>产品 B</li>
    └── <li>关于</li>

└── <button class="button">提交</button>

└── <table>
    ├── <tr>
    │   └── <td>第 1 行</td>
    ├── <tr>
    │   └── <td>第 2 行</td>
    └── <tr>
        └── <td>第 3 行</td>

└── <ul class="feature-list">
    ├── <li>特性一</li>
    └── <li>特性二</li>
```

### 4.1 基础选择器

| 选择器     | 示例            | 含义                                | 比喻             |
| ---------- | --------------- | ----------------------------------- | ---------------- |
| 通配选择器 | `*`             | 选中所有元素                        | 给所有人         |
| 标签选择器 | `div`、`p`      | 选中所有该标签                      | 给所有男生/女生  |
| 类选择器   | `.className`    | 选中 class 属性中包含该独立词的元素 | 给所有穿红衣服的 |
| ID 选择器  | `#idName`       | 选中对应 id 的元素（页面唯一）      | 给学号 001 的    |
| 属性选择器 | `[type="text"]` | 根据属性选中                        | 给戴眼镜的       |

```css
/* 选中所有段落 */
p {
  color: #333;
}

/* 选中 class="button" 的元素 */
.button {
  padding: 10px 20px;
}

/* 选中 id="header" 的元素 */
#header {
  height: 60px;
}

/* 选中 type="text" 的输入框 */
input[type="text"] {
  border: 1px solid #ccc;
}
```

### 4.2 复合选择器

| 选择器   | 写法         | 含义                            | 比喻                   |
| -------- | ------------ | ------------------------------- | ---------------------- |
| 并集     | `h1, h2, p`  | 选中 h1 或 h2 或 p              | 给张三、李四、王五     |
| 后代     | `nav a`      | 选中 nav 内的所有 a（无论多深） | 给教室里所有戴眼镜的   |
| 子选择器 | `ul > li`    | 选中 ul 的直接子 li             | 只给儿子辈的，不给孙子 |
| 相邻兄弟 | `h2 + p`     | 选中紧跟 h2 后面的 p            | 给坐在我后面那个人     |
| 通用兄弟 | `h2 ~ p`     | 选中 h2 后面的所有 p            | 给我后面所有人         |
| 交集     | `div.active` | 选中同时是 div 且有 active 类的 | 既是男生又戴眼镜的     |

```css
/* 后代选择器：选中导航里的所有链接 */
.navbar a {
  color: #333;
}

/* 子选择器：只选中直接子菜单项 */
.menu > li {
  display: inline-block;
}

/* 交集选择器：选中同时满足两个条件的元素 */
div.highlight {
  background: yellow;
}

/* 并集选择器：统一设置多个元素 */
h1,
h2,
h3 {
  font-weight: bold;
}
```

> ⚠️ **常见错误**：
>
> - 以为 `ul li` 和 `ul > li` 一样（前者选中所有后代，后者只选直接子元素）
> - 空格很重要！`div.active`（交集，无空格）和 `div .active`（后代，有空格）完全不同！

### 4.3 伪类选择器（:）

**状态伪类**（与用户交互相关）：

| 伪类        | 触发条件          | 
| ----------- | ----------------- | 
| `:hover`    | 鼠标悬停          | 
| `:active`   | 鼠标按下          | 
| `:focus`    | 获得焦点          | 
| `:visited`  | 已访问的链接      | 
| `:disabled` | 禁用的表单元素    | 
| `:checked`  | 选中的单选/复选框 | 

**结构伪类**（根据元素在文档中的位置）：

| 伪类               | 含义             | 比喻               |
| ------------------ | ---------------- | ------------------ |
| `:first-child`     | 第一个子元素     | 老大               |
| `:last-child`      | 最后一个子元素   | 老幺               |
| `:nth-child(n)`    | 第 n 个子元素    | 排名第 n 的        |
| `:nth-child(odd)`  | 奇数位置的子元素 | 排名第1、3、5...的 |
| `:nth-child(even)` | 偶数位置的子元素 | 排名第2、4、6...的 |
| `:not(selector)`   | 排除某个选择器   | 除了...之外的      |

```css
/* 鼠标悬停时变色 */
.button:hover {
  background: #2980b9;
}

/* 斑马纹表格 */
tr:nth-child(even) {
  background: #f5f5f5;
}

/* 排除最后一个元素 */
.navbar a:not(:last-child) {
  margin-right: 10px;
}

/* 第一个列表项不需要上边距 */
li:first-child {
  margin-top: 0;
}
```

> 💡 **`:nth-child` 公式**：
>
> - `:nth-child(2n)` = 偶数项
> - `:nth-child(2n+1)` = 奇数项
> - `:nth-child(3n)` = 每 3 项
> - `n` 从 **0** 开始计算

### 4.4 伪元素选择器（::）

| 伪元素           | 作用             | 比喻                 |
| ---------------- | ---------------- | -------------------- |
| `::before`       | 在元素内容前插入 | 在名字前面加"尊敬的" |
| `::after`        | 在元素内容后插入 | 在名字后面加"同学"   |
| `::first-line`   | 选中第一行       | 只改第一段话         |
| `::first-letter` | 选中第一个字     | 只改第一个字         |
| `::selection`    | 选中的文字       | 鼠标拖蓝的文字       |

```css
/* 常用：用伪元素清除浮动或添加装饰 */
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

/* 在链接前添加图标 */
.external-link::before {
  content: "🔗";
  margin-right: 4px;
}

/* 自定义文字选中的颜色 */
::selection {
  background: #3498db;
  color: white;
}
```

> ⚠️ **注意**：`::before` 和 `::after` 必须设置 `content` 属性才能生效，即使内容为空也要写 `content: ""`。

> 💡 **记忆口诀**：单冒号 `:` 是伪类（状态/位置），双冒号 `::` 是伪元素（插入内容）。

### 4.5 选择器优先级（Specificity）

当多个选择器选中同一元素并设置冲突属性时，优先级高的生效。

#### 🔴 重难点：优先级计算

**优先级计算**（简化版）：

| 选择器类型          | 权重（元组）     | 比喻         |
| ------------------- | ---------------- | ------------ |
| 行内样式 `style=""` | (1, 0, 0, 0)     | 校长直接发话 |
| ID 选择器 `#id`     | (0, 1, 0, 0)     | 班主任       |
| 类/伪类/属性选择器  | (0, 0, 1, 0) × N | 班干部       |
| 标签/伪元素选择器   | (0, 0, 0, 1) × N | 普通学生     |
| 通配符 `*`          | (0, 0, 0, 0)     | 路人甲       |

> ℹ️ **`!important` 不是选择器，而是声明修饰符**：它会提升当前声明的优先级，但优先级比较仍以选择器特异性为基础（即两个 `!important` 声明之间，选择器特异性高的胜出）。`!important` 可以覆盖普通声明（包括普通行内样式），但两个 `!important` 之间仍按选择器特异性比较。

**比较规则**：从高位到低位逐位比较，高位胜出则不再比较低位。

- 15个类选择器 `(0, 0, 15, 0)` 仍然小于 1个ID选择器 `(0, 1, 0, 0)`

```
#nav .menu li a    →  (0, 1, 1, 2)   即 1个ID, 1个类, 2个标签
.nav li a:hover    →  (0, 0, 2, 2)   即 0个ID, 2个类, 2个标签
```

> 🍎 **比喻理解**：优先级就像"官大一级压死人"。
>
> - 校长发话（行内样式）> 班主任（ID）> 班干部（类/伪类）> 普通学生（标签）
> - 先比官职等级，同级再比人数

> ⚠️ **常见错误**：
>
> - 用 `!important` 解决所有冲突（导致维护困难）
> - 写过度深的选择器链（超过 3 层）
> - 以为 10个类选择器能超过 1个ID选择器（实际是 `(0,0,10,0)` < `(0,1,0,0)`）

```css
/* 错误：滥用 !important（普通声明再高的特异性也无法覆盖；
   只有优先级更高的 !important 能翻盘，最终仍要比拼特异性和书写顺序）*/
.button {
  color: red !important;
}

/* 正确：与其滥用 !important，不如用更高的特异性自然覆盖 */
.button {
  color: red;
} /* (0,0,1,0) */
.nav .button {
  color: blue;
} /* (0,0,2,0) > (0,0,1,0) ✓ */
```

### ✅ 本节回顾

- [x] 能区分类选择器 `.class` 和 ID 选择器 `#id`
- [x] 理解后代选择器 `nav a` 和子选择器 `ul > li` 的区别
- [x] 会用 `:hover`、`:nth-child()`、`:not()` 伪类
- [x] 会用 `::before`、`::after` 伪元素
- [x] 能计算选择器优先级

### 📝 自测题

**1. 以下哪个选择器优先级最高？**

- A. `div p`
- B. `.nav a`
- C. `#header`
- D. `*`

**2. `ul > li` 和 `ul li` 的区别是？**

- A. 没有区别
- B. `ul > li` 只选直接子元素，`ul li` 选所有后代
- C. `ul > li` 选所有后代，`ul li` 只选直接子元素
- D. `>` 表示排除

**3. 以下代码会选中哪些元素？**

```css
tr:nth-child(even) {
  background: gray;
}
```

- A. 所有 tr
- B. 奇数行的 tr
- C. 偶数行的 tr
- D. 第一个 tr

**4. 伪元素 `::before` 必须设置的属性是？**

- A. `display`
- B. `content`
- C. `position`
- D. `width`

**5. 计算 `#nav .menu li a:hover` 的优先级。**

- A. (0, 1, 0, 3)
- B. (0, 1, 1, 2)
- C. (0, 0, 2, 2)
- D. (0, 1, 2, 2)

<details>
<summary>点击查看答案</summary>

1. **C**（ID 选择器权重 (0,1,0,0)，最高）
2. **B**（`>` 只选直接子元素）
3. **C**（even 选中偶数位置的子元素）
4. **B**（`content` 必须设置，即使是空字符串）
5. **D**（1个ID(#nav) + 1个类(.menu) + 1个伪类(:hover) + 2个标签(`li`、`a`) = **(0, 1, 2, 2)**）

</details>

### ✏️ 动手练习

1. 创建一个导航栏，用后代选择器设置链接颜色，用 `:hover` 设置悬停效果
2. 创建一个列表，用 `:nth-child(odd)` 实现斑马纹
3. 用 `::before` 在每个列表项前添加一个圆点装饰
4. 尝试计算 `#header .nav li a:hover` 的优先级（写出元组形式）

<details>
<summary>点击参考实现</summary>

**练习 1：导航栏 + 悬停效果**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    .navbar {
      background: #2c3e50;
      padding: 10px 20px;
    }
    /* 后代选择器：选中导航里的所有链接 */
    .navbar a {
      color: #ecf0f1;
      text-decoration: none;
      margin-right: 20px;
      padding: 5px 10px;
    }
    /* 悬停效果 */
    .navbar a:hover {
      background: #3498db;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <nav class="navbar">
    <a href="#">首页</a>
    <a href="#">文章</a>
    <a href="#">关于</a>
  </nav>
</body>
</html>
```

**练习 2：斑马纹列表**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    .zebra-list {
      list-style: none;
      padding: 0;
      width: 300px;
    }
    .zebra-list li {
      padding: 10px 15px;
      border-bottom: 1px solid #ddd;
    }
    /* 奇数项背景色 */
    .zebra-list li:nth-child(odd) {
      background: #f8f9fa;
    }
    /* 偶数项背景色 */
    .zebra-list li:nth-child(even) {
      background: #e9ecef;
    }
  </style>
</head>
<body>
  <ul class="zebra-list">
    <li>第 1 项</li>
    <li>第 2 项</li>
    <li>第 3 项</li>
    <li>第 4 项</li>
    <li>第 5 项</li>
  </ul>
</body>
</html>
```

**练习 3：伪元素圆点装饰**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    .feature-list {
      list-style: none;
      padding: 0;
    }
    .feature-list li {
      padding: 8px 0;
      padding-left: 20px;
      position: relative;
    }
    /* 在每个列表项前添加彩色圆点 */
    .feature-list li::before {
      content: "";
      position: absolute;
      left: 0;
      top: 50%;
      transform: translateY(-50%);
      width: 8px;
      height: 8px;
      background: #e74c3c;
      border-radius: 50%;
    }
  </style>
</head>
<body>
  <ul class="feature-list">
    <li>特性一：响应式布局</li>
    <li>特性二：高性能动画</li>
    <li>特性三：模块化组件</li>
  </ul>
</body>
</html>
```

**练习 4：优先级计算**

```
#header .nav li a:hover
```

| 组成部分 | 类型 | 权重 |
| -------- | ---- | ---- |
| `#header` | ID 选择器 | (0, 1, 0, 0) |
| `.nav` | 类选择器 | (0, 0, 1, 0) |
| `:hover` | 伪类 | (0, 0, 1, 0) |
| `li` | 标签选择器 | (0, 0, 0, 1) |
| `a` | 标签选择器 | (0, 0, 0, 1) |

**结果**：`(0, 1, 2, 2)`（1 个 ID，2 个类/伪类，2 个标签）

</details>
