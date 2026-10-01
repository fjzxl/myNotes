---
title: "JavaScript 核心知识体系 · 四、异步编程"
tags:
  - programming
  - javascript
created: 2026-09-10
updated: 2026-10-01
---

# 四、异步编程

> 📚 本文是 [[topics/programming/Web/javascript|JavaScript 核心知识体系]] 的第 4 / 8 章。 上一章：[[topics/programming/Web/javascript/03-core-mechanisms|三、核心运行机制]] · 下一章：[[topics/programming/Web/javascript/05-dom-and-browser-api|五、DOM 操作与浏览器 API]]


> **本章定位：** 现实世界的程序很少是"一步做完"的：网络请求需要时间、用户操作不可预测、定时任务需要等待。本章将学习 JavaScript 如何处理这些"不等人的任务"。
>
> **学习路线：** 事件循环（为什么 JS 不会卡死）→ 回调函数（原始的异步方式与回调地狱）→ Promise（优雅的异步管理）→ async/await（写起来像同步的异步代码）→ Generator / 顶层 await → 实战代码
>
> **核心要理解的概念：** Event Loop 是 JavaScript 异步的"心脏"。从历史上看，异步编程经历了三个阶段：回调函数（最原始）→ Promise（链式管理）→ async/await（同步写法）。理解这个演进过程，比单纯记语法更重要。

### 4.1 事件循环与任务调度

#### 为什么需要 Event Loop

JavaScript 是**单线程**语言——同一时间只能做一件事。如果没有 Event Loop，当你发起一个网络请求时，整个页面会卡死，直到请求返回；当你点击按钮时，如果后台正在做大量计算，按钮不会有任何反应。

**Event Loop 的核心作用**就是让这个单线程的 JS 能够**非阻塞地处理异步任务**：先执行当前手头的同步代码，把耗时的任务（定时器、网络请求、用户事件）交给浏览器的"后勤部门"（Web APIs），等结果回来了再按优先级排队处理。

> 可以把 Event Loop 想象成餐厅的**前台调度员**：主厨（调用栈）一次只做一道菜，但前台会帮主厨接单、等外卖、通知客人——主厨从不空闲等待，一直在做菜。

```js
// 同步代码会阻塞后续执行
console.log('开始');
for (let i = 0; i < 1000000000; i++) {} // 模拟耗时计算（页面会卡死）
console.log('结束'); // 这行要很久以后才执行

// 异步代码不会阻塞
console.log('1. 同步代码');
setTimeout(() => console.log('3. 定时器回调'), 0);
Promise.resolve().then(() => console.log('2. Promise 回调'));
console.log('4. 同步代码结束');
// 输出顺序：1 → 4 → 2 → 3
// 说明：Promise.then 是微任务，比宏任务 setTimeout 优先执行
```

#### 核心组件

**一句话理解：** Event Loop 由四个核心零件组成：调用栈（当前执行的任务）、Web APIs（浏览器帮忙跑腿的异步任务）、宏任务队列（普通任务排队区）、微任务队列（VIP 快速通道）。

要理解 Event Loop，先认识它的四个核心"零件"：

| 组件 | 作用 | 类比 |
|------|------|------|
| **调用栈（Call Stack）** | 存放正在执行的函数栈帧，后进先出（LIFO） | 主厨的灶台，一次只做一道菜 |
| **Web APIs** | 浏览器提供的异步能力（`setTimeout`、`fetch`、DOM 事件等） | 配菜员、外卖员——帮主厨跑腿 |
| **宏任务队列（Macrotask Queue）** | 存放待执行的宏任务回调，先进先出（FIFO） | 订单台的普通订单 |
| **微任务队列（Microtask Queue）** | 存放 Promise 回调等高优先级任务 | 厨师长插队的加急订单 |

**它们如何协作？**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Event Loop 执行流程图                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────┐        ┌─────────────────────┐        ┌─────────────┐    │
│   │   同步代码   │        │    异步任务调度      │        │   任务队列   │    │
│   │  (调用栈)    │        │    (Web APIs)       │        │  (等待执行)  │    │
│   │             │        │                     │        │             │    │
│   │ console.log │        │  ┌─────────────┐   │        │ ┌─────────┐ │    │
│   │  函数调用   │        │  │  setTimeout │   │ 计时完成 │ │ 宏任务  │ │    │
│   │  等        │        │  │    fetch    │───┼─────────▶│  队列   │ │    │
│   └──────┬──────┘        │  │  DOM 事件   │   │ 放入回调 │ │setTimeout│ │    │
│          │               │  └─────────────┘   │        │ │DOM事件  │ │    │
│          │               │                     │        │ └────┬────┘ │    │
│          │               │  ┌─────────────┐   │        │ ┌────┴────┐ │    │
│          │               │  │  Promise    │   │ 异步完成 │ │ 微任务  │ │    │
│          │               │  │ MutationObs │───┼─────────▶│  队列   │ │    │
│          │               │  └─────────────┘   │ 放入回调 │ │Promise.then│ │
│          │               └─────────────────────┘        │ │queueMicrotask│ │
│          │                        ▲                     │ └────┬────┘ │    │
│          │                        │                     └──────┼──────┘    │
│          │                        │                            │           │
│          │         ┌──────────────┴────────────────────────────┘           │
│          │         │              Event Loop 调度                           │
│          │         │         (1. 清空所有微任务 → 2. 执行一个宏任务)         │
│          │         │                                                        │
│          └─────────┼───────────────────────────────────────────────────────▶│
│                    │                                                        │
│                    ▼                                                        │
│           ┌─────────────────┐                                               │
│           │  调用栈执行回调  │                                               │
│           │  (可能产生新的   │                                               │
│           │   微任务入队)    │                                               │
│           └─────────────────┘                                               │
│                                                                             │
│   💡 核心规则：执行一个宏任务（含同步代码）→ 清空微任务队列 → 渲染 → 循环    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```
Event Loop 的工作流程（简化版）：

  ┌─────────────────────────────────────────────────────────────┐
  │                    主循环（无限循环）                        │
  └─────────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  1️⃣ 执行一个宏任务（ONE）                                    │
  │      从宏任务队列取出一个 → 执行                               │
  │      （如 script 整体、setTimeout 回调、DOM 事件回调等）      │
  └─────────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  2️⃣ 清空微任务队列（ALL）                                    │
  │      while (微任务队列不为空) {                              │
  │        取出一个微任务 → 执行                                   │
  │        （执行中产生的新微任务也加入队列，继续清空）             │
  │      }                                                       │
  └─────────────────────────────────────────────────────────────┘
                              │
                              ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  3️⃣ 渲染更新（浏览器）                                       │
  │      （如果有需要重绘的内容）                                  │
  └─────────────────────────────────────────────────────────────┘
                              │
                              └──▶ 回到步骤 1，继续循环

  ⚠️ 核心顺序：先执行一个宏任务 → 再清空本轮产生的所有微任务
```

