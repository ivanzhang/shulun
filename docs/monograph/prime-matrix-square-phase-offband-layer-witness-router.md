# Prime Matrix square-phase off-band layer witness router

**状态：** `offband_witness_reduced_to_explicit_layer_atoms_and_layer_void_pdec_open`

本步把 off-band 尾素见证进一步落到显式 layer atoms。尾部 b 轴按 `k=floor(2b^2/(P-2b))` 与三分 band 切成连续原子；每个原子对应一个明确的 q 区间 `[P-2b_hi, P-2b_lo]`，其 prime load 就是可用见证数或极端取向负载。因此见证短缺等价于这些 off-band q-区间原子的联合 prime load 小于所需阈值，即一个显式 layer-void PDEC。有限扫描未出现 layer-void；全局仍需证明 off-band layer atoms 中有足够素数，或排斥该 PDEC family。

```text
max_p=5000
finite_prime_count=668
atom_partition_identity_failure_count=0
layer_witness_identity_failure_count=0
layer_void_pdec_count=0
extreme_orientation_pressure_pdec_count=0
row_column_unconditional_closed=false
```

## 1. Layer Atom 正规形

尾素仍写成 `q=P-2b`。在尾窗 `q>floor(4P/5)` 内，按

```text
k = floor(2b^2/(P-2b))
band in {plus_only_noslot, minus_only_noslot, both_offband_middle}
```

把连续 b 段合并成 atom。每个 atom 给出一个明确的 q 区间和其中的素数负载。

## 2. 见证短缺的 PDEC 形态

单侧所需见证仍为

```text
W_required = max(0, floor((2T-H)/2)+1).
```

见证短缺等价于所有 off-band atoms 的 prime load 总和小于 `W_required`。这就是当前登记的 layer-void PDEC。

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| side records | 1336 |
| atom records | 89321 |
| loaded atoms | 31264 |
| combined tail prime load | 38678 |
| plus extreme atom load | 18299 |
| minus extreme atom load | 15895 |
| middle atom load | 4484 |
| atom partition identity failures | 0 |
| layer witness identity failures | 0 |
| layer-void PDEC count | 0 |
| extreme orientation pressure PDEC count | 0 |
| tail envelope defect count | 21 |
| max offband atom count | 182 |
| max required witnesses | 2 |
| min witness surplus | 0 |
| min exact pressure margin | 1 |
| max atom prime load | 11 |

## 4. 最紧见证边界

| P | side | H | T | extreme | W | W_req | surplus | offband atoms | loaded atoms | top atoms |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | `minus` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `` |
| 3 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `` |
| 5 | `minus` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `` |
| 5 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `` |
| 7 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `` |
| 11 | `minus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | `plus_only_noslot:k0:9-9#0` |
| 13 | `plus` | 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | `` |
| 17 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `` |
| 19 | `plus` | 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | `` |
| 73 | `plus` | 7 | 4 | 3 | 1 | 1 | 0 | 3 | 1 | `minus_only_noslot:k1:59-59#1,both_offband_middle:k0:65-65#0,minus_only_noslot:k0:63-63#0` |
| 7 | `minus` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `` |
| 11 | `plus` | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `` |
| 23 | `plus` | 2 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | `both_offband_middle:k0:19-19#1` |
| 37 | `minus` | 2 | 1 | 0 | 1 | 1 | 0 | 2 | 1 | `both_offband_middle:k0:31-31#1,plus_only_noslot:k0:33-35#0` |
| 17 | `minus` | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | `plus_only_noslot:k0:15-15#0` |
| 31 | `plus` | 5 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | `minus_only_noslot:k0:25-25#0` |
| 41 | `plus` | 5 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | `both_offband_middle:k0:35-35#0,minus_only_noslot:k0:33-33#0` |
| 53 | `plus` | 7 | 2 | 2 | 0 | 0 | 0 | 1 | 0 | `minus_only_noslot:k0:45-45#0` |

## 5. 尾包络失败点

