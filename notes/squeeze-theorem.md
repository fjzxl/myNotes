---
title: "夹逼准则（Squeeze Theorem）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-12
---

# 夹逼准则（Squeeze Theorem）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [数列与函数极限](../topics/math/calculus/02-03-sequence-function-limits.md)。

## 一句话定义

若 $f(x)$（或 $b_n$）被两个极限相同的量上下夹住，则它也被迫趋于同一个极限——**两端定中间**。

## 详细解释

数列版：若从某项起恒有 $a_n \le b_n \le c_n$，且 $\lim\limits_{n\to\infty} a_n = \lim\limits_{n\to\infty} c_n = A$，则 $\lim\limits_{n\to\infty} b_n = A$。

函数版：若在 $x_0$ 的某去心邻域（或 $|x|>X$）内 $g(x) \le f(x) \le h(x)$，且 $\lim g(x) = \lim h(x) = A$，则 $\lim f(x) = A$。

使用要点：
- **什么时候用**：极限式整体难算，但容易"放缩"出上下界——典型是 $n$ 项求和、含阶乘 / 指数增长的结构。
- **两端极限必须相等**：放缩过度（两端极限不同）准则失效，要调整放缩粒度。
- 夹逼的本质是把"算不出"换成"估得住"。

## 例子

- 经典求和放缩：$\lim\limits_{n\to\infty}\left(\dfrac{n}{n^2+1}+\dfrac{n}{n^2+2}+\cdots+\dfrac{n}{n^2+n}\right)=1$——分母各异算不了，放缩统一成 $\dfrac{n^2}{n^2+n}\le S\le \dfrac{n^2}{n^2+1}$，两端同趋于 $1$。
- $\lim\limits_{n\to\infty}\left(1+2^n+3^n\right)^{\frac1n} = 3$：由 $1+2^n+3^n\le 3\cdot 3^n$ 得 $3 \le (\cdots)^{1/n} \le 3\cdot 3^{1/n}$，而 $3^{1/n}\to 1$（$n=1$ 时也成立）。

## 与其他概念的关系

- 上游（前驱）：[单调有界定理](monotone-bounded-convergence.md)、极限的 $\varepsilon$-$N$ 定义（放缩后仍要回归定义验证）
- 下游（应用）：两个重要极限之一的 $\lim\limits_{x\to 0}\frac{\sin x}{x}=1$ 就是靠夹逼（$\cos x \le \frac{\sin x}{x} \le 1$）证明的；定积分定义（黎曼和）的放缩估计也用它
- 对比：单调有界定理管"递推数列收敛性"，夹逼管"具体极限值"；前者保证存在，后者直接算出

## 引用来源

- 来源：[数列与函数极限](../topics/math/calculus/02-03-sequence-function-limits.md)（本库高数 Ch1 长文）
- 教材：《高等数学》（同济版）第一章 极限存在准则

## 相关永久笔记

- [单调有界定理](monotone-bounded-convergence.md)
- [两个重要极限](two-important-limits.md)
