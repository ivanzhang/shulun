# Prime Matrix late-support tail gap collar 证书

**状态：** `late_support_tail_gap_reduced_to_core_excess_or_deep_late_collar_open`

late-support tail gap 被压成精确 collar 公式。写 P=2m+1、D=2y-P、E=(D-1)/2。超过二重的 tail 只来自短 core 1<=r<=E；regular tail 在 r=y-1 还有一个端点缺口。因此 G_int=L(L-D)+min(L,y-1)-X_core。若这个 margin 大于 R_named，则正 gap 已成立；否则反例必须进入 deep-late short collar，或由 core-excess/named-return 质量承担。

```text
late_dense_imported=true
late_coordinate_closed=true
regular_tail_endpoint_defect_closed=true
late_core_excess_functional_closed=true
late_margin_exact_formula_closed=true
positive_late_margin_criterion_closed=true
deep_late_collar_excluded=false
core_excess_named_return_pdec_excluded=false
late_dense_tail_named_return_proved=false
row_column_unconditional_closed=false
```

## 1. late 坐标

在 late branch 写

```text
P=2m+1,  H=P-y,  y>m,
D=2y-P,  E=y-m-1=(D-1)/2.
```

当 `r>E` 且 `r<y-1` 时，`H+r>m` 且 `H+r<P-1`，因此

```text
ceil((P-1)/(H+r))=2.
```

端点 `r=y-1` 给出 `H+r=P-1`，所以

```text
ceil((P-1)/(H+r))=1.
```

## 2. core-excess functional

超过二重的整数 tail 只可能来自短 core：

```text
1<=r<=E.
```

定义

```text
X_core=sum_{1<=r<=E} min(L,r)(ceil((P-1)/(P-y+r))-2).
```

于是全整数 tail 精确分解为

```text
C_all = L(2y-L-1)+X_core-min(L,y-1).
```

因此

```text
G_int = L(P-1)-C_all
      = L(L-D)+min(L,y-1)-X_core.
```

若

```text
L(L-D)+min(L,y-1) > X_core+R_named,
```

则 `G=G_prime-R_named>0`。

## 3. 新硬点

```text
IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC
  -> LateSupportExcessCoordinateLedger
  AND RegularTailTwoUnitEndpointDefectLedger
  AND LateCoreExcessFunctionalLedger
  AND LateCollarMarginExactFormulaLedger
  AND DeepLateShortCollarOrCoreExcessNamedReturnPDEC
```

真正剩余是 deep-late short collar，或 `X_core/R_named` 吃掉 late margin。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LateDenseImported | `true` | `false` | 上一层把剩余压成 late-support dense-tail 或 named-return 质量。 | IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC |
| LateCoordinateClosed | `true` | `true` | 写 P=2m+1，H=P-y。late branch 为 y>m；令 D=2y-P，E=y-m-1=(D-1)/2。 | LateSupportExcessCoordinateLedger |
| RegularTailEndpointDefectClosed | `true` | `true` | 当 r>E 且 r<y-1 时，ceil((P-1)/(H+r))=2；端点 r=y-1 给 q=P-1，ceil=1。 | RegularTailTwoUnitEndpointDefectLedger |
| LateCoreExcessFunctionalClosed | `true` | `true` | 所有超过二重的 tail 质量只在 1<=r<=E；定义 X_core=sum min(L,r)(ceil((P-1)/(H+r))-2)。 | LateCoreExcessFunctionalLedger |
| LateMarginExactFormulaClosed | `true` | `true` | C_all=L(2y-L-1)+X_core-min(L,y-1)，故 G_int=L(L-D)+min(L,y-1)-X_core。 | LateCollarMarginExactFormulaLedger |
| PositiveLateMarginCriterionClosed | `true` | `true` | 若 L(L-D)+min(L,y-1)>X_core+R_named，则 G>0。 | LateCollarMarginExactFormulaLedger |
| DeepLateCollarOrCoreExcessStillOpen | `false` | `false` | 若不能正 gap，则必须是 margin 非正的 deep-late short collar，或 X_core/R_named 吃掉该 margin。 | DeepLateShortCollarOrCoreExcessNamedReturnPDEC |
| LateDenseReduced | `true` | `false` | IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC 被压成 late 坐标、端点缺口、core-excess functional、精确 margin 与 deep-collar/core-excess PDEC。 | LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateShortCollarOrCoreExcessNamedReturnPDEC |
| LateDenseProved | `false` | `false` | 本步没有排斥 deep-late short collar，也没有证明 X_core/R_named 不会吃掉 margin。 | DeepLateShortCollarOrCoreExcessNamedReturnPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥 deep-late collar、core-excess/named-return 质量，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateShortCollarOrCoreExcessNamedReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateShortCollarOrCoreExcessNamedReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateShortCollarOrCoreExcessNamedReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书没有排斥 deep-late short collar。
- 本证书没有证明 `X_core` 或 `R_named` 不会吃掉 late margin。
- `DeepLateShortCollarOrCoreExcessNamedReturnPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_late_collar_router.py` | `4068879ef4a1329c70029bb8378525386486d7c8b0822328afb929f5cdb9d1bb` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-integer-margin-router.json` | `5ccd52cc7ac9212bd7479c9ea5279049be6d279f854e11a9ab4c363645575cf7` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.json` | `f10a978ed4750e3994f4075cafaa86cd69d6b525916472195c25a479c13d5cbd` |
| `docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.json` | `b9d4683be96296b04e206cdc5d17afee2e936457da2c913f55a60ac820ddb557` |
