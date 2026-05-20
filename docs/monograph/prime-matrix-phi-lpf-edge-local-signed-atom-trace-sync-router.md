# Prime Matrix Phi-LPF edge-local signed atom trace-sync 证书

**状态：** `phi_lpf_edge_local_signed_atom_fields_reduced_to_new_payload_or_named_return_open`

edge-local signed atom fields 不能由 LPF/Phi/Ferrers label 推出。它们必须在同一 pre-Cauchy trace key 上一次性给出 signed value、local factor、orientation/branch side、alpha/delta payload、ExactUV fixed pair 与 source row；任何缺失、冲突、零因子、超预算或后验读取都进入命名 return。现有 branch-trace/atomic-trace 线已闭成 signed-lane 自证环，因此当前非循环剩余压到新 primitive payload/trace 工件，或 terminal descent/PDEC scope/逐点 signed table，并仍需 ExactUV、模型、Rate 与 DStructure。

```text
signed_atom_fields_target_imported=true
closed_unsigned_edge_labels_imported=true
same_trace_key_requirement_closed=true
named_return_matrix_closed=true
atomic_trace_reduced_to_signed_payload=true
signed_lane_cycle_imported=true
signed_lane_self_proof_eliminated=true
branch_trace_self_proof_eliminated=true
new_primitive_payload_or_trace_artifact_present=false
edge_local_signed_atom_fields_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SignedAtomFieldsTargetImported | `true` | `false` | 上一层已把 edge-local 剩余压到 signed atom fields 或 named return tag。 | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward |
| ClosedUnsignedEdgeLabelsImported | `true` | `true` | LPF/Ferrers edge labels 已闭合，可作为 trace-sync 输入域。 | PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward |
| SameTraceKeyRequirementClosed | `true` | `true` | 若 signed 字段属于不同 trace/source key，则不是 edge-local formula，而是 named split/PDEC return。 | PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward |
| NamedReturnMatrixClosed | `true` | `true` | 每个 signed 字段的缺失、零因子、冲突、超预算或后验读取都有命名 return，不再保留匿名缺口。 | PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward |
| BranchTraceWouldSupplyOrientationConditionally | `true` | `true` | 完整 branch trace 若作为新输入存在，可同时提供 orientation/local factor/ExactUV return 字段。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| AtomicTraceReducedToSignedPayload | `true` | `false` | atomic trace 的可见坐标不产生 signed payload；生产性字段压到 payload constructor。 | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| SignedLaneSelfProofEliminated | `true` | `true` | common packet -> builtin pairing -> branch trace -> payload -> origin identity 已成闭环，不能自证。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| BranchTraceSelfProofEliminatedGlobally | `true` | `true` | 全局 strict 前沿已排除 branch trace 作为当前内部语料的独立证明路线。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate |
| BuiltinPairingStillConditional | `true` | `false` | built-in signed pairing 仍只被条件性压到 exact atomic branch trace。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| ExactUVStillIndependent | `true` | `false` | trace-sync 可登记 edge UV 字段，但 source entropy/fiber 有界性仍是独立门。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| PointwiseTableStillAlternativeButOpen | `true` | `false` | 逐点 Phi-LPF signed table 可作为替代新工件，但当前未提交。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| SignedAtomTraceSyncCurrentCorpusProved | `false` | `false` | 当前语料没有新 primitive payload/trace 工件来填充 same-trace signed atom 字段。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| EdgeLocalSignedAtomFieldsCurrentCorpusProved | `false` | `false` | 命名 return 矩阵只排除匿名缺口，不给 signed value/local factor 公式。 | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步不证明三命题无条件闭合；仍需新 payload/trace、terminal descent 或 PDEC scope，并合取 ExactUV 与晋级门。 | (NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |

## 2. 同 trace key / return 矩阵

| field | same-key requirement | named return | productive input |
| --- | --- | --- | --- |
| `same_trace_key` | edge label、source row、signed value、local factor、orientation、ExactUV 必须属于同一 pre-Cauchy trace key。 | SameTraceKeySplitPDEC | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| `signed_seed_value` | signed seed value 必须由同一 trace 的 payload 字段正向输出。 | MissingSignedAtomValueReturn OR SignedValueConflictPDEC | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `local_factor_multiplier` | local factor 乘积必须与 signed value 和 truncation state 同源。 | ZeroLocalFactorNamedReturn OR LocalFactorTraceMismatchPDEC | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `orientation_parity` | orientation parity 与 branch side 必须从同一 ordered branch operations 读取。 | OrientationBranchSideMismatchReturn | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| `alpha_delta_side` | alpha/delta payload 必须与 signed coefficient 的 formal unit 相同。 | AlphaDeltaSideMismatchReturn | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `exactuv_fixed_pair` | exact `(u,v)`、branch key 与 return tag 必须在 Cauchy/Phi/payment 前同步输出。 | ExactUVMissingOrOverBudgetReturn | PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| `pre_cauchy_source_row` | source row 必须先于 pushforward 登记；不能从下游 payment 或 fiber 反推。 | PreCauchySourceRowAbsentReturn | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |

## 3. slot 规模审计

| N | canonical edges | unsigned labels | open fields/edge | open slots | trace packets |
| --- | ---: | ---: | ---: | ---: | ---: |
| 30 | 7 | 7 | 6 | 42 | 7 |
| 100 | 30 | 30 | 6 | 180 | 30 |
| 997 | 287 | 287 | 6 | 1722 | 287 |
| 5003 | 1347 | 1347 | 6 | 8082 | 1347 |
| 10000 | 2600 | 2600 | 6 | 15600 | 2600 |

## 4. 最新保留基

```text
((NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance)
```

下一直接主攻：

```text
NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact
```

并行出口：

```text
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_edge_local_signed_atom_trace_sync_router.py` | `7c67ade8f881b806cd1a39645e8f82cf89be1c6192db3f2857056893ed80195e` |
| `docs/monograph/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json` | `d0a1d3722c1f082d0df922c9a3e9087773419b5e53c6fef669eb61a7321e914d` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json` | `fe1d86442d7936662a55cd5b8279e339f5bfd21142bd079ec80280c06423df92` |
| `docs/monograph/prime-matrix-strict-branch-trace-signed-payload-cycle-router.json` | `67da3805e5bdb503d768a79b95a3408bbdfede3254557e2e89080e2229d0e3b0` |
| `docs/monograph/prime-matrix-strict-signed-lane-cycle-closure-router.json` | `17e1966e5e4dad0a168abc867d451291be4991c999f28bfbaf494d5875447bf1` |
| `docs/monograph/prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json` | `094823b99842eeb4525d7ea868658fa39ba3d5ac0e7c0163499ab2b70b6f4b5b` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
