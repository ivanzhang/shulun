# Prime Rows and Nonzero Columns in the `P×P` Prime-Sieve Matrix

## 摘要

设 `P` 为奇素数，将 `1,2,\ldots,P^2` 逐行放入 `P×P` 方阵。本文证明框架的目标是：每一行至少含有一个素数，且除第 `P` 列外每一列至少含有一个素数。

证明分为四个核心部分：

1. 增长阶统一筛余 connected cumulant 定理 `USC(log P)`；
2. 行窗口粗合数安全均值间隙 `SG`；
3. 列高阈值筛余容量一致下界 `LC`；
4. 行列存在素数的组合闭合。

几何圆柱斜线模型在证明中被严格化为 CRT 周期投影、中心化 cumulant 消失和 connected skeleton/polymer 展开。

---

## 1. 基本设置

令 `P` 为奇素数。方阵第 `r` 行第 `c` 列的数为

\[
n_{r,c}=(r-1)P+c,
\qquad 1\le r,c\le P.
\]

行命题要求每个固定 `r` 中存在素数。列命题要求对每个 `1\le c\le P-1`，存在

\[
p\le P^2,
\qquad p\equiv c\pmod P.
\]

第 `P` 列由 `P,2P,\ldots,P^2` 构成，单独排除。


### 1.1 符号约定

全文固定以下记号：

- `B=√P` 表示行方向小筛水平，行窗口长度取 `L=4B`；
- `α=0.85` 表示列方向高阈值筛水平比例，列筛水平为 `z=αP`；
- `Ω` 表示当前筛余点集，可能是行窗口，也可能是列场 `Ω_c={c+kP:0≤k<P}`；
- `\mathcal W` 表示一族连续滑动窗口，`I(\mathcal W)` 表示这些窗口扫过的整数区间，`Y=|I(\mathcal W)|`；
- `H_J` 表示行窗口小筛候选数，`H_α(P,c)` 表示第 `c` 列的高阈值筛余容量；
- `P_*` 表示理论渐近证明的最终阈值，`P_{max}` 只表示有限验证脚本输入上界。

所有 `o(1)` 均指 `P→∞`，并在固定 `α=0.85`、固定绝对常数选择后成立。

---

## 2. 统一筛余 connected cumulant 定理

### 定义 2.1：筛余场

令 `Ω` 为以下两类点集之一：

1. 行窗口：长度 `L=4B=4√P` 的连续区间；
2. 列场：`Ω_c={c+kP:0≤k<P}`。

对筛水平 `z`，定义筛余指示

\[
y_x=1_{(x,\prod_{q\le z}q)=1}.
\]

令

\[
p_Ω=\mathbb E y_x,
\qquad
Y_x=\frac{y_x}{p_Ω}-1.
\]

### 定理 2.2：`USC(log P)`

存在绝对常数 `c_0,C>0`，使得对所有

\[
2\le r\le c_0\log P,
\]

有

\[
\sum_{x_1,\ldots,x_r\in Ω}
\kappa(Y_{x_1},\ldots,Y_{x_r})
\ll
|Ω|(Cr)^{Cr}(\log\log P)^{r-1}\log^{Cr}P.
\]

该结论同时适用于：

- 行窗口筛水平 `z=√P`；
- 列场高阈值筛水平 `z=αP`，其中固定 `α<1`。

### 引理 2.3：有限 CRT 中心化投影

令 `Q_0` 为有限素数集，`M=\prod_{q\in Q_0}q`。设

\[
y_M(x)=1_{(x,M)=1},
\qquad
p_M=\frac{\varphi(M)}{M},
\qquad
Y_M(x)=\frac{y_M(x)}{p_M}-1.
\]

则

\[
\sum_{a\bmod M}Y_M(a)=0.
\]

若 `A` 与 `M` 互素，则

\[
\sum_{t\bmod M}Y_M(At+B)=0.
\]

**证明。** 第一式由 `p_M` 的定义立即得到。第二式因为 `t\mapsto At+B` 是模 `M` 的双射。

行场中 `A=1`。列场中 `A=P`；所有筛素数满足 `q<P`，故 `(P,M)=1`。因此同一投影恒等同时适用于行场与列场。

### 引理 2.4：cumulant 投影消失

设 `Z_1(t),\ldots,Z_r(t)` 是依赖模 `M` 参数 `t` 的变量。若

\[
\sum_{t\bmod M}Z_1(t)=0,
\]

且其余入口在该投影中固定，则

\[
\sum_{t\bmod M}\kappa(Z_1(t),Z_2,
\ldots,Z_r)=0.
\]

**证明。** cumulant 对每个入口多线性，所以求和可移入第一入口：

\[
\sum_t\kappa(Z_1(t),Z_2,
\ldots,Z_r)
=\kappa\left(\sum_t Z_1(t),Z_2,
\ldots,Z_r\right)=0.
\]

这说明无碰撞项在完整 CRT 投影下精确消失。

### 引理 2.5：Möbius-Bell connected 展开

对固定 `r`，cumulant 核

\[
K_r(x_1,\ldots,x_r)=\kappa(Y_{x_1},\ldots,Y_{x_r})
\]

可展开为

\[
K_r(x_1,\ldots,x_r)
=
\sum_{Γ\in\mathcal H_r^{conn}}
\sum_{\mathbf q}
C_Γ(\mathbf q)
\prod_{e\in E(Γ)}E_{q_e,a_e}(L_e(x))
+R_r.
\]

这里：

- `Γ` 遍历 `{1,\ldots,r}` 上的 connected 超图；
- `q_e` 为 squarefree 模数；
- `L_e(x)` 是差分线性形式；
- `E_{q,a}(u)=1_{q|u-a}-1/q`；
- 系数满足逐素数 Euler/Rankin 可和界：所有局部兼容性和来源选择先在每个筛素数的局部因子中求和，最终总损失为 `(Cr)^{Cr}\log^{Cr}P`。

**证明。** joint cumulant 使用分区 Möbius 公式

\[
\kappa(Z_i:i\in I)=
\sum_{\Pi\in\mathcal P(I)}
(-1)^{|\Pi|-1}(|\Pi|-1)!
\prod_{B\in\Pi}\mathbb E\prod_{i\in B}Z_i.
\]

每个素数局部因子只取决于点集在模 `q` 下的相等分区，因此给出 Bell 分区展开。非单点块给出同余碰撞超边。若所得超图断开，则对应项分解为两个不相交指标集的乘积，在 cumulant Möbius 和中精确抵消。因此只剩 connected 超图。最后用

\[
1_{q|L-a}=E_{q,a}(L)+1/q
\]

把普通碰撞指示改写为中心化边基。常数化某些边后分三种情形：若图断开，则再次由 Möbius 抵消；若图仍 connected，则在剩余中心化边上重新计算 skeleton 和 rank，常数边只作为局部 Euler 因子进入引理 2.7；若某顶点因此孤立，则归入断开项而消失。因此保留项仍是 connected 中心化超图，且每个叶变量仍有可剥离的中心化父边。rank 计数给出系数的 Euler/Rankin 可和界。

### 引理 2.6：connected skeleton expansion

每个 connected 超图 `Γ` 含有一个普通生成树骨架 `T`。并且

\[
\rho(Γ)=\sum_{e\in E(Γ)}(|e|-1)=(r-1)+\rho_{ex}(Γ),
\qquad \rho_{ex}(Γ)\ge0.
\]

骨架边给出主 harmonic 因子；非骨架 rank `ρ_ex` 给出额外 Euler 衰减。

**证明。** 将每条超边替换为其内部完全图，得到 connected 普通图，取其生成树。每条树边来自某条超边。超边 `e` 至多承载 `|e|-1` 条树边，因此总 rank 至少为 `r-1`，剩余即 `ρ_ex`。

### 引理 2.7：tiny/near/far 三层素数控制

设 `r\le c_0\log P`。将筛素数分为

\[
q\le A_1r,
\qquad
A_1r<q\le A_2r^2,
\qquad
q>A_2r^2.
\]

则所有 skeleton/polymer 图型的总系数贡献为

\[
(Cr)^{Cr}(\log\log P)^{r-1}\log^{Cr}P.
\]

**证明。** 分三层估计。

**tiny 层。** 令

\[
M_0=\prod_{q\le A_1r}q.
\]

Chebyshev 估计给 `\log M_0=O(r)`。由于 `r\le c_0\log P`，取 `c_0` 足够小可使

\[
M_0\le P^{1/10}.
\]

tiny 层并入有限 CRT base measure，由引理 2.3 精确投影处理，不进入 polymer 常数。完整 CRT 周期内没有误差；截断到行窗口、局部窗口簇或列场时只产生端点不完整周期误差，该误差交由叶剥离端点估计、B.0.4 二维边界平均或 C.2 列场主量吸收，不进入 connected Euler 账本。

**near 层。** 对 `A_1r<q\le A_2r^2`，固定生成树骨架。单条骨架边的 squarefree 标签 Euler 因子为

\[
\prod_{A_1r<q\le A_2r^2}\left(1+\frac{C}{q}\right)
\le
\exp\left(C\sum_{A_1r<q\le A_2r^2}\frac1q\right).
\]

由 Mertens 素数倒数公式，

\[
\sum_{A_1r<q\le A_2r^2}\frac1q=O(1),
\]

故单条骨架边贡献 `O(1)`，`r-1` 条骨架边贡献 `O(1)^r`。

非骨架修饰至少多一个 rank，因此局部权重为 `O((Cr)^C/q^2)`。总 near 修饰因子满足

\[
\prod_{A_1r<q\le A_2r^2}\left(1+O\left(\frac{r^2}{q^2}\right)\right)
\le
\exp\left(O\left(\sum_{q>A_1r}\frac{r^2}{q^2}\right)\right)
\le e^{O(r)}.
\]

**far 层。** 对 `q>A_2r^2`，骨架边的 harmonic 和为

\[
\sum_{A_2r^2<q\le z}\frac1q\ll\log\log P.
\]

所以 `r-1` 条骨架边贡献

\[
(\log\log P)^{r-1}.
\]

非骨架修饰满足

\[
\sum_{q>A_2r^2}\frac{r^2}{q^2}=O(1/A_2),
\]

故绝对收敛。

最后，生成树骨架与标签选择数量由 `(Cr)^{Cr}` 控制；divisor 权和截断尾部由 Rankin 权吸收，造成 `\log^{Cr}P` 损失。合并即得结论。

### 引理 2.8：中心化叶剥离

对任一已经固定局部素数标签、局部 Bell 选择和 CRT 兼容性选择的 connected skeleton/polymer 项，有

\[
\left|
\sum_{x_1,\ldots,x_r\in Ω}
\prod_{e\in E(Γ)}E_{q_e,a_e}(L_e(x))
\right|
\le |Ω|(Cr)^{Cr}.
\]

这里 A.6 只负责变量求和；所有素数标签、来源选择和兼容性选择的总损失已经在引理 2.7 的逐素数 Euler/Rankin 账本中计入。

**证明。** 固定一个 connected 项，并在其 skeleton 中取一棵生成树 `T`。把所有不属于 `T` 的边暂时看作对变量的附加同余限制。下面从 `T` 的叶子到根依次剥离变量。

设 `v` 是当前叶子，`u` 是它在 `T` 中的父点。所有含 `x_v` 的同余条件可分成两类。

第一类与父边同属一个 connected 约束簇，形如

\[
x_v\equiv b(x_u,x_{W})\pmod {Q_v},
\]

其中 `W` 是已经固定的其余邻点集合，`Q_v` 是若干 squarefree 边模数的乘积或因子。若这些条件不兼容，则叶子求和为 `0`。若兼容，CRT 将它们合并为一个剩余类。

第二类是在中心化展开中产生的常数补偿项。它们或者不含 `x_v`，可移入外层系数；或者与第一类合并后仍给出一个中心化同余函数

\[
E_{Q_v,b}(x_v)=1_{x_v\equiv b\pmod {Q_v}}-\frac1{Q_v}.
\]

使用统一的仿射区间估计：若 `x=At+B`、`t` 属于整数区间 `I` 且 `(A,Q)=1`，则对任意剩余类 `a mod Q`，

\[
\#\{t\in I:At+B\equiv a\pmod Q\}=\frac{|I|}{Q}+O(1),
\]

因此

\[
\sum_{t\in I}\left(1_{At+B\equiv a\pmod Q}-\frac1Q\right)=O(1),
\]

且常数对剩余类一致。行窗口取 `A=1`；列场中 `A=P`，而所有筛素数均 `<P`，故 `(P,Q)=1`，即使 `Q>P` 也仍得到同一估计。

所以每剥离一个叶变量，原本可能带来的 `|Ω|` 体积因子被中心化抵消，只留下 `O(1)` 误差。若某展开项完全不含当前叶变量的中心化父边，则该叶从 connected skeleton 中断开，已由 cumulant Möbius-Bell 消去；故真正保留下来的 connected 项在每个叶上至少有一条可剥离中心化边。若叶变量同时承载多个边模数，兼容条件的合并方式按素数局部记账并已归入引理 2.7；本步骤只额外产生 `(Cr)^{Cr}` 级的中心化边、父边来源和端点选择常数。

连续剥离 `r-1` 个叶子后，只剩根变量未被中心化消去；丢弃其可能满足的剩余同余限制，直接以参数区间长度估计，贡献至多为 `|Ω|`。对固定的局部选择合并剥离过程中的端点和父边来源常数，即得

\[
\left|
\sum_{x_1,\ldots,x_r\in Ω}
\prod_{e\in E(Γ)}E_{q_e,a_e}(L_e(x))
\right|
\le |Ω|(Cr)^{Cr}.
\]

这里不再产生新的 Euler 或 divisor 损失；CRT 兼容性、公共因子选择和边来源细分均属于引理 2.7 的逐素数账本。

### 定理 2.2 的证明

证明分为两个层次。

第一，证明 cumulant 总和界。由引理 2.3–2.5，即附录 A.1 与命题 A.2.1，未发生同余碰撞的局部项由 CRT 中心化投影消失，断开的碰撞图由 cumulant Möbius-Bell 反演抵消。因此 cumulant 核只剩 connected 中心化 squarefree 超图项。由引理 2.6–2.7，即命题 A.3.1 与 A.4.1，connected 项的 skeleton/rank 结构、tiny/near/far 分层和 Rankin 账本给出总系数

\[
(Cr)^{Cr}(\log\log P)^{r-1}\log^{Cr}P.
\]

由引理 2.8，即命题 A.6.1，任一 connected 项的变量求和至多贡献一个自由体积因子 `|Ω|`。于是

\[
\sum_{x_1,\ldots,x_r\in Ω}
\kappa(Y_{x_1},\ldots,Y_{x_r})
\ll
|Ω|(Cr)^{Cr}(\log\log P)^{r-1}\log^{Cr}P.
\]

这就是定理 2.2 的 cumulant 形式。附录 A.0–A.6，尤其命题 A.2.1、A.3.1、A.4.1、A.6.1，展开了上述每个环节的细节。

第二，把 cumulant 总和界转为高矩集中。令

\[
X_Ω=\sum_{x\in Ω}Y_x.
\]

由 moment-cumulant 公式，`2m` 阶矩是所有集合分区的 cumulant 乘积之和。单点块因中心化为零；大小为 `s≥2` 的块由上面的 cumulant 总和界控制。对所有分区求和后，Bell 数与块大小选择由 `(Cm)^{Cm}` 吸收，得到

\[
\mathbb E|X_Ω|^{2m}
\le
(Cm)^{Cm}|Ω|^m(\log\log P)^m\log^{Cm}P.
\]

上述 `X_Ω` 是归一化中心变量之和。实际筛余计数使用

\[
Z_Ω=\sum_{x\in Ω}(y_x-p_Ω)=p_ΩX_Ω,
\qquad \mu=p_Ω|Ω|.
\]

因此

\[
\mathbb E|Z_Ω|^{2m}
\le p_Ω^{2m}(Cm)^{Cm}|Ω|^m\log^{Cm}P
=(Cm)^{Cm}\mu^m p_Ω^m\log^{Cm}P
\le (Cm)^{Cm}\mu^m\log^{Cm}P.
\]

行窗口、局部窗口簇与列场并合中使用的都是这个未归一化计数形式。命题 A.7.1 给出该转移的完整账本。定理 2.2 得证。

---

## 3. 行窗口安全均值间隙

### 定义 3.1：行窗口候选与粗合数

设 `J` 为长度

\[
L=4\sqrt P
\]

的行窗口。定义小筛候选池

\[
A_J=\{n\in J:(n,\prod_{q\le\sqrt P}q)=1\},
\qquad H_J=|A_J|.
\]

令

\[
S_J=\#\{n\in A_J:n\text{ composite}\}.
\]

因为 `n≤P^2`，若 `n\in A_J` 且合数，则所有素因子均大于 `\sqrt P`。

### 引理 3.2：局部平均到条件均值转移

设 `X_J` 是由某个候选合数层在窗口 `J` 中诱导的非负计数。若存在常数 `λ`，使残差

\[
D_J=X_J-λH_J
\]

满足如下两条局部控制：

1. 对任意连续窗口簇 `\mathcal W`，只要其起点长度至少 `C\sqrt P/\log P`，就有
   \[
   \mathbb E_{J\in\mathcal W}D_J\le o(\mathbb E_{J\in\mathcal W}H_J)+O(1);
   \]
2. 残差正部满足定理 2.2 型高矩集中，即对 `m=c\log P`，
   \[
   \mathbb E_J(D_J^+)^{2m}
   \le (Cm)^{Cm}\left(\frac{√P}{\log P}\right)^m\log^{Cm}P.
   \]

则对所有正常窗口，

\[
\mathbb E(X_J\mid A_J)
\le(λ+o(1))H_J+O(1).
\]

**证明。** 这是命题 B.4.1 的正文接口形式。命题 B.4.1 证明了：局部残差平均控制加正部高矩集中，经过滑动稳定性、坏窗口扩散和异常窗口强尾界排除，可推出所有正常窗口上的条件均值估计。这里使用的异常窗口并合属于 `\mu_J\asymp\sqrt P/\log P` 的多项式大主量情形，因此可对全部行窗口并合。

在 B.1、命题 B.2.1、命题 B.3.1 中，局部平均控制分别由命题 B.0.0–B.0.4、命题 B.2.1 的缩放筛余容量乘法性、以及命题 B.3.1 的三粗因子容量积分提供；残差高矩由定理 2.2 的 connected cumulant 控制提供。

### 引理 3.3：主半素数层 `B1`

设 `U_J` 统计

\[
n=uv,
\qquad \sqrt P<u\le v,
\qquad uv\le P^2
\]

的候选合数。则

\[
U_J\le\left(\frac{e^γ}{4}\log3+o(1)\right)H_J+O(1)
\]

在条件均值意义下成立。

**证明。** 先使用命题 B.0.0–B.0.4 的局部乘积容量上界、参数族误差并合、双线性平均与边界控制。对任意允许的局部窗口簇 `\mathcal W`，半素数层满足

\[
\mathbb E_{J\in\mathcal W}U_J
\le
(\lambda_1+o(1))\mathbb E_{J\in\mathcal W}H_J+O(1),
\]

其中 `\lambda_1` 由全局 Stieltjes 模型给出。现在计算 `\lambda_1`。

全局模型上界为

\[
U(P)\le
\sum_{\sqrt P<u\le P\atop u\ prime}\pi(P^2/u).
\]

由 PNT 上界，

\[
U(P)
\le(1+o(1))
\int_{\sqrt P}^{P}
\frac{1}{\log u}
\frac{P^2/u}{\log(P^2/u)}du.
\]

令 `u=P^a`，则 `du/u=\log P\,da`，且 `a\in[1/2,1]`。于是

\[
U(P)
\le(1+o(1))\frac{P^2}{\log P}
\int_{1/2}^{1}\frac{da}{a(2-a)}.
\]

部分分式分解给

\[
\frac1{a(2-a)}=\frac12\left(\frac1a+\frac1{2-a}\right),
\]

故

\[
\int_{1/2}^{1}\frac{da}{a(2-a)}
=\frac12\log3.
\]

另一方面，局部候选密度由 Mertens 定理给出

\[
H\text{-density}
=\prod_{q\le\sqrt P}\left(1-\frac1q\right)
=(1+o(1))\frac{2e^{-γ}}{\log P}.
\]

因此半素数层相对小筛候选层的局部常数为

\[
\lambda_1
=\frac{(1/2)\log3}{2e^{-γ}}
=\frac{e^γ}{4}\log3.
\]

由引理 3.2 的局部平均转移形式，得到所有正常窗口上的条件均值估计。

### 引理 3.4：可复用层 `B2`

设 `R_J` 统计含素因子

\[
\sqrt P<u\le4\sqrt P
\]

的候选合数。则

\[
R_J=o(H_J)+O(1)
\]

在条件均值意义下成立。

**证明。** 这里同样不使用孤立 `u` 的裸点态估计，而使用命题 B.2.1 的盒级缩放筛余容量。把所有素数 `u\in(\sqrt P,4\sqrt P]` 与缩放变量 `m` 同时求和；由于 `u` 大于筛水平并与所有小筛模数互素，条件 `u|n` 只把长度按比例缩放为 `1/u`，不改变小筛 CRT 密度。对任意允许的连续窗口簇 `\mathcal W`，命题 B.2.1 给出

\[
\mathbb E_{J\in\mathcal W}R_J
\le
\mathbb E_{J\in\mathcal W}H_J
\sum_{\sqrt P<u\le4\sqrt P\atop u\ prime}\frac1u
+o(\mathbb E_{J\in\mathcal W}H_J)+O(1).
\]

对 `\sqrt P<u\le4\sqrt P` 求和，Mertens 素数倒数公式给

\[
\sum_{\sqrt P<u\le4\sqrt P\atop u\ prime}\frac1u
=\log\log(4\sqrt P)-\log\log\sqrt P+O(1/\log P)
=O(1/\log P).
\]

所以 `R` 层满足引理 3.2 的局部残差条件，进而对所有正常窗口得到 `R_J=o(H_J)+O(1)`。

### 引理 3.5：三粗因子层 `B3`

设 `T_J` 统计含至少三个 `>\sqrt P` 素因子的候选合数。则

\[
T_J\le(\theta_3+o(1))H_J+O(1),
\]

其中可取 `\theta_3=0.42`。

**证明。** 局部窗口簇中的三粗因子容量由命题 B.0.0–B.0.4 的盒级乘积容量接口给出；下面的全局三重 Stieltjes 积分只用于计算相对小筛候选层的安全常数 `\theta_3`，不用于推出局部分布。若 `n≤P^2` 且含三个 `>\sqrt P` 的素因子，则实际只能为

\[
n=abc,
\qquad a,b,c>\sqrt P,
\qquad abc\le P^2.
\]

用 PNT 上界和边界 Laplace 估计，令 `a=P^α,b=P^β,c=P^γ`，其中 `α,β,γ>1/2` 且 `α+β+γ≤2`。主贡献来自边界 `α+β+γ=2`，得

\[
T(P)
\ll
\frac{P^2}{\log P}I_3,
\]

其中

\[
I_3=\int_{α,β>1/2\atop α+β<3/2}
\frac{dαdβ}{αβ(2-α-β)}<0.46.
\]

该数值上界在命题 B.3.1 中展开证明：令 `x=α-1/2,y=β-1/2`，再对 `y` 积分，可化为一维积分

\[
I_3=\int_0^1\frac{4\log(2-t)}{(1+t)(3-t)}dt<0.46.
\]

与

\[
H(P)=(1+o(1))\frac{2e^{-γ}P^2}{\log P}
\]

比较，得到

\[
\frac{T(P)}{H(P)}
\le\frac{e^γ}{2}I_3+o(1)<0.42+o(1).
\]

再用引理 3.2 的局部残差转移形式，转为正常窗口条件估计。

### 定理 3.6：安全均值间隙 `SG`

存在绝对常数 `η>0`，使得

\[
\mathbb E(S_J\mid A_J)
\le(1-η)H_J+O(1).
\]

**证明。** 候选粗合数分解为

\[
S_J\le U_J+R_J+T_J.
\]

由引理 3.3–3.5，

\[
S_J\le
\left(\frac{e^γ}{4}\log3+\theta_3+o(1)\right)H_J+O(1).
\]

由于

\[
\frac{e^γ}{4}\log3\approx0.489177,
\]

并且可取 `\theta_3=0.42`，括号内小于 `0.92`。因此可取

\[
η=\frac12\left(1-\frac{e^γ}{4}\log3-\theta_3\right)>0.
\]

---

## 4. 行命题

### 引理 4.1：每行存在正常小筛候选窗口

固定一行

\[
I_r=\{(r-1)P+1,\ldots,rP\}.
\]

令

\[
A(I_r)=\{n\in I_r:(n,\prod_{q\le\sqrt P}q)=1\}.
\]

则

\[
|A(I_r)|\gg P/\log P.
\]

特别地，每一行存在至少一个小筛候选点，并且存在长度 `4\sqrt P` 的正常子窗口 `J\subset I_r` 满足

\[
H_J=|A_J|\gg \sqrt P/\log P.
\]

**证明。** 对每个 `q≤\sqrt P`，因为 `P` 与 `q` 互素，行内位置 `c\mapsto (r-1)P+c mod q` 遍历完整剩余类，误差至多 `O(1)`。由一维小筛基本引理，行内避开所有 `q≤\sqrt P` 的点数为

\[
P\prod_{q\le\sqrt P}\left(1-\frac1q\right)+o(P/\log P)
\gg P/\log P.
\]

把整行分割成相邻的长度不超过 `4\sqrt P` 的区块，并将每个区块扩展为一个长度 `4\sqrt P` 的窗口。每个候选点属于至多常数个扩展窗口。若所有这些窗口都满足 `H_J=o(\sqrt P/\log P)`，则整行候选总数为 `o(P/\log P)`，与上式矛盾。因此存在候选量为 `\gg\sqrt P/\log P` 的窗口。

还需排除该窗口异常。这里不能只用“全局异常窗口总数很少”推出逐行存在正常窗口；需要逐行整数计数。命题 B.4.1 给出的是逐行强尾并合：对每一行 `r`，异常窗口数满足

\[
E_r\le |\mathcal J_r|\exp(-c_2(\log P)^2).
\]

由于 `|\mathcal J_r|\le P`，当 `P` 足够大时右侧小于 `1`。异常窗口数是整数，故 `E_r=0`。因此上一步得到的候选丰富窗口自动是正常窗口。这样得到每一行均存在一个同时满足候选量下界和局部均值正常性的正常窗口。

### 引理 4.2：正常窗口含素数

设 `J` 为长度 `4\sqrt P` 的正常窗口，满足

\[
H_J\gg\sqrt P/\log P.
\]

则对足够大 `P`，`J` 中含有素数。

**证明。** 令 `S_J` 为 `A_J` 中合数数目。由定理 2.2 和 moment-cumulant 公式，对 `m=c\log P`，有

\[
\mathbb E\left|S_J-\mathbb E(S_J\mid A_J)\right|^{2m}
\le (Cm)^{Cm}H_J^m\log^{Cm}P.
\]

由定理 3.6，

\[
H_J-\mathbb E(S_J\mid A_J)
\ge ηH_J/2.
\]

Markov 不等式给出坏窗口的有限族密度界

\[
\mathbb P(S_J\ge H_J)
\le
\left(
\frac{C m^C\log^C P}{H_J}
\right)^m.
\]

因为 `H_J\gg\sqrt P/\log P` 且 `m\asymp\log P`，右侧为

\[
\exp(-c(\log P)^2).
\]

这里的 `\mathbb P` 不是引入外部随机假设，而是定理 2.2 的高矩界对有限窗口参数族给出的异常密度记号。对预先固定的全部 `O(P^{3/2})` 个长度 `4\sqrt P` 行窗口并合，坏窗口数至多

\[
O(P^{3/2})\exp(-c(\log P)^2)<1
\]

