# Prime Matrix square-phase phase-band saving dichotomy router

**状态：** `phaseband_density_pdec_reduced_to_tail_envelope_or_quadratic_phase_saving_bound_open`

本步没有转换目标，而是把当前精确余量拆成 `H-2C=(H-2T)+2(T-C)`。`H` 是半网格幸存数，也就是平方锚侧短区间素数数；`T` 是全部尾素包络；`C` 是上一层 no-slot 二次相位带尾素数。若 `H>2T`，不需要相位信息即可闭合；若 `H<=2T`，则必须由二次相位节省 `T-C` 补足，且所需节省精确为 `max(0, T-floor((H-1)/2))`。有限扫描中尾包络失败点存在，但全部由相位节省补足；全局仍需证明尾包络正余量或二次相位节省下界。

```text
max_p=5000
finite_prime_count=668
decomposition_identity_failure_count=0
tail_envelope_defect_count=21
unrescued_tail_defect_count=0
exact_pressure_defect_count=0
row_column_unconditional_closed=false
```

## 1. 恒等式

记

```text
H = HalfGridSurvivors_side(P)
T = TailPrimeCount_side(P)
C = NoSlotPhaseBandCount_side(P)
S = T-C
```

则当前目标 `H>2C` 精确等价于

```text
H-2C = (H-2T)+2S > 0.
```

`H-2T` 是丢掉二次相位后的尾素总包络余量；`S=T-C` 是二次相位避让节省。

## 2. 节省阈值

当尾包络余量 `H-2T<=0` 时，仍要闭合 `H>2C`，所需的最小整数节省为

```text
S_required = max(0, T-floor((H-1)/2)).
```

所以剩余不再是抽象密度异常，而是一个精确的二分：要么证明 `H>2T`，要么证明 `S>=S_required`。

## 3. 有限审计摘要

| metric | value |
| --- | ---: |
| record count | 1336 |
| combined H | 194541 |
| combined T | 77356 |
| combined C | 34194 |
| combined S=T-C | 43162 |
| decomposition identity failures | 0 |
| tail envelope defect count | 21 |
| tail envelope closure count | 1315 |
| unrescued tail defect count | 0 |
| exact pressure defect count | 0 |
| min exact pressure margin | 1 |
| min tail envelope margin | -3 |
| min phase saving surplus | 0 |
| max required phase saving | 2 |

## 4. 最紧边界

| label | P | side | H | T | C | S | S_req | S_surplus | H-2T | H-2C |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| exact margin | 3 | `minus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| tail envelope | 673 | `minus` | 41 | 22 | 8 | 14 | 2 | 12 | -3 | 25 |
| saving surplus | 3 | `minus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |

## 5. 样本表

| P | side | H | T | C | S | S_req | S_surplus | H-2T | H-2C |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | `plus` | 3 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |
| 13 | `minus` | 3 | 1 | 0 | 1 | 0 | 1 | 1 | 3 |
| 17 | `plus` | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 17 | `minus` | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |
| 19 | `plus` | 3 | 1 | 1 | 0 | 0 | 0 | 1 | 1 |
| 19 | `minus` | 4 | 1 | 0 | 1 | 0 | 1 | 2 | 4 |
| 23 | `plus` | 2 | 1 | 0 | 1 | 1 | 0 | 0 | 2 |
| 23 | `minus` | 3 | 1 | 0 | 1 | 0 | 1 | 1 | 3 |
| 29 | `plus` | 4 | 0 | 0 | 0 | 0 | 0 | 4 | 4 |
| 29 | `minus` | 5 | 0 | 0 | 0 | 0 | 0 | 5 | 5 |
| 31 | `plus` | 5 | 1 | 1 | 0 | 0 | 0 | 3 | 3 |
| 31 | `minus` | 4 | 1 | 0 | 1 | 0 | 1 | 2 | 4 |
| 73 | `plus` | 7 | 4 | 3 | 1 | 1 | 0 | -1 | 1 |
| 73 | `minus` | 8 | 4 | 1 | 3 | 1 | 2 | 0 | 6 |
| 101 | `plus` | 11 | 3 | 1 | 2 | 0 | 2 | 5 | 9 |
| 101 | `minus` | 12 | 3 | 2 | 1 | 0 | 1 | 6 | 8 |
| 499 | `plus` | 40 | 16 | 9 | 7 | 0 | 7 | 8 | 22 |
| 499 | `minus` | 44 | 16 | 6 | 10 | 0 | 10 | 12 | 32 |
| 1009 | `plus` | 72 | 29 | 17 | 12 | 0 | 12 | 14 | 38 |
| 1009 | `minus` | 70 | 29 | 9 | 20 | 0 | 20 | 12 | 52 |
| 2003 | `plus` | 125 | 51 | 28 | 23 | 0 | 23 | 23 | 69 |
| 2003 | `minus` | 139 | 51 | 18 | 33 | 0 | 33 | 37 | 103 |
| 4999 | `plus` | 300 | 118 | 58 | 60 | 0 | 60 | 64 | 184 |
| 4999 | `minus` | 289 | 118 | 46 | 72 | 0 | 72 | 53 | 197 |

