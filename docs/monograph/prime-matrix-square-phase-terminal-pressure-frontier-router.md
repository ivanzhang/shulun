# Prime Matrix square-phase terminal pressure frontier router

**状态：** `terminal_noslot_counterexample_reduced_to_two_named_pressure_defects_open`

本步把当前平方锚 no-slot 剩余合并成一个终端压力前沿：若终端 no-slot 反例存在，则 split 二分强制 k0 或 k>=1 承担半阈值；前者给出 `PrimeWindow<=4*RootLoad`，后者给出 `PrimeWindow<=4*KGe1Load`。因此任何终端 no-slot 反例必须进入 RootWindowDefect 或 KGe1AggregatePressureDefect。这关闭的是最后出口的逻辑二分，不是两个命名缺陷的全局排斥。

```text
max_p=5000
finite_prime_count=668
terminal_pressure_branch_failure_count=0
pressure_to_defect_failure_count=0
terminal_to_named_defect_failure_count=0
terminal_no_slot_count=0
row_column_unconditional_closed=false
```

## 1. 终端二分

若 no-slot 分支达到终端压力，即

```text
NoSlotLoad >= ceil(PrimeWindow/2),
```

而 `NoSlotLoad=K0Load+KGe1Load`，则至少一个分支满足

```text
2*K0Load >= ceil(PrimeWindow/2)
或
2*KGe1Load >= ceil(PrimeWindow/2).
```

于是终端反例强制进入两个命名缺陷之一：

```text
RootWindowDefect:        PrimeWindow <= 4*RootLoad
KGe1AggregateDefect:    PrimeWindow <= 4*KGe1Load
```

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| combined PrimeWindow | 194541 |
| combined K0Load | 4932 |
| combined KGe1Load | 29262 |
| combined NoSlotLoad | 34194 |
| pressure branch failures | 0 |
| pressure-to-defect failures | 0 |
| terminal-to-defect failures | 0 |
| terminal no-slot count | 0 |
| root defect count | 3 |
| k>=1 defect count | 1 |
| pressure branch count | 4 |
| min margin vs 4max | -4 |

## 3. 关键记录

| label | P | side | PrimeWindow | K0 | KGe1 | NoSlot | root defect | k>=1 defect | terminal | margin vs 4max |
| --- | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | ---: |
| worst vs 4max | 523 | plus | 36 | 3 | 10 | 13 | `false` | `true` | `false` | -4 |
| worst root | 13 | plus | 3 | 1 | 0 | 1 | `true` | `false` | `false` | -1 |
| worst k>=1 | 523 | plus | 36 | 3 | 10 | 13 | `false` | `true` | `false` | -4 |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `terminal_noslot_forces_pressure_branch` | `closed` | If NoSlotLoad reaches the split threshold, then k0 or k>=1 carries half the threshold. |
| `pressure_branch_forces_named_defect` | `closed` | A k0 pressure branch forces PrimeWindow<=4*RootLoad; a k>=1 pressure branch forces PrimeWindow<=4*KGe1Load. |
| `terminal_pressure_defect_dichotomy` | `closed` | Any terminal no-slot counterexample must produce RootWindowDefect or KGe1AggregatePressureDefect. |
| `named_pressure_defect_exclusion` | `open` | A global proof still needs to exclude both named pressure defects, or register and reject their PDEC/SAE families. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SplitPressureDichotomyClosed` | `true` | `true` | 终端 no-slot 分支必落入 k0 或 k>=1 压力分支。 | closed |
| `PressureBranchToNamedDefectClosed` | `true` | `true` | 压力分支必给出 RootWindowDefect 或 KGe1AggregatePressureDefect。 | closed |
| `TerminalPressureDefectDichotomyClosed` | `true` | `true` | 任意终端 no-slot 反例都必须进入两个命名压力缺陷之一。 | closed |
| `FiniteNoTerminalNoSlotBranch` | `true` | `false` | 有限扫描 P<=5000 未出现终端 no-slot 分支。 | finite evidence only |
| `RootWindowDefectExcludedGlobally` | `false` | `false` | 仍需排斥 RootWindowDefect，或证明 PrimeSquareEndpointCountGt2SqrtP。 | PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC |
| `KGe1AggregatePressureDefectExcludedGlobally` | `false` | `false` | 仍需排斥 KGe1AggregatePressureDefect 或登记并排斥 MovingLayer-PDEC。 | KGe1AggregatePressureDefectOrMovingLayerPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭终端压力缺陷二分，不关闭全局行/列命题。 | TerminalPressureDefectDichotomyPDECExclusion |

## 6. 下一步

- 主攻：`TerminalPressureDefectDichotomyPDECExclusion`。
- 具体仍是两门：`PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC` 与 `KGe1AggregatePressureDefectOrMovingLayerPDEC`。
- 当前已闭合终端出口二分，但还没有排斥两个命名缺陷，不能称全局无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_terminal_pressure_frontier_router.py` | `132467477a992dd80f810eed5274815a7d5a2c5785a8f5f6453c2fe468cfc132` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
| `data/square-phase-terminal-pressure-frontier-ledger.json` | `0c6eb981f7954e38d12a3c4808269c7ae628aeab3c8aacca8a0cde12e8932f58` |