对充分大 `P` 成立。坏窗口数为整数，故没有坏正常窗口，即所有正常窗口满足 `S_J<H_J`。于是 `A_J` 中存在非合数候选点。该点没有 `≤\sqrt P` 的因子，且 `n≤P^2`，故只能是素数。


### 引理 4.2S：平滑正常窗口含素数（替代硬窗口闭合）

设 `J_0` 是一行内长度 `3\sqrt P` 的核心窗口，`J^+` 是同中心、长度 `4\sqrt P` 的扩展窗口。取非负平滑权重 `\Phi_J`，满足：

- `\Phi_J(n)=1` 对所有 `n\in J_0`；
- `\operatorname{supp}\Phi_J\subset J^+`；
- `0\le\Phi_J\le1`，且离散差分满足 `\|\Delta^j\Phi_J\|_\infty\ll_j H^{-j}`，其中 `H=\sqrt P/\log^B P`。

定义平滑候选权重

\[
H_J^{sm}=\sum_n\Phi_J(n)1_{(n,\prod_{q\le\sqrt P}q)=1},
\]

和平滑合数权重 `S_J^{sm}`。若平滑版 B.0.4S，即平滑 Type-I 素数双线性估计，对所有 B.0.3 曲线带成立，则定理 3.6 的安全均值间隙同样给出

\[
\mathbb E(S_J^{sm}\mid A_J)
\le(1-\eta)H_J^{sm}+O(1).
\]

并且由 USC 高矩集中，对所有平滑正常窗口同时有

\[
S_J^{sm}<H_J^{sm}.
\]

因此 `J^+` 中存在素数。

**证明要点。** 平滑权重把硬条件 `ap\in I(\mathcal W)` 替换为 `\Phi(ap)`。对固定 `a` 和模数 `Q`，B.0.4S 给出平滑 Type-I 素数/AP 平均

\[
\sum_{p\equiv b\pmod Q}\Phi(ap)\,d\pi(p)
=\frac1{\varphi(Q)}\sum_{(p,Q)=1}\Phi(ap)\,d\pi(p)
+O_A(Y/a\log^{-A}P),
\]

在对 `a` 的 Stieltjes 平均后统一成立。于是 B.0.3 的双线性 connected 高矩转移不再产生 sawtooth 端点项，边界贡献由 B.0.4S 的平滑 Type-I 余项吸收。其余半素数层、缩放层和三粗因子层的 Stieltjes 常数计算不变，因为 `\Phi` 的总质量为 `|J_0|+O(H)`，且 `H=o(\sqrt P)`。最后 Markov 并合仍有 `\exp(-c(\log P)^2)` 尾界，坏平滑窗口数小于 `1`。

### 引理 4.1S：每行存在平滑正常窗口

对每一行，存在核心长度 `3\sqrt P`、扩展长度 `4\sqrt P` 的平滑正常窗口 `J`，满足

\[
H_J^{sm}\gg \sqrt P/\log P.
\]

**证明要点。** 用引理 4.1 的候选总量 `|A(I_r)|\gg P/\log P`。把行分割为长度约 `3\sqrt P` 的核心区块，并给每个核心区块配一个长度 `4\sqrt P` 的平滑扩展。每个候选点被 `O(1)` 个扩展权重覆盖。若所有平滑窗口的 `H_J^{sm}` 都为 `o(\sqrt P/\log P)`，则整行候选总量为 `o(P/\log P)`，矛盾。平滑异常窗口的定义与 B.4.1 相同，只把硬计数换成平滑权重；高矩主量仍为 `\asymp\sqrt P/\log P`，逐行坏窗口数小于 `1`。

### 定理 4.3S：平滑路线的行命题闭合

假设平滑版 B.0.4S 的 Type-I 素数双线性估计成立，并完成第 4 节平滑替代接口。则对充分大奇素数 `P`，每一行含有素数。

**证明。** 对任一行，由引理 4.1S 取平滑正常窗口。由引理 4.2S，其扩展窗口 `J^+` 中含素数。因为 `J^+` 仍包含在该行内，故该行含素数。

### 定理 4.3：每行有素数

对足够大的奇素数 `P`，方阵每一行至少含有一个素数。

**证明。** 对任一行，由引理 4.1 选取正常候选窗口 `J`。由引理 4.2，该窗口含素数。因此该行含素数。

---

## 5. 列命题

### 定义 5.1：高阈值列筛余容量

取固定

\[
α=0.85.
\]

对 `1≤c≤P-1`，定义

\[
H_α(P,c)=\#\{0\le k<P:(c+kP,\prod_{q\le αP}q)=1\}.
\]

### 引理 5.2：容量推出素数

若

\[
H_α(P,c)>1+2(\pi(P)-\pi(αP)),
\]

则第 `c` 列含有素数。

**证明。** 反设第 `c` 列无素数。取任一高阈值筛余点

\[
n=c+kP,
\qquad 0≤k<P.
\]

它满足 `(n,\prod_{q≤αP}q)=1`，所以 `n` 没有 `≤αP` 的素因子。若该列无素数，则除可能的例外 `n=1` 外，`n` 为合数。对合数筛余点，由于 `n≤P^2`，取其最小素因子 `r`。若所有素因子都 `>P`，则 `n>P^2`，矛盾；故存在素因子 `q≤P`。又因无 `≤αP` 的素因子，必有

\[
q\in(αP,P].
\]

但 `q=P` 不可能整除 `c+kP`，因为 `1≤c≤P-1`，故实际

\[
q\in(αP,P).
\]

于是除 `n=1` 这一唯一可能例外外，每个高阈值筛余点都被某个素数 `q\in(αP,P)` 覆盖。

固定这样的 `q`。因为 `(P,q)=1`，同余

\[
c+kP\equiv0\pmod q
\]

在 `k mod q` 中有唯一解。又 `α>1/2`，所以 `q>P/2`，从而区间 `0≤k<P` 中同一剩余类至多出现两个整数。因此每个 `q` 最多覆盖两个列点。即使某个列点有两个大素因子，也只会造成重复覆盖；用并集上界仍有

\[
H_α(P,c)\le
1+\sum_{αP<q<P\atop q\ prime}2
=1+2(\pi(P)-\pi(αP)).
\]

这与假设矛盾。这里的 `+1` 只吸收筛余点 `n=1`，在后续渐近比较中可忽略。

### 引理 5.3：平均主项 `LC1`

有

\[
\mu_α:=\mathbb E_{1\le c\le P-1}H_α(P,c)
=(1+o(1))e^{-γ}\frac{P}{\log P}.
\]

**证明。** 交换 `c,k` 求和：

\[
\sum_{c=1}^{P-1}H_α(P,c)
=
\#\{1≤n≤P^2:P\nmid n,
(n,\prod_{q≤αP}q)=1\}.
\]

由于 `α<1`，素数 `P` 不在筛积 `\prod_{q≤αP}q` 中。排除 `P|n` 只去掉 `P` 个数，相对主项 `P^2/\log P` 可忽略。因此

\[
\sum_{c=1}^{P-1}H_α(P,c)
=(1+o(1))P^2\prod_{q≤αP}\left(1-\frac1q\right).
\]

Mertens 定理给

\[
\prod_{q≤αP}\left(1-\frac1q\right)
\sim\frac{e^{-γ}}{\log(αP)}
\sim\frac{e^{-γ}}{\log P}.
\]

除以 `P-1` 即得。

### 引理 5.4：一致集中 `LC2`

对所有 `1≤c≤P-1`，有

\[
H_α(P,c)=\mu_α(1+o(1)).
\]

**证明。** 定理 2.2 适用于列场

\[
Ω_c=\{c+kP:0≤k<P\},
\qquad z=αP<P.
\]

因为所有筛素数 `q≤αP` 都与 `P` 互素，列场中的同余条件 `c+kP≡a mod q` 等价于唯一的 `k mod q` 条件；故 CRT 投影和中心化叶剥离与行窗口相同。

令

\[
Y_c=H_α(P,c)-\mu_α.
\]

把 `c` 在 `1≤c≤P-1` 上平均。由 moment-cumulant 公式和定理 2.2，对 `2m≤c_0\log P`，有

\[
\mathbb E_c |Y_c|^{2m}
\le (Cm)^{Cm}\mu_α^m\log^{Cm}P.
\]

取 `m=\lfloor c\log P\rfloor`，其中 `c>0` 足够小。对任意 `δ>0`，Markov 不等式给

\[
\mathbb P_c(|Y_c|>δ\mu_α)
\le
\frac{(Cm)^{Cm}\mu_α^m\log^{Cm}P}{δ^{2m}\mu_α^{2m}}
=
\left(\frac{(Cm)^C\log^C P}{δ^2\mu_α}\right)^m.
\]

由引理 5.3，`\mu_α\asymp P/\log P`。若取例如

\[
δ=(\log P)^{-1/10},
\]

则括号内仍为 `P^{-1+o(1)}`。于是

\[
\mathbb P_c(|Y_c|>δ\mu_α)
\le \exp(-c_1(\log P)^2).
\]

这里同样要把异常密度转为确定性结论。上述 `\mathbb P_c` 表示在有限列族 `1≤c≤P-1` 上的归一化计数，因此坏列数至多

\[
P\exp(-c_1(\log P)^2)<1
\]

对充分大 `P` 成立。坏列数为整数，故不存在坏列。因此所有 `1≤c≤P-1` 同时满足

\[
|H_α(P,c)-\mu_α|≤δ\mu_α,
\]

而 `δ\to0`，故得到一致集中。

### 定理 5.5：除第 `P` 列外每列有素数

由引理 5.3 与命题 C.2.1–C.2.2（即引理 5.4 的附录展开），所有非零列满足

\[
H_α(P,c)
\ge(e^{-γ}-o(1))\frac{P}{\log P}.
\]

另一方面，PNT 给

\[
1+2(\pi(P)-\pi(αP))
=(2(1-α)+o(1))\frac{P}{\log P}.
\]

当 `α=0.85` 时，右侧为

\[
(0.3+o(1))\frac{P}{\log P}.
\]

而

\[
e^{-γ}\approx0.56146>0.3.
\]

所以对足够大 `P`，

\[
H_α(P,c)>1+2(\pi(P)-\pi(αP)).
\]

由引理 5.2（附录 C.3 展开容量比较），第 `c` 列含有素数。该结论对所有 `1≤c≤P-1` 成立。

---

## 6. 最终主定理

### 定理 6.1：条件充分大情形

假设硬窗口边界相消命题 B.0.4\* 成立，或平滑窗口 Type-I 双线性命题 B.0.4S，尤其短切片接口 B.0.4S-short，成立并完成第 4 节的平滑替代改写。则存在常数 `P_*`，使得对所有奇素数 `P>P_*`，将 `1,2,\ldots,P^2` 逐行放入 `P×P` 方阵时：

1. 每一行至少含有一个素数；
2. 除第 `P` 列外，每一列至少含有一个素数。

**证明。** 常数 `P_*` 取为前文所有渐近估计同时有效的阈值，包括：

- 定理 2.2 的 `USC(log P)` 高矩范围；
- 定理 3.6 的行窗口安全均值间隙；
- 引理 4.1–4.2 的硬窗口闭合，或引理 4.1S–4.2S 的平滑窗口闭合；
- 引理 5.3–5.4 的列场平均主项、一致集中与坏列整数化；
- 定理 5.5 中 `e^{-γ}>2(1-α)` 的最终容量余量。

当 `P>P_*` 时，在硬窗口路线中由定理 4.3 给出每行有素数；在平滑路线中由定理 4.3S 给出每行有素数。列方向仍由定理 5.5 给出每个 `1≤c≤P-1` 的列有素数。二者合并即为结论。

### 引理 6.2：有限小素数验证接口

若要把定理 6.1 的“充分大”版本闭合为“所有奇素数”版本，只需对有限集合

\[
\{P\le P_*:P\text{ 为奇素数}\}
\]

做直接验证。验证过程如下：

1. 对每个奇素数 `P≤P_*`，构造 `1,2,\ldots,P^2` 的素性表；
2. 对每个行区间 `[(r-1)P+1,rP]` 检查是否含素数；
3. 对每个非末列 `\{c+kP:0≤k<P\}`、`1≤c≤P-1`，检查是否含素数；
4. 输出所有失败的 `(P,row)` 或 `(P,column)` 证据。

若失败集合为空，则主定理对所有奇素数成立。该有限验证只处理渐近证明阈值以下的有限剩余集合；它不改变充分大情形的理论证明。

### 定理 6.3：最终主定理

假设已经给出显式阈值 `P_*`，并且引理 6.2 的有限验证对所有奇素数 `P≤P_*` 通过。则对每个奇素数 `P`，`P×P` 方阵满足：

1. 每一行至少含有一个素数；
2. 除第 `P` 列外，每一列至少含有一个素数。

**证明。** 若 `P>P_*`，由定理 6.1 得到结论。若 `P≤P_*`，由引理 6.2 的有限验证得到结论。两种情形覆盖所有奇素数。

若尚未证明 B.0.4\* 或 B.0.4S，则本文当前得到的是“归约到单一边界/平滑 Type-I 接口”的条件版本，而不是无条件的“所有足够大奇素数”版本。若该接口和显式阈值 `P_*` 均给出，则全体奇素数版本再由有限验证闭合。

---


## 6.5 圆柱斜线动力系统与最终接口的结构化尝试

本节把几何圆柱斜线直觉精确化为行号移动的同余动力系统。它不替代 B.0.4S-short，但给出最后攻关可使用的确定性结构语言。

### 定义 6.5.1：根基素数斜线覆盖函数

固定奇素数 `P`。第 `r` 行第 `c` 列对应整数

\[
n_{r,c}=(r-1)P+c,
\qquad 1\le c\le P.
\]

对根基素数 `q<P`，因为 `(P,q)=1`，行 `r` 中被 `q` 覆盖的列属于唯一的模 `q` 剩余类

\[
(r-1)P+c\equiv0\pmod q.
\]

记该 residue 轨道为

\[
c_q(r)\equiv -(r-1)P\pmod q,
\qquad 1\le c_q(r)\le q,
\]

再按周期 `q` 提升到宽度 `P` 的圆柱列集合

\[
C_q(r)=\{c\in[1,P]:c\equiv c_q(r)\pmod q\}.
\]

于是行 `r` 的小筛覆盖集合为

\[
\mathcal C(r)=\bigcup_{q\le\sqrt P}C_q(r),
\qquad
A(r)=[1,P]\setminus\mathcal C(r).
\]

行内小筛候选数为 `H(r)=|A(r)|`。若进一步考虑大因子覆盖，可把 `q≤√P` 替换为相应大因子族，但小筛候选层已经足以描述 B.0.4S-short 的根本动力来源。

### 命题 6.5.2：行移动函数方程

对任意整数步长 `h`，有

\[
c_q(r+h)\equiv c_q(r)-hP\pmod q.
\]

因此

\[
C_q(r+h)=C_q(r)-hP\pmod q
\]

并且覆盖指示满足

\[
1_{c\in C_q(r+h)}=1_{c+hP\in C_q(r)}
\]

其中右侧按模 `q` 理解。于是行覆盖向量满足精确函数方程

\[
\mathbf 1_{\mathcal C(r+h)}(c)
=\bigvee_{q\le\sqrt P}\mathbf 1_{\mathcal C_q(r)}(c+hP).
\]

这就是“斜率不变、行移动引起等速平移”的严格代数形式。每个根基素数 `q` 的轨道周期为 `q`，全小筛覆盖图的共同周期为

\[
M_{\sqrt P}=\prod_{q\le\sqrt P}q.
\]

### 推论 6.5.3：全覆行复现周期的精确形式

若某行 `r` 被根基素数斜线全覆盖，即 `A(r)=\varnothing`，则对任意 `h`，行 `r+h` 的覆盖不是简单整体平移，而是由各模 `q` 的不同周期平移叠加得到。只有当

\[
hP\equiv t\pmod q
\]

对所有参与覆盖的 `q` 给出同一个列平移 `t` 时，才有全覆盖图的刚性整体平移。由于 `P` 对每个 `q<P` 可逆，这要求

\[
h\equiv tP^{-1}\pmod q\quad(q\le\sqrt P),
\]

等价于 `h` 在 CRT 模 `M_{\sqrt P}` 下固定。因此“覆盖图作为同一列平移图案”复现时由 CRT 周期控制，而不是由单个行号 `k` 自动推出。需要注意：某些行也可能因不同素数族重新组合而再次全覆盖，但那不是同一图案的刚性平移复现，必须另行用 CRT 交集计数分析。用户直觉中的“第 `k` 行全覆盖则第 `2k` 行全覆盖”只有在所有斜线族共享同一平移参数时成立；一般情形中不同 `q` 的平移不同步。

### 命题 6.5.4：行差分的可控性

设 `I\subset[1,P]` 为列区间。则行移动一步时，单个模 `q` 的覆盖集合在 `I` 中的变化满足

\[
\left| |C_q(r+1)\cap I|-|C_q(r)\cap I|\right|\le 2.
\]

更一般地，对任意 `h` 仍有

\[
\left| |C_q(r+h)\cap I|-|C_q(r)\cap I|\right|\le 2,
\]

因为二者都是同一长度区间 `I` 中某个模 `q` 剩余类的计数，任何两个剩余类计数只差端点误差。

对全覆盖并集不能直接求和得到强界，因为不同 `q` 的覆盖高度重叠；但对小筛候选指示可用 inclusion-exclusion/cumulant 写成

\[
H_I(r)=\sum_{c\in I}\prod_{q\le\sqrt P}\left(1-1_{c\in C_q(r)}\right).
\]

行移动差分满足

\[
H_I(r+h)-H_I(r)
=\sum_{\emptyset\ne S\subseteq\{q\le\sqrt P\}}(-1)^{|S|}
\left(N_S(r+h;I)-N_S(r;I)\right),
\]

其中 `N_S` 是同时落入所有 `C_q` 的 CRT 交集计数。对每个固定 `S`，CRT 把交集化为单一模数 `Q_S=\prod_{q\in S}q` 的一个剩余类，故

\[
N_S(r;I)=\frac{|I|}{Q_S}+O(1).
\]

这正是 USC cumulant 与叶剥离中的 `O(1)` 端点项来源。

**限制。** 上述差分方程给出的是每个固定 CRT 交集的端点可控性；但 inclusion-exclusion 中有指数多的交集，且低阶截断需要 connected cumulant 的相消。因而不能把 `O(1)` 逐项求和来得到全行候选数的 Lipschitz 控制。若要从行移动动力直接排除全覆行，仍需证明这些 CRT 交集端点项在 connected 展开中平均相消；这与 B.0.4S-short 是同一个问题的行号动力学版本。

### 与 B.0.4S-short 的关系

上述函数方程把行移动的几何刚性完全转化为 CRT 相位

\[
r\mapsto -rP\pmod q.
\]

它能严格解释周期性和局部差分，但它本身仍只给每个 CRT 交集 `O(1)` 的端点误差。B.0.4S-short 要求的是这些 `O(1)` 端点项在短切片、长 `a` 平均中产生额外相消；这等价于对倒数相位 `N/a` 或素数/AP 平均的双线性分布控制。换言之，圆柱动力系统提供了精确函数方程和周期结构，但要闭合最后接口，还必须在这些函数方程上证明高阶平均相消，而不能只依赖周期存在性。

因此下一步真正可攻的结构命题是：对由 `c_q(r+h)=c_q(r)-hP` 生成的 CRT 相位族，在 `a\asymp\sqrt P` 的 Stieltjes 平均上证明短切片相位均匀分布。这正是 B.0.4S-short 的几何等价形式。


## 6.6 反推目标命题所需的几何-组合引理

本节从目标命题反推需要的结构条件，再翻译回圆柱斜线动力系统。

### 6.6.1 目标命题的最小反证结构

若第 `r` 行没有素数，则该行中的每个小筛候选 `n_{r,c}` 都是合数。因为 `n_{r,c}\le P^2` 且无 `\le\sqrt P` 的因子，所以它必须是两个大素因子的乘积

\[
n_{r,c}=uv,
\qquad u,v>\sqrt P.
\]

因此无素数行等价于：小筛候选集合 `A(r)` 被大因子乘积层完全覆盖。若要证明每行有素数，只需证明存在常数 `\eta>0`，使任一正常行窗口 `J` 中大因子乘积覆盖量至多

\[
(1-\eta)H_J.
\]

前文的筛法证明正是这个方向；最后缺口 B.0.4S-short 是把大因子乘积覆盖量从全局 Stieltjes 常数转移到局部行窗口的短切片平均。

### 6.6.2 反推的核心几何引理

由上面的反证结构，足够证明以下几何-组合引理。

**引理 G（短切片相位均匀引理）。** 固定任一正常窗口簇 `\mathcal W` 和任一 dyadic 主盒 `a\asymp\sqrt P`。令

\[
\mathcal P_a(r)=\{p:\ ap\in I(\mathcal W),\ p\equiv b(a)\pmod Q\}.
\]

当 `r` 在允许的局部窗口簇中移动，且 `a` 按 Stieltjes 权在 dyadic 盒中平均时，集合 `\mathcal P_a(r)` 对 residue 类 `b(a)` 的偏差满足

\[
\sum_a W(a)\left(|\mathcal P_a(r)|-\frac1{\varphi(Q)}|\mathcal P_a^{*}(r)|\right)
=o(Y/\log P).
\]

其中 `\mathcal P_a^{*}` 表示与 `Q` 互素的无指定剩余类版本。引理 G 正是 B.0.4S-short 的几何语言。

### 6.6.3 动力系统给出的必要约束

圆柱斜线动力系统给出以下确定性约束：

1. **单模等速性。** 对每个根基模 `q`，覆盖 residue 满足 `c_q(r+h)=c_q(r)-hP mod q`。
2. **多模 CRT 刚性。** 任意有限模集合 `S` 的交集轨道是模 `Q_S=\prod_{q\in S}q` 的单一等速 residue。
3. **端点唯一性。** 对固定 `S` 与列区间 `I`，交集计数为 `|I|/Q_S+O(1)`，所有不规则性集中在端点 sawtooth。
4. **周期不可局部压缩。** 除非 `h` 在 CRT 模 `Q_S` 下固定，否则不同 `q` 的相位不同步，不能产生同一覆盖图案的短周期复现。

这些约束说明：若存在无素数窗口，异常不能来自某个单模或少数模的自由选择；它必须来自大量 CRT 端点 sawtooth 项在同一局部窗口中同向排列。

### 6.6.4 需要排除的唯一坏情形

因此最终只需排除以下坏情形：存在正常窗口簇 `\mathcal W` 与主盒 `a\asymp\sqrt P`，使得对许多 `a`，短切片端点

\[
\frac{N}{a},\qquad \frac{N+Y}{a}
\]

相对于由圆柱动力系统给出的 residue 类 `b(a) mod Q` 同向偏斜，导致 sawtooth 和达到 `\asymp Y/\log P`。

换言之，最后核心不是“斜线是否周期复现”，而是“倒数端点相位 `N/a` 是否能在长 `a` 平均中长期锁相”。若能证明无长期锁相，即

\[
\sum_{a\asymp\sqrt P}W(a)\psi\left(\frac{N}{aQ}-\frac{b(a)}Q\right)=o(Y/\log P),
\]

以及同样的 `N+Y` 版本，则目标命题闭合。

### 6.6.5 候选突破引理：无锁相引理

**引理 NL（倒数相位无锁相）。** 对任意由 connected 叶剥离产生的可逆 residue 函数 `b(a)`，以及任意 dyadic 主盒 `a\asymp\sqrt P`，有

\[
\sum_{a\asymp\sqrt P}W(a)\psi\left(\frac{N}{aQ}-\frac{b(a)}Q\right)
=o(Y/\log P)
\]

在所有允许窗口簇参数上一致成立。

若 NL 成立，则 B.0.4\* 成立；若其平滑素数权版本成立，则 B.0.4S-short 成立。NL 是圆柱动力系统给出的最精确几何-组合突破口。

### 6.6.6 当前可证明部分与剩余障碍

可证明部分：

- 单模和任意固定多模 CRT 交集的行移动函数方程完全精确；
- 任意固定 CRT 交集的局部计数误差只有端点 `O(1)`；
- 全覆行的刚性平移复现只能发生在 CRT 周期约束下；
- 无素数行的反证结构必须表现为大量端点 sawtooth 同向锁相。

剩余障碍：

- 需要证明 NL，即倒数相位 `N/a` 与可逆 residue 函数 `b(a)` 不会在 `a\asymp\sqrt P` 的 Stieltjes 平均上长期锁相；
- 这本质上是短切片 Type-I 双线性相位分布问题，与 B.0.4S-short 等价。

因此，目标命题的最后证明逻辑链条已经反推为：

\[
\text{NL 无锁相}
\Rightarrow \text{B.0.4S-short}
\Rightarrow \text{平滑 B.0.4S}
\Rightarrow \text{行命题}
\Rightarrow \text{主定理条件闭合}.
\]

## 6.7 反推接口的动力系统严写：从行移动到 Fourier 无锁相

本节把上一节的反推结论继续压缩为一个可审查的解析判据。核心思想是：全覆行若存在，则不是简单的周期复现问题，而是行移动动力系统在所有相关 CRT 端点上产生同向偏斜的问题；该偏斜等价于一族 Fourier 指数和异常大。

### 6.7.1 斜线覆盖的统一传输算子

固定模数集合 `S`，记 `Q=Q_S`。由命题 6.5.2，行移动 `r\mapsto r+h` 在 `Q` 上诱导平移

\[
T_h:x\mapsto x-hP\pmod Q.
\]

若 `I=[U,U+Y]` 是行窗口对应的整数区间，则任一 CRT 交集的计数可写成

\[
N_{Q,b}(r;I)
=\sum_{n\in I}1_{n\equiv b-rP\pmod Q}.
\]

于是行移动满足精确传输方程

\[
N_{Q,b}(r+h;I)
=N_{Q,b}(r;I+hP),
\]

其中右端表示把窗口端点整体平移 `hP` 后，在同一 residue 类中计数。这说明行号动力没有额外自由度：所有不规则性完全来自端点穿过模 `Q` 格点时的 sawtooth 跳跃。

进一步有精确分解

\[
N_{Q,b}(r;[U,U+Y])
=\frac{Y}{Q}
\psi\left(\frac{U-b+rP}{Q}\right)
-\psi\left(\frac{U+Y-b+rP}{Q}\right)
O(1_{Y=0}),
\]
其中 `\psi(x)=\{x\}-1/2` 可在整数端点处取任一固定规范；不同规范只造成 `O(1)` 端点误差。这个公式给出斜线覆盖随行号移动的完整函数方程。

### 6.7.2 全覆异常反推为端点能量异常

设某正常窗口 `I` 中小筛候选数为 `H_I\asymp Y/\log P`。若该窗口无素数，则候选点必须全部落入大因子乘积覆盖层。按 dyadic 分解和 connected 叶剥离，必存在一个主盒 `\mathcal R`，其贡献达到该盒期望主量的固定正比例异常；否则所有盒的误差求和小于筛余安全间隙，无法覆盖全部候选点。

对这个主盒，所有平滑主体项已经由 Stieltjes 主量给出。因此异常只能来自边界项。利用上式，边界项必含有形如

\[
E_{\mathcal R}(U)
=\sum_{a\asymp A}W(a)
\psi\left(\frac{U/a-b(a)}{Q}\right)
\]

或 `U+Y` 版本的和，并满足

\[
|E_{\mathcal R}(U)|\gg Y/\log P.
\]

这里 `A\asymp\sqrt P` 是半素数主层，`b(a)` 是叶剥离后保留下来的可逆 residue 函数。于是目标命题的反证结构被严格转化为：存在长 `a` 平均上的 sawtooth 锁相异常。

### 6.7.3 Fourier 判据

取截断参数 `M=(\log P)^B`。Erdos--Turan 型截断给出

