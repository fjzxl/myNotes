---
title: 不等式 · 三、证明：核心工具不等式
tags:
  - math
  - inequality
  - kaoyan
created: 2026-10-11
updated: 2026-10-11
---

> 📚 本文是 [[topics/math/inequalities|不等式]] 的第 2 / 6 章（总览第三部分）。 上一章：[[topics/math/inequalities/01-basics|二、证明：基础不等式]] 下一章：[[topics/math/inequalities/03-advanced|四、证明：高阶不等式]]

# 三、证明：核心工具不等式

> 🎯 **证明篇 ② · 核心工具**：考研和竞赛中最常考、最常用的两类工具——**内积**（柯西-施瓦茨）与**凸性**（伯努利 → 琴生），以及综合运用它们的 Nesbitt。伯努利按传统常放在最前面，这里把它挪到琴生之前：它的证明二（二阶导凸性法）正是凸性方法的最简原型，为琴生、Young 以及应用篇的 $e^x \ge 1+x$ 铺路。

### 柯西-施瓦茨不等式

> **定理（Cauchy-Schwarz）** 对任意实数 $a_1, \ldots, a_n$ 和 $b_1, \ldots, b_n$，
> $$
> \left(\sum_{i=1}^n a_i b_i\right)^2 \le \left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right)
> $$
> 等号成立当且仅当 $a_i = \lambda b_i$（对某个常数 $\lambda$，所有 $i$）或 $b_i$ 全为 $0$。

**含义**：两个向量的点积的平方不超过它们模长平方的乘积，即 $|\vec{a} \cdot \vec{b}|^2 \le |\vec{a}|^2 |\vec{b}|^2$。

![柯西-施瓦茨不等式：投影长度不超过模长](/attachments/images/math/inequalities/cauchy-schwarz-angle.png)

对非零向量，$\vec{a}\cdot\vec{b} = |\vec{a}||\vec{b}|\cos\theta$，而投影长度 $|\vec{b}||\cos\theta| \le |\vec{b}|$，所以点积的绝对值被两个模长之积"卡住"；夹角越接近 $0$ 或 $\pi$，越接近等号，同向与反向共线均可取等。

**证明一（判别式法）**：

若所有 $b_i = 0$，不等式两边均为 $0$，显然成立。

设 $b_1, \ldots, b_n$ 不全为 $0$，考虑关于 $t$ 的二次函数：
$$
f(t) = \sum_{i=1}^n (a_i - t b_i)^2 = \sum_{i=1}^n a_i^2 - 2t \sum_{i=1}^n a_i b_i + t^2 \sum_{i=1}^n b_i^2
$$

由于 $f(t) \ge 0$ 对所有实数 $t$ 成立，且 $\sum b_i^2 > 0$，故该二次函数的判别式 $\Delta \le 0$：
$$
\Delta = 4\left(\sum_{i=1}^n a_i b_i\right)^2 - 4\left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right) \le 0
$$

即
$$
\left(\sum_{i=1}^n a_i b_i\right)^2 \le \left(\sum_{i=1}^n a_i^2\right)\left(\sum_{i=1}^n b_i^2\right)
$$

等号成立 $\Leftrightarrow \Delta = 0 \Leftrightarrow$ 存在 $t$ 使得 $f(t) = 0$，即 $a_i = t b_i$ 对所有 $i$ 成立。$\blacksquare$

**证明二（Lagrange 恒等式）**：

$$
\left(\sum_{i=1}^n a_i^2\right)\left(\sum_{j=1}^n b_j^2\right) - \left(\sum_{i=1}^n a_i b_i\right)^2 = \sum_{1 \le i < j \le n} (a_i b_j - a_j b_i)^2 \ge 0
$$

等号成立当且仅当所有 $a_i b_j = a_j b_i$，即两向量线性相关（$b\ne0$ 时可写成 $a_i=\lambda b_i$；$b=0$ 时也取等）。$\blacksquare$

---

#### 附：Lagrange 恒等式详解

Lagrange 恒等式不仅证明了 Cauchy-Schwarz 不等式，还**精确量化了等号两边的差距**。

> **恒等式**：
> $$
> \left(\sum_{i=1}^n a_i^2\right)\left(\sum_{j=1}^n b_j^2\right) - \left(\sum_{i=1}^n a_i b_i\right)^2 = \sum_{1 \le i < j \le n} (a_i b_j - a_j b_i)^2
> $$

**为什么右边是 $\binom{n}{2}$ 个平方项？**

记 $L=\bigl(\sum a_i^2\bigr)\bigl(\sum b_j^2\bigr)$，$R=\bigl(\sum a_ib_i\bigr)^2$——注意二者**都位于恒等式的左端**（左端整体是 $L-R$ 的差，等号右边才是那串平方项）。先用 $n=2$ 把 $L$、$R$ 各自完整展开，看清每一项从哪来。$L$ 是**两个和的乘积**，展开规则是"各取一项相乘、所有组合都要"：

$$
L = (\underbrace{a_1^2 + a_2^2}_{\text{第一个括号取一项}})(\underbrace{b_1^2 + b_2^2}_{\text{第二个括号取一项}}) = \underbrace{a_1^2b_1^2}_{(1,1)} + \underbrace{a_1^2b_2^2}_{(1,2)} + \underbrace{a_2^2b_1^2}_{(2,1)} + \underbrace{a_2^2b_2^2}_{(2,2)}
$$

共 $2\times 2=4$ 项。注意 $(1,2)$ 与 $(2,1)$ 是**两个不同的项**：$a_1^2b_2^2$ 一般不等于 $a_2^2b_1^2$。$R$ 则是**和的平方**，展开同样取所有组合 $(a_ib_i)(a_jb_j)$，但乘法可交换——$(1,2)$ 与 $(2,1)$ 两项数值相同，合并成系数 $2$ 的交叉项：

