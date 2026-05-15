# Prime Matrix square-phase off-band prefix gap shadow bad-P set router

**状态：** `bad_p_set_materialized_actual_prime_avoidance_open`

本步把列相位密度硬点物化为 BadPSet：在每个固定相位 P 窗口内，所有完整 CRT 覆盖词给出一个有限坏 P 集。有限前沿中实际主素数 P 从不落入对应 BadPSet；但 6 个包的 BadPSet 含有其他素数代表，说明素数性加局部相位仍不足以闭合。最新剩余是解释正式反例链中的实际 formal-unit P 为什么全局避开这些坏集，或把持久命中登记为 PDEC/ColumnCRT。

```text
record_count=11
actual_p_in_bad_set_count=0
bad_prime_packet_count=6
max_bad_p_value_count=18
max_bad_p_density_in_phase_window=0.250000
max_bad_prime_value_count=3
row_column_unconditional_closed=false
```

## 1. BadPSet

对每个 selected cell，BadPSet 是固定 `P` 相位窗口中所有能由完整 CRT 覆盖词解释的 `P` 值。若实际主素数 `P` 落入 BadPSet，则该 selected cell 会被小因子标签完全覆盖。

## 2. 坏集前沿

| P | side | P window | bad values | bad primes | actual P bad? | density |
| ---: | --- | --- | ---: | --- | ---: | ---: |
| 733 | `plus` | `729-736` | `2` | `[]` | `false` | `0.250` |
| 523 | `plus` | `481-576` | `3` | `[499, 541, 563]` | `false` | `0.031` |
| 691 | `minus` | `644-760` | `18` | `[677, 709, 727]` | `false` | `0.154` |
| 683 | `plus` | `613-784` | `11` | `[613, 727]` | `false` | `0.064` |
| 733 | `plus` | `685-784` | `2` | `[]` | `false` | `0.020` |
| 673 | `minus` | `648-675` | `2` | `[]` | `false` | `0.071` |
| 733 | `plus` | `729-736` | `2` | `[]` | `false` | `0.250` |
| 313 | `plus` | `289-320` | `6` | `[317]` | `false` | `0.188` |
| 1129 | `plus` | `1089-1160` | `10` | `[1117]` | `false` | `0.139` |
| 691 | `minus` | `644-760` | `18` | `[677, 709, 727]` | `false` | `0.154` |
| 673 | `minus` | `648-675` | `2` | `[]` | `false` | `0.071` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `compatible_words_to_bad_p_set` | `closed` | Phase-compatible CRT cover words define an explicit finite BadPSet inside the phase window. |
| `actual_frontier_prime_avoids_bad_p_set` | `finite_evidence` | The finite frontier actual prime P is not in the local BadPSet for every packet. |
| `local_prime_bad_examples_exist` | `finite_evidence` | Some local BadPSets contain other prime representatives, so primality plus local phase is not enough. |
| `global_actual_prime_avoidance` | `open` | A global proof still needs to explain why the actual formal-unit prime P avoids BadPSet, or route persistent hits to PDEC/ColumnCRT. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `BadPSetMaterialized` | `true` | `true` | 兼容覆盖词已物化成相位窗口内有限坏 P 集。 | closed |
| `ActualFinitePrimeAvoidsBadPSet` | `true` | `false` | 有限前沿的实际 P 都避开坏集；这不是全局证明。 | finite evidence only |
| `LocalPrimeBadExamplesRuleOutLocalClosure` | `true` | `true` | 坏集中存在其他素数代表，说明局部条件不足以闭合。 | closed |
| `GlobalBadPSetAvoidanceClosed` | `false` | `false` | 仍需列相位/密度机制解释实际 formal-unit P 为什么避开坏集。 | ActualPrimeAvoidsLocalBadPSetByColumnPhaseOrBadPSetPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成坏集物化，不关闭全局命题。 | ActualPrimeAvoidsLocalBadPSetByColumnPhaseOrBadPSetPDEC |

## 5. 下一步

- 主攻：`ActualPrimeAvoidsLocalBadPSetByColumnPhaseOrBadPSetPDEC`。
- 需要把 actual formal-unit P 避开 BadPSet 的有限事实升级为结构证明，或给出持久命中时的 PDEC/ColumnCRT 证书。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_bad_p_set_router.py` | `25c726eb6a571e1b2cbadeb35b25a2622ce08edadfa7c0c3ef8f14c2076f413a` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router.py` | `dc04a453b7fc1f5f5587c1ce1fc7a88ee96c30cf6e4830639fc90fdbb0ce4c06` |
| `data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json` | `366bda520b7fbd1a8ad5e8a602af1ffb19daf9b447569fd5110a6f1f4bac8609` |
| `data/square-phase-offband-prefix-gap-shadow-bad-p-set-ledger.json` | `71d8f20aff9da2560c540af14ddc4e99f11bee2be4aedad1a2023b3e0a4133a6` |
