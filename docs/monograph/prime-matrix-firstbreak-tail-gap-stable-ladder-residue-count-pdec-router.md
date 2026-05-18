# Prime Matrix stable-ladder residue-count PDEC 证书

**状态：** `primitive_fiber_pdec_reduced_to_residue_count_imbalance_open`

primitive pivot-fiber PDEC 可由有限 Fourier 反演写成余数类计数偏差。在固定补坐标纤维 S_h 中令 M_r 统计 n mod q_j=r 的点数，D_r=M_r-|S_h|/q_j。非平凡角色和 A_h=sum_r M_r chi_j(r)=sum_r D_r chi_j(r)。若 |A_h|>=q_j*E/(N-1)，则必存在余数 r 使 |M_r-|S_h|/q_j|>=E/(N-1)。

```text
primitive_fiber_pdec_imported=true
residue_count_vector_closed=true
zero_mean_deviation_closed=true
character_to_residue_deviation_closed=true
residue_imbalance_localization_closed=true
residue_imbalance_threshold_closed=true
anonymous_primitive_character_exit_removed=true
sparse_scale_ladder_sae_carried_forward=true
residue_count_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

## 1. 固定纤维内的余数计数

沿用上一层的 pivot 坐标 `j` 与补坐标纤维 `S_h`。令：

```text
L=|S_h|,
M_r=#{n in S_h: n mod q_j=r},  r in Z/q_jZ.
```

定义均值扣除后的偏差向量：

```text
D_r=M_r-L/q_j.
```

于是：

```text
sum_r D_r=0.
```

## 2. 角色和反演为计数偏差

上一层的 primitive fiber 角色和为：

```text
A_h=sum_{n in S_h} chi_j(n mod q_j)=sum_r M_r chi_j(r).
```

由于 `chi_j` 非平凡，`sum_r chi_j(r)=0`，因此：

```text
A_h=sum_r D_r chi_j(r).
```

## 3. 原子余数类偏差

由三角不等式：

```text
|A_h|<=sum_r |D_r|<=q_j max_r |D_r|.
```

上一层给出阈值：

```text
|A_h|>=q_j*E_a(S)/(N-1).
```

故存在某个余数 `r` 使：

```text
|M_r-L/q_j|>=E_a(S)/(N-1).
```

这把 primitive fiber PDEC cap 改写为固定补坐标纤维中的单余数类计数偏差 cap。

## 4. 新硬点

```text
SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap
  -> StableActualLadderPrimitiveFiberPDECImportedLedger
  AND StableLadderPivotFiberResidueCountVectorLedger
  AND StableLadderPivotFiberZeroMeanDeviationLedger
  AND StableLadderPivotFiberCharacterToResidueDeviationLedger
  AND StableLadderPivotFiberResidueImbalanceLocalizationLedger
  AND StableLadderPivotFiberResidueImbalanceThresholdLedger
  AND NoAnonymousPrimitiveFiberCharacterPDECExitLedger
  AND SparseScaleLadderSAECarriedForwardAfterResidueCountLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap
