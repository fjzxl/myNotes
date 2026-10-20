---
title: 数列与函数极限
tags:
  - math
  - kaoyan
  - math/calculus
---
# 数列与函数极限

> **考纲定位（数一）**：理解极限的概念；理解左极限与右极限的概念及极限存在与左右极限的关系；掌握极限的性质与四则运算法则；掌握极限存在的两个准则（夹逼、单调有界），并会利用它们求极限；掌握用两个重要极限求极限的方法。定义类问题在选择题中直接考"说法辨析"，准则与重要极限是计算题的底层工具。
> 前置：[界与函数](functions-and-bounds.md)（确界、邻域、函数记号）；后续：[无穷小比较与连续](04-05-infinitesimal-continuity.md)、[极限计算综合](06-limit-techniques.md)。导航：[高等数学总览](../calculus.md)。

## 一、为什么需要极限

初等数学能处理"静止"的量，但瞬时速度、曲线在某点的切线斜率、曲边梯形面积都是**变化过程中的终极趋势**。极限就是刻画"无限接近"的精确语言。整个高等数学的地基由三个极限定义铺成：

| 概念 | 定义用到的极限 |
|------|--------------|
| 连续 | $\lim\limits_{x\to x_0}f(x)=f(x_0)$ |
| 导数 | $\lim\limits_{\Delta x\to 0}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$ |
| 定积分 | $\lim\limits_{\lambda\to 0}\sum\limits_{i=1}^{n}f(\xi_i)\Delta x_i$ |

所以这一章的目标不是"会算几个极限"，而是把"无限接近"翻译成可以推理的 $\varepsilon$-语言，并储备两准则、两重要极限这两组核心工具。

## 二、数列极限

### 2.1 定义（ε-N 语言）

$$\lim_{n\to\infty}a_n=A \iff \forall\varepsilon>0,\ \exists N\in\mathbb{N},\ \forall n>N:\ |a_n-A|<\varepsilon$$

逐条拆解（选择题最爱在字眼上做文章）：

- **ε 的任意性**：$\varepsilon$ 是"要多小有多小"的误差标尺。只对某些 $\varepsilon$（如 $\varepsilon=0.1$）找到 $N$ 不够，必须**任意** $\varepsilon>0$ 都行。
- **N 只需存在**：$N$ 依赖 $\varepsilon$（常记 $N(\varepsilon)$），可以放大取整，不要求最小；$N$ 之后**所有**项都落进 $(A-\varepsilon,A+\varepsilon)$——只保证无穷多项不行，"偶尔跑出去"也不行。
- **几何意义**：$A$ 的任意小邻域外至多只有**有限多项**。

### 2.2 用定义证极限（两例核对）

**例 1**：证明 $\lim\limits_{n\to\infty}\dfrac{1}{n}=0$。

对任意 $\varepsilon>0$，要 $\left|\dfrac1n-0\right|=\dfrac1n<\varepsilon$，只需 $n>\dfrac1\varepsilon$。取 $N=\left[\dfrac1\varepsilon\right]+1$，则 $n>N$ 时 $\dfrac1n<\varepsilon$。∎

**例 2**：证明 $\lim\limits_{n\to\infty}\dfrac{2n+1}{3n-1}=\dfrac23$。

先化简差（**找 N 前先放大，把 n 从分母里解放出来**）：

$$\left|\frac{2n+1}{3n-1}-\frac23\right|=\frac{3(2n+1)-2(3n-1)}{3(3n-1)}=\frac{5}{3(3n-1)}\le\frac{5}{3\cdot 2n}=\frac{5}{6n}\quad(n\ge 1)$$

（用了 $3n-1\ge 2n$。）要 $\dfrac{5}{6n}<\varepsilon$ 只需 $n>\dfrac{5}{6\varepsilon}$，取 $N=\left[\dfrac{5}{6\varepsilon}\right]+1$ 即可。∎

放大是 ε-N 证明的核心技巧：不追求最小的 $N$，只求一个够用的界。

### 2.3 收敛数列的性质