#### 宏任务与微任务

**一句话理解：** 宏任务是"普通订单"（setTimeout、DOM 事件），微任务是"加急订单"（Promise.then）——Event Loop 每轮都会先清空微任务队列，再执行一个宏任务。

Event Loop 中的"任务"分为两类，它们的**执行优先级不同**：

| 类型 | 典型来源 | 特点 |
|------|----------|------|
| **宏任务（Macrotask）** | `setTimeout`/`setInterval`、I/O、UI 渲染、`script` 标签整体执行 | 每个循环只执行一个 |
| **微任务（Microtask）** | `Promise.then/catch/finally`、`queueMicrotask`、`MutationObserver` | 当前任务结束后立即全部清空 |
| **渲染回调** | `requestAnimationFrame` | 在渲染阶段执行，位于微任务清空之后 |

**执行优先级：同步代码 > 微任务 > 渲染 > 下一个宏任务**

```js
console.log('1. 同步');

setTimeout(() => console.log('4. 宏任务 setTimeout'), 0);

Promise.resolve()
  .then(() => console.log('3. 微任务 Promise.then'));

console.log('2. 同步');

// 输出顺序：1 → 2 → 3 → 4
```

#### Event Loop 逐轮拆解


**Event Loop 完整流程图：**

```
┌─────────────────────────────────────────────────────────────┐
│                     一轮 Event Loop                         │
│                                                             │
│  ┌─────────────┐                                           │
│  │ 1. 取一个宏  │ ◄── 从宏任务队列取出最老的任务执行       │
│  │    任务执行  │     （如 script 整体、setTimeout 回调）   │
│  └──────┬──────┘     执行期间产生的异步任务 → 交给 Web APIs │
│         │                                                  │
│         ▼                                                  │
│  ┌─────────────┐    完成后回调入队                         │
│  │ 2. 清空微任务│ ◄── 逐个执行所有微任务（包括新产生的）    │
│  │    队列     │                                           │
│  └──────┬──────┘                                           │
│         ▼                                                  │
│  ┌─────────────┐                                           │
│  │ 3. 尝试渲染  │ ◄── 浏览器有机会更新 UI（如果需要）       │
│  │    页面     │                                           │
│  └──────┬──────┘                                           │
│         │                                                  │
│         └──────────────────────► 回到第 1 步，开始下一轮   │
│                                                             │
└─────────────────────────────────────────────────────────────┘

优先级：同步代码 > 微任务 > 渲染 > 下一个宏任务
（每轮循环中，先执行一个宏任务，再清空它产生的所有微任务）
```


**一句话理解：** Event Loop 的工作流程像餐厅的出餐流程：先做完灶台上的菜（同步代码），再处理加急单（微任务），最后拿一个新订单（宏任务）——循环往复。

理解了"零件"和"任务类型"，来看 Event Loop 在一轮循环中具体做了什么：

```
第 1 步：执行调用栈中所有同步代码，直到栈为空
         ↓
第 2 步：检查微任务队列（Microtask Queue）
         只要队列不为空，就逐个取出执行（新产生的微任务也会在本轮继续执行）
         ↓
第 3 步：尝试进行 UI 渲染（如果有需要重绘的话）
         ↓
第 4 步：从宏任务队列（Macrotask Queue）中取出一个任务执行
         ↓
第 5 步：回到第 1 步，开始下一轮循环
```

**关键规则（务必记住）：**

1. **同步代码永远最先执行** —— 无论什么任务来了，都得等当前调用栈清空
2. **微任务优先于宏任务** —— 每轮循环中，会先清空全部微任务，再执行一个宏任务
3. **微任务可以"插队"** —— 如果在执行微任务的过程中又产生了新的微任务，新的微任务也会在本轮被继续执行（不会留给下一轮）
4. **每轮只执行一个宏任务** —— 但一个宏任务执行完毕后，会立刻回到第 2 步检查微任务

**初学者常见误区：**

