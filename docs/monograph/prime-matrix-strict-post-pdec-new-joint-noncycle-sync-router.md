# Prime Matrix strict post-PDEC new-joint 非循环同步证书

**状态：** `post_pdec_new_joint_internal_route_saturated_to_signed_lane_cycle_kz_nocycle_open`

本步继续攻击 post-PDEC 前沿中的 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`。导入 global CRT branch-trace、signed payload、atomic trace payload、signed-lane cycle、new primitive 和 source-rank convergence 证书后，当前内部 new-joint 路线已被压成 signed-lane/source-rank/alpha 终端循环：旧 joint/antisplit 链只给 exact branch trace；branch trace 只给可见坐标；signed payload 又回到 origin/common-packet 闭环；new primitive 若要破环必须是闭环外的 pre-Cauchy actual source rank/no-collapse 工件，而当前没有提交。因而 new-joint 不再是当前内部非循环出口。除非新增真正的 joint/payload/PDEC/external 输入，剩余内部非循环路线收窄为不复用 NCBLK/source-root 的 Kuznetsov/DLS 证明，并仍需高段模型、RatePreservation 与 DStructure/Rankin。行/列命题仍未无条件闭合。

```text
new_joint_current_internal_route_saturated=true
new_explicit_joint_constructor_formula_artifact_present=false
exact_atomic_branch_trace_formula_proved=false
atomic_signed_payload_constructor_proved=false
signed_lane_self_proof_eliminated=true
new_primitive_artifact_independent_present=false
noncircular_kuznetsov_dls_without_source_root_reuse_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PostPDECNewJointActive` | `true` | `false` | PDEC scope 饱和后，当前内部首攻点是新的显式 joint alpha/delta 构造公式。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| `NewJointToBranchTraceImported` | `true` | `false` | 旧 joint/antisplit/atomic rows/builtin-pairing 链把 new-joint 生产性内容压到 exact atomic branch trace。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| `BranchTraceToSignedPayloadImported` | `true` | `false` | 可见 branch trace 只给坐标；signed coefficient/local factor 需要 atomic signed payload constructor。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `FiniteCRTDoesNotCreateSignedPayload` | `true` | `true` | CRT 周期与相位复制不能生成 orientation、local factor 或 signed coefficient。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `SignedLaneCycleImported` | `true` | `true` | branch trace、signed payload、origin identity 与 common packet 已形成闭环；环内节点不能自证。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| `NewPrimitiveMustBeOutsideCycle` | `true` | `false` | new primitive 若只是 trace/payload/origin/common-packet 改名则无效；若要破环必须携带 pre-Cauchy actual source rank/no-collapse 包。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| `SourceRankConvergesToPointwiseKernel` | `true` | `false` | new primitive 与 terminal descent 的内部路线已经汇到同 formal-unit pointwise kernel/alpha 前沿，不是独立终点。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| `NewJointCurrentInternalRouteSaturated` | `true` | `false` | 当前内部 new-joint 路线回到 signed-lane/source-rank/alpha 终端循环；没有给出非循环构造公式。 | new external/primitive joint payload input or KZ no-cycle |
| `NonCircularKZStillOpen` | `true` | `false` | 并行非循环 KZ/DLS 仍未证明；普通 KZ 路线若复用 NCBLK/source-root 则循环。 | NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只删除 new-joint 的旧内部自证路线；没有得到无条件终端矛盾。 | NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 最新内部非循环基

```text
NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件保留的新输入线：

```text
(NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY OR NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse
```

条件新输入仍可为：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
```

## 3. 诚实边界

- 本证书不证明 new-joint、不证明 signed payload，也不证明非循环 KZ/DLS。
- 它只说明当前内部 new-joint 旧路线回到 signed-lane/source-rank/alpha 终端循环。
- 新的 joint/payload/PDEC/external 输入仍可作为独立输入，但当前没有提交。
- 高段模型、RatePreservation 与 DStructure/Rankin 仍未闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_post_pdec_new_joint_noncycle_sync_router.py` | `dd75cb447c15839666026306a30a1c5292ee8b39aa31ab468fe747efc68084b9` |
| `docs/monograph/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json` | `8ea074295bea6900bdb26efb22686da30430e22f94003d9362a25884788bf5d2` |
| `docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.json` | `6437fc285617d3a363361ed354cbba400ab588ee7ea6f3cd8cbb07582d196084` |
| `docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.json` | `969459391db184ef4250b42c88f9947e1884ac92523320b47f887f729e8c6c56` |
| `docs/monograph/prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json` | `fe1d86442d7936662a55cd5b8279e339f5bfd21142bd079ec80280c06423df92` |
| `docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json` | `17e1966e5e4dad0a168abc867d451291be4991c999f28bfbaf494d5875447bf1` |
| `docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json` | `3194b1509c245cd42f607bbab6b96a1e17420454c3ae40245fb859985d38a601` |
| `docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.json` | `3359bdbe51404005aec41ec0378840a4d114c235f20354ef488e2592e3f692c7` |
