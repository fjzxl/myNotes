---
title: "CSS 入门指南 · 第八阶段：动画与交互 —— 让页面动起来"
tags:
  - programming
  - css
created: 2026-09-10
updated: 2026-10-01
---

# 第八阶段：动画与交互 —— 让页面动起来

> 📚 本文是 [[topics/programming/Web/css|CSS 入门指南]] 的第 8 / 10 章。 上一章：[[topics/programming/Web/css/stage-07-responsive-design|第七阶段：响应式设计]] · 下一章：[[topics/programming/Web/css/stage-09-modern-css|第九阶段：现代 CSS 进阶特性]]


> 🎯 **本节目标**：掌握过渡、变换和动画，能写出常见交互效果。
>
> 本节动画示例基于以下 HTML 结构：
>
> ```html
> <button class="button">悬停看我变色</button>
>
> <div class="card">
>   <p>悬停时我会向上浮动</p>
> </div>
>
> <div class="box">我会旋转和缩放</div>
>
> <div class="loading"></div>
> ```

### 🍎 生活比喻：动画就像电影

- **Transition（过渡）** = 淡入淡出（两个状态之间的平滑变化，如从暗到亮）
- **Transform（变换）** = 演员的姿势变化（移动、旋转、缩放）
- **Animation（动画）** = 完整电影（可以有很多帧，循环播放）

三者关系：**Transform 负责变形，Transition 负责平滑过渡，Animation 负责复杂关键帧动画。**

### 8.1 过渡（Transition）

元素从一种状态**平滑过渡**到另一种状态。

```css
.button {
  background-color: blue;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: red;
}
```

> 🍎 **比喻理解**：就像调光开关——不是瞬间变亮，而是慢慢从暗变亮。`0.3s` 就是"用 0.3 秒完成这个变化"。

#### 过渡属性详解

| 属性 | 语法 | 参数说明 | 可选值 | 默认值 |
|------|------|----------|--------|--------|
| `transition-property` | `transition-property: none\|all\|属性名` | 指定哪个CSS属性参与过渡 | `none`（无过渡）<br>`all`（所有可过渡属性）<br>具体属性名如 `width`、`opacity` | `all` |
| `transition-duration` | `transition-duration: 时间` | 过渡持续多久 | `0s`（无过渡）<br>`0.3s`（300毫秒）<br>`1.5s`（1.5秒） | `0s` |
| `transition-timing-function` | `transition-timing-function: 函数` | 过渡速度曲线 | 预定义：`ease` `linear` `ease-in` `ease-out` `ease-in-out`<br>贝塞尔：`cubic-bezier(n,n,n,n)`<br>阶跃：`steps(n, start\|end)` | `ease` |
| `transition-delay` | `transition-delay: 时间` | 延迟多久开始 | `0s`（立即开始）<br>`0.5s`（延迟500毫秒）<br>负值（提前开始） | `0s` |

**简写语法**：

```css
transition: property duration timing-function delay;

/* 示例 */
transition: opacity 0.3s ease-in-out 0.1s;
transition: all 0.5s linear;
transition: transform 0.3s ease, box-shadow 0.3s ease;
```

> ⚠️ **易错点**：简写时 `duration` 和 `delay` 都是时间值，浏览器通过顺序判断——第一个时间是 `duration`，第二个时间是 `delay`。

**哪些CSS属性可以过渡？**

| 分类 | 可过渡属性示例 |
|------|---------------|
| 颜色类 | `color`、`background-color`、`border-color`、`box-shadow` |
| 尺寸类 | `width`、`height`、`padding`、`margin`、`border-width` |
| 变换类 | `transform`（GPU加速，**推荐**） |
| 透明度 | `opacity`（GPU加速，**推荐**） |
| 滤镜 | `filter`（触发重绘，性能较差） |
| 定位 | `top`、`left`、`right`、`bottom`（触发重排，**避免**） |

**常用时间函数详解**：

