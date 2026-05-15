# ES6 教程

> 面向对象：已有 JavaScript 基础，希望系统掌握 ES6+ 核心特性的开发者。

## 1. 引言

ECMAScript 6（简称 ES6），正式名称为 ECMAScript 2015，于 2015 年 6 月由 ECMA International 正式发布。它解决了 JavaScript 长期以来存在的变量提升（hoisting）、回调地狱、缺乏模块化支持、原型继承晦涩等核心痛点。

### 1.1 四大设计原则

**向后的兼容性（Backward Compatibility）**

ES6 是 JavaScript 历史上最大的一次语法升级，但所有新特性均为严格模式下或新语法形式引入，不会破坏现有代码的运行。

**语法糖与底层原语的分离（Syntactic Sugar vs. Primitives）**

ES6 的设计者区分了"让代码更简洁易读"的语法糖和"提供全新能力"的底层原语：
- **语法糖**：Class 语法并不改变 JavaScript 基于原型的继承模型，只是提供了更熟悉的声明方式。
- **底层原语**：Proxy 和 Symbol 是真正全新的底层原语，开启了 JavaScript 元编程和对象行为自定义的全新可能性。

**工程化友好（Engineering Friendliness）**

引入了大量有利于代码组织、复用和维护的特性，如模块化、解构赋值、块级作用域等。

**为工具链优化（Toolchain Optimization）**

ES6 在设计时充分考虑了静态分析的需求。ES 模块的静态导入/导出语法使得构建工具能够在编译时确定模块依赖图，从而实现 Tree Shaking（死代码消除）等关键优化。

### 1.2 新特性全景图

| 特性类别 | 核心特性 | 解决的问题 | 后续演进 |
|---------|---------|-----------|---------|
| 变量与作用域 | `let`、`const`、块级作用域、TDZ | `var` 提升和函数作用域混乱 | 无重大变化，模式已稳定 |
| 函数增强 | 箭头函数、默认参数、剩余参数、展开运算符 | `this` 绑定混乱、参数处理繁琐 | ES2018 扩展了对象展开 |
| 字符串处理 | 模板字面量、多行字符串、标签模板、`String.raw` | 字符串拼接可读性差、HTML 转义困难 | ES2018 引入 `s` (dotAll) 标志，ES2024 引入 `v` 标志 |
| 解构赋值 | 数组解构、对象解构、嵌套解构、默认值 | 从复杂结构中提取数据代码冗长 | 模式广泛应用于现代代码库 |
| 面向对象 | Class 语法、`extends`、`super`、静态方法 | 原型继承语法晦涩、不符合直觉 | ES2022 增加私有字段 `#` |
| 模块化 | `import`/`export`、默认导出、命名空间导出 | 缺乏官方模块标准、AMD/CommonJS 碎片化 | ES2020 动态导入、`import.meta` |
| 异步编程 | Promise、`then`/`catch`、静态方法 | 回调地狱、错误处理困难 | ES2017 `async/await`、ES2024 `Promise.withResolvers` |
| 数据结构 | `Map`、`Set`、`WeakMap`、`WeakSet` | 对象键只能是字符串、缺乏集合抽象 | 无重大变化 |
| 新类型 | `Symbol`、Well-Known Symbols、全局注册表 | 属性名冲突、无法定义不可枚举的内部属性 | 持续增加新的 Well-Known Symbols |
| 迭代协议 | `for...of`、可迭代协议、迭代器协议 | `for...in` 遍历属性而非值、自定义迭代困难 | ES2018 异步迭代器 + `for await...of` 语法 |
| 生成器 | `function*`、`yield`、双向通信 | 无法暂停/恢复函数执行、无限序列表达困难 | ES2018 异步生成器 |
| 元编程 | `Proxy`（13 种 trap）、`Reflect` API | 无法拦截对象的基本操作 | ES2021 `WeakRef` / `FinalizationRegistry` |
| 数值扩展 | 二进制/八进制字面量、`Number.isFinite`、Math 新方法 | 数值判断不可靠、缺乏位运算支持 | ES2020 `BigInt` |
| 数组增强 | `Array.from`、`Array.of`、`find`、`findIndex`、迭代方法 | 类数组转换繁琐、搜索方法缺失 | ES2023 `toSorted`、`toReversed` 等不可变方法 |
| 对象增强 | 简写属性、计算属性名、方法简写、`Object.assign` | 对象字面量重复代码多 | ES2018 Rest/Spread 属性、ES2022 `Object.hasOwn` |
| Unicode 支持 | `String.fromCodePoint`、`codePointAt`、`u` 标志 | 四字节字符处理错误、码点操作缺失 | ES2024 `v` 标志、Well-formed strings |

---

## 2. 变量与作用域

### 2.1 `let` 与 `const`

`let` 和 `const` 声明的变量具有**块级作用域**（block scope），解决了 `var` 的函数作用域和变量提升问题。

```javascript
// var 的问题：变量提升
console.log(a); // undefined（不会报错）
var a = 1;

// let：不存在变量提升
console.log(b); // ReferenceError: Cannot access 'b' before initialization
let b = 2;

// const：必须初始化，且不能重新赋值
const c = 3;
c = 4; // TypeError: Assignment to constant variable

// const 保证的是绑定（binding）不变，而非值不可变
const arr = [1, 2];
arr.push(3);        // OK
arr = [1, 2, 3];    // TypeError

const obj = { a: 1 };
obj.a = 2;          // OK
obj = {};           // TypeError

// 如需完全不可变，需配合 Object.freeze（浅冻结）或使用不可变库
```

**使用建议**：
- 默认使用 `const`
- 确实需要重新赋值时（如循环计数器、累加器），使用 `let`
- 避免使用 `var`

### 2.2 暂时性死区（TDZ）

从块级作用域的顶部到变量声明语句之间，称为"暂时性死区"（Temporal Dead Zone）。在 TDZ 中访问变量会抛出 `ReferenceError`。

```javascript
{
  // TDZ 开始
  console.log(x); // ReferenceError
  
  let x = 10;     // TDZ 结束
}
```

