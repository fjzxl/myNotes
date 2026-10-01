---
title: TypeScript 入门教程
tags:
  - programming
  - typescript
created: 2026-09-10
updated: 2026-10-01
---
# TypeScript 入门教程

> 面向对象：已有 JavaScript（ES6+）基础，希望系统掌握 TypeScript 核心类型系统的开发者。
> 前置知识：[[topics/programming/Web/es6]]、[[topics/programming/Web/javascript]]
> 进阶篇：[[topics/programming/Web/typescript/type-system]] —— 结构化类型、型变、条件类型、infer、类型体操
> 导航：[[notes/MOC - programming]] · 推荐顺序：JavaScript → ES6+ → 本文 → [[topics/programming/Web/typescript/interface]]（接口专题）→ [[topics/programming/Web/typescript/type-system]]

> **示例说明**：各代码块是独立的小例子，不是可直接拼接成一个 `.ts` 文件的完整程序；不同小节可能重复使用 `User`、`Shape` 等名称。

## 目录

| 章节 | 内容 |
|------|------|
| [1. 引言](#1-引言) | TypeScript 是什么、为什么用、快速上手 |
| [2. 基本类型注解](#2-基本类型注解) | 原始类型、数组/元组、函数、联合与交叉、别名、特殊类型、断言、枚举 |
| [3. 访问修饰符](#3-访问修饰符) | `public`/`private`/`protected`/`readonly`、ES 私有字段 |
| [4. 参数属性](#4-参数属性) | 构造函数参数属性简写 |
| [5. 抽象类](#5-抽象类) | `abstract` 类与方法、与接口的对比 |
| [6. 接口](#6-接口) | 对象形状、继承、实现、声明合并、interface vs type |
| [7. 泛型](#7-泛型) | 泛型函数/类/接口、约束、默认类型、`keyof` |
| [8. 类型收窄与高级类型操作](#8-类型收窄与高级类型操作) | 类型守卫、可辨识联合、条件类型、映射类型、模板字面量类型 |
| [9. 工具类型](#9-工具类型) | 内置工具类型分类详解与手写实现 |
| [10. 工程配置与实践](#10-工程配置与实践) | tsconfig 核心选项、类型声明、渐进迁移 |
| [11. 总结](#11-总结) | 学习优先级建议 |
| [附录：速查表](#附录速查表) | 常用类型注解写法、内置工具类型一览 |
| [参考资料](#参考资料) | 书籍与官方文档 |

---

## 1. 引言

### 1.1 TypeScript 是什么

TypeScript（简称 TS）是微软开发的 JavaScript **超集**：它沿用 JavaScript 语法，并增加**静态类型系统**。已有 JavaScript 通常可以渐进迁移；开启严格检查后，类型检查器仍可能报告原有代码中的问题。常见流程是由 `tsc` 或构建工具把 TS 转成 JavaScript，并在开发阶段进行类型检查；类型注解本身不会进入运行时，但枚举、参数属性等 TS 特性可能生成 JavaScript 代码。

三个关键定位：

- **兼容 JS 语法**：迁移成本低，JS 项目可以渐进式改造
- **类型信息会擦除**：类型注解不改变运行时行为；少数 TS 语法（如 `enum`、参数属性）会生成运行时代码
- **渐进式**：`any`（或逐步收紧的编译选项）允许新旧代码长期共存

#### 从 JavaScript 过渡：代码照常运行，类型先帮你检查

TypeScript 写的是 JavaScript 程序，类型注解是额外的开发期约束。下面两段的运算逻辑相同；差别在于 TS 会先拒绝不符合声明的调用，编译后并不会给乘法加上运行时类型判断。

```javascript
// JavaScript：乘法会把数字字符串隐式转换为数字
function double(value) {
  return value * 2;
}

double('3'); // 6
```

```typescript
function double(value: number): number {
  return value * 2;
}

double(3);                 // OK
// double('3');            // 类型错误：string 不是 number
double(Number('3'));       // OK：显式转换仍由 JavaScript 在运行时执行
```

因此，TS 类型既不会替 JavaScript 做隐式转换，也不会自动校验运行时值；它让调用约定在代码运行前可见。想看对象形状如何写成接口，见 [[topics/programming/Web/typescript/interface]]。

### 1.2 为什么用 TypeScript

| 痛点 | TS 的解决方式 |
|------|--------------|
| 拼写错误、`undefined` 访问只能在运行时发现 | 编译期类型检查直接报错 |
| 重构靠全局搜索，改一处崩一片 | 改类型/重命名字段，所有不兼容处立即标红 |
| IDE 补全靠猜 | 类型即文档，补全、跳转、参数提示精确到字段 |
| 团队协作靠口头约定数据结构 | 接口/类型是机器检查的"强制契约" |
| 第三方库 API 用错 | `.d.ts` 声明文件提供精确的函数签名 |

**同时要保持清醒**：TS 只做**编译期**检查，运行时收到的外部数据（HTTP 响应、用户输入）依然是不可信的，边界处需要运行时校验（zod、valibot 等）配合。

### 1.3 快速上手

```bash
# 在项目中安装编译器（便于团队固定版本）
npm install -D typescript

# 编译：生成 intro.js
npx tsc intro.ts

# 指定目标版本与严格模式
npx tsc intro.ts --target es2020 --strict

# 为项目生成 tsconfig.json（后续命令可直接使用项目配置）
npx tsc --init --strict

# 监听模式
npx tsc --watch
```

实际项目一般不直接敲 `tsc`，而是用构建工具链：

- **Vite**：只转译、不做类型检查；Vite 7 及之前版本默认用 esbuild，Vite 8 默认用 Oxc，类型检查应另跑 `tsc --noEmit`
- **tsx / ts-node**：可直接运行 TS 脚本；tsx 通常只转译，ts-node 默认会做类型检查（除非启用 `transpileOnly`）
- **Node.js 原生运行**：22.18+ / 23.6+ 默认以类型擦除方式运行 `.ts`；这种模式只接受可擦除语法，不检查类型、不读取 `tsconfig.json`、不支持 `.tsx`，也不能处理需要生成 JavaScript 的语法（如 `enum`、参数属性）

```typescript
// intro.ts —— 第一段 TS 代码
function greet(name: string): string {
  return `Hello, ${name}!`;
}

greet('TS');  // OK
// greet(42); // 编译错误：Argument of type 'number' is not assignable
```

---

## 2. 基本类型注解

### 2.1 原始类型

```typescript
let id: number = 1;
let name: string = 'Alice';
let ok: boolean = true;
let u: undefined = undefined;
let n: null = null;
let big: bigint = 100n;        // target 需 ≥ es2020
let sym: symbol = Symbol('k');

// 类型推断：声明时初始化可省略注解，TS 自动推断
let count = 0;      // 推断为 number
let msg = 'hi';     // 推断为 string
// 函数返回值同样会被推断，多数情况下无需手写
```

**建议**：能被准确推断的变量注解和函数返回类型通常不必重复书写。独立函数的参数通常需要注解；回调参数等若已有上下文类型，TS 可以自动推断，无需再写一遍。

### 2.2 数组与元组

```typescript
// 数组：两种等价写法
let nums: number[] = [1, 2, 3];
let strs: Array<string> = ['a', 'b'];  // 泛型写法

// 元组：长度固定、各位置类型固定
let point: [number, number] = [1, 2];
let person: [name: string, age: number] = ['Alice', 25]; // 具名元组，可读性更好

// 可选元素与剩余元素
let maybe: [number, string?] = [1];
let row: [id: number, ...tags: string[]] = [7, 'a', 'b'];

// 只读元组：不可 push/修改
const size: readonly [number, number] = [1920, 1080];

// 注意：数组注解不会约束"内容结构"
// let users: object[] 什么对象都能放 —— 需要结构约束时用接口/类型别名（见第 6 节）
```

### 2.3 对象类型

```typescript
// 内联对象类型：属性用 ; 或 , 分隔
let user: { name: string; age: number } = { name: 'Alice', age: 25 };

// 可选属性（age 可以不传）
let profile: { name: string; age?: number } = { name: 'Bob' };

// 只读属性：初始化后不可再赋值
let cfg: { readonly host: string } = { host: 'localhost' };
// cfg.host = '127.0.0.1'; // 错误

// 未知的属性多写会直接报错（对象字面量的"多余属性检查"）
// let u2: { name: string } = { name: 'A', extra: 1 }; // 错误：extra 不存在
```

### 2.4 函数类型

```typescript
// 参数与返回值注解（返回值通常可推断，省略）
function add(a: number, b: number): number {
  return a + b;
}

// 箭头函数
const pow = (base: number, exp: number): number => base ** exp;

// 函数类型的变量
let op: (a: number, b: number) => number;
op = add;
op = (x, y) => x * y; // 上下文推断出参数类型

// 可选参数、默认参数、剩余参数
function greet(name: string, greeting = 'Hello', ...tags: string[]) {
  return `${greeting}, ${name}${tags.length ? ` (${tags.join(',')})` : ''}`;
}

// 可选参数与联合类型：name? 等价于 name: string | undefined
function log(id?: number) {}
function log2(id: number | undefined) {} // 调用时必须显式传一个参数

// 函数重载：同一函数按参数形态给出不同签名
function parse(input: string): number;
function parse(input: number): string;
function parse(input: string | number) {
  return typeof input === 'string' ? Number(input) : String(input);
}
const a = parse('42');   // a: number
const b = parse(42);     // b: string
```

### 2.5 联合类型与字面量类型

```typescript
// 联合类型：值满足任一成员类型即可 —— "或"（并集；此处 string 与 number 互斥）
type ID = string | number;

function printId(id: ID) {
  // 使用前必须收窄（见第 8 节），否则只能访问公共成员
  if (typeof id === 'string') console.log(id.toUpperCase());
  else console.log(id.toFixed(0));
}

// 字面量类型：值被限定为具体的几个取值 —— 建模"状态机"的利器
type Status = 'idle' | 'loading' | 'success' | 'error';
let status: Status = 'idle';
// status = 'done'; // 错误
```

**交叉类型**与联合相反，是"既要又要"（交集）：值必须**同时满足**所有成员类型。

```typescript
type Named = { name: string };
type Aged  = { age: number };
type Person = Named & Aged; // { name: string; age: number }
const p: Person = { name: 'Alice', age: 25 };

// 用途一：混入 —— 在既有类型上追加一组字段
type WithTimestamp<T> = T & { createdAt: Date; updatedAt: Date };

// 用途二：交叉两个函数类型，得到可按输入选择的调用签名
type Formatter =
  ((input: string) => string) &
  ((input: number) => number);
declare const format: Formatter;
const s1: string = format('hi'); // 按实参类型选择签名
const n1: number = format(42);
// format(true); // 错误：没有 boolean 签名
```

**交叉的三个细节**（容易踩坑）：

1. **交叉是对每个属性取交集**——声明交叉类型时通常不会因属性冲突立即报错；冲突属性会变成 `never`，错误往往要到构造或使用该属性时才暴露：

```typescript
type StrBox = { value: string };
type NumBox = { value: number };
type BadBox = StrBox & NumBox;
// BadBox['value'] 的类型是 string & number = never
// bad.value 的值无法正常构造或使用；交叉类型声明本身不会指出冲突来源
```

2. **`interface extends` 多继承遇到同样的冲突会直接编译报错**。所以组合"会各自演化的接口"时优先 `extends`，让冲突及早暴露；`&` 更适合给现成类型混入一次性字段：

```typescript
interface IStr { value: string }
interface INum { value: number }
// interface IBad extends IStr, INum {} // 编译错误：属性 'value' 类型不兼容
```

3. **对联合满足分配律**：`(A | B) & C = (A & C) | (B & C)`——交集"穿过"联合的每一支。类似的逐成员处理思想在条件类型中成为分发律（见 [8.3](#83-条件类型与-infer)）；集合论视角详见 [[topics/programming/Web/typescript/type-system]] 第 2、4 节。

将多个接口形状合并为交叉类型，或将接口组成可辨识联合的示例见 [[topics/programming/Web/typescript/interface]]。

### 2.6 类型别名 `type`

```typescript
// type 给任何类型起名字：对象、联合、函数、元组、字面量……
type Point = { x: number; y: number };
type Handler = (e: Event) => void;
type Pair<T> = [T, T];
type Direction = 'up' | 'down';

const from: Point = { x: 0, y: 0 };
const to: Point = { x: 1, y: 1 };
const dist = (a: Point, b: Point): number =>
  Math.hypot(b.x - a.x, b.y - a.y);
```

`type` 与 `interface` 的详细对比见 [6.5](#65-interface-与-type-怎么选)。

### 2.7 特殊类型：any / unknown / void / never

| 类型 | 含义 | 使用建议 |
|------|------|---------|
| `any` | 关闭类型检查，可赋给任何类型、可做任何操作 | 能不用就不用；它会"传染"给接触到的每个变量 |
| `unknown` | 安全版 `any`：可以接收任何值，但**使用前必须收窄** | 处理外部输入的默认选择 |
| `void` | 函数没有有意义的返回值 | 返回值类型；变量几乎不用 |
| `never` | 永远不会有的类型：抛错、死循环、穷尽分支的兜底 | 用于穷尽性检查（见 8.2） |

```typescript
// any vs unknown
let a: any = getData();
a.foo.bar;            // 不检查，运行时可能炸

let b: unknown = getData();
// b.foo;             // 错误：unknown 使用前必须收窄
if (typeof b === 'string') console.log(b.toUpperCase()); // OK

// never 与穷尽检查
function unreachable(): never {
  throw new Error('unreachable');
}

type Shape = { kind: 'circle'; r: number } | { kind: 'square'; s: number };
function area(s: Shape): number {
  switch (s.kind) {
    case 'circle': return Math.PI * s.r ** 2;
    case 'square': return s.s ** 2;
    default: {
      const _exhaustive: never = s; // 若将来加了新 kind 而没处理，这里编译报错
      return _exhaustive;
    }
  }
}
```

`null` 与 `undefined`：在 `strictNullChecks`（严格模式默认开启）下，它们是独立的类型，只能显式赋值给包含它们的类型。**务必开启严格模式**，这是 TS 价值最大的一项配置。

### 2.8 类型断言与非空断言

类型断言是"**我比编译器更清楚这个值的类型**"的声明。它不做运行时转换或验证，并绕过相应的静态检查；若断言类型与原类型完全不相关，编译器仍可能拒绝，需要先转为 `unknown`。因此它是危险的逃生口，不是数据校验。

```typescript
// as 断言：getElementById 的类型是 HTMLElement | null；需自行确认元素存在且确实是 canvas
const canvas = document.getElementById('main') as HTMLCanvasElement;

// 双重断言：类型不相容时需要经过 unknown 中转 —— 通常意味着设计有问题
const user = JSON.parse(raw) as unknown as User;

// 非空断言 !：告诉编译器"这里不可能是 null/undefined"
const first = list.find(x => x.id === target)!.name;

// as const：将字面量保留为最窄类型，并把属性视为只读（不等于运行时 Object.freeze）
const config = { host: 'localhost', port: 8080 } as const;
// 类型：{ readonly host: "localhost"; readonly port: 8080 }
```

**原则**：断言应该是最后手段。优先收窄（第 8 节），其次运行时校验，实在不行才 `as`。

### 2.9 枚举 enum

```typescript
// 数字枚举：默认从 0 自增，支持反向映射
enum Direction { Up, Down, Left, Right }
Direction.Up;    // 0
Direction[0];    // 'Up'（反向映射，仅数字枚举有）

// 字符串枚举：无反向映射，但调试时可读，更推荐
enum Status {
  Active = 'ACTIVE',
  Inactive = 'INACTIVE',
}

// const enum：编译时内联，不生成运行时对象
const enum Fast { A = 1, B = 2 }
const x = Fast.A; // 编译产物只有 const x = 1 /* Fast.A */
// const enum 会在编译时内联；跨包发布时可能因声明与运行时代码版本不一致而出问题。
// 使用单文件转译工具或发布库时，应先确认工具链对 const enum 的处理方式。
```

**常见替代方案**：用 `as const` 对象 + 字面量联合。对象本身仍是运行时值；生成的 JavaScript 就是这个普通对象，不会额外生成枚举对象或数字枚举的反向映射：

```typescript
const DIRECTION = {
  Up: 'UP',
  Down: 'DOWN',
} as const;

type Direction = keyof typeof DIRECTION;   // 'Up' | 'Down'
type DirectionValue = (typeof DIRECTION)[Direction]; // 'UP' | 'DOWN'
```

---

## 3. 访问修饰符

TS 在 ES Class 之上提供 `public`、`private`、`protected` 三个访问修饰符；访问限制由**编译期检查**。修饰符本身会擦除，但字段仍可能作为普通 JavaScript 属性存在，所以 TS `private` 不等于运行时私有；运行时私有字段见下文的 ES `#`。

| 修饰符 | 类内部 | 子类 | 实例外部 |
|--------|:------:|:----:|:--------:|
| `public`（默认） | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ❌ |
| `private` | ✅ | ❌ | ❌ |
| `readonly` | 只读，初始化后不可再赋值 | — | — |

```typescript
class Account {
  public id: number;           // 默认就是 public，可省略
  private balance: number;     // 仅类内部可访问
  protected owner: string;     // 类内部 + 子类
  readonly createdAt: Date;    // 初始化后不可变

  constructor(id: number, balance: number, owner: string) {
    this.id = id;
    this.balance = balance;
    this.owner = owner;
    this.createdAt = new Date();
  }

  deposit(amount: number): void {
    if (amount <= 0) throw new Error('invalid amount');
    this.balance += amount;    // 类内部 OK
  }

  get balanceValue(): number {  // getter 提供只读出口
    return this.balance;
  }
}

const acc = new Account(1, 100, 'Alice');
acc.deposit(50);
// acc.balance;        // 编译错误：属性"balance"为私有属性
// acc.owner = 'Bob';  // 编译错误：属性"owner"受保护
```

**TS `private` vs ES `#` 私有字段**：

```typescript
class Wallet {
  #secret = 42;         // ECMAScript 私有字段：运行时强私有
  getSecret() { return this.#secret; }
}

const w = new Wallet();
// (w as any).secret        // undefined —— 字段名在运行时就被封装了
// (w as any)['#secret']    // 合法的普通字符串键访问，结果为 undefined
// w.#secret               // 类外直接访问私有标识符会报语法错误
```

| | TS `private` | ES `#field` |
|--|-------------|-------------|
| 检查时机 | 仅编译期 | 编译期 + **运行时**（真正不可访问） |
| 编译产物 | 普通属性 | `WeakMap`/原生私有字段 |
| 子类访问 | `protected` 可放行 | 永远不允许 |
| 选择建议 | 一般业务代码 | 确需运行时隔离（库、安全敏感数据） |

### 3.1 类的类型：类既是值也是类型

```typescript
class Point {
  x: number;
  y: number;
  constructor(x: number, y: number) {
    this.x = x;
    this.y = y;
  }
}

const p1: Point = new Point(1, 2); // 类名可以作类型注解（实例的类型）
// 结构化：只要形状匹配即可赋值，不要求显式 implements
const p2: Point = { x: 0, y: 0 };  // OK —— TS 是结构化类型系统
```

---

## 4. 参数属性

参数属性（Parameter Properties）是"声明字段 + 构造函数赋值"的语法糖：在构造函数参数前加修饰符，TS 会自动完成字段声明和赋值。

```typescript
// 完整写法
class UserFull {
  public name: string;
  private password: string;
  readonly id: number;
  constructor(name: string, password: string, id: number) {
    this.name = name;
    this.password = password;
    this.id = id;
  }
}

// 参数属性简写：完全等价
class User {
  constructor(
    public name: string,
    private password: string,
    readonly id: number,
  ) {}
}

const u = new User('Alice', '***', 1);
u.name;  // 'Alice'
// u.password; // 编译错误：私有
```

**注意**：
- 只有带 `public` / `private` / `protected` / `readonly` 前缀的参数才是参数属性；无修饰符的参数就是普通参数，两者可在构造函数中混排
- 继承时参数属性在 `super()` 调用**之后**才赋值，因此无法在 `super()` 前使用

---

## 5. 抽象类

抽象类（`abstract class`）在 TS 类型检查中**不能直接实例化**，用于表达"子类共同骨架 + 必须实现的缺口"。它仍会生成普通 JavaScript 类；运行时并没有 `abstract` 检查。

```typescript
abstract class Shape {
  protected name: string;

  constructor(name: string) {
    this.name = name;
  }

  // 抽象方法：只有签名，子类必须实现
  abstract area(): number;
  abstract perimeter(): number;

  // 具体方法：公共逻辑写在基类（模板方法模式）
  describe(): string {
    return `${this.name}: area=${this.area().toFixed(2)}, perimeter=${this.perimeter().toFixed(2)}`;
  }
}

class Circle extends Shape {
  constructor(private r: number) {
    super('Circle');
  }
  area(): number { return Math.PI * this.r ** 2; }
  perimeter(): number { return 2 * Math.PI * this.r; }
}

class Square extends Shape {
  constructor(private s: number) {
    super('Square');
  }
  area(): number { return this.s ** 2; }
  perimeter(): number { return 4 * this.s; }
}

const shapes: Shape[] = [new Circle(1), new Square(2)];
shapes.forEach(s => console.log(s.describe()));
// new Shape('x'); // 编译错误：不能创建抽象类的实例
```

**抽象类 vs 接口**：

| | 抽象类 | 接口 |
|--|--------|------|
| 关系 | is-a（"是一种"） | can-do / has-a（"能做什么/长什么样"） |
| 成员实现 | ✅ 可包含具体实现 | ❌ 只有签名（TS 中） |
| 构造函数实现 / 字段实现 | ✅ 可执行初始化逻辑 | ❌ 接口只能声明属性签名，不能提供实现 |
| 修饰符 | 支持 private/protected | 只描述公开成员 |
| 数量 | 只能单继承 `extends` | 可多实现/多继承 |
| 编译产物 | 真实的类 | 完全擦除 |

**经验法则**：要在基类里放公共逻辑 → 抽象类；只定义契约 → 接口。

---

## 6. 接口

> 本章介绍接口语法；如果想先理解“为什么 JavaScript 开发需要接口”，请读 [[topics/programming/Web/typescript/interface]]。

### 6.1 描述对象形状

```typescript
interface User {
  name: string;
  age?: number;        // 可选
  readonly id: number; // 只读
  sayHi(): void;       // 方法签名
}

const u: User = {
  id: 1,
  name: 'Alice',
  sayHi() { console.log(`Hi, ${this.name}`); },
};
```

### 6.2 函数类型与索引签名

```typescript
// 可调用接口：描述"函数"的签名（比 type 少见，但可附带属性）
interface SearchFn {
  (source: string, keyword: string): boolean;
  defaultProps?: Record<string, string>; // 函数还可以挂属性
}

const search: SearchFn = (src, kw) => src.includes(kw);

// 索引签名：任意字符串键 → 固定值类型
interface Dictionary {
  [key: string]: number;
}
const scores: Dictionary = { math: 95, english: 88 };
scores.physic = 90;

// 数字索引：类数组结构
interface StringArray {
  [index: number]: string;
}
```

### 6.3 继承与实现

```typescript
interface Named {
  name: string;
}
interface Aged {
  age: number;
}

// 接口可以多继承
interface Employee extends Named, Aged {
  department: string;
}

const e: Employee = { name: 'Alice', age: 25, department: 'FE' };

// 类用 implements 实现接口（可同时实现多个）
class Engineer implements Employee {
  constructor(
    public name: string,
    public age: number,
    public department: string,
  ) {}
}

// 接口只检查公开成员 —— private/protected 不参与匹配
```

### 6.4 声明合并

同名 `interface` 会**自动合并**成员——这是扩展第三方类型（如 `window`）的标准手段，也是 `interface` 独有的能力：

```typescript
interface Window {
  __APP_VERSION__: string;
}
// window.__APP_VERSION__ 现在有了类型

interface Config {
  host: string;
}
interface Config {
  port: number; // 与上面的 Config 合并为 { host; port }
}
```

注意：在**模块文件**（有 `import`/`export`）中，直接声明 `interface Window` 只会创建局部接口、**不会**合并进全局，需要 `declare global` 包裹：

```typescript
declare global {
  interface Window {
    __APP_VERSION__: string;
  }
}
```

### 6.5 interface 与 type 怎么选

| 能力 | `interface` | `type` |
|------|:-----------:|:------:|
| 描述对象/函数形状 | ✅ | ✅ |
| 原始类型、联合、元组别名 | ❌ | ✅ |
| 同名自动合并（declaration merging） | ✅ | ❌（重名报错） |
| 扩展方式 | `extends` | 交叉 `&` |
| 条件类型/映射类型操作 | ❌ | ✅ |
| 错误信息可读性（继承链） | 更好 | 交叉过深时较差 |

**建议**：公开 API、需要被 extends/implements 或可能被第三方扩展的对象形状 → `interface`；联合、工具类型派生、其他一切 → `type`。团队内保持统一比选哪个更重要。

---

## 7. 泛型

泛型（Generics）让类型成为**参数**：一份逻辑适配多种类型，同时保住类型信息。JavaScript 函数运行时仍是普通函数；`<T>` 只供类型检查器关联输入和输出，不会生成“带类型参数”的 JavaScript 函数。

### 7.1 泛型函数

```typescript
// 没有泛型的两种写法都有损失：
// function first(arr: any[]): any          // 丢失类型
// function first(arr: number[]): number    // 只支持 number

// 泛型：调用时才确定 T，且全程保留
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}

const n = first([1, 2, 3]);            // n: number | undefined（自动推断，数组可能为空）
const s = first(['a', 'b']);           // s: string | undefined
const m = first<number>([]);           // 显式指定，复杂场景用
```

### 7.2 泛型约束 `extends`

裸泛型 `T` 上无法访问任何属性，用 `extends` 声明"至少长什么样"：

```typescript
// 约束：只要有 length
function logLength<T extends { length: number }>(x: T): number {
  return x.length;  // OK
}
logLength('hello');  // string 有 length
logLength([1, 2]);   // 数组有 length
// logLength(123);   // 错误：number 没有 length

// 经典模式：keyof 约束 —— 安全地从对象取属性
function pick<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
const user = { name: 'Alice', age: 25 };
pick(user, 'name');  // 返回类型 string
// pick(user, 'email'); // 编译错误：'email' 不存在于 'name' | 'age'

// 合并两个对象，返回类型精确到字段
function merge<A extends object, B extends object>(a: A, b: B): A & B {
  return { ...a, ...b };
}
```

### 7.3 默认类型与多个类型参数

```typescript
// 默认类型：不传 T 时使用兜底
interface ApiResponse<T = unknown> {
  code: number;
  message: string;
  data: T;
}

const r1: ApiResponse = { code: 0, message: 'ok', data: null }; // data: unknown
const r2: ApiResponse<{ id: number }[]> = {
  code: 0, message: 'ok',
  data: [{ id: 1 }],
};

// 多个类型参数
function swap<A, B>(pair: [A, B]): [B, A] {
  return [pair[1], pair[0]];
}
const swapped = swap(['age', 25]); // [number, string]
```

### 7.4 泛型类与泛型接口

```typescript
// 泛型类
class Queue<T> {
  private items: T[] = [];

  push(item: T): void { this.items.push(item); }
  pop(): T | undefined { return this.items.shift(); }
  get size(): number { return this.items.length; }
}

const q = new Queue<number>();
q.push(1);
// q.push('a'); // 错误

// 泛型接口 + 实现类
interface Repository<T, ID = string> {
  findById(id: ID): Promise<T | null>;
  save(entity: T): Promise<void>;
}

class UserRepo implements Repository<{ id: number }, number> {
  async findById(id: number) { return { id }; }
  async save() {}
}
```

### 7.5 泛型的常见用途速记

| 模式 | 例子 |
|------|------|
| 容器/集合 | `Queue<T>`、`Map<K, V>`、`Promise<T>` |
| 工具函数保类型 | `identity<T>`、`pick<T, K extends keyof T>` |
| API 响应包装 | `ApiResponse<T>`、`Page<T>` |
| 仓库/DAO | `Repository<T, ID>` |
| 事件系统 | `on<E extends keyof Events>(name: E, cb: (e: Events[E]) => void)` |

---

## 8. 类型收窄与高级类型操作

### 8.1 类型守卫（Type Guards）

联合类型使用前必须**收窄**（narrowing）为具体分支，TS 通过控制流分析自动完成。

收窄使用的 `typeof`、`in`、`instanceof`、`===` 都是普通 JavaScript 检查。运行时判断负责分支选择；TS 根据同一段检查推断分支内的类型，因此类型安全不需要额外的运行时代码。相关运行时语法见 [[topics/programming/Web/javascript]]。

```typescript
type Fish = { swim: () => void };
type Bird = { fly: () => void };

// typeof：收窄原始类型
function format(x: string | number) {
  if (typeof x === 'string') return x.trim(); // x: string
  return x.toFixed(2);                        // x: number
}

// 真值收窄：排除 null/undefined
function greet(name: string | null) {
  if (name) console.log(name.toUpperCase()); // name: string
}

// in：检查属性是否存在 —— 结构区分
function move(pet: Fish | Bird) {
  if ('swim' in pet) {
    pet.swim();  // pet: Fish
  } else {
    pet.fly();   // pet: Bird
  }
}

// instanceof：收窄类实例
function logErr(e: unknown) {
  if (e instanceof Error) console.error(e.message); // e: Error
}

// 相等收窄：=== 缩小字面量联合
function setStatus(s: 'idle' | 'done') {
  if (s === 'idle') { /* s: 'idle' */ }
}

// 数组过滤：TS 5.5 起可自动推断类型谓词；显式标注 `(x): x is number` 在旧版本也可用：
const nums = [1, null, 2, null].filter((x): x is number => x !== null);
// nums: number[]
```

**自定义守卫**：复用判断逻辑时，用类型谓词 `pet is Fish` 告诉编译器"返回 true 意味着什么"：

```typescript
function isFish(pet: Fish | Bird): pet is Fish {
  return 'swim' in pet;
}

function feed(pet: Fish | Bird) {
  if (isFish(pet)) pet.swim();
  else pet.fly();
}
```

`asserts` 形式：守卫不返回值，而是承诺"通过则断言成立"，失败时抛错：

```typescript
function assertDefined<T>(value: T | null | undefined): asserts value is T {
  if (value == null) throw new Error('unexpected null');
}

function process(user: User | null) {
  assertDefined(user);
  user.name; // 收窄为 User
}
```

### 8.2 可辨识联合（Discriminated Unions）

给联合的每个分支一个**字面量类型的公共字段**（kind/tag/type），TS 即可沿 `switch` 自动收窄，配合 `never` 兜底获得穷尽性检查——建模状态机、协议消息、AST 的首选方式：

```typescript
type NetworkState =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: string }
  | { status: 'error'; message: string };

function render(state: NetworkState): string {
  switch (state.status) {
    case 'idle':    return '等待中';
    case 'loading': return '加载中…';
    case 'success': return state.data;      // 仅此分支有 data
    case 'error':   return state.message;   // 仅此分支有 message
  }
}

// 穷尽性检查：新增分支而忘了处理时，default 里把值赋给 never 会编译报错
function assertNever(x: never): never { throw new Error('missed: ' + JSON.stringify(x)); }
function renderSafe(state: NetworkState): string {
  switch (state.status) {
    case 'idle': return '等待中';
    // case 'loading' … 假设漏写了几个分支
    default: return assertNever(state); // 若有遗漏，这里报错提示
  }
}
```

### 8.3 条件类型与 infer

条件类型即"类型层面的三目表达式"：`T extends U ? X : Y`。

```typescript
type IsString<T> = T extends string ? true : false;
type A = IsString<'hi'>;  // true
type B = IsString<42>;    // false

// infer：在 extends 子句里"捕获"嵌套的类型
type ElementType<T> = T extends (infer U)[] ? U : never;
type E1 = ElementType<string[]>;   // string
type E2 = ElementType<number[][]>; // number[]（只剥一层）

// 递归 infer：完全展平嵌套数组
type Flatten<T> = T extends (infer U)[]
  ? Flatten<U>
  : T;
type F = Flatten<number[][][]>;    // number

// 提取函数返回值 / 参数（内置工具类型的实现原理，见第 9 节）
type ReturnOf<T> = T extends (...args: any[]) => infer R ? R : never;
type ArgsOf<T> = T extends (...args: infer A) => any ? A : never;

// Promise 递归解包
type Awaited<T> = T extends Promise<infer U> ? Awaited<U> : T;
type X = Awaited<Promise<Promise<number>>>; // number
```

**分布式条件类型**：裸类型参数传入联合时，条件类型会对联合**逐成员**求值再合并——这是 `Exclude` 能工作的原理：

```typescript
type ToArray<T> = T extends unknown ? T[] : never;
type R = ToArray<string | number>; // string[] | number[]（而非 (string|number)[]）

type Without<T, U> = T extends U ? never : T;
type W = Without<'a' | 'b' | 'c', 'a'>; // 'b' | 'c'

// 不想分发时，用 [T] 包住
type IsNever<T> = [T] extends [never] ? true : false;
```

### 8.4 映射类型

映射类型即"类型层面的 `for...in`"：基于既有类型批量生成新类型的字段。

```typescript
type User = { id: number; name: string; age: number };

// 遍历 key 生成同构的新类型
type Optional<T> = { [K in keyof T]?: T[K] };
type PartialUser = Optional<User>; // { id?: number; name?: string; age?: number }

// 修饰符可以增（+）也可以删（-），readonly 同理
type Mutable<T> = { -readonly [K in keyof T]: T[K] };
type Required2<T> = { [K in keyof T]-?: T[K] }; // 与内置 Required 等价

// as 重映射：改变键名，甚至过滤键
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
type UserGetters = Getters<User>;
// { getId: () => number; getName: () => string; getAge: () => number }

type DropId<T> = { [K in keyof T as Exclude<K, 'id'>]: T[K] };
// { name: string; age: number }
```

### 8.5 模板字面量类型

模板字面量类型在**类型层面**做字符串拼接，配合内置的 `Uppercase` / `Lowercase` / `Capitalize` / `Uncapitalize` 四个关键字，可以把字符串规则也纳入类型检查：

```typescript
type World = 'world';
type Greeting = `hello ${World}`; // 'hello world'

// 联合会自动做笛卡尔积
type Lang = 'zh' | 'en';
type Page = 'home' | 'about';
type Route = `/${Page}/${Lang}`;  // '/home/zh' | '/home/en' | '/about/zh' | '/about/en'

// 事件名生成（与 8.4 的重映射是天生一对）
type DOMEvent = `on${Capitalize<'click' | 'focus'>}`; // 'onClick' | 'onFocus'

// 约束字符串格式：以 / 开头的路由才合法
function goto(route: `/${string}`) {}
goto('/home');  // OK
// goto('home'); // 编译错误
```

---

## 9. 工具类型

TypeScript 内置了一组工具类型（`lib.es5.d.ts` 等）。多数常用工具类型可以用第 8 节的映射类型、条件类型和 `infer` 来理解；少数（如字符串大小写工具类型）由编译器特殊处理。按用途分四类：

### 9.1 属性修饰类

| 工具类型 | 效果 |
|----------|------|
| `Partial<T>` | 所有属性变可选 |
| `Required<T>` | 所有属性变必选 |
| `Readonly<T>` | 所有属性变只读 |
| `Pick<T, K>` | 挑选一部分属性 |
| `Omit<T, K>` | 排除一部分属性 |
| `Record<K, V>` | 用键集合构造同值类型 |

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

// 局部更新：表单/patch 接口的高频用法
function updateUser(id: number, patch: Partial<User>) {}
updateUser(1, { name: 'Bob' });

// 投影：对外暴露的视图
type PublicUser = Pick<User, 'id' | 'name'>;       // { id; name }
type SafeUser = Omit<User, 'password'>;             // 除 password 外全部

// 字典
type ScoreMap = Record<string, number>;
type UserById = Record<number, User>;
```

### 9.2 联合处理类

```typescript
type T0 = Exclude<'a' | 'b' | 'c', 'a' | 'b'>; // 'c'
type T1 = Extract<'a' | 'b' | 'c', 'a' | 'f'>; // 'a'
type T2 = NonNullable<string | null | undefined>; // string

// 实现原理就是分布式条件类型（见 8.3）
type MyExclude<T, U> = T extends U ? never : T;
type MyExtract<T, U> = T extends U ? T : never;
```

### 9.3 函数与异步类

```typescript
// 从函数类型反推参数/返回值 —— 拿不到源码时（第三方库）特别有用
type Fetcher = (url: string, init?: RequestInit) => Promise<Response>;

type Args = Parameters<Fetcher>;        // [url: string, init?: RequestInit]
type Ret = ReturnType<Fetcher>;         // Promise<Response>
type CtorArgs = ConstructorParameters<typeof Error>; // [message?: string]

// Awaited：递归解包 Promise
type Data = Awaited<ReturnType<Fetcher>>; // Response
```

### 9.4 手写实现：理解原理

工具类型是学习映射/条件类型最好的练习题：

```typescript
type MyPartial<T> = { [K in keyof T]?: T[K] };
type MyRequired<T> = { [K in keyof T]-?: T[K] };
type MyReadonly<T> = { readonly [K in keyof T]: T[K] };
type MyPick<T, K extends keyof T> = { [P in K]: T[P] };
type MyRecord<K extends keyof any, V> = { [P in K]: V };
type MyOmit<T, K extends keyof T> = MyPick<T, Exclude<keyof T, K>>;
type MyNonNullable<T> = T extends null | undefined ? never : T;
type MyReturnType<T extends (...args: any) => any> =
  T extends (...args: any) => infer R ? R : any;
type MyParameters<T extends (...args: any) => any> =
  T extends (...args: infer A) => any ? A : never;
type MyAwaited<T> = T extends Promise<infer U> ? MyAwaited<U> : T;
```

---

## 10. 工程配置与实践

### 10.1 tsconfig.json 核心选项

```jsonc
{
  "compilerOptions": {
    "target": "ES2022",            // 编译目标的 JS 版本
    "module": "ESNext",            // 模块格式（配合打包器常用 ESNext）
    "moduleResolution": "bundler", // 模块解析策略（打包器项目）
    "strict": true,                // 严格模式总开关（强烈建议）
    "isolatedModules": true,       // 确保代码可由 Vite/Oxc 等单文件转译器处理
    "noUncheckedIndexedAccess": true, // 索引访问额外加 undefined（更安全）
    "esModuleInterop": true,       // CommonJS 互操作
    "skipLibCheck": true,          // 跳过 .d.ts 检查（加速编译）
    "outDir": "dist",
    "paths": { "@/*": ["./src/*"] }// 路径别名（打包器需同步配置）
  }
}
```

**版本提示（TypeScript 6.0+）**：部分 `tsconfig` 默认值有变化，例如 `strict` 默认开启、`types` 默认不自动包含所有可见的 `@types` 包、`rootDir` 默认是配置文件所在目录。项目配置建议明确写出依赖的选项；需要 Node 全局类型时，再按需设置 `"types": ["node"]`。

`strict: true` 展开后最重要的几项：

| 选项 | 作用 |
|------|------|
| `noImplicitAny` | 禁止隐式 any——推断不出类型就报错 |
| `strictNullChecks` | `null`/`undefined` 不再能赋给任意类型 |
| `strictFunctionTypes` | 函数类型按逆变关系检查参数（方法签名有兼容性例外） |
| `strictBindCallApply` / `strictPropertyInitialization` | bind/call 检查；字段必须初始化 |

### 10.2 类型声明文件（.d.ts）

```typescript
// types.d.ts —— 描述无类型的 JS 模块
declare module 'legacy-lib' {
  export function init(options?: { debug?: boolean }): void;
}
```

- **`@types/*` 包**：主流库的官方/社区类型，`npm i -D @types/lodash` 即可
- **自带类型的库**：现代库（Vue、zod 等）直接在包里带 `.d.ts`，无需安装
- **`declare`**：告诉编译器"这个全局变量/模块在运行时存在"，不产出 JS

### 10.3 渐进迁移策略

```bash
# 第一步：允许 JS 共存
tsc --init --allowJs --checkJs --noEmit
```

- `// @ts-check`：单文件开启 JS 类型检查
- `// @ts-expect-error`：**推荐**的抑制标记——若下一行其实没有错误，这行本身会报错，倒逼清理
- `// @ts-ignore`：无脑抑制，尽量不用
- 迁移节奏：`allowJs` → 改后缀 `.ts` → 开 `strict` → 收紧 `any`（可用 `type-coverage` 类工具统计）

---

## 11. 总结

学习路径回顾：先从 [[topics/programming/Web/javascript]] 熟悉运行时语言，再用 [[topics/programming/Web/es6]] 补齐现代 JavaScript 语法，然后学习本文的静态类型与工程实践；需要理解类型推导规则时继续阅读 [[topics/programming/Web/typescript/type-system]]。

**学习优先级建议**（对标 [[topics/programming/Web/es6]] 的分级方式）：

| 优先级 | 内容 |
|--------|------|
| 第一（日常必用） | 基本注解与推断、接口/type、联合与字面量、函数类型、`strict` 模式下的 null 处理 |
| 第二（重要工具） | 泛型函数与约束、可辨识联合、`Partial`/`Pick`/`Omit`/`Record`、类型守卫 |
| 第三（进阶能力） | 条件类型与 infer、映射类型、模板字面量类型、手写工具类型 |
| 第四（特定场景） | 声明合并、`infer` 递归、tsconfig 深度定制、`.d.ts` 编写 |

**核心心法**：

1. **类型是文档，更是约束**——先建模数据结构（联合、字面量），逻辑自然清晰
2. **能推断不注解，能收窄不断言**——`as` 是逃生门，不是常用门
3. **运行时边界必须校验**——TS 不检查外部输入，配合 zod 等 schema 库
4. **从 `strict: true` 开始**——事后补严格模式的成本远高于一开始就开

---

## 附录：速查表

### A.1 常用类型注解写法

```typescript
// 变量
let n: number;  let s: string;  let b: boolean;
let arr: string[];  let tup: [string, number];
let obj: { a: string; b?: number };

// 函数
const f = (a: number, b?: string, ...rest: boolean[]): void => {};
type Fn = (a: number) => string;

// 联合 / 交叉 / 字面量
type U = string | number;
type I = { a: 1 } & { b: 2 };
type L = 'on' | 'off';

// 泛型
function g<T extends object, K extends keyof T>(o: T, k: K): T[K] { return o[k]; }

// 断言
const el = document.querySelector('#app') as HTMLDivElement;
const frozen = { a: 1 } as const;
```

### A.2 内置工具类型一览

| 工具类型 | 一句话说明 |
|----------|-----------|
| `Partial<T>` / `Required<T>` / `Readonly<T>` | 属性可选 / 必选 / 只读 |
| `Pick<T, K>` / `Omit<T, K>` | 取一部分 / 去掉一部分属性 |
| `Record<K, V>` | 键集合 → 同值类型的字典 |
| `Exclude<T, U>` / `Extract<T, U>` | 从联合中剔除 / 抽取 |
| `NonNullable<T>` | 去掉 null/undefined |
| `Parameters<T>` / `ReturnType<T>` | 函数参数元组 / 返回值 |
| `ConstructorParameters<T>` / `InstanceType<T>` | 构造参数 / 实例类型 |
| `Awaited<T>` | 递归解包 Promise |
| `Uppercase/Lowercase/Capitalize/Uncapitalize<S>` | 字符串字面量大小写变换 |

---

## 参考资料

**书籍**

- 《Programming TypeScript》Boris Cherny —— 系统全面，类型系统设计视角
- 《Effective TypeScript》Dan Vanderkam —— 82 条实操建议，进阶必读

**在线资源**

- [TypeScript 官方手册（The TypeScript Handbook）](https://www.typescriptlang.org/docs/handbook/) —— 最重要的第一手资料，配套 [练习场 Playground](https://www.typescriptlang.org/play)
- [Node.js TypeScript 文档](https://nodejs.org/api/typescript.html) —— 原生类型擦除的支持范围与限制
- [Vite Features：TypeScript](https://vite.dev/guide/features) —— 转译与类型检查的职责分离
- [TypeScript Deep Dive](https://basarat.gitbook.io/typescript/) —— 免费在线书，工程向
- [type-challenges](https://github.com/type-challenges/type-challenges) —— 类型体操题库，检验第 8~9 节的掌握程度
