---
title: "JavaScript 核心知识体系 · 二、引用类型详解"
tags:
  - programming
  - javascript
created: 2026-09-10
updated: 2026-10-01
---

# 二、引用类型详解

> 📚 本文是 [[topics/programming/Web/javascript|JavaScript 核心知识体系]] 的第 2 / 8 章。 上一章：[[topics/programming/Web/javascript/01-language-basics|一、语言基础]] · 下一章：[[topics/programming/Web/javascript/03-core-mechanisms|三、核心运行机制]]


> **本章定位：** 在掌握了基本类型后，本章将深入 JavaScript 的"容器"：对象、数组、函数。这三者是构建任何 JavaScript 程序的基石。
>
> **学习路线：** 对象（键值对容器）→ 数组（有序列表）→ 函数（一等公民与高级特性）→ 其他内置对象 → 实操练习
>
> **核心要理解的概念：** "引用传递"——对象、数组、函数在赋值时传递的不是值本身，而是"指向内存地址的引用"。这是初学者最容易混淆的点，务必通过代码实验来理解。

### 2.1 对象（Object）
#### 创建方式与属性操作

**一句话理解：** 对象是 JavaScript 的"万能容器"，你可以用字面量、构造函数、`Object.create()` 等方式创建它，并随时增删改查其中的属性。

**创建对象的四种方式对比：**

```js
// 1. 对象字面量（最常用）
const obj1 = { name: 'Alice', age: 25 };

// 2. new Object()
const obj2 = new Object();
obj2.name = 'Bob';

// 3. 构造函数 + new（类实例模式）
function Person(name) {
  this.name = name;
}
const obj3 = new Person('Charlie');

// 4. Object.create() — 精确指定原型
const proto = { greet() { return 'hi'; } };
const obj4 = Object.create(proto);
```

| 方式 | 适用场景 | 原型链 |
|------|----------|--------|
| `{}` 对象字面量 | 创建单一、确定的对象 | `__proto__` → `Object.prototype` |
| `new Object()` | 与字面量等价，语义上更"面向对象" | 同上 |
| `new Constructor()` | 需要批量生产同类对象（类实例） | `__proto__` → `Constructor.prototype` |
| `Object.create(proto)` | 精确控制原型链，实现继承 | `__proto__` → 直接指定 `proto` |


**初学者常见错误：**
- ❌ 用 `obj.key` 访问变量键名：`let key = 'name'; obj.key` 访问的是 `"key"` 属性，不是 `"name"`
- ✅ 变量键名应使用方括号：`obj[key]`
- ❌ 删除对象属性用 `delete obj.key` 后以为内存立即释放——`delete` 只是移除属性引用，垃圾回收是异步的
- ❌ 用 `for...in` 遍历数组——会遍历到继承的可枚举属性，且顺序不保证，应使用 `for...of` 或数组方法

#### 构造函数模式 vs Object.create() 模式

**一句话理解：** 构造函数模式适合创建大量相似实例，`Object.create()` 模式适合精确控制原型继承关系，两者本质都是围绕 `prototype` 工作。

这是两种建立原型链的方式，各有适用场景。

**构造函数模式（`new Constructor()`）：**

```js
function Dog(name) {
  this.name = name;
}

// 方法定义在原型上（节省内存，所有实例共享）
Dog.prototype.bark = function() {
  return `${this.name} says woof!`;
};

const myDog = new Dog('Buddy');
const yourDog = new Dog('Max');

myDog.bark();        // 'Buddy says woof!'
yourDog.bark();      // 'Max says woof!'
myDog.__proto__ === Dog.prototype;  // true
myDog instanceof Dog;               // true
```

> 💡 **关于 this：** 你可能好奇 `this.name` 中的 `this` 到底指向谁——在构造函数中它指向新实例，在方法中它指向调用者。但 `this` 的指向规则远比这复杂（严格模式、箭头函数、回调丢失上下文等），详见第 3 章「this 绑定机制」。

**工作流程：**
```
new Dog('Buddy')
    ↓
1. 创建新对象 {}
2. 设置 __proto__ → Dog.prototype
3. 执行构造函数（设置属性）
4. 返回对象
```

**Object.create() 模式：**

```js
const animal = {
  type: 'animal',
  speak() { return 'some sound'; }
};

// 明确指定 cat 的原型是 animal
const cat = Object.create(animal);
cat.name = 'Kitty';

console.log(cat.__proto__ === animal);  // true
cat.speak();               // 'some sound'
// cat instanceof animal;  // ❌ TypeError！instanceof 右侧必须是函数/构造函数
```

**工作流程：**

```
Object.create(animal)
    ↓
1. 创建新对象 {}
2. 设置 __proto__ → animal（明确指定的原型对象）
3. [无构造函数执行]
4. 返回对象
```

对比 `new` 的 4 步，`Object.create()` 只有 3 步——**跳过了构造函数执行**。这意味着：
- 不会执行任何初始化逻辑（如 `this.name = name`）
- 实例创建后属性为空，需要手动赋值（如 `cat.name = 'Kitty'`）
- 更轻量，适合"基于现有对象创建新对象"的组合场景

