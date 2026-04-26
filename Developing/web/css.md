# CSS 入门指南

> **CSS（层叠样式表）** 用于控制网页的外观和布局。它描述了 HTML 元素应该如何被渲染显示，包括颜色、字体、间距、边框、背景、动画等方方面面。
>
> 学习 CSS 的核心逻辑：**先让元素可见 → 再让元素好看 → 最后让元素排好队**。

---

## 学习路线图

```
第一阶段：CSS 是什么、怎么引入页面（建立整体认知）
    ↓
第二阶段：改颜色、改字体、改间距（最直观，有即时反馈）
    ↓
第三阶段：理解盒模型与显示方式（明白元素占多少空间）
    ↓
第四阶段：精准选中元素（选择器）
    ↓
第五阶段：背景与装饰（让页面更丰富）
    ↓
第六阶段：布局系统（让元素各就各位）
    ↓
第七阶段：响应式设计（适配手机、平板、电脑）
    ↓
第八阶段：动画与交互（让页面动起来）
    ↓
第九阶段：现代 CSS 特性（变量、函数、新属性）
    ↓
第十阶段：工程化与最佳实践（走向专业）
```

### 📖 阅读指南

| 读者类型       | 阅读建议                                                                   |
| -------------- | -------------------------------------------------------------------------- |
| **完全新手**   | 按顺序阅读，每个阶段先读**比喻理解**，再做**自测题**，最后完成**动手练习** |
| **有一定基础** | 跳过熟悉内容，重点看 🔴 **重难点** 和 ⚠️ **易错点**                        |
| **速查参考**   | 善用目录和 `Ctrl+F` 搜索关键词                                             |

**文档符号说明**：

- 🍎 **生活比喻**：用日常事物类比 CSS 概念
- 🔴 **重难点**：必须掌握的核心概念
- ⚠️ **易错点**：初学者常犯的错误
- 💡 **记忆口诀**：帮助记忆的顺口溜
- 📝 **自测题**：检验理解程度的选择题/判断题
- ✏️ **动手练习**：可执行的代码练习

---

## 📑 目录与学习建议

| 阶段 | 内容 | 难度 | 预计时间 |
|:---:|:---|:---:|:---:|
| 一 | 初识 CSS —— 先让样式生效 | ⭐ | 30 分钟 |
| 二 | 给文字"化妆" —— 最直观的改变 | ⭐ | 45 分钟 |
| 三 | 盒模型与显示方式 —— 理解元素的空间占用 | ⭐⭐ | 1.5 小时 |
| 四 | 选择器 —— 精准选中要修改的元素 | ⭐⭐ | 1 小时 |
| 五 | 背景与装饰 —— 让页面更丰富 | ⭐⭐ | 45 分钟 |
| 六 | 布局系统 —— 让元素各就各位 | ⭐⭐⭐ | 2 小时 |
| 七 | 响应式设计 —— 适配不同屏幕 | ⭐⭐⭐ | 1.5 小时 |
| 八 | 动画与交互 —— 让页面动起来 | ⭐⭐⭐ | 1.5 小时 |
| 九 | 现代 CSS 进阶特性 | ⭐⭐ | 1 小时 |
| 十 | CSS 架构与工程化 | ⭐⭐⭐ | 1 小时 |

> 💡 **给初学者的建议**：按顺序逐个阶段学习，不要跳过基础直接看布局。每个阶段务必完成**自测题**，有不确定的及时回到正文复习。

---

## 核心概念速查

| 概念             | 一句话理解                                                        | 生活比喻                                                                      |
| ---------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **选择器**       | 告诉浏览器"我要改哪个元素"                                        | 就像老师点名："第三排穿红衣服的同学"                                          |
| **属性**         | 告诉浏览器"我要改它的什么"                                        | 就像说："把头发染成蓝色"                                                      |
| **值**           | 告诉浏览器"改成什么样"                                            | 就像说："染成深蓝色 #00008B"                                                  |
| **盒模型**       | 每个元素都是一个盒子，由 content + padding + border + margin 组成 | 就像快递盒：商品 + 气泡膜 + 纸箱 + 两个箱子间的距离                           |
| **`border-box`** | `width` 包含 content + padding + border，设置多少就是多少         | 就像说"整个包裹宽 10cm"——就是 10cm，内部自己压缩                             |
| **`content-box`**| `width` 只包含 content，实际占地需要心算                          | 就像说"杯子宽 10cm"——实际还要加上包装                                       |
| **选择器优先级** | 多个样式冲突时，优先级高的生效                                    | 就像游戏规则：校长发话 > 班主任 > 班干部 > 普通学生（先比官职，同级再比人数） |
| **`block`**      | 独占一行，可设宽高                                                | 一人一张桌子                                                                  |
| **`inline`**     | 共占一行，不可设宽高                                              | 几人挤一张长桌                                                                |
| **`inline-block`**| 共占一行，可设宽高                                               | 长桌上每人有固定座位                                                          |
| **Flexbox**      | 一维布局，沿主轴排列                                              | 就像排队：可以横着排，也可以竖着排                                            |
| **Grid**         | 二维布局，同时控制行和列                                          | 就像棋盘：有横有竖，形成格子                                                  |
| **Position**     | 定位方式                                                          | 就像人站在哪里：原地站(static)、站队时踮脚(relative)、站到操场角落(absolute)  |
| **Z-Index**      | 层叠顺序                                                          | 就像一叠纸，数字大的在上面                                                    |

---

## 第一阶段：初识 CSS —— 先让样式生效

> 🎯 **本节目标**：理解 CSS 的作用，能写出第一个生效的样式，掌握三种引入方式，会打开开发者工具。

