---
title: "n 项和极限（Limits of Sums）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-20
---

# n 项和极限（Limits of Sums）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [极限计算方法综合](../topics/math/calculus/06-limit-techniques.md)。

## 一句话定义

项数随 $n$ 增长的和式 $S_n=\sum_{k=1}^n a_k(n)$ **不能逐项取极限**（四则法则只对固定有限项成立）；三法解决：先求和、夹逼、定积分定义——按「能否写出闭式 / 能否整体放缩 / 是否呈 $f\!\left(\frac kn\right)\cdot\frac1n$ 形状」选择。

## 详细解释

| 信号 | 方法 | 例 |
|------|------|---|
| 等比、裂项、求和公式可用 | 先求闭式，再取极限 | $\sum\dfrac1{k(k+1)}=1-\dfrac1{n+1}\to1$ |
| 各项可放缩出同限上下界 | 夹逼 | $\sum_{k=1}^n\dfrac k{n^2+k}\to\dfrac12$ |
| 提出因子 $\dfrac1n$ 后剩 $f\!\left(\dfrac kn\right)$ | 定积分定义 | $\dfrac1n\sum\sin\dfrac{k\pi}n\to\int_0^1\sin\pi x\,dx=\dfrac2\pi$ |

- **为什么逐项非法**：「每一项的极限」加起来根本不是同一个和——项数在变，$n$ 项的极限加和与 $\infty$ 没有四则法则可依。逐项求极限的合法版本正是黎曼和收敛于积分。
- **夹逼与积分的分界**：夹逼只要上下界同极限（精度粗，适合各项难精确的情形）；积分定义要求每项精确落在格点 $f\!\left(\frac kn\right)\cdot\frac1n$ 上。判据：**提出 $\dfrac1n$ 看剩余部分**。
- 根式版变体：$\sqrt[n]{a_1^n+\cdots+a_m^n}\to\max a_i$（夹逼：夹在 $\max a_i$ 与 $\max a_i\cdot m^{1/n}$ 之间）。

## 例子

- 夹逼：$S_n=\sum_{k=1}^n\dfrac k{n^2+k}$，由 $\dfrac{\sum k}{n^2+n}\le S_n\le\dfrac{\sum k}{n^2+1}$（下界恒为 $\dfrac12$，上界趋于 $\dfrac12$）得 $S_n\to\dfrac12$。
- 积分定义：$\lim\limits_{n\to\infty}\dfrac1n\sum_{k=1}^n\sin\dfrac{k\pi}n=\int_0^1\sin(\pi x)\,dx=\dfrac2\pi$（数值核对：$n=2000$ 时和 $\approx0.63662=\dfrac2\pi$）。

## 与其他概念的关系

- 上游（前驱）：[夹逼准则](squeeze-theorem.md)（三法之一的原理）
- 下游（应用）：定积分定义（Ch3 黎曼和——本卡的严格化）；与级数（Ch8）的分界：级数是**无穷多项**的收敛问题，本卡是 $n$ 项和随 $n$ 的趋势，勿混
- 对比：[单调有界定理](monotone-bounded-convergence.md) 管递推数列，本卡管和式数列，两者是数列极限题的两大入口

## 引用来源

- 来源：[极限计算方法综合](../topics/math/calculus/06-limit-techniques.md)（本库高数 Ch1 长文）
- 教材：《高等数学》（同济版）第一章 极限存在准则、第五章 定积分定义

## 相关永久笔记

- [夹逼准则](squeeze-theorem.md)
- [七种未定式](indeterminate-forms.md)
