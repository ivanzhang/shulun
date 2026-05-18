# Prime Matrix scale-ladder word-entropy 证书

**状态：** `persistent_scale_ladder_signature_reduced_to_word_entropy_open`

持久尺度阶梯签名被拆成 dyadic 指数词 sigma=(b_1,...,b_d)。未进入 product-width 出口时 sum b_i<=K_0=ceil(log_2 max(W_0,1))，因此尺度词个数至多 2^{K_0}，聚合压力必须落到单个尺度词。若该词下实际素坐标和相位稳定，则回到固定 MCRT/ColumnCRT/PDEC；否则剩余是固定尺度词内首个移动素坐标或相位漂移。

```text
persistent_scale_ladder_imported=true
dyadic_word_partition_closed=true
product_budget_closed=true
word_entropy_finite_cap_closed=true
aggregate_to_single_scale_word_closed=true
fixed_scale_ladder_columncrt_exit_closed=true
first_moving_scale_ladder_phase_localized=true
sparse_scale_ladder_sae_carried_forward=true
anonymous_persistent_scale_ladder_removed=true
first_moving_scale_ladder_phase_excluded=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

## 1. dyadic 尺度词

持久尺度阶梯由 dyadic 尺度组成：

```text
B_i=2^{b_i}, b_i>=1,
sigma=(b_1,...,b_d).
```

尺度词的合成尺度为：

```text
A_sigma=prod_i B_i=2^{sum_i b_i}.
```

## 2. product 预算与词熵

若 `A_sigma>W_0`，已经进入 product-width ColumnCRT/PDEC 或有限原子。因此非出口分支满足：

```text
sum_i b_i<=K_0=ceil(log_2 max(W_0,1)).
```

正整数有序组成给出有限尺度词数：

```text
N_ladder(K_0)=1+sum_{n=1}^{K_0}2^{n-1}<=2^{K_0}.
```

所以持久尺度阶梯不能作为匿名无限容量池。

## 3. 压力定位到单个尺度词

尺度词单元互不混同。若聚合压力为：

```text
E_total=sum_sigma E_sigma
```

且 `E_total>U`，则至少一个尺度词满足：

```text
E_sigma>U/N_ladder(K_0).
```

## 4. 固定词出口与首移动层

对承压尺度词 `sigma`，若实际素坐标和相位残基在无限子族中稳定，则它是固定 MCRT/ColumnCRT/PDEC 或有限原子。若不稳定，则存在首个移动素坐标或相位残基；新的直接硬点被定位到该首移动层。

## 5. 新硬点

```text
PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC
  -> PersistentScaleLadderSignatureImportedLedger
  AND ScaleLadderDyadicWordPartitionLedger
  AND ScaleLadderProductBudgetLedger
  AND ScaleLadderWordEntropyFiniteCapLedger
  AND AggregatePersistentPressureToSingleScaleWordLedger
  AND FixedScaleLadderMCRTColumnCRTExitLedger
  AND FirstMovingScaleLadderPhaseCoordinateLedger
  AND SparseScaleLadderSAECarriedForwardLedger
  AND NoAnonymousPersistentScaleLadderSignatureLedger
  AND FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC
