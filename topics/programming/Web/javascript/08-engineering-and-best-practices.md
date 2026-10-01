---
title: "JavaScript 核心知识体系 · 八、工程化与最佳实践"
tags:
  - programming
  - javascript
created: 2026-09-10
updated: 2026-10-01
---

# 八、工程化与最佳实践

> 📚 本文是 [[topics/programming/Web/javascript|JavaScript 核心知识体系]] 的第 8 / 8 章。 上一章：[[topics/programming/Web/javascript/07-error-handling-and-debugging|七、错误处理与调试]]


> **本章定位：** 当代码从"个人脚本"成长为"团队协作项目"时，规范、设计模式和性能优化就变得至关重要。本章将带你从"会写代码"走向"会写工程代码"。
>
> **学习路线：** 代码规范（严格模式、ESLint、Prettier）→ 设计模式（单例、工厂、观察者、策略、代理）→ 性能优化（内存管理、性能分析、代码分割）→ 综合项目实战
>
> **建议：** 设计模式不需要死记硬背，关键是理解每种模式解决了什么问题。当你在实际项目中遇到类似问题时，自然会想起"哦，这种情况可以用观察者模式"。

### 8.1 代码规范

#### 严格模式（use strict）

**一句话理解：** `"use strict"` 是 JavaScript 的"严格检查开关"，开启后引擎会拒绝一些不安全的语法（如隐式声明全局变量），并抛出错误，帮助你在开发阶段发现潜在问题。

```js
'use strict';

// ❌ 隐式创建全局变量（非严格模式下不会报错）
function sloppy() {
  x = 10; // ReferenceError: x is not defined
}

// ❌ 删除不可删除的属性
delete Object.prototype; // TypeError

// ❌ 重复参数名
function dup(a, a) { // SyntaxError
  return a;
}

// ❌ 八进制字面量
const num = 010; // SyntaxError

// ❌ this 默认绑定到 undefined（而非 window）
function showThis() {
  console.log(this); // undefined
}
showThis();
```

**启用方式：**
```js
// 方式 1：脚本顶部（对整个脚本生效）
'use strict';
const x = 1;

// 方式 2：函数内部（仅对该函数生效）
function strictFn() {
  'use strict';
  // ...
}

// 方式 3：ES Module 自动严格模式（无需手写）
// 所有 import/export 模块默认就是严格模式
```

**现代工程中的实践：**
- 使用 ES Modules 或打包工具（Webpack/Vite）时，模块自动进入严格模式，通常不需要手动写 `"use strict"`
- 遗留的 IIFE 或独立 `<script>` 标签脚本中仍可显式声明

---

#### 代码风格与 Lint 工具（ESLint / Prettier）

**为什么需要代码规范？**
- 团队协作时代码风格一致，降低阅读成本
- 自动发现潜在错误（如未使用变量、== 比较、异步函数未 await）
- 格式化工具消除关于"是否加分号""缩进几个空格"的无效争论

**ESLint：代码质量检查**

```bash
# 初始化 ESLint
npm init @eslint/config

# 常用预设：
# - eslint:recommended（基础推荐规则）
# - airbnb（最严格的社区规范）
# - standard（无分号风格）
```

`.eslintrc.json` 示例：
```json
{
  "env": {
    "browser": true,
    "es2022": true,
    "node": true
  },
  "extends": "eslint:recommended",
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "rules": {
    "no-unused-vars": ["warn", { "argsIgnorePattern": "^_" }],
    "eqeqeq": ["error", "always"],
    "curly": ["error", "all"],
    "no-var": "error",
    "prefer-const": "warn"
  }
}
```

**Prettier：代码格式化**

```bash
npm install --save-dev prettier
```