| 误区 | 正解 |
|------|------|
| "`setTimeout(..., 0)` 会立刻执行" | 它会被放入宏任务队列，至少要等到当前同步代码 + 所有微任务执行完 |
| "微任务和宏任务是交替执行的" | 不是交替！是一整批微任务清空后，才执行一个宏任务 |
| "`await` 是同步的" | `await` 之前的代码同步执行，`await` 之后的代码被包装成微任务 |
| "`Promise.then` 里的回调会在当前代码结束后立刻执行" | 正确，但注意是"当前调用栈清空后"，而不是"下一行代码" |

#### 面试高频题

**一句话理解：** Event Loop 的面试题万变不离其宗——关键在于判断同步代码的执行顺序、Promise 回调进入微任务队列的时机、以及 setTimeout 进入宏任务队列的延迟。

**经典面试题 1：**

```js
console.log('1');

setTimeout(() => console.log('2'), 0);

Promise.resolve().then(() => console.log('3'));

Promise.resolve().then(() => setTimeout(() => console.log('4'), 0));

console.log('5');

// 输出：1 → 5 → 3 → 2 → 4
```

**解析：**
1. 同步：`1` → `5`
2. 微任务：`3`（Promise.then）
3. 宏任务：`2`（setTimeout）
4. 宏任务：`4`（Promise.then 中注册的 setTimeout）

**经典面试题 2：**

```js
async function async1() {
  console.log('2');
  await async2();
  console.log('4');
}

async function async2() {
  console.log('3');
}

console.log('1');
setTimeout(() => console.log('5'), 0);

async1();

console.log('6');

// 输出：1 → 2 → 3 → 6 → 4 → 5
```

**解析：**
- `await` 前面的代码（`console.log('2')`）同步执行
- `async2()` 本身是同步调用，`console.log('3')` 立即输出
- `await` 后面的代码（`console.log('4')`）相当于被包装成 `Promise.then`，放入微任务队列
- 因此同步代码 `1 → 2 → 3 → 6` 先走完，再执行微任务 `4`，最后执行宏任务 `5`

#### Event Loop 进阶：渲染、Node.js 差异与性能

**一句话理解：** 浏览器在 Event Loop 的每轮间隙有机会渲染页面，如果同步代码或微任务执行超过 16ms，就会掉帧卡顿；Node.js 的 Event Loop 比浏览器更复杂，有六个阶段。

**1. 渲染管道与 Event Loop 的关系**

浏览器在每一轮 Event Loop 结束时，会尝试进行一次 UI 渲染（如果需要）。这意味着：

```
同步代码 → 清空微任务 → [样式计算 → 布局 → 绘制 → 合成] → 下一个宏任务
                         ↑
                    渲染阶段（约 16.7ms/帧，60fps）
```

| 时机 | 会发生什么 |
|------|-----------|
| **同步代码执行期间** | 页面不会更新，用户看到的是"旧画面" |
| **微任务清空后** | 浏览器有机会进行渲染 |
| **宏任务之间** | 浏览器可以响应用户输入、更新界面 |

> ⚠️ **重要推论**：如果同步代码或微任务执行时间太长（超过 50ms），浏览器就来不及渲染，用户会感觉到**页面卡顿**。这就是"长任务（Long Task）"问题的根源。

```js
// ❌ 错误：阻塞主线程 3 秒，页面完全卡死
const btn = document.getElementById('btn');
btn.addEventListener('click', () => {
  const start = Date.now();
  while (Date.now() - start < 3000) {} // 3 秒内页面无法响应任何操作
  console.log('done');
});
```

**2. 浏览器 vs Node.js 的 Event Loop 差异**

两者核心思想相同，但实现细节有显著差异：

| 特性 | 浏览器（Browser） | Node.js |
|------|------------------|---------|
| **核心机制** | 单 Event Loop | 多 Phase（6 个阶段）的 Event Loop |
| **微任务** | `Promise.then`、`queueMicrotask`、`MutationObserver` | `Promise.then`、`queueMicrotask` |
| **Node 独有** | — | `process.nextTick`（优先级最高，甚至高于微任务） |
| **Node 独有** | — | `setImmediate`（在 I/O 事件后执行，优先级低于微任务） |
| **执行顺序** | 宏任务 → 微任务 → 渲染 → 下一宏任务 | timers → pending I/O → idle → poll → check → close → 下一循环 |

```js
// Node.js 特有的优先级演示
setTimeout(() => console.log('setTimeout'), 0);
setImmediate(() => console.log('setImmediate'));
Promise.resolve().then(() => console.log('Promise'));
process.nextTick(() => console.log('nextTick'));

// Node.js 输出：nextTick → Promise → setTimeout / setImmediate（顺序不固定）
// 浏览器输出：Promise → setTimeout
```

> **关键区别**：`process.nextTick` 是 Node.js 的"微任务中的微任务"，会在当前操作完成后、其他微任务之前立即执行。由于它可能"饿死" Event Loop，官方建议优先使用 `queueMicrotask`。

**3. 长时间任务的危害与优化**

当主线程被长时间占用时，用户会体验到：
- 点击按钮没有反应
- 滚动页面卡顿
- 动画掉帧
- 输入框延迟

**解决方案：任务切片（Yield to Main）**

将大任务拆分成多个小任务，在每个小任务之间把控制权交还给浏览器：

