---
title: "七种未定式（Indeterminate Forms）"
tags:
  - permanent-note
  - math
  - kaoyan
created: 2026-10-20
---

# 七种未定式（Indeterminate Forms）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。提取自 [极限计算方法综合](../topics/math/calculus/06-limit-techniques.md)。

## 一句话定义

七种「零件的极限行为都明确（趋于 0、∞ 或 1），整体却定不了型」的结构——$\dfrac00$、$\dfrac\infty\infty$、$0\cdot\infty$、$\infty-\infty$、$1^\infty$、$0^0$、$\infty^0$；每种都有标准转化路线，最终都汇入 $\dfrac00$ 或 $\dfrac\infty\infty$ 主战场。

## 详细解释

| 型 | 标准转化 | 首选工具 |
|----|---------|---------|
| $\dfrac00$、$\dfrac\infty\infty$ | 直接进主战场 | 等价替换 / 约零因子 → 泰勒 → 洛必达 |
| $0\cdot\infty$ | 翻一个因子 | 留下求导变简单的（对数、反三角留分子） |
| $\infty-\infty$ | 通分 / 有理化 / 倒代换 | 化回主战场 |
| $1^\infty$ | $e^{\lim\psi(\varphi-1)}$ | 快算法（依赖 $\varphi-1\to0$） |
| $0^0$、$\infty^0$ | $u^v=e^{v\ln u}$ | 化为指数上的 $0\cdot\infty$ |

三条使用纪律：

- **先定型再动笔**：大部分极限是确定型（无穷大运算律、有界 × 无穷小 = 0），代入即得；只有确认是未定式才走流程。
- **前四型是差与商、后三型是幂指**：幂指型必须先取对数——四则运算法则不含幂指，$\lim u^v\ne(\lim u)^{\lim v}$。
- **其余都化到主战场**：转化是有限步骤的「换衣」，不要在 $0\cdot\infty$、$\infty-\infty$ 上直接硬算。

## 例子

- $\infty-\infty$ 通分：$\lim\limits_{x\to1}\left(\dfrac1{x-1}-\dfrac2{x^2-1}\right)=\lim\limits_{x\to1}\dfrac1{x+1}=\dfrac12$。
- $0\cdot\infty$ 翻因子：$\lim\limits_{x\to0^+}x\ln x=\lim\limits_{x\to0^+}\dfrac{\ln x}{1/x}\to0$。
- $0^0$ 取对数：$\lim\limits_{x\to0^+}x^x=e^{\lim x\ln x}=e^0=1$——**不是** 0，也**不是**不存在。

## 与其他概念的关系

- 上游（前驱）：[等价无穷小替换](equivalent-infinitesimals.md)（主战场的轻武器）、[两个重要极限](two-important-limits.md)（$1^\infty$ 快算法的来源）
- 下游（应用）：洛必达法则与泰勒展开（Ch2）——主战场的重武器，未定式分类是它们的使用前提（洛必达只吃 $\dfrac00$ 与 $\dfrac\infty\infty$）
- 对比：确定型（无穷大运算律）与未定式的分界，见 [无穷小、无穷大与连续](../topics/math/calculus/04-05-infinitesimal-continuity.md) §1.2

## 引用来源

- 来源：[极限计算方法综合](../topics/math/calculus/06-limit-techniques.md)（本库高数 Ch1 长文）
- 教材：《高等数学》（同济版）第一章 极限运算法则

## 相关永久笔记

- [幂指式极限](power-form-limit.md)
- [等价无穷小替换](equivalent-infinitesimals.md)
- [两个重要极限](two-important-limits.md)