`.prettierrc` 示例：
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 100
}
```

**ESLint + Prettier 配合使用：**
```bash
npm install --save-dev eslint-config-prettier eslint-plugin-prettier
```

```json
// .eslintrc.json
{
  "extends": [
    "eslint:recommended",
    "plugin:prettier/recommended" // 关闭与 Prettier 冲突的规则，并将 Prettier 作为 ESLint 规则运行
  ]
}
```

**package.json 脚本集成：**
```json
{
  "scripts": {
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "format": "prettier --write src/"
  }
}
```

**关键细节：**
- `eslint --fix` 能自动修复大量格式问题（如引号、分号、缩进）
- 推荐在 IDE 中安装 ESLint 和 Prettier 插件，保存时自动格式化
- 团队项目应在 Git 钩子（husky + lint-staged）中强制提交前检查，防止不规范代码进入仓库


### 8.2 设计模式（JavaScript 实现）

设计模式是解决常见软件设计问题的**可复用方案**。在 JavaScript 中，由于语言的动态性和一等函数特性，某些模式的实现比传统 OOP 语言更简洁。

---

#### 单例模式（Singleton）

**一句话理解：** 确保一个类只有一个实例，并提供一个全局访问点。常用于配置管理、全局状态、数据库连接池等。

```js
class Singleton {
  constructor() {
    if (Singleton.instance) {
      return Singleton.instance;
    }
    this.data = {};
    Singleton.instance = this;
  }

  set(key, value) {
    this.data[key] = value;
  }

  get(key) {
    return this.data[key];
  }
}

const a = new Singleton();
const b = new Singleton();
a.set('name', 'Alice');
console.log(b.get('name')); // "Alice"
console.log(a === b);       // true
```

**使用闭包的替代实现（隐藏 instance）：**
```js
const Singleton = (function () {
  let instance;

  function createInstance() {
    return { data: {}, createdAt: Date.now() };
  }

  return {
    getInstance() {
      if (!instance) {
        instance = createInstance();
      }
      return instance;
    }
  };
})();
```

**现代简化版（ES Module 天然单例）：**
```js
// config.js
const config = {
  apiBase: 'https://api.example.com',
  timeout: 5000
};

export default config; // 模块只加载一次，天然单例
```

---

#### 工厂模式（Factory）

**一句话理解：** 不直接 `new` 对象，而是通过一个"工厂函数"根据参数创建不同类型的对象。适合创建逻辑复杂、类型多样的对象。

```js
class Notification {
  send(message) {
    throw new Error('子类必须实现 send 方法');
  }
}

class EmailNotification extends Notification {
  send(message) {
    console.log(`[Email] ${message}`);
  }
}

class SmsNotification extends Notification {
  send(message) {
    console.log(`[SMS] ${message}`);
  }
}

class PushNotification extends Notification {
  send(message) {
    console.log(`[Push] ${message}`);
  }
}

// 工厂函数
function createNotification(type) {
  switch (type) {
    case 'email': return new EmailNotification();
    case 'sms':   return new SmsNotification();
    case 'push':  return new PushNotification();
    default:      throw new Error(`未知通知类型: ${type}`);
  }
}

// 使用
const notifier = createNotification('email');
notifier.send('订单已发货');
```

**简单工厂 vs 工厂方法 vs 抽象工厂：**
- 简单工厂：一个函数根据参数创建对象（如上例）
- 工厂方法：把创建逻辑延迟到子类
- 抽象工厂：创建相关对象族（如 UI 组件库的主题切换）

---

#### 观察者模式（Observer / Pub-Sub）

**一句话理解：** 定义对象间的一对多依赖，当一个对象状态改变时，所有依赖它的对象都会自动收到通知。

```js
class Subject {
  constructor() {
    this.observers = [];
  }

  subscribe(observer) {
    this.observers.push(observer);
  }

  unsubscribe(observer) {
    this.observers = this.observers.filter(obs => obs !== observer);
  }

  notify(data) {
    this.observers.forEach(observer => observer.update(data));
  }
}

class Observer {
  constructor(name) {
    this.name = name;
  }
  update(data) {
    console.log(`${this.name} 收到数据:`, data);
  }
}

// 使用
const subject = new Subject();
const obs1 = new Observer('观察者A');
const obs2 = new Observer('观察者B');