```js
// ✅ 正确：用 setTimeout / requestIdleCallback 拆分任务
function processChunk(items, chunkSize = 100) {
  let index = 0;

  function doChunk() {
    const end = Math.min(index + chunkSize, items.length);
    for (let i = index; i < end; i++) {
      processItem(items[i]);
    }
    index = end;

    if (index < items.length) {
      // 把控制权交还给浏览器，让用户有机会看到更新
      setTimeout(doChunk, 0);
    }
  }

  doChunk();
}

// ✅ 现代方式：使用 scheduler.yield()（Chrome 115+）
async function modernProcess(items) {
  for (const item of items) {
    processItem(item);
    // 每处理完一个就主动让出主线程
    if (scheduler?.yield) await scheduler.yield();
    else await new Promise(r => setTimeout(r, 0));
  }
}
```

**4. 给初学者的记忆口诀**

> **"同步先行，微队清零，一宏一巡，渲染伺机。"**
>
> - 同步代码最先跑完
> - 微任务队列要全部清空
> - 一次只取一个宏任务
> - 渲染穿插在任务间隙进行

---

### 4.2 回调函数与异步基础
#### 回调函数与回调地狱

**一句话理解：** 回调函数就是"你帮我做件事，做完后调用这个函数通知我"。但如果一件事套着一件事，回调就会一层一层嵌套，形成"回调地狱"。

**生活类比：**
- 回调函数 = **叫外卖时留的电话**：你点完餐（发起异步操作），留下电话号码（回调函数），商家做好后打电话通知你（执行回调）
- 回调地狱 = **俄罗斯套娃式的跑腿**：你去超市买酱油，买完后发现需要醋，买完醋发现需要蒜，买完蒜发现需要姜……每次都要先完成上一步才能知道下一步买什么，任务嵌套得越来越深，代码向右无限延伸

**回调函数：** 早期异步编程方式，将函数作为参数传递

```js
function loadScript(src, callback) {
  const script = document.createElement('script');
  script.src = src;
  script.onload = () => callback(null, script);
  script.onerror = () => callback(new Error('加载失败'));
  document.head.appendChild(script);
}

loadScript('a.js', (err, script) => {
  if (err) return console.error(err);
  loadScript('b.js', (err, script) => {
    if (err) return console.error(err);
    loadScript('c.js', (err, script) => {
      if (err) return console.error(err);
      // 继续嵌套...
    });
  });
});
```

**回调地狱（Callback Hell）：** 嵌套过深导致代码难以维护

```js
// 回调地狱示例
getUser(userId, (err, user) => {
  if (err) return handleError(err);
  getOrders(user.id, (err, orders) => {
    if (err) return handleError(err);
    getProducts(orders, (err, products) => {
      if (err) return handleError(err);
      processCart(products, (err, result) => {
        if (err) return handleError(err);
        // 终于拿到了结果
      });
    });
  });
});
```

**回调函数的问题总结：**
- 嵌套过深导致代码横向延伸，可读性差
- 错误处理需要在每个回调中重复写 `if (err)`
- 并行执行多个异步任务很困难

> 接下来的两节，我们将学习 **Promise** 和 **async/await** —— 它们就是为了解决回调地狱而诞生的现代异步方案。

### 4.3 Promise
#### 状态与链式调用


**Promise 状态机：**

```
┌─────────────────────────────────────────────────────────────┐
│                    Promise 状态机图                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│              new Promise(executor)                          │
│                     │                                       │
│                     ▼                                       │
│              ┌─────────────┐                                │
│              │   pending   │ ◄── 初始状态，待定             │
│              │   (待定)    │                                │
│              └──────┬──────┘                                │
│                     │                                       │
│         ┌───────────┴───────────┐                           │
│         │                       │                           │
│         ▼                       ▼                           │
│   ┌─────────────┐        ┌─────────────┐                   │
│   │  fulfilled  │        │  rejected   │                   │
│   │  (已兑现)   │        │  (已拒绝)   │                   │
│   │  resolve()  │        │  reject()   │                   │
│   └──────┬──────┘        └──────┬──────┘                   │
│          │                      │                           │
│          ▼                      ▼                           │
│        .then()               .catch()                       │
│     获取成功结果           获取失败原因                      │
│                                                             │
│  ⚠️ 状态一旦改变就不可再变：                                 │
│     pending → fulfilled 后，不能再变成 rejected              │
│     pending → rejected  后，不能再变成 fulfilled             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```


**一句话理解：** Promise 就是一个"承诺令牌"——你交给别人一个令牌（创建 Promise），对方要么兑现承诺（resolve）要么毁约（reject），而你可以用 `.then()` 来预约"兑现后要做的事"。

**生活类比：**
- Promise = **网购订单**：你下单后订单进入"待发货"（pending）状态，商家要么发货（fulfilled）要么缺货退款（rejected）。你可以提前设置"发货后通知我"（.then）和"缺货后联系我"（.catch），不用一直刷新页面等结果
- 链式调用 = **快递中转站**：每个 `.then()` 都是一个中转站，上一个站点的包裹（返回值）会自动送到下一个站点处理，如果某个站点出问题了，直接跳到异常处理中心（.catch）

Promise 有三种状态（**状态只能改变一次**）：

| 状态 | 含义 | 转换 |
|------|------|------|
| `pending` | 待定（初始状态） | → fulfilled 或 → rejected |
| `fulfilled` | 已兑现（操作成功） | 不可变 |
| `rejected` | 已拒绝（操作失败） | 不可变 |

```js
const promise = new Promise((resolve, reject) => {
  // pending 状态
  resolve('成功'); // → fulfilled
  // reject('失败'); // → rejected（只会执行一个）
});

promise
  .then(result => console.log(result))  // '成功'
  .catch(error => console.error(error)) // 不执行
  .finally(() => console.log('完成'));  // 始终执行
```