**核心区别：**

| 对比项 | `new Constructor()` | `Object.create(proto)` |
|--------|-------------------|------------------------|
| 构造函数 | 会被调用 | 不会被调用 |
| 原型指定 | 自动指向 `Constructor.prototype` | 手动指定任意对象 |
| `constructor` 属性 | ✅ 正确指向构造函数 | ⚠️ 取决于原型对象上是否有 `constructor`（普通对象字面量默认指向 `Object`） |
| `instanceof` | ✅ 可用 | ❌ 不可用 |
| 适用场景 | 需要"类"、批量实例化 | 精确继承、对象组合 |

```js
// Object.create() 的 constructor 问题
const cat = Object.create(animal);

// cat 本身没有 constructor 属性，会沿原型链查找：
// cat → animal → Object.prototype → null
// animal 本身也没有 constructor，最终找到 Object.prototype.constructor
console.log(cat.constructor === Object);  // true

// 这就是为什么用 Object.create() 时，实例的 constructor 不指向 "父类"
// 如果需要修正，先定义构造函数，再用 Object.defineProperty 显式添加
function Animal() {}
Object.defineProperty(animal, 'constructor', {
  value: Animal,
  enumerable: false,
  writable: true,
  configurable: true
});
console.log(cat.constructor === Animal);  // true
```

#### `prototype` 与 `__proto__` 的区别

**一句话理解：** `prototype` 是构造函数的"方法仓库"（只有函数有），`__proto__` 是每个对象的"家谱指针"（所有对象都有）。前者用来"存放"共享方法，后者用来"查找"继承的方法。

**生活类比：**
- `prototype` = **模具厂的图纸库**：工厂（构造函数）把公共的模具图纸（共享方法）放在图纸库（prototype）里，所有用这个模具生产出来的产品（实例）都能共享这些图纸
- `__proto__` = **产品上的防伪溯源码**：每个产品（实例）上都贴了一个溯源码（`__proto__`），扫码就能找到生产它的工厂图纸库（prototype）。如果产品本身没有某个功能，就扫码溯源去图纸库里找

这是两个**完全不同**的属性，只是名字长得像，导致大量误解。

| 对比项 | `prototype` | `__proto__` |
|--------|-------------|-------------|
| **谁有** | **普通函数**有（箭头函数没有） | **所有对象**都有（`Object.create(null)` 除外） |
| **作用** | 构造函数用来"存放实例共享的方法" | 对象用来"指向自己的原型，建立查找链路" |
| **方向** | 构造函数 → 原型对象（发方法） | 实例 → 原型对象（找方法） |
| **是否标准** | 标准属性 | 已标准化（ES2015 附录 B），推荐标准写法 `Object.getPrototypeOf()` |

**一句话记住区别：**

> `prototype` 是**构造函数**的属性，用来给实例发方法；
> `__proto__` 是**实例**的属性，用来沿着原型链找方法。

```js
function Dog(name) {
  this.name = name;
}

// ─── prototype：只有函数才有 ───
console.log(Dog.prototype);           // { constructor: f Dog() }
console.log(typeof Dog.prototype);    // 'object'

// 往 prototype 上放方法，所有实例共享
Dog.prototype.bark = function() {
  return `${this.name} says woof!`;
};

// ─── __proto__：每个对象都有 ───
const myDog = new Dog('Buddy');
console.log(myDog.__proto__);         // { constructor: f Dog(), bark: f }

// 实例的 __proto__ 就是构造函数的 prototype
console.log(myDog.__proto__ === Dog.prototype);  // true ✅

// 普通对象也有 __proto__，但没有 prototype
// ⚠️ Object.create(null) 创建的对象没有 __proto__ 属性！
const plainObj = {};
console.log(plainObj.__proto__);      // Object.prototype
console.log(plainObj.prototype);      // undefined ❌（普通对象没有）
```

**原型链查找演示：**

```js
myDog.bark();  // myDog 自身没有 bark，沿 __proto__ 找到 Dog.prototype.bark

// 查找路径可视化：
// myDog.bark
//    ↓ 自身没有，查 __proto__
// myDog.__proto__ === Dog.prototype
//    ↓ 找到了 bark！
// Dog.prototype.bark()
```

**为什么要有两个属性？**

JavaScript 设计之初就分离了这两个角色：
- `Dog.prototype` 是**蓝图仓库**：构造函数说"我的实例们，你们的方法在我这里"
- `myDog.__proto__` 是**导航链路**：实例说"我找不到属性时，去这里问问"

如果没有 `__proto__` 这个链路，引擎就不知道怎么从一个实例找到它的原型方法；如果没有 `prototype`，构造函数就不知道往哪里放共享方法。


**初学者常见错误：**
- ❌ 把 `prototype` 和 `__proto__` 当成同一个东西——前者只在函数上有，后者在所有对象上有
- ❌ 修改实例的 `__proto__` —— 这是非标准遗留属性，且修改它性能极差，应使用 `Object.setPrototypeOf()`（但也很少需要）
- ❌ 给内置对象原型（如 `Array.prototype`）添加方法——会污染所有数组实例，且可能与未来标准冲突
- ✅ 推荐做法：使用 `Object.create()` 或 `class extends` 来建立原型继承关系

