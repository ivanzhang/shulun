# Prime Matrix square-phase off-band prefix gap shadow selector H lower primitive affine collapse router

**状态：** `primitive_affine_collapse_closed_current_sweep_global_bound_open`

本步把当前唯一 primitive 身份组压成仿射整数型：`fill_ell=gap`、`generator_ell=gap-2`、`margin=(gap-1)/2`、`|delta_b|=(gap-5)/2`、`|delta_u|=(gap-3)/4`。当前行全部闭合。全局剩余是证明此类仿射塌缩受全局约束，或排斥持久 Affine-PDEC/SAE。

```text
affine_row_count=1
unique_affine_key_count=1
repeated_affine_key_count=0
all_affine_collapse_identities_closed=true
row_column_unconditional_closed=false
```

## 1. 仿射塌缩行

| gap ell | ell step | margin | |db| | |du| | rho jump | key |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 31 | `29->31` | 15 | 13 | 7 | 5 | `gap=31|ell=29->31|m=15|db=13|du=7` |

## 2. 闭合的仿射身份

- `fill_ell=gap_ell`。
- `generator_ell=gap_ell-2`。
- `generator_margin=(gap_ell-1)/2`。
- `|delta_b|=(gap_ell-5)/2`。
- `|delta_u|=(gap_ell-3)/4`。
- `rho_jump=2*(fill_ell-generator_ell)+1`。

## 3. 下一步

- 主攻：`PrimitiveAffineCollapseGlobalBoundOrAffinePDECExclusion`。
- 证明这种仿射塌缩无法持久复现，或把复现登记为 Affine-PDEC/SAE。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_primitive_affine_collapse_router.py` | `260ccacab0d4d426ba5097cc63aacf39fd731c0236ab55c32fe3e003c0b29938` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-margin-slot-primitive-identity-ledger.json` | `c4a2bfa9e30b4444723f339d4501c3ea14b97fc62954ac659095bacc80c2d5f1` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-ledger.json` | `ffe10c92b29452a7e91fee637f355909cbbf890e61a75c270f82b7bf913722ec` |
