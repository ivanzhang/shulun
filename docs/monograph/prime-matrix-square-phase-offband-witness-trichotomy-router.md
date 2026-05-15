# Prime Matrix square-phase off-band witness trichotomy router

**状态：** `phase_saving_reduced_to_required_offband_tailprime_witnesses_open`

本步把二次相位节省 `T-C` 具体化为 off-band 尾素见证数。对每个尾素 `q=P-2b`，令 `base=2b^2 mod q`、`h=(P-1)/2`、`lower=q-h`。若 `base<lower`，它只给 plus 侧 no-slot 负载；若 `base>h`，它只给 minus 侧 no-slot 负载；若 `lower<=base<=h`，它同时给两侧 off-band 节省。因此同一尾素不可能同时伤害两侧。单侧压力目标 `H>2C` 等价于：当尾包络缺陷 `2T-H>=0` 时，至少存在 `floor((2T-H)/2)+1` 个 off-band 尾素见证。有限扫描没有见证不足；全局仍需证明这些见证必存在，或排斥尾素过度集中到单侧极端取向的 PDEC。

```text
max_p=5000
finite_prime_count=668
trichotomy_failure_count=0
double_noslot_failure_count=0
pressure_witness_equivalence_failure_count=0
witness_shortage_count=0
row_column_unconditional_closed=false
```

## 1. 尾素三分

尾素写为 `q=P-2b`，并记

```text
h = (P-1)/2
base = 2b^2 mod q
lower = q-h = h-2b+1.
```

则三种情况互斥且穷尽：

| condition | meaning |
| --- | --- |
| `base<lower` | 只给 plus 侧 no-slot 负载，minus 侧是 off-band 见证 |
| `base>h` | 只给 minus 侧 no-slot 负载，plus 侧是 off-band 见证 |
| `lower<=base<=h` | 同时给 plus/minus 两侧 off-band 见证 |

因此同一尾素不会同时成为两侧 no-slot 负载。

## 2. 见证阈值

记 `H=HalfGridSurvivors_side(P)`、`T=TailPrimeCount(P)`、`C=NoSlotPhaseBandCount_side(P)`。单侧目标为 `H>2C`。当 `H<=2T` 时，所需 off-band 见证数为

```text
W_required = floor((2T-H)/2)+1.
```

且 `H>2C` 等价于 `W>=W_required`，其中 `W=T-C`。

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| side records | 1336 |
| pair records | 668 |
| tail prime total | 38678 |
| plus-only no-slot total | 18299 |
| minus-only no-slot total | 15895 |
| both-offband middle total | 4484 |
| trichotomy failures | 0 |
| double no-slot failures | 0 |
| pair identity failures | 0 |
| pressure-witness equivalence failures | 0 |
| witness shortage count | 0 |
| tail envelope defect count | 21 |
| max required off-band witnesses | 2 |
| min witness surplus | 0 |
| min exact pressure margin | 1 |

## 4. 最紧见证边界