### 🍎 生活比喻：CSS 是什么？

想象你要参加一场派对：

- **HTML** = 你的骨骼和身材（结构）—— "这是一个有头、有身体、有四肢的人"
- **CSS** = 你的衣服、发型、妆容（表现）—— "穿红色连衣裙、卷发、涂口红"
- **JavaScript** = 你的动作和行为（交互）—— "跳舞、打招呼、拿饮料"

没有 CSS，网页就像素颜的人——结构完整，但看起来单调乏味。有了 CSS，网页才能变得美观、有风格。

```
┌─────────────────────────────────────────────┐
│                  浏览器页面                   │
│  ┌───────────────────────────────────────┐  │
│  │  HTML：结构（骨架）                     │  │
│  │  "这里有个按钮，上面写着提交"            │  │
│  └───────────────────────────────────────┘  │
│  ┌───────────────────────────────────────┐  │
│  │  CSS：样式（皮肤衣服）                  │  │
│  │  "按钮是蓝色的，圆角，鼠标放上去变深"    │  │
│  └───────────────────────────────────────┘  │
│  ┌───────────────────────────────────────┐  │
│  │  JavaScript：行为（肌肉）               │  │
│  │  "点击按钮后弹出提示框"                 │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### 1.1 CSS 的基本语法

```css
选择器 {
  属性: 值;
  属性: 值;
}
```

就像中文的"把...改成..."句式：

```
把      h1    改成    颜色红色、大小24像素
↑       ↑             ↑
选择器  元素          属性:值
```

```css
h1 {
  color: red;
  font-size: 24px;
}
```

**语法规则**：

- 每个声明以 `;` 结尾（**建议每行都写**，避免遗漏导致后续样式失效）
- 属性和值之间用 `:` 分隔
- 多条声明用 `{}` 包裹
- CSS **标签选择器（如 `div`、`p`）和属性名**不区分大小写，但**类选择器（`.class`）和 ID 选择器（`#id`）区分大小写**；类名和 ID 最好与 HTML 中保持完全一致

> ⚠️ **常见错误**：忘记写分号 `;` 导致后面的样式不生效！
>
> ```css
> /* 错误：第一行缺少分号 */
> h1 {
>     color: red
>     font-size: 24px;  /* 这行不会生效！ */
> }
> ```

### 1.2 三种引入方式

| 方式           | 代码写法                                   | 生活比喻                   | 使用场景                      |
| -------------- | ------------------------------------------ | -------------------------- | ----------------------------- |
| **外部样式表** | `<link rel="stylesheet" href="style.css">` | 衣服放在衣柜里，谁想穿去拿 | ✅ 最推荐，样式与结构分离     |
| **内部样式表** | `<style>` 标签写在 HTML 的 `<head>` 中     | 把衣服标签缝在身上         | 小型页面或单页演示            |
| **行内样式**   | `<div style="color: red;">`                | 用马克笔直接画在身上       | ❌ 不推荐，优先级过高且难维护 |

**🍎 比喻理解**：

- **外部样式表** = 学校统一校服（一个文件管所有页面，修改一处全局生效）
- **内部样式表** = 班级临时规定的着装（只影响当前页面）
- **行内样式** = 某人用马克笔在衣服上写了个字（只影响这一个元素，且很难擦掉）

**完整的入门示例**（建议新手直接复制保存为两个文件尝试）：

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>我的第一个 CSS 页面</title>
    <!-- 外部样式表引入 -->
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Hello CSS!</h1>
    <p class="intro">这是一段介绍文字。</p>
    <button>点击我</button>
  </body>
</html>
```

```css
/* style.css */
body {
  font-family: Arial, "Microsoft YaHei", sans-serif;
  background-color: #f0f2f5;
  padding: 40px;
}

h1 {
  color: #2c3e50;
  font-size: 32px;
}

.intro {
  color: #666;
  line-height: 1.6;
}

button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #2980b9;
}
```

> 💡 **练习建议**：创建上述两个文件，用浏览器打开 `index.html`，然后修改 `style.css` 中的颜色、字号，观察页面变化。
>
> 📋 **全文通用练习模板**：上面这个 `index.html` 是一个最基础的网页骨架。后续各阶段的学习和练习，都可以直接复用它——只需要在 `<body>` 里增删元素，在 `style.css` 里写对应的选择器和样式即可。如果你希望一个文件搞定练习，也可以把 `<link>` 去掉，改成 `<style>` 标签把 CSS 直接写在 `<head>` 中。

### 1.3 CSS 注释

```css
/* 这是 CSS 注释，不会显示在页面上 */

/*
 * 多行注释
 * 可以写多行
 */
```

> ⚠️ **注意**：CSS 只有 `/* */` 这一种注释方式，**没有** `//` 单行注释！
>
> ```css
> /* 这是正确的注释 */
>
> // 这是错误的！CSS 不支持这种注释
> color: red;
> ```

### 1.4 浏览器开发者工具初探

- **打开方式**：F12 或 `Cmd+Option+I`（Mac）/ `Ctrl+Shift+I`（Windows）
- **Elements 面板**：查看 DOM 结构和样式
- **Styles 面板**：查看和实时修改元素的 CSS
- **盒模型可视化**：直观看到 content / padding / border / margin
- **常用技巧**：
  - hover 状态调试：在 Styles 面板点击 `:hov` 按钮
  - 实时修改：点击属性值直接修改，页面即时生效
  - 复制计算后的样式：查看元素的最终实际样式

> 💡 **新手必备习惯**：写 CSS 时一定要开着开发者工具，实时查看效果！

