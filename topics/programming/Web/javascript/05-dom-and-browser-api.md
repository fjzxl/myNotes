---
title: "JavaScript 核心知识体系 · 五、DOM 操作与浏览器 API"
tags:
  - programming
  - javascript
created: 2026-09-10
updated: 2026-10-01
---

# 五、DOM 操作与浏览器 API

> 📚 本文是 [[topics/programming/Web/javascript|JavaScript 核心知识体系]] 的第 5 / 8 章。 上一章：[[topics/programming/Web/javascript/04-asynchronous-programming|四、异步编程]] · 下一章：[[topics/programming/Web/javascript/06-es6-modern-features|六、ES6+ 现代特性]]


> **本章定位：** 从"语言本身"走向"与浏览器对话"。我们将学习如何通过 JavaScript 操控网页、响应用户交互、使用浏览器提供的各种能力。
>
> **学习路线：** DOM 核心（选元素、改元素）→ 事件系统（捕获、冒泡、委托）→ 浏览器 API（定时器、存储、网络、文件）→ 性能优化（减少重排、防抖节流、懒加载）→ 前端交互项目实战
>
> **本章统一示例页面：** 以下是一个完整的 HTML 页面结构，本章 5.1 ~ 5.4 的绝大部分代码示例均可直接在此页面中运行。建议将此代码保存为 `dom-demo.html` 并在浏览器中打开，边学边练。

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <title>DOM 操作学习示例</title>
  <style>
    .container { max-width: 600px; margin: 20px auto; padding: 20px; font-family: system-ui; }
    .section { margin-bottom: 30px; padding: 15px; border: 1px solid #e5e7eb; border-radius: 8px; }
    .list { list-style: none; padding: 0; }
    .item { padding: 10px; margin: 5px 0; background: #f3f4f6; border-radius: 4px; cursor: pointer; }
    .item.active { background: #dbeafe; border-left: 4px solid #2563eb; }
    .box { width: 50px; height: 50px; background: #3b82f6; margin: 10px 0; }
    .grandparent { padding: 20px; background: #fee2e2; }
    .parent { padding: 20px; background: #fef3c7; }
    .child { padding: 10px 20px; background: #d1fae5; border: none; cursor: pointer; }
    .gallery { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 10px; }
    .gallery img { width: 100%; height: 80px; object-fit: cover; border-radius: 4px; }
    #dropZone { border: 2px dashed #ccc; padding: 30px; text-align: center; color: #6b7280; margin-top: 10px; }
  </style>
</head>
<body>
  <div id="app" class="container">
    <h1 id="pageTitle">DOM 操作学习示例</h1>
    <p class="desc">本章 5.1 ~ 5.4 的代码示例均基于此页面结构运行</p>

    <!-- 5.1 DOM 核心：节点选择、增删改、样式 -->
    <section class="section" id="domSection">
      <h2>节点操作演示区</h2>
      <ul id="todoList" class="list">
        <li class="item" data-id="1">学习节点类型</li>
        <li class="item active" data-id="2">掌握选择器语法</li>
        <li class="item" data-id="3">理解增删改操作</li>
      </ul>
      <div id="contentBox" class="box"></div>
      <input type="text" id="nameInput" placeholder="输入名字" value="Alice">
    </section>

    <!-- 5.2 事件系统：事件流、绑定、委托 -->
    <section class="section" id="eventSection">
      <h2>事件演示区</h2>
      <div class="grandparent" id="eventGrandpa">
        <div class="parent" id="eventParent">
          <button class="child" id="eventBtn">点击观察事件流</button>
        </div>
      </div>
      <a href="https://example.com" id="demoLink">示例链接</a>
    </section>

    <!-- 5.3 浏览器 API：动画、存储、Fetch、文件 -->
    <section class="section" id="apiSection">
      <h2>浏览器 API 演示区</h2>
      <div id="animBox" class="box"></div>
      <button id="startAnim">开始动画</button>
      <button id="saveBtn">保存到 localStorage</button>
      <div id="weatherResult"></div>
    </section>

    <!-- 5.4 性能优化：懒加载、防抖节流、拖放 -->
    <section class="section" id="perfSection">
      <h2>性能优化演示区</h2>
      <div class="gallery" id="imgGallery">
        <img data-src="https://picsum.photos/200/200?random=1" alt="图1">
        <img data-src="https://picsum.photos/200/200?random=2" alt="图2">
        <img data-src="https://picsum.photos/200/200?random=3" alt="图3">
      </div>
      <input type="file" id="fileInput" accept="image/*">
      <div id="dropZone">拖拽图片到此处上传</div>
      <div id="scrollArea" style="height: 100px; overflow-y: auto; border: 1px solid #ddd; padding: 10px;">
        <p>滚动区域内容（用于测试节流）...</p>
        <p>滚动区域内容...</p>
        <p>滚动区域内容...</p>
        <p>滚动区域内容...</p>
        <p>滚动区域内容...</p>
        <p>滚动区域内容...</p>
      </div>
    </section>
  </div>
</body>
</html>
```

### 5.1 DOM 核心

#### 节点类型与层级关系

**一句话理解：** DOM（Document Object Model）是浏览器将 HTML 文档解析成的一棵**树形结构**，JavaScript 通过操作这棵树来改变网页内容和样式。

**家族关系类比：**
- 把 DOM 想象成一张家谱图
- `<html>` 是祖宗，`<body>` 是其子辈，`<div>`、`<p>` 是孙辈
- 同一辈分的兄弟节点就是 **兄弟（sibling）**

**DOM 树形结构示例：**

```html
<!-- 原始 HTML -->
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <div id="container">
      <h1>Hello</h1>
      <p>World</p>
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
      </ul>
    </div>
  </body>
</html>
```

```
Document (nodeType: 9)
│
└── html ELEMENT_NODE (nodeType: 1)
    │
    ├── head ELEMENT_NODE
    │   └── title ELEMENT_NODE
    │       └── "My Page" TEXT_NODE (nodeType: 3)
    │
    └── body ELEMENT_NODE
        └── div#container ELEMENT_NODE
            │
            ├── h1 ELEMENT_NODE ─── firstElementChild
            │   └── "Hello" TEXT_NODE
            │
            ├── p ELEMENT_NODE ───── nextElementSibling
            │   └── "World" TEXT_NODE
            │
            └── ul ELEMENT_NODE ──── lastElementChild
                │
                ├── li ELEMENT_NODE ── firstElementChild
                │   └── "Item 1" TEXT_NODE
                │
                └── li ELEMENT_NODE ── nextElementSibling / lastElementChild
                    └── "Item 2" TEXT_NODE
```

**图中关系标注：**
- `parentNode`：向上走一级（如 `h1.parentNode` → `div#container`）
- `children`：向下收集所有元素子节点（如 `div#container.children` → `[h1, p, ul]`）
- `firstElementChild` / `lastElementChild`：第一个 / 最后一个元素子节点
- `nextElementSibling` / `previousElementSibling`：横向的兄弟节点
- `childNodes`：包含文本节点（如 `title` 和 `title` 内的 `"My Page"` 之间的换行和缩进也是 TEXT_NODE）

**初学者常见错误：**
- ❌ 用 `childNodes` 遍历时没注意会把空格文本节点也算进去，导致得到意料之外的 `#text` 节点
- ✅ 建议优先使用 `children`、`firstElementChild` 等只返回元素节点的属性

**12 种节点类型（初学者重点掌握前 2 种）：**

| 节点类型 | 常量值 | 说明 | 示例 |
|---|---|---|---|
| `ELEMENT_NODE` | 1 | **元素节点**（最常用） | `<div>`、`<p>`、`<span>` |
| `TEXT_NODE` | 3 | **文本节点** | `Hello World` |
| `COMMENT_NODE` | 8 | 注释节点 | `<!-- 注释 -->` |
| `DOCUMENT_NODE` | 9 | 文档节点（根节点） | `document` |

```js
// 查看节点类型
const div = document.createElement('div');
console.log(div.nodeType); // 1
console.log(div.nodeName); // "DIV"

const text = document.createTextNode('hello');
console.log(text.nodeType); // 3
console.log(text.nodeName); // "#text"
```

**节点层级关系（属性速查）：**
```js
const child = document.querySelector('.item');

// 向上找
child.parentNode;        // 父节点（可能是元素或文档）
child.parentElement;     // 父元素节点（更常用）
child.closest('.list');  // 向上查找最近的匹配选择器的祖先

// 向下找
child.childNodes;        // 所有子节点（含文本、注释）
child.children;          // 仅元素子节点（常用）
child.firstElementChild; // 第一个元素子节点
child.lastElementChild;  // 最后一个元素子节点

// 横向找
child.previousElementSibling; // 上一个兄弟元素
child.nextElementSibling;     // 下一个兄弟元素
```

**初学者常见错误：**
- ❌ 用 `childNodes` 遍历时没注意会把空格文本节点也算进去，导致得到意料之外的 `#text` 节点
- ✅ 建议优先使用 `children`、`firstElementChild` 等只返回元素节点的属性

---

#### 节点选择与遍历

**选择器演进路线（从旧到新）：**

```js
// 1. 最古老的方式（按 ID / 标签 / 类名）
document.getElementById('header');          // 返回单个元素
document.getElementsByTagName('div');       // 返回 HTMLCollection（实时集合）
document.getElementsByClassName('active');  // 返回 HTMLCollection（实时集合）

// 2. 现代方式（CSS 选择器）
document.querySelector('.list > li:first-child');  // 返回第一个匹配的元素
document.querySelectorAll('.item');                // 返回 NodeList（静态快照）
```

**`querySelectorAll` vs `getElementsByClassName` 核心区别：**

```js
const items1 = document.querySelectorAll('.item');     // NodeList（静态）
const items2 = document.getElementsByClassName('item'); // HTMLCollection（实时）

// 动态性对比
const newItem = document.createElement('div');
newItem.className = 'item';
document.body.appendChild(newItem);

console.log(items1.length); // 不变（快照）
console.log(items2.length); // +1（实时更新）
```

> **一句话记住：** `querySelectorAll` 是拍照，拍完不再变；`getElementsBy*` 是直播，随时跟着 DOM 变。

**遍历节点：**
```js
const list = document.querySelector('.list');

// 方式 1：for...of（推荐，支持 break）
for (const child of list.children) {
  console.log(child.textContent);
}

// 方式 2：Array.from + 数组方法
Array.from(list.children).forEach(child => {
  console.log(child.className);
});

// 方式 3：ES6 展开运算符
[...list.children].map(child => child.dataset.id);
```

**初学者常见错误：**
- ❌ `querySelectorAll` 返回的是 NodeList，不能直接调用 `map`/`filter`
- ✅ 先用 `[...nodeList]` 或 `Array.from(nodeList)` 转为真数组再使用数组方法

---

#### 节点增删改与属性操作

**创建与插入节点：**
```js
// 1. 创建元素
const div = document.createElement('div');
div.textContent = 'Hello';
div.id = 'box';
div.className = 'container active';

// 2. 插入到 DOM
document.body.appendChild(div);           // 末尾追加（老方法）
parent.append(div, '文本', anotherDiv);   // 末尾追加（新方法，可插多个）
parent.prepend(div);                      // 开头插入
parent.before(div);                       // 插入到 parent 前面（同级）
parent.after(div);                        // 插入到 parent 后面（同级）

// 3. 替换与删除
oldElement.replaceWith(newElement);       // 替换
oldElement.remove();                      // 删除自己（现代方法）
parent.removeChild(oldElement);           // 删除子节点（老方法）
```

**属性操作：**
```js
const input = document.querySelector('#nameInput'); // 基于本章统一页面结构

// HTML 标准属性（推荐）
input.id = 'username';
input.type = 'text';
input.value = 'Alice';
input.disabled = true;

// 自定义数据属性 data-*
input.dataset.userId = '1001';      // 对应 HTML 中 data-user-id="1001"
input.dataset.role = 'admin';       // 对应 data-role="admin"
console.log(input.dataset);          // DOMStringMap { userId: '1001', role: 'admin' }

// classList（操作类名的最佳方式）
const box = document.querySelector('#contentBox'); // 基于本章统一页面结构
box.classList.add('active', 'visible');
box.classList.remove('hidden');
box.classList.toggle('expanded');   // 有则删，无则加
box.classList.contains('active');   // true/false
box.classList.replace('old', 'new');
```

**innerHTML vs textContent vs innerText：**

| 属性 | 是否解析 HTML | 是否触发重排 | XSS 风险 | 性能 |
|---|---|---|---|---|
| `innerHTML` | ✅ 解析标签 | 是 | ⚠️ 高 | 慢（需解析 HTML 字符串） |
| `textContent` | ❌ 纯文本 | 是 | ✅ 安全 | 快（不解析标签） |
| `innerText` | ❌ 纯文本 | 是 | ✅ 安全 | 慢（会计算 CSS 样式） |

```js
const div = document.querySelector('#contentBox'); // 基于本章统一页面结构

// textContent：不解析 HTML，性能最好
div.textContent = '<script>alert(1)</script>'; // 页面上显示为纯文本

// innerHTML：解析 HTML，有 XSS 风险，必须转义用户输入
div.innerHTML = '<b>加粗</b>'; // 页面上显示加粗文字

// innerText：会受 CSS 影响（如 display:none 的元素内容不会被读取）
```

**初学者常见错误：**
- ❌ 直接将用户输入拼接进 `innerHTML`，导致 XSS 攻击
- ✅ 用户输入一律用 `textContent` 插入，或先用 `DOMPurify` 等库消毒

---

#### 样式操作与重排重绘优化

**修改样式的三种方式（从差到好）：**

```js
const box = document.querySelector('#contentBox'); // 基于本章统一页面结构

// ❌ 最差：直接修改 style（难以维护，优先级过高）
box.style.width = '100px';
box.style.height = '100px';
box.style.backgroundColor = 'red'; // 注意驼峰命名

// ✅ 推荐：通过 classList 切换类名（样式在 CSS 中集中管理）
box.classList.add('active');
box.classList.remove('hidden');

// ✅ 批量修改 style 时的兜底方案
box.style.cssText = 'width:100px; height:100px; background:red;';
```

**获取计算样式：**
```js
// getComputedStyle 返回元素最终应用的样式（含 CSS 文件和内联样式）
const style = window.getComputedStyle(box);
console.log(style.width);        // "100px"
console.log(style.color);        // "rgb(255, 0, 0)"
console.log(style.marginTop);    // 即使是 margin: 10px，也会解析为 marginTop
```

**重排（Reflow）与重绘（Repaint）：**

浏览器渲染页面的流程：

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  DOM 树     │     │   布局计算   │     │   绘制像素   │     │   合成图层   │
│  CSSOM 树   │ ──▶ │  (Reflow)   │ ──▶ │  (Paint)    │ ──▶ │ (Composite) │
│             │     │ 计算几何位置 │     │ 填充颜色样式 │     │  GPU 加速   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
     ↑                                                              ↑
     └──────────── 修改样式/结构会触发重排 ─────────────────────────┘
```

- **重排（Reflow）**：元素的几何属性（尺寸、位置）发生变化，浏览器需要重新计算布局。**代价最大**。
- **重绘（Repaint）**：元素的外观属性（颜色、背景、可见性）发生变化，不影响布局。**代价较小**。

**触发重排的操作（避免频繁执行）：**
```js
// 读取布局属性（会导致浏览器强制同步布局）
const width = element.offsetWidth;
const height = element.offsetHeight;
const rect = element.getBoundingClientRect();

// 写入布局属性
element.style.width = '200px';
element.style.marginLeft = '10px';
```

> **一句话记住：** 先读后写会触发两次布局；读写分离、批量处理可减少重排。

**批量操作减少重排：**
```js
// ❌ 每次循环都触发重排
const list = document.querySelector('.list');
for (let i = 0; i < 100; i++) {
  list.innerHTML += `<li>Item ${i}</li>`; // ⚠️ 每次都会序列化全部 DOM → 拼接 → 重新解析，O(n²) 性能灾难！
}

// ✅ 方案 1：DocumentFragment（内存中组装，一次性插入）
const fragment = document.createDocumentFragment();
for (let i = 0; i < 100; i++) {
  const li = document.createElement('li');
  li.textContent = `Item ${i}`;
  fragment.appendChild(li);
}
list.appendChild(fragment); // 只触发 1 次重排

// ✅ 方案 2：innerHTML 字符串拼接（1 次解析）
let html = '';
for (let i = 0; i < 100; i++) {
  html += `<li>Item ${i}</li>`;
}
list.innerHTML = html;

// ✅ 方案 3：先隐藏再操作（脱离文档流，操作完再显示）
const originalDisplay = list.style.display;
list.style.display = 'none';
// ... 大量 DOM 操作 ...
list.style.display = originalDisplay; // 恢复原来的显示模式
```

**CSS 动画优化：**
```css
/* 触发 GPU 加速的属性（只触发合成层，不触发重排重绘） */
.animated {
  transform: translateX(100px);
  opacity: 0.5;
  will-change: transform; /* 提前告知浏览器准备优化 */
}
```

> **黄金法则：** 优先使用 `transform` 和 `opacity` 做动画，它们几乎不触发重排。

**初学者常见错误：**
- ❌ 在循环中反复读取 `offsetWidth` 再写入样式，导致浏览器强制同步布局（Forced Synchronous Layout）
- ✅ 先集中读取所有布局属性，存储到变量中，再集中写入样式


### 5.2 事件系统

#### 事件流（捕获 / 目标 / 冒泡）

**一句话理解：** 当用户点击一个按钮时，这个点击事件不是只发生在按钮上，而是从 `window` 一路传递到按钮，再从按钮传回 `window`。这个过程分为三个阶段。

**水流类比：**
- 把 DOM 树想象成一条河，`<html>` 是上游，目标元素是下游
- **捕获阶段**：事件从上游（window）往下游（目标）流
- **目标阶段**：事件到达目标元素本身
- **冒泡阶段**：事件从下游往回流，直到 window

```
window → document → html → body → div → button(目标) → div → body → html → document → window
  |________ 捕获阶段 ________|   |目标|   |________ 冒泡阶段 ________|
```

```js
// 验证事件流的三个阶段
const grandparent = document.querySelector('.grandparent');
const parent = document.querySelector('.parent');
const child = document.querySelector('.child');

// 第三个参数 useCapture = true，表示在捕获阶段监听
grandparent.addEventListener('click', () => console.log('grandparent 捕获'), true);
parent.addEventListener('click', () => console.log('parent 捕获'), true);
child.addEventListener('click', () => console.log('child 目标'));
parent.addEventListener('click', () => console.log('parent 冒泡'));
grandparent.addEventListener('click', () => console.log('grandparent 冒泡'));

// 点击 child，控制台输出顺序：
// grandparent 捕获 → parent 捕获 → child 目标 → parent 冒泡 → grandparent 冒泡
```

**`event` 对象上的阶段属性：**
```js
element.addEventListener('click', (e) => {
  console.log(e.eventPhase);
  // 1: CAPTURING_PHASE（捕获阶段）
  // 2: AT_TARGET（目标阶段）
  // 3: BUBBLING_PHASE（冒泡阶段）
});
```

**初学者常见错误：**
- ❌ 以为事件只发生在目标元素上，忽略了事件流机制
- ✅ 理解事件流是利用事件委托和排查事件冲突的基础

---

#### 事件绑定与移除

**`addEventListener` 是标准的事件绑定方式：**

```js
const btn = document.querySelector('#eventBtn'); // 基于本章统一页面结构

// 基础绑定
btn.addEventListener('click', handleClick);

// 带选项的绑定
btn.addEventListener('click', handleClick, {
  capture: false,  // 是否在捕获阶段触发（默认 false，即在冒泡阶段触发）
  once: true,      // 只触发一次，触发后自动移除监听
  passive: true    // 告知浏览器不会调用 preventDefault()，可提升滚动性能
});
```

**`capture` 选项对事件流的深层影响：**

`capture` 只决定监听器在**哪条路上被触发**，但不会影响事件流本身的路径。事件依然会从 `window` → 目标 → `window` 走完整的三阶段流程。

```js
const grandpa = document.querySelector('#eventGrandpa');
const parent = document.querySelector('#eventParent');
const btn = document.querySelector('#eventBtn');

// 捕获阶段监听器（从外向内）
grandpa.addEventListener('click', () => console.log('grandpa 捕获'), true);
parent.addEventListener('click', () => console.log('parent 捕获'), true);
btn.addEventListener('click', () => console.log('btn 捕获'), true);

// 冒泡阶段监听器（从内向外）
grandpa.addEventListener('click', () => console.log('grandpa 冒泡'), false);
parent.addEventListener('click', () => console.log('parent 冒泡'), false);
btn.addEventListener('click', () => console.log('btn 冒泡'), false);

// 点击 btn，控制台输出顺序：
// grandpa 捕获 → parent 捕获 → btn 捕获 → btn 冒泡 → parent 冒泡 → grandpa 冒泡
```

**关键发现：目标阶段的特殊行为**

当事件到达**目标元素本身**时，`capture: true` 和 `capture: false` 的监听器**都会触发**，且按照**注册顺序**执行：

```js
const btn = document.querySelector('#eventBtn');

btn.addEventListener('click', () => console.log('1. 冒泡绑定'), false);
btn.addEventListener('click', () => console.log('2. 捕获绑定'), true);
btn.addEventListener('click', () => console.log('3. 冒泡绑定2'), false);

// 点击 btn，输出：
// 1. 冒泡绑定 → 2. 捕获绑定 → 3. 冒泡绑定2
// 在目标元素上，capture 选项失效，只按注册顺序执行！
```

**`stopPropagation()` 在不同阶段的作用差异：**

```js
// 场景 1：在捕获阶段阻止传播
grandpa.addEventListener('click', (e) => {
  console.log('grandpa 捕获');
  e.stopPropagation(); // 事件不会再向下传递到 parent 和 btn
}, true);

// 场景 2：在冒泡阶段阻止传播
btn.addEventListener('click', (e) => {
  console.log('btn 冒泡');
  e.stopPropagation(); // 事件不会再向上冒泡到 parent 和 grandpa
});

// 场景 3：在目标元素上阻止传播
btn.addEventListener('click', (e) => {
  e.stopPropagation();
  // 阻止了冒泡，但 btn 上其他监听器仍然会继续执行！
  // 因为 stopPropagation 只影响传播方向，不影响同一元素上的其他监听器
});
```

> **一句话总结：** `capture` 选项只控制监听器在"去程"还是"回程"被调用；在目标元素上，所有监听器都会执行。`stopPropagation()` 在捕获阶段能"截断去路"，在冒泡阶段能"阻断归途"。

**`once` 与 `passive` 的独立作用域：**

| 选项 | 影响捕获阶段 | 影响冒泡阶段 | 影响目标阶段 | 说明 |
|---|---|---|---|---|
| `capture: true` | ✅ 触发 | ❌ 不触发 | ✅ 触发（与注册顺序有关） | 只在去程触发 |
| `capture: false` | ❌ 不触发 | ✅ 触发 | ✅ 触发（与注册顺序有关） | 只在回程触发 |
| `once: true` | ✅ 生效 | ✅ 生效 | ✅ 生效 | 只执行一次，与阶段无关 |
| `passive: true` | ✅ 生效 | ✅ 生效 | ✅ 生效 | 禁止调用 preventDefault，与阶段无关 |

**初学者常见错误：**
- ❌ 以为 `capture: true` 能让监听器"只在捕获阶段触发、跳过目标阶段"——实际上目标阶段一定会触发
- ❌ 在目标元素上用 `stopPropagation()` 想阻止同元素上的其他监听器——这做不到，要用 `stopImmediatePropagation()`
- ❌ 父容器开了 `capture: true`，子元素开了 `capture: false`，以为父容器一定能"抢先处理"——如果点击的是子元素，两者都会在目标阶段触发，顺序取决于注册先后

---

**为什么不要用 `onclick`？**
```js
// ❌ 老方式：只能绑定一个处理器，后面的会覆盖前面的
btn.onclick = () => console.log('第一次');
btn.onclick = () => console.log('第二次'); // 第一次的处理器被覆盖了！

// ✅ 新方式：可以绑定多个处理器，依次执行
btn.addEventListener('click', () => console.log('A'));
btn.addEventListener('click', () => console.log('B'));
// 点击后输出 A，然后输出 B
```

**移除事件监听：**
```js
function handler() {
  console.log('clicked');
}

btn.addEventListener('click', handler);
btn.removeEventListener('click', handler); // 必须传入同一个函数引用

// ❌ 以下无法移除，因为匿名函数不是同一个引用
btn.addEventListener('click', () => {});
btn.removeEventListener('click', () => {}); // 无效！
```

**`preventDefault` 与 `stopPropagation`：**
```js
const link = document.querySelector('#demoLink'); // 基于本章统一页面结构

link.addEventListener('click', (e) => {
  e.preventDefault();      // 阻止默认行为（如跳转页面、提交表单）
  e.stopPropagation();     // 阻止事件继续冒泡（父元素不会再收到此事件）
  console.log('只处理这里，不跳转，也不冒泡');
});
```

**常见事件类型速查：**

| 类别 | 事件 | 说明 |
|---|---|---|
| 鼠标 | `click` / `dblclick` | 单击 / 双击 |
| 鼠标 | `mousedown` / `mouseup` / `mousemove` | 按下 / 松开 / 移动 |
| 鼠标 | `mouseenter` / `mouseleave` | 进入 / 离开（不冒泡） |
| 鼠标 | `mouseover` / `mouseout` | 进入 / 离开（会冒泡） |
| 键盘 | `keydown` / `keyup` / `keypress` | 按下 / 松开 / 按下字符键 |
| 表单 | `input` / `change` / `submit` | 输入 / 值改变 / 提交 |
| 触摸 | `touchstart` / `touchmove` / `touchend` | 移动端触摸事件 |
| 滚动 | `scroll` | 元素或页面滚动 |
| 尺寸 | `resize` | 窗口大小改变 |
| 加载 | `DOMContentLoaded` / `load` | DOM 就绪 / 所有资源加载完成 |

**初学者常见错误：**
- ❌ 在循环中绑定事件时忘记使用闭包，导致所有元素都触发同一个索引值
- ✅ 用事件委托或在循环内用 `let` / 箭头函数捕获当前元素

---

#### 事件委托与事件代理

**一句话理解：** 与其给 100 个按钮各绑定一个点击事件，不如给它们的父容器绑定一个事件，通过判断 `e.target` 来知道具体点了哪个按钮。

**班主任点名类比：**
- 不用给每个学生配一个点名员（100 个监听器）
- 班主任站在讲台上（父容器），谁举手（事件发生），一眼就能看到（e.target）

```js
// ❌ 低效：给每个 li 绑定事件
const items = document.querySelectorAll('#todoList .item'); // 基于本章统一页面结构
items.forEach(item => {
  item.addEventListener('click', () => console.log(item.textContent));
});
// 问题 1：如果有 1000 个 li，就有 1000 个监听器，内存消耗大
// 问题 2：动态新增的 li 没有绑定事件

// ✅ 高效：事件委托给父元素 ul
const list = document.querySelector('#todoList'); // 基于本章统一页面结构
list.addEventListener('click', (e) => {
  // e.target 是实际被点击的元素
  // ⚠️ 不要用 e.target.tagName，如果点击了 li 内部的 span 会失效
  const item = e.target.closest('li');
  if (item) {
    console.log('点击了：', item.textContent);
  }
});
// 优点 1：只有一个监听器，内存占用极小
// 优点 2：动态新增的 li 也能响应点击（因为事件是从 li 冒泡到 ul 的）
```

**更精确的事件委托（利用 closest）：**
```js
list.addEventListener('click', (e) => {
  // closest 会向上查找最近的匹配选择器的祖先元素
  const item = e.target.closest('.item');
  if (item) {
    console.log('点击了 item：', item.dataset.id);
  }
});
```

**事件委托的应用场景：**
- 长列表（表格、聊天记录）的点击操作
- 动态生成的内容（如无限滚动加载的新内容）
- 需要批量处理的相似元素交互

**初学者常见错误：**
- ❌ 在事件委托中直接使用 `e.target`，但用户可能点击的是 li 内部的 `<span>` 或 `<button>`
- ✅ 使用 `e.target.closest('li')` 确保能正确找到预期的元素

---

#### 自定义事件

**一句话理解：** 浏览器内置的事件（如 click、scroll）不够用？你可以自己定义一种事件，在代码的任意位置触发它。

**使用 `CustomEvent` 实现组件间通信：**

```js
// 1. 定义并触发自定义事件
const notifyEvent = new CustomEvent('user:login', {
  detail: { userId: 1001, name: 'Alice' }, // 传递自定义数据
  bubbles: true,    // 允许冒泡
  cancelable: true  // 允许 preventDefault
});

document.dispatchEvent(notifyEvent);

// 2. 监听自定义事件
document.addEventListener('user:login', (e) => {
  console.log('用户登录了：', e.detail.name);
});
```

**简易发布订阅模式（Event Bus）：**

```js
class EventBus {
  constructor() {
    this.events = {};
  }

  on(event, callback) {
    if (!this.events[event]) this.events[event] = [];
    this.events[event].push(callback);
  }

  off(event, callback) {
    if (!this.events[event]) return;
    this.events[event] = this.events[event].filter(cb => cb !== callback);
  }

  emit(event, data) {
    if (!this.events[event]) return;
    this.events[event].forEach(callback => callback(data));
  }
}

// 使用
const bus = new EventBus();
bus.on('message', (data) => console.log('收到消息：', data));
bus.emit('message', { text: 'Hello' }); // 收到消息： { text: 'Hello' }
```

**初学者常见错误：**
- ❌ 使用自定义事件时忘记设置 `bubbles: true`，导致事件无法通过委托捕获
- ✅ 如果需要事件代理，务必确保 `bubbles: true`


### 5.3 浏览器 API

#### 定时器与 requestAnimationFrame

**`setTimeout` 与 `setInterval`：**

```js
// setTimeout：延迟执行一次
const timeoutId = setTimeout(() => {
  console.log('1 秒后执行');
}, 1000);
clearTimeout(timeoutId); // 取消执行

// setInterval：每隔一段时间执行一次
const intervalId = setInterval(() => {
  console.log('每 2 秒执行一次');
}, 2000);
clearInterval(intervalId); // 取消定时器
```

**定时器的精度问题：**
- `setTimeout` 和 `setInterval` 的延迟时间**不是精确的**
- 当浏览器标签页处于后台时，为了省电，定时器最小间隔会被限制（通常 ≥ 1000ms）
- 页面忙时（如大量计算），回调会被推迟

```js
// ❌ 用 setInterval 做动画可能丢帧
box.style.left = '0px'; // 必须先设置初始值，否则 parseInt('') 得 NaN
setInterval(() => {
  box.style.left = parseInt(box.style.left) + 1 + 'px';
}, 16); // 理论上 60fps，实际可能不流畅
```

**`requestAnimationFrame`（rAF）：**

**一句话理解：** 告诉浏览器"下一帧重绘前帮我执行这个动画函数"，浏览器会自动根据屏幕刷新率（通常 60fps 或 120fps）调度。

```js
let start = null;
const box = document.querySelector('#animBox'); // 基于本章统一页面结构

function step(timestamp) {
  if (!start) start = timestamp;
  const progress = timestamp - start;

  // 1 秒内向右移动 200px
  box.style.transform = `translateX(${Math.min(progress / 5, 200)}px)`;

  if (progress < 1000) {
    requestAnimationFrame(step); // 继续下一帧
  }
}

requestAnimationFrame(step);
```

**rAF 的优势：**
- 与显示器刷新率同步，动画更流畅
- 页面在后台标签页时自动暂停，节省 CPU/GPU
- 会自动合并多次调用，避免不必要的重绘

**`setTimeout` vs `requestAnimationFrame` 对比：**

| 特性 | `setTimeout` | `requestAnimationFrame` |
|---|---|---|
| 调用时机 | 固定延迟后 | 下次重绘前 |
| 后台运行 | 继续执行（可能卡顿） | 自动暂停（省电） |
| 动画流畅度 | 可能丢帧 | 与刷新率同步 |
| 适用场景 | 延迟任务、轮询 | 动画、视觉更新 |

**初学者常见错误：**
- ❌ 用 `setInterval` 驱动动画，导致页面卡顿或电池消耗过快
- ✅ 所有视觉动画都应优先使用 `requestAnimationFrame`

---

#### Storage（localStorage / sessionStorage）

**一句话理解：** `localStorage` 是浏览器的"永久记事本"（除非手动删除，否则一直存在），`sessionStorage` 是"临时便签"（关闭标签页就消失）。

```js
// localStorage：数据永久保存，同源页面共享
localStorage.setItem('username', 'Alice');
localStorage.getItem('username');        // "Alice"
localStorage.removeItem('username');     // 删除指定键
localStorage.clear();                    // 清空所有数据

// sessionStorage：仅在当前标签页会话期间有效
sessionStorage.setItem('tempId', '123');
```

**存储对象的正确方式（必须序列化）：**
```js
const user = { id: 1, name: 'Alice', tags: ['admin'] };

// ✅ 存入时 JSON.stringify
localStorage.setItem('user', JSON.stringify(user));

// ✅ 取出时 JSON.parse
const saved = JSON.parse(localStorage.getItem('user'));
console.log(saved.name); // "Alice"
```

**初学者常见错误：**
- ❌ 直接存储对象：`localStorage.setItem('user', user)` → 实际存的是 `"[object Object]"`
- ❌ 取出后忘记 `JSON.parse`，直接当对象使用导致报错
- ✅ 封装工具函数统一管理序列化逻辑

**Storage 工具函数封装：**
```js
const storage = {
  set(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
  },
  get(key, defaultValue = null) {
    const item = localStorage.getItem(key);
    try {
      return item ? JSON.parse(item) : defaultValue;
    } catch {
      return item || defaultValue;
    }
  },
  remove(key) {
    localStorage.removeItem(key);
  }
};

// 使用
storage.set('settings', { theme: 'dark', fontSize: 16 });
const settings = storage.get('settings', { theme: 'light' });
```

**Storage 限制与注意事项：**
- 容量限制：通常每个域名 **5MB** 左右
- 只能存储字符串，且是**同步操作**，大数据量会阻塞主线程
- **敏感数据（如 token）不要直接存 localStorage**，有 XSS 泄露风险；重要凭证应使用 `httpOnly` Cookie
- `storage` 事件：同源其他页面修改 Storage 时触发，可用于跨标签页通信

```js
window.addEventListener('storage', (e) => {
  console.log('其他页面修改了 Storage');
  console.log('键：', e.key);
  console.log('旧值：', e.oldValue);
  console.log('新值：', e.newValue);
});
// 当同源的其他页面执行 localStorage.setItem('theme', 'dark') 时输出：
// 其他页面修改了 Storage
// 键： theme
// 旧值： light
// 新值： dark
```

---

#### Fetch API 与 AbortController

**`fetch` 是现代浏览器内置的 HTTP 请求 API，返回 Promise：**

```js
// GET 请求
fetch('https://api.example.com/users')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    return response.json(); // 解析 JSON
  })
  .then(data => console.log(data))
  .catch(err => console.error('请求失败：', err));
```

**POST 请求与自定义请求头：**
```js
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
  },
  body: JSON.stringify({ name: 'Alice', age: 25 })
})
.then(res => res.json())
.then(data => console.log(data));
```

**async/await 风格（推荐）：**
```js
async function getUser(id) {
  try {
    const response = await fetch(`https://api.example.com/users/${id}`);
    if (!response.ok) throw new Error('User not found');
    return await response.json();
  } catch (err) {
    console.error(err);
    return null;
  }
}
```

**取消请求（AbortController）：**
```js
const controller = new AbortController();

fetch('https://api.example.com/slow-endpoint', {
  signal: controller.signal
})
.then(res => res.json())
.then(data => console.log(data))
.catch(err => {
  if (err.name === 'AbortError') {
    console.log('请求已被取消');
  }
});

// 5 秒后取消请求
setTimeout(() => controller.abort(), 5000);
```

**Fetch 与 XMLHttpRequest 对比：**

| 特性 | Fetch API | XMLHttpRequest |
|---|---|---|
| API 风格 | 基于 Promise | 基于事件回调 |
| 进度监控 | 需使用 ReadableStream | 原生支持 `onprogress` |
| 同步请求 | 不支持（好事） | 支持（已废弃） |
| IE 兼容 | IE 不支持 | IE7+ 支持 |

**初学者常见错误：**
- ❌ 忽略 `response.ok` 检查，`fetch` 只对网络错误（断网）reject，HTTP 4xx/5xx 仍返回 resolved Promise
- ✅ 始终检查 `response.ok` 或 `response.status` 再处理数据
- ❌ 忘记 `await response.json()` 是异步的，直接返回 `response.json()` 的结果

---

#### 文件与拖放 API

**文件读取（FileReader）：**
```js
const input = document.querySelector('#fileInput'); // 基于本章统一页面结构

input.addEventListener('change', (e) => {
  const file = e.target.files[0]; // FileList 是一个类数组对象

  if (file.type.startsWith('image/')) {
    const reader = new FileReader();

    reader.onload = (event) => {
      const img = document.createElement('img');
      img.src = event.target.result; // Base64 数据 URL
      document.body.appendChild(img);
    };
    reader.onerror = (e) => console.error('文件读取失败:', e);

    reader.readAsDataURL(file); // 读取为 Data URL
  }
});
```

**FileReader 的读取方式：**

| 方法 | 结果格式 | 适用场景 |
|---|---|---|
| `readAsText(file)` | 文本字符串 | 读取 `.txt`、`.json`、`.csv` |
| `readAsDataURL(file)` | Base64 Data URL | 预览图片、音频 |
| `readAsArrayBuffer(file)` | ArrayBuffer | 二进制数据处理、文件上传分片 |

**拖放 API（Drag & Drop）：**
```js
const dropZone = document.querySelector('#dropZone'); // 基于本章统一页面结构

// 必须阻止默认行为，否则浏览器会直接打开文件
dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('drag-over');
});

