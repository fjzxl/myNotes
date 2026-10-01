---
title: CSS 入门指南
tags:
  - programming
  - css
created: 2026-09-10
updated: 2026-10-01
---

# CSS 入门指南

> **CSS（层叠样式表）** 用于控制网页的外观和布局。它描述了 HTML 元素应该如何被渲染显示，包括颜色、字体、间距、边框、背景、动画等方方面面。
>
> 学习 CSS 的核心逻辑：**先让元素可见 → 再让元素好看 → 最后让元素排好队**。

---

## 学习路线图

```
第一阶段：CSS 是什么、怎么引入页面（建立整体认知）
    ↓
第二阶段：改颜色、改字体、改间距（最直观，有即时反馈）
    ↓
第三阶段：理解盒模型与显示方式（明白元素占多少空间）
    ↓
第四阶段：精准选中元素（选择器）
    ↓
第五阶段：背景与装饰（让页面更丰富）
    ↓
第六阶段：布局系统（让元素各就各位）
    ↓
第七阶段：响应式设计（适配手机、平板、电脑）
    ↓
第八阶段：动画与交互（让页面动起来）
    ↓
第九阶段：现代 CSS 特性（变量、函数、新属性）
    ↓
第十阶段：工程化与最佳实践（走向专业）
```

### 📖 阅读指南

| 读者类型       | 阅读建议                                                                   |
| -------------- | -------------------------------------------------------------------------- |
| **完全新手**   | 按顺序阅读，每个阶段先读**比喻理解**，再做**自测题**，最后完成**动手练习** |
| **有一定基础** | 跳过熟悉内容，重点看 🔴 **重难点** 和 ⚠️ **易错点**                        |
| **速查参考**   | 善用目录和 `Ctrl+F` 搜索关键词                                             |

**文档符号说明**：

- 🍎 **生活比喻**：用日常事物类比 CSS 概念
- 🔴 **重难点**：必须掌握的核心概念
- ⚠️ **易错点**：初学者常犯的错误
- 💡 **记忆口诀**：帮助记忆的顺口溜
- 📝 **自测题**：检验理解程度的选择题/判断题
- ✏️ **动手练习**：可执行的代码练习

---

## 📑 目录与学习建议

| 阶段 | 内容 | 难度 | 预计时间 |
|:---:|:---|:---:|:---:|
| 一 | 初识 CSS —— 先让样式生效 | ⭐ | 30 分钟 |
| 二 | 给文字"化妆" —— 最直观的改变 | ⭐ | 45 分钟 |
| 三 | 盒模型与显示方式 —— 理解元素的空间占用 | ⭐⭐ | 1.5 小时 |
| 四 | 选择器 —— 精准选中要修改的元素 | ⭐⭐ | 1 小时 |
| 五 | 背景与装饰 —— 让页面更丰富 | ⭐⭐ | 45 分钟 |
| 六 | 布局系统 —— 让元素各就各位 | ⭐⭐⭐ | 2 小时 |
| 七 | 响应式设计 —— 适配不同屏幕 | ⭐⭐⭐ | 1.5 小时 |
| 八 | 动画与交互 —— 让页面动起来 | ⭐⭐⭐ | 1.5 小时 |
| 九 | 现代 CSS 进阶特性 | ⭐⭐ | 1 小时 |
| 十 | CSS 架构与工程化 | ⭐⭐⭐ | 1 小时 |

> 💡 **给初学者的建议**：按顺序逐个阶段学习，不要跳过基础直接看布局。每个阶段务必完成**自测题**，有不确定的及时回到正文复习。

---

## 核心概念速查

