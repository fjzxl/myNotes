---
title: "笔记编撰计划 · 高等数学 + 前端 + 软考架构师（2026-10 ~ 2027-07）"
tags:
  - project
  - plan
  - math
  - programming
  - exams
status: active
created: 2026-10-01
updated: 2026-10-02
deadline: 2027-07-04
---

# 📝 笔记编撰计划 · 高等数学 + 前端 + 软考架构师（2026-10 ~ 2027-07）

> **39 周（2026-10-05 ~ 2027-07-04）三线推进**：数学（高数总览 + 45 个专题 + 2 份真题复盘）、前端（21 篇，求职动作后置到 6 月）、软考系统架构设计师（**2027-05 下旬考试**，大纲详见 [[topics/exams/ruankao/system-architect]]）。每周总量维持约 16 小时、按阶段在三线间重新分配：软考冲刺期（2027-03 ～ 05）软考升至约 7h、数学降速转短稿、前端仅隔周轻量；考后 6 月数学恢复主攻并启动线代，前端完成求职项目。考研路线延伸至预计的 2027-12 考期。
> 相关索引：[[notes/MOC - math]] · [[notes/MOC - programming]] · [[notes/MOC - exams]]

## 项目目标

- **高等数学**：按考研数一大纲完成 8 大章首轮学习，形成 `topics/math/calculus.md` 总览 + 45 个专题笔记 + 2 份限时真题复盘，衔接已有的 [[topics/math/inequalities]]。Ch1–Ch4 保持长文标准；2027-03 起的新单元按短稿推进（见「节奏与写作约定」）。首轮覆盖不等于考研数学全部完成；2027 年 6 月中起继续线代、概率与综合复习。
- **前端求职**：在现有 HTML/CSS/JS/TS 基础上（[[topics/programming/Web/javascript]]、[[topics/programming/Web/css]]、TypeScript 系列）以 **Vue 3 + TypeScript 为主线**——TS 从已有基础系列走向框架集成实战（新增 `vue-integration`），React 做求职所需的对照入门，工程化围绕一个可部署的 Vue 项目展开。**求职动作（项目 MVP、作品讲解、模拟面试）后置到 2027-06**，为软考冲刺让路；学习线不停，React 对照与工程化笔记按余力取舍。
- **软考架构师**：三科一次通过（目标 **2027-05 下旬**考试）。执行细节以 [[topics/exams/ruankao/system-architect]] 为单一事实源——基础期过教程、攒两份项目素材卡，强化期 4 套综合真题与案例五大题型，冲刺期每周 1 篇限时论文（累计 12–16 篇）；本计划只负责把里程碑嵌入每周节奏。

## 范围

### ✅ In scope

- 2026-10 至 2027-07：高等数学 8 章首轮笔记与练习（3 月起短稿化）；Vue 3 主线、TypeScript 框架集成实战、React 对照入门、工程化（隔周轻量、可顺延）；6 月集中完成 Vue 求职项目与面试材料
- 软考三科：基础期教程精读与两份项目素材卡；强化期 4 套综合真题与案例五大题型；冲刺期每周 1 篇限时论文；2027-03 中下旬完成报名
- 2027-06 中至预计考期：线性代数、概率论与数理统计首轮学习；三科综合复习、分章节真题与限时套卷
- 每写完一章同步更新对应 MOC 并跑 `python scripts/check_notes.py`

### ❌ Out of scope（留给下一阶段）

- 软考论文历年题目全覆盖与整本模拟卷（覆盖 5 个方向即可，题库以真题为限）
- 2027-07 前系统编写线性代数、概率论与数理统计专题笔记（6 月后列学习/复习路线，是否扩展成完整长文按备考进度决定）
- 2027-07 前刷完全部 2010-2026 真题（前期做典型题，整卷与成体系复盘放到后续阶段）
- HTML 语义化 / HTTP 网络基础的独立长篇教程（项目实作仍需掌握必要语义标签、HTTP 方法/状态码与 CORS）
- 数据结构与算法笔记

## 节奏与写作约定

