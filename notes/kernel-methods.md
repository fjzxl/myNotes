---
title: 核方法
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# 核方法

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W8 读 UML p.202-226 时填写本卡，填完删除本行。

## 一句话定义

（待填：只要算法只依赖内积，就能用一个核函数隐式地在高维空间工作——不必显式升维）

## 详细解释

填写时回答：

- 核技巧为什么「免费」——计算发生在哪、没有发生在哪？
- 合法核的条件（Mercer / 半正定）怎么理解？
- 表示定理说的是什么（最优解落在由数据张成的 span 里）？
- 中文桥梁：《数学之美》第 7 章核函数（并行线 W5-W8 正好同期）。

## 例子

（待填：多项式核在低维算出高维内积的一个手算例子）

## 与其他概念的关系

- 上游（前驱）：[PCA 降维](pca-dimensionality-reduction.md)——同属「谱方法 / 内积几何」家族，一个升维一个降维
- 下游（应用）：SVM、高斯过程；Transformer 注意力里的 QK^T 也可看作一种核视角
- 对比：显式特征映射 vs 隐式核计算

## 引用来源

- 《Understanding Machine Learning》p.202-226（Part II Ch7-8）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W8 交付卡（对接《数学之美》第 7 章）

## 相关永久笔记

- [PCA 降维](pca-dimensionality-reduction.md)
