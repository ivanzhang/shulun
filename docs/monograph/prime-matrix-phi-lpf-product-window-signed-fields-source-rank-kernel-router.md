# Prime Matrix Phi-LPF product-window signed fields source-rank kernel 证书

**状态：** `product_window_signed_fields_synced_to_source_rank_kernel_open`
**核验日期：** `2026-05-26`

本步把 product-window 的 `PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` 接入已有 signed atom trace-sync 与 source-rank convergence。无符号 edge label 只给输入域；signed fields 必须同属一个 pre-Cauchy trace key，否则进入命名 return。生产性出口 `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` 也不能作为未解释黑箱保留，必须携带 actual pre-Cauchy source-rank/no-collapse 包，并在共同 pointwise kernel 后落到 `AlphaRowAnchorPhaseEmissionFormulaLedger`、pre-Cauchy 算术恒等式与同表 rank/multiplicity。行/列命题仍未无条件闭合。

```text
product_window_signed_fields_imported=true
latest_trace_sync_imported=true
same_trace_key_and_named_return_matrix_synced=true
new_payload_source_atom_alignment_imported=true
strict_payload_independent_terminal_rejected=true
source_rank_package_atomized=true
post_antisplit_convergence_imported=true
edge_local_signed_atom_fields_proved=false
alpha_row_anchor_phase_emission_formula_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=AlphaRowAnchorPhaseEmissionFormulaLedger
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` | `PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward` | edge-local signed value、local factor、orientation、ExactUV 与 source row 必须同属一个 pre-Cauchy trace key。 |
| `PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward` | `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward` | 命名 return 矩阵关闭匿名缺口；生产性出口是 new payload，非生产性出口必须命名。 |
| `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` | `ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger` | new primitive payload 若不是环内改名，必须携带 actual pre-Cauchy source-rank/no-collapse 包。 |
| `ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger` | `ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger` | source-rank/no-collapse 包实际拆成 source entropy、complete key 与 fixed-key ExactUV local multiplicity。 |
| `ActualPreCauchySourceDomainAbsoluteEntropyLedger / CompletePrimitiveEmitterKeyPartitionLedger / FixedKeyExactUVLocalMultiplicityO1Ledger` | `PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate` | 内部 source-rank 路线在同 formal-unit 的 primitive alpha/delta pointwise kernel 上汇合。 |
| `PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate` | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | 共同核表的当前第一硬点是 alpha row anchor/phase emission，并行还需 pre-Cauchy 算术恒等式与同表 rank/multiplicity。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ProductWindowSignedFieldsImported | `true` | `false` | 上一层 product-window first-seed 路由已把直接 signed 硬点定位到 edge-local signed atom fields。 | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward |
| LatestTraceSyncImported | `true` | `true` | 已有 latest signed atom trace-sync 可直接作用在 product-window signed fields 入口。 | PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward |
| SameTraceKeyAndNamedReturnMatrixSynced | `true` | `true` | 跨 key、缺失、冲突、零因子、超预算或后验读取均进入命名 return，不再是匿名缺口。 | PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward |
| NewPayloadSourceAtomAlignmentImported | `true` | `false` | `NewPrimitive...` 已接到 source-atom alignment，不再能作为未解释的新黑箱。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| StrictPayloadIndependentTerminalRejected | `true` | `true` | 当前语料没有独立 new primitive 工件；若只是 signed-lane 环内改名则不能破环。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| SourceRankPackageAtomized | `true` | `false` | source-rank/no-collapse 包被拆成 source entropy、complete key 与 fixed-key local multiplicity。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| PostAntisplitConvergenceImported | `true` | `false` | new payload 与 terminal descent 的内部路线在 pointwise kernel 后收敛到 alpha row anchor。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| ProductWindowTupleSignedFormulaStillPaired | `true` | `false` | 本步只吸收 edge-local signed fields；tuple-level signed seed formula 仍是 product-window first-seed 配套硬点。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward |
| OrientationExactUVInternalStillPaired | `true` | `false` | orientation、ExactUV return 与 internal prime-adjoin transition 仍是同一 product-window first-seed 路线的配套义务。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| PointwiseSignedTableStillParallel | `true` | `false` | 逐点 Phi-LPF signed table 仍是直接旁路，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| ExactUVAndExternalInputStillIndependent | `true` | `false` | ExactUV/source entropy 与外部 trace 或平方根行尺度输入不能由本 trace-sync 自动推出。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND (ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients OR PointwiseSqrtPrimeInputCOne OR ExternalDIBFIKuznetsovDispersionTheoremMatch) |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只把 product-window signed fields 吸收到 source-rank/pointwise-kernel 前沿；未证明三命题无条件闭合。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |

## 3. 导入 slot 样本

| N | canonical edges | open signed slots | trace packets |
| --- | ---: | ---: | ---: |
| 10000 | 2600 | 15600 | 2600 |

## 4. 最新保留基

```text
((PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients OR PointwiseSqrtPrimeInputCOne OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger
```

并行仍需：

```text
IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients
PointwiseSqrtPrimeInputCOne
```

行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
| `docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.json` | `231294a3f0a9cfe6d8af17db958a40f71b1bbfdabcefe3dc5d7c2d1a7a15b72a` |
| `docs/monograph/prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.json` | `29bb5d64199756775ef9df2087df090bccbbde1df957400e77da202cd6d9fd53` |
| `docs/monograph/prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.json` | `9391ae3665799bbdc480248f17b0c7900cbafa505cab6ed806b643ea68aa7272` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-first-seed-to-edge-local-fields-router.json` | `6e9e2d46715893e2895674f36e9fa5f058cabbff2e2574a3edf3420960056305` |
| `docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json` | `3194b1509c245cd42f607bbab6b96a1e17420454c3ae40245fb859985d38a601` |
| `docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.json` | `3359bdbe51404005aec41ec0378840a4d114c235f20354ef488e2592e3f692c7` |
| `experiments/prime_matrix_phi_lpf_product_window_signed_fields_source_rank_kernel_router.py` | `3c7d1317163cf40c8aa298ba032af520beb26331e85954ac0e5f1cb553583e43` |
