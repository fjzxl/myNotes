---
title: "JavaScript 核心知识体系 · 三、核心运行机制"
tags:
  - programming
  - javascript
created: 2026-09-10
updated: 2026-10-01
---

# 三、核心运行机制

> 📚 本文是 [[topics/programming/Web/javascript|JavaScript 核心知识体系]] 的第 3 / 8 章。 上一章：[[topics/programming/Web/javascript/02-reference-types|二、引用类型详解]] · 下一章：[[topics/programming/Web/javascript/04-asynchronous-programming|四、异步编程]]


> **本章定位：** JavaScript 的"内功心法"。执行上下文、作用域链、闭包、this 绑定、原型链与继承——这些概念比较抽象，但理解它们之后，你就能看透任何 JavaScript 代码的运行逻辑。
>
> **学习路线：** 执行上下文与作用域（代码运行的"舞台"）→ this 绑定（谁调用我）→ 原型链与继承（对象的关系网）→ IIFE（模块化的前身）→ 手写实现核心 API
>
> **建议：** 本章概念较抽象，建议配合浏览器 DevTools 的断点调试（Sources 面板）来学习。遇到看不懂的概念，先假设它成立，继续往下读，回头再看会有新的理解。

### 3.1 执行上下文与作用域

#### 全局 / 函数 / 块级执行上下文


**执行上下文栈变化过程：**

```
调用栈 (Call Stack) 的变化：

初始状态：
┌─────────────────┐
│  全局上下文      │ ◄── 栈底（始终存在）
│  globalVar      │
└─────────────────┘

执行 outer()：
┌─────────────────┐
│  outer 上下文   │ ◄── 栈顶
│  outerVar       │
├─────────────────┤
│  全局上下文      │
│  globalVar      │
└─────────────────┘

执行 inner()：
┌─────────────────┐
│  inner 上下文   │ ◄── 栈顶（正在执行）
│  innerVar       │
├─────────────────┤
│  outer 上下文   │
│  outerVar       │
├─────────────────┤
│  全局上下文      │
│  globalVar      │
└─────────────────┘

inner() 执行完毕：
┌─────────────────┐
│  outer 上下文   │ ◄── 回到栈顶，继续执行
│  outerVar       │
├─────────────────┤
│  全局上下文      │
└─────────────────┘
```


**一句话理解：** 执行上下文就是 JavaScript 引擎运行代码时的"工作环境快照"，它记录了当前有哪些变量、函数、以及 `this` 指向谁。每次进入函数或脚本时，引擎都会拍一张新快照。

**生活类比：**
- 执行上下文 = **剧院的舞台场景**：每一场戏（函数调用）都有自己的布景、道具和演员名单（变量环境）。上一场戏的道具不会带到下一场，除非演员（闭包）把道具带出了剧场
- 全局上下文 = **剧院大厅**：所有观众和工作人员（全局变量）都在大厅里，最先布置，最后撤场
- 函数上下文 = **临时舞台**：每演一场戏就搭一个新舞台，戏演完了就拆掉（出栈）

**执行上下文（Execution Context）**是 JavaScript 引擎执行代码时的"运行环境"。JavaScript 中有三种执行上下文。

**三种类型：**

| 类型 | 创建时机 | 特点 |
|------|----------|------|
| **全局上下文** | 脚本首次运行 | 浏览器中 `window`（Node 中 `global`），最先创建，最后销毁 |
| **函数上下文** | 每次调用函数 | 每次调用都创建一个独立的函数上下文 |
| **eval 上下文** | 调用 `eval()` 时 | `eval` 内部的代码在当前执行上下文中运行，但会创建新的词法环境 |

> **注意**：`let`/`const` 所在的代码块 `{}` 不会创建新的**执行上下文**，而是创建一个新的**词法环境（Lexical Environment）**来管理块级作用域。这是执行上下文内部的机制，不要混淆。

```js
// 执行上下文的变化演示
const globalVar = '我在全局';

function outer() {
  const outerVar = '我在 outer';
  console.log(this); // 函数上下文中的 this（非严格模式为 window）

  function inner() {
    const innerVar = '我在 inner';
    // inner 可以访问 outerVar 和 globalVar —— 作用域链向上查找
    console.log(innerVar, outerVar, globalVar);
  }
  inner(); // 创建 inner 的函数执行上下文
}

outer(); // 创建 outer 的函数执行上下文
// 全局执行上下文一直存在，直到页面关闭
```

#### 关于 `eval()` 执行上下文

**一句话理解：** `eval()` 是一个"危险的后门"——它能执行任意字符串代码，但会带来性能损耗、安全风险和调试困难，现代开发中应尽量避免使用。

`eval()` 直接调用时**在当前执行上下文中创建新的词法环境**，内部可以访问外部变量，同时它声明的变量也可能"泄露"到外部（非严格模式下 `var` 会绑定到当前作用域）。间接调用时则在全局作用域执行。

**直接调用 vs 间接调用：**

| 调用方式 | 示例 | 作用域行为 |
|---------|------|-----------|
| **直接调用** | `eval('var x = 1')` | 在当前作用域执行，变量可能泄露到外部 |
| **间接调用** | `(0, eval)('var x = 1')` | 在全局作用域执行，始终操作全局对象 |

**代码示例：**

```js
function demo() {
  const outer = 'I am outer';

  // 直接调用：可以访问并修改外部作用域
  eval("console.log(outer); var leaked = 'I leak out'");

  console.log(leaked); // 'I leak out'（非严格模式下 var 泄露）
}
demo();
// console.log(leaked); // ❌ ReferenceError: leaked is not defined（函数外不可见）

// 严格模式下 eval 拥有独立作用域，不会泄露
function strictDemo() {
  'use strict';
  eval("var notLeaked = 'I am trapped'");
  // console.log(notLeaked); // ❌ ReferenceError
}
strictDemo();

// 间接调用始终指向全局作用域
function indirectEval() {
  const x = 'local';
  (0, eval)("console.log(typeof x); var globalVar = 'I am global'");
}
indirectEval();
console.log(globalThis.globalVar); // 'I am global'（浏览器/Node 均可访问）
```

