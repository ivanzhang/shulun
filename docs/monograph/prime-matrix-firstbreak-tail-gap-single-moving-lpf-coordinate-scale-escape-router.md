# Prime Matrix single-moving LPF coordinate scale-escape 证书

**状态：** `single_moving_lpf_coordinate_drift_reduced_to_scale_escape_open`

单个 moving LPF coordinate drift 被拆成有界 dyadic 尺度退化和无界尺度逃逸。若尺度有界，则 mu 只取有限素值，持久复现回到固定坐标 ColumnCRT/PDEC 或有限原子。若真漂移，则 B(mu) 必无界；加入 mu 后后继支撑至多 ceil(W_prefix/B)，从而同尺度循环不可能。剩余是尺度逃逸递降族或稀疏 drift/SAE。

```text
single_coordinate_drift_imported=true
stable_prefix_closed=true
dyadic_scale_closed=true
bounded_scale_degenerates_closed=true
unbounded_scale_escape_closed=true
post_coordinate_support_descent_closed=true
same_scale_cycle_excluded=true
sparse_drift_registered=true
anonymous_single_coordinate_drift_removed=true
scale_escaping_coordinate_excluded=false
sparse_drift_sae_summability_proved=false
row_column_unconditional_closed=false
```

## 1. 单坐标与 dyadic 尺度

上一层剩余为单个 `mu` 随 `P` 漂移。稳定前缀仍给出：

```text
W_prefix=floor(W/A_prefix).
```

对 `mu` 定义 dyadic 尺度：

```text
B(mu)=2^floor(log_2 mu),
B(mu)<=mu<=2B(mu).
```

## 2. 有界尺度退化

若 `B(mu)` 在无限子族中有界，则 `mu` 只可能取有限多个素值。由无限鸽巢，存在固定 `mu` 的无限子族。该分支不是 moving drift，而是已登记的固定坐标 ColumnCRT/PDEC 或有限原子。

因此真正的单坐标漂移必须满足：

```text
B(mu)->infty
```

沿一个 cofinal 子族成立。

## 3. 后继支撑递降

加入 `mu` 后，后继 residual 支撑宽度满足：

```text
W_after<=ceil(W_prefix/mu)<=ceil(W_prefix/B(mu)).
```

由于非有限活动层有 `B(mu)>=2`，若尚未进入有限原子，则 `W_after<W_prefix`。所以单坐标尺度逃逸不能在同一支撑尺度上循环。

## 4. 稀疏 drift 出口

若漂移事件不能形成持久同尺度压力，只能登记为 sparse drift/SAE 质量；本证书只登记该出口，不证明全局求和界。

## 5. 新硬点

```text
SingleMovingLPFCoordinateDriftOrPrefixColumnCRTPDEC
  -> SingleMovingLPFCoordinateDriftImportedLedger
  AND SingleMovingCoordinateStablePrefixLedger
  AND SingleMovingCoordinateDyadicScaleLedger
  AND BoundedScaleDriftDegeneratesToFixedCoordinateLedger
  AND UnboundedCoordinateScaleEscapeLedger
  AND PostMovingCoordinateSupportDescentLedger
  AND SameScaleCoordinateCycleExcludedLedger
  AND SparseCoordinateDriftSAERegistrationLedger
  AND NoAnonymousSingleCoordinateDriftLedger
  AND ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC
```