dropZone.addEventListener('dragleave', () => {
  dropZone.classList.remove('drag-over');
});

dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('drag-over');

  const files = e.dataTransfer.files;
  for (const file of files) {
    console.log('拖入文件：', file.name, file.size);
  }
});
```

**初学者常见错误：**
- ❌ 拖放时忘记在 `dragover` 和 `drop` 事件中调用 `e.preventDefault()`，导致浏览器直接打开文件
- ❌ 把 `e.dataTransfer.files` 当数组使用（它是 FileList），需用 `for...of` 或 `Array.from()` 遍历


### 5.4 性能优化

#### DOM 操作性能优化

**一句话理解：** DOM 操作是 JavaScript 中最昂贵的操作之一，因为每次修改都可能触发浏览器的重排（Reflow）和重绘（Repaint）。优化的核心思路是**减少操作次数**和**批量处理**。

**四大优化策略：**

**1. 使用 DocumentFragment（内存中组装）**
```js
// ❌ 每次 appendChild 都触发重排
const list = document.querySelector('#todoList'); // 基于本章统一页面结构
for (let i = 0; i < 1000; i++) {
  const li = document.createElement('li');
  li.textContent = `Item ${i}`;
  list.appendChild(li); // 1000 次重排！
}

// ✅ 先在内存中组装，一次性插入
const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  const li = document.createElement('li');
  li.textContent = `Item ${i}`;
  fragment.appendChild(li); // 不触发重排，因为 fragment 不在 DOM 中
}
list.appendChild(fragment); // 只触发 1 次重排
```

**2. 克隆代替创建（cloneNode）**
```js
// 如果需要创建大量相似元素
const template = document.createElement('li');
template.className = 'item';