> ⚠️ **为什么不推荐使用 `eval`**
> 1. **性能**：JS 引擎无法在编译期优化包含 `eval` 的作用域，因为运行时可能注入任意代码。
> 2. **安全**：执行任意字符串代码极易遭受 XSS / 代码注入攻击。
> 3. **调试困难**：动态生成的代码难以追踪错误堆栈。
>
> 现代替代方案：`JSON.parse()`（解析 JSON）、`new Function()`（创建隔离作用域的函数）、模板字符串（动态拼接）、`Proxy` + `Reflect`（元编程）。

```js
// 全局上下文
const globalVar = '全局';

function outer() {
  // outer 函数上下文
  const outerVar = 'outer';

  function inner() {
    // inner 函数上下文
    const innerVar = 'inner';
    console.log(globalVar, outerVar, innerVar); // 三者皆可访问
  }
  inner();
}
outer();
```

#### 全局上下文的差异：浏览器 vs Node

**一句话理解：** 浏览器中的全局对象是 `window`，Node.js 中是 `global`，ES2020 又统一了 `globalThis`——写跨平台代码时要注意这个差异。

全局上下文在不同运行环境中的具体表现有显著差异，理解这些差异对编写跨平台代码至关重要。

| 特性 | 浏览器（Browser） | Node.js |
|------|------------------|---------|
| **全局对象** | `window` | `global` |
| **顶层 `this`** | 指向 `window` | 模块内指向 `module.exports`；REPL 中指向 `global` |
| **全局变量挂载** | `var`/`function` 声明自动成为 `window` 的属性 | 模块文件内的 `var`/`function` 属于模块作用域，**不会**自动挂载到 `global` |
| **脚本引入方式** | `<script>` 标签直接运行 | 文件即模块，默认拥有独立作用域 |
| **跨平台统一访问** | `globalThis` 指向 `window` | `globalThis` 指向 `global` |

**浏览器环境示例：**

```js
var browserVar = 'I am on window';
function browserFn() { return 'hello'; }

console.log(window.browserVar); // 'I am on window'
console.log(window.browserFn === browserFn); // true
console.log(this === window); // true（普通脚本）；ES 模块中顶层 this 为 undefined
```

**Node.js 环境示例：**

```js
var nodeVar = 'I am module-scoped';
function nodeFn() { return 'hello'; }

console.log(global.nodeVar); // undefined（模块隔离）
console.log(global.nodeFn === nodeFn); // false（模块隔离）

// 必须显式挂载才会进入全局对象
global.explicitGlobal = 'truly global';
console.log(global.explicitGlobal); // 'truly global'

console.log(this === module.exports); // true（CJS 模块）；ESM 中顶层 this 为 undefined
console.log(this === global); // false
```

**使用 `globalThis` 消除环境差异：**

```js
// ES2020 标准，任何环境都可用
globalThis.setTimeout === window?.setTimeout; // true（浏览器）
globalThis.setTimeout === global.setTimeout;  // true（Node）

// 安全的全局对象引用
const root = globalThis;
```

> **关键结论：** 浏览器中全局上下文就是全局命名空间；而 Node.js 中每个文件默认是一个模块，拥有独立的作用域，只有显式赋值给 `global` / `globalThis` 或使用 `global.` 前缀声明的变量才是真正全局的。

#### 变量对象与作用域链


**作用域链查找路径：**

```
全局作用域
  └── outer() 作用域
        └── inner() 作用域

inner 中访问变量时的查找顺序：
  1. 先在 inner 自身的变量对象中查找
  2. 找不到 → 沿着作用域链向上，到 outer 的变量对象查找
  3. 找不到 → 继续向上，到全局变量对象查找
  4. 找不到 → ReferenceError: xxx is not defined

┌─────────────────────────────────────────────┐
│  inner 作用域                                │
│    能找到：innerVar                          │
│    找不到 → 向上                             │
├─────────────────────────────────────────────┤
│  outer 作用域                                │
│    能找到：outerVar, innerVar（作用域链查找）│
│    找不到 → 向上                             │
├─────────────────────────────────────────────┤
│  全局作用域                                  │
│    能找到：globalVar                         │
│    找不到 → ReferenceError                   │
└─────────────────────────────────────────────┘
```


**一句话理解：** 变量对象是执行上下文中的"变量仓库"，作用域链是多个变量对象按层级连接成的查找路径——找变量时就沿着这条链从内向外搜索。

**变量对象（VO / AO）：**

每个执行上下文都有一个变量对象，用于存储：
- 函数形参（函数上下文）
- 函数声明（函数声明提升）
- 变量声明（`var`，提升但值为 `undefined`）

| 上下文类型 | 变量对象包含 |
|-----------|-------------|
| 全局上下文 | 全局变量（`var` 声明）、函数声明 |
| 函数上下文 | 形参、函数声明（提升）、`var` 声明（提升） |
| 块级作用域 | `let`/`const` 声明（由词法环境管理，不创建新的执行上下文） |

**作用域链：**

当查找变量时，引擎沿着**作用域链**从内向外搜索：

```js
const a = '全局';

function outer() {
  const b = 'outer';

  function inner() {
    const c = 'inner';
    console.log(a, b, c); // 沿作用域链向外找
  }
  inner();
}
outer();
```

```
inner 函数上下文
    ↓
outer 函数上下文（b / outerVar 在这里）
    ↓
全局上下文（globalVar 在这里）
    ↓
报错 ReferenceError
```

#### 闭包的形成条件与内存管理


**闭包内存结构图：**