#### 三条核心关系（务必记住）

**一句话理解：** `实例.__proto__ === 构造函数.prototype`，这是 JavaScript 原型系统的核心等式，理解了它，原型链就通了。

```
┌─────────────────────────────────────────────────────────────┐
│  1. 构造函数.prototype  =  实例的原型对象                      │
│     Dog.prototype ────────→ { constructor: Dog, bark: fn }   │
│                                                              │
│  2. 实例.__proto__  =  构造函数.prototype                      │
│     myDog.__proto__ ──────→ Dog.prototype                    │
│                                                              │
│  3. 原型对象.constructor  =  构造函数                          │
│     Dog.prototype.constructor ──→ Dog                        │
└─────────────────────────────────────────────────────────────┘
```

```js
// 验证三条核心关系
function Dog(name) {
  this.name = name;
}
Dog.prototype.bark = function() {
  return `${this.name} says woof!`;
};

const myDog = new Dog('Buddy');

// 关系 1：实例.__proto__ === 构造函数.prototype
console.log(myDog.__proto__ === Dog.prototype); // true

// 关系 2：原型对象.constructor === 构造函数
console.log(Dog.prototype.constructor === Dog); // true

// 关系 3：原型链查找
console.log(myDog.bark()); // "Buddy says woof!" —— 自身没有 bark，去原型上找
console.log(myDog.toString()); // 原型链继续向上找到 Object.prototype.toString
```

#### 应用场景选择

**一句话理解：** 选择对象创建方式就像选择交通工具——近路步行（字面量）、多人出行拼车（构造函数）、精确路线导航（Object.create()），按场景选最合适的。

**何时用构造函数模式（`new Foo()`）：**
- 需要批量创建同类对象（"类"的概念）
- 需要使用 `instanceof` 判断引用类型
- 需要 `constructor` 属性指向正确的构造函数
- 方法可以放在原型上共享，节省内存

**何时用 Object.create()：**
- 实现原型继承时（建立任意的原型链）
- 对象组合（mixin 模式）
- 创建具有指定原型的对象（以某个对象为原型，但不触发构造函数）
- 需要跳过构造函数直接建立原型链接

```js
// 三种创建方式对比
// 方式 1：字面量（最常用，简单直接）
const person1 = { name: 'Alice', age: 25 };

// 方式 2：构造函数（批量创建同类对象）
function Person(name, age) {
  this.name = name;
  this.age = age;
}
Person.prototype.greet = function() {
  return `Hi, I'm ${this.name}`;
};
const person2 = new Person('Bob', 30);

// 方式 3：Object.create()（精确控制原型）
// ⚠️ 对象方法建议用普通函数，不要用箭头函数（否则 this 指向外部）
const animal = { speak() { return 'sound'; } };
const dog = Object.create(animal);
dog.speak = function() { return 'woof'; };
console.log(dog.speak()); // "woof" —— 自身有就用自身的，没有才去找原型
```

#### 属性访问与操作

**一句话理解：** 访问对象属性有两种方式——点符号（`obj.key`，简洁但键名固定）和方括号（`obj[key]`，灵活支持变量和特殊字符）。

```js
const user = { firstName: 'Alice', 'last-name': 'Smith' };

// 点号访问（属性名必须是合法标识符）
user.firstName;

// 中括号访问（支持变量和特殊字符）
user['last-name'];
const key = 'firstName';
user[key];

// 属性增删改查
user.age = 25;          // 增 / 改
user.email = undefined; // 值设为 undefined，但属性仍在
delete user.email;      // 真正删除属性
'age' in user;          // true（检查自身 + 原型链）
user.hasOwnProperty('age'); // true（仅检查自身属性）
```

#### 属性描述符与定义属性

**一句话理解：** 属性描述符让你像设置"门禁系统"一样精确控制对象属性——能否读取（enumerable）、能否修改（writable）、能否删除（configurable）。

每个对象属性都由一个**属性描述符**控制其行为：

```js
const obj = {};

// Object.defineProperty 精确控制属性
Object.defineProperty(obj, 'name', {
  value: 'Alice',
  writable: false,       // 不可重新赋值
  enumerable: true,      // 可枚举（for...in / Object.keys）
  configurable: false    // 不可删除，描述符不可再修改
});

obj.name = 'Bob';        // 严格模式下报错，非严格静默失败
console.log(obj.name);   // 'Alice'
```

**属性描述符分类：**

| 类型 | 包含字段 | 说明 |
|------|----------|------|
| **数据描述符** | `value`, `writable` | 保存值的属性 |
| **存取描述符** | `get`, `set` | 通过 getter/setter 访问 |

```js
const user = {
  firstName: 'Alice',
  lastName: 'Smith'
};

Object.defineProperty(user, 'fullName', {
  get() { return this.firstName + ' ' + this.lastName; },
  set(value) {
    [this.firstName, this.lastName] = value.split(' ');
  },
  enumerable: true
});

