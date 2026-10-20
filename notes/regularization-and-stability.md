---
title: 稳定性与正则化
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# 稳定性与正则化

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W7 读 UML p.171-201 时填写本卡，填完删除本行。

## 一句话定义

（待填：不问假设类多大，问算法对单个训练样本的扰动多敏感——稳定性给出另一种泛化界）

## 详细解释

填写时回答：

- 「算法稳定」的形式定义（换掉一个样本，输出变化被什么控制）？
- Tikhonov 正则化（岭回归型）如何同时做到「正则」与「稳定」？
- 与 VC 路线的分工：什么时候稳定性界比一致收敛界更紧？
- 对接工程侧：LoRA 为什么有效——低秩约束 = 一种容量限制，[AI Engineering 导读](../topics/ai/ai-engineering.md) p.78-91 的工程直觉由本卡供给理论。

## 例子

（待填）

## 与其他概念的关系

- 上游（前驱）：[交叉验证与过拟合](cross-validation-and-overfitting.md)——同一问题的两条防线
- 下游（应用）：LoRA（工程侧）、SGD 的隐式正则（W7 同周读的 Ch6）
- 对比：显式正则（加罚项）vs 隐式正则（算法自带）

## 引用来源

- 《Understanding Machine Learning》p.171-201（Part II Ch5-6）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W7 交付卡（对接 LoRA 直觉）

## 相关永久笔记

- [交叉验证与过拟合](cross-validation-and-overfitting.md)
- [神经网络的学习理论](neural-network-learning-theory.md)
