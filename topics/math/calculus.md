---
title: 高等数学总览
tags:
  - math
  - kaoyan
  - math/calculus
---
# 高等数学总览（考研数一）

> 本文是高等数学线的**导航页**：学习路线、章节清单、考纲权重。具体内容都在各章节笔记里，这里只做索引。
> 进度总控与每周排程见 [笔记编撰计划](../../projects/note-writing-plan.md)；全部数学索引见 [MOC - math](../../notes/MOC%20-%20math.md)。

## 1. 考纲定位（数一）

- 高等数学在数学一中约占 **56%**（线代、概率各约 22%）。
- 一元微积分（Ch1–Ch4）是绝对核心，既直接命题（极限、导数应用、积分计算），又是多元微积分（Ch5–Ch7）与级数（Ch8）的工具。
- 数一特有：空间解析几何（Ch5 的一部分）、三重积分、曲线曲面积分、傅里叶级数——这些恰好都在短稿区，性价比策略是"长文打地基、短稿过特有"。

## 2. 章节导航

> 命名与结构遵循 [笔记编撰计划](../../projects/note-writing-plan.md)：`topics/math/calculus/` 下按编号组织；Ch1–Ch3 与 Ch4 的 21–23 长文标准，`24-ode-applications`（W23 落点）起短稿。✅ = 已完成，⏳ = 待写。

### Ch1 函数、极限、连续

| 专题 | 笔记 | 状态 |
|------|------|------|
| 01 函数概念与性质 | [functions-and-bounds](calculus/functions-and-bounds.md)（含确界理论与闭区间套定理） | ✅ |
| 02–03 数列与函数极限 | [02-03-sequence-function-limits](calculus/02-03-sequence-function-limits.md) | ✅ |
| 04–05 无穷小/无穷大、连续 | [04-05-infinitesimal-continuity](calculus/04-05-infinitesimal-continuity.md)（等价替换、间断点、闭区间连续函数性质） | ✅ |
| 06 极限计算方法综合 | [06-limit-techniques](calculus/06-limit-techniques.md)（七种未定式决策 · 泰勒与洛必达预置 · 数列极限三法） | ✅ |
| Ch1 复习 | [ch1-review](calculus/ch1-review.md)（框架图 · 反例库 · A/B 卷自测） | ✅ |

### Ch2 一元函数微分学

| 专题 | 笔记 | 状态 |
|------|------|------|
| 07 导数概念与求导法则 | [07-derivative](calculus/07-derivative.md)（定义与左右导数 · 可导与连续 · 四则/反函数/链式 · 基本导数表） | ✅ |
| 08 微分与高阶导数 | `08-differential-higher-order`（微分、隐函数/参数方程/对数求导、高阶导数） | ⏳ |
| 09 中值定理 | `09-mean-value-theorems`（罗尔 / 拉格朗日 / 柯西） | ⏳ |
| 10 泰勒公式 | `10-taylor-formula`（泰勒公式与常用展开） | ⏳ |
| 11 洛必达 | `11-lhopital`（洛必达法则与未定式） | ⏳ |
| 12 单调性与极值 | `12-monotonicity-extrema`（单调性、极值与最值） | ⏳ |
| 13 凹凸性与作图 | `13-concavity-asymptote`（凹凸性、拐点、渐近线与函数作图） | ⏳ |
| 14 导数综合应用 | `14-derivative-applications`（不等式证明、方程根讨论） | ⏳ |

### Ch3 一元函数积分学

| 专题 | 笔记 | 状态 |
|------|------|------|
| 15 不定积分 | `15-indefinite-integral`（概念与基本积分表） | ⏳ |
| 16 换元法 | `16-substitution`（第一 / 第二类换元） | ⏳ |
| 17 分部与有理函数 | `17-parts-rational`（分部积分与有理函数积分） | ⏳ |
| 18 定积分 | `18-definite-integral`（定积分、变限积分与 N-L 公式） | ⏳ |
| 19 反常积分 | `19-improper-integral`（判敛与计算） | ⏳ |
| 20 定积分应用 | `20-integral-applications`（面积 / 旋转体 / 弧长 / 物理） | ⏳ |

### Ch4 常微分方程

| 专题 | 笔记 | 状态 |
|------|------|------|
| 21 一阶方程 | `21-first-order-ode`（可分离 / 齐次 / 一阶线性 / 伯努利） | ⏳ |
| 22 可降阶与解的结构 | `22-reducible-ode`（可降阶方程、解的结构、欧拉方程） | ⏳ |
| 23 二阶常系数线性 | `23-second-order-ode`（齐次 + 非齐次） | ⏳ |
| 24 微分方程综合 | `24-ode-applications`（综合与应用） | ⏳ |

### Ch5–Ch8 多元与级数（W23 起短稿）

