# Prime Matrix tail gap 全整数 margin 分裂证书

**状态：** `normalized_tail_gap_reduced_to_integer_margin_or_late_support_dense_tail_open`

归一化 tail gap 被继续压成全整数 margin。由于 prime tail 是 integer tail 的子和，只要 G_int=L(P-1)-C_all 超过命名 return 质量 R_named，就得到正 gap。特别地，当首破裂 y 仍在前半支撑 y<=floor(P/2) 时，所有 tail carrier 都满足 ceil((P-1)/(P-y+r))<=2，从而 G_int>=L(P-2y+L)>0；因此 pure tail 本身不能吃满零块义务。剩余硬点集中到 late-support dense-tail 或 R_named 过大。

```text
normalized_tail_gap_imported=true
one_dimensional_tail_imported=true
integer_margin_functional_closed=true
prime_tail_dominated_by_integer_tail_closed=true
positive_branch_criterion_closed=true
early_half_support_tail_cannot_saturate_closed=true
integer_margin_positive_globally_proved=false
late_support_dense_tail_named_return_pdec_excluded=false
normalized_positive_gap_proved=false
row_column_unconditional_closed=false
```

## 1. 全整数 margin

由上一层

```text
C_tail = sum_{prime q=H+r<P} min(L,r) ceil((P-1)/(H+r)),
H=P-y.
```

去掉素数限制，定义

```text
C_all = sum_{1<=r<y} min(L,r) ceil((P-1)/(P-y+r)),
G_int = L(P-1)-C_all.
```

于是

```text
C_tail <= C_all,
G_prime=L(P-1)-C_tail >= G_int.
```

因此若

```text
G_int > R_named,
```

则 `G=G_prime-R_named>0`。

## 2. 前半支撑不能由 pure tail 饱和

若 `P` 为奇素数且

```text
y <= floor(P/2),
```

则对所有 `1<=r<y`，有

```text
P-y+r > (P-1)/2,
ceil((P-1)/(P-y+r)) <= 2.
```

又 `1<=L<=y`，所以

```text
C_all <= 2 sum_{1<=r<y} min(L,r)
      = L(2y-L-1),
G_int >= L(P-2y+L) > 0.
```

这说明在前半支撑中，tail envelope 即使按全整数上界也不能吃满 `L(P-1)`。

## 3. 新硬点

```text
NormalizedTailGapPositiveOrDenseTailReturnPDEC
  -> NormalizedIntegerTailMarginFunctionalLedger
  AND PrimeTailDominatedByIntegerTailEnvelopeLedger
  AND EarlyHalfSupportTailCannotSaturateLemma
  AND IntegerMarginPositiveBranchCriterionLedger
  AND IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC
```

真正剩余是 late-support dense-tail，或 `R_named` 吃掉整数 margin 的命名 return 质量。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| NormalizedTailGapImported | `true` | `false` | 上一层把正 gap 硬点压成 q=H+r 的一维 prime-tail functional。 | NormalizedTailGapPositiveOrDenseTailReturnPDEC |
| OneDimensionalTailImported | `true` | `true` | 已得到 C_tail=sum_{prime q=H+r<P} min(L,r)ceil((P-1)/(H+r))。 | ExactPrimeTailEnvelopeOneDimensionalLedger |
| IntegerMarginFunctionalClosed | `true` | `true` | 定义 G_int=L(P-1)-C_all，其中 C_all=sum_{1<=r<y}min(L,r)ceil((P-1)/(P-y+r))。 | NormalizedIntegerTailMarginFunctionalLedger |
| PrimeTailDominatedByIntegerTailClosed | `true` | `true` | 因 prime tail 是 integer tail 的子和，C_tail<=C_all，故 G'=L(P-1)-C_tail>=G_int。 | PrimeTailDominatedByIntegerTailEnvelopeLedger |
| PositiveBranchCriterionClosed | `true` | `true` | 若 G_int>R_named，则 G=L(P-1)-C_tail-R_named>0。 | IntegerMarginPositiveBranchCriterionLedger |
| EarlyHalfPureTailCannotSaturateClosed | `true` | `true` | 若 P 为奇素数且 y<=floor(P/2)，则 ceil((P-1)/(P-y+r))<=2，故 G_int>=L(P-2y+L)>0。 | EarlyHalfSupportTailCannotSaturateLemma |
| LateSupportOrNamedReturnStillOpen | `false` | `false` | 仍未排斥 y>floor(P/2) 的 late-support dense-tail，或 R_named 吃掉整数 margin 的命名 return 质量。 | IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC |
| NormalizedTailGapReduced | `true` | `false` | NormalizedTailGapPositiveOrDenseTailReturnPDEC 被压成整数 margin、prime/integer 支配、前半支撑 tail 不饱和，以及 late-support/named-return PDEC。 | NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC |
| NormalizedPositiveGapProved | `false` | `false` | 本步没有证明全局 G>0；只关闭前半支撑的 pure-tail 饱和解释，并把失败口径集中到 late support 或 R_named。 | IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥 late-support dense-tail/named-return 质量，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书没有证明全局 `G>0`。
- 本证书只证明 prime tail 被 integer tail 支配，并关闭前半支撑 pure-tail 饱和解释。
- `IntegerTailMarginPositiveOrLateSupportDenseTailNamedReturnPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_integer_margin_router.py` | `74b720c70739b76e92503b1ae0cad05d234f29cdfe63e5f26288d2d4d1be2fcc` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-normalization-router.json` | `f10a978ed4750e3994f4075cafaa86cd69d6b525916472195c25a479c13d5cbd` |
| `docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.json` | `b9d4683be96296b04e206cdc5d17afee2e936457da2c913f55a60ac820ddb557` |
| `docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.json` | `a3dd4c8f63dec374475a41dfa3b6439bf2c62823e30576ef870b05e713f752f0` |