```
outer() 执行完毕，调用栈已弹出 outer
但 outer 的词法环境未被回收！

┌─────────────────────────────────────────┐
│  堆内存中保留的闭包环境                  │
│                                         │
│  ┌─────────────────┐                    │
│  │ outer 的词法环境 │ ◄── 被 inner 引用  │
│  │   count: 0      │    无法被垃圾回收  │
│  │   name: "x"     │                    │
│  └─────────────────┘                    │
│           ▲                             │
│           │                             │
│  ┌────────┴────────┐                    │
│  │   inner 函数     │  持有对 outer 环境的引用
│  │  [[Scopes]]      │  （这就是闭包！）   │
│  └─────────────────┘                    │
└─────────────────────────────────────────┘

outer() 虽然执行完了，但只要 inner 还被外部引用，
outer 的变量环境就会一直留在内存中，供 inner 访问。
```


**一句话理解：** 闭包就是函数"记住了"自己诞生时的环境，即使这个环境已经"结束"了，函数依然能访问那里的变量。就像一个人带着家乡的方言去外地工作，无论走到哪里，他都能说家乡话。

**生活类比：**
- 闭包 = **带钥匙出门的人**：你住在某栋公寓（外部函数）的 302 室，你有一把钥匙（内部函数）。即使你离开公寓大楼（外部函数执行完毕），你依然能凭钥匙回到 302 室（访问外部变量）。这把钥匙就是闭包
- 没有闭包 = **访客**：你只是去公寓拜访朋友，离开后你就再也进不去了

**闭包（Closure）**：当函数能访问其词法作用域外部的变量时，就形成了闭包。闭包 = 函数 + 其词法环境的引用。

**闭包形成的条件：**
1. 内部函数定义在外部函数中，且**引用了外部函数的变量**
2. 内部函数被外部返回或传递给其他地方（使外部能继续持有该函数的引用）

> 闭包在内部函数被创建并引用外部变量时即已形成。"外部引用仍然存在"是闭包**持续存在**的条件，而非形成条件。

```js
function outer() {
  const x = 'closure';

  // inner 被返回，外部仍有引用
  return function inner() {
    console.log(x); // x 是闭包变量
  };
}

const fn = outer(); // outer 已执行完毕，但 x 仍被 inner 引用，不会被 GC 回收
fn(); // 'closure'
```

**内存管理要点：**

| 场景 | 内存释放 | 原因 |
|------|----------|------|
| 闭包无外部引用 | ✅ 被 GC 回收 | 闭包对象成为垃圾 |
| 闭包被长期不必要地持有 | ❌ 内存泄漏 | 闭包引用的变量无法释放 |
| 闭包引用大对象 | ⚠️ 注意 | 可能导致内存持续增长 |

```js
// 典型内存泄漏：闭包引用大量数据
function bad() {
  const largeData = new Array(1000000).fill('x');
  const small = '只用到一点点';

  return function() {
    return small; // 现代引擎（如 V8）通常只保留实际引用的变量，但旧引擎可能保留整个作用域对象
  };
}

// 正确做法：避免在闭包中捕获不必要的大对象
function good() {
  const small = '只用到一点点';

  return function() {
    return small;  // 只捕获需要的小变量
  };
  // 没有 largeData，不存在内存泄漏风险
}
```


**初学者常见错误：**
- ❌ 在循环中创建闭包时，所有闭包共享同一个变量：`for (var i = 0; i < 3; i++) { setTimeout(() => console.log(i), 0); }` 输出 3 个 3
- ✅ 用 `let` 替代 `var`，或用 IIFE 创建独立作用域
- ❌ 闭包持有大量数据但从不释放——会导致内存泄漏，闭包用完后应解除引用
- ❌ 以为闭包只和返回函数有关——实际上只要内部函数引用了外部变量，就形成了闭包（"被外部访问"只决定闭包生命周期，不是形成条件）

#### 闭包实战应用（模块化 / 柯里化 / 数据缓存）

**一句话理解：** 闭包不仅是面试考点，更是实战利器——用它实现模块化封装、函数柯里化（逐步传参）和数据缓存，能大幅提升代码的封装性和复用性。

**1. 模块化（Module Pattern）：**

利用闭包创建私有变量，模拟面向对象的封装：

```js
const Counter = (function() {
  let count = 0; // 私有变量，外部无法直接访问

  return {
    increment() { return ++count; },
    decrement() { return --count; },
    getCount() { return count; }
  };
})();

Counter.increment(); // 1
Counter.increment(); // 2
Counter.getCount();  // 2
Counter.count;       // undefined（私有，访问不到）
```

**2. 柯里化（Currying）：**

将多参数函数转化为单参数函数链，闭包保存中间状态：

```js
function curriedAdd(a) {
  return function(b) {
    return a + b;
  };
}
const add5 = curriedAdd(5);
add5(3); // 8
add5(10); // 15（5 被闭包保存）

// 通用柯里化
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn(...args);
    }
    return function(...args2) {
      return curried(...args, ...args2);
    };
  };
}

const add = curry((a, b, c) => a + b + c);
add(1)(2)(3);  // 6
add(1, 2)(3);  // 6
add(1, 2, 3);  // 6
```

**3. 数据缓存（Memoization）：**

闭包保存计算结果，避免重复计算：

```js
function memoize(fn) {
  const cache = {}; // 闭包中的缓存

  return function(...args) {
    const key = JSON.stringify(args);
    if (Object.prototype.hasOwnProperty.call(cache, key)) {
      console.log('命中缓存');
      return cache[key];
    }
    const result = fn(...args);
    cache[key] = result;
    return result;
  };
}

const fib = memoize(function(n) {
  return n <= 1 ? n : fib(n - 1) + fib(n - 2);
});
fib(10);  // 首次计算
fib(10);  // 命中缓存
```

---

### 3.2 this 绑定机制

#### 四种绑定规则（默认 / 隐式 / 显式 / new）

**一句话理解：** `this` 不是函数自带的属性，而是函数被调用时"临时颁发的身份牌"——谁调用的我，我就是谁；没人调用我，我就是全局（或 `undefined`）；用 `new` 调用我，我就是新对象。

