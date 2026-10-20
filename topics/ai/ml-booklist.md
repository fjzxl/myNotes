---
title: 机器学习书单与完整阅读计划
tags:
  - ai
  - ai/machine-learning
  - ai/reading-plan
  - ai/booklist
---

# 机器学习书单与完整阅读计划

> 一份免费正版机器学习教材书单（13 本，其中 7 本出自剑桥大学出版社），外加一条按本库现状排好的四阶段阅读路径，与逐本开读前的阅读基础自查。
> 目标不是"把书啃完"，而是**给本地的 [《AI Engineering》](ai-engineering-guidebook.pdf) 把理论地基补上**——那本 384 页的工程实践书讲得非常全，但它假设你已经知道"为什么 LoRA 是低秩的""为什么泛化误差可以这么估计"。

**书单来源**：公众号「大宝小密圈」2026-10-11《这 10 本免费机器学习教材，一半出自剑桥大学出版社》<https://mp.weixin.qq.com/s/R-YpfxxgHZPyc8Thk_6P5g>（①-⑩）；2026-10-16 自选增补 ⑪⑫⑬（均为作者官方免费发放）。
**链接核验**：2026-10-15 逐条实测 ①-⑩ 全部 HTTP 200 有效；⑪⑫⑬ 于 2026-10-16 下载时实测有效。

---

## 一、这份书单与本库已有内容怎么分工

本库的 AI 线目前有 3 块，方向各不相同，先分清楚才不会重复劳动：

| 已有内容 | 性质 | 覆盖 | 缺什么 |
|---|---|---|---|
| [《AI Engineering》(2025, 384p)](ai-engineering-guidebook.pdf) · [导读](ai-engineering.md) | **工程实践** | LLM 原理与训练 / LoRA·GRPO / RAG / Context Engineering / Agent·ReAct·多智能体 / MCP / 推理优化 / vLLM 部署 / 评测 | **理论根基**——所有"怎么做"都默认你已经知道"为什么" |
| [MoE](MoE.md) | 单点概念 | 混合专家模型的门控、稀疏激活、负载均衡、专家并行 | 与深度学习理论的连接 |
| [深入理解 AI Agent](understanding-ai-agent.md) | **原理层（中文开源）** | Agent = LLM + 上下文 + 工具：上下文工程、工具与 MCP、Coding Agent、评估、持续进化、多 Agent 协作（10 章 + 109 实验） | — 这本补的正是本表想补的那块 |
| [深入理解 AI Infra](understanding-ai-infra.md) | **系统层（中文开源）** | 加速器架构 · 算子与运行时 · 超节点 · 数据中心网络 · 推理优化 · 分布式推理与训练 · 资源调度 · 端边云（12 章 + 110 实验 + 计算工具） | 不排进三线周程，性能/成本问题时按需回查 |
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
| ③ | Mathematical Analysis of ML Algorithms | Tong Zhang（UIUC）· 剑桥大学出版社 | 往数学原理深处钻 | ✅ 已下载 `mathematical-analysis-of-ml-algorithms.pdf`（研究生级） |
| ④ | **The Principles of Deep Learning Theory**（471p） | Roberts、Yaida、Hanin · 剑桥大学出版社 | 深度学习底层的有效理论 | ✅ 已下载 `principles-of-deep-learning-theory.pdf`（暂缓，见计划） |
| ⑦ | Algorithmic Aspects of Machine Learning | Moitra（MIT）· 剑桥大学出版社 | 算法视角吃透 ML | ✅ 已下载 `algorithmic-aspects-of-machine-learning.pdf` |

### 第二组 · 数学与概率地基

| # | 书名 | 作者 / 出处 | 一句话 | 链接状态 |
|---|---|---|---|---|
| ② | **Mathematics for Machine Learning**（417p） | Deisenroth、Faisal、Ong · 剑桥大学出版社 | 数学功底薄弱的先拿这本补课 | ✅ 已下载 `mathematics-for-machine-learning.pdf` |
| ⑧ | Probability: Theory and Examples | Durrett（杜克） | 概率论的系统训练 | ✅ 已下载 `probability-theory-and-examples.pdf` |
| ⑨ | Elementary Probability for Applications | Durrett（杜克） | 概率论落到实战 | ✅ 已下载 `elementary-probability-for-applications.pdf` |