TDZ 的本质：JavaScript 引擎在扫描代码时，会预先知道块内声明了哪些变量，但在实际声明之前不允许访问。这使得 `typeof` 也不再是 100% 安全的操作。

```javascript
// 在 let 声明之前，typeof 也会报错
if (true) {
  console.log(typeof undeclaredVar); // "undefined"（未声明的变量不会报错）
  console.log(typeof x);             // ReferenceError（TDZ 中）
  let x;
}
```

### 2.3 块级作用域与闭包

块级作用域让 `for` 循环中的闭包问题得到根本解决：

```javascript
// ES5：需要借助 IIFE
for (var i = 0; i < 3; i++) {
  (function(j) {
    setTimeout(() => console.log(j), 100);
  })(i);
}

// ES6：let 每次迭代都会创建新的绑定
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100); // 0, 1, 2
}
```

---

## 3. 函数增强

### 3.1 箭头函数（Arrow Function）

箭头函数提供了更简洁的语法，并且**没有自己的 `this`、`arguments`、`super` 和 `new.target`**。

```javascript
// 基本语法
const add = (a, b) => a + b;

// 多行需要花括号和 return
const multiply = (a, b) => {
  const result = a * b;
  return result;
};

// 返回对象需要括号包裹
const createUser = name => ({ name, active: true });
```

**关键特性：`this` 的词法绑定**

箭头函数的 `this` 在定义时确定，继承自外层作用域，不会因为调用方式改变。

```javascript
const team = {
  members: ['Alice', 'Bob'],
  leader: 'Charlie',
  
  // 普通函数：this 取决于调用方式
  showLeaderWrong: function() {
    this.members.forEach(function(member) {
      console.log(`${member}'s leader is ${this.leader}`); // undefined
    });
  },
  
  // 箭头函数：this 继承外层词法环境
  showLeaderRight: function() {
    this.members.forEach(member => {
      console.log(`${member}'s leader is ${this.leader}`); // Charlie
    });
  }
};
```

**不适用场景**：
- 不能作为构造函数使用（没有 `[[Construct]]`）
- 没有 `prototype` 属性
- 不能用作 `Generator` 函数
- 需要动态 `this` 的场景（如 DOM 事件处理回调中需要通过 `this` 访问绑定元素时）

### 3.2 默认参数（Default Parameters）

```javascript
function greet(name = 'Guest', greeting = 'Hello') {
  return `${greeting}, ${name}!`;
}

greet();              // "Hello, Guest!"
greet('Alice');       // "Hello, Alice!"
greet(undefined, 'Hi'); // "Hi, Guest!"（显式传 undefined 会触发默认值）
```

**默认参数可以引用前面的参数**：

```javascript
function createRectangle(width, height = width) {
  return { width, height };
}

createRectangle(5); // { width: 5, height: 5 }
```

**默认参数是惰性求值的**：

```javascript
let counter = 0;
function increment(x = counter++) {
  return x;
}
increment(); // 0
increment(); // 1
increment(); // 2
```

### 3.3 剩余参数（Rest Parameters）

使用 `...` 将不定数量的参数收集为一个数组。

```javascript
function sum(...numbers) {
  return numbers.reduce((acc, n) => acc + n, 0);
}

sum(1, 2, 3, 4); // 10
```

**剩余参数必须是最后一个参数**：

```javascript
function log(prefix, ...messages) {
  console.log(`[${prefix}]`, ...messages);
}
```

剩余参数与 `arguments` 的区别：
- `arguments` 是类数组对象，没有数组方法
- 剩余参数是真正的数组，可以直接使用 `.map()`、`.filter()` 等
- 箭头函数没有 `arguments`，必须使用剩余参数

### 3.4 展开运算符（Spread Operator）

展开运算符是剩余参数的逆操作：将可迭代对象展开为单独的元素。

```javascript
// 数组展开
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4]; // [1, 2, 3, 4]

// 函数调用
const numbers = [1, 2, 3];
Math.max(...numbers); // 3（等同于 Math.max(1, 2, 3)）

// 数组浅拷贝
const original = [1, 2, { a: 3 }];
const copy = [...original];

// 合并数组
const merged = [...arr1, ...arr2];

// 对象展开（ES2018）
const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 }; // { a: 1, b: 2, c: 3 }
```

**注意**：展开运算符进行的是浅拷贝。

```javascript
const obj = { nested: { value: 1 } };
const copy = { ...obj };
copy.nested.value = 2;
console.log(obj.nested.value); // 2（原对象也被修改）
```

---

## 4. 字符串处理

### 4.1 模板字面量（Template Literals）

使用反引号（`` ` ``）包裹，支持多行字符串和插值表达式。

```javascript
const name = 'Alice';
const age = 25;

// 插值
const greeting = `Hello, ${name}! You are ${age} years old.`;

// 多行字符串
const html = `
  <div>
    <h1>${name}</h1>
    <p>Age: ${age}</p>
  </div>
`;

// 表达式支持
const result = `Sum: ${1 + 2 + 3}`; // "Sum: 6"

// 支持函数调用
const upper = str => str.toUpperCase();
const shout = `${upper('hello')}!`; // "HELLO!"
```

### 4.2 标签模板（Tagged Templates）

标签模板允许用函数处理模板字面量，接收字符串数组和插值表达式值。

```javascript
function highlight(strings, ...values) {
  return strings.reduce((result, str, i) => {
    const value = values[i] !== undefined ? `<b>${values[i]}</b>` : '';
    return result + str + value;
  }, '');
}

const name = 'Alice';
const age = 25;
highlight`Name: ${name}, Age: ${age}`;
// "Name: <b>Alice</b>, Age: <b>25</b>"
```

**实际应用场景**：

```javascript
// SQL 查询参数化（防止 SQL 注入）
function sql(strings, ...values) {
  return {
    text: strings.reduce((acc, str, i) => acc + str + `$${i + 1}`, ''),
    values
  };
}

const query = sql`SELECT * FROM users WHERE id = ${userId}`;
// { text: "SELECT * FROM users WHERE id = $1", values: [42] }

// 样式组件（styled-components 的核心原理）
function css(strings, ...values) {
  // 处理样式字符串...
}

const color = 'red';
const styles = css`
  color: ${color};
  font-size: 16px;
