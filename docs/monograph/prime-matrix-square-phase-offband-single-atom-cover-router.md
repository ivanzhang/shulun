# Prime Matrix square-phase off-band single atom cover router

**状态：** `offband_layer_void_reduced_to_single_atom_prime_load_or_distributed_cover_pdec_open`

本步把 layer-void 见证硬点再压成单 atom 覆盖门。若某个 off-band layer atom 的 prime load 至少等于所需见证数，单侧立即闭合；否则即使总见证数足够，也必须由多个 loaded atoms 分散覆盖，登记为 DistributedCoverPDEC。有限扫描中存在一个单 atom 不足的分散覆盖点，但最小 loaded-atom 覆盖仍存在且大小为 2；全局仍需证明存在足够负载的单 atom，或把分散覆盖异常继续压成更小的多 atom 门。

```text
max_p=5000
finite_prime_count=668
positive_required_count=21
distributed_cover_pdec_count=1
single_atom_failure_count=1
minimal_cover_failure_count=0
row_column_unconditional_closed=false
```

## 1. 单 Atom 覆盖门

记单侧所需 off-band 见证数为 `W_required`。若存在一个 off-band layer atom 满足

```text
prime_load(atom) >= W_required,
```

则该侧的 off-band 见证门立即闭合。

## 2. 分散覆盖 PDEC

若总 off-band 见证数足够但没有任何单 atom 达到 `W_required`，则见证必须分散在多个 atoms 中。这被登记为 `DistributedCoverPDEC`；有限审计中该形态确实出现 1 次。

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| side records | 1336 |
| positive required count | 21 |
| single atom cover count | 20 |
| distributed cover PDEC count | 1 |
| single atom failure count | 1 |
| minimal cover failure count | 0 |
| tail envelope defect count | 21 |
| max required witnesses | 2 |
| max single atom load | 11 |
| max minimal cover size | 2 |
| min single atom margin on positive required | -1 |
| min witness surplus | 0 |
| min exact pressure margin | 1 |

## 4. 正阈值最紧边界

| P | side | H | T | W | W_req | max atom load | atom margin | cover size | cover load | top atom |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 733 | `plus` | 44 | 23 | 13 | 2 | 1 | -1 | 2 | 2 | `minus_only_noslot:k0:697-705#1` |
| 23 | `plus` | 2 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | `both_offband_middle:k0:19-19#1` |
| 37 | `minus` | 2 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | `both_offband_middle:k0:31-31#1` |
| 73 | `plus` | 7 | 4 | 1 | 1 | 1 | 0 | 1 | 1 | `minus_only_noslot:k1:59-59#1` |
| 43 | `minus` | 4 | 2 | 2 | 1 | 1 | 0 | 1 | 1 | `plus_only_noslot:k0:39-41#1` |
| 47 | `minus` | 3 | 2 | 2 | 1 | 1 | 0 | 1 | 1 | `plus_only_noslot:k0:43-45#1` |
| 113 | `plus` | 9 | 5 | 2 | 1 | 1 | 0 | 1 | 1 | `minus_only_noslot:k0:99-101#1` |
| 293 | `plus` | 20 | 10 | 5 | 1 | 1 | 0 | 1 | 1 | `minus_only_noslot:k0:271-275#1` |
| 523 | `plus` | 36 | 18 | 5 | 1 | 1 | 0 | 1 | 1 | `minus_only_noslot:k0:493-499#1` |
| 421 | `plus` | 28 | 14 | 8 | 1 | 1 | 0 | 1 | 1 | `minus_only_noslot:k0:393-399#1` |
| 73 | `minus` | 8 | 4 | 3 | 1 | 2 | 1 | 1 | 2 | `plus_only_noslot:k0:67-71#2` |
| 157 | `minus` | 12 | 6 | 6 | 1 | 2 | 1 | 1 | 2 | `plus_only_noslot:k0:147-155#2` |
| 313 | `plus` | 21 | 11 | 6 | 1 | 2 | 1 | 1 | 2 | `minus_only_noslot:k1:281-283#2` |
| 419 | `minus` | 26 | 13 | 8 | 1 | 2 | 1 | 1 | 2 | `plus_only_noslot:k0:401-417#2` |
| 673 | `minus` | 41 | 22 | 14 | 2 | 3 | 1 | 1 | 3 | `plus_only_noslot:k0:649-671#3` |
| 683 | `plus` | 46 | 23 | 13 | 1 | 2 | 1 | 1 | 2 | `minus_only_noslot:k5:599-601#2` |
| 691 | `minus` | 43 | 23 | 14 | 2 | 3 | 1 | 1 | 3 | `plus_only_noslot:k0:667-689#3` |
| 199 | `minus` | 16 | 8 | 5 | 1 | 3 | 2 | 1 | 3 | `plus_only_noslot:k0:187-197#3` |
| 271 | `minus` | 20 | 10 | 7 | 1 | 3 | 2 | 1 | 3 | `plus_only_noslot:k0:257-269#3` |
| 487 | `plus` | 30 | 15 | 8 | 1 | 3 | 2 | 1 | 3 | `minus_only_noslot:k0:457-463#3` |

## 5. 尾包络失败点

