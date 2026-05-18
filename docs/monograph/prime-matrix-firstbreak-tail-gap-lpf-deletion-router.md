# Prime Matrix weighted rough tail LPF 删除债务证书

**状态：** `weighted_rough_tail_reduced_to_lpf_deletion_debt_open`

weighted rough tail 的失败形态被改写为最小素因子删除债务。小端 q<=z 的非素数质量先精确扣出为 D_small；大端 z<q<P 中，每个非素数有唯一最小素因子 ell<=z，于是 D_large=sum B_ell。按 ell 递增筛时，前缀 rough 质量的 telescoping 降幅正是 B_ell，且每个 B_ell 是 q=ell*n、gcd(n,W_<ell)=1 的 CRT 删除单元。若真实 gap 仍失败，则不是 rough 集合抽象过密，而是某些 dyadic 最小素因子层删除质量不足，或命名 return 吃掉这些删除。

```text
weighted_rough_target_imported=true
small_tail_finite_nonprime_defect_closed=true
large_tail_lpf_partition_closed=true
rough_prefix_deletion_telescoping_closed=true
lpf_crt_deletion_cell_closed=true
lpf_sieved_gap_functional_closed=true
dyadic_lpf_deletion_debt_excluded=false
lpf_deletion_debt_proved_impossible=false
row_column_unconditional_closed=false
```

## 1. 小端与大端

沿用

```text
w(q)=min(L,q-H)ceil((P-1)/q),
z=floor(sqrt(P-1)).
```

先把小端非素数质量单独扣出：

```text
D_small=sum_{H<q<=z, q not prime}w(q).
```

`q=1` 若出现在 tail 中，也自动归入这个有限小端。

## 2. 最小素因子唯一分区

若 `z<q<P` 且 `q` 非素数，则 `lpf(q)<=sqrt(q)<=z`，且 `lpf(q)` 唯一。因此

```text
B_ell=sum_{z<q<P, ell=lpf(q)}w(q),
D_large=sum_{ell<=z}B_ell,
D_np=D_small+D_large.
```

这把非素数筛缺陷变成互不重叠的最小素因子删除层。

## 3. CRT 删除单元

记

```text
W_<ell=prod_{p<ell}p.
```

则每个删除层有精确 CRT 形式：

```text
B_ell=sum_{z/ell<n<P/ell, gcd(n,W_<ell)=1} w(ell*n).
```

这说明每个删除块都是 `q=0 mod ell` 且避开更小素数模的 CRT 单元。

## 4. 前缀 rough telescoping

令 `W_u=prod_{p<=u}p`，并定义

```text
S_u=sum_{z<q<P, gcd(q,W_u)=1}w(q).
```

按素数 `ell` 递增筛时：

```text
S_{ell^-}-S_ell=B_ell,
S_0-S_z=sum_{ell<=z}B_ell.
```

所以 weighted rough over-density 等价于这些 CRT 删除层总降幅过小。

## 5. 筛后 gap

设

```text
Phi=L(L-D)+min(L,y-1)-X_core.
```

则真实 gap 为

```text
G=Phi+D_small+sum_{ell<=z}B_ell-R_named.
```

若

```text
Phi+D_small+sum B_ell>R_named,
```

则正 gap 已成立。若反例仍存在，则必须满足

```text
sum B_ell<=R_named-Phi-D_small.
```

这就是最小素因子删除债务。

## 6. 新硬点

```text
SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC
  -> SmallTailFiniteNonprimeDefectLedger
  AND LargeTailLeastPrimeFactorPartitionLedger
  AND RoughPrefixDeletionTelescopingLedger
  AND LeastPrimeFactorCRTDeletionCellLedger
  AND SievedGapLPFDeletionFunctionalLedger
  AND DyadicLPFDeletionDebtOrNamedReturnPDEC
  AND LPFDeletionDebtOrRoughPrefixOverdensityPDEC
```

下一步不再处理重叠包含-排除，而是攻击 disjoint LPF 删除层的 dyadic 债务。