`;
```

### 4.3 字符串新方法

```javascript
// 判断是否以某字符串开头/结尾
str.startsWith('Hello'); // boolean
str.endsWith('!');       // boolean
str.includes('world');   // boolean

// 重复字符串
'na'.repeat(3); // "nanana"

// 补全长度
'5'.padStart(2, '0');  // "05"
'5'.padEnd(2, '0');    // "50"

// 去除空白
'  hello  '.trimStart(); // "hello  "
'  hello  '.trimEnd();   // "  hello"
```

---

## 5. 解构赋值

解构赋值允许从数组或对象中提取值，并赋值给变量。

### 5.1 数组解构

```javascript
const [a, b] = [1, 2];
console.log(a, b); // 1 2

// 跳过元素
const [first, , third] = [1, 2, 3];

// 剩余元素
const [head, ...tail] = [1, 2, 3, 4];
// head: 1, tail: [2, 3, 4]

// 默认值
const [x = 10, y = 20] = [undefined, 5];
// x: 10, y: 5

// 交换变量
[a, b] = [b, a];
```

### 5.2 对象解构

```javascript
const user = { name: 'Alice', age: 25, country: 'CN' };

// 基本解构
const { name, age } = user;

// 重命名
const { name: userName } = user;

// 默认值
const { role = 'user' } = user; // role: "user"

// 嵌套解构
const person = {
  info: {
    address: {
      city: 'Beijing'
    }
  }
};
const { info: { address: { city } } } = person;

// 剩余属性（ES2018）
const { name, ...rest } = user;
// rest: { age: 25, country: 'CN' }
```

### 5.3 实战模式

```javascript
// 函数参数解构
function createUser({ name, age, role = 'user' }) {
  return { name, age, role };
}

// 嵌套参数解构
function drawChart({ size: { width = 100, height = 100 }, coords: [x, y] }) {
  // ...
}

// 与展开运算符结合（复制对象并修改部分属性）
const updatedUser = { ...user, age: 26 };

// 解构配合重命名和默认值（API 数据处理常用）
const { data: users = [], error: err = null } = apiResponse;

// 陷阱：右侧为 null 或 undefined 会直接报错
// const { a } = null;      // TypeError: Cannot destructure property...
// const { a } = undefined; // TypeError
// 安全做法：先确保右侧有值，或提供空对象默认值
function safeDestructure(options = {}) {
  const { host = 'localhost', port = 8080 } = options;
  return { host, port };
}
```

---

## 6. 对象增强

### 6.1 属性简写

```javascript
const name = 'Alice';
const age = 25;

// ES5
const user1 = { name: name, age: age };

// ES6
const user2 = { name, age };
```

### 6.2 计算属性名

```javascript
const key = 'dynamicKey';
const obj = {
  [key]: 'value',
  [`${key}_suffix`]: 'another value'
};
// { dynamicKey: 'value', dynamicKey_suffix: 'another value' }
```

### 6.3 方法简写

```javascript
const user = {
  name: 'Alice',
  
  // ES5
  sayHi: function() {
    return 'Hi!';
  },
  
  // ES6（注意：不是箭头函数，有自己的 this）
  greet() {
    return `Hello, I'm ${this.name}`;
  }
};
```

### 6.4 `Object.assign`

用于对象浅拷贝和合并。

```javascript
const target = { a: 1 };
const source = { b: 2 };

Object.assign(target, source);
// target: { a: 1, b: 2 }

// 浅拷贝惯用法
const copy = Object.assign({}, original);

// 合并多个对象
const merged = Object.assign({}, obj1, obj2, obj3);
```

**注意**：`Object.assign` 只复制可枚举的自有属性，且是浅拷贝。此外，它会调用源对象的 getter 并将返回值作为普通属性复制到目标对象，不会复制 getter/setter 本身。

### 6.5 对象展开运算符（ES2018）

```javascript
// 比 Object.assign 更简洁的浅拷贝
const copy = { ...original };

// 合并对象（后面的属性覆盖前面的）
const merged = { ...defaults, ...options };

// 添加/覆盖属性
const updated = { ...user, age: 26, active: true };

// 删除属性（通过解构+展开）
const { password, ...safeUser } = user;
```

### 6.6 `Object.hasOwn`（ES2022）

`Object.hasOwn` 是 `Object.prototype.hasOwnProperty` 的更可靠替代，不受对象覆盖 `hasOwnProperty` 的影响。

```javascript
const obj = {
  a: 1,
  hasOwnProperty: 'oops' // 意外覆盖了原型方法
};

// 旧写法可能报错
// obj.hasOwnProperty('a'); // TypeError: obj.hasOwnProperty is not a function

// 新写法安全可靠
Object.hasOwn(obj, 'a');     // true
Object.hasOwn(obj, 'b');     // false
Object.hasOwn(obj, 'toString'); // false（继承属性）
```

---

## 7. 数组增强

### 7.1 `Array.from`

将类数组对象或可迭代对象转换为真正的数组。

```javascript
// 类数组转数组
const divs = document.querySelectorAll('div');
const divArray = Array.from(divs);

// 字符串转数组
Array.from('hello'); // ['h', 'e', 'l', 'l', 'o']

// Set 转数组
Array.from(new Set([1, 2, 2, 3])); // [1, 2, 3]

// 带映射函数（替代 map + from 的组合）
Array.from([1, 2, 3], x => x * 2); // [2, 4, 6]

// 生成序列
Array.from({ length: 5 }, (_, i) => i); // [0, 1, 2, 3, 4]
```

### 7.2 `Array.of`

解决 `Array` 构造函数因参数数量不同行为不一致的问题。

```javascript
Array(3);    // [empty × 3]（创建一个长度为3的空数组）
Array(3, 4); // [3, 4]