| P | side | tail margin | W | W_req | max atom load | cover size | top atom |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 673 | `minus` | -3 | 14 | 2 | 3 | 1 | `plus_only_noslot:k0:649-671#3` |
| 691 | `minus` | -3 | 14 | 2 | 3 | 1 | `plus_only_noslot:k0:667-689#3` |
| 733 | `plus` | -2 | 13 | 2 | 1 | 2 | `minus_only_noslot:k0:697-705#1` |
| 47 | `minus` | -1 | 2 | 1 | 1 | 1 | `plus_only_noslot:k0:43-45#1` |
| 73 | `plus` | -1 | 1 | 1 | 1 | 1 | `minus_only_noslot:k1:59-59#1` |
| 113 | `plus` | -1 | 2 | 1 | 1 | 1 | `minus_only_noslot:k0:99-101#1` |
| 313 | `plus` | -1 | 6 | 1 | 2 | 1 | `minus_only_noslot:k1:281-283#2` |
| 23 | `plus` | 0 | 1 | 1 | 1 | 1 | `both_offband_middle:k0:19-19#1` |
| 37 | `minus` | 0 | 1 | 1 | 1 | 1 | `both_offband_middle:k0:31-31#1` |
| 43 | `minus` | 0 | 2 | 1 | 1 | 1 | `plus_only_noslot:k0:39-41#1` |
| 293 | `plus` | 0 | 5 | 1 | 1 | 1 | `minus_only_noslot:k0:271-275#1` |
| 421 | `plus` | 0 | 8 | 1 | 1 | 1 | `minus_only_noslot:k0:393-399#1` |
| 523 | `plus` | 0 | 5 | 1 | 1 | 1 | `minus_only_noslot:k0:493-499#1` |
| 73 | `minus` | 0 | 3 | 1 | 2 | 1 | `plus_only_noslot:k0:67-71#2` |
| 157 | `minus` | 0 | 6 | 1 | 2 | 1 | `plus_only_noslot:k0:147-155#2` |
| 419 | `minus` | 0 | 8 | 1 | 2 | 1 | `plus_only_noslot:k0:401-417#2` |
| 683 | `plus` | 0 | 13 | 1 | 2 | 1 | `minus_only_noslot:k5:599-601#2` |
| 199 | `minus` | 0 | 5 | 1 | 3 | 1 | `plus_only_noslot:k0:187-197#3` |
| 271 | `minus` | 0 | 7 | 1 | 3 | 1 | `plus_only_noslot:k0:257-269#3` |
| 487 | `plus` | 0 | 8 | 1 | 3 | 1 | `minus_only_noslot:k0:457-463#3` |

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `single_atom_cover_sufficient_gate` | `closed` | If one off-band layer atom has prime load at least the required witness count, then the side closes immediately. |
| `minimal_loaded_atom_cover_certificate` | `closed` | The required witness load can be certified by the smallest number of loaded off-band atoms sorted by prime load. |
| `distributed_cover_pdec_registration` | `closed` | Failure of single-atom cover is registered as a distributed-cover PDEC requiring multiple off-band atoms. |
| `finite_distributed_cover_profile` | `finite_counterexample_to_single_atom_only` | The finite audit finds the distributed-cover profile when a single off-band atom fails, but the minimal loaded-atom cover still exists. |
| `global_single_atom_load_bound` | `open` | A global proof still needs one off-band layer atom with enough prime load, or exclusion of distributed-cover PDEC. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SingleAtomCoverGateClosed` | `true` | `true` | 单个 off-band atom 的 prime load 达到阈值即可闭合单侧。 | closed |
| `MinimalCoverCertificateClosed` | `true` | `true` | 最小 loaded-atom 覆盖证书均可计算并与见证总量一致。 | closed |
| `FiniteDistributedCoverProfileMaterialized` | `false` | `false` | 有限扫描出现单 atom 不足的分散覆盖形态；需继续压成双 atom 门。 | finite distributed profile; next split |
| `GlobalSingleAtomLoadBoundClosed` | `false` | `false` | 仍需全局证明存在足够负载的单 off-band atom，或排斥分散覆盖 PDEC。 | SingleOffBandLayerAtomPrimeLoadLowerBoundOrDistributedCoverPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 layer-void 硬点压成单 atom 负载或分散覆盖 PDEC，不关闭全局行/列命题。 | SingleOffBandLayerAtomPrimeLoadLowerBoundOrDistributedCoverPDECExclusion |

## 8. 下一步

- 主攻：`SingleOffBandLayerAtomPrimeLoadLowerBoundOrDistributedCoverPDECExclusion`。
- 需证明至少一个 off-band layer atom 的 q 区间含有足够多素数。
- 若单 atom 失败，则必须进入多 atom 分散覆盖 PDEC；有限唯一分散点由两个 atoms 覆盖。
- 当前仍未证明全局行/列无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_single_atom_cover_router.py` | `a4ada5a086b6f8fc2cc1b90dfca0445a0b3c91e240109f0c770eaf213852d0e0` |
| `experiments/prime_matrix_square_phase_offband_layer_witness_router.py` | `498e72d870def8c6b65909b274c52c6c1cab58b74f836b84aa4311cb2051d77a` |
| `experiments/prime_matrix_square_phase_offband_witness_trichotomy_router.py` | `2251a43359e5c348e23e36c6a08cc72add038d56d76d2b5300e18082c395c302` |
| `data/square-phase-offband-single-atom-cover-ledger.json` | `28fc59167e8167423153c2205c73fecb05dc858413859e6a76ee57b2995a4d4c` |