subject.subscribe(obs1);
subject.subscribe(obs2);

subject.notify({ temperature: 25 }); // 两个观察者都会收到
```

**与发布订阅模式的区别：**
- **观察者模式**：Subject 直接管理 Observer 列表，耦合度稍高
- **发布订阅模式**：引入事件中心（Event Bus），发布者和订阅者不直接感知对方，完全解耦

---

#### 策略模式（Strategy）

**一句话理解：** 定义一系列算法，把它们一个个封装起来，并且使它们可以互相替换。避免大量的 `if...else` 或 `switch`。

```js
// ❌ 传统写法：满屏 if/else
function calculatePrice(type, price) {
  if (type === 'normal') return price;
  if (type === 'member') return price * 0.9;
  if (type === 'vip')    return price * 0.8;
  if (type === 'promo')  return price * 0.7;
}

// ✅ 策略模式：算法即对象
const strategies = {
  normal: price => price,
  member: price => price * 0.9,
  vip:    price => price * 0.8,
  promo:  price => price * 0.7
};

function calculatePrice(type, price) {
  const strategy = strategies[type];
  if (!strategy) throw new Error(`未知策略: ${type}`);
  return strategy(price);
}

// 使用
console.log(calculatePrice('vip', 100)); // 80

// 动态添加新策略
strategies.blackFriday = price => price * 0.5;
```

**适用场景：**
- 表单验证规则（不同字段不同验证策略）
- 支付方式选择
- 排序算法切换
- 优惠券计算

---

#### 代理模式（Proxy）

**一句话理解：** 为对象提供一个替身（代理），以控制对这个对象的访问。常用于懒加载、权限校验、缓存、日志记录。

```js
// 基础示例：访问计数代理
const user = { name: 'Alice', age: 25 };

const proxyUser = new Proxy(user, {
  get(target, prop) {
    console.log(`读取属性: ${String(prop)}`);
    return target[prop];
  },
  set(target, prop, value) {
    console.log(`设置属性: ${String(prop)} = ${value}`);
    target[prop] = value;
    return true;
  }
});

proxyUser.name;      // 日志: 读取属性: name
proxyUser.age = 26;  // 日志: 设置属性: age = 26
```

**缓存代理（提升性能）：**
```js
function expensiveCompute(n) {
  console.log(`计算 ${n}...`);
  return n * n;
}

const cachedCompute = new Proxy(expensiveCompute, {
  cache: new Map(),
  apply(target, thisArg, args) {
    const key = JSON.stringify(args);
    if (this.cache.has(key)) {
      console.log('命中缓存');
      return this.cache.get(key);
    }
    const result = target.apply(thisArg, args);
    this.cache.set(key, result);
    return result;
  }
});

cachedCompute(5); // 计算 5...
cachedCompute(5); // 命中缓存
```

**验证代理（数据校验）：**
```js
const validator = {
  set(target, prop, value) {
    if (prop === 'age') {
      if (!Number.isInteger(value) || value < 0 || value > 150) {
        throw new TypeError('age 必须是 0-150 的整数');
      }
    }
    target[prop] = value;
    return true;
  }
};

const person = new Proxy({}, validator);
person.age = 25;  // ✅
person.age = -1;  // ❌ TypeError
```

**关键细节：**
- `Proxy` 是 ES6 原生支持的，比 Object.defineProperty 更强大，能拦截 13 种操作
- `Reflect` 工具对象常与 Proxy 配合使用，保持默认行为的正确性
- Vue 3 的响应式系统底层就是基于 `Proxy` 实现的


### 8.3 性能优化

#### 内存管理与垃圾回收机制

**一句话理解：** JavaScript 是自动内存管理的语言，引擎会自动回收不再使用的内存。但如果不小心保留了不必要的引用，就会造成**内存泄漏**。

**垃圾回收算法（核心两种）：**

1. **标记-清除（Mark-and-Sweep）**：最主流的算法
   - 从根对象（window/global）出发，遍历所有可到达的引用并"标记"
   - 未被标记的对象视为垃圾，会被回收

2. **引用计数（Reference Counting）**：旧式算法（IE6 的 COM 对象）
   - 对象被引用次数为 0 时回收
   - 缺陷：无法处理**循环引用**（已现代浏览器废弃）

```js
// 循环引用示例（旧版 IE 中会泄漏）
function leak() {
  const a = {};
  const b = {};
  a.ref = b;
  b.ref = a;
  // 函数结束后，a 和 b 互相引用，引用计数不为 0，但已无法从根访问
}
// 现代浏览器的标记-清除算法能正确处理这种情况
```

**常见内存泄漏场景：**

```js
// 1. 意外的全局变量
function createLeak() {
  leakedVar = 'I am global'; // 忘记 var/let/const
}

