---
title: "求导四则与反函数法则（Differentiation Rules）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-20
---

# 求导四则与反函数法则（Differentiation Rules）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [导数概念与求导法则](../topics/math/calculus/07-derivative.md)。

## 一句话定义

$[u\pm v]'=u'\pm v'$，$[uv]'=u'v+uv'$，$\left[\dfrac uv\right]'=\dfrac{u'v-uv'}{v^2}$；反函数导数互倒：$\varphi'(y_0)=\dfrac1{f'(x_0)}$。

## 详细解释

- **乘法法则的心脏是"加一项减一项"**：$\Delta(uv)=\Delta u\cdot v(x_0+\Delta x)+u(x_0)\cdot\Delta v$，除以 $\Delta x$ 取极限，$v$ 的连续性（可导 ⇒ 连续）把 $v(x_0+\Delta x)$ 送回 $v(x_0)$。
- **商法则先证倒数**：$\left(\dfrac1v\right)'=-\dfrac{v'}{v^2}$（通分差商即得），再与乘法组合；分子顺序"**分子导分母不导 − 分子不导分母导**"——用 $(\tan x)'=\sec^2x$ 的推导锁死符号记忆。
- **两条红线**：$(uv)'\ne u'v'$（$x\cdot x$：$2x\ne1$）；法则要求**每个成员都可导**，某段不可导时法则对该点失效（分段点回定义）。
- **反函数法则的三个条件**：单调（$\Delta y\ne0\Rightarrow\Delta x\ne0$，比值有意义）、连续（$\Delta y\to0\Rightarrow\Delta x\to0$）、$f'(x_0)\ne0$（倒数才有意义）；几何：互为反函数的曲线关于 $y=x$ 对称，对称点斜率互倒。
- **装备线路**：$\sin'$、$e'$ 由定义直证 → 商法则出 $\tan'$ → 反函数法则出 $\arcsin'$、$\arctan'$、$\ln'$ → 换底 / 链式补全导数表。

## 例子

- $(\tan x)'=\left(\dfrac{\sin x}{\cos x}\right)'=\dfrac{\cos^2x+\sin^2x}{\cos^2x}=\sec^2x$。
- $(\arcsin x)'=\dfrac1{(\sin y)'}=\dfrac1{\cos y}=\dfrac1{\sqrt{1-x^2}}$（主值区间内 $\cos y>0$ 取正根）。
- $(\ln x)'=\dfrac1{(e^y)'}=\dfrac1x$——对数导数由指数导数反出。

## 与其他概念的关系

- 上游（前驱）：[导数的定义](derivative-definition.md)（法则全部由差商极限推出）
- 下游（应用）：[链式法则](chain-rule.md) 与四则混用覆盖一切初等函数求导；高阶导数（`08`）逐阶反复使用
- 对比：极限四则（Ch1）与求导四则形似而不同——极限版只要求各极限存在，求导版还要求可导性本身

## 引用来源

- 来源：[导数概念与求导法则](../topics/math/calculus/07-derivative.md)（本库高数 Ch2 长文）
- 教材：《高等数学》（同济版）第二章 函数的求导法则

## 相关永久笔记

- [导数的定义](derivative-definition.md)
- [链式法则](chain-rule.md)
- [可导与连续](differentiability-vs-continuity.md)（乘法法则证明里用到"可导 ⇒ 连续"）