console.log(user.fullName); // 'Alice Smith'
user.fullName = 'Bob Jones';
console.log(user.firstName); // 'Bob'
```

**一次性定义多个属性：**

```js
Object.defineProperties(user, {
  age: { value: 25, writable: true, enumerable: true },
  id: { value: 1001, writable: false, enumerable: false }
});
```


**初学者常见错误：**
- ❌ 用 `Object.defineProperty` 定义属性时忘记设置 `writable` 和 `configurable`——默认都是 `false`，创建后无法修改和删除
- ❌ 用 `Object.defineProperty` 实现响应式时陷入死循环——在 getter/setter 中访问/修改同一个属性会无限递归
- ❌ 以为 `enumerable: false` 的属性完全不可见——`Object.keys()` 看不到，但 `Object.getOwnPropertyNames()` 可以看到

#### 对象遍历方法对比

**一句话理解：** `for...in` 遍历自身+继承的可枚举属性，`Object.keys` 只遍历自身键名，`Object.entries` 同时拿到键值——根据需求选对工具。

| 方法 | 遍历范围 | 返回类型 | 遍历原型链 |
|------|----------|----------|------------|
| `for...in` | 可枚举的字符串键（含继承） | 键名 | ✅ |
| `Object.keys()` | 自身可枚举的字符串键 | 数组 | ❌ |
| `Object.values()` | 自身可枚举的字符串键值 | 数组 | ❌ |
| `Object.entries()` | 自身可枚举的字符串键值对 | 二维数组 | ❌ |
| `Object.getOwnPropertyNames()` | 自身所有字符串键（含不可枚举） | 数组 | ❌ |
| `Object.getOwnPropertySymbols()` | 自身所有 Symbol 键 | 数组 | ❌ |
| `Reflect.ownKeys()` | 自身所有键（字符串 + Symbol，含不可枚举） | 数组 | ❌ |

```js
const obj = { a: 1, b: 2 };
Object.defineProperty(obj, 'c', { value: 3, enumerable: false });

Object.keys(obj);              // ['a', 'b']
Object.getOwnPropertyNames(obj); // ['a', 'b', 'c']

// 遍历推荐写法
for (const [key, value] of Object.entries(obj)) {
  console.log(key, value);
}
```

> **注意**：`for...in` 会遍历原型链上的可枚举属性，通常需要配合 `hasOwnProperty` 过滤；`Object.keys/values/entries` 只遍历自身属性，是更安全的现代选择。


**初学者常见错误：**
- ❌ 用 `for...in` 遍历数组——会遍历到继承的属性，且顺序不保证，应使用 `for...of`
- ❌ 用 `for...of` 遍历普通对象——对象默认不可迭代，会报错，应使用 `Object.keys()` 或 `Object.entries()`
- ❌ `Object.keys()` 只返回自身的可枚举属性，不包含 `Symbol` 键——需要 `Symbol` 键时用 `Reflect.ownKeys()`

### 2.2 数组（Array）
#### 创建与基础操作

**一句话理解：** 数组是有序的元素队列，支持在头部/尾部增删元素，也能通过索引直接访问和修改任意位置的值。

```js
// 创建数组
const arr1 = [1, 2, 3];
const arr2 = new Array(3);       // [empty × 3] — 创建长度为3的空槽数组，无实际元素
const arr3 = Array.from('abc');  // ['a', 'b', 'c']
const arr4 = Array.of(3);        // [3] — 与 new Array(3) 区别

// 基础操作
arr1.push(4);        // 尾部添加，返回新长度
arr1.pop();          // 尾部删除，返回被删元素
arr1.unshift(0);     // 头部添加，返回新长度
arr1.shift();        // 头部删除，返回被删元素
arr1.splice(1, 1);   // 从索引1删除1个元素
arr1.slice(0, 2);    // 截取 [0,2)，返回新数组（不改变原数组）
arr1.indexOf(2);     // 查找索引，找不到返回 -1
arr1.includes(2);    // 是否包含
arr1.join('-');      // '1-2-3'
```

> `push/pop` 操作尾部速度快（O(1)），`unshift/shift` 操作头部需要整体移动元素（O(n)），大量数据时优先操作尾部。


**初学者常见错误：**
- ❌ `const arr = new Array(3)` 创建的是 `[empty × 3]`（3 个空槽），不是 `[3]` 或 `[undefined, undefined, undefined]`
- ✅ 创建指定长度且填充默认值的数组：`new Array(3).fill(0)` 或 `Array.from({ length: 3 }, () => 0)`
- ❌ 用 `delete arr[0]` 删除数组元素——会留下空槽，`length` 不变，应使用 `splice` 或 `filter`
- ✅ `arr.length = 0` 是清空数组的高效方式（会删除所有元素，length 变为 0）

#### 高级迭代方法（map / filter / reduce / find 等）

**一句话理解：** 数组的高阶方法让你用声明式的方式处理数据——`map` 变形、`filter` 筛选、`reduce` 汇总、`find` 查找，替代繁琐的 `for` 循环。

| 方法 | 作用 | 返回值 | 是否改变原数组 |
|------|------|--------|----------------|
| `map` | 对每个元素执行回调，返回新数组 | 新数组 | ❌ |
| `filter` | 保留满足条件的元素 | 新数组 | ❌ |
| `reduce` | 累积计算为单一值 | 任意类型 | ❌ |
| `find` | 查找第一个满足条件的元素 | 元素 / `undefined` | ❌ |
| `findIndex` | 查找第一个满足条件的索引 | 索引 / `-1` | ❌ |
| `some` | 是否有元素满足条件 | `boolean` | ❌ |
| `every` | 是否所有元素满足条件 | `boolean` | ❌ |
| `forEach` | 遍历执行副作用 | `undefined` | ❌（但回调内可改引用类型） |
| `sort` | 排序 | 原数组（⚠️ 改变原数组） | ✅ |
| `reverse` | 反转 | 原数组（⚠️ 改变原数组） | ✅ |

```js
const nums = [1, 2, 3, 4, 5];

