---
title: "JavaScript 核心知识体系 · 七、错误处理与调试"
tags:
  - programming
  - javascript
created: 2026-09-10
updated: 2026-10-01
---

# 七、错误处理与调试

> 📚 本文是 [[topics/programming/Web/javascript|JavaScript 核心知识体系]] 的第 7 / 8 章。 上一章：[[topics/programming/Web/javascript/06-es6-modern-features|六、ES6+ 现代特性]] · 下一章：[[topics/programming/Web/javascript/08-engineering-and-best-practices|八、工程化与最佳实践]]


> **本章定位：** 写出能运行的代码只是第一步，写出能稳定运行、出了问题能快速定位的代码才是专业开发者的标志。
>
> **学习路线：** 错误类型（认识敌人）→ 异常处理（try/catch、全局捕获、错误上报）→ 调试技巧（DevTools、console 高级用法、性能分析）→ 错误处理演练
>
> **建议：** 调试是一项实践技能，光看不行。建议故意写几个有 bug 的函数，然后只用 DevTools（不用 console.log）来定位问题。

### 7.1 错误类型

#### 语法错误 / 运行时错误 / 逻辑错误

JavaScript 中的错误大致分为三类，排查思路各不相同：

| 错误类型 | 发生时机 | 表现形式 | 排查方法 |
|---|---|---|---|
| **语法错误**（Syntax Error） | 代码解析阶段，引擎还未执行 | 控制台红色报错，指出具体行号 | 根据提示检查括号、引号、关键字拼写 |
| **运行时错误**（Runtime Error） | 代码执行过程中 | 程序中断，抛出异常对象 | `try...catch` 捕获 + 断点调试 |
| **逻辑错误**（Logic Error） | 代码语法正确且能运行，但结果不对 | 无报错，但输出不符合预期 | 单步调试、添加断言、单元测试 |

**语法错误示例：**
```js
// ❌ 缺少闭合括号
if (true {
  console.log('hello');
}
// Uncaught SyntaxError: Unexpected token '{'

// ❌ 关键字拼写错误
const x = 1;
lety = 2;  // Uncaught SyntaxError: Unexpected identifier
```

**运行时错误示例：**
```js
// ❌ 访问 undefined 的属性
const user = null;
console.log(user.name); // Uncaught TypeError: Cannot read properties of null

// ❌ 调用非函数
const fn = undefined;
fn(); // Uncaught TypeError: fn is not a function

// ❌ 访问不存在的变量
console.log(notDefined); // Uncaught ReferenceError: notDefined is not defined
```

**逻辑错误示例：**
```js
// ❌ 本意是求 1 到 10 的和，但结果不对
function sum(n) {
  let result = 0;
  for (let i = 0; i <= n; i++) {
    result = i; // 逻辑错误：应该是 result += i;
  }
  return result;
}
console.log(sum(10)); // 10，期望 55
```

**排查优先级口诀：**
> 先查语法（能不能跑）→ 再查运行时（跑到哪崩了）→ 最后查逻辑（结果对不对）。

---

#### 内置错误类型（Error / TypeError / RangeError 等）

JavaScript 内置了 7 种标准错误构造函数，全部继承自 `Error`：

```js
// 错误原型链
// Error → TypeError / RangeError / ReferenceError / SyntaxError / URIError / EvalError / AggregateError
```

| 错误类型 | 触发场景 | 示例 |
|---|---|---|
| `Error` | 通用错误基类，通常手动抛出 | `throw new Error('Something wrong')` |
| `TypeError` | 类型不匹配（如 null 上取属性、非函数被调用） | `null.foo`、`123()` |
| `RangeError` | 数值超出允许范围 | `new Array(-1)`、`(123).toFixed(101)` |
| `ReferenceError` | 引用不存在的变量 | `console.log(x)`（x 未声明） |
| `SyntaxError` | 代码语法解析失败 | `JSON.parse('{bad}')` |
| `URIError` | URI 编码/解码失败 | `decodeURI('%')` |
| `AggregateError` | 多个错误聚合（Promise.any  reject 时） | `Promise.any([p1, p2])` 全部失败时 |

**自定义错误类型（继承 Error）：**
```js
class ValidationError extends Error {
  constructor(field, message) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}

function createUser(data) {
  if (!data.name) {
    throw new ValidationError('name', '用户名不能为空');
  }
}

try {
  createUser({});
} catch (err) {
  console.log(err.name);    // "ValidationError"
  console.log(err.field);   // "name"
  console.log(err.message); // "用户名不能为空"
}
```

