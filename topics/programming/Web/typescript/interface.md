---
title: TypeScript 接口：从 JavaScript 对象约定到类型契约
tags:
  - programming
  - typescript
  - interface
created: 2026-09-30
---

# TypeScript 接口：从 JavaScript 对象约定到类型契约

> 本文用 JavaScript 与 TypeScript 的对照，解释接口是什么、为什么有用，以及它**不能**替代什么。
> 前置知识：[[topics/programming/Web/javascript]]、[[topics/programming/Web/es6]]
> TS 入门：[[topics/programming/Web/typescript/intro]] · 类型系统进阶：[[topics/programming/Web/typescript/type-system]] · 导航：[[notes/MOC - programming]]

> **示例说明**：每个代码块聚焦一个概念，适合单独阅读；不同代码块可能重复使用类型名。

## 一句话理解

**JavaScript 允许对象“拿来就用”，TypeScript 接口则把对象需要满足的形状写成可检查的约定。**

可以把接口想成一张“数据说明书”：它告诉调用方和实现方，某类对象应该有哪些属性、属性是什么类型、可以调用哪些方法。TypeScript 在开发时检查这份约定；接口本身不会在运行时创建对象或验证数据。

## 1. 先看 JavaScript：约定存在，但没人替你检查

JavaScript 对象可以随时增删属性，函数也可以接收不同形状的对象。小程序里这很灵活；项目变大后，数据结构往往只靠函数名、注释和团队记忆来传递。

```javascript
function formatUser(user) {
  return `${user.name}（${user.age} 岁）`;
}

formatUser({ name: '小林', age: 20 }); // 正常
formatUser({ name: '小林' });         // 仍然调用成功，结果中出现 undefined
formatUser({ nmae: '小林', age: 20 }); // 拼错字段，直到运行时才暴露
```

这里的问题不是 JavaScript 不允许表达对象，而是普通 JavaScript 不会预先检查 `formatUser` 需要什么对象。调用者可能传错字段，维护者也很难知道改动会影响哪些调用点。

## 2. TypeScript 接口：把隐含约定写出来

给这类对象定义一个接口，再用它约束函数参数：

```typescript
interface User {
  name: string;
  age: number;
}

function formatUser(user: User): string {
  return `${user.name}（${user.age} 岁）`;
}

formatUser({ name: '小林', age: 20 }); // OK
// formatUser({ name: '小林' });      // 错误：缺少 age
// formatUser({ nmae: '小林', age: 20 }); // 错误：对象字面量字段不符合约定
```

`User` 接口相当于函数的输入说明：

- **调用方**知道要准备哪些数据，IDE 也能提示字段和类型。
- **实现方**可以直接使用 `user.name`、`user.age`，重命名属性时能发现关联代码。
- **编译器**能尽早指出常见拼写错误、漏传字段和类型不匹配。

所以接口的重点不是“给对象加功能”，而是**让数据约定可见，并由工具在开发阶段检查**。

## 3. JavaScript 与 TypeScript 接口对比

| 问题 | JavaScript | TypeScript `interface` |
|------|------------|-------------------------|
| 对象形状怎么表达 | 常用注释、文档或约定 | 直接列出属性和方法签名 |
| 何时发现字段错误 | 通常运行到相关代码时 | 类型检查阶段通常就能发现 |
| IDE 能否据此补全/重构 | 取决于工具推断或 JSDoc | 通常有更明确的字段提示和引用分析 |
| 是否创建运行时对象 | 对象由代码创建 | 接口不创建对象，编译后被擦除 |
| 能否检查外部 JSON 的真实内容 | 不能自动检查 | 也不能；需要运行时校验 |

TypeScript 是在 JavaScript 之上增加静态类型检查能力，不是因为 JavaScript 没有对象或无法使用对象，而是为了让对象约定能被编辑器、编译器和团队成员共同理解。

## 4. 接口描述的不只是数据

接口可以描述属性、可选属性、只读属性和方法。下面的 `id` 必须存在且不能通过这个类型重新赋值；`nickname` 可以省略；`rename` 描述一个方法的调用方式。

```typescript
interface UserProfile {
  readonly id: number;
  name: string;
  nickname?: string;
  rename(newName: string): void;
}

const profile: UserProfile = {
  id: 1,
  name: '小林',
  rename(newName) {
    this.name = newName;
  },
};

profile.nickname; // string | undefined
profile.rename('小林同学');
// profile.id = 2; // 错误：id 是只读属性
```

`readonly` 是类型层面的限制，不会冻结运行时对象；如果需要运行时不可变，还要使用相应的 JavaScript 机制。可选属性读取时可能是 `undefined`，使用前仍要判断。

## 5. 接口是结构约定，不是必须显式声明的“身份”

TypeScript 主要采用**结构化类型**：对象只要具有所需成员，就能满足接口，不需要先声明 `implements`。

```typescript
interface Point {
  x: number;
  y: number;
}

function distance(point: Point): number {
  return Math.hypot(point.x, point.y);
}

const origin = { x: 0, y: 0, label: '原点' };
distance(origin); // OK：包含 Point 所需的 x、y
```

这和 Java 等名义类型语言常见的“必须显式实现接口”不同。TypeScript 接口检查的是**对象是否符合形状**，而不是对象是否登记了某个接口身份。

有一个容易误会的细节：直接把对象字面量传给函数时，TypeScript 会做额外属性检查；先放入变量后再传入，结构兼容检查通常允许多余字段。额外属性检查是帮助发现拼写错误的规则，不代表对象运行时不能有其他属性。