| 值 | `cubic-bezier` 等价 | 效果描述 | 适用场景 |
|----|---------------------|----------|----------|
| `ease` | `cubic-bezier(0.25, 0.1, 0.25, 1)` | 慢-快-慢（默认） | 普通过渡 |
| `linear` | `cubic-bezier(0, 0, 1, 1)` | 匀速 | 颜色渐变 |
| `ease-in` | `cubic-bezier(0.42, 0, 1, 1)` | 慢开始，快结束 | 淡入、进入 |
| `ease-out` | `cubic-bezier(0, 0, 0.58, 1)` | 快开始，慢结束 | 淡出、离开 |
| `ease-in-out` | `cubic-bezier(0.42, 0, 0.58, 1)` | 对称的慢-快-慢 | 呼吸效果 |
| `steps(n, start\|end)` | — | 阶跃式变化 | 步进动画 |

```css
/* 贝塞尔曲线自定义速度 */
transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1); /* 带弹性的效果 */

/* 阶跃函数 - 适合翻页效果 */
transition: background-position 0.3s steps(4, end);
```

```css
/* 过渡多个属性 */
/* 💡 transition 必须写在基础状态，不要只写在 :hover 上，否则移出时没有过渡！ */
.card {
  transition:
    transform 0.3s ease,
    opacity 0.3s ease;
  opacity: 0.9;
}

.card:hover {
  transform: translateY(-5px);
  opacity: 1;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15); /* 仅改变值，不过渡 */
}
```

> 💡 **性能提示**：过渡 `transform` 和 `opacity` 性能最好（GPU加速）。尽量避免过渡 `width`、`height`、`top`、`left`、`margin`、`padding`（触发重排），以及 `box-shadow`、`filter`（触发重绘）。

### 8.2 变换（Transform）

#### 2D 变换函数详解

| 函数 | 语法 | 参数说明 | 示例效果 |
|------|------|----------|----------|
| `translate(x, y)` | `translate(水平px, 垂直px)` | 正值向右/下移动，负值向左/上移动<br>`translateX(tx)` 只水平移动<br>`translateY(ty)` 只垂直移动 | `translate(50px, 100px)` |
| `rotate(角度)` | `rotate(deg)` | 正值顺时针，负值逆时针<br>角度单位：`deg`（度）、`turn`（圈） | `rotate(45deg)`、`rotate(0.5turn)` |
| `scale(x, y)` | `scale(倍数)` | `scale(sx)` 宽高同缩放<br>`scale(sx, sy)` 宽高分别缩放<br>大于1放大，小于1缩小 | `scale(1.5)`、`scale(1, 1.2)` |
| `skew(x, y)` | `skew(角度deg)` | 沿X/Y轴倾斜扭曲<br>`skewX(ax)` 只沿X轴<br>`skewY(ay)` 只沿Y轴 | `skew(10deg, 5deg)` |
| `matrix(a, b, c, d, e, f)` | `matrix(6个数值)` | 2D矩阵变换（综合上述所有变换）<br>需要数学基础，一般用上面更直观 | `matrix(1,0,0,1,50,100)` |

```css
/* 2D 变换示例 */
transform: translate(50px, 100px); /* 平移 - 移动位置 */
transform: rotate(45deg); /* 旋转 - 转多少度 */
transform: scale(1.5); /* 缩放 - 放大缩小 */
transform: skew(10deg, 5deg); /* 倾斜 - 斜着拉 */

/* 单独轴向变换 */
transform: translateX(30px); /* 只向右移动30px */
transform: translateY(-20px); /* 只向上移动20px */
transform: scaleX(2); /* 只宽度放大2倍 */
transform: rotateZ(90deg); /* 只沿Z轴旋转（同rotate） */

/* 组合变换 */
/* ⚠️ transform 从右向左运算：先 translate（基于原始尺寸居中），再 scale */
transform: scale(1.1) translate(-50%, -50%);
```

#### 3D 变换函数详解

| 函数 | 语法 | 参数说明 | 示例效果 |
|------|------|----------|----------|
| `translate3d(x, y, z)` | `translate3d(tx, ty, tz)` | 3D空间平移 | `translate3d(0, 0, -50px)` |
| `rotateX(角度)` | `rotateX(deg)` | 沿X轴旋转（前后翻转） | `rotateX(45deg)` |
| `rotateY(角度)` | `rotateY(deg)` | 沿Y轴旋转（左右翻转） | `rotateY(45deg)` |
| `rotateZ(角度)` | `rotateZ(deg)` | 沿Z轴旋转（平面旋转） | `rotateZ(45deg)` |
| `scale3d(sx, sy, sz)` | `scale3d(sx, sy, sz)` | 3D空间缩放 | `scale3d(1, 1, 2)` |
| `perspective(距离)` | `perspective(px)` | 透视距离（设置在父元素）<br>值越小，透视越强烈 | `perspective(1000px)` |

