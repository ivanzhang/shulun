# Prime Matrix strict 非递归核表到终端叶子同步证书

**状态：** `nonrecursive_kernel_joint_route_synced_to_terminal_leaf_open`

本步把新非递归核表合同与旧 joint-alpha 固定点、终端叶子防火墙接通。结论是：刚钉出的 joint constructor rule 若没有新的显式公式，只会沿 joint alpha-side/same-row/row-level 表回到 signed-source 固定点。终端下降 schema 已去掉无名自循环，但当前活动叶子仍是 canonical-lock 或 noncanonical full-S 合法模式；二者均未证明，所以行/列命题仍未无条件闭合。

```text
sync_closed=true
field_contract_boundary_closed=true
joint_constructor_path_is_fixed_point_without_new_formula=true
terminal_descent_schema_closed=true
current_leaf_firewall_active_basis_reduced=true
noncanonical_legal_closure_mode_proved=false
acyclic_terminal_canonical_lock_proved=false
row_column_unconditional_closed=false
```

## 1. 前沿同步

`NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn` 的第一生产性原子 `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple` 已由既有 joint-alpha 链同步到 signed-source 固定点；除非提交新的 actual joint constructor 公式工件，否则该正向构造线不能闭合。因此当前内部自足硬点回到终端叶子前沿：`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode`，同时保留 `ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem`、`RatePreservationLedger_FOR_moving_atom_packet` 与 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 并行验收。

## 2. 同步链

| from | to |
| --- | --- |
| NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| JointAlphaSidePrimitiveWordCoefficientRuleLedger | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands | signed-source fixed point |
| signed-source fixed point | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate | TerminalLeafFirewallInputs_OR_CanonicalLock |
| TerminalLeafFirewallInputs_OR_CanonicalLock | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NonrecursiveFieldContractImported` | `true` | `true` | 非递归逐点核表字段边界已闭合，第一生产性原子钉为 joint constructor rule。 | ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple |
| `JointConstructorRouteReducesToAlphaSide` | `true` | `false` | 显式 joint alpha/delta rule 继续压成 joint alpha-side word/coefficient rule，未给公式。 | JointAlphaSidePrimitiveWordCoefficientRuleLedger |
| `JointAlphaSideReducesToSameRow` | `true` | `false` | joint alpha-side 的硬点是 unsigned word skeleton 与 signed coefficient 同行同源。 | JointAlphaSameRowPrimitiveWordSignedCoefficientOriginIdentityBeforePushforward |
| `SameRowBridgeReturnsToRowLevelTable` | `true` | `false` | same-row 桥接回收到逐行 clean-core 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `JointRouteHitsSignedSourceFixedPoint` | `true` | `true` | joint-alpha/cycle-cut 线已证明会回到 signed-source 固定点，不能作为非循环证明。 | AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `TerminalDescentSchemaClosedLeafOpen` | `true` | `false` | 终端 well-founded 下降的无隐藏循环 schema 已闭合，但叶子防火墙未全排斥。 | TerminalLeafFirewallInputs_OR_CanonicalLock |
| `CurrentLeafFirewallReduced` | `true` | `false` | 当前已物化 PDEC/sparse 前沿清零后，活动终端剩 canonical-lock 或 noncanonical legal mode。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode |
| `NoncanonicalLegalModeStillOpen` | `true` | `false` | noncanonical full-S 合法模式仍需实际源恒等、强化反原子或外部合同；strict 自足线未闭合。 | NoncanonicalFullSComplementLegalClosureMode |
| `ExactUVIncidenceStillParallel` | `true` | `false` | 非递归核表的 rank/multiplicity 口径仍需 actual exact-UV bounded multiplicity incidence。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `RatePreservationStillOpen` | `false` | `false` | moving-atom packet 的 log-power 速率保持仍未由当前同步证明。 | RatePreservationLedger_FOR_moving_atom_packet |
| `DStructureGateStillOpen` | `true` | `false` | DStructure/Rankin 晋级门仍只完成边界命名，未独立接受。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 当前同步只删除 joint constructor 伪出口并定位终端二选一，尚未得到反例矛盾。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 当前严格活动基

```text
(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一主攻点：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode
```
