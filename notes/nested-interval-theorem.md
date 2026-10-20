---
title: "闭区间套定理（Nested Interval Theorem）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-19
---

# 闭区间套定理（Nested Interval Theorem）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [界与函数](../topics/math/calculus/functions-and-bounds.md)。

## 一句话定义

**嵌套且长度趋于零的闭区间列，公共点恰好存在一个**——所有区间"收缩"到同一个实数 $\xi$ 上，且 $\xi$ 被每个区间实打实地包含（端点不丢）。

## 详细解释

> 条件：$[a_{n+1},b_{n+1}]\subseteq[a_n,b_n]$ 且 $b_n-a_n\to0$。结论：$\bigcap_{n=1}^{\infty}[a_n,b_n]=\{\xi\}$（唯一），且 $a_n\to\xi,\ b_n\to\xi$。

- 三个关键词各司其职：**嵌套**保证区间不"分家"；**长度趋于零**保证只收缩到一个点（否则如 $[0,1+\tfrac1n]$ 交出整段 $[0,1]$）；**闭**保证极限点被扣住——开区间套 $(0,\tfrac1n)$ 嵌套且长度趋于零，交集却是**空**的（$0$ 是极限位置但不属于任何开区间）。
- 证明链条恰好走完完备性家族的推导链：嵌套 $\Rightarrow$ $\{a_n\}$ 单调增有上界 $\Rightarrow$（单调有界定理）收敛于 $\xi=\sup\{a_n\}$ $\Rightarrow$ 每个 $b_n$ 都是 $\{a_k\}$ 的上界，故 $a_n\le\xi\le b_n$；唯一性由长度趋于零反证。
- 本质用途：**存在性证明的构造机器**。标准玩法是二分法——每次保留"仍有所需性质"的那一半区间，得到区间套，公共点即"存在"的那个点。

## 例子

- 二分逼近上确界：右端恒为上界、左端上方恒有集合 $E$ 的点地二分，区间套的公共点同时满足"是上界"与"$\varepsilon$-逼近"两条特征，即 $\sup E$（这也是"区间套定理 $\Rightarrow$ 确界存在定理"的证明）。
- 零点定理的标准证明：$f(a)f(b)<0$ 时每次保留端点异号的那一半，公共点即零点 $\xi$（见 [介值定理与零点定理](intermediate-value-theorem.md)）。
- $\sqrt2$ 的不足/过剩近似值 $a_n,b_n$ 构成区间套；在有理数系里这个套的"公共点"不存在——完备性失效的直观展示。

## 与其他概念的关系

- 上游（前驱）：[单调有界定理](monotone-bounded-convergence.md)（本定理证明的必经之路）；确界存在定理（与之等价，同属实数完备性家族）
- 下游（应用）：[介值定理与零点定理](intermediate-value-theorem.md)（二分法证明）；聚点定理、一致连续性定理（Cantor）的证明工具
- 对比：单调有界定理由"一列数"的走势断言极限存在，本定理由"一列区间的收缩"断言公共点存在——前者适合递推数列，后者适合存在性构造

## 引用来源

- 来源：[界与函数](../topics/math/calculus/functions-and-bounds.md)（本库高数 Ch1 长文，§1.4）
- 教材：《数学分析》（华东师大版）第一章 实数完备性；《高等数学》（同济版）第一章相关内容

## 相关永久笔记

- [单调有界定理](monotone-bounded-convergence.md)
- [介值定理与零点定理](intermediate-value-theorem.md)
- [夹逼准则](squeeze-theorem.md)
- [数列与子列极限](subsequence-limits.md)（致密性定理可由区间套二分法证）
