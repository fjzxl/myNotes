---
title: "笔记编撰计划 · 高等数学 + 前端（2026-10 ~ 2027-04）"
tags:
  - project
  - plan
  - math
  - programming
status: active
created: 2026-10-01
updated: 2026-10-01
deadline: 2027-04-04
---

# 📝 笔记编撰计划 · 高等数学 + 前端（2026-10 ~ 2027-04）

> **26 周（2026-10-05 ~ 2027-04-04）分阶段推进**：计划产出约 69 篇笔记（高数总览 + 45 个专题页 + 2 份真题复盘；前端 21 篇），并完成求职作品集与面试练习。前 4 周按 6 小时/周爬坡，之后按约 16 小时/周执行。4 月后衔接线代、概率与数一总复习，路线延伸至预计的 2027-12 考期。
> 相关索引：[[notes/MOC - math]] · [[notes/MOC - programming]]

## 项目目标

- **高等数学**：按考研数一大纲完成 8 大章首轮学习，形成 `topics/math/calculus.md` 总览 + 45 个专题笔记 + 2 份限时真题复盘，衔接已有的 [[topics/math/inequalities]]。首轮覆盖不等于考研数学全部完成；4 月后继续线代、概率与综合复习。
- **前端求职**：在现有 HTML/CSS/JS/TS 基础上（[[topics/programming/Web/javascript]]、[[topics/programming/Web/css]]、TypeScript 系列）以 **Vue 3 + TypeScript 为主线**——TS 从已有基础系列走向框架集成实战（新增 `vue-integration`），React 做求职所需的对照入门，工程化围绕一个可部署的 Vue 项目展开；目标是形成可展示的作品与面试材料，而非平均学完两个框架。

## 范围

### ✅ In scope

- 2026-10 至 2027-04：高等数学 8 章首轮笔记与练习；Vue 3 主线、TypeScript 框架集成实战、React 对照入门、工程化及一个 Vue 求职作品
- 2027-04 至预计考期：线性代数、概率论与数理统计首轮学习；三科综合复习、分章节真题与限时套卷
- 每写完一章同步更新对应 MOC 并跑 `python scripts/check_notes.py`

### ❌ Out of scope（留给下一阶段）

- 2027-04 前系统编写线性代数、概率论与数理统计专题笔记（4 月后列学习/复习路线，是否扩展成完整长文按备考进度决定）
- 2027-04 前刷完全部 2010-2026 真题（前期做典型题，整卷与成体系复盘放到后续阶段）
- HTML 语义化 / HTTP 网络基础的独立长篇教程（项目实作仍需掌握必要语义标签、HTTP 方法/状态码与 CORS）
- 数据结构与算法笔记

## 节奏与写作约定

- **时间预算**：W1–W4 每周 6 小时（数学约 3h、前端约 3h）；W5–W26 每周约 16 小时。建议工作日 3 天各 2h 数学、2 天各 2h 前端；周末各 3h，一天偏数学练习/复盘，一天偏前端编码/作品。每周复盘后可按实际情况调配。
- **启动期产出**：前 4 周每周只有约 6 小时，按“数学 1 个学习/整理单元 + 前端 1 个学习/项目单元”爬坡，不按 3 篇长文计产量；较难内容顺延，不通过压缩做题或不核对代码来赶进度。
- **常态时间预算**：W5–W26 每周约 16 小时。可先按数学 9h（新知识、做题、闭卷复习均计入）+前端 7h（学习、编码、作品与笔记均计入）执行；每四周检查一次实际耗时与掌握情况。
- **笔记体量**：取消固定行数目标。按问题复杂度决定长度：目录/索引只保留导航，普通专题以“理解所需的最少解释 + 已核对例题 + 易错点”为准；证明与应用繁多的主题再展开。行数不作为完成标准。
- **数学章节统一结构**：考纲定位（以当年大纲为准）→ 概念与定义 → 定理及证明思路 → 典型例题（至少自行演算核对）→ 易错点与做题套路 → 前后章节/不等式专题互链；另留闭卷回忆与错题复测时间。
- **前端章节统一结构**：与 `css.md` / `javascript.md` 章节相同——导航头（上一章/下一章 wikilink）→ 目标 → 正文（代码示例可运行）→ 小结与自测。
- **文件命名**：英文 kebab-case；数学放 `topics/math/calculus/`，前端放 `topics/programming/Web/vue|react|engineering/`（TS 笔记沿用已有 `topics/programming/Web/typescript/`，不加数字前缀）。
- **互链与收尾**：新笔记加入对应 MOC；数学章节在 [[notes/MOC - math]] 的章节清单勾选；每周末跑校验脚本。
- **插图**（如需要）放 `attachments/images/math/calculus/` 或 `attachments/images/programming/<topic>/`。

