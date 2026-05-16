# Prime Matrix square-phase off-band prefix gap shadow selector H lower margin slot absorption normal form router

**状态：** `margin_slot_absorption_normal_form_closed_current_sweep_global_bound_open`

本步把 phase bridge 超标吸收写成 margin/slot 正规形：`absorbing_depth_spare = generator_margin + |delta_b|`，且 `generator_right_spare = generator_margin + |delta_u| + fill_left_spare`。当前唯一行两个身份均闭合。全局剩余是证明该正规形预算界，或排斥持久 NormalForm-PDEC/SAE。

```text
normal_form_row_count=1
unique_normal_form_key_count=1
repeated_normal_form_key_count=0
all_absorbing_spare_identities_closed=true
all_post_absorption_slack_equals_abs_delta_b=true
all_right_spare_decompositions_closed=true
row_column_unconditional_closed=false
```

## 1. 正规形行

| gap ell | margin | delta b | delta u | absorbing spare | margin+|db| | right spare decomposition | key |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | 15 | -13 | -7 | 28 | 28 | 25 | `gap=31|margin=15|db=-13|du=-7|rho=5` |

## 2. 结构结论

- 超标吸收不再依赖自由三分量预算，而被压成 margin 与槽位位移的两个等式。
- 剩余 slack 精确等于 `|delta_b|`，说明 `b` 槽位移是最终余量来源。
- 全局失败必须破坏这些等式或复现同一 NormalForm-PDEC 键。

## 3. 下一步

- 主攻：`MarginSlotAbsorptionNormalFormBoundOrNormalFormPDECExclusion`。
- 证明 margin/slot 正规形在端点缺口修复中全局成立，或排斥持久正规形原子。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_margin_slot_absorption_normal_form_router.py` | `d67989b01e842a19286a018c9dbd1afb8c1e703bac04e5c1ddb54dd54edf3141` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json` | `3db447d1c8fc9bfb346b90cd809f88f0e21999c6618937f7b798ca17091787bf` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-ledger.json` | `10ab00402bb2f21ca1c5e4d7fc089a1a098571b340741e8605bae44968dbbc8c` |
