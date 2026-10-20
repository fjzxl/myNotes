---
title: VC 维
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# VC 维

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W4 读 UML p.67-99 时填写本卡，填完删除本行。

## 一句话定义

（待填：VC 维衡量的是什么——注意它不是「参数个数」，而是假设类能打散的最大点集规模）

## 详细解释

填写时回答：

- 「打散（shatter）」的精确定义？为什么定义在「存在一个可打散的点集」上？
- Sauer 引理怎么说（假设类在 n 个点上的增长被 VC 维控制）？
- VC 维有限 ⇔ 可学习（一致收敛刻画）——这条等价链的每一环分别是什么？
- 常见坑：参数多 ≠ VC 维大（找出一个反例直觉）。

## 例子

（待填：二维平面上的线性分类器 VC 维 = 3，自己验证）

## 与其他概念的关系

- 上游（前驱）：[偏差-复杂度权衡](bias-complexity-tradeoff.md)——VC 维是「复杂度」端的定量刻度
- 下游（应用）：[神经网络的学习理论](neural-network-learning-theory.md)——NN 为什么能挣脱 VC 维的悲观界
- 对比：与「参数计数」的容量直觉对比

## 引用来源

- 《Understanding Machine Learning》p.67-99（Part I Ch5-6）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W4 交付卡（重点：它到底在衡量什么）

## 相关永久笔记

- [偏差-复杂度权衡](bias-complexity-tradeoff.md)
- [学习问题的形式化定义](formal-definition-of-learning.md)
- [神经网络的学习理论](neural-network-learning-theory.md)
