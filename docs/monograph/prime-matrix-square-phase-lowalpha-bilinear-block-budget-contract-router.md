# Prime Matrix square-phase low-alpha 双线性块 signed budget 合同

**状态：** `bilinear_block_weighted_budget_contract_closed_bounds_open`

coprime boundary 双线性块的验收不应要求每个块单独小于总角度阈值；正确充分条件是加权预算 `sum_b mass_share_b * signed_ratio_b <= theta_z`。这一步闭合了块级预算如何推出 coprime edge 角度界的合同。若合同失败，失败必定位到具体 `(z,bucket)`，成为 LocalizedBlock-PDEC；若合同通过，下一步只需证明各块的 signed ratio 预算。

```text
weighted_block_budget_contract_closed=true
sample_satisfies_weighted_block_budget=true
balanced_block_dispersion_bound_proved=false
unbalanced_endpoint_pdec_excluded=false
localized_block_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. z 层预算

| z | target angle | weighted block budget | slack | pass |
| ---: | ---: | ---: | ---: | --- |
| 7 | 8.509258 | n/a | n/a | `true` |
| 13 | 2.715323 | 0.090174 | 2.625149 | `true` |
| 31 | 0.591273 | 0.021395 | 0.569878 | `true` |
| 61 | 0.221522 | 0.033461 | 0.188061 | `true` |

## 2. 块级贡献

| z | bucket | abs share | signed/abs | weighted budget |
| ---: | --- | ---: | ---: | ---: |
| 13 | `balanced<=2` | 0.157450 | 0.400790 | 0.063104 |
| 13 | `mid<=4` | 0.174940 | 0.012484 | 0.002184 |
| 13 | `unbalanced<=8` | 0.143338 | 0.000106 | 0.000015 |
| 13 | `far>8` | 0.524272 | 0.047438 | 0.024870 |
| 31 | `balanced<=2` | 0.179123 | 0.027417 | 0.004911 |
| 31 | `mid<=4` | 0.195326 | 0.002149 | 0.000420 |
| 31 | `unbalanced<=8` | 0.200323 | 0.080038 | 0.016034 |
| 31 | `far>8` | 0.425227 | 0.000073 | 0.000031 |
| 61 | `balanced<=2` | 0.249309 | 0.031722 | 0.007908 |
| 61 | `mid<=4` | 0.214256 | 0.021097 | 0.004520 |
| 61 | `unbalanced<=8` | 0.177040 | 0.028766 | 0.005093 |
| 61 | `far>8` | 0.359395 | 0.044350 | 0.015939 |

## 3. 证明边界

- 已闭合：块级 signed ratio 的加权预算推出 coprime edge 角度界。
- 未闭合：balanced/mid 块 signed ratio 预算。
- 未闭合：unbalanced/far endpoint PDEC 排斥或 signed ratio 预算。
- 当前最大加权块为 `z=13, balanced<=2`，贡献 `0.063104`。
- 下一目标：`WeightedBilinearBlockSignedBudgetOrLocalizedBlockPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-coefficient-formula-split-router.json` | `e9ae5080e5df364181f29c6acdff03bdb8259181f99065df89405a98be3fa2fd` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-coprime-boundary-bilinear-router.json` | `314e3b5b439a6928a478d24c1c439fcf692303883334747ac84e95f510dd569d` |
| `experiments/prime_matrix_square_phase_lowalpha_bilinear_block_budget_contract_router.py` | `b948789c2fe939f019865924015a0281506e725192198f57185a38d669f15fd1` |