const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  const clone = template.cloneNode(true); // true 表示深克隆
  clone.textContent = `Item ${i}`;
  fragment.appendChild(clone);
}
list.appendChild(fragment);
// cloneNode 比 createElement + 多次设置属性更快
```

**3. 离线操作（脱离文档流）**
```js
const list = document.querySelector('#todoList'); // 基于本章统一页面结构

// ✅ 方案 A：display none
list.style.display = 'none';
// ... 大量 DOM 操作 ...
list.style.display = '';

// ✅ 方案 B：使用 CSS contain（让浏览器知道这部分独立渲染）
// 💡 CSS contain 在 Safari 15 之前支持有限，生产环境建议配合 @supports 检测
list.style.contain = 'strict'; // 该元素的布局/样式/绘制与其他元素隔离
```

**4. 缓存查询结果**
```js
// ❌ 每次循环都查询 DOM
for (let i = 0; i < 100; i++) {
  document.querySelector('#pageTitle').textContent = `进度: ${i}%`; // 基于本章统一页面结构
}

// ✅ 缓存元素引用
const status = document.querySelector('#pageTitle'); // 基于本章统一页面结构
for (let i = 0; i < 100; i++) {
  status.textContent = `进度: ${i}%`;
}
```

---

#### 防抖（debounce）与节流（throttle）

**一句话理解：**
- **防抖（Debounce）**：等用户停止操作后再执行（如搜索框输入完 300ms 后才发请求）
- **节流（Throttle）**：不管操作多频繁，固定时间间隔只执行一次（如滚动时每隔 16ms 检查一次位置）

**生活类比：**
- 防抖 = 电梯关门：最后一个人进来后，再等 3 秒才关门；如果又有人进来，重新等 3 秒
- 节流 = 水龙头滴水：不管怎么拧，最多每秒滴一滴

**防抖实现（简化版）：**
```js
// ℹ️ 简化版，生产环境建议用 lodash 或实现 leading/trailing/cancel
function debounce(fn, delay = 300) {
  let timer = null;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}

