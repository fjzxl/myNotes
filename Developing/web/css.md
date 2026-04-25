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

| 读者类型 | 阅读建议 |
|---------|---------|
| **完全新手** | 按顺序阅读，每个阶段先读**比喻理解**，再做**自测题**，最后完成**动手练习** |
| **有一定基础** | 跳过熟悉内容，重点看 🔴 **重难点** 和 ⚠️ **易错点** |
| **速查参考** | 善用目录和 `Ctrl+F` 搜索关键词 |

**文档符号说明**：
- 🍎 **生活比喻**：用日常事物类比 CSS 概念
- 🔴 **重难点**：必须掌握的核心概念
- ⚠️ **易错点**：初学者常犯的错误
- 💡 **记忆口诀**：帮助记忆的顺口溜
- 📝 **自测题**：检验理解程度的选择题/判断题
- ✏️ **动手练习**：可执行的代码练习

---

## 核心概念速查

| 概念 | 一句话理解 | 生活比喻 |
|------|-----------|---------|
| **选择器** | 告诉浏览器"我要改哪个元素" | 就像老师点名："第三排穿红衣服的同学" |
| **属性** | 告诉浏览器"我要改它的什么" | 就像说："把头发染成蓝色" |
| **值** | 告诉浏览器"改成什么样" | 就像说："染成深蓝色 #00008B" |
| **盒模型** | 每个元素都是一个盒子，由 content + padding + border + margin 组成 | 就像快递盒：商品 + 气泡膜 + 纸箱 + 两个箱子间的距离 |
| **选择器优先级** | 多个样式冲突时，优先级高的生效 | 就像游戏规则：校长发话 > 班主任 > 班干部 > 普通学生（先比官职，同级再比人数）|
| **Flexbox** | 一维布局，沿主轴排列 | 就像排队：可以横着排，也可以竖着排 |
| **Grid** | 二维布局，同时控制行和列 | 就像棋盘：有横有竖，形成格子 |
| **Position** | 定位方式 | 就像人站在哪里：原地站(static)、站队时踮脚(relative)、站到操场角落(absolute) |
| **Z-Index** | 层叠顺序 | 就像一叠纸，数字大的在上面 |

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
把    h1    改成    颜色红色、大小24像素
↑     ↑           ↑
选择器  元素          属性:值
```

```css
h1 {
    color: red;
    font-size: 24px;
}
```

**语法规则**：
- 每个声明以 `;` 结尾（最后一行可省略，但建议写上）
- 属性和值之间用 `:` 分隔
- 多条声明用 `{}` 包裹
- CSS 选择器和属性名不区分大小写，但**习惯用小写**；类名和 ID 最好与 HTML 中保持完全一致（HTML 中区分大小写）

> ⚠️ **常见错误**：忘记写分号 `;` 导致后面的样式不生效！
> ```css
> /* 错误：第一行缺少分号 */
> h1 {
>     color: red
>     font-size: 24px;  /* 这行不会生效！ */
> }
> ```

### 1.2 三种引入方式

| 方式 | 代码写法 | 生活比喻 | 使用场景 |
|------|---------|---------|---------|
| **外部样式表** | `<link rel="stylesheet" href="style.css">` | 衣服放在衣柜里，谁想穿去拿 | ✅ 最推荐，样式与结构分离 |
| **内部样式表** | `<style>` 标签写在 HTML 的 `<head>` 中 | 把衣服标签缝在身上 | 小型页面或单页演示 |
| **行内样式** | `<div style="color: red;">` | 用马克笔直接画在身上 | ❌ 不推荐，优先级过高且难维护 |

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
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的第一个 CSS 页面</title>
    <!-- 外部样式表引入 -->
    <link rel="stylesheet" href="style.css">
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

### 1.3 注释

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

- [ ] 能说出 CSS 的作用和基本语法结构
- [ ] 知道三种引入方式，优先使用外部样式表
- [ ] 会写 CSS 注释
- [ ] 能打开开发者工具并找到 Styles 面板

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

| 表示方式 | 示例 | 说明 | 什么时候用 |
|----------|------|------|-----------|
| 颜色关键字 | `red`、`blue`、`black` | 147 个预定义颜色 | 快速测试、教学演示 |
| 十六进制 | `#ff0000`、`#f00` | 最常用，#RRGGBB | **日常开发首选** |
| RGB | `rgb(255, 0, 0)` | 红绿蓝三通道 | 需要动态计算颜色时 |
| RGBA | `rgba(255, 0, 0, 0.5)` | 带透明度（0~1） | **需要半透明时** |
| HSL | `hsl(0, 100%, 50%)` | 色相、饱和度、亮度 | 主题色系统、调整深浅 |
| HSLA | `hsla(0, 100%, 50%, 0.5)` | 带透明度的 HSL | 需要透明度的主题色 |

**💡 记忆口诀**：
> 日常开发用 **十六进制**，
> 半透明用 **RGBA**，
> 调深浅用 **HSL**。

> ⚠️ **重点**：`#fff` 是 `#ffffff` 的简写，`#f00` 是 `#ff0000` 的简写，书写更简洁！

> ⚠️ **常见错误**：`opacity` 设置透明度会**影响整个元素及其所有子元素**，而 `rgba` 只影响**当前属性**（如只让背景半透明，文字保持不透明）！
> ```css
> /* 错误：子元素也会变透明 */
> .parent { opacity: 0.5; }
>
> /* 正确：只有背景半透明，子元素不受影响 */
> .parent { background: rgba(0, 0, 0, 0.5); }
> ```

### 2.2 字体样式（Font）

| 属性 | 作用 | 常用值 | 生活比喻 |
|------|------|--------|---------|
| `font-size` | 字体大小 | `16px`、`1.2em`、`1rem` | 字多大，就像字号 |
| `font-family` | 字体族 | `"Microsoft YaHei", Arial` | 用什么字体，就像选钢笔/毛笔 |
| `font-weight` | 字重（粗细） | `normal`(400)、`bold`(700) | 笔的粗细 |
| `font-style` | 字体样式 | `normal`、`italic` | 正写还是斜写 |
| `line-height` | 行高 | `1.5`、`24px` | 行与行的间距 |

**字体栈写法**（从左到右依次回退）：

```css
body {
    font-family: "Helvetica Neue", Helvetica, Arial, "PingFang SC", "Microsoft YaHei", sans-serif;
}
```

> 🍎 **比喻理解**：字体栈就像"点名优先级"——
> 1. 先叫 `"Helvetica Neue"`（Mac 优先字体）
> 2. 不在？叫 `Helvetica`
> 3. 不在？叫 `Arial`（Windows 英文字体）
> 4. 不在？叫 `"PingFang SC"`（Mac 中文字体）
> 5. 不在？叫 `"Microsoft YaHei"`（Windows 中文字体）
> 6. 都不在？用系统默认的 `sans-serif`（无衬线字体）