- **时间预算（三线分配，总量维持约 16h/周）**：W1–W4 爬坡 6h（数学 3 / 前端 2 / 软考 1）；W5–W22 常态 16h（数学 6 / 前端 4 / 软考 4 / 缓冲 2）；W23–W34 软考冲刺 16h（软考 7 / 数学 4.5 / 前端 1.5 / 缓冲 2）；W35–W39 考后 16h（数学 10 / 前端 5 / 缓冲 1）。每四周检查一次实际耗时与掌握情况，落后时按「风险 & 调整规则」降级。
- **启动期产出**：前 4 周按「数学 1 个单元 + 前端 1 个单元 + 软考教程 1 个域」爬坡，不按长文计产量；较难内容顺延，不通过压缩做题或不核对代码来赶进度。
- **数学短稿约定**：W23（2027-03）起数学新单元一律按短稿标准执行——要点 + 已核对例题 + 易错点，不做长证明展开；Ch1–Ch4 保持长文。二轮复习时再按需深化成文。
- **笔记体量**：取消固定行数目标。按问题复杂度决定长度：目录/索引只保留导航，普通专题以“理解所需的最少解释 + 已核对例题 + 易错点”为准；证明与应用繁多的主题再展开。行数不作为完成标准。
- **数学章节统一结构**：考纲定位（以当年大纲为准）→ 概念与定义 → 定理及证明思路 → 典型例题（至少自行演算核对）→ 易错点与做题套路 → 前后章节/不等式专题互链；另留闭卷回忆与错题复测时间。短稿保留同一骨架，压缩证明与应用篇幅。
- **前端章节统一结构**：与 `css.md` / `javascript.md` 章节相同——导航头（上一章/下一章 wikilink）→ 目标 → 正文（代码示例可运行）→ 小结与自测。
- **软考论文练习**：每篇用 [[templates/practice-log]] 记录限时表现与改进点；素材卡、骨架与真题矩阵见 [[topics/exams/ruankao/system-architect]]，不在本计划重复维护。
- **文件命名**：英文 kebab-case；数学放 `topics/math/calculus/`，前端放 `topics/programming/Web/vue|react|engineering/`（TS 笔记沿用已有 `topics/programming/Web/typescript/`，不加数字前缀）。
- **互链与收尾**：新笔记加入对应 MOC；数学章节在 [[notes/MOC - math]] 的章节清单勾选；每周末跑校验脚本。
- **插图**（如需要）放 `attachments/images/math/calculus/` 或 `attachments/images/programming/<topic>/`。

## 路线一：高等数学（总览 1 + 专题笔记 45 + 真题复盘 2）

> W23 起 Ch5–Ch8 及专题页按短稿标准执行（见「节奏与写作约定」），确保软考冲刺期数学推进不中断；长文标准仅保留给 Ch1–Ch4。

### 第一部分 · 一元函数微积分（总览 + 22 个专题页）

总览页 + 四章专题页。为控制切换成本，将数列极限与函数极限合写、无穷小与连续性合写；如学习中发现内容过长，再拆成互链子页。

- `topics/math/calculus.md` —— 总览：学习路线、章节导航、考纲权重
- **Ch1 函数、极限、连续**
  - `01-functions` 函数概念与性质（有界/单调/奇偶/周期、初等函数）
  - `02-03-sequence-function-limits` 数列与函数极限（定义、夹逼、单调有界、两个重要极限）
  - `04-05-infinitesimal-continuity` 无穷小/无穷大、等价替换、连续与间断点、闭区间连续函数性质
  - `06-limit-techniques` 极限计算方法综合（题型汇总）
- **Ch2 一元函数微分学**
  - `07-derivative` 导数概念与求导法则
  - `08-differential-higher-order` 微分、复合/隐函数/参数方程求导、高阶导数
  - `09-mean-value-theorems` 中值定理（罗尔/拉格朗日/柯西）
  - `10-taylor-formula` 泰勒公式与常用展开
  - `11-lhopital` 洛必达法则与未定式
  - `12-monotonicity-extrema` 单调性、极值与最值
  - `13-concavity-asymptote` 凹凸性、拐点、渐近线与函数作图
  - `14-derivative-applications` 导数综合应用（不等式证明、方程根讨论）
