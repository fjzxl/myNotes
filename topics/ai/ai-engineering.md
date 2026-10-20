---
title: AI Engineering（Daily Dose of Data Science）· 导读
tags:
  - ai
  - ai/llm
  - ai/ai-engineering
  - ai/book
---

# AI Engineering：LLM、RAG 与 Agent 的系统设计模式（导读）

> 开源免费书（封面标注 FREE · 2025 Edition），**本地 PDF**：[ai-engineering-guidebook.pdf](ai-engineering-guidebook.pdf)（384 页，作者标称通读约 20 小时）
> 全名 *AI Engineering: System Design Patterns for LLMs, RAG and Agents*，Akshay Pachaar & Avi Chawla 出品（Daily Dose of Data Science，<https://www.dailydoseofds.com>）
> 定位：本库 [机器学习书单](ml-booklist.md) 理论线的**服务对象**——16 周计划里每周的「同步线」读的就是它；书前附 2 分钟自评（<https://bit.ly/ai-engg-assessment>），会按你的水平推荐章节

---

## 一、这本书在本库的位置

它是**工程实践书**：LLM 原理与训练、LoRA/GRPO、RAG、Context Engineering、Agent/ReAct/多智能体、MCP、推理优化、vLLM 部署、评测，一条龙讲「怎么做」。它假设你已经知道「为什么 LoRA 是低秩的」「为什么泛化误差可以这么估计」——这正是 [ml-booklist](ml-booklist.md) 理论线（①UML 主线 + 数学补强）要补的地基。两边的关系：**理论线解释它，它给理论线提供落点**；每周对照读法见 ml-booklist 第四节的「同步线」表。

## 二、章节地图（11 章 · 384 页）

| # | 章 | 页码 | 内容与亮点小节 |
|---|---|---|---|
| 1 | LLMs | p.6-48 | 是什么/为何大/怎么造；**从零训练 LLM** p.18；**7 个生成参数** p.29；**4 种生成策略** p.33；用 LLM 训 LLM 的 3 技术 p.37；本地运行 4 法 p.40；**Transformer vs MoE** p.44（对接 [MoE](MoE.md)） |
| 2 | Prompt Engineering | p.49-65 | 推理型提示 3 技法 p.51；Verbalized Sampling p.58；JSON prompting p.61 |
| 3 | Fine-tuning | p.66-104 | 5 种微调技术 p.70；**LoRA from scratch** p.78-85；自造 IFT 数据集 p.86；SFT vs RFT p.92；**GRPO 动手** p.94；OpenEnv p.101；ART p.103 |
| 4 | RAG | p.105-145 | 向量数据库 p.107；系统 workflow p.113；**5 种分块策略** p.118；Prompting/RAG/Finetuning 取舍 p.124；8 种架构 p.126；Agentic RAG p.128；HyDE p.131；vs REFRAG/CAG p.139-141 |
| 5 | Context Engineering | p.146-175 | Agent 的上下文工程 p.149；**6 类上下文** p.156；workflow 实操 p.158；Claude Skills 里的应用 p.168 |
| 6 | AI Agents | p.176-263 | 构建块 p.181；记忆类型 p.195；**5 种设计模式** p.199；**ReAct from scratch** p.205；5 个层级 p.231；30 个术语 p.235；4 层结构 p.240；**多智能体 7 模式** p.242；A2A p.245 / AG-UI p.248 / 协议版图 p.252；Opik 优化 p.255；部署策略 p.260 |
| 7 | MCP | p.264-303 | 架构总览 p.269；Tools/Resources/Prompts p.273；API vs MCP p.278；vs Function Calling p.281；6 个原语 p.282；**MCP Agent/Client/Server 实操** p.286-291；工具过载陷阱与 Server Manager p.287 |
| 8 | LLM Optimization | p.304-330 | 模型压缩 p.306；传统 ML vs LLM 推理 p.318；**KV Cache** p.326 |
| 9 | LLM Evaluation | p.331-357 | G-eval p.332；Arena-as-a-Judge p.335；多轮评测 p.337；MCP 应用评测 p.341；组件级评测 p.348；红队 p.352 |
| 10 | LLM Deployment | p.358-369 | vLLM p.361；LitServe p.365 |
| 11 | LLM Observability | p.370-384 | 评测 vs 可观测 p.371；落地实现 p.373 |

## 三、怎么读：四个同步段

