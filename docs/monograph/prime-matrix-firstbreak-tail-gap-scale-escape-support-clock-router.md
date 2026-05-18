# Prime Matrix scale-escape support-clock 证书

**状态：** `scale_escaping_single_coordinate_descent_reduced_to_support_clock_open`

尺度逃逸单坐标递降被加上整数支撑时钟 K(W)=ceil(log_2 max(W,1))。每个真实逃逸坐标有 B>=2 且 W_next<=ceil(W/B)，所以 K 严格下降。因此同一反例纤维不能形成 scale-escape 内循环；抽象剩余被压成终端宽度原子、product-width ColumnCRT/PDEC、持久尺度阶梯签名或 sparse scale-ladder SAE。

```text
scale_escape_descent_imported=true
integer_support_clock_closed=true
halving_clock_descent_closed=true
finite_depth_per_fiber_closed=true
terminal_width_one_finite_atom_closed=true
scale_ladder_product_width_exit_closed=true
persistent_scale_ladder_signature_registered=true
sparse_scale_ladder_sae_registered=true
cyclic_scale_escape_descent_excluded=true
anonymous_scale_escape_descent_removed=true
persistent_scale_ladder_excluded=false
sparse_scale_ladder_sae_summability_proved=false
row_column_unconditional_closed=false
```

## 1. 支撑时钟

上一层剩余为尺度逃逸单坐标递降或 sparse drift/SAE。对任一有效支撑宽度 `W` 定义整数时钟：

```text
K(W)=ceil(log_2 max(W,1)).
```

`K(W)=0` 等价于 `W<=1`，此时 residual 支撑已退化为有限原子或命名边界。

## 2. 单步严格下降

真实尺度逃逸层满足 `B_i>=2`，并继承上一层支撑递降：

```text
W_{i+1}<=ceil(W_i/B_i)<=ceil(W_i/2).
```

因此当 `W_i>=2` 时：

```text
K(W_{i+1})<=K(W_i)-1.
```

这给出非循环证明路线中的单调量：尺度逃逸不能回到同一支撑时钟层。

## 3. 有限深度与终端出口

从初始 `W_0` 出发，同一反例纤维上的尺度逃逸步数至多：

```text
K(W_0)=ceil(log_2 max(W_0,1)).
```

若递降到 `W<=1`，则进入有限原子或已命名边界。若尺度阶梯乘积越过初始支撑：

```text
prod_i B_i>W_0,
```

则合成周期超过支撑，进入 ColumnCRT/PDEC 或有限原子。

## 4. 持久阶梯签名与 sparse 出口

未被终端宽度或 product-width 吸收的无限族，不能再以匿名 scale-escape descent 存在。它必须保留一个有序尺度阶梯签名及相位数据。不能在同一签名上持久复现的事件登记为 sparse scale-ladder SAE；本证书只登记该出口，不证明全局求和界。

## 5. 新硬点

```text
ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC
  -> ScaleEscapingSingleCoordinateDescentImportedLedger
  AND ScaleEscapeIntegerSupportClockLedger
  AND ScaleEscapeHalvingClockDescentLedger
  AND FiniteDepthScaleEscapePerFiberLedger
  AND TerminalWidthOneFiniteAtomLedger
  AND ScaleLadderProductWidthColumnCRTExitLedger
  AND PersistentScaleLadderSignatureRegistrationLedger
  AND SparseScaleLadderSAERegistrationLedger
  AND NoCyclicScaleEscapeDescentLedger
  AND NoAnonymousScaleEscapeDescentLedger
  AND PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC
```

