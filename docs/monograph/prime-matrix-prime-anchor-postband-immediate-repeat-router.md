# Prime Matrix prime-anchor post-band immediate repeat router

**状态：** `prime_anchor_nonzero_coverage_preempted_by_first_postband_repeat`

在 prime-anchor 过滤后，长 AP 非零 residue 覆盖分支被更早截断：当前 admitted 带后的第一个素数锚就是 P=9887，residue=18，而 18 已在原始 minus:71 已用 residue 集中。因此在同一无 reset epoch 中，反例链无法先补入任何新缺失非零 residue；若 epoch 延伸到该点，立即进入 transport reset-PDEC；若不延伸，则回到 endpoint motion/SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=PrimeAnchorFilteredNonzeroResidueCoverageOrTransportResetPDEC
current_prime_filtered_union_size=35
current_prime_filtered_nonzero_spare=35
first_postband_prime_anchor={'step': 90, 'p': 9887, 'residue': 18, 'is_prime_p': True, 'smallest_factor': None, 'already_in_prime_filtered_union': True, 'already_in_original_used_residues': True}
first_postband_prime_is_repeat=true
first_postband_prime_is_original_used_repeat=true
new_prime_anchor_count_before_first_repeat=0
missing_nonzero_remaining_at_first_repeat=35
repeat_p_extension_beyond_epoch_p_max=630
repeat_extension_over_epoch_width=0.123991340287
coverage_before_reset_possible_in_same_epoch=false
next_direct_attack_target=ImmediatePrimeAnchorRepeatTransportResetPDECOrEndpointMotionSAE
```

## 1. admitted 带后首个素数锚窗口

| step | P | residue | prime P | smallest factor | in filtered union | in original used |
| ---: | ---: | ---: | --- | ---: | --- | --- |
| 83 | 9327 | 26 | `false` | 3 | `true` | `true` |
| 84 | 9407 | 35 | `false` | 23 | `true` | `true` |
| 85 | 9487 | 44 | `false` | 53 | `true` | `true` |
| 86 | 9567 | 53 | `false` | 3 | `true` | `true` |
| 87 | 9647 | 62 | `false` | 11 | `false` | `false` |
| 88 | 9727 | 0 | `false` | 71 | `false` | `false` |
| 89 | 9807 | 9 | `false` | 3 | `true` | `true` |
| 90 | 9887 | 18 | `true` |  | `true` | `true` |

## 2. 判定

- admitted 带后的第一个素数锚是 `P=9887`，步号 `90`，residue `18`。
- 该 residue 已经属于原始 `minus:71` 已用集合，不只是 prime-filtered 合并集合。
- 因此在同一无 reset epoch 中，长 AP 无法先补任何新缺失非零 residue；首次素数锚已经触发旧 residue。
- 若该 epoch 不允许延伸到此点，则出口是 endpoint motion/SAE；若允许延伸，则出口是 transport reset-PDEC。
- 下一主攻点：`ImmediatePrimeAnchorRepeatTransportResetPDECOrEndpointMotionSAE`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json` | `d3d3ef44e7f59396feb07cbbc0baddda7b986c1fcdee64f403bae838d7e5284b` |
| `data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json` | `700cecf965360332bed795ea9148abdf80d2b5ad99a658bbe06695da41e5b9cb` |
