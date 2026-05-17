# Prime Matrix prime-anchor repeat reset atom router

**状态：** `one_slot_prime_anchor_repeat_reset_atom_instantiated`

首个 post-band 素数锚 P=9887 与原始 singleton 记录 P=7757 具有同一 minus:71 residue=18，且差值为 2130=30*71。这不是新的 residue 覆盖，而是一个已实例化的一槽 repeat-reset 原子。若同一 epoch 延伸到该点，必须进入 reset-PDEC；若反例链拒绝 reset，端点必须在首个 post-band 素数锚之前切断，转入 endpoint motion/SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=ImmediatePrimeAnchorRepeatTransportResetPDECOrEndpointMotionSAE
original_record_p=7757
repeat_prime_anchor_p=9887
repeat_residue=18
p_delta=2130
p_delta_over_ell=30
exact_same_residue_ell_translate=true
reset_atom_instantiated=true
new_prime_anchor_count_before_first_repeat=0
missing_nonzero_remaining_at_reset_atom=35
endpoint_cut_required_to_avoid_reset=true
next_direct_attack_target=OneSlotPrimeAnchorRepeatResetPDECExclusionOrEndpointMotionSAE
```

## 1. reset atom

| field | value |
| --- | --- |
| `side` | `minus` |
| `ell` | `71` |
| `residue` | `18` |
| `original_p` | `7757` |
| `repeat_p` | `9887` |
| `original_lift` | `109` |
| `repeat_lift` | `139` |
| `lift_delta` | `30` |
| `p_delta` | `2130` |
| `slot_keys` | `['644:128:71']` |
| `formal_unit` | `one-slot-repeat-reset|side=minus|ell=71|residue=18|lift_delta=30|p=7757->9887` |

## 2. endpoint cut alternative

| field | value |
| --- | --- |
| `must_cut_before_step` | `90` |
| `must_cut_before_p` | `9887` |
| `last_admitted_step` | `82` |
| `last_epoch_p_max` | `9257` |
| `step_gap_after_admitted_band` | `8` |
| `p_extension_beyond_epoch_p_max` | `630` |
| `p_extension_beyond_admitted_lattice_p_max` | `640` |
| `composite_buffer_step_count` | `7` |
| `composite_buffer_steps` | `[83, 84, 85, 86, 87, 88, 89]` |
| `composite_buffer_p_values` | `[9327, 9407, 9487, 9567, 9647, 9727, 9807]` |

## 3. 判定

- `9887-7757=2130=30*71`，所以这是同一 residue packet 的整周期平移。
- 在该 repeat 前没有任何新素数锚补入缺失非零 residue。
- 若保持同一无 reset epoch，则 reset-PDEC atom 已经实例化。
- 若避免 reset，则必须在首个 post-band 素数锚前切断，进入 endpoint motion/SAE。
- 下一主攻点：`OneSlotPrimeAnchorRepeatResetPDECExclusionOrEndpointMotionSAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-prime-anchor-postband-immediate-repeat-ledger.json` | `29b4a6143fb6056fa230d88c0bf015b440922b463fea68b12c02adf5149f2051` |
| `data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json` | `700cecf965360332bed795ea9148abdf80d2b5ad99a658bbe06695da41e5b9cb` |