$$
R = (a_1b_1 + a_2b_2)^2 = \underbrace{a_1^2b_1^2}_{(1,1)} + \underbrace{2a_1b_1a_2b_2}_{(1,2)+(2,1)\text{ 合并}} + \underbrace{a_2^2b_2^2}_{(2,2)}
$$

$L$ 与 $R$ 的展开式相减：对角项 $(1,1)$、$(2,2)$ 一减一零、恰好抵消，只剩

$$
a_1^2b_2^2 + a_2^2b_1^2 - 2a_1b_1a_2b_2 = (a_1b_2 - a_2b_1)^2 .
$$

对一般的 $n$，上面的计算原样照搬——同样是"两边展开、对角项抵消、交叉项凑成完全平方"三步——只是项数从 4 项涨到 $n^2$ 项，无法逐项罗列，于是改为**按下标对分组**处理。$L$ 展开的 $n^2$ 项 $a_i^2b_j^2$ 与 $R$ 展开的 $n^2$ 项 $a_ib_ia_jb_j$ 相减后：

- **对角项**（$i=j$）：$a_i^2b_i^2 - a_i^2b_i^2 = 0$，全部抵消；
- **每个无序对 $\{i,j\}$**（$i<j$）贡献 4 项：$L$ 侧的 $a_i^2b_j^2 + a_j^2b_i^2$（来自乘积展开，两项不同），与 $R$ 侧的 $a_ib_ia_jb_j + a_jb_ja_ib_i = 2a_ib_ia_jb_j$（来自平方的交叉项，两项相同），合成一组恰好凑成完全平方：

$$
a_i^2b_j^2 + a_j^2b_i^2 - 2a_ib_ia_jb_j = (a_ib_j - a_jb_i)^2 .
$$

$n$ 个下标产生 $\binom{n}{2}$ 个无序对，右边就是 $\binom{n}{2}$ 个平方项。这就是那行"交叉项"的来历：$a_i^2b_j^2$ 与 $a_j^2b_i^2$ 来自乘积 $L$ 的展开（两种取法各算一项），$-2a_ib_ia_jb_j$ 来自平方 $R$ 的交叉项（两种顺序合并成系数 $2$）。

**低维验证**：

- $n=2$：$(a_1^2+a_2^2)(b_1^2+b_2^2) - (a_1b_1+a_2b_2)^2 = (a_1b_2-a_2b_1)^2$
  这正是向量 $(a_1,a_2)$ 与 $(b_1,b_2)$ 张成的平行四边形**面积的平方**。

- $n=3$：差距为三个投影面积平方之和：
  $$
  (a_1b_2-a_2b_1)^2 + (a_2b_3-a_3b_2)^2 + (a_3b_1-a_1b_3)^2
  $$

**几何意义**：对向量 $\vec{a}, \vec{b} \in \mathbb{R}^n$，

$$
|\vec{a}|^2 |\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2 = \sum_{i<j}(a_i b_j - a_j b_i)^2 = \det G(\vec{a},\vec{b})
$$

其中 $G(\vec{a},\vec{b})$ 是 $\vec{a}, \vec{b}$ 组成的 Gram 矩阵。**当 $n=3$ 时**，这个和式恰好等于 $|\vec{a}\times\vec{b}|^2$（二维子式正是叉积分量的平方）；对一般的 $n$，没有标准的"叉积"概念，但这个和式仍然是 $|\vec{a}|^2|\vec{b}|^2(1-\cos^2\theta) = |\vec{a}|^2|\vec{b}|^2\sin^2\theta$ 的代数精确表达。Cauchy-Schwarz 只是它 $\ge 0$ 的平凡推论。$\blacksquare$

#### Lagrange 恒等式的完整推导

上面"详解"里讲了**是什么**和**意味着什么**,这里给出**怎么证**——把左边的双重求和一步步展开,凑出右边的 $\binom{n}{2}$ 个平方项。

**目标**:
$$
\underbrace{\left(\sum_{i=1}^{n} a_i^{2}\right)\left(\sum_{j=1}^{n} b_j^{2}\right)}_{L} - \underbrace{\left(\sum_{i=1}^{n} a_i b_i\right)^{2}}_{R} \stackrel{?}{=} \sum_{1 \le i < j \le n}(a_i b_j - a_j b_i)^{2}
$$

**步骤 1:把 $L$ 和 $R$ 都写成双重求和**

$L$ 拆对角线项 + 非对角线项:
$$
L = \sum_{i,j} a_i^{2} b_j^{2} = \underbrace{\sum_{i} a_i^{2} b_i^{2}}_{\text{对角}(i=j)} + \underbrace{\sum_{i \neq j} a_i^{2} b_j^{2}}_{\text{非对角}}
$$

$R$ 同样拆:
$$
R = \sum_{i,j} a_i b_i \cdot a_j b_j = \sum_{i} a_i^{2} b_i^{2} + \sum_{i \neq j} a_i b_i a_j b_j
$$

**步骤 2:$L - R$,对角线项自动抵消**
$$
L - R = \sum_{i \neq j} a_i^{2} b_j^{2} - \sum_{i \neq j} a_i b_i a_j b_j = \sum_{i \neq j}\big(a_i^{2} b_j^{2} - a_i b_i a_j b_j\big)
$$

**步骤 3:对每对 $(i,j)$ 和 $(j,i)$ 配对** (关键一步!)

非对角求和里,$(i,j)$ 和 $(j,i)$ (其中 $i<j$) 贡献合起来:
$$
\big(a_i^{2} b_j^{2} - a_i b_i a_j b_j\big) + \big(a_j^{2} b_i^{2} - a_j b_j a_i b_i\big) = a_i^{2} b_j^{2} + a_j^{2} b_i^{2} - 2 a_i b_i a_j b_j
$$

