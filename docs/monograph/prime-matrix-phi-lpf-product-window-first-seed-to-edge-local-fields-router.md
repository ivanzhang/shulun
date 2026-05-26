# Prime Matrix Phi-LPF product-window first seed to edge-local fields 证书

**状态：** `product_window_first_seed_synced_to_edge_local_signed_fields_open`
**核验日期：** `2026-05-26`

Product-window 的 first-edge semiprime seed 已同步到更窄的 edge-local signed fields 前沿。diagonal `(p,p)` 被 source 三原子吸收；offdiagonal `(p,q,t)` 的 LPF/Phi tuple 与 tail fiber 是无符号闭合账本；pure `(p,q)` edge 的 owner、product、rank/degree 与 multiplicity label 也已闭合。剩余不再是 LPF/Phi 支撑或容量问题，而是 tuple-level signed seed formula、edge-local signed atom fields 或命名 return，并且仍要携带 orientation、ExactUV、internal prime-adjoin transition 与 source 三原子。

```text
product_window_first_seed_imported=true
diagonal_private_signed_escape_removed=true
offdiagonal_tuple_unsigned_fields_closed=true
edge_local_unsigned_labels_closed=true
lpf_phi_unsigned_scope_exhausted=true
signed_atom_field_table_proved=false
new_primitive_payload_or_trace_artifact_present=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
tuple_level_required_attack_target=PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `PhiLPFBucketSignedCoefficientLawBeforePushforward` | `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward` | product-window bucket bridge 已把递推路线的第一直接硬点压到 first seed 与 internal transition。 |
| `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` | `PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward` | semiprime first edge 先按 `p=q` 与 `p<q` 唯一拆分。 |
| `PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward` | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | diagonal square-base lane 没有私有 signed 出口，回到已携带的 source 三原子。 |
| `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward` | `PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward AND PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward` | offdiagonal occurrence 的 owner、first q 与 q-rough tail 字段闭合；signed seed 公式仍开。 |
| `PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward` | `PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward` | two-prime pure kernel 的 swap-symmetry 伪出口已删除，只剩 canonical edge-local formula-or-return。 |
| `PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward` | `PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward AND PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` | edge-local 入口先剥离 LPF/Phi/Ferrers 无符号 label，剩余为 signed atom fields 或命名 return。 |
| `PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` | `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward` | signed fields 若不直接给出，必须进入新 primitive payload/trace、terminal descent、same-set PDEC 或逐点表旁路。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ProductWindowFirstSeedImported | `true` | `false` | product-window bucket bridge 的直接递推负载已经是 first seed 与 internal transition。 | PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| DiagonalOffDiagonalSplitImported | `true` | `true` | FIRST_SEED 可直接接入 diagonal/offdiagonal 拆分。 | PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| DiagonalPrivateSignedEscapeRemoved | `true` | `true` | diagonal `(p,p)` 不再提供私有 signed 出口，只能回到 source 三原子。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| OffDiagonalTupleUnsignedFieldsClosed | `true` | `true` | offdiagonal `(p,q,t)` 的 owner、first q、q-rough tail 与 Phi fiber mass 已闭合。 | PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward |
| OffDiagonalSignedFormulaStillOpen | `true` | `false` | tuple 的 signed seed value 不能由无符号 Phi mass 反推，必须正向给出公式或 return。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward |
| TwoPrimeSwapExitRemoved | `true` | `true` | `p*q=q*p` 不产生 signed cancellation；LPF owner 域只保留 canonical `(p,q)`。 | PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward |
| EdgeLocalUnsignedLabelsClosed | `true` | `true` | pure edge 的 owner、product、LPF bucket、rank/degree 与 multiplicity-one label 已闭合。 | PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward |
| LatestEdgeFieldCutSynced | `true` | `true` | 最新 edge-local sync 已把 formula-or-return 替换为 signed atom fields 或命名 return。 | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward |
| LPFPhiUnsignedScopeExhausted | `true` | `true` | LPF/Phi/Ferrers 在本层只支付支撑、纤维、tuple 与 edge label，不支付 sign/local factor/orientation。 | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward |
| SignedAtomTracePayloadStillOpen | `true` | `false` | 同 trace key 与命名 return 路由可接下 signed fields，但当前没有新 primitive payload/trace 工件。 | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact |
| OrientationExactUVInternalStillPaired | `true` | `false` | orientation、ExactUV return 与 internal prime-adjoin transition 是同一 first-seed 路线的配套义务。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| PointwiseSignedTableStillParallel | `true` | `false` | 逐点 Phi-LPF signed value table 仍是直接旁路，但当前没有证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| ExternalInputsStillNeedObject | `true` | `false` | 外部 trace/Type-II 或短区间输入仍需先有 signed coefficient 对象或平方根行尺度点态输入。 | ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients OR PointwiseSqrtPrimeInputCOne |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只同步 product-window first seed 的下游字段切分；没有证明三命题无条件闭合。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |

## 3. 字段耗尽表

| field group | status | remaining | meaning |
| --- | --- | --- | --- |
| diagonal square-base | `absorbed_to_source_atoms` | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows | `p=p` diagonal 不是 first-seed 的私有 signed 出口。 |
| offdiagonal tuple owner/fiber | `closed_unsigned` | PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward | `(owner_p, first_q, q_rough_tail_t)` 与 Phi tail mass 已闭合。 |
| pure two-prime canonical edge label | `closed_unsigned` | PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward | `owner_p, first_q, pq, rank/degree, multiplicity` 已闭合。 |
| tuple signed seed formula | `open_signed` | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward | 需要 source tuple 推前前 signed seed 公式。 |
| edge-local signed atom fields | `open_signed_or_return` | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward | 需要 signed value、local factor、orientation 入口、ExactUV pair 或命名 return。 |
| trace/payload productive exit | `open_payload` | NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact | 需要新的 primitive atomic signed payload/trace 工件，不能由无符号 label 自动生成。 |

## 4. 最大样本读数

| source | N | count A | count B | ok | note |
| --- | ---: | ---: | ---: | --- | --- |
| offdiagonal tuple | 10000 | 5468 | 5468 | `true` | tuple occ equals Phi tail fiber sum |
| edge-local label | 10000 | 2600 | 2600 | `true` | canonical edges equal unique closed labels |

## 5. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward OR NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients OR PointwiseSqrtPrimeInputCOne) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
```