// 使用：搜索框输入
const searchInput = document.querySelector('#nameInput'); // 基于本章统一页面结构
searchInput.addEventListener('input', debounce((e) => {
  console.log('发送搜索请求：', e.target.value);
}, 500));
```

**节流实现（简化版）：**
```js
// 方式 1：时间戳法（第一次立即执行，但会忽略间隔内最后一次调用）
function throttle(fn, interval = 100) {
  let lastTime = 0;
  return function (...args) {
    const now = Date.now();
    if (now - lastTime >= interval) {
      lastTime = now;
      fn.apply(this, args);
    }
  };
}

// 方式 2：定时器法（保证最后一次执行，但不是立即执行）
function throttleTimer(fn, interval = 100) {
  let timer = null;
  return function (...args) {
    if (!timer) {
      fn.apply(this, args);
      timer = setTimeout(() => {
        timer = null;
      }, interval);
    }
  };
}

// 使用：滚动加载
window.addEventListener('scroll', throttle(() => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 200) {
    console.log('快到底了，加载更多');
  }
}, 200));
```

**对比表：**

| 场景 | 适用方案 | 原因 |
|---|---|---|
| 搜索框实时搜索 | 防抖 | 用户输入完才搜索，减少请求次数 |
| 窗口 resize 调整 | 防抖 | 调整完后再计算布局 |
| 滚动加载更多 | 节流 | 持续滚动时定期检查位置 |
| 按钮防止重复点击 | 节流 | 固定时间内只能点一次 |
| 鼠标移动画跟随效果 | 节流 | 降低更新频率，减少重绘 |

**初学者常见错误：**
- ❌ 在滚动事件中直接执行复杂计算，导致页面卡顿掉帧
- ✅ 所有高频触发的事件（scroll、resize、mousemove、input）都应先做防抖或节流处理

---

#### 懒加载与预加载

**懒加载（Lazy Load）：**
**一句话理解：** 图片或资源只有在即将进入用户视野时才加载，避免一次性加载全部资源拖慢首屏。

```js
// 方式 1：IntersectionObserver（现代推荐方案）
const imageObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src; // 把 data-src 赋值给 src
      img.onload = () => {
        img.classList.add('loaded');
        observer.unobserve(img); // 加载成功后才停止观察
      };
      img.onerror = () => observer.unobserve(img); // 加载失败也要停止观察
    }
  });
});