// map — 数据转换
const doubled = nums.map(n => n * 2); // [2, 4, 6, 8, 10]

// filter — 数据筛选
const evens = nums.filter(n => n % 2 === 0); // [2, 4]

// reduce — 数据聚合
const sum = nums.reduce((acc, n) => acc + n, 0); // 15
// ⚠️ 不指定初始值时，空数组调用 reduce 会报错！
const max = nums.reduce((acc, n) => n > acc ? n : acc, -Infinity); // 5

// find — 查找单个元素
const firstEven = nums.find(n => n % 2 === 0); // 2

// 链式调用（函数式风格）
const result = nums
  .filter(n => n > 2)
  .map(n => n * 10)
  .reduce((a, b) => a + b, 0); // 120
```

**sort 的陷阱：**

```js
[2, 10, 5].sort();         // [10, 2, 5] — 默认按字符串 Unicode 排序！
[2, 10, 5].sort((a, b) => a - b); // [2, 5, 10] — 正确数字排序
```


**初学者常见错误：**
- ❌ `forEach` 里用 `return` 想跳出循环——`forEach` 的 `return` 只跳出当前回调，相当于 `continue`，不能终止整个循环
- ✅ 需要提前终止的循环用 `for...of` 配合 `break`，或用 `some`/`every`/`find`
- ❌ `map` 里忘记 `return`——会导致结果数组出现 `undefined`
- ❌ `reduce` 忘记提供初始值——空数组调用会报错，且类型推断可能出错

#### 常见场景（去重 / 扁平化 / 排序 / 分组）

**一句话理解：** 实际开发中数组的四大高频操作——去重（Unique）、扁平化（Flat）、排序（Sort）、分组（Group），掌握它们的实现思路能应对大部分数据处理需求。

```js
const arr = [1, 2, 2, 3, 3, 3];

// 去重
[...new Set(arr)];                    // [1, 2, 3]
arr.filter((v, i, a) => a.indexOf(v) === i); // [1, 2, 3]

// 扁平化
const nested = [1, [2, 3], [4, [5, 6]]];
nested.flat(1);          // [ 1, 2, 3, 4, [ 5, 6 ] ]
nested.flat(Infinity);   // 任意深度

// 排序（不改变原数组的安全写法）
const sorted = [...arr].sort((a, b) => a - b);
// ES2023: arr.toSorted((a, b) => a - b);

// 分组
const people = [
  { name: 'Alice', age: 25 },
  { name: 'Bob', age: 30 },
  { name: 'Charlie', age: 25 }
];
// 💡 ||= 是 ES2021 语法，旧环境请用：acc[p.age] = acc[p.age] || []
const grouped = people.reduce((acc, p) => {
  (acc[p.age] ||= []).push(p);
  return acc;
}, {});
// { 25: [{ name: 'Alice' }, { name: 'Charlie' }], 30: [{ name: 'Bob' }] }
```

### 2.3 函数（Function）
#### 函数声明 / 表达式 / 箭头函数

**一句话理解：** 函数声明会提升（先上车后补票）、函数表达式不会提升（先买票再上车）、箭头函数没有自己的 `this`（借用外部环境的身份）。

```js
// 1. 函数声明 — 存在函数提升
function add(a, b) {
  return a + b;
}

// 2. 函数表达式 — 变量提升，但赋值不提升
const multiply = function(a, b) {
  return a * b;
};

// 3. 箭头函数 — 简洁，没有自己的 this/arguments，不能 new
const subtract = (a, b) => a - b;
const greet = name => `Hello, ${name}`;
const getObj = () => ({ x: 1 }); // 返回对象需加括号

// 4. Function 构造函数（极少使用）
const divide = new Function('a', 'b', 'return a / b');
```

**三种方式的差异速查：**

| 特性 | 函数声明 | 函数表达式 | 箭头函数 |
|------|----------|------------|----------|
| 提升 | ✅ 函数整体提升 | ⚠️ 变量提升，赋值不提升 | ❌ 无提升 |
| 自己的 `this` | ✅ 有 | ✅ 有 | ❌ 继承外层 |
| 自己的 `arguments` | ✅ 有 | ✅ 有 | ❌ 无（用剩余参数） |
| 作为构造函数 | ✅ 可以 | ✅ 可以 | ❌ 不可以 |
| 适用场景 | 通用 | 回调、需要控制提升时 | 短回调、需要固定 this 时 |

#### 默认参数 / 剩余参数 / 参数解构

**一句话理解：** 默认参数让函数更容错（没传值就用默认值），剩余参数让函数接收任意数量的参数，参数解构让传入的对象/数组自动拆包成变量。

```js
// 默认参数
function greet(name = 'Guest') {
  return `Hello, ${name}`;
}
greet(); // 'Hello, Guest'

