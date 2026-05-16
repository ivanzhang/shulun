# Prime Matrix square-phase off-band prefix gap shadow selector H lower one-slot residue epoch capacity router

**状态：** `one_slot_epoch_capacity_closed_active_epoch_count_open`

本步把一槽低模 occupancy 写成 reset-free epoch 容量：固定 `(side,ell)` 中，一个无 reset epoch 最多使用 `ell` 个 residue，否则必然重复 residue 并回到 transport reset-PDEC。当前 40 个活跃 epoch 总容量 2674，实际使用 257，未用 2417；最大占用率 0.309859。剩余硬点不是单个 epoch 容量，而是全局活跃 epoch 数量界或 reset-PDEC 排斥。

```text
active_one_slot_epoch_count=40
total_residue_capacity=2674
total_used_residue_count=257
total_unused_residue_count=2417
one_slot_rankin_mass=4.291749690880
max_occupancy_ratio=0.309859154930
min_spare_ratio=0.690140845070
row_column_unconditional_closed=false
```

## 1. epoch 容量行

| side | ell | used | capacity | occupancy | spare | Rankin mass | p range |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `minus` | 71 | 22 | 71 | 0.309859 | 0.690141 | 0.309859 | `4177..9257` |
| `minus` | 43 | 12 | 43 | 0.279070 | 0.720930 | 0.279070 | `2137..9397` |
| `minus` | 61 | 13 | 61 | 0.213115 | 0.786885 | 0.213115 | `3187..8237` |
| `minus` | 53 | 11 | 53 | 0.207547 | 0.792453 | 0.207547 | `3137..6607` |
| `minus` | 41 | 8 | 41 | 0.195122 | 0.804878 | 0.195122 | `2087..8837` |
| `minus` | 37 | 7 | 37 | 0.189189 | 0.810811 | 0.189189 | `2027..6967` |
| `minus` | 59 | 10 | 59 | 0.169492 | 0.830508 | 0.169492 | `3257..7877` |
| `plus` | 37 | 6 | 37 | 0.162162 | 0.837838 | 0.162162 | `2917..9787` |
| `minus` | 31 | 5 | 31 | 0.161290 | 0.838710 | 0.161290 | `2837..4357` |
| `minus` | 67 | 10 | 67 | 0.149254 | 0.850746 | 0.149254 | `3967..9127` |
| `minus` | 47 | 7 | 47 | 0.148936 | 0.851064 | 0.148936 | `2357..6857` |
| `plus` | 79 | 11 | 79 | 0.139241 | 0.860759 | 0.139241 | `5639..7417` |
| `plus` | 61 | 8 | 61 | 0.131148 | 0.868852 | 0.131148 | `3257..5227` |
| `plus` | 31 | 4 | 31 | 0.129032 | 0.870968 | 0.129032 | `2767..6569` |
| `plus` | 47 | 6 | 47 | 0.127660 | 0.872340 | 0.127660 | `2063..9473` |
| `minus` | 79 | 10 | 79 | 0.126582 | 0.873418 | 0.126582 | `5197..8887` |
| `minus` | 89 | 11 | 89 | 0.123596 | 0.876404 | 0.123596 | `7307..9887` |
| `minus` | 73 | 9 | 73 | 0.123288 | 0.876712 | 0.123288 | `4337..8597` |
| `minus` | 83 | 10 | 83 | 0.120482 | 0.879518 | 0.120482 | `5927..9787` |
| `minus` | 101 | 12 | 101 | 0.118812 | 0.881188 | 0.118812 | `8387..9857` |
| `minus` | 97 | 11 | 97 | 0.113402 | 0.886598 | 0.113402 | `7537..8737` |
| `minus` | 29 | 3 | 29 | 0.103448 | 0.896552 | 0.103448 | `2687..6337` |
| `plus` | 41 | 4 | 41 | 0.097561 | 0.902439 | 0.097561 | `2017..6053` |
| `plus` | 53 | 4 | 53 | 0.075472 | 0.924528 | 0.075472 | `3877..5471` |
| `plus` | 67 | 4 | 67 | 0.059701 | 0.940299 | 0.059701 | `6047..8807` |
| `plus` | 71 | 4 | 71 | 0.056338 | 0.943662 | 0.056338 | `5987..9497` |
| `plus` | 97 | 5 | 97 | 0.051546 | 0.948454 | 0.051546 | `8467..9491` |
| `plus` | 59 | 3 | 59 | 0.050847 | 0.949153 | 0.050847 | `5333..7949` |
| `plus` | 101 | 5 | 101 | 0.049505 | 0.950495 | 0.049505 | `9337..9479` |
| `minus` | 103 | 5 | 103 | 0.048544 | 0.951456 | 0.048544 | `8537..9227` |
| `minus` | 107 | 5 | 107 | 0.046729 | 0.953271 | 0.046729 | `9277..9907` |
| `plus` | 43 | 2 | 43 | 0.046512 | 0.953488 | 0.046512 | `3697..7349` |
| `minus` | 23 | 1 | 23 | 0.043478 | 0.956522 | 0.043478 | `4987..4987` |
| `plus` | 83 | 3 | 83 | 0.036145 | 0.963855 | 0.036145 | `5557..7867` |
| `plus` | 29 | 1 | 29 | 0.034483 | 0.965517 | 0.034483 | `3187..3187` |
| `plus` | 73 | 1 | 73 | 0.013699 | 0.986301 | 0.013699 | `8647..8647` |
| `plus` | 89 | 1 | 89 | 0.011236 | 0.988764 | 0.011236 | `7207..7207` |
| `plus` | 103 | 1 | 103 | 0.009709 | 0.990291 | 0.009709 | `9461..9461` |
| `plus` | 107 | 1 | 107 | 0.009346 | 0.990654 | 0.009346 | `9419..9419` |
| `minus` | 109 | 1 | 109 | 0.009174 | 0.990826 | 0.009174 | `9817..9817` |