document.querySelectorAll('img[data-src]').forEach(img => {
  imageObserver.observe(img);
});
```

```html
<!-- HTML 结构 -->
<img data-src="photo.jpg" alt="描述" class="lazy">
```

```css
/* 占位与加载动画 */
.lazy {
  opacity: 0;
  transition: opacity 0.3s;
}
.lazy.loaded {
  opacity: 1;
}
```

**预加载（Preload / Prefetch）：**

```html
<!-- preload：当前页面即将用到的关键资源（高优先级） -->
<link rel="preload" href="critical.css" as="style">
<link rel="preload" href="font.woff2" as="font" crossorigin>

<!-- prefetch：下一个页面可能用到的资源（低优先级，空闲时加载） -->
<link rel="prefetch" href="next-page.js">

<!-- DNS 预解析 -->
<link rel="dns-prefetch" href="//cdn.example.com">
```

**JavaScript 动态预加载：**
```js
// 提前加载图片到浏览器缓存
function preloadImage(url) {
  const img = new Image();
  img.src = url;
}

// 鼠标悬停时预加载下一页
const nextLink = document.querySelector('a[rel="next"]');
if (nextLink) {
  nextLink.addEventListener('mouseenter', () => {
    preloadImage(nextLink.href);
  });
}
```

**对比表：**

| 技术 | 目的 | 加载时机 | 优先级 |
|---|---|---|---|
| **Lazy Load** | 减少首屏加载量 | 进入视口时 | 按需 |
| **Preload** | 提前加载当前页关键资源 | 立即 | 高 |
| **Prefetch** | 预加载下一页资源 | 空闲时 | 低 |
| **Preconnect** | 提前建立 TCP/TLS 连接 | 立即 | 中 |

**初学者常见错误：**
- ❌ 懒加载时忘记给图片设置占位尺寸，导致布局抖动（Layout Shift）
- ✅ 为懒加载图片预留 `width` 和 `height` 或使用 `aspect-ratio`，避免 CLS（Cumulative Layout Shift）问题


### 🛠️ 实操：前端交互项目实战

#### 待办事项管理器（Todo List）— 含增删改查、本地存储、筛选排序

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <title>Todo List</title>
  <style>
    * { box-sizing: border-box; }
    body { font-family: system-ui, sans-serif; max-width: 500px; margin: 40px auto; padding: 0 20px; }
    .input-group { display: flex; gap: 8px; margin-bottom: 16px; }
    input[type="text"] { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 6px; }
    button { padding: 10px 16px; border: none; background: #2563eb; color: white; border-radius: 6px; cursor: pointer; }
    button:hover { background: #1d4ed8; }
    .filters { display: flex; gap: 8px; margin-bottom: 12px; }
    .filters button { background: #e5e7eb; color: #374151; }
    .filters button.active { background: #2563eb; color: white; }
    .todo-list { list-style: none; padding: 0; margin: 0; }
    .todo-item { display: flex; align-items: center; gap: 10px; padding: 10px; border: 1px solid #e5e7eb; border-radius: 6px; margin-bottom: 8px; }
    .todo-item.completed span { text-decoration: line-through; color: #9ca3af; }
    .todo-item input[type="checkbox"] { cursor: pointer; }
    .todo-item span { flex: 1; }
    .todo-item .delete { background: #ef4444; padding: 6px 10px; font-size: 12px; }
    .stats { margin-top: 12px; color: #6b7280; font-size: 14px; }
  </style>
</head>
<body>
  <h1>📝 Todo List</h1>
  <div class="input-group">
    <input type="text" id="todoInput" placeholder="输入待办事项，按回车添加">
    <button id="addBtn">添加</button>
  </div>
  <div class="filters">
    <button data-filter="all" class="active">全部</button>
    <button data-filter="active">未完成</button>
    <button data-filter="completed">已完成</button>
  </div>
  <ul class="todo-list" id="todoList"></ul>
  <div class="stats" id="stats"></div>

  <script>
    const todoInput = document.getElementById('todoInput');
    const addBtn = document.getElementById('addBtn');
    const todoList = document.getElementById('todoList');
    const filterBtns = document.querySelectorAll('.filters button');
    const statsEl = document.getElementById('stats');

    let todos = JSON.parse(localStorage.getItem('todos')) || [];
    let currentFilter = 'all';

    function save() {
      localStorage.setItem('todos', JSON.stringify(todos));
    }

    function render() {
      todoList.innerHTML = '';
      const filtered = todos.filter(todo => {
        if (currentFilter === 'active') return !todo.completed;
        if (currentFilter === 'completed') return todo.completed;
        return true;
      });

      filtered.forEach(todo => {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
        li.innerHTML = `
          <input type="checkbox" ${todo.completed ? 'checked' : ''} data-id="${todo.id}">
          <span>${escapeHtml(todo.text)}</span>
          <button class="delete" data-id="${todo.id}">删除</button>
        `;
        todoList.appendChild(li);
      });

      const activeCount = todos.filter(t => !t.completed).length;
      statsEl.textContent = `共 ${todos.length} 项，待完成 ${activeCount} 项`;
    }

    function escapeHtml(text) {
      const div = document.createElement('div');
      div.textContent = text;
      return div.innerHTML;
    }

    function addTodo() {
      const text = todoInput.value.trim();
      if (!text) return;
      todos.push({ id: Date.now(), text, completed: false });
      todoInput.value = '';
      save();
      render();
    }

    todoList.addEventListener('click', (e) => {
      // ⚠️ 如果 button 内部有图标（如 <i>×</i>），e.target 会是图标元素
      const btn = e.target.closest('button');
      if (btn) {
        const id = Number(btn.dataset.id);
        todos = todos.filter(t => t.id !== id);
        save();
        render();
      }
    });

    todoList.addEventListener('change', (e) => {
      if (e.target.tagName === 'INPUT') {
        const id = Number(e.target.dataset.id);
        const todo = todos.find(t => t.id === id);
        if (todo) {
          todo.completed = e.target.checked;
          save();
          render();
        }
      }
    });

    addBtn.addEventListener('click', addTodo);
    todoInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') addTodo();
    });

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.dataset.filter;
        render();
      });
    });

    render();
  </script>
</body>
</html>
```

