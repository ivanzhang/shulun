# Prime Matrix tail gap 归一化证书

**状态：** `positive_tail_gap_reduced_to_one_dimensional_tail_index_functional_open`

positive stable tail gap 被归一化成一维 tail-index 和式。令 q=H+r，H=P-y。则 P-q=y-r，故 terminal row window B∩[P-q,y-1] 变为 B∩[y-r,y-1]，长度精确为 min(L,r)。因此 C_tail=sum_{prime q=H+r<P} min(L,r)ceil((P-1)/(H+r))。剩余硬点不再是窗口几何，而是证明该一维 prime-tail functional 留出正 gap；若没有，失败只能登记为 dense tail、tail saturation 或 named-return mass PDEC。

```text
positive_gap_imported=true
explicit_gap_functional_imported=true
tail_index_change_of_variables_closed=true
exact_prime_tail_envelope_closed=true
all_integer_dominating_envelope_closed=true
named_return_separation_closed=true
normalized_positive_gap_proved=false
dense_tail_return_pdec_excluded=false
positive_stable_tail_gap_proved=false
row_column_unconditional_closed=false
```

## 1. q=H+r 归一化

设 `H=P-y`。对 tail carrier 写

```text
q=H+r,  1<=r<P-H.
```

则

```text
P-q = P-H-r = y-r.
```

因此 terminal row window 精确为

```text
B ∩ [P-q,y-1] = B ∩ [y-r,y-1],
|B ∩ [P-q,y-1]| = min(L,r).
```

## 2. 一维 tail functional

于是 prime tail envelope 化成

```text
C_tail = sum_{prime q=H+r<P} min(L,r) ceil((P-1)/(H+r)).
```

去掉素数限制给出安全上界

```text
C_tail <= C_all = sum_{1<=r<P-H} min(L,r) ceil((P-1)/(H+r)).
```

gap 分离为

```text
G_prime = L(P-1)-C_tail,
G = G_prime-R_named.
```

## 3. 新硬点

因此

```text
PositiveStableTailGapOrNamedReturnMassPDEC
  -> TailIndexChangeOfVariablesLedger
  AND ExactPrimeTailEnvelopeOneDimensionalLedger
  AND StableTailGapNamedReturnSeparationLedger
  AND NormalizedTailGapPositiveOrDenseTailReturnPDEC
```

真正剩余是证明归一化 prime-tail functional 留出正 gap；若失败，必须证明 dense tail、tail saturation
或 named-return mass 已经构成 PDEC/SAE。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PositiveGapImported | `true` | `false` | 上一层把 stable tail gap 的直接主攻设为正 gap 或命名 return/PDEC。 | PositiveStableTailGapOrNamedReturnMassPDEC |
| ExplicitGapFunctionalImported | `true` | `true` | 已得到 \|S_{q<=H}\|>=L(P-1)-R_named-C_tail。 | ExplicitStableTailGapFunctionalLedger |
| TailIndexChangeOfVariablesClosed | `true` | `true` | 令 q=H+r。因 H=P-y，行窗口 B∩[P-q,y-1]=B∩[y-r,y-1]，长度精确为 min(L,r)。 | TailIndexChangeOfVariablesLedger |
| ExactPrimeTailEnvelopeClosed | `true` | `true` | 因此 C_tail=sum_{prime q=H+r<P} min(L,r) ceil((P-1)/(H+r))。 | ExactPrimeTailEnvelopeOneDimensionalLedger |
| AllIntegerDominatingEnvelopeClosed | `true` | `true` | 去掉 q 为素数的限制得到安全上界 C_tail<=C_all=sum_{1<=r<P-H} min(L,r) ceil((P-1)/(H+r))。 | AllIntegerTailEnvelopeDominatesPrimeTailLedger |
| NamedReturnSeparationClosed | `true` | `true` | gap 可分为 G_prime=L(P-1)-C_tail 与 G=G_prime-R_named；命名 return 质量只进入最后扣除项。 | StableTailGapNamedReturnSeparationLedger |
| NormalizedPositiveGapStillOpen | `false` | `false` | 仍未证明归一化 gap 足够大；若不足，则必须由 prime tail 过密、tail 饱和或 R_named 过大承担。 | NormalizedTailGapPositiveOrDenseTailReturnPDEC |
| PositiveGapReduced | `true` | `false` | PositiveStableTailGapOrNamedReturnMassPDEC 被压成 tail-index 归一化、精确 prime tail envelope、gap 分离和归一化正 gap/稠密 return。 | TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedTailGapPositiveOrDenseTailReturnPDEC |
| PositiveGapProved | `false` | `false` | 本步没有证明正 gap；只把 C_tail 化成一维 r-sum，并把失败形态登记为 dense tail/named return PDEC。 | NormalizedTailGapPositiveOrDenseTailReturnPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需归一化正 gap 或 dense tail/named return 排斥，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedTailGapPositiveOrDenseTailReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedTailGapPositiveOrDenseTailReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND TailIndexChangeOfVariablesLedger AND ExactPrimeTailEnvelopeOneDimensionalLedger AND StableTailGapNamedReturnSeparationLedger AND NormalizedTailGapPositiveOrDenseTailReturnPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书不证明归一化 gap 为正。
- 本证书只把 `C_tail` 化成一维 `r=q-H` 的 exact prime-tail functional。
- `NormalizedTailGapPositiveOrDenseTailReturnPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_tail_gap_normalization_router.py` | `03ebc3ef1af7b7422e1755739b920b46b4832cd7f263c7a8fd2c5149d7bbe9f6` |
| `docs/monograph/prime-matrix-firstbreak-stable-tail-gap-router.json` | `b9d4683be96296b04e206cdc5d17afee2e936457da2c913f55a60ac820ddb557` |
| `docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.json` | `a3dd4c8f63dec374475a41dfa3b6439bf2c62823e30576ef870b05e713f752f0` |
| `docs/monograph/prime-matrix-firstbreak-arrival-raw-mass-layer-router.json` | `14c7ff4e6754e6dba6f8801ebc0ee8c9fa775dcf7a81669765f0aa0d9369fc49` |
| `docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json` | `239ad1e89e72ffed043aeaa5087190a2714c04038f7a7743c563405442e389a8` |
