# Prime Matrix endpoint cut zero-gain router

**状态：** `endpoint_cut_before_reset_has_zero_prime_anchor_gain`

若为避免 P=9887 的 one-slot reset 而在首个 post-band 素数锚前切断端点，端点外延区间 step=83..89 没有任何实际素数锚。其中 residue 62 与 0 只是形式缺口，实际 P=9647 与 P=9727 均为合数/被 71 整除。因此 endpoint cut 分支在当前 primitive epoch 内是零收益 SAE 形态；若不切断，则 step=90 的 P=9887 立即实例化 one-slot reset-PDEC。

```text
row_column_unconditional_closed=false
previous_hardpoint=OneSlotPrimeAnchorRepeatResetPDECExclusionOrEndpointMotionSAE
cut_buffer_step_count=7
formal_gap_composite_row_count=2
formal_gap_composite_residues=[62, 0]
actual_prime_anchor_count_before_reset=0
actual_new_prime_anchor_count_before_reset=0
endpoint_cut_actual_gain_zero=true
reset_atom_instantiated_at_first_prime_anchor=true
reset_or_zero_gain_endpoint_dichotomy_closed_current_epoch=true
next_direct_attack_target=ZeroGainEndpointCutSAEOrOneSlotResetPDECExclusion
```

## 1. endpoint cut buffer

| step | P | residue | prime P | smallest factor | route |
| ---: | ---: | ---: | --- | ---: | --- |
| 83 | 9327 | 26 | `false` | 3 | `old_residue_composite_anchor` |
| 84 | 9407 | 35 | `false` | 23 | `old_residue_composite_anchor` |
| 85 | 9487 | 44 | `false` | 53 | `old_residue_composite_anchor` |
| 86 | 9567 | 53 | `false` | 3 | `old_residue_composite_anchor` |
| 87 | 9647 | 62 | `false` | 11 | `formal_gap_but_composite_anchor` |
| 88 | 9727 | 0 | `false` | 71 | `formal_gap_but_composite_anchor` |
| 89 | 9807 | 9 | `false` | 3 | `old_residue_composite_anchor` |

## 2. first prime anchor after buffer

| step | P | residue | route |
| ---: | ---: | ---: | --- |
| 90 | 9887 | 18 | `prime_anchor_repeat_reset` |

## 3. 判定

- `step=83..89` 是端点切断前唯一可用缓冲，实际素数锚数为 0。
- `residue 62` 与 `residue 0` 是形式缺口，但对应 `P=9647,9727` 都不是素数锚。
- 若端点不切断，`step=90,P=9887` 立刻进入已实例化的一槽 repeat-reset 原子。
- 因此当前 epoch 内的二分是：`reset-PDEC` 或 `zero-gain endpoint cut SAE`。
- 下一主攻点：`ZeroGainEndpointCutSAEOrOneSlotResetPDECExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-prime-anchor-repeat-reset-atom-ledger.json` | `5a4de3905509dad8ed93f756c290e711d5a13521fef4398c599ff806663ae0ee` |
| `data/prime-matrix-prime-anchor-postband-immediate-repeat-ledger.json` | `29b4a6143fb6056fa230d88c0bf015b440922b463fea68b12c02adf5149f2051` |