### ✅ 本节回顾

- [x] 能说出 CSS 的作用和基本语法结构
- [x] 知道三种引入方式，优先使用外部样式表
- [x] 会写 CSS 注释
- [x] 能打开开发者工具并找到 Styles 面板

### 📝 自测题

**1. 以下哪种引入 CSS 的方式最推荐？**

- A. 行内样式 `style="color: red;"`
- B. 内部样式表 `<style>...</style>`
- C. 外部样式表 `<link rel="stylesheet" href="style.css">`
- D. 都一样

**2. CSS 注释的正确写法是？**

- A. `// 这是注释`
- B. `/* 这是注释 */`
- C. `<!-- 这是注释 -->`
- D. `# 这是注释`

**3. 以下代码有什么错误？**

```css
h1 {
    color: red
    font-size: 24px;
}
```

- A. `h1` 不能作为选择器
- B. `color: red` 后面缺少分号
- C. `font-size` 写法错误
- D. 没有错误

<details>
<summary>点击查看答案</summary>

1. **C**（外部样式表最利于维护和复用）
2. **B**（CSS 只支持 `/* */` 注释）
3. **B**（`color: red` 后缺少 `;`，导致 `font-size` 不生效）

</details>

---

## 第二阶段：给文字"化妆" —— 最直观的改变

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

---

## 第三阶段：盒模型与显示模式 —— 理解元素的空间占用

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

---

## 第四阶段：选择器 —— 精准选中要修改的元素

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
/* 错误：滥用 !important（一旦使用，其他声明无论特异性多高都无法覆盖）*/
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

---

## 第五阶段：背景与装饰 —— 让页面更丰富

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

---

## 第六阶段：布局系统 —— 让元素各就各位

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

---

## 第七阶段：响应式设计 —— 适配不同屏幕

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

---

## 第八阶段：动画与交互 —— 让页面动起来

> 🎯 **本节目标**：掌握过渡、变换和动画，能写出常见交互效果。
>
> 本节动画示例基于以下 HTML 结构：
>
> ```html
> <button class="button">悬停看我变色</button>
>
> <div class="card">
>   <p>悬停时我会向上浮动</p>
> </div>
>
> <div class="box">我会旋转和缩放</div>
>
> <div class="loading"></div>
> ```

### 🍎 生活比喻：动画就像电影

- **Transition（过渡）** = 淡入淡出（两个状态之间的平滑变化，如从暗到亮）
- **Transform（变换）** = 演员的姿势变化（移动、旋转、缩放）
- **Animation（动画）** = 完整电影（可以有很多帧，循环播放）

三者关系：**Transform 负责变形，Transition 负责平滑过渡，Animation 负责复杂关键帧动画。**

### 8.1 过渡（Transition）

元素从一种状态**平滑过渡**到另一种状态。

```css
.button {
  background-color: blue;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: red;
}
```

> 🍎 **比喻理解**：就像调光开关——不是瞬间变亮，而是慢慢从暗变亮。`0.3s` 就是"用 0.3 秒完成这个变化"。

#### 过渡属性详解

| 属性 | 语法 | 参数说明 | 可选值 | 默认值 |
|------|------|----------|--------|--------|
| `transition-property` | `transition-property: none\|all\|属性名` | 指定哪个CSS属性参与过渡 | `none`（无过渡）<br>`all`（所有可过渡属性）<br>具体属性名如 `width`、`opacity` | `all` |
| `transition-duration` | `transition-duration: 时间` | 过渡持续多久 | `0s`（无过渡）<br>`0.3s`（300毫秒）<br>`1.5s`（1.5秒） | `0s` |
| `transition-timing-function` | `transition-timing-function: 函数` | 过渡速度曲线 | 预定义：`ease` `linear` `ease-in` `ease-out` `ease-in-out`<br>贝塞尔：`cubic-bezier(n,n,n,n)`<br>阶跃：`steps(n, start\|end)` | `ease` |
| `transition-delay` | `transition-delay: 时间` | 延迟多久开始 | `0s`（立即开始）<br>`0.5s`（延迟500毫秒）<br>负值（提前开始） | `0s` |

**简写语法**：

```css
transition: property duration timing-function delay;

/* 示例 */
transition: opacity 0.3s ease-in-out 0.1s;
transition: all 0.5s linear;
transition: transform 0.3s ease, box-shadow 0.3s ease;
```

> ⚠️ **易错点**：简写时 `duration` 和 `delay` 都是时间值，浏览器通过顺序判断——第一个时间是 `duration`，第二个时间是 `delay`。

**哪些CSS属性可以过渡？**

| 分类 | 可过渡属性示例 |
|------|---------------|
| 颜色类 | `color`、`background-color`、`border-color`、`box-shadow` |
| 尺寸类 | `width`、`height`、`padding`、`margin`、`border-width` |
| 变换类 | `transform`（GPU加速，**推荐**） |
| 透明度 | `opacity`（GPU加速，**推荐**） |
| 滤镜 | `filter`（触发重绘，性能较差） |
| 定位 | `top`、`left`、`right`、`bottom`（触发重排，**避免**） |

**常用时间函数详解**：

| 值 | `cubic-bezier` 等价 | 效果描述 | 适用场景 |
|----|---------------------|----------|----------|
| `ease` | `cubic-bezier(0.25, 0.1, 0.25, 1)` | 慢-快-慢（默认） | 普通过渡 |
| `linear` | `cubic-bezier(0, 0, 1, 1)` | 匀速 | 颜色渐变 |
| `ease-in` | `cubic-bezier(0.42, 0, 1, 1)` | 慢开始，快结束 | 淡入、进入 |
| `ease-out` | `cubic-bezier(0, 0, 0.58, 1)` | 快开始，慢结束 | 淡出、离开 |
| `ease-in-out` | `cubic-bezier(0.42, 0, 0.58, 1)` | 对称的慢-快-慢 | 呼吸效果 |
| `steps(n, start\|end)` | — | 阶跃式变化 | 步进动画 |

