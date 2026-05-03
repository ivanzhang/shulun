# QLOW-MID-COMP 外向舍入误差预算

**状态：** `interval_budget_ready_not_yet_formal_interval_proof`

本文件把紧区间网格证书升级为“区间化前的预算证书”：

\[
C_{\rm grid}+C_{\rm Lip}+C_{\rm interval}<C_{\rm target}.
\]

它不把浮点扫描当作证明；作用是量化正式外向舍入证明最多允许消耗多少余量。

## 总预算

- 目标常数：`0.35`。
- 预留外向舍入总预算：`0.065000`。
- 最小原始余量：`0.117304`。
- 扣除预算后最小余量：`0.052304`。
- 最紧样本：`P=2003, R=9`。

## 预算拆分

| 来源 | 预算 | 证明义务 |
| --- | ---: | --- |
| `phi_quadrature_and_mellin` | 0.022750 | 给 `Phihat` 的 Mellin/积分截断与求积外向误差 |
| `trig_log_interval_oracle` | 0.016250 | 给 `sin/cos/log` 的有理区间包络误差 |
| `selberg_weight_solver` | 0.013000 | 给 Selberg 线性系统、`omega` 与 `V_omega` 的区间求解误差 |
| `grid_endpoint_and_cell_weight` | 0.007800 | 给端点、网格宽度和 `|Phihat|` 加权平均替换误差 |
| `json_decimal_rounding` | 0.005200 | 给十进制导出和表格抄录误差 |

## Selberg 子项进展

`docs/monograph/selberg-rational-weight-audit.md` 已把有限样本中的 Selberg 最优权线性系统改为有理精确审计。
因此 `selberg_weight_solver=0.013000` 在当前样本上不再表示浮点消元误差，而应解释为以下剩余义务的保守预算：

- 从有限样本推广到 `P>=P0` 的统一 `V_omega` 与对数矩常数；
- `sum |omega_l|log(l)/l` 中 `log(l)` 的有理区间 oracle；
- 正式稿中有理表格抄录和外向输出误差。

## sin/cos/log 子项进展

`docs/monograph/trig-log-interval-oracle-audit.md` 已用纯有理级数建立当前样本所有三角与对数调用的统一 oracle 半径。
其最大半径为 `2.333e-67`，远小于 `trig_log_interval_oracle=0.016250` 的预算量级。
`docs/monograph/qlow-mid-comp-hq-interval-audit.md` 又把该半径接入 `H/Q`，得到 `rho` 增量 `6.600e-67`。
因此当前有限样本中的 `sin/cos/log` 外向包络和 `H/Q` 复数区间增量都不再是常数余量瓶颈。
`docs/monograph/qlow-mid-comp-supnorm-audit.md` 进一步给出 Phihat-free 的 `sup rho` 旁路，最紧 `supBound=0.296630<0.35`。
所以 `QLOW-MID-COMP` 的紧区间常数界不再依赖 `Phihat` 求积外向区间。


## 样本余量表

| P | R | certified | rawSlack | postBudgetUpper | postBudgetSlack | pass |
|---:|---:|---:|---:|---:|---:|:---:|
| 2003 | 9 | 0.232696 | 0.117304 | 0.297696 | 0.052304 | Y |
| 2003 | 14 | 0.221604 | 0.128396 | 0.286604 | 0.063396 | Y |
| 5003 | 12 | 0.226291 | 0.123709 | 0.291291 | 0.058709 | Y |
| 5003 | 19 | 0.216654 | 0.133346 | 0.281654 | 0.068346 | Y |
| 10007 | 15 | 0.220040 | 0.129960 | 0.285040 | 0.064960 | Y |
| 10007 | 25 | 0.208588 | 0.141412 | 0.273588 | 0.076412 | Y |

## 严格化判据

若后续区间程序逐项证明

\[
C_{\rm interval}\le 0.065000,
\]

则当前样本证书全部仍满足 `C_comp<0.35`。进一步地，`sup-rho` 旁路已把 `Phihat` 从紧区间证明中移除，下一步应集中在统一 Selberg 矩常数与 `RRD/OSPC`。

## 未闭合点

- 当前预算表不是形式证明；它只是给出形式证明需要满足的误差上限。
- `sin/cos/log` 与 `H/Q` 复数区间增量已完成样本级审计。
- Selberg 权样本线性系统已精确审计，但仍需 `P>=P0` 的统一矩常数。
- `Phihat` 的 Mellin/求积外向区间已被 `sup-rho` 旁路绕开，不再是 `QLOW-MID-COMP` 必需输入。
- `H/Q` 网格值仍可进一步做全区间复数重算，以替代当前十进制预算。
- 完成这些后，`QLOW-MID-COMP` 才能从 `grid certificate` 升级为 `interval proof certificate`。