// 默认参数可以是表达式（惰性求值）
function createUser(name, id = Date.now()) {
  return { name, id };
}

// 剩余参数（真数组，替代 arguments）
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
sum(1, 2, 3, 4); // 10

// 参数解构
function printUser({ name, age = 18 }) {
  console.log(`${name}, ${age}岁`);
}
printUser({ name: 'Alice' }); // 'Alice, 18岁'

// 解构 + 剩余
function printUserRest({ name, ...rest }) {
  console.log(name, rest); // 'Alice' { age: 25, city: 'BJ' }
}
```

#### 一等公民特性（First-Class Citizen）

**一句话理解：** JavaScript 中的函数是"一等公民"——可以像普通变量一样被赋值、传递、返回，这使得回调函数、高阶函数、闭包等高级特性成为可能。

在 JavaScript 中，函数是**一等公民**，意味着函数与其他数据类型（string、number、object 等）享有完全平等的地位。

##### 函数作为参数（回调函数）

```js
const nums = [1, 2, 3];

// 将函数传给另一个函数
nums.map(function(n) { return n * 2; });
nums.map(n => n * 2); // 箭头函数更简洁

// 自定义高阶函数
function withLogging(fn) {
  return function(...args) {
    console.log('调用参数:', args);
    const result = fn(...args);
    console.log('返回结果:', result);
    return result;
  };
}

const add = (a, b) => a + b;
const loggedAdd = withLogging(add);
loggedAdd(2, 3); // 打印参数和结果，返回 5
```

##### 函数作为返回值（闭包 / 工厂函数）

```js
// 工厂函数：根据不同配置返回不同的函数
function makeMultiplier(factor) {
  return function(number) {
    return number * factor;
  };
}
const double = makeMultiplier(2);
const triple = makeMultiplier(3);
double(5); // 10
triple(5); // 15

// 柯里化（Currying）
const curriedAdd = a => b => a + b;
const add5 = curriedAdd(5);
add5(3); // 8
```

> 💡 **深入理解：** 上面 `makeMultiplier` 的示例就是闭包，但闭包的形成条件、内存模型、以及经典陷阱（如循环中的闭包），详见第 3 章「词法作用域与闭包」。

##### 函数作为数据结构成员（对象方法 / 数组元素）

```js
// 对象方法
const calculator = {
  add: (a, b) => a + b,
  subtract: (a, b) => a - b
};
calculator.add(2, 3); // 5

// 函数数组（策略模式雏形）
const strategies = [
  n => n * 2,
  n => n ** 2,
  n => n + 10
];
strategies.forEach(fn => console.log(fn(5))); // 10, 25, 15
```

##### 函数的属性与方法（name / length / 自定义属性）

```js
function greet(name) { return 'Hello ' + name; }

// 内置属性
greet.name;    // 'greet'（函数名）
greet.length;  // 1（形参个数，剩余参数不计入）

// 自定义属性（可用于缓存、元数据等）
greet.version = '1.0';
greet.description = '问候函数';
console.log(greet.version); // '1.0'

// 函数方法
greet.call(null, 'Alice');    // 指定 this 调用
greet.apply(null, ['Alice']); // 以数组传参调用
const bound = greet.bind(null, 'Bob'); // 预设参数
bound(); // 'Hello Bob'
```

#### 高阶函数与函数式编程基础

**一句话理解：** 高阶函数就是"函数的函数"——接收函数作为参数或返回函数的函数，它是函数式编程的基石，让代码更抽象、更可复用。

**高阶函数（Higher-Order Function）**：接收函数作为参数，或返回函数的函数。

```js
// compose：从右向左组合多个函数
const compose = (...fns) => x => fns.reduceRight((v, f) => f(v), x);

// pipe：从左向右组合
const pipe = (...fns) => x => fns.reduce((v, f) => f(v), x);

// 使用
const trim = s => s.trim();
const toUpper = s => s.toUpperCase();
const addPrefix = s => `ID:${s}`;

const format = pipe(trim, toUpper, addPrefix);
format('  alice  '); // 'ID:ALICE'
```

**纯函数与副作用：**

```js
// ❌ 非纯函数：依赖外部状态，产生副作用
let count = 0;
function increment() {
  count++;       // 修改外部状态
  console.log(count); // I/O 副作用
}

