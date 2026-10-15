---
title: 机器学习书单与 16 周学习计划
tags:
  - ai
  - machine-learning
  - reading-plan
  - booklist
created: 2026-10-15
updated: 2026-10-15
---

# 机器学习书单与 16 周学习计划

> 一份免费正版机器学习教材书单（10 本，其中 6 本出自剑桥大学出版社），外加一条按本库现状排好的阅读路径。
> 目标不是"把书啃完"，而是**给本地的 [《AI Engineering》](ai-engineering-guidebook.pdf) 把理论地基补上**——那本 384 页的工程实践书讲得非常全，但它假设你已经知道"为什么 LoRA 是低秩的""为什么泛化误差可以这么估计"。

**书单来源**：公众号「大宝小密圈」2026-10-11《这 10 本免费机器学习教材，一半出自剑桥大学出版社》<https://mp.weixin.qq.com/s/R-YpfxxgHZPyc8Thk_6P5g>
**链接核验**：2026-10-15 逐条实测，10 个直链全部 HTTP 200 有效。

---

## 一、这份书单与本库已有内容怎么分工

本库的 AI 线目前有 3 块，方向各不相同，先分清楚才不会重复劳动：

| 已有内容 | 性质 | 覆盖 | 缺什么 |
|---|---|---|---|
| [《AI Engineering》(2025, 384p)](ai-engineering-guidebook.pdf) | **工程实践** | LLM 原理与训练 / LoRA·GRPO / RAG / Context Engineering / Agent·ReAct·多智能体 / MCP / 推理优化 / vLLM 部署 / 评测 | **理论根基**——所有"怎么做"都默认你已经知道"为什么" |
| [MoE](MoE.md) | 单点概念 | 混合专家模型的门控、稀疏激活、负载均衡、专家并行 | 与深度学习理论的连接 |
| [深入理解 AI Agent](understanding-ai-agent.md) | **原理层（中文开源）** | Agent = LLM + 上下文 + 工具：上下文工程、工具与 MCP、Coding Agent、评估、持续进化、多 Agent 协作（10 章 + 109 实验） | — 这本补的正是本表想补的那块 |
| [Claude Code](Claude%20Code.md) | 方法论心得 | Agent 编程的任务拆解与多智能体拓扑 | 无（经验帖，不缺理论） |
| [前线部署工程师 FDE](fde-guide.md) | 岗位与价值交付 | AI 时代如何把技术能力转成客户价值 | 与本库无关，属求职线 |

