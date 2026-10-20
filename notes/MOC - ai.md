---
title: AI MOC
tags:
  - moc
  - ai
created: 2026-09-09
updated: 2026-10-18
---

# MOC · AI（AI 知识地图）

> AI 相关的笔记与研究。Claude Code、模型架构、Agent 设计等。

## 全景

按 **基础理论 / 工程实践 / 产品应用 / 行业思考** 四个维度组织：
- 基础：Transformer、Attention、训练方法
- 工程：Prompt、RAG、Fine-tuning、Agent
- 产品：主流 LLM 对比、AI 产品分析
- 思考：行业趋势、个人判断

## 核心笔记

> 必读、最常翻

- [Claude Code](../topics/ai/Claude%20Code.md) —— Claude Code 使用心得（Agent 编程实战）
- [MoE](../topics/ai/MoE.md) —— Mixture of Experts 架构
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— 13 本免费正版教材（链接已实测）+ 给《AI Engineering》补理论地基的阅读路线
- [AI Engineering 导读](../topics/ai/ai-engineering.md) —— Daily Dose of Data Science 免费工程书（384p）：章节地图、四段同步读法与理论对接点
- [深入理解 AI Agent](../topics/ai/understanding-ai-agent.md) —— 开源书索引（Apache-2.0，10 章 + 109 个实验）：本库 Agent 主题的原理层
- [深入理解 AI Infra](../topics/ai/understanding-ai-infra.md) —— 开源书索引（Apache-2.0，12 章 + 110 实验 + 计算工具）：从硬件约束与量化估算推导系统设计，Agent 书的姊妹篇（本库系统层）
- [前线部署工程师 FDE](../topics/ai/fde-guide.md) —— 开源书索引（范冰）：AI 时代的价值交付与岗位，本库求职线的参考

## 按类别

### LLM 与基础模型

- [MoE](../topics/ai/MoE.md) —— Mixture of Experts
- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— 理论书单与阅读路径（UML 补泛化理论，MML 补数学地基）

### AI Infra / 系统

- [深入理解 AI Infra](../topics/ai/understanding-ai-infra.md) —— 加速器、算子、超节点、数据中心网络到推理/训练系统的量化设计；[LLM 工程知识地图](../topics/ai/llm-engineering-map.md) L3 部署层的深水区参考

### 学习路线

- [机器学习书单与完整阅读计划](../topics/ai/ml-booklist.md) —— 每周 5-6h，一学期啃完 UML 正文 + 《数学之美》并行；《AI Engineering》按周同步读
- [LLM 工程知识地图](../topics/ai/llm-engineering-map.md) —— 待补 18 项的分层攻略（资源锚点 + 解锁时机）
- [Agent 实操线](../topics/ai/agent-practice-plan.md) —— 109 实验五阶段（每周 2-3h，与理论线分开记账）
- UML 16 周计划的原子卡骨架（2026-10-16 预建，W2-W13 读到即填）：
  - W2 [学习问题的形式化定义](../notes/formal-definition-of-learning.md) · W3 [偏差-复杂度权衡](../notes/bias-complexity-tradeoff.md) · W4 [VC 维](../notes/vc-dimension.md)
  - W5 [提升法](../notes/boosting.md) · W6 [交叉验证与过拟合](../notes/cross-validation-and-overfitting.md) · W7 [稳定性与正则化](../notes/regularization-and-stability.md)
  - W8 [核方法](../notes/kernel-methods.md) · W9 [决策树](../notes/decision-trees.md) · W10 [神经网络的学习理论](../notes/neural-network-learning-theory.md)
  - W11 [在线学习](../notes/online-learning.md) · W12 [聚类](../notes/clustering.md) + [PCA 降维](../notes/pca-dimensionality-reduction.md) · W13 [生成模型](../notes/generative-models.md)

### Agent / Coding Agent