### 第三组 · 神经网络与拓展

| # | 书名 | 作者 / 出处 | 一句话 | 链接状态 |
|---|---|---|---|---|
| ⑤ | Machine Learning with Neural Networks | Mehlig（哥德堡大学） | 对神经网络做系统性拆解 | ✅ 已下载 `machine-learning-with-neural-networks.pdf` |
| ⑥ | Deep Learning on Graphs | Yao Ma 等 · 剑桥大学出版社 | 图神经网络入门 | ✅ 已下载 `deep-learning-on-graphs.pdf` |
| ⑩ | Advanced Data Analysis from an Elementary Point of View | Shalizi（CMU） | 数据科学高阶读物 | ✅ 已下载 `advanced-data-analysis.pdf` |

### 第四组 · 增补（2026-10-16，自选三本）

| # | 书名 | 作者 / 出处 | 一句话 | 链接状态 |
|---|---|---|---|---|
| ⑪ | **Understanding Deep Learning**（541p，19 章） | Prince · MIT Press，官网免费 PDF | 深度学习的现代图解教材——④ 的平缓前置，配图与直觉在同类书里最好 | ✅ 已下载 `understanding-deep-learning.pdf`（v5.0.3，2026-02-09） |
| ⑫ | **《动手学深度学习》d2l-zh**（797p，16 章，PyTorch 版） | Aston Zhang、Lipton、李沐、Smola · 剑桥大学出版社 2023 | 每小节都是可运行 notebook 的中文动手教材，理论线的代码伴读 | ✅ 已下载 `dive-into-deep-learning-zh-pytorch.pdf` |
| ⑬ | **Speech and Language Processing 3rd ed. 草稿**（646p） | Jurafsky（斯坦福）、Martin（科罗拉多博尔德） | NLP/LLM 理论标准教材，第 3 版已重构为 LLM 优先（Vol I 前 8 章即 LLM 主线） | ✅ 已下载 `speech-and-language-processing.pdf`（2026-08 完整版） |

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
⑪  https://github.com/udlbook/udlbook/releases/download/v5.0.3/UnderstandingDeepLearning_02_09_26_C.pdf   （官网 https://udlbook.github.io/udlbook/）
⑫  https://zh-v2.d2l.ai/d2l-zh-pytorch.pdf   （官网 https://zh.d2l.ai/）
⑬  https://web.stanford.edu/~jurafsky/slp3/ed3book_aug26.pdf   （官网 https://web.stanford.edu/~jurafsky/slp3/）
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

按**只读正文 + 挑习题**的节奏，正文约 342 页（Part I-IV），附录 A-C 与 Notes 不精读（查阅用）。每周原子卡已预建骨架（W2-W13 共 13 张，`notes/` 下，清单见 [MOC - ai](../../notes/MOC%20-%20ai.md) 学习路线区）——读到哪周填哪张，填完删掉骨架标记行。

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
| **W16** | **决策点**：前置条件（MML Ch2 线代 + Ch6 概率至少读过一遍）是否满足？按第五节「完整路线」决定下一步（默认进入阶段二，④ 的开读点后移到阶段三） | — | 学习复盘，决定下一轮读什么 |

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

## 五、完整路线：16 周之后怎么走（阶段二 → 四）

上文 16 周计划即十三本书中的**阶段一**。十三本书按「现在读得动」的先后排成四个阶段，每个阶段都有进入条件（不满足就先补条件）与退出产出（没有产出就重读，不往前赶）：

