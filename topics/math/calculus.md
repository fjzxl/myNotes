---
title: 高等数学总览
tags:
  - math
  - kaoyan
  - calculus
aliases:
  - Calculus
created: 2026-10-10
updated: 2026-10-10
---
# 高等数学总览（考研数一）

> 本文是高等数学线的**导航页**：学习路线、章节清单、考纲权重。具体内容都在各章节笔记里，这里只做索引。
> 进度总控与每周排程见 [笔记编撰计划](../../projects/note-writing-plan.md)；全部数学索引见 [MOC - math](../../notes/MOC%20-%20math.md)。

## 1. 考纲定位（数一）

- 高等数学在数学一中约占 **56%**（线代、概率各约 22%）。
- 一元微积分（Ch1–Ch4）是绝对核心，既直接命题（极限、导数应用、积分计算），又是多元微积分（Ch5–Ch7）与级数（Ch8）的工具。
- 数一特有：空间解析几何（Ch5 的一部分）、三重积分、曲线曲面积分、傅里叶级数——这些恰好都在短稿区，性价比策略是"长文打地基、短稿过特有"。

## 2. 章节导航

> 命名与结构遵循 [笔记编撰计划](../../projects/note-writing-plan.md)：`topics/math/calculus/` 下按编号组织；Ch1–Ch4 长文标准，Ch5 起短稿。✅ = 已完成，⏳ = 待写。

### Ch1 函数、极限、连续

| 专题 | 笔记 | 状态 |
|------|------|------|
| 01 函数概念与性质 | [functions-and-bounds](functions-and-bounds.md)（含确界理论，位于 `topics/math/` 根目录） | ✅ |
| 02–03 数列与函数极限 | [02-03-sequence-function-limits](calculus/02-03-sequence-function-limits.md) | ✅ |
| 04–05 无穷小/无穷大、连续 | `04-05-infinitesimal-continuity`（等价替换、间断点、闭区间连续函数性质） | ⏳ |
| 06 极限计算方法综合 | `06-limit-techniques`（题型汇总） | ⏳ |

### Ch2 一元函数微分学

`07-derivative` 导数概念与求导法则 · `08-differential-higher-order` 微分与高阶导数 · `09-mean-value-theorems` 中值定理 · `10-taylor-formula` 泰勒公式 · `11-lhopital` 洛必达 · `12-monotonicity-extrema` 单调性与极值 · `13-concavity-asymptote` 凹凸性与作图 · `14-derivative-applications` 综合应用（⏳ 全部待写）

### Ch3 一元函数积分学

`15-indefinite-integral` 不定积分 · `16-substitution` 换元法 · `17-parts-rational` 分部与有理函数 · `18-definite-integral` 定积分与 N-L 公式 · `19-improper-integral` 反常积分 · `20-integral-applications` 定积分应用（⏳ 全部待写）

### Ch4 常微分方程

`21-first-order-ode` 一阶方程 · `22-reducible-ode` 可降阶与解的结构 · `23-second-order-ode` 二阶常系数线性 · `24-ode-applications` 综合应用（⏳ 全部待写）

### Ch5–Ch8 多元与级数（W23 起短稿）

- Ch5 向量代数与空间解析几何：`25-vectors` · `26-planes-and-lines` · `27-surfaces-curves`
- Ch6 多元函数微分学：`28-multivariable-limit` · `29-partial-derivative` · `30-chain-and-implicit` · `31-directional-derivative` · `32-multivariable-extrema`
- Ch7 多元函数积分学：`33-double-integral` · `34-triple-integral` · `35/36-line-integral` · `37/38-surface-integral`
- Ch8 无穷级数：`39-40-series-concepts-positive-tests` · `41-alternating-series` · `42-power-series` · `43-taylor-series` · `44-fourier-series`

### 专题与真题（考后 W35–W38）

`45-mvt-proof-special` 中值定理证明题 · `46-integral-inequality` 积分不等式（衔接 [inequalities](inequalities.md)）· `47-series-summation` 级数求和 · `48-synthetic-problems` 综合 · 真题复盘①②

## 3. 学习路线

```
界与函数(01) → 极限(02-03) → 无穷小与连续(04-05) → 极限计算(06)
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
- [functions-and-bounds](functions-and-bounds.md) —— 确界与函数（前置基础）
- [MOC - math](../../notes/MOC%20-%20math.md) —— 数学总索引（含线代、概率路线）
- [笔记编撰计划](../../projects/note-writing-plan.md) —— 39 周排程