与 ml-booklist 的 16 周同步线一致，全书切成四段，**不通读**，按周取用：

| 段 | 周次 | 本书部分 | 读时带着的问题 |
|---|---|---|---|
| ① | W1-W4 | p.6-48（LLMs） | 「这些组件在数学上对应什么」——建立工程概念 ↔ 理论概念的对照地图；p.44 MoE 段配合 [MoE](MoE.md) 一起读 |
| ② | W5-W10 | p.49-175（Prompt/Fine-tuning/RAG/Context） | W7 读 UML 稳定性正则化的同一周，读 LoRA（p.78-91）——「限制容量为什么反而 generalize 好」正是 LoRA 有效性的理论侧写 |
| ③ | W11-W13 | p.176-254（Agents） | 读完 UML 在线学习（W11）再看 Agent 决策：ReAct 的试错循环就是探索/利用；动手点 ReAct from scratch p.205 |
| ④ | W14-W16 | p.255-384（MCP/优化/评测/部署/可观测） | 收尾工程面；KV Cache（p.326）配 MML 的矩阵运算直觉；评测章（p.331-357）回看 W6 的 validation——held-out 为什么能估泛化 |

## 四、理论与工程对接点（本导读的核心）

工程书写「怎么做」，理论线回答「为什么行得通」。目前排定的对接：

| 书中主题（页码） | 理论线的解释（书单哪本/哪周） |
|---|---|
| LoRA 低秩适配（p.78-91） | ① W7 Regularization and Stability——容量受限假设类的泛化收益；阶段三 ④ PDLT 的参数谱视角再深一层 |
| MoE 稀疏激活（p.44-48） | [MoE](MoE.md) 科普层；④ 的「初始化有效理论」解释专家坍塌的表达性根源 |
| 评测体系（p.331-357） | ① W6 Model Selection and Validation——为什么 held-out 集能估泛化；G-eval/Arena 当 judge 的统计含义 |
| Agent 决策（p.176-263） | ① W11 Online Learning（探索/利用）；[Claude Code](Claude%20Code.md) 的任务拆解=搜索空间划分 |
| 生成参数与策略（p.29-36） | 概率直觉（⑨ EP4A / 考研概率）：temperature 本质是对下一 token 分布重加权后再采样 |
| KV Cache 与模型压缩（p.304-330） | ② MML Ch2/Ch4——矩阵运算与分解的直觉（注意力矩阵的重复计算为什么可缓存） |

> 新增对接点时补进这张表——它是「理论线学到的东西往哪放」的登记簿。

## 五、动手清单

书里带可运行代码的章节，适合在对应周次顺手做掉（Python 环境）：

- LoRA from scratch（p.78）——与 W7 同步
- Build a Reasoning LLM using GRPO（p.94）——W5-W10 段
- Context Engineering workflow（p.158）——W11-W13 段
- ReAct Implementation from scratch（p.205）——W11-W13 段
- Opik Agent 优化（p.255）、MCP Client/Server（p.289/p.291）——W14-W16 段

## 六、来源与版权

封面标注 FREE（2025 Edition），由 Daily Dose of Data Science（Akshay Pachaar & Avi Chawla）官方发放，官网 <https://www.dailydoseofds.com>。著作权归作者/出品方所有；本库按个人学习用途保存 PDF 与这份索引，不再分发。

---

## 相关笔记

- [机器学习书单与完整阅读计划](ml-booklist.md) —— 理论线主线（16 周 + 四阶段），本文是其「同步线」的对象
- [MoE](MoE.md) —— 对接本书 p.44-48 的概念详解
- [LLM 工程知识地图](llm-engineering-map.md) —— 待补 18 项的分层攻略（本导读是其页码锚点的主要来源）
- [深入理解 AI Agent](understanding-ai-agent.md) —— 原理层：本书 Agents/MCP 章（p.176-303）的中文系统版
- [Claude Code](Claude%20Code.md) —— Agent 编程方法论，本书多智能体章的实践对照
- [MOC - ai](../../notes/MOC%20-%20ai.md) —— AI 知识地图

## 更新记录

- **2026-10-16** 初始创建：从本地 PDF 提取目录与前言，核实全名/作者/出品方/免费声明；建章节地图（11 章 384 页）、四段同步读法、理论对接点表与动手清单；MoE / ml-booklist / understanding-ai-agent / MOC-ai 补回链。