**正好是完全平方** $(a_i b_j - a_j b_i)^{2}$!

**步骤 4:配对求和即得**
$$
L - R = \sum_{i < j}\big[(a_i b_j - a_j b_i)^{2}\big] \quad \blacksquare
$$

> **小诀窍**:这个证明唯一的技术是"把 $i \neq j$ 拆成 $i<j$ 和 $i>j$ 两半,再配对合并"——记下"配对 $(i,j)/(j,i)$"这个动作,以后推导 Gram 行列式、Plücker 关系时还会反复用到。

#### 矩阵视角(一眼看清结构)

记 $A=(a_1,\ldots,a_n)$,$B=(b_1,\ldots,b_n)$ 为行向量。Lagrange 恒等式可重写为:
$$
\det \begin{pmatrix} A A^{\top} & A B^{\top} \\ B A^{\top} & B B^{\top} \end{pmatrix} = \sum_{i<j}(a_i b_j - a_j b_i)^{2}
$$

左边是 Gram 矩阵的行列式;右边是"外积 $A \wedge B$ 的模方"。这正是 Grassmann 外代数的种子——所以这个恒等式**不只是 Cauchy-Schwarz 的工具,它是现代多重线性代数的开端**。（把 Gram 行列式画成"平行四边形面积的平方"的几何图,见[[topics/math/inequalities/04-multiview#多视角柯西-施瓦茨不等式|多视角·柯西-施瓦茨]]。）

**用矩阵「看出」乘积结果——Cauchy–Binet 读法**。把 $\vec a,\vec b$ 竖着并成 $n\times 2$ 矩阵 $M=\begin{pmatrix}\vec a & \vec b\end{pmatrix}$（按列放）。左边的乘积与内积**先合成一个行列式**：

$$
M^{\top}M=\begin{pmatrix}\vec a\cdot\vec a & \vec a\cdot\vec b\\ \vec a\cdot\vec b & \vec b\cdot\vec b\end{pmatrix},\qquad \det(M^{\top}M)=\|\vec a\|^{2}\|\vec b\|^{2}-(\vec a\cdot\vec b)^{2}
$$

对「2 列」情形用 **Cauchy–Binet 公式**（把 $\det(M^{\top})\det(M)$ 按 Laplace 定理取两行分组展开即得）：

$$
\det(M^{\top}M)=\sum_{1\le i<j\le n}\det\!\begin{pmatrix}a_i & b_i\\ a_j & b_j\end{pmatrix}^{2}=\sum_{i<j}(a_ib_j-a_jb_i)^{2}
$$

于是整条恒等式读作：**乘积一侧先装进 Gram 行列式，Cauchy–Binet 把它自动展开成 $\binom{n}{2}$ 个 $2\times2$ 子式的平方**——右边那串平方项不是硬凑的，是行列式乘法公式的机械输出。等号成立 $\iff$ 所有子式为零 $\iff$ $M$ 的两列成比例（$\vec a\parallel\vec b$），这也是 C-S 取等条件的另一个来源。

**投影面积读法（面积版勾股）**：子式 $\det M_{ij}=a_ib_j-a_jb_i$ 是平行四边形 $\langle\vec a,\vec b\rangle$ 向坐标二平面 $(e_i,e_j)$ **正交投影的带号面积**。恒等式于是说：**平行四边形面积的平方 = 它在所有坐标二平面上投影面积的平方和**——与向量版勾股 $\|v\|^2=\sum_i v_i^2$ 完全同构（一维的"坐标分量"换成二维的"投影面积分量"）。$n=3$ 时三个投影面积恰是 $\vec a\times\vec b$ 的三个分量，这正是 $|\vec a\times\vec b|^2$ 写成三个平方和的原因。

**数值验证（$n=3$）**：$\vec a=(1,2,3)$，$\vec b=(3,2,1)$。$\det G=14\cdot14-10^2=96$；三个子式 $\begin{vmatrix}1&3\\2&2\end{vmatrix}=-4$、$\begin{vmatrix}2&2\\3&1\end{vmatrix}=-4$、$\begin{vmatrix}1&3\\3&1\end{vmatrix}=-8$，平方和 $16+16+64=96$ ✓。

（同一机制放大到 $n$ 个向量，就是 [[topics/math/inequalities/04-multiview#5-升级只有矩阵世界才有的两条行列式不等式|Hadamard 行列式不等式的 Gram 视角]]："体积 $\le$ 棱长之积"。）

#### 历史小注(为什么叫 Lagrange 恒等式)

- **1773, Lagrange**:在研究二次型判别式时,首次明确写出这个恒等式。
- **1821, Cauchy**:用它推出 Cauchy-Schwarz 不等式 (即 $\Delta \le 0$ 的推论)。
- **1844, Grassmann**:把它放进外代数的框架,认识到 $a_i b_j - a_j b_i$ 正是 $\vec{a}\wedge\vec{b}$ 的坐标 —— **多重线性代数的起点**。

> **考研定位**:Lagrange 恒等式本身不直接命题,但它是 **Cauchy-Schwarz 的代数根** + **行列式与向量夹角的桥梁**。掌握它,看到"证 Cauchy-Schwarz"或"求两向量夹角"的题目,你就多一条"用恒等式改写"的解题路径。

---

### 伯努利不等式

> **定理（Bernoulli）** 设 $x > -1$，$r$ 为正整数，则
> $$
> (1+x)^r \ge 1 + rx
> $$
> 等号成立当且仅当 $r=1$ 或 $x=0$。

**含义**：**单利 $\le$ 复利**。把 $1+rx$ 读作"利率 $x$ 存 $r$ 期的单利"，$(1+x)^r$ 读作"逐期滚动的复利"，不等式断言复利永不输给单利。几何上，$y = 1+rx$ 恰是曲线 $y=(1+x)^r$ 在 $x=0$ 处的切线，所以这条不等式的本质是**曲线与切线的上下位置关系**。

> **定义（凸函数）**：设 $f$ 在区间 $I$ 上有定义，若对任意 $x_1, x_2 \in I$ 和任意 $\lambda \in [0,1]$，有
> $$
> f(\lambda x_1 + (1-\lambda) x_2) \le \lambda f(x_1) + (1-\lambda) f(x_2)
> $$
> 则称 $f$ 为 $I$ 上的**凸函数**（几何：弦在曲线上方，如 $y=x^2$ 的碗口向上）；若不等号对 $x_1 \neq x_2$、$0 < \lambda < 1$ 严格成立，则称**严格凸函数**。**凹函数**是反概念（不等号反向，弦在图像下方）。本节的推广与证明二、下一节的琴生，用的都是这条定义；判定方法与常见例子集中放在[琴生一节后的附录](#附凸函数与凹函数的判定)。

**推广（实数指数）**：当 $x > -1$ 时，$(1+x)^r$ 对任意实数 $r$ 都有定义，它与切线 $1+rx$ 的上下关系由 $r(r-1)$ 的符号统一决定：

| 指数 $r$ | $f'' = r(r-1)(1+x)^{r-2}$ 的符号 | 曲线形态 | 结论 |
|:---:|:---:|:---:|:---|
| $r>1$ 或 $r<0$ | $+$ | 凸 | $(1+x)^r \ge 1+rx$ |
| $0<r<1$ | $-$ | 凹 | $(1+x)^r \le 1+rx$ |
| $r=0$ 或 $r=1$ | $0$ | 与切线重合 | 恒等式 $(1+x)^r = 1+rx$ |

前两行的等号当且仅当 $x=0$。一句话记忆：**凸则在切线上方，凹则在切线下方**。

**证明一（数学归纳法，整数情形）**：

*基例* $r=1$：$(1+x)^1 = 1+x$，等号成立。

*归纳假设*：设 $r=k$（正整数）时，对一切 $x > -1$ 有 $(1+x)^k \ge 1+kx$。

*归纳步* $r=k+1$：由 $1+x>0$，可对归纳假设两边同乘正数 $(1+x)$：
$$
\begin{aligned}
(1+x)^{k+1} &= (1+x)^k (1+x) \\
&\ge (1+kx)(1+x) \quad \text{（归纳假设两边同乘 } 1+x>0\text{）} \\
&= 1 + (k+1)x + kx^2 \\
&\ge 1 + (k+1)x \quad \text{（因 } kx^2 \ge 0\text{）}
\end{aligned}
$$
*等号追溯*：基例中 $r=1$ 恒取等；对 $r \ge 2$，归纳步要求 $kx^2 = 0$ 即 $x=0$（且归纳链上每步同理），故等号当且仅当 $r=1$ 或 $x=0$。$\blacksquare$

**证明二（二阶导凸性法，覆盖全部实数 $r$）**：

设 $f(x) = (1+x)^r - (1+rx)$（$x > -1$），连续求导两次：
$$
f'(x) = r(1+x)^{r-1} - r, \qquad f''(x) = r(r-1)(1+x)^{r-2}
$$
由于 $(1+x)^{r-2} > 0$，$f''$ 的符号完全由 $r(r-1)$ 决定，逐一对照上表：

- **$r>1$ 或 $r<0$**：$f'' > 0$，$f$ 严格凸；又 $f'(0)=0$，故 $x=0$ 是唯一的全局最小点，$f(x) \ge f(0) = 0$，等号当且仅当 $x=0$。
- **$0<r<1$**：$f'' < 0$，$f$ 严格凹，$x=0$ 是全局最大点，$f(x) \le f(0) = 0$，即 $(1+x)^r \le 1+rx$（不等号反向），等号同样仅当 $x=0$。
- **$r=0$ 或 $r=1$**：$f \equiv 0$，两边恒等。

一个证明同时给出主定理（正整数 $r$ 是 $r\ge1$ 的特例）与全部推广情形。$\blacksquare$

---

### 琴生不等式

> **前驱**：凸函数定义（[伯努利一节](#伯努利不等式)）
>
> **定理（Jensen）** 设 $f$ 是区间 $I$ 上的凸函数，$x_1, \ldots, x_n \in I$，$\lambda_1, \ldots, \lambda_n > 0$ 且 $\sum \lambda_i = 1$，则
> $$
> f\left(\sum_{i=1}^n \lambda_i x_i\right) \le \sum_{i=1}^n \lambda_i f(x_i)
> $$
> 等号成立条件：若 $f$ 严格凸，则当且仅当 $x_1 = x_2 = \cdots = x_n$；若 $f$ 仅凸，等号当且仅当它在 $[\min x_i,\max x_i]$ 上是仿射函数（形如 $kx+b$）。例如 $f(x)=|x|$，$\lambda_1=\lambda_2=1/2$，$x_1=1,x_2=3$ 时，两边都为 $2$；若改成 $x_1=-1,x_2=1$，则是 $0<1$，不取等。
>
> 若 $f$ 是凹函数，则不等号反向：$f\left(\sum \lambda_i x_i\right) \ge \sum \lambda_i f(x_i)$。

**含义**：凸函数在加权平均点处的值不超过函数值的加权平均。直观图景就是"**弦在曲线上方**"：

![琴生不等式：凸函数的弦在曲线上方](/attachments/images/math/inequalities/jensen-convex.png)

图中加权点 $\lambda x_1+(1-\lambda)x_2$ 处，曲线上的点（红）始终不高于弦上的点（紫）。

**证明（数学归纳法）**：

*基例* $n=2$：由凸函数定义，对任意 $x_1, x_2 \in I$ 和 $\lambda \in (0,1)$，
$$
f(\lambda x_1 + (1-\lambda) x_2) \le \lambda f(x_1) + (1-\lambda) f(x_2)
$$
这正是 $n=2$ 的琴生不等式。

*归纳假设*：假设对 $n=k$ 成立，即对任意 $y_1, \ldots, y_k \in I$ 和满足 $\sum_{i=1}^k \alpha_i = 1$ 的正权重 $\alpha_i$，有
$$
f\left(\sum_{i=1}^k \alpha_i y_i\right) \le \sum_{i=1}^k \alpha_i f(y_i)
$$

*归纳步* $n=k+1$：设 $x_1, \ldots, x_{k+1} \in I$，$\lambda_1, \ldots, \lambda_{k+1} > 0$ 且 $\sum_{i=1}^{k+1} \lambda_i = 1$。

令 $S = \sum_{i=1}^k \lambda_i = 1 - \lambda_{k+1}$，并定义 $\mu_i = \lambda_i / S$（$i=1, \ldots, k$），则 $\sum_{i=1}^k \mu_i = 1$。

记 $y = \sum_{i=1}^k \mu_i x_i$。由凸函数定义（$n=2$ 情形）：
$$
f\left(\sum_{i=1}^{k+1} \lambda_i x_i\right) = f\left(S \cdot y + \lambda_{k+1} \cdot x_{k+1}\right) \le S \cdot f(y) + \lambda_{k+1} f(x_{k+1})
$$

再由归纳假设（取 $y_i = x_i,\; \alpha_i = \mu_i$）：
$$
f(y) = f\left(\sum_{i=1}^k \mu_i x_i\right) \le \sum_{i=1}^k \mu_i f(x_i)
$$

代入上式得：
$$
\begin{aligned}
f\left(\sum_{i=1}^{k+1} \lambda_i x_i\right) &\le S \cdot \sum_{i=1}^k \mu_i f(x_i) + \lambda_{k+1} f(x_{k+1}) \\
&= \sum_{i=1}^k \lambda_i f(x_i) + \lambda_{k+1} f(x_{k+1}) \\
&= \sum_{i=1}^{k+1} \lambda_i f(x_i)
\end{aligned}
$$

等号条件：对严格凸函数，要求归纳假设中的取等号，即 $x_1 = \cdots = x_k = y$；同时要求凸函数定义中的取等号，即 $y = x_{k+1}$。故所有 $x_i$ 相等。$\blacksquare$

**推论（算术平均 $\le$ 均方根）**：
取 $f(x) = x^2$（凸函数），$\lambda_i = 1/n$，得
$$
\left(\frac{a_1 + \cdots + a_n}{n}\right)^2 \le \frac{a_1^2 + \cdots + a_n^2}{n}
$$
即
$$
\frac{a_1 + \cdots + a_n}{n} \le \sqrt{\frac{a_1^2 + \cdots + a_n^2}{n}}
$$

---

#### 附：凸函数与凹函数的判定

凸函数与严格凸的代数定义见伯努利一节（加权平均点处的函数值 $\le$ 函数值的加权平均）。**凹函数**则是相反的概念：弦总在图像**下方**，如 $y=-x^2$ 的拱顶形，定义中不等号反向即可。

**几何直观**：函数 $f$ 是**凸函数** $\Leftrightarrow$ 函数图像上任意两点间的弦总在该两点间函数图像的**上方**（或重合）。用“弦在上、切线在下”记方向，比“向上鼓/向下鼓”更不易混淆；切线说法用于可导情形。

**等价判定方法（考研常用）**：

| 方法 | 条件 | 结论 |
|------|------|------|
| **一阶导数法** | $f'(x)$ 在 $I$ 上单调递增 | $f$ 是凸函数 |
| **二阶导数法** | $f''(x) \ge 0$ 对所有 $x \in I$ | $f$ 是凸函数 |
| **严格凸** | $f''(x) > 0$ | $f$ 是严格凸函数 |

对凹函数，上述条件反向：$f'(x)$ 单调递减 $\Leftrightarrow$ $f''(x) \le 0$。

**常见凸函数例子**：
- $f(x) = x^2$（$f''(x) = 2 > 0$）
- $f(x) = e^x$（$f''(x) = e^x > 0$）
- $f(x) = -\ln x$（$x > 0$，$f''(x) = \frac{1}{x^2} > 0$）
- $f(x) = |x|^p$（$p \ge 1$）

**常见凹函数例子**：
- $f(x) = \ln x$（$x > 0$，$f''(x) = -\frac{1}{x^2} < 0$）
- $f(x) = \sqrt{x}$（$x > 0$，$f''(x) = -\frac{1}{4}x^{-3/2} < 0$）
- $f(x) = \sin x$（在 $[0, \pi]$ 上）

**重要关系**：若 $f$ 是凸函数，则 $-f$ 是凹函数；反之亦然。因此只需记住凸函数的结论，凹函数的不等号反向即可。

---

### Nesbitt 不等式

> **前驱**：[柯西-施瓦茨](#柯西-施瓦茨不等式)、[[topics/math/inequalities/01-basics#均值不等式|AM-GM]]
>
> **定理（Nesbitt）** 对任意正实数 $a,b,c$，
> $$
> \frac{a}{b+c} + \frac{b}{c+a} + \frac{c}{a+b} \ge \frac{3}{2}
> $$
> 等号成立当且仅当 $a=b=c$。

**证明一（对称换元）**：

令 $x = b+c$，$y = c+a$，$z = a+b$，则 $a = \frac{y+z-x}{2}$，$b = \frac{z+x-y}{2}$，$c = \frac{x+y-z}{2}$。显然 $x,y,z > 0$（正数之和）；且 $x+y-z=2c>0$（轮换同理），即[[topics/math/inequalities/01-basics#三角不等式绝对值不等式|三角形不等式]]成立，故 $x,y,z$ 可构成三角形三边。

原式变为：
$$
\sum_{cyc} \frac{y+z-x}{2x} = \frac{1}{2}\sum_{cyc}\left(\frac{y}{x} + \frac{z}{x} - 1\right) = \frac{1}{2}\left(\frac{y}{x}+\frac{z}{x}+\frac{z}{y}+\frac{x}{y}+\frac{x}{z}+\frac{y}{z} - 3\right)
$$

由 AM-GM，$\frac{y}{x}+\frac{x}{y} \ge 2$ 等，故上式
$$
\ge \frac{1}{2}(2+2+2-3) = \frac{3}{2}
$$

$\blacksquare$

**证明二（Cauchy-Schwarz / Titu 引理）**：

先把整条证明链摆出来——两个不等号各司其职，含义随后逐一交代：

$$
\underbrace{\sum_{cyc}\frac{a}{b+c}}_{\text{目标}}
\;\overset{\text{①}}{\ge}\;
\underbrace{\frac{(a+b+c)^{2}}{2(ab+bc+ca)}}_{\text{中间量}}
\;\overset{\text{②}}{\ge}\;
\underbrace{\frac{3}{2}}_{\text{要证的下界}}
$$

- **① 合并分式**：三个分式"各自除"的总和，不小于"分子合并、分母合并后一次除"的商——工具是柯西-施瓦茨的等价形式（**Titu 引理 / Engel 形式**）。它把三个形状杂乱的分式压缩成一个只含 $a+b+c$ 与 $ab+bc+ca$ 的对称中间量，② 才有的放矢。
- **② 估计中间量**：证中间量 $\ge\tfrac32$，化归为 $a^2+b^2+c^2\ge ab+bc+ca$，一步配方即得。

两步的取等条件都是 $a=b=c$，链是紧的：$\tfrac32$ 不只是下界，更是取得到的最小值。

**① 用了什么（Titu 引理）**：对任意实数 $x_i$ 与正数 $y_i$，

$$
\sum_i \frac{x_i^2}{y_i} \;\ge\; \frac{\big(\sum_i x_i\big)^{2}}{\sum_i y_i}
$$

**这条不等号在说什么**：左边是"各除各的"之和——每个分子 $x_i$ 单独按分母 $y_i$ 除一次；右边是"合并后一次除"——分子总额除以分母总额。引理断言**分开除不比合并除便宜**：各比值 $x_i/y_i$ 越参差，左边比右边贵得越多；比值全相等时两种除法恰好等价（口诀「分开除贵，合并除省」的 $p=1$ 版）。

推导只需一行：取向量 $u=\bigl(\frac{x_i}{\sqrt{y_i}}\bigr)$ 与 $v=(\sqrt{y_i})$，C-S 的 $(\sum u_i^2)(\sum v_i^2)\ge(\sum u_iv_i)^2$ 给出

$$
\Big(\sum_i \frac{x_i^2}{y_i}\Big)\Big(\sum_i y_i\Big) \;\ge\; \Big(\sum_i \frac{x_i}{\sqrt{y_i}}\cdot\sqrt{y_i}\Big)^{2} = \big(\sum_i x_i\big)^{2}
$$

交叉项的根号成对约掉，正是这组构造的用意；两边除以 $\sum y_i$ 即得引理。取等 $\iff$ 两向量成比例 $\iff \dfrac{x_1}{y_1}=\cdots=\dfrac{x_n}{y_n}$。

**① 怎么用（关键动作：把每项配成"平方 ÷ 正数"）**：Titu 的分子必须是"某数的平方"，$\dfrac{a}{b+c}$ 不是现成形状；把分子分母**同乘 $a>0$**（分式值不变、分母仍为正）即得 $\dfrac{a}{b+c}=\dfrac{a^2}{a(b+c)}$，再取 $x_i=a,b,c$ 与 $y_i=a(b+c),\,b(c+a),\,c(a+b)$ 代入：

$$
\sum_{cyc} \frac{a}{b+c} = \sum_{cyc} \frac{a^2}{a(b+c)} \ge \frac{(a+b+c)^2}{a(b+c)+b(c+a)+c(a+b)} = \frac{(a+b+c)^2}{2(ab+bc+ca)}
$$

最后一个等号只是把分母展开合并（$ab+ac+bc+ba+ca+cb=2(ab+bc+ca)$）。① 的取等条件是比值全等，即 $\frac{1}{b+c}=\frac{1}{c+a}=\frac{1}{a+b}$（分子分母约去 $a$ 后），亦即 $a=b=c$，与定理一致。

> **为什么同乘 $a$，而不是利用 $a=(\sqrt a)^{2}$ 直接取 $x_i=\sqrt a$、$y_i=b+c$**：后者对引理同样合法，但分子和变成 $\sqrt a+\sqrt b+\sqrt c$，由 [C-S](#柯西-施瓦茨不等式) 反而有 $(\sqrt a+\sqrt b+\sqrt c)^{2}\le 3(a+b+c)$，得到的下界不超过 $\tfrac32$（不均衡时严格更小），② 接不上去。同乘 $a$ 让分子和恰为 $a+b+c$，② 才严丝合缝。**配平方的诀窍：让"分子之和"尽量简单，且取等点对得上题目的对称中心。**

**② 的验证**：只需证 $\dfrac{(a+b+c)^2}{2(ab+bc+ca)} \ge \dfrac{3}{2}$，去分母即 $(a+b+c)^2 \ge 3(ab+bc+ca)$，展开合并即 $a^2+b^2+c^2 \ge ab+bc+ca$，配方即得：

$$
a^2+b^2+c^2-ab-bc-ca=\tfrac{1}{2}\bigl[(a-b)^2+(b-c)^2+(c-a)^2\bigr]\ge 0
$$

② 在且仅在 $a=b=c$ 时取等（三个平方同时为零），与 ① 的取等条件**恰好相同**——整条链在 $a=b=c$ 处同时取等，$\tfrac32$ 是取得到的最小值。$\blacksquare$

（Titu 引理的名称来历、缺口恒等式与使用要点见下方[附：Titu 引理详解](#附titu-引理engel-形式详解)；它也是高阶篇[[topics/math/inequalities/03-advanced#权方和不等式|权方和不等式]]在 $p=1$ 的特例。）

---

#### 附：Titu 引理（Engel 形式）详解

Nesbitt [证明二](#nesbitt-不等式)开头那条"平方 ÷ 正数"的引理值得单独摊开：它是竞赛与考研中出场率最高的 C-S 改写形式，也是连接均值链与权方和的枢纽。本附依次给出：名称来历与等价性、第二个证明（缺口恒等式）、两个特例与谱系、使用配方与失效边界。

**名称与出身**：竞赛圈称 **Titu 引理**——源自罗马尼亚裔美国数学家 Titu Andreescu，他在 IMO 教练生涯与著作中大量使用这一形式；教材多称**柯西-施瓦茨的 Engel 形式**——因德国数学家 Arthur Engel 在《Problem-Solving Strategies》中系统使用而得名；文献里也叫 **Bergström 不等式**。三个名字、一条公式。它与 C-S **等价而非削弱**：上文已用一行构造（向量 $u$、$v$ 代入 C-S）从 C-S 推出它；反过来，在 Titu 中取 $x_i=a_ib_i$、$y_i=b_i^2$（$b_i$ 全不为 $0$；有零分量时先剔除那些坐标——它们对 C-S 两边的贡献本来就是零），得

$$
\sum a_i^2\;\ge\;\frac{\bigl(\sum a_ib_i\bigr)^{2}}{\sum b_i^{2}}
\qquad\Longleftrightarrow\qquad
\bigl(\sum a_ib_i\bigr)^{2}\le\bigl(\sum a_i^{2}\bigr)\bigl(\sum b_i^{2}\bigr),
$$

正是 C-S。同一枚硬币的两面：C-S 是"内积视角"，Titu 是"分式视角"，各有顺手的题型。

> **引理（重述）** 对任意实数 $x_1,\ldots,x_n$ 与**正数** $y_1,\ldots,y_n$：
> $$
> \sum_{i=1}^{n}\frac{x_i^{2}}{y_i}\;\ge\;\frac{\bigl(\sum_{i=1}^{n}x_i\bigr)^{2}}{\sum_{i=1}^{n}y_i}
> $$
> 等号成立 $\iff$ 存在常数 $\lambda$ 使 $x_i=\lambda y_i$（全体 $i$），即 $\dfrac{x_1}{y_1}=\cdots=\dfrac{x_n}{y_n}$。分子可正可负（两边的符号都被平方吸收）；**分母必须全正**——越界的后果见下方「失效边界」。

**证法二（缺口恒等式）**：上文那行构造是证法一（向量代入 C-S）；证法二仿照 [Lagrange 恒等式](#附lagrange-恒等式详解)——不止证"谁大"，还要**精确写出差多少**：

$$
\sum_{i=1}^{n}\frac{x_i^{2}}{y_i}\;-\;\frac{\bigl(\sum_{i=1}^{n}x_i\bigr)^{2}}{\sum_{i=1}^{n}y_i}
\;=\;\frac{1}{\sum_{i=1}^{n}y_i}\sum_{1\le i<j\le n}\frac{(x_iy_j-x_jy_i)^{2}}{y_iy_j}
$$

右边是 $\binom{n}{2}$ 个非负项，不等式与取等条件一并立得（每项为零 $\iff$ $x_iy_j=x_jy_i$ 对一切 $i<j$ $\iff$ 比值全等）。来历仍是 Lagrange 恒等式：把证法一的向量代入，第 $(i,j)$ 项为

$$
u_iv_j-u_jv_i=\frac{x_i}{\sqrt{y_i}}\sqrt{y_j}-\frac{x_j}{\sqrt{y_j}}\sqrt{y_i}=\frac{x_iy_j-x_jy_i}{\sqrt{y_iy_j}},
$$

平方后分母恰为 $y_iy_j$。$n=2$ 手验：左边通分合并，分子 $(x_1y_2-x_2y_1)^{2}$、分母 $y_1y_2(y_1+y_2)$，与公式一致。$\blacksquare$

**同一缺口、两种读法**：记 $r_i=\dfrac{x_i}{y_i}$、$\bar r=\dfrac{\sum x_i}{\sum y_i}$。逐项改写 $\dfrac{(x_iy_j-x_jy_i)^{2}}{y_iy_j}=y_iy_j\,(r_i-r_j)^{2}$，缺口变为 $\dfrac{1}{\sum y_i}\sum_{i<j}y_iy_j(r_i-r_j)^{2}$；再用「成对差之和 $=$ 总权重 $\times$ 加权方差」（与[[topics/math/inequalities/01-basics#切比雪夫不等式|切比雪夫思路二]]所用恒等式同族），它恰等于

$$
\sum_{i=1}^{n}y_i\bigl(r_i-\bar r\bigr)^{2}\;\ge\;0 .
$$

前者按**成对差**累计（Lagrange 风格），后者按**对加权均值的偏差**累计（方差 / [[topics/math/inequalities/04-multiview#多视角琴生不等式|平行轴定理]]风格）——后者正是[[topics/math/inequalities/05-applications#场景四资源分配中的均衡是平均分还是按能力分|场景四（资源分配）]]用过的差值恒等式。于是 Titu 的缺口有了名字：**归一化负载 $r_i$ 的加权离散度**——$r_i$ 越参差，"分开除"比"合并除"贵得越多；取等即负载完全均衡。

**两个特例、一条谱系**：

- **分子全一 → AM-HM**：取 $x_i=1$ 得 $\sum\frac{1}{y_i}\ge\frac{n^{2}}{\sum y_i}$，翻转即 $\dfrac{n}{\sum 1/y_i}\le\dfrac{\sum y_i}{n}$——均值链第一环「调和 $\le$ 算术」正是 Titu 的特例。
- **升幂 → 权方和**：$\sum\frac{a_i^{p+1}}{b_i^{p}}\ge\frac{(\sum a_i)^{p+1}}{(\sum b_i)^{p}}$ 即[[topics/math/inequalities/03-advanced#权方和不等式|权方和不等式]]，Titu 是 $p=1$（习题 [[topics/math/inequalities/06-exercises#b-组进阶结构识别与构造|B2]]、[[topics/math/inequalities/06-exercises#b-组进阶结构识别与构造|B3]] 分别练这两层）。
- **换成积分 → 分式型积分估计**：对 $g>0$，$\displaystyle\int_a^b\frac{f^{2}}{g}\,\mathrm dx\;\ge\;\frac{\bigl(\int_a^b f\,\mathrm dx\bigr)^{2}}{\int_a^b g\,\mathrm dx}$，即[[topics/math/inequalities/05-applications#柯西-施瓦茨积分形式|积分 C-S]]的 Engel 换装。

一句话谱系：**AM-HM —分子全一→ Titu —升幂→ 权方和 —一般化→ Hölder**（推导链方向相反：Hölder ⇒ 权方和 ⇒ Titu ⇒ AM-HM）；而 Titu 与 C-S 一行互推——站在链上任何一层，都能望见柯西。

**使用配方（三步）**：

| 步骤 | 动作 | 自检 |
|:---:|:---|:---|
| ① 认形状 | 分式和求下界 | 每个分母全正（"一正"） |
| ② 配平方 | 把每项改写成 $\dfrac{(\text{某数})^{2}}{\text{正数}}$，必要时分子分母同乘，如 $\dfrac{a}{b+c}=\dfrac{a^{2}}{a(b+c)}$ | 分子同源、其和能算 |
| ③ 套引理 | 得单分式下界 | 取等 $\frac{x_i}{y_i}$ 全等与题设"定值"相容（"二定三相等"） |

**例（同一道题，Titu 为何比 AM-GM 更贴）**：$a,b>0$、$a+b=1$，求 $\dfrac{1}{a}+\dfrac{4}{b}$ 的最小值。

- AM-GM 路线（界是松的）：

$$
\frac{1}{a}+\frac{4}{b}\;\ge\;2\sqrt{\frac{4}{ab}}\;=\;\frac{4}{\sqrt{ab}}\;\ge\;\frac{4}{\sqrt{1/4}}\;=\;8,
$$

  两步取等分别要求 $\frac1a=\frac4b$（即 $b=4a$）与 $ab$ 取到最大（即 $a=b$），互不相容——$8$ 只是取不到的下界。
- Titu 路线（一步到位）：

$$
\frac{1}{a}+\frac{4}{b}=\frac{1^{2}}{a}+\frac{2^{2}}{b}\;\ge\;\frac{(1+2)^{2}}{a+b}=9,
$$

  取等即 $\frac1a=\frac2b$（$b=2a$），与 $a+b=1$ 相容：$a=\frac13$、$b=\frac23$，代入 $3+6=9$ ✓。

AM-GM 并没有用错，只是两次放缩的取等点错位，界被放松；Titu 单步放缩，取等点保得住——这是总纲「每次放缩后重查等号」的活例。

**失效边界**：

- **分母全负 → 方向反转**：取 $y=(-1,-1)$、$x=(1,2)$：左边 $=-5$、右边 $=-\tfrac92$，"≥"不成立。一般做法：令 $z_i=-y_i>0$ 套 Titu 再翻回，得同款公式但方向为 $\le$；取等条件（比值全等）不变。
- **分母混合符号 → 无一般结论**：$y=(1,1,-1)$（$\sum y_i=1$）时，$x=(1,1,0)$：左边 $2$、右边 $4$，"≥"失效；$x=(1,-1,0)$：左边 $2$、右边 $0$，"≥"成立——方向随 $x$ 而变。$y=(1,-1)$ 更使右边分母为零、直接无意义。此时应改用其它工具。
- **分母和无定值 → 只有下界、没有最小值**：引理给出的是表达式形式的界；若题设没有 $a+b=1$ 这类定值把它落成数字，或定值与取等条件不相容，得到的都只是下界——与习题 [[topics/math/inequalities/06-exercises#答案与详解|A1]]「取等点不可达」是同一教训的两副面孔。

> **一句话记忆**：口诀 #11「分开除贵，合并除省」的 $p=1$ 版——分子逐项平方、分母逐项为正，右端一次合并除；取等 $=$ 分子按分母比例分配。识别信号：**分式和求下界**。物理直觉（并联电路按电导分流、总功耗最小）见[[topics/math/inequalities/04-multiview#多视角nesbitt-不等式与-titu-引理|多视角：Nesbitt 与 Titu]]。

---

> ↩ [[topics/math/inequalities|返回总览]]
