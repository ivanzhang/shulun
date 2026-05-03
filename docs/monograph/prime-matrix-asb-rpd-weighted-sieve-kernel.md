# ASB/RPD 加权区间筛闭合内核

**状态：** `asb_rpd_reduced_to_weighted_interval_sieve_budget_or_low_mod_defect`

本文继续硬攻完整 `ASB/RPD` 链条。目标不是把未证输入包装成结论，而是把粗合数侧统一写成第一锚粗互补因子恒等式，再用有限加权 Selberg 二次型预算控制，并明确失败时必须输出的低模缺陷。

## 1. 反例与确定分解

固定 ASB 采样窗口

\[
J=[L,R],\qquad |J|\asymp p,
\]

并取

\[
z=p^\alpha,\qquad e^{-1}<\alpha<1/2.
\]

令

\[
R_z(J)=\{n\in J:(n,P(z))=1\}.
\]

在 `J\subset[1,p^2]` 中，每个 `n\in R_z(J)` 若不是素数，则其全部素因子都大于 `z`，且至少一个素因子不超过 `p`。因此有确定分解

\[
|R_z(J)|
=
P_z(J)+S_z(J)+M_{\ge3}(J),
\tag{1}
\]

其中 `P_z(J)=|R_z(J)\cap\mathbb P|`，`S_z(J)` 是两个粗素因子的半素数项，`M_{\ge3}(J)` 是至少三个粗素因子的项。

`RPD` 等价于存在固定 `\eta>0` 使

\[
P_z(J)\ge \eta |R_z(J)|.
\tag{2}
\]

由 `(1)`，只需证明

\[
S_z(J)+M_{\ge3}(J)\le (1-\eta)|R_z(J)|.
\tag{3}
\]

后文用第一锚恒等式把 `(3)` 的左侧统一成一个加权区间筛上界。

## 2. 加权区间 Selberg 引理

设有一族整数区间

\[
\mathcal I=\{I_j=[A_j,B_j]\cap\mathbb Z\}_{j\in\mathcal J},
\]

并给每个区间赋同一个筛层 `y`。本节采用严格小于层下端的小素乘积

\[
P_{<y}=\prod_{\ell<y}\ell ,
\]

以避免锚端点本身被筛掉。定义权函数

\[
w(n)=\#\{j:n\in I_j\},\qquad
X=\sum_n w(n).
\]

对平方自由 `r|P_{<y}`，令

\[
A(r)=\sum_{r\mid n}w(n),\qquad
\rho(r)=A(r)-{X\over r}.
\]

若 `K=|\mathcal J|`，则每个区间对模 `r` 的端点误差至多为 `1`，故

\[
|\rho(r)|\le K.
\tag{4}
\]

对任意 Selberg 权 `\lambda_d`，支撑在 `d|P_{<y}, d<\xi` 且 `\lambda_1=1`，有

\[
\sum_{(n,P_{<y})=1}w(n)
\le
XQ_y(\lambda;\xi)+E_{\mathcal I,y}(\lambda;\xi),
\tag{5}
\]

其中

\[
Q_y(\lambda;\xi)=
\sum_{\substack{d,e<\xi\\d,e\mid P_{<y}}}{\lambda_d\lambda_e\over[d,e]},
\]

\[
E_{\mathcal I,y}(\lambda;\xi)=
\sum_{\substack{d,e<\xi\\d,e\mid P_{<y}}}\lambda_d\lambda_e\rho([d,e]).
\]

取最小化权 `\lambda^\ast` 后，

\[
\sum_{(n,P_{<y})=1}w(n)
\le X\Lambda_y(\xi)+E_{\mathcal I,y}(\lambda^\ast;\xi).
\tag{WIS}
\]

若端点误差不能进入预算，则由 `(5)` 必有加权低模缺陷

\[
\sum_{r<\xi^2,\ r\mid P_{<y}}
\beta_r(\lambda^\ast)|\rho(r)|
\]

超预算，其中

\[
\beta_r(\lambda^\ast)=
\sum_{\substack{d,e<\xi\\[d,e]=r}}|\lambda_d^\ast\lambda_e^\ast|.
\]

因此每个加权区间筛估计都有严格二分：