**常用 font 简写**（按顺序：style weight size/line-height family）：

```css
body {
    font: 400 16px/1.5 "Microsoft YaHei", sans-serif;
}
```

> ⚠️ **注意**：简写时 `font-size` 和 `font-family` 是必填项，否则不生效。

### 2.3 文本排版（Text）

| 属性 | 作用 | 常用值 | 比喻 |
|------|------|--------|------|
| `text-align` | 水平对齐 | `left`、`center`、`right` | 文字在横线上怎么排 |
| `text-decoration` | 文本装饰 | `none`、`underline` | 加下划线、删除线 |
| `text-transform` | 大小写转换 | `uppercase`、`lowercase` | 全大写、全小写 |
| `letter-spacing` | 字间距 | `2px`、`0.05em` | 字与字的呼吸空间 |
| `word-spacing` | 词间距 | `4px` | 英文单词间的距离 |
| `white-space` | 空白处理 | `normal`、`nowrap` | 换不换行 |

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
    white-space: nowrap;      /* 不换行 */
    overflow: hidden;         /* 超出隐藏 */
    text-overflow: ellipsis;  /* 显示省略号 */
}

/* 多行省略（WebKit 浏览器） */
.multi-line {
    display: -webkit-box;         /* 弹性盒模型 */
    -webkit-line-clamp: 3;        /* 限制3行 */
    -webkit-box-orient: vertical; /* 垂直排列 */
    overflow: hidden;
}
```

> 💡 **记忆口诀**：单行省略三件套——**不换行、超出藏、省略号**。

> 🔴 **重难点**：`text-overflow: ellipsis` 必须配合 `white-space: nowrap` 和 `overflow: hidden` 才能生效，三者缺一不可！

### ✅ 本节回顾

- [ ] 能用至少两种方式设置颜色
- [ ] 会写字体栈，了解中文字体的回退策略
- [ ] 掌握 `text-align`、`text-decoration`、`letter-spacing` 的用法
- [ ] 能实现单行文字省略效果

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
a { text-decoration: none; }
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

1. 创建一个段落，设置文字颜色为深蓝 `#2c3e50`，字号 `18px`，行高 `1.8`
2. 给标题设置居中、大写、增加字间距
3. 实现一个固定宽度 200px 的容器，内部文字超出时显示省略号


---

## 第三阶段：盒模型 —— 理解元素的空间占用

> 🎯 **本节目标**：理解盒模型的四层结构，掌握 padding、border、margin 的写法，会使用 `border-box`，理解 display 模式。
>
> 盒模型是 CSS 中**最重要的概念**。不理解它，布局永远学不好。

### 🍎 生活比喻：盒模型就像快递包裹

想象你网购了一个杯子，收到快递时的包装：

```
┌─────────────────────────────────────┐
│                                     │
│            margin（外边距）           │  ← 两个快递盒之间的距离
│         "快递盒与快递盒的间距"         │
│  ┌─────────────────────────────────┐│
│  │                                 ││
│  │         border（边框）            ││  ← 纸箱的厚度
│  │         "纸箱的纸板厚度"           ││
│  │  ┌─────────────────────────────┐││
│  │  │                             │││
│  │  │      padding（内边距）        │││  ← 气泡膜、填充物
│  │  │      "保护商品的海绵层"        │││
│  │  │  ┌───────────────────────┐  │││
│  │  │  │                       │  │││
│  │  │  │    content（内容）      │  │││  ← 杯子本身
│  │  │  │    "你买的商品"          │  │││
│  │  │  │                       │  │││
│  │  │  └───────────────────────┘  │││
│  │  │                             │││
│  │  └─────────────────────────────┘││
│  │                                 ││
│  └─────────────────────────────────┘│
│                                     │
└─────────────────────────────────────┘
```

**关键记忆**：
- **content** = 杯子（你真正关心的东西）
- **padding** = 气泡膜（保护内部，背景色会延伸到这里）
- **border** = 纸箱边界（看得见的外壳）
- **margin** = 两个快递盒之间的距离（透明，背景色不会到这）

> 💡 **记忆口诀**：
> - **padding** = **p**adding = **内**部填充（背景色会延伸到这）
> - **margin** = **m**argin = **外**部间距（与其他盒子的距离）
> - **border** = 边界线，分隔内外

### 🔴 重难点：两种盒模型对比

这是初学者**最容易混淆**的概念！

| 特性 | content-box（默认） | border-box |
|------|-------------------|-----------|
| `width` 包含什么 | **只有 content** | content + padding + border |
| 设置 `width: 200px` 后的宽度 | 到 border 为止：200 + padding + border | 到 border 为止就是 200px（padding 和 border 被包含在内） |
| 生活比喻 | 你说"杯子宽 10cm"，但不包括包装 | 你说"整个包裹宽 10cm"，包含所有包装 |
| 计算难度 | 需要心算：总宽 = width + padding×2 + border×2 | 所见即所得 |

```css
/* 强烈推荐全局设置！ */
*, *::before, *::after {
    box-sizing: border-box;
}
```

> 🍎 **比喻理解**：
> - `content-box` = 你说"我的杯子宽 10cm"，但实际占地还要加上气泡膜和纸箱的厚度
> - `border-box` = 你说"整个包裹宽 10cm"，不管里面怎么包装，总占地就是 10cm

**直观对比**：

```css
/* 假设都设置 width: 200px, padding: 20px, border: 2px */

/* content-box 到 border 为止的宽度 = 200 + 40 + 4 = 244px（再加 margin 才是总占用） */
.box1 {
    box-sizing: content-box;
    width: 200px;
    padding: 20px;
    border: 2px solid red;
}

/* border-box 到 border 为止的宽度 = 200px（内容区会被压缩到 156px） */
.box2 {
    box-sizing: border-box;
    width: 200px;
    padding: 20px;
    border: 2px solid blue;
}
```

> ⚠️ **常见错误**：
> - 给 `span`、`a` 等行内元素设置 `width` 和 `height` 不生效（需要改为 `display: block` 或 `inline-block`）
> - 设置 `height: 100%` 不生效（需要**所有祖先元素**链路上都有确定高度，通常需要 `html, body { height: 100%; }`）

### 3.1 内容区（Content）

- `width`：设置内容宽度
- `height`：设置内容高度
- 默认只对块级元素生效

### 3.2 内边距（Padding）

元素**内部**的间距，背景色会延伸到 padding 区域。

