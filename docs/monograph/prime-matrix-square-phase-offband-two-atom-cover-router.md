# Prime Matrix square-phase off-band two atom cover router

**状态：** `distributed_cover_reduced_to_two_atom_load_or_higher_distributed_pdec_open`

本步把上一层暴露的分散覆盖形态压成双 atom 覆盖门。若两个最大 loaded off-band atoms 的 prime load 之和达到所需见证数，单侧闭合；否则才登记为更高阶分散覆盖 PDEC。有限扫描中唯一单 atom 不足点 `P=733` plus 由两个 load=1 的 off-band atoms 覆盖，因此没有更高阶分散覆盖 PDEC；全局仍需证明双 atom 负载下界，或排斥高阶分散异常。

```text
max_p=5000
finite_prime_count=668
positive_required_count=21
single_atom_failure_count=1
higher_distributed_cover_pdec_count=0
row_column_unconditional_closed=false
```

## 1. 双 Atom 覆盖门

记两个最大 loaded off-band atoms 的负载和为 `L2`。若

```text
L2 >= W_required,
```

则单侧见证门闭合。只有 `L2<W_required` 时才进入更高阶分散覆盖 PDEC。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| side records | 1336 |
| positive required count | 21 |
| single atom failure count | 1 |
| two atom cover count | 21 |
| higher distributed cover PDEC count | 0 |
| tail envelope defect count | 21 |
| max required witnesses | 2 |
| max top-two atom load | 14 |
| max minimal cover size | 2 |
| min two atom margin on positive required | 0 |
| min exact pressure margin | 1 |

## 3. 正阈值最紧边界

| P | side | W | W_req | max atom | top-two load | two margin | min cover | top atoms |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 733 | `plus` | 13 | 2 | 1 | 2 | 0 | 2 | `minus_only_noslot:k0:697-705#1,minus_only_noslot:k1:681-687#1` |
| 23 | `plus` | 1 | 1 | 1 | 1 | 0 | 1 | `both_offband_middle:k0:19-19#1` |
| 37 | `minus` | 1 | 1 | 1 | 1 | 0 | 1 | `both_offband_middle:k0:31-31#1` |
| 73 | `plus` | 1 | 1 | 1 | 1 | 0 | 1 | `minus_only_noslot:k1:59-59#1` |
| 43 | `minus` | 2 | 1 | 1 | 2 | 1 | 1 | `plus_only_noslot:k0:39-41#1,both_offband_middle:k0:37-37#1` |
| 47 | `minus` | 2 | 1 | 1 | 2 | 1 | 1 | `plus_only_noslot:k0:43-45#1,both_offband_middle:k0:41-41#1` |
| 113 | `plus` | 2 | 1 | 1 | 2 | 1 | 1 | `minus_only_noslot:k0:99-101#1,both_offband_middle:k0:103-103#1` |
| 293 | `plus` | 5 | 1 | 1 | 2 | 1 | 1 | `minus_only_noslot:k0:271-275#1,minus_only_noslot:k1:261-263#1` |
| 421 | `plus` | 8 | 1 | 1 | 2 | 1 | 1 | `minus_only_noslot:k0:393-399#1,minus_only_noslot:k1:383-385#1` |
| 523 | `plus` | 5 | 1 | 1 | 2 | 1 | 1 | `minus_only_noslot:k0:493-499#1,minus_only_noslot:k3:463-465#1` |
| 73 | `minus` | 3 | 1 | 2 | 3 | 2 | 1 | `plus_only_noslot:k0:67-71#2,plus_only_noslot:k1:61-61#1` |
| 157 | `minus` | 6 | 1 | 2 | 3 | 2 | 1 | `plus_only_noslot:k0:147-155#2,plus_only_noslot:k1:139-139#1` |
| 313 | `plus` | 6 | 1 | 2 | 3 | 2 | 1 | `minus_only_noslot:k1:281-283#2,minus_only_noslot:k0:289-295#1` |
| 419 | `minus` | 8 | 1 | 2 | 3 | 2 | 1 | `plus_only_noslot:k0:401-417#2,plus_only_noslot:k1:387-391#1` |
| 673 | `minus` | 14 | 2 | 3 | 4 | 2 | 1 | `plus_only_noslot:k0:649-671#3,plus_only_noslot:k1:631-637#1` |
| 683 | `plus` | 13 | 1 | 2 | 3 | 2 | 1 | `minus_only_noslot:k5:599-601#2,minus_only_noslot:k0:649-655#1` |
| 691 | `minus` | 14 | 2 | 3 | 5 | 3 | 1 | `plus_only_noslot:k0:667-689#3,plus_only_noslot:k4:617-619#2` |
| 199 | `minus` | 5 | 1 | 3 | 4 | 3 | 1 | `plus_only_noslot:k0:187-197#3,plus_only_noslot:k1:177-179#1` |
| 271 | `minus` | 7 | 1 | 3 | 4 | 3 | 1 | `plus_only_noslot:k0:257-269#3,plus_only_noslot:k2:239-239#1` |
| 487 | `plus` | 8 | 1 | 3 | 4 | 3 | 1 | `minus_only_noslot:k0:457-463#3,minus_only_noslot:k1:445-449#1` |

