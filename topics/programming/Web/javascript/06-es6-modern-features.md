---
title: "JavaScript 核心知识体系 · 六、ES6+ 现代特性"
tags:
  - programming
  - javascript
created: 2026-09-10
updated: 2026-10-01
---

# 六、ES6+ 现代特性

> 📚 本文是 [[topics/programming/Web/javascript|JavaScript 核心知识体系]] 的第 6 / 8 章。 上一章：[[topics/programming/Web/javascript/05-dom-and-browser-api|五、DOM 操作与浏览器 API]] · 下一章：[[topics/programming/Web/javascript/07-error-handling-and-debugging|七、错误处理与调试]]


> **本章定位：** 现代 JavaScript（ES2015 及以后版本）带来的语法革新。这些特性让代码更简洁、更易读、更易维护，也是目前主流开发的标准写法。
>
> **学习路线：** 语法增强（解构、模板字符串、展开运算符）→ 迭代协议（for...of、生成器）→ 模块化（ES Modules）→ 后续新特性（私有字段、动态导入、不变性方法）→ 现代化重构实战
>
> **建议：** 如果你之前学过其他编程语言，ES6+ 的很多特性会让你感到亲切（如 Python 的解包、Java 的类私有字段）。可以对比学习，加深记忆。

### 6.1 语法增强

#### 解构赋值（对象 / 数组 / 嵌套 / 重命名）

解构赋值允许从数组或对象中提取值，直接赋给变量，使代码更简洁。

**解构赋值可视化图解：**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           解构赋值直观理解                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   【对象解构】—— 按键名匹配                                                │
│                                                                             │
│   const user = { name: 'Alice', age: 25, city: 'Beijing' };               │
│                                                                             │
│   const { name, age } = user;                                              │
│              │      │                                                      │
│              ▼      ▼                                                      │
│         { name: 'Alice', age: 25 }   →   name = 'Alice', age = 25        │
│                                                                             │
│   【数组解构】—— 按位置匹配                                                │
│                                                                             │
│   const arr = [10, 20, 30, 40, 50];                                      │
│                                                                             │
│   const [a, b, ...rest] = arr;                                            │
│              │   │   │                                                     │
│              ▼   ▼   ▼                                                     │
│         [10, 20, [30, 40, 50]]   →   a=10, b=20, rest=[30,40,50]       │
│                                                                             │
│   【跳过元素】                                                             │
│                                                                             │
│   const [first, , third] = arr;                                           │
│              │       │                                                     │
│              ▼       ▼                                                     │
│         [10, 20, 30]   →   first=10, third=30（第二个元素被跳过）        │
│                                                                             │
│   【重命名】                                                              │
│                                                                             │
│   const { name: userName, age: userAge } = user;                          │
│                  │              │                                        │
│                  ▼              ▼                                        │
│         'Alice' → userName,   25 → userAge                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**对象解构：**
```js
const user = { name: 'Alice', age: 25, city: 'Beijing' };

// 基础解构
const { name, age } = user;

// 重命名
const { name: userName, age: userAge } = user;

// 默认值（当属性为 undefined 时生效）
const { gender = 'female' } = user;

// 剩余属性（收集到对象中）
const { name: n, ...rest } = user;
console.log(rest); // { age: 25, city: 'Beijing' }
```

**数组解构：**
```js
const arr = [10, 20, 30];

const [a, b] = arr;        // a=10, b=20
const [first, , third] = arr; // 跳过元素
const [x, ...others] = arr;   // others=[20,30]

// 默认值
const [p = 1, q = 2] = [100]; // p=100, q=2

// 交换变量
let m = 1, n = 2;
[m, n] = [n, m];
```

**嵌套解构：**
```js
const data = {
  user: {
    profile: { email: 'alice@example.com' },
    tags: ['admin', 'editor']
  }
};

const { user: { profile: { email }, tags: [role] } } = data;
console.log(email, role); // alice@example.com admin
```

**关键细节：**
- 解构时如果变量先声明，赋值需用括号包裹：`({ a, b }) = obj` 会报错，应写为 `({ a, b } = obj)`
- `null` 和 `undefined` 无法解构，会抛出 TypeError
- 默认值只对 `undefined` 生效，`null` 不会触发默认值

---

#### 模板字符串与标签模板

**模板字符串（Template Literals）：**
```js
const name = 'World';

// 基本插值
const greeting = `Hello, ${name}!`;

// 多行文本（保留换行和缩进）
const html = `
  <div>
    <h1>${name}</h1>
  </div>