## 6. `implements`：检查类是否满足契约

JavaScript 本身没有 `implements` 语法。TypeScript 类可以用它表达并检查“这个类提供这些公开成员”：

```typescript
interface Store {
  get(key: string): string | undefined;
  set(key: string, value: string): void;
}

class MemoryStore implements Store {
  private data = new Map<string, string>();

  get(key: string): string | undefined {
    return this.data.get(key);
  }

  set(key: string, value: string): void {
    this.data.set(key, value);
  }
}
```

`implements Store` 会在编译期检查类的公开成员是否满足接口，但不会替类生成方法，也不会在运行时验证实例。接口也不只用于类：更常见的情况是用它描述函数参数、返回值和普通对象。

## 7. 接口组合与 `interface` / `type` 的选择

可以通过 `extends` 组合接口，避免重复声明公共字段：

```typescript
interface HasId {
  id: number;
}

interface UserRecord extends HasId {
  name: string;
}

const user: UserRecord = { id: 1, name: '小林' };
```

### 交叉：一个值同时满足多个接口

如果一个对象同时具有两组成员，可以让接口 `extends` 多个接口，也可以用交叉类型 `&` 组合接口形状：

```typescript
interface HasId {
  id: number;
}

interface HasTimestamps {
  createdAt: Date;
}

interface UserProfile extends HasId, HasTimestamps {
  name: string;
}

// 交叉类型也要求同时具备所有成员
type AuditedUser = UserProfile & { active: boolean };

const user: AuditedUser = {
  id: 1,
  createdAt: new Date(),
  name: '小林',
  active: true,
};
```

这里的 `extends` 是接口声明的扩展方式，`&` 是类型层面的交叉运算；两者表达的核心要求都是“成员要齐全”。若交叉的同名属性类型互不兼容（例如 `string` 与 `number`），该属性会变成无法正常赋值的类型；设计上应统一字段类型，而不是依赖交叉来消除冲突。

### 联合：一个值可以是多种接口形状之一

联合类型表示“满足其中一种即可”。TypeScript 不能用 `interface` 声明直接写出 `A | B`，需要用 `type` 给若干接口组成的联合命名：

```typescript
interface CardPayment {
  kind: 'card';
  lastFour: string;
}

interface BankPayment {
  kind: 'bank';
  accountId: string;
}

type Payment = CardPayment | BankPayment;

function describePayment(payment: Payment): string {
  switch (payment.kind) {
    case 'card': return `银行卡尾号 ${payment.lastFour}`;
    case 'bank': return `银行账户 ${payment.accountId}`;
  }
}
```

`kind` 是**可辨识字段**：它让 TypeScript 和读代码的人都能看出当前是哪一种形状。未收窄前，只能安全访问所有分支共有的成员；进入某个 `kind` 分支后，才可访问该分支独有的属性。普通 JavaScript 也能在运行时检查 `payment.kind` 并分支处理，TS 额外在编译期检查每个分支访问的字段是否存在。更多可辨识联合见 [[topics/programming/Web/typescript/intro]] 的联合类型章节。

接口和类型别名都能描述对象形状，常见区别如下：

| 场景 | 通常选择 |
|------|----------|
| 对象/类的公开契约，期望通过 `extends` 扩展 | `interface` |
| 联合、交叉、元组、条件类型、映射类型等组合类型 | `type` |
| 需要同名声明合并（如扩展全局或第三方接口） | `interface` |

```typescript
interface AppConfig {
  host: string;
}

interface AppConfig {
  port: number;
}

// 两次 interface 声明会合并，AppConfig 同时要求 host 和 port。
const config: AppConfig = { host: 'localhost', port: 3000 };
```

更多语法细节、索引签名和选型说明见 [[topics/programming/Web/typescript/intro]] 的接口章节；联合与交叉的类型集合视角见 [[topics/programming/Web/typescript/type-system]]。实际项目中，保持团队风格一致通常比争论 `interface` 或 `type` 更重要。

## 8. 接口不等于运行时校验

接口只供 TypeScript 在开发期检查。接口编译后不存在，因此不能凭它判断服务器真的返回了正确数据：

```typescript
interface ApiUser {
  id: number;
  name: string;
}

const response: unknown = await fetch('/api/user').then(r => r.json());
// 不能仅靠 `response as ApiUser` 确认数据正确；断言不会执行检查。
```

HTTP 响应、表单输入、`localStorage` 内容等外部数据应先做**运行时校验**，校验成功后再当作 `ApiUser` 使用；可使用 schema 校验库（如 Zod），或编写明确的类型守卫。相关基础见 [[topics/programming/Web/typescript/intro]] 的类型收窄与断言章节。

## 9. 何时值得使用接口

- 函数会被多个模块调用，需要清楚说明参数/返回值形状。
- 同一种数据在多个地方复用，想避免字段名称和类型漂移。
- 类或组件需要提供稳定的公开 API。
- 希望 IDE 支持补全、跳转和安全重构。
- 与服务器或第三方库交互，需要表达预期的数据形状（但边界仍需要运行时校验）。

如果对象只在一小段代码里使用，类型推断已足够清晰，就不必为每个临时对象都单独造一个接口。

## 小结

JavaScript 的对象使用方式灵活，约定常散落在调用代码和文档里；TypeScript 接口把这些约定集中成可复用、可检查的类型契约。它提升的是开发期的沟通、补全与错误发现能力，**不会替代 JavaScript 对象，也不会替代运行时数据校验**。

继续阅读：[[topics/programming/Web/typescript/intro]] → [[topics/programming/Web/typescript/type-system]]。