| 阶段 | 时长 | 精读 | 伴读 / 查阅 | 进入条件 | 退出产出 |
|---|---|---|---|---|---|
| **一 · 理论地基**（上文 16 周） | 16 周 | ① UML 正文 | 《数学之美》并行 + 《AI Engineering》同步 + ② MML 查阅 | 考研三门数学的基本运算；敢读英文数学教材 | 12+ 张原子卡；W16 决策点 |
| **二 · 概率与网络补强** | 8-10 周 | ⑨ EP4A 全 6 章快过（2-3 周）→ ⑤ Mehlig Part II（6-8 周，与 ⑨ 收尾重叠） | ② MML Ch6/Ch7 按需查 + ⑫ 同题跑代码 | ① Part I-II 读完 | 概率直觉补瓷实（顺带服务考研）；SGD / 反向传播 / 深度网络原子卡 |
| **三 · 深度学习理论** | 12-16 周 | ④ PDLT 精读 Ch1-3、选读 Ch4-5（RG Flow 与有效理论） | ⑧ PTE 当字典 + ⑪ UDL 图解垫脚 | ① 读完 + 谱理论（② Ch2/Ch4）与高斯分布运算过关 | 参数分布 / 有效理论原子卡，对接 [MoE](MoE.md) |
| **四 · 问题驱动** | 开放 | ③⑦⑥⑩⑬ 按需选读（见下） | ③ 配 ⑧ 的测度论概率 | 已开始做研究，或工作压到具体问题 | 按专题产出 |

几个关键选择（章节结构均已对照下载的 PDF 目录核实）：

- **阶段二先 ⑨ 后 ⑤**：⑨ 只有 6 章（组合概率 → 独立性 → 分布 → 极限定理 → 条件概率 → 马尔可夫链），应用向、篇幅轻，2-3 周快过正好把 ① 里「以概率至少 1-δ」的直觉补瓷实，还直接压在考研概率的考感上。⑤ 只精读 Part II（感知机 → SGD → 深度网络 → 卷积 → 循环网络）；Part I 的 Hopfield / Boltzmann 机器物理味重，与 ④ 的统计物理方法同源，留到阶段三前后回头看。
- **阶段三才开 ④**：即第三节说的「① 啃完 + 线代概率补齐」——阶段二就是那个「补齐」。⑧ 是测度论概率的标准教材（Ch1 从测度讲起，Ch3 特征函数与中心极限定理、Ch4 鞅），本阶段**不通读**，只在 ④ 卡在高斯积分 / 收敛 / 集中不等式时按章回查；④ 的物理记号与推导卡住时，去 ⑪ 找同一概念的图解版（Ch4 深度网络、Ch7 梯度与初始化、Ch9 正则化、Ch12 Transformer）。
- **⑫ 是贯穿性的动手线**：理论线读到哪章，⑫ 就跑哪章的 notebook——⑤ Part II 对应 ⑫ Ch4（MLP）与 Ch11（优化算法），④ 对应 Ch12 前后的注意力内容，考研三门对应 Ch2 预备知识的另一套讲法。中文正文 + 代码仓 Apache-2.0，是全单唯一「读中文 + 动手」的书。
- **阶段四是问题驱动，不是书驱动**：
  - **③ lt-book**：从概率不等式（Ch2：Markov → Hoeffding → Bernstein）与一致收敛（Ch3：empirical process、covering number）讲起，相当于 ① Part IV 的数学加强版。做到需要 Rademacher / covering 工具时按章读，前置是实分析。
  - **⑦ Moitra**：专题手册——NMF、张量分解、稀疏恢复、稀疏编码、GMM、矩阵补全，SVD 是贯穿工具。遇到对应专题读对应章。
  - **⑥ DLG**：应用线。前置是深度学习实践（《AI Engineering》+ ⑤ Part II），核心是 Part Two 的 Ch5 GNN，书配代码（PyTorch/DGL），选读 + 跑代码。
  - **⑩ ADA**：统计思维线，24 章：回归 → 模拟 / Bootstrap → 树 / PCA → 因果推断四连章（Ch19-22）→ 时间序列，R 语言。与前三个阶段互不依赖，想换脑子时可独立平行开一条。
  - **⑬ SLP3**：NLP/LLM 理论线。第 3 版已重构为 LLM 优先——Vol I 前 8 章（词与 token → n-gram → 逻辑回归 → embedding → 神经网络 → Transformer 与预训练 → post-training）就是 LLM 主线，做 LLM 应用或想深挖 [AI Engineering 导读](ai-engineering.md) p.6-48 背后原理时按章查。草稿无正式许可条款（作者明言欢迎课堂使用与自行打印），个人查阅、不再分发。
