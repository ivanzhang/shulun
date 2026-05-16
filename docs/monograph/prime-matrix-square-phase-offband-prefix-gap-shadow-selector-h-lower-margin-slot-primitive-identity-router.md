# Prime Matrix square-phase off-band prefix gap shadow selector H lower margin slot primitive identity router

**状态：** `margin_slot_primitive_identities_closed_current_sweep_global_bound_open`

本步把 margin/slot 吸收正规形继续压成六个 slot-depth primitive 身份：`fill_left_spare=fill_ell-generator_ell+1`、`generator_left-margin=fill_left_spare`、`generator_right=|delta_u|-1`、`fill_margin=generator_margin+|delta_b|-1`、`fill_left=fill_margin+1`、`phase_bridge_gap=gap_ell+generator_margin`。当前唯一行全部闭合。全局剩余是证明这些 primitive 身份稳定成立，或排斥持久 Primitive-PDEC/SAE。

```text
primitive_row_count=1
unique_primitive_key_count=1
repeated_primitive_key_count=0
all_primitive_identities_closed=true
row_column_unconditional_closed=false
```

## 1. primitive 身份

| gap ell | ell step | margin | db | du | fill spare | gen right | fill margin | bridge | key |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | `29->31` | 15 | -13 | -7 | 3 | 6 | 27 | 46 | `gap=31|eg=29->31|gm=15|db=-13|du=-7|fls=3` |

## 2. 闭合的等式

- `fill_left_spare=fill_ell-generator_ell+1`。
- `generator_left_depth-generator_margin=fill_left_spare`。
- `generator_right_depth=|delta_u|-1`。
- `fill_margin=generator_margin+|delta_b|-1`。
- `fill_left_depth=fill_margin+1`。
- `phase_bridge_gap=gap_ell+generator_margin`。

## 3. 下一步

- 主攻：`SlotDepthPrimitiveIdentityBoundOrPrimitivePDECExclusion`。
- 将这些 primitive 身份转成全局 slot-depth 约束，或登记违反身份的 Primitive-PDEC/SAE。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_margin_slot_primitive_identity_router.py` | `4a86fea6c8a888cf864a595d34e08dd294f0ba25561cb33e127a63b2a73aab44` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-absorption-normal-form-ledger.json` | `10ab00402bb2f21ca1c5e4d7fc089a1a098571b340741e8605bae44968dbbc8c` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-phase-bridge-excess-source-ledger.json` | `3db447d1c8fc9bfb346b90cd809f88f0e21999c6618937f7b798ca17091787bf` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json` | `c4a2bfa9e30b4444723f339d4501c3ea14b97fc62954ac659095bacc80c2d5f1` |