- [Claude Code](../topics/ai/Claude%20Code.md) —— Claude Code 使用笔记（Agent 编程：拆解问题、分配任务、多智能体协作）
- [深入理解 AI Agent](../topics/ai/understanding-ai-agent.md) —— 第 5 章 Coding Agent + 第 2 章 Agent Skills，是本篇的系统版对照
- [Agent 实操线](../topics/ai/agent-practice-plan.md) —— 109 实验的 A-E 五阶段执行计划（贯穿项目：养大一个自己的 coding agent）
- 待补充：Agent 设计模式、Multi-agent 协作（可从 [深入理解 AI Agent](../topics/ai/understanding-ai-agent.md) 第 10 章切入）

### 行业与思考

- [创新：协同进化（闪念）](../inbox/innovation-flash.md) —— 2026-09 闪念，已按 PARA 移入 inbox 待整理；定期清点时再决定去向
- [前线部署工程师 FDE](../topics/ai/fde-guide.md) —— 岗位与价值交付视角：技术能力怎么转成客户价值，与本库前端求职线相关；附 4 个生态仓库导读与 fde-reader 双语电子书 PDF

## 待补充

18 个空项已迁至 [LLM 工程知识地图](../topics/ai/llm-engineering-map.md) 分层管理（L1 模型基础 / L2 应用工程 / L3 部署 / L4 Agent / L5 产品对比，每项带资源锚点与解锁时机）；写完一篇在那里勾掉并回链本 MOC。

## 按标签查找

Foam 的图谱面板没有查询语法（0.44+ 可用 foam-query 代码块按 tag / link / property 筛选笔记）。按标签筛选用左侧 **Tag Explorer** 面板，或 `Ctrl+Shift+P` → `Foam: Search Tag`；孤立笔记（待补充链接）在 `Foam: Show Graph` 面板查看。

- `ai` —— 所有 AI 笔记（学科伞形，Tag Explorer 树的根）
- `ai/machine-learning` —— 机器学习理论卡
- `ai/llm` —— LLM 基础
- `ai/agent` —— Agent 相关

## 相关 MOC

- [MOC - programming](MOC%20-%20programming.md) —— 编程（Agent 编程实践）
- [MOC - math](MOC%20-%20math.md) —— 数学（深度学习数学基础）

## 更新记录

- **2026-09-09** —— 初始创建（重构后）
- **2026-10-10** —— [Claude Code](../topics/ai/Claude%20Code.md) 由一句话闪念扩充为完整笔记（范式转变、任务拆解、多智能体拓扑、实践清单）；闪念 [创新：协同进化](../inbox/innovation-flash.md) 按 PARA 移入 inbox
- **2026-10-15** —— 全库审查修订：「闪念」链接文字更正为《创新：协同进化》（与目标笔记标题一致）；「按标签查找」的图谱查询表述更新（0.44+ 有 foam-query）；[MoE](../topics/ai/MoE.md) 补 `llm` 标签，使下方标签清单可检索。
- **2026-10-16** —— [机器学习书单](../topics/ai/ml-booklist.md)扩充为四阶段完整阅读计划（新增阶段二至四路线 + 逐本阅读基础自查），本 MOC 三处链接文字同步为《机器学习书单与完整阅读计划》；新增 [AI Engineering 导读](../topics/ai/ai-engineering.md)（核心笔记区）。
- **2026-10-16** —— 书单增补 ⑪UDL ⑫d2l-zh ⑬SLP3（10 → 13 本）；新增 [Agent 实操线](../topics/ai/agent-practice-plan.md)（109 实验五阶段执行计划，Agent / Coding Agent 区收录）。
- **2026-10-16** —— 新增 [LLM 工程知识地图](../topics/ai/llm-engineering-map.md)（「待补充」18 项迁出分层管理）；预建 UML 16 周计划的 13 张原子卡骨架（`notes/`，学习路线区列清单）。
- **2026-10-18** —— 新增 [深入理解 AI Infra](../topics/ai/understanding-ai-infra.md)（Agent 书姊妹篇的开源书索引：12 章 + 110 实验 + 计算工具，中文 PDF 已入库）；核心笔记区收录，并新设「AI Infra / 系统」类别。
