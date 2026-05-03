# RPD 第一锚粗互补因子恒等式

**状态：** `rpd_composite_side_exactly_first_anchor_rough_cofactor_count`

本文补正并强化 `ASB/RPD` 预算链：粗合数侧不需要先拆成半素数与 `M_{\ge3}`，也不需要把半素数互补素数项和第二锚尾项相加。全部粗合数可由第一锚粗互补因子一次性精确计数。

## 1. 设置

固定 ASB 窗口

\[
J=[L,R]\subset[1,p^2],
\qquad z=p^\alpha.
\]

令

\[
R_z(J)=\{n\in J:(n,P(z))=1\},
\]

并记粗合数集合

\[
C_z(J)=R_z(J)\setminus\mathbb P.
\]

## 2. 第一锚恒等式

对每个 `n\in C_z(J)`，令

\[
a=P^-(n),\qquad c={n\over a}.
\]

因为 `n` 是 `z`-rough 合数，所以

\[
z<a\le \sqrt n\le p,
\qquad P^-(c)\ge a,
\qquad c\ge a.
\]

且 `n\in[L,R]` 等价于

\[
\max(a,\lceil L/a\rceil)\le c\le \lfloor R/a\rfloor.
\]

反过来，若 `a` 为素数、`z<a\le p`，且整数 `c` 满足

\[
\max(a,\lceil L/a\rceil)\le c\le \lfloor R/a\rfloor,
\qquad P^-(c)\ge a,
\]

则 `n=ac` 属于 `J`，没有不超过 `z` 的素因子，并且是合数，故 `n\in C_z(J)`。

映射 `n -> (a,c)` 由最小素因子唯一确定，因此得到精确恒等式

\[
|C_z(J)|
=
\sum_{\substack{z<a\le p\\ a\in\mathbb P}}
\#\left\{
c:
\max(a,\lceil L/a\rceil)\le c\le \lfloor R/a\rfloor,\quad
P^-(c)\ge a
\right\}.
\tag{FAC}
\]

这条恒等式同时包含：

- `c` 为素数的半素数项；
- `c` 为合数的 `M_{\ge3}` 项；
- 重复因子情形，如 `a^2` 或 `a^2b`，因为条件是 `P^-(c)\ge a` 而不是 `>a`。

## 3. 对旧链条的改进

旧链条写成

```text
semiprime prime-cofactor interval bound
+ M>=3 second-anchor tail bound
```

这在证明上容易出现重复预算：用 `rough` 上界包住“互补素数”时，已经把复合互补因子也算入；再额外加 `M_{\ge3}` 会双计数。

`(FAC)` 直接给出正确对象：

```text
all rough composites
= first-anchor rough cofactor count.
```

因此 `RPD` 等价于

\[
\sum_{z<a\le p}
\#\{c\in I_a(J):P^-(c)\ge a\}
\le (1-\eta)|R_z(J)|.
\tag{RPD-FAC}
\]

而不是半素数预算加多因子预算。

## 4. 加权区间筛版本

把锚 `a` 按层 `A_\nu\le a<A_{\nu+1}` 分组，并使用共同小素乘积

\[
P_{<A_\nu}=\prod_{\ell<A_\nu}\ell.
\]

由于 `a\ge A_\nu` 且 `P^-(c)\ge a`，有

\[
1_{P^-(c)\ge a}\le 1_{(c,P_{<A_\nu})=1}.
\]

所以 `(FAC)` 可由分层加权区间筛上界控制：

\[
|C_z(J)|
\le
\sum_\nu
\sum_{(c,P_{<A_\nu})=1}w_\nu(c),
\]

其中

\[
w_\nu(c)=
\#\{a\in[A_\nu,A_{\nu+1})\cap\mathbb P:
c\in I_a(J)\}.
\]

对每层套用有限 Selberg 二次型，得到