```css
/* 四个方向 */
padding: 10px;                    /* 上下左右都是 10px */
padding: 10px 20px;               /* 上下 10px，左右 20px */
padding: 10px 20px 30px 40px;     /* 上、右、下、左（顺时针） */

/* 单独设置 */
padding-top: 10px;
padding-right: 20px;
padding-bottom: 30px;
padding-left: 40px;
```

> 💡 **记忆口诀**：顺时针，上右下左，对称时可以简写。

### 3.3 边框（Border）

```css
/* 简写：宽度 样式 颜色 */
border: 1px solid #ccc;

/* 单独设置 */
border-width: 2px;
border-style: dashed;   /* solid、dashed、dotted、double、none */
border-color: red;

/* 圆角 */
border-radius: 8px;             /* 统一圆角 */
border-radius: 8px 16px;        /* 左上+右下 / 右上+左下 */
border-radius: 50%;             /* 正圆（元素宽高相等时） */
```

> 💡 **常用边框技巧**：
> - 细线边框：`border: 1px solid #e0e0e0`
> - 无边框但占位：`border: 1px solid transparent`
> - 三角形（利用边框）：`border: 10px solid transparent; border-bottom-color: red;`

### 3.4 外边距（Margin）

元素**外部**的间距，背景色不会延伸到这里。

```css
margin: 10px;
margin: 10px auto;   /* 上下 10px，左右自动（水平居中常用） */
margin: 0 auto;      /* 块级元素水平居中 */
```

#### 🔴 重难点：垂直外边距合并

两个垂直相邻的块级元素，上下 margin 会**合并取最大值**，而不是相加。

```css
.box1 { margin-bottom: 20px; }
.box2 { margin-top: 30px; }
/* 实际间距是 30px，不是 50px！ */
```

> 🍎 **生活比喻**：就像两个人排队，每个人都说"我要和前面的人保持 20cm 距离"，"我要和后面的人保持 30cm 距离"——实际上他们只隔了 30cm，不是 50cm。

> ⚠️ **常见错误**：
> - 期望 `margin: 0 auto` 居中但元素没有设置宽度（块级元素默认宽度 100%，看不出居中）
> - 父元素包裹的子元素 `margin-top` "溢出"到父元素外（可用 `overflow: hidden` 或父元素加 `padding` 解决）

```css
/* 错误示例：子元素的 margin-top 会"溢出"到父元素外面 */
.parent {
    height: 100px;
}
.child {
    margin-top: 20px; /* 这个 margin 会溢出！ */
}

/* 推荐方案（无副作用，现代浏览器） */
.parent {
    display: flow-root;
}
/* 兼容旧浏览器的方案 */
.parent {
    overflow: hidden;   /* 注意：可能裁切溢出内容 */
}
```

### 3.5 元素的显示模式（Display）

| 值 | 特点 | 典型元素 | 生活比喻 |
|----|------|----------|---------|
| `block` | 独占一行，可设宽高 | `div`、`p`、`h1~h6` | 就像一人占一个座位 |
| `inline` | 共占一行，不可设宽高 | `span`、`a`、`strong` | 就像大家挤在一张长椅上 |
| `inline-block` | 共占一行，可设宽高 | `input`、`button`、`textarea` | 就像长椅上每个人有自己的固定座位 |
| `inline`（特殊） | 共占一行，默认可设宽高 | `img` | 就像长椅上的特殊座位（可替换元素） |
| `none` | 隐藏，不占空间 | — | 就像这个人从世界上消失了 |
| `flex` | 弹性盒布局 | — | 像军训排队，有队长指挥 |
| `grid` | 网格布局 | — | 像棋盘，横竖分明 |

```css
/* 行内转块级 */
span {
    display: block;
}

/* 块级转行内块（既能并排又能设宽高） */
.nav-item {
    display: inline-block;
    width: 100px;
    height: 40px;
}
```

> ⚠️ **常见坑**：`inline-block` 元素之间会出现约 4px 的空白间隙（来自 HTML 中的空格/换行）。
> - 解决方案1：父元素设置 `font-size: 0`，子元素再单独设置字体大小
> - 解决方案2：使用 Flexbox 替代（更推荐）

> ⚠️ **注意**：`display: none` 会让元素完全消失（不占空间），与 `visibility: hidden`（隐藏但占位）不同。

| 特性 | `display: none` | `visibility: hidden` |
|------|----------------|---------------------|
| 是否占空间 | ❌ 不占 | ✅ 占 |
| 是否可见 | ❌ 不可见 | ❌ 不可见 |
| 子元素状态 | 也消失 | 默认也隐藏（可单独设置可见） |
| 生活比喻 | 这个人消失了 | 这个人隐形了，但位置还在 |

### ✅ 本节回顾

- [ ] 能用"快递盒"比喻解释盒模型的四层
- [ ] 知道 padding 和 margin 的区别
- [ ] 会用简写设置四个方向的内边距/外边距
- [ ] 理解 `border-box` 的优势，会全局设置
- [ ] 知道 block、inline、inline-block 的区别
- [ ] 理解垂直外边距合并现象

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

### 4.1 基础选择器

| 选择器 | 示例 | 含义 | 比喻 |
|--------|------|------|------|
| 通配选择器 | `*` | 选中所有元素 | 给所有人 |
| 标签选择器 | `div`、`p` | 选中所有该标签 | 给所有男生/女生 |
| 类选择器 | `.className` | 选中 class 属性中包含该独立词的元素 | 给所有穿红衣服的 |
| ID 选择器 | `#idName` | 选中对应 id 的元素（页面唯一） | 给学号 001 的 |
| 属性选择器 | `[type="text"]` | 根据属性选中 | 给戴眼镜的 |

```css
/* 选中所有段落 */
p { color: #333; }

/* 选中 class="button" 的元素 */
.button { padding: 10px 20px; }

/* 选中 id="header" 的元素 */
#header { height: 60px; }

/* 选中 type="text" 的输入框 */
input[type="text"] { border: 1px solid #ccc; }
```

> 💡 **记忆口诀**：
> - 类选择器前面有个点 `.`，就像"点名叫你"
> - ID 选择器前面有个井号 `#`，就像"编号唯一"

### 4.2 复合选择器

| 选择器 | 写法 | 含义 | 比喻 |
|--------|------|------|------|
| 并集 | `h1, h2, p` | 选中 h1 或 h2 或 p | 给张三、李四、王五 |
| 后代 | `nav a` | 选中 nav 内的所有 a（无论多深） | 给教室里所有戴眼镜的 |
| 子选择器 | `ul > li` | 选中 ul 的直接子 li | 只给儿子辈的，不给孙子 |
| 相邻兄弟 | `h2 + p` | 选中紧跟 h2 后面的 p | 给坐在我后面那个人 |
| 通用兄弟 | `h2 ~ p` | 选中 h2 后面的所有 p | 给我后面所有人 |
| 交集 | `div.active` | 选中同时是 div 且有 active 类的 | 既是男生又戴眼镜的 |