- **Ch3 一元函数积分学**
  - `15-indefinite-integral` 不定积分概念与基本积分表
  - `16-substitution` 换元积分法（第一/第二类）
  - `17-parts-rational` 分部积分与有理函数积分
  - `18-definite-integral` 定积分、变限积分与 N-L 公式
  - `19-improper-integral` 反常积分判敛与计算
  - `20-integral-applications` 定积分应用（面积/旋转体/弧长/物理）
- **Ch4 常微分方程**
  - `21-first-order-ode` 一阶方程（可分离/齐次/一阶线性/伯努利）
  - `22-reducible-ode` 可降阶方程、线性方程解的结构、欧拉方程
  - `23-second-order-ode` 二阶常系数线性方程（齐次+非齐次）
  - `24-ode-applications` 微分方程综合与应用

### 第二部分 · 多元微积分与级数（20 个原始主题合并为 19 个专题页）

- **Ch5 向量代数与空间解析几何（数一特有）**
  - `25-vectors` 向量代数（数量积/向量积/混合积）
  - `26-planes-and-lines` 平面与直线方程及位置关系
  - `27-surfaces-curves` 曲面（旋转面/柱面/二次曲面）与空间曲线
- **Ch6 多元函数微分学**
  - `28-multivariable-limit` 多元函数极限与连续
  - `29-partial-derivative` 偏导数与全微分
  - `30-chain-and-implicit` 复合函数与隐函数求导
  - `31-directional-derivative` 方向导数、梯度与几何应用（切平面/法线）
  - `32-multivariable-extrema` 多元极值、条件极值与拉格朗日乘数法
- **Ch7 多元函数积分学**
  - `33-double-integral` 二重积分（直角/极坐标、交换次序）
  - `34-triple-integral` 三重积分（投影/截面/球面坐标）
  - `35-line-integral-1` 第一类曲线积分
  - `36-line-integral-2` 第二类曲线积分与格林公式
  - `37-surface-integral-1` 第一类曲面积分
  - `38-surface-integral-2` 第二类曲面积分、高斯与斯托克斯公式
- **Ch8 无穷级数**
  - `39-40-series-concepts-positive-tests` 常数项级数概念、性质与正项级数判别法
  - `41-alternating-series` 交错级数、绝对/条件收敛
  - `42-power-series` 幂级数与和函数
  - `43-taylor-series` 函数展开为幂级数
  - `44-fourier-series` 傅里叶级数（数一）

### 第三部分 · 专题与真题启动（考后 W35–W38，做题为主）

- `45-mvt-proof-special` 中值定理证明题专题
- `46-integral-inequality` 积分不等式与积分综合题（衔接 [[topics/math/inequalities]]）
- `47-series-summation` 级数求和与敛散综合
- `48-synthetic-problems` 多元微积分综合（或按错题情况改为机动）
- 真题复盘 ①②（从 2010–2013 年卷中选两套，用 [[templates/practice-log|练习记录模板]] 记录限时表现与错题复测）

## 路线二：前端求职能力（21 篇笔记 + 项目里程碑）

### Vue 3 主线（9 篇，W2–W11）

- `topics/programming/Web/vue.md` —— 总览：学习路线与章节导航
- `01-vue-essentials` 核心概念、SFC 与模板语法
- `02-composition-api` 组合式 API（setup/ref/reactive/computed/watch）
- `03-components-basics` 组件基础（props/emit/slot/生命周期）
- `04-components-advanced` 组件进阶（provide/inject、Teleport、Suspense、自定义指令）
- `05-reactivity-system` 响应式系统原理（Proxy、effect、依赖收集）
- `06-vue-router` Vue Router 4（路由、守卫、懒加载）
- `07-pinia` Pinia 状态管理
- `08-vue-engineering` 工程实战（项目结构、性能优化、常见面试题）

### React 对照线（4 篇，W14–W17：建立可迁移认知，不重复完整学习 Vue 全家桶）

- `topics/programming/Web/react.md` —— 总览
- `01-react-mental-model` React 入门、JSX、组件与渲染模型
- `02-react-state-hooks` props/state、事件与核心 Hooks（对照 Vue Composition API）
- `03-react-ecosystem-comparison` React Router 与状态管理生态（对照 Vue Router/Pinia），同步标注 TS 类型写法，与 `typescript/vue-integration` 互链

