# Prime Matrix square-phase half-grid no-slot phase-band PDEC router

**状态：** `halfgrid_pressure_reduced_to_noslot_tailprime_phaseband_density_pdec_open`

本步把 `HalfGridSurvivors>2*NoSlotLoad` 的剩余硬点压成唯一 no-slot 二次相位带 PDEC。对尾素 `q=P-2b`，令 `delta_plus(b)` 为 `-2b^2 mod q` 的正代表，`delta_minus(b)` 为 `2b^2 mod q` 的正代表。无槽条件精确等价于 `delta_side(b)>(P-1)/2`。因此总压力反例等价于落入该上半相位带的尾素数量至少达到半个半网格幸存数。有限扫描未出现此 PDEC；全局仍需排斥该二次相位带密度异常，或将持久异常送入 PDEC/SAE/ColumnCRT。

```text
max_p=5000
finite_prime_count=668
phaseband_identity_failure_count=0
pressure_equivalence_failure_count=0
phaseband_pressure_pdec_count=0
row_column_unconditional_closed=false
```

## 1. 二次相位带正规形

尾素写成 `q=P-2b`，`h=(P-1)/2`。定义

```text
delta_plus(b)  = least positive residue of -2b^2 mod q,
delta_minus(b) = least positive residue of  2b^2 mod q.
```

则该尾素在对应方向没有可用半网格槽，当且仅当

```text
delta_side(b) > h.
```

于是 `NoSlotLoad` 不再是抽象负载，而是尾素在一个显式二次相位上半带中的计数。

## 2. 压力反例等价式

上一层目标为

```text
HalfGridSurvivors_side(P) > 2*NoSlotLoad_side(P).
```

由于 `NoSlotLoad=NoSlotPhaseBandCount`，失败当且仅当

```text
NoSlotPhaseBandCount_side(P) >= ceil(HalfGridSurvivors_side(P)/2).
```

这就是当前唯一剩余 PDEC。

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| record count | 1336 |
| combined half-grid survivors | 194541 |
| combined tail prime count | 77356 |
| combined phase-band count | 34194 |
| identity failures | 0 |
| pressure equivalence failures | 0 |
| phase-band pressure PDEC count | 0 |
| min total pressure margin | 1 |
| max phase-band density | 1.000000 |
| max required density for defect | 4.000000 |

## 4. 边界记录

| label | P | side | H | threshold | tail primes | phase-band | density | required density | margin |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| worst margin | 3 | `minus` | 1 | 1 | 0 | 0 | 0.000000 | None | 1 |
| max phase density | 13 | `plus` | 3 | 2 | 1 | 1 | 1.000000 | 2.000000 | 1 |
| max required density | 59 | `plus` | 8 | 4 | 1 | 1 | 1.000000 | 4.000000 | 6 |

## 5. 样本表