**这份书单补的正是第一块的地基**。而 [数学之美](#并行线--数学之美每周约-1-章) 是中文桥梁，[MML](#工具书--mml不精读查用) 同时服务考研数学。

---

## 二、10 本书清单（含核验与状态）

全部为作者官方放出的免费 PDF，非盗版扫描件。

### 第一组 · 机器学习理论

| # | 书名 | 作者 / 出处 | 一句话 | 链接状态 |
|---|---|---|---|---|
| ① | **Understanding Machine Learning: From Theory to Algorithms**（449p） | Shalev-Shwartz（希伯来）、Ben-David（滑铁卢）· 剑桥大学出版社 | 理论与算法一并覆盖，ML 理论入门的公认首选 | ✅ 已下载 `understanding-machine-learning.pdf` |
| ③ | Mathematical Analysis of ML Algorithms | Tong Zhang（UIUC）· 剑桥大学出版社 | 往数学原理深处钻 | 🔗 有效（研究生级） |
| ④ | **The Principles of Deep Learning Theory**（471p） | Roberts、Yaida、Hanin · 剑桥大学出版社 | 深度学习底层的有效理论 | ✅ 已下载 `principles-of-deep-learning-theory.pdf`（暂缓，见计划） |
| ⑦ | Algorithmic Aspects of Machine Learning | Moitra（MIT）· 剑桥大学出版社 | 算法视角吃透 ML | 🔗 有效 |

### 第二组 · 数学与概率地基

| # | 书名 | 作者 / 出处 | 一句话 | 链接状态 |
|---|---|---|---|---|
| ② | **Mathematics for Machine Learning**（417p） | Deisenroth、Faisal、Ong · 剑桥大学出版社 | 数学功底薄弱的先拿这本补课 | ✅ 已下载 `mathematics-for-machine-learning.pdf` |
| ⑧ | Probability: Theory and Examples | Durrett（杜克） | 概率论的系统训练 | 🔗 有效 |
| ⑨ | Elementary Probability for Applications | Durrett（杜克） | 概率论落到实战 | 🔗 有效 |

### 第三组 · 神经网络与拓展

| # | 书名 | 作者 / 出处 | 一句话 | 链接状态 |
|---|---|---|---|---|
| ⑤ | Machine Learning with Neural Networks | Mehlig（哥德堡大学） | 对神经网络做系统性拆解 | 🔗 有效 |
| ⑥ | Deep Learning on Graphs | Yao Ma 等 · 剑桥大学出版社 | 图神经网络入门 | 🔗 有效 |
| ⑩ | Advanced Data Analysis from an Elementary Point of View | Shalizi（CMU） | 数据科学高阶读物 | 🔗 有效 |

### 直链（全部实测有效）

```
①  https://cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf
②  https://mml-book.github.io/book/mml-book.pdf
③  https://tongzhang-ml.org/lt-book/lt-book.pdf
④  https://arxiv.org/pdf/2106.10165
⑤  https://arxiv.org/pdf/1901.05639
⑥  https://yaoma24.github.io/dlg_book/dlg_book.pdf
⑦  https://people.csail.mit.edu/moitra/docs/bookexv2.pdf
⑧  https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf
⑨  https://sites.math.duke.edu/~rtd/EP4A/EP4A_April2021.pdf
⑩  https://stat.cmu.edu/~cshalizi/ADAfaEPoV/ADAfaEPoV.pdf
```

> 版本会更新，以作者主页为准。链接失效时搜书名进作者主页，永远是第一手的。

---

## 三、为什么不按文章的 ① → ③ → ④ 顺序走

原文建议的主线是 ①UML → ③ → ④。但 **③ 和 ④ 都是研究生级**：

- ④《Principles of Deep Learning Theory》471 页，第 4-5 章的重整化群流（RG Flow）与有效理论，单章就超出「一学期 5-6h/周」的容量
- ③《Mathematical Analysis of ML Algorithms》要求的是相当扎实的实分析基础

原文自己也写了：「第 3、6、7、10 本——那是你**已经开始做研究**之后的事了」。所以本计划调整为：

> **① 打地基 → 数学之美做中文桥梁 → ④ 留作「① 啃完 + 线代概率补齐」之后的深化项**

④ 已经下载，但不排在第一年。先放进书架，读到想要时再开。

---

## 四、16 周计划（每周 5-6 小时）

### 主线 A · Understanding ML（449 页）

按**只读正文 + 挑习题**的节奏，正文约 342 页（Part I-IV），附录 A-C 与 Notes 不精读（查阅用）。

| 周次 | 内容 | 页码 | 本周交付 |
|---|---|---|---|
| **W1** | 摸底：Preface + Introduction（p.7-30）；同时开《AI Engineering》LLMs 段 | UML p.7-30 | 一页笔记：UML 与 AI Engineering 的对照表（哪个概念在哪边） |
| **W2** | Part I ① A Gentle Start → ② A Formal Learning Model | p.33-53 | 原子卡：**学习问题的形式化定义**（训练集/假设类/泛化） |
| **W3** | Part I ③ Learning via Uniform Convergence → ④ Bias-Complexity Tradeoff | p.54-66 | 原子卡：**偏差-复杂度权衡** |
| **W4** | Part I ⑤ The VC-Dimension → ⑥ Nonuniform Learnability | p.67-99 | 原子卡：**VC 维**（重点：它到底在衡量什么） |
| **W5** | Part II ① Linear Predictors → ② Boosting | p.117-143 | 原子卡：**提升法**与集成学习直觉 |
| **W6** | Part II ③ Model Selection and Validation → ④ Convex Learning Problems | p.144-170 | 原子卡：**交叉验证与过拟合** |
| **W7** | Part II ⑤ Regularization and Stability → ⑥ Stochastic Gradient Descent | p.171-201 | 原子卡：**稳定性正则化**（对接 AI Engineering 的 LoRA 直觉） |
| **W8** | Part II ⑦ Support Vector Machines → ⑧ Kernel Methods | p.202-226 | 原子卡：**核方法**（对接《数学之美》第 7 章） |
| **W9** | Part II ⑨ Multiclass, Ranking... → ⑩ Decision Trees | p.227-257 | 原子卡：**决策树与集成** |
| **W10** | Part II ⑪ Nearest Neighbor → ⑫ Neural Networks | p.258-284 | 原子卡：**神经网络的学习理论**（本周开始与 AI Engineering 的 LLM 段对读） |
| **W11** | Part III ① Online Learning | p.287-306 | 原子卡：**在线学习** |
| **W12** | Part III ② Clustering → ③ Dimensionality Reduction | p.307-341 | 原子卡：**聚类**、**PCA 降维**（对接 MML 第 10-11 章） |
| **W13** | Part III ④ Generative Models → ⑤ Feature Selection and Generation | p.342-372 | 原子卡：**生成模型** |
| **W14** | 回读 Part I ⑥ The Runtime of Learning + 整本串线 | p.100-114 | 把 W2-W13 的原子卡织成网，补上遗漏的概念连接 |
| **W15** | 复习：只看自己标的 ★ 章节；对照 Part II 检查能否用自己的话讲清一个算法 | — | 一页「我真正读懂了什么」的清单 |
| **W16** | **决策点**：前置条件（MML Ch2 线代 + Ch6 概率至少读过一遍）是否满足？决定是否开 ④DL Theory | — | 学习复盘，决定下一轮读什么 |

**Part IV（高级理论 p.373-418：Rademacher / Covering Numbers / PAC-Bayes）本轮跳过**，留作深化。其中 PAC-Bayes 最实用（W14 之后若有余力可单独读 p.415 起）。

### 并行线 · 数学之美（每周约 1 章）

《人工智能中的数学之美》[美] Anil Ananthaswamy，中国科学技术出版社 2025 年 10 月，472 页 / 244 千字。中文正文、科普笔法，每章约 30-40 页，1-1.5 小时读完，与主线**不冲突**。

| 周次 | 章节 | 与主线的关系 |
|---|---|---|
| W1-W4 | 第 1-4 章：模式识别的紧迫性 / 全景观测 / 数据深层结构 / **概率论的全视角分析** | **第 4 章直接对接 W3-W4 的均匀收敛与 VC 维** |
| W5-W8 | 第 5-8 章：分类与聚类 / **矩阵运算中的数学机制** / **核函数** / 物理学对数据科学的贡献 | 第 6-7 章对接 W8 的核方法 |
| W9-W12 | 第 9-12 章：**深度学习中的误解与实际情况** / **持久误区的算法修正** / 计算机视觉 / 未知领域的探索 | 第 9-10 章是全书最实用的部分——正好在读完 UML 泛化理论后读，效果最好 |
| W13-W16 | 回读第 9-10 章 + 整理 | 把「误解」与 UML 的严格结论逐条对照 |

### 同步线 · 《AI Engineering》（每周 1.5-2 小时）

按主线进度读对应段落，**不要通读**——它的价值在与主线互证。

| 周次 | 对应段落 | 为什么现在读 |
|---|---|---|
| W1-W4 | p.6-48 · LLMs（What is an LLM / How are LLMs built / Train from scratch / Generation） | 建立"这些东西在理论上对应什么"的地图 |
| W5-W10 | p.49-175 · Prompt / Fine-tuning·LoRA·GRPO / RAG / Context Engineering | W7 的稳定性正则化正好解释 LoRA 为什么有效 |
| W11-W13 | p.176-254 · AI Agents / ReAct / 多智能体 / A2A / AG-UI | 读完 UML 的在线学习与决策树再看 Agent 决策 |
| W14-W16 | p.255-384 · MCP / 推理优化（KV-Cache·压缩）/ 评测 / vLLM | 收尾，把工程面补齐 |

### 工具书 · MML（不精读，查用）

**《Mathematics for Machine Learning》只当查阅手册**，遇到具体数学问题再翻。不排进周计划。

| 遇到什么情况 | 翻哪章 |
|---|---|
| 特征、奇异值、矩阵分解、PCA 的数学 | Ch2 线性代数 p.23 · Ch4 矩阵分解 p.104 |
| 概率分布、期望方差、最大似然 | Ch6 概率与分布 p.178 |
| 梯度下降为什么能work、损失景观 | Ch7 连续优化 p.231 |
| 线性回归推导、SVM 推导 | Ch9 p.295 · Ch12 p.376 |

---

## 五、顺带服务考研数学（数一 44% 的分值）

数一的线代占 22%、概率占 22%。这条线读的不是"额外的 AI 书"，**有一部分正好压在考研的考点上**：

| 本计划中的材料 | 对应数一考点 | 用法 |
|---|---|---|
| MML Ch2 线性代数（p.23-69） | 线性代数 | 换一种视角建立矩阵运算直觉 |
| MML Ch6 概率与分布（p.178-227） | 概率论 | 比同济版更强调分布与统计量的推导 |
| ④DL Theory Ch1.1-1.3 高斯积分·相关统计（p.22-44） | 概率论 | 深度学习里高斯分布的作用 |
| 《数学之美》第 4 章 概率论的全视角分析 | 概率论 | 中文、科普，建立"概率在干什么"的直觉 |

⚠️ **但要说清楚**：考研指定教材是同济版《高等数学》《线性代数》《概率论与数理统计》。上面这些**不能替代同济版的应试训练**——它们的价值是补强直觉和解释「为什么这些工具存在」，不是替代题海和真题。应试主干仍然是 [数学主线](../math/calculus.md) 与同济版教材。

---

## 六、版权提醒

免费 PDF 基本都写明：**仅供个人学习、查看、下载，不得再分发、转售或用于衍生作品**。自己读自己学没问题；别打包上传网盘"分享"。

本库约定：大体积 PDF 就地放在主题目录并 gitignore（`.gitignore` 的 `topics/ai/*.pdf` 规则已覆盖），不进版本库、跨设备靠各自下载。

---

## 相关笔记

- [MOC - ai](../../notes/MOC%20-%20ai.md) —— AI 知识地图
- [MoE](MoE.md) —— 混合专家模型（本计划 ④DL Theory 的深层理论指向这里）
- [Claude Code](Claude%20Code.md) —— Agent 编程心得
- [MOC - math](../../notes/MOC%20-%20math.md) —— 数学主线（考研数一）

## 更新记录

- **2026-10-15** 初始创建：据公众号书单整理 10 本（链接全部实测有效），下载 ①②④ 三本 PDF，结合本库已有的《AI Engineering》排定 16 周计划（每周 5-6h）；记录与考研数一的重合点。
