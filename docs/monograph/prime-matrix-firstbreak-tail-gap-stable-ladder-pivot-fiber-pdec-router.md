# Prime Matrix stable-ladder pivot-fiber PDEC 证书

**状态：** `stable_ladder_fourier_cap_reduced_to_pivot_fiber_pdec_open`

稳定实际 ladder 的非平凡 Fourier cap 可按角色分解和补坐标纤维分割进一步局部化。对任意非平凡角色 chi=prod_i chi_i，选取非平凡 pivot 坐标 j；按其余坐标 h 分割支撑。若全局角色和 |S_chi| 至少为 Lambda，则三角不等式强制存在某个纤维 h，使单坐标角色和至少为 Lambda/|G_{-j}|。代入上一层 Lambda=N*E/(N-1) 与 |G_{-j}|=N/q_j，得到原子阈值 q_j*E/(N-1)。

```text
stable_ladder_fourier_cap_imported=true
character_factorization_closed=true
nontrivial_pivot_coordinate_closed=true
complement_fiber_partition_closed=true
global_character_to_pivot_fiber_localization_closed=true
primitive_pivot_character_correlation_closed=true
anonymous_fourier_cap_removed=true
sparse_scale_ladder_sae_carried_forward=true
primitive_fiber_pdec_cap_proved=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

## 1. 角色分解与 pivot 坐标

稳定 ladder 的有限群为：

```text
G=prod_i Z/q_iZ,  N=|G|=prod_i q_i.
```

任一角色都分解为：

```text
chi(g)=prod_i chi_i(g_i).
```

若 `chi` 非平凡，则存在 `j` 使 `chi_j` 非平凡；固定这样的 `j` 作为 pivot 坐标。

## 2. 补坐标纤维分割

令：

```text
G_{-j}=prod_{i!=j} Z/q_iZ,
|G_{-j}|=N/q_j,
S_h={n in S: tau_{-j}(n)=h}.
```

对每个纤维定义单坐标角色和：

```text
A_h=sum_{n in S_h} chi_j(n mod q_j).
```

则全局角色和精确分解为：

```text
S_chi=sum_h chi_{-j}(h) * A_h.
```

## 3. 全局异常到单坐标异常

由三角不等式：

```text
|S_chi|<=sum_h |A_h|<=|G_{-j}| max_h |A_h|.
```

因此若 `|S_chi|>=Lambda`，则存在补坐标纤维 `h` 使：

```text
|A_h|>=Lambda/|G_{-j}|.
```

代入上一层 Fourier 桥给出的 `Lambda=N*E_a(S)/(N-1)`，得到：

```text
|A_h|>=q_j*E_a(S)/(N-1).
```

这把 stable ladder Fourier cap 改写成一个单素数模数 `q_j` 上、固定补坐标纤维中的原子相位相关 cap。

## 4. 新硬点

```text
SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap
  -> StableActualLadderFourierCapImportedLedger
  AND StableLadderCharacterFactorizationLedger
  AND StableLadderNontrivialPivotCoordinateLedger
  AND StableLadderComplementFiberPartitionLedger
  AND StableLadderGlobalCharacterToPivotFiberLocalizationLedger
  AND StableLadderPrimitivePivotCharacterCorrelationLedger
  AND NoAnonymousStableLadderFourierCapLedger
  AND SparseScaleLadderSAECarriedForwardAfterPivotFiberLedger
  AND SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap
```

剩余从全局 Fourier cap 变成 primitive pivot-fiber PDEC cap，或 sparse scale-ladder SAE 全局求和问题。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| StableActualLadderFourierCapImported | `true` | `false` | 上一层把稳定实际 ladder 的匿名 ColumnCRT 出口改写为非平凡 Fourier/PDEC cap。 | SparseScaleLadderSAESummabilityOrStableActualLadderFourierPDECCap |
| StableLadderCharacterFactorizationClosed | `true` | `true` | 有限乘积群 G=prod_i Z/q_iZ 的每个角色可分解为 chi(g)=prod_i chi_i(g_i)。 | StableLadderCharacterFactorizationLedger |
| StableLadderNontrivialPivotCoordinateClosed | `true` | `true` | 若 chi 非平凡，则至少一个坐标 chi_j 非平凡；选择这样的 pivot 坐标 j。 | StableLadderNontrivialPivotCoordinateLedger |
| StableLadderComplementFiberPartitionClosed | `true` | `true` | 按其余坐标 h=tau_{-j}(n) 分割支撑 S，得到互不相交纤维 S_h。 | StableLadderComplementFiberPartitionLedger |
| StableLadderGlobalCharacterToPivotFiberLocalizationClosed | `true` | `true` | 若 \|S_chi\|>=Lambda，则存在补坐标纤维 h 使 \|sum_{n in S_h}chi_j(n mod q_j)\|>=Lambda/\|G_{-j}\|。 | StableLadderGlobalCharacterToPivotFiberLocalizationLedger |
| StableLadderPrimitivePivotCharacterCorrelationClosed | `true` | `true` | 代入 Lambda=N*E/(N-1) 与 \|G_{-j}\|=N/q_j，得到单坐标阈值 q_j*E/(N-1)。 | StableLadderPrimitivePivotCharacterCorrelationLedger |
| NoAnonymousStableLadderFourierCap | `true` | `true` | 稳定 ladder 的全局 Fourier cap 不再匿名；它必落到某个 pivot 坐标和补坐标纤维的原子相位相关。 | NoAnonymousStableLadderFourierCapLedger |
| SparseScaleLadderSAECarriedForwardAfterPivotFiber | `true` | `false` | 非持久实际 ladder 事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。 | SparseScaleLadderSAECarriedForwardAfterPivotFiberLedger |
| StableActualLadderPrimitiveFiberPDECCapStillOpen | `false` | `false` | 仍未证明所有 pivot-fiber 原子相位相关都低于阈值，也未证明 sparse scale-ladder SAE 全局可求和。 | SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需给出 primitive fiber PDEC cap，或证明 sparse scale-ladder SAE 全局可控。 | SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap |

## 6. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFTriplePressureImportedLedger AND IteratedLPFOrderedRoughResidualChainLedger AND LPFSupportProductReciprocityInvariantLedger AND LPFDepthRankBudgetLedger AND IteratedLPFCRTWordCellLedger AND IteratedLPFProductWidthColumnCRTExitLedger AND TerminalResidualFiniteAtomLedger AND IteratedLPFWellFoundedNoCycleLedger AND RankBudgetedMovingFamilyImportedLedger AND IteratedLPFWordSignaturePartitionLedger AND LPFWordEntropyFiniteCapLedger AND AggregatePressureToSingleLPFWordLedger AND FixedLPFWordColumnCRTExitLedger AND FirstMovingLPFCoordinateLedger AND MovingCoordinateSupportReciprocityLedger AND NoAnonymousRankBudgetedMovingFamilyLedger AND FirstMovingLPFCoordinatePressureImportedLedger AND StablePrefixProductSupportLedger AND FirstMovingCoordinateEffectiveWidthLedger AND LowMovingCoordinateFiniteAtomLedger AND FirstMovingCoordinateDyadicPartitionLedger AND MovingCoordinateActiveProductWidthExitLedger AND MovingCoordinateActiveCountBoundLedger AND SingleMovingCoordinatePressureLocalizationLedger AND FixedMovingCoordinateDegeneratesToColumnCRTLedger AND NoAnonymousFirstMovingCoordinatePoolLedger AND SingleMovingLPFCoordinateDriftImportedLedger AND SingleMovingCoordinateStablePrefixLedger AND SingleMovingCoordinateDyadicScaleLedger AND BoundedScaleDriftDegeneratesToFixedCoordinateLedger AND UnboundedCoordinateScaleEscapeLedger AND PostMovingCoordinateSupportDescentLedger AND SameScaleCoordinateCycleExcludedLedger AND SparseCoordinateDriftSAERegistrationLedger AND NoAnonymousSingleCoordinateDriftLedger AND ScaleEscapingSingleCoordinateDescentImportedLedger AND ScaleEscapeIntegerSupportClockLedger AND ScaleEscapeHalvingClockDescentLedger AND FiniteDepthScaleEscapePerFiberLedger AND TerminalWidthOneFiniteAtomLedger AND ScaleLadderProductWidthColumnCRTExitLedger AND PersistentScaleLadderSignatureRegistrationLedger AND SparseScaleLadderSAERegistrationLedger AND NoCyclicScaleEscapeDescentLedger AND NoAnonymousScaleEscapeDescentLedger AND PersistentScaleLadderSignatureImportedLedger AND ScaleLadderDyadicWordPartitionLedger AND ScaleLadderProductBudgetLedger AND ScaleLadderWordEntropyFiniteCapLedger AND AggregatePersistentPressureToSingleScaleWordLedger AND FixedScaleLadderMCRTColumnCRTExitLedger AND FirstMovingScaleLadderPhaseCoordinateLedger AND SparseScaleLadderSAECarriedForwardLedger AND NoAnonymousPersistentScaleLadderSignatureLedger AND FirstMovingScaleLadderPhaseDriftImportedLedger AND FixedScaleWordSlotLedger AND FinitePrimeChoicesPerScaleSlotLedger AND FiniteResidueChoicesPerPrimeSlotLedger AND FiniteActualScaleLadderAtomSetLedger AND InfinitePigeonholeStableActualScaleLadderLedger AND NoPersistentFirstMovingScaleLadderPhaseDriftLedger AND StableActualScaleLadderMCRTColumnCRTExitLedger AND SparseScaleLadderSAECarriedForwardAfterFiniteSlotLockLedger AND NoAnonymousFirstMovingScaleLadderPhaseDriftLedger AND StableActualLadderOrSparseSAEImportedLedger AND StableActualLadderFiniteGroupLedger AND StableActualLadderZeroMeanCellFunctionLedger AND StableActualLadderExactExcessIdentityLedger AND StableActualLadderFourierPDECBridgeLedger AND StableActualLadderNontrivialCharacterLowerBoundLedger AND NoAnonymousStableActualLadderColumnCRTExitLedger AND SparseScaleLadderSAECarriedForwardAfterFourierBridgeLedger AND StableActualLadderFourierCapImportedLedger AND StableLadderCharacterFactorizationLedger AND StableLadderNontrivialPivotCoordinateLedger AND StableLadderComplementFiberPartitionLedger AND StableLadderGlobalCharacterToPivotFiberLocalizationLedger AND StableLadderPrimitivePivotCharacterCorrelationLedger AND NoAnonymousStableLadderFourierCapLedger AND SparseScaleLadderSAECarriedForwardAfterPivotFiberLedger AND SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 诚实边界

- 本证书没有证明 primitive pivot-fiber PDEC cap。
- 本证书没有证明 sparse scale-ladder SAE 全局可求和。
- 本证书只把 stable ladder 的全局 Fourier cap 局部化为单坐标纤维相位相关输入。
- `SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_pivot_fiber_pdec_router.py` | `8fb6f59a75187da32e78f40ac1f3836aab5a687f7d8d52861a70758c4d1628cb` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-fourier-pdec-router.json` | `d52ae4c6a9033807f58a4e7ab3690971f344e6659c7110f291ec7adb413fb26c` |