Array.of(3);    // [3]
Array.of(3, 4); // [3, 4]
Array.of();     // []
```

### 7.3 新的实例方法

```javascript
const arr = [5, 12, 8, 130, 44];

// find / findIndex：查找满足条件的第一个元素/索引
arr.find(x => x > 10);      // 12
arr.findIndex(x => x > 10); // 1

// findLast / findLastIndex（ES2023）
arr.findLast(x => x > 10);      // 130
arr.findLastIndex(x => x > 10); // 4

// includes（ES2016）：判断是否包含（比 indexOf 更直观）
arr.includes(8);  // true
arr.includes(99); // false

// 注意：includes 可以正确判断 NaN
[NaN].includes(NaN); // true
[NaN].indexOf(NaN);  // -1

// some / every（ES5 已有，但常与 ES6 新方法配合使用）
arr.some(x => x > 100);  // true
arr.every(x => x > 0);   // true
```

### 7.4 `at()` 方法（ES2022）

`at()` 方法接受一个整数参数，返回指定索引处的元素，支持负索引（从后往前数）。

```javascript
const arr = [1, 2, 3, 4, 5];

arr.at(0);    // 1（等价于 arr[0]）
arr.at(-1);   // 5（等价于 arr[arr.length - 1]）
arr.at(-2);   // 4

// 字符串也有 at() 方法
'hello'.at(-1); // "o"
```

**优势**：在链式调用中比 `arr[arr.length - 1]` 更简洁直观。

```javascript
// 旧写法
users[users.length - 1].name;

// 新写法
users.at(-1).name;
```

### 7.5 不可变方法（ES2023）

```javascript
const original = [3, 1, 2];

// 返回新数组，不修改原数组
original.toSorted();    // [1, 2, 3]（原数组不变）
original.toReversed();  // [2, 1, 3]
original.toSpliced(1, 1, 99); // [3, 99, 2]

// 指定位置替换
original.with(1, 99);   // [3, 99, 2]
```

---

## 8. 面向对象：Class

### 8.1 基本语法

ES6 Class 是原型继承的语法糖，提供了更清晰的声明方式。

```javascript
class Animal {
  // 构造方法
  constructor(name) {
    this.name = name;
  }
  
  // 实例方法（自动添加到 prototype 上）
  speak() {
    console.log(`${this.name} makes a sound.`);
  }
  
  // 静态方法
  static isAnimal(obj) {
    return obj instanceof Animal;
  }
}

const dog = new Animal('Buddy');
dog.speak(); // "Buddy makes a sound."
```

### 8.2 继承

```javascript
class Dog extends Animal {
  constructor(name, breed) {
    super(name); // 调用父类构造函数
    this.breed = breed;
  }
  
  // 重写父类方法
  speak() {
    super.speak(); // 调用父类方法
    console.log(`${this.name} barks.`);
  }
  
  // 静态方法可以被继承
  static createPuppy(name) {
    return new Dog(name, 'Unknown');
  }
}

const puppy = new Dog('Max', 'Golden Retriever');
puppy.speak();
// "Max makes a sound."
// "Max barks."
```

### 8.3 关键细节

```javascript
class Example {
  // 类表达式也可以有名字
  // const MyClass = class NamedClass { ... }
  
  // getter / setter
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }
  
  set fullName(value) {
    [this.firstName, this.lastName] = value.split(' ');
  }
  
  // 静态属性（ES2022 支持直接声明）
  static count = 0;
  
  // 私有字段（ES2022）
  #secret = 42;
  
  getSecret() {
    return this.#secret;
  }
  
  // 私有方法（ES2022）
  #validate() {
    return this.#secret > 0;
  }
  
  // new.target：在构造函数中判断是如何被调用的
  constructor(name) {
    // 如果通过 new 调用，new.target 指向当前类
    // 如果通过 Reflect.construct 调用，new.target 可能指向子类
    if (new.target === Example) {
      console.log('Direct instantiation');
    }
  }
}
```

**Class 与构造函数的区别**：
- Class 必须通过 `new` 调用，否则会抛出 `TypeError`
- Class 内部默认启用严格模式
- Class 的方法不可枚举（`enumerable: false`）
- Class 声明不会提升（存在 TDZ）

---

## 9. 模块化

### 9.1 导出（Export）

```javascript
// math.js

// 命名导出
export const PI = 3.14159;

export function add(a, b) {
  return a + b;
}

// 默认导出（每个模块只能有一个）
// 默认导出函数的同时，会在当前模块创建一个名为 multiply 的局部绑定
export default function multiply(a, b) {
  return a * b;
}

// 也可以先定义再导出
function subtract(a, b) {
  return a - b;
}

// 复用默认导出的局部绑定 multiply 作为命名导出
export { subtract, multiply as times };
```

### 9.2 导入（Import）

```javascript
// 默认导入（名字可以自定义）
import multiply from './math.js';

// 命名导入
import { add, PI, subtract as minus } from './math.js';

// 同时导入默认和命名
import multiply, { add, PI } from './math.js';

// 命名空间导入
import * as math from './math.js';
math.add(1, 2);
math.PI;

// 副作用导入（只执行模块，不导入绑定）
import './polyfill.js';
```

### 9.3 动态导入（ES2020）

```javascript
// import() 返回 Promise，支持按需加载
button.addEventListener('click', async () => {
  const { default: Chart } = await import('./chart.js');
  const chart = new Chart(data);
});

// 条件加载
if (condition) {
  const module = await import('./conditional.js');
}

// 同时支持 await 在顶层（Top-level await，ES2022）
// const data = await import('./data.json', { assert: { type: 'json' } });
```

### 9.4 `import.meta`（ES2020）

`import.meta` 是一个包含当前模块上下文信息的对象，最常见的是 `import.meta.url`（当前模块的 URL）。

```javascript
// 获取当前模块路径
console.log(import.meta.url); // "file:///path/to/module.js"

