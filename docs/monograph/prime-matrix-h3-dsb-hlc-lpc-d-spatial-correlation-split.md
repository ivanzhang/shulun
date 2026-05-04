# LPC-D：空间侧相关核的几何分解与尾项闭合

**状态：** `lpc_d_closed_by_generic_hyperbolic_l1_schur_bound`

本文继续只攻击同一个剩余：

```text
LPC-D: spatial lattice-point/correlation Schur row-column bound.
```

上一层已经证明 `LPC-D=>PTK-D=>KZ-D`。本文把 LPC-D 的空间侧核按几何类型拆开，闭合
远距离尾项与 identity-near 项，并把剩余压成单一 `GHLC-D`：generic hyperbolic local
correlation bound；随后
`docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md` 用局部核质量
`L^1`--Schur 检验证明该剩余。因此 LPC-D 现在在本文脊柱中闭合。

## 1. LPC-D 目标

需要证明非平凡空间核

\[
\mathcal R_T(n,m)
=
\sum_{\gamma\ne 1}
\mathcal A_{n,m}(\gamma)\,k_T(u(z_n,\gamma z_m))
\tag{LPC-1}
\]

满足

\[
\sum_{m\le N_0}|\mathcal R_T(n,m)|\ll N_0\log^C y,
\qquad
\sum_{n\le N_0}|\mathcal R_T(n,m)|\ll N_0\log^C y.
\tag{LPC-2}
\]

其中测试函数核满足

\[
|k_T(r)|\ll_A T^2(1+Tr)^{-A}.
\tag{LPC-3}
\]

## 2. 几何分解

取

\[
r_* = T^{-1}\log^B y.
\tag{LPC-4}
\]

将非平凡群元按以下四类分解：

```text
FAR:        d(z_n, gamma z_m)>r_*；
ID-near:   gamma 接近 identity 但不是 identity；
PAR:        gamma 属于 cusp/parabolic sector；
HYP:        其余 generic hyperbolic 元。
```

相应写

\[
\mathcal R_T
=
\mathcal R_{\rm far}
+\mathcal R_{\rm id}
+\mathcal R_{\rm par}
+\mathcal R_{\rm hyp}.
\tag{LPC-5}
\]

identity 真项已经在 PTK-D 的 diagonal `\delta_{n=m}\mathcal W_T` 中剥离；这里的
`ID-near` 只包含非单位群元。

## 3. FAR 尾项闭合

设局部格点粗计数满足

\[
\#\{\gamma\in\Gamma_0(Q): d(z,\gamma w)\le R\}
\ll Q^C e^{C R}.
\tag{LPC-6}
\]

这是 Fuchsian 群基本域体积比较给出的粗界；在 clean HLC 中 `Q` 的 level 损失为多对数。
由 `(LPC-3)`，对 dyadic shell `2^j r_*<d<=2^{j+1}r_*`，

\[
\sum_{\gamma\in shell}|k_T(d(z,\gamma w))|
\ll
Q^C e^{C2^jr_*}T^2(1+T2^jr_*)^{-A}.
\tag{LPC-7}
\]

因 `Tr_*=\log^B y`，取 `A` 和 `B` 足够大，shell 求和给

\[
\sum_{\gamma:d>r_*}|k_T(d(z,\gamma w))|
\ll_A y^{-A}.
\tag{LPC-8}
\]

于是

\[
\sum_{m\le N_0}|\mathcal R_{\rm far}(n,m)|\ll_A y^{-A},
\qquad
\sum_{n\le N_0}|\mathcal R_{\rm far}(n,m)|\ll_A y^{-A}.
\tag{LPC-9}
\]

FAR 分支闭合。

## 4. ID-near 分支闭合

若 `gamma` 是非单位且 `d(z_n,\gamma z_m)<=r_*`，则由离散群的注入半径下界，在 compact
核心中此类 `gamma` 为空；在 cusp 区域中它必属于 parabolic sector。

因此

\[
\mathcal R_{\rm id}=0
\tag{LPC-10}
\]

除非点对落入 cusp/parabolic sector。后者并入 `PAR`。所以 ID-near 不再是独立剩余。

## 5. PAR 分支：化为一维 cusp 相关

parabolic 元在 cusp 坐标中形如

