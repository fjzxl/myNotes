---
title: AI MOC
tags:
  - moc
  - ai
created: 2026-09-09
updated: 2026-10-15
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
- [机器学习书单与 16 周学习计划](../topics/ai/ml-booklist.md) —— 10 本免费正版教材（链接已实测）+ 给《AI Engineering》补理论地基的阅读路线
- [深入理解 AI Agent](../topics/ai/understanding-ai-agent.md) —— 开源书索引（Apache-2.0，10 章 + 109 个实验）：本库 Agent 主题的原理层
- [前线部署工程师 FDE](../topics/ai/fde-guide.md) —— 开源书索引（范冰）：AI 时代的价值交付与岗位，本库求职线的参考

## 按类别

### LLM 与基础模型

- [MoE](../topics/ai/MoE.md) —— Mixture of Experts
- [机器学习书单与 16 周学习计划](../topics/ai/ml-booklist.md) —— 理论书单与阅读路径（UML 补泛化理论，MML 补数学地基）

### 学习路线

- [机器学习书单与 16 周学习计划](../topics/ai/ml-booklist.md) —— 每周 5-6h，一学期啃完 UML 正文 + 《数学之美》并行；《AI Engineering》按周同步读

### Agent / Coding Agent

- [Claude Code](../topics/ai/Claude%20Code.md) —— Claude Code 使用笔记（Agent 编程：拆解问题、分配任务、多智能体协作）
- [深入理解 AI Agent](../topics/ai/understanding-ai-agent.md) —— 第 5 章 Coding Agent + 第 2 章 Agent Skills，是本篇的系统版对照
- 待补充：Agent 设计模式、Multi-agent 协作（可从 [深入理解 AI Agent](../topics/ai/understanding-ai-agent.md) 第 10 章切入）

### 行业与思考

- [创新：协同进化（闪念）](../inbox/innovation-flash.md) —— 2026-09 闪念，已按 PARA 移入 inbox 待整理；定期清点时再决定去向
- [前线部署工程师 FDE](../topics/ai/fde-guide.md) —— 岗位与价值交付视角：技术能力怎么转成客户价值，与本库前端求职线相关

## 待补充

### 基础

- [ ] Transformer 架构笔记
- [ ] Attention 机制（Self-Attention、MHA、MQA、GQA）
- [ ] 位置编码（Positional Encoding、RoPE、ALiBi）
- [ ] 训练流程（预训练、SFT、RLHF、DPO）
- [ ] 推理优化（KV-Cache、Speculative Decoding、量化）

### 工程

- [ ] Prompt Engineering
- [ ] RAG 系统设计
- [ ] Fine-tuning 实操（LoRA、QLoRA）
- [ ] 模型评估与基准
- [ ] 本地部署（Ollama、vLLM、llama.cpp）
- [ ] Function Calling / Tool Use
- [ ] MCP 协议

### Agent

- [ ] ReAct、Reflexion、Plan-and-Execute 模式
- [ ] Memory 系统（短期、长期、向量）
- [ ] Multi-agent 协作框架（AutoGen、CrewAI、LangGraph）

### 产品与对比

- [ ] 主流 LLM 对比（GPT/Claude/Gemini/开源模型）
- [ ] AI 编程工具对比（Copilot、Cursor、Claude Code）
- [ ] 国产 LLM 调研

## 按标签查找

Foam 的图谱面板没有查询语法（0.44+ 可用 foam-query 代码块按 tag / link / property 筛选笔记）。按标签筛选用左侧 **Tag Explorer** 面板，或 `Ctrl+Shift+P` → `Foam: Search Tag`；孤立笔记（待补充链接）在 `Foam: Show Graph` 面板查看。

- `ai` —— 所有 AI 笔记
- `llm` —— LLM 基础
- `agent` —— Agent 相关

## 相关 MOC

- [MOC - programming](MOC%20-%20programming.md) —— 编程（Agent 编程实践）
- [MOC - math](MOC%20-%20math.md) —— 数学（深度学习数学基础）

## 更新记录

- **2026-09-09** —— 初始创建（重构后）
- **2026-10-10** —— [Claude Code](../topics/ai/Claude%20Code.md) 由一句话闪念扩充为完整笔记（范式转变、任务拆解、多智能体拓扑、实践清单）；闪念 [创新：协同进化](../inbox/innovation-flash.md) 按 PARA 移入 inbox
- **2026-10-15** —— 全库审查修订：「闪念」链接文字更正为《创新：协同进化》（与目标笔记标题一致）；「按标签查找」的图谱查询表述更新（0.44+ 有 foam-query）；[MoE](../topics/ai/MoE.md) 补 `llm` 标签，使下方标签清单可检索。