```css
/* 贝塞尔曲线自定义速度 */
transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); /* 带弹性的效果 */

/* 阶跃函数 - 适合翻页效果 */
transition: background-position 0.3s steps(4, end);
```

```css
/* 过渡多个属性 */
/* 💡 transition 必须写在基础状态，不要只写在 :hover 上，否则移出时没有过渡！ */
.card {
  transition:
    transform 0.3s ease,
    opacity 0.3s ease;
  opacity: 0.9;
}

.card:hover {
  transform: translateY(-5px);
  opacity: 1;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* 仅改变值，不过渡 */
}
```

> 💡 **性能提示**：过渡 `transform` 和 `opacity` 性能最好（GPU加速）。尽量避免过渡 `width`、`height`、`top`、`left`、`margin`、`padding`（触发重排），以及 `box-shadow`、`filter`（触发重绘）。

### 8.2 变换（Transform）

#### 2D 变换函数详解

| 函数 | 语法 | 参数说明 | 示例效果 |
|------|------|----------|----------|
| `translate(x, y)` | `translate(水平px, 垂直px)` | 正值向右/下移动，负值向左/上移动<br>`translateX(tx)` 只水平移动<br>`translateY(ty)` 只垂直移动 | `translate(50px, 100px)` |
| `rotate(角度)` | `rotate(deg)` | 正值顺时针，负值逆时针<br>角度单位：`deg`（度）、`turn`（圈） | `rotate(45deg)`、`rotate(0.5turn)` |
| `scale(x, y)` | `scale(倍数)` | `scale(sx)` 宽高同缩放<br>`scale(sx, sy)` 宽高分别缩放<br>大于1放大，小于1缩小 | `scale(1.5)`、`scale(1, 1.2)` |
| `skew(x, y)` | `skew(角度deg)` | 沿X/Y轴倾斜扭曲<br>`skewX(ax)` 只沿X轴<br>`skewY(ay)` 只沿Y轴 | `skew(10deg, 5deg)` |
| `matrix(a, b, c, d, e, f)` | `matrix(6个数值)` | 2D矩阵变换（综合上述所有变换）<br>需要数学基础，一般用上面更直观 | `matrix(1,0,0,1,50,100)` |

```css
/* 2D 变换示例 */
transform: translate(50px, 100px); /* 平移 - 移动位置 */
transform: rotate(45deg); /* 旋转 - 转多少度 */
transform: scale(1.5); /* 缩放 - 放大缩小 */
transform: skew(10deg, 5deg); /* 倾斜 - 斜着拉 */

/* 单独轴向变换 */
transform: translateX(30px); /* 只向右移动30px */
transform: translateY(-20px); /* 只向上移动20px */
transform: scaleX(2); /* 只宽度放大2倍 */
transform: rotateZ(90deg); /* 只沿Z轴旋转（同rotate） */

/* 组合变换 */
/* ⚠️ transform 从右向左运算：先 translate（基于原始尺寸居中），再 scale */
transform: scale(1.1) translate(-50%, -50%);
```

#### 3D 变换函数详解

| 函数 | 语法 | 参数说明 | 示例效果 |
|------|------|----------|----------|
| `translate3d(x, y, z)` | `translate3d(tx, ty, tz)` | 3D空间平移 | `translate3d(0, 0, -50px)` |
| `rotateX(角度)` | `rotateX(deg)` | 沿X轴旋转（前后翻转） | `rotateX(45deg)` |
| `rotateY(角度)` | `rotateY(deg)` | 沿Y轴旋转（左右翻转） | `rotateY(45deg)` |
| `rotateZ(角度)` | `rotateZ(deg)` | 沿Z轴旋转（平面旋转） | `rotateZ(45deg)` |
| `scale3d(sx, sy, sz)` | `scale3d(sx, sy, sz)` | 3D空间缩放 | `scale3d(1, 1, 2)` |
| `perspective(距离)` | `perspective(px)` | 透视距离（设置在父元素）<br>值越小，透视越强烈 | `perspective(1000px)` |

```css
/* 3D 变换示例：父元素需要设置 perspective 才能看到立体效果 */
.parent {
  perspective: 1000px; /* 透视距离，值越大透视越平，值越小透视越强 */
  perspective-origin: center center; /* 透视原点 */
}

.child {
  transform: rotateX(45deg); /* 沿X轴旋转 */
  transform-style: preserve-3d; /* 保持3D空间（父元素设置） */
}
```

**常用3D变换效果**：

```css
/* 卡片翻转效果 */
.card {
  transform-style: preserve-3d;
  transition: transform 0.6s;
}
.card:hover {
  transform: rotateY(180deg);
}
.card-front,
.card-back {
  backface-visibility: hidden; /* 隐藏背面 */
}
.card-back {
  transform: rotateY(180deg); /* 背面预先翻转 */
}

/* 立方体效果 */
.cube {
  transform-style: preserve-3d;
  transform: rotateX(-30deg) rotateY(45deg);
}
.cube .face {
  position: absolute;
  width: 100px;
  height: 100px;
}
.front  { transform: translateZ(50px); }
.back   { transform: rotateY(180deg) translateZ(50px); }
.left   { transform: rotateY(-90deg) translateZ(50px); }
.right  { transform: rotateY(90deg) translateZ(50px); }
.top    { transform: rotateX(90deg) translateZ(50px); }
.bottom { transform: rotateX(-90deg) translateZ(50px); }
```

