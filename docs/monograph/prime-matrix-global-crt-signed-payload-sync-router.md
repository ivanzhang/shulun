# Prime Matrix global CRT signed payload 同步路由器

**状态：** `global_crt_internal_route_reduced_to_signed_payload_with_external_pdec_retained`

本步把 global CRT/Q1-Q2 最新前沿继续同步到 signed payload 层。`ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` 已由 strict payload 前沿压成 `AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn`。同时，PDEC same-set 手臂在当前内部自足语料中已饱和到新 joint 公式线，而该线也已回到 branch-trace/payload。因此，在不引入新的外部或 scope-PDEC 证书时，内部自足路线的最新最窄硬点是 signed payload。但新 acyclic same-set scope 证书和外部 DI/BFI 输入仍保留为独立未证入口；ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 也仍需合取闭合。行/列命题尚未无条件闭合。

```text
global_crt_branch_trace_basis_imported=true
exact_atomic_trace_reduced_to_signed_payload=true
finite_crt_cannot_generate_signed_payload=true
pdec_internal_arm_saturated_to_new_joint=true
external_or_new_pdec_scope_still_open=true
strict_internal_self_contained_basis_sharpened=true
atomic_signed_payload_constructor_proved=false
acyclic_same_set_scope_match_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
```

## 1. 同步链

| from | to |
| --- | --- |
| `global CRT branch trace frontier` | `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` |
| `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn` | `AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn` |
| `internal PDEC same-set arm` | `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` |
| `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` | `ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn then AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn` |
| `external/new PDEC scope certificate` | `retained as independent unproved input` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `GlobalCRTBranchTraceBasisImported` | `true` | `false` | 上一层已把 global CRT/Q1-Q2 路线压成 PDEC scope 或 exact atomic branch trace。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `ExactAtomicTraceReducedToSignedPayload` | `true` | `false` | branch trace 一侧已被 strict payload 前沿压到 pre-assignment signed payload constructor。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `FiniteCRTCannotGenerateSignedPayload` | `true` | `true` | CRT 周期扩张只复制零同余类和可见坐标 trace；orientation、local factor 和 signed coefficient 不是纯位置相位数据。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `PDECInternalArmSaturatedToNewJoint` | `true` | `false` | PDEC same-set 手臂在当前内部语料中已饱和；若不提交新 scope 证书，它回到新 joint 公式线。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `InternalNewJointLineAlsoReturnsToPayload` | `true` | `false` | 内部自足线中，PDEC 饱和后的新 joint 公式已经经 branch-trace 链压到 signed payload。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `ExternalOrNewPDECScopeStillOpen` | `true` | `false` | 新 acyclic same-set scope 证书或外部 DI/BFI 无投影窗口证书仍可作为独立输入，但当前未证。 | AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| `StrictInternalSelfContainedBasisSharpened` | `true` | `false` | 若不引入新的外部/scope PDEC 输入，global CRT 路线的内部自足硬点已经只剩 signed payload。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `ActualEmitterExactUVStillParallel` | `true` | `false` | payload 可登记 exact UV/key，但 bounded multiplicity incidence 仍是并行未证门。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `AtomicSignedPayloadConstructorCurrentCorpusProved` | `false` | `false` | 当前材料没有给出不经 assignment/origin 环的 atomic signed payload 正向构造公式。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `GlobalStructuralCRTContradictionCurrentCorpusFound` | `false` | `false` | 本步识别了 CRT 坐标层与 signed payload 层的结构断点，但尚未从中推出终端矛盾。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR new AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 缺少 signed payload 或新 PDEC scope 证书，同时 ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 仍未合取闭合。 | (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 活动基

内部自足线：

```text
AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

保留新 scope/PDEC 输入的总活动基：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

外部/新 scope 扩展口径：

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn
```

审稿边界：本文件只完成 global CRT 最新前沿与 signed payload 前沿的同步；
它没有证明 signed payload constructor、PDEC scope、ExactUV、模型余量、RatePreservation 或 DStructure/Rankin。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.json` | `6437fc285617d3a363361ed354cbba400ab588ee7ea6f3cd8cbb07582d196084` |
| `docs/monograph/prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json` | `fe1d86442d7936662a55cd5b8279e339f5bfd21142bd079ec80280c06423df92` |
| `docs/monograph/prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json` | `3c7602bf11d29d837d1a05964368f085de2c10dc5e786bd518b55a85b4ce3cbf` |
| `docs/monograph/prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json` | `7a72bed5901b1c6b5575db7161c23108f5f4fc17e1848d75cb00b20fd1e6c993` |
