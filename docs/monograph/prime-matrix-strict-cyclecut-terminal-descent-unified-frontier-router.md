# Prime Matrix strict cycle-cut / terminal descent 统一前沿

**状态：** `cyclecut_terminal_descent_pdec_unified_to_joint_declaration_line_open`

本步把 source-entropy 下游的两个出口继续统一：seed-cycle-cut 已饱和到 PDEC 或 new joint，terminal descent 已登记为宏循环，PDEC same-set 在当前 strict 内部语料中也已饱和。因此内部自足线的第一生产性单点压成 `PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple`；但 canonical-lock、independent source bridge、PDEC/外部谱、complete/fixed-key、ExactUV、模型余量、RatePreservation 和 DStructure/Rankin 仍开放，行/列命题未无条件闭合。

```text
source_entropy_exit_imported=true
seed_cycle_cut_branch_saturated=true
terminal_descent_macrocycle_detected=true
pdec_internal_branch_saturated=true
new_joint_formula_reduced_to_declaration_line=true
pre_cauchy_joint_declaration_line_proved=false
joint_productive_field_basis_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
```

## 1. 压缩边

| from | to | meaning |
| --- | --- | --- |
| `ActualPreCauchySourceDomainAbsoluteEntropyLedger` | `AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` | source entropy 下游进入 signed 坐标-来源环；不能自证，只能走 cycle-cut 或 terminal descent 出口。 |
| `AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput` | `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` | seed-cycle-cut 顺序拆分被排除，联合 emitter 路线回到 row-level 固定点。 |
| `AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate` | `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop` | terminal descent 当前下钻链形成 TERMINAL->SOURCE->PAIR->JOINT->TERMINAL 宏循环。 |
| `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate` | `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR conditionally accepted same-set/external certificate` | PDEC same-set 分支在当前 strict 内部语料中不再给独立非循环出口。 |
| `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` | `PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple` | 新的 actual joint alpha/delta 公式首个生产性字段是 Cauchy/payment 前联合 declaration line。 |
| `PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple` | `JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger` | declaration line 之后仍需 rows formula、word/coefficient identity 与命名回流账本。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `SourceEntropyExitImported` | true | false | source entropy 首原子已同步到 signed 坐标-来源环；该环不能作为证明。 | AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate |
| `SeedCycleCutBranchSaturated` | true | false | cycle-cut 分支已直接攻击到饱和：顺序拆分不成立，联合 emitter 未证且回到 signed-source 固定点。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `TerminalDescentRejectedAsWellFoundedProof` | true | false | terminal descent 当前脊柱是宏循环，不能作为 well-founded descent 或矛盾。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop |
| `PDECInternalBranchSaturated` | true | false | PDEC same-set 在当前 strict 内部语料中不是独立非循环出口；条件 PDEC/外部线只能保留为输入。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `NewJointFormulaReducedToDeclarationLine` | true | false | 新 joint 公式已字段化；第一生产性原子是同一 actual source tuple 的 pre-Cauchy 联合 declaration line。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple |
| `JointProductiveFieldBasisStillOpen` | true | false | declaration line、rows formula、word/coefficient identity 与 no-downstream-return ledger 仍未合取证明。 | PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger |
| `CanonicalLockStillParallel` | true | false | canonical-lock 可破 terminal 宏循环，但当前仅是开放并行门。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary |
| `IndependentBridgeStillParallel` | true | false | 若走 independent source bridge，必须在 ExactUV/pair-energy/joint 回环前独立证明。 | IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop |
| `PDECOrExternalConditionStillRetained` | true | false | same-set PDEC 或外部 DIBFI 可作为条件输入保留，但没有在当前内部语料中无条件证明。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch |
| `CompleteFixedExactUVModelRateDStructureGatesStillOpen` | true | false | 统一前沿只压缩 cycle/terminal/PDEC 出口；complete-key、fixed-key、ExactUV、模型余量、RatePreservation 与 DStructure 仍需独立验收。 | CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `RowColumnUnconditionalClosureReached` | false | false | 本步没有找到全局无条件矛盾；只把最新内部主攻单点压到 joint declaration line。 | row/column theorem still open |

## 3. 内部第一生产性单点

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple
```

完整 joint 字段基：

```text
PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger
```

## 4. 统一保留剩余基

```text
((PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple AND JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND JointEmitterPrepushforwardWordCoefficientIdentityLedger AND JointEmitterNoDownstreamRecoveryAndNamedReturnLedger) OR AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 结论边界

- 本文件是前沿同步与硬点压缩，不是行/列命题证明。
- terminal descent 宏循环不能当作 well-founded descent。
- PDEC same-set 在当前内部语料中只是条件保留线；自足破环仍需新的 joint declaration line 或其他独立输入。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_cyclecut_terminal_descent_unified_frontier_router.py` | `30173d6c24864ef517d4ceed1f26af90e2959ff6f9a7f39e3f7c45f184defc4b` |
| `docs/monograph/prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json` | `266319a61ccd56e74c500a1ab1e4f8ed3b977473de37b0c5647607bae3621b2a` |
| `docs/monograph/prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json` | `d374690b63ed1b8b60b5261607a84a9c83d7dfa19fb0d3803904f5f011d80c56` |
| `docs/monograph/prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json` | `23dfb706049a1477bf3532ad61c07b79cf4bba0bd68bd33da0ed6ae2621e0966` |
| `docs/monograph/prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json` | `3c7602bf11d29d837d1a05964368f085de2c10dc5e786bd518b55a85b4ce3cbf` |
| `docs/monograph/prime-matrix-strict-joint-emitter-formula-field-atom-router.json` | `c90a834b01badfa0462f3499e347ff99aa2341ee62bb288787db6eca3e9b3463` |