#### transform 相关属性

| 属性 | 作用 | 可选值 |
|------|------|--------|
| `transform-origin` | 变换原点（默认 center center） | `x y z` 或 `left/center/right` |
| `transform-style` | 保持3D空间 | `flat`（平面）、`preserve-3d`（3D空间） |
| `backface-visibility` | 背面是否可见 | `visible`、`hidden` |
| `perspective` | 透视距离（父元素设置） | `none`、`<length>` |

```css
/* 变换原点示例 */
.transform-origin-demo {
  transform-origin: top left; /* 绕左上角旋转 */
  transform: rotate(45deg);
}
```

> 🍎 **比喻理解**：
>
> - `translate` = 把照片从左边移到右边
> - `rotate` = 把照片转个角度
> - `scale` = 把照片放大或缩小
> - `skew` = 把照片斜着拉

> 💡 **居中技巧**：`position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);` 是元素绝对居中的经典方案。
>
> 🍎 **为什么需要 translate(-50%, -50%)？** 因为 `top: 50%` 是把元素的**顶部**放在中间，不是把元素中心放在中间。`translate(-50%, -50%)` 就是把元素往回拉自身宽高的一半，让中心点对齐。

### 8.3 动画（Animation）

#### @keyframes 关键帧定义

```css
/* 定义关键帧 - 两种语法 */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  50% {
    opacity: 0.5;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 使用动画 */
.element {
  opacity: 0; /* 初始隐藏，避免动画执行前元素瞬间可见的闪烁 */
  animation: slideUp 0.5s ease-out forwards;
}
```

> 🍎 **比喻理解**：`@keyframes` 就像电影分镜——
>
> - `0%` = 第一帧（电影开场）
> - `50%` = 中间帧（高潮）
> - `100%` = 最后一帧（结局）
> - `forwards` = 演完保持最后一帧的姿势（不散场）

#### 动画属性详解

| 属性 | 语法 | 参数说明 | 可选值 | 默认值 |
|------|------|----------|--------|--------|
| `animation-name` | `animation-name: name\|none` | 指定要使用的关键帧名称 | `@keyframes`定义的名称<br>`none`（无动画） | `none` |
| `animation-duration` | `animation-duration: 时间` | 动画持续时间 | `0s`（无动画）<br>`0.3s`、`1.5s` | `0s` |
| `animation-timing-function` | `animation-timing-function: 函数` | 动画速度曲线 | 同 transition-timing-function<br>预定义+贝塞尔+阶跃 | `ease` |
| `animation-delay` | `animation-delay: 时间` | 动画延迟开始时间 | `0s`（立即）<br>正值（延迟）<br>负值（提前，从中间开始） | `0s` |
| `animation-iteration-count` | `animation-iteration-count: n\|infinite` | 动画循环次数 | 具体数字 `1`、`3`<br>`infinite`（无限循环） | `1` |
| `animation-direction` | `animation-direction: 方向` | 动画播放方向 | `normal`（正向，从0%到100%）<br>`reverse`（反向，从100%到0%）<br>`alternate`（交替，来回播放）<br>`alternate-reverse`（反向交替） | `normal` |
| `animation-fill-mode` | `animation-fill-mode: 模式` | 动画前后状态 | `none`（保持原样）<br>`forwards`（停在最后一帧）<br>`backwards`（使用第一帧状态直到延迟结束）<br>`both`（forwards+backwards） | `none` |
| `animation-play-state` | `animation-play-state: 状态` | 动画运行/暂停 | `running`（运行）<br>`paused`（暂停） | `running` |

**简写语法**：

```css
animation: name duration timing-function delay iteration-count direction fill-mode;

/* 示例 */
animation: slideUp 0.5s ease-out 0.2s infinite alternate forwards;
animation: fadeIn 0.3s ease-in-out 1 normal both;
```

> ⚠️ **易错点**：`animation-delay` 是第二个时间值，不是第一个。如果写 `0.5s 1s`，则是延迟0.5秒，播放1秒。

**animation-direction 详细效果**：

| 值 | 效果描述 | 播放示例（假设0%→100%是向上移动） |
|----|----------|-----------------------------------|
| `normal` | 始终从0%到100% | ↑ ↑ ↑ |
| `reverse` | 始终从100%到0% | ↓ ↓ ↓ |
| `alternate` | 奇数次正向，偶数次反向 | ↑ ↓ ↑ ↓ |
| `alternate-reverse` | 奇数次反向，偶数次正向 | ↓ ↑ ↓ ↑ |

**animation-fill-mode 详细效果**：

| 值 | 动画前状态 | 播放期间 | 动画结束后状态 |
|----|------------|----------|----------------|
| `none` | 元素原样式 | 关键帧控制 | 回到元素原样式 |
| `forwards` | 元素原样式 | 关键帧控制 | 停在最后一帧 |
| `backwards` | 使用第一帧状态 | 关键帧控制 | 回到元素原样式 |
| `both` | 使用第一帧状态 | 关键帧控制 | 停在最后一帧 |

**暂停/继续动画（结合JavaScript）**：

```css
.paused {
  animation-play-state: paused;
}
.running {
  animation-play-state: running;
}
```

#### 常用动画示例

