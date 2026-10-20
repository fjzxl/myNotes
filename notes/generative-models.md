---
title: 生成模型
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# 生成模型

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W13 读 UML p.342-372 时填写本卡，填完删除本行。

## 一句话定义

（待填：建模 P(x) 本身而非 P(y|x)——从「判别世界」跨入「生成世界」的第一步）

## 详细解释

填写时回答：

- 生成 vs 判别：各自的损失、各自的适用场景？
- 似然建模的困难在哪里（高维归一化常数）？
- 谱系一张图：朴素贝叶斯 / HMM → VAE / GAN / 扩散——⑪ UDL Ch14-18 是现代版的完整展开
- 对接工程侧：LLM 就是下一 token 的条件生成模型，temperature / 采样策略（[AI Engineering 导读](../topics/ai/ai-engineering.md) p.29-36）是本卡的工程延伸。

## 例子

（待填）

## 与其他概念的关系

- 上游（前驱）：考研概率（联合 / 条件分布）
- 下游（应用）：LLM 的生成、扩散模型、数据增强
- 对比：[神经网络的学习理论](neural-network-learning-theory.md)——判别侧的现代理论

## 引用来源

- 《Understanding Machine Learning》p.342-372（Part III Ch4）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W13 交付卡

## 相关永久笔记

- [神经网络的学习理论](neural-network-learning-theory.md)