`;

// 表达式插值
const sum = `1 + 2 = ${1 + 2}`;

// 嵌套模板
const items = ['a', 'b'];
const list = `<ul>${items.map(i => `<li>${i}</li>`).join('')}</ul>`;
```

**标签模板（Tagged Templates）：**
```js
function highlight(strings, ...values) {
  return strings.reduce((result, str, i) => {
    // ⚠️ 用三元判断会漏掉 0/false/'' 等合法 falsy 值
    const val = i < values.length ? `[${values[i]}]` : '';
    return result + str + val;
  }, '');
}

const name = 'Alice';
const age = 25;
highlight`Name: ${name}, Age: ${age}`;
// "Name: [Alice], Age: [25]"
```

**应用场景：**
- **styled-components / CSS-in-JS**：`css\`color: ${props.color}\``
- **i18n 国际化**：`i18n\`Hello ${name}\``
- **SQL 查询防注入**：自动转义参数

**关键细节：**
- `strings` 是模板中纯字符串部分的数组，其长度始终比 `values` 多 1
- 标签函数接收的第一个参数是 `strings`（含 `raw` 属性，可获取原始转义字符）

---

#### 展开运算符与剩余参数

**展开运算符（Spread Operator）...**

数组展开：
```js
const arr1 = [1, 2];
const arr2 = [3, 4];
const merged = [...arr1, ...arr2]; // [1, 2, 3, 4]

const copy = [...arr1]; // 浅拷贝
const strChars = [...'hello']; // ['h','e','l','l','o']

// 与解构结合
const [head, ...tail] = [1, 2, 3, 4]; // head=1, tail=[2,3,4]
```

对象展开：
```js
const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 }; // { a: 1, b: 2, c: 3 }

// 对象浅拷贝与合并
const defaults = { host: 'localhost', port: 3000 };
const config = { ...defaults, port: 8080 }; // 后面的属性覆盖前面

// 注意：对象展开是浅拷贝
const nested = { data: { value: 1 } };
const clone = { ...nested };
clone.data.value = 2;
console.log(nested.data.value); // 2（共享引用）
```

**剩余参数（Rest Parameters）：**
```js
// 收集函数剩余参数
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
sum(1, 2, 3, 4); // 10

// 与命名参数结合
function greet(greeting, ...names) {
  return `${greeting}, ${names.join(' and ')}!`;
}
greet('Hello', 'Alice', 'Bob'); // "Hello, Alice and Bob!"

// 与解构结合
const { id, ...metadata } = { id: 1, name: 'A', tag: 'x' };
```

**关键细节：**
- 剩余参数必须是函数参数的最后一个，否则会报错
- 展开运算符与剩余参数语法相同（`...`），但使用位置不同：展开在调用/字面量处，剩余在声明/解构处
- 类数组对象（如 `arguments`）不能直接用数组方法，但 `[...arguments]` 可转为真数组

---

### 6.2 迭代协议

#### 可迭代协议与迭代器协议

**迭代协议解决了什么问题？**

在 ES6 之前，JavaScript 没有统一的遍历接口。数组有 `.forEach()`，字符串有 `.charAt()`，对象只能用 `for...in` —— 每种数据类型都有自己的遍历方式，互不兼容。迭代协议通过定义**统一的标准接口**，让任何数据结构只要实现了这个接口，就能用同一种方式遍历。

```
┌──────────────────────────────────────────────────────────────────────┐
│                        迭代协议的核心思想                              │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   可迭代对象 (Iterable)          迭代器 (Iterator)         消费者      │
│                                                                      │
│   ┌─────────┐   [Symbol.iterator]()   ┌─────────┐   next()           │
│   │  Array  │ ──────────────────────▶ │         │ ──────────▶        │
│   │  String │ ──────────────────────▶ │ Iterator│ ──────────▶        │
│   │  Map    │ ──────────────────────▶ │ (协议)   │ ──────────▶ for...of│
│   │  Set    │ ──────────────────────▶ │         │ ──────────▶ 展开运算符│
│   └─────────┘                         └─────────┘ ──────────▶ Array.from│
│       ▲                                    │                         │
│       └────────────────────────────────────┘                         │
│                                                                      │
│   可迭代协议：对象必须实现 [Symbol.iterator]() 方法                     │
│   迭代器协议：返回的对象必须有 next() 方法，产出 { value, done }       │
└──────────────────────────────────────────────────────────────────────┘
```

