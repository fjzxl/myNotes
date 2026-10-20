---
title: 交叉验证与过拟合
tags:
  - permanent-note
  - ai
  - ai/machine-learning
---

# 交叉验证与过拟合

> **Zettelkasten 永久笔记** —— 一个概念，一个笔记。
> 🚧 **骨架**（预建 2026-10-16）：W6 读 UML p.144-170 时填写本卡，填完删除本行。

## 一句话定义

（待填：用 held-out / k 折数据估计泛化误差，从而在假设类与超参里做选择）

## 详细解释

填写时回答：

- held-out 估计为什么无偏？它的方差从哪来（取决于什么）？
- k 折交叉验证在偏差与方差之间怎么取舍（k 的两端各发生什么）？
- 训练 / 验证 / 测试三集的职责边界；「验证集泄露」的典型形态？
- 对接工程侧：[AI Engineering 导读](../topics/ai/ai-engineering.md) p.331-357 的 LLM 评测体系，理论根就在本卡。

## 例子

（待填）

## 与其他概念的关系

- 上游（前驱）：[偏差-复杂度权衡](bias-complexity-tradeoff.md)——交叉验证就是在数据端做这个权衡
- 下游（应用）：[稳定性与正则化](regularization-and-stability.md)——另一条控制过拟合的路线
- 对比：结构风险最小化（用复杂度罚项）vs 数据驱动选择（交叉验证）

## 引用来源

- 《Understanding Machine Learning》p.144-170（Part II Ch3）
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— W6 交付卡

## 相关永久笔记

- [偏差-复杂度权衡](bias-complexity-tradeoff.md)
- [稳定性与正则化](regularization-and-stability.md)
