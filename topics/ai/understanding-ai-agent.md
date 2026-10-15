---
title: 深入理解 AI Agent（李博杰）· 开源书索引
tags:
  - ai
  - agent
  - mcp
  - book
  - reading-plan
created: 2026-10-15
updated: 2026-10-15
---

# 深入理解 AI Agent：设计原理与工程实践

> 开源免费书，Apache-2.0，**本地 PDF**：[understanding-ai-agent-zh-cn.pdf](understanding-ai-agent-zh-cn.pdf)
> 仓库：<https://github.com/bojieli/ai-agent-book>（54.4k star / 6.2k fork）
> 在线阅读：<https://bojieli.github.io/ai-agent-book/astro/> ｜ 作者：李博杰（GitHub: bojieli）

**核心公式：Agent = LLM + 上下文 + 工具**

作者的第一判断是：真正拉开差距的不是模型本身，而是 **Harness 工程**——把「LLM 是大脑、上下文是它记得什么、工具是它能做什么」这三块组织起来的那一层。这与 [Claude Code](Claude%20Code.md) 那篇心得是同一个判断。

---

## 一、为什么收进本库

本库 AI 线目前是「工程书 + 两个单点」的结构：本地 [《AI Engineering》](ai-engineering-guidebook.pdf) 讲工程实践、[MoE](MoE.md) 讲一个架构、[Claude Code](Claude%20Code.md) 讲方法论。**缺的是「Agent 这套东西到底是什么、从哪来」的原理层**——而这本书正好是中文、免费、Apache-2.0、且配 109 个可运行实验。

前置要求很友好：能读懂中等复杂度的 Python、用过 LLM 产品、熟悉一款 AI 辅助编程工具。**除第 8 章后训练外，全书对数学和机器学习要求很低**——这一点对本库当前以考研数学为主线的处境很关键。

---

## 二、十章速览

| 章 | 主题 | 核心 | 实验 |
|:--:|---|---|:--:|
| 1 | 🚀 AI Agent 入门 | Agent = LLM + 上下文 + 工具；Harness 工程才是竞争力 | 4 |
| 2 | 🎯 上下文工程 | 上下文决定能力上限：KV Cache、提示工程、**Agent Skills**、上下文压缩 | 10 |
| 3 | 📚 用户记忆和知识库 | 跨会话记住用户、接入外部知识：用户记忆、RAG、结构化索引、知识图谱 | 12 |
| 4 | 🛠️ 工具 | 工具是 Agent 的双手：**MCP 协议**、感知/执行/协作三类工具、主动工具发现 | 5 |
| 5 | 💻 Coding Agent 与通用 Agent | 代码是「能创造新工具的工具」，生产级 Coding Agent 全景 | 16 |
| 6 | 🎙️ 交互：观察与动作空间的扩展 | 异步与事件驱动、语音交互、Computer Use、机器人操作 | 14 |
| 7 | 🎯 Agent 的评估 | 把表现变成可比较信号：评估环境、指标、统计显著性 | 14 |
| 8 | 🧠 模型后训练 | 预训练 / SFT / RL 三阶段：何时选 SFT、何时选 RL | 19 |
| 9 | 🔄 Agent 的持续进化 | 从运行轨迹获得学习信号，更新知识、指令、程序与参数 | 9 |
| 10 | 🤝 多 Agent 协作 | 协作框架、上下文共享/隔离、涌现的「Agent 社会」 | 6 |

> **版本提示**：书稿已从 1.4 升到 **2.0**。2.0 把原第四章的「异步交互」与原第九章的「多模态 Agent」合并重组为新第六章，原第 6/7/8 章顺延为 7/8/9 章。网上流传的旧 PDF 结构会与上表对不上——本地这份是 `latest` 直链拉下来的最新版。

配套 **109 个实验**（含本地项目与外部复现轨道），支持 Python 3.11–3.13，用 `uv` 管理环境。第 6、7、8、10 章另有 22 个外部仓库**未内置**（出于体积与版权），需按附录说明自行克隆。

另有姊妹篇《深入理解 AI Infra》：<https://github.com/bojieli/ai-infra-book>

---

## 三、与本库已有内容的分工

| 本库笔记 | 对应本书 | 关系 |
|---|---|---|
| [Claude Code](Claude%20Code.md) | 第 5 章 Coding Agent + 第 2 章 Agent Skills | **强互补**——本库那篇讲「怎么拆解任务、怎么组织多智能体」的实战心得，这本书第 5 章讲「生产级 Coding Agent 的完整架构」；第 2 章的 Skills 概念正好解释本库 `foam.code-snippets` 那套片段机制在 Agent 语境下是什么 |
| [《AI Engineering》](ai-engineering-guidebook.pdf) | 第 2 / 4 / 7 章 | **部分重叠**——两本都讲 MCP 与 Agent 评估。本书更偏「为什么这样设计」，AI Engineering 更偏「怎么用 vLLM / LitServe 部署」 |
| [MoE](MoE.md) | 第 3 章（模型后处理视角） | 这本从**分布式系统**讲 MoE（专家并行、All-to-All 通信），与本库那篇的**模型架构**视角互补 |
| [ml-booklist](ml-booklist.md) 的同步线 | 全书 | 理论层读 UML，工程层读 AI Engineering，**原理层读这本**——三本正好补齐 ML 理论的三个缺口 |

---

## 四、怎么读

**最省力的路径**（作者在 [LEARNING.md](https://github.com/bojieli/ai-agent-book/blob/main/docs/zh-CN/LEARNING.md) 给了完整建议，这里是压缩版）：

1. **第 1 章**先建框架（半章，1 小时）
2. **第 2 章上下文工程 + 第 4 章工具**——这两章是全书的两条工程主线，上下文决定它「记得什么」，工具决定它「能干什么」
3. 再回头看第 3 章记忆与知识库、第 5 章 Coding Agent
4. 第 7 章评估、第 9 章持续进化——**这两章是让 Agent 从「能跑」变成「可靠」的关键**
5. 第 6、8、10 章（交互 / 后训练 / 多 Agent）按需，属于前沿与拓展

**不要只读正文**。作者的强调：读懂设计原则后，用 coding agent 从头实现一遍，观察输出、排查不符合预期的地方；每章末尾有思考题（[参考答案](https://github.com/bojieli/ai-agent-book/blob/main/book/reference-answers.md)）。

**配套代码不必逐行读**——全部由 coding agent 生成，作者自己也不逐行看。关键是把架构、核心组件和设计原则想清楚。

**落地项目建议**（作者给出）：第 1–5 章足以做出一个可用的 coding agent；第 7、9 章帮它建评估集并从失败案例持续改进；第 8 章介入模型本身；第 6、10 章加语音、Computer Use 与多 Agent 协作。

---

## 相关笔记

- [MOC - ai](../../notes/MOC%20-%20ai.md) —— AI 知识地图
- [Claude Code](Claude%20Code.md) —— Agent 编程心得
- [机器学习书单与 16 周学习计划](ml-booklist.md) —— 理论书单与阅读路径
- [MoE](MoE.md) —— 混合专家模型
- [前线部署工程师（FDE）· 索引](fde-guide.md) —— 同属 AI 线，但讲的是岗位与职业路径

## 更新记录

- **2026-10-15** 初始创建：收录 v2.0 版（10 章 / 109 实验 / Apache-2.0），下载中文 PDF 到本地，与 Claude Code、AI Engineering、MoE 三篇建立分工与交叉引用。