| P | side | H | tail primes | phase-band | density | margin | top phase records |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 13 | `plus` | 3 | 1 | 1 | 1.000000 | 1 | `11:3` |
| 13 | `minus` | 3 | 1 | 0 | 0.000000 | 3 | `` |
| 17 | `plus` | 1 | 0 | 0 | 0.000000 | 1 | `` |
| 17 | `minus` | 3 | 0 | 0 | 0.000000 | 3 | `` |
| 19 | `plus` | 3 | 1 | 1 | 1.000000 | 1 | `17:6` |
| 19 | `minus` | 4 | 1 | 0 | 0.000000 | 4 | `` |
| 23 | `plus` | 2 | 1 | 0 | 0.000000 | 2 | `` |
| 23 | `minus` | 3 | 1 | 0 | 0.000000 | 3 | `` |
| 29 | `plus` | 4 | 0 | 0 | 0.000000 | 4 | `` |
| 29 | `minus` | 5 | 0 | 0 | 0.000000 | 5 | `` |
| 31 | `plus` | 5 | 1 | 1 | 1.000000 | 3 | `29:12` |
| 31 | `minus` | 4 | 1 | 0 | 0.000000 | 4 | `` |
| 101 | `plus` | 11 | 3 | 1 | 0.333333 | 9 | `97:39` |
| 101 | `minus` | 12 | 3 | 2 | 0.666667 | 8 | `83:29,89:22` |
| 499 | `plus` | 40 | 16 | 9 | 0.562500 | 22 | `491:210,467:173,433:171,487:166,439:146` |
| 499 | `minus` | 44 | 16 | 6 | 0.375000 | 32 | `457:176,401:142,409:120,449:103,419:18` |
| 1009 | `plus` | 72 | 29 | 17 | 0.586207 | 38 | `997:421,947:415,991:325,823:304,827:301` |
| 1009 | `minus` | 70 | 29 | 9 | 0.310345 | 52 | `967:378,883:370,877:315,971:218,937:214` |
| 2003 | `plus` | 125 | 51 | 28 | 0.549020 | 69 | `1999:990,1997:978,1993:942,1987:858,1879:706` |
| 2003 | `minus` | 139 | 51 | 18 | 0.352941 | 103 | `1867:779,1759:623,1823:615,1637:497,1949:457` |
| 4999 | `plus` | 300 | 118 | 58 | 0.491525 | 184 | `4993:2476,4987:2416,4973:2136,4651:2063,4969:2020` |
| 4999 | `minus` | 289 | 118 | 46 | 0.389831 | 197 | `4861:2162,4903:2109,4639:1994,4831:1951,4679:1911` |

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `noslot_phaseband_identity` | `closed` | NoSlotLoad_side(P) equals the number of tail primes q=P-2b with delta_side(b)>floor((P-1)/2). |
| `halfgrid_pressure_to_phaseband_pdec` | `closed` | HalfGridSurvivors_side(P)<=2*NoSlotLoad_side(P) is equivalent to NoSlotPhaseBandCount_side(P)>=ceil(HalfGridSurvivors_side(P)/2). |
| `finite_no_phaseband_pressure_pdec` | `finite_evidence` | The finite audit finds no no-slot phase-band pressure PDEC up to the tested bound. |
| `phaseband_density_exclusion` | `open` | A global proof still needs to exclude the tail-prime phase-band density needed to cover half of the half-grid survivors, or route it to PDEC/SAE/ColumnCRT. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `NoSlotPhaseBandIdentityClosed` | `true` | `true` | `NoSlotLoad` 已完全等价为尾素二次相位 gap 落入上半带。 | closed |
| `PressureDefectEqualsPhaseBandPDECClosed` | `true` | `true` | 最新总压力反例等价于 no-slot 相位带尾素数达到半个半网格幸存数。 | closed |
| `FiniteNoPhaseBandPressurePDEC` | `true` | `false` | 有限扫描 P<=5000 中没有相位带压力 PDEC。 | finite evidence only |
| `GlobalPhaseBandDensityExcluded` | `false` | `false` | 仍需全局排斥尾素二次相位上半带密度异常。 | NoSlotTailPrimePhaseBandDensityPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把最新硬点压成唯一相位带 PDEC，不关闭全局行/列命题。 | NoSlotTailPrimePhaseBandDensityPDECExclusion |

## 8. 下一步

- 主攻：`NoSlotTailPrimePhaseBandDensityPDECExclusion`。
- 也就是排斥尾素 `q=P-2b` 在二次相位上半带中的密度高到覆盖半个 half-grid survivor 数。
- 若不能直接排斥，应将持久高密度相位带登记为 PDEC、端点 SAE 或 ColumnCRT。
- 当前仍未证明全局行/列无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py` | `d7f77df43459b5a51641980dbb6768baa1e1657261e6a61f889930a262c2c32e` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
| `experiments/prime_matrix_square_phase_halfgrid_boundary_word_router.py` | `e432647d97be53b293f53cc6e3713982f9540848941e3f14a97ed771ae10ba99` |
| `data/square-phase-halfgrid-noslot-phaseband-pdec-ledger.json` | `2c8cdd78cf92527bb7a968cceca92a4148550034dc2fb512b4ef1016ecc86888` |
