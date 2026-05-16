# Prime Matrix square-phase off-band prefix gap shadow selector H lower corridor phase budget router

**状态：** `corridor_phase_budget_identity_closed_current_sweep_global_bound_open`

本步把短走廊不等式分解为精确三分量身份 `p_delay = generator_right_depth + phase_bridge_gap + fill_left_depth`。当前三条身份全部闭合，`3*gap_ell` 最小余量为 13。唯一分量超标发生在 `gap_ell=31` 的 phase bridge，但被另两个深度分量余量吸收。全局剩余是证明三分量预算界，或把 phase bridge 超标登记并排斥为 PhaseBridge-PDEC/SAE。

```text
phase_budget_row_count=3
all_phase_budget_identities_closed=true
all_corridor_3gap_slack_positive=true
min_corridor_3gap_slack=13
max_phase_bridge_gap_over_gap=1.483870967742
all_phase_bridges_within_2gap=true
component_excess_row_count=1
min_other_component_spare_after_excess=13
row_column_unconditional_closed=false
```

## 1. 三分量身份

| gap ell | generator phase | fill phase | gen right | bridge gap | fill left | total | 3gap slack | excess |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 43 | `[2048, 2075]` | `[2115, 2138]` | 12 | 40 | 22 | 74 | 55 | 0 |
| 31 | `[2669, 2693]` | `[2739, 2768]` | 6 | 46 | 28 | 80 | 13 | 15 |
| 59 | `[3177, 3218]` | `[3249, 3274]` | 31 | 31 | 8 | 70 | 107 | 0 |

## 2. 预算解释

- `p_delay` 被完全解释为生成相位右深度、两相位区间间隙、填充相位左深度三项之和。
- `gap_ell=31` 是唯一出现单分量超标的行：phase bridge 超过一个 `gap_ell`，但总预算仍保留 13 余量。
- 若全局出现短走廊失效，必须表现为三分量预算无法吸收的 phase bridge/深度超标，可登记为 PhaseBridge-PDEC/SAE。

## 3. 下一步

- 主攻：`CorridorPhaseBudgetBoundOrPhaseBridgePDECExclusion`。
- 对 phase bridge gap 建立 CRT/slot 控制：证明其总能被左右深度余量吸收，或登记不可吸收超标原子。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_corridor_phase_budget_router.py` | `9c37afc4a4a12b1fa2c380d2a72beb79b62fd2013d41a5559ba2df6813da8016` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-repair-corridor-ledger.json` | `8af116227ee290b0341711947c640d3bceb05b32be2ca833c322aa61900a69bf` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-corridor-phase-budget-ledger.json` | `53a5e2b1c0a7fb57d210885b9719c9aefa93cdaa5e34ff579e9df37187fdb969` |
