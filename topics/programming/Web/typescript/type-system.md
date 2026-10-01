# TypeScript 类型系统

> TypeScript 进阶篇：把类型注解变成**类型编程**。
> 讲清楚类型系统本身的规则——结构化类型、型变、条件类型、`infer`、递归，以及类型体操的套路与边界。
> 前置知识：[[topics/programming/Web/typescript/intro]]
> 导航：[[notes/MOC - programming]] · 接口直观介绍：[[topics/programming/Web/typescript/interface]] · JavaScript 运行时基础：[[topics/programming/Web/javascript]] · 现代语法：[[topics/programming/Web/es6]]

> **示例说明**：代码块分别展示独立类型技巧；有些别名（如 `Awaited`、`Flatten`）与标准库或其他章节重名，不能不加处理地合并到同一个源文件。

## 目录

| 章节 | 内容 |
|------|------|
| [1. 引言：从"标注"到"编程"](#1-引言从标注到编程) | 本文定位、类型编程的本质 |
| [2. 类型即集合](#2-类型即集合) | 结构化 vs 名义、集合运算、顶层类型、品牌化 |
| [3. 型变（Variance）](#3-型变variance) | 协变/逆变/双变、strictFunctionTypes、显式标注、UnionToIntersection |
| [4. 条件类型深入](#4-条件类型深入) | 分发律、阻断分发、Equal 判定 |
| [5. infer：类型层面的模式匹配](#5-infer类型层面的模式匹配) | 位置决定方向、元组 rest、带约束的 infer |
| [6. 递归类型](#6-递归类型) | 递归条件类型、尾递归消除、Split/Join |
| [7. 映射类型深入](#7-映射类型深入) | 同构映射、as 重映射 |
| [8. 模板字面量类型深入](#8-模板字面量类型深入) | intrinsic 关键字、Trim/LengthOfString |
| [9. 现代特性补全（4.7 → 6.0）](#9-现代特性补全47--60) | satisfies、const 类型参数、NoInfer、unique symbol、TS 6.0 推断改进 |
| [10. 类型体操实战六题](#10-类型体操实战六题) | 经典挑战的解题套路 |
| [11. 类型编程的边界](#11-类型编程的边界) | 何时停手、性能与可读性 |
| [参考资料](#参考资料) | 官方文档与题库 |

---

## 1. 引言：从"标注"到"编程"

[[topics/programming/Web/typescript/intro]] 里我们用类型**描述**数据；本文把类型系统当作一门**语言**来用——它有变量（泛型参数）、表达式（条件类型/映射类型）、函数（泛型别名）、递归，甚至模式匹配（`infer`）。

```typescript
// 入门篇：给值贴类型标签
let id: number = 1;

// 本文：类型本身可以被"计算"
type Unpacked<T> = T extends Promise<infer U> ? U : T;   // 类型层面的函数
type AllOptional<T> = { [K in keyof T]?: T[K] };          // 类型层面的映射
```

### 先分清 JavaScript 运行时与 TypeScript 类型阶段

JavaScript 表达式会在程序运行时计算；TypeScript 的 `type`、`keyof`、条件类型等只在检查阶段计算。部分关键字同名，但所处阶段不同：JavaScript 的 `typeof` 返回运行时字符串，类型位置的 `typeof` 则读取变量的静态类型。

```typescript
const user = { name: '小林', age: 20 };

console.log(typeof user); // JavaScript 运行时结果：'object'

type User = typeof user;         // TypeScript 类型：{ name: string; age: number }
type UserKeys = keyof User;      // 类型：'name' | 'age'
```

编译后保留 `user` 和 `console.log`，而 `User`、`UserKeys` 不会生成 JavaScript。这个差异是理解类型体操的关键：它计算的是**类型关系**，不是在程序运行时处理值。JavaScript 的 `typeof` 等运行时行为见 [[topics/programming/Web/javascript]]；对象约定与接口的关系见 [[topics/programming/Web/typescript/interface]]。

这门"类型语言"的表达能力可以模拟一般计算；但实际编译器会限制递归深度和检查工作量，所以不能把它当作无限制的运行时计算模型。工程上恰恰相反：**类型代码越简单越好**，类型体操只在"消除重复、防止手写漂移"有真实收益时才值得。本文既讲"怎么写"，也讲"何时该停"。

---

## 2. 类型即集合

### 2.1 结构化 vs 名义

TS 是**结构化类型系统**（structural typing，鸭子类型的静态版）：类型的兼容性由**成员形状**决定，与"类型叫什么名字、在哪里声明"无关。Java/C# 是**名义类型系统**（nominal typing）：名字不同就不兼容，除非显式继承。

它和 JavaScript 的“有这个属性就能用”很像：JS 在运行时尝试访问成员，TS 则在编译期检查所需成员是否存在、类型是否匹配。接口专题中的 [[topics/programming/Web/typescript/interface]] 有从 JS 对象调用到结构化类型的完整对照。

```typescript
interface Point2D { x: number; y: number }
interface Coords  { x: number; y: number }  // 名字不同、来源不同

const a: Point2D = { x: 0, y: 0 };
const b: Coords = a;   // OK —— 形状相同即兼容（名义系统会报错）

// 多一个成员也兼容（宽度子类型），这是结构化的自然推论
// const c: Point2D = { x: 0, y: 0, z: 1 }; // 但直接写对象字面量会被"多余属性检查"拦截
const viaVar = { x: 0, y: 0, z: 1 };
const d: Point2D = viaVar;                 // 经由变量中转则不受限
```

结构化带来便利，也带来"过宽"问题——两个语义完全不同的 `number`（人民币 vs 美元）彼此兼容。解决办法是**品牌化**（见 2.4）。

### 2.2 集合运算

把类型看成**值的集合**，很多规则立刻变得显然：

| 集合概念 | TS 对应 | 备注 |
|----------|---------|------|
| 子集 | `A extends B` | "A 是 B 的子类型" ≈ "A ⊆ B" |
| 空集 ∅ | `never` | 任何类型的子类型；没有值 |
| 全集 | `unknown` | 所有值的类型 |
| 并集 | `A \| B` | 联合 |
| 交集 | `A & B` | 交叉；集合不相交时化简为 `never`（属性冲突即此情形，基础用法见 [[topics/programming/Web/typescript/intro]] 2.5） |
| 过滤联合成员 | `Exclude<A, B>` | 移除联合中可赋给 `B` 的成员；不是任意类型集合的完整差集 |

```typescript
type T0 = string & number;      // never：没有值既是字符串又是数字
type T1 = 'a' | 'b';            // 集合 { 'a', 'b' }
type T2 = T1 & 'a';             // 'a'：交集
type T3 = Exclude<T1, 'a'>;     // 'b'：差集
type T4 = Exclude<string, 'a'>; // string：宽类型 string 不会被拆成所有字符串逐个过滤

// never 是"空联合"：对它分发 = 什么都不做
type IsNumber<T> = T extends number ? true : false;
type R = IsNumber<never>;       // never（不是 false！）
```

对对象交叉类型而言，同名必选属性若类型冲突（如 `{ id: string } & { id: number }`），通常表现为 `id: never`，而不是整个类型别名直接显示为 `never`；这一点及接口组合示例见 [[topics/programming/Web/typescript/interface]]。

几个**顶层类型**的精确语义，容易混淆：

| 类型 | 集合含义 | 可赋值性 |
|------|----------|----------|
| `unknown` | 全集 | 任何值可赋给它；使用前必须收窄 |
| `any` | 逃逸舱 | 双向兼容，**关闭检查**，没有健康的集合语义 |
| `{}` | 除 `null`/`undefined` 外的一切 | **包含原始值**！`const a: {} = 42` 合法 |
| `object` | 所有非原始值 | 原始值不行，函数/数组可以 |
| `Object` | 历史兼容 | 几乎一切值，基本别用 |

### 2.3 类型层级全景

```typescript
// strictNullChecks 开启时，自上而下可近似理解为"子集"关系（extends 方向）
// unknown
//   └── {}               （一切非 null/undefined）
//         ├── object ── Array / Function / Date / 自定义类与接口 ...
//         ├── string ── 字面量联合 'a' | 'b' ── 具体字面量 'a'
//         ├── number ── 字面量联合 1 | 2    ── 具体字面量 1
//         ├── boolean ── true | false
//         ├── symbol ── unique symbol
//         └── bigint
// never —— 空集，位于最底层，是一切类型的子类型
```

收窄（[[topics/programming/Web/typescript/intro]] 的类型收窄一节）本质就是**沿这棵树向下移动**：`'a' | 'b'` 经 `=== 'a'` 收窄成 `'a'`。

### 2.4 品牌化（Branding）：模拟名义类型

在结构化系统里人为加一个"身份标记"字段，让语义不同的类型互不兼容：

```typescript
type Brand<T, B extends string> = T & { readonly __brand: B };

type CNY = Brand<number, 'CNY'>;
type USD = Brand<number, 'USD'>;

const price = 99 as USD;
// const refund: CNY = price; // 编译错误：__brand 'USD' 与 'CNY' 不兼容

function payInUSD(amount: USD) {}
payInUSD(price);         // OK
// payInUSD(100 as CNY); // 编译错误 —— 真实的钱数单位错误在编译期被拦下
```

标准库也用类似手法：`unique symbol`（见 9.4）就是天然的"品牌"，枚举成员之所以互不兼容，靠的也是字面量身份。

---

## 3. 型变（Variance）

**型变**回答一个问题：`Box<Cat>` 和 `Box<Animal>` 之间是什么关系？

- **协变（covariant）**：方向一致 —— `Cat extends Animal` 则 `Box<Cat> extends Box<Animal>`
- **逆变（contravariant）**：方向相反 —— `Cat extends Animal` 则 `Consumer<Animal> extends Consumer<Cat>`
- **双变（bivariant）**：两个方向都允许（不健全的历史兼容）
- **不变（invariant）**：两个方向都不允许，必须完全相同

记忆法（"输入逆变，输出协变"，PECS 的 TS 版）：**只产出 T → 协变；只消费 T → 逆变；又产又消 → 不变**。

型变只影响 TypeScript 对**函数/容器类型能否赋值**的判断。JavaScript 运行时不会根据 `in` / `out` 标记转换函数或包装数组；运行时行为仍由实际传入的值和函数代码决定。

### 3.1 TS 各位置的型变规则

```typescript
interface Animal { name: string }
interface Dog extends Animal { breed: string }

// ① 对象属性 / 返回值：协变
declare let dogs: Dog[];
declare let animals: Animal[];
animals = dogs;          // 允许 —— 数组协变（其实并不健全，见下）
// dogs = animals;       // 错误

// 协变的不健全性（TS 为了实用性放行的坑）：
animals.push({ name: 'Cat' }); // 往 Animal[] 塞了一只猫
dogs[0].breed;                 // 运行时 undefined —— 类型系统"说谎"了

// ② 函数参数：逆变（strictFunctionTypes 下）
type Handler<T> = (payload: T) => void;

const onAnimal: Handler<Animal> = a => console.log(a.name);
let onDog: Handler<Dog>;
onDog = onAnimal;        // OK：能处理所有动物的处理器，当然能处理狗（逆变赋值）
// const onDog2: Handler<Dog> = (d: Dog) => d.breed;
// let bad: Handler<Animal> = onDog2; // 严格模式报错：只懂狗的处理器接不住猫
```

### 3.2 strictFunctionTypes 与方法的陷阱

`strictFunctionTypes`（`strict` 已包含）开启后，**函数属性**按逆变检查；但 **方法简写语法**声明的方法仍按双变规则比较（为兼容 DOM 事件处理器等历史设计）。双变意味着兼容性检查会接受参数方向上的任一关系，并非完全不检查：

```typescript
interface Comparable<T> {
  compare(a: T, b: T): number;        // 方法简写：按双变规则比较，参数方向检查较宽松
}
interface Comparable2<T> {
  compare: (a: T, b: T) => number;    // 函数属性：逆变检查
}

declare const numCmp: Comparable2<number>;
// const strCmp: Comparable2<string> = numCmp; // 报错（被正确拦截）
```

**结论**：写接口时，函数类型成员用**属性箭头写法**才能获得完整检查。

### 3.3 显式型变标注（TS 4.7）

泛型接口/别名可以（也只能在不标注会报错或需要文档化时）显式声明型变方向：

```typescript
interface Source<out T> { get(): T; }          // 协变：只产出
interface Sink<in T>     { set(value: T): void; } // 逆变：只消费
interface Cell<in out T> { get(): T; set(v: T): void; } // 不变：又产又消
```

收益：库作者把型变意图写进类型；检查器不用再反推（还能避免循环型变导致的检查爆炸）。

### 3.4 型变的应用：UnionToIntersection

参数位置的逆变是许多"魔法"工具类型的原理——把联合塞进参数位置再回收，联合就变成了交叉：

```typescript
type UnionToIntersection<U> =
  (U extends unknown ? (arg: U) => void : never) extends (arg: infer I) => void
    ? I : never;

type R = UnionToIntersection<{ a: 1 } | { b: 2 }>; // { a: 1 } & { b: 2 }
```

原理：分发把联合拆成多个函数类型 `(arg:{a:1})=>void | (arg:{b:2})=>void`；与 `(arg: infer I) => void` 匹配时，逆变位置的参数只能同时"接收"两者 → `I` 被推断为交叉。

---

## 4. 条件类型深入

`T extends U ? X : Y` 是类型层面的 `if`。本节讲它最重要的性质：**分发律**。

它借用了 JavaScript 条件表达式的写法，但两者处理的不是同一种东西：JS 的 `condition ? a : b` 在运行时根据布尔值选择结果；TS 条件类型根据一个**类型是否可赋给另一个类型**选择结果，不会生成运行时分支，也不是 `instanceof` 检查。

### 4.1 分发律（Distributivity）

当条件类型的**被检查者是裸类型参数**（naked type parameter）且传入联合时，会对联合**逐成员求值再合并**：

```typescript
type ToArray<T> = T extends unknown ? T[] : never;

type R1 = ToArray<string | number>;
// = ToArray<string> | ToArray<number>
// = string[] | number[]
// —— 而不是 (string | number)[]

// Exclude/Extract 全靠分发：
type MyExclude<T, U> = T extends U ? never : T;
type T0 = MyExclude<'a' | 'b' | 'c', 'a'>;
// 'a' extends 'a' → never；'b' → 'b'；'c' → 'c'，合并 → 'b' | 'c'
```

### 4.2 阻断分发

不希望分发时，把类型参数**包进非裸位置**（元组、数组等）：

```typescript
// never 是空联合，分发无从发生 → 永远返回 never，无法判断"是不是 never"
type IsNeverBroken<T> = T extends never ? true : false; // IsNeverBroken<never> = never ❌

// 包一层元组阻断分发：
type IsNever<T> = [T] extends [never] ? true : false;   // ✅
type A = IsNever<never>;   // true
type B2 = IsNever<number>; // false
```

**实践规则**：凡是"对联合整体做布尔判断"的条件类型，第一步都是 `[T] extends [X]`。同款套路还出现在 `IsUnion`、`IsAny` 等 type-challenges 题里。

### 4.3 两个条件的化简行为

```typescript
// 布尔的分发：true | false 合并成 boolean —— 联合判断"返回 boolean"的经典来源
type IsNumber<T> = T extends number ? true : false;
type R = IsNumber<number | string>; // boolean

// any 的特殊行为：条件类型对 any 直接"两边都给"
type IsString<T> = T extends string ? true : false;
type X = IsString<any>;  // boolean（而非 true/false）

// 函数重载：条件类型只与最后一个重载签名匹配
declare function f(x: string): number;
declare function f(x: number): string; // ← 只看这个
type R2 = ReturnType<typeof f>;        // string
```

### 4.4 类型相等的标准判定

`X extends Y && Y extends X` 太弱（`any`、字面量与宽类型互相 extends）。社区公认最严格的相等判断：

```typescript
type Equal<X, Y> =
  (<T>() => T extends X ? 1 : 2) extends (<T>() => T extends Y ? 1 : 2)
    ? true : false;

type A = Equal<{ a: 1 }, { a: 1 }>;        // true
type B = Equal<number, number | any>;      // false（朴素写法会误判）
type C = Equal<[], readonly[]>;            // false
```

原理：两个"对任意 T 求条件类型"的泛型签名，只有当 X、Y 在 TS 内部**完全同构**时才会被判兼容。体操题里辨析"真相等"就靠它。

---

## 5. infer：类型层面的模式匹配

`infer U` 在 `extends` 右侧声明一个"待推断"的占位符，条件类型由此获得**解构**能力——它是所有"提取类"工具类型的核心。

### 5.1 位置决定推断方向

```typescript
// 从数组元素提取（协变位置）
type ElementOf<T> = T extends (infer U)[] ? U : never;
type E = ElementOf<string[]>;            // string

// 从返回值提取（协变位置）
type ReturnOf<T> = T extends (...args: any[]) => infer R ? R : never;

// 从参数提取（逆变位置）→ 内置 Parameters
type ArgsOf<T> = T extends (...args: infer A) => any ? A : never;

// 多个占位符：元组头尾
type Head<T extends any[]> = T extends [infer F, ...any[]] ? F : never;
type Tail<T extends any[]> = T extends [any, ...infer R] ? R : [];

// Promise 解包（内置 Awaited 就是这么递归的，见第 6 节）
type Then<T> = T extends Promise<infer U> ? U : T;
```

### 5.2 元组 rest 的 infer

```typescript
// 同时抓头和尾
type Both<T extends any[]> = T extends [infer F, ...infer M, infer L]
  ? [F, L]
  : never;
type B = Both<[1, 2, 3, 4]>; // [1, 4]

// rest 也可以出现在中间，用来做"去头去尾"变换
type DropFirst<T extends any[]> = T extends [any, ...infer R] ? R : [];
type DropLast<T extends any[]> = T extends [...infer R, any] ? R : [];
```

### 5.3 带约束的 infer（TS 4.7）

`infer` 可以直接携带约束，推断结果自动收窄，省掉 `Extract` 清理：

```typescript
// 旧写法：推断出来还要过滤
type FirstString<T> = T extends [infer F, ...any[]] ? Extract<F, string> : never;

// 新写法：约束直接写在 infer 上
type FirstString2<T> = T extends [infer F extends string, ...any[]] ? F : never;

type A = FirstString2<['hi', 42]>; // 'hi'

// 配合分发做"过滤出合法成员"：
type OnlyNumber<T> = T extends infer U extends number ? U : never;
type N = OnlyNumber<'x' | 1 | 2>; // 1 | 2
```

### 5.4 infer 的注意事项

- 同一条件分支里，同名 `infer` 出现多次必须推断出**一致**的类型，否则按协变位置合并、逆变位置交叉处理
- 针对函数重载，`infer` 只与**最后一个**重载签名匹配
- 不希望某个位置参与推断污染泛型参数时，用 `NoInfer`（见 9.3）

---

## 6. 递归类型

条件类型的分支里可以引用自身（TS 4.1+），从此类型层面可以写循环——`Awaited`、`DeepReadonly`、`Split` 全是递归。

### 6.1 基本形态

```typescript
// 递归解包 Promise（内置 Awaited 的简化版）
type Awaited<T> = T extends Promise<infer U> ? Awaited<U> : T;
type X = Awaited<Promise<Promise<number>>>; // number

// 递归展平数组
type Flatten<T> = T extends (infer U)[] ? Flatten<U> : T;
type F = Flatten<number[][][]>; // number
```

递归三要素与运行时递归完全同构：**终止条件**（`extends Promise` 不成立时）、**递归调用**、**问题规模收缩**（每层剥掉一层包装）。

### 6.2 深度限制与尾递归消除

TS 对类型递归有实例化深度与检查器工作量限制，具体阈值受版本和类型形状影响；普通递归常在几十层左右触及限制。**TS 4.5 起对部分条件类型尾递归做优化**，特定简单模式的上限可达约 **1000** 次，但这不是可依赖的通用配额：

```typescript
// ✅ 尾递归：递归调用直接作为分支结果，符合时可获得尾递归优化
// 名字用 NumRange：全局 DOM 里已有 interface Range，全局脚本中会重名冲突
type NumRange<Len extends number, Acc extends 1[] = []> =
  Acc['length'] extends Len ? Acc : NumRange<Len, [...Acc, 1]>;

type R10 = NumRange<10>['length']; // 10

// ❌ 非尾递归：返回值还要"再加工"（把递归结果包进新元组），通常更早触及深度限制
type PrependRange<Len extends number, Acc extends 1[] = []> =
  Acc['length'] extends Len ? Acc : [...PrependRange<Len, [...Acc, 1]>, 0];
```

写深层递归的口诀：**用一个累加器参数（Acc）把"回溯时的计算"搬进递归调用本身**，把非尾递归改造成尾递归。

### 6.3 经典递归：Split / Join

```typescript
type Split<S extends string, D extends string> =
  D extends '' ? [S]
  : S extends `${infer Head}${D}${infer Rest}`
    ? [Head, ...Split<Rest, D>]   // 递归结果被元组包裹，不属于尾递归
    : [S];

type P = Split<'a,b,c', ','>;    // ['a', 'b', 'c']

type Join<T extends string[], D extends string> =
  T extends []
    ? ''
    : T extends [infer F extends string]
      ? F
      : T extends [infer F extends string, ...infer R extends string[]]
        ? `${F}${D}${Join<R, D>}`  // 注意：前面有拼接，不是尾递归
        : never;

type J = Join<['a', 'b', 'c'], '.'>; // 'a.b.c'
```

`Split` 的模式 `${infer Head}${D}${infer Rest}` 是模板字面量 + `infer` 的组合拳（第 8 节展开）。

---

## 7. 映射类型深入

映射类型常类比 JavaScript 的 `for...in`，因为两者都“按键逐项处理”；但映射类型不会遍历某个运行时对象，也不会创建新的对象，只变换编译器掌握的类型结构。

### 7.1 同构映射（Homomorphic）

`{ [K in keyof T]: ... }` 形式的映射是**同构**的：TS 自动保留 `T` 上每个属性的 `readonly` 和 `?` 修饰符，仿佛"原样复印后再修改"：

```typescript
interface User {
  id: number;
  name?: string;
  readonly token: string;
}

// 同构：? 和 readonly 被保留
type Clone<T> = { [K in keyof T]: T[K] };
type C = Clone<User>;
// { id: number; name?: string; readonly token: string }

// 非同构：修饰符全部丢失（键集合是写死的，与 User 无关）
type Fake = { [K in 'id' | 'name']: unknown }; // 全部必选、可变
```

内置 `Partial`/`Readonly` 正是利用同构 + 修饰符重写；`+`/`-` 用来显式增删修饰符（手写实现见 [[topics/programming/Web/typescript/intro|intro]] 第 9 节）。

### 7.2 as 重映射：过滤与改名

TS 4.1 的 `as` 子句对键做二次计算，产出 `never` 即**删除**该键——映射类型从此有了"filter + map"：

```typescript
type User = { id: number; name: string; age: number };

// 过滤：Exclude 掉不要的键
type DropId<T> = { [K in keyof T as Exclude<K, 'id'>]: T[K] };
// { name: string; age: number }

// 改名：模板字面量生成新键（Camelize 的核心手法）
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
// { getId: () => number; getName: () => string; getAge: () => number }

// 过滤 + 改名可以同时做：
type Methods<T> = {
  [K in keyof T as T[K] extends Function ? K : never]: T[K];
};
```

`string & K` 是常见小技巧：`keyof T` 可能含数字或 `symbol`；这里要把键传给只接受字符串的 `Capitalize`，与 `string` 取交集可筛出字符串键。

### 7.3 键值联动

```typescript
// 由值类型反推键（保留原键、改值类型）
type Nullify<T> = { [K in keyof T]: T[K] | null };

// 分别挑出必选键与可选键；显式包含 undefined 的必选属性仍会被正确区分
type OptionalKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? K : never;
}[keyof T];
type RequiredKeys<T> = Exclude<keyof T, OptionalKeys<T>>;

type Example = { id: number; nickname?: string };
type ExampleOptionalKeys = OptionalKeys<Example>; // 'nickname'

// 键集合来自另一个类型的值：Record<K, V> 的本质
type MyRecord<K extends keyof any, V> = { [P in K]: V };
// keyof any = string | number | symbol —— 一切合法属性键
```

---

## 8. 模板字面量类型深入

它借用了 JavaScript 模板字符串的书写形式，但处理对象不同：JavaScript 在运行时把值插入字符串；模板字面量类型在编译期把**字符串字面量类型**组合成允许的取值集合。

```typescript
const userId = 42;
const url = `/users/${userId}`; // JavaScript 运行时字符串：'/users/42'

type UserRoute = `/users/${number}`; // TypeScript 类型：匹配 /users/数字 的字符串
const route: UserRoute = '/users/42';
// const invalid: UserRoute = '/users/me'; // 类型错误
```

相同的反引号语法因此有两个用途：值位置生成字符串，类型位置约束字符串格式。

### 8.1 内置字符串工具是 intrinsic

`Uppercase`/`Lowercase`/`Capitalize`/`Uncapitalize` 不是用 TS 语法实现的，而是编译器**内建关键字**（intrinsic）：

```typescript
// lib.es5.d.ts 里的真实源码：
type Uppercase<S extends string> = intrinsic;
type Lowercase<S extends string> = intrinsic;
type Capitalize<S extends string> = intrinsic;
type Uncapitalize<S extends string> = intrinsic;
```

它们是模板字面量类型仅有的四个"原生函数"；更复杂的字符串算法全部要靠**递归**（第 6 节）+ `infer` 手写。

### 8.2 模板字面量 + infer：字符串解构

模板字面量在 `extends` 右侧就是一个**字符串模式匹配器**：

```typescript
// 取首字符（空字符串不匹配此模式，结果为 never）
type Head<S extends string> = S extends `${infer F}${infer _Rest}` ? F : never;
type H = Head<'hello'>; // 'h'

// 判断前缀
type StartsWith<S extends string, P extends string> =
  S extends `${P}${string}` ? true : false;
type ST = StartsWith<'foobar', 'foo'>; // true
```

注意模式的贪婪性：`${infer F}` 默认匹配**最少**字符（非贪婪），`${string}` 匹配剩余全部——写解析逻辑时按"第一个分隔符"思考。

### 8.3 递归字符串算法：Trim / Replace / LengthOfString

```typescript
type Whitespace = ' ' | '\t' | '\n';

// Trim：两侧去空白 —— extends 右侧用联合，天然逐个模式尝试
type Trim<S extends string> =
  S extends `${Whitespace}${infer R}` | `${infer R}${Whitespace}`
    ? Trim<R>
    : S;

type T1 = Trim<'  hello\n'>; // 'hello'

// Replace：替换第一个子串
type Replace<S extends string, From extends string, To extends string> =
  From extends ''
    ? S
    : S extends `${infer L}${From}${infer R}` ? `${L}${To}${R}` : S;

type T2 = Replace<'foobar', 'ob', 'xx'>; // 'foxxar'

// LengthOfString：尾递归数长度（累加器模式，见 6.2）
type LengthOfString<S extends string, Acc extends any[] = []> =
  S extends `${infer First}${infer Rest}`
    ? LengthOfString<Rest, [...Acc, First]>
    : Acc['length'];

type L = LengthOfString<'hello'>; // 5
```

`LengthOfString` 是把非尾递归（先算 Rest 长度再 +1）改写成尾递归的标准示范：用一个元组 `Acc` 做累加器，最终取 `length`。

---

## 9. 现代特性补全（4.7 → 6.0）

### 9.1 satisfies：校验但不拓宽（TS 4.9）

`as` 断言会**放弃**字面量推断；`satisfies` 则是"**检查通过后保留原推断**"——既有约束又不丢精度：

```typescript
type Colors = 'red' | 'green' | 'blue';
type RGB = [number, number, number];

const palette = {
  red: [255, 0, 0],
  green: '#00ff38',
  blue: [0, 0, 255],
} satisfies Record<Colors, string | RGB>;

const r = palette.red;      // [number, number, number] —— 元组没有被拓宽成 number[]！
const g = palette.green;    // string —— 可变属性的字符串字面量仍会拓宽（经 tsc 实测）
palette.red[0].toFixed();   // OK
// const cyan = palette.cyan; // 编译错误：拼写错误被拦下

// 对比 as：断言之后字段全变宽类型，palette.red 变成 string | RGB…
```

**经验**：配置对象、查表结构（常量映射）优先 `satisfies`；确需改变类型视角才用 `as`。

### 9.2 const 类型参数（TS 5.0）

泛型函数推断时，`const` 修饰让参数按**最窄字面量 + 只读元组**推断，相当于函数版 `as const`：

```typescript
function identity<const T>(value: T): T {
  return value;
}

const arr = identity(['a', 'b']);
// 不加 const：通常推断为 string[]（字面量拓宽）
// 加 const：  readonly ['a', 'b']

// 典型用途：接住调用方传来的精确键列表
// 注意：约束要写成 readonly，否则 const 修饰会被忽略
function pickKeys<const K extends readonly string[]>(...keys: K): K { return keys; }
const ks = pickKeys('id', 'name'); // readonly ['id', 'name']
```

### 9.3 NoInfer：阻止泛型被"反向污染"（TS 5.4）

多参数泛型中，不希望某个参数位置参与 `C` 的推断：

```typescript
function createStreetLight<C extends string>(
  colors: C[],
  defaultColor: NoInfer<C>,   // 不加 NoInfer：'blue' 会把 C 扩成 'red'|'yellow'|'green'|'blue'
) {}

createStreetLight(['red', 'yellow', 'green'], 'red');  // OK
// createStreetLight(['red', 'yellow', 'green'], 'blue'); // 正确地报错
```

规则直觉：**希望"约束别人"的参数（如键列表）保持纯净**，别让"消费方"（如默认值）参与推断。

### 9.4 unique symbol 与类型级标识

`unique symbol` 是 `symbol` 的字面量子类型——每个声明都是**独一无二**的类型，天然可做类型级身份：

```typescript
declare const authToken: unique symbol;
type Token = typeof authToken; // 独一无二的静态类型标识

interface Authenticated {
  [authToken]: true;   // 用 unique symbol 作属性键 = 编译器级"印章"
}
function requireAuth(u: Authenticated) {}
// requireAuth({}); // 错误：缺少印章
```

`declare` 和接口属性都不会生成 JavaScript。若运行时真的要读取 `authToken` 属性，程序仍须在别处创建对应的 symbol 并把它放到对象上；如果只用作静态品牌，则它没有运行时检查能力。普通对象字面量不能自然满足这个独特键的要求，但 `as` 断言仍能绕过类型检查。

### 9.5 TS 6.0：改进不使用 `this` 的函数推断

TS 6.0 降低了不使用 `this` 的函数表达式对泛型推断顺序的影响。下面的例子中，即使 `consume` 写在 `produce` 前面，`produce` 推出的 `T = number` 仍能传给 `consume` 的 `y`：

```typescript
declare function callIt<T>(obj: {
  produce: (x: number) => T;
  consume: (y: T) => void;
}): void;

callIt({
  consume: y => y.toFixed(), // TS 6.0 推断 y 为 number
  produce: x => x * 2,
});
```

TS 7.0 是 TypeScript 编译器的原生实现迁移，目标是保持 TS 6.0 的类型系统语义；它属于工具链实现变化，不是新的类型语法。依赖 TypeScript 编译器 API 的插件与框架工具需另行确认版本兼容性。

---

## 10. 类型体操实战六题

以下六题覆盖上文全部原语，答案都可提交到 [type-challenges](https://github.com/type-challenges/type-challenges)。

**① TupleToUnion（简单）** —— 元组本质是"带数字键的对象"：

```typescript
type TupleToUnion<T extends any[]> = T[number];
type U = TupleToUnion<[1, 2, 'x']>; // 1 | 2 | 'x'
```

**② First / Last（简单）** —— rest infer 定位首尾：

```typescript
type First<T extends any[]> = T extends [infer F, ...any[]] ? F : never;
type Last<T extends any[]>  = T extends [...any[], infer L] ? L : never;
```

**③ DeepReadonly（中等）** —— 递归 + 分支处理函数（函数不该被递归展开）：

```typescript
type DeepReadonly<T> =
  T extends Function ? T
  : T extends object ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
  : T;
```

**④ UnionToIntersection（中等）** —— 逆变回收联合（原理见 3.4）：

```typescript
type UnionToIntersection<U> =
  (U extends unknown ? (arg: U) => void : never) extends (arg: infer I) => void
    ? I : never;
```

**⑤ LengthOfString（中等）** —— 模板字面量逐字符消费 + 尾递归累加器（见 8.3）。

**⑥ OptionalKeys（困难）** —— "空对象能否赋给 Pick 后的类型"判定可选性，再借映射过滤：

```typescript
type OptionalKeys<T> = {
  [K in keyof T]-?: {} extends Pick<T, K> ? K : never;
}[keyof T];

type R = OptionalKeys<{ a: number; b?: string }>; // 'b'
```

拆解：映射值产出"键或 never"，再 `[keyof T]` 索引一次拿到键的联合——**"映射出标记、索回收束"**是联合过滤的通用套路。

---

## 11. 类型编程的边界

1. **可读性是第一约束**。类型代码的读者是半年后的自己和同事。三层嵌套条件类型若不能一眼看懂，优先重构成"多个小类型别名接力"，每步起个名字。
2. **复杂度守恒**。类型里省掉的运行时代码，会在类型里加倍长回来。如果一个"工具类型"超过 20 行还收不了尾，考虑改用 zod 这类 schema 库（运行时校验 + 类型自动导出，`z.infer<typeof Schema>`）。
3. **类型不是运行时防线**。类型体操做得再精巧，`JSON.parse` 出来的数据依然不经过任何检查。边界校验、TS、类型体操三者各司其职。
4. **性能真实存在**。海量条件类型实例化会显著拖慢 `tsc` 与 IDE 响应；深层递归的实例化深度限制（见第 6 节）就是为保护检查器设计的。大型 monorepo 里慎用"深度类型体操"的公共库 API。
5. **何时值得体操**：✅ 消除大量手写重复（几十个相似的 CRUD 类型）；✅ 框架/库的公共 API 推断；❌ 面试式炫技、一次性用五层的映射类型。

---

## 参考资料

- [TypeScript 官方手册 · Type Manipulation](https://www.typescriptlang.org/docs/handbook/2/types-from-types.html) —— 条件类型/映射/模板字面量的官方讲解
- [TS 4.7 Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-7.html) —— 显式型变标注、infer 约束
- [TS 4.9 Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html) —— `satisfies`
- [TS 5.0 Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html) —— const 类型参数
- [TS 5.4 Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-4.html) —— `NoInfer`
- [TS 6.0 Release Notes](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html) / [TS 7.0 Announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) —— 最新推断改进与编译器版本说明
- [type-challenges](https://github.com/type-challenges/type-challenges) —— 按难度分级的类型体操题库，本文第 10 节题目均可提交验证
- 《Programming TypeScript》Boris Cherny —— 第 6 章"Advanced Types"与本文章节互为补充