```

剩余从持久尺度阶梯签名变成固定尺度词内首个移动素坐标/相位漂移，或 sparse scale-ladder SAE/ColumnCRT/PDEC。

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PersistentScaleLadderSignatureImported | `true` | `false` | 上一层把 scale-escape 剩余压成持久尺度阶梯签名或 sparse scale-ladder SAE/ColumnCRT/PDEC。 | PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC |
| ScaleLadderDyadicWordPartitionClosed | `true` | `true` | 每个持久尺度阶梯给出唯一 dyadic 指数词 sigma=(b_1,...,b_d)，其中 B_i=2^{b_i}, b_i>=1。 | ScaleLadderDyadicWordPartitionLedger |
| ScaleLadderProductBudgetClosed | `true` | `true` | 未进入 product-width 出口时 prod_i B_i<=W_0，等价于 sum_i b_i<=K_0=ceil(log_2 max(W_0,1))。 | ScaleLadderProductBudgetLedger |
| ScaleLadderWordEntropyFiniteCapClosed | `true` | `true` | 正整数有序组成给出尺度词个数 N_ladder(K_0)<=2^{K_0}；持久签名不能作为匿名无限容量池。 | ScaleLadderWordEntropyFiniteCapLedger |
| AggregatePersistentPressureToSingleScaleWordClosed | `true` | `true` | 有限尺度词集合上若聚合压力超界，则至少一个尺度词承载平均以上压力。 | AggregatePersistentPressureToSingleScaleWordLedger |
| FixedScaleLadderMCRTColumnCRTExitClosed | `true` | `true` | 若承压尺度词下的实际素坐标和相位残基在无限子族中稳定，则进入固定 MCRT/ColumnCRT/PDEC 或有限原子。 | FixedScaleLadderMCRTColumnCRTExitLedger |
| FirstMovingScaleLadderPhaseCoordinateClosed | `true` | `true` | 若承压尺度词不稳定，则存在首个移动素坐标或相位残基；新的硬点被定位到该首移动层。 | FirstMovingScaleLadderPhaseCoordinateLedger |
| SparseScaleLadderSAECarriedForward | `true` | `false` | 不能在同一尺度词上持久复现的事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。 | SparseScaleLadderSAECarriedForwardLedger |
| NoAnonymousPersistentScaleLadderSignature | `true` | `true` | 持久尺度阶梯签名被拆成有限尺度词、固定 MCRT 出口、首移动层或 sparse SAE；不再保留匿名签名池。 | NoAnonymousPersistentScaleLadderSignatureLedger |
| FirstMovingScaleLadderPhaseStillOpen | `false` | `false` | 仍未排斥固定尺度词内首个移动素坐标/相位漂移，也未证明 sparse SAE 全局可求和。 | FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥首移动尺度阶梯相位漂移，或证明其必回流为 ColumnCRT/PDEC/SAE 且全局可控。 | FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC |

## 7. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFTriplePressureImportedLedger AND IteratedLPFOrderedRoughResidualChainLedger AND LPFSupportProductReciprocityInvariantLedger AND LPFDepthRankBudgetLedger AND IteratedLPFCRTWordCellLedger AND IteratedLPFProductWidthColumnCRTExitLedger AND TerminalResidualFiniteAtomLedger AND IteratedLPFWellFoundedNoCycleLedger AND RankBudgetedMovingFamilyImportedLedger AND IteratedLPFWordSignaturePartitionLedger AND LPFWordEntropyFiniteCapLedger AND AggregatePressureToSingleLPFWordLedger AND FixedLPFWordColumnCRTExitLedger AND FirstMovingLPFCoordinateLedger AND MovingCoordinateSupportReciprocityLedger AND NoAnonymousRankBudgetedMovingFamilyLedger AND FirstMovingLPFCoordinatePressureImportedLedger AND StablePrefixProductSupportLedger AND FirstMovingCoordinateEffectiveWidthLedger AND LowMovingCoordinateFiniteAtomLedger AND FirstMovingCoordinateDyadicPartitionLedger AND MovingCoordinateActiveProductWidthExitLedger AND MovingCoordinateActiveCountBoundLedger AND SingleMovingCoordinatePressureLocalizationLedger AND FixedMovingCoordinateDegeneratesToColumnCRTLedger AND NoAnonymousFirstMovingCoordinatePoolLedger AND SingleMovingLPFCoordinateDriftImportedLedger AND SingleMovingCoordinateStablePrefixLedger AND SingleMovingCoordinateDyadicScaleLedger AND BoundedScaleDriftDegeneratesToFixedCoordinateLedger AND UnboundedCoordinateScaleEscapeLedger AND PostMovingCoordinateSupportDescentLedger AND SameScaleCoordinateCycleExcludedLedger AND SparseCoordinateDriftSAERegistrationLedger AND NoAnonymousSingleCoordinateDriftLedger AND ScaleEscapingSingleCoordinateDescentImportedLedger AND ScaleEscapeIntegerSupportClockLedger AND ScaleEscapeHalvingClockDescentLedger AND FiniteDepthScaleEscapePerFiberLedger AND TerminalWidthOneFiniteAtomLedger AND ScaleLadderProductWidthColumnCRTExitLedger AND PersistentScaleLadderSignatureRegistrationLedger AND SparseScaleLadderSAERegistrationLedger AND NoCyclicScaleEscapeDescentLedger AND NoAnonymousScaleEscapeDescentLedger AND PersistentScaleLadderSignatureImportedLedger AND ScaleLadderDyadicWordPartitionLedger AND ScaleLadderProductBudgetLedger AND ScaleLadderWordEntropyFiniteCapLedger AND AggregatePersistentPressureToSingleScaleWordLedger AND FixedScaleLadderMCRTColumnCRTExitLedger AND FirstMovingScaleLadderPhaseCoordinateLedger AND SparseScaleLadderSAECarriedForwardLedger AND NoAnonymousPersistentScaleLadderSignatureLedger AND FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 8. 诚实边界

- 本证书没有证明固定尺度词内首个移动素坐标/相位漂移不可能。
- 本证书没有证明 sparse scale-ladder SAE 全局可求和。
- 本证书只关闭匿名持久尺度阶梯签名池和尺度词聚合压力口径。
- `FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_scale_ladder_word_entropy_router.py` | `163e025fd1ee0dd471da6de736f26a6b3174e7a4d83e016e616a940b3786b6f0` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json` | `4dfe3b824d5d11788941ee4bd2a4dbe0ff7a7693e1ffd8b3fd2fa8ce50550705` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json` | `6b868246b6f4ef3560e71693da177d566f7a2310a6e539110838371b6db5e168` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json` | `3fa3246c30134bf6ecf97e839fc07704d12e009e50ec8fe0303b8575285d12bf` |
