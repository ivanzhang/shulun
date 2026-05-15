# Prime Matrix square-phase terminal pressure PDEC registration router

**状态：** `terminal_pressure_defects_registered_pdec_families_exclusion_open`

本步把终端压力二分的两个出口登记为可审查 PDEC family：RootWindowDefect 记录 P、side、根窗 q 区间、负载和 margin；KGe1AggregatePressureDefect 记录 P、side、聚合负载、top moving atoms 和 margin。因此任何终端 no-slot 反例若出现，不再是无名失败，而必须落入这两个已登记 family。全局仍需排斥这些 family，不能声称命题已无条件闭合。

```text
max_p=5000
finite_prime_count=668
registered_pdec_count=4
rootwindow_pdec_count=3
kge1_pdec_count=1
terminal_registered_pdec_count=0
row_column_unconditional_closed=false
```

## 1. PDEC family

| family | registered fields | defect inequality |
| --- | --- | --- |
| `RootWindowDefectPDEC` | `P, side, root_q_interval, root_b_interval, RootLoad, PrimeWindow, terminal flag` | `PrimeWindow<=4*RootLoad` |
| `KGe1AggregatePressureDefectPDEC` | `P, side, KGe1Load, top moving atoms, PrimeWindow, terminal flag` | `PrimeWindow<=4*KGe1Load` |

## 2. 有限登记摘要

| metric | value |
| --- | ---: |
| registered PDEC count | 4 |
| RootWindow PDEC count | 3 |
| KGe1 PDEC count | 1 |
| pressure-branch registered count | 4 |
| terminal registered count | 0 |
| min defect margin | -4 |

## 3. 最坏登记样本

| family | P | side | branch | PrimeWindow | branch load | no-slot | pressure | terminal | margin | formal unit |
| --- | ---: | --- | --- | ---: | ---: | ---: | --- | --- | ---: | --- |
| KGe1AggregatePressureDefectPDEC | 523 | plus | k>=1 | 36 | 10 | 13 | `true` | `false` | -4 | P=523\|side=plus\|branch=k>=1\|K1=10 |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `rootwindow_pdec_schema` | `closed` | Every RootWindow pressure defect is registered with P, side, root q-window, load, margin, and terminal flag. |
| `kge1_aggregate_pdec_schema` | `closed` | Every k>=1 aggregate pressure defect is registered with P, side, aggregate load, top moving atoms, margin, and terminal flag. |
| `terminal_defect_has_registered_family` | `closed` | Any terminal no-slot counterexample enters one of the two registered PDEC families. |
| `registered_pressure_pdec_exclusion` | `open` | A global proof still needs to exclude the registered RootWindow and MovingLayer PDEC families. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `RootWindowPDECSchemaClosed` | `true` | `true` | RootWindowDefect 已有固定 formal-unit 字段和缺陷不等式。 | closed |
| `KGe1MovingLayerPDECSchemaClosed` | `true` | `true` | KGe1AggregatePressureDefect 已有固定 formal-unit 字段和 top moving atoms。 | closed |
| `FiniteRegisteredPressureDefectsNonterminal` | `true` | `false` | 有限扫描 P<=5000 中已登记压力缺陷均非终端 no-slot。 | finite evidence only |
| `RegisteredRootWindowPDECExcludedGlobally` | `false` | `false` | 仍需证明 RootWindowDefect family 不能在终端反例链中持久出现。 | PrimeSquareEndpointCountGt2SqrtPOrRootWindowPDEC |
| `RegisteredKGe1MovingLayerPDECExcludedGlobally` | `false` | `false` | 仍需证明 KGe1AggregatePressureDefect family 不能在终端反例链中持久出现。 | KGe1AggregatePressureDefectOrMovingLayerPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只登记缺陷 family，不关闭全局行/列命题。 | RootWindowPDECAndMovingLayerPDECExclusion |

## 6. 下一步

- 主攻：`RootWindowPDECAndMovingLayerPDECExclusion`。
- RootWindow 侧可继续攻 `PrimeSquareEndpointCountGt2SqrtP` 或证明根缺陷不能终端化。
- MovingLayer 侧可继续攻 top moving atoms 的相位/短簇不可持久化。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_terminal_pressure_pdec_registration_router.py` | `aa4cace41849cf851dc5ed7117bbff7ee9e8cc0b6f1c3bae2a1658b2e32fa491` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
| `experiments/prime_matrix_square_phase_k0_rootwindow_defect_router.py` | `9287ea0da760a470634e04dc7304b6a3df43460a5bbea96eeaac8b3a59e0be6c` |
| `data/square-phase-terminal-pressure-pdec-registration-ledger.json` | `bc80f44f7c3fc573fcda4b2754ad0ec1bec19b46aecf1ec794bd2a43c17949e1` |