```css
/* 3D 变换示例：父元素需要设置 perspective 才能看到立体效果 */
.parent {
  perspective: 1000px; /* 透视距离，值越大透视越平，值越小透视越强 */
  perspective-origin: center center; /* 透视原点 */
}

.child {
  transform: rotateX(45deg); /* 沿X轴旋转 */
  transform-style: preserve-3d; /* 保持3D空间（父元素设置） */
}
```

**常用3D变换效果**：

```css
/* 卡片翻转效果 */
.card {
  transform-style: preserve-3d;
  transition: transform 0.6s;
}
.card:hover {
  transform: rotateY(180deg);
}
.card-front,
.card-back {
  backface-visibility: hidden; /* 隐藏背面 */
}
.card-back {
  transform: rotateY(180deg); /* 背面预先翻转 */
}

/* 立方体效果 */
.cube {
  transform-style: preserve-3d;
  transform: rotateX(-30deg) rotateY(45deg);
}
.cube .face {
  position: absolute;
  width: 100px;
  height: 100px;
}
.front  { transform: translateZ(50px); }
.back   { transform: rotateY(180deg) translateZ(50px); }
.left   { transform: rotateY(-90deg) translateZ(50px); }
.right  { transform: rotateY(90deg) translateZ(50px); }
.top    { transform: rotateX(90deg) translateZ(50px); }
.bottom { transform: rotateX(-90deg) translateZ(50px); }
```

#### transform 相关属性

| 属性 | 作用 | 可选值 |
|------|------|--------|
| `transform-origin` | 变换原点（默认 center center） | `x y z` 或 `left/center/right` |
| `transform-style` | 保持3D空间 | `flat`（平面）、`preserve-3d`（3D空间） |
| `backface-visibility` | 背面是否可见 | `visible`、`hidden` |
| `perspective` | 透视距离（父元素设置） | `none`、`<length>` |

```css
/* 变换原点示例 */
.transform-origin-demo {
  transform-origin: top left; /* 绕左上角旋转 */
  transform: rotate(45deg);
}
```

> 🍎 **比喻理解**：
>
> - `translate` = 把照片从左边移到右边
> - `rotate` = 把照片转个角度
> - `scale` = 把照片放大或缩小
> - `skew` = 把照片斜着拉

> 💡 **居中技巧**：`position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);` 是元素绝对居中的经典方案。
>
> 🍎 **为什么需要 translate(-50%, -50%)？** 因为 `top: 50%` 是把元素的**顶部**放在中间，不是把元素中心放在中间。`translate(-50%, -50%)` 就是把元素往回拉自身宽高的一半，让中心点对齐。

### 8.3 动画（Animation）

#### @keyframes 关键帧定义

```css
/* 定义关键帧 - 两种语法 */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  50% {
    opacity: 0.5;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 使用动画 */
.element {
  opacity: 0; /* 初始隐藏，避免动画执行前元素瞬间可见的闪烁 */
  animation: slideUp 0.5s ease-out forwards;
}
```

> 🍎 **比喻理解**：`@keyframes` 就像电影分镜——
>
> - `0%` = 第一帧（电影开场）
> - `50%` = 中间帧（高潮）
> - `100%` = 最后一帧（结局）
> - `forwards` = 演完保持最后一帧的姿势（不散场）

#### 动画属性详解

