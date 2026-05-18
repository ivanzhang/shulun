# Prime Matrix cofactor-LPF single-r pressure 证书

**状态：** `dyadic_cofactor_lpf_pressure_reduced_to_single_r_fixed_pair_pressure_open`

dyadic r 层过载在 small-product 分支中不能继续保持为层总量。若活动乘积不超过 cell 支撑宽度，活动素因子个数受到对数界控制；总层压力超标时，必须有单个 r 承担超过平均阈值的压力。固定 r 后再按源 ell 分区，最终得到固定 (r,ell) 的 rough-m CRT 单元。

```text
dyadic_pressure_imported=true
active_prime_cardinality_closed=true
small_z_finite_atom_boundary_closed=true
single_r_pressure_localization_closed=true
fixed_r_source_ell_partition_closed=true
fixed_r_ell_rough_m_crt_cell_closed=true
fixed_pair_product_width_closed=true
single_r_pressure_excluded=false
row_column_unconditional_closed=false
```

## 1. small-product 给出活动个数界

在 dyadic 层 `Z<r<=2Z` 中，活动集合为

```text
R_Z(C)={r: Z<r<=2Z, E_r(C)>0}.
```

`Z<2` 的最低层作为有限小素因子原子边界单独登记。以下取 `Z>=2`。若仍处于 small-product 分支

```text
M_Z=prod_{r in R_Z(C)}r <= W_C=width(C),
```

而每个活动 `r>Z`，则

```text
|R_Z(C)| <= K_Z=floor(log W_C/log Z).
```

这把 small-product 分支转成活动素因子个数有限的压力问题。

## 2. single-r 压力定位

若 dyadic 层超预算

```text
E_Z(C)>U_Z,
```

且 `|R_Z(C)|<=K_Z`，则必有某个活动素因子

```text
E_r(C)>U_Z/K_Z.
```

因此反例不能只停留在 dyadic 总层，必须落到单个 `r`。

## 3. 固定 r 到固定 (r,ell)

固定 `r` 后按源 `ell` 分区：

```text
E_r(C)=sum_{ell in Y, ell>r}E_{r<-ell}(C).
```

若单个 `r` 仍超预算，则同样存在固定 `ell` 源层超预算。该 pair 的单元为

```text
q=ell*r*m,
m_min=ceil(n_min/r),
m_max=floor(n_max/r),
gcd(m,W_<r)=1.
```

权重为

```text
alpha_{ell,r*m}=j*u(ell*r*m).
```

## 4. 新硬点

```text
DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC
  -> ActivePrimeCardinalityFromProductLedger
  AND SmallZFiniteAtomBoundaryLedger
  AND SingleCofactorPrimePressureLocalizationLedger
  AND FixedRSourceEllPartitionLedger
  AND FixedREllRoughMCRTCellLedger
  AND FixedPairProductWidthColumnCRTExitLedger
  AND SingleRSmallProductPressurePDEC
  AND SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC
```

剩余变成 single-r/fixed-pair rough-m pressure，或 fixed-pair ColumnCRT/PDEC。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DyadicPressureImported | `true` | `false` | 上一层把 cofactor-LPF 覆盖债务压成 dyadic r 层过载或 small-product ColumnCRT/PDEC。 | DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC |
| ActiveCardinalityClosed | `true` | `true` | 在 dyadic 层 Z<r<=2Z 且 Z>=2 中，若活动乘积 M_Z<=W_C，则活动素因子个数 a_Z 受 K_Z=floor(log W_C/log Z) 控制。 | ActivePrimeCardinalityFromProductLedger |
| SmallZBoundaryClosed | `true` | `true` | Z<2 的最低 cofactor prime 层只含有限小素因子，单独登记为有限原子边界。 | SmallZFiniteAtomBoundaryLedger |
| SingleRPressureClosed | `true` | `true` | 若 E_Z>U_Z 且 a_Z<=K_Z，则某个活动 r 满足 E_r>U_Z/K_Z。 | SingleCofactorPrimePressureLocalizationLedger |
| FixedREllPartitionClosed | `true` | `true` | 固定 r 后，E_r=sum_{ell in Y, ell>r}E_{r<-ell}；若 E_r 超预算，则至少一个 ell 源层超预算。 | FixedRSourceEllPartitionLedger |
| FixedPairMCRTCellClosed | `true` | `true` | 固定 r 与 ell 后，q=ell*r*m，m 位于显式短区间且 gcd(m,W_<r)=1。 | FixedREllRoughMCRTCellLedger |
| FixedPairProductWidthClosed | `true` | `true` | 固定 pair 的相位字若需要多个 residual primes，则其 product-width 超过 m 支撑时进入 ColumnCRT/PDEC。 | FixedPairProductWidthColumnCRTExitLedger |
| SingleRSmallProductStillOpen | `false` | `false` | 仍未排除单个 r 或固定 pair 的高压力；本步只把 small-product 层压力压到 single-r/fixed-pair 单元。 | SingleRSmallProductPressurePDEC |
| DyadicPressureReduced | `true` | `false` | DyadicCofactorLPFPressureOrSmallProductColumnCRTPDEC 被压成 active cardinality、single-r pressure、fixed-pair rough-m CRT 与 product-width 出口。 | ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC |
| SingleRPressureExcluded | `false` | `false` | 本步没有证明 single-r/fixed-pair pressure 不可能。 | SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥 single-r/fixed-pair rough-m pressure 或证明其必回流为 ColumnCRT/PDEC/SAE。 | SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC |

## 6. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 诚实边界

- 本证书没有证明 single-r/fixed-pair pressure 不可能。
- 本证书只把 small-product dyadic 压力压成单个 `r` 与固定 `(r,ell)` 单元。
- `SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_single_r_pressure_router.py` | `df09f036495f56d3cecafe2f6a8cec5ca8e640794a89822a86b41c34001f3d05` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json` | `a974b12d5b59cad79da5dc7e950fd3d37d5c71fd018c9698654442588277e06c` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json` | `d0820c64d6454d2627268b840d6a30f988a104577904f8875f20e4ff5b2df8d2` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json` | `815193dc88d323df25634a9ccc113d5720ea0b6081cd0547993b2f622cc7e1ed` |