- **与考研错峰**：本线预算每周 5-6h；考研冲刺期（考前 2-3 个月）降到 ≤2h，只保留 ② MML 查阅——理论线永远不给应试主干让位，但也别反过来挤占它。

---

## 六、阅读基础自查（每本开读前的最低线）

十三本书的语言、工具、数学台阶差异很大。先对齐三个公共维度，再逐本自查：

- **数学台阶**：L0 = 考研三门（同济高数 / 线代 / 概率）的基本运算级 → L1 = 数学成熟度（能读定义-定理-证明、会放缩与归纳）→ L2 = 实分析（测度、Lebesgue 积分）→ L3 = 研究生级专题。
- **语言**：除《数学之美》外全是英文教材。① 的前几章本身就是「英文数学教材怎么读」的训练场——不是「英文好了再开 ①」，而是反过来。
- **工具**：⑥ 要 PyTorch/DGL，⑩ 要 R，② 做配套练习需 Python，⑫ 要 Python/PyTorch（每节即 notebook）；其余纸笔够用。

| 书 | 台阶 | 最低基础 | 自查（能做到再开） |
|---|---|---|---|
| ① UML | L1 | 考研三门基本运算 + 组合计数 | 用 Markov 不等式证出 Chebyshev；看懂「以概率至少 1-δ」在说什么 |
| ② MML | L0 | 微积分入门 | 链式法则、矩阵乘法、全概率展开各默写一遍 |
| ③ lt-book | L2 | 实分析 + ① 的 PAC / VC 框架 | 能陈述控制收敛定理；会推条件期望的塔式法则 |
| ④ PDLT | L1+ | 特征值 / SVD、矩阵微积分、高斯分布运算 | 算出多元高斯的边缘 / 条件分布；Taylor 展开到二阶 |
| ⑤ Mehlig | L1 | 高数（含一阶 ODE）+ 线代 | 会解 x' = −∇E 型最速下降 ODE；知道梯度下降是它的离散化 |
| ⑥ DLG | L1 + 工程 | 监督学习全流程 + PyTorch | 独立写过一个训练循环；手推过 MLP 的反向传播 |
| ⑦ Moitra | L1+ + 算法课 | 本科算法（复杂度、随机化）+ SVD | 手推过 SVD；分析过一个随机算法的期望复杂度 |
| ⑧ PTE | L2 | 实分析（或接受在它的 Ch1 现场学测度论） | 说得出测度、可测函数、Lebesgue 积分的定义 |
| ⑨ EP4A | L0 | 高数（积分、级数） | 二重积分换序；e^x 的幂级数展开 |
| ⑩ ADA | L1 + 统计入门 | 微积分 + 线代 + 入门统计（+ R） | 写出 OLS 公式 β = (XᵀX)⁻¹Xᵀy 并说出几何意义 |
| ⑪ UDL | L1 | 线代 + 基本概率 | 会算矩阵函数的雅可比；说得出贝叶斯定理与 MLE 的关系 |
| ⑫ d2l-zh | L0 + Python | Python 与张量运算基础 | 装好环境，跑通第 2 章任意一个 notebook |
| ⑬ SLP3 | L1 | 条件概率 / MLE + 基础线代 | 会推导 n-gram 加一平滑的概率公式 |

一句话版：**L0 就能开 ⑨①②⑤⑫（① 顺带练英文数学阅读，⑫ 全中文还带代码）；⑥⑩ 各加一块工程 / 统计基础；⑪⑬ 要线代与概率顺手；④⑦ 要谱理论啃得动；③⑧ 才真正吃实分析。** 台阶不是硬门槛，是「读得动 vs 读不动」的分界——卡在台阶上时，回 ② MML 或同济版补对应章，比硬啃划算。

