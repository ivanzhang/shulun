# Prime Matrix square-phase low-alpha z=61 权函数 P-profile 抵消

**状态：** `z61_weight_function_profile_cancellation_open`

深度格权函数偏差已按来源素数 `P` 精确分解。样本显示逐 `P` 独立绝对预算对 balanced/mid/unbalanced 不足，因此真正剩余是跨 `P` profile 的系统抵消；若某个 `P`-profile 原子长期承担异常偏差，则直接形成 ProfileWeight-PDEC。

```text
p_profile_decomposition_identity_closed=true
profile_independent_budget_sufficient_for_all_buckets=false
cross_p_profile_cancellation_needed=true
cross_p_profile_cancellation_proved=false
profile_weight_pdec_excluded=false
row_column_unconditional_closed=false
```

## 1. bucket profile 预算

| bucket | profile crude | cell abs | cap | credit | required credit | independent sufficient |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `balanced<=2` | 0.447800 | 0.177263 | 0.221522 | 0.270537 | 0.226278 | false |
| `mid<=4` | 0.402746 | 0.182229 | 0.221522 | 0.220517 | 0.181224 | false |
| `unbalanced<=8` | 0.431447 | 0.204937 | 0.221522 | 0.226510 | 0.209925 | false |
| `far>8` | 0.272598 | 0.115186 | 0.221522 | 0.157412 | 0.051076 | false |

## 2. bucket 按 P 的绝对贡献

| bucket | P | abs linear/bucket abs |
| --- | ---: | ---: |
| `balanced<=2` | 10007 | 0.017240 |
| `balanced<=2` | 36739 | 0.070875 |
| `balanced<=2` | 83561 | 0.220626 |
| `balanced<=2` | 200003 | 0.139059 |
| `mid<=4` | 10007 | 0.018853 |
| `mid<=4` | 36739 | 0.094069 |
| `mid<=4` | 83561 | 0.140485 |
| `mid<=4` | 200003 | 0.149339 |
| `unbalanced<=8` | 10007 | 0.028669 |
| `unbalanced<=8` | 36739 | 0.089615 |
| `unbalanced<=8` | 83561 | 0.155856 |
| `unbalanced<=8` | 200003 | 0.157307 |
| `far>8` | 10007 | 0.020238 |
| `far>8` | 36739 | 0.069306 |
| `far>8` | 83561 | 0.126866 |
| `far>8` | 200003 | 0.056188 |

## 3. 最大 P-profile 原子

| P | bucket | omega | shell | abs linear/bucket abs | nonzero share | max W/abs L |
| ---: | --- | ---: | --- | ---: | ---: | ---: |
| 83561 | `balanced<=2` | 3 | `(D,2D]` | 0.050045 | 0.031972 | 0.059747 |
| 83561 | `balanced<=2` | 3 | `(2D,4D]` | 0.049211 | 0.028419 | 0.049183 |
| 200003 | `balanced<=2` | 3 | `(D,2D]` | 0.040290 | 0.025232 | 0.097288 |
| 200003 | `unbalanced<=8` | 4 | `(D,2D]` | 0.038630 | 0.012456 | 0.257731 |
| 200003 | `mid<=4` | 4 | `(4D,8D]` | 0.037804 | 0.010895 | 0.077258 |
| 200003 | `unbalanced<=8` | 3 | `(D,2D]` | 0.031925 | 0.016147 | 0.158284 |
| 36739 | `far>8` | 4 | `(D,2D]` | 0.029666 | 0.014204 | 0.124614 |
| 83561 | `unbalanced<=8` | 4 | `(4D,8D]` | 0.028876 | 0.014210 | 0.127788 |
| 83561 | `mid<=4` | 3 | `(4D,8D]` | 0.028581 | 0.013462 | 0.068401 |
| 200003 | `balanced<=2` | 2 | `(D,2D]` | 0.027557 | 0.012421 | 0.107261 |
| 83561 | `unbalanced<=8` | 4 | `(D,2D]` | 0.025811 | 0.014490 | 0.238128 |
| 36739 | `unbalanced<=8` | 4 | `(D,2D]` | 0.025801 | 0.009718 | 0.238224 |
| 83561 | `far>8` | 3 | `(D,2D]` | 0.025649 | 0.046462 | 0.127731 |
| 36739 | `unbalanced<=8` | 3 | `(D,2D]` | 0.025020 | 0.014951 | 0.105533 |
| 83561 | `far>8` | 4 | `(D,2D]` | 0.023645 | 0.019351 | 0.256665 |
| 83561 | `far>8` | 3 | `(2D,4D]` | 0.023630 | 0.028139 | 0.069319 |
| 83561 | `balanced<=2` | 4 | `(4D,8D]` | 0.022137 | 0.018416 | 0.085657 |
| 83561 | `unbalanced<=8` | 4 | `(8D,16D]` | 0.021717 | 0.011686 | 0.105952 |
| 200003 | `mid<=4` | 3 | `(2D,4D]` | 0.021532 | 0.014905 | 0.319858 |
| 83561 | `balanced<=2` | 2 | `(D,2D]` | 0.021477 | 0.013649 | 0.134782 |