## 6. 命题行

| name | status | statement |
| --- | --- | --- |
| `tail_envelope_phase_saving_identity` | `closed` | For each side, H-2C=(H-2T)+2(T-C), where H is half-grid survivors, T is the full tail-prime envelope, and C is no-slot phase-band load. |
| `tail_envelope_sufficient_gate` | `closed` | If H>2T, then the no-slot phase-band pressure defect is excluded without using the quadratic phase saving. |
| `phase_saving_rescue_gate` | `closed` | When H<=2T, the exact target is equivalent to T-C >= T-floor((H-1)/2). |
| `finite_no_exact_pressure_defect` | `finite_evidence` | The finite audit finds no exact phase-band pressure defect up to the tested bound. |
| `global_tail_or_saving_bound` | `open` | A global proof still needs either H>2T, or enough quadratic phase saving T-C, for every prime-square side. |

## 7. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SavingDecompositionIdentityClosed` | `true` | `true` | `H-2C=(H-2T)+2(T-C)` 逐侧逐 P 精确成立。 | closed |
| `TailEnvelopeOnlyClosesAllFiniteCases` | `false` | `false` | 若为 true，尾素总包络本身已经闭合；有限审计显示它并非总是 true。 | phase saving is needed where false |
| `PhaseSavingRescuesFiniteTailDefects` | `true` | `false` | 有限审计中所有尾包络失败点均由二次相位节省补足。 | finite evidence only |
| `ExactPhaseBandPressureDefectAbsentFinite` | `true` | `false` | 有限扫描未出现精确相位带压力缺陷。 | finite evidence only |
| `GlobalTailEnvelopeOrSavingBoundClosed` | `false` | `false` | 仍需全局证明尾包络正余量或二次相位节省下界。 | TailEnvelopeOrQuadraticPhaseSavingGlobalLowerBound |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把相位带 PDEC 拆成两项可攻输入，不关闭全局行/列命题。 | TailEnvelopeOrQuadraticPhaseSavingGlobalLowerBound |

## 8. 下一步

- 主攻：`TailEnvelopeOrQuadraticPhaseSavingGlobalLowerBound`。
- 第一支：证明平方锚短区间素数数 `H` 全局大于两倍尾素包络 `2T`。
- 第二支：在第一支失败处，证明二次相位节省 `S=T-C` 至少达到 `S_required`。
- 当前仍未证明全局行/列无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_phaseband_saving_dichotomy_router.py` | `45e05912084256ab59dfb49d4ee2a59936c079bc6cec548f96ba94767161da5e` |
| `experiments/prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py` | `d7f77df43459b5a51641980dbb6768baa1e1657261e6a61f889930a262c2c32e` |
| `data/square-phase-phaseband-saving-dichotomy-ledger.json` | `244cd2097bfc3a0203dd6801d56a59d148430f6ddcf0adb9ae3456936bf0be81` |