```css
/* 呼吸动画 - 放大缩小循环 */
@keyframes breathe {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}
.breathe {
  animation: breathe 2s ease-in-out infinite;
}

/* 加载旋转动画 */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
.spinner {
  animation: spin 1s linear infinite;
}

/* 闪烁动画 */
@keyframes blink {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}
.blink {
  animation: blink 1s step-start infinite;
}
```

### 8.4 过渡 vs 变换 vs 动画对比

| 特性     | Transition           | Transform      | Animation      |
| -------- | -------------------- | -------------- | -------------- |
| 触发方式 | 状态变化（如 hover） | 立即生效       | 自动播放或触发 |
| 中间状态 | 自动计算             | 无（瞬间变化） | 需定义关键帧   |
| 循环播放 | ❌ 不能              | ❌ 不能        | ✅ 可以        |
| 适用场景 | 简单状态过渡         | 变形、位移     | 复杂动画       |
| 生活比喻 | 调光开关             | 换姿势         | 完整电影       |

> 💡 **实际开发中**：三者常配合使用。`transform` 负责变形，`transition` 负责平滑过渡，`animation` 负责复杂关键帧动画。

### 8.5 毛玻璃效果

```css
.glass {
  background: rgba(255, 255, 255, 0.2);
  -webkit-backdrop-filter: blur(10px); /* Safari 兼容 */
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
/* ⚠️ backdrop-filter 会创建新的层叠上下文，且旧浏览器不支持 */
```

> 🍎 **比喻理解**：就像磨砂玻璃——你看不清玻璃后面的东西，但能看到模糊的轮廓。`blur(10px)` 就是模糊程度。

### ✅ 本节回顾

- [x] 会写 `transition` 实现悬停效果
- [x] 会用 `transform` 实现位移、旋转、缩放
- [x] 会定义 `@keyframes` 并使用 `animation`
- [x] 知道什么时候用 transition，什么时候用 animation

### 📝 自测题

**1. `transition: all 0.3s ease` 中的 `all` 表示？**

- A. 所有元素
- B. 所有属性都会过渡
- C. 所有颜色
- D. 没有特殊含义

**2. `transform: translate(-50%, -50%)` 通常配合什么使用来实现居中？**

- A. `position: relative`
- B. `position: absolute; top: 50%; left: 50%;`
- C. `display: flex`
- D. `margin: 0 auto`

**3. `@keyframes` 中的 `100%` 可以用什么代替？**

- A. `end`
- B. `to`
- C. `last`
- D. `finish`

**4. 以下哪个属性可以实现循环播放动画？**

- A. `transition`
- B. `transform`
- C. `animation-iteration-count: infinite`
- D. `@keyframes`

**5. 性能最好的动画属性是？**

- A. `width` 和 `height`
- B. `top` 和 `left`
- C. `transform` 和 `opacity`
- D. `margin` 和 `padding`

<details>
<summary>点击查看答案</summary>

1. **B**（all 表示所有属性都会参与过渡）
2. **B**（absolute + top/left 50% + translate(-50%, -50%) 是经典居中方案）
3. **B**（`from` = `0%`，`to` = `100%`）
4. **C**（animation-iteration-count 控制循环次数）
5. **C**（transform 和 opacity 触发 GPU 加速）

</details>

### ✏️ 动手练习

1. 给按钮添加悬停过渡效果（颜色 + 上移）
2. 用 `transform` 实现一个元素在父容器中绝对居中
3. 用 `@keyframes` 实现一个加载动画（旋转的圆圈）

<details>
<summary>点击查看参考实现</summary>

**练习 1：按钮悬停过渡效果**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    .button {
      display: inline-block;
      padding: 12px 24px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
      /* 关键：transition 写在基础状态 */
      transition:
        background-color 0.3s ease,
        transform 0.3s ease,
        box-shadow 0.3s ease;
    }

    .button:hover {
      background-color: #2980b9; /* 颜色变深 */
      transform: translateY(-3px); /* 上移3px */
      box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4); /* 阴影加深 */
    }
  </style>
</head>
<body>
  <button class="button">悬停看我</button>
</body>
</html>
```

**练习 2：transform 绝对居中**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    .parent {
      position: relative;
      width: 400px;
      height: 300px;
      background-color: #f0f2f5;
      border: 1px solid #ddd;
    }

    .child {
      position: absolute;
      top: 50%;      /* 顶部定位到父容器中线 */
      left: 50%;     /* 左边定位到父容器中线 */
      /* 关键：往回拉自身宽高的50%，实现中心点居中 */
      transform: translate(-50%, -50%);
      width: 120px;
      height: 80px;
      background-color: #3498db;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <div class="parent">
    <div class="child">完美居中</div>
  </div>
</body>
</html>
```

**练习 3：加载旋转动画**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    /* 定义旋转动画 */
    @keyframes spin {
      from {
        transform: rotate(0deg);
      }
      to {
        transform: rotate(360deg);
      }
    }

    .loader {
      width: 40px;
      height: 40px;
      border: 4px solid #e0e0e0;
      border-top-color: #3498db; /* 只留顶部边框颜色 */
      border-radius: 50%;
      /* 应用动画 */
      animation: spin 0.8s linear infinite;
    }

    /* 加载动画容器 */
    .loading-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }

    .loading-text {
      font-family: Arial, sans-serif;
      color: #666;
      font-size: 14px;
    }

    /* 扩展：带渐变效果的旋转圈 */
    .loader-gradient {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      border: 4px solid transparent;
      border-top-color: #3498db;
      border-right-color: #e74c3c;
      animation: spin 1s linear infinite;
    }
  </style>
