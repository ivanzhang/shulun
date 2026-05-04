# GHLC-D：generic hyperbolic 局部相关的核质量闭合

**状态：** `ghlc_d_closed_by_local_l1_schur_kernel_mass`

本文继续只攻击同一个剩余：

```text
GHLC-D: generic hyperbolic local correlation row-column bound.
```

关键修正是：`GHLC-D` 不能按“点对附近有多少个双曲格点”来硬估计。点态近邻计数会保留
`k_T(0)≈T^2`，从而天然多出一个错误的 `T^2` 因子。正确对象是预迹公式展开后的积分核；
局部双曲球面积为 `≈T^{-2}`，正好抵消核高 `T^2`。因此应使用局部 `L^1` 核质量和 Schur
检验，而不是点态格点计数。

## 1. GHLC-D 的可审查形式

在 `PAR` 与 `FAR` 已剥离后，generic hyperbolic 部分写成

\[
\mathcal R_{\rm hyp}(n,m)
=
\langle \Phi_n,\mathsf K_{\rm hyp}\Phi_m\rangle_{X_Q},
\tag{GHL-1}
\]

其中 `X_Q=Gamma_0(Q)\backslash H`，`\Phi_n,\Phi_m` 是 Poincare 展开中第 `n,m` 个
归一化包，且

\[
\mathsf K_{\rm hyp}(z,w)
=
\sum_{\gamma\in HYP}
\mathcal A(\gamma;z,w)\,
k_T(d(z,\gamma w))\,
1_{d(z,\gamma w)\le r_*},
\qquad
r_*=T^{-1}\log^B y.
\tag{GHL-2}
\]

Clean HLC 的 K1--K6 已把 level、oldform、unit、cusp 数和 dyadic 分裂全部限制为
`\log^{O(1)}y`。因此在本分支中可用

\[
|\mathcal A(\gamma;z,w)|\le \log^{C_0}y
\tag{GHL-3}
\]

作为普通账本，而不是新的解析输入。

Poincare 包的归一化只需下列两条。它们由光滑分块、unfolding 与 K5/K6 的 divisor 账本给出：

\[
\|\Phi_n\|_1\le \log^{C_1}y,\qquad
\sup_{w\in X_Q}\sum_{m\le N_0}|\Phi_m(w)|\le N_0\log^{C_1}y,
\tag{GHL-4}
\]

以及对 `n,m` 互换的同型估计。这里第二式保留了粗的 `N_0` 上界；若使用更精细的有限重叠，
可得到更强估计，但 `GHLC-D` 只需要 `N_0\log^C y`。

## 2. 局部核质量引理

**引理 GHL-L1。** 若 `A>4` 且

\[
|k_T(r)|\ll_A T^2(1+Tr)^{-A},
\tag{GHL-5}
\]

则对任意 `z,w`，

\[
\sup_z\int_{X_Q}|\mathsf K_{\rm hyp}(z,w)|\,d\mu(w)
\ll \log^{C_2}y,
\qquad
\sup_w\int_{X_Q}|\mathsf K_{\rm hyp}(z,w)|\,d\mu(z)
\ll \log^{C_2}y.
\tag{GHL-6}
\]

**证明。**

只证第一式，第二式由 `gamma -> gamma^{-1}` 对称同理。由 `(GHL-2)`、`(GHL-3)` 与非负上界，

\[
\int_{X_Q}|\mathsf K_{\rm hyp}(z,w)|\,d\mu(w)
\le
\log^{C_0}y
\sum_{\gamma\in\Gamma_0(Q)}
\int_{X_Q}
|k_T(d(z,\gamma w))|1_{d(z,\gamma w)\le r_*}\,d\mu(w).
\tag{GHL-7}
\]

对每个 `gamma` 作变量替换 `u=gamma w`。由于双曲测度不变，且 `X_Q` 的 lift 在 `H` 中按
`\Gamma_0(Q)` 平铺，右侧由 unfolding 变为

\[
\log^{C_0}y
\int_{\mathbb H}
|k_T(d(z,u))|1_{d(z,u)\le r_*}\,d\mu(u)
\tag{GHL-8}
\]

再乘上 K5/K6 已记录的 cusp、unit 和 dyadic 多对数重数。用极坐标 `d(z,u)=r`，