| P | side | H | T | C | W | W_req | surplus | tail margin | exact margin | witnesses |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3 | `minus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | `` |
| 3 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | `` |
| 5 | `minus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | `` |
| 5 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | `` |
| 7 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | `` |
| 11 | `minus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | `` |
| 13 | `plus` | 3 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | `` |
| 17 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | `` |
| 19 | `plus` | 3 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | `` |
| 73 | `plus` | 7 | 4 | 3 | 1 | 1 | 0 | -1 | 1 | `59:minus_only_noslot` |
| 7 | `minus` | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | `` |
| 11 | `plus` | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | `` |
| 23 | `plus` | 2 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | `19:both_offband_middle` |
| 37 | `minus` | 2 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | `31:both_offband_middle` |
| 17 | `minus` | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | `` |
| 31 | `plus` | 5 | 1 | 1 | 0 | 0 | 0 | 3 | 3 | `` |

## 5. 尾包络失败点

| P | side | H | T | C | W | W_req | surplus | tail deficit | exact margin | witnesses |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 673 | `minus` | 41 | 22 | 8 | 14 | 2 | 12 | 3 | 25 | `557:plus_only_noslot,541:plus_only_noslot,571:plus_only_noslot,661:plus_only_noslot` |
| 691 | `minus` | 43 | 23 | 9 | 14 | 2 | 12 | 3 | 25 | `683:plus_only_noslot,599:plus_only_noslot,569:plus_only_noslot,593:plus_only_noslot` |
| 733 | `plus` | 44 | 23 | 10 | 13 | 2 | 11 | 2 | 24 | `599:minus_only_noslot,661:minus_only_noslot,617:minus_only_noslot,653:minus_only_noslot` |
| 73 | `plus` | 7 | 4 | 3 | 1 | 1 | 0 | 1 | 1 | `59:minus_only_noslot` |
| 47 | `minus` | 3 | 2 | 0 | 2 | 1 | 1 | 1 | 3 | `43:plus_only_noslot,41:both_offband_middle` |
| 113 | `plus` | 9 | 5 | 3 | 2 | 1 | 1 | 1 | 3 | `101:minus_only_noslot,103:both_offband_middle` |
| 313 | `plus` | 21 | 11 | 5 | 6 | 1 | 5 | 1 | 11 | `281:minus_only_noslot,263:minus_only_noslot,251:minus_only_noslot,293:minus_only_noslot` |
| 23 | `plus` | 2 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | `19:both_offband_middle` |
| 37 | `minus` | 2 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | `31:both_offband_middle` |
| 43 | `minus` | 4 | 2 | 0 | 2 | 1 | 1 | 0 | 4 | `41:plus_only_noslot,37:both_offband_middle` |
| 73 | `minus` | 8 | 4 | 1 | 3 | 1 | 2 | 0 | 6 | `71:plus_only_noslot,61:plus_only_noslot,67:plus_only_noslot` |
| 199 | `minus` | 16 | 8 | 3 | 5 | 1 | 4 | 0 | 10 | `197:plus_only_noslot,167:plus_only_noslot,193:plus_only_noslot,179:plus_only_noslot` |
| 293 | `plus` | 20 | 10 | 5 | 5 | 1 | 4 | 0 | 10 | `271:minus_only_noslot,263:minus_only_noslot,241:minus_only_noslot,251:both_offband_middle` |
| 523 | `plus` | 36 | 18 | 13 | 5 | 1 | 4 | 0 | 10 | `419:minus_only_noslot,463:minus_only_noslot,431:minus_only_noslot,457:minus_only_noslot` |
| 157 | `minus` | 12 | 6 | 0 | 6 | 1 | 5 | 0 | 12 | `151:plus_only_noslot,139:plus_only_noslot,149:plus_only_noslot,137:both_offband_middle` |
| 271 | `minus` | 20 | 10 | 3 | 7 | 1 | 6 | 0 | 14 | `269:plus_only_noslot,233:plus_only_noslot,263:plus_only_noslot,239:plus_only_noslot` |
| 419 | `minus` | 26 | 13 | 5 | 8 | 1 | 7 | 0 | 16 | `359:plus_only_noslot,349:plus_only_noslot,379:plus_only_noslot,409:plus_only_noslot` |
| 421 | `plus` | 28 | 14 | 6 | 8 | 1 | 7 | 0 | 16 | `367:minus_only_noslot,347:minus_only_noslot,383:minus_only_noslot,397:minus_only_noslot` |
| 487 | `plus` | 30 | 15 | 7 | 8 | 1 | 7 | 0 | 16 | `457:minus_only_noslot,461:minus_only_noslot,431:minus_only_noslot,439:minus_only_noslot` |
| 683 | `plus` | 46 | 23 | 10 | 13 | 1 | 12 | 0 | 26 | `613:minus_only_noslot,571:minus_only_noslot,547:minus_only_noslot,599:minus_only_noslot` |

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `tailprime_signed_phase_trichotomy` | `closed` | For each tail prime q=P-2b, base=2b^2 mod q lies in exactly one of plus-only no-slot, minus-only no-slot, or both-offband middle. |
| `no_double_noslot_for_tailprime` | `closed` | A tail prime cannot be no-slot on both plus and minus sides. |
| `offband_witness_pressure_gate` | `closed` | For each side, H>2C is equivalent to having at least max(0, floor((2T-H)/2)+1) off-band tail-prime witnesses when H<=2T. |
| `finite_required_witnesses_present` | `finite_evidence` | The finite audit finds no required off-band witness shortage up to the tested bound. |
| `global_witness_or_orientation_pdec` | `open` | A global proof still needs required off-band witnesses, or exclusion of an extreme-orientation PDEC where too many tail primes fall on one no-slot side. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SignedPhaseTrichotomyClosed` | `true` | `true` | 尾素二次相位三分逐点闭合。 | closed |
| `NoDoubleNoSlotClosed` | `true` | `true` | 同一尾素不会同时成为 plus 与 minus 的 no-slot 负载。 | closed |
| `OffBandWitnessGateClosed` | `true` | `true` | 压力不等式已经等价为 off-band 尾素见证数下界。 | closed |
| `FiniteNoWitnessShortage` | `true` | `false` | 有限扫描没有见证不足。 | finite evidence only |
| `GlobalWitnessOrOrientationPDECExcluded` | `false` | `false` | 仍需全局排斥一侧极端取向过密，或证明所需 off-band 见证必存在。 | RequiredOffBandTailPrimeWitnessOrExtremeOrientationPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把相位节省硬点压成见证/取向 PDEC，不关闭全局行/列命题。 | RequiredOffBandTailPrimeWitnessOrExtremeOrientationPDECExclusion |

## 8. 下一步

- 主攻：`RequiredOffBandTailPrimeWitnessOrExtremeOrientationPDECExclusion`。
- 需要证明尾包络失败处必有足够 off-band 尾素见证。
- 等价地，排斥尾素 `base=2b^2 mod q` 过度集中在单侧极端取向区间。
- 当前仍未证明全局行/列无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_witness_trichotomy_router.py` | `2251a43359e5c348e23e36c6a08cc72add038d56d76d2b5300e18082c395c302` |
| `experiments/prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py` | `d7f77df43459b5a51641980dbb6768baa1e1657261e6a61f889930a262c2c32e` |
| `experiments/prime_matrix_square_phase_phaseband_saving_dichotomy_router.py` | `45e05912084256ab59dfb49d4ee2a59936c079bc6cec548f96ba94767161da5e` |
| `data/square-phase-offband-witness-trichotomy-ledger.json` | `3d6c27ff5e394577d31b6df0d357730465403246ed48e71768e648daa6877ac4` |