## 路线一：高等数学（总览 1 + 专题笔记 45 + 真题复盘 2）

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

### 第三部分 · 专题与真题启动（W24–W26，6 项）

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

### React 对照线（4 篇，W12–W15：建立可迁移认知，不重复完整学习 Vue 全家桶）

- `topics/programming/Web/react.md` —— 总览
- `01-react-mental-model` React 入门、JSX、组件与渲染模型
- `02-react-state-hooks` props/state、事件与核心 Hooks（对照 Vue Composition API）
- `03-react-ecosystem-comparison` React Router 与状态管理生态（对照 Vue Router/Pinia），同步标注 TS 类型写法，与 `typescript/vue-integration` 互链

### TypeScript 实战（已有 3 篇查漏 + 新增 1 篇，W2 查漏 / W16 新增）

已有基础系列不重写，动笔 Vue 前回看查漏即可；真正的缺口是"框架中的 TS"，新增一篇实战收口：

- [[topics/programming/Web/typescript/intro]] —— 入门与工程实践（已有）
- [[topics/programming/Web/typescript/interface]] —— 接口契约（已有）
- [[topics/programming/Web/typescript/type-system]] —— 类型系统进阶（已有）
- `topics/programming/Web/typescript/vue-integration` —— TS × Vue 3 实战（新增，W16）：`defineProps`/`defineEmits` 泛型参数、泛型组件、SFC 类型推导与 vue-tsc、tsconfig 实用项、常用工具类型（Partial/Pick/Omit/Record 等）在组件与组合式函数中的运用；产出物直接作为 W24 起 Vue 项目的 TS 编码规范

### 工程化与构建（7 篇，W17–W23）

按风险预案将 Webpack 深挖并入构建工具笔记，为 TS 实战腾出一周：

- `topics/programming/Web/engineering.md` —— 总览
- `01-package-management` 包管理（npm/pnpm/yarn、lockfile、monorepo 入门）
- `02-bundlers` 构建工具：Vite 原理、配置与插件为主，Webpack 核心（entry/loader/plugin）作对照；后续确有需要再拆分深挖
- `03-code-quality` 代码质量（ESLint/Prettier/husky、TS strict 配置与常见报错治理，衔接 TS 系列）
- `04-testing` 前端测试（Vitest、Testing Library、Playwright）
- `05-performance-deploy` 性能指标与部署（Web Vitals、打包优化、Nginx/Docker）
- `06-ci-cd` CI/CD 与协作（GitHub Actions、Git 工作流、发布）

### 求职作品与验证（不以新增长文为目标）

- 以 Vue 3 + TypeScript 完成一个可部署、有真实业务流程和测试的项目（TS 全程 strict 模式）；最低验收包含多页面路由、表单校验、异步数据的加载/错误状态、响应式布局、自动化测试、在线演示和项目 README。
- 里程碑：岗位要求清单 → 可用 MVP → 测试与部署 → 作品讲解/模拟面试。求职过程中优先按目标岗位反馈调整项目，React 作为差异化补充而非并行主线。

## 26 周总表

> W1–W4 每周约 6 小时，只安排一个主要数学单元和一个前端单元；内容先写短稿并做诊断。W5–W26 每周约 16 小时，通常两个数学单元 + 一个前端单元。单元可以是专题笔记、复习练习或项目里程碑，不把每个单元都强行写成长文。

