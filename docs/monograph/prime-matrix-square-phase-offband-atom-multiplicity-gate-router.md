# Prime Matrix square-phase off-band atom multiplicity gate router

**状态：** `two_atom_gate_reduced_to_required_count_and_loaded_atom_multiplicity_open`

本步把双 atom 负载门压成两个更原子的条件：第一，所需见证数 `W_required` 不超过 2；第二，loaded off-band atom 的个数至少为 `W_required`。因为每个 loaded atom 至少贡献一个素数，两个条件合起来推出 top-two 负载和达到阈值。有限扫描中 `W_required` 最大为 2，且所有正阈值点的 loaded atom 重数均足够；全局仍需证明这两个输入，或排斥所需见证数过大与 loaded atom 重数不足的 PDEC。

```text
max_p=5000
finite_prime_count=668
multiplicity_equivalence_failure_count=0
required_gt_two_pdec_count=0
loaded_multiplicity_shortage_pdec_count=0
row_column_unconditional_closed=false
```

## 1. 重数门

双 atom 覆盖可以被更粗但更结构化的重数门替代：

```text
W_required <= 2
loaded_offband_atom_count >= W_required
```

因为每个 loaded atom 至少含一个尾素，取两个最大 loaded atoms 即可覆盖阈值。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| side records | 1336 |
| positive required count | 21 |
| multiplicity equivalence failures | 0 |
| required > 2 PDEC count | 0 |
| loaded multiplicity shortage count | 0 |
| tail envelope defect count | 21 |
| max required witnesses | 2 |
| max loaded offband atom count | 61 |
| min loaded atom surplus on positive required | 0 |
| min exact pressure margin | 1 |

## 3. 正阈值最紧边界