剩余从单坐标漂移变成尺度逃逸单坐标递降族，或 sparse drift/SAE/ColumnCRT/PDEC。

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SingleMovingCoordinateDriftImported | `true` | `false` | 上一层把首移动坐标池压成单个 mu 随 P 漂移，或 prefix ColumnCRT/PDEC。 | SingleMovingLPFCoordinateDriftOrPrefixColumnCRTPDEC |
| StablePrefixForSingleCoordinateClosed | `true` | `true` | 单坐标漂移仍保留稳定前缀 A_prefix 和有效宽度 W_prefix；漂移只发生在 mu 坐标。 | SingleMovingCoordinateStablePrefixLedger |
| DyadicScaleCoordinateClosed | `true` | `true` | 对 mu 定义 dyadic scale B(mu)=2^floor(log_2 mu)，且 B<=mu<=2B。 | SingleMovingCoordinateDyadicScaleLedger |
| BoundedScaleDegeneratesClosed | `true` | `true` | 若 B(mu) 在无限子族中有界，则 mu 只取有限个素值；无限复现必有固定 mu 子族，回到固定坐标 ColumnCRT/PDEC 或有限原子。 | BoundedScaleDriftDegeneratesToFixedCoordinateLedger |
| UnboundedScaleEscapeClosed | `true` | `true` | 真正单坐标漂移必须沿 cofinal 子族满足 B(mu)->infty；否则已由有界尺度退化吸收。 | UnboundedCoordinateScaleEscapeLedger |
| PostMovingCoordinateSupportDescentClosed | `true` | `true` | 加入 mu 后后继 residual 支撑宽度至多 ceil(W_prefix/mu)<=ceil(W_prefix/B)，因此在 B>=2 时严格小于 W_prefix。 | PostMovingCoordinateSupportDescentLedger |
| SameScaleCoordinateCycleExcluded | `true` | `true` | 每个真实尺度逃逸都严格降低后继支撑，且有界尺度已回到固定坐标；同尺度漂移循环被排除。 | SameScaleCoordinateCycleExcludedLedger |
| SparseCoordinateDriftRegistered | `true` | `false` | 若漂移事件不形成持久同尺度压力，只能登记为稀疏 drift/SAE 质量；本步登记出口但不证明全局求和界。 | SparseCoordinateDriftSAERegistrationLedger |
| NoAnonymousSingleCoordinateDrift | `true` | `true` | 单坐标漂移被拆成固定坐标退化、尺度逃逸支撑递降、稀疏 SAE 或 ColumnCRT/PDEC；不再保留匿名 drift。 | NoAnonymousSingleCoordinateDriftLedger |
| ScaleEscapingCoordinateStillOpen | `false` | `false` | 仍未排除尺度逃逸单坐标递降族，也未证明稀疏 drift SAE 全局可求和。 | ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥尺度逃逸单坐标递降族，或证明其必回流为 ColumnCRT/PDEC/SAE。 | ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC |

## 7. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFTriplePressureImportedLedger AND IteratedLPFOrderedRoughResidualChainLedger AND LPFSupportProductReciprocityInvariantLedger AND LPFDepthRankBudgetLedger AND IteratedLPFCRTWordCellLedger AND IteratedLPFProductWidthColumnCRTExitLedger AND TerminalResidualFiniteAtomLedger AND IteratedLPFWellFoundedNoCycleLedger AND RankBudgetedMovingFamilyImportedLedger AND IteratedLPFWordSignaturePartitionLedger AND LPFWordEntropyFiniteCapLedger AND AggregatePressureToSingleLPFWordLedger AND FixedLPFWordColumnCRTExitLedger AND FirstMovingLPFCoordinateLedger AND MovingCoordinateSupportReciprocityLedger AND NoAnonymousRankBudgetedMovingFamilyLedger AND FirstMovingLPFCoordinatePressureImportedLedger AND StablePrefixProductSupportLedger AND FirstMovingCoordinateEffectiveWidthLedger AND LowMovingCoordinateFiniteAtomLedger AND FirstMovingCoordinateDyadicPartitionLedger AND MovingCoordinateActiveProductWidthExitLedger AND MovingCoordinateActiveCountBoundLedger AND SingleMovingCoordinatePressureLocalizationLedger AND FixedMovingCoordinateDegeneratesToColumnCRTLedger AND NoAnonymousFirstMovingCoordinatePoolLedger AND SingleMovingLPFCoordinateDriftImportedLedger AND SingleMovingCoordinateStablePrefixLedger AND SingleMovingCoordinateDyadicScaleLedger AND BoundedScaleDriftDegeneratesToFixedCoordinateLedger AND UnboundedCoordinateScaleEscapeLedger AND PostMovingCoordinateSupportDescentLedger AND SameScaleCoordinateCycleExcludedLedger AND SparseCoordinateDriftSAERegistrationLedger AND NoAnonymousSingleCoordinateDriftLedger AND ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 8. 诚实边界

- 本证书没有证明尺度逃逸单坐标递降族不可能。
- 本证书没有证明 sparse drift/SAE 全局可求和。
- 本证书只排除有界尺度匿名漂移和同尺度循环。
- `ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_single_moving_lpf_coordinate_scale_escape_router.py` | `48f18982f3a0127878089488987bbcf42a7aac1453871b9e58c57b1b384c8465` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json` | `3fa3246c30134bf6ecf97e839fc07704d12e009e50ec8fe0303b8575285d12bf` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json` | `c2a85de6fe4ea7153190111a2c1656adda5ea7631edf71ff38127f668a3ee5bf` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json` | `54719636b257d5414a51208df863483c167ac34dc12a0f0a1c9f73b9b1b5b515` |
