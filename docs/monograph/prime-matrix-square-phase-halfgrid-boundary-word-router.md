# Prime Matrix square-phase half-grid boundary word router

**状态：** `square_phase_special_longblock_reduced_to_even_halfgrid_boundary_word_open`

本步把平方锚特殊相位长块命中压成偶数半网格覆盖字。因为 `P` 为奇素数，`P^2±r` 在所有奇数 `r` 上都被 `q=2` 覆盖；因此真正决定平方锚素数的只有 `r=2s`。逐项审计证明 `PrimeWindow_side(P)` 精确等于 signed half-grid 中未被奇素数 `q<P` 覆盖的槽数。于是最新总压力硬点化为 `HalfGridSurvivors_side(P)>2*NoSlotLoad_side(P)`。有限扫描没有半网格全覆盖或总压力缺陷；全局仍需证明该半网格幸存下界，或登记边界覆盖字 PDEC/SAE/ColumnCRT。

```text
max_p=5000
finite_prime_count=668
halfgrid_prime_identity_failure_count=0
full_cover_count=0
total_pressure_defect_count=0
row_column_unconditional_closed=false
```

## 1. 半网格正规形

由于 `P` 为奇素数，奇数 `r` 使 `P^2±r` 为偶数，所以全部由 `q=2` 覆盖。令 `r=2s`，`1<=s<=(P-1)/2`。对奇素数 `q<P`：

```text
plus:  q | P^2+2s  iff  s == -P^2 * 2^{-1} (mod q),
minus: q | P^2-2s  iff  s ==  P^2 * 2^{-1} (mod q).
```

因此平方锚全覆盖等价于 signed half-grid 没有任何幸存槽。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| record count | 1336 |
| combined PrimeWindow | 194541 |
| combined half-grid survivors | 194541 |
| combined NoSlotLoad | 34194 |
| identity failures | 0 |
| full cover count | 0 |
| total pressure defect count | 0 |
| min total pressure margin | 1 |
| max boundary run | 106 |

## 3. 边界记录

| label | P | side | W | half survivors | NoSlot | W-2N | boundary run | first survivor r |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| worst margin | 3 | `minus` | 1 | 1 | 0 | 1 | 0 | 2 |
| max boundary run | 3019 | `minus` | 177 | 177 | 26 | 125 | 106 | 2912 |

## 4. 样本边界覆盖字

| P | side | boundary run | first survivor r | word prefix | survivor prefix |
| ---: | --- | ---: | ---: | --- | --- |
| 13 | `plus` | 3 | 4 | `3` | `4,10,12` |
| 13 | `minus` | 0 | 12 | `` | `2,6,12` |
| 17 | `plus` | 3 | 4 | `3` | `4` |
| 17 | `minus` | 4 | 12 | `3,5` | `6,8,12` |
| 19 | `plus` | 5 | 6 | `3,5` | `6,12,18` |
| 19 | `minus` | 4 | 14 | `7,3` | `2,8,12,14` |
| 23 | `plus` | 11 | 12 | `3,13,5,3,7` | `12,18` |
| 23 | `minus` | 2 | 20 | `3` | `6,8,20` |
| 29 | `plus` | 11 | 12 | `3,5,7,3,23` | `12,16,18,22` |
| 29 | `minus` | 8 | 20 | `3,5,19,3` | `2,12,14,18,20` |
| 31 | `plus` | 5 | 6 | `3,5` | `6,10,16,22,30` |
| 31 | `minus` | 6 | 24 | `7,3,5` | `8,14,20,24` |
| 101 | `plus` | 9 | 10 | `3,5,59,3` | `10,22,42,46,52,58,66,70,72,88` |
| 101 | `minus` | 2 | 98 | `3` | `8,20,24,32,38,42,50,60,62,68` |
| 499 | `plus` | 15 | 16 | `3,5,11,3,7,43,3` | `16,36,58,78,88,96,102,106,126,130` |
| 499 | `minus` | 6 | 492 | `67,3,7` | `14,20,30,92,98,108,110,114,122,132` |
| 1009 | `plus` | 9 | 10 | `3,5,7,3` | `10,16,28,42,96,120,126,136,142,166` |
| 1009 | `minus` | 4 | 1004 | `727,3` | `24,60,62,74,84,122,128,158,192,200` |
| 2003 | `plus` | 3 | 4 | `3` | `4,24,28,58,60,70,72,94,100,102` |
| 2003 | `minus` | 14 | 1988 | `3,71,17,3,5,11,3` | `18,30,32,80,86,98,110,126,138,146` |
| 4999 | `plus` | 35 | 36 | `3,5,7,3,179,97,3,13,163,3,173,5,3,23,11,3` | `36,70,88,142,150,156,190,210,238,240` |
| 4999 | `minus` | 4 | 4994 | `541,3` | `30,32,68,74,122,128,152,180,200,210` |