```text
WIS 主项和端点误差进入预算
or
weighted low-mod endpoint defect => CRTDefect/Tail-anchor/OSPC.
```

## 3. 第一锚粗互补因子恒等式

对每个 `n\in R_z(J)\setminus\mathbb P`，令 `a=P^-(n)`，`c=n/a`。则

\[
z<a\le p,\qquad P^-(c)\ge a,\qquad
\max(a,\lceil L/a\rceil)\le c\le\lfloor R/a\rfloor.
\]

反过来，任意满足这些条件的 `(a,c)` 都给出一个 `R_z(J)` 中的合数。由最小素因子唯一性，

\[
S_z(J)+M_{\ge3}(J)
=
\sum_{\substack{z<a\le p\\a\in\mathbb P}}
\#\{c\in I_a(J):P^-(c)\ge a\}.
\tag{FAC}
\]

这一步是对旧链条的关键修正：半素数互补素数和 `M_{\ge3}` 不应分别加粗预算。若用 rough 上界包住互补素数，复合互补因子已经被包含；再另加第二锚尾预算会双计数。`(FAC)` 直接计数全部粗合数，既含半素数也含多因子。

## 4. 第一锚加权区间筛

固定锚层

\[
A_\nu\le a<A_{\nu+1},
\]

取公共筛层 `y_\nu=A_\nu`，并筛去所有 `<A_\nu` 的小素数。对每个锚 `a`，互补因子区间为

\[
I_a(J)=
\left[
\max(a,\lceil L/a\rceil),
\lfloor R/a\rfloor
\right]\cap\mathbb Z.
\]

若 `P^-(c)\ge a` 且 `a\ge A_\nu`，则

\[
1_{P^-(c)\ge a}\le 1_{(c,P_{<A_\nu})=1}.
\]

于是该锚层粗合数贡献满足

\[
\sum_{a\in[A_\nu,A_{\nu+1})}
\#\{c\in I_a(J):P^-(c)\ge a\}
\le
\sum_{(c,P_{<A_\nu})=1}w_\nu(c),
\tag{6}
\]

其中 `w_\nu(c)=#\{a\in[A_\nu,A_{\nu+1}):c\in I_a(J)\}`。

对 `(6)` 套用 `(WIS)`，得到

\[
\sum_{a\in[A_\nu,A_{\nu+1})}
\#\{c\in I_a(J):P^-(c)\ge a\}
\le
X_\nu\Lambda_{y_\nu}(\xi_\nu)+E_\nu.
\tag{7}
\]

这把旧的两项输入统一为：

```text
first-anchor rough-cofactor weighted interval sieve budget
or first-anchor low-mod endpoint defect.
```

注意这里没有使用“短区间必有素数”。我们只需要粗互补因子集合被共同小素层 rough 上界包住，因此这是上界筛，避开了下界筛的 parity 障碍。

## 5. ASB/RPD 主预算不等式

设 `\mathcal A` 为锚层集合。由 `(FAC)` 与 `(7)`，得到可审稿的复合上界

\[
S_z(J)+M_{\ge3}(J)
\le
U_{\rm FAC}(J)+E_{\rm lowmod}(J),
\tag{8}
\]

其中

\[
U_{\rm FAC}(J)=
\sum_{\nu\in\mathcal A}
X_\nu\Lambda_{y_\nu}(\xi_\nu),
\]

`E_lowmod` 是所有同权端点缺陷能量。singleton 走廊与第二锚尾段不再是主预算的必要分支；它们只作为诊断某些第一锚层为何尖峰的局部工具。

因此完整 `RPD` 可由下面的单一预算闭合：

\[
U_{\rm FAC}(J)+E_{\rm lowmod}(J)
\le
(1-\eta)R_z^-(J),
\tag{RPD-Budget}
\]

其中 `R_z^-(J)` 是低筛粗剩余的下界预算。

若 `(RPD-Budget)` 成立，则由 `(1)--(3)` 得到 `RPD`，从而排除 `ASB-Fail`。若失败，则失败不能再笼统称为“素数短区间异常”，而必须落入下列出口之一：