// 常用于解析相对路径
const wasmUrl = new URL('./module.wasm', import.meta.url);
```

### 9.5 ES 模块 vs CommonJS

| 特性 | ES Module | CommonJS |
|------|-----------|----------|
| 语法 | `import`/`export` | `require`/`module.exports` |
| 加载时机 | 静态（编译时） | 动态（运行时） |
| 静态分析 | 支持 Tree Shaking | 不支持 |
| 异步加载 | 原生支持 `import()` | 不支持 |
| 循环依赖 | 部分支持（导出绑定） | 部分支持（导出值的拷贝） |
| 顶层 `this` | `undefined` | `module.exports` |

---

## 10. 新类型：Symbol

### 10.1 基本用法

Symbol 是 ES6 引入的第七种原始数据类型，表示唯一的标识符。

```javascript
const sym1 = Symbol();
const sym2 = Symbol('description');
const sym3 = Symbol('description');

sym2 === sym3; // false（每个 Symbol 都是唯一的）

// 作为对象属性键
const id = Symbol('id');
const user = {
  name: 'Alice',
  [id]: 12345
};

user[id]; // 12345
```

### 10.2 Symbol 的特性

```javascript
// Symbol 属性不可枚举
Object.keys(user);        // ["name"]
Object.getOwnPropertyNames(user); // ["name"]
Object.getOwnPropertySymbols(user); // [Symbol(id)]

// Reflect.ownKeys 返回所有键（包括 Symbol）
Reflect.ownKeys(user); // ["name", Symbol(id)]

// Symbol 不能隐式转换为字符串
'' + sym1; // TypeError
String(sym1); // "Symbol()"（显式转换可以）
```

### 10.3 Well-Known Symbols

JavaScript 内置了一些 Symbol 常量，用于改变语言内部行为。

```javascript
// Symbol.iterator：定义对象的默认迭代器
const obj = {
  data: [1, 2, 3],
  [Symbol.iterator]() {
    let index = 0;
    return {
      next: () => ({
        value: this.data[index++],
        done: index > this.data.length
      })
    };
  }
};

[...obj]; // [1, 2, 3]

// Symbol.toStringTag：自定义 Object.prototype.toString 标签
class MyClass {
  get [Symbol.toStringTag]() {
    return 'MyClass';
  }
}
Object.prototype.toString.call(new MyClass()); // "[object MyClass]"

// Symbol.hasInstance：自定义 instanceof 行为
class ArrayLike {
  static [Symbol.hasInstance](instance) {
    // 示例逻辑较宽松：任何含 length 属性的对象都会匹配
    return Array.isArray(instance) || 'length' in instance;
  }
}
```

### 10.4 全局 Symbol 注册表

```javascript
// Symbol.for：在全局注册表中创建/获取 Symbol
const globalSym = Symbol.for('app.id');
const sameSym = Symbol.for('app.id');
globalSym === sameSym; // true

// Symbol.keyFor：获取全局 Symbol 的键
Symbol.keyFor(globalSym); // "app.id"
Symbol.keyFor(Symbol());  // undefined（非全局 Symbol）
```

---

## 11. 数据结构

### 11.1 Map

Map 是键值对的集合，键可以是任意类型（对象、函数、原始值）。

```javascript
const map = new Map();

// 添加键值对
map.set('name', 'Alice');
map.set(42, 'number key');
map.set({ id: 1 }, 'object key');

// 读取
map.get('name'); // "Alice"
map.has(42);     // true
map.size;        // 3

// 删除
map.delete(42);
map.clear();

// 迭代
for (const [key, value] of map) {
  console.log(key, value);
}

// 初始化
const map2 = new Map([
  ['a', 1],
  ['b', 2]
]);
```

**Map vs Object**：
- Map 的键可以是任意类型，Object 的键会被转为字符串
- Map 保持插入顺序，Object 的键顺序较复杂（整数键会先排序）
- Map 有 `size` 属性，Object 需要手动计算
- Map 在频繁增删场景下性能更好

### 11.2 Set

Set 是值的集合，值不重复。

```javascript
const set = new Set([1, 2, 2, 3]);
// {1, 2, 3}

set.add(4);
set.has(2);  // true
set.delete(2);
set.size;    // 3

// 常用：数组去重
const unique = [...new Set([1, 2, 2, 3])];

// 常用：集合运算
const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);

// 并集
const union = new Set([...a, ...b]);

// 交集
const intersection = new Set([...a].filter(x => b.has(x)));

// 差集
const difference = new Set([...a].filter(x => !b.has(x)));
```

### 11.3 WeakMap 与 WeakSet

WeakMap 的键必须是对象，且不影响垃圾回收（弱引用）。

```javascript
// WeakMap：常用于存储对象的私有数据
const privateData = new WeakMap();

class User {
  constructor(name, secret) {
    this.name = name;
    privateData.set(this, { secret });
  }
  
  getSecret() {
    return privateData.get(this).secret;
  }
}

// 当 User 实例被垃圾回收时，WeakMap 中对应条目自动消失
```

**现代替代方案**：ES2022 引入了 `#privateField` 语法，更直观且是语言层面的支持：

```javascript
class User {
  #secret; // 直接声明私有字段

  constructor(name, secret) {
    this.name = name;
    this.#secret = secret;
  }

  getSecret() {
    return this.#secret;
  }
}
```

两种方案对比：
- WeakMap 方案：适合需要动态添加私有数据、或需要在外部访问私有状态的场景
- `#privateField` 方案：语法更简洁，编译时即可检查权限，更推荐使用

```javascript
// WeakSet：存储对象的弱引用集合
const visited = new WeakSet();

function process(obj) {
  if (visited.has(obj)) return;
  visited.add(obj);
  // ...
}
```

**WeakMap/WeakSet 的限制**：
- 不可迭代（没有 `size`、没有 `keys()`/`values()`）
- 不能遍历（防止暴露垃圾回收状态）
- 键必须是对象

---

## 12. 迭代协议与生成器

### 12.1 可迭代协议（Iterable Protocol）

一个对象是可迭代的，如果它实现了 `@@iterator` 方法（即 `Symbol.iterator`）。

