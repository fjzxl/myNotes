---
title: 不等式 · 八、习题（分层自测）
tags:
  - math
  - math/inequality
  - kaoyan
---

> 📚 本文是 [不等式](../inequalities.md) 的第 6 / 6 章（总览第八部分）。 上一章：[六、应用](05-applications.md)

# 八、习题（分层自测）

> 🎯 **使用说明**：每题限时 10 分钟，先独立完成，卡住再看题后提示，详解统一放在[答案与详解](#答案与详解)。A 组检验"会套公式"、B 组检验"会认结构"、C 组检验"会放缩会迁移"——分别对应考研的送分题、中档题与证明题。错题处理：回到[七、口诀速记](../inequalities.md#七口诀速记)复述对应口诀的结构与取等，隔天重做一次再归档到错题本。

### A 组（基础：直接套用）

**A1** 设 $x>0$，求 $y=x+\dfrac4x$ 的最小值；若限定 $x\in(0,1]$，最小值又是多少？

> 【提示】AM-GM 的取等点在 $x=2$。范围不含取等点时，均值只给下界、给不了最小值——改看单调性。

**A2** 设 $x<0$，求 $y=x+\dfrac4x$ 的最大值。

> 【提示】"一正"不满足。提出负号把变量换成正的再用均值，注意不等号方向。

**A3** 设 $a,b,c>0$ 且 $a+b+c=6$，求：(1) $abc$ 的最大值；(2) $a^2+b^2+c^2$ 的最小值；(3) $ab+bc+ca$ 的最大值。

> 【提示】三问都在 $a=b=c=2$ 处取等；工具依次是 AM-GM、柯西（"平方和的平均不小于平均的平方"）、$(a+b+c)^2\ge 3(ab+bc+ca)$。

**A4** 已知 $\lvert x-2\rvert<1$，证明 $\lvert x^2-4\rvert<5$。

> 【提示】分解为 $\lvert x-2\rvert\cdot\lvert x+2\rvert$，对 $\lvert x+2\rvert=\lvert(x-2)+4\rvert$ 用三角不等式。

### B 组（进阶：结构识别与构造）

**B1** 实数 $x,y,z$ 满足 $x^2+y^2+z^2=1$，求 $x+2y+3z$ 的最大值。

> 【提示】把一次式看成"系数向量与变量的内积"，柯西里系数的平方和 $1^2+2^2+3^2=14$ 就是那个因子；等号方向为 $(x,y,z)\propto(1,2,3)$。

**B2** 设 $a,b,c>0$，证明 $\dfrac{a^2}{b}+\dfrac{b^2}{c}+\dfrac{c^2}{a}\ge a+b+c$。

> 【提示】权方和 $p=1$（即 Titu 引理/柯西 Engel 形式）：分母和恰好是 $a+b+c$。

**B3** 设 $a,b,c>0$，证明 $\dfrac{a^3}{b^2}+\dfrac{b^3}{c^2}+\dfrac{c^3}{a^2}\ge a+b+c$。

> 【提示】权方和 $p=2$。对照 B2：分子幂次 $p+1$、分母幂次 $p$，右端分子和的 $p+1$ 次、分母和的 $p$ 次恰好约成一次。

**B4** $a,b$ 为任意实数，$\varepsilon>0$，证明 $ab\le\dfrac{\varepsilon}{2}a^2+\dfrac{1}{2\varepsilon}b^2$。

> 【提示】基本式 $2uv\le u^2+v^2$，取 $u=\sqrt{\varepsilon}\,a$、$v=b/\sqrt{\varepsilon}$。这是分析学里拆乘积的"$\varepsilon$-技巧"，系数可任意倾斜。

**B5** 设 $x_i>0$（$i=1,\dots,n$），用琴生不等式（取 $f=\ln x$）一步证明 AM-GM。

> 【提示】$\ln$ 是凹函数，凹函数的琴生不等号方向与凸相反。

### C 组（考研向：放缩链与积分）

**C1** 设 $x>-1$，证明 $\dfrac{x}{1+x}\le\ln(1+x)\le x$；并由此推出 $\left(1+\dfrac1n\right)^n<e<\left(1+\dfrac1n\right)^{n+1}$。

> 【提示】求导法：令 $g=x-\ln(1+x)$、$h=\ln(1+x)-\frac{x}{1+x}$，用 $g(0)=h(0)=0$ 与导数符号。第二问取 $x=\frac1n$，两边同乘后取指数。

**C2** 设 $a,b\ge 0$，证明 $a^2b\le\dfrac{2a^3+b^3}{3}$。

> 【提示】把 $a^2b$ 写成 $(a^3)^{2/3}\cdot(b^3)^{1/3}$，即 Young/加权 AM-GM 的标准形状：权重 $\tfrac23+\tfrac13=1$。

**C3** $f,g$ 在 $[0,1]$ 上连续，证明 $\left(\displaystyle\int_0^1 fg\,\mathrm dx\right)^2\le\int_0^1 f^2\,\mathrm dx\cdot\int_0^1 g^2\,\mathrm dx$；并取 $f=x,\ g=x^2$ 做数值验证。

> 【提示】对一切 $\lambda$ 有 $\int_0^1(f-\lambda g)^2\,\mathrm dx\ge 0$，展开是 $\lambda$ 的二次函数，开口向上且非负 $\Rightarrow$ 判别式 $\le 0$。

**C4** 设 $0<a\le b\le c$，用排序不等式证明 $a^2+b^2+c^2\ge ab+bc+ca$，并说明取等条件。

> 【提示】两组 $(a,b,c)$ 与 $(a,b,c)$ 同序配对得最大和 $a^2+b^2+c^2$；$ab+bc+ca$ 是一个乱序和（配对 $a\to b,\ b\to c,\ c\to a$）。

### 答案与详解

**A1 详解**　$x>0$ 时 $x+\dfrac4x\ge 2\sqrt{x\cdot\dfrac4x}=4$，当 $x=\dfrac4x$ 即 $x=2$ 时取等，故最小值 $4$。
限定 $x\in(0,1]$：取等点 $2\notin(0,1]$，均值下界 $4$ **取不到**。改用单调性：$y'=1-\dfrac{4}{x^2}<0$ 对 $x\in(0,1]$ 恒成立（$x<2$ 时 $y'<0$），$y$ 在 $(0,1]$ 上单调递减，最小值在右端点：$y(1)=5$。
**口诀回扣**：「一正二定三相等」第三条"相等取得到"失效 → 换工具，别硬套。

**A2 详解**　$x<0$ 不满足"一正"。令 $t=-x>0$，则 $y=x+\dfrac4x=-\left(t+\dfrac4t\right)\le-4$，$t=2$（即 $x=-2$）时取等，故最大值 $-4$。
**口诀回扣**：均值求"最小"要正数；负数情形提出负号后，最小变最大、方向反转。

**A3 详解**　(1) $abc\le\left(\dfrac{a+b+c}3\right)^3=2^3=8$，$a=b=c=2$ 取等。
(2) 柯西（平方和的平均 $\ge$ 平均的平方）：$(a^2+b^2+c^2)\cdot 3\ge(a+b+c)^2=36$，故 $a^2+b^2+c^2\ge 12$，$a=b=c=2$ 取等。
(3) 由 $(a+b+c)^2\ge 3(ab+bc+ca)$（等价于 $a^2+b^2+c^2\ge ab+bc+ca$）得 $ab+bc+ca\le\dfrac{36}3=12$，同样 $a=b=c=2$ 取等。
**口诀回扣**：「和定积最大」管 (1)；(2) 是柯西特例「先平方再平均，不小于先平均再平方」；(3) 是它自己的平方版推论。三问同点取等——**均衡是所有这些界的公共最优**。

**A4 详解**　$\lvert x^2-4\rvert=\lvert x-2\rvert\cdot\lvert x+2\rvert$。而 $\lvert x+2\rvert=\lvert(x-2)+4\rvert\le\lvert x-2\rvert+4<5$，于是 $\lvert x^2-4\rvert<1\cdot 5=5$。
**口诀回扣**：「同号直达，异号绕行」——绕行的代价就是这里多出的 $\lvert x-2\rvert$。

**B1 详解**　柯西：$(x+2y+3z)^2\le(1^2+2^2+3^2)(x^2+y^2+z^2)=14$，故 $x+2y+3z\le\sqrt{14}$。取等当且仅当 $(x,y,z)=k(1,2,3)$，代入 $x^2+y^2+z^2=1$ 得 $k=\pm\dfrac1{\sqrt{14}}$，最大值在 $k=\dfrac1{\sqrt{14}}$ 达到：$\dfrac{1+4+9}{\sqrt{14}}=\sqrt{14}$。
**口诀回扣**：「乘积和的平方，装进平方和的乘积」——系数向量 $(1,2,3)$ 的平方和就是右侧因子。

**B2 详解**　权方和（$p=1$）：$\dfrac{a^2}{b}+\dfrac{b^2}{c}+\dfrac{c^2}{a}\ge\dfrac{(a+b+c)^2}{a+b+c}=a+b+c$。取等条件 $\dfrac ab=\dfrac bc=\dfrac ca$，正数下即 $a=b=c$。
**口诀回扣**：「分开除贵，合并除省」——三个分式各自除，比合成一次除"贵"出整个右端。

**B3 详解**　权方和（$p=2$）：$\dfrac{a^3}{b^2}+\dfrac{b^3}{c^2}+\dfrac{c^3}{a^2}\ge\dfrac{(a+b+c)^3}{(a+b+c)^2}=a+b+c$。取等 $\dfrac ab=\dfrac bc=\dfrac ca$，即 $a=b=c$。
（数值抽查 $a=b=c=1$：左 $=3=$ 右 ✓；$a=1,b=1,c=4$：左 $=1+\tfrac1{16}+64\approx65.1\ge 6$ ✓。）
**口诀回扣**：与 B2 同一口诀，只是"合并"时的幂次升一级——分子和 $p+1$ 次、分母和 $p$ 次，正好约成一次。

**B4 详解**　取 $u=\sqrt{\varepsilon}\,a,\ v=\dfrac{b}{\sqrt{\varepsilon}}$，由 $2uv\le u^2+v^2$：

$$2ab=2\left(\sqrt{\varepsilon}\,a\right)\left(\frac{b}{\sqrt{\varepsilon}}\right)\le\varepsilon a^2+\frac{b^2}{\varepsilon}\quad\Longrightarrow\quad ab\le\frac{\varepsilon}{2}a^2+\frac{1}{2\varepsilon}b^2$$

取等当且仅当 $\sqrt{\varepsilon}\,a=\dfrac{b}{\sqrt{\varepsilon}}$，即 $b=\varepsilon a$。
**口诀回扣**：Young 的"两项分摊"精神——系数 $\varepsilon$ 可调，意味着误差预算可以在两个平方项之间任意分配（分析学估计的核心动作）。

**B5 详解**　$f=\ln x$，$f''=-\dfrac1{x^2}<0$，是凹函数。凹函数的琴生方向与凸相反：

$$\ln\frac{x_1+\cdots+x_n}{n}\ \ge\ \frac{\ln x_1+\cdots+\ln x_n}{n}$$

两边乘 $n$ 再取指数：$\left(\dfrac{\sum x_i}{n}\right)^n\ge x_1x_2\cdots x_n$，即 $\sqrt[n]{x_1\cdots x_n}\le\dfrac{\sum x_i}{n}$，取等当且仅当 $x_1=\cdots=x_n$。∎
**口诀回扣**：「凸则先混后算更省」——凹则方向反过来；"和定积最大"在这里被一步证出。

**C1 详解**　令 $g(x)=x-\ln(1+x)$：$g(0)=0$，$g'(x)=1-\dfrac1{1+x}=\dfrac{x}{1+x}$，在 $(-1,0)$ 为负、$(0,+\infty)$ 为正，故 $g(x)\ge g(0)=0$，即 $\ln(1+x)\le x$。
令 $h(x)=\ln(1+x)-\dfrac{x}{1+x}$：$h(0)=0$，$h'(x)=\dfrac1{1+x}-\dfrac1{(1+x)^2}=\dfrac{x}{(1+x)^2}$，符号同上，故 $h(x)\ge 0$，即 $\dfrac{x}{1+x}\le\ln(1+x)$。两式合并（$x=0$ 时同时取等）。
取 $x=\dfrac1n>0$，两个不等号都严格：

$$\frac{1}{n+1}<\ln\left(1+\frac1n\right)<\frac1n$$

左半乘 $n+1$：$1<(n+1)\ln\left(1+\dfrac1n\right)$；右半乘 $n$：$n\ln\left(1+\dfrac1n\right)<1$。取指数：

$$\left(1+\frac1n\right)^n<e<\left(1+\frac1n\right)^{n+1}\qquad\blacksquare$$

**口诀回扣**：「$\ln$ 夹在两线之间」——本题就是那条双侧切线界；顺带得到 $e$ 的双侧估计（重要极限二的上界来源，见 [数列与函数极限](../calculus/02-03-sequence-function-limits.md)）。

**C2 详解**　$a^2b=\left(a^3\right)^{2/3}\left(b^3\right)^{1/3}$。由 Young（加权 AM-GM，权重 $\tfrac23+\tfrac13=1$）：

$$\left(a^3\right)^{2/3}\left(b^3\right)^{1/3}\le\frac23\,a^3+\frac13\,b^3=\frac{2a^3+b^3}{3}$$

取等当且仅当 $a^3=b^3$，即 $a=b$。（数值抽查 $a=2,b=1$：$4\le\tfrac{17}3\approx5.67$ ✓。）
**口诀回扣**：「你 $p$ 我 $q$，倒数和一」——这里 $\tfrac1p=\tfrac23,\ \tfrac1q=\tfrac13$；"乘积不超，两项分摊"按权重摊。

**C3 详解**　对任意实数 $\lambda$：$\displaystyle\int_0^1\bigl(f-\lambda g\bigr)^2\,\mathrm dx\ \ge 0$。展开：

$$\lambda^2\int_0^1 g^2\,\mathrm dx-2\lambda\int_0^1 fg\,\mathrm dx+\int_0^1 f^2\,\mathrm dx\ \ge 0\qquad(\forall\lambda)$$

这是关于 $\lambda$ 的开口向上且全程非负的二次函数，判别式 $\le 0$：

$$\left(\int_0^1 fg\,\mathrm dx\right)^2\ \le\ \int_0^1 f^2\,\mathrm dx\cdot\int_0^1 g^2\,\mathrm dx$$

取等当且仅当 $f=\lambda g$（几乎处处成比例）。数值验证 $f=x,\ g=x^2$：$\left(\int_0^1x^3\,\mathrm dx\right)^2=\left(\tfrac14\right)^2=\tfrac1{16}=0.0625$，而 $\int_0^1x^2\,\mathrm dx\cdot\int_0^1x^4\,\mathrm dx=\dfrac13\cdot\dfrac15=\dfrac1{15}\approx0.0667$，$\tfrac1{16}<\tfrac1{15}$ ✓。
**口诀回扣**：「$\sum$ 换 $\int$，结论照搬」——这就是柯西（#5）的积分版；判别式法是它最短的标准证明。

**C4 详解**　数组 $(a,b,c)$ 与自身同序，同序和 $=a\cdot a+b\cdot b+c\cdot c=a^2+b^2+c^2$ 为一切配对中最大；而 $ab+bc+ca$ 对应乱序配对 $a\to b,\ b\to c,\ c\to a$，故 $a^2+b^2+c^2\ge ab+bc+ca$。
取等条件：乱序和不损失当且仅当每个"交换对"中元素相等，即 $a=b=c$。（交叉验证：差 $=\tfrac12\bigl[(a-b)^2+(b-c)^2+(c-a)^2\bigr]\ge 0$，同样在 $a=b=c$ 取等。）
**口诀回扣**：「大配大、小配小，同序产出最高」——同序和是所有配对方案的天花板，乱序怎么排都不会超过它。

---

> ↩ [返回总览](../inequalities.md)
