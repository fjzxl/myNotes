---
title: "介值定理与零点定理（Intermediate Value Theorem）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-18
---

# 介值定理与零点定理（Intermediate Value Theorem）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [无穷小、无穷大与连续](../topics/math/calculus/04-05-infinitesimal-continuity.md)。

## 一句话定义

> 闭区间上的连续曲线不抬笔，因此**中途每个高度都必须经过**：$f(a)F(b)<0$ 时高度 $0$ 必被经过（零点定理）；介于 $f(a)$、$f(b)$ 之间（更一般地，介于最小值 $m$ 与最大值 $M$ 之间）的任何高度都被经过（介值定理）。

## 详细解释

> **零点定理**：$f\in C[a,b]$，$f(a)\cdot f(b)<0$ $\Rightarrow$ $\exists\,\xi\in(a,b)$，$f(\xi)=0$。
> **介值定理**：$f\in C[a,b]$，则对介于 $f(a)$、$f(b)$ 之间的任一 $C$，$\exists\,\xi$ 使 $f(\xi)=C$。
> **值域刻画**（介值 + 最值定理联用）：$f\in C[a,b]\Rightarrow f([a,b])=[m,M]$。

关系链：零点定理是根基，介值定理由它推出（令 $F(x)=f(x)-C$，则 $F(a)F(b)<0$）；值域刻画再把取值范围放宽到整个 $[m,M]$（不限于 $f(a)$、$f(b)$ 之间）。

**存在性证明四步**：① 结论移项成 $F(\xi)=0$ 构造辅助函数；② 找两点使 $F$ 异号（端点、$0$、构造的特殊点）；③ 零点定理收尾；④ 端点本身为零时单独讨论（如 $F(a+b)=0$ 恰好成立的情形）。

两个条件缺一不可的反例：$\dfrac1x\in C(0,1)$（开区间）取不到最值也可无界；在 $[0,1]$ 上于 $0$ 处间断的版本可跳过所有中间值。

## 例子

- 方程 $x=a\sin x+b$（$a,b>0$）有正根且不超过 $a+b$：$F(x)=x-a\sin x-b$，$F(0)=-b<0$，$F(a+b)=a\,[1-\sin(a+b)]\ge0$，端点为零单独说，否则零点定理。
- $f\in C[0,1]$，$f(0)=f(1)$，则存在 $\xi\in[0,\tfrac12]$ 使 $f(\xi)=f(\xi+\tfrac12)$：令 $F(x)=f(x)-f(x+\tfrac12)$，则 $F(0)=-F(\tfrac12)$，乘积 $-F(0)^2\le0$，异号或端点为零。
- 平均值版：$f\in C[a,b]$，$c,d\in[a,b]$，则 $\dfrac{f(c)+f(d)}2\in[m,M]$ 必被取到——凸组合推广一字不改。

## 与其他概念的关系

- 上游（前驱）：最值定理（有界性与最大最小值，闭区间 + 连续）；确界存在定理（最值定理是"确界被取到"的条件版）
- 下游（应用）：第二章罗尔定理 / 拉格朗日中值定理（同样是构造 $F$ 找 $\xi$ 的套路，从"高度穿越"升级为"导数穿越"）；定积分的介值性
- 对比：[单调有界定理](monotone-bounded-convergence.md)管数列**收敛性**（极限存在），本定理管闭区间上的**取值到达**（某高度被取到），一个在无穷远处、一个在有限区间内

## 引用来源

- 来源：[无穷小、无穷大与连续](../topics/math/calculus/04-05-infinitesimal-continuity.md)（本库高数 Ch1 长文）
- 教材：《高等数学》（同济版）第一章 闭区间上连续函数的性质

## 相关永久笔记

- [单调有界定理](monotone-bounded-convergence.md)
- [夹逼准则](squeeze-theorem.md)
- [间断点分类](discontinuity-classification.md)
- [闭区间套定理](nested-interval-theorem.md)（零点定理二分法证明的工具）
- [可导与连续](differentiability-vs-continuity.md)（连续性的"取值"红利与可导性的"变化率"红利对照）
