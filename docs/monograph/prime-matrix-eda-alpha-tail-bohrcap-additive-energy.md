# Bohr-cap 聚集到加法能量异常

**状态：** `alpha_tail_bohrcap_additive_energy_reduction_open`

本文继续压缩高频 `Bohr-cap` 分支。核心结论：若低素 squarefree 高块集合 `D` 的差集大量落入
某个 Bohr 弧，而该 Bohr 弧在真实差值范围内并不大，则 `D` 必须具有异常高的加法能量。

## 1. Bohr 差值集合

沿用

\[
D\subset(B,2B],\qquad \alpha={h\over Q}.
\tag{BAE-1}
\]

对 `T>=1` 定义整数差值集合

\[
\mathcal R_T(h,Q;B)=
\left\{
r\in\mathbb Z:\ 0<|r|\le B,\ 
\left\|{hr\over Q}\right\|\le {1\over T}
\right\}.
\tag{BAE-2}
\]

Bohr-cap 对数为

\[
\mathcal P_T(D;h,Q)
=
\#\{(d,d')\in D^2:d\ne d',\ d-d'\in\mathcal R_T(h,Q;B)\}.
\tag{BAE-3}
\]

令差值重数

\[
\nu_D(r)=\#\{(d,d')\in D^2:d-d'=r\}.
\tag{BAE-4}
\]

则

\[
\mathcal P_T(D;h,Q)=\sum_{r\in\mathcal R_T}\nu_D(r).
\tag{BAE-5}
\]

## 2. 加法能量推出

定义加法能量

\[
E_+(D)=\sum_r \nu_D(r)^2.
\tag{BAE-6}
\]

由 Cauchy--Schwarz，

\[
\mathcal P_T(D;h,Q)^2
\le
|\mathcal R_T(h,Q;B)|\,E_+(D).
\tag{BAE-7}
\]

因此若

\[
\mathcal P_T(D;h,Q)\ge P_0,
\tag{BAE-8}
\]

则

\[
E_+(D)\ge {P_0^2\over |\mathcal R_T(h,Q;B)|}.
\tag{BAE-9}
\]

这一步完全确定性；没有使用随机模型。

## 3. 有效模数二分

写

\[
g=(h,Q),\qquad Q_0={Q\over g},\qquad h_0={h\over g}.
\tag{BAE-10}
\]

则 `(h_0,Q_0)=1`，且 Bohr 条件为

\[
\left\|{h_0r\over Q_0}\right\|\le {1\over T}.
\tag{BAE-11}
\]

乘以 `h_0` 在 `Z/Q_0Z` 上可逆，所以 `R_T` 的大小只由有效模数 `Q_0` 控制。若 `Q_0` 很小，
则频率实际是低有效模缺陷，进入 `PDEC/ColumnCRT`。若 `Q_0` 大，则 `R_T` 稀疏，`(BAE-9)`
迫出高加法能量。

形式化地，当前高频分支二分为：

```text
LowEffectiveMod：Q0 小，进入 PDEC/ColumnCRT；
HighEnergy：E_+(D) 大，进入 squarefree-smooth additive-energy 异常。
```

## 4. 与低素 squarefree 结构的接口

AlphaTail 中的 `D` 是

\[
D=\{d\in(B,2B]:d\mid M_y,\ d\ {\rm squarefree},\ \mu(d)=\sigma\}.
\tag{BAE-12}
\]

因此高加法能量意味着存在大量四元组

\[
d_1-d_2=d_3-d_4,
\qquad d_i\in(B,2B],\quad d_i\mid M_y,\quad \mu(d_i)=\sigma.
\tag{BAE-13}
\]

这是一种强结构异常：低素平方自由数在短 dyadic 块中形成大量平行和。若这种异常持久出现，
它应当进入 `ColumnCRT/PDEC`；若只在单窗出现，则进入 `SAE`。

## 5. 审稿边界

已证明：

```text
HighFreq-BohrCap
=> LowEffectiveMod/PDEC 或 squarefree-smooth additive-energy anomaly.
```

尚未证明：

```text
squarefree-smooth additive-energy anomaly 不可能。
```

下一步最小硬点是给 `D` 的加法能量建立上界；若上界失败，则把失败四元组路由到
`ColumnCRT/PDEC/SAE`。