```css
/* 后代选择器：选中导航里的所有链接 */
.nav a { color: #333; }

/* 子选择器：只选中直接子菜单项 */
.menu > li { display: inline-block; }

/* 交集选择器：选中同时满足两个条件的元素 */
div.highlight { background: yellow; }

/* 并集选择器：统一设置多个元素 */
h1, h2, h3 { font-weight: bold; }
```

> ⚠️ **常见错误**：
> - 以为 `ul li` 和 `ul > li` 一样（前者选中所有后代，后者只选直接子元素）
> - 空格很重要！`div.active`（交集，无空格）和 `div .active`（后代，有空格）完全不同！

### 4.3 伪类选择器（:）

**状态伪类**（与用户交互相关）：

| 伪类 | 触发条件 | 生活比喻 |
|------|----------|---------|
| `:hover` | 鼠标悬停 | 鼠标指着谁 |
| `:active` | 鼠标按下 | 正在按着的按钮 |
| `:focus` | 获得焦点 | 光标在输入框里 |
| `:visited` | 已访问的链接 | 去过的景点 |
| `:disabled` | 禁用的表单元素 | 坏了的开关 |
| `:checked` | 选中的单选/复选框 | 打勾的选项 |

**结构伪类**（根据元素在文档中的位置）：

| 伪类 | 含义 | 比喻 |
|------|------|------|
| `:first-child` | 第一个子元素 | 老大 |
| `:last-child` | 最后一个子元素 | 老幺 |
| `:nth-child(n)` | 第 n 个子元素 | 排名第 n 的 |
| `:nth-child(odd)` | 奇数位置的子元素 | 排名第1、3、5...的 |
| `:nth-child(even)` | 偶数位置的子元素 | 排名第2、4、6...的 |
| `:not(selector)` | 排除某个选择器 | 除了...之外的 |

```css
/* 鼠标悬停时变色 */
.button:hover { background: #2980b9; }

/* 斑马纹表格 */
tr:nth-child(even) { background: #f5f5f5; }

/* 排除最后一个元素 */
.nav-item:not(:last-child) { margin-right: 10px; }

/* 第一个段落不需要上边距 */
p:first-child { margin-top: 0; }
```

> 💡 **`:nth-child` 公式**：
> - `:nth-child(2n)` = 偶数项
> - `:nth-child(2n+1)` = 奇数项
> - `:nth-child(3n)` = 每 3 项
> - `n` 从 **0** 开始计算

### 4.4 伪元素选择器（::）

| 伪元素 | 作用 | 比喻 |
|--------|------|------|
| `::before` | 在元素内容前插入 | 在名字前面加"尊敬的" |
| `::after` | 在元素内容后插入 | 在名字后面加"同学" |
| `::first-line` | 选中第一行 | 只改第一段话 |
| `::first-letter` | 选中第一个字 | 只改第一个字 |
| `::selection` | 选中的文字 | 鼠标拖蓝的文字 |

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

| 选择器类型 | 权重（元组） | 比喻 |
|-----------|-------------|------|
| 行内样式 `style=""` | (1, 0, 0, 0) | 校长直接发话 |
| ID 选择器 `#id` | (0, 1, 0, 0) | 班主任 |
| 类/伪类/属性选择器 | (0, 0, 1, 0) × N | 班干部 |
| 标签/伪元素选择器 | (0, 0, 0, 1) × N | 普通学生 |
| 通配符 `*` | (0, 0, 0, 0) | 路人甲 |

> ℹ️ **`!important` 不是选择器，而是声明修饰符**：它会提升当前声明的优先级，但优先级比较仍以选择器特异性为基础（即两个 `!important` 声明之间，选择器特异性高的胜出）。注意：`!important` **不能**覆盖普通行内样式，只有行内样式自身的 `!important` 才能覆盖其他 `!important`。

**比较规则**：从高位到低位逐位比较，高位胜出则不再比较低位。
- 15个类选择器 `(0, 0, 15, 0)` 仍然小于 1个ID选择器 `(0, 1, 0, 0)`

```
#nav .menu li a    →  (0, 1, 1, 2)   即 1个ID, 1个类, 2个标签
.nav li a:hover    →  (0, 0, 2, 2)   即 0个ID, 2个类, 2个标签
```

> 🍎 **比喻理解**：优先级就像"官大一级压死人"。
> - 校长发话（行内样式）> 班主任（ID）> 班干部（类/伪类）> 普通学生（标签）
> - 先比官职等级，同级再比人数

> ⚠️ **常见错误**：
> - 用 `!important` 解决所有冲突（导致维护困难）
> - 写过度深的选择器链（超过 3 层）
> - 以为 10个类选择器能超过 1个ID选择器（实际是 `(0,0,10,0)` < `(0,1,0,0)`）

```css
/* 错误：滥用 !important */
.button { color: red !important; }

/* 正确：通过增加特异性来覆盖 */
.nav .button { color: blue; }  /* (0,0,2,0) > (0,0,1,0)，类选择器数量更多，优先级更高 */
```

### ✅ 本节回顾

- [ ] 能区分类选择器 `.class` 和 ID 选择器 `#id`
- [ ] 理解后代选择器 `nav a` 和子选择器 `ul > li` 的区别
- [ ] 会用 `:hover`、`:nth-child()`、`:not()` 伪类
- [ ] 会用 `::before`、`::after` 伪元素
- [ ] 能计算选择器优先级

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
tr:nth-child(even) { background: gray; }
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
5. **D**（1个ID + 2个类(`.menu`、`:hover`) + 2个标签(`li`、`a`) = **(0, 1, 2, 2)**）

</details>

### ✏️ 动手练习

1. 创建一个导航栏，用后代选择器设置链接颜色，用 `:hover` 设置悬停效果
2. 创建一个列表，用 `:nth-child(odd)` 实现斑马纹
3. 用 `::before` 在每个列表项前添加一个圆点装饰
4. 尝试计算 `#header .nav li a:hover` 的优先级（写出元组形式）


---

## 第五阶段：背景与装饰 —— 让页面更丰富