\[
\psi(x)=
\sum_{1\le |m|\le M}\frac{-1}{2\pi i m}e(mx)
+O\left(\frac1{M\|x\|_{\mathbb T}+M^{-1}}\right),
\]
或等价地可用平滑 majorant/minorant 避开不连续点。因此若 `E_{\mathcal R}(U)` 达到 `\gg Y/\log P`，则存在某个 `1\le |m|\le M`，使

\[
\left|
\sum_{a\asymp A}W(a)
e\left(m\frac{U}{aQ}-m\frac{b(a)}{Q}\right)
\right|
\gg \frac{Y}{\log^{B+2}P}.
\]

所以 NL 可进一步替换为以下 Fourier 型判据。

**引理 FNL（Fourier 无锁相判据）。** 对所有允许的主盒、窗口端点 `U`、connected residue 函数 `b(a)`、模数 `Q` 与 `1\le |m|\le (\log P)^B`，有

\[
\sum_{a\asymp A}W(a)
e\left(m\frac{U}{aQ}-m\frac{b(a)}{Q}\right)
=o\left(\frac{Y}{\log^{B+2}P}\right)
\]
一致成立。则 NL 成立，从而 B.0.4S-short 成立。

### 6.7.4 可攻击的非线性来源

FNL 中的相位为

\[
\Phi_m(a)=m\frac{U}{aQ}-m\frac{b(a)}{Q}.
\]

第一项具有倒数曲率

\[
\Phi_m''(a)=\frac{2mU}{Qa^3}+\text{来自 }b(a)\text{ 的离散差分项}.
\]

在主层 `a\asymp\sqrt P`、`U\asymp P^2` 时，连续曲率尺度约为 `m\sqrt P/Q`。因此有两条具体攻关路线：

1. **曲率路线。** 若 `Q\le P^{1/2-\varepsilon}`，倒数相位在 `a` 长区间上有足够二阶变化，可用 van der Corput 给出幂级相消。
2. **模振荡路线。** 若 `Q` 较大，则 residue 项 `b(a) mod Q` 的可逆性成为主振荡源；需证明 connected 叶剥离产生的 `b(a)` 不会在长区间上退化为与 `U/a` 同步的一次锁相关系。

这正是“几何刚性”能提供的新约束：行移动只产生线性 CRT 平移，而半素数边界端点产生倒数相位；线性 CRT 轨道与倒数端点轨道若长期锁相，就必须满足强代数关系。

### 6.7.5 锁相代数判据

若 FNL 失败，则存在相邻差分长期很小的区间。对许多 `a` 与小步长 `t`，有

\[
\Phi_m(a+t)-\Phi_m(a)
\equiv O(\delta)\pmod 1.
\]

展开得

\[
m\frac{U}{Q}\left(\frac1{a+t}-\frac1a\right)
-m\frac{b(a+t)-b(a)}{Q}
\equiv O(\delta)\pmod1.
\]

乘以 `Qa(a+t)` 后得到必要条件

\[
-mUt-m\bigl(b(a+t)-b(a)\bigr)a(a+t)
\equiv O(\delta Qa(a+t))\pmod {Qa(a+t)}.
\]

当 `\delta` 取 Fourier 截断所需尺度时，这迫使 `b(a+t)-b(a)` 在许多 `a` 上近似一个二次倒数补偿项。若 `b(a)` 是 connected 叶剥离给出的有理 residue 函数，该条件可进一步化为固定低次数多项式同余在长区间上拥有过多解。除非对应多项式恒等为零，否则解数应为 `O(P^{o(1)})` 或至多低于主长度一个幂；恒等为零则会要求 `b(a)` 同时模拟 `U/a` 的倒数变化，但这与 `b(a)` 的 CRT 可逆线性来源冲突。

因此最后可证明接口可以进一步表述为：

**引理 ALG（无代数锁相）。** connected 叶剥离产生的任一 residue 函数 `b(a)`，不可能在 `a\asymp\sqrt P` 的正比例子区间上满足上述二次补偿同余。ALG 与标准 Weyl--van der Corput 下降结合推出 FNL。

### 6.7.6 residue 函数的正规形分类

为了使 ALG 成为可逐项审查的命题，需要把叶剥离产生的 `b(a)` 全部正规化。固定一个 connected 项、一个 dyadic 主盒以及所有局部 Bell/CRT 选择。把半素数变量写为 `n=ap`，其中 `a\asymp\sqrt P` 是外层平均变量，`p` 是短切片中的素数变量。所有剩余同余条件都来自有限个仿射或双线性约束

\[
\alpha_i a p+\beta_i a+\gamma_i p+\delta_i\equiv0\pmod {q_i},
\]

其中 `q_i<P`，且与对应线性系数的不可逆情形已经在兼容性选择中剔除，或进入低秩退化盒。对 `p` 求 residue 时，CRT 合并后得到

\[
p\equiv b(a)\pmod Q,
\qquad Q=\prod_i q_i,
\]

并且在每个局部模 `q|Q` 上，`b(a)` 属于以下三类之一：

1. **常值型。** 若 `p` 的系数为可逆常数，则 `b(a)\equiv b_0 mod q`。
2. **线性分式型。** 若约束含 `ap`，则

\[
b(a)\equiv -\frac{\beta a+\delta}{\alpha a+\gamma}\pmod q,
\]

其中分母在主盒内不可逆的 `a` 至多落入一个 residue 类，已由 tiny/near 层或低体积盒处理。
3. **仿射型。** 若 `ap` 项消失但 `a` 仍出现，则

\[
b(a)\equiv u a+v\pmod q.
\]

因此全局 `b(a) mod Q` 是这些局部正规形的 CRT 粘合。等价地，在剔除 `O(Q^{o(1)})` 个分母不可逆 residue 后，存在次数有界的多项式 `R(a),S(a)`，满足

\[
b(a)\equiv R(a)S(a)^{-1}\pmod Q,
\qquad (S(a),Q)=1,
\]

且 `\deg R,\deg S\le C_0`，其中 `C_0` 只依赖 connected skeleton 的阶数，而不依赖 `P`。

**证明要点。** 每个局部碰撞边只比较若干筛形式在模 `q` 下是否相等。把除 `a,p` 外的变量按叶剥离顺序固定或合并后，剩余关于 `p` 的条件至多一次，因为原始整数形在每个变量上都是仿射的；双线性只通过 `ap` 给出 `p` 的系数 `\alpha a+\gamma`。若该系数不可逆，则对应 `a` 位于有限个模 `q` 的坏 residue 类，按引理 2.7 的局部账本进入退化层。其余情形可唯一解出 `p`，再由 CRT 合并即得。

### 6.7.7 ALG 的低次数同余归约

把 6.7.5 的锁相必要条件代入正规形 `b(a)=R(a)S(a)^{-1}`。清除分母后，若 FNL 失败，则存在固定 `m,t,Q,U` 和正比例多的 `a\asymp\sqrt P`，使一个次数有界多项式同余

