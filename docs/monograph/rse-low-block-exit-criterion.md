# 低模块预算违例的 OSPC*/CRTDefect 出口准则

**状态：** `algebraic_exit_criterion_remaining_crt_weighted_bound`

本报告把上一节的低模二分推进成一个纯代数出口准则：只要无 `OSPC*` 且无加权 `CRTDefect`，就必有 `RRD-low<=0.006`。因此 `RRD-low` 大贡献只能从两个出口之一离开主链。

## 1. 常数

- `epsilon_low=0.006000`。
- `delta_dir=0.250000`。
- 允许的加权 CRT 缺陷：`epsilon_low/sqrt(1+delta_dir)=0.005366563`。

本报告默认 `delta_dir=1/4`，因此若无 OSPC，则加权 CRT 缺陷需要控制在约 `0.005367` 以内即可吸收 `RRD-low`。

## 2. 块级对象

把低模字典 `D_Z` 分解成有限块 `B=(q,r,s)`，其中 `s` 表示 Buchstab 低层或小模周期类型。令

\[
\Pi_{\le Z}W=\sum_B W_B.
\]

对每个块，按辅助模 `r` 的非零残基分解

\[
C_{B,a}=\sum_{m\equiv a\pmod r} W_B(m),
\qquad
\mathcal A_B=\sum_m |W_B(m)|.
\]

定义有向能量

\[
E_{\rm dir}(B)=
{(r-1)\sum_a |C_{B,a}|^2\over \mathcal A_B^2}.
\]

再定义真实粗数残差在该块上的 CRT 缺陷强度 `kappa_B`，使得

\[
\left|\sum_a d_{B,a}C_{B,a}\right|
\le
\kappa_B\left(\sum_a |C_{B,a}|^2\right)^{1/2},
\]

其中 `d_{B,a}` 是残基类上的真实粗数残差向量。

## 3. 出口引理

若所有低模块都没有 OSPC，即

\[
E_{\rm dir}(B)\le 1+\delta_{\rm dir},
\]

则

\[
\left(\sum_a |C_{B,a}|^2\right)^{1/2}
\le
{\sqrt{1+\delta_{\rm dir}}\over \sqrt{r-1}}\mathcal A_B.
\]

把 `1/sqrt(r-1)` 吸收到块权 `m_B` 后，得到

\[
|\mathcal E_{\rm low}|
\le
\sqrt{1+\delta_{\rm dir}}\sum_B \kappa_B m_B.
\tag{LBE}
\]

因此若同时无加权 CRTDefect，即

\[
\sum_B \kappa_B m_B
\le
{0.006\over \sqrt{1+\delta_{\rm dir}}},
\]

则 `|E_low|<=0.006`，`RRD-low` 被吸收。

其逆否命题就是当前需要的出口：

```text
|E_low| > 0.006
=> 存在低模块 OSPC*
   或 加权 CRTDefect 超过 0.006/sqrt(1+delta_dir)。
```

## 4. 当前剩余

本轮已经把 `low-block=>exit` 变成代数准则。`docs/monograph/h5-1-rrd-low-exit-theorem.md` 进一步把该准则写成 H5.1 出口定理：

```text
|E_low| > 0.006
=> OSPC* or weighted CRTDefect.
```

因此 H5.1 的路由义务已闭合；真正剩余不再是 Hilbert 投影本身，而是两个下游定量输入：

- 证明低模字典可分解为有限近正交块，且 Gram 损失并入 RRD-conversion。
- `OSPC*` 与 `weighted CRTDefect` 已由 `docs/monograph/h5-4-ospc-weighted-crtdefect-absorption.md` 吸收到 H4 的 `PDEC-or-SAE`；后续必须排除这两个最终分支。
- 若上述两出口均不发生，则由 Cauchy--Schwarz 得 |E_low|<=epsilon_low。

下一步最优攻坚不再是 H5.1/H5.4 路由，而是 H4 证书层：证明 persistent 分支的 `PDEC-Cert` 和 sparse 分支的 `SAE-Cert`。