---

##### 两种协议的定义

**1. 可迭代协议（Iterable Protocol）**

```js
// 一个对象成为"可迭代对象"的条件：
// 必须有一个 [Symbol.iterator]() 方法，返回一个迭代器

const iterable = {
  [Symbol.iterator]() {
    // 返回迭代器
    return iteratorObject;
  }
};
```

**2. 迭代器协议（Iterator Protocol）**

```js
// 迭代器必须实现 next() 方法：
const iterator = {
  next() {
    // 返回格式必须是这样的：
    return { value: any, done: boolean };
  }
};
```

| 协议 | 要求 | 作用 |
|------|------|------|
| **可迭代协议** | 实现 `[Symbol.iterator]()` | 声明"这个对象可以被迭代" |
| **迭代器协议** | 实现 `next()` 方法 | 规定"每次迭代如何获取下一个值" |

---

##### 迭代执行流程图

```
┌─────────────────────────────────────────────────────────────────┐
│                     for...of 执行流程                            │
├─────────────────────────────────────────────────────────────────┤

   for (const item of iterable) { ... }
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  1. 调用 iterable[Symbol.iterator]()，获取迭代器                  │
│     iterator = iterable[Symbol.iterator]();                     │
└─────────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. 循环调用 iterator.next()                                    │
│                                                                 │
│     ┌─────────────────────────────────────────────────────┐     │
│     │  result = iterator.next();                          │     │
│     │                                                     │     │
│     │  if (result.done === true) {                        │     │
│     │      结束迭代，退出循环                              │     │
│     │  } else {                                           │     │
│     │      item = result.value;                           │     │
│     │      执行循环体                                     │     │
│     │      回到第 2 步，继续调用 next()                    │     │
│     │  }                                                  │     │
│     └─────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
```

---

##### 手动实现一个完整迭代器

```js
// 创建一个可迭代的计数器
function createCounter(start = 0, end = 5) {
  // Step 1: 创建可迭代对象，实现 [Symbol.iterator]
  return {
    [Symbol.iterator]() {
      // Step 2: 返回迭代器，初始化内部状态
      let current = start;

      // Step 3: 迭代器必须实现 next() 方法
      return {
        next() {
          // Step 4: 判断是否还有元素
          if (current <= end) {
            // 还有元素，返回值并更新状态
            return {
              value: current++,  // 返回当前值，然后递增
              done: false        // 未完成，还有下一个
            };
          } else {
            // 没有更多元素
            return {
              done: true         // 迭代完成
              // value 可省略或设为 undefined
            };
          }
        }
      };
    }
  };
}

// 使用 for...of 遍历
for (const num of createCounter(1, 3)) {
  console.log(num);
}
// 输出：1 → 2 → 3

// 使用展开运算符（因为数组本身实现了迭代协议）
console.log([...createCounter(10, 12)]); // [10, 11, 12]

// 手动迭代过程
const iterator = createCounter(1, 3)[Symbol.iterator]();
console.log(iterator.next()); // { value: 1, done: false }
console.log(iterator.next()); // { value: 2, done: false }
console.log(iterator.next()); // { value: 3, done: false }
console.log(iterator.next()); // { done: true }
```

---

##### 内置可迭代对象一览

```js
// 数组
for (const item of ['a', 'b']) { }  // ✅

// 字符串
for (const char of 'hi') { }         // ✅ 正确处理 Unicode

// Map
for (const [key, value] of new Map([['a', 1]])) { }  // ✅

// Set
for (const item of new Set([1, 2])) { }  // ✅

// arguments（函数参数类数组）
function args() {
  for (const arg of arguments) { }      // ✅
}

// 生成器
function* gen() { yield 1; }
for (const item of gen()) { }            // ✅

// 普通对象 — ❌ 不能直接迭代
const obj = { a: 1, b: 2 };
// for (const item of obj) { }  // TypeError!

// 如需迭代对象属性，使用 Object.keys/values/entries
for (const key of Object.keys(obj)) { }    // ✅
for (const value of Object.values(obj)) { } // ✅
for (const [key, value] of Object.entries(obj)) { } // ✅
```

---

##### 自定义可迭代对象

让普通对象支持 `for...of` 和展开运算符：