| P | side | H | T | extreme | W | W_req | surplus | tail margin | exact margin | top atoms |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 673 | `minus` | 41 | 22 | 8 | 14 | 2 | 12 | -3 | 25 | `plus_only_noslot:k0:649-671#3,plus_only_noslot:k1:631-637#1,plus_only_noslot:k2:619-623#1,plus_only_noslot:k4:601-603#1` |
| 691 | `minus` | 43 | 23 | 9 | 14 | 2 | 12 | -3 | 25 | `plus_only_noslot:k0:667-689#3,plus_only_noslot:k4:617-619#2,plus_only_noslot:k1:649-653#1,plus_only_noslot:k7:597-599#1` |
| 733 | `plus` | 44 | 23 | 10 | 13 | 2 | 11 | -2 | 24 | `minus_only_noslot:k0:697-705#1,minus_only_noslot:k1:681-687#1,minus_only_noslot:k2:671-673#1,minus_only_noslot:k3:661-663#1` |
| 73 | `plus` | 7 | 4 | 3 | 1 | 1 | 0 | -1 | 1 | `minus_only_noslot:k1:59-59#1,both_offband_middle:k0:65-65#0,minus_only_noslot:k0:63-63#0` |
| 47 | `minus` | 3 | 2 | 0 | 2 | 1 | 1 | -1 | 3 | `plus_only_noslot:k0:43-45#1,both_offband_middle:k0:41-41#1` |
| 113 | `plus` | 9 | 5 | 3 | 2 | 1 | 1 | -1 | 3 | `minus_only_noslot:k0:99-101#1,both_offband_middle:k0:103-103#1,minus_only_noslot:k1:95-95#0,minus_only_noslot:k2:91-91#0` |
| 313 | `plus` | 21 | 11 | 5 | 6 | 1 | 5 | -1 | 11 | `minus_only_noslot:k1:281-283#2,minus_only_noslot:k0:289-295#1,minus_only_noslot:k3:267-269#1,minus_only_noslot:k4:263-263#1` |
| 23 | `plus` | 2 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | `both_offband_middle:k0:19-19#1` |
| 37 | `minus` | 2 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | `both_offband_middle:k0:31-31#1,plus_only_noslot:k0:33-35#0` |
| 43 | `minus` | 4 | 2 | 0 | 2 | 1 | 1 | 0 | 4 | `plus_only_noslot:k0:39-41#1,both_offband_middle:k0:37-37#1` |
| 73 | `minus` | 8 | 4 | 1 | 3 | 1 | 2 | 0 | 6 | `plus_only_noslot:k0:67-71#2,plus_only_noslot:k1:61-61#1,both_offband_middle:k0:65-65#0` |
| 199 | `minus` | 16 | 8 | 3 | 5 | 1 | 4 | 0 | 10 | `plus_only_noslot:k0:187-197#3,plus_only_noslot:k1:177-179#1,plus_only_noslot:k3:167-167#1,both_offband_middle:k0:185-185#0` |
| 293 | `plus` | 20 | 10 | 5 | 5 | 1 | 4 | 0 | 10 | `minus_only_noslot:k0:271-275#1,minus_only_noslot:k1:261-263#1,both_offband_middle:k2:257-257#1,both_offband_middle:k3:251-251#1` |
| 523 | `plus` | 36 | 18 | 13 | 5 | 1 | 4 | 0 | 10 | `minus_only_noslot:k0:493-499#1,minus_only_noslot:k3:463-465#1,minus_only_noslot:k4:457-457#1,minus_only_noslot:k9:431-431#1` |
| 157 | `minus` | 12 | 6 | 0 | 6 | 1 | 5 | 0 | 12 | `plus_only_noslot:k0:147-155#2,plus_only_noslot:k1:139-139#1,both_offband_middle:k1:137-137#1,both_offband_middle:k2:131-131#1` |
| 271 | `minus` | 20 | 10 | 3 | 7 | 1 | 6 | 0 | 14 | `plus_only_noslot:k0:257-269#3,plus_only_noslot:k2:239-239#1,plus_only_noslot:k3:233-233#1,plus_only_noslot:k4:227-227#1` |
| 419 | `minus` | 26 | 13 | 5 | 8 | 1 | 7 | 0 | 16 | `plus_only_noslot:k0:401-417#2,plus_only_noslot:k1:387-391#1,plus_only_noslot:k2:377-379#1,plus_only_noslot:k5:357-359#1` |
| 421 | `plus` | 28 | 14 | 6 | 8 | 1 | 7 | 0 | 16 | `minus_only_noslot:k0:393-399#1,minus_only_noslot:k1:383-385#1,minus_only_noslot:k3:367-369#1,both_offband_middle:k0:401-401#1` |
| 487 | `plus` | 30 | 15 | 7 | 8 | 1 | 7 | 0 | 16 | `minus_only_noslot:k0:457-463#3,minus_only_noslot:k1:445-449#1,minus_only_noslot:k2:437-439#1,minus_only_noslot:k3:429-431#1` |
| 683 | `plus` | 46 | 23 | 10 | 13 | 1 | 12 | 0 | 26 | `minus_only_noslot:k5:599-601#2,minus_only_noslot:k0:649-655#1,minus_only_noslot:k3:613-615#1,both_offband_middle:k3:617-617#1` |

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `offband_layer_atom_partition` | `closed` | The tail b-axis is partitioned into contiguous atoms with fixed layer k and fixed signed phase band. |
| `side_witness_count_from_layer_atoms` | `closed` | For each side, the off-band witness count is exactly the total prime load of the opposite-only plus middle layer atoms. |
| `layer_void_pdec_registration` | `closed` | A witness shortage is equivalent to a registered layer-void PDEC over explicit q-interval atoms. |
| `finite_no_layer_void_pdec` | `finite_evidence` | The finite audit finds no off-band layer witness shortage up to the tested bound. |
| `global_offband_layer_prime_witness_lower_bound` | `open` | A global proof still needs to show enough primes in off-band layer atoms, or exclude the layer-void PDEC family. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `LayerAtomPartitionClosed` | `true` | `true` | 尾部 b 轴已按固定 k 与三分 band 切成连续原子。 | closed |
| `LayerWitnessIdentityClosed` | `true` | `true` | off-band 见证数等于对应 layer atoms 的 prime load。 | closed |
| `FiniteNoLayerVoidPDEC` | `true` | `false` | 有限扫描没有 layer-void 见证短缺。 | finite evidence only |
| `GlobalOffBandLayerPrimeWitnessBoundClosed` | `false` | `false` | 仍需证明 off-band layer atoms 中有足够素数，或排斥显式 layer-void PDEC。 | OffBandLayerPrimeWitnessLowerBoundOrLayerVoidPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把见证硬点压成 layer atoms 和 layer-void PDEC，不关闭全局行/列命题。 | OffBandLayerPrimeWitnessLowerBoundOrLayerVoidPDECExclusion |

## 8. 下一步

- 主攻：`OffBandLayerPrimeWitnessLowerBoundOrLayerVoidPDECExclusion`。
- 需证明 off-band layer atoms 的 q 区间素数负载达到所需见证阈值。
- 若失败，则反例必须表现为这些显式 q 区间的联合 prime void。
- 当前仍未证明全局行/列无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_layer_witness_router.py` | `498e72d870def8c6b65909b274c52c6c1cab58b74f836b84aa4311cb2051d77a` |
| `experiments/prime_matrix_square_phase_offband_witness_trichotomy_router.py` | `2251a43359e5c348e23e36c6a08cc72add038d56d76d2b5300e18082c395c302` |
| `experiments/prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py` | `d7f77df43459b5a51641980dbb6768baa1e1657261e6a61f889930a262c2c32e` |
| `data/square-phase-offband-layer-witness-ledger.json` | `a8d66904a7ed2db83c2de3cd4dec8952a044ac594f4d00185674ca8226d54f25` |
