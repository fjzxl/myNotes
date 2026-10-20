---
title: "导数的定义（Derivative Definition）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-20
---

# 导数的定义（Derivative Definition）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [导数概念与求导法则](../topics/math/calculus/07-derivative.md)。

## 一句话定义

$f'(x_0)=\lim\limits_{\Delta x\to0}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$——函数增量与自变量增量之比的极限，即一点处的**瞬时变化率**。

## 详细解释

- **两种等价形式**：$\lim\limits_{\Delta x\to0}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$ 与 $\lim\limits_{x\to x_0}\dfrac{f(x)-f(x_0)}{x-x_0}$，后者在 $x\to x_0$ 型差商里直接认。
- **左右导数**：$f'_\pm(x_0)=\lim\limits_{\Delta x\to0^\pm}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$；可导 $\iff$ 左右导数都存在且相等（与极限的单侧合一平行）。
- **几何**：切线斜率（切线 = 割线的极限位置）；**物理**：瞬时速度。导数存在要求极限**有限**——差商趋于 $\infty$（如 $\sqrt[3]x$ 在 $0$）算不可导，几何上是铅直切线。
- **差商变形**（考研高频）：$\lim\limits_{h\to0}\dfrac{f(x_0+\varphi(h))-f(x_0)}h=f'(x_0)\cdot\lim\dfrac{\varphi(h)}h$，$\varphi(h)=h,2h,\sin h,\ln(1+h)$ 等无穷小均可；但**对称差** $\dfrac{f(x_0+h)-f(x_0-h)}{2h}$ 的存在性**弱于**可导性。
- **定义求导 = 算 $\frac00$ 极限**：$(\sqrt x)'$ 用有理化、$(e^x)'$ 用 $e^h-1\sim h$、$(\sin x)'$ 用第一重要极限——Ch1 工具箱直接上岗。

## 例子

- $\lvert x\rvert$ 在 $0$：左导数 $-1$、右导数 $+1$，存在但不等 ⇒ 不可导（角点）。
- $f(x)=x^2\sin\dfrac1x$（补 $f(0)=0$）在 $0$：差商 $=h\sin\dfrac1h\to0$（有界 × 无穷小）⇒ **可导**——振荡因子不自动判死。

## 与其他概念的关系

- 上游（前驱）：[七种未定式](indeterminate-forms.md)（差商是 $\frac00$ 型）、[等价无穷小替换](equivalent-infinitesimals.md)（定义求导的轻武器）
- 下游（应用）：[可导与连续](differentiability-vs-continuity.md)（可导 ⇒ 连续由此证）、导数应用（单调性、极值、凹凸性）
- 对比：导函数 $f'(x)$ 是逐点定义出的新函数；分段分界点的导数不能由导函数表达式"代入"得到，必须回定义

## 引用来源

- 来源：[导数概念与求导法则](../topics/math/calculus/07-derivative.md)（本库高数 Ch2 长文）
- 教材：《高等数学》（同济版）第二章 导数概念

## 相关永久笔记

- [可导与连续](differentiability-vs-continuity.md)
- [求导四则与反函数法则](differentiation-rules.md)
- [链式法则](chain-rule.md)
