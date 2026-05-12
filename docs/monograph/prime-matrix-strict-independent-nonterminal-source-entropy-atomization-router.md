# Prime Matrix strict 独立非终端 source entropy 原子化路由器

**状态：** `strict_independent_nonterminal_source_entropy_atomized_to_preterminal_support_capacity_open`

本步没有换命题，而是把 `IndependentNonterminalProofOfNewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` 压成同一命题内部的唯一非终端源侧原子：`PreTerminalActualFullSFactorSupportCapacityTheorem`。balanced range 已关闭；K4/K6、朴素 incidence、canonical 偷渡和外部 KLS 都不能作为 strict 自足证明。该原子尚未证明，行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
independent_nonterminal_atomization_closed=true
fixed_point_spine_rejected_as_proof=true
external_lane_excluded_from_strict_self_contained_line=true
preterminal_actual_fulls_factor_support_capacity_proved=false
independent_nonterminal_source_entropy_proof_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 同命题原子化

目标仍是：

```text
NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```

非终端内部原子为：

```text
PreTerminalActualFullSFactorSupportCapacityTheorem
```

条件推出式：

```text
PreTerminalActualFullSFactorSupportCapacityTheorem AND RegisteredCapacityMultiplierDiscipline => NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `IndependentNonterminalTargetActive` | `true` | `false` | 上一层已删除 ExactUV/pair/terminal 固定点证明脊柱，留下独立非终端证明目标。 | IndependentNonterminalProofOfNewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `SameTheoremEntropyNormalFormPreserved` | `true` | `false` | 仍证明同一 source entropy 定理；只允许使用源侧支撑/容量估计加登记容量乘子纪律。 | NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem |
| `OldNoncanonicalCoreAligned` | `true` | `false` | 旧 noncanonical 源核心已把 entropy/anti-atom 二义性压成 actual 支撑/容量核心。 | ActualNoncanonicalFullSFactorSupportCapacityTheoremInput AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `MovingBlockJointAttackAligned` | `true` | `false` | moving-block 内部路与 Full-S KLS 外部路已对齐；strict 自足线只能走内部 exact support/capacity。 | FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource |
| `ExternalLaneNotUsedForStrictSelfContainedProof` | `true` | `true` | 外部 dispersion/KLS 仍可作条件路线，但不能用于 strict 自足证明当前非终端目标。 | internal support/capacity atom only。 |
| `BalancedRangeAlreadyRemoved` | `true` | `true` | balanced range 阈值不再是活动障碍；剩余必须直接控制 actual exact factor support 和容量兼容。 | PreTerminalActualFullSFactorSupportCapacityTheorem |
| `K4K6IncidenceCanonicalShortcutsRejected` | `true` | `true` | K4/K6、朴素 incidence、canonical 支撑偷渡均不能证明 moving same-(u,v) 源熵。 | PreTerminalActualFullSFactorSupportCapacityTheorem |
| `IndependentNonterminalAtomPinned` | `true` | `false` | 独立非终端证明等价压成 pre-terminal actual full-S 因子支撑/容量定理。 | PreTerminalActualFullSFactorSupportCapacityTheorem |
| `PreTerminalActualFullSFactorSupportCapacityCurrentCorpusProved` | `false` | `false` | 当前语料尚未证明该源侧支撑/容量定理，因此不能升级为 source entropy 或行/列无条件闭合。 | PreTerminalActualFullSFactorSupportCapacityTheorem |

## 3. 结构结论

独立非终端 source entropy 证明不能再经 ExactUV/pair-mass 失败、终端三原子或 canonical scoped case。在当前语料中，它与 actual noncanonical full-S 的 pre-terminal 因子支撑/容量定理同义：对每个幸存 formal unit，直接证明 exact (u,v) 支撑下界与 Type/Fourier 容量兼容。

## 4. 下一主攻点

```text
PreTerminalActualFullSFactorSupportCapacityTheorem
```
