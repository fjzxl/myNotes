---
title: "幂指式极限（Power-Form Limits）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-20
---

# 幂指式极限（Power-Form Limits）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [极限计算方法综合](../topics/math/calculus/06-limit-techniques.md)。

## 一句话定义

处理 $u(x)^{v(x)}$ 型极限的总钥匙：恒等式 $u^v=e^{v\ln u}$（$u>0$）把幂指结构搬进指数；$1^\infty$ 型另有快算法 $\varphi^\psi\to e^{\lim\psi(\varphi-1)}$。

## 详细解释

**为什么必须取对数**：四则运算法则只覆盖加、减、乘、除，不含幂指——$\lim u^v\ne(\lim u)^{\lim v}$（$1^\infty$ 型按右式会得 $1$，真值未必是 $1$）。$u^v=e^{v\ln u}$ 是恒等变形，总合法，之后只需求指数上 $v\ln u$ 的极限（通常是 $0\cdot\infty$ 型）。

**$1^\infty$ 快算法的来路**：$\varphi=1+\alpha$（$\alpha\to0$）、$\psi\to\infty$ 时，$\varphi^\psi=\left[(1+\alpha)^{1/\alpha}\right]^{\alpha\psi}$，方括号趋于 $e$，故 $\varphi^\psi\to e^{\lim\alpha\psi}=e^{\lim\psi(\varphi-1)}$——第二重要极限的工程化封装。

**适用边界**：快算法只在 $1^\infty$ 型合法（它依赖 $\varphi-1$ 是无穷小）；$0^0$ 与 $\infty^0$ 必须老实取对数。使用前确认底数在极限点附近为正（如 $x^x$ 只在 $x\to0^+$ 讨论）。

## 例子

- $1^\infty$：$\lim\limits_{x\to0}\left(\dfrac{\sin x}x\right)^{1/x^2}$：$\dfrac{\sin x}x=1-\dfrac{x^2}6+o(x^2)$，指数 $\psi(\varphi-1)=\dfrac1{x^2}\left(-\dfrac{x^2}6+o(x^2)\right)\to-\dfrac16$，极限 $=e^{-1/6}$。
- $0^0$：$\lim\limits_{x\to0^+}x^x=e^{\lim x\ln x}=e^0=1$。
- $\infty^0$：$\lim\limits_{x\to+\infty}x^{1/x}=e^{\lim\frac{\ln x}x}=e^0=1$。

## 与其他概念的关系

- 上游（前驱）：[两个重要极限](two-important-limits.md)（$e$ 的定义与 $1^\infty$ 快算法的推导源）
- 下游（应用）：泰勒展开进指数（如 $(1+x)^{1/x}=e^{1-x/2+o(x)}$，求它与 $e$ 的差是经典考研题）；渐近线与增长率比较（Ch2）
- 对比：[七种未定式](indeterminate-forms.md) 中幂指三型的完整转化表

## 引用来源

- 来源：[极限计算方法综合](../topics/math/calculus/06-limit-techniques.md)（本库高数 Ch1 长文）
- 教材：《高等数学》（同济版）第一章 两个重要极限

## 相关永久笔记

- [两个重要极限](two-important-limits.md)
- [七种未定式](indeterminate-forms.md)
- [等价无穷小替换](equivalent-infinitesimals.md)（快算法里算 $\psi(\varphi-1)$ 的主力工具）