## 5. 命题行

| name | status | statement |
| --- | --- | --- |
| `odd_columns_removed_by_two` | `closed` | For odd P, every odd r in P^2±r is even, hence automatically covered by q=2. |
| `halfgrid_primewindow_identity` | `closed` | PrimeWindow_side(P) equals the number of uncovered even slots r=2s after sieving by odd q<P. |
| `special_long_block_halfgrid_form` | `closed` | A square-phase full cover is equivalent to zero survivors on the signed even half-grid. |
| `total_pressure_halfgrid_form` | `closed` | The latest total pressure defect is exactly HalfGridSurvivors_side(P)<=2*NoSlotLoad_side(P). |
| `finite_no_halfgrid_full_cover_or_pressure_defect` | `finite_evidence` | The finite audit finds no half-grid full cover and no total pressure defect up to the tested bound. |
| `halfgrid_survivor_lower_bound` | `open` | A global proof still needs HalfGridSurvivors_side(P)>2*NoSlotLoad_side(P), or a BoundaryWord-PDEC/SAE/ColumnCRT exclusion. |

## 6. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `OddColumnsRemovedByTwoClosed` | `true` | `true` | 平方锚窗口的奇数列由 `q=2` 自动覆盖，真实自由度只在偶数半网格。 | closed |
| `HalfGridPrimeWindowIdentityClosed` | `true` | `true` | `PrimeWindow` 已精确等于偶数半网格幸存数。 | closed |
| `FiniteNoHalfGridFullCover` | `true` | `false` | 有限扫描 P<=5000 中没有半网格全覆盖。 | finite evidence only |
| `FiniteNoTotalPressureDefect` | `true` | `false` | 有限扫描 P<=5000 中没有 `HalfGridSurvivors<=2*NoSlotLoad`。 | finite evidence only |
| `HalfGridSurvivorLowerBoundProvedGlobally` | `false` | `false` | 仍需全局证明半网格幸存数压过激活尾支撑负载的两倍。 | HalfGridSurvivorBeatsActivatedTailSupportOrBoundaryWordPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把特殊相位硬点压到半网格覆盖字，不关闭全局行/列命题。 | HalfGridSurvivorBeatsActivatedTailSupportOrBoundaryWordPDEC |

## 7. 下一步

- 主攻：`HalfGridSurvivorBeatsActivatedTailSupportOrBoundaryWordPDEC`。
- 也就是证明 signed half-grid 的幸存槽数始终大于 `2*NoSlotLoad`。
- 若失败，反例必须给出一个极长边界覆盖字；该覆盖字的责任素数序列可登记为 BoundaryWord-PDEC、端点 SAE 或 ColumnCRT。
- 当前仍未证明全局行/列无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_halfgrid_boundary_word_router.py` | `e432647d97be53b293f53cc6e3713982f9540848941e3f14a97ed771ae10ba99` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
| `data/square-phase-halfgrid-boundary-word-ledger.json` | `f6899aa901f1704c37756ac305322f0712873a0efadecb0f0f73010e5c5271e6` |