| 周 | 起始日 | 数学：新学/练习/笔记 | 前端：主线笔记/求职实践 |
|----|--------|----------------------|------------------------|
| W1 | 10-05 | `calculus.md` 总览草稿 + 基础诊断 | 采集目标岗位要求，确定 Vue 项目题目 |
| W2 | 10-12 | `01-functions` | `vue.md` 总览 + TS 三篇查漏回看 |
| W3 | 10-19 | `02-03-sequence-function-limits` | Vue `01-vue-essentials` |
| W4 | 10-26 | `04-05-infinitesimal-continuity` | 搭建 Vue 项目骨架并跑通核心开发流程 |
| W5 | 11-02 | `06-limit-techniques` + `07-derivative` | Vue `02-composition-api` |
| W6 | 11-09 | `08-differential-higher-order` + `09-mean-value-theorems` | Vue `03-components-basics` |
| W7 | 11-16 | `10-taylor-formula` + `11-lhopital` | Vue `04-components-advanced` |
| W8 | 11-23 | `12-monotonicity-extrema` + `13-concavity-asymptote` | Vue `05-reactivity-system` |
| W9 | 11-30 | `14-derivative-applications` + `15-indefinite-integral` | Vue `06-vue-router` |
| W10 | 12-07 | `16-substitution` + `17-parts-rational` | Vue `07-pinia` |
| W11 | 12-14 | `18-definite-integral` + `19-improper-integral` | Vue `08-vue-engineering` |
| W12 | 12-21 | `20-integral-applications` + `21-first-order-ode` | `react.md` 对照总览 |
| W13 | 12-28 | `22-reducible-ode` + `23-second-order-ode` | React `01-react-mental-model` |
| W14 | 01-04 | `24-ode-applications` + `25-vectors` | React `02-react-state-hooks` |
| W15 | 01-11 | `26-planes-and-lines` + `27-surfaces-curves` | React `03-react-ecosystem-comparison`（含 TS 类型对照） |
| W16 | 01-18 | `28-multivariable-limit` + `29-partial-derivative` | TS `vue-integration`（TS × Vue 3 实战） |
| W17 | 01-25 | `30-chain-and-implicit` + `31-directional-derivative` | `engineering.md` 总览 |
| W18 | 02-01 | `32-multivariable-extrema` + `33-double-integral` | Engineering `01-package-management` |
| W19 | 02-08 | `34-triple-integral` + `35-line-integral-1` | Engineering `02-bundlers`（Vite + Webpack 对照） |
| W20 | 02-15 | `36-line-integral-2` + `37-surface-integral-1` | Engineering `03-code-quality` |
| W21 | 02-22 | `38-surface-integral-2` + `39-40-series-concepts-positive-tests` | Engineering `04-testing` |
| W22 | 03-01 | `41-alternating-series` + `42-power-series` | Engineering `05-performance-deploy` |
| W23 | 03-08 | `43-taylor-series` + `44-fourier-series` | Engineering `06-ci-cd` |
| W24 | 03-15 | `45-mvt-proof-special` + `46-integral-inequality` | Vue 项目 MVP：核心业务流程与表单校验 |
| W25 | 03-22 | `47-series-summation` + `48-synthetic-problems` | 项目测试、部署、README 与作品讲解 |
| W26 | 03-29 | 两次限时真题复盘；回补最薄弱专题 | 模拟项目讲解/面试，按目标岗位查漏补缺 |

> 🧨 **W18–W19 恰逢寒假/春节（2027-02-06 前后）**：保留学习时段但降低新笔记要求；若产能下降，优先保留数学题目练习与 Vue 项目闭环，笔记合并/顺延，不追赶行数。

## 与知识库的衔接

- 每篇完成后：加入对应 MOC（[[notes/MOC - math]] 章节清单打勾 / [[notes/MOC - programming]] Web 分类加链）
- 提交前跑 `python scripts/check_notes.py`，保持 0 error
- 数学公式用 KaTeX 语法，写完用 Markdown Preview Enhanced 检查渲染
- TypeScript 示例延续 TS 系列的做法：`tsc --strict` 实测通过后再入笔记
- 不等式相关内容优先链接 [[topics/math/inequalities]] 而非重复书写