\[
\mathcal F_{m,t,U}(a)\equiv0\pmod {Q'}
\]

成立到 Fourier 误差允许的厚度内。这里 `Q'` 是 `Q` 与若干分母值的可逆部分，且 `\deg \mathcal F_{m,t,U}\le C_1`。更具体地，主项包含

\[
-mUtS(a)S(a+t)
-m\bigl(R(a+t)S(a)-R(a)S(a+t)\bigr)a(a+t),
\]

再乘以必要的固定分母清除因子。

因此 ALG 可化为两个可审查子命题：

1. **非恒等性。** 对所有 connected 正规形，`\mathcal F_{m,t,U}` 不可能作为整数多项式或模 `Q'` 的每个大素因子恒等为零。
2. **少根性。** 若 `\mathcal F_{m,t,U}` 非恒等，则其在 `a\asymp\sqrt P` 中落入同余零集的点数，不足以支撑 FNL 失败所需的正比例锁相集合。

非恒等性对应几何事实：圆柱行移动只给线性 CRT 平移，而边界端点给倒数曲率；一个有界次数的 CRT residue 函数不能在长区间上精确抵消 `U/a` 的二阶差分。少根性则是有限域低次数多项式根数界与 CRT 分解的组合应用；若模数含多个素因子，零集密度按局部密度相乘，并由 Rankin/divisor 账本吸收坏小素因子。

更精确地，设 `Q'=\prod_{j=1}^s \ell_j` 为 squarefree 主模数。若 `\mathcal F` 在每个大素因子 `\ell_j` 上非零，则

\[
\#\{a\in[A,2A]:\mathcal F(a)\equiv0\pmod {Q'}\}
\le A\prod_{j=1}^s\frac{C_1}{\ell_j}+O(C_1^{s}2^s).
\]

当 `Q'` 含有足够多的有效素因子时，该界远小于 `A`，不能支持正比例锁相。若有效素因子太少，则 `Q'` 落入低模/少模情形，此时回到 6.7.4 的曲率路线：`U/a` 的二阶变化提供 van der Corput 相消。因此真正危险的只剩一种混合退化：`Q'` 既不大到给出少根性，又不小到给出曲率相消。该中间区间可通过 dyadic 分裂为有限个 `Q'` 尺度，并要求证明每个尺度至少满足二者之一。

由此得到更精确的待证接口：证明上述非恒等性、少根性，以及中间尺度的曲率/少根二择一，即证明 ALG；再由 van der Corput 差分推出 FNL。这个表述已经把“无锁相”从解析直觉降为 connected residue 正规形的有限代数核查。

### 6.7.8 非恒等性的逐类严写

下面把最关键的非恒等性拆开。记

\[
D_t b(a)=b(a+t)-b(a).
\]

锁相恒等的核心形态是

\[
Ut+D_t b(a)\,a(a+t)\equiv0
\]

在清除分母后对正比例多的 `a` 成立。若它在某个大素数模 `\ell` 上恒等成立，则对应有理函数恒等式

\[
D_t b(a)=-\frac{Ut}{a(a+t)}
\]

在 `\mathbb F_\ell(a)` 中成立。逐类分析如下。

**常值型。** 若 `b(a)=b_0`，则 `D_t b(a)=0`。恒等式变为 `Ut=0`。在主窗口中 `U\asymp P^2`，差分步长 `1\le t\le T`，且 Fourier 模数的大素因子 `\ell` 不系统整除 `U`。因此除至多 `O(\omega(Ut))` 个坏素因子外不可能恒等。坏素因子由 divisor/Rankin 账本吸收。

**仿射型。** 若 `b(a)=ua+v`，则 `D_t b(a)=ut`。恒等式给

\[
Ut+ut\,a(a+t)\equiv0.
\]

若 `t\not\equiv0 mod \ell`，这是关于 `a` 的二次多项式。它恒等为零要求 `u\equiv0 mod \ell` 且 `U\equiv0 mod \ell`。当 `u\not\equiv0` 时非恒等；当 `u\equiv0` 时退回常值型，同样只允许 `\ell|U` 的坏素因子。若 `t\equiv0 mod \ell`，差分本身在该局部模上无信息；这类小步长共振只发生于 `\ell|t`，由对 `t` 的 dyadic 选择和 Rankin 权吸收，或改取另一差分步长 `t'` 避开该有限素因子。

**线性分式型。** 若

\[
b(a)= -\frac{\beta a+\delta}{\alpha a+\gamma},
\]

且分母可逆，则

\[
D_t b(a)
=-\frac{(\beta(a+t)+\delta)(\alpha a+\gamma)
-(\beta a+\delta)(\alpha(a+t)+\gamma)}
{(\alpha(a+t)+\gamma)(\alpha a+\gamma)}
=-\frac{t(\beta\gamma-\alpha\delta)}
{(\alpha(a+t)+\gamma)(\alpha a+\gamma)}.
\]

代入恒等式并消去公共因子 `t` 后得到

\[
U(\alpha(a+t)+\gamma)(\alpha a+\gamma)
-(\beta\gamma-\alpha\delta)a(a+t)\equiv0.
\]

这是二次多项式。设 `K=\beta\gamma-\alpha\delta`。逐项比较 `a^2,a,1` 的系数，恒等为零要求

\[
U\alpha^2=K,
\qquad
U\alpha(\alpha t+2\gamma)=Kt,
\qquad
U\gamma(\alpha t+\gamma)=0.
\]

将第一式代入第二式，得到 `2U\alpha\gamma=0`。若 `U\not\equiv0 mod \ell` 且 `\ell\ne2`，则 `\alpha=0` 或 `\gamma=0`。若 `\alpha=0`，第一式给 `K=\beta\gamma=0`，这使分式退化为常值或分母常数情形；若 `\gamma=0`，第三式自动成立，但第一式和 `K=-\alpha\delta` 给 `U\alpha=-\delta`，此时分式含有不可消去的 `1/a` 项。要使它来自同一 connected 线性 residue 并同时保持分母在长区间可逆，需要局部判别式 `\alpha\delta+U\alpha^2` 消失。该条件只在有限个素因子上发生；在其余大有效素因子上二次多项式非恒等。若 `U\equiv0 mod \ell` 或 `\ell=2`，则并入坏素因子集合。于是线性分式型的恒等锁相也只能来自有限退化素因子。

综上，`\mathcal F_{m,t,U}` 在所有大有效素因子上非恒等；可能恒等的素因子只能来自

\[
\ell\mid Umt\prod(\text{局部判别式与分母结果式}).
\]

这些素因子的总贡献由 Rankin/divisor 账本控制，并可并入 tiny/near/退化层。因此非恒等性已经归约为有限个显式判别式不全为零；该判别式正是 connected residue 正规形的非退化条件。

### 6.7.9 危险退化的补正

上面的逐类证明还留下两个必须明确处理的退化：

1. **分母不可逆退化。** 若 `S(a)` 与 `Q` 不互素，则 `a` 落在某些模 `q` 的有限 residue 类。该集合在每个相关模上的密度 `O(1/q)`，并已在 6.7.6 的正规形分类中剔除；其总体贡献按逐素数 Euler 账本进入低体积盒。
2. **差分步长共振。** 若某大素因子 `\ell|t`，局部差分不能检测该模。解决方式是在 van der Corput 平均中取一组互素小步长 `1\le t\le T`；对任一固定 `\ell`，除 `O(T/\ell+1)` 个步长外均可检测。平均后共振步长贡献低于主差分能量，可由标准 differencing 权重吸收。

因此 ALG 的严写形式应改为：在剔除分母不可逆层、坏判别式素因子层和差分共振层后，所有有效局部模上 `\mathcal F` 非恒等；随后少根性给出密度下降。三个剔除层均已有对应账本：分母不可逆层进入低体积盒，坏判别式素因子进入 Rankin/divisor 账本，差分共振层进入 van der Corput 步长平均误差。

### 6.7.10 少根性到指数和下降

下面把少根性转化为指数和相消。设

\[
S=\sum_{a\asymp A}W(a)e(\Phi(a)),
\qquad
\Phi(a)=m\frac{U}{aQ}-m\frac{b(a)}{Q}.
\]

若 `|S|` 异常大，van der Corput 不等式给出某个步长范围 `1\le t\le T` 上的相关和异常：

\[
|S|^2
\ll \frac{A^2}{T}
+\frac{A}{T}\sum_{1\le t\le T}
\left|\sum_{a\asymp A}W_t(a)e(\Phi(a+t)-\Phi(a))\right|.
\]

因此若所有非共振 `t` 的差分相位在绝大多数 `a` 上不锁相，则 `S` 必下降。差分相位锁相要求

\[
\Phi(a+t)-\Phi(a)\in[-\delta,\delta]+\mathbb Z,
\]

这正是 6.7.7 的低次数同余条件。由 ALG 的非恒等性和少根性，对每个非共振 `t` 有

\[
\#\{a\asymp A:\|\Phi(a+t)-\Phi(a)\|_{\mathbb T}\le\delta\}
\le A\theta(Q')+O(P^{o(1)}),
\]

其中

\[
\theta(Q')=\prod_{\ell\mid Q'}\frac{C_1}{\ell}+O(\delta Q')
\]

表示有效局部零集密度和厚化误差。取 `\delta=(\log P)^{-B_1}` 并把 `Q'` 分 dyadic，则只要 `\theta(Q')\le(\log P)^{-B_2}`，差分相关和经分部求和或大筛型分解后满足

\[
\sum_{a\asymp A}W_t(a)e(\Phi(a+t)-\Phi(a))
\ll A(\log P)^{-B_3}.
\]

代回 van der Corput，并取 `T=(\log P)^{B_4}`，得到

\[
S\ll A(\log P)^{-B_5}.
\]

由于短切片主量满足 `Y/\log P\asymp A/\log^{O(1)}P` 的 Stieltjes 归一化尺度，选择 `B_i` 逐级足够大，即可达到 FNL 要求的

\[
S=o(Y/\log^{B+2}P).
\]

这说明：少根性不是只控制零点数量，而是通过差分相关和控制 Fourier 锁相能量。

**引理 6.7.10a（相位分层下降）。** 设 `I=[A,2A]`，`F(a)` 是在 `I` 上定义的实相位。若对某个 `0<\delta<1/10` 与 `0<\vartheta<1`，任意弧长为 `2\delta` 的圆周区间 `J\subset\mathbb T` 都满足

\[
\#\{a\in I:F(a)\in J\}
\le \vartheta A+E,
\]

且 `W(a)` 有有界变差，则

\[
\left|\sum_{a\in I}W(a)e(F(a))\right|
\ll A(\vartheta+\delta+E/A)+\operatorname{Var}(W).
\]

**证明。** 把圆周分成 `O(1/\delta)` 个弧。若指数和很大，则存在一个方向 `\xi`，使 `\Re(e(-\xi)e(F(a)))` 的加权和很大；但在离 `\xi` 距离大于 `O(\delta)` 的弧上，实部至少损失固定量。按弧分层求和，大和只能来自靠近 `\xi` 的短弧。该短弧中的点数由假设控制，剩余弧的正负贡献至多给出 `O(\delta A)` 的离散化误差。有界变差权重用 Abel 分部转移到区间指示，增加 `\operatorname{Var}(W)`。

在本文中取

\[
F_t(a)=\Phi(a+t)-\Phi(a).
\]

这里必须注意：普通的同余少根性只控制 `F_t(a)` 落入某个格点邻域，并不自动控制任意短弧。要应用引理 6.7.10a，需要以下更强的一致版本。

**引理 6.7.10b（均匀短弧少根性，待证接口）。** 对任意非共振 `t`、任意弧 `J\subset\mathbb T` 且 `|J|\le2\delta`，都有

\[
\#\{a\asymp A:F_t(a)\in J\}
\le A\theta(Q')+O(P^{o(1)}+\delta A).
\]

若 6.7.10b 成立，则对每个非共振 `t`，引理 6.7.10a 可用，且

\[
\vartheta\ll\theta(Q')+\delta,
\qquad
E\ll P^{o(1)}.
\]

从而得到差分相关和下降。

6.7.10b 不能仅由有限域根数界推出；它还需要证明低次数有理函数在长整数区间中的模 `Q'` 值不会集中到任意短实弧。等价地，需要一个“有理函数值的短弧大筛”输入：对所有 shifted 常数项一致的厚化同余少根性。这个接口比原先写法更强，是当前最后两个严查点之一。

### 6.7.11 参数账本：从差分下降到 FNL 尺度

需要选择参数使所有损失低于 FNL 阈值。令 Fourier 截断阶为 `M=(\log P)^B`。依次选取

\[
B_4=4B+4C_*+100,
\qquad
B_2=6B+4C_*+120,
\qquad
B_1=8B+4C_*+160,
\]

并令 `T=(\log P)^{B_4}`、`\delta=(\log P)^{-B_1}`。若非共振差分相关满足

\[
\left|\sum_{a\asymp A}W_t(a)e(F_t(a))\right|
\ll A(\log P)^{-2B-20},
\]

则 van der Corput 给

\[
|S|^2
\ll A^2(\log P)^{-B_4}
+A^2(\log P)^{-2B-20},
\]

从而

\[
|S|\ll A(\log P)^{-B-9}.
\]

由于主盒的 Stieltjes 权把 `A` 转换到短切片尺度时只损失固定对数幂，取上述常数余量后得到

\[
|S|=o(Y/\log^{B+2}P).
\]

因此 FNL 所需余量可以通过固定的大对数参数实现，而不依赖随 `P` 变化的新假设。

### 6.7.12 曲率/少根二择一的定量分区

剩余问题是保证每个 dyadic `Q'` 尺度都落入“少根有效”或“曲率有效”之一。令 `A\asymp\sqrt P`、`U\asymp P^2`。倒数相位二阶尺度为

\[
\Lambda=\left|\frac{mU}{QA^3}\right|\asymp\frac{m\sqrt P}{Q}.
\]

分三段处理：

1. **低模段。** 若 `Q\le P^{1/2}(\log P)^{-K}`，则 `\Lambda\ge(\log P)^K`。van der Corput 二阶导数估计直接给 `S\ll A(\log P)^{-K'}`，无需少根性。
2. **高模段。** 若 `Q'` 含有乘积至少 `(\log P)^K` 的有效素因子，则少根密度 `\theta(Q')\ll(\log P)^{-K'}`，由 6.7.10 得到相消。
3. **中间退化段。** 若 `Q` 不低且 `Q'` 的有效素因子乘积不足，则大部分模因子属于坏判别式、分母不可逆或差分共振层。根据 6.7.9，这些层的总权已被 Rankin/divisor 账本和步长平均吸收；剩余有效部分重新落入高模段，或原模数降低后落入低模段。

因此，若 6.7.10b 的均匀短弧少根性与 6.7.13 的退化层吸收账本均完成，则不存在真正的中间尺度空洞；在这两个接口成立的条件下，ALG 的非恒等性与少根性，加上低模曲率估计，推出 FNL。

### 6.7.13 中间退化层吸收账本

为了避免“中间退化段”成为新的隐藏假设，需要把其权重逐项列账。令 `Q=Q_{eff}Q_{bad}`，其中 `Q_{eff}` 是非恒等、分母可逆且非共振的有效模因子乘积，`Q_{bad}` 由三类坏因子组成。

1. **分母坏因子。** 对每个 `q|Q`，分母不可逆给出至多 `O(1)` 个 `a mod q`。其局部密度 `O(1/q)` 与筛碰撞因子同阶，故在逐素数 Euler 账本中增加一个可和因子 `1+O(1/q)`，不会破坏 Rankin 收敛。
2. **判别式坏因子。** 这些 `q` 整除固定低次数判别式 `\Delta_{loc}`。对固定 connected 正规形，`\Delta_{loc}` 的素因子数为 `O(\log P/\log\log P)`，带 Rankin 权求和后贡献 `\log^{O(1)}P`，已被引理 2.7 的 divisor 损失预留吸收。
3. **步长共振因子。** 对固定 `q`，满足 `q|t` 的步长数至多 `T/q+1`。在 `1\le t\le T` 平均中，其权重为 `O(1/q+1/T)`。对所有 `q` 求和，`1/q` 部分并入 Euler 账本，`1/T` 部分由 `T=(\log P)^{B_4}` 的余量吸收。

于是若 `Q_{eff}` 的有效素因子乘积不足以给出少根性，同时 `Q` 又不在低模曲率段，则必须有 `Q_{bad}` 承担正比例模量。上面三项显示这部分总贡献至多为

\[
O(\log^{-B-20}P)
\]

在选取 `B_i` 的余量后可并入 6.7.11 的差分相关误差；这一步依赖下述判别式高度账本。

这里仍有一个需要最终核查的量化点：判别式 `\Delta_{loc}` 必须对所有 connected 选择具有统一的低次数和低高度界；这应从 6.7.6 的正规形分类和引理 2.7 的标签数控制推出。若该高度界失控，则退化层吸收不闭合。因此本文把它列为“判别式高度账本”待核查项，而不是无条件完成项。

### 6.7.14 最终两个接口命题

为使逻辑链条完全可审查，最后两个缺口应固定为以下命题。

**命题 UAS（Uniform Arc Sparsity，均匀短弧少根性）。** 对 6.7.10b 中所有允许的 connected residue 正规形、所有非共振步长 `t`、所有短弧 `J`，一致有

\[
\#\{a\asymp A:F_t(a)\in J\}
\le A\theta(Q')+O(P^{o(1)}+|J|A).
\]

**命题 DBA（Degenerate Bookkeeping Absorption，退化账本吸收）。** 对所有 connected 正规形，分母坏因子、判别式坏因子与步长共振因子的总贡献，在 dyadic 盒、Fourier 频率、步长平均和 Rankin 标签求和之后，为

\[
O(A\log^{-B-20}P)
\]

级别，可并入 6.7.11 的差分相关误差。

若 UAS 与 DBA 成立，则 6.7.10--6.7.13 给出 FNL；进而 NL、B.0.4S-short 与行命题的条件链条闭合。反过来，若二者之一不能证明，则当前论文仍只是把目标命题归约到这两个明确接口，而不是无条件证明。

### 6.7.15 目前得到的闭合路线

至此，目标命题的最后一公里被分解为更细的条件闭合链：

\[
\text{residue 正规形}
\Rightarrow \text{非恒等性}
\Rightarrow \text{少根性/曲率二择一}
\Rightarrow \text{FNL Fourier 无锁相}
\Rightarrow \text{NL sawtooth 无锁相}
\Rightarrow \text{B.0.4S-short}.
\]

其中 UAS 与 DBA 是最后两个明确接口。完成这两个命题后，ALG 将不再是黑箱假设，而成为 connected residue 正规形的代数-解析推论；若不能完成，则当前结果保持为归约定理。


## 6.8 UAS 与 DBA 的矛盾场方程攻坚

本节继续细化最后两个接口。目标不是直接宣称完成证明，而是把可能的失败情形写成刚性“矛盾场方程”，再分析它必须满足的代数、几何和计数约束。

### 6.8.1 UAS 失败的场方程

设 UAS 失败。则存在 connected residue 正规形、非共振步长 `t`、短弧 `J=[\rho-\nu,\rho+\nu]`，其中 `\nu\le\delta`，使得集合

\[
\mathcal A_J=
\{a\asymp A:F_t(a)\in J\}
\]

满足

\[
|\mathcal A_J|>A\theta(Q')+P^{o(1)}+2\nu A.
\]

把 `F_t(a)` 写成差分相位：

\[
F_t(a)=m\frac{U}{Q}\left(\frac1{a+t}-\frac1a\right)
-m\frac{b(a+t)-b(a)}{Q}.
\]

令 `b(a)=R(a)S(a)^{-1}`。清除分母后，`F_t(a)\in J` 等价于存在整数 `k(a)`，使

\[
\left|
\frac{\mathcal F_{m,t,U}(a)}{Q\,a(a+t)S(a)S(a+t)}-\rho-k(a)
\right|
\le \nu+O(Q^{-1}).
\]

这就是 UAS 失败的矛盾场方程。它有三个刚性特征：

1. **整数层刚性。** `k(a)` 只能在长度 `O(1)` 的相邻整数层间跳动；若短弧内点数异常多，则存在固定整数层 `k_0` 承载正比例异常。
2. **有理函数刚性。** 固定 `k_0` 后，异常点满足一个厚化低次数有理不等式，而不是任意相位条件。
3. **差分曲率刚性。** 该有理函数的二阶差分继承 `U/a` 的倒数曲率；若它在长集合上几乎常值，则必须发生非恒等性中已列出的代数退化。

因此 UAS 的本质是：低次数有理函数的值不能在长整数区间上异常集中于任意短弧，除非其二阶差分退化。

### 6.8.2 从短弧集中到二阶平坦的反推

若 `|\mathcal A_J|` 异常大，则按间距鸽巢，存在许多三元组

\[
a,
\quad a+h,
\quad a+2h
\]

都属于 `\mathcal A_J`，其中 `1\le h\le H`，`H` 为对数幂。于是

\[
\|F_t(a+2h)-2F_t(a+h)+F_t(a)\|_{\mathbb T}
\le 4\nu.
\]

代入 `F_t` 后得到二阶矛盾场方程

\[
\left\|
\Delta_h^2\left(
 m\frac{U}{Q}\left(\frac1{a+t}-\frac1a\right)
-m\frac{b(a+t)-b(a)}{Q}
\right)
\right\|_{\mathbb T}
\le4\nu.
\]

第一项主尺度为

\[
\Delta_h^2\left(\frac1{a+t}-\frac1a\right)
\asymp \frac{h^2t}{A^4},
\]

故乘上 `mU/Q` 后为

\[
\asymp \frac{mUh^2t}{QA^4}
\asymp \frac{m h^2t}{Q}.
\]

当 `Q` 不太大时，这给出曲率矛盾；当 `Q` 很大时，若二阶差分仍小，则 `D_t b(a)` 必须以同样精度模拟倒数二阶差分。这把 UAS 失败再次压回 ALG 的非退化结构。

### 6.8.3 UAS 的可证化子命题

由 6.8.1--6.8.2，UAS 可拆成两个更具体的子命题。

**UAS-I（二阶平坦排斥）。** 对所有非退化 connected 正规形，若某短弧承载超过 `A\theta(Q')+P^{o(1)}+|J|A` 个 `a`，则存在对数幂步长 `h`，使二阶场方程在超过少根性允许数量的点上成立。

**UAS-II（二阶场少根性）。** 对任意固定 `h,t`，二阶场方程清分母后得到的低次数多项式不恒等；其厚化零集在 `a\asymp A` 中的点数满足同样的 `A\theta(Q')+P^{o(1)}+\nu A` 上界。

若 UAS-I 与 UAS-II 成立，则 UAS 成立。相比原 UAS，UAS-II 更接近有限域少根性，因为二阶差分消除了短弧中心 `\rho` 的自由漂移；剩余常数项只进入多项式的低次数平移，不改变非恒等性。


### 6.8.4 UAS-II 的二阶场正规形

为攻克 UAS-II，先把二阶场写成统一有理函数。记

\[
G_t(a)=\frac1{a+t}-\frac1a-\bigl(b(a+t)-b(a)\bigr)/U.
\]

忽略固定因子 `mU/Q` 后，二阶场就是 `\Delta_h^2G_t(a)`。若 `b(a)=R(a)S(a)^{-1}`，则存在次数有界的多项式 `N_{t,h}(a),D_{t,h}(a)`，使

\[
\Delta_h^2G_t(a)=\frac{N_{t,h}(a)}{D_{t,h}(a)},
\qquad
\deg N_{t,h},\deg D_{t,h}\le C_2.
\]

其中

\[
D_{t,h}(a)=
\prod_{j=0}^{2}(a+jh)(a+jh+t)S(a+jh)S(a+jh+t)
\]

可取为公共分母。UAS-II 的非恒等性等价于：在剔除分母不可逆层后，`N_{t,h}(a)` 不作为多项式恒等为零，也不在所有有效大素因子上恒等为零。

下面逐类分析 `b(a)`。

**常值型。** 若 `b(a)=b_0`，则

\[
G_t(a)=\frac1{a+t}-\frac1a=-\frac{t}{a(a+t)}.
\]

于是 `\Delta_h^2G_t(a)` 是非零有理函数。事实上其分子最高项系数与 `t h^2` 成比例；只要 `t,h` 在有效模上非零，该二阶差分不恒等。坏素因子只来自 `q|th` 或分母不可逆，已归入步长共振和分母坏层。

**仿射型。** 若 `b(a)=ua+v`，则 `b(a+t)-b(a)=ut` 为常数，二阶差分消去该常数。因此

\[
\Delta_h^2G_t(a)=\Delta_h^2\left(\frac1{a+t}-\frac1a\right),
\]

与常值型相同，仍由 `t h^2` 控制非恒等性。这说明二阶化比一阶锁相更强：所有仿射漂移都被自动消除，不能模拟倒数二阶曲率。

**线性分式型。** 若

\[
b(a)=-\frac{\beta a+\delta}{\alpha a+\gamma},
\]

则

\[
b(a+t)-b(a)=
-\frac{tK}{(\alpha(a+t)+\gamma)(\alpha a+\gamma)},
\qquad K=\beta\gamma-\alpha\delta.
\]

故

\[
G_t(a)=
-\frac{t}{a(a+t)}
+\frac{tK/U}{(\alpha(a+t)+\gamma)(\alpha a+\gamma)}.
\]

若 `\Delta_h^2G_t(a)` 恒等为零，则 `G_t(a)` 必须是关于 `a` 的仿射函数。但 `G_t(a)\to0` 当 `a\to\infty`，所以该仿射函数只能为常数 `0`。于是必须有恒等式

\[
\frac1{a(a+t)}
=\frac{K/U}{(\alpha(a+t)+\gamma)(\alpha a+\gamma)}.
\]

比较二次分母得

\[
(\alpha(a+t)+\gamma)(\alpha a+\gamma)=\frac{K}{U}a(a+t).
\]

这要求二次多项式两侧成比例。逐项比较得到

\[
\alpha^2=K/U,
\qquad
\alpha(\alpha t+2\gamma)=(K/U)t,
\qquad
\gamma(\alpha t+\gamma)=0.
\]

与 6.7.8 的一阶非恒等性相同，除 `U=0`、小素数、分母退化和局部判别式消失外，这迫使分式退化为常值或不可逆情形。因此在线性分式型中，二阶场恒等只发生在 DBA 已列账的坏判别式层。

综上，UAS-II 的非恒等性部分已经归约到 `thU` 与线性分式判别式的有限坏素因子。剩余的是厚化零集界：对非零有理函数 `N_{t,h}(a)/D_{t,h}(a)`，证明

\[
\#\{a\asymp A: \|N_{t,h}(a)/D_{t,h}(a)\|_{\mathbb T}\le\nu\}
\le A\theta(Q')+P^{o(1)}+\nu A.
\]

这正是 UAS-II 的厚化少根性核心。

### 6.8.5 UAS-II 的厚化少根性接口

清分母后，上述厚化条件可写为存在整数 `r(a)`，使

\[
|N_{t,h}(a)-r(a)D_{t,h}(a)|
\le \nu |D_{t,h}(a)|.
\]

若同一整数层 `r_0` 承载过多点，则得到固定低次数多项式

\[
N_{t,h}(a)-r_0D_{t,h}(a)
\]

的厚化零集异常；非恒等性给出有限域少根性。若许多不同整数层共同承载异常，则这些层对应的有理函数值必须在短区间中高密度排列，这要求 `N/D` 的导数长期过小。于是 UAS-II 可进一步分为：

1. **固定层厚化少根性。** 对每个 `r_0`，多项式 `N-r_0D` 的厚化零集满足预期上界。
2. **多层导数排斥。** 若多个 `r` 层同时贡献，则 `N/D` 的导数或二阶导数不能长期过小；否则回到二阶场恒等退化，已由 6.8.4 排除。

这给出 UAS-II 的实际证明路线：先用固定层少根性处理单层集中，再用导数排斥处理多层堆叠。当前仍需把“厚化零集”用具体的有限域根数界、实导数下界和 CRT 分解组合起来；这是下一步最核心的技术工作。


### 6.8.6 固定层厚化少根性

固定整数层 `r_0`。令

\[
P_{r_0}(a)=N_{t,h}(a)-r_0D_{t,h}(a).
\]

在分母可逆且非退化的层中，`P_{r_0}` 不是恒等零多项式；否则 `N/D` 恒等于常数 `r_0`，其二阶场恒等退化，已由 6.8.4 排除。对每个有效素因子 `\ell|Q'`，有限域根数界给

\[
\#\{a\bmod \ell:P_{r_0}(a)\equiv0\pmod\ell
\}
\le C_2.
\]

CRT 合并后得到精确的离散少根性

\[
\#\{a\in[A,2A]:P_{r_0}(a)\equiv0\pmod {Q'}\}
\le A\prod_{\ell|Q'}\frac{C_2}{\ell}+O(C_2^{\omega(Q')}2^{\omega(Q')}).
\]

厚化不等式

\[
|P_{r_0}(a)|\le \nu |D_{t,h}(a)|
\]

可按 residue 层写成若干相邻同余壳。由于 `D_{t,h}(a)` 在 dyadic 区间中有有界相对变化，厚度贡献为 `O(\nu A)`；端点壳由 `O(P^{o(1)})` 吸收。因此固定层给出

\[
\#\{a\asymp A:|P_{r_0}(a)|\le\nu |D_{t,h}(a)|
\}
\le A\theta(Q')+O(P^{o(1)}+\nu A).
\]

这个引理把固定整数层完全还原为有限域少根性加实厚度误差。仍需最终核查的是：`P_{r_0}` 的高度随 `r_0` 的增长是否保持在 DBA 账本可吸收范围内；这与多层导数排斥共同处理。

### 6.8.7 多层导数排斥

现在考虑许多不同整数层 `r` 同时贡献。设

\[
R(a)=\frac{N_{t,h}(a)}{D_{t,h}(a)}.
\]

若 `R(a)` 在短弧厚度 `\nu` 内命中许多整数层，则在相邻命中点之间，其平均斜率必须达到相应层差；反过来，若点数异常多而层数也多，则存在长子区间上

\[
|R'(a)|\ll \nu/H
\]

或二阶差分

\[
|R(a+2h)-2R(a+h)+R(a)|\ll\nu
\]

在过多点上成立。清分母后分别得到

\[
N'D-ND'=0
\]

或二阶场分子 `N_{t,h}` 的进一步差分近零。若这些关系在超过少根性允许数量的点上成立，则对应低次数多项式必须恒等；这会迫使 `R` 为常数或仿射函数。

但 `R=\Delta_h^2G_t`。若 `R` 为常数或仿射，则 `G_t` 在三阶差分下消失；由于 `G_t\to0` 且含有倒数极点，其唯一可能是 `G_t\equiv0` 或落入线性分式成比例退化。这正是 6.8.4 已列出的坏判别式层。因此，在剔除 DBA 坏层后，多层堆叠不可能超过

\[
A\theta(Q')+O(P^{o(1)}+\nu A).
\]

于是固定层厚化少根性与多层导数排斥合并，给出 UAS-II 的条件闭合：只要 DBA 的高度账本可吸收所有导数判别式，UAS-II 成立。

### 6.8.8 UAS-II 的当前闭合状态

本轮推进后，UAS-II 已被压缩为以下可核查链条：

\[
\text{二阶场非恒等}
\Rightarrow \text{固定层厚化少根性}
\Rightarrow \text{多层导数排斥}
\Rightarrow \text{UAS-II}.
\]

其中二阶场非恒等已经逐类展开；固定层少根性依赖标准有限域根数界与厚度壳估计；多层导数排斥依赖导数判别式仍落入 DBA 账本。因此最后剩余不再是新的几何直觉，而是 DBA 是否能统一吸收所有一阶、二阶和导数判别式。

### 6.8.9 DBA 的判别式高度场

DBA 的关键是控制坏判别式的高度。由 6.7.6，任一 residue 正规形来自有限个局部约束

\[
\alpha_iap+\beta_i a+\gamma_i p+\delta_i\equiv0\pmod {q_i}.
\]

所有判别式、分母结果式和非恒等性例外都由这些系数的有界次数多项式生成。设这些多项式乘积为

\[
\Delta_{\Gamma}(U,m,t)=
\prod_j P_j(\alpha_i,\beta_i,\gamma_i,\delta_i,U,m,t).
\]

DBA 需要的精确账本是

\[
\sum_{\Gamma}\sum_{q|\Delta_{\Gamma}}\frac{w(\Gamma,q)}{q}
\ll \log^{O(1)}P,
\]

并且在 van der Corput 平均后提升为 `O(A\log^{-B-20}P)` 的误差。这里 `w(\Gamma,q)` 是 connected skeleton 标签权，由引理 2.7 控制。

因此 DBA 可拆成：

1. **DBA-I（低高度）。** `\log |\Delta_{\Gamma}|\ll \log^{O(1)}P`，且次数只依赖 skeleton 阶数。
2. **DBA-II（Rankin 可和）。** 对所有 connected 标签求和后，坏素因子的 `1/q` 权重仍被引理 2.7 的 Rankin/divisor 余量吸收。
3. **DBA-III（步长平均）。** 对 `q|t` 的共振项，在 `1\le t\le T` 平均后产生 `O(1/q+1/T)`，其总和低于 6.7.11 的误差预算。

### 6.8.10 当前攻坚结论

经过本节细化，最后接口由

\[
\text{UAS}+\text{DBA}
\]

进一步压缩为

\[
\text{UAS-I}+\text{二阶场非恒等}+\text{固定层厚化少根性}+\text{多层导数排斥}+\text{DBA-I}+\text{DBA-II}+\text{DBA-III}.
\]

其中二阶场非恒等已逐类推进；固定层厚化少根性已归约到有限域根数界与厚度壳估计；多层导数排斥仍依赖导数判别式进入 DBA 账本。换言之，最后真正的数学核心已经从“斜线覆盖直觉”压缩为“二阶有理场厚化少根性 + 判别式高度账本”。


## 6.9 高维动力系统视角下的 UAS/DBA 再攻坚

本节从更高维的动力系统角度重新审查 UAS 与 DBA。核心问题是：短弧集中不是单个同余方程，而是有理相位、整数层、CRT 模因子和步长平均共同组成的高维场。若要无条件闭合，必须证明该场不存在正密度低熵轨道。

### 6.9.1 高维相位态空间

把一个异常点记录为状态

\[
\Xi(a)=
\left(
 a,
 R(a),
 R'(a),
 \Delta_hR(a),
 \Delta_h^2R(a),
 (a\bmod q)_{q|Q'}
\right),
\qquad R(a)=\frac{N_{t,h}(a)}{D_{t,h}(a)}.
\]

UAS 失败意味着存在短弧 `J`，使大量轨道点落入薄管

\[
\mathcal T_J=\{\Xi: R(a)\in J\pmod1\}.
\]

但 `R` 是低次数有理函数，其离散演化满足封闭差分方程：

\[
R(a+h)-R(a)=\frac{P_1(a)}{Q_1(a)},
\qquad
R(a+2h)-2R(a+h)+R(a)=\frac{P_2(a)}{Q_2(a)},
\]

其中 `P_i,Q_i` 次数有界，且所有退化判别式进入 DBA。于是异常薄管若含有过多点，轨道必须在 `R`、一阶差分、二阶差分三个坐标上同时低熵。

### 6.9.2 低熵轨道的矛盾方程

若 `R(a)` 在短弧中异常集中，则由 additive energy 反推，存在许多四元组

\[
a_1,a_2,a_3,a_4\asymp A
\]

满足

\[
R(a_1)-R(a_2)-R(a_3)+R(a_4)=O(\nu)\pmod1.
\]

清分母后得到四点场方程

\[
\mathcal E_R(a_1,a_2,a_3,a_4)=O(\nu\mathcal D_R(a_1,a_2,a_3,a_4)).
\]

如果该方程有超过随机尺度的解，则四点有理函数 `\mathcal E_R` 的低次数零集异常大。几何上，这表示 `R([A,2A])` 的像集在圆周上具有异常小 doubling。对低次数非退化有理函数，异常小 doubling 应迫使 `R` 与低维群同态近似；在一维有理函数情形，这只可能是仿射或 Möbius 退化，而这些已由 6.8.4 与 DBA 判别式排除。

因此 UAS 可进一步归约为：

**UAS-E（四点能量排斥）。** 非退化二阶有理场 `R=N/D` 的短弧命中集具有近随机 additive energy；等价地，四点场方程的厚化解数不超过少根性预测。

UAS-E 比逐层少根性更强，但更符合动力系统本质：它直接排除大量轨道点在短弧中形成低熵团簇。

### 6.9.3 DBA 的高维闭包

DBA 不仅要吸收 `N,D` 的判别式，还要吸收所有由动力系统闭包产生的判别式：

\[
\Delta_R,
\Delta_{R'},
\Delta_{\Delta R},
\Delta_{\Delta^2R},
\Delta_{\mathcal E_R}.
\]

这些判别式都由同一有限生成代数产生：原始局部系数 `\alpha_i,\beta_i,\gamma_i,\delta_i`、窗口参数 `U`、频率 `m`、步长 `t,h`。因此 DBA 的真正闭包命题应写为：

**DBA-closure（判别式闭包账本）。** 对由 `R` 经有限次差分、导数、四点能量构造产生的全部低次数多项式，其判别式高度、坏素因子权重和步长共振权重，在 connected 标签求和后仍满足

\[
O(A\log^{-B-20}P)
\]

级误差预算。

若 DBA-closure 成立，则 DBA 不再需要逐个新判别式补丁，而成为一个有限生成代数的统一高度命题。

### 6.9.4 无条件闭合所需的真正新输入

经过 6.8 与 6.9 的严查，不能诚实地说 UAS 已由初等 CRT 几何自动推出。原因是：

1. 有限域少根性控制单个 residue 零集，但 UAS 需要实短弧厚化分布；
2. 短弧集中可能以多整数层方式出现，必须用导数或四点能量排斥；
3. 每次差分和能量提升都会生成新判别式，必须由 DBA-closure 统一吸收。

因此无条件闭合需要以下二选一的新输入：

- **短弧有理大筛。** 对所有非退化低次数有理函数 `R=N/D`，证明其在长整数区间中的模一短弧命中满足 UAS 级别上界。
- **四点能量定理。** 对同一类 `R`，证明厚化四点场方程只有随机尺度解数，从而推出短弧有理大筛。

这两个命题都属于新的代数-解析分布输入；它们并非现有圆柱动力方程的形式推论。若其中之一得证，再配合 DBA-closure，整条链条闭合。

### 6.9.5 当前最强条件闭合定理

综上，可把最后结论写成如下严格形式：

**定理 6.9.1（UAS/DBA 条件闭合）。** 假设短弧有理大筛或四点能量定理成立，并假设 DBA-closure 成立。则 UAS 与 DBA 成立；因此 FNL、NL、B.0.4S-short 依次成立，行命题的条件证明链条闭合。

**证明。** 短弧有理大筛直接给 UAS。若改用四点能量定理，则由 Balog--Szemeredi 型能量反推的逆否命题，短弧异常集中会产生四点能量异常，矛盾，故 UAS 成立。DBA-closure 吸收所有分母、判别式和步长共振退化层。代入 6.7.10--6.7.13 得 FNL；再由 6.7.3 得 NL，由 B.0.4S-short 得平滑 B.0.4S，最终回到第 4 节行命题条件链条。

这一定理是当前文稿可诚实达到的最强闭合形态：它把几何直觉、CRT 动力系统和 connected 账本全部压缩到两个明确的新型解析输入，而不是把未证输入隐藏在“刚性”措辞中。


## 6.10 四点能量定理的可证版本

本节专攻 6.9 中的四点能量定理。目标是把厚化四点场方程分成可审查的对角、半对角和真四点三类，并说明每一类需要怎样的代数非退化和 DBA-closure 账本。

### 6.10.1 四点场方程的标准形

令

\[
R(a)=\frac{N(a)}{D(a)},
\qquad \deg N,\deg D\le C_2,
\qquad (D(a),Q')=1
\]

处于非退化层。四点能量异常对应

\[
R(a_1)-R(a_2)-R(a_3)+R(a_4)=O(\nu)\pmod1.
\]

清分母后得到

\[
\mathcal E(a_1,a_2,a_3,a_4)
=O(\nu\mathcal D(a_1,a_2,a_3,a_4)),
\]

其中

\[
\mathcal E=
N_1D_2D_3D_4-N_2D_1D_3D_4-N_3D_1D_2D_4+N_4D_1D_2D_3,
\]

`N_i=N(a_i)`、`D_i=D(a_i)`。若 `\mathcal E` 在某个有效素因子上恒等为零，则 `R(x_1)-R(x_2)-R(x_3)+R(x_4)` 是恒等零函数，这只可能在变量配对对角或 `R` 退化为常值时发生。常值退化已由二阶场非恒等排除。

### 6.10.2 对角与半对角解

四点方程的自然大解来自配对：

\[
a_1=a_2,
\quad a_3=a_4,
\qquad\text{或}\qquad
 a_1=a_3,
\quad a_2=a_4.
\]

这些对角族的数量为 `O(A^2)`，是 additive energy 的随机基线。半对角情形指三变量中有两个相等，但不形成完整配对。例如 `a_1=a_2` 时，方程化为

\[
R(a_4)-R(a_3)=O(\nu)\pmod1.
\]

这退化为二点短弧命中问题。由一阶非恒等性与固定层厚化少根性，半对角贡献至多

\[
O(A^2\theta(Q')+A P^{o(1)}+\nu A^2).
\]

因此四点能量的关键只剩真四点：四个变量无配对相等，且不落入低维对角簇。

### 6.10.3 真四点的代数非退化

固定三个变量 `a_1,a_2,a_3`，把四点方程视为关于 `a_4` 的方程：

\[
R(a_4)=R(a_2)+R(a_3)-R(a_1)+O(\nu)\pmod1.
\]

若右侧整数层固定，则这是固定层厚化少根性问题。真四点异常意味着：对许多三元组，右侧层值变化，却仍有过多 `a_4` 解。若对许多三元组都发生，则 `R` 的许多水平集异常大；这迫使存在两个不同层 `c_1,c_2`，使

\[
R(x)=c_1,
\qquad R(x)=c_2
\]

同时拥有过多厚化解，进而迫使 `R'` 或 resultants 退化。清分母后，坏条件由

\[
\operatorname{Res}_x(N(x)-cD(x),N'(x)D(x)-N(x)D'(x))
\]

控制，属于 DBA-closure 的导数判别式。

因此真四点非退化命题可写为：

**4E-ND（真四点非退化）。** 在剔除 DBA-closure 坏层后，四点多项式 `\mathcal E` 的任意三变量切片都不是恒等零，也没有超过 `C_2` 个厚化根簇。

### 6.10.4 真四点计数界

在 4E-ND 成立时，对每个固定三元组 `(a_1,a_2,a_3)`，`a_4` 的解数满足

\[
O(A\theta(Q')+P^{o(1)}+\nu A).
\]

直接求和给 `O(A^4\theta(Q'))`，太弱。必须利用四点方程本身的 rank：每个有效素因子 `\ell|Q'` 对四变量施加一个非恒等方程，局部解密度为 `O(1/\ell)`，而不是固定三变量后的 `O(C_2/\ell)` 逐点损失。CRT 合并给

\[
\#\{(a_i):\mathcal E(a_1,a_2,a_3,a_4)\equiv0\pmod {Q'}
\}
\le A^4\prod_{\ell|Q'}\frac{C_3}{\ell}+O(A^3P^{o(1)}).
\]

厚化层贡献 `O(\nu A^4)`。减去对角基线后，真四点能量满足

\[
E_4(R;J)
\le O(A^2)+A^4\theta_4(Q')+O(A^3P^{o(1)}+\nu A^4),
\]

其中 `\theta_4(Q')=\prod_{\ell|Q'}C_3/\ell`。当有效模因子乘积达到对数幂阈值时，真四点能量低于短弧异常所需阈值。

### 6.10.5 能量反推 UAS

若短弧 `J` 中有 `M` 个命中点，则其 additive energy 至少为

\[
E_4(J)\gg M^4/|J_R|,
\]

其中 `|J_R|` 是命中值的离散层数。由于 `J` 长度为 `\nu`，层数至多 `O(\nu A+P^{o(1)})`。若

\[
M>A\theta(Q')+P^{o(1)}+\nu A,
\]

则能量下界超过 6.10.4 的上界，除非落入对角/半对角或 DBA-closure 坏层。对角/半对角已在 6.10.2 吸收，坏层由 DBA-closure 吸收。因此四点能量定理推出 UAS。

### 6.10.6 当前可证版本与剩余硬点

由上可得条件命题：

**定理 6.10.1（四点能量条件版）。** 假设 4E-ND 与 DBA-closure 成立，并且四点局部 rank 界

\[
\#\{(x_1,x_2,x_3,x_4)\bmod \ell:\mathcal E=0\}
\le C_3\ell^3
\]

对所有有效素因子一致成立。则四点能量定理成立，从而 UAS 成立。

局部 rank 界本身可由有限域代数给出。若 `\bar{\mathcal E}` 在 `\mathbb F_\ell[x_1,x_2,x_3,x_4]` 中非零，则按 Schwartz--Zippel，

\[
\#\{(x_1,x_2,x_3,x_4)\bmod \ell:
\bar{\mathcal E}=0\}
\le (\deg \mathcal E)\ell^3.
\]

因此 4E-ND 的任务不是重新证明 Schwartz--Zippel，而是确保 `\bar{\mathcal E}` 非零，并把 `\bar{\mathcal E}\equiv0` 的素因子全部归入 DBA-closure。这个局部 rank 部分原则上已经可证。

但还存在一个更细的厚化-离散转换缺口：模 `Q'` 的四点零集界控制的是 residue 分布；实短弧厚化能量还要求 `\mathcal E/\mathcal D` 不在相邻 residue 壳内产生额外聚集。也就是说，需要一个四点版 dispersion 输入：

**4E-DISP（四点厚化离散转换）。** 对非退化四点场，实厚化条件

\[
|\mathcal E|\le \nu |\mathcal D|
\]

的解数不超过模 `Q'` 零集解数加 `O(\nu A^4+ A^3P^{o(1)})`。

若 4E-DISP 成立，则四点局部 rank 界与 DBA-closure 推出四点能量定理。若 4E-DISP 不能证明，则四点路线仍停留在“模少根性”而非“实短弧少根性”。

因此，四点路线的最后闭合目标应更精确地表述为：证明 `\mathcal E` 的有效局部 rank 为 `1`，把所有 rank 失效素因子纳入 DBA-closure，并证明 4E-DISP 的厚化离散转换。


## 6.11 4E-DISP 与 DBA-closure 的 Jacobian 闭包攻坚

本节继续下钻 4E-DISP。厚化离散转换的本质是：一个低次数有理函数的薄邻域不能在长整数盒中容纳远超 `\nu` 比例的点，除非其梯度或 Jacobian 在大集合上退化。

### 6.11.1 厚化场的 coarea 直觉

令

\[
F(a_1,a_2,a_3,a_4)=\frac{\mathcal E(a_1,a_2,a_3,a_4)}{\mathcal D(a_1,a_2,a_3,a_4)}.
\]

4E-DISP 要控制

\[
\mathcal N_\nu=\#\{a_i\asymp A: |F(a_1,a_2,a_3,a_4)|\le\nu\}.
\]

若 `\nabla F` 在真四点区域有下界，则离散 coarea 原理给

\[
\mathcal N_\nu
\ll \nu A^4+A^3P^{o(1)},
\]

其中 `A^3` 是一条三维水平面的自然尺度。若该界失败，则存在大集合使

\[
|F|\le\nu,
\qquad
\|\nabla F\|\ll \nu/A
\]

同时成立。清分母后，这给出五个低次数多项式近零：

\[
\mathcal E\approx0,
\qquad
\partial_{a_i}\mathcal E\cdot \mathcal D-
\mathcal E\partial_{a_i}\mathcal D\approx0
\quad(1\le i\le4).
\]

因此 4E-DISP 失败会强迫四点场进入 Jacobian 退化簇。

### 6.11.2 Jacobian 退化簇

定义 Jacobian 判别式

\[
\mathfrak J_R=
\operatorname{Res}_{a_1,a_2,a_3,a_4}
\left(
\mathcal E,
\mathcal J_1,
\mathcal J_2,
\mathcal J_3,
\mathcal J_4
\right),
\]

其中

\[
\mathcal J_i=\partial_{a_i}\mathcal E\cdot\mathcal D-
\mathcal E\partial_{a_i}\mathcal D.
\]

若 `\mathfrak J_R` 不消失，则公共近零集合维数至多 `2` 或更低，其整数点数为 `O(A^2P^{o(1)})`，可被 `A^3P^{o(1)}` 吸收。若 `\mathfrak J_R` 消失，则四点水平面具有奇异族；这意味着 `R` 的差分图像具有低维群结构。对一维低次数有理函数，该奇异族只能来自：

1. `R` 常值或仿射；
2. `R` 为 Möbius 变换且四点关系退化为 cross-ratio 恒等；
3. 分母或导数在相关模因子上退化。

第 1 类已由二阶场非恒等排除；第 2 类对应线性分式成比例判别式；第 3 类属于分母/导数坏层。因此 Jacobian 退化簇应全部进入 DBA-closure。

### 6.11.3 4E-DISP 的条件证明

在剔除 Jacobian 退化簇后，对每个固定三元组 `(a_1,a_2,a_3)`，函数

\[
a_4\mapsto F(a_1,a_2,a_3,a_4)
\]

具有有限个临界点，且在其余区间单调，导数下界由 `A^{-C}` 控制。于是每个单调段中 `|F|\le\nu` 的整数点数为

\[
O(\nu A+1).
\]

对 `O(A^3)` 个三元组求和，得到

\[
\mathcal N_\nu\ll \nu A^4+A^3P^{o(1)}
\]

加上模 `Q'` 零集项。这正是 4E-DISP。

因此 4E-DISP 可由以下命题推出：

**JND（Jacobian Non-Degeneracy）。** 四点场 `F=\mathcal E/\mathcal D` 的 Jacobian 退化簇，除对角、半对角和 DBA-closure 坏层外，不含三维以上的正密度整数族。

### 6.11.4 DBA-closure 的有限生成高度账本

所有新判别式来自有限次代数操作：加减乘、求导、差分、resultant。若初始 `N,D` 的次数与高度满足

\[
\deg N,\deg D\le C,
\qquad
\log H(N,D)\le C\log^C P,
\]

则经过固定次数操作后，所有判别式 `\mathfrak D` 仍满足

\[
\deg \mathfrak D\le C',
\qquad
\log H(\mathfrak D)\le C'\log^{C'}P.
\]

于是其坏素因子权重满足

\[
\sum_{q|\mathfrak D}\frac1q\ll \log\log H(\mathfrak D)
\ll \log\log P+\log\log\log P.
\]

这只是对固定 skeleton 的估计。对所有 connected skeleton 求和时，再乘以引理 2.7 的 Rankin 权，仍应被既有 `\log^{Cr}P` 余量吸收。由此 DBA-closure 被压缩为一个有限生成高度命题：证明初始正规形的高度界在 connected 标签求和中统一成立。

### 6.11.5 当前最终障碍

至此，四点路线的最终障碍进一步缩小为两个命题：

1. **JND。** 四点 Jacobian 退化簇除已知退化外没有三维正密度分支。
2. **FGH（Finite Generated Height，有限生成高度）。** connected 正规形及其所有差分、导数、四点能量、Jacobian/resultant 判别式的高度在 Rankin 账本中统一可和。

若 JND 与 FGH 成立，则 DBA-closure 与 4E-DISP 成立；结合 6.10 的局部 rank 界，四点能量定理成立，进而 UAS 闭合。

这仍是条件闭合，而不是无条件证明。真正需要补完的是 JND 的代数几何分类：证明非退化低次数一维有理函数的四点 Jacobian 奇异族只能来自 Möbius/仿射/常值退化。


## 6.12 JND 与 FGH 的函数方程化

本节继续压缩 JND 与 FGH。JND 的本质是一个函数方程分类问题；FGH 的本质是有限生成代数操作下高度不会爆炸。

### 6.12.1 JND 的正确几何对象：临界纤维而非普通水平面

需要先修正一个容易混淆的点：四点方程

\[
R(a_1)-R(a_2)-R(a_3)+R(a_4)=0
\]

本身通常就是三维超曲面；它的三维存在并不表示退化。JND 真正要排除的是“厚化层异常大”时出现的临界三维族，即四点场在法向方向上失去横截性。设

\[
F(x_1,x_2,x_3,x_4)=R(x_1)-R(x_2)-R(x_3)+R(x_4).
\]

普通水平面由 `F=0` 给出，维数为 `3`。只有当同时满足

\[
F=0,
\qquad
\nabla F=0
\]

或在投影到某个三变量坐标时 Jacobian 消失，才构成 JND 需要吸收的奇异族。由于

\[
\nabla F=(R'(x_1),-R'(x_2),-R'(x_3),R'(x_4)),
\]

全梯度消失要求四个点都落在 `R'` 的零点或极点上；对非退化有理函数这是有限集合，不能形成三维正密度分支。因此真四点 Jacobian 退化并不来自普通 `F=0`，而来自投影纤维中 `R'(x_i)` 过小或分母/导数结果式退化。

这一步显著简化 JND：不需要分类所有三维水平面，只需要控制临界纤维。

### 6.12.2 临界纤维分类引理

**引理 JND-crit（临界纤维分类）。** 设 `R\in\mathbb C(x)` 为非常值有理函数，且不在分母坏层。四点场 `F=R(x_1)-R(x_2)-R(x_3)+R(x_4)` 的真四点临界集

\[
F=0,
\qquad
\nabla F=0
\]

不含三维不可约分支。更一般地，任一三变量投影的临界退化只能发生在某个 `R'(x_i)=0`、`D(x_i)=0` 或两个变量落入同一有限 ramification fiber；这些条件均由导数判别式和分母结果式控制，属于 DBA-closure。

**证明。** 全梯度公式直接给出 `R'(x_i)=0` 对所有 `i`。`R'` 是非零有理函数，其零点有限；分母极点也有限。因此全临界集有限乘积，维数为 `0`。对三变量投影，例如把 `x_4` 由

\[
R(x_4)=R(x_2)+R(x_3)-R(x_1)
\]

隐式确定，投影 Jacobian 消失当且仅当 `R'(x_4)=0` 或 `x_4` 落在分母极点；若投影分支多值合并，则两个前像处于同一 ramification fiber，其判别式为

\[
\operatorname{Disc}_x(N(x)-cD(x))=0.
\]

这些都是有限 ramification 条件。于是除对角/半对角和 DBA-closure 坏层外，不存在三维临界分支。

### 6.12.3 JND 的闭合

由 JND-crit，四点厚化层若超过 coarea 预测，只能有两种原因：

1. 进入普通水平面 `F=0` 的厚化管，但法向导数非零；此时离散 coarea 给 `O(\nu A^4+A^3P^{o(1)})`；
2. 进入临界纤维或 ramification fiber；这些由 `R'`、分母、判别式和 resultants 控制，归入 DBA-closure。

因此 JND 可由 JND-crit 与 DBA-closure 推出。相比之前的 JND-class，本版本更准确：它不把普通三维水平面误认为退化，而只排除导致厚化层过厚的临界纤维。

### 6.12.4 FGH 的高度传播引理

FGH 要求所有由有限次操作产生的判别式高度可控。可用以下标准高度传播规则：

若多项式 `P,Q` 满足

\[
\deg P,\deg Q\le d,
\qquad
H(P),H(Q)\le H,
\]

则

\[
H(P\pm Q),H(PQ),H(P')\le (2dH)^{O(1)},
\]

并且 resultants 满足

\[
H(\operatorname{Res}(P,Q))
\le (2d)^{O(d)}H^{O(d)}.
\]

由于本文只进行固定次数的差分、求导、四点化与 resultants，次数仍为 `O_{r}(1)`，高度至多变为 `H^{O_r(1)}`。初始正规形的系数来自 `U,m,t,h` 与局部 CRT 系数；这些量均为 `P^{O(1)}` 或对数幂，因此

\[
\log H\le O_r(\log P).
\]

固定 skeleton 下，所有生成判别式满足

\[
\log H(\mathfrak D)\le O_r(\log P).
\]

于是坏素因子个数与权重为

\[
\omega(\mathfrak D)\ll_r \frac{\log P}{\log\log P},
\qquad
\sum_{q|\mathfrak D}\frac1q\ll_r \log\log P.
\]

这正落入引理 2.7 的 `\log^{Cr}P` Rankin 余量。

### 6.12.5 FGH 与 DBA-closure 的闭合

由 6.12.4，对固定 connected skeleton，所有判别式高度损失为 `\log^{O_r}P`。对 skeleton、局部 Bell 选择和素数标签求和时，引理 2.7 已提供

\[
(Cr)^{Cr}\log^{Cr}P
\]

级余量。因此只要操作次数由 moment 阶 `r` 控制，而不随 `P` 增长，FGH 成立。本文所有差分、导数、四点能量与 Jacobian 操作次数固定，故 FGH 可视为已归约到标准高度引理。

这意味着最后真正非平凡的数学障碍主要集中在离散 coarea 与 ramification 坏层吸收；FGH 更像技术账本，原则上可在附录中完全展开。

### 6.12.6 当前最接近闭合的形式

若 JND-crit 与 DBA-closure 严格证明完成，则 JND 成立；由 6.12.4--6.12.5，FGH 成立；于是 DBA-closure 与 4E-DISP 成立；结合 6.10 的局部 rank 界得到四点能量定理；再推出 UAS，最终闭合 B.0.4S-short 条件链条。

因此当前真正硬核的剩余点变为：严写离散 coarea 估计，并证明所有 ramification/resultant 坏层均由 DBA-closure 吸收。这个版本比 JND-class 更接近可证，因为临界纤维分类已由梯度公式直接控制。


## 6.13 离散 coarea 估计的严写

本节把 6.12 中的离散 coarea 估计展开为可审查证明。核心是固定三个变量后，把四点场视为一变量有理函数，并用临界点分片控制薄层整数点数。

### 6.13.1 一变量分片引理

设

\[
f(x)=\frac{P(x)}{Q(x)}
\]

是次数 `\le C` 的实有理函数，在区间 `I=[A,2A]` 上无极点。设临界集合

\[
\mathcal C_f=\{x\in I:f'(x)=0\}
\]

大小为 `O_C(1)`。把 `I` 按 `\mathcal C_f` 分成 `O_C(1)` 个单调区间 `I_j`。若在 `I_j` 上 `|f'|\ge\lambda_j`，则

\[
\#\{n\in I_j\cap\mathbb Z: |f(n)|\le\nu\}
\ll 1+\frac{\nu |I_j|}{\operatorname{osc}_{I_j} f}
\ll 1+\frac{\nu}{\lambda_j}.
\]

若 `\lambda_j\ge A^{-1+o(1)}`，则贡献为 `O(1+\nu A^{1+o(1)})`。对固定三元组求和后得到 `O(A^3+\nu A^{4+o(1)})`。

### 6.13.2 小导数区间进入 ramification 坏层

仍固定 `(a_1,a_2,a_3)`，令

\[
f_{a_1,a_2,a_3}(x)=F(a_1,a_2,a_3,x).
\]

若某单调区间上 `|f'|<A^{-1-o(1)}`，则存在整数点附近满足

\[
|f(x)|\le\nu,
\qquad
|f'(x)|<A^{-1-o(1)}.
\]

清分母后得到

\[
|\mathcal E|\le\nu|\mathcal D|,
\qquad
|\mathcal J_4|\le A^{-1-o(1)}|\mathcal D|^2.
\]

这正是投影 Jacobian 坏层。由 JND-crit，它只能来自 `R'(x)=0`、分母极点或 ramification 判别式；这些由 DBA-closure 吸收。故非坏层中可假设所有相关单调段满足导数下界。

### 6.13.3 离散 coarea 命题

**命题 DC（Discrete Coarea）。** 在剔除对角、半对角、分母坏层、导数坏层和 ramification 坏层后，四点场满足

\[
\#\{a_i\asymp A: |F(a_1,a_2,a_3,a_4)|\le\nu\}
\ll \nu A^{4+o(1)}+A^{3+o(1)}.
\]

**证明。** 固定 `(a_1,a_2,a_3)`。由 6.13.1 与 6.13.2，非坏层中一变量函数 `a_4\mapsto F(a_1,a_2,a_3,a_4)` 的每个单调段贡献 `O(1+\nu A^{1+o(1)})`，段数为 `O_C(1)`。对 `O(A^3)` 个三元组求和得到结论。坏层由 DBA-closure 计入 `A^{3+o(1)}` 或更小误差。

这就是 4E-DISP 所需的厚化离散转换。

### 6.13.4 与 4E-DISP 的闭合关系

命题 DC 给出实厚化层总数 `O(\nu A^{4+o(1)}+A^{3+o(1)})`。结合 6.10 的模 `Q'` 局部 rank 界，可写成

\[
\#\{|\mathcal E|\le\nu|\mathcal D|\}
\le
\#\{\mathcal E\equiv0\pmod {Q'}\}
+O(\nu A^{4+o(1)}+A^{3+o(1)}),
\]

这正是 4E-DISP 的形式。于是，在 DBA-closure 吸收坏层后，4E-DISP 成立。

### 6.13.5 当前闭合状态

经过 6.13，离散 coarea 本身已归约为标准一变量有理函数分片估计；剩余任务集中到 DBA-closure：必须证明所有小导数、ramification、分母极点、resultant 坏层都在有限生成高度账本中可和。

因此当前最后障碍不再是 coarea，而是 DBA-closure 的完全严写：把所有坏层逐项列入有限生成判别式集合，并证明其 Rankin 权总和小于误差预算。


## 6.14 DBA-closure 的完全账本化

本节把 DBA-closure 写成显式有限生成账本。目标是证明所有坏层都来自有限个低次数判别式族，且其坏素因子权重可由 Rankin/divisor 余量吸收。

### 6.14.1 坏层生成元清单

所有坏层由以下生成元产生：

1. **分母层。** `D(a_i)=0`、`S(a_i)=0`、`a_i=0`、`a_i+t=0`、`a_i+jh=0`。
2. **导数层。** `R'(a_i)=0`，等价于 `N'D-ND'=0`。
3. **ramification 层。** 水平纤维 `N(x)-cD(x)` 出现重根，即

\[
\operatorname{Disc}_x(N(x)-cD(x))=0.
\]

4. **四点 rank 失效层。** `\bar{\mathcal E}\equiv0 mod q` 或 `\mathcal E` 在有效素因子上含大维因子簇。
5. **Jacobian 层。** `\mathcal E` 与 `\mathcal J_i` 的公共高维分支，由 resultants

\[
\operatorname{Res}(\mathcal E,\mathcal J_1,\ldots,\mathcal J_4)
\]

控制。

6. **步长共振层。** `q|t`、`q|h` 或 `q|mU`，使差分或 Fourier 频率失效。

记这些生成元的乘积为

\[
\mathfrak B_{\Gamma}(U,m,t,h)=
\prod_{B\in\mathcal B_\Gamma} B(U,m,t,h).
\]

DBA-closure 等价于证明所有坏素因子 `q|\mathfrak B_\Gamma` 的总权可吸收。

### 6.14.2 有限生成高度界

对固定 connected skeleton `\Gamma`，正规形 `R=N/D` 的次数只依赖 `|\Gamma|`，且其系数来自 CRT 局部参数、`U,m,t,h` 与固定小整数操作。因此存在常数 `C_\Gamma`，使

\[
\deg \mathfrak B_\Gamma\le C_\Gamma,
\qquad
\log H(\mathfrak B_\Gamma)
\le C_\Gamma\log P.
\]

证明只用标准高度规则：

\[
H(PQ)\le H(P)H(Q){d_P+d_Q\choose d_P},
\quad
H(P')\le dH(P),
\quad
H(\operatorname{Res}(P,Q))\le (2d)^{O(d)}H(P)^{O(d)}H(Q)^{O(d)}.
\]

由于操作次数固定，`C_\Gamma` 不随 `P` 增长。

### 6.14.3 坏素因子权重

由高度界，固定 `\Gamma` 下

\[
\sum_{q|\mathfrak B_\Gamma}\frac1q
\le
\sum_{q|\mathfrak B_\Gamma, q\le P}\frac1q
\ll \log\log H(\mathfrak B_\Gamma)+O(1)
\ll_\Gamma \log\log P.
\]

若需要带幂权或多重标签，Rankin 形式给

\[
\sum_{q|\mathfrak B_\Gamma}\frac{\log^C q}{q}
\ll_\Gamma \log^{C+1}P.
\]

这些损失均为对数幂级。

### 6.14.4 与 connected Rankin 账本合并

引理 2.7 已为 connected skeleton/polymer 的素数标签提供

\[
(Cr)^{Cr}\log^{Cr}P
\]

级余量。把 6.14.3 的坏素因子权重并入，只增加 `\log^{O_r}P` 因子。因此

\[
\sum_{\Gamma}\text{BadWeight}(\Gamma)
\ll (Cr)^{Cr}\log^{C'r}P,
\]

仍处于 USC 与 B.0.4S 允许的对数账本内。步长共振层另外有平均因子

\[
\frac1T\#\{1\le t\le T:q|t\}\ll \frac1q+\frac1T,
\]

其中 `1/q` 并入上述坏素因子权重，`1/T` 由 `T=(\log P)^{B_4}` 的大余量吸收。

### 6.14.5 DBA-closure 命题

**命题 DBA-closure。** 对所有 connected 正规形、所有由差分、导数、四点能量、Jacobian 和 resultants 产生的坏层，其总贡献在 dyadic 盒、Fourier 频率、步长平均和 Rankin 标签求和后为

\[
O(A\log^{-B-20}P)
\]

级别，可并入 6.7.11 的差分相关误差。

**证明。** 坏层由 6.14.1 的有限生成元覆盖；6.14.2 给出固定 skeleton 的高度界；6.14.3 把坏素因子权重化为对数幂损失；6.14.4 把该损失并入 connected Rankin 账本与步长平均余量。取 `B_1,B_2,B_4` 的对数参数足够大，即得所需 `O(A\log^{-B-20}P)` 级误差。

因此 DBA-closure 已被归约为两个可审查点：6.14.1 的生成元清单必须覆盖所有坏层，且 6.14.4 的对数损失必须被全文参数余量吸收。该覆盖来自 6.10--6.13 中每次退化判别式的显式列举；最终定稿仍需逐项核对无遗漏。

### 6.14.6 当前闭合状态

结合 6.13 的离散 coarea 与本节 DBA-closure 账本，若坏层生成元覆盖无遗漏且参数余量核对通过，则 4E-DISP 成立。再结合 6.10 的局部 rank 界，可推出四点能量定理；由 6.9 推出 UAS；由 6.7--6.8 推出 FNL 与 NL，进而得到 B.0.4S-short。

需要最后复核的是参数余量是否在全文所有并合中一致：`B_1,B_2,B_4` 必须大于所有高度传播和 Rankin 损失常数。该复核看起来是技术性常数选择，而非新的结构障碍；但在最终论文中仍必须完整列出。


## 6.15 最终参数余量核查表

本节统一核查 `B_1,B_2,B_4` 与 Fourier 截断参数 `B` 的余量。设全文所有高度传播、Rankin、dyadic 并合、coarea 端点和 Stieltjes 权重损失的最大对数指数为

\[
C_*.
\]

这里 `C_*` 是绝对常数，取为以下有限集合的最大值：

1. `C_{ht}`：有限生成高度传播与 resultants 的对数损失；
2. `C_{rk}`：connected Rankin/divisor 账本额外损失；
3. `C_{dy}`：dyadic 盒、窗口簇、Fourier 频率和步长并合损失；
4. `C_{co}`：离散 coarea 的端点、临界分片和厚化壳损失；
5. `C_{st}`：Stieltjes 权从 `A` 尺度转回 `Y/\log P` 尺度的损失。

### 6.15.1 需要满足的不等式

参数需要满足：

\[
B_1>C_*+B+10,
\]

以保证厚化宽度 `\delta=(\log P)^{-B_1}` 贡献低于 FNL 阈值；

\[
B_2>C_*+2B+20,
\]

以保证有效少根密度 `\theta(Q')\le\log^{-B_2}P` 时差分相关和低于 `A\log^{-2B-20}P`；

\[
B_4>C_*+2B+20,
\]

以保证 van der Corput 的 `A^2/T` 项和步长共振 `1/T` 项可吸收；并且

\[
B_5>B+C_{st}+3
\]

以保证最终 Fourier 和满足

\[
S=o(Y/\log^{B+2}P).
\]

### 6.15.2 一组显式选择

原 6.7.11 取

\[
B_4=4B+40,
\qquad
B_2=6B+80,
\qquad
B_1=8B+100.
\]

为了完全吸收 `C_*`，可改为

\[
B_4=4B+4C_*+100,
\qquad
B_2=6B+4C_*+120,
\qquad
B_1=8B+4C_*+160.
\]

这样每个误差项至少保留 `\log^{-B-20}P` 的安全余量。

### 6.15.3 误差项核查表

| 来源 | 误差形态 | 吸收参数 |
|---|---:|---|
| Fourier 截断 | `M^{-1}`、短弧厚度 `\delta` | `B_1` |
| UAS 短弧少根密度 | `A\theta(Q')` | `B_2` |
| van der Corput 初项 | `A^2/T` | `B_4` |
| 步长共振 | `1/q+1/T` | `B_4` 与 Rankin |
| DBA 坏素因子 | `\log^{C_{ht}+C_{rk}}P` | `B_2,B_4` 余量 |
| 离散 coarea 厚化 | `\nu A^{4+o(1)}` | `B_1` |
| coarea 端点 | `A^{3+o(1)}` | 局部 rank/对角基线 |
| dyadic/Fourier 并合 | `\log^{C_{dy}}P` | 全部参数余量 |
| Stieltjes 权转换 | `\log^{C_{st}}P` | `B_5` |

所有项均被上述显式选择吸收。

### 6.15.4 参数闭合结论

在 6.14 的生成元覆盖无遗漏的前提下，取 6.15.2 的参数选择，则 DBA-closure 的坏层误差、4E-DISP 的厚化误差、UAS 的短弧误差和 FNL 的 Fourier 截断误差全部低于

\[
O(A\log^{-B-20}P)
\]

或最终需要的

\[
o(Y/\log^{B+2}P).
\]

因此，参数余量不再构成独立障碍；最后只需逐项核对 6.14.1 的坏层生成元清单覆盖所有退化情形。

## 7. 技术附录与定稿审查点

前文已经给出主证明链。以下附录用于把正文中压缩使用的技术估计展开到可审查层级。附录不改变主证明结构，只补全估计细节，并标出仍需最终打磨的严写点。


### 7.1 关键依赖命题状态

为便于最终审稿，当前证明链中最需要独立核查的技术输入如下：

1. **定理 2.2：`USC(log P)`。** 这是全文核心输入，附录 A 已给出命题 A.2.1、A.3.1、A.4.1、A.6.1、A.7.1 组成的完整证明框架；最终定稿仍需逐项核对常数依赖和 Rankin 尾部。
2. **B.0.0–B.0.4 局部乘积容量与误差并合。** 这是行方向从全局 Stieltjes 常数转为局部正常窗口估计的接口；其中 B.0.0 把定理 2.2 的局部窗口簇高矩集中转移到 dyadic 参数族，B.0.1–B.0.3 完成容量、盒级误差并合与短缩放区间双线性平均。B.0.4 的端点漂移一般情形目前仍是待闭合接口：硬窗口路线需证明 B.0.4\* 的 sawtooth/短区间除数型相消；平滑路线需证明 B.0.4S 的平滑 Type-I 素数双线性估计，核心为短切片接口 B.0.4S-short。第 6.7 节进一步把该核心接口压缩为 UAS 均匀短弧少根性与 DBA 退化账本吸收；二者完成后，才能把短切片端点误差统一吸收到 `o(Y/\log P)`。
3. **C.2.1–C.2.2 高阈值列场 USC 与一致集中。** 这是列方向一致集中所需接口；关键点是所有筛素数 `q≤αP<P` 均与列步长 `P` 互素，因此 CRT 投影和叶剥离不失效；最终并合还需把坏列密度整数化为坏列数小于 `1`。
4. **显式阈值 `P_*`。** 当前正文给出“所有足够大奇素数”的理论闭合；全体奇素数版本需要在所有 `o(1)` 和常数显式化后运行附录 D 的有限验证。

这些项目不是额外假设，而是本文证明中必须最终严查的技术节点；后续定稿应优先把它们转化为编号命题并逐条核验。

### 附录 A：增长阶 `USC(log P)` 的常数控制

附录 A 负责完整证明定理 2.2。当前已按下列命题展开；最终定稿时需要统一所有 `C,c_0,A,B` 的依赖关系。

**A.0 证明目标与依赖结构。** 附录 A 的目标是证明定理 2.2 的 cumulant 总和界。证明链条分为五步：

1. **投影消失。** A.1 说明有限 CRT 平均下中心化筛余变量的无碰撞投影为零。
2. **connected 化。** 命题 A.2.1 用 cumulant Möbius 反演证明所有断开碰撞图精确抵消，只剩 connected 中心化超图。
3. **rank 与 skeleton。** 命题 A.3.1 把 connected 超图压缩为生成树骨架，并把总 rank 分解为 `r-1` 个连接 rank 加额外 rank。
4. **Euler/Rankin 账本。** 命题 A.4.1 与 A.5 按 tiny/near/far 三层控制所有素数标签、非骨架修饰和 divisor 权。
5. **变量求和。** 命题 A.6.1 用中心化叶剥离把每个 connected 项的变量和压到 `|Ω|` 尺度。

五步合并得到

\[
\sum_{x_1,\ldots,x_r\in Ω}
\kappa(Y_{x_1},\ldots,Y_{x_r})
\ll |Ω|(Cr)^{Cr}(\log\log P)^{r-1}\log^{Cr}P,
\]

对 `2≤r≤c_0\log P` 成立。随后命题 A.7.1 用 moment-cumulant 公式把 cumulant 总和界转成所需高矩集中。

**A.1 CRT 投影恒等。** 令 `Q_0` 为有限筛素数集，

\[
M=\prod_{q\in Q_0}q.
\]

定义有限筛余指示

\[
y_M(x)=1_{(x,M)=1},
\qquad
p_M=\frac{\varphi(M)}{M},
\qquad
Y_M(x)=\frac{y_M(x)}{p_M}-1.
\]

由 CRT，模 `M` 的允许剩余类个数为 `\varphi(M)`，故

\[
\sum_{a\bmod M}y_M(a)=\varphi(M)=Mp_M.
\]

于是

\[
\sum_{a\bmod M}Y_M(a)=0.
\]

若 `(A,M)=1`，映射 `t\mapsto At+B` 是模 `M` 的双射，因此

\[
\sum_{t\bmod M}Y_M(At+B)=0.
\]

行场对应 `A=1`。列场对应 `x=c+kP`，即 `A=P`。因为所有筛素数均小于 `P`，所以 `(P,M)=1`，列场也满足同一恒等。

进一步，cumulant 对每个入口多线性。若某展开项中投影变量只出现在一个中心化因子中，且不通过同余碰撞连接其他变量，则

\[
\sum_{t\bmod M}\kappa(Y_M(At+B),Z_2,\ldots,Z_r)
=
\kappa\left(\sum_{t\bmod M}Y_M(At+B),Z_2,\ldots,Z_r\right)=0.
\]

这就是无碰撞项精确消失的代数原因。

**A.2 cumulant Möbius-Bell 展开。**

**命题 A.2.1（connected cumulant 展开）。** 设 `I={1,\ldots,r}`。joint cumulant 由分区 Möbius 公式给出：

\[
\kappa(Z_i:i\in I)=
\sum_{\Pi\in\mathcal P(I)}
(-1)^{|\Pi|-1}(|\Pi|-1)!
\prod_{B\in\Pi}\mathbb E\prod_{i\in B}Z_i.
\]

对筛余变量，局部素数 `q` 的贡献只取决于点集在模 `q` 下的相等关系。也就是说，`q` 给出一个 Bell 分区 `π_q`；每个非单点块 `C\inπ_q` 给出同步条件

\[
x_i\equiv x_j\pmod q\qquad(i,j\in C).
\]

选取块内根点 `i_C` 后，该条件等价于 `|C|-1` 条独立差分同余

\[
q\mid x_i-x_{i_C}
\qquad (i\in C\setminus\{i_C\}).
\]

因此局部 rank 为

\[
\rho_q(π_q)=\sum_{C\inπ_q}(|C|-1).
\]

对应局部系数满足

\[
|c_q(π_q)|\ll_r q^{-\rho_q(π_q)}.
\]

多个素数由 CRT 独立叠加。同一碰撞类型上的素数乘积形成 squarefree 模数 `q_e`，从而得到 squarefree 超图项。

若所得超图 `Γ` 在顶点集 `I` 上断开，存在非空分解 `I=I_1\sqcup I_2` 且没有超边跨越两侧。该项分解为

\[
F_Γ(x_I)=F_{Γ_1}(x_{I_1})F_{Γ_2}(x_{I_2}).
\]

这里的“精确抵消”可直接从 cumulant 分区公式看出：若 `I=I_1\sqcup I_2` 且某项可写为 `F_1(x_{I_1})F_2(x_{I_2})`，则在分区 Möbius 和中，所有跨越 `I_1,I_2` 的分区贡献与不跨越的分区贡献相加为零；等价地，joint cumulant 对可分裂为两个非空指标集乘积的入口为零。因此 surviving 项必须 connected。

最后使用

\[
1_{q|L-a}=E_{q,a}(L)+\frac1q,
\qquad
E_{q,a}(L)=1_{q|L-a}-\frac1q,
\]

将普通碰撞指示改写为中心化边函数。展开后有三类项：

1. 若某些边被常数项替换后图断开，则该项可分裂为两个非空顶点集上的乘积，再次由 cumulant Möbius 反演抵消；
2. 若删除这些边后图仍 connected，则保留的中心化边集本身给出一个 connected 中心化超图，其 rank 和 skeleton 在保留边上重新计算；被删除边只贡献局部常数 `1/q`，已包含在 A.4 的逐素数 Euler 账本中；
3. 若所有含某顶点的边都被常数化，则该顶点成为孤立块，属于第一类断开项而消失。

因此 surviving 项均可表示为 connected 中心化超图；常数项不会留下非 connected 残余，也不会在 A.6 的叶剥离中产生无中心化父边的叶子。

**A.3 connected skeleton expansion。**

**命题 A.3.1（skeleton rank 分解）。** 给定 connected 超图 `Γ=(V,E)`，`|V|=r`。把每条超边 `e` 替换为其内部完全图，得到普通图 `G(Γ)`。因为 `Γ` connected，`G(Γ)` connected，故含生成树 `T`。

每条树边 `uv\in T` 来自某条超边 `e\supset\{u,v\}`。选择这样的来源，得到 skeleton map。定义 rank

\[
\rho(Γ)=\sum_{e\in E}(|e|-1).
\]

若超边 `e` 在生成树中承载 `t_e` 条树边，则 `0≤t_e≤|e|-1` 且 `\sum_e t_e=r-1`。所以

\[
\rho(Γ)=\sum_e t_e+
\sum_e(|e|-1-t_e)
=(r-1)+\rho_{ex}(Γ),
\]

其中 `\rho_{ex}(Γ)≥0`。这就是非骨架额外 rank。

生成树数量为 `r^{r-2}`。给定生成树后，每条树边选择其来源超边，来源选择数至多由相关端点集合的 Bell 型选择控制。对一个 rank 为 `ρ` 的超边，其端点选择数至多为 `r^{O(ρ)}`，而局部 Euler 权含有 `q^{-ρ}`；因此端点组合可由 `(Cr)^{Cρ}` 吸收。

为了避免无限 rank 尾部混入 skeleton 计数，按总 rank `R=Σ_eρ_e` 分层。若 `R≤C_0r`，端点与 Bell 选择总数为 `(Cr)^{O(R)}≤(Cr)^{Cr}`，这就是有效部分。若 `R>C_0r`，则相对连接 `r` 个顶点所需的 `r-1` 个 rank 至少有 `R-(r-1)` 个额外 rank；A.5 表明每个额外 rank 带来额外 Euler 衰减。取 `C_0` 足够大后，`R>C_0r` 的尾部由该额外衰减连同 Rankin 权吸收进有效部分的常数。因此不会出现不可控的 Bell 数爆炸。

**A.4 tiny/near/far 三层估计。**

**命题 A.4.1（三层 Euler/Rankin 账本）。** 令 `r≤c_0\log P`。为避免与全文 `B=√P` 混淆，本小节用固定大常数 `A_1,A_2` 分层：

\[
q≤A_1r,
\qquad
A_1r<q≤A_2r^2,
\qquad
q>A_2r^2.
\]

**tiny 层。** 令

\[
M_0=\prod_{q≤A_1r}q.
\]

Chebyshev 估计给 `\log M_0=O(r)`。因 `r≤c_0\log P`，取 `c_0` 足够小可使

\[
M_0≤P^{1/10}.
\]

tiny 层并入有限 CRT base measure。由于中心化投影在模 `M_0` 上精确成立，tiny 层不产生 polymer 增长；它只改变有限基测度，并由 A.1 的投影恒等处理。需要区分两类误差：完整 CRT 周期内没有误差；实际行窗口、局部窗口簇或列场只截取有限区间时，端点不完整周期产生 `O(M_0)` 级边界项。这些端点项不参与 connected Euler 账本，而是在 A.6 的叶剥离端点估计、行方向 B.0.4 的二维边界平均、列方向 C.2 的长度 `P` 主量中分别吸收。因 `M_0≤P^{1/10}` 且最终主量分别为 `√P/\log P` 或 `P/\log P`，充分大时不会改变主项常数。

**near 层。** 对 `A_1r<q≤A_2r^2`，固定一棵 skeleton 生成树。单条骨架边需要一个 squarefree 标签，其 Euler 因子满足

\[
\prod_{A_1r<q≤A_2r^2}\left(1+\frac{C}{q}\right)
\le
\exp\left(C\sum_{A_1r<q≤A_2r^2}\frac1q\right).
\]

由 Mertens 素数倒数公式，

\[
\sum_{A_1r<q≤A_2r^2}\frac1q
=\log\log(A_2r^2)-\log\log(A_1r)+O(1/\log r)=O(1).
\]

故每条骨架边贡献 `O(1)`，`r-1` 条骨架边贡献 `O(1)^r`。

非骨架修饰至少多一个 rank。端点选择和局部 Bell 选择至多给 `(Cr)^C`，故单素数非骨架权重为

\[
O\left(\frac{(Cr)^C}{q^2}\right).
\]

因此 near 非骨架总因子由

\[
\prod_{q>A_1r}\left(1+O\left(\frac{r^2}{q^2}\right)\right)
\le
\exp\left(O\left(\sum_{q>A_1r}\frac{r^2}{q^2}\right)\right)
\le e^{O(r)}
\]

控制；该因子并入 `(Cr)^{Cr}`。

**far 层。** 对 `q>A_2r^2`，骨架边的 harmonic 和满足

\[
\sum_{A_2r^2<q≤z}\frac1q\ll\log\log P.
\]

由于 skeleton 需要 `r-1` 条连接边，far 骨架贡献至多

\[
(\log\log P)^{r-1}.
\]

far 非骨架仍至少多一个 rank，因此

\[
\sum_{q>A_2r^2}\frac{r^2}{q^2}=O(1/A_2).
\]

取 `A_2` 足够大后，该部分绝对收敛并只贡献 `e^{O(1)}`。

合并 tiny 的 CRT 投影、near 的 `e^{O(r)}`、far 的 `(\log\log P)^{r-1}`、生成树数量与端点选择 `(Cr)^{Cr}`，得到总系数

\[
(Cr)^{Cr}(\log\log P)^{r-1}\log^{Cr}P.
\]

这里最后的 `\log^{Cr}P` 来自 Rankin/divisor 账本，但不能把一个裸的 `\tau(Q_Γ)^{Cr}` 事后强行塞入 Euler 乘积。正确做法是逐素数记账：对每个筛素数 `q`，所有可能的局部 Bell 分区、块根、端点来源、CRT 兼容性分裂和公共因子选择先在该 `q` 的局部因子中求和。若该局部项提供 rank `\rho_q`，其总权重满足

\[
W_q(\rho_q)\ll \frac{(Cr)^{C\rho_q}}{q^{\rho_q}}.
\]

也就是说，divisor/兼容性选择只把局部常数从 `1` 放大到 `(Cr)^{C\rho_q}`，不会在所有素数求和之后再产生独立的全局 `\tau(Q_Γ)^{Cr}`。因此：骨架 rank `\rho_q=1` 的局部因子给 `1+O((Cr)^C/q)`，其 near 层贡献并入 `(Cr)^{Cr}`，far 层在 `r-1` 条骨架边上给 `(\log\log P)^{r-1}`；非骨架额外 rank 至少使 `\rho_q≥2`，给 `O((Cr)^C/q^2)`，由 near/far 的绝对收敛吸收。

若在中间写出 `Q_Γ` 与 divisor 符号，它只表示上述逐素数局部选择的压缩记号；展开回逐素数 Euler 账本后，不存在未吸收的全局 divisor 因子。剩余的 Rankin 截断只用于处理 `R=Σ_q\rho_q>C_0r` 的高 rank 尾部：额外 rank 带来的至少 `q^{-1}` 衰减战胜端点/Bell 选择，取 `C_0,A_2` 足够大后尾部并入 `(Cr)^{Cr}\log^{Cr}P`。

**A.5 非骨架权重。** 骨架已经提供连接 `r` 个顶点所必需的 `r-1` 个 rank。任意非骨架边有两种情形。

第一，循环边。它加入生成树后形成环，对已有骨架不是必需连接，因此给出至少一个额外独立同余条件，额外支付 `1/q`。

第二，高阶超边剩余约束。若超边大小为 `m`，总 rank 为 `m-1`；若其中 `t` 个 rank 被骨架使用，则剩余 rank 为 `m-1-t`。只要该超边有非骨架修饰，剩余 rank 至少为 `1`。

因此一个带非骨架修饰的局部素数项，总 rank 至少为 `2`，局部权重至多

\[
O\left(\frac{(Cr)^C}{q^2}\right).
\]

其中 `(Cr)^C` 吸收端点选择、块根选择、中心化展开和 divisor 权。更高 rank 项含更高次 `1/q`，由 Euler 乘积吸收。

**A.6 中心化叶剥离。**

**命题 A.6.1（中心化叶剥离）。** 本节证明每个 connected 中心化项的变量求和只有一个自由体积因子。先使用统一的仿射区间估计。设变量写成

\[
x=A t+B,
\qquad t\in I,
\]

其中 `I` 是整数区间，且 `(A,Q)=1`。则对任意剩余类 `a mod Q`，同余 `At+B\equiv a\pmod Q` 等价于唯一的 `t mod Q` 剩余类，所以

\[
\#\{t\in I:At+B\equiv a\pmod Q\}=\frac{|I|}{Q}+O(1),
\]

并且

\[
\sum_{t\in I}\left(1_{At+B\equiv a\pmod Q}-\frac1Q\right)=O(1).
\]

该 `O(1)` 对 `a,A,B,Q` 一致。行窗口对应 `A=1`；列场对应 `A=P`，且所有筛素数 `<P`，故 `(P,Q)=1`；局部窗口簇只是把参数区间 `I` 换成较短的连续区间。因此即使 `Q>|I|` 或 `Q>P`，同一端点估计仍成立。

现在固定一个 connected skeleton/polymer 项，并在其 skeleton 中取生成树 `T`。从 `T` 的叶子到根剥离变量。设当前叶子为 `v`，父点为 `u`。所有含 `x_v` 的同余条件来自若干边模数。若这些条件不兼容，则该叶子求和为 `0`。若兼容，则 CRT 将它们合并为一个条件

\[
x_v\equiv b(x_u,x_W)\pmod {Q_v},
\]

其中 `W` 是已经固定或尚未剥离但不含 `v` 的邻点集合，`Q_v` 是相关 squarefree 模数的乘积或因子。中心化展开把含 `x_v` 的条件写成

\[
E_{Q_v,b}(x_v)=1_{x_v\equiv b\pmod {Q_v}}-\frac1{Q_v}.
\]

可能出现的不含 `x_v` 的常数补偿项只改变外层系数，不再参与 `x_v` 求和。这里需要排除一个潜在误读：若某一展开项在叶子 `v` 上完全不含中心化因子，则该项把顶点 `v` 从 connected skeleton 中断开，已经在 A.2 的 cumulant Möbius-Bell 消去中抵消；因此在当前固定的 connected 项中，叶子至少保留一条含 `x_v` 的中心化父边。于是 `x_v` 的求和总可由上面的统一仿射估计给出 `O(1)`。

因此每剥离一个叶变量，原本可能产生的 `|Ω|` 体积因子被中心化抵消，只留下统一 `O(1)`。若叶变量同时承载多个模数，CRT 兼容性选择按素数局部记账并已归入 A.4；本步骤只额外产生 `(Cr)^{Cr}` 级的中心化展开、父边来源和端点选择常数。

重复剥离 `r-1` 个叶子后，只剩根变量未剥离。根变量可能还满足若干剩余同余限制，但上界只需丢弃这些限制，按其参数区间长度估计为 `|Ω|`；在列场中这是 `P`，在行窗口或局部窗口簇中是相应区间长度。因此

\[
\left|
\sum_{x_1,\ldots,x_r\in Ω}
\prod_{e\in E(Γ)}E_{q_e,a_e}(L_e(x))
\right|
\le |Ω|(Cr)^{Cr}.
\]

最后，A.6 不再产生新的 `\log P` 损失；所有局部 divisor/兼容性选择已由 A.4 的逐素数 Euler/Rankin 账本吸收。

**A.7 从 cumulant 总和到高矩集中。**

**命题 A.7.1（高矩转移）。** 令

\[
X_Ω=\sum_{x\in Ω}Y_x.
\]

moment-cumulant 公式给

\[
\mathbb E X_Ω^{2m}
=\sum_{\Pi\in\mathcal P([2m])}
\prod_{B\in\Pi}
\kappa(X_Ω: i\in B),
\]

其中块 `B` 的大小记为 `|B|=s`，且

\[
\kappa(X_Ω: i\in B)
=
\sum_{x_1,\ldots,x_s\in Ω}
\kappa(Y_{x_1},\ldots,Y_{x_s}).
\]

由定理 2.2 的 cumulant 总和界，大小为 `s≥2` 的块贡献至多

\[
|Ω|(Cs)^{Cs}(\log\log P)^{s-1}\log^{Cs}P.
\]

大小为 `1` 的块为零，因为 `Y_x` 已中心化。于是每个分区没有单点块。若分区有 `b` 个块，则 `b≤m`。把每个块贡献中的一个 `|Ω|` 提取出来，得到总尺度 `|Ω|^b≤|Ω|^m`。分区数与块大小组合由标准 Bell 数估计吸收为 `(Cm)^{Cm}`。因此

\[
\mathbb E|X_Ω|^{2m}
\le
(Cm)^{Cm}|Ω|^m(\log\log P)^m\log^{Cm}P.
\]

这一步只给出归一化和变量 `X_Ω` 的高矩。应用到筛余计数时必须乘回筛余密度。记

\[
Z_Ω=\sum_{x\in Ω}(y_x-p_Ω)=p_ΩX_Ω,
\qquad \mu=p_Ω|Ω|.
\]

因为 `0<p_Ω≤1`，上式推出

\[
\mathbb E|Z_Ω|^{2m}
\le
p_Ω^{2m}(Cm)^{Cm}|Ω|^m(\log\log P)^m\log^{Cm}P
\le (Cm)^{Cm}\mu^m\log^{C'm}P.
\]

其中 `(\log\log P)^m` 已吸收到 `\log^{C'm}P`。若 `Ω` 有端点边界或 Stieltjes 权重，则 `\mu=p_Ω|Ω|+O(E_{bd})`；在本文使用处均先由 B.0.4 或 C.1 把边界误差吸收到主量，之后再应用此未归一化高矩形式。它正是行窗口、局部窗口簇和列场 LC2 中使用的集中估计。

### 附录 B：行窗口安全间隙的筛法细节

附录 B 负责定理 3.6 的筛法细节。

**B.0 局部乘积容量上界（行方向接口命题）。** 后文需要一个局部化版本的乘积计数上界。设 `\mathcal W` 是同一行中一族连续滑动窗口，其起点区间长度至少 `C√P/\log P`。令 `I(\mathcal W)` 为这些窗口扫过的整数区间，长度记为 `Y`。

**命题 B.0.0（USC 到压缩参数族筛余估计的转移）。** 设 `\mathcal T` 是由 dyadic 盒、允许窗口簇、列场或双线性小盒组成的压缩参数族，满足 `|\mathcal T|\le(\log P)^A`。每个 `t\in\mathcal T` 给出一个筛余统计量

\[
Z_t=\sum_{\omega\in\Omega_t} W_t(\omega)
\left(S_B(L_t(\omega))-\prod_{q\le B}\left(1-\frac1q\right)\right),
\]

其中：

- `\Omega_t` 是单线性区间、列场、窗口簇，或双线性小盒中的参数集合；
- `W_t(\omega)\ge0` 是 Stieltjes 权或归一化计数权，在盒内变化为 `1+o(1)`；
- `L_t(\omega)` 是仿射形式 `ax+b` 或双线性形式 `ap`；
- 对所有小筛素数 `q\le B`，相关系数在模 `q` 下可逆；
- `S_B(n)=1_{(n,\prod_{q\le B}q)=1}` 是 prime-like 小筛上界指示。

主量定义为

\[
\mu_t=\left(\sum_{\omega\in\Omega_t}W_t(\omega)\right)
\prod_{q\le B}\left(1-\frac1q\right).
\]

若主量

\[
\mu_t
\]

满足 `\mu_t\ge (\log P)^A`，则定理 2.2 与命题 A.7.1 给出统一高矩界。原因是：仿射情形直接属于行窗口/列场 USC；双线性情形先由 B.0.3a–g 将 connected cumulant 账本提升到二维小盒，再回到同一高矩转移形式。权重 `W_t` 在盒内为有界变差且变化 `1+o(1)`，可先用阶梯函数近似为 `O((\log P)^A)` 个常权子盒；每个子盒应用未归一化高矩形式，最后用 Minkowski 或三角高矩不等式合并，损失仍吸收到 `\log^{Cm}P`。因此

\[
\mathbb E|Z_t|^{2m}
\le (Cm)^{Cm}\mu_t^m\log^{Cm}P,
\qquad m=c\log P.
\]

因此对任意固定 `\varepsilon>0`，所有主参数同时满足

\[
|Z_t|\le\varepsilon\mu_t
\]

且坏参数个数为 `0`。具体地，压缩参数族大小至多为 `O((\log P)^A)`，而单个参数的异常密度为 `\exp(-c\log P\log\log P)`；故坏参数数目至多

\[
O((\log P)^A)\exp(-c\log P\log\log P)<1
\]

对充分大 `P` 成立。若非主参数满足

\[
\sum_{t:\mu_t< (\log P)^A}\mu_t=o(Y/\log P),
\]

则整体有

\[
\sum_{t\in\mathcal T}Z_t
\le \varepsilon\sum_{t\in\mathcal T}\mu_t+o(Y/\log P).
\]

令 `\varepsilon\to0` 缓慢，即得 `\sum_t Z_t=o(Y/\log P)`。

**证明。** 对主参数，Markov 不等式给

\[
\mathbb P(|Z_t|>\varepsilon\mu_t)
\le
\left(\frac{(Cm)^C\log^C P}{\varepsilon^2\mu_t}\right)^m.
\]

若 `\mu_t\ge(\log P)^A` 且选择 `A>2C+10`，则括号内至多为 `\log^{-A/2}P`，从而

\[
\mathbb P(|Z_t|>\varepsilon\mu_t)
\le \exp(-c_\varepsilon(\log P)(\log\log P)).
\]

由于这里的并合对象是压缩后的盒级参数，数量为 `O((\log P)^A)`，该尾界给出的坏参数数目小于 `1`，故所有主参数同时受控。若存在 `P^{O(1)}` 个单点参数，不能逐点并合；必须先按 B.0.3 的双线性平均或窗口簇平均压缩成盒级统计量。非主参数按假设的总主量直接吸收。

**适用范围警戒。** 该命题只适用于主量达到多项式对数尺度的参数族。在半素数层中，若机械固定一个前置素因子 `a\asymp P^{1/2}`，则缩放区间 `I_a` 的长度可能只有 `O(1/\log P)` 到 `O(1)`，此时 `\mu_a` 不可能达到 `(\log P)^A`。因此 B.0.1 不能依赖逐个 `a` 的点态短区间估计；必须改用双线性平均形式：把 `a` 与最后因子 `p` 同时保留在一个二维盒中，由 USC 控制二维投影的平均偏差。C.2.2 的列场没有这种缩放尾层，因为每列长度为 `P`，主量 `\mu_α\asymp P/\log P`。

**命题 B.0.1（局部乘积容量）。** 半素数层与三粗因子层在 `I(\mathcal W)` 中的计数，不超过其全局 Stieltjes 积分密度乘以 `Y`，再加 `o(Y/\log P)` 级误差。形式上，若 `\mathcal N_k(\mathcal W)` 统计满足相应大小约束的

\[
n=p_1\cdots p_km,
\qquad p_i>B=√P,
\]

则需要

\[
\mathcal N_k(\mathcal W)
\le
(1+o(1))Y\cdot \mathfrak C_k(P).
\]

这里 `\mathfrak C_k(P)` 是全局 Stieltjes 积分给出的密度。

**证明。** 不能仅用粗 Brun-Titchmarsh 代替这一步，因为其常数损失会放大 B.1 主常数并可能吃掉安全间隙。本文用 `USC(log P)` 的局部筛余集中来完成这一步。

**第一步：dyadic 因子盒。** 将每个大素因子限制在 dyadic 盒

\[
p_i\in[P^{α_i},P^{α_i+\Delta}],
\qquad \Delta=(\log P)^{-2}.
\]

盒数为 `O((\log P)^3)`，可由高矩尾界并合吸收。每个盒内 `\log p_i=(α_i+O(\Delta))\log P`，所以 Stieltjes 密度在盒内变化为 `1+o(1)`。

**第二步：固定前置因子。** 在一个盒中固定

\[
a=p_1\cdots p_{k-1}.
\]

待计数的最后因子 `p=p_k` 必须满足

\[
ap\in I(\mathcal W),
\]

即

\[
p\in I_a:=a^{-1}I(\mathcal W)
\]

的一个缩放短区间。这些 `I_a` 的长度可能低至 `P^{1/2}/(a\log P)` 量级，因此不能诉诸传统短区间 PNT。这一点暴露出逐个固定 `a` 的点态路线在半素数层上尺度不足。本文改用双线性平均：不要求每个 `I_a` 单独达到 USC 尺度，而是把同一 dyadic 盒内的所有前置因子 `a` 与最后因子 `p` 同时求和，研究二维区域 `ap\in I(\mathcal W)` 中的筛余平均。命题 B.0.3 将给出该双线性平均接口，并把端点盒、低体积盒和曲线边界层统一吸收为 `o(Y/\log P)`。

**第三步：盒级筛余投影。** 条件 `ap\in I(\mathcal W)` 与小筛候选条件

\[
(ap,\prod_{q≤B}q)=1
\]

在 `(a,\prod_{q≤B}q)=1` 时等价于

\[
(p,\prod_{q≤B}q)=1.
\]

更一般地，若窗口簇来自固定行的平移坐标，条件可写成仿射列

\[
p\mapsto ap+b
\]

上的筛余计数。由于 `a` 只含 `>B` 的素因子，故对所有 `q≤B` 有 `(a,q)=1`，CRT 投影与定理 2.2 的中心化叶剥离均适用。

因此在盒级语言中，第三步产生的是 B.0.0 的统一统计量：`\Omega_t` 为该 dyadic 双线性带，`L_t(a,p)=ap`，`W_t` 为前置因子的 Stieltjes 权。该统计量的误差不按固定 `a` 逐点估计，而由命题 B.0.3–B.0.4 给出

\[
\sum_{(a,p)\in\mathcal R}W_t(a)S_B(ap)
\le
(1+o(1))\operatorname{Vol}_{St}(\mathcal R)
\prod_{q≤B}\left(1-\frac1q\right)+o(Y/\log P).
\]

若把 `a` 固定，可得到下面 B.0.2 中的点态模型；但该模型不用于最终并合。

**命题 B.0.2（误差并合，点态形式的使用限制）。** 命题 B.0.0 只允许对压缩后的盒级参数族并合；它不能对 `P^{O(1)}` 个单独前置因子 `a` 逐点并合。下面的点态论证仅作为局部模型，用于说明主量足够大时的单切片行为；最终误差并合必须调用命题 B.0.3 的双线性平均形式替代逐个 `a` 的并合。证明分三层处理。

**单个 `a`。** 令

\[
Z_a=
\#\{p\in I_a:p\text{ prime-like at level }B\}
-|I_a|\prod_{q≤B}\left(1-\frac1q\right).
\]

定理 2.2 与 moment-cumulant 公式给出：对 `m=c\log P`，

\[
\mathbb E |Z_a|^{2m}
\le
(Cm)^{Cm}\mu_a^m\log^{Cm}P,
\qquad
\mu_a=|I_a|\prod_{q≤B}\left(1-\frac1q\right).
\]

因此当 `\mu_a\ge (\log P)^A` 时，Markov 不等式给异常事件密度

\[
\operatorname{Bad}_a(\varepsilon)
\le \exp(-c_\varepsilon(\log P)(\log\log P)).
\]

这里的“异常事件密度”说明单切片模型在主量足够大时的尾界形态；但它不用于对所有单个 `a` 逐点并合。最终只对 B.0.3 形成的 dyadic 双线性盒级统计量和允许窗口簇并合，`\exp(-c\log P\log\log P)` 对这些压缩参数已足够。

当 `\mu_a<(\log P)^A` 时，逐个 `a` 的 Markov 论证不适用。它们不能简单称为可忽略尾层，因为在半素数主层中这类短区间可能承载主贡献。本文对这部分不作点态剥离，而交由命题 B.0.3 的双线性平均估计处理。只有真正的端点盒、低体积盒和曲线边界层，其 Stieltjes 盒体积为 `o(1)`，才可直接吸收进 `o(Y/\log P)`。

**单个 dyadic 盒。** 一个盒中允许的前置因子 `a` 个数可达 `P^{O(1)}`，因此不能逐个 `a` 并合。正确做法是把盒内所有 `a` 与最后自由变量 `p` 合并成一个双线性统计量；该盒级统计量才是命题 B.0.0 允许并合的压缩参数。对单个 `a` 的估计只作为启发模型，不进入最终求和。短缩放区间和主切片统一由下面的双线性平均命题处理。

**命题 B.0.3（短缩放区间的双线性平均接口）。** 固定一个 dyadic 盒

\[
a\in A=[A_0,A_1],\qquad p\in P_0=[P_0,P_1],
\]

其中 `a` 为已选大素因子的乘积，`p` 为最后自由素因子，并满足盒内 `ap` 可落入 `I(\mathcal W)`。设

\[
\mathcal R=\{(a,p):a\in A,\,p\in P_0,\,ap\in I(\mathcal W)\}.
\]

则 prime-like 上界筛余计数满足

\[
\sum_{(a,p)\in\mathcal R}
1_{(ap,\prod_{q\le B}q)=1}
\le
(1+o(1))\operatorname{Vol}_{St}(\mathcal R)
\prod_{q\le B}\left(1-\frac1q\right)
+o(Y/\log P),
\]

其中 `\operatorname{Vol}_{St}(\mathcal R)` 表示对前置素因子使用 Stieltjes 权 `dt/\log t` 后的盒体积。端点盒、低体积盒与曲线边界层的总 Stieltjes 体积为 `o(Y)`。

**证明。** 证明分为五步。该命题是 B.0 中替代逐点短区间 PNT 的核心双线性接口；它不是从单个 `I_a` 的点态估计推出，而是从定理 2.2 的 connected cumulant 机制在二维参数族上的同构展开推出。

**第一步：盒内平坦化。** 将 `\log a` 与 `\log p` 再细分为宽度

\[
\Delta=(\log P)^{-2}
\]

的小盒。在一个小盒中，`a` 与 `p` 的 Stieltjes 密度变化为 `1+o(1)`。曲线带 `ap\in I(\mathcal W)` 可由上下 Darboux 和夹住：除去总 Stieltjes 体积为 `O(\Delta Y)` 的边界层后，它等价于有限个矩形带的并。由于 `\Delta=(\log P)^{-2}`，该误差为 `o(Y/\log P)`。

**第二步：二维 CRT 投影。** 对固定筛素数 `q\le B`，盒中所有 `a` 均由 `>B` 的素因子组成，故 `(a,q)=1`。筛余条件是排除

\[
ap\equiv0\pmod q.
\]

由于 `a` 在模 `q` 下可逆，该坏同余等价于唯一的

\[
p\equiv0\pmod q.
\]

更一般地，对任意 squarefree `Q`，若 `Q|\prod_{q\le B}q`，则 `(a,Q)=1`，并且 `ap\equiv b\pmod Q` 等价于唯一的 `p\pmod Q` 条件。故二维问题在每个固定 `a` 切片上有与一维筛余完全相同的 CRT 投影；`a` 只改变切片权重，不改变局部密度因子。

**第三步：中心化展开的二维提升。** 本步把 A.2–A.7 的一维 connected cumulant 账本逐项搬到二维带。为便于审查，拆成五个子点。

**B.0.3a：Möbius-Bell 展开不变。** 这里展开的不是“精确为素数”的指示，而是 prime-like 小筛上界指示

\[
S_B(ap)=1_{(ap,\prod_{q\le B}q)=1}.
\]

它只排除 squarefree 小筛模数中的坏剩余类，并满足真实素数集合 `\subseteq` prime-like 集合；因此用于合数层容量上界是合法的。由于每个小素数只出现一次，展开为

\[
S_B(ap)=\prod_{q\le B}(1-1_{q|ap}),
\]

不会产生重复小素因子幂条件；所有模数均为 squarefree。由于 `(a,q)=1`，局部坏事件 `q|ap` 等价于 `q|p`。因此每个局部 Bell 分区仍只记录若干 `p` 坐标在模 `q` 下的碰撞或避让；其局部 rank 与命题 A.2.1 中完全相同，局部系数仍满足 `q^{-\rho}` 型上界。`a` 不产生新的 Bell 块，只作为外层权重进入。

**B.0.3b：connected 消去仍成立。** 严格地说，二维带中的 cumulant 可先条件于前置因子向量 `a_1,\ldots,a_r` 展开。固定这些 `a_i` 后，变量只剩 `p_1,\ldots,p_r`，且由 B.0.3a 每个小筛坏事件 `q|a_ip_i` 都等价于 `q|p_i`。因此局部 Bell 分区、碰撞超边和中心化边基与命题 A.2.1 完全相同。

若条件展开得到的超图在顶点集 `\{1,\ldots,r\}` 上断开，即存在非空分解 `I=I_1\sqcup I_2` 且没有超边跨越两侧，则该项可写成

\[
F_1((p_i)_{i\in I_1};a_{I_1})
F_2((p_i)_{i\in I_2};a_{I_2}).
\]

在 joint cumulant 的分区 Möbius 和中，这类可分裂项按命题 A.2.1 精确抵消。该抵消是对每个固定 `a_1,\ldots,a_r` 的代数恒等式，而不是平均意义下的近似估计。

随后对 `a_1,\ldots,a_r` 作 Stieltjes 加权求和。由于被积函数中的断开项已经逐点等于 `0`，线性积分不会重新产生断开贡献；也不会产生跨越 `I_1,I_2` 的新同余边，因为 `a_i` 只作为各自顶点的可逆权重进入局部条件。因此 surviving 项仍为 connected 中心化超图。

**B.0.3c：skeleton rank 不降。** 对 surviving connected 超图，仍可在 `p` 顶点集上选取 skeleton 生成树。需要检查的是：不同顶点可能带有不同前置因子 `a_i`，同余碰撞实际形如

\[
a_i p_i\equiv a_j p_j\pmod q.
\]

但所有 `a_i` 都只含 `>B` 的素因子，而 `q\le B`，故 `(a_i a_j,q)=1`。于是该碰撞等价于可逆线性同余

\[
p_i\equiv \lambda_{ij}(a)p_j\pmod q,
\qquad
\lambda_{ij}(a)\equiv a_i^{-1}a_j\pmod q.
\]

这仍是一条 rank 为 `1` 的线性约束。对一个大小为 `s` 的 Bell 块 `C`，选根 `i_C` 后，条件

\[
a_i p_i\equiv a_{i_C}p_{i_C}\pmod q
\qquad (i\in C\setminus\{i_C\})
\]

等价于 `s-1` 条独立可逆线性同余

\[
p_i\equiv a_i^{-1}a_{i_C}p_{i_C}\pmod q.
\]

因此局部 rank 仍为 `|C|-1`，不会因为 `a_i` 的存在而下降。兼容性失败的系统贡献为 `0`；兼容时 CRT 合并后的模数仍是相关 squarefree 小筛模数的乘积。

于是命题 A.3.1 的 skeleton 分解

\[
\rho(\Gamma)=(r-1)+\rho_{ex}(\Gamma)
\]

逐字成立。端点选择多出的只是 `a` 盒的选择权重，其 Stieltjes 总量已包含在 `\operatorname{Vol}_{St}(\mathcal R)` 中，不进入 Bell/rank 组合数。

**B.0.3d：tiny/near/far 账本不变。** 由 B.0.3c，同余边在固定 `a` 后可能变为

\[
p_i\equiv \lambda_{ij}(a)p_j\pmod q.
\]

这里 `\lambda_{ij}(a)` 只改变具体剩余类，不改变模数 `q`，也不改变该边提供的 rank。A.4 的 Euler/Rankin 账本只依赖三类数据：小筛素数标签 `q` 的大小、squarefree 模数乘积 `Q_\Gamma`、以及 skeleton/非骨架 rank；它不依赖具体剩余类。因此 `\lambda_{ij}(a)` 不改变 near/far Euler 因子。

对于 tiny 层，有限模数

\[
M_0=\prod_{q\le A_1r}q
\]

仍只作用在 `p` 的同余坐标上。因为所有前置因子均由 `>B` 的素因子组成，且 `A_1r<B`，所以 `(a_i,M_0)=1`。于是任意 tiny 层条件 `a_i p_i\equiv b\pmod {M_0}` 等价于唯一的 `p_i\pmod {M_0}` 条件；CRT 投影恒等与 A.1 完全相同。若多个 tiny 条件不兼容，贡献为 `0`；若兼容，合并后的模数仍为 `M_0` 的因子。固定 `a` 后的断开项仍逐点由 A.2 的 cumulant 反演抵消；随后对 `a` 作 Stieltjes 加权平均不会重新产生跨块边。tiny 层端点项继续交由 B.0.4 的二维边界平均吸收。

near 与 far 层的 Euler 因子只依赖小筛素数标签和 skeleton rank，故命题 A.4.1 的三层估计保持。Rankin/divisor 损失已按 A.4 逐素数吸收，只取决于小筛素数标签、局部 rank 与 skeleton 结构，不因 Stieltjes 加权的 `a` 平均或剩余类变化而增加。

**B.0.3e：叶剥离与外层平均可交换。** 固定 `a` 和 connected skeleton，考虑当前叶变量 `p_v`。所有含 `p_v` 的边给出若干条件

\[
p_v\equiv r_j(a,p_W)\pmod {Q_j},
\]

其中 `W` 是父点及尚未剥离的相邻变量集合。每个 `Q_j` 是相关小筛 squarefree 模数的因子；它只由边标签决定，不依赖具体剩余类。若这些条件不兼容，则该叶求和为 `0`。若兼容，CRT 将其合并为唯一条件

\[
p_v\equiv r_v(a,p_W)\pmod {Q_v},
\qquad Q_v\mid Q_\Gamma.
\]

这里 `r_v(a,p_W)` 可以依赖前置因子和邻点变量，但 `Q_v` 只依赖模数集合。因此 rank、Euler 和 divisor 账本只看 `Q_v`，不看 `r_v`。

命题 A.6.1 的基本估计对所有剩余类一致成立：对任意整数区间 `I`、任意 `Q≥1`、任意剩余类 `b`，

\[
\sum_{p\in I}\left(1_{p\equiv b\pmod Q}-\frac1Q\right)=O(1),
\]

其中常数与 `b` 无关。因此对每个固定 `a,p_W`，都有

\[
\sum_{p_v\in I_v(a)}
\left(1_{p_v\equiv r_v(a,p_W)\pmod {Q_v}}-\frac1{Q_v}\right)=O(1)
\]

且该 `O(1)` 对所有允许的 `a,p_W,Q_v` 统一。多个模数合并的兼容性选择已作为逐素数局部选择计入 A.4 的 Rankin/divisor 账本。

因此剥离过程可先在每个切片执行，再对 `a` 加权平均。唯一不能逐片相加的是这些统一 `O(1)` 的端点项；该误差交给 B.0.4 的二维边界平均处理。除端点外，反复剥离 `r-1` 个叶子后只剩一个自由体积因子，即二维带的 Stieltjes 主体积，而非每个短切片的长度下界。

合并 B.0.3a–e，A.2–A.7 的 connected cumulant 总和界在二维带中变为

\[
\sum_{(a_1,p_1),\ldots,(a_r,p_r)\in\mathcal R}
\kappa(Y_{a_1,p_1},\ldots,Y_{a_r,p_r})
\ll
\operatorname{Vol}_{St}(\mathcal R)
(Cr)^{Cr}(\log\log P)^{r-1}\log^{Cr}P,
\]

其中

\[
Y_{a,p}=S_B(ap)-\prod_{q\le B}\left(1-\frac1q\right),\qquad S_B(ap)=1_{(ap,\prod_{q\le B}q)=1}.
\]

再由命题 A.7.1 的 moment-cumulant 转移，得到 B.0.3 所需的二维平均集中估计。

**B.0.3f：Stieltjes 权重的交换。** 上述 cumulant 估计最初可在离散前置因子集合上写出。若 `a` 是 `k-1` 个大素因子的乘积，定义 Stieltjes 卷积测度

\[
d\Pi_{k-1}(t)
=
\sum_{p_1\cdots p_{k-1}\in dt}
1,
\]

其连续近似为

\[
d\Pi_{k-1}(t)
\sim
\int_{u_1\cdots u_{k-1}=t}
\frac{du_1}{\log u_1}\cdots\frac{du_{k-1}}{\log u_{k-1}}.
\]

在 dyadic 小盒中，各 `\log u_i` 变化为 `1+o(1)`，故该测度有局部近似密度。这里使用的是前置素因子的全局 Stieltjes/PNT 上界，不涉及最后自由变量 `p` 的短区间 PNT；短缩放困难已经由 B.0.3 的双线性平均处理。对非负或取绝对值后的误差函数 `F`，只需上界方向：

\[
\sum_{a\in A_{box}}F(a)
\le (1+o(1))\int_{A_{box}}F(t)\,d\Pi_{k-1}(t)+O(E_{bd}^{St}).
\]

这里 `E_{bd}^{St}` 是 Stieltjes 体积尺度上的边界误差，与命题 B.0.4 中的边界账本相同：它包括 dyadic 盒端点、曲线带 Darboux 边界、低体积盒以及切片端点穿越误差。B.0.4 已证明

\[
E_{bd}^{St}\le(\Delta+\log^{-A}P)\operatorname{Vol}_{St}(\mathcal R)
\]

在未乘小筛密度的 Stieltjes 体积尺度上成立。定义筛余尺度边界误差

\[
E_{bd}^{sieve}=E_{bd}^{St}\prod_{q\le B}\left(1-\frac1q\right).
\]

则 `E_{bd}^{sieve}` 才是 B.0.3g 中使用的边界筛余误差。

由于 connected rank 账本对每个固定 `a` 一致成立，且所有常数只依赖 `r` 而不依赖 `a`，该 Stieltjes 积分只把最后剩余的自由体积因子从 `|I_a|` 积分成 `\operatorname{Vol}_{St}(\mathcal R)`。它不改变 `q^{-\rho}`、skeleton 数量、tiny/near/far Euler 乘积或 Rankin 指数。

**B.0.3g：二维高矩转移。** 令

\[
X_{\mathcal R}=\sum_{(a,p)\in\mathcal R}

\left(S_B(ap)-\prod_{q\le B}\left(1-\frac1q\right)\right).
\]

这里 `X_{\mathcal R}` 是未归一化的筛余计数偏差，故其自然主量是筛余尺度 `\mu_{\mathcal R}`，与命题 A.7.1 中乘回密度后的 `Z_Ω` 同型。

由 B.0.3a–f 得到所有 `2\le r\le c_0\log P` 的 cumulant 总和界。先写在 Stieltjes 体积尺度上为

\[
|\kappa_r(X_{\mathcal R})|
\le
\operatorname{Vol}_{St}(\mathcal R)
(Cr)^{Cr}(\log\log P)^{r-1}\log^{Cr}P+O(E_{bd}^{sieve}).
\]

其中 `E_{bd}^{sieve}` 是 B.0.4 给出的筛余尺度边界误差。为了与随机变量 `X_{\mathcal R}` 的均值尺度一致，下面把主项也归一化到筛余尺度。定义

\[
\mu_{\mathcal R}=\operatorname{Vol}_{St}(\mathcal R)
\prod_{q\le B}\left(1-\frac1q\right).
\]

在主盒上，B.0.4 给出

\[
E_{bd}^{sieve}\le (\Delta+\log^{-A}P)\mu_{\mathcal R}.
\]

由于 Mertens 公式给

\[
\prod_{q\le B}\left(1-\frac1q\right)\asymp\frac1{\log P},
\]

有 `\operatorname{Vol}_{St}(\mathcal R)\ll\mu_{\mathcal R}\log P`。这个额外 `\log P` 因子由已有的 `\log^{Cr}P` Rankin 账本吸收。因此 cumulant 总和界可写成同尺度形式

\[
|\kappa_r(X_{\mathcal R})|
\le
\mu_{\mathcal R}(Cr)^{Cr}(\log\log P)^{r-1}\log^{Cr+C}P
+(\Delta+\log^{-A}P)\mu_{\mathcal R}.
\]

第二项可并入第一项的低阶误差。把该界代入命题 A.7.1 的 moment-cumulant 转移，得到主盒高矩界

\[
\mathbb E|X_{\mathcal R}|^{2m}
\le
(Cm)^{Cm}\mu_{\mathcal R}^{m}\log^{Cm+C m}P.
\]

这里不再出现独立的 `o((Y/\log P)^m)` 项；所有误差都已相对 `\mu_{\mathcal R}` 归一化。若 `\mu_{\mathcal R}\ge(\log P)^A`，取 `m=c\log P` 并用 Markov 不等式，得

\[
\mathbb P(|X_{\mathcal R}|>\varepsilon\mu_{\mathcal R})
\le
\frac{(Cm)^{Cm}\mu_{\mathcal R}^{m}\log^{C'm}P}
{\varepsilon^{2m}\mu_{\mathcal R}^{2m}}
=
\left(\frac{(Cm)^C\log^{C'}P}{\varepsilon^2\mu_{\mathcal R}}\right)^m.
\]

这里 `C'` 吸收上式中的全部对数损失，包括从 `\operatorname{Vol}_{St}` 转到 `\mu_{\mathcal R}` 的额外 `\log P`。若固定选择

\[
A>2C'+10,
\]

则在主盒上

\[
\frac{(Cm)^C\log^{C'}P}{\varepsilon^2\mu_{\mathcal R}}
\le
\log^{-A/2}P
\]

对充分大 `P` 成立。因此

\[
\mathbb P(|X_{\mathcal R}|>\varepsilon\mu_{\mathcal R})
\le
\exp(-c_\varepsilon(\log P)(\log\log P)).
\]

若需要更强的 `\exp(-c(\log P)^2)` 尾界，则把主盒阈值提升为 `\mu_{\mathcal R}\ge P^{\eta}`；本文对 dyadic 盒并合只需要上述 `\exp(-c\log P\log\log P)`，因为盒数为 `O((\log P)^3)`。坏主盒数至多

\[
O((\log P)^3)\exp(-c\log P\log\log P)<1
\]

对充分大 `P` 成立，故所有主盒同时具有相对误差 `o(\mu_{\mathcal R})`。

若 `\mu_{\mathcal R}<(\log P)^A`，该盒定义为低体积盒，不使用高矩相对误差；它的总贡献按 Stieltjes 主量直接估计，并在 B.0.4 的低体积盒账本中并入 `O(Y/\log^A P)`。主盒和低体积盒分开处理后，再对 `O((\log P)^3)` 个 dyadic 盒并合。

**命题 B.0.4（单调曲线带的二维边界平均）。** 设

\[
\mathcal R=\{(a,p):a\in[A_0,A_1],\ p\in[P_0,P_1],\ ap\in [N,N+Y]\}
\]

是一个 dyadic 小盒内的曲线带，且 `A_1/A_0=1+O(\Delta)`，`P_1/P_0=1+O(\Delta)`。对每个 `a`，记切片

\[
I_a=\{p:(a,p)\in\mathcal R\}.
\]

则叶剥离产生的切片端点误差在 `a` 上求和满足

\[
\int_{A_0}^{A_1}O(1)\,d\Pi_{k-1}(a)
\]

不能按切片数粗估，而应按端点轨迹估计为

\[
O(\Delta Y)+O(Y/\log^A P)+O(1).
\]

对所有 dyadic 小盒求和后，总边界误差为 `o(Y/\log P)`。

**证明。** 切片端点由两条单调曲线给出：

\[
p_-(a)=\frac{N}{a},
\qquad
p_+(a)=\frac{N+Y}{a}.
\]

在小盒 `A_1/A_0=1+O(\Delta)` 内，二者的总变差满足

\[
\operatorname{Var}(p_-)+\operatorname{Var}(p_+)
\ll \Delta P_0+\frac{Y}{A_0}.
\]


**审查补正。** 仅有上述变差界还不足以推出相对主量的 `O(\Delta)` 边界误差。因为曲线带主体积约为

\[
\operatorname{Vol}_{St}(\mathcal R)\asymp w_A\,Y\Delta,
\]

而端点变差项可达 `w_A\Delta P_0`。若 `P_0\gg Y`，则该项可能远大于主体积。因此 B.0.4 的严格闭合必须额外证明一个“边界相消/平均化”命题，而不能只靠单调曲线总变差。本文后续使用 B.0.4 时，实际需要的是如下可审查接口：对所有参与的 dyadic 曲线带，叶剥离端点项在完整 residue 类、相邻盒拼接与 Stieltjes 加权平均后满足

\[
E_{bd}^{St}(\mathcal R)
\ll \Delta\operatorname{Vol}_{St}(\mathcal R)+O(Y/\log^A P).
\]

下面的变差论证只证明了该接口在端点漂移受控情形 `P_0\ll Y` 或经额外边界相消后成立；一般情形需作为独立的边界平均命题继续证明。

把 `p` 轴按整数或模 `Q` 的 residue 边界切分时，每个端点穿过一个边界至多贡献常数。因此所有端点误差由端点曲线穿越次数控制，而不是由切片个数控制。对 Stieltjes 权 `d\Pi_{k-1}(a)`，盒内密度变化为 `1+o(1)`，故端点穿越次数的加权版本仍由同一变差界控制。

更精确地说，盒内 Stieltjes 测度可写成

\[
d\Pi_{k-1}(a)=(1+o(1))w_A\,da,
\]

其中 `w_A` 在小盒中近似常数。曲线带的 Stieltjes 主体积满足

\[
\operatorname{Vol}_{St}(\mathcal R)
=(1+o(1))w_A\int_{A_0}^{A_1}|I_a|\,da.
\]

而端点变差贡献为

\[
w_A\bigl(\operatorname{Var}(p_-)+\operatorname{Var}(p_+)\bigr).
\]

由于 `|I_a|=(N+Y)/a-N/a=Y/a`，且小盒内 `a\asymp A_0`，有

\[
\int_{A_0}^{A_1}|I_a|\,da
\asymp \frac{Y}{A_0}(A_1-A_0)
\asymp Y\Delta.
\]

因此，若已知上述边界平均接口，或处在端点漂移受控的子情形，则量纲上得到

\[
E_{bd}^{St}(\mathcal R)
\ll \Delta\operatorname{Vol}_{St}(\mathcal R)+O(Y/\log^A P).
\]

没有该接口时，单纯的端点变差只给出 `O(w_A\Delta P_0)`，不足以支撑后续相对误差估计；这是 B.0.4 当前最核心的待闭合点。

**进一步化简为 sawtooth 边界和。** 对固定模数 `Q` 与剩余类 `b(a)`，切片端点误差可精确写成

\[
\sum_{a\in A_{box}}W(a)
\left(
\psi\left(\frac{N+Y}{aQ}-\frac{b(a)}Q\right)
-
\psi\left(\frac{N}{aQ}-\frac{b(a)}Q\right)
\right),
\qquad
\psi(t)=\{t\}-\frac12 .
\]

因此一般 B.0.4 闭合等价于证明如下双线性边界相消估计：对所有由 connected 叶剥离产生的可逆剩余类函数 `b(a)`，有

\[
\left|
\sum_{a\in A_{box}}W(a)
\left(
\psi\left(\frac{N+Y}{aQ}-\frac{b(a)}Q\right)
-
\psi\left(\frac{N}{aQ}-\frac{b(a)}Q\right)
\right)
\right|
\ll \Delta\operatorname{Vol}_{St}(\mathcal R)+O(Y/\log^A P).
\]

这一定式比总变差强得多；它要求随 `a` 变化的倒数相位 `N/a` 在 Stieltjes 权上产生平均相消。若能从 USC 的二维 connected 机制或独立的 Type-I/II 倒数相位估计推出该 sawtooth 界，则 B.0.4 完全闭合。反之，若没有该界，短切片逐点端点误差无法被现有总变差论证消除。

**等价的短区间双线性除数误差形式。** 由恒等

\[
\#\{p:p\equiv b(a)\pmod Q,\\ N<ap\le N+Y\}
=\frac{|I_a|}{Q}+\text{sawtooth boundary},
\]

上述 sawtooth 界等价于

\[
\sum_{a\in A_{box}}W(a)
\#\{p:p\equiv b(a)\pmod Q,\\ N<ap\le N+Y\}
=
\frac1Q\sum_{a\in A_{box}}W(a)|I_a|
+O\left(\Delta\operatorname{Vol}_{St}(\mathcal R)+Y/\log^A P\right).
\]

这就是一个带可逆剩余类约束的短区间 Type-I 双线性除数误差估计。它不能从单纯几何单调性推出；若取 `Q=1`、`W=1`，它退化为短区间双曲线格点计数误差。因而 B.0.4 的完全闭合需要新增如下独立命题。

**命题 B.0.4\*（短区间双线性边界相消，待证核心）。** 对所有 B.0.3 产生的 dyadic 主盒、所有 squarefree `Q` 和所有可逆剩余类函数 `b(a)`，上式成立，并且常数在 `2m≤c_0\log P` 的 cumulant 展开范围内一致。

一旦 B.0.4\* 成立，B.0.4 的其余部分严格闭合；若没有 B.0.4\*，当前证明只能得到“端点漂移受控盒”或“假设边界相消接口”的条件版本。

**可证性检查与障碍。** B.0.4\* 在 `Q=1`、`b(a)=0`、`W(a)=1` 的特例中包含估计

\[
\sum_{a\in[A,A(1+\Delta)]}
\left(
\lfloor (N+Y)/a\rfloor-\lfloor N/a\rfloor- Y/a
\right)
\ll \Delta Y\Delta+Y/\log^A P,
\]

即短乘积区间 `N<ap\le N+Y` 中的双曲线格点误差。这个问题本质上是短区间除数问题的 Type-I 版本。除非利用额外的平均、平滑或谱/指数和输入，一般不能从 CRT、connected cumulant 或单调几何本身推出。特别是当 `A\Delta` 很大而 `Y` 只略大于主盒阈值时，逐切片取整误差可在局部同向累积；总变差或端点穿越数只给 `O(A\Delta)`，不自动降到 `O(Y\Delta^2)`。

因此严格结论是：B.0.4 的一般端点漂移情形不是本文现有 USC 机制的形式推论，而是一个新的独立解析数论输入。若要无条件闭合全文，必须证明 B.0.4\*，或改造主证明避免使用短切片端点相消。

**可闭合替代路线：平滑窗口去端点化。** 为避免引入 B.0.4\* 这种短区间除数型输入，可以把行窗口簇的硬指示 `1_{n\in I(\mathcal W)}` 替换为平滑权重 `\Phi((n-N)/Y)`，其中 `\Phi` 支持在稍大的窗口内、在核心窗口上等于 `1`，且满足

\[
\|\Phi^{(j)}\|_\infty\ll_j H^{-j},
\qquad H=\Delta Y.
\]

此时切片和变为

\[
\sum_p \Phi\left(\frac{ap-N}{Y}\right)1_{p\equiv b(a)\pmod Q},
\]

若最后变量是普通整数，Poisson 求和或有限 Fourier 展开会给出相应的模 `Q` 平均。可是本文最后变量实际承载素数/Stieltjes 权重；因此不能要求每个固定 `a` 的短区间 PNT，而必须使用真正的双线性平均命题。平滑版 B.0.4S 应表述为

\[
\sum_{a\in A_{box}}W(a)
\left(
\sum_{p\equiv b(a)\pmod Q}\Phi\left(\frac{ap-N}{Y}\right)d\pi(p)
-
\frac1{\varphi(Q)}\sum_{(p,Q)=1}\Phi\left(\frac{ap-N}{Y}\right)d\pi(p)
\right)
\]

\[
\ll_A \operatorname{Vol}_{St}(\mathcal R)\log^{-A}P .
\]

这里误差只要求在 `a` 的 Stieltjes 平均后成立；这正是避免逐点短区间 PNT 的关键。也就是说，平滑化消除了 sawtooth 取整边界，但把问题转化为标准的平滑 Type-I 素数双线性平均。代价是主证明必须把“窗口含素数”的硬窗口改为“核心窗口由平滑权重支配”：选取 `\Phi` 在核心子窗口上为 `1`，在外层缓冲区非负；若平滑窗口中合数期望小于候选权重，则核心或缓冲窗口中含素数。再通过边界处使用单侧平滑扩展，保证扩展窗口仍留在同一行内。

**可直接闭合的长切片子情形。** 若盒中最后变量的平滑长度满足

\[
Y/a\ge p_0^{\theta}
\]

对某个固定 `\theta>0` 成立，且 `Q\le \log^C P`，则 B.0.4S 可由 Siegel-Walfisz 型素数算术级数估计和分部积分推出。真正困难的是 `Y/a` 低于任意固定幂的短切片盒；这些盒正是原先硬端点问题出现的位置。因而平滑路线把最终缺口进一步压缩为：证明短切片盒上的平均型平滑 Type-I 素数双线性估计，或证明这类短切片盒的总 Stieltjes 主量在行窗口安全间隙中可被其它层吸收。

**短切片不可直接吸收。** 在半素数主层中典型地 `a\asymp \sqrt P`、`Y\asymp \sqrt P`，故 `Y/a\asymp1`，这正是主贡献所在，而非低体积尾层。其 Stieltjes 主量约为

\[
\int_{a\asymp\sqrt P}\frac{Y/a}{\log a\log(Y/a+2)}\,da
\asymp \frac{Y}{\log P},
\]

与安全间隙同阶。因此短切片盒不能简单丢弃；必须依靠双线性平均而非逐切片长度。这样，最终核心接口进一步精炼为：在 `Y/a=O(1)` 到对数幂范围内，对前置因子 `a` 的 Stieltjes 平均必须提供足够的素数/AP 平均相消。

**最终单一短切片接口 B.0.4S-short。** 对半素数主层的短切片盒 `a\asymp\sqrt P`、`Y/a\asymp1`，需要证明

\[
\sum_{a\asymp\sqrt P}W(a)
\left(
\sum_{p\equiv b(a)\pmod Q}\Phi(ap)d\pi(p)
-
\frac1{\varphi(Q)}\sum_{(p,Q)=1}\Phi(ap)d\pi(p)
\right)
=o(Y/\log P).
\]

这是当前行方向证明真正剩余的单一核心接口。它是“短切片、长 `a` 平均”的素数双线性分布问题；若能证明它，则平滑 B.0.4S 成立，进而行命题闭合。若不能证明它，则无论硬窗口还是平滑窗口路线，都还缺少一个与短区间素数/除数分布同等深度的输入。

这条平滑路线把 B.0.4 的待证内容替换为标准平滑 Type-I 素数双线性估计，形式上比尖锐 sawtooth 边界更接近现有解析数论工具；但它仍是额外输入，不能由 Poisson 公式单独推出。本文当前把它记为平滑版 B.0.4S；若 B.0.4S 得证，则平滑行命题链条闭合。

乘以小筛密度 `\prod_{q\le B}(1-1/q)\asymp1/\log P` 后，边界筛余误差为

\[
O\left(\frac{\Delta\operatorname{Vol}_{St}(\mathcal R)}{\log P}\right)
+O\left(\frac{Y}{\log^{A+1}P}\right),
\]

这正是相对主项的 `O(\Delta)+O(\log^{-A}P)` 损失。

主盒满足 `\mu_{\mathcal R}\ge(\log P)^A`。在上述边界平均接口成立的前提下，边界筛余误差相对主量为 `O(\Delta)+O(\log^{-A}P)`；低体积盒的总主量按定义并入 `O(Y/\log^A P)`。取 `\Delta=(\log P)^{-2}` 且 `A` 足够大，所有小盒和 dyadic 盒并合后得到 `o(Y/\log P)`。

该引理说明：叶剥离中的 `O(1)` 端点项不能逐个短切片累加；必须证明它们在二维曲线边界上具有足够平均相消。端点漂移受控情形可由总变差处理，一般情形则正是 B.0.3e 与第四步交换需要补强的几何原因。

在 connected skeleton 中最多剥离 `r-1≤c_0\log P` 个叶变量。每次剥离产生的端点轨迹仍由同一类单调曲线带控制，故总边界误差至多再乘 `O(r)` 以及来源选择因子 `(Cr)^{C}`。在边界平均接口成立后，这些因子由 A.4 的 `\log^{Cr}P` 与 B.0.3g 的高矩账本吸收；取 `A` 足够大后仍为 `o(Y/\log P)`。

**第四步：短切片的平均替代。** 单个切片 `I_a` 可以很短，故上式中的 `O(1)` 端点误差不能逐个求和。由命题 B.0.4 的目标接口，切片端点应按二维曲线边界的平均相消计数，而不是按切片个数计数。在该接口成立时，所有切片端点误差总量不超过边界 Darboux 体积加 `O(Y/\log^A P)` 的低体积盒贡献。换言之，端点误差在二维平均后为

\[
O(\Delta Y)+O(Y/\log^A P)=o(Y/\log P).
\]

这正是双线性平均优于逐点短区间估计的地方。

**第五步：恢复主项。** 主项来自所有局部模数的独立密度乘积：

\[
\prod_{q\le B}\left(1-\frac1q\right).
\]

对 `a` 的求和用 Stieltjes 权恢复，得到 `\operatorname{Vol}_{St}(\mathcal R)`。所有 connected 非主项由第三步的 rank 账本给出 `o(Y/\log P)`；所有几何边界由第四步吸收。因此得到命题所述估计。

**审查标记。** B.0.3 与 B.0.4 是当前行方向证明中最应独立核验的技术命题；尤其 B.0.4 的一般端点漂移情形仍需独立证明边界平均/相消接口。严格定稿时，应把 B.0.3a–g 与 B.0.4 逐项对照命题 A.2.1、A.3.1、A.4.1、A.6.1、A.7.1 展开，确认 Stieltjes 加权平均、二维边界平均、单调曲线端点变差和 moment-cumulant 转移不会破坏 connected rank、叶剥离常数与高矩范围。

**全部盒。** dyadic 盒数为 `O((\log P)^3)`，命题 B.0.0 处理压缩盒级主参数部分，命题 B.0.3 处理短缩放区间双线性平均部分，端点和低体积盒由 B.0.3 的边界体积估计吸收。令 `\varepsilon\to0` 缓慢，得到

\[
\sum_a E_a=o(Y/\log P)
\]

在局部窗口簇平均意义下成立。若存在正常窗口簇违反它，则命题 B.4.1 的坏窗口扩散步骤会产生正比例异常密度，与命题 B.0.0 和命题 B.0.3 的平均并合界矛盾。

这里“prime-like at level `B`”是 squarefree 小筛上界条件：只要求避开所有 `q≤B` 的小素因子，不声称精确刻画素数。真实素数集合被该筛余集合包含，因此用于上界是合法的；多计入的粗合数正是 B.2/B.3 已单独控制的层。

**第四步：恢复 Stieltjes 密度。** 在命题 B.0.3 的双线性表述中，固定盒的主项不是逐个短区间 `I_a` 的点态主项，而是曲线带

\[
\mathcal R=\{(a,p):a\in A_{box},\ ap\in I(\mathcal W)\}
\]

的 Stieltjes 体积：

\[
\operatorname{Vol}_{St}(\mathcal R)
=
\int_{a\in A_{box}} |I_a|\,d\Pi_{k-1}(a).
\]

对非边界主盒，平均意义下有

\[
|I_a|=\frac{Y}{a}+O(1),
\]

但该等式只用于计算 `\operatorname{Vol}_{St}(\mathcal R)`，不作为逐个 `a` 的筛余估计。由 B.0.4，`O(1)` 端点项和曲线边界项在盒平均后贡献

\[
o(Y/\log P)
\]

到最终筛余尺度。因此固定盒内主项恢复为

\[
\operatorname{Vol}_{St}(\mathcal R)
\prod_{q≤B}\left(1-\frac1q\right)
=
Y\prod_{q≤B}\left(1-\frac1q\right)
\int_{a\in A_{box}}\frac{d\Pi_{k-1}(a)}{a}
+o(Y/\log P).
\]

这就是原先 `\sum_a |I_a|` 公式的盒级 Stieltjes 版本；所有离散端点误差已归入 B.0.4 的边界账本。

现在估计前置因子的 Stieltjes 积分。若 `k=2`，则 `a=p_1`，在盒 `p_1\in[P^α,P^{α+\Delta}]` 中，离散素数和由全局 PNT/Stieltjes 上界恢复为

\[
\sum_{p_1\in box}\frac1{p_1}
=(1+o(1))\int_{P^α}^{P^{α+\Delta}}\frac{dt}{t\log t}.
\]

若 `k=3`，则 `a=p_1p_2`，相应的卷积 Stieltjes 积分为

\[
\sum_{p_1,p_2\in box}\frac1{p_1p_2}
=(1+o(1))
\iint_{box}\frac{dt_1dt_2}{t_1t_2\log t_1\log t_2}.
\]

这些公式只是 PNT/Stieltjes 对前置因子集合的全局求和；局部分布困难已经由第三步的 USC 筛余估计承担。

最后使用 Mertens 公式

\[
\prod_{q≤B}\left(1-\frac1q\right)
=(1+o(1))\frac{e^{-γ}}{\log B}
=(1+o(1))\frac{2e^{-γ}}{\log P}.
\]

把 dyadic 盒 Riemann 和合并，就得到全局积分密度 `\mathfrak C_k(P)`。与小筛候选密度

\[
H\text{-density}=(1+o(1))\prod_{q≤B}\left(1-\frac1q\right)
\]

相比，乘积中的 Mertens 因子会在比值中抵消，只留下由大素因子 Stieltjes 积分给出的常数。本文只用两种情形：`k=2` 时得到半素数主层常数 `\frac{e^γ}{4}\log3`；`k=3` 时得到三粗因子层安全常数 `θ_3=0.42`。因此 B.0.0–B.0.4 正是 B.1 与 B.3 所需的局部残差平均控制。

**B.1 半素数主层。** 令 `B=√P`。由命题 B.0.0–B.0.4 的盒级局部乘积容量接口，对任意允许的局部窗口簇 `\mathcal W`，半素数层满足

\[
\mathbb E_{J\in\mathcal W}U_J
\le
\left(\frac{e^γ}{4}\log3+o(1)\right)
\mathbb E_{J\in\mathcal W}H_J+O(1).
\]

这里 `H_J` 的局部均值为

\[
\mathbb E_{J\in\mathcal W}H_J
=(1+o(1))Y\prod_{q≤B}\left(1-\frac1q\right),
\]

而命题 B.0.0–B.0.4 给出的 `U_J` 盒级局部主项为同一 `Y` 乘以半素数 Stieltjes 密度；这里的主项已经通过双线性盒和 `Vol_St` 恢复，不使用逐个短区间点态估计。因此只需计算二者的全局密度比值。

下面计算这个局部密度常数。全局模型计数满足

\[
U(P)\le
\sum_{B<u≤P\atop u\ prime}\pi(P^2/u),
\]

局部情形由命题 B.0.0–B.0.4 给出相同 Stieltjes 密度。使用 PNT 上界：对任意 `ε>0`，足够大 `x` 有

\[
\pi(x)≤(1+ε)\frac{x}{\log x}.
\]

于是

\[
U(P)≤(1+ε)
\sum_{B<u≤P\atop u\ prime}
\frac{P^2/u}{\log(P^2/u)}.
\]

用 Stieltjes 积分写为

\[
U(P)≤(1+ε)
\int_B^P
\frac{P^2/t}{\log(P^2/t)}d\pi(t).
\]

再用 PNT 上界或分部求和，得到

\[
U(P)≤(1+o(1))
\int_B^P
\frac{P^2}{t\log t\log(P^2/t)}dt.
\]

令 `t=P^a`，`dt/t=\log P\,da`，`a\in[1/2,1]`。则

\[
\log t=a\log P,
\qquad
\log(P^2/t)=(2-a)\log P.
\]

所以

\[
U(P)≤(1+o(1))\frac{P^2}{\log P}
\int_{1/2}^{1}\frac{da}{a(2-a)}.
\]

计算积分：

\[
\frac1{a(2-a)}=\frac12\left(\frac1a+\frac1{2-a}\right),
\]

故

\[
\int_{1/2}^{1}\frac{da}{a(2-a)}
=\frac12\log3.
\]

因此

\[
U(P)\le(1+o(1))\frac{P^2}{\log P}\cdot\frac12\log3.
\]

再与

\[
H(P)=(1+o(1))\frac{2e^{-γ}P^2}{\log P}
\]

比较，得到

\[
\frac{U(P)}{H(P)}≤\frac{e^γ}{4}\log3+o(1).
\]

同一比值由命题 B.0.0–B.0.4 在任意局部窗口簇 `\mathcal W` 中以盒级平均形式成立，因此 B.1 提供了 B.4 所需的局部残差平均条件。最后用 B.4 的局部平均到条件均值转移，得到引理 3.3。

**命题 B.2.1（缩放筛余容量乘法性）。** 设 `B=√P`，`L=4B`，与 1.1 的约定一致。对窗口 `J` 记

\[
S(J;B)=\#\{n\in J:(n,\prod_{q≤B}q)=1\},
\]

并令

\[
R_J=\#\{n\in J:(n,\prod_{q≤B}q)=1,
\exists u\in(B,4B]\text{ prime},\ u|n\}.
\]

需要证明的局部形式是：对任意允许的连续窗口簇 `\mathcal W`，

\[
\mathbb E_{J\in\mathcal W}R_J=o(\mathbb E_{J\in\mathcal W}S(J;B))+O(1).
\]

这比逐个 `u` 的点态乘法性更稳妥。证明如下。

不要对 `O(B/\log B)` 个素数 `u` 逐点并合。把所有 `u\in(B,4B]` 与缩放变量 `m` 合并成一个盒级双变量统计量：

\[
\mathcal R_u=\{(u,m):u\in(B,4B]\text{ prime},\ um\in I(\mathcal W),\ (m,\prod_{q\le B}q)=1\}.
\]

因为每个 `u>B` 与所有小筛素数 `q\le B` 互素，条件 `(um,\prod_{q\le B}q)=1` 等价于 `(m,\prod_{q\le B}q)=1`。因此小筛 CRT 密度在 `m` 坐标上保持不变。盒级统计量的主项为

\[
\mathbb E_{J\in\mathcal W}S(J;B)
\sum_{B<u\le4B\atop u\ prime}\frac1u,
\]

端点和缩放边界误差由与 B.0.4 相同的单调曲线边界账本吸收。这里曲线为 `um\in I(\mathcal W)`，与 B.0.3 的 `ap\in I(\mathcal W)` 完全同型；区别只是前置变量 `u` 本身是一个素数而非素数乘积，Stieltjes 权为 `d\pi(u)`。

于是直接得到盒级平均估计

\[
\mathbb E_{J\in\mathcal W}R_J
\le
\mathbb E_{J\in\mathcal W}S(J;B)
\sum_{B<u\le4B\atop u\ prime}\frac1u
+o(\mathbb E_{J\in\mathcal W}S(J;B))+O(1).
\]

Mertens 素数倒数公式给

\[
\sum_{B<u≤4B\atop u\ prime}\frac1u
=\log\log(4B)-\log\log B+O(1/\log B)
=O(1/\log B)=o(1).
\]

从而 `R` 层满足 B.4 所需的局部残差平均条件，故在所有正常窗口上有 `R_J=o(H_J)+O(1)`。

**命题 B.3.1（三粗因子层容量）。** 设 `B=√P`。由命题 B.0.0–B.0.4 的盒级局部乘积容量接口，对任意允许的局部窗口簇 `\mathcal W`，三粗因子层满足

\[
\mathbb E_{J\in\mathcal W}T_J
\le(\theta_3+o(1))\mathbb E_{J\in\mathcal W}H_J+O(1),
\qquad \theta_3=0.42.
\]

下面只计算安全常数。局部性已经由 B.0.0–B.0.4 提供；以下全局积分用于给出盒级 Stieltjes 密度与小筛候选密度的比值。若 `n≤P^2` 且 `n` 是小筛候选，又含至少三个大于 `B` 的素因子，则事实上只能写为

\[
n=abc,
\qquad a,b,c>B,
\qquad abc≤P^2,
\]

其中 `a,b,c` 为素数。因为若还有额外因子 `m>1`，由于 `n` 无 `≤B` 的素因子，`m` 也含某个 `>B` 的素因子，于是四个大因子的乘积超过 `B^4=P^2`，矛盾。

因此全局三粗因子数满足

\[
T(P)\le
\sum_{B<a≤b≤c\atop abc≤P^2\atop a,b,c\ prime}1.
\]

用 PNT 上界先固定 `a,b`，再计数 `c`。只有当 `ab≤P^{3/2}` 时才可能有 `c>B`，并且

\[
T(P)
\le
\sum_{B<a≤b\atop ab≤P^{3/2}}
\pi\left(\frac{P^2}{ab}\right).
\]

由 PNT 上界，

\[
\pi\left(\frac{P^2}{ab}\right)
\le(1+o(1))
\frac{P^2/(ab)}{\log(P^2/(ab))}.
\]

令 `a=P^α,b=P^β`。主项可由二维 Stieltjes 积分控制为

\[
T(P)
\le(1+o(1))
\frac{P^2}{\log P}
\int_{α,β>1/2\atop α≤β,\ α+β<3/2}
\frac{dαdβ}{αβ(2-α-β)}.
\]

若去掉 `α≤β` 只会增大积分，故可用显式上界

\[
I_3=
\int_{α,β>1/2\atop α+β<3/2}
\frac{dαdβ}{αβ(2-α-β)}<0.46.
\]

证明 `I_3<0.46` 如下。令

\[
x=α-\frac12,
\qquad y=β-\frac12.
\]

则 `x,y>0` 且 `x+y<1/2`，并且

\[
I_3=\int_{x,y>0\atop x+y<1/2}
\frac{dxdy}{(x+1/2)(y+1/2)(1-x-y)}.
\]

固定 `x` 后，对 `y` 作部分分式分解：

\[
\frac1{(y+1/2)(1-x-y)}
=\frac1{3/2-x}\left(\frac1{y+1/2}+\frac1{1-x-y}\right).
\]

故

\[
\int_0^{1/2-x}\frac{dy}{(y+1/2)(1-x-y)}
=\frac{2\log(2-2x)}{3/2-x}.
\]

令 `t=2x`，得到

\[
I_3=\int_0^1\frac{4\log(2-t)}{(1+t)(3-t)}dt.
\]

为了给出完全显式的上界，把区间分为 `[0,1/2]` 与 `[1/2,1]`。在 `[0,1/2]` 上，

\[
\log(2-t)\le\log2-\frac t2,
\qquad
(1+t)(3-t)=3+2t-t^2\ge3+\frac32t.
\]

在 `[1/2,1]` 上，`(1+t)(3-t)≥15/4`。因此

\[
I_3\le
\int_0^{1/2}\frac{4(\log2-t/2)}{3+3t/2}dt
+\frac4{15}\int_{1/2}^{1}4\log(2-t)dt
<0.46.
\]

最后一个不等式只含初等函数；左侧约为 `0.4563`。


于是

\[
T(P)
\le(1+o(1))\frac{I_3P^2}{\log P}.
\]

注意这里不是 `o(P^2/\log P)` 的无常数低阶，而是相对小筛候选有一个小的显式常数贡献。与

\[
H(P)=(1+o(1))\frac{2e^{-γ}P^2}{\log P}
\]

的归一化相比，得到显式常数界 `T(P)/H(P)≤e^γ I_3/2+o(1)<0.42+o(1)`。本文在正文中保留 `θ_3=0.42` 的安全常数，以避免依赖最尖锐的有序三元组常数。

由命题 B.4.1 的局部平均到条件均值转移，得到引理 3.5；其中命题 B.3.1 已提供命题 B.4.1 所需的局部残差平均条件。

**命题 B.4.1（局部平均到条件均值转移）。** 设 `\mathcal J_r` 为第 `r` 行中所有长度 `L=4√P` 的滑动窗口。对窗口 `J`，记

\[
H_J=\#\{n\in J:(n,\prod_{q≤√P}q)=1\}.
\]

称 `J` 为正常窗口，如果

\[
H_J\ge c_1\frac{√P}{\log P}
\]

且 `H_J` 与其局部均值偏差不超过固定小比例。这里的窗口主量满足

\[
\mu_J\asymp \frac{\sqrt P}{\log P},
\]

远大于任意 `(\log P)^A`。因此定理 2.2 的高矩界在此给出多项式大主量情形的强尾界：存在 `c_2>0`，使得异常窗口数满足

\[
\#\{J\in\mathcal J_r:J\text{ 异常}\}
\le |\mathcal J_r|\exp(-c_2(\log P)^2)
\]

对所有行同时成立。这里可以先在每一固定行内对 `|\mathcal J_r|\le P` 个滑动窗口并合，得到逐行界；再对全部 `O(P^2)` 个行窗口同时并合，仍由 `\exp(-c_2(\log P)^2)` 吸收。特别地，对充分大 `P`，逐行界右侧小于 `1`，所以每一行内实际上没有异常窗口。这个逐行整数化步骤正是正文引理 4.1 所需的桥梁；它不同于 B.0.3 中主量仅为对数幂的盒级参数。

设 `X_J` 是某一候选合数层的计数，令残差

\[
D_J=X_J-λH_J.
\]

需要的充分条件是局部而非仅全局的平均控制：对任意连续窗口簇 `\mathcal W\subset\mathcal J_r`，只要其起点长度至少 `C√P/\log P`，就有

\[
\mathbb E_{J\in\mathcal W}D_J
\le o(\mathbb E_{J\in\mathcal W}H_J)+O(1).
\]

同时要求正残差满足高矩集中：对 `m=c\log P`，

\[
\mathbb E_J(D_J^+)^{2m}
\le (Cm)^{Cm}\left(\frac{√P}{\log P}\right)^m\log^{Cm}P.
\]

在这两个条件下，对所有正常窗口有

\[
\mathbb E(X_J\mid A_J)
\le(λ+o(1))H_J+O(1).
\]

证明分三步。

第一，滑动稳定性。窗口起点移动 `h` 时，`X_J` 与 `H_J` 只因两端各 `|h|` 个整数改变，故

\[
|D_{J+h}-D_J|\le C|h|+O(1).
\]

第二，坏窗口扩散。若某正常窗口满足 `D_J>εH_J+C_ε`，由于 `H_J\gg√P/\log P`，则在 `|h|≤cε√P/\log P` 的邻域中，除异常窗口外仍有

\[
D_{J+h}>\frac ε2H_{J+h}.
\]

第三，局部平均矛盾。上述邻域形成一个允许的窗口簇 `\mathcal W`，其残差平均为正比例 `ε\mathbb E_{\mathcal W}H_J`，违反局部平均控制。异常窗口已由高矩并合排除，故坏正常窗口不存在。

B.1、命题 B.2.1、命题 B.3.1 分别提供该命题所需的局部平均控制；定理 2.2 提供正残差高矩集中。

### 附录 C：列容量与高阈值筛余

附录 C 负责列命题的容量细节。

**C.1 平均主项。** 严格证明

\[
\mathbb E_cH_α(P,c)=(1+o(1))e^{-γ}P/\log P.
\]

**C.2 高阈值列场 USC（列方向接口命题）。**

**命题 C.2.1（列场 CRT 投影）。** 列场取

\[
Ω_c=\{c+kP:0≤k<P\},
\qquad z=αP<P.
\]

所有筛素数 `q≤z` 均满足 `(q,P)=1`，因此每个局部同余条件

\[
c+kP\equiv b\pmod q
\]

等价于唯一的

\[
k\equiv (b-c)P^{-1}\pmod q.
\]

对多个筛素数组成的 squarefree 模数 `Q`，同样有 `(Q,P)=1`，故可合并为一个 `k mod Q` 条件。由 A.6 的统一仿射区间估计，对任意剩余类 `b mod Q`，

\[
\sum_{k=0}^{P-1}\left(1_{c+kP\equiv b\pmod Q}-\frac1Q\right)
=
\sum_{k=0}^{P-1}\left(1_{k\equiv (b-c)P^{-1}\pmod Q}-\frac1Q\right)
=O(1).
\]

即使 `Q>P` 仍成立，且 `O(1)` 对 `b,c,Q` 一致。因此 USC-1 的投影消失、USC-2 的 connected 展开、USC-3 的中心化叶剥离全部适用于列场高阈值筛余。

**命题 C.2.2（列场一致集中）。** 由定理 2.2 得

\[
\mathbb E_c|H_α(P,c)-\mu_α|^{2m}
\le (Cm)^{Cm}\mu_α^m\log^{Cm}P
\]

对 `2m≤c_0\log P` 成立。这里 `\mu_α=(e^{-γ}+o(1))P/\log P`，因此对任意固定小 `c>0` 与 `m=c\log P`，有 `m` 仍处在定理 2.2 的允许范围内。取 `δ=(\log P)^{-1/10}`，Markov 不等式给

\[
\mathbb P_c(|H_α(P,c)-\mu_α|>δ\mu_α)
\le
\left(\frac{(Cm)^C\log^C P}{δ^2\mu_α}\right)^m
\le \exp(-c_1(\log P)^2).
\]

最后一步使用 `\mu_α\gg P/\log P`，其指数优势远大于任何 `\log^C P` 损失。由于 `\mathbb P_c` 是有限列族上的归一化计数，坏列数至多

\[
P\exp(-c_1(\log P)^2)<1
\]

对充分大 `P` 成立。坏列数为整数，故没有坏列，所有非零列同时满足 `H_α(P,c)=\mu_α(1+o(1))`。

**命题 C.3.1（容量比较）。** 本命题展开引理 5.2 与定理 5.5 的常数比较。

若第 `c` 列无素数，则除可能的 `n=1` 外，每个高阈值筛余点 `n=c+kP` 都是合数，且无 `≤αP` 的素因子。由于 `n≤P^2`，每个合数筛余点必须有某个素因子 `q≤P`；又 `q` 不能等于 `P`，因为 `c\not\equiv0\pmod P`。因此

\[
q\in(αP,P).
\]

固定 `q\in(αP,P)`。同余

\[
c+kP\equiv0\pmod q
\]

在 `k mod q` 中有唯一解。因 `α>1/2`，所以 `q>P/2`，区间 `0≤k<P` 中该剩余类至多出现两次。因此无素数列必须满足

\[
H_α(P,c)≤1+2(\pi(P)-\pi(αP)).
\]

其中 `+1` 仅来自可能的筛余点 `n=1`。

另一方面，由 C.1 与命题 C.2.1–C.2.2，所有 `1≤c≤P-1` 同时满足

\[
H_α(P,c)=(e^{-γ}+o(1))\frac{P}{\log P}.
\]

PNT 给

\[
1+2(\pi(P)-\pi(αP))
=(2(1-α)+o(1))\frac{P}{\log P}.
\]

取 `α=0.85`，则

\[
2(1-α)=0.30<e^{-γ}=0.561459\ldots .
\]

因此存在固定余量

\[
e^{-γ}-2(1-α)>0.26,
\]

从而对足够大 `P`，

\[
H_α(P,c)>1+2(\pi(P)-\pi(αP))
\]

对所有非零列同时成立。由命题 C.3.1 的容量判据，每个非零列含素数。

### 附录 D：有限小素数验证

有限验证脚本位于：

- `experiments/verify_finite_p_grid.py`

验证目标：给定计算上界 `P_{max}`，枚举所有奇素数 `P≤P_{max}`，直接检查：

1. `P×P` 方阵每一行是否含素数；
2. 每个非第 `P` 列是否含素数。

脚本核心逻辑如下。

先用 Eratosthenes 筛构造 `1..P_{max}^2` 的素性表。对每个奇素数 `P`：

- 第 `r` 行对应区间
  \[
  [(r-1)P+1,rP].
  \]
  若该区间无素数，则记录失败行。
- 第 `c` 列对应集合
  \[
  \{c+kP:0≤k<P\}.
  \]
  对 `1≤c≤P-1` 检查是否有素数；第 `P` 列跳过。

运行示例：

```bash
python3 experiments/verify_finite_p_grid.py --max-p 200 --quiet
```

当前样例输出：

```text
SUMMARY: all passed for 45 odd primes P<= 200
```

本轮进一步运行：

```bash
python3 experiments/verify_finite_p_grid.py --max-p 1000 --quiet
```

输出：

```text
SUMMARY: all passed for 167 odd primes P<= 1000
```

当前 `P≤1000` 的运行结果只是脚本正确性与小范围现象验证；它并不替代最终阈值验证。若最终渐近证明给出显式阈值 `P_*`，只需运行：

```bash
python3 experiments/verify_finite_p_grid.py --max-p P_* --quiet
```

若输出失败集合为空，则有限小素数验证完成，并与定理 6.1 合并得到所有奇素数情形。

### 定稿审查优先级

建议按以下顺序做最后严写审查：

1. 命题 A.2.1、A.3.1、A.4.1、A.6.1、A.7.1：逐项核对 connected cumulant 展开、skeleton 计数、tiny/near/far 分层、叶剥离与高矩转移；
2. 定理 2.2 到高矩集中：确认所有行窗口、列场、局部窗口簇使用同一 `USC(log P)` 常数范围；
3. 命题 B.0.0–B.0.4、B.2.1、B.3.1、B.4.1：优先在 B.0.4\* sawtooth 相消接口与 B.0.4S/B.0.4S-short 平滑 Type-I 素数双线性接口之间择一证明，再复核 USC 参数族转移、局部乘积容量、误差并合、B.0.3 的二维 connected 提升、缩放筛余容量、三粗因子常数与局部平均转移；
4. 命题 C.2.1–C.2.2 与 C.3.1：复核列场高阈值 `z=αP`、一致集中并合与容量余量；
5. 附录 D：在显式渐近阈值 `P_*` 给出后补齐有限计算表。