| 章 | 专题 | 笔记 | 状态 |
|----|------|------|------|
| Ch5 向量代数与空间解析几何 | 25 向量代数 | `25-vectors`（数量积 / 向量积 / 混合积） | ⏳ |
| Ch5 | 26 平面与直线 | `26-planes-and-lines`（方程及位置关系） | ⏳ |
| Ch5 | 27 曲面与空间曲线 | `27-surfaces-curves`（旋转面 / 柱面 / 二次曲面） | ⏳ |
| Ch6 多元函数微分学 | 28 多元极限与连续 | `28-multivariable-limit` | ⏳ |
| Ch6 | 29 偏导数与全微分 | `29-partial-derivative` | ⏳ |
| Ch6 | 30 复合与隐函数求导 | `30-chain-and-implicit` | ⏳ |
| Ch6 | 31 方向导数与梯度 | `31-directional-derivative`（含切平面 / 法线） | ⏳ |
| Ch6 | 32 多元极值 | `32-multivariable-extrema`（条件极值、拉格朗日乘数法） | ⏳ |
| Ch7 多元函数积分学 | 33 二重积分 | `33-double-integral`（直角 / 极坐标、交换次序） | ⏳ |
| Ch7 | 34 三重积分 | `34-triple-integral`（投影 / 截面 / 球面坐标） | ⏳ |
| Ch7 | 35 第一类曲线积分 | `35-line-integral-1` | ⏳ |
| Ch7 | 36 第二类曲线积分 | `36-line-integral-2`（格林公式） | ⏳ |
| Ch7 | 37 第一类曲面积分 | `37-surface-integral-1` | ⏳ |
| Ch7 | 38 第二类曲面积分 | `38-surface-integral-2`（高斯与斯托克斯公式） | ⏳ |
| Ch8 无穷级数 | 39–40 级数概念与正项判敛 | `39-40-series-concepts-positive-tests` | ⏳ |
| Ch8 | 41 交错级数 | `41-alternating-series`（绝对 / 条件收敛） | ⏳ |
| Ch8 | 42 幂级数 | `42-power-series`（幂级数与和函数） | ⏳ |
| Ch8 | 43 泰勒级数 | `43-taylor-series`（函数展开为幂级数） | ⏳ |
| Ch8 | 44 傅里叶级数 | `44-fourier-series`（数一） | ⏳ |

### 专题与真题（考后 W35–W38）

| 专题 | 笔记 | 状态 |
|------|------|------|
| 45 中值定理证明题 | `45-mvt-proof-special` | ⏳ |
| 46 积分不等式 | `46-integral-inequality`（衔接 [inequalities](inequalities.md)） | ⏳ |
| 47 级数求和 | `47-series-summation`（求和与敛散综合） | ⏳ |
| 48 综合 | `48-synthetic-problems`（多元微积分综合，或按错题情况改为机动） | ⏳ |
| 真题复盘①② | 2010–2013 年卷中选两套，用 [练习记录模板](../../templates/practice-log.md) 记录限时表现与错题复测 | ⏳ |

## 3. 学习路线

```
界与函数(01) → 极限(02-03) → 无穷小与连续(04-05) → 极限计算(06) → Ch1复习
      ↓ Ch1 打牢后
导数(07-08) → 中值定理(09-10) → 洛必达(11) → 导数应用(12-14)
      ↓
积分计算(15-19) → 积分应用(20) → 微分方程(21-24)
      ↓（2027-03 起转短稿）
空间几何(25-27) → 多元微分(28-32) → 多元积分(33-38) → 级数(39-44)
      ↓
专题(45-48) + 真题复盘 → 线代 / 概率（另一条线）
```

关键依赖：**Ch1 的极限定义是全卷的地基**——连续、导数、定积分、级数、反常积分全部用极限定义；Ch2–Ch3 互相成就（变限积分求导、分部积分）；不等式工具（[inequalities](inequalities.md)）贯穿放缩题。

## 4. 章节笔记统一结构

每篇按 [计划](../../projects/note-writing-plan.md) 约定的骨架：**考纲定位 → 概念与定义 → 定理及证明思路 → 典型例题（自行核对）→ 易错点与做题套路 → 前后互链 + 自测清单**。短稿篇目同骨架、压缩证明与应用。

## 5. 相关笔记

- [inequalities](inequalities.md) —— 不等式专题（放缩工具箱）
- [functions-and-bounds](calculus/functions-and-bounds.md) —— 确界与函数（前置基础）
- [ch1-review](calculus/ch1-review.md) —— Ch1 复习页（框架 · 反例库 · 自测）
- [MOC - math](../../notes/MOC%20-%20math.md) —— 数学总索引（含线代、概率路线）
- [笔记编撰计划](../../projects/note-writing-plan.md) —— 39 周排程
