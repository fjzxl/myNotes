---
title: "等价无穷小替换（Equivalent Infinitesimals）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-18
---

# 等价无穷小替换（Equivalent Infinitesimals）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [无穷小、无穷大与连续](../topics/math/calculus/04-05-infinitesimal-continuity.md)。

## 一句话定义

> 求极限时，**因式位置**（乘除）里的无穷小可以整体换成它的等价主部，极限值不变；**加减位置**不能各自替换，除非替换后主部不相消——纪律一句话：**乘除可换，加减保阶**。

## 详细解释

**替换定理**：$\alpha\sim\alpha'$、$\beta\sim\beta'$ 且 $\lim\dfrac{\alpha'}{\beta'}$ 存在（或为 $\infty$），则 $\lim\dfrac\alpha\beta=\lim\dfrac{\alpha'}{\beta'}$。

为什么加减危险：等价的本质是 $\alpha\sim\beta\iff\alpha=\beta+o(\beta)$——两者只差一个**更高阶**的项。乘除时这个高阶误差被主部吸收；加减时若两个主部恰好相消，剩下的恰恰是被忽略的高阶项，替换就把它算没了。

必背等价表（$x\to0$）：

- 一阶：$\sin x\sim\tan x\sim\arcsin x\sim\arctan x\sim\ln(1+x)\sim e^{x}-1\sim x$，$a^{x}-1\sim x\ln a$，$(1+x)^{\alpha}-1\sim\alpha x$
- 二阶：$1-\cos x\sim\dfrac{x^2}2$，$x-\ln(1+x)\sim\dfrac{x^2}2$
- 三阶：$x-\sin x\sim\dfrac{x^3}6$，$\tan x-x\sim\dfrac{x^3}3$，$\tan x-\sin x\sim\dfrac{x^3}2$，$x-\arctan x\sim\dfrac{x^3}3$

加减结构的两种安全处理：**提公因子**化成乘积（$\tan x-\sin x=\tan x\,(1-\cos x)$）；或直接**用三阶条 / 泰勒展开**（等价替换就是泰勒展开只留首项）。

## 例子

- $\lim\limits_{x\to0}\dfrac{e^{x^2}-\cos x}{x^2}$：分子拆 $(e^{x^2}-1)+(1-\cos x)\sim x^2+\dfrac{x^2}2=\dfrac32x^2$，得 $\dfrac32$——加减但主部不消，可换。
- $\lim\limits_{x\to0}\dfrac{\sin x-x\cos x}{x^3}$：拆 $(\sin x-x)+x(1-\cos x)\sim-\dfrac{x^3}6+\dfrac{x^3}2=\dfrac{x^3}3$，得 $\dfrac13$——**注意 $\sin x-x$ 带负号**。
- 反例：$\dfrac{\tan x-\sin x}{x^3}$ 各自替换成 $\dfrac{x-x}{x^3}=0$，真值是 $\dfrac12$。

## 与其他概念的关系

- 上游（前驱）：极限与无穷小的关系式 $\lim f=A\iff f=A+\alpha$；[两个重要极限](two-important-limits.md)（$\frac{\sin x}x\to1$ 正是 $\sin x\sim x$ 的出处）
- 下游（应用）：泰勒展开求极限（等价表 = 展开只留首项的特例）；$1^\infty$ 快算法 $e^{\lim\psi(\varphi-1)}$ 里的 $\varphi-1$ 替换
- 对比：洛必达（`06-limit-techniques`）是通法但对幂结构易越洛越复杂，等价替换是低阶版的轻武器，常先换再洛

## 引用来源

- 来源：[无穷小、无穷大与连续](../topics/math/calculus/04-05-infinitesimal-continuity.md)（本库高数 Ch1 长文）
- 教材：《高等数学》（同济版）第一章 无穷小的比较

## 相关永久笔记

- [两个重要极限](two-important-limits.md)
- [夹逼准则](squeeze-theorem.md)
- [间断点分类](discontinuity-classification.md)
- [七种未定式](indeterminate-forms.md)（替换纪律在主战场的调度规则）
- [导数的定义](derivative-definition.md)（定义求导就是 0/0 极限，替换是其轻武器）