**学习要点：**
- 用 `localStorage` 实现数据持久化
- 事件委托统一处理列表项的点击和勾选
- `textContent` 防止 XSS，比 `innerHTML` 更安全
- 过滤状态通过 `data-filter` 属性管理，无需多个监听器

---

#### 图片画廊 — 含懒加载、灯箱预览、拖拽排序

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <title>图片画廊</title>
  <style>
    .gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 12px; }
    .gallery img { width: 100%; height: 150px; object-fit: cover; border-radius: 8px; cursor: pointer; opacity: 0; transition: opacity 0.3s; }
    .gallery img.loaded { opacity: 1; }
    .lightbox { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.9); justify-content: center; align-items: center; z-index: 1000; }
    .lightbox.active { display: flex; }
    .lightbox img { max-width: 90%; max-height: 90%; border-radius: 8px; }
    .lightbox .close { position: absolute; top: 20px; right: 30px; color: white; font-size: 36px; cursor: pointer; }
  </style>
</head>
<body>
  <h1>🖼️ 图片画廊</h1>
  <div class="gallery" id="gallery"></div>

  <div class="lightbox" id="lightbox">
    <span class="close" id="closeBtn">&times;</span>
    <img src="" alt="preview" id="lightboxImg">
  </div>

  <script>
    const images = [
      'https://picsum.photos/400/400?random=1',
      'https://picsum.photos/400/400?random=2',
      'https://picsum.photos/400/400?random=3',
      'https://picsum.photos/400/400?random=4',
      'https://picsum.photos/400/400?random=5',
      'https://picsum.photos/400/400?random=6'
    ];

    const gallery = document.getElementById('gallery');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const closeBtn = document.getElementById('closeBtn');

    // 生成图片元素
    images.forEach((src, index) => {
      const img = document.createElement('img');
      img.dataset.src = src;
      img.alt = `图片 ${index + 1}`;
      gallery.appendChild(img);
    });

    // 懒加载
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.onload = () => img.classList.add('loaded');
          observer.unobserve(img);
        }
      });
    });

    document.querySelectorAll('.gallery img').forEach(img => observer.observe(img));

    // 灯箱预览
    gallery.addEventListener('click', (e) => {
      if (e.target.tagName === 'IMG') {
        lightboxImg.src = e.target.src;
        lightbox.classList.add('active');
      }
    });

    closeBtn.addEventListener('click', () => lightbox.classList.remove('active'));
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) lightbox.classList.remove('active');
    });
  </script>