```js
// 创建一个"可迭代的范围对象"
const range = {
  start: 1,
  end: 5,

  // 实现可迭代协议
  [Symbol.iterator]() {
    let current = this.start;
    const self = this; // 保存引用

    return {
      next() {
        if (current <= self.end) {
          return { value: current++, done: false };
        }
        return { done: true };
      }
    };
  }
};

// 现在可以这样使用：
[...range];                  // [1, 2, 3, 4, 5]
Array.from(range);           // [1, 2, 3, 4, 5]
for (const n of range) {
  console.log(n);            // 1, 2, 3, 4, 5
}

// 解构赋值
const [first, second, ...rest] = range; // first=1, second=2, rest=[3, 4, 5]
```

---

#### for...of 与生成器函数（function* / yield）

##### 为什么需要生成器？

迭代器的手动实现比较繁琐——需要创建可迭代对象、返回迭代器、编写 `next()` 方法。生成器函数提供了一种更简洁的方式来创建迭代器：

```js
// ❌ 手动实现迭代器：需要手动管理状态
const manualIterator = {
  [Symbol.iterator]() {
    let current = 0;
    return {
      next() {
        if (current < 3) return { value: ++current, done: false };
        return { done: true };
      }
    };
  }
};

// ✅ 生成器实现：自动帮你管理状态，自动实现迭代器协议
function* generatorIterator() {
  yield 1;  // 暂停，返回 1
  yield 2;  // 暂停，返回 2
  yield 3;  // 暂停，返回 3
  return;   // 完成
}
```

---

##### 生成器函数执行流程

```
┌─────────────────────────────────────────────────────────────────┐
│                      生成器函数执行流程                           │
└─────────────────────────────────────────────────────────────────┘

   const gen = generatorFn();
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  1. 创建生成器对象（gen），函数体不执行                             │
│                                                                 │
│     gen ───▶ { [[GeneratorStatus]]: 'suspended', ... }          │
└─────────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. 第一次调用 gen.next()                                        │
│                                                                 │
│     gen.next()                                                  │
│         │                                                       │
│         ▼                                                       │
│     函数体开始执行 → 遇到第一个 yield → 暂停 → 返回 { value, done }│
│                                                                 │
│     ┌─────────────────────────────────────────────────────┐     │
│     │  function* gen() {                                  │     │
│     │      console.log('A');    ──▶  输出 'A'             │     │
│     │      yield 1;              ──▶  暂停，返回 { value: 1, done: false } │
│     │      console.log('B');      ←── 下次 next() 时执行   │     │
│     │      yield 2;              ──▶  暂停，返回 { value: 2, done: false } │
│     │      console.log('C');      ←── 下次 next() 时执行   │     │
│     │      return 'done';        ──▶  完成，返回 { value: 'done', done: true } │
│     │  }                                                   │     │
│     └─────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
```

---

##### 生成器方法详解

```js
function* simpleGen() {
  yield 1;
  yield 2;
  yield 3;
  return 'finished';
}

const gen = simpleGen();

// next() — 恢复执行到下一个 yield
console.log(gen.next()); // { value: 1, done: false }
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: 3, done: false }
console.log(gen.next()); // { value: 'finished', done: true }

// return() — 提前终止生成器
const gen2 = simpleGen();
gen2.next();              // { value: 1, done: false }
gen2.return('early');     // { value: 'early', done: true }
// 后续 next() 一直返回 { done: true }

// throw() — 向生成器内部抛入错误
const gen3 = simpleGen();
gen3.next();
try {
  gen3.throw(new Error('Oops!'));
} catch (e) {
  console.log('Caught:', e.message); // 'Oops!'
}
```

---

##### next() 参数的双向通信

`yield` 可以接收外部传入的值，这是生成器强大的**双向通信**能力：

```
┌─────────────────────────────────────────────────────────────────┐
│                     yield 的双向通信机制                          │
└─────────────────────────────────────────────────────────────────┘

   function* echo() {
     const msg = yield 'ready';  // 暂停，返回 'ready'，等待外部传值
     yield msg;                  // 用接收到的值继续执行
   }

   const gen = echo();

   // 第一次 next()：启动生成器，执行到 yield，返回右侧表达式值
   const result1 = gen.next();
   console.log(result1); // { value: 'ready', done: false }
                         //           ↑
                         //     yield 'ready' 的返回值

   // 第二次 next('hello')：传入 'hello'，yield 表达式变为 'hello'
   const result2 = gen.next('hello');
   console.log(result2); // { value: 'hello', done: false }
                         //           ↑
                         //     const msg = 'hello' 后的 yield msg 返回值
```

**实际应用场景：实现生产者-消费者模式**