| 概念             | 一句话理解                                                        | 生活比喻                                                                      |
| ---------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **选择器**       | 告诉浏览器"我要改哪个元素"                                        | 就像老师点名："第三排穿红衣服的同学"                                          |
| **属性**         | 告诉浏览器"我要改它的什么"                                        | 就像说："把头发染成蓝色"                                                      |
| **值**           | 告诉浏览器"改成什么样"                                            | 就像说："染成深蓝色 #00008B"                                                  |
| **盒模型**       | 每个元素都是一个盒子，由 content + padding + border + margin 组成 | 就像快递盒：商品 + 气泡膜 + 纸箱 + 两个箱子间的距离                           |
| **`border-box`** | `width` 包含 content + padding + border，设置多少就是多少         | 就像说"整个包裹宽 10cm"——就是 10cm，内部自己压缩                             |
| **`content-box`**| `width` 只包含 content，实际占地需要心算                          | 就像说"杯子宽 10cm"——实际还要加上包装                                       |
| **选择器优先级** | 多个样式冲突时，优先级高的生效                                    | 就像游戏规则：校长发话 > 班主任 > 班干部 > 普通学生（先比官职，同级再比人数） |
| **`block`**      | 独占一行，可设宽高                                                | 一人一张桌子                                                                  |
| **`inline`**     | 共占一行，不可设宽高                                              | 几人挤一张长桌                                                                |
| **`inline-block`**| 共占一行，可设宽高                                               | 长桌上每人有固定座位                                                          |
| **Flexbox**      | 一维布局，沿主轴排列                                              | 就像排队：可以横着排，也可以竖着排                                            |
| **Grid**         | 二维布局，同时控制行和列                                          | 就像棋盘：有横有竖，形成格子                                                  |
| **Position**     | 定位方式                                                          | 就像人站在哪里：原地站(static)、站队时踮脚(relative)、站到操场角落(absolute)  |
| **Z-Index**      | 层叠顺序                                                          | 就像一叠纸，数字大的在上面                                                    |

---

## 📑 章节导航

全文按学习阶段拆分为 10 篇独立笔记，建议按顺序阅读：

1. [[topics/programming/Web/css/stage-01-getting-started|第一阶段：初识 CSS —— 先让样式生效]]
2. [[topics/programming/Web/css/stage-02-text-styling|第二阶段：给文字"化妆" —— 最直观的改变]]
3. [[topics/programming/Web/css/stage-03-box-model|第三阶段：盒模型与显示模式 —— 理解元素的空间占用]]
4. [[topics/programming/Web/css/stage-04-selectors|第四阶段：选择器 —— 精准选中要修改的元素]]
5. [[topics/programming/Web/css/stage-05-backgrounds|第五阶段：背景与装饰 —— 让页面更丰富]]
6. [[topics/programming/Web/css/stage-06-layout|第六阶段：布局系统 —— 让元素各就各位]]
7. [[topics/programming/Web/css/stage-07-responsive-design|第七阶段：响应式设计 —— 适配不同屏幕]]
8. [[topics/programming/Web/css/stage-08-animation|第八阶段：动画与交互 —— 让页面动起来]]
9. [[topics/programming/Web/css/stage-09-modern-css|第九阶段：现代 CSS 进阶特性]]
10. [[topics/programming/Web/css/stage-10-architecture|第十阶段：CSS 架构与工程化]]

---

## 附录：CSS 属性选择决策图

```
我要修改...什么？
│
├─ 颜色 ───────────→ background-color / color / border-color
│
├─ 尺寸 ───────────→ width / height / font-size
│
├─ 间距 ───────────→ 内？→ padding / 外？→ margin
│
├─ 边框 ───────────→ border / border-radius
│
├─ 位置 ───────────→ 一维？→ Flexbox / 二维？→ Grid / 堆叠？→ position + z-index
│
├─ 背景 ───────────→ background / background-image
│
├─ 阴影 ───────────→ box-shadow / text-shadow
│
└─ 动画 ───────────→ 简单？→ transition / 复杂？→ animation + @keyframes
```

---

## 附录：学习资源与建议

### 推荐资源