### TypeScript 实战（已有 3 篇查漏 + 新增 1 篇，W2 查漏 / W20 新增）

已有基础系列不重写，动笔 Vue 前回看查漏即可；真正的缺口是"框架中的 TS"，新增一篇实战收口：

- [[topics/programming/Web/typescript/intro]] —— 入门与工程实践（已有）
- [[topics/programming/Web/typescript/interface]] —— 接口契约（已有）
- [[topics/programming/Web/typescript/type-system]] —— 类型系统进阶（已有）
- `topics/programming/Web/typescript/vue-integration` —— TS × Vue 3 实战（新增，W20）：`defineProps`/`defineEmits` 泛型参数、泛型组件、SFC 类型推导与 vue-tsc、tsconfig 实用项、常用工具类型（Partial/Pick/Omit/Record 等）在组件与组合式函数中的运用；产出物直接作为 6 月起 Vue 项目冲刺的 TS 编码规范

### 工程化与构建（7 篇，W21 起隔周推进；冲刺期可整体顺延至 7 月，不视为落后）

按风险预案将 Webpack 深挖并入构建工具笔记：

- `topics/programming/Web/engineering.md` —— 总览
- `01-package-management` 包管理（npm/pnpm/yarn、lockfile、monorepo 入门）
- `02-bundlers` 构建工具：Vite 原理、配置与插件为主，Webpack 核心（entry/loader/plugin）作对照；后续确有需要再拆分深挖
- `03-code-quality` 代码质量（ESLint/Prettier/husky、TS strict 配置与常见报错治理，衔接 TS 系列）
- `04-testing` 前端测试（Vitest、Testing Library、Playwright）
- `05-performance-deploy` 性能指标与部署（Web Vitals、打包优化、Nginx/Docker）
- `06-ci-cd` CI/CD 与协作（GitHub Actions、Git 工作流、发布）

### 求职作品与验证（动作后置到 2027-06，软考后集中进行）

- 以 Vue 3 + TypeScript 完成一个可部署、有真实业务流程和测试的项目（TS 全程 strict 模式）；最低验收包含多页面路由、表单校验、异步数据的加载/错误状态、响应式布局、自动化测试、在线演示和项目 README。
- 里程碑：岗位要求清单（W1）→ 项目骨架（W4，冲刺期仅维护）→ MVP 与测试部署（W35–W37）→ 作品讲解/模拟面试（W38–W39）。求职过程中优先按目标岗位反馈调整项目，React 作为差异化补充而非并行主线。

## 路线三：软考系统架构设计师（里程碑嵌入总表）

> 三科大纲、论文模块（素材卡 / 六段模板 / 真题矩阵 / 自评清单）以 [[topics/exams/ruankao/system-architect]] 为单一事实源，此处只列阶段对齐与硬节点。

- **阶段对齐**：基础期 = W1–W13（教程精读 + 两份素材卡 + 第 1 篇论文精写）；强化期 = W14–W22（4 套综合真题 + 案例五大题型 + 论文 3 篇限时）；冲刺期 = W23–W34（报名、每周 1 篇限时论文、综合刷题保持、考前总复盘）。与数学、前端共用每周预算（见「节奏与写作约定」）。
- **硬节点**：素材卡 ×2 与第 1 篇精写 ≤ W13；综合真题 4 套与案例五大题型 ≤ W22；**报名 W23–W25（2027-03 中下旬，窗口约一周，错过再等半年）**；论文累计 12–16 篇；考试 W34 前后（预计 5 月下旬，以准考证为准）。
- **冲突规则**：冲刺期若数学短稿与论文时间冲突，论文优先，数学做题保持即可。

## 39 周总表

> W1–W4 爬坡 6h/周（每线各 1 个轻单元）；W5–W22 常态 16h（数学 6h / 前端 4h / 软考 4h）；W23–W34 软考冲刺 16h（软考 7h / 数学 4.5h / 前端 1.5h）——数学新单元一律短稿，前端隔周 1 篇轻量工程化笔记（可整体顺延不视为落后）；W35–W39 考后 16h（数学 10h / 前端 5h）。软考论文按 ①–⑭ 编号累计 14 篇，覆盖 5 个方向。