```js
function* consumerProducer() {
  // 等待外部提供数据
  const data = yield 'WAITING_FOR_DATA';

  // 处理数据
  const processed = data.map(x => x * 2);
  yield processed; // 返回处理结果
}

// 使用
const cp = consumerProducer();
console.log(cp.next().value);                    // 'WAITING_FOR_DATA'

// 传入数据，生成器收到 data = [1, 2, 3]
const result = cp.next([1, 2, 3]);
console.log(result.value);                       // [2, 4, 6]
```

---

##### yield* 委托迭代

`yield*` 将迭代委托给另一个可迭代对象：

```js
function* genA() {
  yield 1;
  yield 2;
}

function* genB() {
  yield 'start';
  yield* genA();  // 委托给 genA，完全展开其所有值
  yield 'end';
}

// 在仅使用 next() 消费时，效果等价于：
function* genB_equivalent() {
  yield 'start';
  yield 1;         // genA 的值
  yield 2;         // genA 的值
  yield 'end';
}
// ℹ️ 注意：yield* 还会传递 .return() 和 .throw() 调用，两者并非完全等价

console.log([...genB()]); // ['start', 1, 2, 'end']
```

---

##### 生成器与惰性计算

生成器的核心优势：**惰性计算**（Lazy Evaluation）——只在需要时计算下一个值：

```js
// ✅ 生成器：惰性，按需生成
function* fibonacci() {
  let [a, b] = [0, 1];
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

const fib = fibonacci();
fib.next().value; // 0  — 只计算到 0
fib.next().value; // 1  — 只计算到 1
fib.next().value; // 1  — 只计算到 1
// ... 每次只计算一个值，内存高效

// ❌ 数组：立即计算全部
const fibArray = [0, 1, 1, 2, 3, 5, ...]; // 要算到哪？无法预知
```

**无限数据流的处理：**

```js
// 生成自然数序列（无限）
function* naturalNumbers() {
  let n = 1;
  while (true) {
    yield n++;
  }
}

// 只取前 10 个（正确的惰性方式：不需要展开全部）
function* take(iterable, n) {
  let count = 0;
  for (const item of iterable) {
    if (count++ < n) yield item;
    else return;
  }
}

const first10 = [...take(naturalNumbers(), 10)];
console.log(first10); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// 取偶数（惰性过滤）
function* filter(iterable, predicate) {
  for (const item of iterable) {
    if (predicate(item)) {
      yield item;
    }
  }
}

const evenNums = filter(naturalNumbers(), n => n % 2 === 0);
[...take(evenNums, 5)]; // [2, 4, 6, 8, 10]
```

---

##### 关键细节汇总

| 特性 | 说明 |
|------|------|
| **执行时机** | 调用 `.next()` 才执行，惰性求值 |
| **状态保存** | 每次 `.next()` 后暂停，状态保留 |
| **返回值** | `.next()` 返回 `{ value, done }` |
| **传值机制** | `.next(value)` 的参数作为上一个 `yield` 的值 |
| **终止方法** | `.return()` 提前结束，`.throw()` 抛入错误 |
| **可迭代** | 生成器对象本身是迭代器，也是可迭代对象 |

```js
// 生成器同时是迭代器，也是可迭代对象
function* gen() { yield 1; }

const g = gen();

// ✅ 生成器有 next() 方法
g.next(); // { value: 1, done: false } —— 已消耗第一个值！

// ✅ 生成器实现了 [Symbol.iterator]()
g[Symbol.iterator]() === g; // true！所以可以用 for...of
// ⚠️ 注意：g.next() 已消耗了第一个值，for...of 从第二个值开始
for (const item of g) { console.log(item); } // 这里不会输出 1
```

### 6.3 模块化

#### CommonJS 与 ES Modules 对比

| 特性 | CommonJS (CJS) | ES Modules (ESM) |
|---|---|---|
| 语法 | `require` / `module.exports` | `import` / `export` |
| 加载时机 | **运行时**同步加载 | **编译时**静态分析 |
| 输出方式 | 值的拷贝 | 值的引用（只读绑定） |
| 顶层 `this` | 指向 `module.exports` | 指向 `undefined` |
| 动态导入 | 天然支持 | `import()` 表达式 |
| 文件扩展名 | `.js`（Node 默认） | `.mjs` 或 `"type": "module"` |

**CommonJS 示例：**
```js
// math.js
function add(a, b) { return a + b; }
module.exports = { add };

// main.js
const math = require('./math.js');
console.log(math.add(1, 2));
```

