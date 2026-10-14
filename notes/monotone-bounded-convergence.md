---
title: "单调有界定理（Monotone Convergence Theorem）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-12
---

# 单调有界定理（Monotone Convergence Theorem）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [数列与函数极限](../topics/math/calculus/02-03-sequence-function-limits.md)。

## 一句话定义

**单调且有界的数列必有极限**——这是数列收敛的一个充分条件（不必要）。

## 详细解释

- 单调递增 + 有上界 $\Rightarrow$ 收敛；单调递减 + 有下界 $\Rightarrow$ 收敛。
- 核心价值：**不用求出极限就能断言极限存在**，特别适合递推数列 $a_{n+1}=f(a_n)$。
- 使用套路（递推数列两步走）：
  1. **数学归纳法证有界**（先猜出界，常用第一项代入迭代观察）；
  2. **作差 / 作比证单调**（$a_{n+1}-a_n$ 定号，或 $\frac{a_{n+1}}{a_n}$ 与 1 比较）。
- 两步都成立后，对递推式两边取极限（设 $\lim a_n = A$），解出 $A$——存在性与求值分开处理。

## 例子

- 经典：$a_1=\sqrt2,\ a_{n+1}=\sqrt{2+a_n}$。归纳证 $a_n<2$（有上界），且 $a_{n+1}>a_n$（单调增）⇒ 收敛；对递推两边取极限得 $A=\sqrt{2+A}$，解出 $A=2$。
- 反例记忆（为何只是充分条件）：摆动数列 $(-1)^n$ 有界但不单调、也不收敛——有界 ≠ 收敛。

## 与其他概念的关系

- 上游（前驱）：确界原理（实数完备性）、[界与函数](../topics/math/functions-and-bounds.md) 中的上确界概念
- 下游（应用）：与 [夹逼准则](squeeze-theorem.md) 并列为本章两大极限存在准则；幂级数收敛域讨论中部分和数列的收敛判断也用它
- 对比：夹逼准则直接"算出"极限值，本定理只保证"存在"，求值需另对递推式取极限

## 引用来源

- 来源：[数列与函数极限](../topics/math/calculus/02-03-sequence-function-limits.md)（本库高数 Ch1 长文）
- 教材：《高等数学》（同济版）第一章 极限存在准则

## 相关永久笔记

- [夹逼准则](squeeze-theorem.md)
- [两个重要极限](two-important-limits.md)