**链式调用原理：**
- `then`/`catch`/`finally` 返回新的 Promise
- 返回值作为下一个 Promise 的 resolve 值
- 抛出错误会使返回的 Promise 变为 rejected

```js
Promise.resolve(1)
  .then(x => x + 1)      // 2
  .then(x => {
    throw new Error('错误');
    return x;
  })
  .then(x => x + 1)      // 不执行
  .catch(e => -1)        // 捕获错误，返回 -1
  .then(x => console.log(x)); // -1
```

#### 静态方法（all / race / allSettled / any）

**一句话理解：** `Promise.all` 等所有成功、`Promise.race` 取第一个完成的、`Promise.allSettled` 等全部结束不管成败、`Promise.any` 取第一个成功的——按需选择并发控制策略。

| 方法 | 作用 | 特点 |
|------|------|------|
| `Promise.all()` | 所有 Promise 都 resolved 才返回 | 任一 rejected 则整体 rejected |
| `Promise.race()` | 返回最先 settled（resolved/rejected）的 | 竞速，谁先完成返回谁 |
| `Promise.allSettled()` | 等所有 Promise settled | 始终返回完整结果数组 |
| `Promise.any()` | 任一 resolved 则返回 | 全部 rejected 才 reject |

```js
// Promise.all - 全部成功才成功
Promise.all([p1, p2, p3])
  .then(([res1, res2, res3]) => console.log('全部成功'))
  .catch(err => console.log('有失败', err));

// Promise.race - 竞速
Promise.race([p1, p2, p3])
  .then(first => console.log('最先完成', first))
  .catch(err => console.log('最先失败', err));

// Promise.allSettled - 无论成功失败都返回
Promise.allSettled([p1, p2, p3]).then(results => {
  results.forEach((r, i) => {
    if (r.status === 'fulfilled') console.log(`p${i+1}成功:`, r.value);
    else console.log(`p${i+1}失败:`, r.reason);
  });
});

// Promise.any - 任一成功即成功
Promise.any([p1, p2, p3])
  .then(first => console.log('某个成功', first))
  .catch(err => console.log('全部失败', err.errors));
```

#### 常见面试题与手写实现

**手写 Promise（简化版）：**

```js
class MyPromise {
  constructor(executor) {
    this.state = 'pending';
    this.value = undefined;
    this.callbacks = [];

    const resolve = (value) => {
      if (this.state !== 'pending') return;
      this.state = 'fulfilled';
      this.value = value;
      // 必须用异步方式执行回调（Promise/A+ 规范要求）
      setTimeout(() => {
        this.callbacks.forEach(cb => cb.onFulfilled(value));
      });
    };

    const reject = (reason) => {
      if (this.state !== 'pending') return;
      this.state = 'rejected';
      this.value = reason;
      // 必须用异步方式执行回调（Promise/A+ 规范要求）
      setTimeout(() => {
        this.callbacks.forEach(cb => cb.onRejected(reason));
      });
    };

    try {
      executor(resolve, reject);
    } catch (e) {
      reject(e);
    }
  }

  then(onFulfilled, onRejected) {
    return new MyPromise((resolve, reject) => {
      const callback = {
        onFulfilled: onFulfilled || (v => v),
        onRejected: onRejected || (e => { throw e; })
      };

      if (this.state === 'pending') {
        this.callbacks.push({
          onFulfilled: () => {
            try {
              resolve(callback.onFulfilled(this.value));
            } catch (e) {
              reject(e);
            }
          },
          onRejected: () => {
            try {
              resolve(callback.onRejected(this.value));
            } catch (e) {
              reject(e);
            }
          }
        });
      } else if (this.state === 'fulfilled') {
        setTimeout(() => {
          try {
            resolve(callback.onFulfilled(this.value));
          } catch (e) {
            reject(e);
          }
        });
      } else {
        setTimeout(() => {
          try {
            resolve(callback.onRejected(this.value));
          } catch (e) {
            reject(e);
          }
        });
      }
    });
  }

  catch(onRejected) {
    return this.then(null, onRejected);
  }

  // ⚠️ 简化版 finally：未处理 onFinally 返回 rejected Promise 的情况
  // 标准行为：若 onFinally() 返回 rejected Promise，应传递该错误
  finally(onFinally) {
    return this.then(
      value => { onFinally(); return value; },
      reason => { onFinally(); throw reason; }
    );
  }

  static resolve(value) {
    return new MyPromise(resolve => resolve(value));
  }

  static reject(reason) {
    return new MyPromise((_, reject) => reject(reason));
  }
}
```

---

### 4.4 async / await
#### 语法糖与错误处理（try / catch）

**一句话理解：** `async/await` 就是给 Promise 穿了一件"同步代码的外衣"——你写的代码看起来是一行一行顺序执行的，但底层依然是 Promise 在运作。

**生活类比：**
- Promise 的 `.then().catch()` = **打电话办事**：打一个电话，对方说"办好了我再打给你"，你得守在电话旁等回调，一连串的事情要嵌套着打电话
- async/await = **面对面排队办事**：你站在窗口前（await），前面的人办完才轮到你，事情一件一件按顺序来，直观且不容易乱。但如果前面的人办得很慢，你后面的队伍（后续代码）也得等着

`async/await` 是 Promise 的语法糖，让异步代码看起来像同步代码。