**关键细节：**
- 自定义错误时务必设置 `this.name`，否则堆栈跟踪中显示的还是 `"Error"`
- `Error` 实例包含 `message`（描述）和 `stack`（堆栈跟踪字符串）两个核心属性
- 不要用 `throw '字符串'` 或 `throw 404`，这会丢失堆栈信息，始终 `throw new Error(...)`


### 7.2 异常处理

#### try...catch...finally

**一句话理解：** `try` 包裹可能出错的代码；一旦出错，`catch` 捕获错误并处理；无论是否出错，`finally` 中的代码都会执行（常用于清理资源）。

```js
try {
  const data = JSON.parse(userInput);
  console.log(data.name);
} catch (err) {
  // err 是抛出的错误对象
  console.error('解析失败:', err.message);
} finally {
  // 无论 try 成功还是 catch 执行了，finally 都会执行
  console.log('清理工作完成');
}
```

**catch 捕获的匹配规则：**
- `try` 中**同步代码**抛出的错误会被 `catch` 捕获
- `try` 中**异步回调**里抛出的错误**无法被外部 catch 捕获**

```js
// ❌ 异步错误无法被外部 catch 捕获
try {
  setTimeout(() => {
    throw new Error('异步错误');
  }, 0);
} catch (err) {
  // 这里捕获不到！
  console.log(err);
}

// ✅ 正确做法：在异步回调内部 try/catch
setTimeout(() => {
  try {
    throw new Error('异步错误');
  } catch (err) {
    console.log('捕获到:', err.message);
  }
}, 0);

// ✅ 或者 Promise 用 .catch()
Promise.resolve()
  .then(() => {
    throw new Error('Promise 错误');
  })
  .catch(err => {
    console.log('Promise 捕获:', err.message);
  });
```

**try...catch 的性能考量：**
- `try...catch` 本身几乎没有性能开销，但**发生错误时**创建错误对象和堆栈跟踪比较昂贵
- 不要把整个函数体包在 try...catch 中，只包裹真正可能出错的最小代码块

```js
// ❌ 过度包裹
function process(data) {
  try {
    const a = step1(data);
    const b = step2(a);
    const c = step3(b);
    return c;
  } catch (err) {
    console.error(err);
  }
}

// ✅ 精确包裹
function process(data) {
  const a = step1(data);
  let b;
  try {
    b = step2(a); // 只有这一步可能出错
  } catch (err) {
    console.error('step2 失败:', err);
    b = defaultValue;
  }
  const c = step3(b);
  return c;
}
```

---

#### 全局错误捕获（error 事件 / unhandledrejection）

**页面级错误兜底：**
```js
// 捕获同步错误和资源加载错误（如图片 404、脚本加载失败）
window.addEventListener('error', (event) => {
  console.log('错误信息:', event.message);
  console.log('出错文件:', event.filename);
  console.log('行号:', event.lineno);
  console.log('列号:', event.colno);
  console.log('错误对象:', event.error);

  // 上报到监控服务
  reportError({
    message: event.message,
    stack: event.error?.stack,
    url: location.href
  });
});

// 捕获未处理的 Promise 拒绝（异步错误兜底）
window.addEventListener('unhandledrejection', (event) => {
  console.log('未处理的 Promise 错误:', event.reason);

  // 上报
  reportError({
    message: event.reason?.message || String(event.reason),
    stack: event.reason?.stack,
    type: 'unhandledrejection'
  });

  // 阻止控制台报错（可选）
  event.preventDefault();
});

// 捕获已处理的 Promise 拒绝（之前未被处理的 rejection 后来被 .catch() 处理了）
window.addEventListener('rejectionhandled', (event) => {
  console.log('之前未处理的 rejection 已被处理:', event.reason);
});
```

**Error Boundary 思想（纯 JS 实现）：**
```js
function safeExec(fn, fallback = null) {
  try {
    return fn();
  } catch (err) {
    console.error('safeExec 捕获:', err);
    return fallback;
  }
}

// 使用
const result = safeExec(() => JSON.parse(maybeInvalidJson), {});
```

**关键细节：**
- `window.onerror` 是老式写法，已被 `addEventListener('error')` 取代
- 跨域脚本（`crossorigin` 未设置）的错误信息会被浏览器抹除，只能看到 `"Script error."`
- 要获取完整堆栈，需在 `<script>` 标签加 `crossorigin="anonymous"`，且服务器返回 `Access-Control-Allow-Origin`

