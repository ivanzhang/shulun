# Prime Matrix square-phase off-band prefix gap shadow hull absorption router

**状态：** `fixed_shape_union_supply_reduced_to_hull_count_or_complement_absorption_pdec_open`

本步把固定形状并集素数供给写成精确 hull 分解：`hull primes = target-union primes + complement-pocket primes`，且覆盖缺口候选数就是互补孔袋候选数。若 `hull_prime_count > coverage_defect_candidate_count`，目标并集必含素数；否则反例必须表现为互补孔袋吸收全部 hull 素数的显式 PDEC。有限账本中没有目标并集全空，但全局仍需证明计数胜出或排斥吸收。

```text
template_count=27
identity_failure_count=0
count_gate_closed_count=16
count_gate_residual_count=11
actual_union_void_count=0
row_column_unconditional_closed=false
```

## 1. Hull 分解

对每个模板，把 hull 内奇候选分成目标并集 `U` 与互补孔袋 `C`：

```text
Prime(hull) = Prime(U) + Prime(C)
coverage_defect = |C|
```

因此若 `Prime(hull)>|C|`，即使互补孔袋全是素数，也无法吸收所有 hull 素数，目标并集必含素数。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| template records | 27 |
| identity failures | 0 |
| count-gate closed | 16 |
| count-gate residual | 11 |
| actual union void | 0 |
| min hull-count margin | -6 |
| min complement absorption margin | 1 |
| max complement candidates | 12 |
| max complement primes | 4 |
| max complement pockets | 2 |

## 3. 吸收最紧边界

| P | side | hull | U primes | C primes | C cand | count margin | absorption margin | pockets | atoms |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 733 | `plus` | `675-705` | 1 | 3 | 10 | -6 | 1 | `677-695#3` | `minus_only_noslot:k0:697-705,both_offband_middle:k2:675-675` |
| 691 | `minus` | `649-665` | 1 | 2 | 5 | -2 | 1 | `655-663#2` | `both_offband_middle:k0:665-665,plus_only_noslot:k1:649-653` |
| 733 | `plus` | `675-687` | 1 | 1 | 2 | 0 | 1 | `677-679#1` | `minus_only_noslot:k1:681-687,both_offband_middle:k2:675-675` |
| 683 | `plus` | `639-657` | 1 | 3 | 4 | 0 | 1 | `641-647#3` | `both_offband_middle:k0:657-657,minus_only_noslot:k0:649-655,both_offband_middle:k1:639-639` |
| 523 | `plus` | `485-501` | 1 | 2 | 3 | 0 | 1 | `487-491#2` | `both_offband_middle:k0:501-501,minus_only_noslot:k0:493-499,both_offband_middle:k1:485-485` |
| 73 | `plus` | `59-65` | 1 | 1 | 1 | 1 | 1 | `61-61#1` | `both_offband_middle:k0:65-65,minus_only_noslot:k0:63-63,minus_only_noslot:k1:59-59` |
| 37 | `minus` | `31-35` | 1 | 0 | 0 | 1 | 1 | `` | `plus_only_noslot:k0:33-35,both_offband_middle:k0:31-31` |
| 23 | `plus` | `19-19` | 1 | 0 | 0 | 1 | 1 | `` | `both_offband_middle:k0:19-19` |
| 673 | `minus` | `619-637` | 2 | 0 | 3 | -1 | 2 | `625-629#0` | `plus_only_noslot:k1:631-637,plus_only_noslot:k2:619-623` |
| 733 | `plus` | `681-705` | 2 | 1 | 4 | -1 | 2 | `689-695#1` | `minus_only_noslot:k0:697-705,minus_only_noslot:k1:681-687` |
| 293 | `plus` | `261-275` | 2 | 1 | 2 | 1 | 2 | `267-269#1` | `minus_only_noslot:k0:271-275,both_offband_middle:k1:265-265,minus_only_noslot:k1:261-263` |
| 421 | `plus` | `387-401` | 2 | 1 | 2 | 1 | 2 | `389-391#1` | `both_offband_middle:k0:401-401,minus_only_noslot:k0:393-399,both_offband_middle:k1:387-387` |
| 113 | `plus` | `95-103` | 2 | 1 | 1 | 2 | 2 | `97-97#1` | `both_offband_middle:k0:103-103,minus_only_noslot:k0:99-101,minus_only_noslot:k1:95-95` |
| 43 | `minus` | `37-41` | 2 | 0 | 0 | 2 | 2 | `` | `plus_only_noslot:k0:39-41,both_offband_middle:k0:37-37` |
| 47 | `minus` | `41-45` | 2 | 0 | 0 | 2 | 2 | `` | `plus_only_noslot:k0:43-45,both_offband_middle:k0:41-41` |
| 313 | `plus` | `273-295` | 3 | 1 | 4 | 0 | 3 | `277-279#1,285-287#0` | `minus_only_noslot:k0:289-295,minus_only_noslot:k1:281-283,minus_only_noslot:k2:273-275` |
| 271 | `minus` | `245-269` | 3 | 1 | 3 | 1 | 3 | `249-253#1` | `plus_only_noslot:k0:257-269,both_offband_middle:k0:255-255,plus_only_noslot:k1:245-247` |
| 419 | `minus` | `387-417` | 3 | 1 | 3 | 1 | 3 | `393-397#1` | `plus_only_noslot:k0:401-417,both_offband_middle:k0:399-399,plus_only_noslot:k1:387-391` |
| 157 | `minus` | `139-155` | 3 | 0 | 2 | 1 | 3 | `141-143#0` | `plus_only_noslot:k0:147-155,both_offband_middle:k0:145-145,plus_only_noslot:k1:139-139` |
| 73 | `minus` | `61-71` | 3 | 0 | 1 | 2 | 3 | `63-63#0` | `plus_only_noslot:k0:67-71,both_offband_middle:k0:65-65,plus_only_noslot:k1:61-61` |
| 691 | `minus` | `665-689` | 3 | 0 | 0 | 3 | 3 | `` | `plus_only_noslot:k0:667-689,both_offband_middle:k0:665-665` |
| 673 | `minus` | `619-671` | 4 | 4 | 12 | -4 | 4 | `625-647#4` | `plus_only_noslot:k0:649-671,plus_only_noslot:k2:619-623` |
| 691 | `minus` | `649-689` | 4 | 2 | 6 | 0 | 4 | `655-665#2` | `plus_only_noslot:k0:667-689,plus_only_noslot:k1:649-653` |
| 487 | `plus` | `445-465` | 4 | 0 | 3 | 1 | 4 | `451-455#0` | `both_offband_middle:k0:465-465,minus_only_noslot:k0:457-463,minus_only_noslot:k1:445-449` |

