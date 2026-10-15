---
title: 数学 MOC
tags:
  - moc
  - math
created: 2026-09-09
updated: 2026-10-12
---

# MOC · Math（数学地图）

> 数学学习笔记，**主要服务于考研数学一**（2027-12 考试）。
> 范围：高数 + 线代 + 概率论与数理统计 + 空间解析几何。

## 全景

按考研数一考试范围组织：
- **高等数学**（约 56%）：函数、极限、导数、积分、级数、微分方程
- **线性代数**（约 22%）：行列式、矩阵、向量、特征值、二次型
- **概率论与数理统计**（约 22%）：随机变量、数字特征、统计推断

## 核心笔记

> 已有的、重要的

- [inequalities](../topics/math/inequalities.md) —— 不等式专题（考研核心工具）
- [functions-and-bounds](../topics/math/functions-and-bounds.md) —— 界与函数（高数起点：确界 · 函数性质 · 初等函数 · 参数方程 · 极坐标 · 图形变换）
- [calculus](../topics/math/calculus.md) —— 高等数学总览（章节导航与学习路线）

## 按考研章节

### 高等数学

#### 一、函数、极限、连续

- [x] [functions-and-bounds](../topics/math/functions-and-bounds.md) —— 界与函数（基础概念）
- [x] [02-03-sequence-function-limits](../topics/math/calculus/02-03-sequence-function-limits.md) —— 数列与函数极限（定义 · 性质 · 夹逼 · 单调有界 · 两个重要极限）
  - 原子卡：[夹逼准则](squeeze-theorem.md) · [单调有界定理](monotone-bounded-convergence.md) · [两个重要极限](two-important-limits.md)
- [ ] 连续函数
- [ ] 无穷小与无穷大

#### 二、一元函数微分学

- [ ] 导数与微分
- [ ] 中值定理
- [ ] 导数应用（单调性、极值、凹凸性）

#### 三、一元函数积分学

- [ ] 不定积分
- [ ] 定积分
- [ ] 反常积分

#### 四、多元函数微分学

- [ ] 偏导数与全微分
- [ ] 多元复合函数求导
- [ ] 多元函数极值

#### 五、多元积分

- [ ] 二重积分
- [ ] 三重积分
- [ ] 曲线曲面积分

#### 六、无穷级数

- [ ] 常数项级数
- [ ] 幂级数
- [ ] 傅里叶级数

#### 七、常微分方程

- [ ] 一阶微分方程
- [ ] 高阶微分方程

#### 八、空间解析几何

- [ ] 向量代数
- [ ] 平面与直线
- [ ] 曲面与曲线

### 线性代数

- [ ] 行列式
- [ ] 矩阵
- [ ] 向量组与线性方程组
- [ ] 特征值与特征向量
- [ ] 二次型

### 概率论与数理统计

- [ ] 随机事件与概率
- [ ] 随机变量及其分布
- [ ] 多维随机变量
- [ ] 数字特征
- [ ] 大数定律与中心极限定理
- [ ] 数理统计（参数估计、假设检验）

## 按工具 / 主题

### 不等式（专题）

- [inequalities](../topics/math/inequalities.md) —— 不等式体系总览（依赖图 · 15 条一览表 · 口诀速记；证明 / 多视角 / 应用 / 习题分居 inequalities/ 六章）
  - [一·基础不等式](../topics/math/inequalities/01-basics.md) · [二·核心工具](../topics/math/inequalities/02-core-tools.md) · [三·高阶不等式](../topics/math/inequalities/03-advanced.md) · [四·多视角理解](../topics/math/inequalities/04-multiview.md) · [五·应用](../topics/math/inequalities/05-applications.md) · [六·分层习题](../topics/math/inequalities/06-exercises.md)

#### 不等式原子卡（Zettelkasten · 2026-10-15 建立骨架，正文待填）

一个概念一张卡，卡与卡之间双向互链。枢纽卡：琴生 → 均值 / 伯努利 / Hölder；柯西-施瓦茨 → Young / Hölder / 积分形式。

| # | 原子卡 | 上游 | 下游 |
|---|--------|------|------|
| 1 | [三角不等式](triangle-inequality.md) | — | Minkowski |
| 2 | [均值不等式 AM-GM](arithmetic-geometric-mean.md) | 琴生 | Hölder |
| 3 | [排序不等式](rearrangement-inequality.md) | — | 切比雪夫 |
| 4 | [切比雪夫不等式](chebyshev-sum-inequality.md) | 排序 | — |
| 5 | [柯西-施瓦茨](cauchy-schwarz-inequality.md) ★ | 三角 | Hölder / Young / 积分形式 |
| 6 | [伯努利不等式](bernoulli-inequality.md) | 琴生 | 指对 |
| 7 | [琴生不等式](jensen-inequality.md) ★ | — | 均值 / 伯努利 / Hölder / 指对 |
| 8 | [Nesbitt 不等式](nesbitt-inequality.md) | 柯西 | 权方和 |
| 9 | [Young 不等式](young-inequality.md) | 琴生 | Hölder |
| 10 | [Hölder 不等式](holder-inequality.md) ★ | 柯西 / Young | 权方和 / 积分形式 |
| 11 | [权方和不等式](weighted-power-sum-inequality.md) | Hölder / Nesbitt | — |
| 12 | [Minkowski 不等式](minkowski-inequality.md) | 三角 | 积分形式 |
| 13 | [指数与对数不等式](exponential-logarithmic-inequality.md) | 琴生 | — |
| 14 | [三角函数不等式](trigonometric-inequality.md) | — | — |
| 15 | [积分形式（四件套）](integral-form-inequalities.md) | 柯西 / 琴生 / Hölder / Minkowski | — |

