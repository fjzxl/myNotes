# ES6 入门与实践：给有 JavaScript 基础的你

> **阅读前提**：假设你已经能用 JavaScript 写基础代码（变量、函数、条件判断、循环、简单 DOM 操作），但还没有系统学习过 ES6。
>
> **学习目标**：读完本文后，你能熟练使用 ES6 编写现代 JavaScript 代码，理解这些特性解决了什么问题，并知道在实际项目中如何应用。

---

## 📋 目录与学习路线

| 章节 | 内容 | 难度 | 建议时间 |
|------|------|------|---------|
| [0. 什么是 ES6？](#0-什么是-es6为什么要学) | 背景介绍 | ⭐ | 5 min |
| [1. let 与 const](#1-变量的新声明方式let-与-const) | 新变量声明 | ⭐ | 20 min |
| [2. 模板字符串](#2-字符串的革新模板字面量) | 字符串处理 | ⭐ | 15 min |
| [3. 函数增强](#3-函数增强) | 箭头函数、默认参数等 | ⭐ | 25 min |
| [4. 解构赋值](#4-解构赋值) | 数据提取 | ⭐ | 20 min |
| [5. 函数增强（续）](#5-函数增强续) | 函数组合技巧 | ⭐ | 15 min |
| [6. 对象增强](#6-对象增强) | 简写、计算属性等 | ⭐ | 15 min |
| [7. 数组增强](#7-数组增强) | 新方法 | ⭐ | 15 min |
| [8. Class](#8-类class-语法) | 面向对象 | ⭐⭐ | 30 min |
| [9. 模块化](#9-模块化) | import/export | ⭐⭐ | 25 min |
| [10. Promise](#10-异步编程promise) | 异步基础 | ⭐⭐ | 35 min |
| [11. async/await](#11-asyncawait) | 异步进阶 | ⭐⭐ | 30 min |
| [12. Set 与 Map](#12-新的数据结构) | 新数据结构 | ⭐⭐ | 20 min |
| [13. Symbol](#13-symbol) | 新原始类型 | ⭐⭐ | 15 min |
| [14. 迭代器](#14-迭代与遍历) | for...of | ⭐⭐ | 15 min |
| [15. 生成器](#15-生成器-generator进阶) | Generator | ⭐⭐⭐ | 选读 |
| [16. Proxy](#16-proxy--reflect进阶) | 元编程 | ⭐⭐⭐ | 选读 |
| [附录 A](#附录-a事件循环与异步原理) | 事件循环 | ⭐⭐⭐ | 遇到问题时回来看 |
| [附录 B](#附录-b速查表) | 速查表 | - | 备用 |

**学习建议**：
- 前 7 章（带 ⭐ 的）是**日常开发最常用**的内容，建议按顺序仔细阅读并动手练习。
- 第 8~11 章是现代 JS 工程化的核心，必须掌握。
- 第 12~14 章使用频率中等，了解即可，遇到场景再深入。
- 第 15~16 章属于进阶内容，初学者可以先跳过，知道有这些东西就行。

---

## 0. 什么是 ES6？为什么要学？

### ES6 是什么

**ES6** = **ECMAScript 2015**，是 JavaScript 语言的一次重大升级，2015 年正式发布。

你可以把 ECMAScript 理解为 JavaScript 的"标准规范"，而 ES6 就是这个规范的第 6 个版本。日常说的 ES6+，通常泛指从 ES6 开始的所有现代 JavaScript 特性（ES2015、ES2016、ES2017……）。

### 一句话总结：ES6 让 JavaScript 从"能写"变成"好写"

在 ES6 之前，JavaScript 有很多让人头疼的问题：

| 痛点 | ES5 写法 | ES6 解决方案 |
|------|---------|------------|
| 变量提升导致意外错误 | `var` 声明的变量会"提升" | `let` / `const` + 块级作用域 |
| 字符串拼接又臭又长 | `'Hello, ' + name + '!'` | 模板字符串 `` `Hello, ${name}!` `` |
| `this` 指向经常搞错 | `var self = this` 这种 workaround | 箭头函数的词法 `this` |
| 从对象/数组里取数据代码冗长 | `var name = user.name` | 解构赋值 `const { name } = user` |
| 回调函数层层嵌套 | "回调地狱" | Promise + async/await |
| 没有官方模块化方案 | 依赖 AMD/CommonJS 等第三方方案 | `import` / `export` |

### 浏览器支持

现代浏览器（Chrome、Firefox、Edge、Safari 的最新两个大版本）已经**原生支持**绝大部分 ES6 特性。只有一些非常老的浏览器（如 IE11）需要借助 [Babel](https://babeljs.io/) 等工具转译。

> 💡 **实际建议**：现在写代码，完全可以放心使用 ES6+ 语法。如果项目需要兼容老浏览器，构建工具会自动帮你转译，你只需关注写出现代、优雅的代码。

---

## 1. 变量的新声明方式：let 与 const

> 这是 ES6 **最基础也最重要**的改变。学会用 `let` 和 `const` 替代 `var`，是你迈向现代 JS 的第一步。

### 1.1 var 的问题：为什么需要改变？

ES5 只有 `var` 一种变量声明方式，但它有两个大坑：**变量提升**和**没有块级作用域**。

#### 坑 1：变量提升（Hoisting）

```js
console.log(name);  // undefined（居然不报错！）
var name = 'Alice';
console.log(name);  // "Alice"
```

上面这段代码实际被解释器理解为：

```js
var name;           // 声明被"提升"到作用域顶部
console.log(name);  // undefined
name = 'Alice';     // 赋值留在原地
console.log(name);  // "Alice"
```

这种**先使用、后声明却不报错**的行为，常常导致难以发现的 Bug。

#### 坑 2：没有块级作用域

```js
var count = 10;

if (count > 5) {
  var message = 'count 大于 5';
}

console.log(message);  // "count 大于 5" —— if 块外面的代码居然能访问到！
```

在别的语言（如 Java、C++）中，`if`、`for` 这种大括号 `{}` 会形成一个**块级作用域**，块外访问不到块内的变量。但 `var` 只有**函数作用域**，没有块级作用域。

#### 坑 3：循环中的闭包陷阱（经典面试题）

```js
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);
  }, 100);
}
// 输出：3, 3, 3（而不是 0, 1, 2）
```

原因：`var i` 是在整个函数作用域内的同一个变量。循环结束时 `i` 已经是 3，三个定时器回调都引用了这个已经被改成 3 的 `i`。

### 1.2 let：有块级作用域的变量

`let` 的用法和 `var` 看起来一样，但行为完全不同：

```js
let count = 10;

if (count > 5) {
  let message = 'count 大于 5';
}

console.log(message);  // ReferenceError: message is not defined ✅
```

现在 `message` 被正确地限制在 `if` 块内部了！

#### let 解决循环闭包问题

```js
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);
  }, 100);
}
// 输出：0, 1, 2 ✅
```

原因：每次循环迭代，`let` 都会创建一个新的块级作用域，`i` 的值被"快照"保存到该作用域中。

#### let 不会被提升（严格说是 TDZ）

```js
console.log(name);  // ReferenceError: Cannot access 'name' before initialization ✅
let name = 'Alice';
```

这次真的报错了！这反而是一种**保护**——让你不会因为先使用后声明而产生隐晦的 Bug。

### 1.3 const：常量声明

`const` 和 `let` 几乎一样，也有块级作用域，也受 TDZ 限制。唯一的区别是：**const 声明的变量不能被重新赋值**。

```js
const PI = 3.14159;
PI = 3;  // TypeError: Assignment to constant variable ✅
```

#### ⚠️ 重要：const 保护的是"绑定"，不是"值"

这是初学者最容易混淆的地方：

```js
const user = { name: 'Alice', age: 25 };

user.name = 'Bob';      // ✅ 可以！修改对象属性没问题
user.age = 30;          // ✅ 可以！
user = {};              // ❌ TypeError！不能重新赋值整个对象

const numbers = [1, 2, 3];
numbers.push(4);        // ✅ 可以！修改数组内容没问题
numbers[0] = 10;        // ✅ 可以！
numbers = [5, 6];       // ❌ TypeError！不能重新赋值整个数组
```

如果你想让对象/数组也"完全不可变"，需要用 `Object.freeze()`（浅冻结）或者 Immutable 库，这不是 ES6 的核心内容。

### 1.4 TDZ（Temporal Dead Zone，暂时性死区）

这是一个听起来吓人但理解很简单的概念：

```js
{
  // 从这里到 let 声明的那一行，就是 "TDZ"
  console.log(x);  // ReferenceError：在 TDZ 中访问 x
  let x = 10;
  console.log(x);  // 10 ✅
}
```

简单说：**用 `let`/`const` 声明的变量，在声明之前那一片区域就是"死区"，访问会报错**。这防止了 `var` 那种"先访问得到 undefined"的奇怪行为。

> 💡 **不需要死记硬背 TDZ 这个术语**。只要记住：**`let`/`const` 声明的变量，先声明再使用，总是安全的**。

---

### 💭 知识检查点

**问题**：下面代码会报错吗？如果会，是在哪一行？

```js
console.log(x);  // 第1行
let x = 10;
```

<details>
<summary>点击查看答案</summary>

**会报错**。第1行 `console.log(x)` 会抛出 `ReferenceError: Cannot access 'x' before initialization`。

因为 `let x = 10` 的声明本身也被 TDZ 保护了，在声明之前的区域访问都会报错。

</details>

---

### 1.5 实践规则

现在你只需要记住三条规则：

1. **默认使用 `const`** —— 如果确定一个变量不需要重新赋值，就用 `const`。这会让你的代码更安全，也更容易阅读（读者一看就知道这个变量不会被改）。
2. **确实需要重新赋值时，用 `let`** —— 比如循环计数器、累加器等。
3. **永远不要使用 `var`** —— 除非你在维护很老的代码库。

```js
// ✅ 好的实践
const API_URL = 'https://api.example.com';
const user = { name: 'Alice' };
let count = 0;
for (let i = 0; i < 10; i++) {
  count += i;
}

// ❌ 避免
var API_URL = '...';
var count = 0;
```

### ✏️ 练习

**练习 1** ⭐：下面的代码会输出什么？为什么？

```js
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 0);
}
```

如果把 `var` 改成 `let`，输出会变吗？变成什么？

**练习 2** ⭐：找出下面代码的问题：

```js
const config = { debug: true };
config.debug = false;
config = { debug: true };
```

**练习 3** ⭐：用 `let` 重写下面的代码，确保 `message` 只在 `if` 块内部可访问：

```js
if (true) {
  var message = 'hello';
}
console.log(message);
```

**练习 4** ⭐⭐：下面代码会输出什么？还是会报错？为什么？

```js
const arr = [];
for (const i = 0; i < 3; i++) {
  arr.push(() => i);
}
console.log(arr.map(fn => fn()));
```

---

### 📌 本章要点

1. **`var` 有两个致命缺陷**：变量提升（先使用后声明不报错）和没有块级作用域
2. **`let` 有块级作用域**，每次循环迭代都会创建新变量，解决了经典闭包陷阱
3. **`const` 和 `let` 都有 TDZ**（暂时性死区），在声明前访问会报错——这是保护，不是限制
4. **`const` 保护的是绑定不是值**：可以修改对象的属性，但不能重新赋值整个对象
5. **实践原则**：默认用 `const`，需要重新赋值时用 `let`，永远不用 `var`

---

## 2. 字符串的革新：模板字面量

> 模板字面量（Template Literals）是 ES6 中**最直观、最容易上手**的特性之一。它用反引号 `` ` `` 包裹字符串，解决了传统字符串拼接的痛苦。

### 2.1 字符串拼接的痛点

ES5 中拼接动态内容：

```js
var name = 'Alice';
var age = 25;
var hobby = 'coding';

var sentence = 'My name is ' + name + ', I am ' + age + ' years old, and I love ' + hobby + '.';
// 可读性差，容易漏空格，引号多容易出错
```

### 2.2 模板字符串语法

用反引号 `` ` `` 代替单双引号，用 `${}` 嵌入表达式：

```js
const name = 'Alice';
const age = 25;
const hobby = 'coding';

const sentence = `My name is ${name}, I am ${age} years old, and I love ${hobby}.`;
// 清晰、直观、不易出错
```

`${}` 里可以写**任何有效的 JavaScript 表达式**：

```js
const a = 10, b = 20;

console.log(`a + b = ${a + b}`);                          // "a + b = 30"
console.log(`Uppercase: ${name.toUpperCase()}`);           // "Uppercase: ALICE"
console.log(`Is adult: ${age >= 18 ? 'Yes' : 'No'}`);     // "Is adult: Yes"
console.log(`Random: ${Math.random()}`);                   // "Random: 0.8342..."
```

### 2.3 多行字符串

ES5 写多行字符串：

```js
var html = '<div class="card">\n' +
  '  <h2>Title</h2>\n' +
  '  <p>Content here</p>\n' +
  '</div>';
```

ES6 写多行字符串：

```js
const html = `
  <div class="card">
    <h2>Title</h2>
    <p>Content here</p>
  </div>
`;
```

直接在反引号里换行即可，无需 `\n` 和字符串拼接。

> ⚠️ **注意**：模板字符串会保留所有的空格和缩进。如果你在意字符串开头的换行或多余的缩进，可以使用 `.trim()` 或者调整代码缩进。

### 2.4 嵌套模板

模板字符串里可以嵌套另一个模板字符串：

```js
const items = ['apple', 'banana', 'orange'];

const list = `
  <ul>
    ${items.map(item => `<li>${item}</li>`).join('')}
  </ul>
`;
// <ul>
//   <li>apple</li><li>banana</li><li>orange</li>
// </ul>
```

这在生成 HTML、SQL 等模板时非常有用。

### 2.5 标签模板（Tagged Templates）—— 了解即可

标签模板是一种高级用法，初学者可以先跳过，知道有这个东西就行：

```js
function highlight(strings, ...values) {
  let result = '';
  strings.forEach((str, i) => {
    result += str;
    if (i < values.length) {
      result += `[${values[i]}]`;
    }
  });
  return result;
}

const name = 'Alice';
const age = 25;
highlight`She is ${name}, ${age} years old.`;
// "She is [Alice], [25] years old."
```

实际应用：库函数 [styled-components](https://styled-components.com/)、[graphql-tag](https://github.com/apollographql/graphql-tag) 都大量使用了标签模板。

### ✏️ 练习

**练习 1** ⭐：用模板字符串改写下面的代码：

```js
var user = { name: 'Bob', score: 85 };
var msg = 'Congratulations, ' + user.name + '! Your score is ' + user.score + '.';
```

**练习 2** ⭐：用模板字符串生成一段 HTML（假设 `title = 'My Page'`，`content = 'Hello World'`）：

```html
<article>
  <h1>My Page</h1>
  <p>Hello World</p>
</article>
```

**练习 3** ⭐⭐：用嵌套模板实现一个生成表格的函数：

```js
const headers = ['Name', 'Age', 'City'];
const rows = [
  ['Alice', 25, 'Beijing'],
  ['Bob', 30, 'Shanghai'],
  ['Charlie', 35, 'Guangzhou']
];
// 期望生成 HTML 表格字符串
```

---

### 📌 本章要点

1. **模板字符串用反引号 `` ` `` 包裹**，用 `${}` 插入表达式
2. **`${}` 里可以是任何表达式**：变量、运算、三元表达式、函数调用都可以
3. **模板字符串支持多行**，保留空格和缩进（可用 `.trim()` 去除首尾空白）
4. **标签模板**（了解即可）：用于 `styled-components`、GraphQL 等库

---

## 3. 函数增强

### 3.1 箭头函数

箭头函数（Arrow Functions）是 ES6 中最具代表性的语法糖之一。它让函数写起来更短，同时解决了 JavaScript 中 infamous 的 `this` 绑定问题。

#### 基本语法

```js
// ES5 函数表达式
var add = function(a, b) {
  return a + b;
};

// ES6 箭头函数
const add = (a, b) => {
  return a + b;
};

// 如果函数体只有一行 return，可以进一步简化
const add = (a, b) => a + b;
```

三种省略规则：

```js
// 1. 只有一个参数时，可以省略括号
const square = x => x * x;

// 2. 没有参数或多个参数，括号不能省略
const sayHi = () => 'Hi';
const greet = (name, time) => `Good ${time}, ${name}!`;

// 3. 函数体只有一行表达式时，省略 {} 和 return，表达式的结果就是返回值
const double = x => x * 2;

// 如果要返回一个对象字面量，需要用括号包起来（否则 {} 会被当成函数体）
const makeUser = name => ({ name: name, active: true });
```

#### 箭头函数与 this —— 必须理解的核心区别

这是箭头函数**最重要**的特性，也是面试高频考点。

**普通函数的 `this` 由调用方式决定**：

```js
const person = {
  name: 'Alice',
  sayHi: function() {
    console.log('Hi, I am ' + this.name);
  }
};

person.sayHi();  // "Hi, I am Alice" ✅

const fn = person.sayHi;
fn();  // "Hi, I am undefined"（非严格模式下是 window）
// this 丢失了！因为 fn() 是"普通调用"
```

**箭头函数的 `this` 由定义时的外层作用域决定**（词法绑定）：

```js
const person = {
  name: 'Alice',
  sayHi: () => {
    console.log('Hi, I am ' + this.name);
  }
};

person.sayHi();  // "Hi, I am undefined"
// 因为箭头函数定义时，外层的 this 是全局对象，不是 person
```

⚠️ **所以，不要把箭头函数直接作为对象的方法**（除非你知道自己在做什么）。

---

### 💭 知识检查点

**问题**：下面代码的输出是什么？

```js
const obj = {
  name: 'Alice',
  // 用箭头函数定义方法
  sayHi: () => console.log(`Hi, I am ${this.name}`)
};

obj.sayHi();  // 输出什么？
```

<details>
<summary>点击查看答案</summary>

输出 `Hi, I am undefined`。

箭头函数的 `this` 在定义时就已经确定，指向定义时外层的 `this`，而不是 `obj`。所以 `this.name` 不是 `Alice`，而是 `undefined`（或严格模式下 `undefined`）。

</details>

---

#### 箭头函数的真正用武之地：回调

箭头函数最大的价值在**回调函数**中：

```js
// ❌ ES5：需要 var self = this 这种 hack
var timer = {
  seconds: 0,
  start: function() {
    var self = this;  // 保存 this，否则 setTimeout 里 this 会变
    setInterval(function() {
      self.seconds++;
      console.log(self.seconds);
    }, 1000);
  }
};

// ✅ ES6：箭头函数自动继承外层 this
const timer = {
  seconds: 0,
  start() {
    setInterval(() => {
      this.seconds++;  // this 就是 timer 对象！
      console.log(this.seconds);
    }, 1000);
  }
};
```

再比如 DOM 事件处理中的经典场景：

```js
// ❌ ES5
button.addEventListener('click', function() {
  this.classList.add('active');  // this 是 button，没问题
  setTimeout(function() {
    this.classList.remove('active');  // ❌ this 变成了 window！
  }, 1000);
});

// ✅ ES6
button.addEventListener('click', function() {
  this.classList.add('active');
  setTimeout(() => {
    this.classList.remove('active');  // ✅ this 继承自外层，还是 button
  }, 1000);
});
```

#### ⚠️ 箭头函数不能做的事

| 特性 | 箭头函数 | 说明 |
|------|---------|------|
| 构造函数 | ❌ 不支持 | 不能用 `new` 调用 |
| `arguments` | ❌ 没有 | 用剩余参数 `...args` 代替 |
| `prototype` | ❌ 没有 | 无法添加原型方法 |
| 改变 `this` | ❌ 不支持 | `call`/`apply`/`bind` 对箭头函数无效 |
| 生成器 | ❌ 不支持 | 不能用 `function*` 语法 |

```js
// 如果需要 arguments，用剩余参数
const logArgs = (...args) => {
  console.log(args);  // 真正的数组
};
logArgs(1, 2, 3);  // [1, 2, 3]
```

### 3.2 默认参数

ES5 设置默认值的常见做法有 Bug：

```js
function greet(name) {
  name = name || 'Guest';  // 问题：''、0、false 也会触发默认值！
  return 'Hello, ' + name;
}

greet('');     // "Hello, Guest" ❌ 明明传了空字符串
greet(0);      // "Hello, Guest" ❌ 明明传了 0
```

ES6 默认参数**只在参数为 `undefined` 时生效**：

```js
function greet(name = 'Guest') {
  return `Hello, ${name}`;
}

greet();            // "Hello, Guest" ✅ 没传参
greet(undefined);   // "Hello, Guest" ✅ 显式传 undefined
greet('');          // "Hello, " ✅ 空字符串不会被替换
greet(null);        // "Hello, null" ✅ null 也不会被替换
greet('Alice');     // "Hello, Alice" ✅
```

默认值也可以是表达式，甚至引用前面的参数：

```js
function createUser(name, greeting = `Hello, ${name}!`) {
  return { name, greeting };
}

createUser('Alice');  // { name: "Alice", greeting: "Hello, Alice!" }
```

### 3.3 剩余参数（Rest Parameters）

ES5 中处理不定数量参数：

```js
function sum() {
  // arguments 是类数组对象，不是真正的数组
  var args = Array.prototype.slice.call(arguments);
  return args.reduce(function(a, b) { return a + b; }, 0);
}
```

ES6 剩余参数：

```js
function sum(...numbers) {
  // numbers 是真正的数组，可以直接用数组方法
  return numbers.reduce((a, b) => a + b, 0);
}

sum(1, 2, 3, 4);  // 10
```

```js
// 可以和其他参数混用，但剩余参数必须是最后一个
function greet(greeting, ...names) {
  return `${greeting}, ${names.join(' and ')}!`;
}

greet('Hello', 'Alice', 'Bob', 'Charlie');
// "Hello, Alice and Bob and Charlie!"
```

### 3.4 展开运算符（Spread Operator）

展开运算符 `...` 和剩余参数写法一样，但用在**调用方**（函数调用、数组/对象字面量）而不是**定义方**。

#### 展开数组

```js
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// ES5：用 concat
var combined = arr1.concat(arr2);

// ES6：用展开运算符
const combined = [...arr1, ...arr2];  // [1, 2, 3, 4, 5, 6]

// 更灵活的用法
const withExtra = [0, ...arr1, 99, ...arr2, 100];
// [0, 1, 2, 3, 99, 4, 5, 6, 100]
```

#### 函数调用中展开

```js
const nums = [5, 10, 3];

// ES5
Math.max.apply(null, nums);  // 10

// ES6
Math.max(...nums);  // 10
```

#### 数组浅拷贝

```js
const original = [1, 2, 3];
const copy = [...original];

copy.push(4);
console.log(original);  // [1, 2, 3]（互不影响）
console.log(copy);      // [1, 2, 3, 4]

// ⚠️ 注意：是浅拷贝！如果数组元素是对象，内部引用还是共享的
const objects = [{ a: 1 }, { b: 2 }];
const objectsCopy = [...objects];
objectsCopy[0].a = 999;
console.log(objects[0].a);  // 999
```

#### 展开字符串

```js
const chars = [...'hello'];  // ['h', 'e', 'l', 'l', 'o']
```

### ✏️ 练习

**练习 1** ⭐：将下面的 ES5 函数改写成箭头函数：

```js
var multiply = function(x, y) {
  return x * y;
};
```

**练习 2** ⭐：下面的代码有什么问题？如何修复？

```js
const counter = {
  count: 0,
  increment: () => {
    this.count++;
    console.log(this.count);
  }
};
counter.increment();
```

**练习 3** ⭐：用剩余参数和展开运算符实现一个函数，它接收任意数量的数字，返回它们的平均值：

```js
average(1, 2, 3, 4);  // 2.5
```

**练习 4** ⭐：合并两个数组 `[1, 2]` 和 `[3, 4]`，并在中间插入 `99`：

```js
// 期望结果：[1, 2, 99, 3, 4]
```

**练习 5** ⭐⭐：实现一个 `createUrl(base, ...paths)` 函数，将 base 和 paths 组合成完整 URL：

```js
createUrl('https://api.example.com', 'users', '123', 'posts');
// 期望：'https://api.example.com/users/123/posts'
```

---

### 📌 本章要点

1. **箭头函数语法糖**：`const fn = x => x * 2`，单参数可省略括号，单行函数体可省略 `{}` 和 `return`
2. **箭头函数没有自己的 `this`**：继承定义时外层的 `this`，永远不变
3. **箭头函数不能用作构造函数**，也没有 `arguments` 和 `prototype`
4. **默认参数**：只在参数为 `undefined` 时生效，`''`、`0`、`null` 不会触发默认值
5. **剩余参数 `...args`**：必须是最后一个参数，得到真正的数组
6. **展开运算符 `...`**：在调用时使用，将数组/可迭代对象展开为独立元素

---

## 4. 解构赋值

> 解构赋值（Destructuring）让你可以从数组或对象中**一次性提取多个值**。这是日常开发中使用频率极高的特性。

### 4.1 数组解构

```js
const colors = ['red', 'green', 'blue'];

// ES5
var first = colors[0];
var second = colors[1];
var third = colors[2];

// ES6 解构
const [first, second, third] = colors;
console.log(first, second, third);  // "red" "green" "blue"
```

#### 跳过元素

```js
const [a, , c] = [10, 20, 30];
console.log(a, c);  // 10 30（跳过了 20）
```

#### 剩余模式

```js
const [head, ...tail] = [1, 2, 3, 4, 5];
console.log(head);  // 1
console.log(tail);  // [2, 3, 4, 5]
```

#### 默认值

```js
const [x = 1, y = 2, z = 3] = [10, 20];
console.log(x, y, z);  // 10 20 3（z 没有对应值，用默认值）
```

#### 实用场景：交换变量

```js
let a = 1, b = 2;
[a, b] = [b, a];  // 不需要临时变量！
console.log(a, b);  // 2 1
```

### 4.2 对象解构

```js
const user = {
  id: 1,
  name: 'Alice',
  email: 'alice@example.com',
  address: {
    city: 'Beijing',
    country: 'China'
  }
};

// ES5
var name = user.name;
var email = user.email;

// ES6
const { name, email } = user;
console.log(name, email);  // "Alice" "alice@example.com"
```

#### 重命名

```js
// 把 user.name 提取出来，变量名叫 userName
const { name: userName, email: userEmail } = user;
console.log(userName);  // "Alice"
```

#### 默认值

```js
const { age = 18 } = user;
console.log(age);  // 18（user 中没有 age 属性）
```

#### 嵌套解构

```js
const { address: { city } } = user;
console.log(city);  // "Beijing"

// 同时提取多层数据
const { name, address: { country } } = user;
console.log(name, country);  // "Alice" "China"
```

#### 剩余属性（ES2018）

```js
const { id, ...rest } = user;
console.log(id);     // 1
console.log(rest);   // { name: "Alice", email: "...", address: {...} }
```

### 4.3 函数参数解构 —— 最实用的模式

这是解构在真实项目中最常见的用法：

```js
// ❌ 不解构：代码冗长，容易写错顺序
function printUser(user) {
  console.log(user.name + ' (' + user.email + '), age: ' + (user.age || 18));
}

// ✅ 解构：清晰、可以设默认值
function printUser({ name, email, age = 18 }) {
  console.log(`${name} (${email}), age: ${age}`);
}

printUser({ name: 'Bob', email: 'bob@test.com' });
// "Bob (bob@test.com), age: 18"
```

嵌套参数解构：

```js
function displayAddress({ name, address: { city, country } }) {
  console.log(`${name} lives in ${city}, ${country}`);
}

displayAddress(user);
// "Alice lives in Beijing, China"
```

给整个参数设默认值（防止不传参时报错）：

```js
function fetchData({ url, method = 'GET', headers = {} } = {}) {
  console.log(`${method} ${url}`);
}

fetchData();  // 不会报错！默认参数是空对象
fetchData({ url: '/api/users' });  // "GET /api/users"
fetchData({ url: '/api/users', method: 'POST' });  // "POST /api/users"
```

### ✏️ 练习

**练习 1** ⭐：用解构从数组中提取第一个和最后一个元素（提示：结合剩余模式）：

```js
const nums = [10, 20, 30, 40, 50];
// 期望：first = 10, last = 50
```

**练习 2** ⭐：解构下面的对象，提取 `title` 和 `author.name`：

```js
const book = {
  title: 'JavaScript Guide',
  author: { name: 'John', email: 'john@test.com' },
  year: 2023
};
```

**练习 3** ⭐：用参数解构优化这个函数：

```js
function createButton(options) {
  var text = options.text || 'Click';
  var color = options.color || 'blue';
  var size = options.size || 'medium';
  return `<button class="${size}" style="color:${color}">${text}</button>`;
}
```

**练习 4** ⭐⭐：用解构交换两个变量，不能使用临时变量：

```js
let a = 1, b = 2;
// 交换后：a = 2, b = 1
```

**练习 5** ⭐⭐⭐：解构下面的嵌套对象，提取 `type` 和 `firstCoords`：

```js
const data = {
  type: 'locations',
  locations: [
    { name: 'Beijing', coords: [39.9, 116.4] },
    { name: 'Tokyo', coords: [35.6, 139.7] }
  ]
};
// 期望：type = 'locations', firstCoords = [39.9, 116.4]
```

---

### 📌 本章要点

1. **数组解构**：`const [a, b, ...rest] = arr`，按位置匹配，支持剩余模式
2. **对象解构**：`const { name, age } = user`，按属性名匹配，支持重命名 `{ name: n }`
3. **默认值**：`const { age = 18 } = user`，只在属性不存在或值为 `undefined` 时生效
4. **嵌套解构**：`const { address: { city } } = user`，可以提取嵌套属性
5. **函数参数解构**：让参数更清晰，`function fn({ name, age = 18 }) {}`
6. **交换变量**：`[a, b] = [b, a]`，不需要临时变量

---

## 5. 函数增强（续）

> 第 3 章已经介绍了箭头函数、默认参数、剩余参数和展开运算符。这里补充一些使用技巧和常见组合模式。

### 常用组合模式

```js
// 箭头函数 + 默认参数 + 解构
const createUser = ({ name, role = 'user', active = true } = {}) => ({
  id: Math.random().toString(36).substr(2, 9),
  name,
  role,
  active,
  createdAt: new Date()
});

createUser({ name: 'Alice' });
// { id: "abc123", name: "Alice", role: "user", active: true, createdAt: ... }
```

### ✏️ 练习

**练习 1** ⭐：写一个 `formatDate` 函数，接收一个日期对象和可选的格式字符串（默认 `'YYYY-MM-DD'`），返回格式化后的字符串。

**练习 2** ⭐⭐：用箭头函数 + 默认参数 + 解构实现一个 `createProduct` 函数：

```js
createProduct({ name: 'Widget', price: 99.9, category: 'electronics' });
// 期望返回：{ id: 'xxx', name: 'Widget', price: 99.9, category: 'electronics', createdAt: Date }
```

---

### 📌 本章要点

1. **组合使用**：箭头函数 + 默认参数 + 解构可以写出极简的函数
2. **工厂函数模式**：ES6 的对象增强让创建和返回对象更简洁

---

## 6. 对象增强

> ES6 让对象字面量的写法更简洁，并增加了几个实用方法。

### 6.1 属性简写

当属性名和变量名相同时，可以只写变量名：

```js
const name = 'Alice';
const age = 25;

// ES5
var person = { name: name, age: age };

// ES6
const person = { name, age };
// 等价于 { name: 'Alice', age: 25 }
```

这在返回对象时特别有用：

```js
function makePoint(x, y) {
  return { x, y };  // 而不是 { x: x, y: y }
}
```

### 6.2 方法简写

```js
// ES5
var person = {
  name: 'Alice',
  sayHi: function() {
    return 'Hi, ' + this.name;
  }
};

// ES6
const person = {
  name: 'Alice',
  sayHi() {  // 省略 :function
    return `Hi, ${this.name}`;
  }
};
```

> ⚠️ 注意：方法简写和传统 `sayHi: function() {}` 有一个细微区别——方法简写创建的函数是可作为构造函数的（虽然通常你不会这么做），而且它们有 `prototype` 属性。但对日常开发来说，几乎可以互换使用。

### 6.3 计算属性名

允许用表达式作为属性名：

```js
const prefix = 'user';
const id = 42;

const obj = {
  [prefix + '_id']: id,
  [prefix + '_name']: 'Alice',
  [`${prefix}_email`]: 'alice@test.com'
};

console.log(obj.user_id);     // 42
console.log(obj.user_name);   // "Alice"
```

这在根据变量动态生成属性名时非常有用，比如 Redux 的 action handler：

```js
const handlers = {
  [ACTION_TYPES.LOADING](state) {
    return { ...state, loading: true };
  },
  [ACTION_TYPES.SUCCESS](state, action) {
    return { ...state, loading: false, data: action.payload };
  }
};
```

### 6.4 Object.assign —— 对象浅合并

```js
const target = { a: 1, b: 2 };
const source = { b: 3, c: 4 };

Object.assign(target, source);
console.log(target);  // { a: 1, b: 3, c: 4 }
// 后面的 source 会覆盖 target 中的同名属性
```

常用技巧——对象浅拷贝：

```js
const original = { x: 1, y: 2 };
const copy = Object.assign({}, original);

// 或者用展开运算符（更常用）
const copy2 = { ...original };
```

> ⚠️ `Object.assign` 和 `{...obj}` 都是**浅拷贝**。如果对象嵌套了其他对象，嵌套的对象仍然是共享引用。

### 6.5 Object.is —— 更精确的比较

```js
// === 的两个例外
NaN === NaN;        // false
+0 === -0;          // true

// Object.is 修正了这两个问题
Object.is(NaN, NaN);    // true ✅
Object.is(+0, -0);      // false ✅
Object.is({}, {});      // false（和 === 一样，引用不同）
```

日常开发中，`===` 足够用了。只有处理 `NaN` 或关心 `+0`/`-0` 区别时，才需要 `Object.is`。

### ✏️ 练习

**练习 1** ⭐：用属性简写和方法简写重写下面的对象：

```js
var name = 'Bob';
var age = 30;
var person = {
  name: name,
  age: age,
  greet: function() {
    return 'Hello from ' + this.name;
  }
};
```

**练习 2** ⭐：写一个函数 `createCounter`，返回一个对象，包含 `increment`、`decrement` 和 `getValue` 方法：

```js
const counter = createCounter(10);
counter.increment();   // value 变成 11
counter.decrement();   // value 变成 10
console.log(counter.getValue());  // 10
```

**练习 3** ⭐：用计算属性名创建一个对象，它的键是 `'key_0'` 到 `'key_4'`，值分别是 `0` 到 `4`。

**练习 4** ⭐⭐：用 `Object.assign` 实现一个 `mergeDefaults` 函数，将默认值和用户配置合并：

```js
const defaults = { theme: 'light', lang: 'en', debug: false };
const userConfig = { theme: 'dark' };
mergeDefaults(defaults, userConfig);
// 期望：{ theme: 'dark', lang: 'en', debug: false }
```

---

### 📌 本章要点

1. **属性简写**：`{ name, age }` 等价于 `{ name: name, age: age }`
2. **方法简写**：`{ sayHi() {} }` 等价于 `{ sayHi: function() {} }`
3. **计算属性名**：`[expr]: value`，可以用表达式作为属性名
4. **对象浅拷贝**：`{ ...obj }` 或 `Object.assign({}, obj)`
5. **`Object.is`**：比 `===` 更精确的比较，罕用

---

## 7. 数组增强

> ES6 为数组增加了多个实用方法，让常见操作不再需要借助 `Array.prototype` 的 hack。

### 7.1 Array.from —— 类数组/可迭代对象转数组

```js
// 字符串转数组
Array.from('hello');  // ['h', 'e', 'l', 'l', 'o']

// Set 转数组
Array.from(new Set([1, 2, 3]));  // [1, 2, 3]

// 类数组对象（有 length 和数字键的对象）
const arrayLike = { 0: 'a', 1: 'b', length: 2 };
Array.from(arrayLike);  // ['a', 'b']
```

第二个参数是映射函数：

```js
Array.from([1, 2, 3], x => x * 2);  // [2, 4, 6]

// 等价于
[1, 2, 3].map(x => x * 2);
```

### 7.2 Array.of —— 根据参数创建数组

解决 `new Array()` 的歧义：

```js
Array.of(7);       // [7] ✅
Array.of(1, 2, 3); // [1, 2, 3] ✅

// 对比：
new Array(7);      // [empty × 7]（7 个空位！不是 [7]）
new Array(1, 2, 3); // [1, 2, 3]
```

### 7.3 find / findIndex —— 查找元素

```js
const users = [
  { id: 1, name: 'Alice' },
  { id: 2, name: 'Bob' },
  { id: 3, name: 'Charlie' }
];

// 找到第一个满足条件的元素
users.find(u => u.id === 2);       // { id: 2, name: 'Bob' }
users.find(u => u.id === 999);     // undefined（没找到）

// 找到第一个满足条件的元素的索引
users.findIndex(u => u.id === 2);  // 1
users.findIndex(u => u.id === 999); // -1（没找到）
```

对比 `indexOf`：`indexOf` 只能按值查找（用 `===` 比较），`findIndex` 可以按任意条件查找。

### 7.4 fill —— 填充数组

```js
Array(3).fill(0);           // [0, 0, 0]
[1, 2, 3, 4].fill(0, 1, 3); // [1, 0, 0, 4]（从索引 1 填充到 3，不包括 3）
```

### 7.5 keys / values / entries —— 返回迭代器

```js
const arr = ['a', 'b', 'c'];

[...arr.keys()];     // [0, 1, 2]
[...arr.values()];   // ['a', 'b', 'c']
[...arr.entries()];  // [[0, 'a'], [1, 'b'], [2, 'c']]
```

配合 `for...of` 使用：

```js
for (const [index, value] of arr.entries()) {
  console.log(`${index}: ${value}`);
}
// 0: a
// 1: b
// 2: c
```

### ✏️ 练习

**练习 1** ⭐：用 `Array.from` 生成一个 `[0, 1, 2, 3, 4]` 的数组。

**练习 2** ⭐：从下面的数组中找到第一个分数大于 80 的学生：

```js
const students = [
  { name: 'Alice', score: 72 },
  { name: 'Bob', score: 85 },
  { name: 'Charlie', score: 90 }
];
```

**练习 3** ⭐：创建一个长度为 5 的数组，所有元素初始化为 `'pending'`。

**练习 4** ⭐⭐：实现一个函数 `uniqueByField`，根据指定字段对对象数组去重：

```js
const users = [
  { id: 1, name: 'Alice' },
  { id: 2, name: 'Bob' },
  { id: 1, name: 'Alice' },  // 重复
  { id: 3, name: 'Charlie' }
];
uniqueByField(users, 'id');
// 期望返回：[{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }, { id: 3, name: 'Charlie' }]
```

---

### 📌 本章要点

1. **`Array.from`**：将类数组或可迭代对象转为真正的数组，可带映射函数
2. **`Array.of`**：创建数组，`Array.of(7)` 得到 `[7]`，而 `new Array(7)` 得到 7 个空位
3. **`find / findIndex`**：按条件查找，返回元素或索引；找不到时分别返回 `undefined` 和 `-1`
4. **`fill`**：填充数组，可指定起止位置
5. **`keys / values / entries`**：返回迭代器，配合 `for...of` 或展开运算符使用

---

## 8. 类：Class 语法

> ES6 的 `class` 提供了一种更清晰、更直观的方式来创建对象和处理继承。它本质上是 ES5 构造函数和原型继承的**语法糖**，但大大降低了学习曲线。

### 8.1 从 ES5 构造函数到 Class

ES5 中创建"类"的写法：

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.sayHi = function() {
  return 'Hi, I am ' + this.name;
};

Person.prototype.grow = function() {
  this.age++;
};

var p = new Person('Alice', 25);
p.sayHi();  // "Hi, I am Alice"
```

问题：
- `Person` 到底是普通函数还是构造函数？看代码不直观
- 原型方法分散在 `prototype` 上，和构造函数定义分离
- 继承的写法更加晦涩（`Object.create`、`call` 等）

ES6 Class 写法：

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHi() {
    return `Hi, I am ${this.name}`;
  }

  grow() {
    this.age++;
  }
}

const p = new Person('Alice', 25);
console.log(p.sayHi());  // "Hi, I am Alice"
console.log(typeof Person);  // "function"（Class 本质仍是函数）
```

优点一目了然：
- `constructor` 明确标出构造函数
- 所有方法都写在 `class` 体内部，结构清晰
- 继承语法直观（见下节）

> 💡 **重要认知**：`class` 并没有改变 JavaScript 基于原型的继承本质，它只是让写法更符合直觉。你可以把 `class` 理解为"更好的构造函数语法"。

### 8.2 extends 继承

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} makes a sound.`;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);        // 调用父类的 constructor，必须！
    this.breed = breed; // 然后才能使用 this
  }

  speak() {
    return `${super.speak()} Woof!`;  // super.speak() 调用父类方法
  }
}

const dog = new Dog('Buddy', 'Golden Retriever');
console.log(dog.speak());  // "Buddy makes a sound. Woof!"
console.log(dog instanceof Dog);     // true
console.log(dog instanceof Animal);  // true
```

#### 关于 super 的规则

1. **子类构造函数中，必须先调用 `super()`，然后才能使用 `this`**。
   ```js
   class Cat extends Animal {
     constructor(name) {
       this.name = name;  // ❌ ReferenceError：必须先调用 super()
       super(name);
     }
   }
   ```

2. **如果子类没有定义 constructor，JavaScript 会自动创建一个调用 `super(...args)` 的构造函数**。
   ```js
   class Cat extends Animal {}  // 自动有 constructor(...args) { super(...args); }
   ```

### 8.3 静态方法

静态方法直接挂在类上，而不是实例上：

```js
class MathHelper {
  static add(a, b) {
    return a + b;
  }

  static multiply(a, b) {
    return a * b;
  }
}

MathHelper.add(2, 3);       // 5
MathHelper.multiply(2, 3);  // 6

const helper = new MathHelper();
// helper.add(2, 3);  // ❌ TypeError：实例不能访问静态方法
```

实用场景：工厂方法、工具函数：

```js
class User {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  // 工厂方法：从 JSON 数据创建 User
  static fromJSON(json) {
    return new User(json.name, json.email);
  }
}

const user = User.fromJSON({ name: 'Alice', email: 'alice@test.com' });
```

### 8.4 getter 和 setter

让你可以像访问属性一样调用方法：

```js
class Temperature {
  constructor(celsius) {
    this._celsius = celsius;  // 约定：下划线开头表示"私有"（只是约定，不是真正的私有）
  }

  // getter：像属性一样读取
  get fahrenheit() {
    return this._celsius * 9 / 5 + 32;
  }

  // setter：像属性一样赋值
  set fahrenheit(value) {
    this._celsius = (value - 32) * 5 / 9;
  }

  get celsius() {
    return this._celsius;
  }
}

const temp = new Temperature(0);
console.log(temp.fahrenheit);  // 32（像属性一样访问，不加括号！）
temp.fahrenheit = 212;         // 像属性一样赋值
console.log(temp.celsius);     // 100
```

### 8.5 Class 的重要特性

| 特性 | 说明 |
|------|------|
| 不会提升 | `class` 声明不会像函数声明那样提升，必须先声明后使用 |
| 默认严格模式 | 类体内部自动使用严格模式 |
| 方法不可枚举 | `class` 中定义的方法的 `enumerable` 属性为 `false` |
| 必须用 new | 不用 `new` 调用会报错 |

```js
const p = Person('Alice', 25);  // ❌ TypeError: Class constructor Person cannot be invoked without 'new'
```

### 8.6 ES2022 私有字段（扩展）

从 ES2022 开始，JavaScript 支持真正的私有字段，用 `#` 前缀：

```js
class BankAccount {
  #balance = 0;  // 真正的私有字段，类外部完全访问不到

  deposit(amount) {
    if (amount > 0) this.#balance += amount;
  }

  getBalance() {
    return this.#balance;
  }
}

const account = new BankAccount();
account.deposit(100);
console.log(account.getBalance());  // 100
// console.log(account.#balance);   // ❌ SyntaxError：私有字段不能在类外部访问
// console.log(account._balance);   // undefined（不存在这个属性）
```

> 💡 如果你看到现代代码库中有 `#` 开头的字段，就知道它是真正私有的。旧代码中通常用 `_balance` 这种下划线约定来表示"请不要直接访问"。

### ✏️ 练习

**练习 1** ⭐：创建一个 `Rectangle` 类，有 `width` 和 `height` 属性，以及 `area`（getter）和 `perimeter`（getter）方法。

**练习 2** ⭐：创建一个 `Square` 类继承 `Rectangle`，只需要一个参数 `side`。

**练习 3** ⭐：给 `Rectangle` 添加一个静态方法 `fromJSON`，可以从 `{ width: 10, height: 20 }` 这样的对象创建实例。

**练习 4** ⭐⭐：下面的代码有什么错误？

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    this.breed = breed;
    super(name);
  }
}
```

**练习 5** ⭐⭐：给 `BankAccount` 类添加一个 `transfer(to, amount)` 方法，实现转账功能：

```js
const account1 = new BankAccount(1000);
const account2 = new BankAccount(500);
account1.transfer(account2, 200);
account1.getBalance();  // 800
account2.getBalance();  // 700
```

---

### 📌 本章要点

1. **`class` 是语法糖**：本质上是构造函数 + 原型继承，写法更直观
2. **`constructor` 是构造函数**：用 `new` 调用类时自动执行
3. **继承用 `extends`**：`super()` 调用父类构造函数，必须先调用才能用 `this`
4. **静态方法用 `static`**：直接挂在类上，用 `ClassName.method()` 调用
5. **getter/setter**：用 `get`/`set` 关键字定义，像属性一样访问
6. **ES2022 私有字段 `#field`**：真正的私有，外部无法访问

---

## 9. 模块化

> 模块化是现代 JavaScript 工程化的基石。在 ES6 之前，社区发展出了 CommonJS（Node.js）、AMD（RequireJS）、UMD 等多种模块化方案，碎片化严重。ES6 引入了官方的模块标准：`import` 和 `export`。

### 9.1 为什么需要模块化？

没有模块化的时代，代码是这样组织的：

```html
<script src="utils.js"></script>
<script src="api.js"></script>
<script src="app.js"></script>
```

问题：
- 所有变量都在全局命名空间，容易冲突
- 加载顺序很重要，但 HTML 中不直观
- 无法清晰表达依赖关系
- 无法按需加载

### 9.2 export —— 导出

#### 命名导出（Named Export）

一个模块可以导出多个东西：

```js
// math.js
export const PI = 3.14159;

export function add(a, b) {
  return a + b;
}

export class Calculator {
  multiply(a, b) {
    return a * b;
  }
}

// 也可以在文件末尾统一导出
export { PI, add, Calculator };

// 导出时重命名
const veryLongName = 42;
export { veryLongName as answer };
```

#### 默认导出（Default Export）

每个模块只能有一个默认导出：

```js
// utils.js
export default function greet(name) {
  return `Hello, ${name}!`;
}

// 默认导出可以是任意值：函数、类、对象、常量
const config = { apiUrl: 'https://api.example.com' };
export default config;
```

### 9.3 import —— 导入

```js
// 导入命名导出（用花括号）
import { PI, add, Calculator } from './math.js';

// 导入默认导出（不用花括号）
import greet from './utils.js';

// 同时导入默认和命名导出
import greet, { PI, add } from './combined.js';

// 重命名导入
import { add as plus } from './math.js';
plus(1, 2);  // 3

// 命名空间导入（导入所有导出到一个对象）
import * as math from './math.js';
math.PI;        // 3.14159
math.add(1, 2); // 3

// 仅执行模块（不导入任何绑定）
import './init.js';  // 运行模块的副作用代码
```

> ⚠️ **注意**：在浏览器中，ES Module 需要在 `<script>` 标签上加 `type="module"`：
> ```html
> <script type="module" src="app.js"></script>
> ```
> 在 Node.js 中，`.mjs` 文件或设置 `"type": "module"` 才能使用 ES Module。

### 9.4 ES Module vs CommonJS

| 特性 | ES Module | CommonJS |
|------|-----------|----------|
| 语法 | `import` / `export` | `require()` / `module.exports` |
| 加载时机 | 编译时（静态分析） | 运行时（动态执行） |
| Tree Shaking | ✅ 支持 | ❌ 不支持 |
| 导入的绑定 | 只读的**活绑定** | 值的**拷贝** |
| 动态导入 | `import()` 函数 | `require()` 本来就是动态的 |

#### 活绑定（Live Binding）是什么意思？

```js
// counter.js
export let count = 0;
export function increment() {
  count++;
}

// main.js
import { count, increment } from './counter.js';
console.log(count);  // 0
increment();
console.log(count);  // 1 ✅ 自动更新了！
```

ES Module 导入的不是值的"快照"，而是对导出变量的**实时引用**。

### 9.5 实际项目中的模块化组织

```js
// components/Button.js
export default class Button {
  constructor(text) {
    this.text = text;
  }
  render() {
    return `<button>${this.text}</button>`;
  }
}

// components/index.js —— 统一的出口文件
export { default as Button } from './Button.js';
export { default as Input } from './Input.js';
export { default as Modal } from './Modal.js';

// app.js
import { Button, Input } from './components/index.js';
// 或者更简洁：import { Button, Input } from './components';
```

### ✏️ 练习

**练习 1** ⭐：创建 `math.js`，导出 `add`、`subtract` 两个命名导出，以及 `multiply` 作为默认导出。然后在 `main.js` 中导入并使用它们。

**练习 2** ⭐：下面的导入语句分别导入了什么？

```js
import React, { useState, useEffect } from 'react';
```

**练习 3** ⭐⭐：为什么不能这样写？

```js
if (condition) {
  import { foo } from './module.js';  // ❌
}
```

> 提示：`import` 语句必须是顶层静态的。如果确实需要条件导入，应该用什么？（答案：`import()` 动态导入函数）

**练习 4** ⭐⭐：写出下面导入的等价形式（用命名空间导入）：

```js
import { createElement, Component } from 'react';
```

---

### 📌 本章要点

1. **`export` 命名导出**：每个模块可有多个，`import { name } from 'mod'`
2. **`export default`**：每个模块只能有一个，`import name from 'mod'`
3. **混合导入**：`import defaultExp, { named1, named2 } from 'mod'`
4. **导入是只读的活绑定**：导入的变量和导出方是同一引用
5. **`import()` 是动态导入**：返回 Promise，用于条件加载

---

## 10. 异步编程：Promise

> JavaScript 是单线程的，很多操作（网络请求、定时器、文件读写）都是异步的。ES6 引入的 Promise 是 JavaScript 异步编程的转折点。

### 10.1 回调地狱（Callback Hell）

ES5 中处理多个连续的异步操作：

```js
getUser(userId, function(err, user) {
  if (err) return handleError(err);

  getOrders(user.id, function(err, orders) {
    if (err) return handleError(err);

    getDetails(orders[0].id, function(err, details) {
      if (err) return handleError(err);

      // ... 越来越深的嵌套
      // 代码呈"箭头型"向右延伸，难以阅读和维护
    });
  });
});
```

问题：
- 嵌套层级深，可读性差
- 错误处理要在每个回调里写一遍
- 并行多个异步操作很困难

### 10.2 Promise 基础

Promise 是一个表示**异步操作最终完成或失败**的对象。它有三种状态：

- **Pending**（进行中）：初始状态
- **Fulfilled**（已成功）：操作成功完成
- **Rejected**（已失败）：操作失败

状态一旦从 Pending 变成 Fulfilled 或 Rejected，就**不可再改变**。

```js
const promise = new Promise((resolve, reject) => {
  // 异步操作
  setTimeout(() => {
    const success = Math.random() > 0.5;

    if (success) {
      resolve('操作成功！');  // 状态变为 fulfilled
    } else {
      reject(new Error('操作失败'));  // 状态变为 rejected
    }
  }, 1000);
});

// 使用 Promise
promise
  .then(result => {
    console.log(result);  // 操作成功时执行
  })
  .catch(error => {
    console.error(error);  // 操作失败时执行
  })
  .finally(() => {
    console.log('无论成功失败都执行');
  });
```

### 10.3 Promise 链

Promise 最大的价值在于**链式调用**：

```js
fetchUser(userId)
  .then(user => fetchOrders(user.id))     // then 里返回一个新的 Promise
  .then(orders => fetchDetails(orders[0].id))  // 继续链式调用
  .then(details => console.log(details))   // 处理最终结果
  .catch(err => console.error(err));       // 任何一步出错都会到这里
```

对比回调地狱，代码变成了**纵向的、清晰的流水线**。

#### then 的返回值规则

```js
fetchUser(1)
  .then(user => {
    // 1. 返回一个值：会被包装成 resolved 的 Promise
    return user.name;
  })
  .then(name => {
    // name === "Alice"
    // 2. 返回一个 Promise：会等待这个 Promise 完成
    return fetchOrders(name);
  })
  .then(orders => {
    // orders 是 fetchOrders 的结果
    // 3. 抛出错误：会变成 rejected 的 Promise
    if (orders.length === 0) throw new Error('No orders');
    return orders;
  })
  .catch(err => {
    // 捕获上面的错误
  });
```

### 10.4 Promise 静态方法

#### Promise.resolve / Promise.reject

快速创建已完成的 Promise：

```js
Promise.resolve(42).then(v => console.log(v));  // 42
Promise.reject(new Error('bad')).catch(e => console.error(e));
```

#### Promise.all —— 等待所有完成

```js
const p1 = fetch('/api/users');
const p2 = fetch('/api/posts');
const p3 = fetch('/api/comments');

Promise.all([p1, p2, p3])
  .then(([usersRes, postsRes, commentsRes]) => {
    // 三个请求都成功完成
  })
  .catch(err => {
    // 任何一个失败，立即进入 catch
  });
```

> ⚠️ `Promise.all` 是"一损俱损"的：只要有一个失败，整个就失败。

#### Promise.race —— 谁先完成用谁

```js
const fetchData = fetch('/api/data');
const timeout = new Promise((_, reject) =>
  setTimeout(() => reject(new Error('请求超时')), 5000)
);

Promise.race([fetchData, timeout])
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));
// 如果 5 秒内 fetch 没完成，就会触发超时错误
```

#### Promise.allSettled（ES2020）—— 等待全部完成，不中断

```js
Promise.allSettled([p1, p2, p3]).then(results => {
  results.forEach(r => {
    if (r.status === 'fulfilled') {
      console.log('成功:', r.value);
    } else {
      console.log('失败:', r.reason);
    }
  });
});
// 即使 p2 失败了，p1 和 p3 的结果仍然能拿到
```

### 10.5 把回调 API 包装成 Promise

很多旧 API 还是回调形式的，可以用 `Promise` 包装：

```js
// 把 setTimeout 包装成 Promise
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

delay(1000).then(() => console.log('1 秒后执行'));

// 把 Node.js 的 fs.readFile 包装成 Promise
const fs = require('fs');
function readFile(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}
```

### ✏️ 练习

**练习 1** ⭐：创建一个 `delay(ms)` 函数，返回一个 Promise，在 `ms` 毫秒后 resolve。

**练习 2** ⭐：用 `Promise.all` 并行加载两个数据：

```js
const fetchUser = id => fetch(`/api/users/${id}`).then(r => r.json());
const fetchPosts = () => fetch('/api/posts').then(r => r.json());
// 并行加载用户和文章，等两者都完成后再打印
```

**练习 3** ⭐⭐：下面的代码会输出什么？顺序是什么？

```js
Promise.resolve()
  .then(() => console.log(1))
  .then(() => console.log(2));

Promise.resolve()
  .then(() => console.log(3))
  .then(() => console.log(4));
```

**练习 4** ⭐⭐：用 `Promise.race` 实现一个带超时的 fetch：

```js
function fetchWithTimeout(url, timeoutMs) {
  // 如果 fetch 超过 timeoutMs 毫秒未完成，抛出超时错误
}
```

---

### 📌 本章要点

1. **Promise 三种状态**：pending（进行中）、fulfilled（成功）、rejected（失败）
2. **状态不可逆**：一旦从 pending 变成 fulfilled 或 rejected，就不能再改变
3. **`then` 返回新 Promise**：可以链式调用
4. **`catch` 捕获错误**：任何一步出错都会跳到最近的 `catch`
5. **`Promise.all`**：全部成功才成功，一个失败就失败
6. **`Promise.race`**：谁先完成用谁
7. **`Promise.allSettled`**：等全部完成，无论成功失败

---

## 11. async/await

> `async/await` 是 ES2017（ES8）引入的语法，它让异步代码看起来像同步代码。它**不是替代 Promise**，而是建立在 Promise 之上的语法糖。

### 11.1 从 Promise 到 async/await

Promise 链已经比回调好了，但仍有嵌套感：

```js
fetchUser(1)
  .then(user => fetchOrders(user.id))
  .then(orders => {
    console.log(orders);
    return orders[0];
  })
  .catch(err => console.error(err));
```

用 async/await：

```js
async function loadUserData(userId) {
  try {
    const user = await fetchUser(userId);
    const orders = await fetchOrders(user.id);
    console.log(orders);
    return orders[0];
  } catch (err) {
    console.error(err);
  }
}
```

看起来就像普通的同步代码！但注意：
- `await` 只能出现在 `async` 函数内部
- `await` 后面跟着一个 Promise
- `async` 函数**总是返回一个 Promise**

### 11.2 async 函数的本质

```js
async function foo() {
  return 'hello';
}

// 等价于
function foo() {
  return Promise.resolve('hello');
}

foo().then(v => console.log(v));  // "hello"
```

如果 `async` 函数里抛出错误：

```js
async function bar() {
  throw new Error('oops');
}

// 等价于返回 rejected 的 Promise
bar().catch(e => console.error(e));  // Error: oops
```

### 11.3 await 的行为

```js
const result = await somePromise;
```

- 如果 `somePromise` 成功（resolved），`await` 返回它的值
- 如果 `somePromise` 失败（rejected），`await` 会抛出错误（可以用 try/catch 捕获）

```js
async function fetchData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('获取数据失败:', error);
    return null;  // 提供一个默认值
  }
}
```

### 11.4 并行 vs 串行

初学者常犯的错误：把可以并行的操作写成串行：

```js
// ❌ 串行：总耗时 = 3s + 2s = 5s
async function loadSlow() {
  const users = await fetch('/api/users');      // 3 秒
  const posts = await fetch('/api/posts');      // 2 秒
  return { users, posts };
}

// ✅ 并行：总耗时 = max(3s, 2s) = 3s
async function loadFast() {
  const [users, posts] = await Promise.all([
    fetch('/api/users'),   // 同时开始
    fetch('/api/posts')    // 同时开始
  ]);
  return { users, posts };
}
```

**判断标准**：如果后面的 `await` **不依赖**前面 `await` 的结果，就应该并行。

### 11.5 常见陷阱

#### 陷阱 1：forEach 里不能用 async/await

```js
const ids = [1, 2, 3];

// ❌ 错误：forEach 不会等待异步操作完成
ids.forEach(async (id) => {
  const user = await fetchUser(id);
  console.log(user);
});
console.log('这里会在请求完成前打印！');

// ✅ 正确：用 for...of 实现串行
async function processUsers(ids) {
  for (const id of ids) {
    const user = await fetchUser(id);
    console.log(user);
  }
  console.log('所有用户处理完毕');
}

// ✅ 正确：用 map + Promise.all 实现并行
async function processUsersParallel(ids) {
  const users = await Promise.all(ids.map(id => fetchUser(id)));
  console.log(users);
}
```

#### 陷阱 2：忘记加 await

```js
async function getData() {
  const response = fetch('/api/data');  // ❌ 忘记 await！
  const data = response.json();         // 这里 response 还是 Promise
  return data;
}
```

#### 陷阱 3：try/catch 范围过大

```js
// ❌ 如果 fetchOrders 失败，会误以为是 fetchUser 的问题
async function load() {
  try {
    const user = await fetchUser(1);
    const orders = await fetchOrders(user.id);
    const details = await fetchDetails(orders[0].id);
    return details;
  } catch (e) {
    // 不知道哪一步出的错
    console.error(e);
  }
}

// ✅ 更精细的错误处理
async function load() {
  let user;
  try {
    user = await fetchUser(1);
  } catch (e) {
    console.error('获取用户失败:', e);
    return null;
  }

  try {
    const orders = await fetchOrders(user.id);
    return await fetchDetails(orders[0].id);
  } catch (e) {
    console.error('获取订单或详情失败:', e);
    return null;
  }
}
```

### ✏️ 练习

**练习 1** ⭐：把下面的 Promise 链改写成 async/await：

```js
fetchUser(1)
  .then(user => fetchOrders(user.id))
  .then(orders => console.log(orders))
  .catch(err => console.error(err));
```

**练习 2** ⭐：写一个 `getJSON(url)` 函数，用 async/await 封装 `fetch`：

```js
const data = await getJSON('https://api.example.com/users');
```

**练习 3** ⭐⭐：并行获取多个 URL 的数据：

```js
const urls = [
  'https://api.example.com/users',
  'https://api.example.com/posts',
  'https://api.example.com/comments'
];
// 并行获取，等全部完成后返回数组
```

**练习 4** ⭐⭐：写一个 `retry(fn, times)` 函数，失败时重试指定次数：

```js
async function fetchWithRetry() {
  const data = await retry(() => fetch('/api/data').then(r => r.json()), 3);
  return data;
}
```

**练习 5** ⭐⭐⭐：实现一个 `asyncPool(concurrency, tasks)` 函数，限制并发数：

```js
// 同时最多只有 2 个任务在执行
const results = await asyncPool(2, [
  () => fetch('/api/1'),
  () => fetch('/api/2'),
  () => fetch('/api/3'),
  () => fetch('/api/4')
]);
```

---

### 📌 本章要点

1. **`async` 函数总是返回 Promise**：即使你返回普通值，它也会被包装成 Promise
2. **`await` 等待 Promise 完成**：暂停 async 函数执行，等待 Promise resolve/reject
3. **并行用 `Promise.all`**：不依赖的 await 应该并行，而不是串行
4. **避免 forEach + async**：forEach 不会等待 async 回调，用 for...of 或 Promise.all
5. **错误处理**：用 try/catch，可以精确定位哪一步出错

---

## 12. 新的数据结构

> ES6 引入了两个重要的新数据结构：`Set` 和 `Map`。它们弥补了传统 `Object` 和 `Array` 在某些场景下的不足。

### 12.1 Set —— 值的集合，自动去重

`Set` 是一种值的集合，其中**每个值只能出现一次**。

```js
// 创建
const set = new Set([1, 2, 2, 3, 3, 3]);
console.log(set);  // Set { 1, 2, 3 }

// 基本操作
set.add(4);        // 添加
set.has(2);        // true —— 判断是否存在
set.delete(3);     // true —— 删除成功
set.size;          // 3 —— 元素个数（不是 length！）
set.clear();       // 清空
```

遍历：

```js
const fruits = new Set(['apple', 'banana', 'orange']);

for (const fruit of fruits) {
  console.log(fruit);
}

fruits.forEach(fruit => console.log(fruit));
```

#### 最实用场景：数组去重

```js
const arr = [1, 2, 2, 3, 3, 3, 4];
const unique = [...new Set(arr)];  // [1, 2, 3, 4]

// 对象数组按某字段去重？Set 帮不上忙，需要配合 filter
```

> 💡 `Set` 判断重复使用的是 **SameValueZero** 算法（与 `===` 类似，但 `NaN` 被视为等于自身）。因此 `new Set([NaN, NaN])` 只会保留一个 `NaN`，`new Set([+0, -0])` 也只会保留一个值。

### 12.2 Map —— 键可以是任意类型的字典

传统 `Object` 的键只能是字符串或 `Symbol`。`Map` 的键**可以是任意类型**：对象、函数、甚至是另一个 Map。

```js
// 创建
const map = new Map([
  ['name', 'Alice'],
  ['age', 25]
]);

// 基本操作
map.set('email', 'alice@test.com');
map.get('name');         // "Alice"
map.has('age');          // true
map.delete('age');
map.size;                // 2
map.clear();
```

#### 任意类型的键

```js
const map = new Map();

const objKey = { id: 1 };
const funcKey = function() {};

map.set(objKey, '用对象做键');
map.set(funcKey, '用函数做键');
map.set(123, '用数字做键');  // Object 会把数字转成字符串 "123"

console.log(map.get(objKey));   // "用对象做键"
console.log(map.get(funcKey));  // "用函数做键"
```

这在需要给对象附加元数据，但又不想污染对象本身时非常有用。

#### 遍历

```js
const map = new Map([['a', 1], ['b', 2], ['c', 3]]);

// for...of（Map 默认迭代的是 [key, value]）
for (const [key, value] of map) {
  console.log(`${key} => ${value}`);
}

// forEach（注意参数顺序是 value, key）
map.forEach((value, key) => {
  console.log(`${key} => ${value}`);
});
```

#### Map vs Object

| 特性 | Map | Object |
|------|-----|--------|
| 键的类型 | 任意类型 | 字符串 / Symbol |
| 键的顺序 | 保持插入顺序 | 不保证（虽然现代引擎通常保持） |
| 大小 | `.size` 属性 | 需要手动计算 `Object.keys(obj).length` |
| 性能（频繁增删） | 更好 | 较差 |
| 序列化 | 不支持直接 JSON.stringify | 原生支持 |
| 默认键 | 无 | 有原型链上的键（toString 等） |

### 12.3 WeakMap / WeakSet —— 了解即可

"Weak" 的含义是它们对对象的引用是**弱引用**，不会阻止垃圾回收。

```js
// WeakMap —— 键必须是对象
let user = { name: 'Alice' };
const wm = new WeakMap();
wm.set(user, { lastVisit: Date.now() });

// 当 user 不再被其他地方引用时，垃圾回收器可以回收它
// WeakMap 中对应的条目也会自动消失
user = null;  // wm 中的条目会被 GC 回收
```

`WeakMap` 不可遍历（没有 `size`、`forEach`、`keys` 等方法），只有 `set`、`get`、`has`、`delete`。

**典型场景**：存储对象的私有数据、缓存计算结果（避免内存泄漏）。

```js
// 用 WeakMap 实现私有数据
const privateData = new WeakMap();

class User {
  constructor(name) {
    privateData.set(this, { password: 'secret' });
    this.name = name;
  }

  getPassword() {
    return privateData.get(this).password;
  }
}

// User 实例被销毁后，对应的 privateData 条目会自动被清理
```

### ✏️ 练习

**练习 1** ⭐：用 `Set` 给下面的数组去重：

```js
const nums = [1, 2, 2, 3, 4, 4, 4, 5];
```

**练习 2** ⭐：创建一个 `Map`，用 DOM 元素作为键，存储每个元素的点击次数：

```js
const button1 = document.getElementById('btn1');
const button2 = document.getElementById('btn2');
// ...
```

**练习 3** ⭐：`Map` 和 `Object` 各适合什么场景？各举一个例子。

**练习 4** ⭐⭐：用 `Map` 实现一个简单的缓存函数：

```js
function cached(fn) {
  // 缓存相同参数的计算结果
}

const slowSquare = cached(n => {
  console.log('computing...');
  return n * n;
});
slowSquare(5);  // 计算，打印 "computing..."
slowSquare(5);  // 使用缓存，不打印
slowSquare(6);  // 计算，打印 "computing..."
```

---

### 📌 本章要点

1. **`Set` 自动去重**：用 `===` 比较（`NaN` 也只保留一个）
2. **`Set` 操作**：`add`、`has`、`delete`、`clear`；用 `for...of` 或 `forEach` 遍历
3. **`Map` 键可以是任意类型**：对象、函数、数字都可以
4. **`Map` 有 `.size`**：直接获取元素个数，比 `Object.keys().length` 方便
5. **`WeakMap/WeakSet`**：弱引用，不阻止垃圾回收；键必须是对象；不可遍历

---

## 13. Symbol

> `Symbol` 是 ES6 引入的一种**新的原始数据类型**（和 `string`、`number`、`boolean` 等同级）。它的主要目的是创建**唯一的、不会冲突的属性键**。

### 13.1 为什么需要 Symbol？

想象你在开发一个库，需要在用户传入的对象上附加一些内部属性：

```js
// 你的库代码
function myLibrary(obj) {
  obj._internal_id = Math.random();  // 用了 _internal_id 这个名字
  // ...
}

// 用户代码
var data = {
  name: 'Alice',
  _internal_id: 'user-defined'  // 哎呀，冲突了！
};

myLibrary(data);
console.log(data._internal_id);  // 变成了你库里的随机数，用户的值被覆盖了！
```

即使你用很奇怪的名字，理论上还是有冲突的可能。`Symbol` 彻底解决了这个问题。

### 13.2 创建 Symbol

```js
const s1 = Symbol('description');
const s2 = Symbol('description');

console.log(s1 === s2);  // false —— 即使描述相同，Symbol 也是唯一的！
```

`Symbol('description')` 中的字符串只是描述（description），用于调试，不影响唯一性。

### 13.3 作为对象属性键

```js
const METADATA = Symbol('metadata');

const obj = {
  name: 'data',
  [METADATA]: { version: 2, author: 'Alice' }
};

console.log(obj[METADATA]);  // { version: 2, author: 'Alice' }

// Symbol 属性不会被常规遍历访问到
console.log(Object.keys(obj));              // ['name']
console.log(JSON.stringify(obj));           // '{"name":"data"}' —— Symbol 属性被忽略！

// 获取 Symbol 属性的方法
console.log(Object.getOwnPropertySymbols(obj));  // [Symbol(metadata)]
console.log(Reflect.ownKeys(obj));               // ['name', Symbol(metadata)]
```

### 13.4 全局 Symbol 注册表

如果你需要在不同地方获取**同一个** Symbol，可以用全局注册表：

```js
const gs1 = Symbol.for('app.id');
const gs2 = Symbol.for('app.id');
console.log(gs1 === gs2);  // true

Symbol.keyFor(gs1);  // "app.id"

const local = Symbol('local');
console.log(Symbol.keyFor(local));  // undefined（不在全局注册表中）
```

### 13.5 Well-Known Symbols —— 了解即可

JavaScript 内置了一些 Symbol，用来定制对象在特定语言操作中的行为：

| Symbol | 作用 |
|--------|------|
| `Symbol.iterator` | 定义对象的默认迭代器（`for...of` 使用） |
| `Symbol.toStringTag` | 定制 `Object.prototype.toString.call()` 的返回 |
| `Symbol.toPrimitive` | 定制对象转原始值的行为 |

```js
// Symbol.toStringTag
class MyCollection {
  get [Symbol.toStringTag]() {
    return 'MyCollection';
  }
}
console.log(Object.prototype.toString.call(new MyCollection()));
// "[object MyCollection]"
```

> 初学者不需要深入这些。只要知道 Symbol 的存在，以及它是用来创建唯一属性键的即可。

### ✏️ 练习

**练习 1** ⭐：创建两个 Symbol，证明它们即使描述相同也不相等。

**练习 2** ⭐：用 Symbol 给对象添加一个"隐藏"属性，验证它不会出现在 `for...in` 和 `Object.keys()` 中。

**练习 3** ⭐⭐：用 `Symbol.for` 在不同地方获取同一个 Symbol：

```js
// 在 module1.js 中
const KEY = Symbol.for('app.key');

// 在 module2.js 中
const KEY = Symbol.for('app.key');

// 验证它们是同一个 Symbol
```

---

### 📌 本章要点

1. **Symbol 是唯一标识**：每次 `Symbol()` 都创建新的 Symbol，即使描述相同也不相等
2. **Symbol 作为属性键**：`obj[symbolKey]`，不会被 `Object.keys()`、`for...in`、`JSON.stringify()` 访问
3. **`Symbol.for`**：全局注册表，同一 key 创建相同的 Symbol
4. **Well-Known Symbols**：`Symbol.iterator`、`Symbol.toStringTag` 等，定制语言内部行为

---

## 14. 迭代与遍历

> ES6 引入了**迭代协议**（Iterable Protocol），让遍历数据的方式更加统一和强大。配合 `for...of`，你可以用同一种方式遍历数组、字符串、Map、Set 等。

### 14.1 for...of —— 遍历值的循环

先回顾一下 `for...in` 的问题：

```js
const arr = ['a', 'b', 'c'];
arr.customProp = 'hello';

for (const key in arr) {
  console.log(key);  // "0", "1", "2", "customProp"
  // 遍历的是属性名（包括自定义属性），不是值！
}
```

`for...of` 遍历的是**值**，而且只遍历可迭代对象的元素：

```js
for (const value of arr) {
  console.log(value);  // "a", "b", "c"（不会遍历到 customProp）
}
```

### 14.2 内置可迭代对象

以下内置对象都实现了迭代协议，可以直接用 `for...of`：

```js
// Array
for (const item of [10, 20, 30]) { /* ... */ }

// String
for (const char of 'hello') { /* ... */ }

// Map
for (const [key, value] of new Map([['a', 1]])) { /* ... */ }

// Set
for (const value of new Set([1, 2, 3])) { /* ... */ }

// arguments（函数内部的类数组对象）
function test() {
  for (const arg of arguments) { /* ... */ }
}

// NodeList（DOM 查询结果）
for (const node of document.querySelectorAll('div')) { /* ... */ }
```

### 14.3 迭代器协议 —— 了解原理

一个对象要成为**可迭代**的，必须实现 `[Symbol.iterator]` 方法，该方法返回一个**迭代器**（iterator）。迭代器是一个有 `next()` 方法的对象，每次调用返回 `{ value, done }`。

```js
const str = 'hello';
const iterator = str[Symbol.iterator]();

console.log(iterator.next());  // { value: 'h', done: false }
console.log(iterator.next());  // { value: 'e', done: false }
// ...
console.log(iterator.next());  // { value: undefined, done: true }
```

> 💡 **日常开发中，你几乎不需要手动操作迭代器**。理解 `for...of` 背后是这样工作的就够了。

### 14.4 自定义可迭代对象（进阶）

```js
const range = {
  from: 1,
  to: 5,
  [Symbol.iterator]() {
    let current = this.from;
    const last = this.to;
    return {
      next() {
        return current <= last
          ? { value: current++, done: false }
          : { done: true };
      }
    };
  }
};

for (const n of range) {
  console.log(n);  // 1, 2, 3, 4, 5
}
```

### 14.5 展开运算符与可迭代对象

展开运算符 `...` 只能用于**可迭代对象**：

```js
const chars = [ ...'hello' ];     // ['h', 'e', 'l', 'l', 'o']
const nums = [ ...new Set([1,2,3]) ];  // [1, 2, 3]

// 普通对象不是可迭代的！
// const obj = { a: 1, b: 2 };
// const arr = [ ...obj ];  // ❌ TypeError
```

对象展开 `{...obj}` 是 ES2018 的特性，它不是基于迭代协议，而是基于 `Object.keys()` 的枚举。

### ✏️ 练习

**练习 1** ⭐：用 `for...of` 遍历字符串 `"JavaScript"`，打印每个字符。

**练习 2** ⭐：用解构和 `for...of` 遍历 Map：

```js
const map = new Map([['a', 1], ['b', 2], ['c', 3]]);
// 期望输出：
// a => 1
// b => 2
// c => 3
```

**练习 3** ⭐：`for...in` 和 `for...of` 有什么区别？分别适合遍历什么？

**练习 4** ⭐⭐：实现一个生成随机 ID 的可迭代对象：

```js
const idGenerator = {
  [Symbol.iterator]: function*() {
    // 生成 5 个随机 ID 后停止
  }
};

for (const id of idGenerator) {
  console.log(id);  // 5 个随机字符串
}
```

---

### 📌 本章要点

1. **`for...of` 遍历值**，`for...in` 遍历键
2. **可迭代对象**：实现了 `[Symbol.iterator]()`，返回迭代器
3. **迭代器**：`next()` 方法返回 `{ value, done }`
4. **内置可迭代对象**：Array、String、Map、Set、NodeList 等
5. **展开运算符 `...`**：可用于任何可迭代对象

---

## 15. 生成器 Generator（进阶）

> 生成器是一种**可以暂停和恢复执行**的特殊函数。初学者可以先了解概念，遇到具体场景（如惰性序列、流程控制）时再深入学习。

### 15.1 基本语法

生成器函数用 `function*`（注意星号位置）声明，内部用 `yield` 暂停：

```js
function* simpleGenerator() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = simpleGenerator();

console.log(gen.next());  // { value: 1, done: false }
console.log(gen.next());  // { value: 2, done: false }
console.log(gen.next());  // { value: 3, done: false }
console.log(gen.next());  // { value: undefined, done: true }
```

生成器返回的对象既是迭代器，也是可迭代对象：

```js
for (const n of simpleGenerator()) {
  console.log(n);  // 1, 2, 3
}
```

### 15.2 双向通信

通过 `next(value)` 可以向生成器内部传递数据：

```js
function* twoWay() {
  const a = yield '给我一个值';
  console.log('收到:', a);
  const b = yield '再给我一个值';
  console.log('收到:', b);
  return '完成';
}

const gen = twoWay();
console.log(gen.next().value);        // "给我一个值"
console.log(gen.next('AAA').value);   // "收到: AAA" → "再给我一个值"
console.log(gen.next('BBB'));         // "收到: BBB" → { value: "完成", done: true }
```

### 15.3 实用场景

#### 场景 1：无限序列（惰性求值）

```js
function* idGenerator() {
  let id = 1;
  while (true) {
    yield id++;
  }
}

const ids = idGenerator();
console.log(ids.next().value);  // 1
console.log(ids.next().value);  // 2
console.log(ids.next().value);  // 3
// 不会死循环，因为 yield 会暂停
```

#### 场景 2：遍历树结构

```js
function* traverse(node) {
  yield node.value;
  for (const child of node.children) {
    yield* traverse(child);  // yield* 委托给另一个生成器
  }
}

const tree = {
  value: 'A',
  children: [
    { value: 'B', children: [{ value: 'D', children: [] }] },
    { value: 'C', children: [] }
  ]
};

for (const val of traverse(tree)) {
  console.log(val);  // A, B, D, C
}
```

> 💡 生成器是实现 `async/await` 的底层基础之一。`async/await` 本质上就是"生成器 + Promise"的语法糖。

### ✏️ 练习

**练习 1** ⭐：写一个生成器 `range(start, end)`，生成从 `start` 到 `end` 的整数序列。

**练习 2** ⭐：写一个生成器 `fibonacci()`，生成无限斐波那契数列，然后取前 10 个值。

**练习 3** ⭐⭐：用 `yield*` 实现一个生成器委托：

```js
function* gen1() {
  yield 1;
  yield 2;
}

function* gen2() {
  yield* gen1();  // 委托
  yield 3;
}
// 遍历 gen2() 应该得到 1, 2, 3
```

---

### 📌 本章要点

1. **生成器用 `function*` 声明**，内部用 `yield` 暂停执行
2. **`next()` 返回 `{ value, done }`**：调用时恢复执行
3. **生成器是迭代器**：可以直接用 `for...of` 遍历
4. **`yield*` 委托**：将迭代委托给另一个生成器
5. **惰性求值**：只在调用 `next()` 时计算，适合无限序列

---

## 16. Proxy & Reflect（进阶）

> Proxy 可以拦截对象的基本操作（如读取属性、设置属性、删除属性等），让你自定义对象的行为。这是 JavaScript 元编程（metaprogramming）的重要工具。

### 16.1 Proxy 基础

```js
const target = { name: 'Alice', age: 25 };

const proxy = new Proxy(target, {
  // 拦截属性读取
  get(target, prop, receiver) {
    if (prop in target) {
      return target[prop];
    }
    return `属性 ${String(prop)} 不存在`;
  },

  // 拦截属性设置
  set(target, prop, value, receiver) {
    if (prop === 'age' && typeof value !== 'number') {
      throw new TypeError('age 必须是数字');
    }
    target[prop] = value;
    return true;  // 必须返回 true 表示成功
  }
});

console.log(proxy.name);    // "Alice"
console.log(proxy.email);   // "属性 email 不存在"
proxy.age = 30;             // OK
// proxy.age = 'hello';     // TypeError: age 必须是数字
```

### 16.2 常用 Trap

| Trap | 拦截的操作 |
|------|-----------|
| `get` | 读取属性 `obj.prop` |
| `set` | 设置属性 `obj.prop = value` |
| `has` | `prop in obj` |
| `deleteProperty` | `delete obj.prop` |
| `ownKeys` | `Object.keys()`、`for...in` 等 |

### 16.3 Reflect API

`Reflect` 是一个内置对象，提供与 Proxy trap 一一对应的方法，用于执行对象的"默认操作"。

```js
const obj = { name: 'Alice' };

// 传统方式 vs Reflect
obj.hasOwnProperty('name');   // true（只检查自有属性）
Reflect.has(obj, 'name');     // true（检查自身及原型链，等价于 `in` 操作符）

// Reflect 的真正价值：配合 Proxy 实现默认行为
const logged = new Proxy(obj, {
  get(target, prop, receiver) {
    console.log(`读取: ${String(prop)}`);
    return Reflect.get(target, prop, receiver);  // 执行默认读取
  },
  set(target, prop, value, receiver) {
    console.log(`设置: ${String(prop)} = ${value}`);
    return Reflect.set(target, prop, value, receiver);  // 执行默认设置
  }
});
```

### 16.4 实用案例

#### 响应式数据（Vue 3 的核心机制）

```js
function reactive(target) {
  return new Proxy(target, {
    get(target, prop, receiver) {
      // track(target, prop);  // 依赖收集
      return Reflect.get(target, prop, receiver);
    },
    set(target, prop, value, receiver) {
      const oldValue = target[prop];
      const result = Reflect.set(target, prop, value, receiver);
      if (oldValue !== value) {
        // trigger(target, prop);  // 触发更新
      }
      return result;
    }
  });
}

const state = reactive({ count: 0 });
state.count++;  // 自动触发更新
```

#### 防御性对象（防止意外修改）

```js
function protect(obj) {
  return new Proxy(obj, {
    set(target, prop, value) {
      if (!(prop in target)) {
        throw new Error(`不允许添加新属性: ${String(prop)}`);
      }
      return Reflect.set(target, prop, value);
    },
    deleteProperty(target, prop) {
      throw new Error(`不允许删除属性: ${String(prop)}`);
    }
  });
}

const config = protect({ apiUrl: 'https://...' });
config.apiUrl = 'new url';     // ✅ OK
// config.timeout = 5000;      // ❌ Error: 不允许添加新属性
// delete config.apiUrl;       // ❌ Error: 不允许删除属性
```

> 初学者了解 Proxy 能做什么即可。实际项目中直接使用 Proxy 的场景不多，更多的是在框架内部（如 Vue 3）接触它。

### ✏️ 练习

**练习 1** ⭐：用 Proxy 创建一个对象，访问任何不存在的属性时返回 `0`（而不是 `undefined`）。

**练习 2** ⭐⭐：用 Proxy 实现一个简单的验证：对象的 `age` 属性只能设置为正整数。

**练习 3** ⭐⭐⭐：用 Proxy 实现一个只读的数组（禁止添加、删除、修改元素）：

```js
const readOnlyArr = readonlyArray([1, 2, 3]);
readOnlyArr.push(4);     // ❌ 抛出错误
readOnlyArr[0] = 10;     // ❌ 抛出错误
delete readOnlyArr[0];   // ❌ 抛出错误
readOnlyArr.length = 0;  // ❌ 抛出错误
```

---

### 📌 本章要点

1. **Proxy 拦截操作**：`new Proxy(target, handler)`，handler 定义各种 trap
2. **常用 Trap**：`get`、`set`、`has`、`deleteProperty`、`ownKeys`
3. **Reflect 是默认行为**：配合 Proxy 使用，执行"正常"操作
4. **Proxy 用途**：Vue 3 响应式、数据验证、只读对象等

---

## 综合练习：实战一个小项目

> 本章综合运用前面学到的 ES6 特性，实现一个简单的用户数据管理模块。建议先自己尝试，遇到困难再看提示。

### 项目：用户管理模块

**需求**：
1. 获取用户列表（模拟 API 调用）
2. 根据 ID 获取单个用户
3. 创建新用户
4. 更新用户信息
5. 删除用户
6. 用户数据缓存（相同请求不重复获取）

**技术要求**：使用 `class`、`async/await`、`解构`、`箭头函数`、`Set`、`Map`、`模板字符串` 等 ES6 特性。

---

### 第一步：定义用户类和存储

```js
class UserManager {
  constructor() {
    this._users = new Map();  // 缓存用户数据
    this._cache = new Map();  // 记录正在请求中的 Promise（防止重复请求）
  }

  // ... 实现下面的方法
}
```

> 💡 `_cache` 用 `Map` 而不是 `Set` 存储 Promise，这样可以存储"请求中的 Promise"，方便在后续请求到来时直接返回同一个 Promise。

---

### 第二步：实现 fetchUsers（获取用户列表）

```js
// 模拟 API 调用，返回 Promise
async fetchUsers() {
  // 用 setTimeout 模拟 1 秒延迟
  // 返回模拟数据：[ { id: 1, name: 'Alice', email: 'alice@test.com' }, ... ]
}
```

**提示**：使用 `delay` 包装 setTimeout，结合 `Array.from` 生成模拟数据。

<details>
<summary>点击查看参考实现</summary>

```js
async fetchUsers() {
  await this._delay(1000);
  const users = [
    { id: 1, name: 'Alice', email: 'alice@test.com' },
    { id: 2, name: 'Bob', email: 'bob@test.com' },
    { id: 3, name: 'Charlie', email: 'charlie@test.com' }
  ];
  // 同时缓存到 _users，确保 createUser 的 ID 计算正确
  users.forEach(u => this._users.set(u.id, u));
  return users;
}

_delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

</details>

---

### 第三步：实现 fetchUser（根据 ID 获取单个用户，带缓存）

**要求**：
- 如果用户已在缓存中，直接返回
- 如果正在请求中（防止重复请求），等待当前请求完成
- 如果缓存和请求中都没有，从 API 获取

```js
async fetchUser(id) {
  // 1. 检查 _users 缓存
  // 2. 检查 _cache 是否正在请求
  // 3. 如果都没，开始请求并加入 _cache
  // 4. 请求完成后更新缓存并从 _cache 移除
}
```

**提示**：可以用 `_cache` 存储 `正在请求的 Promise`，而不是简单的 Set。

<details>
<summary>点击查看参考实现</summary>

```js
async fetchUser(id) {
  // 1. 如果已缓存，直接返回
  if (this._users.has(id)) {
    console.log(`[缓存] 获取用户 ${id}`);
    return this._users.get(id);
  }

  // 2. 如果正在请求中，等待它完成
  if (this._cache.has(id)) {
    console.log(`[等待] 等待用户 ${id} 请求完成`);
    return this._cache.get(id);
  }

  // 3. 开始新请求
  console.log(`[API] 获取用户 ${id}`);
  const promise = this._fetchUserFromAPI(id);
  this._cache.set(id, promise);

  try {
    const user = await promise;
    this._users.set(id, user);
    return user;
  } finally {
    this._cache.delete(id);
  }
}

async _fetchUserFromAPI(id) {
  await this._delay(1000);
  const users = await this.fetchUsers();
  const user = users.find(u => u.id === id);
  if (!user) throw new Error(`用户 ${id} 不存在`);
  return user;
}
```

</details>

---

### 第四步：实现 createUser（创建用户）

**要求**：使用参数解构 + 默认值

```js
createUser({ name, email, age = 18 } = {}) {
  // 生成新 ID（比现有最大 ID 大 1）
  // 返回新用户对象
}
```

<details>
<summary>点击查看参考实现</summary>

```js
createUser({ name, email, age = 18 } = {}) {
  if (!name || !email) {
    throw new Error('name 和 email 是必填项');
  }

  const existingIds = [...this._users.values()].map(u => u.id);
  const maxId = existingIds.length > 0 ? Math.max(...existingIds) : 0;

  const newUser = {
    id: maxId + 1,
    name,
    email,
    age,
    createdAt: new Date().toISOString()
  };

  this._users.set(newUser.id, newUser);
  return newUser;
}
```

</details>

---

### 第五步：实现 updateUser（更新用户）

**要求**：使用解构赋值提取要更新的字段

```js
updateUser(id, updates) {
  // 查找用户，不存在则抛出错误
  // 合并更新（只更新提供的字段）
  // 返回更新后的用户
}
```

<details>
<summary>点击查看参考实现</summary>

```js
updateUser(id, updates) {
  const user = this._users.get(id);
  if (!user) {
    throw new Error(`用户 ${id} 不存在`);
  }

  // 解构 + 剩余属性
  const { name, email, age, ...rest } = updates;

  // 合并更新（只更新提供的字段）
  const updatedUser = {
    ...user,
    ...(name && { name }),
    ...(email && { email }),
    ...(age !== undefined && { age }),
    updatedAt: new Date().toISOString()
  };

  this._users.set(id, updatedUser);
  return updatedUser;
}
```

</details>

---

### 第六步：实现 deleteUser（删除用户）

```js
deleteUser(id) {
  // 删除成功返回 true，用户不存在返回 false
}
```

<details>
<summary>点击查看参考实现</summary>

```js
deleteUser(id) {
  if (!this._users.has(id)) {
    return false;
  }
  this._users.delete(id);
  return true;
}
```

</details>

---

### 完整使用示例

```js
const manager = new UserManager();

async function main() {
  try {
    // 1. 获取所有用户
    console.log('=== 获取用户列表 ===');
    const users = await manager.fetchUsers();
    console.log(users);

    // 2. 获取单个用户（会缓存）
    console.log('\n=== 获取用户 1 ===');
    const user1 = await manager.fetchUser(1);
    console.log(user1);

    // 3. 再次获取用户 1（从缓存）
    console.log('\n=== 再次获取用户 1 ===');
    const user1Again = await manager.fetchUser(1);
    console.log(user1Again);

    // 4. 创建新用户
    console.log('\n=== 创建新用户 ===');
    const newUser = manager.createUser({
      name: 'Diana',
      email: 'diana@test.com'
    });
    console.log(newUser);

    // 5. 更新用户
    console.log('\n=== 更新用户 ===');
    const updated = manager.updateUser(1, { age: 30 });
    console.log(updated);

    // 6. 删除用户
    console.log('\n=== 删除用户 ===');
    const deleted = manager.deleteUser(2);
    console.log('删除成功:', deleted);

  } catch (error) {
    console.error('错误:', error.message);
  }
}

main();
```

**期望输出**：
```
=== 获取用户列表 ===
[ { id: 1, name: 'Alice', ... }, ... ]

=== 获取用户 1 ===
[API] 获取用户 1
{ id: 1, name: 'Alice', ... }

=== 再次获取用户 1 ===
[缓存] 获取用户 1
{ id: 1, name: 'Alice', ... }

=== 创建新用户 ===
{ id: 4, name: 'Diana', email: 'diana@test.com', age: 18, ... }

=== 更新用户 ===
{ id: 1, name: 'Alice', email: 'alice@test.com', age: 30, ... }

=== 删除用户 ===
删除成功: true
```

---

### 🎯 扩展挑战

1. **⭐⭐⭐ 添加用户搜索功能**：实现 `searchUsers(query)` 方法，根据 name 或 email 模糊搜索
2. **⭐⭐⭐ 添加批量操作**：实现 `fetchUsersByIds(ids)`，用 `Promise.all` 并行获取多个用户
3. **⭐⭐⭐⭐ 添加本地存储**：使用 `localStorage` 持久化缓存，实现页面刷新后数据不丢失

---

### 📌 本章涉及的技术点

| 特性 | 使用位置 |
|------|---------|
| `class` | UserManager 类定义 |
| `async/await` | fetchUsers, fetchUser, main |
| `箭头函数` | Map/Set 回调、Promise 处理 |
| `解构赋值` | createUser 参数、updateUser 字段提取 |
| `剩余参数` | updateUser 的 rest |
| `展开运算符` | 数组/对象展开、对象合并 |
| `模板字符串` | 日志输出 |
| `Map` | 存储用户数据 |
| `Set` | 防重复请求标记 |
| `let/const` | 所有变量声明 |
| `Promise` | async/await 底层 |

---

## 附录 A：事件循环与异步原理

> 本附录解释 JavaScript 的异步执行机制。如果你刚开始学 ES6，可以**先跳过这一节**。当你对 Promise 和 async/await 感到困惑，或者遇到"为什么先打印 A 后打印 B"的诡异问题时，再回来看。

### A.1 为什么需要事件循环？

JavaScript 是**单线程**语言——同一时间只能做一件事。但浏览器/Node.js 需要处理网络请求、定时器、用户点击等异步操作。事件循环（Event Loop）就是协调**同步代码**和**异步回调**执行的机制。

### A.2 核心概念

```
┌───────────────────────────────────────┐
│            Call Stack                 │  ← 同步代码执行的地方，后进先出
│  [main] → [fn1] → [fn2] → ...        │
└──────────────┬────────────────────────┘
               │
               ▼
┌───────────────────────────────────────┐
│         Web APIs / Node APIs          │  ← 浏览器/Node 提供的异步能力
│  setTimeout, fetch, DOM, fs.readFile  │
└──────────────┬────────────────────────┘
               │
               ▼
┌─────────────────────┬──────────────────┐
│   Macrotask Queue   │  Microtask Queue │
│ (Task Queue)        │                  │
│  - setTimeout       │  - Promise.then  │
│  - setInterval      │  - await 之后    │
│  - I/O              │  - MutationObs.  │
│  - UI rendering     │  - queueMicrotask│
└─────────┬───────────┴───────┬──────────┘
          │                   │
          └─────────┬─────────┘
                    ▼
             Event Loop 检查规则：
             1. 执行一个 macrotask
             2. 清空所有 microtasks
             3. 可能渲染 UI
             4. 下一个 macrotask
```

**关键规则**：
1. 同步代码直接在 Call Stack 中执行
2. 异步操作完成后，回调被放入对应的队列
3. Event Loop 每次从 Macrotask Queue 取一个任务执行
4. 执行完一个 Macrotask 后，**清空整个 Microtask Queue**
5. 然后可能渲染 UI，再进入下一轮

> 💡 简单记忆：**Microtask 优先级高于 Macrotask**。Promise 的回调总是比 setTimeout 先执行。

### A.3 执行时序示例

```js
console.log('1: 同步代码');

setTimeout(() => {
  console.log('2: macrotask (setTimeout)');
}, 0);

Promise.resolve().then(() => {
  console.log('3: microtask (Promise.then)');
});

console.log('4: 同步代码');

// 输出顺序：
// 1: 同步代码
// 4: 同步代码
// 3: microtask (Promise.then)
// 2: macrotask (setTimeout)
```

**为什么 `setTimeout(..., 0)` 不是立即执行？**

即使延迟是 0，`setTimeout` 的回调也要先进入 Macrotask Queue，等当前同步代码执行完、所有 Microtask 清空后，才会执行。

### A.4 await 的微任务机制

```js
async function demo() {
  console.log('A');
  await Promise.resolve();   // await 之后的代码 = 放入微任务队列
  console.log('B');          // 在微任务中执行
}

console.log('C');
demo();
console.log('D');

// 输出：C, A, D, B
```

解析：
1. `C` —— 同步代码
2. 调用 `demo()`，打印 `A`，遇到 `await`，`demo` 暂停，返回一个 Promise
3. `D` —— 同步代码，Call Stack 清空
4. `B` —— Microtask 队列中的代码执行

### A.5 复杂时序题解析

```js
console.log('start');

setTimeout(() => console.log('timeout'), 0);

Promise.resolve()
  .then(() => {
    console.log('then 1');
    Promise.resolve().then(() => console.log('then 1-1'));
  })
  .then(() => console.log('then 2'));

console.log('end');

// 输出：start, end, then 1, then 1-1, then 2, timeout
```

解析：
1. `start`, `end`：同步代码
2. `then 1`：第一个微任务
3. `then 1-1`：在 `then 1` 执行时插入微任务队列，排在 `then 2` 之前
4. `then 2`：`then 1` 完成后，新的微任务
5. `timeout`：下一轮事件循环的 macrotask

> ⚠️ 面试常考这类题目，但日常开发中不需要刻意去背。记住核心规则（同步 → 微任务 → 宏任务）就能推出大部分情况。

---

## 附录 B：速查表

### B.1 var vs let vs const

| 特性 | `var` | `let` | `const` |
|------|-------|-------|---------|
| 作用域 | 函数作用域 | 块级作用域 | 块级作用域 |
| 提升 | ✅ 提升，初始化为 `undefined` | ❌ TDZ（暂时性死区） | ❌ TDZ |
| 重复声明 | ✅ 允许 | ❌ 不允许 | ❌ 不允许 |
| 重新赋值 | ✅ 允许 | ✅ 允许 | ❌ 不允许（绑定不可变） |
| 声明时初始化 | 不需要 | 不需要 | **必须** |
| 推荐使用 | ❌ 不再使用 | 需要重新赋值时 | **默认选择** |

### B.2 遍历方法对比

| 方法 | 遍历目标 | 遍历 Symbol | 遍历原型 | 适用场景 |
|------|---------|------------|---------|---------|
| `for...in` | 所有可枚举属性键 | ❌ | ✅ | 遍历对象键（不推荐用于数组） |
| `Object.keys()` | 自身可枚举字符串键 | ❌ | ❌ | 获取对象键数组 |
| `Object.getOwnPropertyNames()` | 自身所有字符串键 | ❌ | ❌ | 包括不可枚举键 |
| `Object.getOwnPropertySymbols()` | 自身 Symbol 键 | ✅ | ❌ | 获取 Symbol 属性 |
| `Reflect.ownKeys()` | 自身所有键 | ✅ | ❌ | 获取全部键 |
| `for...of` | 可迭代对象的值 | - | - | 遍历数组、字符串、Map、Set 等 |

### B.3 字符串方法

| 方法 | 说明 | 示例 |
|------|------|------|
| `` `Hello ${name}` `` | 模板字符串 | `` `Hi, ${user.name}` `` |
| `str.includes(sub)` | 是否包含子串 | `'abc'.includes('b')` → `true` |
| `str.startsWith(sub)` | 是否以子串开头 | `'abc'.startsWith('ab')` → `true` |
| `str.endsWith(sub)` | 是否以子串结尾 | `'abc'.endsWith('bc')` → `true` |
| `str.repeat(n)` | 重复 n 次 | `'ha'.repeat(3)` → `'hahaha'` |

### B.4 数组方法

| 方法 | 说明 | ES 版本 |
|------|------|---------|
| `Array.from(iterable)` | 类数组/可迭代对象转数组 | ES6 |
| `Array.of(1, 2, 3)` | 根据参数创建数组 | ES6 |
| `arr.find(fn)` | 查找满足条件的第一个元素 | ES6 |
| `arr.findIndex(fn)` | 查找满足条件的第一个元素的索引 | ES6 |
| `arr.fill(value)` | 填充数组 | ES6 |
| `arr.keys()` | 返回索引迭代器 | ES6 |
| `arr.values()` | 返回值迭代器 | ES6 |
| `arr.entries()` | 返回 `[index, value]` 迭代器 | ES6 |
| `arr.includes(value)` | 是否包含某值 | ES2016 |
| `arr.flat(depth)` | 数组扁平化 | ES2019 |
| `arr.at(index)` | 支持负索引 | ES2022 |

### B.5 Promise 方法

| 方法 | 说明 |
|------|------|
| `new Promise((resolve, reject) => {})` | 创建 Promise |
| `promise.then(onFulfilled, onRejected)` | 成功/失败回调 |
| `promise.catch(onRejected)` | 失败回调 |
| `promise.finally(onFinally)` | 无论成败都执行 |
| `Promise.resolve(value)` | 返回 resolved 的 Promise |
| `Promise.reject(reason)` | 返回 rejected 的 Promise |
| `Promise.all([p1, p2])` | 全部成功才成功，一失败就失败 |
| `Promise.race([p1, p2])` | 谁先完成用谁 |
| `Promise.allSettled([p1, p2])` | 等全部完成，不中断 |

### B.6 常用语法速查

```js
// 解构
const { a, b: c, d = 1 } = obj;
const [x, , ...rest] = arr;

// 箭头函数
const fn = x => x * 2;
const fn2 = (x, y) => { return x + y; };

// 默认参数
function greet(name = 'Guest') { /* ... */ }

// 剩余参数 + 展开
function sum(...nums) { /* nums 是数组 */ }
const arr = [1, 2, ...other];

// 对象简写
const obj = { name, age, sayHi() { /* ... */ } };

// Class
class Child extends Parent {
  constructor(x) {
    super(x);
    this.x = x;
  }
  static method() { /* ... */ }
}

// 模块
export const foo = 1;
export default function() {}
import { foo } from './mod.js';
import myFn from './mod.js';

// async/await
async function fetchData() {
  try {
    const res = await fetch('/api');
    return await res.json();
  } catch (e) {
    console.error(e);
  }
}
```

---

## 附录 C：练习题答案

> 建议先自己思考，实在想不出来再看答案。

### 第 1 章

**练习 1** ⭐：`var` 版本输出 `3, 3, 3`，因为 `var i` 是函数作用域的同一个变量。改成 `let` 后输出 `0, 1, 2`，因为每次迭代创建新的块级作用域。

**练习 2** ⭐：第三行 `config = { debug: true }` 会报错。`const` 不能重新赋值，但可以修改对象属性。

**练习 3** ⭐：
```js
if (true) {
  let message = 'hello';
}
console.log(message);  // ReferenceError
```

**练习 4** ⭐⭐：输出 `[0, 1, 2]`。

原因：ES6 的 `for` 循环为 `const` 声明的变量在**每次迭代**都创建一个新的绑定。所以每次循环时 `i` 的值都被"快照"保存到闭包函数中。

这和 `let` 在 for 循环中的行为类似，都是每次迭代创建新绑定。`for (const i = 0; ...)` 实际上是有效的语法！

### 第 2 章

**练习 1** ⭐：
```js
const msg = `Congratulations, ${user.name}! Your score is ${user.score}.`;
```

**练习 2** ⭐：
```js
const html = `
<article>
  <h1>${title}</h1>
  <p>${content}</p>
</article>
`;
```

**练习 3** ⭐⭐：
```js
const generateTable = (headers, rows) => `
<table>
  <thead><tr>${headers.map(h => `<th>${h}</th>`).join('')}</tr></thead>
  <tbody>
    ${rows.map(row => `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`).join('')}
  </tbody>
</table>
`;
```

### 第 3 章

**练习 1** ⭐：`const multiply = (x, y) => x * y;`

**练习 2** ⭐：箭头函数的 `this` 继承自定义时的外层作用域，不是 `counter` 对象。应改为普通函数：
```js
const counter = {
  count: 0,
  increment() {
    this.count++;
    console.log(this.count);
  }
};
```

**练习 3** ⭐：
```js
const average = (...nums) => {
  if (nums.length === 0) return 0;
  return nums.reduce((a, b) => a + b, 0) / nums.length;
};
```

**练习 4** ⭐：
```js
const arr1 = [1, 2];
const arr2 = [3, 4];
const result = [...arr1, 99, ...arr2];  // [1, 2, 99, 3, 4]
```

**练习 5** ⭐⭐：
```js
const createUrl = (base, ...paths) =>
  paths.reduce((url, path) => `${url}/${path}`, base);
```

### 第 4 章

**练习 1** ⭐：
```js
const [first, ...rest] = nums;
const last = rest.pop();
```
或更简洁：
```js
const [first, ...middle] = nums;
const last = middle[middle.length - 1];
```

**练习 2** ⭐：
```js
const { title, author: { name: authorName } } = book;
```

**练习 3** ⭐：
```js
function createButton({ text = 'Click', color = 'blue', size = 'medium' } = {}) {
  return `<button class="${size}" style="color:${color}">${text}</button>`;
}
```

**练习 4** ⭐⭐：`[a, b] = [b, a]`（不需要临时变量！）

**练习 5** ⭐⭐⭐：
```js
const { type, locations: [{ coords: firstCoords }] } = data;
// type = 'locations', firstCoords = [39.9, 116.4]
```

### 第 5 章

**练习 1** ⭐：
```js
function formatDate(date, format = 'YYYY-MM-DD') {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return format
    .replace('YYYY', year)
    .replace('MM', month)
    .replace('DD', day);
}
```

**练习 2** ⭐⭐：
```js
const createProduct = ({ name, price = 0, category = 'uncategorized' } = {}) => ({
  id: Math.random().toString(36).substr(2, 9),
  name,
  price,
  category,
  createdAt: new Date()
});
```

### 第 6 章

**练习 1** ⭐：
```js
const person = {
  name,
  age,
  greet() {
    return `Hello from ${this.name}`;
  }
};
```

**练习 2** ⭐：
```js
function createCounter(initial = 0) {
  let value = initial;
  return {
    increment() { value++; },
    decrement() { value--; },
    getValue() { return value; }
  };
}
```

**练习 3** ⭐：
```js
// 计算属性名主要用于对象字面量。批量生成时，可以先用计算属性名语法构建键值对数组
const obj = Object.fromEntries(
  Array.from({ length: 5 }, (_, i) => [`key_${i}`, i])
);
// { key_0: 0, key_1: 1, key_2: 2, key_3: 3, key_4: 4 }
```

**练习 4** ⭐⭐：
```js
const mergeDefaults = (defaults, config) => Object.assign({}, defaults, config);
```

### 第 7 章

**练习 1** ⭐：
```js
const arr = Array.from({ length: 5 }, (_, i) => i);  // [0, 1, 2, 3, 4]
```

**练习 2** ⭐：
```js
const students = [
  { name: 'Alice', score: 72 },
  { name: 'Bob', score: 85 },
  { name: 'Charlie', score: 90 }
];
const topStudent = students.find(s => s.score > 80);
// { name: 'Bob', score: 85 }
```

**练习 3** ⭐：
```js
const arr = Array(5).fill('pending');
```

**练习 4** ⭐⭐：
```js
const uniqueByField = (arr, field) => {
  const seen = new Set();
  return arr.filter(item => {
    const val = item[field];
    if (seen.has(val)) return false;
    seen.add(val);
    return true;
  });
};
```

### 第 8 章

**练习 1** ⭐、**2** ⭐、**3** ⭐：
```js
class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  get area() {
    return this.width * this.height;
  }

  get perimeter() {
    return 2 * (this.width + this.height);
  }

  static fromJSON(json) {
    return new Rectangle(json.width, json.height);
  }
}

class Square extends Rectangle {
  constructor(side) {
    super(side, side);
  }
}
```

**练习 4** ⭐⭐：`super(name)` 必须在 `this.breed = breed` 之前调用。子类构造函数中，必须先 `super()` 才能使用 `this`。

**练习 5** ⭐⭐：
```js
class BankAccount {
  constructor(balance = 0) {
    this.#balance = balance;
  }

  deposit(amount) {
    if (amount > 0) this.#balance += amount;
  }

  withdraw(amount) {
    if (amount > 0 && amount <= this.#balance) {
      this.#balance -= amount;
    }
  }

  transfer(to, amount) {
    if (amount <= this.#balance) {
      this.withdraw(amount);
      to.deposit(amount);
    }
  }

  getBalance() {
    return this.#balance;
  }
}
```

### 第 9 章

**练习 2** ⭐：`React` 是默认导出，`useState` 和 `useEffect` 是命名导出。

**练习 3** ⭐⭐：`import` 语句必须是顶层静态的，不能在 `if` 块内。条件导入应该用动态导入：
```js
if (condition) {
  const { foo } = await import('./module.js');
}
```

**练习 4** ⭐⭐：
```js
import * as React from 'react';
// 使用时：React.createElement, React.Component
// 注意：这和 import { createElement, Component } 不完全等价
// import * 会导入 react 的所有导出，而 import { ... } 只导入指定的
```

### 第 10 章

**练习 1** ⭐：
```js
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
```

**练习 2** ⭐：
```js
Promise.all([fetchUser(1), fetchPosts()]).then(([user, posts]) => {
  console.log(user, posts);
});
```

**练习 3** ⭐⭐：输出 `1, 3, 2, 4`。两个 Promise 链并行执行，微任务按入队顺序执行。

**练习 4** ⭐⭐：
```js
function fetchWithTimeout(url, timeoutMs) {
  return Promise.race([
    fetch(url),
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error('请求超时')), timeoutMs)
    )
  ]);
}
```

### 第 11 章

**练习 1** ⭐：
```js
async function loadUserData(userId) {
  try {
    const user = await fetchUser(userId);
    const orders = await fetchOrders(user.id);
    console.log(orders);
  } catch (err) {
    console.error(err);
  }
}
```

**练习 2** ⭐：
```js
async function getJSON(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}
```

**练习 3** ⭐⭐：
```js
async function fetchAll(urls) {
  const promises = urls.map(url => fetch(url).then(r => r.json())));
  return Promise.all(promises);
}
// 或使用更简洁的写法：
async function fetchAll(urls) {
  return Promise.all(urls.map(async url => {
    const res = await fetch(url);
    return res.json();
  }));
}
```

**练习 4** ⭐⭐：
```js
async function retry(fn, times) {
  for (let i = 0; i < times; i++) {
    try {
      return await fn();
    } catch (e) {
      if (i === times - 1) throw e;
    }
  }
}
```

**练习 5** ⭐⭐⭐：
```js
async function asyncPool(concurrency, tasks) {
  const results = [];
  const executing = [];

  for (const task of tasks) {
    const p = Promise.resolve().then(() => task());
    results.push(p);

    if (concurrency <= tasks.length) {
      const e = p.then(() => executing.splice(executing.indexOf(e), 1));
      executing.push(e);
      if (executing.length >= concurrency) {
        await Promise.race(executing);
      }
    }
  }

  return Promise.all(results);
}
```

### 第 12 章

**练习 1** ⭐：`const unique = [...new Set(nums)];`

**练习 2** ⭐：
```js
const clickMap = new Map();
button1.addEventListener('click', () => {
  clickMap.set(button1, (clickMap.get(button1) || 0) + 1);
});
```

**练习 3** ⭐：
- `Object` 适合：配置对象、JSON 数据、结构固定的键值对（键是字符串）。
- `Map` 适合：键是对象/函数、频繁增删、需要保持插入顺序的场景。

**练习 4** ⭐⭐：
```js
function cached(fn) {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (cache.has(key)) {
      console.log('使用缓存...');
      return cache.get(key);
    }
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}
```

### 第 13 章

**练习 1** ⭐：
```js
const s1 = Symbol('test');
const s2 = Symbol('test');
console.log(s1 === s2);  // false
```

**练习 2** ⭐：
```js
const hidden = Symbol('hidden');
const obj = {};
obj[hidden] = 'secret';

for (const key in obj) console.log(key);  // 无输出
console.log(Object.keys(obj));  // []
console.log(Object.getOwnPropertySymbols(obj));  // [Symbol(hidden)]
```

**练习 3** ⭐⭐：
```js
// module1.js
const KEY = Symbol.for('app.key');

// module2.js
const KEY = Symbol.for('app.key');
// KEY === KEY (来自 module1) 为 true
```

### 第 14 章

**练习 1** ⭐：
```js
for (const char of 'JavaScript') {
  console.log(char);
}
```

**练习 2** ⭐：
```js
for (const [key, value] of map) {
  console.log(`${key} => ${value}`);
}
```

**练习 3** ⭐：
- `for...in` 遍历**可枚举属性键**（包括继承的），适合遍历对象的键。
- `for...of` 遍历**可迭代对象的值**，适合遍历数组、字符串、Map、Set 等。
- **数组遍历优先用 `for...of` 或 `forEach`**，不要用 `for...in`（会遍历到自定义属性，且顺序不保证）。

**练习 4** ⭐⭐：
```js
const idGenerator = {
  *[Symbol.iterator]() {
    for (let i = 0; i < 5; i++) {
      yield Math.random().toString(36).substr(2, 9);
    }
  }
};
```

### 第 15 章

**练习 1** ⭐：
```js
function* range(start, end) {
  for (let i = start; i <= end; i++) {
    yield i;
  }
}
```

**练习 2** ⭐：
```js
function* fibonacci() {
  let [prev, curr] = [0, 1];
  while (true) {
    yield curr;
    [prev, curr] = [curr, prev + curr];
  }
}

const fib = fibonacci();
const first10 = [];
for (let i = 0; i < 10; i++) {
  first10.push(fib.next().value);
}
console.log(first10);  // [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

**练习 3** ⭐⭐：
```js
function* gen1() {
  yield 1;
  yield 2;
}

function* gen2() {
  yield* gen1();
  yield 3;
}
// 遍历 gen2() 得到 1, 2, 3
```

### 第 16 章

**练习 1** ⭐：
```js
const withDefault = new Proxy({}, {
  get(target, prop) {
    return prop in target ? target[prop] : 0;
  }
});
```

**练习 2** ⭐⭐：
```js
const person = new Proxy({}, {
  set(target, prop, value) {
    if (prop === 'age' && (!Number.isInteger(value) || value <= 0)) {
      throw new TypeError('age 必须是正整数');
    }
    target[prop] = value;
    return true;
  }
});
```

---

## 附录 D：推荐学习资源

### 官方与权威文档
- [MDN JavaScript 指南](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide) —— 最权威、最全面的参考
- [ECMAScript 规范](https://tc39.es/ecma262/) —— 语言规范原文，适合深入细节时查阅

### 在线教程
- [JavaScript.info](https://javascript.info/) —— 现代 JavaScript 教程，质量极高，有中文版
- [ES6 入门教程（阮一峰）](https://es6.ruanyifeng.com/) —— 中文社区最知名的 ES6 参考书

### 练习平台
- [Codewars](https://www.codewars.com/) —— 用编程挑战巩固语法
- [LeetCode](https://leetcode.cn/) —— 算法题中大量使用 ES6+ 语法

### 工具
- [Babel REPL](https://babeljs.io/repl) —— 看 ES6 代码被转译成 ES5 后的样子，帮助理解底层
- [Can I use](https://caniuse.com/) —— 查询浏览器对新特性的支持情况

---

> 🎉 **恭喜完成！** 如果你读到了这里，已经对 ES6 的核心特性有了系统的了解。接下来的建议：
>
> 1. **回头做一遍练习题**（不要直接看答案）。
> 2. **在你的项目中开始用 `const`/`let`、箭头函数、模板字符串、解构赋值**。这些都是零成本、立即可用的改进。
> 3. **遇到异步操作时，尝试用 Promise 和 async/await 替代回调**。
> 4. **保持学习**：ES 标准每年都在演进（ES2016、ES2017……），掌握 ES6 的基础后，后续的新特性会很容易上手。
>
> Happy Coding! 🚀

