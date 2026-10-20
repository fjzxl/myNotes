---
title: "可导与连续（Differentiability vs Continuity）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-20
---

# 可导与连续（Differentiability vs Continuity）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [导数概念与求导法则](../topics/math/calculus/07-derivative.md)。

## 一句话定义

**可导 ⇒ 连续 ⇒ 极限存在**，链条每一步都不可逆——证明只有一行（$\Delta y=\dfrac{\Delta y}{\Delta x}\cdot\Delta x\to f'(x_0)\cdot0=0$），反例库却要背一串。

## 详细解释

- **证明**：可导给出 $\dfrac{\Delta y}{\Delta x}\to f'(x_0)$（有限），配上 $\Delta x\to0$，"有限 × 无穷小 = 无穷小"即 $\Delta y\to0$。
- **逆否命题更好用**：间断 ⇒ 不可导（判可导前先查连续性，一步排雷）。
- **三类"连续但不可导"的标准反例**（几何画像各不相同）：

| 反例 | 在 $0$ 处 | 几何画像 |
|------|----------|---------|
| $\lvert x\rvert$ | 左右导数 $-1\ne1$ | 角点（两条单侧切线） |
| $\sqrt[3]{x}$ | 差商 $\to+\infty$ | 铅直切线 |
| $x\sin\dfrac1x$（补 $f(0)=0$） | 差商 $=\sin\dfrac1x$ 振荡 | 无限抖动 |

- **更细的层次**：$x^2\sin\dfrac1x$（补 $f(0)=0$）在 $0$ **可导**（$f'(0)=0$）但导函数在 $0$ **不连续**——可导性对振荡的容忍度取决于"压得住压不住"（$x$ 压不住 $x\sin\dfrac1x$ 的差商，$x^2$ 压得住）。
- **对称差陷阱**：$\lim\limits_{h\to0}\dfrac{f(x_0+h)-f(x_0-h)}{2h}$ 存在 ⇏ 可导（$\lvert x\rvert$ 在 $0$ 对称差恒 $0$）；反方向（可导 ⇒ 对称差 = $f'(x_0)$）成立。

## 例子

- 分段点判可导的完整流程：先验连续（左右极限 $=f(x_0)$），再用**定义**算左右导数——用 $\lim\limits_{x\to x_0}f'(x)$ 代替定义是经典错误，$x^2\sin\dfrac1x$ 正是"导函数极限不存在、该点却可导"的活证。

## 与其他概念的关系

- 上游（前驱）：[导数的定义](derivative-definition.md)（一切由差商极限出发）
- 下游（应用）：可导性的判定题；`09` 中值定理要求"闭区间连续 + 开区间可导"——两个条件分别对应本文链条的两环
- 对比：闭区间上连续函数管"取值"（最值、介值），可导性管"变化率"——条件不同、结论族不同，混用即错

## 引用来源

- 来源：[导数概念与求导法则](../topics/math/calculus/07-derivative.md)（本库高数 Ch2 长文）
- 教材：《高等数学》（同济版）第二章 可导性与连续性

## 相关永久笔记

- [导数的定义](derivative-definition.md)
- [介值定理与零点定理](intermediate-value-theorem.md)（连续性的"取值"红利，与可导性的"变化率"红利对照）