\[
|C_z(J)|
\le
\sum_\nu X_\nu\Lambda_{A_\nu}(\xi_\nu)+E_{\rm lowmod}(J).
\tag{FAC-Selberg}
\]

若 `(FAC-Selberg)` 小于 `(1-\eta)R_z^-(J)`，则 `RPD` 成立。若失败，则失败只能来自：

1. 第一锚粗互补因子在低模上端点缺陷过大；
2. 低筛粗剩余下界 `R_z^-(J)` 过弱；
3. 上述低模缺陷触发 `CRTDefect/Tail-anchor/OSPC`。

## 5. 审稿结论

`(FAC)` 是当前 ASB/RPD 链条中最重要的结构化简：它把半素数、三因子、singleton 走廊全部统一为第一锚粗互补因子恒等式。后续数值化应优先计算 `(FAC-Selberg)`，而不是分别给半素数和 `M_{\ge3}` 配预算。

## 6. 审计核查

审计脚本 `experiments/prime_matrix_rpd_first_anchor_identity_audit.py` 与报告
`docs/monograph/prime-matrix-rpd-first-anchor-identity-audit.md` 给出 `max_p=2000`、`alpha=0.43`、后排 `25%`、最坏 `40` 个窗口的核查：

- 低筛粗剩余：`2002`。
- 粗素数：`548`。
- 粗合数：`1454`。
- 第一锚整数容量：`7086`。
- 第一锚粗互补因子：`1454`。
- 恒等式差：`0`。

这验证了 `(FAC)` 在压力窗口上的精确性，并暴露下一步真正数值化对象：不是 `semiprime + M_{\ge3}` 两套预算，而是第一锚 rough cofactor 的同权 Selberg 预算。

## 7. FAC 模型预算核查

进一步审计见 `experiments/prime_matrix_rpd_fac_budget_audit.py` 与
`docs/monograph/prime-matrix-rpd-fac-budget-audit.md`。同一批压力窗口中，

- Mertens 模型量 `sum cap(I_a) V(<a)` 为 `1075.256057`。
- 全局所需常数为 `1454/1075.256057=1.352236`。
- 对 `eta=0.10`，全局允许常数为 `1.675694`；对 `eta=0.18`，全局允许常数为 `1.526743`。
- 逐窗口最大所需常数出现在 `p=53,q_row=43`，为 `1.695703`。
- 逐窗口最小允许常数分别为 `1.570917` 与 `1.431280`。

因此该模型审计给出两个结论：

```text
全局平均有余量；
单一 FAC 常数逐窗口不够，必须加入分层/端点修正或低模缺陷出口。
```

这把下一步硬点精确化为：证明分层同权 Selberg 常数与端点误差在每个窗口内低于允许常数；若失败，则必须从失败项中抽取加权低模端点缺陷，并接入 `CRTDefect/Tail-anchor/OSPC`。

## 8. 低模端点缺陷定位

新增 `experiments/prime_matrix_rpd_fac_lowmod_defect_audit.py` 与
`docs/monograph/prime-matrix-rpd-fac-lowmod-defect-audit.md` 进一步把 FAC 尖峰写成截断低模缺陷账本：

\[
D_T(J)=
\sum_{z<a\le p}
\left(
\#\{c\in I_a(J):(c,\prod_{\ell<\min(a,T)}\ell)=1\}
-|I_a(J)|V(<\min(a,T))
\right).
\]

同批 `40` 个压力窗口全部为 FAC 正缺陷窗口。最尖峰窗口 `p=53,q_row=43,J=[2479,2537]` 中，

- FAC 缺陷为 `5.333565`。
- `T=7` 已捕获 `72.4969%`。
- `T=13` 已捕获 `84.9151%`。
- `T=17` 已捕获 `90.9089%`。

这说明最大尖峰不是高层随机黑箱，而是很早就在低模端点账本中显现。下一步最小义务相应变成：

```text
large D_T for small T
=> CRT low-mod endpoint defect
=> CRTDefect/Tail-anchor/OSPC.
```