---

#### 错误上报与监控

**前端错误上报的核心数据：**
```js
function captureError(error, context = {}) {
  const report = {
    // 错误信息
    message: error.message,
    stack: error.stack,
    name: error.name,

    // 环境信息
    url: location.href,
    userAgent: navigator.userAgent,
    timestamp: Date.now(),

    // 自定义上下文
    ...context
  };

  // 发送到监控系统（使用 sendBeacon 保证页面关闭前也能发出）
  if (navigator.sendBeacon) {
    navigator.sendBeacon('/api/log', JSON.stringify(report));
  } else {
    // fallback：IE 不支持 sendBeacon
    fetch('/api/log', { method: 'POST', body: JSON.stringify(report), keepalive: true });
  }
}
```

**图片 Ping 上报（兼容旧浏览器）：**
```js
function reportByImage(url, data) {
  const img = new Image();
  img.src = `${url}?data=${encodeURIComponent(JSON.stringify(data))}`;
}
```

**错误采样与限频（避免错误风暴拖垮服务器）：**
```js
class ErrorReporter {
  constructor(options = {}) {
    this.sampleRate = options.sampleRate || 1; // 1 = 100% 上报
    this.maxErrorsPerMinute = options.maxErrorsPerMinute || 10;
    this.errorCount = 0;
    this.resetTimer = setInterval(() => {
      this.errorCount = 0;
    }, 60000);
  }

  destroy() {
    clearInterval(this.resetTimer);
  }

  report(error, context) {
    if (Math.random() > this.sampleRate) return;
    if (this.errorCount >= this.maxErrorsPerMinute) return;

    this.errorCount++;
    navigator.sendBeacon('/api/errors', JSON.stringify({
      message: error.message,
      stack: error.stack,
      url: location.href,
      ...context
    }));
  }
}

const reporter = new ErrorReporter({ sampleRate: 0.1 }); // 只上报 10%
```

**关键细节：**
- `navigator.sendBeacon` 是异步、非阻塞的，且会在页面卸载前尽力发送，比 `fetch` 更适合错误上报
- 生产环境应**去重相同错误**（按 message + stack 前 3 行哈希），避免同一错误重复上报几千次
- 敏感信息（如用户 token、密码字段）应在发送前过滤掉


### 7.3 调试技巧

#### 浏览器 DevTools 调试

Chrome / Edge / Firefox 的 DevTools 是前端调试的核心工具，掌握以下面板能大幅提升定位问题的效率。

**Elements 面板（DOM & CSS）：**
- 实时编辑 HTML/CSS 并立即看到效果
- 用 `Ctrl+Shift+C`（或点击左上角箭头）快速选中页面元素
- 在 Styles 面板中点击样式规则前的 checkbox 可临时禁用某条 CSS
- Computed 面板查看元素最终计算后的样式值

**Console 面板：**
- 执行任意 JavaScript 代码
- 查看错误、警告、日志
- `$0` 引用当前在 Elements 面板选中的元素
- `$_` 引用上一个表达式的结果

**Sources 面板（断点调试）：**

| 操作 | 快捷键 | 作用 |
|---|---|---|
| 打断点 | 点击行号 | 执行到此处暂停 |
| 单步执行 | `F10` | 执行下一行，不进入函数内部 |
| 步入函数 | `F11` | 进入函数内部执行 |
| 步出函数 | `Shift+F11` | 执行完当前函数剩余部分并跳出 |
| 继续执行 | `F8` | 继续运行到下一个断点 |
| 禁用所有断点 | `Ctrl+F8` | 临时关闭断点 |

**条件断点：** 右键点击行号 → "Add conditional breakpoint"，可设置如 `i === 5` 的条件，仅在条件满足时暂停。

**Network 面板：**
- 查看所有 HTTP 请求的时序瀑布图
- 点击请求可查看 Headers、Preview、Response、Timing
- 勾选 Disable cache 可强制不读缓存
- 模拟慢速网络：Network → Throttling → Fast 3G / Slow 3G

**Application 面板：**
- 查看和编辑 localStorage / sessionStorage / Cookies
- 查看 Service Worker、Cache Storage
- 模拟离线状态（Service Workers → Offline checkbox）

**Performance 面板：**
- 录制页面运行过程，分析 CPU 占用、渲染帧率、函数调用栈
- 用于定位卡顿、长任务、强制同步布局等问题