// 2. 闭包引用外部大对象
function setup() {
  const hugeData = new Array(1000000).fill('x');
  const btn = document.getElementById('btn');
  btn.addEventListener('click', () => {
    console.log('clicked');
    // 这个回调持有对 hugeData 的引用，即使 hugeData 从未在回调中使用
  });
}
// ✅ 修复：如果不需要，不要让闭包捕获大对象

// 3. 移除 DOM 元素但保留引用
const elements = [];
function remove() {
  const el = document.getElementById('temp');
  el.remove();
  elements.push(el); // ❌ 仍保留引用，DOM 元素无法回收
}
// ✅ 修复：remove 后清空引用  elements = []

// 4. 定时器/回调未清理
let timer = setInterval(() => { /* ... */ }, 1000);
// 组件销毁时必须 clearInterval(timer)

// 5. 事件监听未移除
function bind() {
  const handler = () => console.log('move');
  window.addEventListener('mousemove', handler);
  // 如果不再监听，必须 removeEventListener
}
```

**Chrome DevTools Memory 面板定位泄漏：**
1. Performance → Memory → 选择 Heap snapshot
2. 操作页面后点击 "Take snapshot"
3. 对比多个时间点的快照（Comparison view），查看哪些对象持续增长
4. 查看 Retainers 链，追踪是谁持有引用导致无法回收

---

#### 性能分析工具使用

**浏览器内置工具：**

| 工具 | 用途 | 关键指标 |
|---|---|---|
| **Performance** | 录制运行时性能 | FPS、Long Tasks、Layout/Scripting/Paint 耗时 |
| **Lighthouse** | 自动化性能审计 | FCP、LCP、CLS、TBT、Speed Index |
| **Memory** | 堆内存分析 | Heap Size、Retainers、Detached DOM |
| **Network** | 资源加载分析 | TTFB、Download Time、瀑布图 |

**核心 Web 指标（Core Web Vitals）：**

| 指标 | 全称 | 含义 | 良好标准 |
|---|---|---|---|
| **FCP** | First Contentful Paint | 首个内容渲染时间 | ≤ 1.8s |
| **LCP** | Largest Contentful Paint | 最大内容渲染时间 | ≤ 2.5s |
| **CLS** | Cumulative Layout Shift | 累积布局偏移 | ≤ 0.1 |
| **TBT** | Total Blocking Time | 总阻塞时间 | ≤ 200ms |
| **FID** | First Input Delay | 首次输入延迟 | ≤ 100ms |

**Performance API（代码中测量）：**
```js
// 测量函数执行时间
const start = performance.now();
doSomething();
const end = performance.now();
console.log(`耗时: ${(end - start).toFixed(2)}ms`);

// Performance Observer 监听核心指标
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log('LCP:', entry.startTime, entry.element);
  }
});
observer.observe({ entryTypes: ['largest-contentful-paint'] });

// 标记关键时间点
performance.mark('app-start');
// ... 加载逻辑 ...
performance.mark('app-ready');
performance.measure('app-load', 'app-start', 'app-ready');
```

---

#### 代码分割与按需加载

**一句话理解：** 不要把所有代码打包成一个巨大的 JS 文件，而是按路由、按功能拆分成小块，用户访问时才加载需要的部分。

**动态导入（ESM 原生支持）：**
```js
// ❌ 静态导入：无论是否用到，都会打包进主 chunk
import Chart from './chart.js';

