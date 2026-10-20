---
title: "链式法则（Chain Rule）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-20
---

# 链式法则（Chain Rule）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [导数概念与求导法则](../topics/math/calculus/07-derivative.md)。

## 一句话定义

复合函数 $y=f(\varphi(x))$ 的导数等于各层导数之积：$\dfrac{dy}{dx}=\dfrac{dy}{du}\cdot\dfrac{du}{dx}=f'(u)\cdot\varphi'(x)$——**外层导数在内层取值处算，再乘以内层导数**。

## 详细解释

- **朴素证明的漏洞**：$\dfrac{\Delta y}{\Delta x}=\dfrac{\Delta y}{\Delta u}\cdot\dfrac{\Delta u}{\Delta x}$ 要求 $\Delta u\ne0$，但振荡型内层函数可以无限次回到同一值（$\Delta u=0$）。补救：把外层可导写成增量形式 $f(u_0+\Delta u)-f(u_0)=f'(u_0)\Delta u+\alpha\Delta u$（$\alpha\to0$，**约定 $\alpha(0)=0$**），两边除 $\Delta x$ 取极限即得——"先恒等变形再取极限"的标准手艺。
- **使用流程**：分解复合（$y=e^{x^2}$ 拆成 $e^u$、$u=x^2$）→ 由外向内逐层求导 → 相乘。多层同理：$(\sin^32x)'=3\sin^22x\cdot\cos2x\cdot2$。
- **Leibniz 记号的直观**：$\dfrac{dy}{dx}=\dfrac{dy}{du}\cdot\dfrac{du}{dx}$ 像分式约分——好记但不是证明；微分的严格化（一阶微分形式不变性）让这个直观合法。
- **高频错误**：漏乘内层导数（$(\sin2x)'=\cos2x$ ❌）；多层跳步；把"外层导数"算成"外层函数在 $x$ 处的导数"（应在 $u=\varphi(x)$ 处算）。
- **适用前提**：外层在**内层取值处** $u_0=\varphi(x_0)$ 可导、内层在 $x_0$ 可导——内层取值点错位是最隐蔽的条件错误。

## 例子

- $\left(e^{x^2}\right)'=e^{x^2}\cdot2x=2x\,e^{x^2}$。
- $(\ln\sin x)'=\dfrac1{\sin x}\cdot\cos x=\cot x$。
- $f=x^2\sin\dfrac1x$（$x\ne0$）的导函数 $f'=2x\sin\dfrac1x-\cos\dfrac1x$——链式 + 乘法的合作产物（该函数的 $0$ 点行为见 [可导与连续](differentiability-vs-continuity.md)）。

## 与其他概念的关系

- 上游（前驱）：复合函数分解（界与函数）；[求导四则与反函数法则](differentiation-rules.md)（与之配合覆盖初等函数求导）
- 下游（应用）：隐函数求导（`08`，对方程两边逐项链式）、参数方程求导（$\frac{dy}{dx}=\frac{dy/dt}{dx/dt}$）、换元积分（Ch3 的反向操作）
- 对比：极限的复合传递（连续函数极限号可穿入）与链式法则是"复合"在极限与导数两个世界的对应物

## 引用来源

- 来源：[导数概念与求导法则](../topics/math/calculus/07-derivative.md)（本库高数 Ch2 长文）
- 教材：《高等数学》（同济版）第二章 复合函数的求导法则

## 相关永久笔记

- [求导四则与反函数法则](differentiation-rules.md)
- [导数的定义](derivative-definition.md)
- [等价无穷小替换](equivalent-infinitesimals.md)（复合结构极限的工具，与链式同源于"逐层处理"）