---

#### console 高级用法

`console.log` 之外，还有大量实用的调试方法：

```js
const user = { name: 'Alice', age: 25, role: 'admin' };
const items = ['apple', 'banana', 'cherry'];

// 1. 表格形式展示数据
console.table(user);
console.table(items);
console.table([{ name: 'A', age: 20 }, { name: 'B', age: 30 }]);

// 2. 分组输出（可折叠）
console.group('用户数据');
console.log('姓名:', user.name);
console.log('年龄:', user.age);
console.groupEnd();

// 3. 条件输出（条件为 false 时打印）
console.assert(user.age > 30, '年龄不大于 30');

// 4. 计时器
console.time('耗时');
for (let i = 0; i < 1000000; i++) {}
console.timeEnd('耗时'); // "耗时: 2.345ms"

// 5. 计数器
console.count('点击');
console.count('点击');
console.countReset('点击'); // 重置计数

// 6. 堆栈跟踪
function foo() { bar(); }
function bar() { console.trace('跟踪到这里'); }
foo();
// 输出完整的调用栈：bar → foo → （全局）

// 7. 样式化输出
console.log('%c 成功 ', 'background: #22c55e; color: white; padding: 4px; border-radius: 4px;', '数据已保存');
console.log('%c 错误 ', 'background: #ef4444; color: white;', '保存失败');
```

**用 debugger 语句强制断点：**
```js
function complexCalc(data) {
  const step1 = data * 2;
  debugger; // 执行到这里会自动打开 DevTools 并暂停
  const step2 = step1 + 10;
  return step2;
}
```

---

#### 断点与性能分析

**长任务（Long Task）定位：**

浏览器要求每一帧在 16.6ms 内完成（60fps）。如果某个任务超过 50ms，就会被标记为 Long Task，导致页面卡顿。

```js
// 一段刻意制造的卡顿代码
function heavyCalculation() {
  const arr = [];
  for (let i = 0; i < 1000000; i++) {
    arr.push(Math.sqrt(i));
  }
  return arr;
}

// 优化：使用 requestIdleCallback 或分片执行
function chunkedCalculation(chunkSize = 10000) {
  const arr = [];
  let i = 0;

  function processChunk() {
    const end = Math.min(i + chunkSize, 1000000);
    for (; i < end; i++) {
      arr.push(Math.sqrt(i));
    }
    if (i < 1000000) {
      requestIdleCallback(processChunk); // 浏览器空闲时继续
    }
  }

  processChunk();
  return arr;
}
```

**Performance 面板分析步骤：**
1. 打开 Performance → 点击录制按钮（◉）
2. 在页面上执行卡顿的操作
3. 停止录制 → 查看 Main 线程的火焰图
4. 找到宽长的黄色条（Scripting）→ 点击展开查看具体函数调用栈

**强制同步布局（Forced Synchronous Layout）检测：**

```js
// ❌ 错误示范：读-写-读-写交替
const boxes = document.querySelectorAll('.box');
boxes.forEach(box => {
  const height = box.offsetHeight;      // 读取（触发布局）
  box.style.height = height * 2 + 'px'; // 写入（标记需要布局）
});
// 每次循环都触发一次布局，性能极差

// ✅ 正确示范：先批量读取，再批量写入
const heights = [];
boxes.forEach(box => {
  heights.push(box.offsetHeight); // 批量读取
});
boxes.forEach((box, i) => {
  box.style.height = heights[i] * 2 + 'px'; // 批量写入
});
```

**Lighthouse 快速性能审计：**
- DevTools → Lighthouse 标签 → 选择 Categories（Performance、Accessibility、Best Practices）→ Analyze
- 会生成性能评分和优化建议（如减少主线程工作、图片压缩、移除未使用 JS）


### 🛠️ 实操：错误处理演练

#### 为一个小型项目添加统一的错误边界（全局 try/catch + 错误上报）