**生活类比：**
- `this` = **角色扮演游戏中的"当前角色"**：同一个人（函数）在不同的剧本（调用场景）中扮演不同的角色（`this` 指向）
  - 默认绑定 = **路人甲**：没人给你发角色卡，你就是默认身份（全局对象）
  - 隐式绑定 = **团队任务**：队长（`obj`）喊你做事，你的身份就是队长的队员
  - 显式绑定 = **导演指定**：导演（`call/apply/bind`）直接指定你演谁
  - new 绑定 = **新生儿**：你扮演的是一个全新诞生的角色（实例对象）

`this` 的指向由**调用方式**决定，共有四种绑定规则：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          this 绑定规则速查图                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                      「this 是谁？」—— 四个问题帮你快速判断                  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────┐    │
│   │  问题 1：是否用 new 调用？                                         │    │
│   │         是 → this = 新创建的实例对象                               │    │
│   │         否 ↓                                                      │    │
│   └─────────────────────────────────────────────────────────────────┘    │
│                                 ↓                                          │
│   ┌─────────────────────────────────────────────────────────────────┐    │
│   │  问题 2：是否用 call/apply/bind 显式绑定？                        │    │
│   │         是 → this = 指定的对象                                     │    │
│   │         否 ↓                                                      │    │
│   └─────────────────────────────────────────────────────────────────┘    │
│                                 ↓                                          │
│   ┌─────────────────────────────────────────────────────────────────┐    │
│   │  问题 3：是否通过 obj.method() 隐式调用？                          │    │
│   │         是 → this = obj（谁调用就指向谁）                          │    │
│   │         否 ↓                                                      │    │
│   └─────────────────────────────────────────────────────────────────┘    │
│                                 ↓                                          │
│   ┌─────────────────────────────────────────────────────────────────┐    │
│   │  问题 4：以上都不是？                                              │    │
│   │         → this = 全局对象（严格模式为 undefined）                   │    │
│   └─────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│   📝 记忆口诀：「new > 显式 > 隐式 > 默认」                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 绑定规则 | 调用方式 | `this` 指向 | 优先级 |
|----------|----------|------------|--------|
| **默认绑定** | 普通函数调用 | 全局对象（严格模式为 `undefined`） | 最低 |
| **隐式绑定** | `obj.method()` | `obj`（调用上下文的对象） | ⭐⭐⭐ |
| **显式绑定** | `call/apply/bind` | 指定的对象 | ⭐⭐⭐⭐ |
| **new 绑定** | `new Constructor()` | 新创建的对象 | 最高 |

**1. 默认绑定（Default Binding）：**

```js
function say() {
  console.log(this);
}

say(); // 非严格模式：window / 严格模式：undefined

const obj = {
  name: 'Alice',
  say: say
};
obj.say(); // this 被隐式绑定为 obj
```

**2. 隐式绑定（Implicit Binding）：**

```js
const person = {
  name: 'Bob',
  greet() {
    console.log(`I am ${this.name}`);
  }
};

person.greet(); // 'I am Bob' — this 指向 person

// 隐式丢失
const fn = person.greet;
fn(); // 'I am '（浏览器中 window.name 默认为空字符串）— fn 引用的是普通函数，默认绑定生效
// 严格模式下：TypeError: Cannot read properties of undefined (reading 'name')
```

**3. 显式绑定（Explicit Binding）：**

```js
function greet(greeting) {
  console.log(`${greeting}, ${this.name}`);
}

const user = { name: 'Charlie' };

greet.call(user, 'Hello');     // 'Hello, Charlie'
greet.apply(user, ['Hi']);     // 'Hi, Charlie'
greet.bind(user)('Hey');       // 'Hey, Charlie'
```

**4. new 绑定（Constructor Binding）：**

```js
function Person(name) {
  this.name = name; // this 指向新创建的对象
}

const p = new Person('Dave');
console.log(p.name); // 'Dave'

// 如果不用 new，直接调用函数，this 指向全局（严格模式下为 undefined）
// ⚠️ 以下污染行为仅在浏览器普通脚本且非严格模式下发生
// Person('Eve'); console.log(name); // 'Eve'（污染全局）
```


**初学者常见错误：**
- ❌ 以为 `this` 由函数定义位置决定——实际上由调用方式决定（箭头函数除外）
- ❌ 把对象方法作为回调传递时丢失 `this`：`btn.addEventListener('click', obj.method)` —— `method` 里的 `this` 变成按钮
- ✅ 修复方法：`btn.addEventListener('click', obj.method.bind(obj))` 或使用箭头函数
- ❌ 回调函数中用普通函数导致 `this` 指向 `window`（非严格模式），应使用箭头函数保持外层 `this`

#### 绑定优先级

**一句话理解：** 当多种 `this` 绑定规则同时出现时，优先级从高到低是：`new` 绑定 > 显式绑定（call/apply/bind）> 隐式绑定（obj.method()）> 默认绑定。

**优先级从高到低：`new` > `bind` > `call/apply` > 隐式 > 默认**

> 💡 `bind` 创建的硬绑定函数，后续再用 `call`/`apply` 无法改变其 `this`。

```js
function greet() {
  console.log(this.name);
}

const obj1 = { name: 'obj1' };
const obj2 = { name: 'obj2' };

// 1. bind 的优先级高于隐式
const boundGreet = greet.bind(obj1);
boundGreet.call(obj2); // 'obj1'（bind 绑定优先）

// 2. new 的优先级高于 bind
const Person = function(name) {
  this.name = name;
};
const BoundPerson = Person.bind({ name: 'bound' });
const p = new BoundPerson('new'); // 'new'（new 创建新对象，忽略 bind）
console.log(p.name); // 'new'
```

**优先级速查：**

```
new > bind/call/apply > obj.method() > func()
```

#### 箭头函数的 this（词法绑定）

**一句话理解：** 箭头函数没有自己的 `this`，它像"寄生虫"一样借用外层作用域的 `this`——这让它在回调函数中行为可预测，但也导致它不能作为构造函数使用。

箭头函数**没有自己的 `this`**，它沿用**定义时**的外层 `this`，不会因调用方式改变。