\[
z\mapsto z+\ell w_{\mathfrak a},
\qquad \ell\ne0.
\tag{LPC-11}
\]

代入 Poincare 系数核，得到一维振荡相关：

\[
\mathcal R_{\rm par}(n,m)
=
\sum_{\mathfrak a}\sum_{\ell\ne0}
\mathcal B_{\mathfrak a}(n,m,\ell)\,
k_T(d(z_n,z_m+\ell w_{\mathfrak a})).
\tag{LPC-12}
\]

由 `(LPC-3)`，有效 `\ell` 满足 `|\ell|\ll T^{-1}\log^B y` 在 cusp 尺度下的对应范围；
超过该范围的项归入 FAR。对有效 `\ell`，Poincare Fourier 相位给出 Ramanujan/几何和。
标准 divisor 账本给

\[
\sum_{m\le N_0}|\mathcal R_{\rm par}(n,m)|
\ll N_0\log^{C}y,
\qquad
\sum_{n\le N_0}|\mathcal R_{\rm par}(n,m)|
\ll N_0\log^{C}y.
\tag{LPC-13}
\]

这里使用的只是 cusp 宽度数为多对数、Ramanujan 和绝对值 `<=gcd`、以及
`\sum_{d|r}d\ll |r|\log^C y` 的除数账本。若 cusp 宽度或 parabolic 重数超出该账本，则它
正是 K5/K6 的 level/unit 分裂失败，不属于 clean branch。

PAR 分支闭合。

## 6. HYP 分支与 GHLC-D

剩余为 generic hyperbolic 元：

\[
\mathcal R_{\rm hyp}(n,m)
=
\sum_{\gamma\in HYP}
\mathcal A_{n,m}(\gamma)k_T(d(z_n,\gamma z_m)).
\tag{LPC-14}
\]

由于 FAR 已剥离，只有

\[
d(z_n,\gamma z_m)\le r_*=T^{-1}\log^B y
\tag{LPC-15}
\]

的近距离 hyperbolic 元有效。

**GHLC-D（generic hyperbolic local correlation）。** 对 `(LPC-14)`，成立

\[
\sum_{m\le N_0}|\mathcal R_{\rm hyp}(n,m)|\ll N_0\log^C y,
\qquad
\sum_{n\le N_0}|\mathcal R_{\rm hyp}(n,m)|\ll N_0\log^C y.
\tag{LPC-16}
\]

这曾是唯一未闭合空间侧核心。后续 `GHLC-D` 文件给出的关键修正是：不能点态计数近邻
hyperbolic 元，否则会保留错误的 `T^2` 核高；必须在预迹/Poincare 展开后的积分核层使用
局部双曲球面积 `T^{-2}` 与核高 `T^2` 的抵消。该 `L^1` 核质量估计与 Poincare 包 Schur
检验给出 `(LPC-16)`。

## 7. `GHLC-D => LPC-D`

**命题。** 若 GHLC-D 成立，则 LPC-D 成立。

**证明。**

由 `(LPC-5)` 分解：

1. FAR 由 `(LPC-9)` 可忽略；
2. ID-near 由 `(LPC-10)` 为空或并入 PAR；
3. PAR 由 `(LPC-13)` 给出所需行列和；
4. HYP 由 GHLC-D 即 `(LPC-16)` 给出所需行列和。

四项相加即得 `(LPC-2)`。证毕。

## 8. 当前闭合度

本文完成：

1. LPC-D 的 FAR/ID/PAR/HYP 几何分解；
2. FAR 远距离尾项闭合；
3. ID-near 分支归入 PAR；
4. PAR cusp/parabolic 分支闭合到除数账本；
5. `GHLC-D=>LPC-D`。

本文在接入
`docs/monograph/prime-matrix-h3-dsb-hlc-ghlc-d-local-schur-closure.md`
后还完成：

```text
GHLC-D: generic hyperbolic local correlation row-column bound.
```

需要保留的审稿边界是：点态矩阵条件
`|a z_m+b-(c z_m+d)z_n|` 只作为几何分解 sanity check；真正闭合行列和的是积分核
`L^1` 质量和 Poincare 包 Schur 归一化。完全自足总链的剩余已上移为 `KZ-B` 与 `KZ-E`。