```js
/**
 * 统一错误边界系统
 * 功能：
 * 1. 全局捕获同步和异步错误
 * 2. 统一格式化错误信息
 * 3. 上报到监控端点（带采样和限频）
 * 4. 用户友好的错误提示（替代控制台红字）
 */

class ErrorBoundary {
  constructor(options = {}) {
    this.endpoint = options.endpoint || '/api/log';
    this.sampleRate = options.sampleRate || 1;
    this.maxPerMinute = options.maxPerMinute || 20;
    this.count = 0;

    // 每分钟重置计数
    this.resetTimer = setInterval(() => { this.count = 0; }, 60000);

    this.init();
  }

  destroy() {
    clearInterval(this.resetTimer);
  }

  init() {
    // 1. 全局同步错误捕获
    window.addEventListener('error', (event) => {
      this.handleError(event.error, {
        type: 'window.error',
        filename: event.filename,
        lineno: event.lineno
      });
      event.preventDefault();
    });

    // 2. 全局 Promise 错误捕获
    window.addEventListener('unhandledrejection', (event) => {
      this.handleError(
        event.reason instanceof Error ? event.reason : new Error(String(event.reason)),
        { type: 'unhandledrejection' }
      );
      event.preventDefault();
    });

    // 3. 包装 console.error，也纳入上报
    const originalError = console.error;
    console.error = (...args) => {
      originalError.apply(console, args);
      const message = args.map(a => (a instanceof Error ? a.message : String(a))).join(' ');
      if (message) {
        this.report({ message, stack: '', type: 'console.error' }, false);
      }
    };
  }

  handleError(error, context = {}) {
    if (!error) return;

    // 展示用户友好的提示
    this.showUserFeedback(error);

    // 上报
    this.report(error, context);
  }

  showUserFeedback(error) {
    // 避免重复创建提示框
    if (document.getElementById('error-toast')) return;

    const toast = document.createElement('div');
    toast.id = 'error-toast';
    toast.style.cssText = `
      position: fixed; bottom: 20px; right: 20px; background: #ef4444; color: white;
      padding: 12px 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);
      font-family: sans-serif; z-index: 9999; max-width: 400px;
    `;
    toast.innerHTML = `
      <strong>⚠️ 出错了</strong><br>
      <small>${error.message}</small><br>
      <button id="dismiss-error" style="margin-top:8px;padding:4px 12px;border:none;border-radius:4px;cursor:pointer;">关闭</button>
    `;
    document.body.appendChild(toast);

    document.getElementById('dismiss-error').addEventListener('click', () => {
      toast.remove();
    });

    setTimeout(() => toast.remove(), 8000);
  }

  report(error, context, shouldSample = true) {
    if (shouldSample && Math.random() > this.sampleRate) return;
    if (this.count >= this.maxPerMinute) return;
    this.count++;

    const payload = {
      message: error.message || String(error),
      stack: error.stack || '',
      name: error.name || 'Error',
      url: location.href,
      userAgent: navigator.userAgent,
      timestamp: Date.now(),
      ...context
    };

    if (navigator.sendBeacon) {
      navigator.sendBeacon(this.endpoint, JSON.stringify(payload));
    } else {
      fetch(this.endpoint, {
        method: 'POST',
        body: JSON.stringify(payload),
        keepalive: true
      }).catch(() => {});
    }
  }
}

// 启动错误边界
const boundary = new ErrorBoundary({
  endpoint: 'https://your-monitor.com/api/errors',
  sampleRate: 1.0,
  maxPerMinute: 30
});

// 使用示例：在业务代码中手动上报
function riskyOperation() {
  try {
    return JSON.parse(maybeJson);
  } catch (err) {
    boundary.handleError(err, { module: 'riskyOperation', userId: 123 });
    return null;
  }
}
```

---

#### 使用 DevTools Performance 面板分析并优化一段卡顿代码

**以下是一段有性能问题的代码，作为分析对象：**

```js
// ❌ 问题代码：强制同步布局 + 无意义的 DOM 操作
function updateLayout() {
  const boxes = document.querySelectorAll('.box');

  boxes.forEach((box, index) => {
    // 读取布局属性（触发布局）
    const width = box.offsetWidth;
    const height = box.offsetHeight;

    // 写入样式（标记需要重排）
    box.style.width = (width + 10) + 'px';
    box.style.height = (height + 10) + 'px';
    box.textContent = `Box ${index}: ${width}x${height}`;

    // 再次读取（浏览器被迫立即重新计算布局）
    console.log(box.offsetWidth);
  });
}

setInterval(updateLayout, 100);
```

**Performance 面板分析步骤：**
1. 打开 Chrome DevTools → Performance 标签
2. 点击 ⏺ 开始录制
3. 等待 2-3 秒后点击 ⏹ 停止
4. 在 Main 线程火焰图中看到大量紫色（Layout）和黄色（Scripting）交替的条形
5. 底部 Summary 显示 Layout 占用了大量时间

**优化后的代码：**