```js
const obj = {
  name: 'obj',
  // 普通函数：this 指向调用时的 obj
  greetNormal: function() {
    console.log(this.name);
  },
  // 箭头函数：this 沿用定义时的外层（这里是全局）
  greetArrow: () => {
    console.log(this.name);
  }
};

obj.greetNormal(); // 'obj'
obj.greetArrow();  // ''（浏览器中 window.name 默认为空字符串）

// 对比：setTimeout 中的行为差异
obj.greetNormal(); // 'obj'（立即调用）
setTimeout(obj.greetNormal, 100); // ''（this 丢失，回退到 window/window.name 默认为空字符串）
setTimeout(() => obj.greetNormal(), 100); // 'obj'（箭头函数内通过 obj. 显式调用）
```

**箭头函数不适用的场景：**

| 场景 | 不能用的原因 |
|------|-------------|
| 对象方法 | `this` 无法指向对象本身 |
| 构造函数 | 不能用 `new` 调用箭头函数 |
| 事件回调（需要 `this`） | 无法指向 DOM 元素 |

```js
// ❌ 错误：箭头函数不能用作构造函数
const Person = (name) => { this.name = name; };
new Person('a'); // TypeError: Person is not a constructor

// ❌ 错误：对象方法中的 this
const counter = {
  count: 0,
  inc: () => { this.count++; }, // this 继承外层作用域，不是 counter
};
counter.inc();
console.log(counter.count); // 0（未增加）
```


**初学者常见错误：**
- ❌ 试图用箭头函数作为构造函数：`new (() => {})()` 会报错，箭头函数没有 `prototype`，也不能被 `new`
- ❌ 在对象方法里用箭头函数定义方法，期望 `this` 指向对象——箭头函数的 `this` 指向对象定义时的上下文，通常是全局
- ✅ 对象方法应使用普通函数或方法简写，`this` 才能正确指向调用对象
- ❌ 在需要动态 `this` 的场景（如事件处理器、原型方法）使用箭头函数，导致 `this` 不符合预期

#### 常见陷阱与防御性写法

**一句话理解：** `this` 是 JavaScript 最容易踩坑的地方——回调中丢失上下文、隐式绑定被意外覆盖、类方法中 this 指向实例——学会用箭头函数、`bind` 或代理模式来防御。

**陷阱 1：setTimeout 中的 this 丢失**

```js
const user = {
  name: 'Alice',
  greet() {
    console.log(this.name);
  }
};

setTimeout(user.greet, 100); // 浏览器非严格模式：''（window.name 默认为空字符串）；严格模式：undefined
setTimeout(() => user.greet(), 100); // 'Alice'（箭头函数保持）

// 防御性写法 1：bind
setTimeout(user.greet.bind(user), 100); // 'Alice'

// 防御性写法 2：箭头函数包装
setTimeout(() => user.greet(), 100); // 'Alice'
```

**陷阱 2：隐式丢失**

```js
const obj = {
  name: 'Bob',
  greet() { console.log(this.name); }
};

const greet = obj.greet; // 引用赋值，丢失上下文
greet(); // undefined

// 防御：使用箭头函数或重新绑定
const greetBound = () => obj.greet();
greetBound(); // 'Bob'
```

**陷阱 3：链式调用中的 this**

```js
const calculator = {
  value: 0,
  add(n) {
    this.value += n;
    return this; // 返回 this 以支持链式调用
  },
  subtract(n) {
    this.value -= n;
    return this;
  }
};

calculator.add(5).subtract(2).add(3);
console.log(calculator.value); // 6
```

**this 指向快速判断法：**

```
看代码在哪里调用，不是看在哪里定义
1. 有 new 调用 → this 是 new 创建的新对象
2. 有 call/apply/bind → this 是指定的对象
3. 有 obj.method() → this 是 obj
4. 普通函数调用 → this 是 window/undefined（严格模式）
5. 箭头函数 → 继承外层作用域的 this
```

---

### 3.3 原型链与继承

#### 构造函数与 prototype

**一句话理解：** 构造函数是"工厂"，`prototype` 是工厂的"图纸库"——每次 `new` 一个实例，引擎就会按照图纸库里的模板来创建对象并建立继承关系。

每个函数都有一个 `prototype` 属性，它是一个对象，用来存放实例共享的方法和属性。

```js
function Animal(name) {
  this.name = name; // 实例属性
}

// prototype 上存放共享方法
Animal.prototype.speak = function() {
  return `${this.name} makes a sound`;
};

const dog = new Animal('Dog');
const cat = new Animal('Cat');

dog.speak(); // 'Dog makes a sound'
cat.speak(); // 'Cat makes a sound'

// dog 和 cat 共享 speak 方法，不会在每个实例上创建新函数
dog.speak === cat.speak; // true
```


**初学者常见错误：**
- ❌ 在构造函数中定义方法：`function Foo() { this.bar = function() {} }` —— 每个实例都会创建独立的方法函数，浪费内存
- ✅ 方法应定义在 `Foo.prototype` 上，所有实例共享同一个方法
- ❌ 重写 `prototype` 后忘记恢复 `constructor`：`Dog.prototype = { bark() {} }` 切断了 `constructor` 链接
- ✅ 重写时应设置 `Dog.prototype.constructor = Dog`

#### `__proto__` 与原型链查找

**一句话理解：** 每个对象都有一个"隐藏的电话簿"（`__proto__`），上面写着"如果我找不到某个属性，请打这个电话问我爸"。如果爸爸也找不到，就继续问爷爷，一直问到老祖宗 `Object.prototype`，这就是原型链。

**生活类比：**
- 原型链 = **家族技能传承**：你（实例对象）会自己学的技能就自己做（自身属性），不会的就去问爸爸（原型），爸爸不会的问爷爷（原型的原型），直到问到家族老祖宗（`Object.prototype`），老祖宗也不会就说 `undefined`
- `__proto__` = **族谱上的"父亲"一栏**：每个族谱记录（对象）都有一个"父亲"栏，指向上一代的族谱（原型对象）
- `prototype` = **家族的"祖传秘籍"**：专门放在一个房间里（构造函数.prototype），供所有后代查阅