> 跨簇连接：指对与三角函数两张卡直通 Ch1 的 [夹逼准则](squeeze-theorem.md) / [两个重要极限](two-important-limits.md)——不等式与极限两簇之间目前只有这两条通路，待填正文时可以继续加。

## 学习方法

- 三线总计划与写作排程：[笔记编撰计划](../projects/note-writing-plan.md)（高数线）
- 跟大学微积分课同步推进
- 每章用 Zettelkasten 拆分成小卡片（原子笔记）
- 不等式等专题单独成册
- 错题集：单独文件夹 + 永久笔记
- 真题：2010-2026 共 17 年，留到强化期做

## 按标签查找

Foam 没有图谱查询语法。按标签筛选用左侧 **Tag Explorer** 面板，或 `Ctrl+Shift+P` → `Foam: Search Tag`；连接与孤立情况在 `Foam: Show Graph` 面板查看。

- `math` —— 所有数学笔记
- `inequality` —— 不等式专题
- `kaoyan` —— 考研相关

## 相关 MOC

- [MOC - programming](MOC%20-%20programming.md) —— 编程（算法数学基础）
- [MOC - ai](MOC%20-%20ai.md) —— AI（深度学习数学基础）

## 更新记录

- **2026-09-09** —— 初始创建（重构后），纳入考研数一完整大纲
- **2026-09-17 ~ 09-19** —— [inequalities](../topics/math/inequalities.md) 大扩充（现 1657 行 / 20 张插图）：高阶不等式（Young / Hölder / 权方和 / Minkowski）、多视角理解（向量·矩阵·几何·物理）、应用（指数/对数/三角/积分），插图统一放 `attachments/images/math/inequalities/`
- **2026-09-30** —— 索引维护：同步不等式专题最新结构与更新记录
- **2026-10-09** —— 新增 [functions-and-bounds](../topics/math/functions-and-bounds.md)：占位稿「基础概念」补全为完整笔记（确界理论、函数概念与四性质、初等函数、参数方程、极坐标、图形变换），并挂入 Ch1 清单与不等式专题导航
- **2026-10-09** —— 「学习方法」接入 [笔记编撰计划](../projects/note-writing-plan.md)（原为单向链接，补全双向导航）
- **2026-10-10** —— 新增 [高等数学总览](../topics/math/calculus.md)（W1 计划内交付：章节导航、学习路线、考纲权重）与 [数列与函数极限](../topics/math/calculus/02-03-sequence-function-limits.md)（Ch1 长文：ε-语言、左右极限、性质与四则、夹逼、单调有界、Heine 归结原则、两个重要极限）；Ch1 勾选第二项
- **2026-10-10** —— [inequalities](../topics/math/inequalities.md) 新增「口诀速记」（总纲三句 · 十五条口诀表 · 均值链专记 · 选工具顺口溜）与「分层习题」13 题（A 基础 4 / B 进阶 5 / C 考研向 4，均附提示与详解），并与 [数列与函数极限](../topics/math/calculus/02-03-sequence-function-limits.md) 互链（$e$ 的双侧估计）；AM-GM 半圆插图升级——补入射影定理全套标注（母 Rt△ABQ 与母子相似填充、$AP=a$/$PB=b$ 分段、两条直角边的射影公式、直角标记），正文与图逐元素对应
- **2026-10-11** —— [inequalities](../topics/math/inequalities.md) 拆分为总览 + 六章（原 1657 行；`01-basics` ~ `06-exercises`）：总览保留依赖图、15 条一览表与口诀速记，证明 / 多视角 / 应用 / 习题分居 `topics/math/inequalities/`；174 个文内锚点改写为跨文件链接，章节按「第 N / 6 章」互链；当日新增的 Titu 引理附录随 Nesbitt 落在 `02-core-tools`
- **2026-10-12** —— 「按工具 / 主题」的不等式条目下补六章直达导航（对齐 MOC - programming 的 JS/CSS 章节先例）；10-11 拆分条目补记原行数 1657；Ch1 新增「交付即提取」首批 3 张原子卡（[夹逼准则](squeeze-theorem.md) / [单调有界定理](monotone-bounded-convergence.md) / [两个重要极限](two-important-limits.md)），落实「学习方法」里既定的 Zettelkasten 约定，后续每交付一篇计划内长文提取 3–5 张
- **2026-10-12** —— 不等式专题的 111 处 `[[路径#锚点]]` 式 wikilink（hub + 六章）统一改为 Markdown 锚点链接：`#` 锚点 wikilink 在 Foam 中点击会触发「创建笔记」而非跳转（跨版本解析不可靠），Markdown 链接 `[文字](路径.md#锚点)` 为 VS Code / Foam / GitHub 三端可跳转的标准形式；`check_notes.py` 已将此类 wikilink 记为 error 防再发