**ES Modules 示例：**
```js
// math.mjs
export function add(a, b) { return a + b; }

// main.mjs
import { add } from './math.mjs';
console.log(add(1, 2));
```

**关键差异：**
- CJS 的 `require` 可以在代码任何位置调用（条件加载）；ESM 的 `import` 声明必须位于模块顶层
- CJS 导出的是值的**浅拷贝**（基础类型复制值，对象/数组复制引用）；修改导出对象内部的属性会影响外部，但重新赋值 `module.exports` 不会影响已 `require` 的模块。ESM 导出的是**实时只读引用**
- ESM 支持循环依赖的静态分析，CJS 在循环依赖时可能得到未完成的 `exports` 对象

---

#### import / export 语法详解

**命名导出与导入：**
```js
// utils.js
export const PI = 3.14159;
export function sum(a, b) { return a + b; }

// main.js
import { PI, sum } from './utils.js';
```

**默认导出与导入：**
```js
// logger.js
export default function log(msg) {
  console.log(`[LOG] ${msg}`);
}

// main.js
import log from './logger.js';
// 等价于 import { default as log } from './logger.js';
```

**重命名导入（解决命名冲突）：**
```js
import { PI as MATH_PI } from './utils.js';
import { PI as PHYSICS_PI } from './physics.js';
```

**命名空间导入：**
```js
import * as utils from './utils.js';
console.log(utils.PI);      // 3.14159
console.log(utils.sum(1, 2)); // 3
```

**混合导出（默认 + 命名）：**
```js
// api.js
export default function request() { /* ... */ }
export const BASE_URL = 'https://api.example.com';
export function handleError() { /* ... */ }

// main.js
import request, { BASE_URL, handleError } from './api.js';
```

**副作用导入（只执行模块，不导入值）：**
```js
import './polyfill.js'; // 执行 polyfill，不导入任何绑定
```

**关键细节：**
- `export` 声明的是 **绑定(binding)** 而非值，导出方修改值会同步反映到导入方（但导入方不能重新赋值）
- `export default` 每个模块只能有一个，本质上是导出一个名为 `default` 的绑定
- 在浏览器中，ESM 自动启用**严格模式**，且模块在独立作用域中运行，不会污染全局变量

---

#### 循环依赖与树摇优化（Tree Shaking）

**循环依赖（Circular Dependencies）：**
当模块 A 导入 B，而 B 又导入 A 时形成循环。

```js
// a.js
import { b } from './b.js';
export const a = 'A';
console.log(b); // 在 CJS 中可能为 undefined；ESM 中若存在顶层同步交叉访问，也会触发 TDZ 报错

// b.js
import { a } from './a.js';
export const b = 'B';
```

- **CJS**：运行时会缓存未完成的 `module.exports`，可能导致部分导出为 `undefined`
- **ESM**：由于静态分析，引擎能构建依赖图并按正确顺序实例化，循环依赖问题更可控
- **最佳实践**：尽量避免循环依赖；若无法避免，将共享逻辑提取到第三个模块

**Tree Shaking（树摇优化）：**
打包工具（如 Rollup、Webpack）利用 ESM 的静态结构，在编译时剔除未使用的代码（dead code elimination）。

```js
// utils.js
export function used() { return 'important'; }
export function unused() { return 'dead code'; } // 若未被导入，打包时会被移除

// main.js
import { used } from './utils.js';
```

**确保 Tree Shaking 生效的关键：**
- 使用 ESM 语法（`import` / `export`）
- 避免副作用导入（`import 'xxx'` 会让打包工具认为整个模块都有副作用）
- 在 `package.json` 中设置 `"sideEffects": false`（声明模块无副作用，可被安全移除）
- 对确实有副作用的文件，精确声明：`"sideEffects": ["*.css", "./src/polyfill.js"]`

---

### 6.4 后续版本新特性（ES2020+）

#### 类私有字段与方法

ES2022 正式支持使用 `#` 前缀声明类的私有成员，只能在类内部访问。

```js
class BankAccount {
  // 私有字段
  #balance = 0;

  // 静态私有字段
  static #bankName = 'Central Bank';

  constructor(initialBalance) {
    this.#balance = initialBalance;
  }

  // 私有方法
  #validate(amount) {
    return amount > 0;
  }

  deposit(amount) {
    if (!this.#validate(amount)) throw new Error('Invalid amount');
    this.#balance += amount;
    return this.#balance;
  }

  getBalance() {
    return this.#balance;
  }

  static getBankName() {
    return BankAccount.#bankName;
  }
}

const account = new BankAccount(100);
account.deposit(50);
console.log(account.getBalance()); // 150
// console.log(account.#balance); // SyntaxError: Private field must be declared in an enclosing class
```

