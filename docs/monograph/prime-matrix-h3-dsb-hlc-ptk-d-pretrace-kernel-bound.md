# PTK-D：预迹核上界到空间侧格点计数的归约

**状态：** `ptk_d_closed_after_lpc_d_local_schur_closure`

本文继续只攻击同一个剩余：

```text
PTK-D: pretrace kernel bound.
```

上一层已经证明 `PTK-D=>KZ-D`。本文把 PTK-D 再压缩：预迹核上界只剩一个空间侧
`LPC-D`（lattice-point/correlation）行列和上界。本文完成从 `LPC-D` 到 `PTK-D` 的证明，
并内联测试函数与 Schur 账本。后续
`docs/monograph/prime-matrix-h3-dsb-hlc-lpc-d-spatial-correlation-split.md` 与
`docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md` 已闭合 LPC-D 的
FAR/ID/PAR/HYP 四分支，因此 PTK-D 在本文脊柱中闭合。

## 1. PTK-D 目标

谱投影核为

\[
K_T(n,m)=\int_{\Omega_T}\rho_\omega(n)\overline{\rho_\omega(m)}\,d\mu(\omega).
\tag{PTK-1}
\]

PTK-D 要证明

\[
K_T(n,m)=\delta_{n=m}\mathcal W_T+\mathcal O_T(n,m),
\quad
\mathcal W_T\ll T^2\log^{C}y,
\tag{PTK-2}
\]

以及

\[
\sum_{m\le N_0}|\mathcal O_T(n,m)|\ll N_0\log^{C}y,
\qquad
\sum_{n\le N_0}|\mathcal O_T(n,m)|\ll N_0\log^{C}y.
\tag{PTK-3}
\]

## 2. 谱截断测试函数

取偶函数 `h_T(t)`，满足：

1. `h_T(t)>=1` for `|t|<=T`；
2. `h_T(t)>=0`；
3. `h_T(t)\ll_A (1+|t|/T)^{-A}`；
4. Selberg/Harish-Chandra 逆变换 `k_T(u)` 满足
   \[
   |k_T(u)|\ll_A T^2(1+T\,d(u,0))^{-A}.
   \tag{PTK-4}
   \]

这里 `u` 是双曲距离变量。该测试函数可由固定 Schwartz 函数缩放和自卷积构造；正性来自
自卷积，衰减来自 Fourier/Selberg transform 的反复分部积分。该构造与 KZ-C 的 Bessel
transform 衰减同型，不是新的深谱输入。

用 `h_T` majorize sharp cutoff 后，只需证明平滑谱核上界；sharp cutoff 损失并入多对数。

## 3. 预迹公式的空间侧

对 level `Q` 的谱投影核，预迹公式给出

\[
K_T(z,w)
=
\sum_{\gamma\in\Gamma_0(Q)}
k_T(u(z,\gamma w))
\tag{PTK-5}
\]

加上可显式处理的 Eisenstein/continuous normalization 项。oldform 与 holomorphic 项已在
KZ-D 文档中归入多对数账本。

把 Fourier 系数核 `K_T(n,m)` 表示为 Poincare 系数：

\[
K_T(n,m)
=
\langle P_n,\,\Pi_T P_m\rangle,
\tag{PTK-6}
\]

其中 `P_n` 是第 `n` 个 Poincare series，`\Pi_T` 是由 `h_T` 定义的平滑谱投影。
代入 `(PTK-5)` 后得到空间侧相关核

\[
K_T(n,m)
=
\mathcal D_T(n,m)+\mathcal R_T(n,m),
\tag{PTK-7}
\]

其中 `\mathcal D_T` 来自 identity/parabolic diagonal，`\mathcal R_T` 来自非平凡
`\gamma`。

## 4. 对角项

Poincare series 的 identity 项给出

\[
\mathcal D_T(n,m)=\delta_{n=m}\mathcal W_T+O_A(y^{-A}),
\tag{PTK-8}
\]