</head>
<body>
  <div class="loading-container">
    <div class="loader"></div>
    <span class="loading-text">加载中...</span>
  </div>

  <br><br>

  <div class="loading-container">
    <div class="loader-gradient"></div>
    <span class="loading-text">加载中...</span>
  </div>
</body>
</html>
```

</details>

---

## 第九阶段：现代 CSS 进阶特性

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

---

## 第十阶段：CSS 架构与工程化

> 🎯 **本节目标**：了解命名规范、性能优化和现代 CSS 工具链。

### 🍎 生活比喻：CSS 架构就像工厂管理

- **BEM 命名** = 零件编号系统（每个零件有唯一的、有规律的编号）
- **性能优化** = 流水线优化（减少不必要的步骤）
- **预处理器** = 自动化机器（Sass 像高级机床，能批量生产）

### 10.1 命名规范

#### BEM 命名法

- **B**lock（块）：独立组件 `.card`
- **E**lement（元素）：块的一部分 `.card__title`
- **M**odifier（修饰符）：变体 `.card--featured`

```html
<div class="card card--featured">
  <h2 class="card__title">标题</h2>
  <p class="card__desc">描述</p>
  <button class="card__button card__button--primary">按钮</button>
</div>
```

```css
/* Block */
.card {
}

/* Element */
.card__title {
}
.card__desc {
}
.card__button {
}

/* Modifier */
.card--featured {
}
.card__button--primary {
}
```

> 🍎 **比喻理解**：BEM 就像工厂零件编号——
>
> - `card` = 产品名称（卡片）
> - `__title` = 产品的组成部分（卡片的标题）
> - `--featured` = 产品的特殊型号（推荐版卡片）

> 💡 **BEM 优点**：
>
> - 命名清晰，一眼看出元素关系
> - 低特异性，不容易冲突
> - 组件化思维，便于维护

> ⚠️ **常见错误**：
>
> ```css
> /* 错误：过深的嵌套 */
> .card__list__item__title {
> }
>
> /* 正确：命名上保持扁平（不出现 `__` 后再接 `__`），DOM 结构中当然可以嵌套 */
> .product-list__item {
> }
> .product-list__title {
> }
>
> /* 不推荐：后代选择器会增加特异性，违背 BEM 低特异性原则 */
> /* 应直接写 .product-list__title { } */
> ```

#### 命名前缀（可选）

| 前缀           | 含义    | 示例                         | 比喻        |
| -------------- | ------- | ---------------------------- | ----------- |
| `l-`           | 布局    | `.l-container`、`.l-sidebar` | 房间布局    |
| `c-`           | 组件    | `.c-button`、`.c-card`       | 家具组件    |
| `u-`           | 工具类  | `.u-text-center`、`.u-mb-10` | 通用工具    |
| `js-`          | JS 钩子 | `.js-dropdown`               | JS 专用按钮 |
| `is-` / `has-` | 状态    | `.is-active`、`.has-error`   | 状态标签    |

### 10.2 CSS 性能优化

| 优化建议                             | 为什么                       | 比喻                                   |
| ------------------------------------ | ---------------------------- | -------------------------------------- |
| 避免过深的选择器（建议最多 3 层）    | 降低维护难度和特异性冲突风险 | 找人时层层传话太慢                     |
| 使用 `transform` 和 `opacity` 做动画 | GPU 加速，不触发重排         | 用传送门移动，不用走路                 |
| 合并同类型属性                       | 减少代码量                   | 把同类货物装在一个箱子里               |
| 移除无用 CSS                         | 减少文件大小                 | 扔掉不用的工具                         |
| 适度使用 `will-change`               | 动画前临时设置，结束后移除   | 提前告诉工厂准备特殊材料，但不用时撤掉 |

```css
/* 性能优化示例 */
/* ⚠️ will-change 不要在默认状态长期保留！会持续占用 GPU 内存 */
/* 推荐：通过 JS 在动画开始前添加 class，动画结束后移除 */
.animated-element {
  transition: transform 0.3s;
}

