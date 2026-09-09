---
title: AI MOC
tags:
  - moc
  - ai
created: 2026-09-09
updated: 2026-09-09
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

- [[topics/ai/Claude Code]] —— Claude Code 使用心得（Agent 编程实战）
- [[topics/ai/MoE]] —— Mixture of Experts 架构

## 按类别

### LLM 与基础模型

- [[topics/ai/MoE]] —— Mixture of Experts

### Agent / Coding Agent

- [[topics/ai/Claude Code]] —— Claude Code 使用笔记
- 待补充：Agent 设计模式、Multi-agent 协作

### 行业与思考

- [[topics/ai/note]] —— 闪念与短想法

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

## Foam 图谱查询

```
tag:ai                            # 所有 AI 笔记
tag:ai AND tag:llm                # LLM 基础
tag:ai AND tag:agent              # Agent 相关
tag:ai AND -ORPHANS:true          # 孤立的 AI 笔记（待补充链接）
```

## 相关 MOC

- [[notes/MOC - programming]] —— 编程（Agent 编程实践）
- [[notes/MOC - math]] —— 数学（深度学习数学基础）

## 更新记录

- **2026-09-09** —— 初始创建（重构后）