剩余从抽象尺度逃逸递降变成持久尺度阶梯签名，或 sparse scale-ladder SAE/ColumnCRT/PDEC。

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ScaleEscapingSingleCoordinateDescentImported | `true` | `false` | 上一层把单个 moving LPF 坐标压成尺度逃逸递降或 sparse drift/SAE/ColumnCRT/PDEC。 | ScaleEscapingSingleCoordinateDescentOrSparseDriftSAEColumnCRTPDEC |
| IntegerSupportClockDefined | `true` | `true` | 对每个有效支撑宽度 W 定义整数时钟 K(W)=ceil(log_2 max(W,1))；K(W)=0 等价于 W<=1。 | ScaleEscapeIntegerSupportClockLedger |
| HalvingClockDescentClosed | `true` | `true` | 真实尺度逃逸层满足 B>=2 且 W_next<=ceil(W/B)，因此 W>=2 时 K(W_next)<=K(W)-1。 | ScaleEscapeHalvingClockDescentLedger |
| FiniteDepthPerFiberClosed | `true` | `true` | 每个固定反例纤维上的尺度逃逸步数至多 K(W_0)；同一纤维不能有无限 scale-escape 内循环。 | FiniteDepthScaleEscapePerFiberLedger |
| TerminalWidthOneFiniteAtomClosed | `true` | `true` | 若递降到 W<=1，则 residual 支撑只剩有限原子或已命名边界，不能继续作为匿名 moving-family 容量池。 | TerminalWidthOneFiniteAtomLedger |
| ScaleLadderProductWidthExitClosed | `true` | `true` | 若尺度阶梯乘积越过初始有效宽度，则合成周期超过支撑，进入 ColumnCRT/PDEC 或有限原子出口。 | ScaleLadderProductWidthColumnCRTExitLedger |
| PersistentScaleLadderSignatureRegistered | `true` | `false` | 未被终端宽度、product-width 或稀疏性吸收的无限族必须保留有序尺度阶梯与相位签名；本步登记该持久签名，不排斥它。 | PersistentScaleLadderSignatureRegistrationLedger |
| SparseScaleLadderSAERegistered | `true` | `false` | 不能在同一签名上持久复现的尺度逃逸事件登记为 sparse scale-ladder SAE；本步不证明全局求和。 | SparseScaleLadderSAERegistrationLedger |
| NoCyclicScaleEscapeDescent | `true` | `true` | 整数时钟严格下降，故尺度逃逸递降不能构成同宽度循环或回到旧尺度支撑层。 | NoCyclicScaleEscapeDescentLedger |
| NoAnonymousScaleEscapeDescent | `true` | `true` | 抽象 scale-escape 口径被拆成终端原子、product-width ColumnCRT/PDEC、持久阶梯签名或 sparse SAE。 | NoAnonymousScaleEscapeDescentLedger |
| PersistentScaleLadderStillOpen | `false` | `false` | 仍未排斥持久尺度阶梯签名，也未证明 sparse scale-ladder SAE 全局可求和。 | PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥持久尺度阶梯签名，或证明其必回流为 ColumnCRT/PDEC/SAE 且全局可控。 | PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC |

## 7. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFTriplePressureImportedLedger AND IteratedLPFOrderedRoughResidualChainLedger AND LPFSupportProductReciprocityInvariantLedger AND LPFDepthRankBudgetLedger AND IteratedLPFCRTWordCellLedger AND IteratedLPFProductWidthColumnCRTExitLedger AND TerminalResidualFiniteAtomLedger AND IteratedLPFWellFoundedNoCycleLedger AND RankBudgetedMovingFamilyImportedLedger AND IteratedLPFWordSignaturePartitionLedger AND LPFWordEntropyFiniteCapLedger AND AggregatePressureToSingleLPFWordLedger AND FixedLPFWordColumnCRTExitLedger AND FirstMovingLPFCoordinateLedger AND MovingCoordinateSupportReciprocityLedger AND NoAnonymousRankBudgetedMovingFamilyLedger AND FirstMovingLPFCoordinatePressureImportedLedger AND StablePrefixProductSupportLedger AND FirstMovingCoordinateEffectiveWidthLedger AND LowMovingCoordinateFiniteAtomLedger AND FirstMovingCoordinateDyadicPartitionLedger AND MovingCoordinateActiveProductWidthExitLedger AND MovingCoordinateActiveCountBoundLedger AND SingleMovingCoordinatePressureLocalizationLedger AND FixedMovingCoordinateDegeneratesToColumnCRTLedger AND NoAnonymousFirstMovingCoordinatePoolLedger AND SingleMovingLPFCoordinateDriftImportedLedger AND SingleMovingCoordinateStablePrefixLedger AND SingleMovingCoordinateDyadicScaleLedger AND BoundedScaleDriftDegeneratesToFixedCoordinateLedger AND UnboundedCoordinateScaleEscapeLedger AND PostMovingCoordinateSupportDescentLedger AND SameScaleCoordinateCycleExcludedLedger AND SparseCoordinateDriftSAERegistrationLedger AND NoAnonymousSingleCoordinateDriftLedger AND ScaleEscapingSingleCoordinateDescentImportedLedger AND ScaleEscapeIntegerSupportClockLedger AND ScaleEscapeHalvingClockDescentLedger AND FiniteDepthScaleEscapePerFiberLedger AND TerminalWidthOneFiniteAtomLedger AND ScaleLadderProductWidthColumnCRTExitLedger AND PersistentScaleLadderSignatureRegistrationLedger AND SparseScaleLadderSAERegistrationLedger AND NoCyclicScaleEscapeDescentLedger AND NoAnonymousScaleEscapeDescentLedger AND PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 8. 诚实边界

- 本证书没有证明持久尺度阶梯签名不可能。
- 本证书没有证明 sparse scale-ladder SAE 全局可求和。
- 本证书只关闭抽象 scale-escape 内循环和匿名递降口径。
- `PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_scale_escape_support_clock_router.py` | `7a09fffb41e7434f487a62eec09b9184b44a4ecda465162033a7f4d0753b9a05` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json` | `6b868246b6f4ef3560e71693da177d566f7a2310a6e539110838371b6db5e168` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json` | `3fa3246c30134bf6ecf97e839fc07704d12e009e50ec8fe0303b8575285d12bf` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json` | `c2a85de6fe4ea7153190111a2c1656adda5ea7631edf71ff38127f668a3ee5bf` |
