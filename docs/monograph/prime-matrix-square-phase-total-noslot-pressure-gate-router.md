# Prime Matrix square-phase total no-slot pressure gate router

**状态：** `joint_pressure_pdec_reduced_to_total_noslot_pressure_defect_open`

本步把 `JointPressureCompanionPDECExclusion` 压成单一标量门：终端 no-slot 反例、joint pressure-companion PDEC、以及 `PrimeWindow<=2*NoSlotLoad` 三者是同一个整数条件的不同写法。因此最新最窄剩余是证明 `PrimeWindow>2*NoSlotLoad`，或将其失败登记并排斥为 TotalPressure-PDEC。

```text
max_p=5000
finite_prime_count=668
terminal_equivalence_failure_count=0
joint_equivalence_failure_count=0
total_pressure_defect_count=0
row_column_unconditional_closed=false
```

## 1. 单一标量门

令 `W=PrimeWindow`，`N=NoSlotLoad=K0Load+KGe1Load`。由于 `N` 为整数，

```text
N >= ceil(W/2)    iff    W <= 2N.
```

因此排斥终端 no-slot 反例等价于证明

```text
PrimeWindow > 2*NoSlotLoad.
```

这也等价于排斥上一层 joint pressure-companion PDEC。

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| record count | 1336 |
| combined PrimeWindow | 194541 |
| combined NoSlotLoad | 34194 |
| terminal equivalence failures | 0 |
| joint equivalence failures | 0 |
| total pressure defects | 0 |
| terminal no-slot count | 0 |
| joint PDEC count | 0 |
| min total pressure margin | 1 |
| max total pressure margin | 225 |

## 3. 边界记录

| label | P | side | PrimeWindow | K0 | KGe1 | NoSlot | margin W-2N | terminal | joint |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| worst margin | 3 | plus | 1 | 0 | 0 | 0 | 1 | `false` | `false` |
| best margin | 4969 | minus | 307 | 3 | 38 | 41 | 225 | `false` | `false` |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `terminal_total_pressure_equivalence` | `closed` | NoSlotLoad>=ceil(PrimeWindow/2) is equivalent to PrimeWindow<=2*NoSlotLoad. |
| `joint_pdec_total_pressure_equivalence` | `closed` | The joint pressure-companion PDEC is equivalent to the total no-slot pressure defect. |
| `finite_total_pressure_absence` | `finite_evidence` | The finite audit finds PrimeWindow>2*NoSlotLoad for every tested P and sign. |
| `total_pressure_defect_exclusion` | `open` | A global proof still needs to prove PrimeWindow>2*NoSlotLoad, or register and exclude TotalPressure-PDEC. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `TerminalEqualsTotalPressureClosed` | `true` | `true` | `NoSlotLoad>=ceil(W/2)` 与 `W<=2*NoSlotLoad` 是同一个整数条件。 | closed |
| `JointPDECEqualsTotalPressureClosed` | `true` | `true` | joint pressure-companion PDEC 与总 no-slot 压力缺陷等价。 | closed |
| `FiniteNoTotalPressureDefect` | `true` | `false` | 有限扫描 P<=5000 中 `PrimeWindow>2*NoSlotLoad` 全部成立。 | finite evidence only |
| `TotalPressureDefectExcludedGlobally` | `false` | `false` | 仍需全局排斥总 no-slot 压力缺陷。 | TotalNoSlotPressureDefectExclusionOrTotalPressurePDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 joint PDEC 排斥压成单一标量不等式，不关闭全局行/列命题。 | TotalNoSlotPressureDefectExclusionOrTotalPressurePDEC |

## 6. 下一步

- 主攻：`TotalNoSlotPressureDefectExclusionOrTotalPressurePDEC`。
- 也就是证明 `PrimeWindow>2*NoSlotLoad`；若失败，登记总压力 PDEC 并继续向相位/短簇结构投影。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_total_noslot_pressure_gate_router.py` | `f32c6b8f3f24f0d74afc0bb2a37207d45fd302b4f6c88f5306f2e1e9a3c4c5e4` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
| `data/square-phase-total-noslot-pressure-gate-ledger.json` | `3f9fae4e9df0405164862cd3226fe10fb68215a6b7cf44ef8541625c862265f2` |
