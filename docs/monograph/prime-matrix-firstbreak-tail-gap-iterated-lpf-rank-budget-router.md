# Prime Matrix iterated-LPF rank-budget 证书

**状态：** `second_lpf_triple_pressure_reduced_to_rank_budgeted_iterated_lpf_family_open`

二级/triple rough-t pressure 被改写成迭代 LPF 因子词。每加入一个 least-prime-factor，合成 CRT 周期乘积同步扩大，而 residual 支撑宽度按该乘积收缩。因此同一尺度上不可能无限循环；若周期乘积超过支撑宽度，只剩 ColumnCRT/PDEC 或有限原子。剩余不是自由 triple pressure，而是有显式深度预算的 moving-family。

```text
second_lpf_triple_pressure_imported=true
ordered_residual_chain_closed=true
support_product_reciprocity_closed=true
depth_rank_budget_closed=true
iterated_crt_word_cell_closed=true
product_width_exit_closed=true
terminal_residual_finite_atom_closed=true
well_founded_no_cycle_closed=true
rank_budgeted_moving_family_excluded=false
row_column_unconditional_closed=false
```

## 1. 从 triple cell 到因子词

上一层剩余为二级 LPF/triple rough-t pressure。固定 `(r,ell,s)` 后：

```text
q=ell*r*m,
m=s*t,
s=lpf(m)>=r,
gcd(t,W_<s)=1.
```

若 residual `n_i>1`，递归取：

```text
a_i=lpf(n_i),
n_i=a_i*n_{i+1},
gcd(n_{i+1},W_<a_i)=1.
```

于是 LPF 因子词满足：

```text
r<=s<=a_1<=a_2<=...
```

允许重复；重复只表示同一素因子的幂次继续消耗 residual。

## 2. 支撑-周期互反不变量

令：

```text
A_h=s*prod_{i<=h}a_i.
```

原 m 支撑宽度为 `width_m`。经过因子词 `A_h` 后，残余支撑满足：

```text
width(n_h-support)<=ceil(width_m/A_h).
```

这就是当前最关键的非循环结构：CRT 周期乘积越大，能承载同一相位字的 residual 支撑越小。

## 3. 秩预算

非有限分支中 `r>=2`，且每个新增因子都至少为 `r`。因此若仍未进入 product-width 出口，必须有：

```text
A_h<=width_m.
```

从而：

```text
d<=floor(log_r(width_m)).
```

这里 `d` 是包含初始二级因子 `s` 的总因子深度。所以 triple pressure 不能隐藏成无限 LPF 塔；它只能是有限秩、有限深的因子词 moving-family。

## 4. product-width 出口

若某一活动因子词的合成模数乘积超过原支撑宽度：

```text
M_word>width_m,
```

则同一相位字在该支撑内至多命中孤立有限原子，必须登记为 ColumnCRT/PDEC 或有限原子。

## 5. 新硬点

```text
SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC
  -> SecondLPFTriplePressureImportedLedger
  AND IteratedLPFOrderedRoughResidualChainLedger
  AND LPFSupportProductReciprocityInvariantLedger
  AND LPFDepthRankBudgetLedger
  AND IteratedLPFCRTWordCellLedger
  AND IteratedLPFProductWidthColumnCRTExitLedger
  AND TerminalResidualFiniteAtomLedger
  AND IteratedLPFWellFoundedNoCycleLedger
  AND RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC
```

