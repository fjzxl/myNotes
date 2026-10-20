---
title: 导数概念与求导法则
tags:
  - math
  - kaoyan
  - math/calculus
---
# 导数概念与求导法则

> **考纲定位（数一）**：理解导数的概念及可导性与连续性的关系；了解导数的几何意义，会求平面曲线的切线方程与法线方程；掌握基本初等函数的导数公式、导数的四则运算法则与复合函数的求导法则；会求分段函数的导数；会求反函数的导数。导数定义是选择题字眼题的高发区（左右导数、可导与连续、差商变形），求导计算则贯穿整卷——中值定理、泰勒、洛必达、积分与微分方程全部以它为地基。
> 前置：[数列与函数极限](02-03-sequence-function-limits.md)（定义求导本质是算 $\dfrac00$ 型极限）、[无穷小、无穷大与连续](04-05-infinitesimal-continuity.md)（连续性语言、可导 ⇒ 连续的预告）、[极限计算方法综合](06-limit-techniques.md)（差商极限的工具箱）。后续：`08-differential-higher-order`（微分、隐函数 / 参数方程求导、高阶导数）。导航：[高等数学总览](../calculus.md)。

**目录**

- [一、导数的概念：两个问题与一个定义](#一导数的概念两个问题与一个定义)：[引例](#11-引例瞬时速度与切线斜率) · [定义与记号](#12-定义与记号) · [左右导数](#13-左右导数) · [导函数](#14-导函数与在区间上可导)
- [二、导数的意义与定义求导](#二导数的意义与定义求导)：[切线与法线](#21-几何意义切线与法线) · [用定义求导三例](#22-用定义求导三例)
- [三、可导与连续](#三可导与连续)：[可导必连续](#31-可导必连续) · [关系链与反例](#32-关系链与反例) · [分段分界点求导流程](#33-分段函数分界点的求导流程)
- [四、求导法则](#四求导法则)：[四则运算](#41-四则运算法则) · [反函数求导](#42-反函数求导) · [链式法则](#43-复合函数求导与链式法则) · [基本导数表](#44-基本导数表)
- [五、题型与方法总结](#五题型与方法总结)
- [六、易错点清单](#六易错点清单)
- [七、与其他笔记的联系](#七与其他笔记的联系)
- [附：自测清单](#附自测清单)

## 一、导数的概念：两个问题与一个定义

### 1.1 引例：瞬时速度与切线斜率

**瞬时速度**。自由落体 $s=\dfrac12gt^2$，求 $t_0=2$ 秒末的瞬时速度。时间段 $[2,2+\Delta t]$ 内的平均速度

$$\bar v=\frac{\Delta s}{\Delta t}=\frac{\tfrac12g\left[(2+\Delta t)^2-4\right]}{\Delta t}=\tfrac12 g(4+\Delta t)\ \xrightarrow{\Delta t\to0}\ 2g\approx19.6\ \text{m/s}$$

（数值核对：$\Delta t=0.01$ 时 $\bar v\approx19.649$。）**平均 → 瞬时**的桥梁正是极限。

**切线斜率**。曲线上点 $M(x_0,y_0)$ 处的切线，定义为割线 $MN$ 当 $N$ 沿曲线滑向 $M$ 时的**极限位置**，于是

$$k_{\text{切}}=\lim_{N\to M}k_{\text{割}}=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}.$$

两个问题（运动学 / 几何）落在**同一个数学结构**上：**函数增量与自变量增量之比的极限**。这个结构值得一个名字。

### 1.2 定义与记号

> **定义（导数）** 设 $f$ 在 $x_0$ 的某邻域内有定义。若极限
> $$f'(x_0)=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}=\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}$$
> 存在（有限），则称 $f$ 在 $x_0$ 处**可导**，极限值称为 $f$ 在 $x_0$ 的**导数**。

- **等价形式**（换元 $x=x_0+\Delta x$）：$f'(x_0)=\lim\limits_{x\to x_0}\dfrac{f(x)-f(x_0)}{x-x_0}$——遇到 $x\to x_0$ 的差商直接认。
- **记号**：$f'(x_0)$、$y'\big|_{x=x_0}$、$\dfrac{dy}{dx}\Big|_{x=x_0}$、$\dfrac{df(x_0)}{dx}$。Leibniz 记号 $\dfrac{dy}{dx}$ 目前作**整体**看；它在链式法则里"像分式相消"的直观（§4.3）与微分的严格化（`08`）里再兑现。
- **读法**：导数是因变量对自变量在一点的**瞬时变化率**——速度、斜率、增长率都是它的化身。
- **若差商趋于 $\infty$**（如 $y=\sqrt[3]{x}$ 在 $0$，差商 $\to+\infty$）：按考研口径**不可导**，几何上是**铅直切线**。"导数为无穷"不是导数存在。

### 1.3 左右导数

> **定义** $f'_-(x_0)=\lim\limits_{\Delta x\to0^-}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$，$f'_+(x_0)=\lim\limits_{\Delta x\to0^+}\dfrac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$。
> **定理** $f$ 在 $x_0$ 可导 $\iff$ 左、右导数**都存在且相等**。

与极限的「单侧合一」（[02-03 §3.2](02-03-sequence-function-limits.md)）完全平行——**必须**分左右求导的信号：分段函数分界点；含 $\lvert x-a\rvert$、$\max\{f,g\}$、$\operatorname{sgn}$ 的函数；区间端点（闭区间 $[a,b]$ 上只在端点谈单侧导数）。

**例（核对）**：$f(x)=\lvert x\rvert$ 在 $0$：左导数 $\lim\limits_{h\to0^-}\dfrac{\lvert h\rvert}{h}=\lim\dfrac{-h}{h}=-1$，右导数 $=+1$，存在但不等 $\Rightarrow$ 不可导（几何：角点，两条单侧切线）。∎

### 1.4 导函数与在区间上可导

若 $f$ 在开区间 $I$ 内每点可导，则 $x\mapsto f'(x)$ 也是函数，称为**导函数**：

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}\quad(\text{此处 }x\text{ 是变量，}h\to0).$$

$f'(x_0)$ 是导函数在 $x_0$ 的值——**但**分界点、无定义点必须回到定义（§3.3）：导函数表达式往往只覆盖分段中的某一支。

## 二、导数的意义与定义求导

### 2.1 几何意义：切线与法线

$f'(x_0)$ 是曲线 $y=f(x)$ 在 $M(x_0,f(x_0))$ 处切线的斜率：

$$\textbf{切线：}\ y-f(x_0)=f'(x_0)(x-x_0);\qquad \textbf{法线：}\ y-f(x_0)=-\frac1{f'(x_0)}(x-x_0)\ (f'(x_0)\ne0).$$

**例（核对）**：$y=\sqrt x$ 在点 $(4,2)$：$f'(4)=\dfrac1{2\sqrt4}=\dfrac14$（§2.2 例 1），切线 $y=\dfrac x4+1$（数值核对：$x=4.01$ 处切线值 $2.0025$，$\sqrt{4.01}\approx2.00250$）；法线 $y-2=-4(x-4)$。∎

### 2.2 用定义求导三例

**例 1（核对，有理化）**：$f(x)=\sqrt x$。差商 $=\dfrac{\sqrt{x+h}-\sqrt x}{h}=\dfrac1{\sqrt{x+h}+\sqrt x}\xrightarrow{h\to0}\dfrac1{2\sqrt x}$（$x>0$）。∎——分子有理化正是 [06 §3.1 轻武器](06-limit-techniques.md#31-轻武器四件套)的动作。

**例 2（核对，等价替换）**：$f(x)=e^x$。差商 $=\dfrac{e^{x+h}-e^x}h=e^x\cdot\dfrac{e^h-1}h\to e^x\cdot1$（$e^h-1\sim h$，[等价无穷小替换](../../../notes/equivalent-infinitesimals.md)）。∎——定义求导就是 $\dfrac00$ 型极限，Ch1 的整套工具在此上岗。

**例 3（核对，第一重要极限）**：$f(x)=\sin x$。和差化积：

$$\frac{\sin(x+h)-\sin x}h=\frac{2\cos\left(x+\frac h2\right)\sin\frac h2}h=\cos\left(x+\frac h2\right)\cdot\frac{\sin\frac h2}{\frac h2}\ \xrightarrow{h\to0}\ \cos x.$$

∎（数值核对：$x=1$、$h=10^{-7}$ 时差商 $\approx0.5403024=\cos1$。）同法可证 $(\cos x)'=-\sin x$（练习，答案对导数表）。

## 三、可导与连续

### 3.1 可导必连续

> **定理** $f$ 在 $x_0$ 可导 $\Rightarrow$ $f$ 在 $x_0$ 连续。

**证明（核对）**：$\Delta y=\dfrac{\Delta y}{\Delta x}\cdot\Delta x$。$\Delta x\to0$ 时 $\dfrac{\Delta y}{\Delta x}\to f'(x_0)$（有限），$\Delta x\to0$，故 $\Delta y\to0$，即连续。∎（有限 × 无穷小 = 无穷小，[04-05 §1.2](04-05-infinitesimal-continuity.md#12-无穷小的运算性质)。）

**逆否命题**更好用：$f$ 在 $x_0$ 间断 $\Rightarrow$ 不可导——[04-05](04-05-infinitesimal-continuity.md#五易错点清单) 早已预告「间断点是不可导的第一嫌疑」。反方向不成立，见下。

### 3.2 关系链与反例

$$\textbf{可导}\ \Longrightarrow\ \textbf{连续}\ \Longrightarrow\ \textbf{极限存在}\qquad(\text{两步都不可逆})$$

| 反例 | 在 $x=0$ 处 | 击破的命题 |
|------|-----------|-----------|
| $\lvert x\rvert$ | 连续、不可导 | 连续 ⇒ 可导（角点：左右导数 $-1\ne1$） |
| $\sqrt[3]{x}$ | 连续、不可导 | 差商 → $+\infty$ 也要有导数（铅直切线仍算不可导） |
| $x\sin\dfrac1x$（补 $f(0)=0$） | 连续、不可导 | 有界 × 无穷小保证连续，但差商 $=\sin\dfrac1x$ 振荡 |
| $x^2\sin\dfrac1x$（补 $f(0)=0$） | **可导**！ | "振荡因子出现 = 不可导"想当然（见 §3.3） |

**例（核对）**：$f(x)=x\lvert x\rvert$ 在 $0$：差商 $=\dfrac{h\lvert h\rvert}h=\lvert h\rvert\to0$，故 $f'(0)=0$——含绝对值未必不可导，要看差商本身；$x\ne0$ 处 $f'(x)=2\lvert x\rvert$。∎

**拓展（数一不考，知道即可）**：存在**处处连续、处处不可导**的函数（Weierstrass 函数）——连续性能坏到这个程度；所以"连续 ⇒ 可导"不但逻辑上不成立，反例还遍地都是。

### 3.3 分段函数分界点的求导流程

**标准流程**：① 先验连续（左右极限 $=f(x_0)$，否则直接不可导）；② 左导数：用**左段表达式**算 $\lim\limits_{h\to0^-}\dfrac{f(x_0+h)-f(x_0)}h$；③ 右导数同理；④ 都存在且相等才可导。

**陷阱一：用 $\lim\limits_{x\to x_0}f'(x)$ 代替定义。** 两者是不同的极限！反例：$f(x)=\begin{cases}x^2\sin\dfrac1x,&x\ne0\\ 0,&x=0\end{cases}$

- 定义：$f'(0)=\lim\limits_{h\to0}\dfrac{h^2\sin\frac1h}h=\lim h\sin\dfrac1h=0$（有界 × 无穷小）——**可导**；
- 导函数：$f'(x)=2x\sin\dfrac1x-\cos\dfrac1x$（$x\ne0$，四则 + 链式），当 $x\to0$ 时因 $-\cos\dfrac1x$ 振荡而**无极限**。

结论：$f'$ 在 $0$ 存在但不连续——**"导函数在该点的极限"既不是该点可导的必要条件，也不能当作判据**。（附带收获：这就是 [06 §3.3](06-limit-techniques.md#33-洛必达法则) 洛必达失效例里那个函数；导函数间断点只能是第二类的——Darboux 定理，拓展。）

**陷阱二：对称差。** 若 $f'(x_0)$ 存在，则拆项可证 $\lim\limits_{h\to0}\dfrac{f(x_0+h)-f(x_0-h)}{2h}=f'(x_0)$；但**对称差极限存在推不回可导**：$\lvert x\rvert$ 在 $0$ 的对称差 $\equiv0$，而 $f'(0)$ 不存在（左 $-1$ 右 $1$）。"对称"把单侧差异抹掉了。

**例（核对，参数反问题）**：$f(x)=\begin{cases}x^2,&x\le1\\ ax+b,&x>1\end{cases}$，确定 $a,b$ 使 $f$ 处处可导。

连续性（可导的门槛）：$a+b=1$。左导数：$\lim\limits_{h\to0^-}\dfrac{(1+h)^2-1}h=2$；右导数：$\lim\limits_{h\to0^+}\dfrac{a(1+h)+b-1}h=\lim\dfrac{ah}h=a$（用了 $a+b=1$）。相等得 $a=2$，从而 $b=-1$。∎（数值核对：$a=2,b=-1$ 时左右差商均 $\to2$。）

## 四、求导法则

### 4.1 四则运算法则

设 $u=u(x)$、$v=v(x)$ 在 $x$ 处可导：

$$[u\pm v]'=u'\pm v',\qquad [uv]'=u'v+uv',\qquad [Cu]'=Cu',\qquad \left[\frac uv\right]'=\frac{u'v-uv'}{v^2}\ (v\ne0).$$

**乘法法则的证明思路（核对）**：核心是"**加一项减一项**"的增量替换——在 $x_0$ 处，

$$\Delta(uv)=u(x_0+\Delta x)\,v(x_0+\Delta x)-u(x_0)v(x_0)=[u(x_0+\Delta x)-u(x_0)]\,v(x_0+\Delta x)+u(x_0)\,[v(x_0+\Delta x)-v(x_0)].$$

除以 $\Delta x$ 取极限；$v$ 可导 $\Rightarrow$ $v$ 连续（§3.1），故 $v(x_0+\Delta x)\to v(x_0)$，得 $u'v+uv'$。∎

**商法则**先证倒数：$\left(\dfrac1v\right)'=-\dfrac{v'}{v^2}$——$\dfrac{\frac1{v(x_0+\Delta x)}-\frac1{v(x_0)}}{\Delta x}=-\dfrac{v(x_0+\Delta x)-v(x_0)}{\Delta x}\cdot\dfrac1{v(x_0+\Delta x)v(x_0)}\to-\dfrac{v'(x_0)}{v(x_0)^2}$，再与乘法法则组合。

**例 1（核对，导出导数表成员）**：$(\tan x)'=\left(\dfrac{\sin x}{\cos x}\right)'=\dfrac{\cos^2x+\sin^2x}{\cos^2x}=\sec^2x$。∎（数值核对：$x=0.5$ 处差商 $\approx1.2984465=\sec^20.5$。）

**例 2（核对）**：$\left(\dfrac{x}{x^2+1}\right)'=\dfrac{(x^2+1)-x\cdot2x}{(x^2+1)^2}=\dfrac{1-x^2}{(x^2+1)^2}$（在 $x=1$ 处为 $0$）。∎

**警示**：$(uv)'\ne u'v'$——取 $u=v=x$：$(x^2)'=2x\ne1$。乘积求导是"**交叉照顾**"（我导你不导 + 我不导你导），不是"各自导"。

### 4.2 反函数求导

> **定理** 设 $y=f(x)$ 在区间 $I$ 上单调、连续、可导且 $f'(x)\ne0$，则其反函数 $x=\varphi(y)$ 在对应区间上可导，且
> $$\varphi'(y_0)=\frac1{f'(x_0)}\qquad(f(x_0)=y_0).$$

**证明思路（核对）**：$\dfrac{\Delta x}{\Delta y}=\dfrac1{\Delta y/\Delta x}$。单调保证 $\Delta y\ne0\Rightarrow\Delta x\ne0$（比值有意义）；$\varphi$ 连续（[界与函数 §2.1](functions-and-bounds.md#21-函数的概念) 反函数存在条件）保证 $\Delta y\to0$ 时 $\Delta x\to0$，于是 $\varphi'(y_0)=\dfrac1{f'(x_0)}$。∎——**互为反函数，导数互为倒数**；几何上两曲线关于 $y=x$ 对称，对称点处斜率互倒。

**例 1（核对）**：$y=\arcsin x$：反函数 $x=\sin y$，$y\in\left(-\dfrac\pi2,\dfrac\pi2\right)$（主值区间保证单调，[界与函数 §2.3](functions-and-bounds.md#23-初等函数)）。

$$(\arcsin x)'=\frac1{(\sin y)'}=\frac1{\cos y}=\frac1{\sqrt{1-\sin^2y}}=\frac1{\sqrt{1-x^2}}\quad(\text{主值区间内}\cos y>0,\ \text{取正根}).$$

（数值核对：$x=0.5$ 处差商 $\approx1.1547006=\dfrac1{\sqrt{0.75}}$。）∎

**例 2（核对）**：$y=\arctan x$：$x=\tan y$，$y\in\left(-\dfrac\pi2,\dfrac\pi2\right)$，$(\arctan x)'=\dfrac1{\sec^2y}=\dfrac1{1+\tan^2y}=\dfrac1{1+x^2}$。∎

**例 3（核对）**：$y=\ln x$：反函数 $x=e^y$，$(\ln x)'=\dfrac1{(e^y)'}=\dfrac1{e^y}=\dfrac1x$。∎——对数导数由指数导数反出，三个反三角 / 对数条全部由反函数法则装备进导数表。

### 4.3 复合函数求导与链式法则

> **定理（链式法则）** 设 $u=\varphi(x)$ 在 $x_0$ 可导，$y=f(u)$ 在 $u_0=\varphi(x_0)$ 可导，则复合函数 $y=f(\varphi(x))$ 在 $x_0$ 可导，且
> $$\frac{dy}{dx}=f'(u_0)\cdot\varphi'(x_0),\qquad\text{即}\quad \frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}.$$

**证明思路（核对，含一个著名漏洞的补救）**：朴素想法是 $\dfrac{\Delta y}{\Delta x}=\dfrac{\Delta y}{\Delta u}\cdot\dfrac{\Delta u}{\Delta x}$ 再取极限——但 $\Delta u$ 可能等于 $0$（分母非法，振荡型内层函数会无限次取到同一值）。补救：把 $f$ 在 $u_0$ 的可导改写成"增量形式"

$$\Delta y=f'(u_0)\Delta u+\alpha\cdot\Delta u,\qquad \alpha\to0\ (\Delta u\to0),\ \text{约定}\ \alpha(0):=0,$$

（约定 $\alpha(0)=0$ 后 $\Delta u=0$ 时该式自动成立）。两边除 $\Delta x$：$\dfrac{\Delta y}{\Delta x}=\left[f'(u_0)+\alpha\right]\dfrac{\Delta u}{\Delta x}\to\left[f'(u_0)+0\right]\varphi'(x_0)$。∎——"先恒等变形再取极限"与 $\varepsilon$-$\delta$ 证明里的放大是同一门手艺。

**使用要点**：

- **先分解，再逐层，最后相乘**。分解复合是 [界与函数 §2.1](functions-and-bounds.md#21-函数的概念) 的基本功：$y=e^{x^2}$ 拆成 $y=e^u$、$u=x^2$，得 $\dfrac{dy}{dx}=e^u\cdot2x=2x\,e^{x^2}$。（数值核对：$x=1$ 处差商 $\approx5.4365645=2e$。）
- **多层链式**从外到内逐层剥：$\left(\sin^3 2x\right)'=3\sin^22x\cdot\cos2x\cdot2=6\sin^22x\cos2x$（数值核对：$x=0.3$ 处 $\approx1.5788066$）。
- **Leibniz 记号的直观**：$\dfrac{dy}{dx}=\dfrac{dy}{du}\cdot\dfrac{du}{dx}$ 形式上像分式约分——好用，但记号不是证明；微分的严格化（`08`）会让这个直观合法化。
- 链式 + 四则混合作业中，最常见的错是**漏乘内层导数**与**该用乘法法则处只用链式**。

### 4.4 基本导数表

| 函数 | 导数 | 来源 |
|------|------|------|
| $C$（常数） | $0$ | 定义（差商 $\equiv0$） |
| $x^{\alpha}$ | $\alpha x^{\alpha-1}$ | $\alpha=n$ 整数：二项式定理；一般 $\alpha$：对数求导法（`08`）；$\sqrt x$ 已由定义直证（§2.2） |
| $a^{x}$ | $a^{x}\ln a$ | $a^x=e^{x\ln a}$ + 链式 |
| $e^{x}$ | $e^{x}$ | 定义（§2.2 例 2） |
| $\log_a x$ | $\dfrac1{x\ln a}$ | 换底 $\log_ax=\dfrac{\ln x}{\ln a}$ |
| $\ln x$ | $\dfrac1x$ | 反函数法则（§4.2 例 3） |
| $\sin x$ | $\cos x$ | 定义（§2.2 例 3） |
| $\cos x$ | $-\sin x$ | 定义（§2.2 例 3 练习） |
| $\tan x$ | $\sec^2x$ | 商法则（§4.1 例 1） |
| $\cot x$ | $-\csc^2x$ | 商法则（$\cot=\cos/\sin$，练习） |
| $\sec x$ | $\sec x\tan x$ | 倒数法则（$\sec=1/\cos$，练习） |
| $\csc x$ | $-\csc x\cot x$ | 倒数法则（练习） |
| $\arcsin x$ | $\dfrac1{\sqrt{1-x^2}}$ | 反函数法则（§4.2 例 1） |
| $\arccos x$ | $-\dfrac1{\sqrt{1-x^2}}$ | $\arccos x=\dfrac\pi2-\arcsin x$ |
| $\arctan x$ | $\dfrac1{1+x^2}$ | 反函数法则（§4.2 例 2） |
| $\operatorname{arccot} x$ | $-\dfrac1{1+x^2}$ | $\operatorname{arccot}x=\dfrac\pi2-\arctan x$ |

必背标准：闭卷 10 秒内写全 16 条；表内每个成员都应能说出**至少一条来路**（定义 / 四则 / 反函数 / 链式中的哪条路）——考场上忘了可以现场重造。

## 五、题型与方法总结

| 目标 | 方法 | 信号 |
|------|------|------|
| 用定义求导 / 判可导 | 差商极限（$\Delta x\to0$ 或 $x\to x_0$ 两种形式）；Ch1 工具全上 | "利用定义""讨论 $f$ 在 $x_0$ 的可导性" |
| 分段函数分界点 | 先验连续 → 左右导数用**定义**分别算 | 分段点、$\lvert x-a\rvert$、$\max\{f,g\}$ |
| 含 $f'(x_0)$ 的极限 | 凑差商：$\dfrac{f(x_0+\varphi(h))-f(x_0)}h=\dfrac{f(x_0+\varphi(h))-f(x_0)}{\varphi(h)}\cdot\dfrac{\varphi(h)}h$ | $\varphi(h)=h,\ 2h,\ \sin h,\ \ln(1+h)$ 等无穷小 |
| 对称差 | 若 $f'(x_0)$ 存在则 $=f'(x_0)$；反向不成立（$\lvert x\rvert$） | 选择题"下列极限存在能否推出可导" |
| 切线 / 法线方程 | $f'(x_0)$ 代入两点式；法线斜率取负倒数 | 给点求切线、切线平行 / 垂直条件 |
| 复合求导 | 分解 → 逐层 → 相乘 | $e^{\square}$、$\ln\square$、$\sin\square$ 套层结构 |
| 四则混合 | 法则 + 导数表；先化简再求导 | 乘积、商、混合式 |
| 参数 $a,b$ 反问题 | 连续给一个方程 + 左右导数相等给另一个 | "确定 $a,b$ 使 $f$ 可导" |
| 反函数导数 | 互倒公式 $\varphi'(y_0)=1/f'(x_0)$ | 反三角、对数类；抽象反函数题 |

**例（核对，凑差商）**：设 $f$ 在 $x_0$ 可导，求 $\lim\limits_{h\to0}\dfrac{f(x_0+2h)-f(x_0)}h$。凑：$=\lim\dfrac{f(x_0+2h)-f(x_0)}{2h}\cdot\dfrac{2h}h=2f'(x_0)$。（数值核对：$f=x^2$、$x_0=1$ 时 $h=10^{-4}$ 给 $4.0004\to4=2f'(1)$。）∎——分子的增量必须与分母的 $h$ **配套**；换 $\varphi(h)=\sin h$、$\ln(1+h)$ 同法（配 $\dfrac{\varphi(h)}h\to1$）。

## 六、易错点清单

- **$f'(x_0)$ 与 $[f(x_0)]'$**：后者是对常数求导（$=0$），风马牛不相及。
- **分段点用导函数极限判可导**：必须用定义算左右导数；$x^2\sin\dfrac1x$ 反例（§3.3 陷阱一）。
- **对称差当可导判据**：$\dfrac{f(x_0+h)-f(x_0-h)}{2h}$ 存在 ⇏ 可导（$\lvert x\rvert$ 在 $0$ 对称差恒 $0$）。
- **连续 ⇒ 可导**：方向反了；角点（$\lvert x\rvert$）、铅直切线（$\sqrt[3]x$）、振荡（$x\sin\dfrac1x$）三类反例要随取随用。
- **差商 → ∞ 当"导数存在"**：铅直切线仍是不可导。
- **$(uv)'=u'v'$、$\left(\dfrac uv\right)'=\dfrac{u'}{v'}$**：乘除法则记错；商法则分子是"**分子导分母不导 − 分子不导分母导**"（$\tan'$ 的推导帮你锁符号）。
- **链式漏乘内层导数**：$(\sin2x)'=\cos2x$ ❌——差一个 $2$；多层复合逐层剥,别跳步。
- **$a^x$ 与 $x^a$ 的导数互串**：$a^x\to a^x\ln a$（指数函数，底固定），$x^\alpha\to\alpha x^{\alpha-1}$（幂函数，指数固定）。
- **反函数求导忘验条件**：要单调 + $f'(x_0)\ne0$，缺了互倒公式无意义。
- **凑差商时增量不配套**：$\dfrac{f(x_0+2h)-f(x_0)}h=2f'(x_0)$ 不是 $f'(x_0)$；$\dfrac{f(x_0+h)-f(x_0-h)}h=2f'(x_0)$ 也不是 $f'(x_0)$ 的一半——数清增量与分母的倍数。

## 七、与其他笔记的联系

- 前置：[02-03](02-03-sequence-function-limits.md)（差商极限即 $\dfrac00$ 型，两个重要极限装备 $\sin'$）、[04-05](04-05-infinitesimal-continuity.md)（连续性语言；可导 ⇒ 连续在此展开为定理）、[06](06-limit-techniques.md)（定义求导的工具箱）、[界与函数](functions-and-bounds.md)（复合分解、反函数主值区间）。
- 后续：`08-differential-higher-order` —— 微分（Leibniz 记号的兑现）、隐函数 / 参数方程求导、对数求导法（$x^\alpha$ 一般情形）、高阶导数；`09`–`11` —— 中值定理、泰勒、洛必达，全部以本文法则为计算引擎；`12`–`14` —— 单调性、极值、凹凸性、作图。
- 原子卡：[导数的定义](../../../notes/derivative-definition.md) · [可导与连续](../../../notes/differentiability-vs-continuity.md) · [求导四则与反函数法则](../../../notes/differentiation-rules.md) · [链式法则](../../../notes/chain-rule.md)
- [Ch1 复习页](ch1-review.md) —— Ch1 侧的三轮复习已把「可导 ⇒ 连续」列入反例库回看项。

## 附：自测清单

- [ ] 能默写导数定义（两种形式）与左右导数充要条件，并说出三类"必须分左右"的信号
- [ ] 能用定义推出 $(\sqrt x)'$、$(e^x)'$、$(\sin x)'$，并指出每步用的 Ch1 工具（有理化 / 等价替换 / 第一重要极限）
- [ ] 能默写关系链"可导 ⇒ 连续 ⇒ 极限存在"，并对每个箭头给出反例（$\lvert x\rvert$ 在 $0$；$f(x)=\dfrac{\sin x}x$ 补定义 $f(0)=2$——极限存在但不连续）
- [ ] 能完整论证 $x^2\sin\dfrac1x$ 在 $0$ 可导、但 $f'$ 在 $0$ 不连续；并解释为何不能用 $\lim f'$ 判分段点可导
- [ ] 能用左右导数处理 $\lvert x\rvert$、$x\lvert x\rvert$、$\max\{x,x^2\}$ 型函数的分界点
- [ ] 能叙述乘法法则与反函数法则的证明思路（增量替换；$\Delta x/\Delta y$ 互倒）
- [ ] 能闭卷写全 16 条基本导数表，并为每条指出一条来路
- [ ] 能独立完成参数题（$\begin{cases}x^2\\ ax+b\end{cases}$ 型）与凑差商题（$2h$、$\sin h$ 变体）
- [ ] 能算对 $(\tan x)'$、$\left(\dfrac{x}{x^2+1}\right)'$、$\left(\sin^32x\right)'$ 并数值自检
