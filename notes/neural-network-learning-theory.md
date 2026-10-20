---
title: 神经网络的学习理论
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# 神经网络的学习理论

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W10 读 UML p.258-284 时填写本卡，填完删除本行。

## 一句话定义

（待填：参数远多于数据、VC 维可以任意大，网络为什么还能泛化——经典理论在哪里失效）

## 详细解释

填写时回答：

- 经典界（VC / 一致收敛）用到 NN 上为什么给出无用的悲观结论？
- 实际观察到的「双下降」与隐式正则怎么动摇「容量大 = 过拟合」的旧叙事？
- SGD 在这个图景里扮演什么角色？
- 深化入口：书单阶段三 ④《The Principles of Deep Learning Theory》与 ⑪ UDL——本卡是它们的门票。

## 例子

（待填）

## 与其他概念的关系

- 上游（前驱）：[VC 维](vc-dimension.md)——先知道悲观界长什么样，才懂它为何失效
- 下游（应用）：[MoE](../topics/ai/MoE.md)（工程放大版）、④ PDLT 的有效理论
- 对比：显式容量控制（[稳定性与正则化](regularization-and-stability.md)）vs 隐式正则

## 引用来源

- 《Understanding Machine Learning》p.258-284（Part II Ch12）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W10 交付卡（本周起与 AI Engineering 的 LLM 段对读）

## 相关永久笔记

- [VC 维](vc-dimension.md)
- [稳定性与正则化](regularization-and-stability.md)
- [生成模型](generative-models.md)
