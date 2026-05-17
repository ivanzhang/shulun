# Prime Matrix accepted reset full relief horizon router

**状态：** `full_missing_nonzero_relief_requires_long_post_reset_horizon`

接受 P=9887 的一槽 reset 后，补完全部 35 个缺失非零 residue 直到 step=1192, P=98047, residue=67 才完成；这距离 reset 有 1102 个同步步、88160 的 P 距离，并且期间出现 225 个 repeat prime anchor。因此完整 relief 不是局部容量修补，而是长程 support-motion 义务；若该长程运动不可吸收，则回到 accepted reset-PDEC 排斥。

```text
row_column_unconditional_closed=false
previous_hardpoint=AcceptedResetPDECExclusionOrDelayedReliefSupportMotionSAE
missing_nonzero_count_at_reset=35
reset_step=90
reset_p=9887
first_relief=(step=115,P=11887,residue=30)
full_relief=(step=1192,P=98047,residue=67)
full_relief_step_gap_after_reset=1102
full_relief_p_gap_after_reset=88160
repeat_prime_anchor_count_until_full_relief=225
new_relief_prime_anchor_count_until_full_relief=35
composite_missing_candidate_count_until_full_relief=101
full_relief_extension_over_epoch_width=17.474906514466
next_direct_attack_target=AcceptedResetPDECExclusionOrLongReliefHorizonSupportMotionSAE
```

## 1. new relief rows

| # | step | P | residue |
| ---: | ---: | ---: | ---: |
| 1 | 115 | 11887 | 30 |
| 2 | 123 | 12527 | 31 |
| 3 | 129 | 13007 | 14 |
| 4 | 133 | 13327 | 50 |
| 5 | 135 | 13487 | 68 |
| 6 | 136 | 13567 | 6 |
| 7 | 139 | 13807 | 33 |
| 8 | 151 | 14767 | 70 |
| 9 | 165 | 15887 | 54 |
| 10 | 174 | 16607 | 64 |
| 11 | 178 | 16927 | 29 |
| 12 | 189 | 17807 | 57 |
| 13 | 192 | 18047 | 13 |
| 14 | 196 | 18367 | 49 |
| 15 | 213 | 19727 | 60 |
| 16 | 217 | 20047 | 25 |
| 17 | 220 | 20287 | 52 |
| 18 | 237 | 21647 | 63 |
| 19 | 238 | 21727 | 1 |
| 20 | 246 | 22367 | 2 |
| 21 | 280 | 25087 | 24 |
| 22 | 282 | 25247 | 42 |
| 23 | 300 | 26687 | 62 |
| 24 | 322 | 28447 | 47 |
| 25 | 358 | 31327 | 16 |
| 26 | 361 | 31567 | 43 |
| 27 | 382 | 33247 | 19 |
| 28 | 436 | 37567 | 8 |
| 29 | 487 | 41647 | 41 |
| 30 | 532 | 45247 | 20 |
| 31 | 634 | 53407 | 15 |
| 32 | 694 | 58207 | 58 |
| 33 | 792 | 66047 | 17 |
| 34 | 1053 | 86927 | 23 |
| 35 | 1192 | 98047 | 67 |

## 2. 判定

- 首个 relief 已经在 reset 之后，完整 relief 更远到 `P=98047`。
- 到完整 relief 前共有 `225` 个 repeat prime-anchor，不提供新增缺失 residue 容量。
- 形式上命中缺失 residue 但为合数的候选也有 `101` 个，不能计入 actual load。
- 因此当前剩余转为 accepted reset-PDEC 排斥，或长程 support-motion SAE 吸收。
- 下一主攻点：`AcceptedResetPDECExclusionOrLongReliefHorizonSupportMotionSAE`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-two-residue-spare-prime-anchor-filter-ledger.json` | `d3d3ef44e7f59396feb07cbbc0baddda7b986c1fcdee64f403bae838d7e5284b` |
| `data/prime-matrix-cross-carrier-fifty-unit-residue-saturation-ledger.json` | `700cecf965360332bed795ea9148abdf80d2b5ad99a658bbe06695da41e5b9cb` |
| `data/prime-matrix-one-slot-reset-prefix-no-relief-ledger.json` | `0c6eabb1626ae9e9b5df333aa1edf9594bc512a9de00c44fa5bdcbd2438f79fb` |
