---
title: PCA 降维
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# PCA 降维

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W12 读 UML p.307-341 时填写本卡，填完删除本行。

## 一句话定义

（待填：找方差最大的正交方向，把数据压到低维而重构误差最小）

## 详细解释

填写时回答：

- 「最大方差」与「最小重构误差」为什么等价？
- PCA 与 SVD 的关系（数据中心化后呢）？
- 特征值谱怎么读（该保留几维、能量占比）？
- 数学侧对接：② MML Ch2 / Ch4（书单 W12 注明对接第 10-11 章）；工程侧：嵌入向量的降维是 RAG 检索的常客。

## 例子

（待填：二维手算一个 2×2 协方差矩阵的主方向）

## 与其他概念的关系

- 上游（前驱）：考研线代（特征值 / 正交对角化）——PCA 就是它的第一现场应用
- 下游（应用）：可视化、去噪、嵌入压缩
- 对比：[聚类](clustering.md)（连续压缩 vs 离散分组）、[核方法](kernel-methods.md)（核 PCA = 非线性版）

## 引用来源

- 《Understanding Machine Learning》p.307-341（Part III Ch3，与聚类同段）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W12 交付卡（对接 MML 第 10-11 章）

## 相关永久笔记

- [聚类](clustering.md)
- [核方法](kernel-methods.md)