## 4. 单 Atom 不足点

| P | side | W_req | top-two load | atoms |
| ---: | --- | ---: | ---: | --- |
| 733 | `plus` | 2 | 2 | `minus_only_noslot:k0:697-705#1,minus_only_noslot:k1:681-687#1` |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `two_atom_cover_sufficient_gate` | `closed` | If the two largest loaded off-band atoms have total prime load at least the required witness count, then the side closes. |
| `distributed_cover_profile_absorbed_by_two_atoms` | `finite_evidence` | The finite distributed-cover profile is absorbed by two loaded off-band atoms. |
| `higher_distributed_cover_pdec_registration` | `closed` | Failure of two-atom cover is registered as a higher-distributed-cover PDEC. |
| `finite_no_higher_distributed_cover_pdec` | `finite_evidence` | The finite audit finds no positive-required side requiring more than two loaded off-band atoms. |
| `global_two_atom_load_bound` | `open` | A global proof still needs two off-band layer atoms with enough prime load, or exclusion of higher distributed-cover PDEC. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TwoAtomCoverGateClosed` | `true` | `true` | 两个最大 loaded off-band atoms 的负载和达到阈值即可闭合单侧。 | closed |
| `FiniteNoHigherDistributedCoverPDEC` | `true` | `false` | 有限扫描中没有需要超过两个 atoms 的正阈值点。 | finite evidence only |
| `GlobalTwoAtomLoadBoundClosed` | `false` | `false` | 仍需全局证明两个 off-band atoms 足够，或排斥更高阶分散覆盖 PDEC。 | TwoOffBandLayerAtomPrimeLoadLowerBoundOrHigherDistributedCoverPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把分散覆盖压成双 atom 门，不关闭全局行/列命题。 | TwoOffBandLayerAtomPrimeLoadLowerBoundOrHigherDistributedCoverPDECExclusion |

## 7. 下一步

- 主攻：`TwoOffBandLayerAtomPrimeLoadLowerBoundOrHigherDistributedCoverPDECExclusion`。
- 需证明两个 off-band layer atoms 的 q 区间素数负载和达到所需阈值。
- 若失败，则进入更高阶分散覆盖 PDEC。
- 当前仍未证明全局行/列无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_two_atom_cover_router.py` | `7fcf706defe2773fd22a4a39023b11e18b67d93acb50c03124725350e6f2cd90` |
| `experiments/prime_matrix_square_phase_offband_single_atom_cover_router.py` | `a4ada5a086b6f8fc2cc1b90dfca0445a0b3c91e240109f0c770eaf213852d0e0` |
| `experiments/prime_matrix_square_phase_offband_layer_witness_router.py` | `498e72d870def8c6b65909b274c52c6c1cab58b74f836b84aa4311cb2051d77a` |
| `data/square-phase-offband-two-atom-cover-ledger.json` | `0e95a8173c56e002b2da830342fe9486217e5612cd552ed388bb949a6d20a9d2` |
