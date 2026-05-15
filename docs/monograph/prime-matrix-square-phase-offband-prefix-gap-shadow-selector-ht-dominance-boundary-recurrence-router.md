# Prime Matrix square-phase off-band prefix gap shadow selector H/T dominance boundary recurrence router

**状态：** `selector_square_window_tail_dominance_boundary_core_isolated_open_global`

本步把平方窗-尾素数支配的低余量边界隔离出来。扩展到 P<=10000 时，prime rho hit 为 612 个，支配失败数为 0；唯一零余量仍在有限边界核内，margin<=1 的最大 P 为 1777。

```text
max_p=10000
prime_rho_hit_count=612
formula_failure_count=0
dominance_failure_count=0
min_margin=0
zero_margin_count=1
margin_le_1_count=7
margin_le_1_distinct_p_values=[157, 173, 1777]
margin_le_1_max_p=1777
recurrent_low_margin_signature_count=2
row_column_unconditional_closed=false
```

## 1. P 区间余量

| P range | hits | min margin | zero margin | margin<=1 | margin<=3 | p at min |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 3..2000 | 150 | 0 | 1 | 7 | 15 | `[173]` |
| 2001..5000 | 194 | 5 | 0 | 0 | 0 | `[2467]` |
| 5001..10000 | 268 | 37 | 0 | 0 | 0 | `[5297]` |

## 2. 低余量对象

| margin | template | p | side | rho | W | H | T | slack | signature |
| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 0 | 4 | 173 | plus | 2 | 1 | 13 | 6 | 0 | `side=plus|W=1|rho=2|template=4` |
| 1 | 1 | 157 | minus | 7 | 2 | 12 | 6 | 1 | `side=minus|W=2|rho=7|template=1` |
| 1 | 2 | 157 | plus | 7 | 1 | 14 | 6 | 1 | `side=plus|W=1|rho=7|template=2` |
| 1 | 3 | 157 | plus | 7 | 1 | 14 | 6 | 1 | `side=plus|W=1|rho=7|template=3` |
| 1 | 6 | 157 | minus | 7 | 2 | 12 | 6 | 1 | `side=minus|W=2|rho=7|template=6` |
| 1 | 2 | 1777 | plus | 7 | 1 | 104 | 51 | 1 | `side=plus|W=1|rho=7|template=2` |
| 1 | 3 | 1777 | plus | 7 | 1 | 104 | 51 | 1 | `side=plus|W=1|rho=7|template=3` |

## 3. 复现签名

| signature | hits | distinct P | P values | min margin | recurrent |
| --- | ---: | ---: | --- | ---: | ---: |
| `side=minus|W=2|rho=7|template=1` | 1 | 1 | `[157]` | 1 | `false` |
| `side=minus|W=2|rho=7|template=6` | 1 | 1 | `[157]` | 1 | `false` |
| `side=plus|W=1|rho=2|template=4` | 1 | 1 | `[173]` | 0 | `false` |
| `side=plus|W=1|rho=7|template=2` | 2 | 2 | `[157, 1777]` | 1 | `true` |
| `side=plus|W=1|rho=7|template=3` | 2 | 2 | `[157, 1777]` | 1 | `true` |

## 4. 结构判断

- 当前扩展扫描仍没有支配失败；这只是有限证据，不是全局证明。
- `margin=0` 是单点边界；`margin<=1` 没有越过当前有限边界核。
- 若低余量签名在高 P 复现，必须进入 BoundaryRecurrence-PDEC/ColumnCRT；若不复现，则剩余是边界核之后的 asymptotic dominance。
- 当前仍未证明全局行/列无条件闭合。

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `finite_low_margin_boundary_isolated` | `closed_on_current_sweep` | Low-margin selector rho hits are isolated and grouped by boundary recurrence signature. |
| `current_no_high_p_margin_le_1_recurrence` | `closed_on_current_sweep` | No margin<=1 hit appears beyond the current finite boundary core in the tested range. |
| `asymptotic_square_window_tail_dominance` | `open` | A global proof must show the dominance margin stays nonnegative beyond the finite boundary core. |
| `low_margin_boundary_recurrence_pdec` | `open` | If low-margin classes recur indefinitely, they must be routed to a boundary recurrence PDEC/ColumnCRT. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CurrentDominanceStillHoldsAtExtendedBound` | `true` | `true` | 扩展有限扫描中平方窗-尾素数支配仍无失败。 | closed on current finite sweep |
| `LowMarginBoundaryCoreIsolated` | `true` | `true` | margin<=1 的边界核已定位并签名化。 | closed on current finite sweep |
| `AsymptoticDominanceProved` | `false` | `false` | 仍需无条件证明边界核之后支配余量不再跌破 0。 | AsymptoticSquareWindowTailDominanceOrLowMarginBoundaryRecurrencePDEC |
| `BoundaryRecurrencePDECExcluded` | `false` | `false` | 若低余量签名高处复现，仍需 PDEC/ColumnCRT 排斥。 | AsymptoticSquareWindowTailDominanceOrLowMarginBoundaryRecurrencePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只隔离边界复现结构，不关闭全局行/列命题。 | AsymptoticSquareWindowTailDominanceOrLowMarginBoundaryRecurrencePDEC |

## 7. 下一步

- 主攻：`AsymptoticSquareWindowTailDominanceOrLowMarginBoundaryRecurrencePDEC`。
- 内部路线：证明边界核之后 selector rho 命中强制平方窗-尾素数支配余量非负。
- PDEC 路线：若低余量签名高处复现，构造对应 BoundaryRecurrence/ColumnCRT 排斥。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_dominance_boundary_recurrence_router.py` | `6e96ce376f5fdc22e74506882343775be363928d0a0f5eb9faba82c22b4709b7` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py` | `5f53bd13fef7ac641fb9bf25f0d67d25e79d4e2d8977b667785fd6c93ded5529` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-ledger.json` | `dcdf4b1ded2c507ba24399bf075a29d392a08c69174fbfcc6aef9dd96a1e5e4b` |
| `data/square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-ledger.json` | `0d6b2d4befb0e16e2e492b06cfb620f0d8c56eebbca0646f668d33f0eb16e12e` |
