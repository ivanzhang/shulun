# Prime Matrix cofactor-LPF 覆盖债务证书

**状态：** `dyadic_rough_cofactor_debt_reduced_to_local_cofactor_lpf_cover_debt_open`

dyadic rough cofactor interval 的不足不再只作为支撑下界黑箱保留。对每个 cell 先写全整数权重包络 F_C 与 rough 支撑 B_C；若 B_C 低于预算 A_C，则被小 cofactor 因子删除的 E_C=F_C-B_C 必超过 F_C-A_C。再按 cofactor 的最小素因子 r=lpf(n)<ell 分区，得到 disjoint 的短区间 CRT 覆盖债务。

```text
dyadic_cofactor_debt_imported=true
weighted_envelope_closed=true
support_quota_criterion_closed=true
cofactor_lpf_partition_closed=true
cofactor_lpf_crt_cell_closed=true
product_width_dichotomy_closed=true
local_cofactor_lpf_cover_debt_excluded=false
row_column_unconditional_closed=false
```

## 1. cell 权重包络

固定上一层的 dyadic/quotient/cofactor cell `C=(Y,sigma,j)`。写

```text
alpha_{ell,n}=j*u(ell*n).
```

全整数包络、rough 支撑与删除质量为

```text
F_C=sum_{ell in Y} sum_{n in I_{ell,j,sigma}} alpha_{ell,n},
B_C=sum_{ell in Y} sum_{n in I_{ell,j,sigma}, gcd(n,W_<ell)=1} alpha_{ell,n},
E_C=F_C-B_C.
```

若局部预算为 `A_C`，则

```text
B_C<A_C  <=>  E_C>F_C-A_C.
```

因此 rough 支撑债务等价于 cofactor 小素因子过覆盖债务。

## 2. cofactor LPF 分区

对被删除的 cofactor，按

```text
r=lpf(n)<ell
```

作互不重叠分区：

```text
E_C=sum_{ell in Y} sum_{r<ell} E_{r<-ell},
E_{r<-ell}=sum_{n in I_{ell,j,sigma}, r=lpf(n)} alpha_{ell,n}.
```

每个层又有 CRT 形式

```text
n=r*m,
gcd(m,W_<r)=1,
ceil(n_min/r)<=m<=floor(n_max/r).
```

这一步只使用整数的最小素因子唯一性，不使用短区间素数存在性。

## 3. product-width 出口

若某个局部覆盖债务使用 distinct cofactor primes `R_C`，定义

```text
M_R=prod_{r in R_C}r.
```

完整相位字以 `M_R` 为周期。若 `M_R` 超过该 cell 的支撑宽度，则同一覆盖字不能由局部短周期漂移稳定复现；
它必须登记为有限原子、ColumnCRT/PDEC，或转入更深的 moving-support 出口。

## 4. 新硬点

```text
DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC
  -> CofactorCellWeightedEnvelopeLedger
  AND RoughSupportQuotaCriterionLedger
  AND CofactorLeastPrimeFactorPartitionLedger
  AND CofactorLPFCRTCellLedger
  AND CofactorCoverPrimeProductWidthLedger
  AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC
  AND CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC
```

剩余不再是未解析的 rough 支撑不足，而是 cofactor 最小素因子覆盖过量或 product-width ColumnCRT/PDEC。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DyadicCofactorDebtImported | `true` | `false` | 上一层把 LPF 删除债务定位到 dyadic/quotient/cofactor interval 的 rough 支撑债务。 | DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC |
| WeightedEnvelopeClosed | `true` | `true` | 对每个 cofactor cell 写出全整数权重包络 F_C、rough 支撑质量 B_C 与被小因子删除质量 E_C=F_C-B_C。 | CofactorCellWeightedEnvelopeLedger |
| SupportQuotaCriterionClosed | `true` | `true` | 若目标预算为 A_C，则 B_C<A_C 等价于 E_C>F_C-A_C；局部支撑债务变成 cofactor 小因子过覆盖。 | RoughSupportQuotaCriterionLedger |
| CofactorLPFPartitionClosed | `true` | `true` | 对 gcd(n,W_<ell)>1 的 cofactor，按 r=lpf(n)<ell 作互不重叠分区。 | CofactorLeastPrimeFactorPartitionLedger |
| CofactorLPFCRTCellClosed | `true` | `true` | 每个 r 层写成 n=r*m 且 gcd(m,W_<r)=1 的短区间 CRT 单元。 | CofactorLPFCRTCellLedger |
| ProductWidthDichotomyClosed | `true` | `true` | 若一个局部覆盖族使用 distinct primes R，则其完整相位字周期为 M_R=prod R；M_R 超过支撑宽度时只能作为有限原子或 ColumnCRT/PDEC 复现。 | CofactorCoverPrimeProductWidthLedger |
| LocalCoverDebtStillOpen | `false` | `false` | 仍未排除 cofactor-LPF 过覆盖本身；本步只把 rough 支撑不足改写为更低素因子的显式覆盖债务。 | LocalCofactorLPFCoverDebtOrFiniteAtomPDEC |
| CofactorRoughDebtReduced | `true` | `false` | DyadicRoughCofactorIntervalDebtOrColumnCRTPDEC 被压成局部权重包络、quota、cofactor-LPF 分区、CRT cell 与 product-width 出口。 | CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC |
| ProductWidthColumnCRTExcluded | `false` | `false` | 本步没有证明 product-width/ColumnCRT 出口不可能。 | CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥 cofactor-LPF 覆盖债务或证明其必回流为有限原子、ColumnCRT/PDEC/SAE。 | CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC |

## 6. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND DyadicLPFDeletionLayerPartitionLedger AND DyadicDebtLocalizationForAnyBudgetVectorLedger AND RampSaturatedTailWeightSplitLedger AND QuotientLayerCofactorIntervalLedger AND CofactorIntervalEndpointFormulaLedger AND RoughCofactorIntervalCRTSupportLedger AND DyadicRoughCofactorIntervalDebtOrNamedReturnPDEC AND CofactorCellWeightedEnvelopeLedger AND RoughSupportQuotaCriterionLedger AND CofactorLeastPrimeFactorPartitionLedger AND CofactorLPFCRTCellLedger AND CofactorCoverPrimeProductWidthLedger AND LocalCofactorLPFCoverDebtOrFiniteAtomPDEC AND CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 诚实边界

- 本证书没有证明 cofactor-LPF 过覆盖不可能。
- 本证书只把局部 rough 支撑不足改写为更低素因子的显式 CRT 覆盖债务。
- `CofactorLPFCoverDebtOrProductWidthColumnCRTPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_cofactor_lpf_cover_router.py` | `9f972e53ef81f65c8e1263beebfb6bef7f97a5894855d0480cd5182ea9ab794f` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-dyadic-cofactor-router.json` | `815193dc88d323df25634a9ccc113d5720ea0b6081cd0547993b2f622cc7e1ed` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-deletion-router.json` | `f59a57081a109ae4dac81c86cb87f5590ca50f8627e6ad8b944326fed1b84e8e` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.json` | `0a036df32f9e79916aa6bae21031a046974501d74b9679a93fdca81b08d48e38` |