</body>
</html>
```

**学习要点：**
- `IntersectionObserver` 实现高性能懒加载，替代 scroll 监听
- 灯箱利用固定定位（`position: fixed`）和半透明遮罩层
- 点击遮罩层关闭（判断 `e.target === lightbox`）

---

#### 天气预报查询应用 — 含 Fetch API 请求、数据渲染、错误处理

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <title>天气预报</title>
  <style>
    body { font-family: system-ui; max-width: 400px; margin: 40px auto; text-align: center; }
    input { padding: 10px; width: 60%; border: 1px solid #ddd; border-radius: 6px; }
    button { padding: 10px 16px; background: #2563eb; color: white; border: none; border-radius: 6px; cursor: pointer; }
    .weather { margin-top: 20px; padding: 20px; background: #f3f4f6; border-radius: 12px; display: none; }
    .weather.show { display: block; }
    .temp { font-size: 48px; font-weight: bold; color: #1f2937; }
    .error { color: #ef4444; margin-top: 12px; }
    .loading { color: #6b7280; margin-top: 12px; }
  </style>
</head>
<body>
  <h1>🌤️ 天气查询</h1>
  <div>
    <input type="text" id="cityInput" placeholder="输入城市名（如 Beijing）">
    <button id="searchBtn">查询</button>
  </div>
  <div class="loading" id="loading" style="display:none;">加载中...</div>
  <div class="error" id="error"></div>
  <div class="weather" id="weather">
    <h2 id="cityName"></h2>
    <div class="temp" id="temp"></div>
    <p id="desc"></p>
  </div>

  <script>
    const cityInput = document.getElementById('cityInput');
    const searchBtn = document.getElementById('searchBtn');
    const weatherEl = document.getElementById('weather');
    const loadingEl = document.getElementById('loading');
    const errorEl = document.getElementById('error');

    async function fetchWeather(city) {
      loadingEl.style.display = 'block';
      errorEl.textContent = '';
      weatherEl.classList.remove('show');

      try {
        // 使用 Open-Meteo 免费 API（无需 Key）
        const geoRes = await fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(city)}&count=1`);
        if (!geoRes.ok) throw new Error('地理编码服务异常');
        const geoData = await geoRes.json();

        if (!geoData.results || geoData.results.length === 0) {
          throw new Error('未找到该城市');
        }

        const { latitude, longitude, name } = geoData.results[0];

        const weatherRes = await fetch(
          `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`
        );
        if (!weatherRes.ok) throw new Error('天气服务异常');
        const weatherData = await weatherRes.json();
        const current = weatherData.current_weather;

        document.getElementById('cityName').textContent = name;
        document.getElementById('temp').textContent = `${current.temperature}°C`;
        document.getElementById('desc').textContent = `风速: ${current.windspeed} km/h`;
        weatherEl.classList.add('show');
      } catch (err) {
        errorEl.textContent = '查询失败：' + err.message;
      } finally {
        loadingEl.style.display = 'none';
      }
    }

    searchBtn.addEventListener('click', () => {
      const city = cityInput.value.trim();
      if (city) fetchWeather(city);
    });

    cityInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') searchBtn.click();
    });
  </script>