```js
// async 函数返回 Promise
async function fetchData() {
  return 'data'; // 相当于 Promise.resolve('data')
}

fetchData().then(console.log); // 'data'

// await 暂停执行，等待 Promise 解决
async function process() {
  const result = await Promise.resolve('hello');
  console.log(result); // 'hello'
}
```

**错误处理：**

```js
// 方式1：try...catch
async function fetchUser(id) {
  try {
    const res = await fetch(`/api/user/${id}`);
    const data = await res.json();
    return data;
  } catch (error) {
    console.error('请求失败:', error);
    return null;
  }
}

// 方式2：Promise.catch
async function fetchUser2(id) {
  return fetch(`/api/user/${id}`)
    .then(res => res.json())
    .catch(error => {
      console.error('请求失败:', error);
      return null;
    });
}

// 方式3：顶层 await（ES2022）
// await 可以直接在模块顶层使用
const data = await fetch('/api/config').then(r => r.json());
```

#### 并发控制与顺序执行

**一句话理解：** 并发控制是"同时做多件事但不超过上限"，顺序执行是"一件做完再做下一件"——前者用 `Promise.all` 配合调度器，后者用 `for...of` 配合 `await`。

```js
// ❌ 错误：串行执行，不必要地等待
async function wrongApproach(urls) {
  const results = [];
  for (const url of urls) {
    const res = await fetch(url); // 每个请求等前一个完成
    results.push(await res.json());
  }
  return results;
}

// ✅ 正确：并发执行
async function rightApproach(urls) {
  const promises = urls.map(url => fetch(url).then(r => r.json()));
  return Promise.all(promises);
}

// ✅ 带并发限制的并发执行（⚠️ 教学简化版，生产环境推荐 p-limit 库）
async function limitedConcurrency(urls, limit = 3) {
  if (limit <= 0) throw new Error('limit must be > 0');
  const results = [];
  const executing = new Set();

  for (const url of urls) {
    const promise = fetch(url).then(r => r.json());
    results.push(promise);

    // 用 Set 避免数组 splice 的竞态问题（多个 Promise 同时完成时）
    const p = promise.finally(() => executing.delete(p));
    executing.add(p);

    if (executing.size >= limit) {
      await Promise.race(executing);
    }
  }

  return Promise.all(results);
}

// 顺序执行：需要保序的场景
async function sequential(urls) {
  const results = [];
  for (const url of urls) {
    const res = await fetch(url);
    results.push(await res.json());
  }
  return results;
}
```

---

### 4.5 其他异步方案

**一句话理解：** Generator 函数是"可以暂停和恢复的函数"，通过 `yield` 交出执行权、通过 `next()` 恢复执行——它是理解 async/await 底层实现的重要概念。

Generator 是可暂停和恢复的函数，通过 `yield` 产生值。

```js
function* numberGenerator() {
  yield 1;
  yield 2;
  return 3;
}

const gen = numberGenerator();
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: true }

// 生成器用于异步流程控制
function* asyncFlow() {
  const data = yield fetch('/api/data').then(r => r.json());
  const more = yield fetch('/api/more').then(r => r.json());
  return { data, more };
}

// 使用
function run(generator) {
  const gen = generator();

  function step({ value, done }) {
    if (done) return value;
    return value.then(
      data => step(gen.next(data)),
      err => step(gen.throw(err))
    );
  }

  return step(gen.next());
}

run(asyncFlow);
```

#### 顶层 await

**一句话理解：** ES2022 允许在模块顶层直接使用 `await`，让模块加载本身变成异步的——适合在模块初始化时执行异步配置读取或数据获取。

ES2022 支持在模块顶层使用 `await`。

```js
// module.js
const data = await fetch('/api/config').then(r => r.json());
export const config = data;

// 场景1：动态模块初始化
const messages = await import('./messages.js');

// 场景2：条件加载
const isLoggedIn = await checkAuth();
const module = isLoggedIn
  ? await import('./loggedIn.js')
  : await import('./loggedOut.js');

// 注意：顶层 await 会阻塞模块执行
// 可能影响并行加载的其他模块
```

### 🛠️ 实操：异步编程实战

#### 手写实现一个简化版 Promise（理解核心原理）

**核心思路：** Promise/A+ 规范的核心是：状态机 + 回调队列 + 异步执行。

**实现要点：**
- **状态机**：只能从 pending → fulfilled 或 pending → rejected，不能反向转换
- **回调存储**：then 可以多次调用，需要存储成功/失败回调队列
- **异步执行**：根据规范，`then` 的回调必须异步执行，用 `setTimeout` 模拟
- **值穿透**：若省略 onFulfilled 或 onRejected，上一个 Promise 的值/原因会自动传递到下一个 then

**关键细节：**
- `onFulfilled` 和 `onRejected` 可选，如果忽略值会继续传递
- 抛出的异常会被下一个 catch 捕获
- 需要处理 `then` 在 Promise 内部被同步调用的情况（此时状态还是 pending）

**验证方法：** 使用 `promises-aplus-tests` 包运行规范测试