```javascript
// 内置可迭代对象
const iterableObjects = [
  Array,      // [...]
  String,     // "..."
  Map,        // new Map()
  Set,        // new Set()
  arguments,  // 函数参数
  NodeList    // DOM 查询结果
];
```

### 12.2 `for...of`

`for...of` 遍历可迭代对象的值，`for...in` 遍历对象的可枚举属性键。

```javascript
const arr = ['a', 'b', 'c'];

// for...of：遍历值
for (const value of arr) {
  console.log(value); // 'a', 'b', 'c'
}

// for...in：遍历索引（字符串键）
for (const index in arr) {
  console.log(index); // '0', '1', '2'
}

// for...of 也可用于解构
for (const [key, value] of map) {
  // ...
}
```

### 12.3 迭代器协议（Iterator Protocol）

迭代器对象必须有一个 `next()` 方法，返回 `{ value, done }`。

```javascript
function createRangeIterator(start, end) {
  let current = start;
  return {
    next() {
      if (current <= end) {
        return { value: current++, done: false };
      }
      return { value: undefined, done: true };
    }
  };
}

const iter = createRangeIterator(1, 3);
iter.next(); // { value: 1, done: false }
iter.next(); // { value: 2, done: false }
iter.next(); // { value: 3, done: false }
iter.next(); // { value: undefined, done: true }
```

### 12.4 生成器（Generator）

生成器函数使用 `function*` 声明，内部使用 `yield` 暂停执行。

```javascript
function* numberGenerator() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = numberGenerator();
gen.next(); // { value: 1, done: false }
gen.next(); // { value: 2, done: false }
gen.next(); // { value: 3, done: false }
gen.next(); // { value: undefined, done: true }

// 生成器是可迭代的
for (const num of numberGenerator()) {
  console.log(num); // 1, 2, 3
}

[...numberGenerator()]; // [1, 2, 3]
```

**双向通信**：

```javascript
function* twoWayGenerator() {
  const received = yield 'sent'; // 暂停，等待外部传入值
  yield `Got: ${received}`;
}

const gen = twoWayGenerator();
gen.next();           // { value: 'sent', done: false }
gen.next('hello');    // { value: 'Got: hello', done: false }
```

**惰性计算无限序列**：

```javascript
function* fibonacci() {
  let [a, b] = [0, 1];
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

const fib = fibonacci();
fib.next(); // { value: 0, done: false }
fib.next(); // { value: 1, done: false }
fib.next(); // { value: 1, done: false }

// 配合 for...of 和 break 使用
for (const num of fibonacci()) {
  if (num > 100) break;
  console.log(num);
}
```

**委托生成器**：

```javascript
function* gen1() {
  yield 1;
  yield 2;
}

function* gen2() {
  yield 'a';
  yield* gen1(); // 委托给另一个生成器/可迭代对象
  yield 'b';
}

[...gen2()]; // ['a', 1, 2, 'b']
```

### 12.5 异步迭代器与 `for await...of`（ES2018）

异步迭代器协议与常规迭代器类似，但 `next()` 返回的是 `Promise<{ value, done }>`。任何实现了 `Symbol.asyncIterator` 的对象都可以用 `for await...of` 遍历。

```javascript
// 异步生成器函数
async function* fetchPages(urls) {
  for (const url of urls) {
    const response = await fetch(url);
    yield await response.json();
  }
}

// 使用 for await...of 消费异步迭代器
async function main() {
  const urls = ['/api/page1', '/api/page2'];
  for await (const data of fetchPages(urls)) {
    console.log(data);
  }
}
```

**与 `for...of` 的区别**：
- `for...of` 用于同步可迭代对象（`Symbol.iterator`）
- `for await...of` 用于异步可迭代对象（`Symbol.asyncIterator`），且只能用在 `async` 函数内部

```javascript
// 将同步可迭代对象转为异步迭代
const asyncIterable = {
  [Symbol.asyncIterator]() {
    let i = 0;
    return {
      next: () => {
        if (i >= 3) return Promise.resolve({ done: true });
        return Promise.resolve({ value: i++, done: false });
      }
    };
  }
};

(async () => {
  for await (const num of asyncIterable) {
    console.log(num); // 0, 1, 2
  }
})();
```

---

## 13. 异步编程

### 13.1 Promise 基础

Promise 是异步操作的最终完成（或失败）及其结果值的代理。

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('success');
    // 或 reject(new Error('failed'));
  }, 1000);
});

promise
  .then(value => {
    console.log(value); // "success"
    return value + '!';
  })
  .then(value => {
    console.log(value); // "success!"
  })
  .catch(error => {
    console.error(error);
  })
  .finally(() => {
    console.log('done'); // 无论成功失败都执行
  });
```

**Promise 状态**：
- **pending**：初始状态
- **fulfilled**：操作成功完成
- **rejected**：操作失败
- 状态一旦改变就不可再变

### 13.2 Promise 链与错误处理

```javascript
fetchUser(1)
  .then(user => fetchOrders(user.id))
  .then(orders => {
    // 如果这里抛出异常，会被 catch 捕获
    if (orders.length === 0) throw new Error('No orders');
    return orders[0];
  })
  .then(order => fetchDetails(order.id))
  .catch(error => {
    // 捕获链中任何位置的 reject 或 throw
    console.error(error);
    return { error: true }; // 返回默认值，链继续
  })
  .then(result => {
    // 如果 catch 返回了值，这里会接收到
  });
```

### 13.3 Promise 静态方法

```javascript
// Promise.all：所有 Promise 成功才算成功，有一个失败就整体失败
const [users, orders] = await Promise.all([
  fetchUsers(),
  fetchOrders()
]);

// Promise.race：返回最先完成的那个（无论成功或失败）
const result = await Promise.race([
  fetchData(),
  new Promise((_, reject) => 
    setTimeout(() => reject(new Error('Timeout')), 5000)
  )
]);

// Promise.allSettled：等待所有完成，返回状态数组（ES2020）
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject('error'),
  Promise.resolve(3)
]);
// [
//   { status: 'fulfilled', value: 1 },
//   { status: 'rejected', reason: 'error' },
//   { status: 'fulfilled', value: 3 }
// ]