**关键细节：**
- 私有字段必须在类顶层声明，不能在构造函数中动态添加
- 子类无法访问父类的私有成员（与 `private` 类似，但语法层面强制隔离）
- 使用 `in` 运算符可检查对象是否含有某私有字段：`#balance in account` → `true`

---

#### 动态 import()

ES2020 引入的 `import()` 函数允许在运行时动态加载模块，返回一个 Promise。

```js
// 条件加载
async function loadLocale(lang) {
  const module = await import(`./locales/${lang}.js`);
  return module.default;
}

// 懒加载（如路由懒加载）
const button = document.getElementById('load');
button.addEventListener('click', async () => {
  const { createChart } = await import('./chart.js');
  createChart(data);
});

// 错误处理
async function safeImport(path) {
  try {
    const mod = await import(path);
    return mod;
  } catch (err) {
    console.error(`Failed to load ${path}:`, err);
    return null;
  }
}
```

**关键细节：**
- `import()` 可以在代码任何位置使用（包括条件语句、函数内部）
- 模块只会执行一次，多次 `import()` 同一路径返回的是同一个模块实例
- 在打包工具中，`import()` 会自动触发代码分割（Code Splitting），生成独立的 chunk

---

#### 数组不变性方法（toSorted / toReversed 等）

ES2023 引入了数组的不可变版本方法，它们不会修改原数组，而是返回新数组。

```js
const arr = [3, 1, 2];

// toSorted：不改变原数组的 sort
const sorted = arr.toSorted((a, b) => a - b);
console.log(arr);     // [3, 1, 2]（原数组不变）
console.log(sorted);  // [1, 2, 3]

// toReversed：不改变原数组的 reverse
const reversed = arr.toReversed();
console.log(reversed); // [2, 1, 3]

// toSpliced：不改变原数组的 splice
const spliced = arr.toSpliced(1, 1, 'a', 'b');
console.log(spliced); // [3, 'a', 'b', 2]
console.log(arr);     // [3, 1, 2]

// with：不改变原数组的索引替换
const replaced = arr.with(1, 'x');
console.log(replaced); // [3, 'x', 2]
```

**关键细节：**
- 这些方法适用于需要**不可变数据**的场景（如 React 状态管理、Redux）
- 对于对象/数组元素，仍是**浅拷贝**，嵌套对象修改仍会影响原数据
- 这些方法同样存在于 `TypedArray` 上

---

### 🛠️ 实操：现代化重构练习

#### 将一个 ES5 项目重构为 ES6+（替换 var/函数/拼接字符串/回调地狱）

**重构前（ES5 风格）：**
```js
var users = ['Alice', 'Bob', 'Charlie'];

function greetUsers(list) {
  var result = [];
  for (var i = 0; i < list.length; i++) {
    result.push('Hello, ' + list[i] + '!');
  }
  return result;
}

function fetchUserData(id, callback) {
  setTimeout(function () {
    if (id > 0) {
      callback(null, { id: id, name: 'User ' + id });
    } else {
      callback(new Error('Invalid ID'));
    }
  }, 100);
}

fetchUserData(1, function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data); // { id: 1, name: 'User 1' }
  fetchUserData(data.id + 1, function (err2, data2) {
    if (err2) {
      console.error(err2);
      return;
    }
    console.log(data, data2);
  });
});
```

**重构后（ES6+ 风格）：**
```js
const users = ['Alice', 'Bob', 'Charlie'];

const greetUsers = (list) =>
  list.map(name => `Hello, ${name}!`);

const fetchUserData = (id) =>
  new Promise((resolve, reject) => {
    setTimeout(() => {
      id > 0
        ? resolve({ id, name: `User ${id}` })
        : reject(new Error('Invalid ID'));
    }, 100);
  });

// 使用 async/await 消除回调地狱
(async () => {
  try {
    const data = await fetchUserData(1);
    const data2 = await fetchUserData(data.id + 1);
    console.log(data, data2);
  } catch (err) {
    console.error(err);
  }
})();
```