```

剩余从 primitive fiber 角色相关变成 residue-count PDEC cap，或 sparse scale-ladder SAE 全局求和问题。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| StableActualLadderPrimitiveFiberPDECImported | `true` | `false` | 上一层把稳定 ladder 的全局 Fourier cap 局部化为单坐标 pivot 纤维角色相关。 | SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap |
| StableLadderPivotFiberResidueCountVectorClosed | `true` | `true` | 在固定补坐标纤维 S_h 内定义 M_r=#{n in S_h:n=r mod q_j} 与 L=\|S_h\|。 | StableLadderPivotFiberResidueCountVectorLedger |
| StableLadderPivotFiberZeroMeanDeviationClosed | `true` | `true` | 定义 D_r=M_r-L/q_j，则 sum_r D_r=0。 | StableLadderPivotFiberZeroMeanDeviationLedger |
| StableLadderPivotFiberCharacterToResidueDeviationClosed | `true` | `true` | 非平凡角色满足 sum_r chi_j(r)=0，因此 A_h=sum_r D_r chi_j(r)。 | StableLadderPivotFiberCharacterToResidueDeviationLedger |
| StableLadderPivotFiberResidueImbalanceLocalizationClosed | `true` | `true` | 由 \|A_h\|<=sum_r \|D_r\|<=q_j max_r \|D_r\|，角色异常强制某个余数类计数偏差异常。 | StableLadderPivotFiberResidueImbalanceLocalizationLedger |
| StableLadderPivotFiberResidueImbalanceThresholdClosed | `true` | `true` | 若 \|A_h\|>=q_j*E/(N-1)，则存在 r 使 \|M_r-L/q_j\|>=E/(N-1)。 | StableLadderPivotFiberResidueImbalanceThresholdLedger |
| NoAnonymousPrimitiveFiberCharacterPDECExit | `true` | `true` | primitive fiber 角色相关出口被改写成固定余数类的计数偏差出口。 | NoAnonymousPrimitiveFiberCharacterPDECExitLedger |
| SparseScaleLadderSAECarriedForwardAfterResidueCount | `true` | `false` | 非持久实际 ladder 事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。 | SparseScaleLadderSAECarriedForwardAfterResidueCountLedger |
| StableActualLadderResidueCountPDECCapStillOpen | `false` | `false` | 仍未证明所有固定纤维余数类计数偏差都低于阈值，也未证明 sparse scale-ladder SAE 全局可求和。 | SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需给出 residue-count PDEC cap，或证明 sparse scale-ladder SAE 全局可控。 | SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap |

## 6. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFTriplePressureImportedLedger AND IteratedLPFOrderedRoughResidualChainLedger AND LPFSupportProductReciprocityInvariantLedger AND LPFDepthRankBudgetLedger AND IteratedLPFCRTWordCellLedger AND IteratedLPFProductWidthColumnCRTExitLedger AND TerminalResidualFiniteAtomLedger AND IteratedLPFWellFoundedNoCycleLedger AND RankBudgetedMovingFamilyImportedLedger AND IteratedLPFWordSignaturePartitionLedger AND LPFWordEntropyFiniteCapLedger AND AggregatePressureToSingleLPFWordLedger AND FixedLPFWordColumnCRTExitLedger AND FirstMovingLPFCoordinateLedger AND MovingCoordinateSupportReciprocityLedger AND NoAnonymousRankBudgetedMovingFamilyLedger AND FirstMovingLPFCoordinatePressureImportedLedger AND StablePrefixProductSupportLedger AND FirstMovingCoordinateEffectiveWidthLedger AND LowMovingCoordinateFiniteAtomLedger AND FirstMovingCoordinateDyadicPartitionLedger AND MovingCoordinateActiveProductWidthExitLedger AND MovingCoordinateActiveCountBoundLedger AND SingleMovingCoordinatePressureLocalizationLedger AND FixedMovingCoordinateDegeneratesToColumnCRTLedger AND NoAnonymousFirstMovingCoordinatePoolLedger AND SingleMovingLPFCoordinateDriftImportedLedger AND SingleMovingCoordinateStablePrefixLedger AND SingleMovingCoordinateDyadicScaleLedger AND BoundedScaleDriftDegeneratesToFixedCoordinateLedger AND UnboundedCoordinateScaleEscapeLedger AND PostMovingCoordinateSupportDescentLedger AND SameScaleCoordinateCycleExcludedLedger AND SparseCoordinateDriftSAERegistrationLedger AND NoAnonymousSingleCoordinateDriftLedger AND ScaleEscapingSingleCoordinateDescentImportedLedger AND ScaleEscapeIntegerSupportClockLedger AND ScaleEscapeHalvingClockDescentLedger AND FiniteDepthScaleEscapePerFiberLedger AND TerminalWidthOneFiniteAtomLedger AND ScaleLadderProductWidthColumnCRTExitLedger AND PersistentScaleLadderSignatureRegistrationLedger AND SparseScaleLadderSAERegistrationLedger AND NoCyclicScaleEscapeDescentLedger AND NoAnonymousScaleEscapeDescentLedger AND PersistentScaleLadderSignatureImportedLedger AND ScaleLadderDyadicWordPartitionLedger AND ScaleLadderProductBudgetLedger AND ScaleLadderWordEntropyFiniteCapLedger AND AggregatePersistentPressureToSingleScaleWordLedger AND FixedScaleLadderMCRTColumnCRTExitLedger AND FirstMovingScaleLadderPhaseCoordinateLedger AND SparseScaleLadderSAECarriedForwardLedger AND NoAnonymousPersistentScaleLadderSignatureLedger AND FirstMovingScaleLadderPhaseDriftImportedLedger AND FixedScaleWordSlotLedger AND FinitePrimeChoicesPerScaleSlotLedger AND FiniteResidueChoicesPerPrimeSlotLedger AND FiniteActualScaleLadderAtomSetLedger AND InfinitePigeonholeStableActualScaleLadderLedger AND NoPersistentFirstMovingScaleLadderPhaseDriftLedger AND StableActualScaleLadderMCRTColumnCRTExitLedger AND SparseScaleLadderSAECarriedForwardAfterFiniteSlotLockLedger AND NoAnonymousFirstMovingScaleLadderPhaseDriftLedger AND StableActualLadderOrSparseSAEImportedLedger AND StableActualLadderFiniteGroupLedger AND StableActualLadderZeroMeanCellFunctionLedger AND StableActualLadderExactExcessIdentityLedger AND StableActualLadderFourierPDECBridgeLedger AND StableActualLadderNontrivialCharacterLowerBoundLedger AND NoAnonymousStableActualLadderColumnCRTExitLedger AND SparseScaleLadderSAECarriedForwardAfterFourierBridgeLedger AND StableActualLadderFourierCapImportedLedger AND StableLadderCharacterFactorizationLedger AND StableLadderNontrivialPivotCoordinateLedger AND StableLadderComplementFiberPartitionLedger AND StableLadderGlobalCharacterToPivotFiberLocalizationLedger AND StableLadderPrimitivePivotCharacterCorrelationLedger AND NoAnonymousStableLadderFourierCapLedger AND SparseScaleLadderSAECarriedForwardAfterPivotFiberLedger AND StableActualLadderPrimitiveFiberPDECImportedLedger AND StableLadderPivotFiberResidueCountVectorLedger AND StableLadderPivotFiberZeroMeanDeviationLedger AND StableLadderPivotFiberCharacterToResidueDeviationLedger AND StableLadderPivotFiberResidueImbalanceLocalizationLedger AND StableLadderPivotFiberResidueImbalanceThresholdLedger AND NoAnonymousPrimitiveFiberCharacterPDECExitLedger AND SparseScaleLadderSAECarriedForwardAfterResidueCountLedger AND SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 诚实边界

- 本证书没有证明 residue-count PDEC cap。
- 本证书没有证明 sparse scale-ladder SAE 全局可求和。
- 本证书只把 primitive fiber 角色相关局部化为单余数类计数偏差输入。
- `SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_residue_count_pdec_router.py` | `f9a9fd652e0482d2b0838e988c747a66fd55f1d55bfd6ac4e4ec8e61e5582f32` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.json` | `838ab07539e07e326446286f27d85f83e898d99f3fa1fbe9c2148d586c14cddb` |