| 属性 | 语法 | 参数说明 | 可选值 | 默认值 |
|------|------|----------|--------|--------|
| `animation-name` | `animation-name: name\|none` | 指定要使用的关键帧名称 | `@keyframes`定义的名称<br>`none`（无动画） | `none` |
| `animation-duration` | `animation-duration: 时间` | 动画持续时间 | `0s`（无动画）<br>`0.3s`、`1.5s` | `0s` |
| `animation-timing-function` | `animation-timing-function: 函数` | 动画速度曲线 | 同 transition-timing-function<br>预定义+贝塞尔+阶跃 | `ease` |
| `animation-delay` | `animation-delay: 时间` | 动画延迟开始时间 | `0s`（立即）<br>正值（延迟）<br>负值（提前，从中间开始） | `0s` |
| `animation-iteration-count` | `animation-iteration-count: n\|infinite` | 动画循环次数 | 具体数字 `1`、`3`<br>`infinite`（无限循环） | `1` |
| `animation-direction` | `animation-direction: 方向` | 动画播放方向 | `normal`（正向，从0%到100%）<br>`reverse`（反向，从100%到0%）<br>`alternate`（交替，来回播放）<br>`alternate-reverse`（反向交替） | `normal` |
| `animation-fill-mode` | `animation-fill-mode: 模式` | 动画前后状态 | `none`（保持原样）<br>`forwards`（停在最后一帧）<br>`backwards`（使用第一帧状态直到延迟结束）<br>`both`（forwards+backwards） | `none` |
| `animation-play-state` | `animation-play-state: 状态` | 动画运行/暂停 | `running`（运行）<br>`paused`（暂停） | `running` |

**简写语法**：

```css
animation: name duration timing-function delay iteration-count direction fill-mode;

/* 示例 */
animation: slideUp 0.5s ease-out 0.2s infinite alternate forwards;
animation: fadeIn 0.3s ease-in-out 1 normal both;
```

> ⚠️ **易错点**：`animation-delay` 是第二个时间值，不是第一个。如果写 `0.5s 1s`，则是延迟0.5秒，播放1秒。

**animation-direction 详细效果**：

| 值 | 效果描述 | 播放示例（假设0%→100%是向上移动） |
|----|----------|-----------------------------------|
| `normal` | 始终从0%到100% | ↑ ↑ ↑ |
| `reverse` | 始终从100%到0% | ↓ ↓ ↓ |
| `alternate` | 奇数次正向，偶数次反向 | ↑ ↓ ↑ ↓ |
| `alternate-reverse` | 奇数次反向，偶数次正向 | ↓ ↑ ↓ ↑ |

**animation-fill-mode 详细效果**：

| 值 | 动画前状态 | 播放期间 | 动画结束后状态 |
|----|------------|----------|----------------|
| `none` | 元素原样式 | 关键帧控制 | 回到元素原样式 |
| `forwards` | 元素原样式 | 关键帧控制 | 停在最后一帧 |
| `backwards` | 使用第一帧状态 | 关键帧控制 | 回到元素原样式 |
| `both` | 使用第一帧状态 | 关键帧控制 | 停在最后一帧 |

**暂停/继续动画（结合JavaScript）**：

```css
.paused {
  animation-play-state: paused;
}
.running {
  animation-play-state: running;
}
```

#### 常用动画示例

```css
/* 呼吸动画 - 放大缩小循环 */
@keyframes breathe {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}
.breathe {
  animation: breathe 2s ease-in-out infinite;
}

/* 加载旋转动画 */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
.spinner {
  animation: spin 1s linear infinite;
}

/* 闪烁动画 */
@keyframes blink {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}
.blink {
  animation: blink 1s step-start infinite;
}
```

### 8.4 过渡 vs 变换 vs 动画对比

| 特性     | Transition           | Transform      | Animation      |
| -------- | -------------------- | -------------- | -------------- |
| 触发方式 | 状态变化（如 hover） | 立即生效       | 自动播放或触发 |
| 中间状态 | 自动计算             | 无（瞬间变化） | 需定义关键帧   |
| 循环播放 | ❌ 不能              | ❌ 不能        | ✅ 可以        |
| 适用场景 | 简单状态过渡         | 变形、位移     | 复杂动画       |
| 生活比喻 | 调光开关             | 换姿势         | 完整电影       |

> 💡 **实际开发中**：三者常配合使用。`transform` 负责变形，`transition` 负责平滑过渡，`animation` 负责复杂关键帧动画。

### 8.5 毛玻璃效果

```css
.glass {
  background: rgba(255, 255, 255, 0.2);
  -webkit-backdrop-filter: blur(10px); /* Safari 兼容 */
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
/* ⚠️ backdrop-filter 会创建新的层叠上下文，且旧浏览器不支持 */
```

> 🍎 **比喻理解**：就像磨砂玻璃——你看不清玻璃后面的东西，但能看到模糊的轮廓。`blur(10px)` 就是模糊程度。

### ✅ 本节回顾