1. 低筛粗剩余下界不足，即 `R_z^-(J)` 的端点缺陷异常；
2. 第一锚粗互补因子加权端点缺陷异常；
3. 上述异常合成后触发 `CRTDefect/Tail-anchor/OSPC`。

## 6. 对完整闭合的影响

本轮推进把 ASB/RPD 的剩余结构压缩为：

```text
first-anchor weighted rough-cofactor budget
versus
lower rough-residue budget
or weighted low-mod defect exits.
```

这比先前的

```text
prime-cofactor interval bound
+ M>=3 second-anchor Mertens envelope
```

更窄：两者不应相加；它们是同一个第一锚粗互补因子恒等式的不同投影。

## 7. 仍未闭合的最后硬点

必须诚实保留两个独立义务：

1. **数值化同权预算。** 需要为实际第一锚层选择 `y_\nu,\xi_\nu`，把 `(RPD-Budget)` 的所有 `Λ`、端点项和 `R_z^-` 放在同一 convention 下核算。
2. **缺陷出口排斥。** 若 `E_lowmod` 超预算，必须证明该低模端点缺陷确实触发 `CRTDefect/Tail-anchor/OSPC`，并被前文矛盾场刚性排除。

在这两项完成前，不能宣称 `ASB/RPD` 已无条件闭合。但当前最小硬点已经从多个分散输入压缩为一个可计算、可审稿的同权预算不等式。

## 8. FAC 常数审计后的硬点再压缩

新增 `docs/monograph/prime-matrix-rpd-fac-budget-audit.md` 对同批压力窗口计算

\[
U_{\rm FAC}^{\rm model}(J)=
\sum_{z<a\le p}{\rm cap}(I_a(J))
\prod_{\ell<a}\left(1-{1\over\ell}\right).
\]

审计结果为：

- 粗合数与 FAC 真实 rough 互补因子同为 `1454`，恒等式差 `0`。
- 全局模型量为 `1075.256057`，全局所需常数 `C=1.352236`。
- 对 `eta=0.10` 与 `eta=0.18`，全局允许常数分别为 `1.675694` 与 `1.526743`。
- 逐窗口最大所需常数为 `1.695703`，而逐窗口最小允许常数分别为 `1.570917` 与 `1.431280`。

所以不能用一个裸全局 `C_FAC` 常数直接证明所有窗口。当前最小闭合目标应改写为更严格的二分：

```text
分层/端点修正 FAC-Selberg 预算逐窗口进入余量
or
超预算窗口产生加权低模端点缺陷
=> CRTDefect/Tail-anchor/OSPC.
```

这一步没有闭合 `ASB/RPD`，但排除了一个错误方向：仅凭全局 Mertens 放大常数不足以完成证明；必须利用窗口端点、锚层分布和 CRT 低模缺陷出口。

## 9. 低模缺陷出口的可计算形式

新增 `docs/monograph/prime-matrix-rpd-fac-lowmod-defect-audit.md` 把超预算项写成

\[
D_T(J)=
\sum_{z<a\le p}
\left(
\#\{c\in I_a(J):(c,\prod_{\ell<\min(a,T)}\ell)=1\}
-|I_a(J)|V(<\min(a,T))
\right).
\]

这是 `(WIS)` 中 `E_{\mathcal I,y}` 的低模截断影子：若 `D_T` 在小 `T` 已经接近最终 FAC 缺陷，则失败来源不是高锚层平均常数，而是短区间端点在小 CRT 模数上的偏置。

审计显示最尖峰窗口 `p=53,q_row=43` 的最终 FAC 缺陷为 `5.333565`；`T=13` 捕获 `84.9151%`，`T=17` 捕获 `90.9089%`。在 `40` 个压力窗口中，`T=101` 的最小捕获率已经达到 `80.4688%`，平均捕获率 `95.9096%`。

因此当前闭合接口可进一步写为：

```text
FAC 尖峰
=> small/medium low-mod endpoint defect D_T
=> CRTDefect/Tail-anchor/OSPC
or finer layered Selberg absorption.
```

剩余未证的是最后一箭头：必须把大的 `D_T` 严格翻译为已有矛盾场中的有向低模集中，而不能仅以数值相关性替代证明。