```js
// ✅ 优化方案：批量读写分离 + requestAnimationFrame + 缓存引用
const boxes = document.querySelectorAll('.box');

function updateLayoutOptimized() {
  // 1. 批量读取（第一阶段）
  const measurements = [];
  boxes.forEach((box, index) => {
    measurements.push({
      index,
      width: box.offsetWidth,
      height: box.offsetHeight,
      box // 缓存引用
    });
  });

  // 2. 批量写入（第二阶段）
  measurements.forEach(({ index, width, height, box }) => {
    const newWidth = width + 10;
    const newHeight = height + 10;
    // ⚠️ cssText 会覆盖元素所有内联样式，如有其他样式请逐个设置
    box.style.width = `${newWidth}px`;
    box.style.height = `${newHeight}px`;
    box.textContent = `Box ${index}: ${newWidth}x${newHeight}`;
  });
}

// 3. 使用 rAF 代替 setInterval，与刷新率同步
function loop() {
  updateLayoutOptimized();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

**优化效果验证：**
重新录制 Performance，对比优化前后：
- 优化前：Layout 占比 > 60%，帧率 < 20fps
- 优化后：Layout 占比 < 10%，帧率稳定在 60fps

---

#### 编写一组刻意包含错误的代码，仅用调试工具定位并修复（不 console.log）

**练习代码（包含 5 个隐藏错误）：**

```js
// 目标：实现一个简单的购物车，但代码中有 5 个 bug
// 规则：不使用 console.log，仅用 DevTools 断点和 Watch 定位问题

const cart = {
  items: [],

  add(product) {
    const existing = this.items.find(item => item.id = product.id); // Bug 1
    if (existing) {
      existing.qty++;
    } else {
      this.items.push({ ...product, qty: 1 });
    }
    this.updateUI();
  },

  remove(productId) {
    const idx = this.items.indexOf(item => item.id === productId); // Bug 2
    this.items.splice(idx, 1);
    this.updateUI();
  },

  getTotal() {
    return this.items.reduce((sum, item) => {
      return sum + item.price * item.qty; // Bug 3
    });
  },

  updateUI() {
    const list = document.getElementById('cart-list');
    list.innerHTML = this.items.map(item => `
      <li>${item.name} x ${item.qty} = $${item.price * item.qty}</li>
    `); // Bug 4
    document.getElementById('total').textContent = this.getTotal();
  },

  checkout() {
    fetch('/api/checkout', {
      method: 'POST',
      body: { items: this.items } // Bug 5
    });
  }
};

// 初始化
const products = [
  { id: 1, name: 'Apple', price: 1.5 },
  { id: 2, name: 'Banana', price: 0.8 }
];

document.getElementById('add-apple').addEventListener('click', () => cart.add(products[0]));
document.getElementById('add-banana').addEventListener('click', () => cart.add(products[1]));
```

**答案与修复（供参考）：**

| Bug | 位置 | 问题 | 修复 |
|---|---|---|---|
| 1 | `find` 回调 | 使用了赋值 `=` 而非比较 `===`，导致 `existing` 永远为 truthy | 改为 `item.id === product.id` |
| 2 | `indexOf` | `indexOf` 不支持回调函数，应使用 `findIndex` | 改为 `this.items.findIndex(...)` |
| 3 | `reduce` | `reduce` 缺少初始值 `0`，当数组为空时返回 `undefined` | 改为 `reduce(..., 0)` |
| 4 | `map` 结果 | `map` 返回数组，直接赋值给 `innerHTML` 会得到逗号分隔的字符串 | 改为 `.map(...).join('')` |
| 5 | `fetch` body | `body` 必须是字符串或 FormData，不能直接传对象 | 改为 `body: JSON.stringify({...})` 并添加 `headers: { 'Content-Type': 'application/json' }` |

**调试技巧提示：**
- 在 `add` 方法的 `find` 行打断点，用 Watch 面板观察 `existing` 的值
- 在 `getTotal` 的 `reduce` 行打断点，观察每次迭代的 `sum` 和返回值
- 在 Network 面板查看 `checkout` 请求，发现 Payload 格式不对


> **本章小结：** 我们学习了 JavaScript 的错误类型、try/catch/finally 异常处理、全局错误捕获与上报机制，以及浏览器 DevTools 的调试技巧和性能分析方法。
>
> **下一章预告：** 最后一章将带我们进入工程化领域——代码规范、设计模式、内存管理与性能优化，以及如何从零搭建一个规范的前端项目。
