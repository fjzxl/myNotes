---
title: 偏差-复杂度权衡
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# 偏差-复杂度权衡

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W3 读 UML p.54-66 时填写本卡，填完删除本行。

## 一句话定义

（待填：泛化误差如何被拆成「近似误差 + 估计误差」，假设类大小如何在两端此消彼长）

## 详细解释

填写时回答：

- 分解定理的两个误差项分别由什么决定？各自对应「偏差」「方差」的哪个直觉？
- 假设类变大 / 变小分别伤在哪一端？
- 为什么这个分解直接解释了「过拟合」与「欠拟合」？

## 例子

（待填）

## 与其他概念的关系

- 上游（前驱）：[学习问题的形式化定义](formal-definition-of-learning.md)
- 下游（应用）：[交叉验证与过拟合](cross-validation-and-overfitting.md)——用数据挑假设类大小，就是在权衡这两端
- 对比：[VC 维](vc-dimension.md) 给「复杂度」一侧提供定量刻度

## 引用来源

- 《Understanding Machine Learning》p.54-66（Part I Ch3-4）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W3 交付卡

## 相关永久笔记

- [学习问题的形式化定义](formal-definition-of-learning.md)
- [VC 维](vc-dimension.md)
- [交叉验证与过拟合](cross-validation-and-overfitting.md)
