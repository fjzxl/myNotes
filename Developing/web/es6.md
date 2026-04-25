# es6

## intro

ECMAScript 6（简称 ES6），正式名称为 ECMAScript 2015，于 2015 年 6 月由 ECMA International 正式发布。解决了 JavaScript 长期以来存在的变量提升（hoisting）、回调地狱、缺乏模块化支持、原型继承晦涩等核心痛点。

## 核心理念

第一个核心原则是**向后的兼容性（Backward Compatibility）**。

第二个原则是**语法糖与底层原语的分离（Syntactic Sugar vs. Primitives）**。ES6 的设计者们有意识地区分了"让代码更简洁易读"的语法糖和"提供全新能力"的底层原语。例如，类（Class）语法被广泛认为是语法糖，因为它并不改变 JavaScript 基于原型的继承模型，只是提供了一种更 familiar 的声明方式。而 Proxy 和 Symbol 则是真正全新的底层原语，它们开启了 JavaScript 元编程和对象行为自定义的全新可能性。

第三个原则是**工程化友好（Engineering Friendliness）**。ES6 充分考虑了现代软件工程的最佳实践，引入了大量有利于代码组织、复用和维护的特性。

第四个原则是**为工具链优化（Toolchain Optimization）**。ES6 在设计时就充分考虑了静态分析的需求。ES 模块的静态导入/导出语法使得构建工具能够在编译时确定模块依赖图，从而实现 Tree Shaking（死代码消除）等关键优化。类的声明式语法使得 IDE 和类型检查器更容易推断对象的结构和方法签名。

## 新特性

| 特性类别 | 核心特性 | 解决的问题 | 后续演进 |
|---------|---------|-----------|---------|
| 变量与作用域 | `let`、`const`、块级作用域、TDZ | `var` 提升和函数作用域混乱 | 无重大变化，模式已稳定 |
| 函数增强 | 箭头函数、默认参数、剩余参数、展开运算符 | `this` 绑定混乱、参数处理繁琐 | ES2018 扩展了对象展开 |
| 字符串处理 | 模板字面量、多行字符串、标签模板 | 字符串拼接可读性差、HTML 转义困难 | ES2018 引入 `String.raw` 完善 |
| 解构赋值 | 数组解构、对象解构、嵌套解构、默认值 | 从复杂结构中提取数据代码冗长 | 模式广泛应用于现代代码库 |
| 面向对象 | Class 语法、`extends`、`super`、静态方法 | 原型继承语法晦涩、不符合直觉 | ES2022 增加私有字段 `#` |
| 模块化 | `import`/`export`、默认导出、命名空间导出 | 缺乏官方模块标准、AMD/CommonJS 碎片化 | ES2020 动态导入、`import.meta` |
| 异步编程 | Promise、`then`/`catch`、静态方法 | 回调地狱、错误处理困难 | ES2017 async/await、ES2024 `Promise.withResolvers` |
| 数据结构 | `Map`、`Set`、`WeakMap`、`WeakSet` | 对象键只能是字符串、缺乏集合抽象 | 无重大变化 |
| 新类型 | `Symbol`、Well-Known Symbols、全局注册表 | 属性名冲突、无法定义不可枚举的内部属性 | 持续增加新的 Well-Known Symbols |
| 迭代协议 | `for...of`、可迭代协议、迭代器协议 | `for...in` 遍历属性而非值、自定义迭代困难 | ES2018 异步迭代器 |
| 生成器 | `function*`、`yield`、双向通信 | 无法暂停/恢复函数执行、无限序列表达困难 | ES2018 异步生成器 |
| 元编程 | `Proxy`（13 种 trap）、`Reflect` API | 无法拦截对象的基本操作 | ES2021 `WeakRef`、ES2024 `Atomics` 扩展 |
| 数值扩展 | 二进制/八进制字面量、`Number.isFinite`、Math 新方法 | 数值判断不可靠、缺乏位运算支持 | ES2020 BigInt |
| 数组增强 | `Array.from`、`Array.of`、`find`、`findIndex`、迭代方法 | 类数组转换繁琐、搜索方法缺失 | ES2023 `toSorted`、`toReversed` 等不可变方法 |
| 对象增强 | 简写属性、计算属性名、方法简写、`Object.assign` | 对象字面量重复代码多 | ES2018 Rest/Spread 属性、ES2022 `Object.hasOwn` |
| Unicode 支持 | `String.fromCodePoint`、`codePointAt`、`u` 标志 | 四字节字符处理错误、码点操作缺失 | ES2024 `v` 标志、Well-formed strings |

## 函数增强

### 箭头函数

### 参数

### 展开运算符

## 字符串

### 模板字面量

### 标签模板

## 解构赋值

## 异步编程

## 事件循环

能画出代码的执行时序图，理解 `await` 后的代码为何进入微任务队列。

## symbol

## 元编程