> 🎯 **本节目标**：能设置背景色、背景图、阴影和渐变，让页面更有层次感。

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
background-color: rgba(0, 0, 0, 0.5);   /* 半透明黑色 */
```

> 💡 **半透明背景技巧**：用 `rgba(255,255,255,0.9)` 做毛玻璃感遮罩，比纯色更高级。

### 5.2 背景图片

```css
background-image: url("bg.jpg"); /* 路径相对于 CSS 文件，不是 HTML 文件 */
background-repeat: no-repeat;            /* repeat、repeat-x、repeat-y */
background-position: center center;      /* 水平 垂直 */
background-size: cover;                  /* cover、contain、具体宽高 */
background-attachment: fixed;            /* 固定背景（视差效果） */
```

| `background-size` 值 | 效果 | 生活比喻 |
|---------------------|------|---------|
| `cover` | 等比缩放，完全覆盖容器（可能裁剪图片） | 把照片放大到铺满整个相框，边缘可能裁掉 |
| `contain` | 等比缩放，图片完整显示（可能有留白） | 把照片完整放进相框，留白边 |
| `100% 100%` | 拉伸填满（可能变形） | 强行拉变形铺满 |
| `auto` | 保持原始尺寸 | 原样展示 |

> 🔴 **重难点**：`cover` 和 `contain` 的区别是初学者最常搞混的！
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
box-shadow: 0 2px 4px rgba(0,0,0,0.1), 0 8px 16px rgba(0,0,0,0.1);  /* 多层阴影 */
box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);  /* 内阴影 */

/* 文字阴影 */
text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
```

> 🍎 **比喻理解**：`box-shadow` 的参数就像描述一个影子：
> - `0` = 影子在正下方（不左右偏）
> - `4px` = 影子向下偏移 4px
> - `8px` = 影子模糊程度（越大越模糊）
> - `rgba(0,0,0,0.1)` = 黑色的、很淡的影子

> 💡 **阴影层次感技巧**：
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
> - `to right`：从左到右
> - `to bottom right`：从左上到右下
> - `135deg`：角度写法，0deg 是从下到上，顺时针增加

### ✅ 本节回顾

- [ ] 会用 `background` 简写设置背景
- [ ] 理解 `background-size: cover` 和 `contain` 的区别
- [ ] 会写 `box-shadow` 和 `text-shadow`
- [ ] 能创建线性渐变背景

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

---

## 第六阶段：布局系统 —— 让元素各就各位

> 🎯 **本节目标**：理解文档流、定位、Flexbox 和 Grid，能选择合适的布局方式。
>
> 布局是 CSS 最难也最重要的部分。学习顺序：**正常流 → 定位 → Flexbox → Grid**。

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
│  行内  行内       │
└─────────────────┘
```

### 6.2 定位系统（Position）

| 值 | 说明 | 定位参考 | 生活比喻 |
|----|------|----------|---------|
| `static` | 默认，正常文档流 | — | 正常坐着 |
| `relative` | 相对定位 | 相对于自身原位置 | 站起来但椅子还占着 |
| `absolute` | 绝对定位 | 相对于最近的定位祖先 | 站到讲台角落 |
| `fixed` | 固定定位 | 相对于视口（默认） | 站在门口不动 |
| `sticky` | 粘性定位 | 滚动到阈值前像 relative，之后像 fixed | 粘在墙上的便利贴 |

```css
/* 相对定位：原位置保留，视觉偏移 */
.box {
    position: relative;
    top: 10px;      /* 向下移 10px */
    left: 20px;     /* 向右移 20px */
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
    top: 0;          /* 滚动到视口顶部时粘住 */
    z-index: 100;
}
```

#### 🔴 重难点：定位上下文（Containing Block）

`absolute` 元素相对于最近的 **定位祖先**（`position` 为非 `static`）。

> ⚠️ **特殊陷阱**：如果祖先设置了 `transform`、`perspective`、`filter`（不为 `none`）或 `will-change: transform`，也会成为定位参考！这甚至会让 `fixed` 元素"失效"。
> - `fixed` 默认相对于视口，但若祖先有上述属性，会相对于该祖先。

> 🍎 **比喻理解**：就像小孩找家长——
> - 先问爸爸：`position: relative?` → 是的话，就以爸爸为参考
> - 爸爸不是？问爷爷：`position: relative/absolute/fixed?`
> - 一直问到 `html`（祖宗），总会找到一个
>
> ⚠️ **`overflow: hidden` 不裁剪 absolute 子元素**！只有同时是定位参考的祖先的 `overflow: hidden` 才会生效。

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
> - 给子元素设置 `absolute` 但父元素没有设置定位，导致元素飞到页面角落
> - `fixed` 元素宽度默认收缩为内容宽度，需要手动设置 `width`

**z-index**：控制层叠顺序，数值越大越在上层。只在同一个**层叠上下文**中比较。

> ⚠️ **常见陷阱**：z-index 只在同一层叠上下文中有效！如果父元素创建了新的层叠上下文（如设置了 `opacity: 0.99`、`transform`、`filter`、`isolation: isolate`），子元素的 `z-index: 9999` 也无法突破父元素的层级！
> - Flex/Grid 容器的子项即使 `position: static`，设置 `z-index`（非 `auto`）也会创建层叠上下文并生效。

```css
.modal {
    position: fixed;
    z-index: 1000;    /* 弹窗要在最上层 */
}