## 4. 最大跨 P 抵消单元

| bucket | omega | shell | profile crude share | cell net share | credit share |
| --- | ---: | --- | ---: | ---: | ---: |
| `balanced<=2` | 3 | `(D,2D]` | 0.101233 | 0.004628 | 0.096605 |
| `far>8` | 4 | `(D,2D]` | 0.061543 | 0.003811 | 0.057731 |
| `balanced<=2` | 4 | `(4D,8D]` | 0.046001 | 0.001726 | 0.044274 |
| `mid<=4` | 3 | `(2D,4D]` | 0.060865 | 0.012615 | 0.048250 |
| `unbalanced<=8` | 3 | `(2D,4D]` | 0.055654 | 0.001851 | 0.053803 |
| `far>8` | 4 | `(2D,4D]` | 0.028938 | 0.003000 | 0.025938 |
| `unbalanced<=8` | 4 | `(D,2D]` | 0.092160 | 0.040538 | 0.051622 |
| `mid<=4` | 4 | `(2D,4D]` | 0.054439 | 0.015235 | 0.039204 |
| `far>8` | 4 | `(4D,8D]` | 0.026900 | 0.003616 | 0.023285 |
| `far>8` | 5 | `(2D,4D]` | 0.021164 | 0.000493 | 0.020671 |
| `balanced<=2` | 4 | `(D,2D]` | 0.041963 | 0.014536 | 0.027427 |
| `mid<=4` | 4 | `(D,2D]` | 0.040673 | 0.008971 | 0.031702 |
| `balanced<=2` | 4 | `(8D,16D]` | 0.028819 | 0.003007 | 0.025812 |
| `mid<=4` | 4 | `(4D,8D]` | 0.052350 | 0.026114 | 0.026236 |
| `unbalanced<=8` | 3 | `(D,2D]` | 0.072313 | 0.041577 | 0.030736 |
| `far>8` | 4 | `(8D,16D]` | 0.023828 | 0.010203 | 0.013624 |

## 5. 证明边界

- 已闭合：每个深度格权函数偏差到 `P`-profile 的精确分解。
- 重要负结果：逐 `P` 独立绝对预算不足以闭合所有 bucket。
- 当前真正剩余：证明跨 `P` profile 抵消，或将持续 profile 偏差登记为 ProfileWeight-PDEC。
- 下一目标：`CrossPProfileCancellationOrProfileWeightPDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-depth-cell-weight-function-router.json` | `7dd039f7fbb0cdd63a3e0267abb40bc1fc674dafb7a9a17b77d1b950b729267d` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-kernel-depth-cancellation-router.json` | `7db79319df6fa99cbb2fd1c49d0b877ea1aac2b662dd73eadc89354b35d6925c` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_weight_profile_cancellation_router.py` | `b956e50b39144d7d79e41d70f96a730de12aae8854d445a7acbdbb311010dcc6` |
