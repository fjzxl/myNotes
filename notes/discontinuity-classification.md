---
title: "间断点分类（Discontinuity Classification）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-18
---

# 间断点分类（Discontinuity Classification）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [无穷小、无穷大与连续](../topics/math/calculus/04-05-infinitesimal-continuity.md)。

## 一句话定义

> 以**左右极限是否都存在**为第一刀：都存在是**第一类**（极限相等而不连续为**可去**，不相等为**跳跃**）；至少一个不存在是**第二类**（趋于 $\infty$ 为**无穷间断**，振荡不收敛为**振荡间断**）。

## 详细解释

连续三要素：$f(x_0)$ 有定义、$\lim\limits_{x\to x_0}f(x)$ 存在、两者相等——缺一即间断。分类时先找**嫌疑点**（无定义点、分段点、$e^{1/x}$ 型分界），逐个算左右极限再落刀：

- **可去**：左右极限存在且相等，只是 $f(x_0)$ 缺席或对不上。改名"可去"的理由：补充/修改定义 $f(x_0):=$ 极限值即连续。
- **跳跃**：左右极限都存在但不等，差一个"台阶"，定义怎么改都救不回来。
- **无穷**：至少一侧趋于 $\infty$（如 $\dfrac1x$ 于 $0$）。
- **振荡**：极限不存在也非无穷（如 $\sin\dfrac1x$ 于 $0$——归结原则取两条数列可证）。

判别 $e^{1/x}$、$\arctan\dfrac1x$ 型务必分左右：两侧行为天然不对称。

## 例子

一题见全部四类骨架：$f(x)=\dfrac{x^2-x}{|x|(x^2-1)}=\dfrac{\operatorname{sgn}x}{x+1}$（$x\ne0,\pm1$）——

- $x\to0$：左 $-1$、右 $1$，**跳跃**；
- $x\to1$：极限 $\dfrac12$ 但无定义，**可去**（补 $f(1)=\tfrac12$ 即连续）；
- $x\to-1$：$|f|\to\infty$，**无穷间断**。

另有：$\dfrac{\sin x}x$ 于 $0$ 可去；$x\sin\dfrac1x$ 于 $0$ 可去（补 $0$）；$\operatorname{sgn}x$ 于 $0$ 跳跃。

## 与其他概念的关系

- 上游（前驱）：左极限与右极限（"双单合一"）；Heine 定理（证振荡间断极限不存在的武器）
- 下游（应用）：可导 ⇒ 连续——间断点是不可导的第一嫌疑；定积分存在性（第一类间断 + 振荡有界不影响可积）
- 对比：**极限不存在 ≠ 间断点**——间断点要求 $f$ 在该点的某去心邻域内有定义（如 $\ln x$ 于 $0$：左侧根本无定义，通常不在此语境下讨论）

## 引用来源

- 来源：[无穷小、无穷大与连续](../topics/math/calculus/04-05-infinitesimal-continuity.md)（本库高数 Ch1 长文）
- 教材：《高等数学》（同济版）第一章 连续函数的运算与间断点

## 相关永久笔记

- [等价无穷小替换](equivalent-infinitesimals.md)
- [介值定理与零点定理](intermediate-value-theorem.md)
- [两个重要极限](two-important-limits.md)
