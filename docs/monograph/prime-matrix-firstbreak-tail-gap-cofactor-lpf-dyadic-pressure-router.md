# Prime Matrix cofactor-LPF dyadic pressure 证书

**状态：** `cofactor_lpf_cover_debt_reduced_to_dyadic_pressure_or_small_product_columncrt_open`

cofactor-LPF 覆盖债务被继续拆成局部 excess threshold、活动素因子 product-width 二分、dyadic r 层压力定位和固定 r 的 rough-m CRT 支撑。若活动素因子乘积大于 cell 支撑宽度，只能作为 product-width ColumnCRT/PDEC 复现；若乘积不大，则反例必须集中在 small-product active cover，且至少一个 dyadic r 层超过其候选预算。

```text
cofactor_lpf_cover_debt_imported=true
excess_threshold_closed=true
active_prime_product_dichotomy_closed=true
dyadic_r_partition_closed=true
overfull_localization_closed=true
fixed_r_m_endpoint_closed=true
r_layer_crt_closed=true
small_product_concentration_excluded=false
dyadic_pressure_excluded=false
row_column_unconditional_closed=false
```

## 1. excess threshold

上一层给出 `B_C<A_C <=> E_C>F_C-A_C`。本层记

```text
H_C=F_C-A_C.
```

因此局部反例要求

```text
E_C>H_C.
```

这把支撑不足变成明确的覆盖过量阈值。

## 2. active product 二分

令

```text
R_C={r prime: E_r(C)>0},
M_C=prod_{r in R_C}r.
```

若 `M_C>width(C)`，同一覆盖相位字的复现周期超过 cell 支撑宽度，必须进入 product-width ColumnCRT/PDEC 或有限原子出口。
若 `M_C<=width(C)`，则所有高覆盖被迫集中在 small-product active set 上。

## 3. dyadic r 层压力

按 `Z<r<=2Z` 分解：

```text
E_C=sum_Z E_Z(C),
M_C=prod_Z M_Z.
```

若候选允许预算 `U_Z` 满足

```text
sum_Z U_Z<=H_C
```

而反例要求 `E_C>H_C`，则存在某个 dyadic 层

```text
E_Z(C)>U_Z.
```

这把局部 over-cover 压到一个 dyadic `r` 层。

## 4. 固定 r 的 lower CRT 单元

固定 `r` 后，上一层的 cofactor 区间 `n_min<=n<=n_max` 给出

```text
n=r*m,
m_min=ceil(n_min/r),
m_max=floor(n_max/r).
```

并保留

```text
gcd(m,W_<r)=1.
```

所以过载层变成更低阶 rough-m CRT 支撑问题，而不是原命题的短区间素数存在性。

## 5. 新硬点

```text
CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC
  -> CofactorCoverExcessThresholdLedger
  AND ActiveCofactorPrimeProductDichotomyLedger
  AND DyadicCofactorPrimePressurePartitionLedger
  AND OverfullDyadicRLayerLocalizationLedger
  AND FixedRToMIntervalEndpointLedger
  AND RLayerRoughMCRTSupportLedger
  AND SmallProductActiveCoverConcentrationPDEC
  AND DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC
```

剩余变成 dyadic r 层过载，或 small-product active cover 的 ColumnCRT/PDEC。

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CofactorLPFCoverDebtImported | `true` | `false` | 上一层把 rough 支撑不足改写为 cofactor 最小素因子覆盖过量或 product-width ColumnCRT/PDEC。 | CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC |
| ExcessThresholdClosed | `true` | `true` | 对 cell C，令 H_C=F_C-A_C；局部反例要求 E_C>H_C。 | CofactorCoverExcessThresholdLedger |
| ActivePrimeProductDichotomyClosed | `true` | `true` | 活动 cofactor primes R_C 的乘积 M_C=prod R_C；若 M_C 超过支撑宽度，则进入 product-width ColumnCRT/PDEC，否则进入 small-product concentration。 | ActiveCofactorPrimeProductDichotomyLedger |
| DyadicRPartitionClosed | `true` | `true` | 按 Z<r<=2Z 分解 E_C=sum_Z E_Z，同时 M_C=prod_Z M_Z。 | DyadicCofactorPrimePressurePartitionLedger |
| OverfullLocalizationClosed | `true` | `true` | 若 E_C>H_C 且候选允许预算 sum_Z U_Z<=H_C，则至少一个 dyadic r 层满足 E_Z>U_Z。 | OverfullDyadicRLayerLocalizationLedger |
| FixedRMEndpointClosed | `true` | `true` | 固定 r 后，n=r*m 给出 m_min=ceil(n_min/r)、m_max=floor(n_max/r) 的显式短区间。 | FixedRToMIntervalEndpointLedger |
| RLayerCRTClosed | `true` | `true` | 固定 r 层保留 gcd(m,W_<r)=1，成为更低阶 rough-m CRT 支撑。 | RLayerRoughMCRTSupportLedger |
| SmallProductConcentrationStillOpen | `false` | `false` | 仍未排除 active product 小于支撑宽度时的局部高覆盖集中。 | SmallProductActiveCoverConcentrationPDEC |
| CofactorCoverDebtReduced | `true` | `false` | CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC 被压成 excess threshold、active product 二分、dyadic r 压力层与 small-product 出口。 | CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC |
| DyadicPressureExcluded | `false` | `false` | 本步没有证明 dyadic r 层过载不可能。 | DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥 dyadic cofactor-LPF pressure 或 small-product ColumnCRT/PDEC。 | DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC |

## 7. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 8. 诚实边界

- 本证书没有证明 dyadic r 层过载不可能。
- 本证书没有证明 small-product active cover concentration 不可能。
- 本证书只把 cofactor-LPF 覆盖债务压成 product-width 二分和 dyadic r 层压力。
- `DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_dyadic_pressure_router.py` | `30c0006077bc25ffa7ea92a97f2fc838df9dd15a7ba9a97650d2c77fbd416d29` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json` | `d0820c64d6454d2627268b840d6a30f988a104577904f8875f20e4ff5b2df8d2` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json` | `815193dc88d323df25634a9ccc113d5720ea0b6081cd0547993b2f622cc7e1ed` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json` | `f59a57081a109ae4dac81c86cb87f5590ca50f8627e6ad8b944326fed1b84e8e` |