// ✅ 动态导入：用到时才加载，打包工具会自动分割代码
async function showChart() {
  const { default: Chart } = await import('./chart.js');
  new Chart(container);
}

// 按钮点击时加载
button.addEventListener('click', showChart);
```

**Webpack/Vite 中的代码分割：**
```js
// 路由级懒加载（React 示例）
const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));

// 手动指定 chunk 名称（便于调试）
const Admin = lazy(() => import(/* webpackChunkName: "admin" */ './pages/Admin'));
```

**预加载关键 chunk：**
```js
// 用户鼠标悬停在"关于"链接时，预加载 About 页面代码
link.addEventListener('mouseenter', () => {
  import(/* webpackPrefetch: true */ './pages/About');
});
```

**关键细节：**
- 代码分割的收益：首屏加载快、缓存命中率高（第三方库单独 chunk，升级业务代码不影响 vendor 缓存）
- 过度分割的问题：HTTP/2 下虽然可以多路复用，但太多小文件仍会增加解析开销
- 一般建议：entry（入口）、vendor（第三方库）、route（路由页面）、async（异步功能模块）四层分割


### 🛠️ 实操：综合项目实战

#### 从零搭建一个符合 ESLint + Prettier 规范的 JavaScript 项目

**项目结构：**
```
my-project/
├── src/
│   ├── main.js
│   └── utils/
│       └── format.js
├── .eslintrc.json
├── .prettierrc
├── .editorconfig
├── package.json
└── .gitignore
```

**package.json：**
```json
{
  "name": "my-project",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "format": "prettier --write src/"
  },
  "devDependencies": {
    "eslint": "^8.57.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-prettier": "^5.1.0",
    "prettier": "^3.2.0",
    "vite": "^5.0.0"
  }
}
```

**.eslintrc.json：**
```json
{
  "env": {
    "browser": true,
    "es2022": true,
    "node": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:prettier/recommended"
  ],
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "rules": {
    "no-console": "warn",
    "no-unused-vars": ["warn", { "argsIgnorePattern": "^_" }],
    "eqeqeq": ["error", "always"],
    "curly": ["error", "all"],
    "no-var": "error",
    "prefer-const": "warn",
    "prefer-arrow-callback": "warn"
  }
}
```

**.prettierrc：**
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 100,
  "endOfLine": "lf"
}
```

**.editorconfig：**
```ini
root = true

[*]
charset = utf-8
indent_style = space
indent_size = 2
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
```

**Git 钩子配置（husky + lint-staged）：**
```bash
npm install --save-dev husky lint-staged
npx husky init
```

```json
// package.json 中添加
{
  "lint-staged": {
    "*.js": ["eslint --fix", "prettier --write"]
  }
}
```

```bash
# .husky/pre-commit
echo 'npx lint-staged' > .husky/pre-commit
```

---

#### 实现一个前端路由系统（Hash / History 模式）