tuple 层仍需：

```text
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

配套仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.json` | `231294a3f0a9cfe6d8af17db958a40f71b1bbfdabcefe3dc5d7c2d1a7a15b72a` |
| `docs/monograph/prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json` | `d0a1d3722c1f082d0df922c9a3e9087773419b5e53c6fef669eb61a7321e914d` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-router.json` | `0e44595e31aa51c619fbd654f67faae1afb625fad2f8b95d68b1bd56f22d9865` |
| `docs/monograph/prime-matrix-phi-lpf-latest-edge-local-field-cut-sync-router.json` | `d23f9b7f42beecfd32ee511bcde2bbe06b574d02e2bbffffa2c78107b508a562` |
| `docs/monograph/prime-matrix-phi-lpf-latest-semiprime-seed-diagonal-sync-router.json` | `581120e8ec06f7126f5ffb8e87ad7ae6b135eb2f4793f4fda75a955087e9f55b` |
| `docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json` | `f9b2e9eaf8020cde5952237044a1d62308564951b9e00f4cf163ab46d5b62ccf` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-bucket-stack-bridge-router.json` | `cd0ebf3b6efc7adc4b17abe83edca61a06b010651f8d7058f7322015bcd559c1` |
| `docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json` | `68844af913e21b39317b6f47244070c96d3c5e4b630a00b1a0c7a029f66148f6` |
| `experiments/prime_matrix_phi_lpf_product_window_first_seed_to_edge_local_fields_router.py` | `106ad031e285681aa66d8da41cf664245923b8822049cd03fd0eb190316ee5a6` |