| 周 | 起始日 | 数学：新学/练习/笔记 | 前端：主线笔记/求职实践 | 软考：教程/真题/论文 |
|----|--------|----------------------|------------------------|---------------------|
| W1 | 10-05 | `calculus.md` 总览草稿 + 基础诊断 | 采集目标岗位要求，确定 Vue 项目题目 | 熟悉考试机制与科目结构，排教程精读顺序 |
| W2 | 10-12 | `01-functions` | `vue.md` 总览 + TS 三篇查漏回看 | 教程：架构风格与质量属性 |
| W3 | 10-19 | `02-03-sequence-function-limits` | Vue `01-vue-essentials` | 教程：架构评估（ATAM）、4+1 视图 |
| W4 | 10-26 | `04-05-infinitesimal-continuity` | 搭建 Vue 项目骨架并跑通开发流程 | 教程：软件工程域 + 分章题 |
| W5 | 11-02 | `06-limit-techniques` | Vue `02-composition-api` | **素材卡①**；教程：数据库域 |
| W6 | 11-09 | `07-derivative` | Vue `03-components-basics` | 教程：操作系统域 + 分章题 |
| W7 | 11-16 | `08-differential-higher-order` | Vue `04-components-advanced` | 教程：网络域；范文精读 ① |
| W8 | 11-23 | `09-mean-value-theorems` | Vue `05-reactivity-system` | 教程：安全与新技术域 + 错题归档 |
| W9 | 11-30 | `10-taylor-formula` | Vue `06-vue-router` | **素材卡②**；教程：法规/数学域 |
| W10 | 12-07 | `11-lhopital` | Vue `07-pinia` | 范文精读 ②③；论文骨架背诵 |
| W11 | 12-14 | `12-monotonicity-extrema` | Vue `08-vue-engineering`（主线收官） | 按真题矩阵给 5 个方向列提纲 |
| W12 | 12-21 | `13-concavity-asymptote` | Vue 主线复盘；项目迭代 | 论文①：第 1 篇不限时精写（上） |
| W13 | 12-28 | `14-derivative-applications` | 弹性：项目迭代/补漏 | 论文①（下）完成 + 对照自评 |
| W14 | 01-04 | `15-indefinite-integral` | `react.md` 对照总览 | 综合 2024.11 真题 + 错题域归档 |
| W15 | 01-11 | `16-substitution` | React `01-react-mental-model` | 案例①质量属性+架构评估；论文②高并发（限时） |
| W16 | 01-18 | `17-parts-rational` | React `02-react-state-hooks` | 综合 2025.5 真题 |
| W17 | 01-25 | `18-definite-integral` | React `03-react-ecosystem-comparison` | 案例②缓存一致性 |
| W18 | 02-01 | `19-improper-integral`（春节轻量） | 弹性：项目维护 | 综合 2025.11（轻）；论文③数据方向 |
| W19 | 02-08 | `20-integral-applications`（春节轻量） | 弹性：项目维护 | 案例③嵌入式（轻） |
| W20 | 02-15 | `21-first-order-ode` | TS `vue-integration` | 综合 2026.5 真题；四套错题总复盘 |
| W21 | 02-22 | `22-reducible-ode` | `engineering.md` 总览 | 案例④Web 应用；论文④架构风格 |
| W22 | 03-01 | `23-second-order-ode` | Engineering `01-package-management` | 案例⑤安全关键；强化期收尾复盘 |
| W23 | 03-08 | `24-ode-applications`（转短稿节奏） | —（前端让位冲刺） | 冲刺启动：关注**报名通知**；2026.10 真题；论文⑤质量保障 |
| W24 | 03-15 | `25-vectors` + `26-planes-and-lines` 短稿 | Engineering `02-bundlers`（轻） | **完成报名**（窗口约一周，勿错过）；论文⑥高并发复写提速 |
| W25 | 03-22 | `27-surfaces-curves` + `28-multivariable-limit` 短稿 | — | 综合每两天 1 套启动；论文⑦数据方向 |
| W26 | 03-29 | `29-partial-derivative` + `30-chain-and-implicit` 短稿 | Engineering `03-code-quality`（轻） | 论文⑧架构风格；错题域回补 |
| W27 | 04-05 | `31-directional-derivative` + `32-multivariable-extrema` 短稿 | — | 案例限时 1 套；论文⑨ |
| W28 | 04-12 | `33-double-integral` + `34-triple-integral` 短稿 | Engineering `04-testing`（轻） | 论文⑩（只写练过方向） |
| W29 | 04-19 | `35-line-integral-1` + `36-line-integral-2` 短稿 | — | 案例限时 2 套；论文⑪ |
| W30 | 04-26 | `37-surface-integral-1` + `38-surface-integral-2` 短稿 | Engineering `05-performance-deploy`（轻） | 论文⑫；案例模板背诵启动 |
| W31 | 05-03 | `39-40-series-concepts` + `41-alternating-series` 短稿 | — | 论文⑬；素材卡数字全量过一遍 |
| W32 | 05-10 | `42-power-series` + `43-taylor-series` + `44-fourier-series` 短稿（Ch1–8 收官） | — | 论文⑭；案例模板背熟；打印准考证 |
| W33 | 05-17 | 保持练习：错题回顾，不开新单元 | — | 考前总复盘：骨架/素材/数字/时间分配 |
| W34 | 05-24 | 保持练习 | — | **考试周（预计 5 月下旬，以准考证为准）** |
| W35 | 05-31 | 限时真题复盘① + 最薄弱专题回补 | Engineering `06-ci-cd`；项目重启 | 考后归档：论文、错题与感受 |
| W36 | 06-07 | 真题复盘② + `45-mvt-proof-special` | Vue 项目 MVP：核心流程与表单校验 | —（软考线结束） |
| W37 | 06-14 | `46-integral-inequality` + **线代启动**（行列式） | 项目测试、部署、README | — |
| W38 | 06-21 | `47-series-summation` + `48-synthetic-problems`（做题为主） | 作品讲解稿 + 模拟面试① | — |
| W39 | 06-28 | 线代：矩阵与向量组推进 | 模拟面试②；按岗位反馈查漏 | — |

