# SQF-QLOW 最优 Selberg 权扫描

**状态：** `weight_optimization_scan_not_a_proof`

本实验比较两类权：标准对数权与精确最小化 `Q(0)` 的 Selberg 权。
目的不是替代证明，而是判断 `SQF-QLOW` 是否应使用核适配/低频优化权。

## 摘要
- P=2003 R=P^0.3 R=9 std Q0/abs=0.176 budget=0.198 opt Q0/abs=0.122 budget=0.163 optL1/stdL1=1.58
- P=2003 R=P^0.35 R=14 std Q0/abs=0.136 budget=0.177 opt Q0/abs=0.090 budget=0.144 optL1/stdL1=1.81
- P=5003 R=P^0.3 R=12 std Q0/abs=0.149 budget=0.185 opt Q0/abs=0.101 budget=0.152 optL1/stdL1=1.68
- P=5003 R=P^0.35 R=19 std Q0/abs=0.115 budget=0.166 opt Q0/abs=0.081 budget=0.140 optL1/stdL1=1.68
- P=10007 R=P^0.3 R=15 std Q0/abs=0.131 budget=0.176 opt Q0/abs=0.086 budget=0.142 optL1/stdL1=1.87
- P=10007 R=P^0.35 R=25 std Q0/abs=0.100 budget=0.157 opt Q0/abs=0.073 budget=0.135 optL1/stdL1=1.64

## 判读

- 若 `optimal-Q0` 显著降低 `Q0/abs` 且不显著增大 `budget`，则 `SQF-QLOW` 应使用精确 Selberg 极小权。
- 若 `Q0/abs` 降低但 `budget` 不降，瓶颈不是 `t=0`，而是 `|t|≈1` 的低频带。
- 若 `lambda_l1` 暴涨，则权重优化会破坏上界筛误差账本，不能直接采用。

## 下一步接口

把 `SQF-QLOW` 拆成：

```text
QLOW-OPT: 选择 Selberg 权最小化低频二次型；
QLOW-STAB: 优化权在 |t|<=T0 内保持稳定；
QLOW-VAR: 优化权的总变差不破坏 RRD/OSPC 账本。
```