// Promise.any：返回第一个成功的，全部失败才失败（ES2021）
const first = await Promise.any([fetchA(), fetchB(), fetchC()]);

// Promise.withResolvers（ES2024）
const { promise, resolve, reject } = Promise.withResolvers();
// 等价于：
// let resolve, reject;
// const promise = new Promise((res, rej) => { resolve = res; reject = rej; });
```

### 13.4 async/await（ES2017）

`async`/`await` 是 Promise 的语法糖，让异步代码看起来像同步代码。

```javascript
async function fetchUserData(userId) {
  try {
    const user = await fetchUser(userId);
    const orders = await fetchOrders(user.id);
    return { user, orders };
  } catch (error) {
    console.error('Failed to fetch:', error);
    throw error; // 重新抛出或返回默认值
  }
}

// async 函数总是返回 Promise
fetchUserData(1).then(data => console.log(data));
```

**并发控制**：

```javascript
// 错误：串行执行（慢）
async function slow() {
  const a = await fetchA();
  const b = await fetchB(); // 等待 fetchA 完成才开始
  return [a, b];
}

// 正确：并行执行
async function fast() {
  const [a, b] = await Promise.all([fetchA(), fetchB()]);
  return [a, b];
}
```

### 13.5 事件循环与微任务

理解 Promise 和 `async`/`await` 的执行时机，必须理解 JavaScript 的事件循环。

**执行顺序**：

```javascript
console.log('1');

setTimeout(() => console.log('2'), 0);

Promise.resolve().then(() => console.log('3'));

async function asyncFunc() {
  console.log('4');
  await Promise.resolve();
  console.log('5');
}

asyncFunc();

console.log('6');

// 输出：1, 4, 6, 3, 5, 2
```

**执行时序图**：

```mermaid
flowchart TB
    subgraph 同步执行阶段
        A[console.log('1')]
        B[asyncFunc 调用]
        C[console.log('4')]
        D[await Promise.resolve<br/>暂停, 注册后续代码到微任务队列]
        E[asyncFunc 返回 Promise]
        F[console.log('6')<br/>同步代码结束]
    end

    subgraph 微任务队列
        G[console.log('3')<br/>Promise.then 回调]
        H[console.log('5')<br/>await 后续代码]
    end

    subgraph 宏任务队列
        I[setTimeout 回调<br/>console.log('2')]
    end

    F -->|同步代码执行完毕| G
    G --> H
    H -->|微任务队列清空| I

    style A fill:#90EE90
    style C fill:#90EE90
    style F fill:#90EE90
    style G fill:#87CEEB
    style H fill:#87CEEB
    style I fill:#FFB6C1
```

**执行输出**：`1 → 4 → 6 → 3 → 5 → 2`

**关键规则**：
1. 同步代码最先执行
2. 每个宏任务执行完毕后，会清空当前所有微任务
3. `Promise.then/catch/finally`、`await` 后续代码、MutationObserver 都是微任务
4. `setTimeout`、`setInterval`、I/O 操作是宏任务

---

## 14. 元编程

### 14.1 Proxy

Proxy 用于创建一个对象的代理，拦截并自定义对象的基本操作。

```javascript
const target = { name: 'Alice', age: 25 };

const proxy = new Proxy(target, {
  // 读取属性
  // receiver 是属性访问的原始接收者（通常是 proxy 本身或其继承者）
  // 使用 Reflect.get 传入 receiver，可确保属性若是 getter，其 this 指向正确
  get(target, prop, receiver) {
    if (prop === 'age') {
      return `${target.age} years old`;
    }
    return Reflect.get(target, prop, receiver);
  },
  
  // 设置属性
  set(target, prop, value, receiver) {
    if (prop === 'age' && typeof value !== 'number') {
      throw new TypeError('Age must be a number');
    }
    return Reflect.set(target, prop, value, receiver);
  },
  
  // 判断属性是否存在
  has(target, prop) {
    return prop in target && !prop.startsWith('_');
  },
  
  // 删除属性
  deleteProperty(target, prop) {
    if (prop === 'name') {
      throw new Error('Cannot delete name');
    }
    return Reflect.deleteProperty(target, prop);
  }
});

proxy.age;     // "25 years old"
proxy.age = 'x'; // TypeError
```

### 14.2 常用 Proxy 陷阱（Trap）

| 陷阱 | 触发方式 | 用途 |
|------|---------|------|
| `get` | `obj.prop` / `obj[prop]` | 属性读取拦截、默认值 |
| `set` | `obj.prop = value` | 数据验证、响应式更新 |
| `has` | `prop in obj` | 隐藏私有属性 |
| `deleteProperty` | `delete obj.prop` | 保护属性 |
| `getPrototypeOf` | `Object.getPrototypeOf` | 原型操作 |
| `setPrototypeOf` | `Object.setPrototypeOf` | 原型操作 |
| `ownKeys` | `Object.keys` / `Object.getOwnPropertyNames` / `Reflect.ownKeys` / `for...in` | 过滤属性 |
| `getOwnPropertyDescriptor` | `Object.getOwnPropertyDescriptor` | 属性描述符 |
| `defineProperty` | `Object.defineProperty` | 属性定义拦截 |
| `apply` | `func()` | 函数调用拦截 |
| `construct` | `new Func()` | 构造函数拦截 |

### 14.3 Reflect API

Reflect 是一个内置对象，提供了与 Proxy 陷阱一一对应的静态方法，用于更规范地进行对象操作。

```javascript
// Reflect.get / Reflect.set
Reflect.get(target, 'name');
Reflect.set(target, 'age', 26);

// Reflect.has
Reflect.has(target, 'name'); // true

// Reflect.deleteProperty
Reflect.deleteProperty(target, 'temp');

// Reflect.defineProperty
Reflect.defineProperty(target, 'id', {
  value: 1,
  writable: false,
  configurable: false
});

// Reflect.construct（等同于 new）
const date = Reflect.construct(Date, [2024, 0, 1]);

