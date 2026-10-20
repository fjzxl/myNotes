---
title: 决策树
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# 决策树

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W9 读 UML p.227-257 时填写本卡，填完删除本行。

## 一句话定义

（待填：用轴对齐的递归划分逼近任意决策边界——一棵会问问题的树）

## 详细解释

填写时回答：

- 树的归纳偏置是什么（为什么偏爱浅的、平衡的）？
- 划分准则（信息增益 / Gini）在优化什么？
- 剪枝为什么是正则化（对接 [偏差-复杂度权衡](bias-complexity-tradeoff.md)）？
- 为什么树是 boosting / 随机森林的理想基学习器（不稳定 + 可加权）？

## 例子

（待填）

## 与其他概念的关系

- 上游（前驱）：[提升法（Boosting）](boosting.md)——树的集成是 W5 概念的最大应用场
- 下游（应用）：梯度提升树（工业界表格数据基线）
- 对比：树的「硬划分」 vs 核方法的「软相似度」

## 引用来源

- 《Understanding Machine Learning》p.227-257（Part II Ch9-10，Decision Trees 在 Ch10）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W9 交付卡

## 相关永久笔记

- [提升法（Boosting）](boosting.md)
- [偏差-复杂度权衡](bias-complexity-tradeoff.md)