.overlay {
    position: fixed;
    z-index: 999;     /* 遮罩层在弹窗下面 */
}
```

### 6.3 浮动（Float）—— 了解即可

```css
float: left;     /* 向左浮动 */
float: right;    /* 向右浮动 */
```

浮动最初用于**文字环绕图片**，现代布局中已被 Flexbox 和 Grid 取代。了解清除浮动即可：

```css
.clearfix::after {
    content: "";
    display: block;
    clear: both;
}
```

### 6.4 弹性布局（Flexbox）—— 一维布局

> Flexbox 是现代 CSS 布局的基石，**必须熟练掌握**。

#### 🍎 生活比喻：Flexbox 就像军训排队

- **容器（container）** = 教官
- **项目（items）** = 学生
- **主轴（Main Axis）** = 排队方向（默认横着排）
- **交叉轴（Cross Axis）** = 垂直于排队的方向（默认竖着）
- `justify-content` = 教官喊"沿排队方向看齐"
- `align-items` = 教官喊"沿垂直方向看齐"

```
Flexbox 布局示意：
┌──────────────────────────────────────┐
│  flex container（容器 = 教官）         │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐    │
│  │ item│ │ item│ │ item│ │ item│    │ ← flex items（学生）
│  └─────┘ └─────┘ └─────┘ └─────┘    │
│  ←────── 主轴（Main Axis）──────→    │
│  ↑                                   │
│  交叉轴（Cross Axis）                 │
│  ↓                                   │
└──────────────────────────────────────┘
```

#### 容器属性

| 属性 | 作用 | 常用值 | 比喻 |
|------|------|--------|------|
| `display: flex` | 开启 flex 布局 | — | 教官开始指挥 |
| `flex-direction` | 主轴方向 | `row`、`column` | 横着排还是竖着排 |
| `justify-content` | 主轴对齐 | `flex-start`、`center`、`flex-end`、`space-between` | 沿主轴方向怎么对齐 |
| `align-items` | 交叉轴对齐（每行内部） | `stretch`、`flex-start`、`center` | 沿交叉轴方向怎么对齐 |
| `align-content` | 多行时行与行的对齐 | 同 justify-content | 只有换行后才生效 |
| `flex-wrap` | 是否换行 | `nowrap`、`wrap` | 挤不下时换不换行 |
| `gap` | 项目间距 | `10px`、`1rem` | 学生之间的间距 |

**justify-content 图示**：

```
flex-start:    │▓▓  ▓▓  ▓▓        │
center:        │    ▓▓  ▓▓  ▓▓    │
flex-end:      │        ▓▓  ▓▓  ▓▓│
space-between: │▓▓        ▓▓      ▓▓│
space-around:  │  ▓▓    ▓▓    ▓▓  │
space-evenly:  │  ▓▓    ▓▓    ▓▓  │
```

> 💡 **记忆口诀**：
> - `justify-content` = **justify**（调整）**content**（内容）= 调整内容在主轴上的位置
> - `align-items` = **align**（对齐）**items**（项目）= 对齐项目在交叉轴上的位置
> - 想不清楚时记住：**justify 是主轴，align 是交叉轴**

#### 项目属性

| 属性 | 作用 | 比喻 |
|------|------|------|
| `flex-grow` | 放大比例（剩余空间分配） | 有多余空间时谁多长 |
| `flex-shrink` | 缩小比例（空间不足时） | 空间不够时谁先缩 |
| `flex-basis` | 初始大小 | 一开始占多大 |
| `flex` | 简写，常用 `flex: 1`（等价于 `1 1 0%`） | 上面三个的缩写 |
| `align-self` | 单独设置对齐方式 | 某个学生搞特殊 |
| `order` | 排列顺序 | 插队顺序 |

#### 常见 Flexbox 布局

```css
/* 水平垂直居中（最常用） */
.center {
    display: flex;
    justify-content: center;   /* 主轴居中 */
    align-items: center;       /* 侧轴居中 */
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
    flex-wrap: wrap;  /* 避免窄屏幕溢出 */
    gap: 20px;
}
.card {
    flex: 1 1 300px;   /* 基础宽度 300px，可 grow 也可 shrink */
    /* ⚠️ 如果只用 flex: 1，flex-basis 为 0%，每行只会放一个元素 */
}

/* 侧边栏 + 主内容 */
.layout {
    display: flex;
}
.sidebar {
    width: 200px;
    flex-shrink: 0;    /* 侧边栏不收缩 */
}
.main {
    flex: 1;            /* 主内容占满剩余空间 */
    min-width: 0;       /* ⚠️ 关键！允许 main 收缩到小于内容宽度，防止溢出 */
}
```

> 💡 **Flexbox 速查口诀**：
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

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }

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

| 场景 | 选择 | 比喻 |
|------|------|------|
| 一维排列（一行或一列） | **Flexbox** | 只排一队 |
| 二维网格（同时控制行列） | **Grid** | 排座位（有行有列） |
| 组件内部对齐（如按钮内图标和文字） | **Flexbox** | 调整一个小组件内部 |
| 整体页面布局 | **Grid** | 整个房间的座位安排 |
| 两者也可以结合使用 | 父 Grid + 子 Flex | 房间用 Grid，每个座位里的人用 Flex 调整姿势 |

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

- [ ] 理解 static、relative、absolute、fixed、sticky 的区别
- [ ] 知道 absolute 的定位上下文是什么
- [ ] 会用 Flexbox 实现水平垂直居中
- [ ] 会用 Grid 创建响应式网格布局
- [ ] 知道什么时候用 Flexbox，什么时候用 Grid

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
> - `@media (min-width: 768px)` = "如果屏幕宽度大于等于 768px，就执行这些样式"
> - 就像"如果房间大于 20 平米，就放一个大沙发"

#### 🔴 重难点：移动优先 vs 桌面优先

| 策略 | 写法 | 比喻 | 推荐度 |
|------|------|------|--------|
| **移动优先** | 先写小屏样式，再用 `min-width` 叠加 | 先设计小房子，再扩建大房子 | ✅ **强烈推荐**（渐进增强）|
| **桌面优先** | 先写大屏样式，再用 `max-width` 覆盖 | 先设计大房子，再拆成小房子 | ⚠️ 视场景而定（B端系统可考虑）|

```css
/* 移动优先写法（推荐） */
.card {
    /* 手机：全宽。块级元素默认就是 100%，此行可省略 */
    /* 如果显式设置 width: 100% 且有 padding，务必配合 box-sizing: border-box */
}

@media (min-width: 576px) {
    .card {
        width: 50%;        /* 平板：半宽 */
    }
}

@media (min-width: 992px) {
    .card {
        width: 33.33%;     /* 桌面：三分之一 */
    }
}
```

> 💡 **为什么推荐移动优先**：
> - 手机用户占比更高
> - CSS 默认就是无媒体查询的样式，从小屏开始写更自然
> - `min-width` 叠加比 `max-width` 覆盖更符合直觉

### 7.2 常用断点

| 名称 | 宽度范围 | 设备 | 比喻 |
|------|----------|------|------|
| 手机 | < 576px | 手机竖屏 | 小口袋 |
| 平板 | 576px - 768px | 手机横屏/小平板 | 书包 |
| 笔记本 | 768px - 991px | 大平板/小笔记本 | 公文包 |
| 桌面 | 992px - 1199px | 普通桌面 | 行李箱 |
| 大屏 | > 1200px | 大屏桌面 | 集装箱 |

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
    flex: 0 1 300px;   /* 不 grow、可 shrink、基础 300px，避免换行后拉伸 */
}
```

#### 🔴 重难点：`clamp()` 函数

`clamp(最小值, 首选值, 最大值)` —— 响应式神器！

> 🍎 **比喻理解**：就像汽车的定速巡航——
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
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

| 值 | 含义 | 比喻 |
|---|------|------|
| `width=device-width` | 视口宽度等于设备宽度 | 窗户多大房间就多大 |
| `initial-scale=1.0` | 初始缩放比例为 1 | 正常大小，不放大不缩小 |