## 4. Count Gate 残余

| P | side | hull | hull primes | C cand | C primes | U primes | pockets |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |
| 733 | `plus` | `675-705` | 4 | 10 | 3 | 1 | `677-695#3` |
| 733 | `plus` | `675-687` | 2 | 2 | 1 | 1 | `677-679#1` |
| 683 | `plus` | `639-657` | 4 | 4 | 3 | 1 | `641-647#3` |
| 523 | `plus` | `485-501` | 3 | 3 | 2 | 1 | `487-491#2` |
| 691 | `minus` | `649-665` | 3 | 5 | 2 | 1 | `655-663#2` |
| 673 | `minus` | `619-637` | 2 | 3 | 0 | 2 | `625-629#0` |
| 733 | `plus` | `681-705` | 3 | 4 | 1 | 2 | `689-695#1` |
| 313 | `plus` | `273-295` | 4 | 4 | 1 | 3 | `277-279#1,285-287#0` |
| 673 | `minus` | `619-671` | 8 | 12 | 4 | 4 | `625-647#4` |
| 691 | `minus` | `649-689` | 6 | 6 | 2 | 4 | `655-665#2` |
| 1129 | `plus` | `1051-1095` | 7 | 9 | 2 | 5 | `1057-1063#2,1073-1081#0` |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `hull_union_complement_prime_partition` | `closed` | For each template, hull primes split exactly into target-union primes plus complement-pocket primes. |
| `hull_count_beats_coverage_defect_gate` | `closed` | If hull_prime_count exceeds the number of complement candidates, the target union must contain a prime. |
| `complement_absorption_pdec_registration` | `closed` | If the target union is prime-void, all hull primes are absorbed by explicit complement pockets. |
| `finite_no_complement_absorption` | `finite_evidence` | The finite audit finds positive complement absorption margin for every template. |
| `global_hull_count_or_absorption_exclusion` | `open` | A global proof still needs hull prime counts beating coverage defects, or exclusion of complement-pocket absorption. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `HullUnionComplementPartitionClosed` | `true` | `true` | hull/目标并集/互补孔袋的候选与素数计数恒等式已闭合。 | closed |
| `HullCountBeatsCoverageDefectGateClosed` | `true` | `true` | `π_hull>D_cov` 是排除穿孔并集全空的充分条件。 | closed |
| `ComplementAbsorptionPDECRegistered` | `true` | `true` | 若充分条件失败，则反例必须让互补孔袋吸收全部 hull 素数。 | closed |
| `FiniteNoComplementAbsorptionPDEC` | `true` | `false` | 有限样本中没有目标并集全空。 | finite evidence only |
| `GlobalHullCountOrAbsorptionClosed` | `false` | `false` | 仍需全局证明 hull 计数胜过覆盖缺口，或排斥互补孔袋吸收。 | HullPrimeCountBeatsCoverageDefectOrComplementPocketAbsorptionPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成计数恒等式和 PDEC 注册，不关闭全局行/列命题。 | HullPrimeCountBeatsCoverageDefectOrComplementPocketAbsorptionPDEC |

## 7. 下一步

- 主攻：`HullPrimeCountBeatsCoverageDefectOrComplementPocketAbsorptionPDEC`。
- 若能证明短 hull 内素数数超过覆盖缺口候选数，则目标并集自动含素数。
- 对 count gate 残余，需排斥互补孔袋吸收全部 hull 素数的 PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router.py` | `33a5f03674af63ed8a7d4347c0ea10ada628cb6e3cb87e046cdfaf94197ff6ef` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_sqrt_input_router.py` | `4cb2f5e660a97927ab5cb90bb0df1cc3ec2857370a28d4c8bcb32eb309ead438` |
| `data/square-phase-offband-prefix-gap-shadow-sqrt-input-ledger.json` | `819d391201c6719a8f93ab4786657e73e7d06f356971d002615aa8fdc10fd0e5` |
| `data/square-phase-offband-prefix-gap-shadow-hull-absorption-ledger.json` | `7be890f2eef77312ef25069b38c5a0d8f2af823b92bde052f63e11f516c4c710` |
