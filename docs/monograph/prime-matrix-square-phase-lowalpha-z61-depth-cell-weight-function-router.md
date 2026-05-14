# Prime Matrix square-phase low-alpha z=61 深度格权函数路由

**状态：** `z61_depth_cell_reduced_to_weight_function_discrepancy_open`

每个深度格的线性余项已精确写成 b 多重序列上的权函数均值偏差：`L_C=sum_b mult(b) W_C(b)-N sum_{m in C}K_m/m`，其中 `W_C(b)=sum_{m|b,m in C}K_m`。因此 DepthShell 预算的剩余证明不再需要同时处理所有模数；它等价于这些显式权函数没有大均值偏差，或任何失败都会表现为权重尖峰/低模相关 PDEC。

```text
depth_cell_weight_function_identity_closed=true
weight_spike_diagnostic_materialized=true
depth_cell_weight_function_discrepancy_proved=false
weight_spike_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. 权函数恒等式

```text
W_C(b)=sum_{m|b, m in C} K_m
L_C=sum_b mult(b)W_C(b)-N*sum_{m in C}K_m/m.
```

该恒等式逐深度格精确匹配上一层 `linear_remainder`。

## 2. 最大贡献深度格

| bucket | omega | shell | moduli | abs linear/bucket abs | nonzero share | max W/abs L | identity err |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| `balanced<=2` | 3 | `(2D,4D]` | 72 | 0.051057 | 0.023794 | 0.047405 | 0.000000 |
| `balanced<=2` | 2 | `(D,2D]` | 18 | 0.042720 | 0.012550 | 0.069190 | -0.000000 |
| `unbalanced<=8` | 3 | `(D,2D]` | 28 | 0.041577 | 0.016809 | 0.121538 | -0.000000 |
| `unbalanced<=8` | 4 | `(D,2D]` | 21 | 0.040538 | 0.012687 | 0.245596 | 0.000000 |
| `far>8` | 3 | `(D,2D]` | 74 | 0.035544 | 0.042321 | 0.095803 | 0.000000 |
| `unbalanced<=8` | 4 | `(4D,8D]` | 75 | 0.030065 | 0.011931 | 0.141412 | -0.000000 |
| `far>8` | 3 | `(2D,4D]` | 75 | 0.028331 | 0.024046 | 0.063362 | -0.000000 |
| `mid<=4` | 3 | `(4D,8D]` | 64 | 0.027561 | 0.011061 | 0.074702 | 0.000000 |
| `mid<=4` | 4 | `(4D,8D]` | 78 | 0.026114 | 0.011886 | 0.111844 | -0.000000 |
| `mid<=4` | 2 | `(D,2D]` | 11 | 0.025089 | 0.008954 | 0.093974 | 0.000000 |
| `mid<=4` | 4 | `(8D,16D]` | 109 | 0.021497 | 0.009664 | 0.093923 | 0.000000 |
| `unbalanced<=8` | 4 | `(8D,16D]` | 114 | 0.018404 | 0.009664 | 0.125026 | -0.000000 |
| `balanced<=2` | 4 | `(2D,4D]` | 49 | 0.018012 | 0.015115 | 0.263540 | -0.000000 |
| `unbalanced<=8` | 3 | `(4D,8D]` | 45 | 0.017670 | 0.008473 | 0.094469 | 0.000000 |
| `unbalanced<=8` | 5 | `(8D,16D]` | 30 | 0.016368 | 0.001969 | 0.135064 | 0.000000 |
| `mid<=4` | 4 | `(2D,4D]` | 47 | 0.015235 | 0.013443 | 0.296073 | -0.000000 |

## 3. 权重尖峰诊断

| bucket | omega | shell | max W value | max W | abs linear | max W/abs L | nonzero share |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| `far>8` | 5 | `(2D,4D]` | 30030 | 3.548971 | 0.334625 | 10.605819 | 0.001282 |
| `balanced<=2` | 5 | `(2D,4D]` | 30030 | 1.492083 | 0.387591 | 3.849630 | 0.001282 |
| `far>8` | 4 | `(2D,4D]` | 102102 | 4.883171 | 2.035063 | 2.399518 | 0.016626 |
| `unbalanced<=8` | 3 | `(2D,4D]` | 52003 | 1.353661 | 0.618487 | 2.188665 | 0.012893 |
| `balanced<=2` | 4 | `(4D,8D]` | 199578 | 1.612257 | 0.812370 | 1.984635 | 0.015229 |
| `far>8` | 4 | `(D,2D]` | 30030 | 4.117028 | 2.585525 | 1.592337 | 0.017474 |
| `mid<=4` | 5 | `(2D,4D]` | 46410 | 1.991301 | 1.444572 | 1.378471 | 0.001282 |
| `unbalanced<=8` | 5 | `(2D,4D]` | 30030 | 1.393075 | 1.357858 | 1.025936 | 0.001099 |
| `balanced<=2` | 3 | `(D,2D]` | 173910 | 1.844587 | 2.177785 | 0.847001 | 0.027367 |
| `far>8` | 4 | `(4D,8D]` | 102102 | 1.855163 | 2.452801 | 0.756345 | 0.017451 |
| `mid<=4` | 4 | `(D,2D]` | 81510 | 2.228957 | 3.628170 | 0.614347 | 0.011130 |
| `mid<=4` | 3 | `(2D,4D]` | 199578 | 2.785340 | 5.101701 | 0.545963 | 0.014909 |
| `unbalanced<=8` | 5 | `(4D,8D]` | 81510 | 1.725848 | 3.487791 | 0.494826 | 0.001649 |
| `far>8` | 3 | `(4D,8D]` | 81719 | 1.785650 | 3.741238 | 0.477289 | 0.012573 |
| `mid<=4` | 3 | `(D,2D]` | 76038 | 1.820251 | 4.081758 | 0.445948 | 0.020405 |
| `far>8` | 5 | `(4D,8D]` | 81510 | 2.704095 | 6.095474 | 0.443623 | 0.001649 |

## 4. 证明边界

- 已闭合：每个深度格余项到 b 序列权函数均值偏差的精确恒等式。
- 已物化：每个深度格的非零覆盖比例、最大权重和二阶矩诊断。
- 未闭合：全局证明这些权函数均值偏差满足深度预算。
- 若失败：失败格给出权重尖峰或低模相关 `WeightFunction-PDEC`。
- 下一目标：`DepthCellWeightFunctionDiscrepancyOrWeightSpikePDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json` | `7db79319df6fa99cbb2fd1c49d0b877ea1aac2b662dd73eadc89354b35d6925c` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-mobius-kernel-normal-form-router.json` | `eac8ba26aab932d189ae6a03e2e8ef9415f90c1746be4693ae0fb543a154d6ad` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_depth_cell_weight_function_router.py` | `f2e34a18278a6c22a102cc3e2c7a824016a183cbbaf504b7cb0b555d238d3470` |
