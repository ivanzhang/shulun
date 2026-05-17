# Prime Matrix one-slot reset prefix no-relief router

**状态：** `accepted_reset_has_no_missing_nonzero_relief_prefix`

若不切断 endpoint，则 P=9887 的一槽 reset 已先于任何新缺失非零 residue relief 出现。即使接受该 reset，直到 step=115, P=11887, residue=30 才出现第一个真实 relief；在 reset 到 relief 之前的前缀中，所有实际素数锚均为已见 residue，prefix_new_missing_nonzero_count=0。因此当前反例链若要取得新容量，必须先承担 accepted reset-PDEC；若拒绝 reset，则只能回到无 payload endpoint SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=OneSlotResetPDECExclusionOrNoPayloadEndpointSAESummability
reset_step=90
reset_p=9887
reset_residue=18
endpoint_cut_actual_payload_empty=true
prefix_prime_anchor_count_before_first_relief=7
prefix_new_missing_nonzero_count_before_first_relief=0
prefix_repeat_prime_anchor_count_before_first_relief=7
first_relief_step_gap_after_reset=25
first_relief_p_gap_after_reset=2000
first_relief_requires_accepted_reset_pdec=true
next_direct_attack_target=AcceptedResetPDECExclusionOrDelayedReliefSupportMotionSAE
```

## 1. reset 后首个 relief 前缀

| step | P | residue | prime P | route |
| ---: | ---: | ---: | --- | --- |
| 90 | 9887 | 18 | `true` | `repeat_prime_anchor_no_relief` |
| 91 | 9967 | 27 | `true` | `repeat_prime_anchor_no_relief` |
| 92 | 10047 | 36 | `false` | `composite_no_payload` |
| 93 | 10127 | 45 | `false` | `composite_no_payload` |
| 94 | 10207 | 54 | `false` | `composite_no_payload` |
| 95 | 10287 | 63 | `false` | `composite_no_payload` |
| 96 | 10367 | 1 | `false` | `composite_no_payload` |
| 97 | 10447 | 10 | `false` | `composite_no_payload` |
| 98 | 10527 | 19 | `false` | `composite_no_payload` |
| 99 | 10607 | 28 | `true` | `repeat_prime_anchor_no_relief` |
| 100 | 10687 | 37 | `true` | `repeat_prime_anchor_no_relief` |
| 101 | 10767 | 46 | `false` | `composite_no_payload` |
| 102 | 10847 | 55 | `true` | `repeat_prime_anchor_no_relief` |
| 103 | 10927 | 64 | `false` | `composite_no_payload` |
| 104 | 11007 | 2 | `false` | `composite_no_payload` |
| 105 | 11087 | 11 | `true` | `repeat_prime_anchor_no_relief` |
| 106 | 11167 | 20 | `false` | `composite_no_payload` |
| 107 | 11247 | 29 | `false` | `composite_no_payload` |
| 108 | 11327 | 38 | `false` | `composite_no_payload` |
| 109 | 11407 | 47 | `false` | `composite_no_payload` |
| 110 | 11487 | 56 | `false` | `composite_no_payload` |
| 111 | 11567 | 65 | `false` | `composite_no_payload` |
| 112 | 11647 | 3 | `false` | `composite_no_payload` |
| 113 | 11727 | 12 | `false` | `composite_no_payload` |
| 114 | 11807 | 21 | `true` | `repeat_prime_anchor_no_relief` |
| 115 | 11887 | 30 | `true` | `first_missing_nonzero_relief` |

## 2. 判定

- `P=9887` 已经是一槽 repeat reset，不是新增 missing residue 覆盖。
- 从 reset 到首个 relief 前，实际素数锚全部落在已见 residue 中。
- 第一个新增缺失非零 residue relief 是 `step=115, P=11887, residue=30`。
- 因而新容量路径必须先接受 reset-PDEC；拒绝 reset 的路径仍是 no-payload endpoint SAE。
- 下一主攻点：`AcceptedResetPDECExclusionOrDelayedReliefSupportMotionSAE`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json` | `d3d3ef44e7f59396feb07cbbc0baddda7b986c1fcdee64f403bae838d7e5284b` |
| `data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json` | `700cecf965360332bed795ea9148abdf80d2b5ad99a658bbe06695da41e5b9cb` |
| `data/prime-matrix-prime-anchor-repeat-reset-atom-ledger.json` | `5a4de3905509dad8ed93f756c290e711d5a13521fef4398c599ff806663ae0ee` |
| `data/prime-matrix-endpoint-cut-no-payload-sae-ledger.json` | `c760c58b89fcb3ddea5e188cf83fc23abd82957c06288cc5642b497106e0e127` |
