# Prime Matrix square-phase joint pressure PDEC router

**状态：** `terminal_counterexample_reduced_to_joint_pressure_companion_pdec_open`

本步把 companion-lift 进一步登记为唯一 joint PDEC family：若终端 no-slot 反例存在，则它不只需要某个压力缺陷，还需要同一 `P,side` 的伴随分支补量，因此必落入 RootWindowCompanionLiftJointPDEC 或 KGe1CompanionLiftJointPDEC。有限扫描未发现 joint PDEC；全局仍需证明该 joint family 不存在或回流到更强缺陷。

```text
max_p=5000
finite_prime_count=668
joint_pdec_count=0
terminal_no_slot_count=0
terminal_to_joint_pdec_failure_count=0
row_column_unconditional_closed=false
```

## 1. Joint PDEC schema

| family | required structure |
| --- | --- |
| `RootWindowCompanionLiftJointPDEC` | `PrimeWindow<=4*RootLoad` and `KGe1Load>=ceil(PrimeWindow/2)-RootLoad` |
| `KGe1CompanionLiftJointPDEC` | `PrimeWindow<=4*KGe1Load` and `RootLoad>=ceil(PrimeWindow/2)-KGe1Load` |

## 2. 有限审计摘要

| metric | value |
| --- | ---: |
| side records | 1336 |
| joint PDEC count | 0 |
| terminal no-slot count | 0 |
| terminal-to-joint failures | 0 |
| min root companion gap | -113 |
| min k>=1 companion gap | -113 |

## 3. 最坏 gap 记录

| label | P | side | PrimeWindow | K0 | KGe1 | NoSlot | root gap | k>=1 gap | terminal |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| worst root gap | 4969 | minus | 307 | 3 | 38 | 41 | -113 | -113 | `false` |
| worst k>=1 gap | 4969 | minus | 307 | 3 | 38 | 41 | -113 | -113 | `false` |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `joint_pressure_companion_schema` | `closed` | A terminalized pressure defect is registered as a joint PDEC with both branch loads and companion gap. |
| `terminal_noslot_implies_joint_pdec` | `closed` | Any terminal no-slot counterexample implies RootWindowCompanionLiftJointPDEC or KGe1CompanionLiftJointPDEC. |
| `finite_joint_pdec_absence` | `finite_evidence` | The finite audit finds no joint pressure-companion PDEC up to the tested bound. |
| `joint_pdec_exclusion` | `open` | A global proof still needs to exclude the joint PDEC family. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `JointPDECSchemaClosed` | `true` | `true` | pressure defect 与 companion-lift 的同时贴合已有唯一 joint PDEC schema。 | closed |
| `TerminalNoSlotImpliesJointPDECClosed` | `true` | `true` | 任意终端 no-slot 反例必落入 joint PDEC family。 | closed |
| `FiniteNoJointPDEC` | `true` | `false` | 有限扫描 P<=5000 中没有 joint PDEC。 | finite evidence only |
| `JointPDECExcludedGlobally` | `false` | `false` | 仍需全局排斥 joint PDEC family。 | JointPressureCompanionPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把终端反例压成 joint PDEC，不关闭全局行/列命题。 | JointPressureCompanionPDECExclusion |

## 6. 下一步

- 主攻：`JointPressureCompanionPDECExclusion`。
- 若不能直接排斥，需要继续把 joint family 投影到更具体的相位/短簇/平方窗输入。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_joint_pressure_pdec_router.py` | `2cfa2a840b282e4b52cfa8373f6cc9876d608a3b5fcc26c35c1f9f7ec2e002e6` |
| `experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py` | `e76e3d8cd721359fca8f6eaf0524787010ed2507ba471a448747d9ee6282c970` |
| `data/square-phase-joint-pressure-pdec-ledger.json` | `739f6a2c010da5d017542dd4369a2a7bb258aaee0c73d0823679699d2e1f626c` |