## 7. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| WeightedRoughTargetImported | `true` | `false` | 上一层把 self-mirror 剩余压成筛后 gap，失败时必须是 weighted sqrt-rough CRT 支撑过密或命名 return 过大。 | SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC |
| SmallTailFiniteDefectClosed | `true` | `true` | q<=z 的非素数 tail 是有限小端，直接作为 D_small 精确扣回；q=1 边界自动包含在内。 | SmallTailFiniteNonprimeDefectLedger |
| LargeTailLPFPartitionClosed | `true` | `true` | 对 z<q<P 的非素数，最小素因子 ell<=z 唯一存在，故大 tail 非素数缺陷按 ell 唯一分块。 | LargeTailLeastPrimeFactorPartitionLedger |
| RoughPrefixTelescopingClosed | `true` | `true` | 按素数 ell 递增筛去 q≡0 mod ell；前缀 rough 质量的每一步降幅正是对应 LPF 删除块 B_ell。 | RoughPrefixDeletionTelescopingLedger |
| LPFCRTDeletionCellClosed | `true` | `true` | 每个 B_ell 可写为 q=ell*n、z/ell<n<P/ell、gcd(n,W_<ell)=1 的 CRT 删除单元。 | LeastPrimeFactorCRTDeletionCellLedger |
| LPFSievedGapFunctionalClosed | `true` | `true` | 真实 gap 改写为 Phi + D_small + sum_ell B_ell - R_named，其中 Phi=L(L-D)+min(L,y-1)-X_core。 | SievedGapLPFDeletionFunctionalLedger |
| DyadicLPFDebtStillOpen | `false` | `false` | 若 gap 失败，则 LPF 删除总量未能超过 R_named-Phi-D_small；必须定位到某些 dyadic ell 层的删除债务或命名 return。 | DyadicLPFDeletionDebtOrNamedReturnPDEC |
| WeightedRoughReduced | `true` | `false` | SelfMirrorSievedTailGapOrWeightedRoughCRTDefectPDEC 被压成小端非素数缺陷、large-tail LPF 唯一分区、前缀删除 telescoping、CRT 删除单元和 dyadic 删除债务。 | SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND LPFDeletionDebtOrRoughPrefixOverdensityPDEC |
| LPFDeletionDebtExcluded | `false` | `false` | 本步没有证明所有 LPF 删除层给出足够质量；只把 rough over-density 变成 disjoint CRT 删除债务。 | LPFDeletionDebtOrRoughPrefixOverdensityPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需排斥 dyadic LPF 删除债务，或证明该债务必回流为 PDEC/SAE/ColumnCRT。 | LPFDeletionDebtOrRoughPrefixOverdensityPDEC |

## 8. 新活动基

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedIntegerTailMarginFunctionalLedger AND PrimeTailDominatedByIntegerTailEnvelopeLedger AND EarlyHalfSupportTailCannotSaturateLemma AND IntegerMarginPositiveBranchCriterionLedger AND LateSupportExcessCoordinateLedger AND RegularTailTwoUnitEndpointDefectLedger AND LateCoreExcessFunctionalLedger AND LateCollarMarginExactFormulaLedger AND DeepLateCollarMirrorContainmentLedger AND CrossCollarPositiveMarginCriterionLedger AND CoreExcessQuotientLayerDecompositionLedger AND CoreExcessLayerConcentrationOrNamedReturnPDEC AND PrimeTailNonprimeDefectExactLedger AND SqrtRoughPrimeTailIdentityLedger AND EndpointParityNonprimeDefectLowerBoundLedger AND SievedTailGapMarginFunctionalLedger AND SievedPositiveGapCriterionLedger AND WeightedRoughTailCRTDefectOrNamedReturnPDEC AND SmallTailFiniteNonprimeDefectLedger AND LargeTailLeastPrimeFactorPartitionLedger AND RoughPrefixDeletionTelescopingLedger AND LeastPrimeFactorCRTDeletionCellLedger AND SievedGapLPFDeletionFunctionalLedger AND DyadicLPFDeletionDebtOrNamedReturnPDEC AND LPFDeletionDebtOrRoughPrefixOverdensityPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 9. 诚实边界

- 本证书没有证明 LPF 删除层总能支付 gap。
- 本证书把 rough over-density 改写为互不重叠的 CRT 删除债务。
- `LPFDeletionDebtOrRoughPrefixOverdensityPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 10. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_lpf_deletion_router.py` | `3e44426badfdce2ed4e6ece6768a10a60df278f93d28b0047acecf601c93d272` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-sieved-defect-router.json` | `0a036df32f9e79916aa6bae21031a046974501d74b9679a93fdca81b08d48e38` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-deep-collar-layer-router.json` | `17ee16b69406b0f1a4f9f932ceb56af5de0ccaf634d2c7f092a15f71da8d72d2` |
| `docs/monograph/prime-matrix-firstbreak-tail-gap-late-collar-router.json` | `496714585ada926f0875418c4d1b5ce1e3d3fa6a5d5074537069120a48b594e3` |