剩余从自由 triple pressure 变成秩预算化迭代 LPF moving-family，或 ColumnCRT/PDEC。

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SecondLPFTriplePressureImported | `true` | `false` | 上一层把 fixed-pair rough-m pressure 的剩余压到二级 LPF/triple rough-t pressure。 | SecondLPFDescentPressureOrTripleMCRTColumnCRTPDEC |
| IteratedLPFOrderedResidualChainClosed | `true` | `true` | 从 residual n_0 开始，若 n_i>1 令 a_i=lpf(n_i)，n_i=a_i n_{i+1}；由 rough 条件得 a_i 非降且 a_i>=r。 | IteratedLPFOrderedRoughResidualChainLedger |
| LPFSupportProductReciprocityClosed | `true` | `true` | 经过含初始 s 的因子词 A_h=s*prod a_i 后，残余支撑宽度至多 ceil(width_m/A_h)；CRT 周期乘积增大时支撑同步收缩。 | LPFSupportProductReciprocityInvariantLedger |
| LPFDepthRankBudgetClosed | `true` | `true` | 非有限分支 r>=2。令 d 为含 s 的总因子深度；若 A_h<=width_m，则 d<=floor(log_r(width_m))；超过该预算即落入单点/有限原子。 | LPFDepthRankBudgetLedger |
| IteratedLPFCRTWordCellClosed | `true` | `true` | 每个有限因子词给出一个确定的 MCRT phase word；相位复现只能沿该词的合成模数周期发生。 | IteratedLPFCRTWordCellLedger |
| IteratedProductWidthExitClosed | `true` | `true` | 若活动因子词的合成模数乘积超过原 m 支撑宽度，则同一相位字至多命中孤立原子，并登记 ColumnCRT/PDEC。 | IteratedLPFProductWidthColumnCRTExitLedger |
| TerminalResidualFiniteAtomClosed | `true` | `true` | 当 residual 支撑宽度降到 1 或 residual=1 时，分支变成固定 q 的有限原子。 | TerminalResidualFiniteAtomLedger |
| IteratedLPFNoCycleClosed | `true` | `true` | 秩函数 (support width, residual product) 在每次真实 LPF 展开中良序下降，排除同尺度循环。 | IteratedLPFWellFoundedNoCycleLedger |
| RankBudgetedMovingFamilyStillOpen | `false` | `false` | 仍未排除随 P 移动的低秩 LPF 因子词族；本步只把 triple pressure 压成有显式秩预算的 moving-family/ColumnCRT 出口。 | RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥秩预算化 moving-family，或证明其必回流为 ColumnCRT/PDEC/SAE。 | RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC |

## 7. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorCoverExcessThresholdLedger AND ActiveCofactorPrimeProductDichotomyLedger AND DyadicCofactorPrimePressurePartitionLedger AND OverfullDyadicRLayerLocalizationLedger AND FixedRToMIntervalEndpointLedger AND RLayerRoughMCRTSupportLedger AND SmallProductActiveCoverConcentrationPDEC AND ActivePrimeCardinalityFromProductLedger AND SmallZFiniteAtomBoundaryLedger AND SingleCofactorPrimePressureLocalizationLedger AND FixedRSourceEllPartitionLedger AND FixedREllRoughMCRTCellLedger AND FixedPairProductWidthColumnCRTExitLedger AND SingleRSmallProductPressurePDEC AND FixedPairPressureImportedLedger AND FixedPairMSupportStrictDescentLedger AND MEqualsOneFiniteAtomLedger AND SecondCofactorLeastPrimeFactorPartitionLedger AND SecondLPFRoughTCRTCellLedger AND SecondLPFProductWidthColumnCRTExitLedger AND ResidualSupportWidthStrictDecreaseNoCycleLedger AND SecondLPFTriplePressureImportedLedger AND IteratedLPFOrderedRoughResidualChainLedger AND LPFSupportProductReciprocityInvariantLedger AND LPFDepthRankBudgetLedger AND IteratedLPFCRTWordCellLedger AND IteratedLPFProductWidthColumnCRTExitLedger AND TerminalResidualFiniteAtomLedger AND IteratedLPFWellFoundedNoCycleLedger AND RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 8. 诚实边界

- 本证书没有证明秩预算化 moving-family 不可能。
- 本证书只证明二级/triple pressure 必须服从支撑-周期互反不变量与有限秩预算。
- `RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_iterated_lpf_rank_budget_router.py` | `257046c394f3c686ca904a24894c4e5943da03b42f4f81482f813d1a0583f578` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json` | `123ec9a28b04798275d24045335861539f5a6578455016fdbed46c802a41592d` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json` | `63c7b8a83211be0fd6f6bb2d324638748ac86a06b6cce10fedcc700a2312b87c` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-cofactor-lpf-dyadic-pressure-router.json` | `a974b12d5b59cad79da5dc7e950fd3d37d5c71fd018c9698654442588277e06c` |