**重构要点总结：**
| ES5 | ES6+ 替代 |
|---|---|
| `var` | `const` / `let` |
| `function` 声明 | 箭头函数（适合回调） |
| 字符串拼接 | 模板字符串 |
| `for` 循环 | `map` / `for...of` |
| 回调嵌套 | `Promise` + `async/await` |
| `arguments` | 剩余参数 `...args` |
| 对象方法 | 对象方法简写 / 计算属性名 |

---

#### 实现一个支持按需加载的模块化工具函数库（ESM 格式）

项目结构：
```
utils/
├── index.js       # 统一入口（可选，用于整体导入）
├── string.js      # 字符串工具
├── array.js       # 数组工具
├── dom.js         # DOM 工具
└── throttle.js    # 节流函数（单独导出，方便 tree-shaking）
```

**string.js：**
```js
export function camelCase(str) {
  return str.replace(/[-_](.)/g, (_, char) => char.toUpperCase());
}

export function truncate(str, maxLength) {
  return str.length > maxLength ? str.slice(0, maxLength) + '…' : str;
}
```

**array.js：**
```js
export function unique(arr) {
  return [...new Set(arr)];
}

export function groupBy(arr, keyFn) {
  return arr.reduce((groups, item) => {
    const key = keyFn(item);
    (groups[key] ||= []).push(item);
    return groups;
  }, {});
}
```

**dom.js：**
```js
export function $(selector, context = document) {
  return context.querySelector(selector);
}

export function $$(selector, context = document) {
  return [...context.querySelectorAll(selector)];
}

export function on(el, event, handler, options) {
  el.addEventListener(event, handler, options);
  return () => el.removeEventListener(event, handler, options);
}
```

**throttle.js：**
```js
export function throttle(fn, delay) {
  let lastTime = 0;
  return function (...args) {
    const now = Date.now();
    if (now - lastTime >= delay) {
      lastTime = now;
      fn.apply(this, args);
    }
  };
}
```

**index.js（可选统一入口）：**
```js
export * from './string.js';
export * from './array.js';
export * from './dom.js';
export { throttle } from './throttle.js';
```

**使用方式（按需加载）：**
```js
// 按需导入，打包工具会自动 tree-shaking 未使用的代码
import { camelCase } from './utils/string.js';
import { throttle } from './utils/throttle.js';

// 或整体导入
import * as utils from './utils/index.js';
```

---

#### 用生成器函数实现一个可迭代的数据流（如斐波那契数列生成器）

```js
function* fibonacci(maxCount = Infinity) {
  let [prev, curr] = [0, 1];
  let count = 0;

  while (count < maxCount) {
    yield curr;
    [prev, curr] = [curr, prev + curr];
    count++;
  }
}

// 基础用法
for (const num of fibonacci(10)) {
  console.log(num); // 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
}

// 配合展开运算符获取数组
const first10 = [...fibonacci(10)];
console.log(first10);

// 惰性筛选：只取偶数
function* filter(iterable, predicate) {
  for (const item of iterable) {
    if (predicate(item)) yield item;
  }
}

const evenFib = filter(fibonacci(20), n => n % 2 === 0);
console.log([...evenFib]); // [2, 8, 34, 144, 610, 2584]

// 惰性映射
function* map(iterable, mapper) {
  for (const item of iterable) {
    yield mapper(item);
  }
}

const squaredFib = map(fibonacci(5), n => n * n);
console.log([...squaredFib]); // [1, 1, 4, 9, 25]
```

**进阶：双向数据流生成器**
```js
function* runningAverage() {
  let sum = 0;
  let count = 0;

  while (true) {
    const value = yield count === 0 ? 0 : sum / count;
    sum += value;
    count++;
  }
}

const avg = runningAverage();
avg.next(); // 启动生成器

console.log(avg.next(10).value); // 10
console.log(avg.next(20).value); // 15
console.log(avg.next(30).value); // 20
```

**关键细节：**
- 生成器函数配合 `yield` 实现了**惰性求值**，适合处理无限序列或大数据流
- 通过组合 `filter`、`map` 等生成器函数，可以构建类似 LINQ/RxJS 的流式数据处理管道
- 双向通信让生成器不仅是"生产者"，还可以作为"消费者"接收外部输入

> **本章小结：** 我们学习了 ES6+ 的语法增强、迭代协议、模块化机制以及后续版本的新特性，并通过实战练习将 ES5 代码重构为现代化的 ES6+ 风格。
>
> **下一章预告：** 学会了让代码在浏览器中运行，接下来要思考的是：代码出错了怎么办？下一章将学习 JavaScript 的错误类型、异常处理机制以及如何使用 DevTools 高效调试。
