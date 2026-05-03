# QLOW-MID-COMP 的 H/Q 区间增量审计

**状态：** `hq_interval_increment_negligible_for_sample_certificate`

本报告把 `sin/cos/log` 有理 oracle 的半径接入

\[
\rho_R(u)=\frac{|H(iu/\log R)|}{K}\frac{|Q(iu/\log R)|}{\mathcal V_\omega}.
\]

若每个 `sin/cos` 坐标外向半径为 `eps`，则每个单位复指数项的复平面误差至多

\[
\delta=\sqrt2\,\varepsilon.
\]

归一化后有

\[
\frac{|H|}{K}\mapsto \frac{|H|}{K}+\delta,\qquad
\frac{|Q|}{\mathcal V_\omega}\mapsto \frac{|Q|}{\mathcal V_\omega}+\delta.
\]

由于两个归一化因子本来都不超过 `1`，得到统一增量

\[
\Delta_{HQ}\le 2\delta+\delta^2.
\]

## 增量结果

- oracle half-radius: `2.333e-67`
- complex term radius: `3.300e-67`
- H/Q rho margin: `6.600e-67`
- minimum slack after H/Q interval: `0.117304`

## 样本表

| P | R | certified | +HQ margin | target | slack | pass |
|---:|---:|---:|---:|---:|---:|:---:|
| 2003 | 9 | 0.232696 | 0.232696 | 0.350 | 0.117304 | Y |
| 2003 | 14 | 0.221604 | 0.221604 | 0.350 | 0.128396 | Y |
| 5003 | 12 | 0.226291 | 0.226291 | 0.350 | 0.123709 | Y |
| 5003 | 19 | 0.216654 | 0.216654 | 0.350 | 0.133346 | Y |
| 10007 | 15 | 0.220040 | 0.220040 | 0.350 | 0.129960 | Y |
| 10007 | 25 | 0.208588 | 0.208588 | 0.350 | 0.141412 | Y |

## 审稿含义

- 当前 `H/Q` 的 trig/log 区间误差对 `C_comp` 的影响为 `O(10^-67)`，远低于预算。
- 这闭合的是 `H/Q` 由三角与对数 oracle 导致的外向增量，不闭合 `Phihat`。
- 剩余真正数值硬点集中到 `Phihat` 的 Mellin/求积外向区间，以及 `P>=P0` 的统一 Selberg 矩常数。
