# Prime Matrix LPF word-entropy / first-moving-coordinate 证书

**状态：** `rank_budgeted_moving_family_reduced_to_first_moving_lpf_coordinate_open`

秩预算化迭代 LPF moving-family 被拆成有限 word 熵和首移动坐标。LPF 唯一性给出有序因子词分区；深度预算使活动 word 集有限。若承压 word 稳定，则回到固定 MCRT/ColumnCRT；若不稳定，则存在首个移动 LPF 坐标，其加入会按 A_prefix*mu 收缩 residual 支撑。剩余硬点变成首移动坐标压力，而非匿名 moving-family。

```text
rank_budgeted_moving_family_imported=true
word_signature_partition_closed=true
word_entropy_finite_cap_closed=true
aggregate_to_single_word_closed=true
fixed_word_columncrt_exit_closed=true
first_moving_coordinate_closed=true
moving_coordinate_support_reciprocity_closed=true
anonymous_moving_family_removed=true
first_moving_coordinate_pressure_excluded=false
row_column_unconditional_closed=false
```

## 1. LPF word 分区

上一层把剩余压成秩预算化 moving-family。对每个 residual，由 LPF 唯一性得到唯一有序因子词：

```text
omega=(s,a_1,...,a_d),
r<=s<=a_1<=...<=a_d,
A(omega)=s*prod_{i<=d}a_i.
```

若 `A(omega)>W`，其中 `W` 是原 m 支撑宽度，则已进入 product-width ColumnCRT/PDEC 或有限原子。

## 2. word 熵预算

未进入 product-width 出口时：

```text
A(omega)<=W.
```

非有限分支所有因子至少为 `r>=2`，因此总因子深度满足：

```text
d+1<=floor(log_r W).
```

所以活动 word 集 `Omega(P,C)` 是有限集合，大小受显式熵预算 `H(W,r)` 控制。它不能作为无限匿名容量池。

## 3. 聚合压力定位

把总压力写为互不重叠 word cell 之和：

```text
E(Omega)=sum_{omega in Omega} E_omega.
```

若 `E(Omega)>U`，则存在单个 word 满足：

```text
E_omega>U/|Omega|.
```

因此剩余压力必须落在单个 LPF word 上，而不能停留在未命名的 moving-family 总量上。

## 4. 固定 word 与首移动坐标

若承压 word 的素坐标和相位残基在族中稳定，则它是固定 MCRT word：

```text
stable omega + stable residues => FixedLPFWordColumnCRTExit.
```

若不稳定，则存在首个移动坐标 `mu`。设它之前的稳定前缀乘积为：

```text
A_prefix.
```

首移动坐标加入后，残余支撑宽度满足：

```text
width_after_mu<=ceil(W/(A_prefix*mu)).
```

若 `A_prefix*mu>W`，则回到 ColumnCRT/PDEC 或有限原子；否则真正剩余只可能是首移动坐标压力。

## 5. 新硬点

```text
RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC
  -> RankBudgetedMovingFamilyImportedLedger
  AND IteratedLPFWordSignaturePartitionLedger
  AND LPFWordEntropyFiniteCapLedger
  AND AggregatePressureToSingleLPFWordLedger
  AND FixedLPFWordColumnCRTExitLedger
  AND FirstMovingLPFCoordinateLedger
  AND MovingCoordinateSupportReciprocityLedger
  AND NoAnonymousRankBudgetedMovingFamilyLedger
  AND FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC
```

剩余从秩预算化 moving-family 变成首移动 LPF 坐标压力，或 word-motion ColumnCRT/PDEC。

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RankBudgetedMovingFamilyImported | `true` | `false` | 上一层把自由 triple pressure 压成有显式深度预算的迭代 LPF moving-family。 | RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC |
| IteratedLPFWordSignaturePartitionClosed | `true` | `true` | LPF 唯一性把每个 residual 分入唯一有序因子词 omega=(s,a_1,...,a_d)，且 A(omega)<=W 或进入 product-width 出口。 | IteratedLPFWordSignaturePartitionLedger |
| LPFWordEntropyFiniteCapClosed | `true` | `true` | 对 omega=(s,a_1,...,a_d)，深度预算 d+1<=floor(log_r W) 给出有限 word 熵 H(W,r)；活动 word 集不能作为无限匿名容量池。 | LPFWordEntropyFiniteCapLedger |
| AggregatePressureToSingleWordClosed | `true` | `true` | 有限 word 集上若总压力超界，则至少一个 word 承载平均以上压力；否则聚合压力已由 word 熵预算吸收。 | AggregatePressureToSingleLPFWordLedger |
| FixedLPFWordColumnCRTExitClosed | `true` | `true` | 若承压 word 的全部素坐标和相位残基在族中稳定，则它不是 moving-family，而是固定 MCRT word，回到 ColumnCRT/PDEC 或有限原子。 | FixedLPFWordColumnCRTExitLedger |
| FirstMovingLPFCoordinateClosed | `true` | `true` | 若 word 不稳定，存在首个移动坐标 mu；其前缀 word 稳定，所有移动都集中到该首移动素层之后。 | FirstMovingLPFCoordinateLedger |
| MovingCoordinateSupportReciprocityClosed | `true` | `true` | 首移动坐标 mu 加入后，残余支撑至多 ceil(W/(A_prefix*mu))；若 A_prefix*mu>W，则直接 ColumnCRT/PDEC/有限原子。 | MovingCoordinateSupportReciprocityLedger |
| NoAnonymousRankBudgetedMovingFamilyClosed | `true` | `true` | rank-budgeted moving-family 被拆成固定 word ColumnCRT 出口或首移动坐标压力；不再保留匿名 moving-family 终端。 | NoAnonymousRankBudgetedMovingFamilyLedger |
| FirstMovingCoordinatePressureStillOpen | `false` | `false` | 仍未排除首移动 LPF 坐标的持久压力；本步只把 moving-family 压到首移动坐标相位/容量接口。 | FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥首移动 LPF 坐标压力，或证明其必回流为 ColumnCRT/PDEC/SAE。 | FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC |

## 7. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFTriplePressureImportedLedger AND IteratedLPFOrderedRoughResidualChainLedger AND LPFSupportProductReciprocityInvariantLedger AND LPFDepthRankBudgetLedger AND IteratedLPFCRTWordCellLedger AND IteratedLPFProductWidthColumnCRTExitLedger AND TerminalResidualFiniteAtomLedger AND IteratedLPFWellFoundedNoCycleLedger AND RankBudgetedMovingFamilyImportedLedger AND IteratedLPFWordSignaturePartitionLedger AND LPFWordEntropyFiniteCapLedger AND AggregatePressureToSingleLPFWordLedger AND FixedLPFWordColumnCRTExitLedger AND FirstMovingLPFCoordinateLedger AND MovingCoordinateSupportReciprocityLedger AND NoAnonymousRankBudgetedMovingFamilyLedger AND FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 8. 诚实边界

- 本证书没有证明首移动 LPF 坐标压力不可能。
- 本证书只删除匿名 rank-budgeted moving-family 口径，把它压成固定 word 出口或首移动坐标压力。
- `FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_lpf_word_entropy_motion_router.py` | `818e4c6631929793060fda6507b12e6d8e5ecbac009157d02446cb9af16ae0e9` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json` | `54719636b257d5414a51208df863483c167ac34dc12a0f0a1c9f73b9b1b5b515` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json` | `123ec9a28b04798275d24045335861539f5a6578455016fdbed46c802a41592d` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json` | `63c7b8a83211be0fd6f6bb2d324638748ac86a06b6cce10fedcc700a2312b87c` |