> ⚠️ **不加 viewport 的后果**：手机浏览器会按桌面宽度渲染页面，导致文字极小，需要手动缩放。就像把一张大海报强行塞进小相框！

### ✅ 本节回顾

- [ ] 理解移动优先和桌面优先的区别，推荐移动优先
- [ ] 会写 `@media (min-width: 768px)` 媒体查询
- [ ] 知道常用断点范围
- [ ] 会设置 viewport meta 标签
- [ ] 会用 `clamp()` 实现响应式文字

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
4. **B**（576px-768px 是平板范围）

</details>

### ✏️ 动手练习

1. 创建一个卡片，手机全宽、平板两列、桌面三列（用媒体查询）
2. 用 `clamp()` 设置一个标题，手机 18px、桌面 32px、中间平滑过渡
3. 在浏览器开发者工具的设备模拟器中测试你的响应式页面

---

## 第八阶段：动画与交互 —— 让页面动起来

> 🎯 **本节目标**：掌握过渡、变换和动画，能写出常见交互效果。

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

**过渡属性**：

| 属性 | 说明 | 比喻 |
|------|------|------|
| `transition-property` | 要过渡的属性 | 调哪个开关 |
| `transition-duration` | 持续时间 | 调光用多久 |
| `transition-timing-function` | 时间函数 | 调光的速度曲线 |
| `transition-delay` | 延迟开始 | 等几秒再调 |

**常用时间函数**：

| 值 | 效果 | 比喻 |
|----|------|------|
| `ease` | 慢-快-慢（默认） | 汽车启动和刹车 |
| `linear` | 匀速 | 火车匀速行驶 |
| `ease-in` | 慢开始 | 火箭发射 |
| `ease-out` | 慢结束 | 汽车刹车 |
| `ease-in-out` | 对称的慢-快-慢 | 优雅的舞蹈 |

```css
/* 过渡多个属性 */
/* 💡 transition 必须写在基础状态，不要只写在 :hover 上，否则移出时没有过渡！ */
.card {
    transition: transform 0.3s ease, opacity 0.3s ease;
    opacity: 0.9;
}

.card:hover {
    transform: translateY(-5px);
    opacity: 1;
    box-shadow: 0 10px 20px rgba(0,0,0,0.15); /* 仅改变值，不过渡 */
}
```

> 💡 **性能提示**：过渡 `transform` 和 `opacity` 性能最好（GPU加速）。尽量避免过渡 `width`、`height`、`top`、`left`、`margin`、`padding`（触发重排），以及 `box-shadow`、`filter`（触发重绘）。

### 8.2 变换（Transform）

```css
/* 2D 变换 */
transform: translate(50px, 100px);   /* 平移 - 移动位置 */
transform: rotate(45deg);             /* 旋转 - 转多少度 */
transform: scale(1.5);                /* 缩放 - 放大缩小 */
transform: skew(10deg, 5deg);         /* 倾斜 - 斜着拉 */

/* 组合变换 */
/* ⚠️ transform 从右向左运算：先 translate（基于原始尺寸居中），再 scale */
transform: scale(1.1) translate(-50%, -50%);

/* 3D 变换：父元素需要设置 perspective 才能看到立体效果 */
.parent {
    perspective: 1000px;
}
.child {
    transform: rotateX(45deg);
}
```

> 🍎 **比喻理解**：
> - `translate` = 把照片从左边移到右边
> - `rotate` = 把照片转个角度
> - `scale` = 把照片放大或缩小
> - `skew` = 把照片斜着拉

> 💡 **居中技巧**：`position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);` 是元素绝对居中的经典方案。
> 
> 🍎 **为什么需要 translate(-50%, -50%)？** 因为 `top: 50%` 是把元素的**顶部**放在中间，不是把元素中心放在中间。`translate(-50%, -50%)` 就是把元素往回拉自身宽高的一半，让中心点对齐。

### 8.3 动画（Animation）

```css
/* 定义关键帧 */
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
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/* 使用动画 */
.element {
    opacity: 0;  /* 初始隐藏，避免动画加载前的闪烁（FOUC） */
    animation: slideUp 0.5s ease-out forwards;
}
```

> 🍎 **比喻理解**：`@keyframes` 就像电影分镜——
> - `0%` = 第一帧（电影开场）
> - `50%` = 中间帧（高潮）
> - `100%` = 最后一帧（结局）
> - `forwards` = 演完保持最后一帧的姿势（不散场）

**动画属性**：

| 属性 | 说明 | 比喻 |
|------|------|------|
| `animation-name` | 关键帧名称 | 电影名字 |
| `animation-duration` | 持续时间 | 电影时长 |
| `animation-timing-function` | 时间函数 | 播放速度曲线 |
| `animation-delay` | 延迟 | 开场前的广告时间 |
| `animation-iteration-count` | 循环次数 | 循环播放几次 |
| `animation-direction` | 方向 | 正放还是倒放 |
| `animation-fill-mode` | 结束后状态 | 演完保持什么姿势 |

### 8.4 过渡 vs 变换 vs 动画对比

| 特性 | Transition | Transform | Animation |
|------|-----------|-----------|-----------|
| 触发方式 | 状态变化（如 hover） | 立即生效 | 自动播放或触发 |
| 中间状态 | 自动计算 | 无（瞬间变化） | 需定义关键帧 |
| 循环播放 | ❌ 不能 | ❌ 不能 | ✅ 可以 |
| 适用场景 | 简单状态过渡 | 变形、位移 | 复杂动画 |
| 生活比喻 | 调光开关 | 换姿势 | 完整电影 |

> 💡 **实际开发中**：三者常配合使用。`transform` 负责变形，`transition` 负责平滑过渡，`animation` 负责复杂关键帧动画。

### 8.5 毛玻璃效果

```css
.glass {
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(10px);  /* Safari 兼容 */
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.3);
}
/* ⚠️ backdrop-filter 会创建新的层叠上下文，且旧浏览器不支持 */
```

> 🍎 **比喻理解**：就像磨砂玻璃——你看不清玻璃后面的东西，但能看到模糊的轮廓。`blur(10px)` 就是模糊程度。

### ✅ 本节回顾

- [ ] 会写 `transition` 实现悬停效果
- [ ] 会用 `transform` 实现位移、旋转、缩放
- [ ] 会定义 `@keyframes` 并使用 `animation`
- [ ] 知道什么时候用 transition，什么时候用 animation

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


---

## 第九阶段：现代 CSS 进阶特性

> 🎯 **本节目标**：掌握 CSS 变量、常用函数和现代属性。

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
    color: var(--undefined-var, black);   /* 变量不存在时使用黑色 */
}