| 资源         | 链接                                                                                         | 用途                 |
| ------------ | -------------------------------------------------------------------------------------------- | -------------------- |
| MDN          | [developer.mozilla.org/zh-CN/docs/Web/CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) | 最权威的参考文档     |
| Can I Use    | [caniuse.com](https://caniuse.com)                                                           | 查浏览器兼容性       |
| CSS Triggers | [csstriggers.com](https://csstriggers.com)                                                   | 查属性触发的渲染阶段 |
| cubic-bezier | [cubic-bezier.com](https://cubic-bezier.com)                                                 | 贝塞尔曲线生成器     |
| Flexbox 游戏 | [flexboxfroggy.com](https://flexboxfroggy.com)                                               | 通过游戏学习 Flexbox |
| Grid 花园    | [cssgridgarden.com](https://cssgridgarden.com)                                               | 通过游戏学习 Grid    |

### 学习建议

1. **先学基础**：选择器、盒模型、常用属性 → 会改颜色、字体、间距
2. **掌握布局**：先理解文档流和定位 → 再学 Flexbox → 最后 Grid
3. **多动手**：做一个完整的响应式页面（从手机到桌面）
4. **善用 DevTools**：实时调试、理解渲染机制、查看计算样式
5. **阅读源码**：看优秀开源项目（如 shadcn/ui）的 CSS 写法
6. **刻意练习**：每天实现一个小组件（按钮、卡片、导航栏、表单）

### 学习检查清单

```
□ 能独立写出一个静态网页（导航 + 内容 + 页脚）
□ 能用 Flexbox 实现常见布局（居中、等分、两端对齐）
□ 能用 Grid 实现响应式网格
□ 能用媒体查询适配手机、平板、桌面
□ 能写出平滑的悬停过渡效果
□ 能使用 CSS 变量管理主题色
□ 能解释清楚盒模型和选择器优先级
```

> 完成以上清单，代表你已经掌握了 CSS 的核心技能，可以进入现代 CSS 框架（Tailwind、Styled-Components等）的学习了！

---

## 终极自测综合题

### 选择题

**1. 盒模型中，背景色会延伸到哪个区域？**

- A. margin
- B. border
- C. padding
- D. 以上全部

**2. 一个元素设置 `width: 200px; padding: 20px; border: 2px solid; margin: 10px; box-sizing: border-box`，它的总宽度（包含 margin）是？**

- A. 200px
- B. 220px
- C. 244px
- D. 264px

**3. `#header .nav a` 和 `.nav a` 同时作用在一个元素上，哪个优先级更高？**

- A. `.nav a`
- B. `#header .nav a`
- C. 一样高
- D. 看谁先写

**4. 以下哪个不是 Flexbox 的属性？**

- A. `justify-content`
- B. `align-items`
- C. `grid-template-columns`
- D. `flex-wrap`

**5. 移动优先的响应式设计，媒体查询应该用？**

- A. `max-width`
- B. `min-width`
- C. `max-height`
- D. `orientation`

**6. `transition: all 0.3s ease` 中，`ease` 表示？**

- A. 匀速
- B. 慢-快-慢
- C. 慢开始
- D. 慢结束

**7. BEM 命名中，`.card--featured` 的 `--featured` 是？**

- A. Block
- B. Element
- C. Modifier
- D. 都不是

### 判断题

**8. `display: none` 和 `visibility: hidden` 效果完全相同。**

**9. 行内元素（inline）可以设置 width 和 height。**

**10. `position: absolute` 的元素会脱离正常文档流。**

**11. `flex: 1` 是 `flex-grow: 1; flex-shrink: 1; flex-basis: 0%` 的简写。**

**12. CSS 变量可以在 JavaScript 中动态修改。**

<details>
<summary>点击查看答案</summary>

**选择题：**

1. **B**（默认 `background-clip: border-box` 下，背景色延伸到 border 区域，包含 content + padding + border）
2. **B**（border-box 下 width 200px 包含 content+padding+border，再加 margin 左右各 10px = 220px）
3. **B**（`#header .nav a` = (0,1,1,1)，`.nav a` = (0,0,1,1)，ID选择器胜出）
4. **C**（grid-template-columns 是 Grid 的属性）
5. **B**（移动优先用 min-width）
6. **B**（ease 是慢-快-慢）
7. **C**（-- 是 Modifier）

**判断题：** 8. **错误**（display:none 不占空间，visibility:hidden 占位）9. **错误**（inline 不能设置宽高，inline-block 可以）10. **正确**（absolute 脱离文档流）11. **正确**（flex: 1 是简写）12. **正确**（JS 可以 setProperty 修改 CSS 变量）

</details>

---

> 本文档持续更新中。如有疑问或建议，欢迎交流探讨。
