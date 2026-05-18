# Prime Matrix deep-late collar quotient-layer 证书

**状态：** `deep_late_reduced_to_self_mirror_collar_or_core_quotient_layer_consumption_open`

deep-late 剩余被拆成几何 collar 与 core quotient 层。若 L<=D，则 x0=y-L>=P-y，零块完全落在自镜像 collar [P-y,y-1]；若 L>D，则只有 X_core 或 R_named 消耗掉 M=L(L-D)+min(L,y-1) 才能阻止正 gap。并且 X_core 按 h=H+r 的 quotient 层 k(h)=ceil((P-1)/h)-2 精确分解。

```text
deep_collar_imported=true
mirror_collar_equivalence_closed=true
cross_collar_positive_margin_closed=true
core_layer_decomposition_closed=true
core_or_named_consumption_closed=true
self_mirror_collar_excluded=false
core_layer_concentration_excluded=false
deep_late_closed=false
row_column_unconditional_closed=false
```

## 1. deep-late collar 等价式

令

```text
x0=y-L,  H=P-y,  D=2y-P.
```

则

```text
L<=D
<=> y-L >= y-D
<=> x0 >= P-y = H.
```

所以 deep-late short collar 等价于

```text
B=[x0,y-1] subset [H,y-1].
```

这把几何剩余从“late 支撑”缩成自镜像 collar 内部相位问题。

## 2. 跨出 collar 时的正 margin 门

若 `L>D`，则跨出 collar。记

```text
M = L(L-D)+min(L,y-1).
```

上一层精确式给出

```text
G_int = M-X_core.
```

因此

```text
X_core+R_named < M  =>  G>0.
```

若反例仍存在，则必须有

```text
X_core+R_named >= M.
```

## 3. core-excess quotient 层

令

```text
h=H+r,  H+1<=h<=m,
k(h)=ceil((P-1)/h)-2.
```

定义 quotient 层

```text
I_k={h: ceil((P-1)/h)=k+2}.
```

则

```text
X_core=sum_{k>=1} k sum_{h in I_k} min(L,h-H).
```

## 4. 新硬点

```text
DeepLateShortCollarOrCoreExcessNamedReturnPDEC
  -> DeepLateCollarMirrorContainmentLedger
  AND CrossCollarPositiveMarginCriterionLedger
  AND CoreExcessQuotientLayerDecompositionLedger
  AND CoreExcessLayerConcentrationOrNamedReturnPDEC
  AND SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC
```

真正剩余是自镜像 collar 内部相位，或 quotient core 层/命名 return 对 margin 的显式消耗。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DeepCollarImported | `true` | `false` | 上一层把 late-support 剩余压成 deep-late collar，或 X_core/R_named 吃掉 margin。 | DeepLateShortCollarOrCoreExcessNamedReturnPDEC |
| MirrorCollarEquivalenceClosed | `true` | `true` | 令 x0=y-L、H=P-y、D=2y-P。L<=D 当且仅当 x0>=H，即 B=[x0,y-1] 完全落在自镜像 collar [H,y-1]。 | DeepLateCollarMirrorContainmentLedger |
| CrossCollarPositiveMarginClosed | `true` | `true` | 若 L>D 且 X_core+R_named < L(L-D)+min(L,y-1)，则正 gap 已成立。 | CrossCollarPositiveMarginCriterionLedger |
| CoreLayerDecompositionClosed | `true` | `true` | 令 h=H+r，k(h)=ceil((P-1)/h)-2；X_core=sum_{h=H+1}^m min(L,h-H)k(h)，并按 k 的 quotient 层精确分解。 | CoreExcessQuotientLayerDecompositionLedger |
| CoreOrNamedConsumptionClosed | `true` | `false` | 若 L>D 但正 gap 失败，则 X_core+R_named 必至少吃掉 M=L(L-D)+min(L,y-1) 的全部 margin。 | CoreExcessLayerConcentrationOrNamedReturnPDEC |
| DeepCollarOrCoreLayerStillOpen | `false` | `false` | 剩余不是一般 late tail，而是自镜像 collar 内部相位问题，或 quotient core 层/命名 return 的显式 margin 消耗。 | SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC |
| DeepCollarReduced | `true` | `false` | DeepLateShortCollarOrCoreExcessNamedReturnPDEC 被压成 collar mirror containment、cross-collar margin、quotient-layer 分解和 core/named 消耗。 | DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC |
| DeepCollarProved | `false` | `false` | 本步没有排斥自镜像 collar，也没有排斥 quotient core 层集中或 R_named 吃掉 margin。 | SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥自镜像 collar 或 core-layer/named-return 质量，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 6. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 诚实边界

- 本证书没有排斥自镜像 collar 内部相位问题。
- 本证书没有排斥 quotient core 层集中或 `R_named` 吃掉 margin。
- `SelfMirrorDeepLateCollarOrCoreLayerExcessNamedReturnPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_deep_collar_layer_router.py` | `7d264aae903da51cfe62006617b50bab33fb4362292b70d0d667c355dbc34ab1` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.json` | `496714585ada926f0875418c4d1b5ce1e3d3fa6a5d5074537069120a48b594e3` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.json` | `5ccd52cc7ac9212bd7479c9ea5279049be6d279f854e11a9ab4c363645575cf7` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.json` | `f10a978ed4750e3994f4075cafaa86cd69d6b525916472195c25a479c13d5cbd` |
