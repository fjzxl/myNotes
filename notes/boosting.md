---
title: 提升法（Boosting）
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# 提升法（Boosting）

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W5 读 UML p.117-143 时填写本卡，填完删除本行。

## 一句话定义

（待填：弱可学习 = 强可学习——boosting 如何把「只比随机猜好一点」的假设放大成强假设）

## 详细解释

填写时回答：

- AdaBoost 的权重更新在做什么（被错分的样本权重变大，下一轮聚焦哪里）？
- 为什么「弱 = 强」这件事在形式化框架里不平凡？
- 集成学习的直觉：多个弱假设的多数表决为什么能降低估计误差？

## 例子

（待填）

## 与其他概念的关系

- 上游（前驱）：[偏差-复杂度权衡](bias-complexity-tradeoff.md)——集成降低的是哪一端
- 下游（应用）：[决策树](decision-trees.md)——树是 boosting / 随机森林最常用的基学习器
- 对比：bagging（并行、降方差）vs boosting（串行、降偏差）

## 引用来源

- 《Understanding Machine Learning》p.117-143（Part II Ch1-2，Boosting 在 Ch2）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W5 交付卡

## 相关永久笔记

- [决策树](decision-trees.md)
- [偏差-复杂度权衡](bias-complexity-tradeoff.md)