```js
class MyPromise {
  constructor(executor) {
    this.state = 'pending';
    this.value = undefined;
    this.reason = undefined;
    this.onFulfilledCallbacks = [];
    this.onRejectedCallbacks = [];

    const resolve = (value) => {
      if (this.state === 'pending') {
        this.state = 'fulfilled';
        this.value = value;
        // 异步执行回调（模拟微任务，实际可用 queueMicrotask）
        setTimeout(() => {
          this.onFulfilledCallbacks.forEach(fn => fn());
        });
      }
    };

    const reject = (reason) => {
      if (this.state === 'pending') {
        this.state = 'rejected';
        this.reason = reason;
        // 异步执行回调（模拟微任务，实际可用 queueMicrotask）
        setTimeout(() => {
          this.onRejectedCallbacks.forEach(fn => fn());
        });
      }
    };

    try {
      executor(resolve, reject);
    } catch (err) {
      reject(err);
    }
  }

  then(onFulfilled, onRejected) {
    onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : value => value;
    onRejected = typeof onRejected === 'function' ? onRejected : reason => { throw reason };

    const promise2 = new MyPromise((resolve, reject) => {
      const handleFulfilled = () => {
        setTimeout(() => {
          try {
            const x = onFulfilled(this.value);
            this.resolvePromise(promise2, x, resolve, reject);
          } catch (e) {
            reject(e);
          }
        }, 0);
      };

      const handleRejected = () => {
        setTimeout(() => {
          try {
            const x = onRejected(this.reason);
            this.resolvePromise(promise2, x, resolve, reject);
          } catch (e) {
            reject(e);
          }
        }, 0);
      };

      if (this.state === 'fulfilled') {
        handleFulfilled();
      } else if (this.state === 'rejected') {
        handleRejected();
      } else {
        this.onFulfilledCallbacks.push(handleFulfilled);
        this.onRejectedCallbacks.push(handleRejected);
      }
    });

    return promise2;
  }

  resolvePromise(promise2, x, resolve, reject) {
    if (promise2 === x) {
      return reject(new TypeError('Chaining cycle detected for Promise'));
    }

    if (x && (typeof x === 'object' || typeof x === 'function')) {
      let called = false;
      try {
        const then = x.then;
        if (typeof then === 'function') {
          then.call(x, y => {
            if (called) return;
            called = true;
            this.resolvePromise(promise2, y, resolve, reject);
          }, err => {
            if (called) return;
            called = true;
            reject(err);
          });
        } else {
          resolve(x);
        }
      } catch (e) {
        if (called) return;
        called = true;
        reject(e);
      }
    } else {
      resolve(x);
    }
  }

  catch(onRejected) {
    return this.then(null, onRejected);
  }

  static resolve(value) {
    return new MyPromise(resolve => resolve(value));
  }

  static reject(reason) {
    return new MyPromise((_, reject) => reject(reason));
  }
}

// 基础用法验证
const p = new MyPromise((resolve, reject) => {
  setTimeout(() => resolve('ok'), 100);
});

p.then(val => {
  console.log(val); // ok
  return val + '!';
}).then(val => {
  console.log(val); // ok!
});
```

---

#### 实现一个带并发限制的请求调度器（如同时最多 3 个请求）

**核心思路：** 控制同时运行的异步任务数量，未执行的任务排队等待。

**实现要点：**
- **任务队列**：维护一个待执行的任务队列
- **运行中的任务跟踪**：记录当前正在执行的任务数量
- **任务完成后触发**：每当有任务完成，从队列取出下一个任务执行
- **Promise 化**：返回 Promise，以便调用方知道任务完成

**两种实现方式：**
1. **class 方式**：封装成类，提供 `add(task)` 方法
2. **函数方式**：返回包装后的 Promise 函数

**关键细节：**
- 队列空时需要等待，不能无限添加
- 需要处理任务被取消的场景
- 可以添加优先级队列支持

```js
class Scheduler {
  constructor(maxConcurrency) {
    this.maxConcurrency = maxConcurrency;
    this.runningCount = 0;
    this.queue = [];
  }

  add(promiseCreator) {
    return new Promise((resolve, reject) => {
      this.queue.push({ promiseCreator, resolve, reject });
      this.run();
    });
  }

  run() {
    while (this.runningCount < this.maxConcurrency && this.queue.length > 0) {
      const { promiseCreator, resolve, reject } = this.queue.shift();
      this.runningCount++;
      // 经 Promise 承接：promiseCreator 同步抛错也不会丢失并发名额
      Promise.resolve()
        .then(promiseCreator)
        .then(resolve, reject)
        .finally(() => {
          this.runningCount--;
          this.run();
        });
    }
  }
}

// ===== 使用示例 =====
const scheduler = new Scheduler(3);

const timeout = (time) => {
  return new Promise(resolve => {
    setTimeout(() => {
      console.log(`任务完成，耗时 ${time}ms`);
      resolve(time);
    }, time);
  });
};

// 添加 5 个任务，但最多同时执行 3 个
[1000, 500, 300, 400, 200].forEach(time => {
  scheduler.add(() => timeout(time)).then(() => {
    console.log(`Promise resolved: ${time}`);
  });
});
```

---

#### 实现一个请求重试机制（失败自动重试 N 次，支持退避策略）

**核心思路：** 失败后自动重试，通过增加间隔时间来避免过度请求。

**实现要点：**
- **重试次数限制**：设置最大重试次数 `maxRetries`
- **退避策略**：每次重试间隔逐渐增加
  - 线性退避：`delay = baseDelay * attempt`
  - 指数退避：`delay = baseDelay * 2^attempt`（常用）
  - 抖动（jitter）：加上随机值避免惊群效应
- **可重试判断**：区分可重试错误（如网络超时）和不可重试错误（如 404）
- **重试计数**：只有可重试错误才计数

**退避策略示例：**
```js
// 指数退避 + 抖动
function getDelay(attempt, baseDelay = 1000) {
  const exp = Math.min(baseDelay * 2 ** attempt, 30000); // 最大30秒
  const jitter = Math.random() * 1000;
  return exp + jitter;
}
```