> 🧨 **W18–W19 恰逢寒假/春节（2027-02-06 前后）**：保留学习时段但降低新笔记要求；若产能下降，优先保留数学题目练习与软考真题/论文，笔记合并/顺延，不追赶行数。
> 📌 **W23–W25 为软考报名窗口**（预计 2027-03 中下旬，窗口约一周）：开放即报，最迟 W25 完成，错过再等半年。

## 与知识库的衔接

- 每篇完成后：加入对应 MOC（[[notes/MOC - math]] 章节清单打勾 / [[notes/MOC - programming]] Web 分类加链）；软考笔记归 [[notes/MOC - exams]]
- 提交前跑 `python scripts/check_notes.py`，保持 0 error
- 数学公式用 KaTeX 语法，写完用 Markdown Preview Enhanced 检查渲染
- TypeScript 示例延续 TS 系列的做法：`tsc --strict` 实测通过后再入笔记
- 不等式相关内容优先链接 [[topics/math/inequalities]] 而非重复书写

## 考研全年衔接路线（2027-06 至预计考期）

> 预计参加 2027 年 12 月数一考试；具体考试日期与当年大纲公布后再校准。因软考冲刺占用 3–5 月，线代首轮推迟到 6 月中启动、概率压缩到 8 月，考研后段节奏比原计划更紧——这是加入软考的已知代价，两个刚性考期（2027-05、2027-12）都不可再让。复习以做题、回忆和错题复测为主，不再为每个知识点都写成长文。

| 阶段 | 数学主线 | 检查点 / 产出 |
|------|----------|----------------|
| 2027-06 中 至 07 | 高数 45–48 专题与两套真题复盘收尾；线性代数首轮：行列式、矩阵、向量组与方程组、特征值、二次型 | 每章做闭卷回忆与典型题；补充必要的短笔记和错题链接 |
| 2027-08 | 概率论与数理统计首轮（压缩至约 5 周）：概率、随机变量与分布、多维分布、数字特征、极限定理、统计推断 | 覆盖 MOC 中的数一范围；每周安排一次前面章节的间隔复习 |
| 2027-09 至 10 | 高数、线代、概率第二轮；按章节做真题题组 | 建立薄弱点清单，优先修复不会列式、方法选择错误和计算失误 |
| 2027-11 | 限时套卷与完整复盘 | 以近 8–10 年试卷为整卷训练主线；较早年份按章节补题。每套都记录失分原因、修复动作和复测结果 |
| 2027-12 至考试 | 查漏补缺与考前节奏 | 公式/方法主动回忆、错题回看、少量模拟；不再开启大型新笔记或新专题 |

