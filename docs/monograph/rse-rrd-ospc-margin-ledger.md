# RSE 主链 RRD/OSPC 余量账本

**状态：** `positive_margin_proof_obligation_ledger`

本账本只做一件事：把 `QLOW-MID-COMP` 的 `sup-rho` 正余量转换成 `RRD/OSPC` 后续证明必须满足的同口径常数目标。它不是 `RRD/OSPC` 的证明。

## 归一化约定

所有 C_* 必须先换算到 QLOW-MID-COMP 的 target=0.35 归一化损失尺度；否则本账本不能使用。

若某个误差项只在未归一化的 `H sum 1/m`、Fourier 能量或 Selberg 变差尺度下给出，必须先证明到 `K V_omega` / `target=0.35` 的换算因子，才能放入本表。

## 可用余量

| 来源 | P | R | target | comp_bound | available_margin |
| --- | ---: | ---: | ---: | ---: | ---: |
| `docs/monograph/qlow-mid-comp-supnorm-audit.json` | 2003 | 9 | 0.350000 | 0.296630 | 0.053370 |

其中 `available_margin = 0.35 - supBound`。当前最紧样本给出约 `0.0533695` 的后续可分配余量。

## 证明义务预算

| 接口 | 预算 | 必须证明的同口径界 | 具体义务 |
| --- | ---: | --- | --- |
| `RRD` 粗数替换误差 | 0.020 | `C_RRD <= 0.020` | 把 E_rough-discrep 的绝对值归一化到 QLOW 的 K V_omega 尺度，并证明同权 convention 下的损失不超过 0.020。 |
| `OSPC` 有向小素集中出口 | 0.020 | `C_OSPC <= 0.020` | 证明 OSPC 必触发 CRTDefect/Tail-anchor 出口，且 Fourier 到缺陷的常数损失不超过 0.020。 |
| `SelbergUniform` P>=P0 统一 Selberg 矩常数 | 0.008 | `C_SelbergUniform <= 0.008` | 把样本网格的 Selberg 有理审计升级为 P>=P0 的矩阵扰动/谱隙统一界。 |
| `LedgerRounding` 账本换算与外向舍入 | 0.003 | `C_round <= 0.003` | 统一 H/Q、Selberg 变差、RSE 核和 RRD/OSPC 之间的归一化换算误差。 |

- 已分配预算：`0.051000`。
- 保留余量：`0.002370`。

因此当前可审查判据为

\[
C_{\rm RRD}+C_{\rm OSPC}+C_{\rm SelbergUniform}+C_{\rm round}<0.053369509758272926.
\]

按上表目标值，只要四项分别落入 `0.020+0.020+0.008+0.003=0.051`，仍有约 `0.0023695` 余量。

## RRD 需要证明的形式

原始接口为

\[
|\mathcal E_{\mathrm{rough-discrep}}|
\le
\eta_{\mathrm{rough}} H\sum_{m\sim M,\ P^-(m)>Y}\frac1m.
\]

下一步不能只估计 `eta_rough`，还必须给出从右侧到 `C_RRD` 的同权换算，目标是 `C_RRD<=0.020`。

## OSPC 需要证明的形式

原始接口为

\[
(r-1)\sum_a |C_a(q,r)|^2
\ge
(1+\delta_{\mathrm{dir}})
\mathcal A(q,r)^2.
\]

下一步必须把该有向能量异常定量推出为 `CRTDefect/Tail-anchor` 可吸收出口，并证明出口损失在 `C_OSPC<=0.020` 内。

## 审稿结论

QLOW-MID-COMP 的样本网格已有正余量；RRD/OSPC 尚未由本账本证明。下一步必须逐项证明 budget 表中的 required_bound。

当前主链最小剩余项已经从笼统的 `RRD/OSPC` 改写为四个可逐项检查的常数不等式。下一步最优硬攻是先做 `RRD` 的同权归一化，因为它是标量误差；随后处理 `OSPC` 的有向 Fourier 到 CRTDefect 的定量出口。

## RRD 子账本更新

新增 `docs/monograph/rse-rrd-same-weight-reduction.md`。审查结论是：旧的一步常数密度替换压力样本最坏 `roughDiff/env=0.2000018136297129`，不能直接证明 `C_RRD<=0.020`。但振幅恒等式

\[
{|\omega_\ell|\over h}\cdot {hH\over \ell M}\big/ {H\over M}
=
{|\omega_\ell|\over \ell}
\]

说明 `RRD` 与 `QLOW` 使用同一 Selberg 变差范数。故 `RRD` 预算进一步拆为

```text
RRD-low        <= 0.006
RRD-perp       <= 0.012
RRD-conversion <= 0.002
```

下一步必须形式化低模投影 `Pi_{<=Z}`，并证明 `RRD-low` 若不小就触发 `OSPC/CRTDefect`。

## OSPC 归一化修正

新增 `docs/monograph/rse-rrd-low-projection-dichotomy.md`。该审查修正 OSPC 的尺度：应使用

\[
E_{\rm dir}(q,r)=
\frac{(r-1)\sum_a |C_a(q,r)|^2}{\mathcal A(q,r)^2}
\]

并以 `E_dir(q,r)>=1+delta_dir` 作为有向集中判据。早期右侧额外除以 `r-1` 的写法过弱，不能作为集中判据。修正后，`RRD-low` 的大情形被精确定位为某个低模块的有向能量/CRTDefect 出口。

## 低模块出口准则

新增 `docs/monograph/rse-low-block-exit-criterion.md`。它给出代数判据：取 `delta_dir=1/4` 时，若无 `OSPC*` 且

\[
\sum_B \kappa_B m_B\le 0.005366563145999495,
\]

则 `RRD-low<=0.006`。因此 `RRD-low` 超预算只能来自 `OSPC*` 或加权 `CRTDefect`。下一步常数义务是证明该加权 CRT 缺陷界，或证明其失败进入 `Tail-anchor/CRTDefect`。

## H5 接受矩阵

新增 `docs/monograph/h5-rrd-ospc-proof-obligation-matrix.md`。该矩阵把本账本的四个总预算拆成六个验收项：

```text
H5.1 RRD-low dichotomy          <= 0.006
H5.2 RRD-perp orthogonal bound  <= 0.012
H5.3 RRD-conversion             <= 0.002
H5.4 OSPC* exit                 <= 0.020
H5.5 SelbergUniform             <= 0.008
H5.6 LedgerRounding             <= 0.003
```

若六项全部成立，则总损失至多 `0.051`，严格小于可用余量 `0.053369509758272926`。新增 `docs/monograph/h5-1-rrd-low-exit-theorem.md` 后，H5.1 的出口路由已经闭合为：`RRD-low` 超预算必触发 `OSPC*` 或 `weighted CRTDefect`。当前最小硬点转为排除这些命名出口，或把它们并入 H4 的 `PDEC-or-SAE` / Tail-anchor 排斥。