// ✅ 纯函数：相同输入始终产生相同输出，无副作用
function add(a, b) {
  return a + b;  // 只依赖参数，不修改外部状态
}
```

### 2.4 其他内置对象
#### Date / RegExp / Math

**一句话理解：** `Date` 处理时间、`RegExp` 处理文本模式匹配、`Math` 提供数学计算工具——这三个内置对象覆盖了开发中最常见的辅助计算需求。

```js
// Date
const now = new Date();
now.getFullYear();   // 2026（年）
now.getMonth();      // 3（0 起始，4 月返回 3）
now.getDate();       // 23（日期）
now.getTime();       // 时间戳（毫秒）
Date.now();          // 当前时间戳（快捷方法）

// RegExp
const emailRegex = /^[\w.-]+@[\w.-]+\.\w+$/;
emailRegex.test('alice@example.com'); // true
'abc123'.replace(/\d+/g, '-');        // 'abc-'

// Math
Math.floor(3.7);   // 3
Math.ceil(3.2);    // 4
Math.round(3.5);   // 4
Math.random();     // [0, 1) 随机数
Math.max(1, 5, 3); // 5
Math.min(...[1, 5, 3]); // 1
```

#### Map / Set / WeakMap / WeakSet

**一句话理解：** `Map` 是"升级版对象"（支持任意类型键），`Set` 是"自动去重数组"，`WeakMap`/`WeakSet` 是"不阻止垃圾回收的轻量版"——它们各自解决普通对象和数组无法处理的问题。

**何时使用：**
- `Map`：键名需要是对象/函数，或需要保持插入顺序且频繁增删
- `Set`：需要去重，或需要高效判断"某个值是否存在"
- `WeakMap`：给对象附加私有数据，且不希望这个数据阻止对象被回收
- `WeakSet`：标记某些对象"是否被处理过"，不影响垃圾回收

| 类型 | 键类型 | 可迭代 | 元素唯一性 | 垃圾回收 |
|------|--------|--------|------------|----------|
| `Map` | 任意类型 | ✅ | 键值对 | 强引用 |
| `Set` | 值本身 | ✅ | 值唯一 | 强引用 |
| `WeakMap` | 仅对象 | ❌ | 键值对 | 弱引用（可被 GC） |
| `WeakSet` | 仅对象 | ❌ | 值唯一 | 弱引用（可被 GC） |

```js
// Map — 任意类型作为键
const map = new Map();
map.set('name', 'Alice');
map.set({ id: 1 }, 'objKey');
map.get('name');        // 'Alice'
map.has('name');        // true
map.delete('name');
map.size;               // 1

// Set — 自动去重
const set = new Set([1, 2, 2, 3]);
set.add(4);
set.has(2); // true
[...set];   // [1, 2, 3, 4]

// WeakMap — 适合私有数据存储，不阻止垃圾回收
const cache = new WeakMap();
const obj = { data: 'sensitive' };
cache.set(obj, 'cached value');
// 当 obj 不再被引用时，WeakMap 中的条目会被自动清理
```

#### Symbol 与 BigInt 应用场景

**一句话理解：** `Symbol` 是"永远不会撞名的身份证"，`BigInt` 是"能算天文数字的计算器"——它们分别解决了属性名冲突和超大整数精度问题。

**Symbol：** 创建唯一标识符，避免属性名冲突。

```js
const id = Symbol('id');
const user = { name: 'Alice', [id]: 1001 };

// Symbol 属性不会被常规遍历捕获
Object.keys(user);      // ['name']
Object.getOwnPropertySymbols(user); // [Symbol(id)]

// 全局 Symbol 注册表
const globalId = Symbol.for('app.id');
Symbol.for('app.id') === globalId; // true

// 内置 Symbol 用于元编程
const obj = {
  [Symbol.toPrimitive](hint) {
    if (hint === 'number') return 42;
    return 'string';
  }
};
+obj;       // 42
String(obj); // 'string'
```

**BigInt：** 处理超出 `Number.MAX_SAFE_INTEGER`（`9007199254740991`）的大整数。

```js
const huge = 9007199254740993n; // 数字后加 n
const alsoHuge = BigInt('9007199254740993');

huge + 1n;  // ✅ BigInt 之间运算
// huge + 1; // ❌ TypeError: Cannot mix BigInt and other types

// 应用场景：ID、时间戳、加密货币计算等
```

### 🛠️ 实操：数据结构与算法练习

#### 用纯数组方法实现一个迷你 Lodash（chunk / groupBy / uniq / flattenDeep）

**核心思路：** 这四个函数涵盖了数组处理中最常见的模式。

| 函数 | 作用 | 关键实现思路 |
|------|------|-------------|
| `chunk` | 将数组拆分为指定大小的子数组 | `slice` 按范围切分，循环遍历 |
| `groupBy` | 按条件将数组成员分组 | `reduce` 累积聚合，键作为分组依据 |
| `uniq` | 去除数组中的重复元素 | `Set` 的天然去重特性，或 `filter + indexOf` |
| `flattenDeep` | 深度扁平化数组 | 递归或 `reduce` 展平，判断是否为数组决定是否继续 |

**思考方向：** 先用最直观的方式实现，再思考如何用更高级的数组方法简化。重点理解 `reduce` 在累积场景（分组、扁平）中的灵活性。

**实现代码：**

```js
const _ = {
  chunk(array, size = 1) {
    const result = [];
    for (let i = 0; i < array.length; i += size) {
      result.push(array.slice(i, i + size));
    }
    return result;
  },

  groupBy(array, iteratee) {
    const func = typeof iteratee === 'function' ? iteratee : (item) => item[iteratee];
    return array.reduce((result, item) => {
      const key = func(item);
      if (!result[key]) result[key] = [];
      result[key].push(item);
      return result;
    }, {});
  },

  uniq(array) {
    return [...new Set(array)];
  },

  flattenDeep(array) {
    return array.reduce((result, item) => {
      return result.concat(Array.isArray(item) ? _.flattenDeep(item) : item);
    }, []);
  }
};