## 考研全年衔接路线（2027-04 至预计考期）

> 预计参加 2027 年 12 月数一考试；具体考试日期与当年大纲公布后再校准。本阶段优先完成高数首轮，4 月后转入线代、概率和三科复习。复习以做题、回忆和错题复测为主，不再为每个知识点都写成长文。

| 阶段 | 数学主线 | 检查点 / 产出 |
|------|----------|----------------|
| 2027-04 至 05 | 线性代数首轮：行列式、矩阵、向量组与方程组、特征值、二次型 | 每章做闭卷回忆与典型题；补充必要的短笔记和错题链接 |
| 2027-06 至 07 | 概率论与数理统计首轮：概率、随机变量与分布、多维分布、数字特征、极限定理、统计推断 | 覆盖 MOC 中的数一范围；每周安排一次前面章节的间隔复习 |
| 2027-08 至 09 | 高数、线代、概率第二轮；按章节做真题题组 | 建立薄弱点清单，优先修复不会列式、方法选择错误和计算失误 |
| 2027-10 至 11 | 限时套卷与完整复盘 | 以近 8–10 年试卷为整卷训练主线；较早年份按章节补题。每套都记录失分原因、修复动作和复测结果 |
| 2027-12 至考试 | 查漏补缺与考前节奏 | 公式/方法主动回忆、错题回看、少量模拟；不再开启大型新笔记或新专题 |

4 月后仍以约 16 小时/周为预算时，建议数学占 10–12 小时，前端求职、项目维护与申请占 4–6 小时；拿到面试/工作机会或官方考期后按实际情况滚动调整。若全职工作改变可用时间，以数学首轮覆盖和周期性真题复盘为不可轻易取消的底线。

## 附带优化任务（不占每周配额，随时做）

来自 2026-10-01 全库检查，均为低优先级：

- [ ] `topics/programming/Web/es6.md` 与 `topics/programming/Web/javascript/06-es6-modern-features.md` 互相加交叉引用，明确分工（es6 = 语法专题深挖，js/06 = 章节导读）
- [ ] 空壳笔记处理：`topics/ai/Claude Code.md`（8 行）、`topics/ai/note.md`（9 行）、`topics/programming/cplusplus/vscodec.md`、`cplusplus/into.md`、`Android_into.md` —— 填充或明确标记占位
- [ ] `topics/ai/note.md` 属闪念性质，考虑移到 `inbox/`
- [ ] 若目标岗位反复要求，再补精简 HTML 语义化 / HTTP 备忘；基础内容先在 Vue 项目中实际使用，不为“凑齐三件套”另写长篇

## 风险 & 调整规则

- **落后时的优先级**：数学 > 前端（考研时间刚性）。前端可整周顺延，数学章节顺序不跳。
- **求职路线优先级**：Vue 项目闭环、TS 实战与工程基础优先；React 对照深度与 Webpack 深挖可合并或顺延（Webpack 已并入 `02-bundlers`），不为”学完两个框架”牺牲作品质量。
- **滚动缓冲**：每周复盘实际投入、做题正确率和笔记耗时；落后一周时先缩短/合并低优先级前端笔记，保留数学做题。若连续两周超出 16 小时仍未完成，不累积追赶，立即下调后续产出范围。
- **质量底线**：笔记完成须同时满足概念表述清楚、例题自行核对、关键题能闭卷复做；行数和按期发布不能替代掌握度。

## 进度更新

- 2026-10-01 —— 计划创建。全库检查通过（0 error），方向为高数 + 前端求职准备。
- 2026-10-01 —— 根据时间预算（前 4 周 6h/周、之后约 16h/周）收敛前端范围为 Vue 主线 + React 对照；增加作品集里程碑、笔记合并和 4 月后线代/概率/总复习路线。
- 2026-10-01 —— 前端线补充 TypeScript：新增 `typescript/vue-integration`（W16），已有 TS 三篇定为 Vue 动笔前查漏（W2）；Webpack 深挖并入 `02-bundlers`（W19），React 生态对照笔记同步标注 TS 类型写法。前端总篇数保持 21 不变。