```js
/**
 * 极简前端路由系统
 * 支持 Hash 模式（#/) 和 History 模式（/path）
 */
class Router {
  constructor(options = {}) {
    this.mode = options.mode || 'hash'; // 'hash' | 'history'
    this.routes = new Map();
    this.currentPath = '';
    this.beforeHooks = [];
    this.afterHooks = [];

    this.init();
  }

  // 注册路由
  register(path, handler) {
    this.routes.set(path, handler);
    return this;
  }

  // 导航前钩子
  beforeEach(hook) {
    this.beforeHooks.push(hook);
  }

  // 导航后钩子
  afterEach(hook) {
    this.afterHooks.push(hook);
  }

  init() {
    if (this.mode === 'hash') {
      // Hash 模式监听 hashchange
      window.addEventListener('hashchange', () => this.handleChange());
      // 初始化时处理当前 hash
      if (!location.hash) {
        location.hash = '/';
      } else {
        this.handleChange();
      }
    } else {
      // History 模式监听 popstate（浏览器前进后退）
      window.addEventListener('popstate', () => this.handleChange());
      // 拦截链接点击
      document.addEventListener('click', (e) => {
        const link = e.target.closest('a[data-router]');
        if (link) {
          e.preventDefault();
          this.push(link.getAttribute('href'));
        }
      });
      this.handleChange();
    }
  }

  getCurrentPath() {
    if (this.mode === 'hash') {
      return location.hash.slice(1) || '/';
    }
    return location.pathname || '/';
  }

  async handleChange() {
    const path = this.getCurrentPath();
    const from = this.currentPath;
    const to = path;

    // 执行 before 钩子
    for (const hook of this.beforeHooks) {
      const result = await hook(to, from);
      if (result === false) return; // 取消导航
    }

    this.currentPath = path;
    const handler = this.routes.get(path) || this.routes.get('*');

    if (handler) {
      handler({ path, params: this.extractParams(path) });
    } else {
      console.warn(`Route not found: ${path}`);
    }

    // 执行 after 钩子
    this.afterHooks.forEach(hook => hook(to, from));
  }

  extractParams(path) {
    // 简易参数提取：/user/:id → 匹配 /user/123
    for (const [routePath] of this.routes) {
      if (routePath.includes(':')) {
        // 先转义正则特殊字符，再替换参数占位符
        const escaped = routePath.replace(/[.+*?^${}()|[\]\\]/g, '\\$&');
        const regex = new RegExp('^' + escaped.replace(/:([^/]+)/g, '([^/]+)') + '$');
        const match = path.match(regex);
        if (match) {
          const keys = [...routePath.matchAll(/:([^/]+)/g)].map(m => m[1]);
          return Object.fromEntries(keys.map((k, i) => [k, match[i + 1]]));
        }
      }
    }
    return {};
  }

  push(path) {
    if (this.mode === 'hash') {
      location.hash = path;
    } else {
      history.pushState({}, '', path);
      this.handleChange();
    }
  }

  replace(path) {
    if (this.mode === 'hash') {
      // ⚠️ 不要用 location.replace()，会导致整页刷新！
      history.replaceState(null, '', '#' + path);
      this.handleChange();
    } else {
      history.replaceState({}, '', path);
      this.handleChange();
    }
  }

  back() {
    history.back();
  }
}

// ===== 使用示例 =====
const router = new Router({ mode: 'hash' });

router.beforeEach((to, from) => {
  console.log(`导航: ${from} → ${to}`);
  return true; // 返回 false 可取消导航
});

router
  .register('/', () => {
    document.getElementById('app').innerHTML = '<h1>首页</h1>';
  })
  .register('/about', () => {
    document.getElementById('app').innerHTML = '<h1>关于我们</h1>';
  })
  .register('/user/:id', ({ params }) => {
    document.getElementById('app').innerHTML = `<h1>用户 ${params.id}</h1>`;
  })
  .register('*', () => {
    document.getElementById('app').innerHTML = '<h1>404 Not Found</h1>';
  });
```

**Hash vs History 模式对比：**

| 特性 | Hash 模式 | History 模式 |
|---|---|---|
| URL 示例 | `/#/user/123` | `/user/123` |
| 浏览器支持 | 所有浏览器 | IE10+ |
| 服务器配置 | 不需要 | 需要配置 fallback 到 index.html |
| SEO 友好度 | 差（# 后内容通常不被索引） | 好 |
| 实现复杂度 | 简单 | 需处理 404 回退 |

---

#### 实现一个简易的状态管理库（类似 Redux 的核心 API：createStore / dispatch / subscribe）