// Reflect.apply（等同于 Function.prototype.apply）
Reflect.apply(Math.max, null, [1, 5, 3]); // 5
```

**为什么用 Reflect 替代直接操作？**
1. 返回值更合理（如 `Reflect.set` 返回布尔值表示是否成功）
2. 可以作为函数使用，支持函数式编程
3. 与 Proxy 陷阱签名完全一致

### 14.4 实战：响应式系统简化版

```javascript
function reactive(obj) {
  const deps = new Map();
  
  return new Proxy(obj, {
    get(target, key) {
      track(deps, key);
      return Reflect.get(target, key);
    },
    set(target, key, value) {
      const result = Reflect.set(target, key, value);
      trigger(deps, key);
      return result;
    }
  });
}

function track(deps, key) {
  // 收集依赖...
}

function trigger(deps, key) {
  // 触发更新...
}

const state = reactive({ count: 0 });
state.count++; // 自动触发依赖更新
```

---

## 15. 数值扩展

### 15.1 新字面量

```javascript
// 二进制
0b1010; // 10

// 八进制
0o755;  // 493

// 已有十进制和十六进制
0xFF;   // 255
```

### 15.2 新方法

```javascript
// 更可靠的类型判断
Number.isNaN(NaN);        // true
Number.isNaN('NaN');      // false（全局 isNaN 会返回 true）

Number.isFinite(42);      // true
Number.isFinite('42');    // false（全局 isFinite 会返回 true）

Number.isInteger(3);      // true
Number.isInteger(3.14);   // false

Number.isSafeInteger(Number.MAX_SAFE_INTEGER);     // true
Number.isSafeInteger(Number.MAX_SAFE_INTEGER + 1); // false

// 解析整数和浮点数（全局方法的更严格版本）
Number.parseInt('42px');     // 42
Number.parseFloat('3.14px'); // 3.14
```

### 15.3 Math 扩展

```javascript
Math.trunc(3.14);    // 3（去除小数部分）
Math.trunc(-3.14);   // -3

Math.sign(-10);      // -1
Math.sign(10);       // 1
Math.sign(0);        // 0

Math.cbrt(27);       // 3（立方根）

Math.hypot(3, 4);    // 5（√(3²+4²)）

// ES2016 引入的指数运算符（与 Math.pow 行为基本一致）
Math.pow(2, 10);
2 ** 10;             // 语法糖，支持 BigInt：2n ** 10n
```

### 15.4 BigInt（ES2020）

```javascript
const huge = 123456789012345678901234567890n;
const alsoHuge = BigInt('123456789012345678901234567890');

// BigInt 和 Number 不能混用
huge + 1n;        // OK
// huge + 1;      // TypeError

// 比较可以混用（Number 精度有限，超大数值可能因截断而不相等）
const small = 123n;
small == 123;  // true（在 Number 精度范围内）
small === 123; // false（类型不同）
```

---

## 16. Unicode 支持

### 16.1 码点处理

ES6 之前，JavaScript 使用 UCS-2（两字节编码），对四字节字符（如 emoji、部分汉字）处理有问题。

```javascript
// 问题：四字节字符被当作两个字符
'𠮷'.length;           // 2（不是 1！）
'𠮷' === '\uD842\uDFB7'; // true（ surrogate pair）

// ES6 解决方案
String.fromCodePoint(0x20BB7); // "𠮷"
'𠮷'.codePointAt(0);           // 134071 (0x20BB7)

// 正确遍历含有四字节字符的字符串
const str = '𠮷a';
for (const char of str) {
  console.log(char); // "𠮷", "a"
}

// 或者使用展开运算符
[...'𠮷a']; // ["𠮷", "a"]
```

### 16.2 Unicode 正则

```javascript
// u 标志：正确处理四字节 Unicode
/^.$/u.test('𠮷'); // true（没有 u 标志会返回 false）

// 使用 \u{...} 表示码点
/\u{20BB7}/u.test('𠮷'); // true

// u 标志（ES6）+ \p{...}（ES2018）：Unicode 属性转义
/\p{Emoji}/u.test('😀'); // true
/\p{Script=Han}/u.test('中'); // true

// v 标志（ES2024）：支持集合运算与更完善的属性匹配
// /[\p{Decimal_Number}&&\p{ASCII}]/v.test('5'); // true（仅匹配 ASCII 数字）
```

---

## 17. 总结

### 17.1 ES6+ 演进路线

```
ES2015 (ES6)     奠基之年：let/const、箭头函数、Class、Promise、Module、Proxy、Symbol...
ES2016           小版本：Array.prototype.includes、指数运算符 (**)
ES2017           async/await、Object.entries/values、padStart/padEnd、尾逗号
ES2018           对象展开/Rest、异步迭代器、Promise.finally、正则增强
ES2019           Array.flat/flatMap、Object.fromEntries、trimStart/trimEnd
ES2020           BigInt、动态导入、Promise.allSettled、全局 This、可选链、空值合并
ES2021           Promise.any、逻辑赋值运算符、数字分隔符、WeakRef
ES2022           顶层 await、Class 私有字段/方法、Object.hasOwn、at()
ES2023           数组不可变方法 (toSorted 等)、findLast/findLastIndex
ES2024           Object.groupBy / Map.groupBy、Promise.withResolvers、正则 v 标志
```

### 17.2 学习优先级建议

对于已有 JS 基础的开发者，建议按以下优先级掌握：

**第一优先级（日常使用）**：
- `let` / `const` 与块级作用域
- 箭头函数与 `this`
- 模板字面量与解构赋值
- 展开运算符与剩余参数
- Promise 与 async/await
- Module 导入导出

**第二优先级（重要工具）**：
- Class 语法
- Map / Set
- 数组新方法（find、includes、from 等）
- 对象增强（简写、计算属性名）

**第三优先级（进阶能力）**：
- Symbol 与迭代协议
- 生成器
- Proxy / Reflect
- WeakMap / WeakSet

**第四优先级（特定场景）**：
- 标签模板
- BigInt
- Unicode 处理
- 元编程细节
