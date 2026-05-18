# Prime Matrix fixed-pair second-LPF descent 证书

**状态：** `fixed_pair_pressure_reduced_to_strict_second_lpf_descent_open`

fixed-pair rough-m pressure 被继续拆成严格下降的二级 LPF 单元。在固定 (r,ell) 中，q=ell*r*m 且 gcd(m,W_<r)=1。m=1 是有限原子；m>1 时令 s=lpf(m)>=r，得到 m=s*t 与 gcd(t,W_<s)=1。由于非有限分支 r>=2，t 的支撑宽度严格小于 m 的支撑宽度，不能形成同尺度循环。

```text
fixed_pair_pressure_imported=true
m_support_strict_descent_closed=true
m_equals_one_finite_atom_closed=true
second_lpf_partition_closed=true
second_lpf_crt_cell_closed=true
second_product_width_closed=true
strict_no_cycle_closed=true
second_lpf_pressure_excluded=false
row_column_unconditional_closed=false
```

## 1. 固定 pair 的 m 单元

上一层把压力压到固定 `(r,ell)`：

```text
q=ell*r*m,
m_min<=m<=m_max,
gcd(m,W_<r)=1,
beta_m=j*u(ell*r*m).
```

`m=1` 只给出单点 `q=ell*r`，登记为有限原子。

## 2. 二级 LPF 分区

对 `m>1`，由 `gcd(m,W_<r)=1` 得

```text
s=lpf(m)>=r.
```

于是

```text
m=s*t,
gcd(t,W_<s)=1,
t_min=ceil(m_min/s),
t_max=floor(m_max/s).
```

并有互不重叠分区：

```text
E_{r<-ell}=E_{m=1}+sum_{s>=r}E_{s<-r,ell}.
```

## 3. 严格下降 no-cycle

记 `width_m=m_max-m_min+1`。固定 `s` 后：

```text
width_t<=ceil(width_m/s)<=ceil(width_m/r).
```

非有限分支已有 `r>=2`。因此若 `width_m>1`，递降后的支撑宽度严格变小；若 `width_m<=1`，直接进入有限原子。
这给出非循环证书：二级 LPF 递降不能在同一支撑尺度上闭环。

## 4. product-width 出口

若二级活动素因子集合为 `S`，定义

```text
M_S=prod_{s in S}s.
```

若 `M_S>width_m`，二级相位字的复现周期超过原 m 支撑宽度，只能登记为 ColumnCRT/PDEC 或有限原子。

## 5. 新硬点

```text
SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC
  -> FixedPairPressureImportedLedger
  AND FixedPairMSupportStrictDescentLedger
  AND MEqualsOneFiniteAtomLedger
  AND SecondCofactorLeastPrimeFactorPartitionLedger
  AND SecondLPFRoughTCRTCellLedger
  AND SecondLPFProductWidthColumnCRTExitLedger
  AND ResidualSupportWidthStrictDecreaseNoCycleLedger
  AND SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC
```

剩余变成二级 LPF/triple rough-t pressure，或二级 product-width ColumnCRT/PDEC。

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FixedPairPressureImported | `true` | `false` | 上一层把 small-product dyadic 压力压到 single-r/fixed-pair rough-m pressure。 | SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC |
| MSupportStrictDescentClosed | `true` | `true` | 固定 (r,ell) 后 q=ell*r*m；非有限分支 r>=2，二级分解后的 t 支撑宽度至多 ceil(width_m/r)，严格小于原 m 支撑或进入有限原子。 | FixedPairMSupportStrictDescentLedger |
| MEqualsOneFiniteAtomClosed | `true` | `true` | m=1 是固定 q=ell*r 的单点有限原子，不能支撑无限复现压力。 | MEqualsOneFiniteAtomLedger |
| SecondLPFPartitionClosed | `true` | `true` | 对 m>1 且 gcd(m,W_<r)=1，令 s=lpf(m)>=r；按 s 作互不重叠的二级 LPF 分区。 | SecondCofactorLeastPrimeFactorPartitionLedger |
| SecondLPFCRTCellClosed | `true` | `true` | 固定 s 后 m=s*t，且 gcd(t,W_<s)=1，得到更低支撑的 rough-t CRT 单元。 | SecondLPFRoughTCRTCellLedger |
| SecondProductWidthClosed | `true` | `true` | 活动 residual primes S 的乘积若超过 m 支撑宽度，则同一二级相位字只能作为 ColumnCRT/PDEC 或有限原子复现。 | SecondLPFProductWidthColumnCRTExitLedger |
| StrictNoCycleClosed | `true` | `true` | 每次二级 LPF 递降都把活动支撑宽度至少除以 r>=2；无限循环只能撞到 width<=1 的有限原子。 | ResidualSupportWidthStrictDecreaseNoCycleLedger |
| SecondLPFPressureStillOpen | `false` | `false` | 仍未排除二级 LPF/triple rough-t pressure；本步只证明它是严格下降的固定三元单元或 ColumnCRT/PDEC。 | SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC |
| FixedPairPressureReduced | `true` | `false` | SingleCofactorPrimePressureOrFixedPairMCRTColumnCRTPDEC 被压成固定 pair 导入、m 支撑严格下降、二级 LPF 分区、rough-t CRT 与 no-cycle 出口。 | FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥二级 LPF/triple pressure 或证明其必回流为 ColumnCRT/PDEC/SAE。 | SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC |

## 7. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 8. 诚实边界

- 本证书没有证明二级 LPF/triple pressure 不可能。
- 本证书只证明 fixed-pair pressure 若继续下钻，必须严格降低支撑尺度或进入 ColumnCRT/PDEC/有限原子。
- `SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_fixed_pair_second_lpf_descent_router.py` | `68aea0f3ad6505b7299a42dfbd6dc7be94ac2f9718e182af2eefa321b24bebd6` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json` | `63c7b8a83211be0fd6f6bb2d324638748ac86a06b6cce10fedcc700a2312b87c` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json` | `a974b12d5b59cad79da5dc7e950fd3d37d5c71fd018c9698654442588277e06c` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-cover-router.json` | `d0820c64d6454d2627268b840d6a30f988a104577904f8875f20e4ff5b2df8d2` |