且由局部 Weyl 体积项与 `h_T` 支撑

\[
\mathcal W_T\ll T^2\log^{C_1}y.
\tag{PTK-9}
\]

这里 `log^{C_1}y` 包括 level cusp 数、归一化常数和 oldform 分裂数。K5/K6 保证这些数量在
clean HLC 账本中为多对数。

## 5. 空间侧剩余 LPC-D

**LPC-D（lattice-point/correlation bound）。** 对非平凡空间侧核 `\mathcal R_T(n,m)`，
成立行列 Schur 上界：

\[
\sum_{m\le N_0}|\mathcal R_T(n,m)|
\ll N_0\log^{C_2}y,
\qquad
\sum_{n\le N_0}|\mathcal R_T(n,m)|
\ll N_0\log^{C_2}y.
\tag{PTK-10}
\]

展开 `\mathcal R_T` 后，`(PTK-10)` 是一个空间侧格点/相关计数命题：

\[
\sum_{m\le N_0}
\left|
\sum_{\gamma\ne 1}
\mathcal A_{n,m}(\gamma)\,k_T(u(z_n,\gamma z_m))
\right|
\ll N_0\log^{C_2}y.
\tag{PTK-11}
\]

其中 `\mathcal A_{n,m}(\gamma)` 是 Poincare 展开产生的振荡/归一化权。`k_T` 的快速衰减把
有效 `\gamma` 限制到双曲距离 `\ll T^{-1}\log^B y` 的管状邻域；远距离项由 `(PTK-4)`
直接给 `O_A(y^{-A})`。

`LPC-D` 曾是 PTK-D 的真正空间侧硬点。它由以下三类估计证明：

```text
local lattice counting in hyperbolic balls;
oscillatory cancellation in the Poincare coefficient phase;
cusp/parabolic sector separation.
```

其中 FAR、ID、PAR 在 LPC-D 分解文件中处理；generic hyperbolic 近邻由局部核质量
`L^1`--Schur 检验处理。关键是对积分核使用
`T^2\int_0^{T^{-1}\log^B y}(1+Tr)^{-A}\sinh r\,dr=O(1)`，而不是点态近邻计数。

## 6. `LPC-D => PTK-D`

**命题。** 若 LPC-D 成立，则 PTK-D 成立。

**证明。**

1. 用第 2 节的 `h_T` 平滑 sharp spectral cutoff，得到平滑核 `K_T`；majorant 只放大左侧。
2. 由预迹公式和 Poincare 系数展开，得到 `(PTK-7)`。
3. 由第 4 节，对角项满足 `(PTK-8)`--`(PTK-9)`。
4. 非对角项 `\mathcal R_T` 的行列和由 LPC-D 即 `(PTK-10)` 控制。
5. 因此 `K_T(n,m)` 满足 `(PTK-2)`--`(PTK-3)`。

证毕。

## 7. 当前闭合度

本文完成：

1. 谱截断测试函数的正性/衰减接口；
2. 预迹公式到 Poincare 系数核的结构展开；
3. 对角 `T^2` 体积项账本；
4. `LPC-D=>PTK-D` 的逐行证明。

本文接入后续 LPC/GHLC 文件后还完成：

```text
LPC-D: spatial lattice-point/correlation Schur row-column bound (PTK-10).
```

下一步若继续完全自足无黑箱硬攻，不应再停留在 PTK-D/LPC-D；剩余应回到
`Kuznetsov-LS` 原子中的 `KZ-B` trace formula 正规化与 `KZ-E` well-factorable dispersion
对数节省。

进一步压缩见 `docs/monograph/prime-matrix-h3-dsb-hlc-lpc-d-spatial-correlation-split.md`。
该文完成 FAR 远距离尾项、ID-near 和 PAR cusp/parabolic 分支，并证明 `GHLC-D=>LPC-D`。
再由 `docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md` 闭合 `GHLC-D`。