## 2. 结构判断

- 单个 `(side,ell)` epoch 内的 Rankin 质量至多为 1；溢出会强制 residue 重复。
- 当前所有活跃 epoch 都有大余量，说明局部容量不是瓶颈。
- 全局可求和必须控制活跃 epoch 的数量，或证明活跃 epoch 过多会触发 transport reset-PDEC/SAE。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `one_slot_reset_free_epoch_capacity` | `closed` | For fixed (side, ell), a reset-free epoch has at most ell singleton residues; an overflow forces repeated residue and exits to transport reset-PDEC. |
| `current_one_slot_epoch_has_large_spare_capacity` | `closed_on_current_sweep` | The current one-slot singleton support uses only a small part of the residue capacity in every active (side, ell) epoch. |
| `active_epoch_count_bound_open` | `open` | A global Rankin bound still needs a bound on active one-slot epochs or a proof that excessive epochs trigger transport reset-PDEC/SAE. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `ResetFreeEpochCapacityClosed` | `true` | `true` | 固定 `(side,ell)` 的无 reset epoch 中，singleton residue 数最多为 `ell`。 | closed |
| `CurrentEpochOverflowAbsent` | `true` | `false` | 当前一槽支持远未填满 residue 容量。 | finite evidence only |
| `ActiveEpochCountBoundProved` | `false` | `false` | 全局 Rankin 可求和仍需要控制活跃 `(side,ell)` epoch 数量。 | ActiveOneSlotEpochCountBound |
| `TransportResetPDECExcluded` | `false` | `false` | 若 epoch 过多或 residue 重复，仍需 transport reset-PDEC 排斥。 | TransportResetPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭的是每个 epoch 内的容量，不关闭全局命题。 | ActiveOneSlotEpochCountBoundOrTransportResetPDECExclusion |

## 5. 下一步

- 主攻：`ActiveOneSlotEpochCountBoundOrTransportResetPDECExclusion`。
- 证明活跃 `(side,ell)` epoch 数量有全局界，或证明过多 epoch 必触发 transport reset-PDEC。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_one_slot_residue_epoch_capacity_router.py` | `0fd8da805fe299a4c3aba3910e653086ccb33dc0c0922d5d6be87b3834ed0e2c` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json` | `60a85b991523e1af0bdb40c950945b3db3163d1132d1ff441e8ccbc46ade0ac6` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