- [x] 会写 `transition` 实现悬停效果
- [x] 会用 `transform` 实现位移、旋转、缩放
- [x] 会定义 `@keyframes` 并使用 `animation`
- [x] 知道什么时候用 transition，什么时候用 animation

### 📝 自测题

**1. `transition: all 0.3s ease` 中的 `all` 表示？**

- A. 所有元素
- B. 所有属性都会过渡
- C. 所有颜色
- D. 没有特殊含义

**2. `transform: translate(-50%, -50%)` 通常配合什么使用来实现居中？**

- A. `position: relative`
- B. `position: absolute; top: 50%; left: 50%;`
- C. `display: flex`
- D. `margin: 0 auto`

**3. `@keyframes` 中的 `100%` 可以用什么代替？**

- A. `end`
- B. `to`
- C. `last`
- D. `finish`

**4. 以下哪个属性可以实现循环播放动画？**

- A. `transition`
- B. `transform`
- C. `animation-iteration-count: infinite`
- D. `@keyframes`

**5. 性能最好的动画属性是？**

- A. `width` 和 `height`
- B. `top` 和 `left`
- C. `transform` 和 `opacity`
- D. `margin` 和 `padding`

<details>
<summary>点击查看答案</summary>

1. **B**（all 表示所有属性都会参与过渡）
2. **B**（absolute + top/left 50% + translate(-50%, -50%) 是经典居中方案）
3. **B**（`from` = `0%`，`to` = `100%`）
4. **C**（animation-iteration-count 控制循环次数）
5. **C**（transform 和 opacity 触发 GPU 加速）

</details>

### ✏️ 动手练习

1. 给按钮添加悬停过渡效果（颜色 + 上移）
2. 用 `transform` 实现一个元素在父容器中绝对居中
3. 用 `@keyframes` 实现一个加载动画（旋转的圆圈）

<details>
<summary>点击查看参考实现</summary>

**练习 1：按钮悬停过渡效果**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    .button {
      display: inline-block;
      padding: 12px 24px;
      background-color: #3498db;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 16px;
      cursor: pointer;
      /* 关键：transition 写在基础状态 */
      transition:
        background-color 0.3s ease,
        transform 0.3s ease,
        box-shadow 0.3s ease;
    }

    .button:hover {
      background-color: #2980b9; /* 颜色变深 */
      transform: translateY(-3px); /* 上移3px */
      box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4); /* 阴影加深 */
    }
  </style>
</head>
<body>
  <button class="button">悬停看我</button>
</body>
</html>
```

**练习 2：transform 绝对居中**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    .parent {
      position: relative;
      width: 400px;
      height: 300px;
      background-color: #f0f2f5;
      border: 1px solid #ddd;
    }

    .child {
      position: absolute;
      top: 50%;      /* 顶部定位到父容器中线 */
      left: 50%;     /* 左边定位到父容器中线 */
      /* 关键：往回拉自身宽高的50%，实现中心点居中 */
      transform: translate(-50%, -50%);
      width: 120px;
      height: 80px;
      background-color: #3498db;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
    }
  </style>
</head>
<body>
  <div class="parent">
    <div class="child">完美居中</div>
  </div>
</body>
</html>
```

**练习 3：加载旋转动画**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <style>
    /* 定义旋转动画 */
    @keyframes spin {
      from {
        transform: rotate(0deg);
      }
      to {
        transform: rotate(360deg);
      }
    }

    .loader {
      width: 40px;
      height: 40px;
      border: 4px solid #e0e0e0;
      border-top-color: #3498db; /* 只留顶部边框颜色 */
      border-radius: 50%;
      /* 应用动画 */
      animation: spin 0.8s linear infinite;
    }

    /* 加载动画容器 */
    .loading-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }

    .loading-text {
      font-family: Arial, sans-serif;
      color: #666;
      font-size: 14px;
    }

    /* 扩展：带渐变效果的旋转圈 */
    .loader-gradient {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      border: 4px solid transparent;
      border-top-color: #3498db;
      border-right-color: #e74c3c;
      animation: spin 1s linear infinite;
    }
  </style>
</head>
<body>
  <div class="loading-container">
    <div class="loader"></div>
    <span class="loading-text">加载中...</span>
  </div>

  <br><br>

  <div class="loading-container">
    <div class="loader-gradient"></div>
    <span class="loading-text">加载中...</span>
  </div>
</body>
</html>
```

</details>