// 使用示例
_.chunk([1, 2, 3, 4, 5], 2);              // [[1, 2], [3, 4], [5]]
_.groupBy([6.1, 4.2, 6.3], Math.floor);  // { 4: [4.2], 6: [6.1, 6.3] }
_.uniq([1, 2, 2, 3, 3, 3]);              // [1, 2, 3]
_.flattenDeep([1, [2, [3, [4]], 5]]);    // [1, 2, 3, 4, 5]
```

---

#### 实现一个支持链式调用的计算器对象（add / subtract / multiply / divide / value）

**核心思路：** 链式调用的关键是每个操作方法返回 `this`（自身引用），使下一个方法得以继续调用。

```js
// 假设初始值为 0
calculator.add(5).multiply(3).subtract(2).value()  // ((0 + 5) * 3 - 2) = 13
```

**实现要点：**
- **两种实现方式**：返回 `this`（修改原对象）或返回新实例（不可变风格）
- **存储中间值**：维护一个私有结果变量
- **`value()` 作为终止操作**：返回当前计算结果，结束链式调用
- **防御性检查**：除法时除数不能为 0

**思考方向：** 理解"fluent API"的设计理念。`value()` 是终端方法，它不返回 `this` 而是返回具体值，标志链式调用的结束。

**实现代码：**

```js
class Calculator {
  constructor(initialValue = 0) {
    this._value = initialValue;
  }

  add(n) {
    this._value += n;
    return this;
  }

  subtract(n) {
    this._value -= n;
    return this;
  }

  multiply(n) {
    this._value *= n;
    return this;
  }

  divide(n) {
    if (n === 0) throw new Error('Division by zero');
    this._value /= n;
    return this;
  }

  // ⚠️ 终止操作：返回数值，调用后不可继续链式调用
  value() {
    return this._value;
  }
}

// 使用
const calc = new Calculator();
calc.add(5).multiply(3).subtract(2).value(); // 13
```

---

#### 用 Map + Set 实现一个简单的数据去重与频次统计工具

**核心思路：** Map 和 Set 是处理这类问题的高效数据结构。

| 数据结构 | 在本题中的作用 |
|----------|----------------|
| `Set` | 天然维护唯一性，去重场景直接使用 |
| `Map` | 键值对结构，适合存储"元素 → 出现次数"的映射 |

**两种常见场景：**
1. **去重**：直接使用 `Set` 即可 `[...new Set(arr)]`
2. **频次统计**：用 `Map` 以元素为键，次数为值，遍历数组累加

**思考方向：** 何时用 `Map` 而非普通对象？当键可能是非字符串类型（如对象、数组）时，`Map` 是更安全和可靠的选择。此外 `Map` 保证键值对的有序遍历。

**进阶扩展：** 可以进一步封装为通用工具，支持传入自定义去重规则或统计函数。

**实现代码：**

```js
class FrequencyCounter {
  constructor() {
    this.map = new Map();
  }

  // 统计频次
  count(array, keyFn = (x) => x) {
    this.map.clear();
    for (const item of array) {
      const key = keyFn(item);
      this.map.set(key, (this.map.get(key) || 0) + 1);
    }
    return this;
  }

  // 获取频次
  get(key) {
    return this.map.get(key) || 0;
  }

  // 去重（支持自定义键函数）
  static unique(array, keyFn = (x) => x) {
    const seen = new Set();
    return array.filter((item) => {
      const key = keyFn(item);
      if (seen.has(key)) return false;
      seen.add(key);
      return true;
    });
  }

  // 获取所有结果
  entries() {
    return [...this.map.entries()];
  }
}

// 使用
const freq = new FrequencyCounter();
freq.count(['a', 'b', 'a', 'c', 'b', 'a']);
freq.get('a'); // 3

// 对象数组按属性去重
const users = [{ id: 1, name: 'A' }, { id: 2, name: 'B' }, { id: 1, name: 'C' }];
FrequencyCounter.unique(users, (u) => u.id);
// [{ id: 1, name: 'A' }, { id: 2, name: 'B' }]
```

> **本章小结：** 我们深入了解了对象、数组、函数的创建与操作方式，理解了原型、`prototype` 与 `__proto__` 的区别，以及数组的各种实用方法和函数式编程基础。
>
> **下一章预告：** 当你能熟练操作对象和函数后，接下来要理解的是它们背后的运行机制——执行上下文、作用域链、闭包、this 绑定和原型链继承。这些"内功"将帮助你真正读懂任何 JavaScript 代码。