`__proto__`（标准写法是 `Object.getPrototypeOf()`）是对象指向其原型的内部链接。当访问对象的属性或方法时，如果对象自身没有，引擎会沿着 `__proto__` 向上查找，形成**原型链**。

```js
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function() {
  return `${this.name} makes a sound`;
};

const dog = new Animal('Dog');

// 原型链结构：
// dog.__proto__ === Animal.prototype
// Animal.prototype.__proto__ === Object.prototype
// Object.prototype.__proto__ === null（终点）

// 属性查找路径：
dog.name           // 1. dog 自身有 → 直接返回
dog.speak          // 2. dog 没有，查 dog.__proto__（Animal.prototype）→ 找到
dog.toString       // 3. Animal.prototype 没有，查 Animal.prototype.__proto__（Object.prototype）→ 找到
dog.xxx            // 4. Object.prototype 也没有 → 返回 undefined（访问属性不存在不会报错）
```

**原型链图示：**

```
┌─────────────────────────────────────────────────────────────┐
│                        dog 实例                              │
│                      (name: 'Dog')                          │
└─────────────────────────────┬───────────────────────────────┘
                              │ __proto__
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Animal.prototype                          │
│                   (constructor: Animal)                     │
│                        (speak: fn)                          │
└─────────────────────────────┬───────────────────────────────┘
                              │ __proto__
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Object.prototype                        │
│                    (constructor: Object)                   │
│                     (hasOwnProperty, toString...)            │
└─────────────────────────────────────────────────────────────┘
```


**初学者常见错误：**
- ❌ 用 `obj.__proto__` 判断原型链——应使用标准方法 `Object.getPrototypeOf(obj)`
- ❌ 在实例上查找 `constructor` 判断类型——`constructor` 可以被重写，不可靠，应使用 `instanceof`
- ❌ 修改已创建实例的 `__proto__` —— 性能极差且破坏引擎优化，应重新设计继承结构
- ❌ 原型链查找到 `Object.prototype` 还继续向上——`Object.prototype.__proto__` 是 `null`，这就是原型链的终点

#### 继承方式演变（原型式 / 寄生组合式）

**一句话理解：** JavaScript 的继承从最早的"借来用用"（原型链继承），发展到"先复制再优化"（寄生组合式），最终演进为 ES6 Class 语法糖——但底层始终是原型链。

**1. 原型链继承（最原始）**

```js
function Parent() {
  this.parentName = 'Parent';
}
Parent.prototype.sayParent = function() { return this.parentName; };

function Child() {
  this.childName = 'Child';
}

// 将 Child 的原型指向 Parent 实例（建立原型链）
Child.prototype = new Parent();
Child.prototype.constructor = Child; // 修正 constructor

const child = new Child();
child.sayParent(); // 'Parent'（沿原型链找到）
```

缺点：Parent 实例属性变成 Child 原型属性，共享导致副作用。

**2. 借用构造函数（Constructor Stealing）**

```js
function Parent(name) {
  this.name = name;
}

function Child(name, age) {
  Parent.call(this, name); // 借用 Parent，继承实例属性
  this.age = age;
}

const child = new Child('Alice', 10);
child.name; // 'Alice'
child.age;  // 10
```

缺点：方法在构造函数内定义，无法共享，内存浪费。

**3. 组合继承（最常用）**

结合原型链（继承方法）和构造函数（继承实例属性）：

```js
function Parent(name) {
  this.name = name;
}
Parent.prototype.sayName = function() { return this.name; };

function Child(name, age) {
  Parent.call(this, name); // 继承实例属性
  this.age = age;
}

Child.prototype = new Parent(); // 继承原型方法
Child.prototype.constructor = Child;
Child.prototype.sayAge = function() { return this.age; };

const child = new Child('Bob', 20);
child.sayName(); // 'Bob'
child.sayAge();  // 20
```

缺点：Parent 被调用了两次（`call` 一次，`new` 一次），有冗余属性。

**4. 寄生组合式继承（最优解）**

用 `Object.create()` 替代 `new Parent()`，避免调用 Parent 构造函数：

```js
function Parent(name) {
  this.name = name;
}
Parent.prototype.sayName = function() { return this.name; };

function Child(name, age) {
  Parent.call(this, name); // 只调用一次
  this.age = age;
}

// 关键：用 create 建立原型链，不调用 Parent 构造函数
Child.prototype = Object.create(Parent.prototype);
Child.prototype.constructor = Child;
Child.prototype.sayAge = function() { return this.age; };

const child = new Child('Charlie', 15);
child.sayName(); // 'Charlie'
child.sayAge();  // 15
```


**初学者常见错误：**
- ❌ 直接 `Child.prototype = Parent.prototype` —— 子类和父类共享同一个原型对象，修改子类会影响父类
- ✅ 正确做法：`Child.prototype = Object.create(Parent.prototype)` 创建独立的原型对象
- ❌ 忘记调用父类构造函数：`function Child() { Parent.call(this); }` 缺失会导致父类属性未初始化
- ❌ ES6 `class` 中在子类构造函数里忘记先调用 `super()` —— 会报错，且 `this` 在 `super()` 之前不可用

#### ES6 Class 语法糖与私有字段（#）

**一句话理解：** ES6 `class` 只是原型继承的"新衣服"，让代码看起来像传统的面向对象语言；而 `#private` 私有字段则是真正的语法级封装，子类也无法访问。

ES6 的 `class` 是原型继承的语法糖，本质上还是基于原型链。

**class 基本语法：**

```js
class Animal {
  constructor(name) {
    this.name = name; // 实例属性
  }

  // 原型方法（所有实例共享）
  speak() {
    return `${this.name} makes a sound`;
  }

  // 静态方法（类本身的方法，实例无法访问）
  static create(name) {
    return new Animal(name);
  }
}

const dog = new Animal('Dog');
dog.speak(); // 'Dog makes a sound'
Animal.create('Cat'); // new Animal('Cat')
```

**extends 与 super：**