```js
/**
 * 极简 Redux-like 状态管理库
 * 核心概念：
 * - State: 单一不可变状态树
 * - Action: 描述发生了什么的普通对象 { type: '...', ... }
 * - Reducer: 纯函数 (state, action) => newState
 * - Store: 持有 state、提供 dispatch 和 subscribe
 */

function createStore(reducer, initialState) {
  let state = initialState;
  const listeners = new Set();

  function getState() {
    return state;
  }

  function dispatch(action) {
    // 校验 action 格式
    if (!action || typeof action.type !== 'string') {
      throw new Error('Action 必须是一个包含 type 属性的对象');
    }

    // 调用 reducer 获取新状态
    const newState = reducer(state, action);

    // 只有在状态变化时才通知（浅比较）
    if (newState !== state) {
      state = newState;
      listeners.forEach(listener => listener(state, action));
    }

    return action;
  }

  function subscribe(listener) {
    listeners.add(listener);

    // 返回取消订阅函数
    return () => {
      listeners.delete(listener);
    };
  }

  // 初始化：派发一个特殊的 init action，让 reducer 返回初始状态
  dispatch({ type: '@@redux/INIT' });

  return { getState, dispatch, subscribe };
}

// ===== 使用示例 =====

// 1. 定义 Reducer（必须是纯函数）
const initialState = { count: 0, user: null };

function reducer(state = initialState, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, count: state.count + 1 };
    case 'DECREMENT':
      return { ...state, count: state.count - 1 };
    case 'SET_USER':
      return { ...state, user: action.payload };
    default:
      return state;
  }
}

// 2. 创建 Store
const store = createStore(reducer);

// 3. 订阅状态变化
const unsubscribe = store.subscribe((newState, action) => {
  console.log(`[${action.type}] 新状态:`, newState);
});

// 4. 派发 Action
store.dispatch({ type: 'INCREMENT' });       // count: 1
store.dispatch({ type: 'INCREMENT' });       // count: 2
store.dispatch({ type: 'SET_USER', payload: { name: 'Alice' } });
store.dispatch({ type: 'DECREMENT' });       // count: 1

// 5. 获取当前状态
console.log(store.getState());
// { count: 1, user: { name: 'Alice' } }

// 6. 取消订阅
unsubscribe();
```

**进阶：中间件机制（Logger 中间件示例）**

```js
function applyMiddleware(store, ...middlewares) {
  const originalDispatch = store.dispatch;

  // 包装 dispatch：让每个中间件都能拦截 action
  const middlewareAPI = {
    getState: store.getState,
    // ⚠️ 简化版限制：中间件内部 dispatch 不会经过其他中间件
    // Redux 真实实现通过闭包引用解决此问题
    dispatch: (action) => originalDispatch(action)
  };

  const chain = middlewares.map(mw => mw(middlewareAPI));

  //  compose 函数：将多个函数从右到左组合
  const composed = chain.reduceRight(
    (next, mw) => mw(next),
    originalDispatch
  );

  store.dispatch = composed;
  return store;
}

// Logger 中间件
function loggerMiddleware({ getState }) {
  return (next) => (action) => {
    console.log('⏩ dispatching:', action);
    const result = next(action);
    console.log('📦 next state:', getState());
    return result;
  };
}

// 使用中间件
const storeWithLogger = applyMiddleware(createStore(reducer), loggerMiddleware);
storeWithLogger.dispatch({ type: 'INCREMENT' });
// 输出:
// ⏩ dispatching: { type: 'INCREMENT' }
// 📦 next state: { count: 1, user: null }
```

**Redux 设计原则总结：**

| 原则 | 说明 |
|---|---|
| **单一数据源** | 整个应用的 state 存储在一个对象树中 |
| **State 只读** | 唯一改变 state 的方法是 dispatch action |
| **纯函数修改** | Reducer 必须是纯函数，相同的输入永远产生相同的输出 |

**关键细节：**
- Reducer 中禁止：修改传入参数、执行有副作用的操作（如 API 请求、路由跳转）、调用非纯函数（如 Date.now()、Math.random()）
- 实际项目中，异步操作（如 API 请求）应使用 Thunk 中间件或 Redux-Saga 处理
- 本实现省略了 combineReducers，实际 Redux 支持将多个 reducer 合并管理不同 state 分支
