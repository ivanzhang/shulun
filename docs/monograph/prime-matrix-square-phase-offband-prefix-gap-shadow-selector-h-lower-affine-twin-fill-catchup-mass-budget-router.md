# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin fill catchup mass budget router

**状态：** `affine_twin_fill_catchup_routed_to_new_residue_mass_or_reset_pdec_global_open`

本步把 fill 追赶路线压成二分：每个最小阈值穿越都必须新增 fill residue；若不是新 residue，则立即是重复 residue/reset/ColumnCRT PDEC。若是新 residue，它至少支付 `1/q` 的 fill-side Rankin 质量。当前三个候选若同时穿越，最小新增 fill Rankin 质量为 0.169986671425；当前 fill epoch 最小 spare ratio 为 0.870967741935。因此容量不产生即时矛盾，最新硬点是全局控制 fill residue 到达率或排斥 fill-catchup mass PDEC。

```text
candidate_q_values=[31, 43, 103]
all_current_fill_epochs_can_absorb_minimal_catchup=true
min_extra_fill_required=1
max_extra_fill_required=8
total_min_new_fill_rankin_mass_required_if_all_candidates_cross=23339/137299 ~= 0.169986671425
max_single_candidate_minimal_route_fill_rankin_mass=4/43 ~= 0.093023255814
min_fill_epoch_spare_ratio=0.870967741935
row_column_unconditional_closed=false
```

## 1. fill 追赶预算

| q | route | fill used | min extra fill | fill capacity | unused | min Rankin mass | max route mass | reset dichotomy |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | `MixedCoaccumulationOnly` | 4 | 1 | 31 | 27 | `1/31` ~= 0.032258 | `2/31` ~= 0.064516 | `true` |
| 43 | `FillCatchUpOrMixed` | 2 | 3 | 43 | 41 | `3/43` ~= 0.069767 | `4/43` ~= 0.093023 | `true` |
| 103 | `FillCatchUpOrMixed` | 1 | 7 | 103 | 102 | `7/103` ~= 0.067961 | `8/103` ~= 0.077670 | `true` |

## 2. 二分

```text
minimal threshold crossing
=> fill-side residue increment
=> new residue with Rankin mass 1/q, or repeated residue/reset PDEC.
```

当前容量足以容纳最小追赶，所以这一步不提供即时矛盾；它把硬点精确转成 fill 侧到达率或 reset PDEC。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `fill_catchup_new_residue_or_reset_dichotomy` | `closed` | Every minimal threshold-crossing route requires fill-side growth; each required fill increment is either a new residue carrying Rankin mass 1/q, or a repeated residue and hence a transport/fixed-residue PDEC. |
| `current_fill_capacity_can_absorb_minimal_catchup` | `closed_current_sweep` | The current fill epochs have enough unused residue capacity for the minimal catch-up witnesses; this is not an exclusion, only a capacity diagnosis. |
| `fill_catchup_mass_pdec_routing` | `closed_routing` | If fill catch-up persists, it creates a named fill-side Rankin mass atom; if residue repeats instead, it exits to reset/ColumnCRT PDEC. |
| `global_fill_residue_arrival_bound` | `open` | A self-contained proof still must bound fill-side residue arrival or exclude the fill-catchup mass PDEC family. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `NewFillOrResetDichotomyClosed` | `true` | `true` | fill 侧追赶必须支付新 residue Rankin 质量，或触发重复 residue/reset PDEC。 | closed routing |
| `CurrentFillCapacityAbsorbsMinimalCatchup` | `true` | `false` | 当前容量足够容纳最小追赶，因此容量本身不是矛盾。 | finite evidence only |
| `FillCatchupMassPDECRouted` | `true` | `true` | 持久 fill 追赶已变成明确 Rankin 质量原子或 reset PDEC。 | exclusion still separate |
| `GlobalFillResidueArrivalBoundProved` | `false` | `false` | 仍需全局控制 fill 侧新增 residue 到达，或排斥质量 PDEC。 | AffineTwinFillResidueArrivalBoundOrFillCatchUpMassPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成追赶质量预算二分，不关闭全局行/列命题。 | AffineTwinFillResidueArrivalBoundOrFillCatchUpMassPDECExclusion |

## 5. 下一步

- 主攻：`AffineTwinFillResidueArrivalBoundOrFillCatchUpMassPDECExclusion`。
- 证明方向：给出 fill-side residue arrival 的全局上界，使其不能补齐阈值缺口。
- 失败方向：若 arrival 过密，输出 `FillCatchUpMass-PDEC`；若 residue 重复，输出 reset/ColumnCRT PDEC。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_fill_catchup_mass_budget_router.py` | `d47fc55dc2674302faf552c6f633f58a973db883bc5923a3e8e0eb92b550c859` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier-ledger.json` | `af447a26eec5e39236b523897a32afba579de755c400d642fe6ae18e3a27ac71` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json` | `fa2485f12eee15af77f301d61a720a4d349ce27c4d9b82e3640f58700c143c03` |