```js
class Dog extends Animal {
  constructor(name, breed) {
    super(name); // 调用父类构造函数，必须先调用
    this.breed = breed;
  }

  speak() {
    return `${this.name} barks`; // 重写父类方法
  }

  static create(name, breed) {
    return new Dog(name, breed);
  }
}

const dog = new Dog('Buddy', 'Golden Retriever');
dog.speak(); // 'Buddy barks'
dog instanceof Animal; // true（instanceof 仍然有效）
```

> **一句话理解：** 用 `#` 开头的变量只能在类内部访问，是真正的"私有"。

ES2022 引入私有字段语法 `#`，解决了传统 `_` 前缀只是约定、仍可被外部访问的问题：

```js
class Counter {
  #count = 0;              // 私有字段，外部无法访问
  increment() {
    this.#count++;
    return this.#count;
  }
}
const c = new Counter();
c.increment();             // 1
// c.#count;               // ❌ SyntaxError：私有字段只能在类内部访问
```

> 💡 **深入细节：** 私有方法、静态私有字段、以及 `#field in obj` 检查语法，详见第 6 章「类私有字段与方法」小节。

**class 与原型继承的本质对比：**

```js
// class 写法
class Animal {
  speak() { return 'sound'; }
}
class Dog extends Animal {}

// 原型写法（等价）
function AnimalProto() {}
AnimalProto.prototype.speak = function() { return 'sound'; };

function DogProto() {}
DogProto.prototype = Object.create(AnimalProto.prototype);
DogProto.prototype.constructor = DogProto;
```

> 💡 **深入学习：** 上面的对比只是冰山一角。原型链的查找机制、`instanceof` 的原理、寄生组合式继承的完整实现，以及「为什么 class 是语法糖」的底层证据，详见第 3 章「原型链与继承」。

---

### 3.4 立即执行函数表达式（IIFE）

#### 语法形式与执行原理

**一句话理解：** IIFE（立即执行函数表达式）就是"定义完马上调用自己的函数"，它的核心价值在于创建独立的作用域，避免变量污染全局命名空间。

**IIFE（Immediately Invoked Function Expression）**：定义后立即执行的函数，常用于创建独立作用域。

```js
// 标准写法（推荐）
(function() {
  const privateVar = '我只在这个函数内有效';
  console.log('IIFE 执行');
})();

// 箭头函数版本
(() => {
  console.log('Arrow IIFE');
})();

// 带返回值
const result = (function() {
  const x = 10;
  return x * 2;
})();
console.log(result); // 20

// 带参数
(function(name) {
  console.log(`Hello, ${name}`);
})('World');
```

**执行原理：**

```
(function(){ ... })()
    ↓
1. (function(){ ... }) — 创建函数表达式
2. () — 立即调用
3. 函数执行完毕后，内部变量被销毁（如果没有闭包引用）
```

**与普通函数的区别：**

```js
// 普通函数：定义后不会自动执行
function fn() { console.log('fn'); }
fn(); // 需要手动调用

// IIFE：定义后立即执行，执行完毕后变量销毁
(function() { console.log('IIFE'); })(); // 自动执行
```

#### 应用场景（作用域隔离 / 模块模式）

**一句话理解：** IIFE 的经典应用场景是"模块模式"——通过闭包暴露公共 API，同时隐藏内部实现细节，这是 ES6 模块系统出现前最常用的模块化方案。

**1. 作用域隔离（避免全局污染）：**

```js
// 传统：变量提升可能污染全局
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 输出 3, 3, 3
}

// IIFE 隔离：为每次迭代创建独立作用域
for (var i = 0; i < 3; i++) {
  (function(j) {
    setTimeout(() => console.log(j), 100); // 输出 0, 1, 2
  })(i);
}

// 现代替代：用 let 替代 IIFE（let 天然块级作用域）
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 输出 0, 1, 2
}
```

**2. 模块模式（Module Pattern）：**

利用 IIFE 创建私有变量和公共 API：

```js
const Calculator = (function() {
  // 私有变量（外部无法直接访问）
  let result = 0;

  // 私有方法
  function validate(n) {
    if (typeof n !== 'number') {
      throw new Error('Must be a number');
    }
  }

  // 公共 API
  return {
    add(n) {
      validate(n);
      result += n;
      return this; // 支持链式调用
    },
    subtract(n) {
      validate(n);
      result -= n;
      return this;
    },
    value() {
      return result;
    }
  };
})();

Calculator.add(5).subtract(2).add(3);
Calculator.value(); // 6
Calculator.result;  // undefined（私有，访问不到）
```

**3. 块级作用域替代（ES6 前）：**

```js
// 场景：需要 var 在代码块内独立
if (true) {
  var tmp = 'var 是函数作用域，整个函数可见';
}
console.log(tmp); // 能访问到

// IIFE 模拟 let 的块级作用域
if (true) {
  (function() {
    var tmp = 'tmp 只在这个 IIFE 内有效';
  })();
}
console.log(tmp); // ReferenceError
```

**4. 常见错误避免：**

```js
// ❌ 错误：IIFE 前面缺少分号，会被解析为函数调用
const num = 1
(function() {})() // TypeError: 1 is not a function（被解析为调用数字 1）

// ✅ 正确：加分号分隔
const a = 1;
(function() {})();

// ✅ 或者用 !、+ 等运算符开头
const b = 1;
!function() {}();
```

---

### 🛠️ 实操：核心机制手写实现

> **难度提示：** ⭐⭐⭐⭐⭐ 本节为**面试进阶内容**，涉及 JavaScript 底层实现原理。初学者如感到困难，可暂时跳过，待学完第 4~6 章后再回头阅读——手写实现的核心价值在于"验证理解"，而非"必须掌握"。

#### 手写 call / apply / bind（理解 this 绑定原理）

**一句话理解：** 手写 `call`/`apply`/`bind` 不仅能应对面试，更能让你深入理解 `this` 绑定的本质——核心就是在指定对象上临时调用函数。

**核心思路：**
- `call/apply`：将函数作为指定对象的方法调用，指定 `this` 为该对象
- `bind`：返回一个新函数，`this` 被永久绑定