**关键细节：**
- 使用 `async/await` 实现同步风格的代码
- 每次重试前等待 delay 时间
- 最终失败后抛出有意义的错误信息

```js
async function retryWithBackoff(fn, {
  maxRetries = 3,
  baseDelay = 1000,
  maxDelay = 30000,
  backoffType = 'exponential', // 'linear' | 'exponential'
  jitter = true,
  shouldRetry = () => true,
  onRetry = null
} = {}) {
  let lastError;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (err) {
      lastError = err;

      if (attempt === maxRetries || !shouldRetry(err)) {
        throw err;
      }

      let delay;
      if (backoffType === 'exponential') {
        delay = Math.min(baseDelay * 2 ** attempt, maxDelay);
      } else {
        delay = Math.min(baseDelay * (attempt + 1), maxDelay);
      }

      if (jitter) {
        delay += Math.random() * 1000;
      }

      if (onRetry) {
        onRetry(err, attempt + 1);
      }

      console.log(`第 ${attempt + 1} 次请求失败，${Math.round(delay)}ms 后重试...`);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }

  throw lastError;
}

// ===== 使用示例 =====
retryWithBackoff(
  () => fetch('/api/data').then(r => {
    if (!r.ok) {              // HTTP 状态错误也要抛出，交由 shouldRetry 判断
      const err = new Error(`HTTP ${r.status}`);
      err.status = r.status;
      throw err;
    }
    return r.json();
  }),
  {
    maxRetries: 3,
    baseDelay: 1000,
    shouldRetry: (err) => {
      // 仅对网络错误或 5xx 服务端错误进行重试
      return !err.status || err.status >= 500;
    },
    onRetry: (err, attempt) => {
      console.warn(`重试第 ${attempt} 次`, err.message);
    }
  }
).then(data => console.log('成功:', data))
 .catch(err => console.error('最终失败:', err));
```

---

#### 用 async/await 完成一个数据分页加载器（含加载状态与错误处理）

**核心思路：** 封装分页逻辑，自动加载下一页直到数据加载完。

**实现要点：**
- **状态管理**：维护 `data`（已加载数据）、`page`（当前页）、`loading`（加载中）、`error`（错误）
- **加载函数**：调用 API 获取某一页数据
- **加载更多**：判断是否还有下一页，加载下一页并合并数据
- **状态回调**：提供回调函数，让 UI 可以响应状态变化

**核心 API 设计：**
```js
const loader = createPaginatedLoader({
  fetchPage: (page) => fetch(`/api/items?page=${page}&size=20`).then(r => r.json()),
  hasMore: (data) => data.length > 0,
  onStateChange: (state) => updateUI(state)
});

await loader.loadAll(); // 加载全部
await loader.loadMore(); // 加载下一页
loader.reset(); // 重置状态
```

**关键细节：**
- `hasMore` 判断逻辑可能因 API 而异（检查 totalPages 或空数组）
- 错误处理：单个页面失败可以重试整个加载流程
- 竞态条件：如果用户快速调用多次 `loadMore`，需要忽略重复调用
- 取消机制：可选，支持在加载过程中取消

```js
function createPaginatedLoader({
  fetchPage,
  hasMore,
  onStateChange,
  initialPage = 1
}) {
  let state = {
    data: [],
    page: initialPage,
    loading: false,
    error: null,
    done: false
  };

  let currentRequest = null;

  const setState = (newState) => {
    state = { ...state, ...newState };
    if (onStateChange) onStateChange({ ...state });
  };

  return {
    get state() {
      return { ...state };
    },

    async loadMore() {
      if (state.loading || state.done) return state;

      const thisRequest = {};
      currentRequest = thisRequest;

      setState({ loading: true, error: null });

      try {
        const pageData = await fetchPage(state.page);

        // 竞态保护：若已有新请求发出，忽略本次结果
        if (currentRequest !== thisRequest) return state;

        const done = !hasMore(pageData);
        setState({
          data: [...state.data, ...pageData],
          page: state.page + 1,
          loading: false,
          done
        });
      } catch (err) {
        if (currentRequest !== thisRequest) return state;
        setState({ loading: false, error: err });
      }

      return state;
    },

    async loadAll() {
      while (!state.done && !state.loading) {
        await this.loadMore();
        if (state.error) break; // 失败即停，避免持续失败时无限重试
      }
      return state;
    },

    reset() {
      currentRequest = null;
      setState({
        data: [],
        page: initialPage,
        loading: false,
        error: null,
        done: false
      });
    }
  };
}

// ===== 使用示例 =====
const loader = createPaginatedLoader({
  fetchPage: (page) =>
    fetch(`/api/items?page=${page}&size=20`).then(r => r.json()),
  hasMore: (data) => data.length > 0,
  onStateChange: (state) => {
    console.log('加载状态:', state.loading, '已加载:', state.data.length);
  }
});

// 加载下一页
await loader.loadMore();

// 加载全部剩余页
await loader.loadAll();

// 重置
loader.reset();
```

> **本章小结：** 我们理解了 Event Loop 的工作原理、Promise 的状态与链式调用、async/await 的语法糖本质，并实现了并发调度器、请求重试机制和分页加载器等实战代码。
>
> **下一章预告：** 在掌握了异步编程后，让我们把代码从"纸面"带到"浏览器"——学习 DOM 操作、事件系统、浏览器 API 以及前端性能优化。
