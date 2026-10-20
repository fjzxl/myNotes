---
title: "两个重要极限（Two Important Limits）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-12
---

# 两个重要极限（Two Important Limits）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [数列与函数极限](../topics/math/calculus/02-03-sequence-function-limits.md)。

## 一句话定义

$$\lim_{x\to 0}\frac{\sin x}{x}=1 \qquad\qquad \lim_{x\to\infty}\left(1+\frac1x\right)^x=\mathrm{e}\ \left(\text{即}\ \lim_{x\to 0}(1+x)^{\frac1x}=\mathrm{e}\right)$$

## 详细解释

- **第一个**是"非零因子极限为 1"的三角模板：任何"无穷小比无穷小"只要能凑成 $\frac{\sin(\square)}{\square}$（$\square\to0$）就趋于 1。它直接给出等价无穷小 $\sin x \sim x$（以及 $\tan x \sim x$），是等价替换体系的源头。
- **第二个**是 $\mathrm{e}$ 的定义式，处理 **$1^\infty$ 型**极限的标准模板：
  $$\lim f^g=\lim\left[1+(f-1)\right]^{\frac{1}{f-1}\cdot(f-1)g}=\mathrm{e}^{\lim (f-1)g}\quad(f\to1,\ g\to\infty)$$
- 几何直观：第一个来自单位圆上"弦 < 弧 < 切线"的夹逼；第二个来自 ($1+\frac1n$)^n 的单调有界收敛（复利 / 连续计息模型）。
- 双侧估计（数值上界）：$\frac{1}{n+1}<\ln\left(1+\frac1n\right)<\frac1n$，考研常用它夹逼含 $\mathrm{e}$ 或 $\ln$ 的数列。

## 例子

- $\lim\limits_{x\to0}\frac{\sin 3x}{\tan 5x}=\lim\limits_{x\to0}\frac{\sin 3x}{3x}\cdot\frac{5x}{\tan 5x}\cdot\frac35=\frac35$——凑模板。
- $\lim\limits_{x\to\infty}\left(\frac{x+2}{x-1}\right)^x$：$1^\infty$ 型，改写为 $\left(1+\frac{3}{x-1}\right)^{\frac{x-1}{3}\cdot\frac{3x}{x-1}}\to \mathrm{e}^{3}$。

## 与其他概念的关系

- 上游（前驱）：[夹逼准则](squeeze-theorem.md)（第一个的证明工具）、[单调有界定理](monotone-bounded-convergence.md)（$\mathrm{e}$ 作为数列极限的存在性）
- 下游（应用）：等价无穷小替换（$\sin x\sim x$、$\ln(1+x)\sim x$、$\mathrm{e}^x-1\sim x$ 全部由这两个极限衍生）；$1^\infty$、$0^0$、$\infty^0$ 型幂指函数极限
- 对比：第一个是 $x\to0$ 的"比值型"，第二个是 $x\to\infty$ 的"幂指型"——考试里 $1^\infty$ 几乎年年以变体出现

## 引用来源

- 来源：[数列与函数极限](../topics/math/calculus/02-03-sequence-function-limits.md)（本库高数 Ch1 长文）
- 教材：《高等数学》（同济版）第一章 两个重要极限

## 相关永久笔记

- [夹逼准则](squeeze-theorem.md)
- [单调有界定理](monotone-bounded-convergence.md)
- [幂指式极限](power-form-limit.md)（$1^\infty$ 快算法的工程化封装）