**实现要点：**
- `call`：参数逐个传递；`apply`：参数以数组传递
- 利用 `obj.fn = this` 的隐式绑定特性
- 记得用 `delete` 删除临时添加的属性

```js
// 手写 call
Function.prototype.myCall = function(context, ...args) {
  // ⚠️ 教学简化：严格模式下 this 不做包装（call(null) 时 this 为 null）
  const ctx = context == null ? globalThis : Object(context);
  const fn = Symbol('fn'); // 避免属性名冲突
  ctx[fn] = this; // 将函数挂到 context 上
  const result = ctx[fn](...args); // 调用，this 指向 context
  delete ctx[fn]; // 清理
  return result;
};

// 手写 apply
Function.prototype.myApply = function(context, args) {
  // ⚠️ 教学简化：严格模式下 this 不做包装（call(null) 时 this 为 null）
  const ctx = context == null ? globalThis : Object(context);
  const fn = Symbol('fn');
  ctx[fn] = this;
  // 原生 apply 支持 args 为 null/undefined
  const applyArgs = args == null ? [] : args;
  const result = ctx[fn](...applyArgs);
  delete ctx[fn];
  return result;
};

// 手写 bind
Function.prototype.myBind = function(context, ...args) {
  const originalFn = this;
  function boundFn(...args2) {
    // 用 new 调用时，this 应该是被 new 创建的实例，不受 context 影响
    if (this instanceof boundFn) {
      return originalFn.apply(this, [...args, ...args2]);
    }
    return originalFn.apply(context, [...args, ...args2]);
  }
  // ⚠️ 教学简化：原生 bind 返回的函数没有 prototype 属性
  // 这里为了支持 new 调用时的原型链继承做了简化处理
  if (originalFn.prototype) {
    boundFn.prototype = Object.create(originalFn.prototype);
  }
  return boundFn;
};
```

#### 手写 new 操作符（理解实例创建与原型关联）

**一句话理解：** `new` 的本质是四步操作：创建空对象、链接原型、绑定 `this` 执行构造函数、返回对象——手写一遍就能彻底理解实例化的完整流程。

**核心思路：** `new` 做了四件事：创建对象、设置原型、执行构造函数、返回对象。

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ 1. 创建空对象 │ ──▶ │ 2. 链接原型  │ ──▶ │ 3. 绑定 this │ ──▶ │ 4. 返回对象  │
│   {}        │     │ 设置 __proto__│     │ 执行构造函数  │     │ 优先返回构造 │
│             │     │ 指向 prototype│     │             │     │ 函数的返回值 │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

```js
function myNew(constructor, ...args) {
  // 1. 创建新对象，同时设置原型链（比先创建再 setPrototypeOf 更高效）
  const instance = Object.create(constructor.prototype);

  // 3. 执行构造函数，this 指向新对象
  const result = constructor.apply(instance, args);

  // 4. 返回（如果构造函数返回对象，则用返回值；否则用新对象）
  return (typeof result === 'object' && result !== null) || typeof result === 'function' ? result : instance;
}

function Person(name) {
  this.name = name;
}
Person.prototype.greet = function() { return `I am ${this.name}`; };

const p = myNew(Person, 'Alice');
p.name;     // 'Alice'
p.greet();  // 'I am Alice'
p instanceof Person; // true（原型链关联）
```

#### 手写一个基于原型的继承体系并对比 Class 写法

**核心思路：** 对比 ES5 原型继承和 ES6 Class 继承，理解它们本质相同。

```js
// === ES5 原型继承 ===
function AnimalES5(name) {
  this.name = name;
}
AnimalES5.prototype.speak = function() {
  return `${this.name} makes a sound`;
};

function DogES5(name, breed) {
  AnimalES5.call(this, name); // 借用构造函数继承实例属性
  this.breed = breed;
}

// 原型链继承（关键）
DogES5.prototype = Object.create(AnimalES5.prototype);
DogES5.prototype.constructor = DogES5;
DogES5.prototype.speak = function() { // 重写方法
  return `${this.name} barks`;
};

// === ES6 Class 继承（等价）===
class Animal {
  constructor(name) { this.name = name; }
  speak() { return `${this.name} makes a sound`; }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name); // 等价于 Animal.call(this, name)
    this.breed = breed;
  }
  speak() { return `${this.name} barks`; }
}

// 验证：两者行为完全相同
const dog1 = new Dog('Buddy', 'Golden');
dog1.speak();            // 'Buddy barks'
dog1 instanceof Animal;  // true
dog1 instanceof Dog;     // true
```

#### 实现一个简单的模块加载器（模拟 CommonJS require）

**核心思路：** 用 IIFE 隔离作用域，用闭包存储模块缓存，模拟 `require` 的加载逻辑。

```js
const MyModule = (function() {
  const modules = {}; // 模块缓存

  function require(moduleName) {
    if (modules[moduleName]) {
      return modules[moduleName].exports;
    }

    // 加载模块（模拟）
    const module = { exports: {} };
    modules[moduleName] = module;

    // 执行模块代码（假定的模块定义）
    // 实际中需要从文件系统或网络加载
    if (moduleName === 'math') {
      module.exports = {
        add: (a, b) => a + b,
        multiply: (a, b) => a * b
      };
    } else if (moduleName === 'counter') {
      let count = 0;
      module.exports = {
        increment: () => ++count,
        getCount: () => count
      };
    }

    return module.exports;
  }

  return { require };
})();

// 使用
const math = MyModule.require('math');
console.log(math.add(2, 3));     // 5
console.log(math.multiply(4, 5)); // 20
```

> **本章小结：** 我们学习了执行上下文、作用域链、闭包、this 绑定的四种规则、原型链与继承的完整机制，并手写实现了 `call`/`apply`/`bind`、`new` 等核心 API。
>
> **下一章预告：** 掌握了 JavaScript 的核心运行机制后，我们将面对一个现实问题：如何处理耗时的异步任务？下一章将学习事件循环、Promise、async/await 以及异步编程的最佳实践。
