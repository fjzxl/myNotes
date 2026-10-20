---
title: 不等式 · 四、证明：高阶不等式
tags:
  - math
  - math/inequality
  - kaoyan
---

> 📚 本文是 [不等式](../inequalities.md) 的第 3 / 6 章（总览第四部分）。 上一章：[三、证明：核心工具不等式](02-core-tools.md) 下一章：[五、多视角理解：向量·矩阵·几何·物理](04-multiview.md)

# 四、证明：高阶不等式

> 🎯 **证明篇 ③ · 拔高**：这一组是 Young → Hölder → 权方和/Minkowski 的递推链，相互依赖。
> 考研大纲对 Young/Hölder 较陌生，但竞赛中常考，建议理解为主。
> 各不等式的积分形式集中在[六、应用的积分形式一节](05-applications.md#积分形式)。

### Young 不等式

> **前驱**：[琴生不等式](02-core-tools.md#琴生不等式)（用 $e^x$ 的凸性）
>
> **定理（Young）** 设 $a,b \ge 0$，$p > 1$，$q > 1$ 且 $\dfrac{1}{p} + \dfrac{1}{q} = 1$，则
> $$
> ab \le \frac{a^p}{p} + \frac{b^q}{q}
> $$
> 等号成立当且仅当 $a^p = b^q$。

> **三问**：固定 共轭指数 $p,q$（$\frac1p+\frac1q=1$）｜比较 乘积 $ab$ 与 两项分摊 $\frac{a^p}{p}+\frac{b^q}{q}$｜取等 $a^p=b^q$

**含义**：Young 是 [AM-GM](01-basics.md#均值不等式) 的推广（$p=q=2$ 时即为 $\displaystyle ab \le \frac{a^2+b^2}{2}$）。

**证明（凸函数法）**：

当 $a=0$ 或 $b=0$ 时，左侧为 $0$、右侧 $\ge 0$，不等式显然成立。故不妨设 $a, b > 0$。

考虑函数 $f(x) = e^x$（严格凸函数）。由 [Jensen 不等式](02-core-tools.md#琴生不等式)或直接用凸函数定义：
$$
ab = e^{\ln a + \ln b} = e^{\frac{1}{p}\cdot p\ln a + \frac{1}{q}\cdot q\ln b} \le \frac{1}{p}e^{p\ln a} + \frac{1}{q}e^{q\ln b} = \frac{a^p}{p} + \frac{b^q}{q}
$$

等号成立当且仅当 $p\ln a = q\ln b$，即 $a^p = b^q$。$\blacksquare$

**证明二（积分法）**：

设 $f(t) = t^{p-1}$，其反函数为 $f^{-1}(s) = s^{1/(p-1)} = s^{q-1}$（因为 $\frac{1}{p}+\frac{1}{q}=1$ 推出 $(p-1)(q-1)=1$）。由 Young 积分不等式（凸函数图像下的面积关系）：
$$
ab \le \int_0^a t^{p-1}\,dt + \int_0^b s^{q-1}\,ds = \frac{a^p}{p} + \frac{b^q}{q}
$$

![Young 不等式：两块积分面积之和不小于矩形面积 ab](/attachments/images/math/inequalities/young-integral-area.png)

上图的直观：曲线 $y = x^{p-1}$ 把第一象限切成两半，蓝色（$[0,a]$ 上曲线下方）与橙色（$[0,b]$ 上曲线左方）两块面积之和不小于矩形 $[0,a]\times[0,b]$ 的面积 $ab$——点 $(a,b)$ 离曲线越远，富余越多；恰在曲线上时两面积之和正好等于 $ab$（等号条件）。

$\blacksquare$

---

### Hölder 不等式

> **前驱**：[Young 不等式](#young-不等式)
>
> **定理（Hölder）** 设 $p > 1$，$q > 1$ 且 $\dfrac{1}{p} + \dfrac{1}{q} = 1$（称 $p,q$ 为共轭指数），对任意非负实数 $a_i, b_i$（$i=1,\ldots,n$），有
> $$
> \sum_{i=1}^n a_i b_i \le \left(\sum_{i=1}^n a_i^p\right)^{1/p} \left(\sum_{i=1}^n b_i^q\right)^{1/q}
> $$
> 任一组全为 $0$ 时取等；两组都非零时，等号成立当且仅当存在常数 $\lambda>0$ 使得 $a_i^p = \lambda b_i^q$（$i=1,\ldots,n$）。

> **三问**：固定 共轭指数 $p,q$ 与各组范数｜比较 耦合和 $\sum a_ib_i$ 与 容量之积 $\bigl(\sum a_i^p\bigr)^{1/p}\bigl(\sum b_i^q\bigr)^{1/q}$｜取等 $a_i^p\propto b_i^q$

**含义**：Hölder 是 [Cauchy-Schwarz](02-core-tools.md#柯西-施瓦茨不等式) 的推广（$p=q=2$ 时即为 Cauchy-Schwarz）。

**证明（Young 不等式 + 标准化）**：

先证明一个引理：若 $u_1, \ldots, u_n \ge 0$ 且 $v_1, \ldots, v_n \ge 0$ 满足 $\sum_{i=1}^n u_i^p = \sum_{i=1}^n v_i^q = 1$，则 $\sum_{i=1}^n u_i v_i \le 1$。

由 Young 不等式（见上节），对每一项：
$$
u_i v_i \le \frac{u_i^p}{p} + \frac{v_i^q}{q}
$$

求和得：
$$
\sum_{i=1}^n u_i v_i \le \frac{1}{p}\sum_{i=1}^n u_i^p + \frac{1}{q}\sum_{i=1}^n v_i^q = \frac{1}{p} + \frac{1}{q} = 1
$$

**一般情形**：令 $A = \left(\sum_{i=1}^n a_i^p\right)^{1/p}$，$B = \left(\sum_{i=1}^n b_i^q\right)^{1/q}$。若 $A=0$ 或 $B=0$，不等式显然成立。否则令 $u_i = a_i/A$，$v_i = b_i/B$（$i=1,\ldots,n$），则 $\sum_{i=1}^n u_i^p = \sum_{i=1}^n v_i^q = 1$，满足引理条件，故：
$$
\sum_{i=1}^n u_i v_i \le 1 \quad \Rightarrow \quad \sum_{i=1}^n \frac{a_i}{A} \cdot \frac{b_i}{B} \le 1 \quad \Rightarrow \quad \sum_{i=1}^n a_i b_i \le AB
$$

$\blacksquare$

---

### 权方和不等式

> **前驱**：[Hölder 不等式](#hölder-不等式)
>
> **定理** 设 $a_i > 0$, $b_i > 0$（$i=1,\ldots,n$），实数 $p > 0$，则
> $$
> \sum_{i=1}^n \frac{a_i^{p+1}}{b_i^p} \ge \frac{\left(\sum_{i=1}^n a_i\right)^{p+1}}{\left(\sum_{i=1}^n b_i\right)^p}
> $$
> 等号成立当且仅当 $\dfrac{a_1}{b_1} = \dfrac{a_2}{b_2} = \cdots = \dfrac{a_n}{b_n}$。

> **三问**：固定 分子和 $\sum a_i$ 与分母和 $\sum b_i$｜比较 分式和 $\sum \frac{a_i^{p+1}}{b_i^p}$ 与 合并式 $\frac{(\sum a_i)^{p+1}}{(\sum b_i)^p}$｜取等 $a_i/b_i$ 全相等

**特例（$p=1$）**：
$$
\sum_{i=1}^n \frac{a_i^2}{b_i} \ge \frac{(a_1 + \cdots + a_n)^2}{b_1 + \cdots + b_n}
$$
这是竞赛中极为常用的形式（即 [Nesbitt 证明二](02-core-tools.md#nesbitt-不等式)用到的 Titu 引理的一般版本），可由 Cauchy-Schwarz 直接推出：
$$
\left(\sum \frac{a_i^2}{b_i}\right)\left(\sum b_i\right) \ge \left(\sum a_i\right)^2
$$

**证明（Hölder 不等式特例）**：

权方和不等式是 Hölder 不等式的直接推论。设 $q = p+1$，$r = (p+1)/p$，则 $\dfrac{1}{q} + \dfrac{1}{r} = 1$。由 Hölder 不等式：

$$
\sum_{i=1}^n a_i = \sum_{i=1}^n \frac{a_i}{b_i^{p/(p+1)}} \cdot b_i^{p/(p+1)} \le \left(\sum_{i=1}^n \frac{a_i^{p+1}}{b_i^p}\right)^{1/(p+1)} \cdot \left(\sum_{i=1}^n b_i\right)^{p/(p+1)}
$$

两边取 $(p+1)$ 次幂：

$$
\left(\sum_{i=1}^n a_i\right)^{p+1} \le \left(\sum_{i=1}^n \frac{a_i^{p+1}}{b_i^p}\right) \cdot \left(\sum_{i=1}^n b_i\right)^p
$$

整理即得权方和不等式。等号条件来自 Hölder 的等号条件。$\blacksquare$

---

### Minkowski 不等式

> **前驱**：[Hölder 不等式](#hölder-不等式)
>
> **定理（Minkowski）** 设 $1\le p<\infty$，对任意实数 $a_i, b_i$（$i=1,\ldots,n$），有
> $$
> \left(\sum_{i=1}^n |a_i + b_i|^p\right)^{1/p} \le \left(\sum_{i=1}^n |a_i|^p\right)^{1/p} + \left(\sum_{i=1}^n |b_i|^p\right)^{1/p}
> $$
> **等号条件须分情况**：$p>1$ 时，两组非零向量须同向成比例（$a=\lambda b$，$\lambda>0$），或其中一组全为 $0$；$p=1$ 时，只需每个坐标 $a_ib_i\ge0$，不要求成比例。例如 $a=(1,0)$、$b=(0,1)$ 在 $p=1$ 时也取等。

> **三问**：固定 两个向量与指数 $p$｜比较 $\lVert a+b\rVert_p$ 与 $\lVert a\rVert_p+\lVert b\rVert_p$｜取等 同向成比例（$p=1$ 逐项同号即可）

**含义**：这是[三角不等式](01-basics.md#三角不等式绝对值不等式)在 $L^p$ 范数下的推广（$p=2$ 时即欧几里得范数的三角不等式，$p=1$ 时即普通的绝对值三角不等式）。

**证明（Hölder 不等式）**：

当 $p=1$ 时，由 $|a_i+b_i| \le |a_i|+|b_i|$ 求和即得。

设 $p > 1$，记 $q = \frac{p}{p-1}$（即 $\frac{1}{p}+\frac{1}{q}=1$）。令 $S = \sum |a_i+b_i|^p$。

$$
\begin{aligned}
S &= \sum_{i=1}^n |a_i+b_i| \cdot |a_i+b_i|^{p-1} \\
&\le \sum_{i=1}^n |a_i| \cdot |a_i+b_i|^{p-1} + \sum_{i=1}^n |b_i| \cdot |a_i+b_i|^{p-1}
\end{aligned}
$$

对两个求和项分别用 Hölder 不等式（注意 $(p-1)q = p$）：

$$
\sum_{i=1}^n |a_i| \cdot |a_i+b_i|^{p-1} \le \left(\sum |a_i|^p\right)^{1/p} \left(\sum |a_i+b_i|^{(p-1)q}\right)^{1/q} = \left(\sum |a_i|^p\right)^{1/p} \cdot S^{1/q}
$$

同理第二项。于是：
$$
S \le S^{1/q}\left[\left(\sum |a_i|^p\right)^{1/p} + \left(\sum |b_i|^p\right)^{1/p}\right]
$$

若 $S=0$ 不等式显然成立；若 $S>0$，两边除以 $S^{1/q} = S^{1-1/p}$，得 $S^{1/p}$ 不超过右边括号内的和，即证。$\blacksquare$

## 本章原子卡（Zettelkasten）

本篇交付时提取的原子笔记，一概念一卡。卡内正文待填，但**结构与互链已建立**——从卡可以跳回本节，从本节可以跳进卡。

- [Young 不等式](../../../notes/young-inequality.md)
- [Hölder 不等式](../../../notes/holder-inequality.md)
- [权方和不等式](../../../notes/weighted-power-sum-inequality.md)
- [Minkowski 不等式](../../../notes/minkowski-inequality.md)

---

> ↩ [返回总览](../inequalities.md)
