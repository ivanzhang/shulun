# QLOW-MID-COMP 紧区间网格证书

**状态：** `compact_grid_certificate_pending_interval_rounding`

本证书把最后单点硬核固定为紧区间

\[
2<u\le U_0,\qquad U_0=12,
\]

并对

\[
\rho_R(u)=\frac{|H(iu/\log R)|}{K}\frac{|Q(iu/\log R)|}{\mathcal V_\omega}
\]

做带权平均与导数余量核查。这里的关键不是裸 `Q` 单调性，而是 `Phihat/H/Q` 联合带权吸收。

## 证书摘要

| P | R | gridRatio | LipMargin | certified | target | pass | worstU | maxRho |
|---:|---:|---:|---:|---:|---:|:---:|---:|---:|
| 2003 | 9 | 0.222953 | 0.009742 | 0.232696 | 0.350 | Y | 3.710 | 0.281688 |
| 2003 | 14 | 0.212462 | 0.009142 | 0.221604 | 0.350 | Y | 4.190 | 0.274510 |
| 5003 | 12 | 0.217061 | 0.009230 | 0.226291 | 0.350 | Y | 4.090 | 0.276486 |
| 5003 | 19 | 0.208084 | 0.008570 | 0.216654 | 0.350 | Y | 4.470 | 0.267230 |
| 10007 | 15 | 0.211043 | 0.008996 | 0.220040 | 0.350 | Y | 4.330 | 0.275205 |
| 10007 | 25 | 0.200412 | 0.008177 | 0.208588 | 0.350 | Y | 4.770 | 0.262816 |

## 导数账本

对任意一个网格小区间 `I`，若 `m_I` 是中点，则

\[
\rho_R(u)\le \rho_R(m_I)+\frac{|I|}{2}\left(
\frac{\log(K!)}{K\log R}+
\frac{\sum_\ell |\omega_\ell|\log\ell/\ell}{\mathcal V_\omega\log R}
\right).
\]

因此

\[
\frac{\int_{2}^{12}|\widehat\Phi|\,|H|\,|Q|\,du/\log R}
{K\mathcal V_\omega\int_{2}^{12}|\widehat\Phi|\,du/\log R}
\le
\operatorname{Avg}_{|\widehat\Phi|}(\rho_R)+\operatorname{LipMargin}.
\]

这个处理保留了 `Phihat` 的真实权重，不再使用会丢失余量的逐点 `sup rho`。

## 审稿口径

- 当前证书仍是浮点网格证书，作用是定位并压缩最后硬点。
- 要升级为正式无条件证明，需要把 `Phihat`、`H`、`Q` 的网格值改为有理区间外向舍入。
- 由于频带 `2<u<=12` 固定，外向舍入表是固定紧区间解析证书，不是有限模板覆盖无限素数情形。
- 若所有行满足 `certified < target`，则 `QLOW-MID-COMP` 可作为 RSE 临界带的常数输入接入主链。

## 最大贡献小区间

### P=2003 R=P^0.3
- u=2.010: rho=0.200474, Q=0.240817, H=0.832472, weightedShare=0.0051
- u=2.030: rho=0.202017, Q=0.243571, H=0.829396, weightedShare=0.0051
- u=2.050: rho=0.203561, Q=0.246352, H=0.826301, weightedShare=0.0051
- u=2.070: rho=0.205106, Q=0.249161, H=0.823187, weightedShare=0.0051
- u=2.090: rho=0.206650, Q=0.251995, H=0.820053, weightedShare=0.0051

### P=2003 R=P^0.35
- u=2.750: rho=0.214287, Q=0.272003, H=0.787813, weightedShare=0.0042
- u=2.730: rho=0.212769, Q=0.269135, H=0.790566, weightedShare=0.0042
- u=2.770: rho=0.215796, Q=0.274882, H=0.785050, weightedShare=0.0042
- u=2.710: rho=0.211241, Q=0.266278, H=0.793308, weightedShare=0.0042
- u=2.790: rho=0.217293, Q=0.277771, H=0.782276, weightedShare=0.0042

### P=5003 R=P^0.3
- u=2.090: rho=0.175501, Q=0.204877, H=0.856618, weightedShare=0.0045
- u=2.110: rho=0.177015, Q=0.207266, H=0.854050, weightedShare=0.0045
- u=2.070: rho=0.173993, Q=0.202513, H=0.859169, weightedShare=0.0045
- u=2.130: rho=0.178535, Q=0.209680, H=0.851465, weightedShare=0.0045
- u=2.050: rho=0.172491, Q=0.200175, H=0.861702, weightedShare=0.0045

### P=5003 R=P^0.35
- u=2.870: rho=0.202019, Q=0.248831, H=0.811871, weightedShare=0.0040
- u=2.890: rho=0.203476, Q=0.251365, H=0.809486, weightedShare=0.0040
- u=2.850: rho=0.200554, Q=0.246306, H=0.814247, weightedShare=0.0040
- u=2.910: rho=0.204924, Q=0.253905, H=0.807090, weightedShare=0.0040
- u=2.830: rho=0.199081, Q=0.243789, H=0.816612, weightedShare=0.0040

### P=10007 R=P^0.3
- u=2.590: rho=0.193444, Q=0.236411, H=0.818252, weightedShare=0.0043
- u=2.570: rho=0.191854, Q=0.233738, H=0.820805, weightedShare=0.0043
- u=2.610: rho=0.195032, Q=0.239101, H=0.815687, weightedShare=0.0043
- u=2.550: rho=0.190260, Q=0.231082, H=0.823345, weightedShare=0.0043
- u=2.630: rho=0.196615, Q=0.241806, H=0.813111, weightedShare=0.0043

### P=10007 R=P^0.35
- u=3.110: rho=0.199117, Q=0.244359, H=0.814857, weightedShare=0.0038
- u=3.090: rho=0.197729, Q=0.242012, H=0.817019, weightedShare=0.0038
- u=3.130: rho=0.200498, Q=0.246710, H=0.812687, weightedShare=0.0038
- u=3.070: rho=0.196332, Q=0.239672, H=0.819172, weightedShare=0.0038
- u=3.150: rho=0.201870, Q=0.249066, H=0.810508, weightedShare=0.0038