| P | side | W_req | loaded atoms | surplus | top atoms |
| ---: | --- | ---: | ---: | ---: | --- |
| 23 | `plus` | 1 | 1 | 0 | `both_offband_middle:k0:19-19#1` |
| 37 | `minus` | 1 | 1 | 0 | `both_offband_middle:k0:31-31#1` |
| 73 | `plus` | 1 | 1 | 0 | `minus_only_noslot:k1:59-59#1` |
| 43 | `minus` | 1 | 2 | 1 | `plus_only_noslot:k0:39-41#1,both_offband_middle:k0:37-37#1` |
| 47 | `minus` | 1 | 2 | 1 | `plus_only_noslot:k0:43-45#1,both_offband_middle:k0:41-41#1` |
| 73 | `minus` | 1 | 2 | 1 | `plus_only_noslot:k0:67-71#2,plus_only_noslot:k1:61-61#1` |
| 113 | `plus` | 1 | 2 | 1 | `minus_only_noslot:k0:99-101#1,both_offband_middle:k0:103-103#1` |
| 199 | `minus` | 1 | 3 | 2 | `plus_only_noslot:k0:187-197#3,plus_only_noslot:k1:177-179#1,plus_only_noslot:k3:167-167#1` |
| 157 | `minus` | 1 | 5 | 4 | `plus_only_noslot:k0:147-155#2,plus_only_noslot:k1:139-139#1,both_offband_middle:k1:137-137#1,both_offband_middle:k2:131-131#1` |
| 271 | `minus` | 1 | 5 | 4 | `plus_only_noslot:k0:257-269#3,plus_only_noslot:k2:239-239#1,plus_only_noslot:k3:233-233#1,plus_only_noslot:k4:227-227#1` |
| 293 | `plus` | 1 | 5 | 4 | `minus_only_noslot:k0:271-275#1,minus_only_noslot:k1:261-263#1,both_offband_middle:k2:257-257#1,both_offband_middle:k3:251-251#1` |
| 313 | `plus` | 1 | 5 | 4 | `minus_only_noslot:k1:281-283#2,minus_only_noslot:k0:289-295#1,minus_only_noslot:k3:267-269#1,minus_only_noslot:k4:263-263#1` |
| 523 | `plus` | 1 | 5 | 4 | `minus_only_noslot:k0:493-499#1,minus_only_noslot:k3:463-465#1,minus_only_noslot:k4:457-457#1,minus_only_noslot:k9:431-431#1` |
| 487 | `plus` | 1 | 6 | 5 | `minus_only_noslot:k0:457-463#3,minus_only_noslot:k1:445-449#1,minus_only_noslot:k2:437-439#1,minus_only_noslot:k3:429-431#1` |
| 419 | `minus` | 1 | 7 | 6 | `plus_only_noslot:k0:401-417#2,plus_only_noslot:k1:387-391#1,plus_only_noslot:k2:377-379#1,plus_only_noslot:k5:357-359#1` |
| 421 | `plus` | 1 | 8 | 7 | `minus_only_noslot:k0:393-399#1,minus_only_noslot:k1:383-385#1,minus_only_noslot:k3:367-369#1,both_offband_middle:k0:401-401#1` |
| 691 | `minus` | 2 | 11 | 9 | `plus_only_noslot:k0:667-689#3,plus_only_noslot:k4:617-619#2,plus_only_noslot:k1:649-653#1,plus_only_noslot:k7:597-599#1` |
| 673 | `minus` | 2 | 12 | 10 | `plus_only_noslot:k0:649-671#3,plus_only_noslot:k1:631-637#1,plus_only_noslot:k2:619-623#1,plus_only_noslot:k4:601-603#1` |
| 683 | `plus` | 1 | 12 | 11 | `minus_only_noslot:k5:599-601#2,minus_only_noslot:k0:649-655#1,minus_only_noslot:k3:613-615#1,both_offband_middle:k3:617-617#1` |
| 733 | `plus` | 2 | 13 | 11 | `minus_only_noslot:k0:697-705#1,minus_only_noslot:k1:681-687#1,minus_only_noslot:k2:671-673#1,minus_only_noslot:k3:661-663#1` |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `two_atom_to_multiplicity_gate` | `closed` | If W_required<=2 and at least W_required off-band atoms are loaded, then the two-atom cover gate closes. |
| `two_atom_multiplicity_equivalence` | `closed` | The finite audit verifies equivalence between the two-atom load gate and the multiplicity gate for all tested sides. |
| `required_witness_at_most_two` | `finite_evidence` | The finite audit finds W_required<=2 up to the tested bound. |
| `loaded_offband_atom_multiplicity_bound` | `finite_evidence` | The finite audit finds enough loaded off-band atoms whenever W_required is positive. |
| `global_required_two_and_loaded_atom_bound` | `open` | A global proof still needs W_required<=2 and enough loaded off-band atoms, or the corresponding PDEC exclusions. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TwoAtomToMultiplicityGateClosed` | `true` | `true` | 双 atom 负载门已压成 W_required<=2 加 loaded atom 重数门。 | closed |
| `FiniteNoRequiredGtTwoPDEC` | `true` | `false` | 有限扫描中所需见证数未超过 2。 | finite evidence only |
| `FiniteNoLoadedMultiplicityShortagePDEC` | `true` | `false` | 有限扫描中 loaded off-band atom 个数均达到所需阈值。 | finite evidence only |
| `GlobalMultiplicityGateClosed` | `false` | `false` | 仍需全局证明 W_required<=2 与 loaded atom 重数下界，或排斥对应 PDEC。 | RequiredWitnessAtMostTwoAndLoadedOffBandAtomMultiplicityBoundOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把双 atom 硬点压成两个更原子的输入，不关闭全局行/列命题。 | RequiredWitnessAtMostTwoAndLoadedOffBandAtomMultiplicityBoundOrPDEC |

## 6. 下一步

- 主攻：`RequiredWitnessAtMostTwoAndLoadedOffBandAtomMultiplicityBoundOrPDEC`。
- 需证明 `W_required<=2`，并证明正阈值处至少有足够多个 loaded off-band atoms。
- 若失败，则分别登记为 required-count PDEC 或 atom-multiplicity-shortage PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_atom_multiplicity_gate_router.py` | `35fef62e68c422f78266fc5866a18e5024d1cde1565e8e5aedcf3bfe34fff3cb` |
| `experiments/prime_matrix_square_phase_offband_two_atom_cover_router.py` | `7fcf706defe2773fd22a4a39023b11e18b67d93acb50c03124725350e6f2cd90` |
| `experiments/prime_matrix_square_phase_offband_layer_witness_router.py` | `498e72d870def8c6b65909b274c52c6c1cab58b74f836b84aa4311cb2051d77a` |
| `data/square-phase-offband-atom-multiplicity-gate-ledger.json` | `9e1ed64e927e94d73bdcc01718ba75f942d289a4313524eaae088c47da70590c` |