.animated-element.is-active {
  will-change: transform;
  transform: translateX(10px);
}
```

### 10.3 现代 CSS 工具

| 工具             | 说明                                 | 比喻             |
| ---------------- | ------------------------------------ | ---------------- |
| **PostCSS**      | CSS 转换器，插件生态丰富             | 万能转换机       |
| **Sass/SCSS**    | 预处理器，支持变量、嵌套、混入、继承 | 高级机床         |
| **Less**         | 预处理器，类似 Sass                  | 另一种机床       |
| **Tailwind CSS** | Utility-First 框架，原子类           | 乐高积木         |
| **CSS-in-JS**    | 样式组件化（React 生态常用）         | 把样式缝在组件里 |

> 💡 **初学者建议**：先扎实掌握原生 CSS，再学 Sass 或 Tailwind。不要一开始就依赖工具。
>
> 🍎 **比喻**：先学会手工做椅子，再用机床批量生产。如果连榫卯结构都不懂，机床参数也调不好。

### ✅ 本节回顾

- [x] 理解 BEM 命名法的三个组成部分
- [x] 知道至少 3 条 CSS 性能优化建议
- [x] 了解 Sass、Tailwind 等现代工具的作用

### 📝 自测题

**1. BEM 中 `__` 连接的是？**

- A. Block 和 Modifier
- B. Block 和 Element
- C. Element 和 Modifier
- D. 两个 Modifier

**2. 以下哪个是性能较好的动画属性？**

- A. `width`
- B. `height`
- C. `transform`
- D. `margin`

**3. `.is-active` 这种前缀通常表示？**

- A. 布局
- B. 组件
- C. 状态
- D. 工具类

<details>
<summary>点击查看答案</summary>

1. **B**（Block\_\_Element）
2. **C**（transform 触发 GPU 加速）
3. **C**（is-/has- 前缀表示状态）

</details>

---

## 附录：CSS 属性选择决策图

```
我要修改...什么？
│
├─ 颜色 ───────────→ background-color / color / border-color
│
├─ 尺寸 ───────────→ width / height / font-size
│
├─ 间距 ───────────→ 内？→ padding / 外？→ margin
│
├─ 边框 ───────────→ border / border-radius
│
├─ 位置 ───────────→ 一维？→ Flexbox / 二维？→ Grid / 堆叠？→ position + z-index
│
├─ 背景 ───────────→ background / background-image
│
├─ 阴影 ───────────→ box-shadow / text-shadow
│
└─ 动画 ───────────→ 简单？→ transition / 复杂？→ animation + @keyframes
```

---

## 附录：学习资源与建议

### 推荐资源

| 资源         | 链接                                                                                         | 用途                 |
| ------------ | -------------------------------------------------------------------------------------------- | -------------------- |
| MDN          | [developer.mozilla.org/zh-CN/docs/Web/CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) | 最权威的参考文档     |
| Can I Use    | [caniuse.com](https://caniuse.com)                                                           | 查浏览器兼容性       |
| CSS Triggers | [csstriggers.com](https://csstriggers.com)                                                   | 查属性触发的渲染阶段 |
| cubic-bezier | [cubic-bezier.com](https://cubic-bezier.com)                                                 | 贝塞尔曲线生成器     |
| Flexbox 游戏 | [flexboxfroggy.com](https://flexboxfroggy.com)                                               | 通过游戏学习 Flexbox |
| Grid 花园    | [cssgridgarden.com](https://cssgridgarden.com)                                               | 通过游戏学习 Grid    |

### 学习建议

1. **先学基础**：选择器、盒模型、常用属性 → 会改颜色、字体、间距
2. **掌握布局**：先理解文档流和定位 → 再学 Flexbox → 最后 Grid
3. **多动手**：做一个完整的响应式页面（从手机到桌面）
4. **善用 DevTools**：实时调试、理解渲染机制、查看计算样式
5. **阅读源码**：看优秀开源项目（如 shadcn/ui）的 CSS 写法
6. **刻意练习**：每天实现一个小组件（按钮、卡片、导航栏、表单）

### 学习检查清单

```
□ 能独立写出一个静态网页（导航 + 内容 + 页脚）
□ 能用 Flexbox 实现常见布局（居中、等分、两端对齐）
□ 能用 Grid 实现响应式网格
□ 能用媒体查询适配手机、平板、桌面
□ 能写出平滑的悬停过渡效果
□ 能使用 CSS 变量管理主题色
□ 能解释清楚盒模型和选择器优先级
```

> 完成以上清单，代表你已经掌握了 CSS 的核心技能，可以进入现代 CSS 框架（Tailwind、Styled-Components等）的学习了！

---

## 终极自测综合题

### 选择题

**1. 盒模型中，背景色会延伸到哪个区域？**

- A. margin
- B. border
- C. padding
- D. 以上全部

**2. 一个元素设置 `width: 200px; padding: 20px; border: 2px solid; margin: 10px; box-sizing: border-box`，它的总宽度（包含 margin）是？**

- A. 200px
- B. 220px
- C. 244px
- D. 264px

**3. `#header .nav a` 和 `.nav a` 同时作用在一个元素上，哪个优先级更高？**

- A. `.nav a`
- B. `#header .nav a`
- C. 一样高
- D. 看谁先写

**4. 以下哪个不是 Flexbox 的属性？**

- A. `justify-content`
- B. `align-items`
- C. `grid-template-columns`
- D. `flex-wrap`

**5. 移动优先的响应式设计，媒体查询应该用？**

- A. `max-width`
- B. `min-width`
- C. `max-height`
- D. `orientation`

**6. `transition: all 0.3s ease` 中，`ease` 表示？**

- A. 匀速
- B. 慢-快-慢
- C. 慢开始
- D. 慢结束

**7. BEM 命名中，`.card--featured` 的 `--featured` 是？**

- A. Block
- B. Element
- C. Modifier
- D. 都不是

### 判断题

**8. `display: none` 和 `visibility: hidden` 效果完全相同。**

**9. 行内元素（inline）可以设置 width 和 height。**

**10. `position: absolute` 的元素会脱离正常文档流。**

**11. `flex: 1` 是 `flex-grow: 1; flex-shrink: 1; flex-basis: 0%` 的简写。**

**12. CSS 变量可以在 JavaScript 中动态修改。**

<details>
<summary>点击查看答案</summary>

**选择题：**

1. **B**（默认 `background-clip: border-box` 下，背景色延伸到 border 区域，包含 content + padding + border）
2. **B**（border-box 下 width 200px 包含 content+padding+border，再加 margin 左右各 10px = 220px）
3. **B**（`#header .nav a` = (0,1,1,1)，`.nav a` = (0,0,1,1)，ID选择器胜出）
4. **C**（grid-template-columns 是 Grid 的属性）
5. **B**（移动优先用 min-width）
6. **B**（ease 是慢-快-慢）
7. **C**（-- 是 Modifier）

**判断题：** 8. **错误**（display:none 不占空间，visibility:hidden 占位）9. **错误**（inline 不能设置宽高，inline-block 可以）10. **正确**（absolute 脱离文档流）11. **正确**（flex: 1 是简写）12. **正确**（JS 可以 setProperty 修改 CSS 变量）

</details>

---

> 本文档持续更新中。如有疑问或建议，欢迎交流探讨。
