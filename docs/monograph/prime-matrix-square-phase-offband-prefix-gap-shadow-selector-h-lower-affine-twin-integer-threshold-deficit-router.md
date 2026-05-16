# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin integer threshold deficit router

**状态：** `affine_twin_pressure_product_reduced_to_integer_threshold_deficit_global_open`

本步把 `PressureProduct` 门压成纯整数阈值：`A_g*A_f <= floor(sqrt(q(q-2)))`。当前全部候选通过，最小整数乘积缺口为 17，若允许两侧同时新增 residue，最少还需 4 个额外 residue 才能穿越阈值。所有当前候选的 fill 侧激活都晚于 generator 侧，最小延迟为 80。因此最新最窄硬点是：证明这种激活延迟/阈值缺口不能被持久补齐；若被补齐，即得到显式 `ThresholdCrossing-PDEC/ColumnCRT`。

```text
candidate_q_values=[31, 43, 103]
realized_q_values=[31]
all_current_rows_pass_integer_threshold_gate=true
min_integer_product_slack=17
min_total_extra_residues_to_cross=4
all_current_fill_epochs_younger_than_generators=true
min_fill_activation_delay_over_generator=80
row_column_unconditional_closed=false
```

## 1. 整数阈值表

| q | product | threshold | slack | min extra | fill delay | fixed gen fail fill | fixed fill fail gen |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 31 | 12 | 29 | 17 | 4 | 80 | 10 | 8 |
| 43 | 16 | 41 | 25 | 4 | 1610 | 6 | 21 |
| 103 | 12 | 101 | 89 | 8 | 1074 | 9 | 102 |

## 2. 等价式

```text
A_g A_f <= floor(sqrt(q(q-2)))
iff (A_g A_f)^2 <= q(q-2)
iff (A_g^2/(q-2)) * (A_f^2/q) <= 1.
```

阈值穿越不再是定性事件：每个 q 都有明确的最小新增 residue 见证。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `integer_threshold_form_of_pressure_gate` | `closed` | The pressure-product gate is equivalent to A_g A_f <= floor(sqrt(q(q-2))). |
| `current_threshold_deficit_materialized` | `closed_current_sweep` | Every current affine-twin q has positive integer product slack; the smallest multi-side crossing deficit is four additional residues. |
| `activation_delay_diagnosis` | `closed_current_sweep` | In every current candidate, the fill-side epoch activates later than the generator-side epoch, explaining why one-sided generator pressure has not synchronized with fill pressure. |
| `threshold_crossing_pdec_routing` | `closed_routing` | If a future row crosses the integer threshold, it is a named ThresholdCrossing-PDEC/ColumnCRT object with explicit extra-residue witnesses. |
| `global_threshold_deficit_bound` | `open` | A self-contained proof still must show persistent affine-twin rows cannot close the integer threshold deficit, or exclude the crossing PDEC family. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `IntegerThresholdEquivalenceClosed` | `true` | `true` | `PressureProduct` 已无损改写为整数乘积阈值。 | closed |
| `CurrentThresholdDeficitPositive` | `true` | `false` | 当前所有候选 q 距离阈值穿越都有正整数缺口。 | finite evidence only |
| `CurrentFillActivationDelayed` | `true` | `false` | 当前所有候选的 fill 侧晚于 generator 侧激活，给出压力不同步的结构诊断。 | finite structural diagnosis |
| `ThresholdCrossingPDECRouted` | `true` | `true` | 若整数阈值被穿越，失败行有明确的最小 residue 增量见证。 | exclusion still separate |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只压窄为阈值缺口守门项，不关闭全局行/列命题。 | AffineTwinThresholdDeficitBoundOrThresholdCrossingPDECExclusion |

## 5. 下一步

- 主攻：`AffineTwinThresholdDeficitBoundOrThresholdCrossingPDECExclusion`。
- 证明方向：把 fill 侧激活延迟和 residue 到达速率结合，证明阈值缺口不能被持久补齐。
- 失败方向：若缺口被补齐，直接输出带最小新增 residue 见证的 `ThresholdCrossing-PDEC/ColumnCRT`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_integer_threshold_deficit_router.py` | `3800d5061d257b27fd190c7f5100fa323bc3ab6603fc6fe4c66bdea9aa5df813` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json` | `3260f7bb9020052ca7362859c608c3ed7508238ae927c79a4a42712ba09a41a2` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json` | `2e401269ab68cb196babfb74e6f7b63c946ee9de37bc6ab5d502f49deaa7bf28` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json` | `fd9f2939f94e6cbdc92892d6b59a86392b4bd71d4b478c501b870974211f6c4e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-ledger.json` | `4585a4af4e66518873bf3edf31e8b868db6baeaf6d7d9466ad3abafbd8283e0e` |