\[
\int_{d(z,u)\le r_*}|k_T(d(z,u))|\,d\mu(u)
\ll
T^2\int_0^{r_*}(1+Tr)^{-A}\sinh r\,dr.
\tag{GHL-9}
\]

若 `r_*<=1`，则 `sinh r\ll r`，令 `s=Tr` 得

\[
T^2\int_0^{r_*}(1+Tr)^{-A}r\,dr
=
\int_0^{Tr_*}s(1+s)^{-A}\,ds
\ll_A 1.
\tag{GHL-10}
\]

若 `r_*>1`，则 `T<=\log^B y`。这是低谱参数块，核高本身只有 `T^2<=\log^{2B}y`；
截断到固定半径内的体积为常数，固定半径外已属于 FAR 尾项并由 `(LPC-8)` 吸收。故该低
`T` 情形也只增加多对数损失，不改变 `(GHL-6)`。

所有非几何重数只贡献 `\log^{C_2}y`，得到 `(GHL-6)`。证毕。

## 3. Schur 行列和闭合

**命题 GHL-Schur。** `(GHL-1)`--`(GHL-6)` 推出 `GHLC-D`：

\[
\sum_{m\le N_0}|\mathcal R_{\rm hyp}(n,m)|\ll N_0\log^C y,
\qquad
\sum_{n\le N_0}|\mathcal R_{\rm hyp}(n,m)|\ll N_0\log^C y.
\tag{GHL-11}
\]

**证明。**

由 `(GHL-1)` 和三角不等式，

\[
\sum_{m\le N_0}|\mathcal R_{\rm hyp}(n,m)|
\le
\int_{X_Q}|\Phi_n(z)|
\int_{X_Q}|\mathsf K_{\rm hyp}(z,w)|
\sum_{m\le N_0}|\Phi_m(w)|\,d\mu(w)d\mu(z).
\tag{GHL-12}
\]

先用 `(GHL-4)` 控制 `m` 包总重，再用 `(GHL-6)` 控制核的 `w` 积分，最后用
`\|\Phi_n\|_1<=\log^{C_1}y`，得到

\[
\sum_{m\le N_0}|\mathcal R_{\rm hyp}(n,m)|
\ll
N_0\log^{C_1+C_2+C_3}y.
\tag{GHL-13}
\]

列和同理，只需把 `(GHL-12)` 中 `n,m` 互换，并使用 `(GHL-4)` 的对偶版本。证毕。

## 4. 与矩阵近距离条件的关系

此前建议把近距离条件写成

\[
|a z_m+b-z_n(cz_m+d)|\ll r_*\sqrt{\Im z_m\,\Im z_n}.
\tag{GHL-14}
\]

这是正确的局部几何恒等式，但它只适合做格点离散性审查；若直接点态求和，会丢失
局部面积 `T^{-2}` 对 `T^2` 核高的抵消。本文的证明保留 `(GHL-14)` 作为 sanity check：
`FAR/ID/PAR/HYP` 的几何分解仍由它识别；真正的行列和上界则由 `(GHL-9)` 的局部核质量给出。

这也解释了为什么 `GHLC-D` 不需要新的 Kloosterman 抵消：在 `PTK-D` 的空间侧，generic
hyperbolic 近邻不是谱大筛的深抵消来源，而是预迹核的局部质量账本。深抵消仍位于更上游
`KZ-B` 与 `KZ-E`，即 trace formula 正规化和 well-factorable dispersion 对数节省。

## 5. 闭合结论

本文闭合：

```text
GHLC-D
=> LPC-D
=> PTK-D
=> KZ-D.
```

严格边界如下：

1. `GHLC-D` 不再是当前未闭合核心；
2. `KZ-D` 的 spectral large sieve 分支在本文脊柱中闭合到预迹核层；
3. 完全自足无黑箱总链仍不能宣称闭合，因为 `KZ-B` 与 `KZ-E` 尚未逐行内联证明；
4. 若主稿中 `\Phi_n` 的 Poincare 包定义尚未显式插入，需把 `(GHL-4)` 作为普通归一化引理
   放入预迹/Poincare 展开章节，但它不是新的深外部定理。