| 性质 | 内容 | 证明思路 |
|------|------|---------|
| 唯一性 | 收敛数列极限唯一 | 反证：设极限 $A\ne B$，取 $\varepsilon=\dfrac{\lvert A-B\rvert}2$，则 $n$ 充分大时 $a_n$ 同时落在两个不相交的邻域内，矛盾 |
| 有界性 | 收敛 $\Rightarrow$ 有界 | 取 $\varepsilon=1$：$n>N$ 时 $\lvert a_n\rvert\le\lvert A\rvert+1$，前 $N$ 项取最大者 |
| 保号性 | 若 $A>0$，则从某项起 $a_n>0$（$A<0$ 同理） | 取 $\varepsilon=\dfrac A2$：$n>N$ 时 $a_n>A-\dfrac A2=\dfrac A2>0$ |
| 子列性 | 收敛 $\Rightarrow$ 任何子列收敛于同一极限（完整关系见 [2.4](#24-子列与子列极限)） | 子列下标趋于无穷，仍满足定义 |

反向辨析（高频选择题点）：

- 有界 $\not\Rightarrow$ 收敛：$a_n=(-1)^n$ 有界发散。
- 收敛 $\iff$ **奇、偶子列都收敛且极限相同**（判断发散的利器：奇偶子列极限不同即发散，如 $(-1)^n$；理论依据见 [2.4](#24-子列与子列极限)）。
- 保号性不可倒着用成严格号：$a_n>0$ 只能推出 $A\ge 0$（例：$a_n=\dfrac1n>0$ 但 $A=0$）。

### 2.4 子列与子列极限

> **定义（子列）** 从 $\{a_n\}$ 中按原有顺序挑出无穷多项 $a_{n_1},a_{n_2},\dots$（下标 $n_1<n_2<\cdots$ 严格递增），称为 $\{a_n\}$ 的**子列**，记 $\{a_{n_k}\}$（第 $k$ 项的下标是 $n_k$）。
>
> 基本不等式：$n_k\ge k$（归纳：$n_1\ge1$，且 $n_{k+1}\ge n_k+1$）。它保证 $k\to\infty$ 时 $n_k\to\infty$——"子列走得和全列一样远"的量化形式，也是一切涉及子列下标的放缩起点。

**数列极限与子列极限的关系**（一正、一反、一拼装、一存在）：

| 关系 | 内容 | 典型用法 |
|------|------|---------|
| 正向：全列 ⇒ 子列 | $a_n\to A$ $\Rightarrow$ **任何**子列 $a_{n_k}\to A$ | 整体结论免费平移到子列 |
| 逆否：子列否证全列 | 有一个子列发散，或两个子列收敛于**不同**极限 $\Rightarrow$ 全列发散 | 判发散的主力 |
| 拼装：子列 ⇒ 全列 | 奇、偶子列都收敛且极限相同 $\iff$ 全列收敛（一般地，有限个子列"拼齐"覆盖全列且同敛即可） | 振荡递推数列证收敛 |
| 存在性：致密性定理 | **有界**数列必有收敛子列（Bolzano–Weierstrass） | 理论引擎（见下） |

**证明要点（核对）**：

- **正向**：对 $\varepsilon>0$ 取 $N$ 使 $n>N$ 时 $\lvert a_n-A\rvert<\varepsilon$；当 $k>N$ 时 $n_k\ge k>N$，故 $\lvert a_{n_k}-A\rvert<\varepsilon$——$n_k\ge k$ 在这里干活。
- **拼装的充分性**：对 $\varepsilon>0$ 分别取奇、偶子列的 $N_1,N_2$，令 $N=\max(N_1,N_2)$，则 $n>N$ 时无论奇偶都落进 $(A-\varepsilon,A+\varepsilon)$。
- **逆否**就是反证：若全列收敛于 $A$，则任何子列都 $\to A$，与"某子列发散 / 两子列极限不同"矛盾。

**例 1（核对）**：$(-1)^n$：奇子列恒 $-1\to-1$、偶子列恒 $1\to1$，两个子列极限不同 ⇒ 发散。

**例 2（核对）**：$a_n=\sin\dfrac{n\pi}2$ 取值 $1,0,-1,0,\dots$ 循环：偶子列恒 $0\to0$ 收敛，奇子列 $1,-1,1,-1,\dots$ 发散——**一个发散子列**就足以判死全列。

**例 3（核对）**：$a_n=n^{(-1)^n}=1,2,\tfrac13,4,\tfrac15,\dots$：奇子列 $\to0$、偶子列 $\to+\infty$。它**无界**但不趋于无穷（$a_n\to+\infty$ 要求从某项起**全部**项都任意大）——"无界 $\ne$ 无穷大"的标准反例，无穷大量的语言见 `04-05`。

**例 4**：振荡递推 $a_{n+1}=1+\dfrac1{a_n}$（4.2 节）：全列不单调，但奇、偶子列各自单调有界且极限同为黄金比 $\dfrac{1+\sqrt5}2$，拼装得全列收敛——"拼装"关系的实战。

**致密性定理（Bolzano–Weierstrass，数列版聚点定理）**

> **定理** 有界数列必有收敛子列。

- **证明思路一（二分 + 闭区间套，核对）**：设 $\{a_n\}\subset[a,b]$。每次把当前区间对半分，必有一半含有**无穷多项**，取其为新区间，得嵌套、长度趋于零的闭区间列；由[闭区间套定理](functions-and-bounds.md#14-闭区间套定理)得公共点 $\xi$。再依次在第 $k$ 个区间 $[c_k,d_k]$ 内挑出下标递增的项 $a_{n_k}$（无穷多项保证挑得动），由 $c_k\le a_{n_k}\le d_k$ 且 $c_k,d_k\to\xi$，用[夹逼准则](../../../notes/squeeze-theorem.md)得 $a_{n_k}\to\xi$。∎
- **证明思路二（单调子列引理）**：任何数列都有单调子列——称 $n$ 为**峰值点**，若 $a_n\ge a_m$ 对一切 $m>n$ 成立；峰值点无穷多时依次取峰值点得递减子列，否则最后一个峰值点之后每一项右侧总有更大者，得递增子列。配上单调有界准则即收敛。这条路不用区间套——两条路合起来再次演示完备性家族内部的互推。
- **定位**：它就是[界与函数](functions-and-bounds.md) 1.3 节完备性家族中"聚点定理"的数列版本；[04-05](04-05-infinitesimal-continuity.md) 里闭区间上连续函数**有界性定理**的反证法（"无界点列压缩出收敛子列，与连续性矛盾"）用的正是它。
- **配套事实**：无界数列必有 $\lvert a_{n_k}\rvert\to+\infty$ 的子列（对每个 $k$ 取下标递增、绝对值超过 $k$ 的项——若取不动，前有限项加界 $k$ 就把全列框死了）。与致密性合起来读：**任何数列要么有收敛子列、要么有趋于无穷的子列**（两者可以兼有，如例 3）。

**术语**：收敛子列的极限称为数列的**极限点**。数一不考这个词，但见到"聚点、极限点"应能翻译成"某个子列的极限"。

**考研定位**：奇偶子列判别是选择 / 判断题常客；"无界 $\ne$ 无穷大"（例 3）反复出现；致密性定理不考证明，但二分、抽子列的思想是存在性证明题的背景板。函数版对应物是 4.3 节归结原则——"找两条数列"就是子列思想借道 Heine 定理攻打函数极限。

## 三、函数极限

### 3.1 自变量趋于有限点：ε-δ 语言

$$\lim_{x\to x_0}f(x)=A \iff \forall\varepsilon>0,\ \exists\delta>0,\ \forall x:\ 0<|x-x_0|<\delta \Rightarrow |f(x)-A|<\varepsilon$$

三个关键点：

- **去心**：$0<|x-x_0|$ 表示 $x\ne x_0$——极限关心**趋势**，与 $f$ 在 $x_0$ 点有没有定义、取什么值无关。分段函数在分界点、$\dfrac{\sin x}{x}$ 在 $x=0$ 处都因此可以谈极限。
- **δ 依赖 ε**，且通常可以缩小（取更小的 δ 当然更够用）。
- 与数列版对照：把"离散的 $n>N$"换成"连续的 $0<|x-x_0|<\delta$"。

**例（核对）**：证明 $\lim\limits_{x\to 2}(3x-1)=5$。

$|3x-1-5|=3|x-2|$，要其 $<\varepsilon$ 只需 $|x-2|<\dfrac\varepsilon3$，取 $\delta=\dfrac\varepsilon3$。∎

### 3.2 左极限与右极限

$$f(x_0^-)=\lim_{x\to x_0^-}f(x)\quad(\text{只用左侧 } x<x_0\text{ 的值}),\qquad f(x_0^+)=\lim_{x\to x_0^+}f(x)\quad(\text{只用右侧})$$

**核心定理**：$\lim\limits_{x\to x_0}f(x)=A\iff f(x_0^-)=f(x_0^+)=A$。

**证明（核对）**：

- (⇒) 全极限的 $\delta$ 对单侧自然够用：$0<\lvert x-x_0\rvert<\delta$ 蕴含 $0<x_0-x<\delta$（左侧）和 $0<x-x_0<\delta$（右侧），两个单侧定义同时成立。
- (⇐) 对 $\varepsilon>0$，由 $f(x_0^-)=A$ 得 $\delta_1$（左半边落进 $(A-\varepsilon,A+\varepsilon)$），由 $f(x_0^+)=A$ 得 $\delta_2$；取 $\delta=\min(\delta_1,\delta_2)$，则 $0<\lvert x-x_0\rvert<\delta$ 时无论左右都落进该邻域。∎

读法上它锁定**两件事**：左右极限**都存在**，且**相等**——只要有一个不存在（如 $e^{1/x}$ 的右极限）或都存在但不等（如 $\dfrac{\lvert x\rvert}{x}$），极限就不存在。四条充要条件的全貌见 [3.7](#37-函数极限的充要条件汇总)。

什么时候**必须**分左右：分段函数分界点；含 $\lvert x-a\rvert$、$\operatorname{sgn}$；以及 $x\to 0$ 时的 $e^{1/x}$、$\arctan\dfrac1x$（左右行为天然不对称）。

| 函数（$x\to 0$） | 左极限 | 右极限 | 结论 |
|---|---|---|---|
| $\dfrac{\lvert x\rvert}{x}$ | $-1$ | $1$ | 极限不存在 |
| $e^{1/x}$ | $e^{-\infty}=0$ | $+\infty$ | 极限不存在 |
| $\arctan\dfrac1x$ | $-\dfrac\pi2$ | $\dfrac\pi2$ | 极限不存在 |

（$e^{1/x}$ 一行核对：$x\to 0^-$ 时 $\dfrac1x\to-\infty$，$e^{1/x}\to 0$；$x\to 0^+$ 时 $\dfrac1x\to+\infty$，指数爆炸。）

### 3.3 自变量趋于无穷：ε-X 语言

$$\lim_{x\to\infty}f(x)=A \iff \forall\varepsilon>0,\ \exists X>0,\ \forall x:\ |x|>X \Rightarrow |f(x)-A|<\varepsilon$$

**例（核对）**：$\lim\limits_{x\to+\infty}\dfrac{2x^2+1}{x^2+3}=2$：$\left|\dfrac{2x^2+1}{x^2+3}-2\right|=\dfrac5{x^2+3}<\dfrac5{x^2}<\varepsilon$，只需 $x>\sqrt{\dfrac5\varepsilon}$，取 $X=\sqrt{5/\varepsilon}$。∎

$x\to+\infty$、$x\to-\infty$ 与 $x\to\infty$ 的关系同样是"双单合一"：$\lim\limits_{x\to\infty}$ 存在 $\iff$ 正负两个方向分别存在且相等（证明与 3.2 同款：(⇐) 取 $X=\max(X_+,X_-)$，$\lvert x\rvert>X$ 时 $x>X_+$ 或 $x<-X_-$，两种情况都已覆盖）。

### 3.4 六种极限过程与性质总表

| 过程 | 语言骨架 | 挑战量 |
|------|---------|--------|
| $n\to\infty$ | $\forall\varepsilon\,\exists N\,\forall n>N$ | 离散、单侧 |
| $x\to x_0$ / $x_0^-$ / $x_0^+$ | $\forall\varepsilon\,\exists\delta\,\forall 0<\lvert x-x_0\rvert<\delta$（附单侧不等号） | 去心邻域 |
| $x\to\infty$ / $+\infty$ / $-\infty$ | $\forall\varepsilon\,\exists X\,\forall\lvert x\rvert>X$ | 无穷远处 |

函数极限的性质与数列版平行，但都带"**局部**"二字（只在 $x_0$ 的某去心邻域内成立）：

- **局部有界**：极限存在 $\Rightarrow$ 在某去心邻域内有界。（注意方向：有界推不回极限。）
- **局部保号**：$A>0\Rightarrow$ 某去心邻域内 $f(x)>\dfrac A2>0$；反之 $f(x)>0$ 只能推出 $A\ge0$。
- **保序性**：某去心邻域内 $f(x)\ge g(x)$ 且两极限存在 $\Rightarrow \lim f\ge\lim g$。**严格不等号取极限后要降级为 $\ge$**：$x^2>0$（$x\ne0$）但 $\lim\limits_{x\to0}x^2=0$，不是 $>0$。

### 3.5 极限与无穷小的关系

$$\lim_{x\to x_0}f(x)=A \iff f(x)=A+\alpha(x),\quad \lim_{x\to x_0}\alpha(x)=0$$

**证明（核对）**：记 $\alpha(x)=f(x)-A$，则 $\lvert\alpha(x)\rvert<\varepsilon$ 与 $\lvert f(x)-A\rvert<\varepsilon$ 是**同一个不等式**——两个方向的 $\varepsilon$-$\delta$ 验证逐字相同。∎

这是把"求极限"改写成"估计误差"的桥梁，也是后续一切无穷小运算（比较、等价替换，见 `04-05`）的起点；泰勒展开"多项式主部 + 无穷小余项"（[06 §3.2](06-limit-techniques.md#32-泰勒展开法)）正是这一分解的升级版。

### 3.6 四则运算法则

若 $\lim f=A$、$\lim g=B$（**同为有限数**），则

$$\lim[f\pm g]=A\pm B,\qquad \lim[fg]=AB,\qquad \lim\frac fg=\frac AB\ (B\ne0)$$

注意三条红线：拆开的每一部分都必须**存在且有限**；除法分母极限非零；"先拆后算"失败时（如 $\dfrac{\sin x}{x}$ 在 $x\to0$，分子分母极限都是 0）要改用重要极限、等价替换或洛必达——这正是 [极限计算方法综合](06-limit-techniques.md) 的主题。

### 3.7 函数极限的充要条件汇总

四条刻画，各司其职（以 $x\to x_0$ 为例，其余极限过程照搬；数列版对应物见 [2.4](#24-子列与子列极限)）：

| 刻画 | 内容 | 证明位置 | 主要用途 |
|------|------|---------|---------|
| 定义（ε-δ） | $\lim\limits_{x\to x_0}f(x)=A$ 的定义本身就是一条充要条件 | §3.1 | 严格证明、一切理论推理的最终依据 |
| 单侧合一 | $\lim\limits_{x\to x_0}f(x)=A\iff f(x_0^-)=f(x_0^+)=A$；$x\to\infty$ 版：正负两方向分别存在且相等 | §3.2、§3.3 | 分段点、单侧不对称函数：把存在性拆成两个单侧计算 |
| 数列刻画（Heine） | $\lim\limits_{x\to x_0}f(x)=A\iff$ 对任意 $x_n\to x_0\ (x_n\ne x_0)$ 都有 $f(x_n)\to A$ | §4.3 | 判极限**不存在**（两条数列）；数列结论平移到函数 |
| 无穷小分解 | $\lim\limits_{x\to x_0}f(x)=A\iff f(x)=A+\alpha(x),\ \alpha\to0$ | §3.5 | 化极限为误差估计；等价替换与泰勒的理论起点 |

三条辨析（选择题改写字眼的高发区）：

- **"存在"与"等于 $A$"**：每条刻画都同时锁定两件事。单侧版本单独读：极限**存在** $\iff$ 左右极限**都存在且相等**，缺一即死——$e^{1/x}$ 在 $0$ 处右极限不存在，$\dfrac{\lvert x\rvert}{x}$ 在 $0$ 处两侧都存在但不等，结局相同。
- **"任意"二字**（Heine）：只验证部分数列不算数——$e^{1/x}$ 沿一切 $x_n\to0^-$ 都有 $f(x_n)\to0$，但极限仍不存在（右侧路径作废，详见 4.3）。
- **必要条件 $\ne$ 充要条件**：局部有界、局部保号只是极限存在的**必要**条件，不能倒着用——$\sin\dfrac1x$ 在 $0$ 的任何去心邻域内有界（$\lvert f\rvert\le1$），但极限不存在（§4.3 例）。

**拓展（数一不考，选读）**：数学分析还给出一条**不预设极限值 $A$** 的存在性充要条件——**柯西准则**：$\lim\limits_{x\to x_0}f(x)$ 存在 $\iff \forall\varepsilon>0,\ \exists\delta>0$，对去心邻域内**任意两点** $x_1,x_2$ 都有 $\lvert f(x_1)-f(x_2)\rvert<\varepsilon$——"函数值彼此任意接近"，全程不提极限是多少。它与数列版柯西准则平行，同属实数完备性家族（[functions-and-bounds](functions-and-bounds.md) 1.3 节），价值在于理论上证明存在而无需先猜出极限值。

**例（核对）**：求 $f(x)=\begin{cases}\dfrac{\sin x}{x},& x<0,\\[2pt] x+1,& x>0\end{cases}$ 在 $x\to0$ 处的极限。

左：$x\to0^-$ 时 $\dfrac{\sin x}x\to1$（§5.1）；右：$x\to0^+$ 时 $x+1\to1$。左右都存在且相等，由单侧刻画 $\lim\limits_{x\to0}f(x)=1$（$f$ 在 $0$ 无定义，与极限无关）。∎

分段点求极限的标准流程：**单侧合一拆开算；两侧不等或一侧不存在即判死；振荡型（$\sin\dfrac1x$ 这类左右都谈不拢的）交给 Heine 取两条数列**。

## 四、极限存在准则

### 4.1 夹逼准则

**数列版**：$y_n\le x_n\le z_n$（$n$ 充分大），且 $y_n\to A,\ z_n\to A$，则 $x_n\to A$。函数版把 $n$ 换成 $x$ 完全平行。

**证明思路**：对任意 $\varepsilon>0$，取 $N=\max(N_y,N_z)$，$n>N$ 时 $A-\varepsilon<y_n\le x_n\le z_n<A+\varepsilon$。

**适用信号**：求和/乘积的项数随 $n$ 变化（无法逐项取极限），且各项容易放缩出共同的上下界。

**例 1（核对）**：求 $\lim\limits_{n\to\infty}\left(\dfrac{1}{\sqrt{n^2+1}}+\dfrac{1}{\sqrt{n^2+2}}+\cdots+\dfrac{1}{\sqrt{n^2+n}}\right)$。

$n$ 项之和，每项介于 $\dfrac{1}{\sqrt{n^2+n}}$ 与 $\dfrac{1}{\sqrt{n^2+1}}$ 之间，故

$$\frac{n}{\sqrt{n^2+n}}\le S_n\le \frac{n}{\sqrt{n^2+1}},\qquad \text{两端都}\to\frac{n}{n}=1\ (n\to\infty)$$

由夹逼，$S_n\to 1$。∎

**例 2（核对）**：证明 $\lim\limits_{n\to\infty}\dfrac{n!}{n^n}=0$。

$0<\dfrac{n!}{n^n}=\dfrac1n\cdot\dfrac2n\cdots\dfrac nn\le\dfrac1n\to 0$（其余因子均 $\le 1$），夹逼得 0。∎

### 4.2 单调有界准则

**内容**：单调递增且有上界的数列必收敛（递减有下界同理）。

**理论根基**：上确界存在定理（[界与函数](functions-and-bounds.md)）——递增有上界，极限就是那个上界的上确界。这是实数系完备性的直接体现（有理数系中单调有界数列可以没有极限，如 $\sqrt2$ 的不足近似值列）。完备性家族的另一位成员——[闭区间套定理](functions-and-bounds.md#14-闭区间套定理)——的证明恰好用到单调有界定理，而它的"二分法"又是闭区间上连续函数那组定理（`04-05`）的标准证明引擎。

**适用信号**：递推数列 $a_{n+1}=f(a_n)$。标准三步：

1. 归纳证**有界**（猜界：先算前几项观察，或对递推式两边取"拟极限"解出候选值）；
2. 归纳证**单调**（作差 $a_{n+1}-a_n$ 或作商 $\dfrac{a_{n+1}}{a_n}$，配合归纳假设）；
3. 递推式两边**取极限**，解方程得 $L$（正负号由保号性/实际范围筛选）。

**例（核对）**：$a_1=\sqrt2$，$a_{n+1}=\sqrt{2+a_n}$，证明 $\{a_n\}$ 收敛并求极限。

有界：$a_1=\sqrt2<2$；若 $a_n<2$ 则 $a_{n+1}=\sqrt{2+a_n}<\sqrt4=2$。归纳得 $a_n<2$。
单调：$a_2=\sqrt{2+\sqrt2}>\sqrt2=a_1$；若 $a_{n+1}>a_n$，则 $a_{n+2}=\sqrt{2+a_{n+1}}>\sqrt{2+a_n}=a_{n+1}$。归纳得递增。
（也可作差：$a_{n+1}-a_n=\dfrac{a_n-a_{n-1}}{\sqrt{2+a_n}+\sqrt{2+a_{n-1}}}$，分子分母同号传递。）
由单调有界准则收敛，设极限为 $L$。递推式取极限：$L=\sqrt{2+L}\Rightarrow L^2-L-2=0\Rightarrow L=2$ 或 $-1$；由 $a_n>0$ 及保号性 $L\ge0$，故 $L=2$。∎

**易错提醒**：$a_{n+1}=1+\dfrac1{a_n}$（$a_1=1$）这类序列**整体不单调**（$1,2,\tfrac32,\tfrac53,\tfrac85,\dots$ 在极限 $(\tfrac{1+\sqrt5}2)$ 两侧振荡）。此时单调有界准则不能直接对全列用，应考察**奇、偶子列**各自单调有界、极限相等；或证明 $|a_{n+1}-L|\le q\,|a_n-L|$（$0<q<1$，压缩映射思想）后夹逼。振荡型递推是判别题的常设陷阱（子列工具的完整版见 [2.4](#24-子列与子列极限)）。

### 4.3 归结原则（Heine 定理）

**内容**：$\lim\limits_{x\to x_0}f(x)=A\iff$ 对**任意**满足 $x_n\to x_0,\ x_n\ne x_0$ 的数列，都有 $f(x_n)\to A$。

两个方向的用法：

- **正用**（函数极限存在）：数列极限的结论可以平移到函数极限，是桥梁。
- **反用**（证明函数极限**不存在**）：找两条都趋于 $x_0$ 的数列，使 $f$ 沿它们趋向不同的值。

**证明思路（核对）**：

- (⇒) 对 $\varepsilon>0$ 取 $\delta$；由 $x_n\to x_0$ 且 $x_n\ne x_0$，$n$ 充分大时 $0<\lvert x_n-x_0\rvert<\delta$，代入即 $\lvert f(x_n)-A\rvert<\varepsilon$。
- (⇐) 逆否构造：设 $x\to x_0$ 时 $f(x)\not\to A$，则存在 $\varepsilon_0>0$，使**每个** $\delta>0$ 都挡不住某个越界点——形式化：$\exists\varepsilon_0>0,\ \forall\delta>0,\ \exists x:\ 0<\lvert x-x_0\rvert<\delta$ 且 $\lvert f(x)-A\rvert\ge\varepsilon_0$。逐次取 $\delta=\dfrac1n$，挑出 $x_n$，得 $x_n\to x_0$、$x_n\ne x_0$，但 $\lvert f(x_n)-A\rvert\ge\varepsilon_0$ 使 $f(x_n)\not\to A$——"坏数列"是被亲手造出来的。∎

**"任意"二字不可放松**：只对**部分**数列验证成功毫无用处——$e^{1/x}$ 沿一切 $x_n\to 0^-$ 都有 $f(x_n)\to 0$（$1/x_n\to-\infty$），但 $\lim\limits_{x\to0}e^{1/x}$ 仍不存在（右侧路径爆炸）。Heine 要求的是**所有**逼近路径齐步走。

**例（核对）**：证明 $\lim\limits_{x\to0}\sin\dfrac1x$ 不存在。

取 $x_n=\dfrac{1}{2n\pi+\pi/2}\to0$，$f(x_n)=\sin\left(2n\pi+\dfrac\pi2\right)=1\to1$；
取 $y_n=\dfrac{1}{2n\pi}\to0$，$f(y_n)=\sin 2n\pi=0\to0$。
两条路径极限不同，由归结原则，极限不存在。∎

（这道题用左右极限不行——左右两侧都振荡；"取两条数列"——把 [2.4](#24-子列与子列极限) 的子列思想借道 Heine 定理搬到函数上——才是对付振荡的武器。）

## 五、两个重要极限

### 5.1 第一重要极限：$\lim\limits_{x\to 0}\dfrac{\sin x}{x}=1$

**证明（夹逼，核对）**：设 $0<x<\dfrac\pi2$，在单位圆中比较（圆心角 $x$）：弦 $\sin x$ < 弧 $x$ < 切线段 $\tan x$。除以 $\sin x>0$：

$$1<\frac{x}{\sin x}<\frac{1}{\cos x}\quad\Longleftrightarrow\quad \cos x<\frac{\sin x}{x}<1$$

$x\to 0^+$ 时 $\cos x\to1$，夹逼得右极限为 1；$\dfrac{\sin x}{x}$ 是偶函数，左极限同为 1。∎

**使用要点**：

- 结构是 $\dfrac{\sin \square}{\square}\to1$，方块必须**趋于 0** 且处处是同一个方块。$x\to\infty$ 时 $\dfrac{\sin x}x\to0$（有界除以无穷大），不是 1。
- 极限里的三角函数用的是**弧度制**（证明依赖"弧长 = 半径 × 弧度"）。

**例（核对）**：$\lim\limits_{x\to0}\dfrac{\sin 3x}{\tan 5x}=\dfrac35\cdot\dfrac{\sin 3x}{3x}\cdot\dfrac{5x}{\tan 5x}=\dfrac35\cdot1\cdot1=\dfrac35$。∎

### 5.2 第二重要极限：$\lim\limits_{n\to\infty}\left(1+\dfrac1n\right)^n=e$

**单调性的证明思路（均值不等式，核对）**：取 $n$ 个 $\left(1+\dfrac1n\right)$ 与 1 个 $1$，由 [均值不等式](../inequalities.md)（AM-GM）：

$$\sqrt[n+1]{\left(1+\tfrac1n\right)^n\cdot 1}\ \le\ \frac{n\left(1+\tfrac1n\right)+1}{n+1}=\frac{n+2}{n+1}=1+\frac1{n+1}$$

两边 $n+1$ 次方：$\left(1+\dfrac1n\right)^n\le\left(1+\dfrac1{n+1}\right)^{n+1}$，即单调递增。

**有界性**：二项展开后每项放大，

$$\left(1+\tfrac1n\right)^n=\sum_{k=0}^n\frac1{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k}\le\sum_{k=0}^n\frac1{k!}\le 1+\sum_{k=1}^{\infty}\frac1{2^{k-1}}=3$$

（用 $k!\ge 2^{k-1}$。）单调递增有上界，由单调有界准则极限存在，记作 $e\approx2.71828$。∎

连续版本：$\lim\limits_{x\to\infty}\left(1+\dfrac1x\right)^x=e$，配套代换 $\lim\limits_{\alpha\to0}(1+\alpha)^{1/\alpha}=e$。

**使用要点**：

- 结构特征：$1^{\infty}$ 型未定式（底趋于 1，指数趋于无穷）。
- 通用套路（$1^\infty$ 快算法）：若 $\varphi\to1$、$\psi\to\infty$，则 $\varphi^\psi\to e^{\lim\psi(\varphi-1)}$。

**例 1（核对）**：$\lim\limits_{n\to\infty}\left(1+\dfrac2n\right)^{3n}$：$\psi(\varphi-1)=3n\cdot\dfrac2n=6$，故为 $e^6$。
（硬凑验证：$\left(1+\dfrac2n\right)^{3n}=\left[\left(1+\dfrac{2}{n}\right)^{n/2}\right]^{6}\to e^6$。）∎

**例 2（核对）**：$\lim\limits_{x\to\infty}\left(\dfrac{x+2}{x-1}\right)^x$：底 $=\ 1+\dfrac3{x-1}\to1$，$\psi(\varphi-1)=x\cdot\dfrac3{x-1}\to3$，故为 $e^3$。∎

## 六、题型与方法总结

| 目标 | 方法 | 信号 |
|------|------|------|
| 证明极限为某值 | ε-N / ε-δ 定义（先放大再解不等式） | 题干直接给极限值 |
| 判断极限不存在 | ① 左右极限不等；② 归结原则取两条数列；③ 无界 | 分段点、$\lvert x\rvert$、$e^{1/x}$、振荡因子 |
| 分段点求极限 | 单侧合一：左右分别算，都存在且相等即极限（[3.7](#37-函数极限的充要条件汇总)） | 分界点、$\lvert x-a\rvert$ 类 |
| 判断数列发散 | ① 奇偶子列极限不同；② 找一个发散子列；③ 无界 | $(-1)^n$、$\sin\dfrac{n\pi}2$、$n^{(-1)^n}$ |
| 和式/积式（项数变动） | 夹逼 | $\sum_{i=1}^n$、$\prod$，各项可整体放缩 |
| 递推数列 | 单调有界三步；振荡则看奇偶子列或压缩 | $a_{n+1}=f(a_n)$ |
| $\dfrac{\sin\square}{\square}$ | 第一重要极限 + 恒等变形 | $\square\to0$ |
| $1^\infty$ | 第二重要极限 / $e^{\lim\psi(\varphi-1)}$ | 庞大指数、底→1 |

## 七、易错点清单

- **ε-N 逻辑**："存在一个 ε" ❌，必须任意 ε；N 后允许个别项越界 ❌，必须全部。
- **去心邻域**：$f$ 在 $x_0$ 无定义不妨碍极限存在；极限存在也不说明 $f(x_0)$ 等于极限（那是连续，`04-05`）。
- **严格不等号取极限降级**：$f>g$ 只能推出 $\lim f\ge\lim g$。
- **保号性的方向**：$A>0\Rightarrow$ 局部 $f>0$ ✔；局部 $f>0\Rightarrow A>0$ ❌（只能 $A\ge0$）。
- **$\dfrac{\sin x}x=1$ 的适用域**：必须 $x\to0$；$x\to1$ 时极限是 $\sin 1$，$x\to\infty$ 时是 0。
- **充要条件的字眼**：单侧合一要求左右**都存在且相等**（一侧不存在、或两侧不等，同样判死）；Heine 要求对**任意**数列成立，只验证部分路径不算数（$e^{1/x}$ 沿左侧一切数列都 $\to0$，极限仍不存在）。
- **$e^{1/x}$、$\arctan\dfrac1x$ 在 $x\to0$**：必分左右，两侧行为不对称是常态不是例外。
- **有界 vs 收敛**：收敛⇒有界，有界⇏收敛，单调+有界⇒收敛；三对关系选择题反复考。
- **子列收敛 ⇏ 全列收敛**：$(-1)^n$ 的奇、偶子列各自收敛而全列发散；判全列要么奇偶拼装，要么单调有界 / 夹逼。
- **四则拆分前提**：每部分极限存在且有限、除式分母极限非零；拆不动时换工具（`06`）。
- **递推数列不单调**就贸然用单调有界准则（振荡型要先处理成单调子列）。
- **夹逼的上下界必须收敛到同一个值**，否则夹而不逼。

## 八、与其他笔记的联系

- [functions-and-bounds](functions-and-bounds.md) —— 前置：确界存在定理是单调有界准则的根；邻域与函数记号在这里定义。
- [inequalities](../inequalities.md) —— 放缩工具：AM-GM 证 $e$ 的单调性；夹逼的界全靠不等式。
- [04-05-infinitesimal-continuity](04-05-infinitesimal-continuity.md)：无穷小比较、等价替换（把本文两个重要极限工具化）、连续与间断。
- [06-limit-techniques](06-limit-techniques.md)：极限计算题型总攻略（泰勒、洛必达预置；变限积分等在 Ch2/Ch3 学完后回填）；章级复习见 [ch1-review](ch1-review.md)。
- [导数](07-derivative.md)与定积分（`18`）的定义直接引用本文的极限语言。

## 附：自测清单

- [ ] 能默写 ε-N、ε-δ、ε-X 三种定义，并指出各自的"任给 / 存在 / 对所有"结构
- [ ] 能用放大法完成一道 ε-N 证明（如例 2），并解释"为什么放大不影响正确性"
- [ ] 能列出必须分左右极限的三类典型函数并算对 $e^{1/x}$、$\arctan\frac1x$ 在 $x\to0$ 的四个单侧极限
- [ ] 能默写函数极限的四条充要条件（ε-δ 定义、单侧合一、Heine、无穷小分解）并各举一个用途；能叙述单侧合一与 Heine(⇐) 的证明思路
- [ ] 能叙述并证明（思路）夹逼准则、单调有界准则；说明单调有界准则与确界存在定理的关系
- [ ] 能独立完成 $a_{n+1}=\sqrt{2+a_n}$ 的三步论证；能说出 $a_{n+1}=1+\frac1{a_n}$ 为何不能直接套
- [ ] 能用归结原则证明 $\lim_{x\to0}\sin\frac1x$ 不存在
- [ ] 能证明两个重要极限（思路），并用 $e^{\lim\psi(\varphi-1)}$ 秒杀 $1^\infty$ 型
- [ ] 能背出易错点清单中"有界/收敛/单调"的三对关系
- [ ] 能默写数列极限与子列的四条关系（正向平移、逆否判发散、奇偶拼装、致密性定理），并用它们判定 $(-1)^n$、$\sin\frac{n\pi}2$ 发散
