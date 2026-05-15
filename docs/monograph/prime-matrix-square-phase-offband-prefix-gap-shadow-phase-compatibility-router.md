# Prime Matrix square-phase off-band prefix gap shadow phase compatibility router

**状态：** `local_phase_compatibility_checked_column_phase_density_open`

本步把兼容 CRT 覆盖词放回固定 small-k/band 相位窗口中检验。每个 selected cell 的 k/band 条件都给出显式 P 窗口；有限前沿 11 个包全部存在与该窗口相交的完整覆盖词。因此局部相位窗口本身不能推出矛盾，剩余必须提升到列相位/密度层：排斥这些兼容覆盖词在同一反例链中持久对齐，或给出 PDEC/ColumnCRT 证书。

```text
record_count=11
local_phase_alone_exclusion_count=0
all_packets_have_phase_compatible_cover_words=true
prime_phase_compatible_packet_count=6
max_phase_compatible_cover_word_count=35
row_column_unconditional_closed=false
```

## 1. 相位窗口

固定 `k` 与 `band` 后，`b_lo..b_hi` 中每个 b 都给出 P 的上下界；取交得到同一个整数窗口。然后把每个完整 CRT 覆盖词的同余类与该窗口求交。

## 2. 兼容性前沿

| P | side | b cell | parent atom | P window | phase-compatible words | prime-compatible words | example |
| ---: | --- | --- | --- | --- | ---: | ---: | --- |
| 733 | `plus` | `23-26` | `minus_only_noslot:k1:681-687` | `729-736` | `4` | `0` | `{'labels': [3, 11, 17, 3], 'residue': 169, 'modulus': 561, 'sample_p': 730}` |
| 523 | `plus` | `12-15` | `minus_only_noslot:k0:493-499` | `481-576` | `6` | `6` | `{'labels': [5, 11, 3, 7], 'residue': 499, 'modulus': 1155, 'sample_p': 499}` |
| 691 | `minus` | `19-21` | `plus_only_noslot:k1:649-653` | `644-760` | `35` | `4` | `{'labels': [3, 7, 5], 'residue': 47, 'modulus': 105, 'sample_p': 677}` |
| 683 | `plus` | `14-17` | `minus_only_noslot:k0:649-655` | `613-784` | `31` | `6` | `{'labels': [3, 7, 5, 3], 'residue': 37, 'modulus': 105, 'sample_p': 667}` |
| 733 | `plus` | `14-18` | `minus_only_noslot:k0:697-705` | `685-784` | `5` | `0` | `{'labels': [3, 7, 5, 3, 23], 'residue': 772, 'modulus': 2415, 'sample_p': 772}` |
| 673 | `minus` | `25-27` | `plus_only_noslot:k2:619-623` | `648-675` | `6` | `0` | `{'labels': [3, 5, 19], 'residue': 92, 'modulus': 285, 'sample_p': 662}` |
| 733 | `plus` | `23-26` | `minus_only_noslot:k1:681-687` | `729-736` | `4` | `0` | `{'labels': [3, 11, 17, 3], 'residue': 169, 'modulus': 561, 'sample_p': 730}` |
| 313 | `plus` | `15-16` | `minus_only_noslot:k1:281-283` | `289-320` | `10` | `2` | `{'labels': [7, 3], 'residue': 2, 'modulus': 21, 'sample_p': 296}` |
| 1129 | `plus` | `29-32` | `minus_only_noslot:k1:1065-1071` | `1089-1160` | `20` | `2` | `{'labels': [3, 7, 5, 3], 'residue': 67, 'modulus': 105, 'sample_p': 1117}` |
| 691 | `minus` | `19-21` | `plus_only_noslot:k1:649-653` | `644-760` | `35` | `4` | `{'labels': [3, 7, 5], 'residue': 47, 'modulus': 105, 'sample_p': 677}` |
| 673 | `minus` | `25-27` | `plus_only_noslot:k2:619-623` | `648-675` | `6` | `0` | `{'labels': [3, 5, 19], 'residue': 92, 'modulus': 285, 'sample_p': 662}` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `fixed_atom_phase_window_formula` | `closed` | The fixed small-k atom conditions give an explicit integer window for P. |
| `crt_word_phase_compatibility_test` | `closed` | Each complete CRT cover word can be checked for intersection with that phase window. |
| `local_phase_not_enough` | `closed` | The finite frontier has phase-compatible complete cover words, so local phase inequalities alone do not yield contradiction. |
| `prime_phase_examples_exist` | `finite_evidence` | Some packets even have prime representatives in phase-compatible CRT classes; this is evidence that the remaining issue is distributional. |
| `global_column_phase_density_exclusion` | `open` | A proof still needs to rule out persistent compatible cover words through column phase, density, or PDEC mechanisms. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FixedPhaseWindowFormulaClosed` | `true` | `true` | 固定 small-k/band 条件已转成显式 P 窗口。 | closed |
| `LocalPhaseExclusionAttemptResolved` | `true` | `true` | 相位窗口内仍有兼容覆盖词；局部相位本身不足以闭合。 | closed |
| `FinitePrimeCompatibleExamples` | `true` | `false` | 有限前沿存在带素数代表的兼容类；提示剩余是密度/列相位排斥。 | finite evidence only |
| `GlobalColumnPhaseDensityExcluded` | `false` | `false` | 仍需排斥兼容 CRT 覆盖词在列相位中持久对齐。 | ColumnPhaseDensityExclusionForCompatibleCRTCoverWordsOrPrimeAvoidancePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭局部相位误攻路线，不关闭全局命题。 | ColumnPhaseDensityExclusionForCompatibleCRTCoverWordsOrPrimeAvoidancePDEC |

## 5. 下一步

- 主攻：`ColumnPhaseDensityExclusionForCompatibleCRTCoverWordsOrPrimeAvoidancePDEC`。
- 局部 small-k 相位已经不足以闭合；下一步应直接构造列相位/密度 PDEC 排斥条件。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_phase_compatibility_router.py` | `dc04a453b7fc1f5f5587c1ce1fc7a88ee96c30cf6e4830639fc90fdbb0ce4c06` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_crt_cover_word_router.py` | `b1b979d3f114422ed43c68277ffed63431a65fa81d83943d39f9ca0ed571938d` |
| `data/square-phase-offband-prefix-gap-shadow-crt-cover-word-ledger.json` | `a8d3b86e09fde5f3e5ea2a7b960299762daf0707cb2374d0db37ee5e84e54839` |
| `data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json` | `366bda520b7fbd1a8ad5e8a602af1ffb19daf9b447569fd5110a6f1f4bac8609` |
