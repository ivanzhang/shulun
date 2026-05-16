# Prime Matrix square-phase off-band prefix gap shadow selector H lower singleton Rankin budget router

**状态：** `singleton_rankin_budget_localized_one_slot_occupancy_open`

本步把 singleton Rankin 质量拆成预算：总质量 4.328474 中，一槽贡献 4.291750，二槽贡献 0.036725，二槽占比 0.8484%。`P` 壳层质量最大 0.668699，没有观察到单调衰减；因此主硬点不是二槽尾项，而是一槽低模占用率的全局衰减/吸收。

```text
singleton_count=300
singleton_rankin_mass_total=4.328474445644
one_slot_mass=4.291749690880
two_slot_mass=0.036724754764
two_slot_mass_share=0.008484
shell_mass_monotone_decreasing=false
row_column_unconditional_closed=false
```

## 1. 证书大小预算

| size | count | Rankin mass | share | modulus range |
| ---: | ---: | ---: | ---: | --- |
| 1 | 257 | 4.291749690880 | 0.991516 | `23..109` |
| 2 | 43 | 0.036724754764 | 0.008484 | `323..4087` |

## 2. P 壳层预算

| P shell | count | mass | mass/1000P | one-slot mass | two-slot mass |
| --- | ---: | ---: | ---: | ---: | ---: |
| `2001..3000` | 43 | 0.484548 | 0.484548 | 0.457750 | 0.026798 |
| `3001..4000` | 42 | 0.666408 | 0.666408 | 0.659113 | 0.007295 |
| `4001..5000` | 39 | 0.668699 | 0.668699 | 0.666387 | 0.002312 |
| `5001..6000` | 34 | 0.548374 | 0.548374 | 0.548055 | 0.000320 |
| `6001..7000` | 36 | 0.634173 | 0.634173 | 0.634173 | 0.000000 |
| `7001..8000` | 36 | 0.492771 | 0.492771 | 0.492771 | 0.000000 |
| `8001..9000` | 34 | 0.415267 | 0.415267 | 0.415267 | 0.000000 |
| `9001..10000` | 36 | 0.418234 | 0.418234 | 0.418234 | 0.000000 |

## 3. 一槽 ell 档预算

| ell band | count | distinct ell | mass | avg mass/ell |
| --- | ---: | ---: | ---: | ---: |
| `0..31` | 14 | 3 | 0.471732 | 0.157244 |
| `32..43` | 39 | 3 | 0.969616 | 0.323205 |
| `44..53` | 28 | 2 | 0.559615 | 0.279807 |
| `54..61` | 34 | 2 | 0.564601 | 0.282301 |
| `62..71` | 40 | 2 | 0.575152 | 0.287576 |
| `72..83` | 44 | 3 | 0.559436 | 0.186479 |
| `84..101` | 45 | 3 | 0.468097 | 0.156032 |
| `102..1000000000` | 13 | 3 | 0.123502 | 0.041167 |

## 4. 最大一槽占用