6 月起数学恢复约 10h/周，前端求职项目占 4–6h；拿到面试/工作机会或官方考期公布后按实际情况滚动调整。若全职工作改变可用时间，以数学首轮覆盖和周期性真题复盘为不可轻易取消的底线。

## 附带优化任务（不占每周配额，随时做）

来自 2026-10-01 全库检查，均为低优先级：

- [ ] `topics/programming/Web/es6.md` 与 `topics/programming/Web/javascript/06-es6-modern-features.md` 互相加交叉引用，明确分工（es6 = 语法专题深挖，js/06 = 章节导读）
- [ ] 空壳笔记处理：`topics/ai/Claude Code.md`（8 行）、`topics/ai/note.md`（9 行）、`topics/programming/cplusplus/vscodec.md`、`cplusplus/into.md`、`Android_into.md` —— 填充或明确标记占位
- [ ] `topics/ai/note.md` 属闪念性质，考虑移到 `inbox/`
- [ ] 若目标岗位反复要求，再补精简 HTML 语义化 / HTTP 备忘；基础内容先在 Vue 项目中实际使用，不为“凑齐三件套”另写长篇

## 风险 & 调整规则

- **刚性考期与优先级**：两个刚性节点为 **2027-05 软考**与 **2027-12 考研**。常态期（W1–W22）优先级 数学 > 软考 > 前端；软考冲刺期（W23–W34）优先级 软考 > 数学 > 前端——前端可整周顺延，软考论文与数学做题尽量不断线。
- **落后时的降级顺序**：先缩短/合并低优先级前端笔记（工程化整体顺延），再把数学新单元压缩为短稿，最后才动软考真题与论文配额（冲刺期论文优先级最高）。若连续两周超出 16 小时仍未完成，不累积追赶，立即下调后续产出范围。
- **软考未过的衔接**：若 2027-05 未通过，下半年 11 月批次二战的冲刺（9–11 月）会与考研套卷期冲突——届时以考研为重，软考二战按最低配置（论文 2 篇复写 + 真题保持）执行。
- **求职路线优先级**：Vue 项目闭环、TS 实战与工程基础优先；React 对照深度与 Webpack 深挖可合并或顺延（Webpack 已并入 `02-bundlers`），不为”学完两个框架”牺牲作品质量。
- **质量底线**：笔记完成须同时满足概念表述清楚、例题自行核对、关键题能闭卷复做；行数和按期发布不能替代掌握度。短稿同样适用，只是允许更少的证明展开。

## 进度更新

- 2026-10-01 —— 计划创建。全库检查通过（0 error），方向为高数 + 前端求职准备。
- 2026-10-01 —— 根据时间预算（前 4 周 6h/周、之后约 16h/周）收敛前端范围为 Vue 主线 + React 对照；增加作品集里程碑、笔记合并和 4 月后线代/概率/总复习路线。
- 2026-10-01 —— 前端线补充 TypeScript：新增 `typescript/vue-integration`（W16），已有 TS 三篇定为 Vue 动笔前查漏（W2）；Webpack 深挖并入 `02-bundlers`（W19），React 生态对照笔记同步标注 TS 类型写法。前端总篇数保持 21 不变。
- 2026-10-02 —— **加入软考（系统架构设计师，2027-05 考期），计划延长为 39 周（至 2027-07-04）**：每周总量维持约 16h、按阶段三线分配（冲刺期软考 7h / 数学 4.5h / 前端 1.5h）；W23 起数学新单元转短稿；线代推迟到 6 月中启动、概率压缩至 8 月；求职项目与面试动作后置到 6 月；新增路线三与 39 周总表软考列（论文 ①–⑭）。