> 🍎 **比喻理解**：
> - `:root` = 大楼的总设计图（全局生效）
> - `.card` 里的 `--card-padding` = 某个房间的特殊要求（只在这个房间生效）
> - `var(--color, black)` = "如果有这个颜色就用，没有就用黑色兜底"

> 💡 **变量优势**：
> - 一处修改，全局生效（换主题色特别方便）
> - 可以在运行时通过 JS 修改
> - 遵循 CSS 级联规则，可局部覆盖

```js
// JavaScript 修改变量（实现换肤功能）
document.documentElement.style.setProperty('--primary-color', '#e74c3c');
```

### 9.2 CSS 函数

| 函数 | 说明 | 示例 | 比喻 |
|------|------|------|------|
| `calc()` | 四则运算 | `width: calc(100% - 40px)` | 计算器 |
| `min()` | 取最小值 | `width: min(100%, 800px)` | 选两个数中较小的 |
| `max()` | 取最大值 | `font-size: max(1rem, 2vw)` | 选两个数中较大的 |
| `clamp()` | 范围限制 | `font-size: clamp(1rem, 2.5vw, 2rem)` | 限速器（不低于、不超过） |
| `minmax()` | Grid 轨道范围 | `repeat(3, minmax(200px, 1fr))` | 区间范围 |
| `repeat()` | 重复轨道 | `repeat(4, 1fr)` | 批量复制 |
| `var()` | CSS 变量 | `var(--color)` | 引用变量 |

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
    -webkit-mask-image: linear-gradient(to bottom, black, transparent); /* Safari 兼容 */
    mask-image: linear-gradient(to bottom, black, transparent);
}
```

> 🍎 **比喻理解**：
> - `clip-path` = 用剪刀把照片剪成特定形状（圆形、多边形）
> - `mask` = 给照片盖上一层灰度纱布，**不透明（黑/白/灰）**的部分显示照片，**透明**的部分隐藏照片。浏览器根据遮罩层的 alpha/亮度决定显示程度。

### ✅ 本节回顾

- [ ] 会定义和使用 CSS 变量
- [ ] 会用 `calc()`、`clamp()`、`min()`、`max()`
- [ ] 了解 `clip-path` 的作用

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
.card { }

/* Element */
.card__title { }
.card__desc { }
.card__button { }

/* Modifier */
.card--featured { }
.card__button--primary { }
```

> 🍎 **比喻理解**：BEM 就像工厂零件编号——
> - `card` = 产品名称（卡片）
> - `__title` = 产品的组成部分（卡片的标题）
> - `--featured` = 产品的特殊型号（推荐版卡片）

> 💡 **BEM 优点**：
> - 命名清晰，一眼看出元素关系
> - 低特异性，不容易冲突
> - 组件化思维，便于维护

> ⚠️ **常见错误**：
> ```css
> /* 错误：过深的嵌套 */
> .card__list__item__title { }
>
> /* 正确：命名上保持扁平（不出现 `__` 后再接 `__`），DOM 结构中当然可以嵌套 */
> .product-list__item { }
> .product-list__title { }
>
> /* 不推荐：后代选择器会增加特异性，违背 BEM 低特异性原则 */
> /* 应直接写 .product-list__title { } */
> ```

#### 命名前缀（可选）

| 前缀 | 含义 | 示例 | 比喻 |
|------|------|------|------|
| `l-` | 布局 | `.l-container`、`.l-sidebar` | 房间布局 |
| `c-` | 组件 | `.c-button`、`.c-card` | 家具组件 |
| `u-` | 工具类 | `.u-text-center`、`.u-mb-10` | 通用工具 |
| `js-` | JS 钩子 | `.js-dropdown` | JS 专用按钮 |
| `is-` / `has-` | 状态 | `.is-active`、`.has-error` | 状态标签 |

### 10.2 CSS 性能优化

| 优化建议 | 为什么 | 比喻 |
|---------|--------|------|
| 避免过深的选择器（建议最多 3 层） | 降低维护难度和特异性冲突风险 | 找人时层层传话太慢 |
| 使用 `transform` 和 `opacity` 做动画 | GPU 加速，不触发重排 | 用传送门移动，不用走路 |
| 合并同类型属性 | 减少代码量 | 把同类货物装在一个箱子里 |
| 移除无用 CSS | 减少文件大小 | 扔掉不用的工具 |
| 适度使用 `will-change` | 动画前临时设置，结束后移除 | 提前告诉工厂准备特殊材料，但不用时撤掉 |

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

| 工具 | 说明 | 比喻 |
|------|------|------|
| **PostCSS** | CSS 转换器，插件生态丰富 | 万能转换机 |
| **Sass/SCSS** | 预处理器，支持变量、嵌套、混入、继承 | 高级机床 |
| **Less** | 预处理器，类似 Sass | 另一种机床 |
| **Tailwind CSS** | Utility-First 框架，原子类 | 乐高积木 |
| **CSS-in-JS** | 样式组件化（React 生态常用） | 把样式缝在组件里 |

> 💡 **初学者建议**：先扎实掌握原生 CSS，再学 Sass 或 Tailwind。不要一开始就依赖工具。
> 
> 🍎 **比喻**：先学会手工做椅子，再用机床批量生产。如果连榫卯结构都不懂，机床参数也调不好。

### ✅ 本节回顾

- [ ] 理解 BEM 命名法的三个组成部分
- [ ] 知道至少 3 条 CSS 性能优化建议
- [ ] 了解 Sass、Tailwind 等现代工具的作用

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

1. **B**（Block__Element）
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

| 资源 | 链接 | 用途 |
|------|------|------|
| MDN | [developer.mozilla.org/zh-CN/docs/Web/CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) | 最权威的参考文档 |
| Can I Use | [caniuse.com](https://caniuse.com) | 查浏览器兼容性 |
| CSS Triggers | [csstriggers.com](https://csstriggers.com) | 查属性触发的渲染阶段 |
| cubic-bezier | [cubic-bezier.com](https://cubic-bezier.com) | 贝塞尔曲线生成器 |
| Flexbox 游戏 | [flexboxfroggy.com](https://flexboxfroggy.com) | 通过游戏学习 Flexbox |
| Grid 花园 | [cssgridgarden.com](https://cssgridgarden.com) | 通过游戏学习 Grid |

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

**判断题：**
8. **错误**（display:none 不占空间，visibility:hidden 占位）
9. **错误**（inline 不能设置宽高，inline-block 可以）
10. **正确**（absolute 脱离文档流）
11. **正确**（flex: 1 是简写）
12. **正确**（JS 可以 setProperty 修改 CSS 变量）

</details>

---

> 本文档持续更新中。如有疑问或建议，欢迎交流探讨。