</body>
</html>
```

**学习要点：**
- `async/await` + `try/catch/finally` 组织异步流程和 UI 状态
- 加载中、成功、错误三种状态的管理
- 使用 `encodeURIComponent` 处理用户输入，防止 URL 注入
- 免费公开 API 的练习技巧

---

#### 自定义事件总线 — 实现一个简易的发布订阅模式用于组件通信

```js
/**
 * 简易事件总线（Event Bus）
 * 适用于无框架的模块化项目，或微前端组件间通信
 */
class EventBus {
  constructor() {
    this.events = new Map(); // 使用 Map 存储事件名 -> 监听器数组
  }

  // 订阅事件
  on(event, callback) {
    if (!this.events.has(event)) {
      this.events.set(event, new Set());
    }
    this.events.get(event).add(callback);

    // 返回取消订阅函数
    return () => this.off(event, callback);
  }

  // 取消订阅
  off(event, callback) {
    const callbacks = this.events.get(event);
    if (callbacks) {
      callbacks.delete(callback);
      if (callbacks.size === 0) {
        this.events.delete(event);
      }
    }
  }

  // 发布事件（同步触发所有监听器）
  emit(event, data) {
    const callbacks = this.events.get(event);
    if (callbacks) {
      callbacks.forEach(cb => {
        try {
          cb(data);
        } catch (err) {
          console.error(`事件 ${event} 的处理器出错:`, err);
        }
      });
    }
  }

  // 只监听一次
  once(event, callback) {
    const wrap = (data) => {
      this.off(event, wrap);
      callback(data);
    };
    this.on(event, wrap);
  }

  // 清空所有事件或指定事件
  clear(event) {
    if (event) {
      this.events.delete(event);
    } else {
      this.events.clear();
    }
  }
}

// ===== 使用示例 =====
const bus = new EventBus();

// 组件 A 订阅消息更新
const unsubscribe = bus.on('message:received', (msg) => {
  console.log('组件 A 收到消息:', msg.text);
});

// 组件 B 发布消息
bus.emit('message:received', { text: 'Hello from B', time: Date.now() });

// 组件 A 取消订阅
unsubscribe();

// 一次性监听
bus.once('app:init', () => {
  console.log('应用初始化完成（只执行一次）');
});
bus.emit('app:init');
bus.emit('app:init'); // 不会再次触发
```

**与 DOM 自定义事件结合：**
```js
// 如果需要在 DOM 元素间通信，可以封装一层
document.addEventListener('app:login', (e) => {
  console.log('登录事件:', e.detail);
});

document.dispatchEvent(new CustomEvent('app:login', {
  detail: { userId: 1, name: 'Alice' }
}));
```

**学习要点：**
- 发布订阅模式解耦了组件间的直接依赖
- 使用 `Set` 存储回调，避免重复添加同一函数
- 每个 `on()` 返回取消订阅函数，方便组件销毁时清理
- `try/catch` 包裹监听器执行，防止一个回调报错影响其他回调

> **本章小结：** 我们学习了 DOM 核心（节点操作、属性修改、样式控制）、事件系统（捕获/目标/冒泡、事件委托、自定义事件）、浏览器 API（定时器、localStorage、Fetch、文件操作）以及前端性能优化技巧（减少重排重绘、防抖节流、懒加载预加载）。
>
> **下一章预告：** 在掌握了 DOM 操作和浏览器 API 后，让我们回到语法层面，学习现代 JavaScript（ES6+）带来的语法革新——解构赋值、模板字符串、生成器函数、模块化等让代码更简洁优雅的特性。