---

## 七、顺带服务考研数学（数一 44% 的分值）

数一的线代占 22%、概率占 22%。这条线读的不是"额外的 AI 书"，**有一部分正好压在考研的考点上**：

| 本计划中的材料 | 对应数一考点 | 用法 |
|---|---|---|
| MML Ch2 线性代数（p.23-69） | 线性代数 | 换一种视角建立矩阵运算直觉 |
| MML Ch6 概率与分布（p.178-227） | 概率论 | 比同济版更强调分布与统计量的推导 |
| ④DL Theory Ch1.1-1.3 高斯积分·相关统计（p.22-44） | 概率论 | 深度学习里高斯分布的作用 |
| 《数学之美》第 4 章 概率论的全视角分析 | 概率论 | 中文、科普，建立"概率在干什么"的直觉 |

⚠️ **但要说清楚**：考研指定教材是同济版《高等数学》《线性代数》《概率论与数理统计》。上面这些**不能替代同济版的应试训练**——它们的价值是补强直觉和解释「为什么这些工具存在」，不是替代题海和真题。应试主干仍然是 [数学主线](../math/calculus.md) 与同济版教材。

---

## 八、版权提醒

免费 PDF 基本都写明：**仅供个人学习、查看、下载，不得再分发、转售或用于衍生作品**。自己读自己学没问题；别打包上传网盘"分享"。

本库约定：大体积 PDF 就地放在主题目录并 gitignore（`.gitignore` 的 `topics/ai/*.pdf` 规则已覆盖），不进版本库、跨设备靠各自下载。

---

## 相关笔记

- [MOC - ai](../../notes/MOC%20-%20ai.md) —— AI 知识地图
- [AI Engineering 导读](ai-engineering.md) —— 同步线那本工程书的章节地图、四段读法与理论对接点
- [MoE](MoE.md) —— 混合专家模型（本计划 ④DL Theory 的深层理论指向这里）
- [Claude Code](Claude%20Code.md) —— Agent 编程心得
- [MOC - math](../../notes/MOC%20-%20math.md) —— 数学主线（考研数一）

## 更新记录

- **2026-10-15** 初始创建：据公众号书单整理 10 本（链接全部实测有效），下载 ①②④ 三本 PDF，结合本库已有的《AI Engineering》排定 16 周计划（每周 5-6h）；记录与考研数一的重合点。
- **2026-10-16** 补齐剩余 7 本（③⑤⑥⑦⑧⑨⑩）PDF 下载，10 本全部就位（文件名沿用 kebab-case）；新增「完整路线」（四阶段：二 = ⑨ 快过 + ⑤ Part II，三 = ④ 精读、⑧ 当字典，四 = ③⑦⑥⑩ 问题驱动选读）与「阅读基础自查」（逐本数学台阶 L0-L2 + 自查题）两节，章节结构均对照 PDF 目录核实；标题改为「完整阅读计划」，原第五/六节重编号为七/八，README / MOC-ai / fde-guide / understanding-ai-agent 的链接文字同步。
- **2026-10-16** 新增《AI Engineering》导读笔记 [ai-engineering.md](ai-engineering.md)（章节地图、四段同步读法、理论对接点、动手清单），分工表与相关笔记补链接。
- **2026-10-16** 书单扩充 10 → 13 本：增补并下载 ⑪ UDL（v5.0.3，541p，MIT Press 官方免费）⑫《动手学深度学习》d2l-zh PyTorch 版（797p，剑桥 2023）⑬ SLP3 草稿（646p，2026-08 完整版，LLM 优先结构）；排入计划——⑪ 作阶段三 ④ 的图解垫脚、⑫ 为贯穿阶段二/三的动手线、⑬ 入阶段四按章查阅；直链、阅读基础自查表与工具清单同步更新。
- **2026-10-18** 分工表新增《深入理解 AI Infra》（系统层，姊妹篇索引 [understanding-ai-infra.md](understanding-ai-infra.md)，中文 PDF 已入库）：不排固定周程，作按需回查的系统层参考。