| side | ell | count | occupancy | mass | p range | residues |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `minus` | 71 | 22 | 0.309859 | 0.309859 | `4177..9257` | `[3, 9, 10, 12, 18, 21, 22, 26, 27, 28, 34, 35, 36, 37, 39, 40]` |
| `minus` | 43 | 12 | 0.279070 | 0.279070 | `2137..9397` | `[1, 3, 9, 11, 12, 19, 20, 23, 25, 26, 30, 41]` |
| `minus` | 61 | 13 | 0.213115 | 0.213115 | `3187..8237` | `[2, 3, 6, 9, 15, 17, 27, 34, 42, 50, 52, 54, 58]` |
| `minus` | 53 | 11 | 0.207547 | 0.207547 | `3137..6607` | `[3, 4, 6, 8, 10, 14, 18, 35, 46, 47, 51]` |
| `minus` | 41 | 8 | 0.195122 | 0.195122 | `2087..8837` | `[1, 4, 17, 22, 31, 32, 33, 37]` |
| `minus` | 37 | 7 | 0.189189 | 0.189189 | `2027..6967` | `[11, 16, 17, 28, 29, 32, 35]` |
| `minus` | 59 | 10 | 0.169492 | 0.169492 | `3257..7877` | `[12, 13, 18, 30, 34, 35, 43, 45, 46, 53]` |
| `plus` | 37 | 6 | 0.162162 | 0.162162 | `2917..9787` | `[19, 24, 29, 31, 32, 35]` |
| `minus` | 31 | 5 | 0.161290 | 0.161290 | `2837..4357` | `[15, 16, 17, 18, 26]` |
| `minus` | 67 | 10 | 0.149254 | 0.149254 | `3967..9127` | `[13, 14, 15, 29, 37, 42, 45, 47, 60, 64]` |
| `minus` | 47 | 7 | 0.148936 | 0.148936 | `2357..6857` | `[7, 16, 25, 26, 32, 33, 42]` |
| `plus` | 79 | 11 | 0.139241 | 0.139241 | `5639..7417` | `[6, 23, 24, 26, 29, 30, 38, 42, 44, 49, 70]` |
| `plus` | 61 | 8 | 0.131148 | 0.131148 | `3257..5227` | `[16, 20, 24, 40, 42, 46, 53, 55]` |
| `plus` | 31 | 4 | 0.129032 | 0.129032 | `2767..6569` | `[8, 9, 12, 28]` |
| `plus` | 47 | 6 | 0.127660 | 0.127660 | `2063..9473` | `[19, 26, 37, 40, 42, 44]` |
| `minus` | 79 | 10 | 0.126582 | 0.126582 | `5197..8887` | `[12, 15, 25, 26, 31, 35, 39, 45, 62, 67]` |
| `minus` | 89 | 11 | 0.123596 | 0.123596 | `7307..9887` | `[8, 9, 10, 18, 24, 31, 32, 33, 48, 73, 81]` |
| `minus` | 73 | 9 | 0.123288 | 0.123288 | `4337..8597` | `[1, 4, 6, 22, 27, 30, 45, 48, 56]` |

## 5. 结构判断

- 二槽 Rankin 质量当前不足 1%，不是主瓶颈。
- P 壳层质量未显示单调衰减，不能把样本剖面直接外推为全局可求和。
- 主硬点压缩为一槽低模 occupancy 的全局衰减，或由 transport reset-PDEC 吸收。

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `singleton_rankin_budget_identity` | `closed` | Singleton Rankin mass is exactly decomposed by certificate size, P-shell, and one-slot ell bands. |
| `two_slot_rankin_mass_small_current_sweep` | `closed_on_current_sweep` | Two-slot singleton mass is small in the current sweep because its CRT modulus is a product of two primes. |
| `one_slot_low_mod_occupancy_decay_open` | `open` | The dominant one-slot low-mod occupancy must be shown to decay or be absorbed by transport reset-PDEC/SAE. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `RankinBudgetIdentityClosed` | `true` | `true` | singleton Rankin 质量已被证书大小、P 壳层、ell 档精确拆分。 | closed |
| `TwoSlotMassSmallCurrentSweep` | `true` | `false` | 二槽质量当前不足总质量 1%，主硬点不在二槽。 | finite evidence only |
| `ShellMassDecayObserved` | `false` | `false` | 1000 宽 P 壳层质量没有单调衰减，不能从样本直接推出可求和。 | one-slot occupancy decay needed |
| `OneSlotLowModOccupancyBoundProved` | `false` | `false` | 一槽低模占用率是主质量来源，仍需全局不等式。 | OneSlotLowModOccupancyDecay |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只定位 Rankin 质量瓶颈，不关闭全局命题。 | OneSlotLowModOccupancyDecayOrTransportResetPDECExclusion |

## 8. 下一步

- 主攻：`OneSlotLowModOccupancyDecayOrTransportResetPDECExclusion`。
- 证明一槽低模 occupancy 随尺度衰减，或将反复占用转入 transport reset-PDEC。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_rankin_budget_router.py` | `34d2823164a17d5abbb5779182b72d5639569fa575cf9c6a23e2862305df6c0d` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_residue_sae_profile_router.py` | `b0c8c4981326d393ce93cd7256bb00ef2ee55eda8d87f8649bdad67cebcd12bd` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json` | `60a85b991523e1af0bdb40c950945b3db3163d1132d1ff441e8ccbc46ade0ac6` |
