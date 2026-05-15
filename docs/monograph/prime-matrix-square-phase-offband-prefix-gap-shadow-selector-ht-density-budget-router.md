# Prime Matrix square-phase off-band prefix gap shadow selector H/T density budget router

**状态：** `selector_square_window_tail_dominance_reduced_to_positive_density_surplus_open_global`

本步把 asymptotic dominance 压成正密度余量输入：若在 selector rho 命中上 `H-2T>=0.01P/logP` 对 `P>=2001` 成立，则常数项也被压过，平方窗-尾素数支配随之闭合。当前有限数据支持该预算，但全局正密度余量尚未证明。

```text
max_p=10000
density_c=0.01
p0=2001
prime_rho_hit_count=612
formula_failure_count=0
dominance_failure_count=0
min_density_surplus_coeff_after_p0=0.012664382839934102
current_density_input_failure_count_at_p0=0
density_floor_closure_failure_count_at_p0=0
row_column_unconditional_closed=false
```

## 1. 充分条件

当前支配余量是

```text
margin = H - 2T - (3-2W).
```

若对边界核之后的 selector rho 命中有

```text
H - 2T >= c P/log P
c P/log P >= 3-2W,
```

则 `margin>=0`。由于 `W=1` 是唯一正常数项，`c=0.01,P0=2001` 已使 `cP/logP>1`，足以压过常数项。

## 2. P 区间密度系数

| P range | hits | min coeff | avg coeff | min margin | p at min coeff |
| --- | ---: | ---: | ---: | ---: | --- |
| 3..2000 | 150 | 0.0 | 0.11856640488956524 | 0 | `[157]` |
| 2001..5000 | 194 | 0.012664382839934102 | 0.10104411254509303 | 5 | `[2467]` |
| 5001..10000 | 268 | 0.05827756323496374 | 0.09883626645316967 | 37 | `[5297]` |

## 3. P0 预算

| P0 | hits | c | min coeff | c-input failures | floor failures | sufficient if global input proved |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 3 | 612 | 0.01 | 0.0 | 6 | 13 | `false` |
| 157 | 605 | 0.01 | 0.0 | 6 | 13 | `false` |
| 173 | 599 | 0.01 | 0.008421701551102589 | 4 | 11 | `false` |
| 1777 | 479 | 0.01 | 0.008421701551102589 | 2 | 0 | `true` |
| 2001 | 462 | 0.01 | 0.012664382839934102 | 0 | 0 | `true` |
| 5001 | 268 | 0.01 | 0.05827756323496374 | 0 | 0 | `true` |

## 4. 最低系数样本

| coeff | template | p | side | rho | W | H | T | H-2T | margin |
| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.0 | 1 | 157 | minus | 7 | 2 | 12 | 6 | 0 | 1 |
| 0.0 | 6 | 157 | minus | 7 | 2 | 12 | 6 | 0 | 1 |
| 0.008421701551102589 | 2 | 1777 | plus | 7 | 1 | 104 | 51 | 2 | 1 |
| 0.008421701551102589 | 3 | 1777 | plus | 7 | 1 | 104 | 51 | 2 | 1 |
| 0.009627284007255946 | 0 | 677 | minus | 2 | 2 | 45 | 22 | 1 | 2 |
| 0.009627284007255946 | 5 | 677 | minus | 2 | 2 | 45 | 22 | 1 | 2 |
| 0.012664382839934102 | 6 | 2467 | minus | 7 | 2 | 136 | 66 | 4 | 5 |
| 0.016256238208738977 | 2 | 1327 | plus | 7 | 1 | 79 | 38 | 3 | 2 |
| 0.016256238208738977 | 3 | 1327 | plus | 7 | 1 | 79 | 38 | 3 | 2 |
| 0.02978781268495826 | 4 | 173 | plus | 2 | 1 | 13 | 6 | 1 | 0 |
| 0.02991390221576325 | 6 | 1747 | minus | 7 | 2 | 107 | 50 | 7 | 8 |
| 0.032512476417477953 | 1 | 1327 | minus | 7 | 2 | 82 | 38 | 6 | 7 |

## 5. 结构判断

- 这一步没有证明短区间素数定理；它只把所需输入精确压成 selector 条件下的正密度余量。
- 普通 BHP/Legendre/RH-PNT 仍不能直接替代该输入；需要同形状的 `H-2T` 正密度证明。
- 若无法证明正密度余量，则必须继续沿低余量签名做 BoundaryRecurrence-PDEC/ColumnCRT 排斥。
- 当前仍未证明全局行/列无条件闭合。

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `positive_density_surplus_sufficient_condition` | `closed` | If H-2T>=cP/logP beyond P0 and cP/logP>=3-2W, then the dominance margin is nonnegative. |
| `current_density_budget_supports_c001_after_2001` | `closed_on_current_sweep` | The finite sweep supports c=0.01 after P0=2001, but this is not a global proof. |
| `selector_positive_density_square_window_surplus` | `open` | A global proof must establish H-2T>=cP/logP on selector rho hits beyond the finite boundary core. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `DensitySurplusSufficientConditionClosed` | `true` | `true` | 正密度余量输入足以推出平方窗-尾素数支配。 | closed |
| `CurrentC001P0Support` | `true` | `true` | 当前有限数据支持 c=0.01, P0=2001。 | finite evidence only |
| `GlobalPositiveDensitySurplusProved` | `false` | `false` | 仍需证明 selector rho 命中上 H-2T 有固定正密度级下界。 | SelectorPositiveDensitySquareWindowSurplusInputOrBoundaryRecurrencePDEC |
| `BoundaryRecurrencePDECExcluded` | `false` | `false` | 若低余量签名高处复现，仍需 PDEC/ColumnCRT 排斥。 | SelectorPositiveDensitySquareWindowSurplusInputOrBoundaryRecurrencePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只给出充分条件和有限预算，不关闭全局行/列命题。 | SelectorPositiveDensitySquareWindowSurplusInputOrBoundaryRecurrencePDEC |

## 8. 下一步

- 主攻：`SelectorPositiveDensitySquareWindowSurplusInputOrBoundaryRecurrencePDEC`。
- 内部路线：证明 selector rho 命中强制 `H-2T>=cP/logP`。
- PDEC 路线：若正密度输入失败，则低余量签名必须长期复现并进入 BoundaryRecurrence/ColumnCRT。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_density_budget_router.py` | `2cdf49886e62f706834bbbe18459e8afdb4c2c1fb653b7e9133aa54dcb52918e` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py` | `5f53bd13fef7ac641fb9bf25f0d67d25e79d4e2d8977b667785fd6c93ded5529` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_dominance_boundary_recurrence_router.py` | `6e96ce376f5fdc22e74506882343775be363928d0a0f5eb9faba82c22b4709b7` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-ledger.json` | `0d6b2d4befb0e16e2e492b06cfb620f0d8c56eebbca0646f668d33f0eb16e12e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-density-budget-ledger.json` | `458949cc7734f7b82044bd47fbda6fb60dfb870b80e6c925d3b259894b18b57b` |
