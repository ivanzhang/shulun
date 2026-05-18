# Prime Matrix LPF 删除债务 dyadic cofactor 证书

**状态：** `lpf_deletion_debt_reduced_to_dyadic_rough_cofactor_interval_debt_open`

LPF 删除债务被继续拆成 dyadic 最小素因子层、权重层和 quotient cofactor 区间。每个 B_ell 先按 ell 的 dyadic 层 B_Y 汇总；若总删除量不足，则相对于任意候选预算向量 A_Y，至少有一个 dyadic 层短缺。层内再按 ramp/saturated 权重和 j=ceil((P-1)/q) 分块。固定 ell 与 j 后，q=ell*n 把问题变成带 gcd(n,W_<ell)=1 的短 cofactor 区间 CRT 支撑。

```text
lpf_debt_imported=true
dyadic_layer_partition_closed=true
debt_localization_closed=true
ramp_saturated_weight_split_closed=true
quotient_layer_cofactor_interval_closed=true
cofactor_interval_endpoint_formula_closed=true
rough_cofactor_interval_crt_support_closed=true
dyadic_rough_cofactor_interval_debt_excluded=false
row_column_unconditional_closed=false
```

## 1. dyadic LPF 层

从上一层

```text
B_ell=sum_{z<q<P, ell=lpf(q)}w(q)
```

按 dyadic `ell` 层定义

```text
B_Y=sum_{Y<ell<=2Y, ell prime}B_ell,
B_tot=sum_Y B_Y.
```

若 `B_tot<=T`，而某个候选预算向量满足 `sum_Y A_Y>T`，则必存在

```text
B_Y<A_Y.
```

这把总债务定位到至少一个 dyadic LPF 层。

## 2. 权重层

写

```text
w(q)=u(q)v(q),
u(q)=min(L,q-H),
v(q)=ceil((P-1)/q).
```

于是

```text
H<q<H+L  =>  u(q)=q-H,
q>=H+L   =>  u(q)=L.
```

这给出 ramp 与 saturated 两个互不重叠的权重区域。

## 3. quotient cofactor 区间

再按

```text
Q_j={q: ceil((P-1)/q)=j}
```

分层。固定 `ell` 与 `j`，写 `q=ell*n`，则 `Q_j` 与 ramp/saturated 条件一起给出一个显式整数区间

```text
n in I_{ell,j,sigma}.
```

端点可直接写出。令 `A=P-1`，则

```text
q_j_min=floor(A/j)+1,
q_j_max=A                     if j=1,
q_j_max=floor(A/(j-1))        if j>=2.
```

对 ramp 层：

```text
q_min=max(z+1,H+1,q_j_min),
q_max=min(P-1,H+L-1,q_j_max).
```

对 saturated 层：

```text
q_min=max(z+1,H+L,q_j_min),
q_max=min(P-1,q_j_max).
```

于是固定 `ell` 后

```text
n_min=ceil(q_min/ell),
n_max=floor(q_max/ell),
I_{ell,j,sigma}=[n_min,n_max]∩Z.
```

同时 LPF 条件保留为

```text
gcd(n,W_<ell)=1.
```

因此局部单元为

```text
B_{Y,sigma,j}=
sum_{Y<ell<=2Y} sum_{n in I_{ell,j,sigma}, gcd(n,W_<ell)=1} u(ell*n)j.
```

并且精确重组：

```text
B_Y=sum_{sigma in {ramp,sat}} sum_j B_{Y,sigma,j}.
```

## 4. 新硬点

```text
LPFDeletionDebtOrRoughPrefixOverdensityPDEC
  -> DyadicLPFDeletionLayerPartitionLedger
  AND DyadicDebtLocalizationForAnyBudgetVectorLedger
  AND RampSaturatedTailWeightSplitLedger
  AND QuotientLayerCofactorIntervalLedger
  AND CofactorIntervalEndpointFormulaLedger
  AND RoughCofactorIntervalCRTSupportLedger
  AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC
  AND DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC
```

剩余不再是全局 LPF 总债务，而是 dyadic/quotient/cofactor interval 的局部 rough CRT 支撑债务。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LPFDebtImported | `true` | `false` | 上一层把 weighted rough over-density 压成互不重叠的 LPF 删除债务。 | LPFDeletionDebtOrRoughPrefixOverdensityPDEC |
| DyadicLayerPartitionClosed | `true` | `true` | 把 ell 按 Y<ell<=2Y 分层，B_tot=sum_Y B_Y，且层之间互不重叠。 | DyadicLPFDeletionLayerPartitionLedger |
| DebtLocalizationClosed | `true` | `true` | 若 sum_Y B_Y<=T 而任意候选预算 sum_Y A_Y>T，则至少一层满足 B_Y<A_Y。 | DyadicDebtLocalizationForAnyBudgetVectorLedger |
| RampSaturatedWeightSplitClosed | `true` | `true` | w(q)=min(L,q-H)ceil((P-1)/q) 精确拆成 H<q<H+L 的 ramp 层与 q>=H+L 的 saturated 层。 | RampSaturatedTailWeightSplitLedger |
| QuotientCellClosed | `true` | `true` | 再按 j=ceil((P-1)/q) 分层；固定 ell、j 后 q=ell*n 把支撑变成一个显式 cofactor 区间。 | QuotientLayerCofactorIntervalLedger |
| CofactorEndpointFormulaClosed | `true` | `true` | 令 A=P-1；Q_j 给出 q_min=floor(A/j)+1、q_max=A(j=1) 或 floor(A/(j-1))，再与 tail/ramp/sat 边界相交并除以 ell。 | CofactorIntervalEndpointFormulaLedger |
| RoughCofactorIntervalClosed | `true` | `true` | 每个 cofactor 区间还带 gcd(n,W_<ell)=1；因此局部债务是短区间 rough-cofactor CRT 支撑问题。 | RoughCofactorIntervalCRTSupportLedger |
| CofactorIntervalDebtStillOpen | `false` | `false` | 仍未证明每个 dyadic/quotient/cofactor interval 的 rough 支撑给出足够删除质量，或失败必为 ColumnCRT/PDEC。 | DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC |
| LPFDebtReduced | `true` | `false` | LPFDeletionDebtOrRoughPrefixOverdensityPDEC 被压成 dyadic LPF 层、预算定位、权重层、quotient cell、rough cofactor interval 与局部债务。 | DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC |
| DyadicCofactorDebtExcluded | `false` | `false` | 本步没有排斥 dyadic rough cofactor interval debt，只把它写成更小的局部 CRT 支撑问题。 | DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥 dyadic rough cofactor interval debt，或证明其必回流为 ColumnCRT/PDEC/SAE。 | DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC |

## 6. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 诚实边界

- 本证书没有证明 dyadic rough cofactor interval debt 不可能。
- 本证书只把 LPF 删除债务定位到更小的局部 CRT 单元。
- `DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_lpf_dyadic_cofactor_router.py` | `4886197d122277f6e76df99d99c2a5d93fcb46d4c8f76ad42db67d898d74b745` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json` | `f59a57081a109ae4dac81c86cb87f5590ca50f8627e6ad8b944326fed1b84e8e` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.json` | `0a036df32f9e79916aa6bae21031a046974501d74b9679a93fdca81b08d48e38` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json` | `17ee16b69406b0f1a4f9f932ceb56af5de0ccaf634d2c7f092a15f71da8d72d2` |
