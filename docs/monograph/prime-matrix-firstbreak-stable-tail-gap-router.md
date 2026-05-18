# Prime Matrix stable tail gap 证书

**状态：** `stable_tail_gap_reduced_to_explicit_functional_and_named_return_mass_open`

stable tail gap 被写成显式 functional。零块覆盖义务总量为 L(P-1)，no-loss 说明这些义务要么成为稳定源记录，要么成为命名 return。若 R_named 记所有 history switch、duplicate、tail saturation 等命名 return 质量，且 C_tail 为上一层 q>H tail envelope，则 |S_{q<=H}|>=L(P-1)-R_named-C_tail。剩余硬点变为证明该 gap 足够大，或证明 R_named/tail saturation 已经是 PDEC/SAE。

```text
tail_gap_imported=true
zero_block_obligation_mass_imported=true
no_loss_accounting_imported=true
stable_total_after_named_returns_closed=true
tail_envelope_imported=true
explicit_tail_gap_functional_closed=true
positive_stable_tail_gap_proved=false
named_return_mass_pdec_excluded=false
stable_total_minus_tail_envelope_gap_proved=false
row_column_unconditional_closed=false
```

## 1. 总源质量

零块覆盖义务域为

```text
O_B={(t,c): x0<=t<y, 1<=c<P},
|O_B|=L(P-1).
```

no-loss 账本给出

```text
O_B = StableSourceRecords disjoint_union NamedReturnRecords.
```

记命名 return 质量为 `R_named`，则

```text
|S| >= L(P-1)-R_named.
```

## 2. gap functional

上一层已经闭合 tail envelope：

```text
C_tail = sum_{H<q<P} |B ∩ [P-q,y-1]| ceil((P-1)/q).
```

因此低步长稳定质量满足显式下界：

```text
|S_{q<=H}| >= L(P-1)-R_named-C_tail.
```

如果该下界不足，不能无名消失；必须由 `R_named`、tail saturation、history switch、duplicate/collision
或 PDEC/SAE 账本承载。

## 3. 新硬点

因此

```text
StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC
  -> ZeroBlockCoverObligationMassLedger
  AND StableSourceTotalAfterNamedReturnsLedger
  AND ExplicitStableTailGapFunctionalLedger
  AND PositiveStableTailGapOrNamedReturnMassPDEC
```

真正剩余是证明 `L(P-1)-R_named-C_tail` 足够大；若失败，则必须证明相应命名 return 质量已经形成 PDEC/SAE。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TailGapImported | `true` | `false` | 上一层把低步长稳定质量压成 \|S\|-C_tail 的显式差额，或 tail saturation PDEC。 | StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC |
| ZeroBlockObligationMassImported | `true` | `true` | 长零块覆盖义务域 O_B={(t,c):x0<=t<y,1<=c<P} 的大小为 L(P-1)。 | ZeroBlockCoverObligationMassLedger |
| NoLossAccountingImported | `true` | `true` | no-loss 账本给出 O_B=StableSourceRecords disjoint_union NamedReturnRecords，无义务丢失。 | ZeroBlockHistoryProjectionNoLossLedger |
| StableTotalAfterNamedReturnsClosed | `true` | `true` | 记 R_named 为 history switch、duplicate、tail saturation 等命名 return 质量，则稳定源总量满足 \|S\|>=L(P-1)-R_named。 | StableSourceTotalAfterNamedReturnsLedger |
| TailEnvelopeImported | `true` | `true` | 上一层已闭合 C_tail=sum_{H<q<P}\|B∩[P-q,y-1]\|ceil((P-1)/q)。 | LargeStepTailTerminalWindowEnvelopeLedger |
| ExplicitTailGapFunctionalClosed | `true` | `true` | 组合得到 \|S_{q<=H}\| >= L(P-1)-R_named-C_tail。 | ExplicitStableTailGapFunctionalLedger |
| PositiveGapStillOpen | `false` | `false` | 仍未证明该显式 gap 超过所需 raw arrival demand；若失败，必须由 R_named 或 tail saturation 承担。 | PositiveStableTailGapOrNamedReturnMassPDEC |
| TailGapReduced | `true` | `false` | StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC 被压成零块总义务、稳定源总量、显式 gap functional 和正 gap/命名 return。 | ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND PositiveStableTailGapOrNamedReturnMassPDEC |
| TailGapProved | `false` | `false` | 本步没有证明 gap 为正或足够大，只把剩余写成显式不等式与命名 return 质量。 | PositiveStableTailGapOrNamedReturnMassPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需正 gap 或命名 return/PDEC 排斥，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND PositiveStableTailGapOrNamedReturnMassPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND PositiveStableTailGapOrNamedReturnMassPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND ZeroBlockCoverObligationMassLedger AND StableSourceTotalAfterNamedReturnsLedger AND ExplicitStableTailGapFunctionalLedger AND PositiveStableTailGapOrNamedReturnMassPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书不证明 tail gap 已经足够大。
- 本证书只把低步长稳定质量下界写成 `L(P-1)-R_named-C_tail`。
- `PositiveStableTailGapOrNamedReturnMassPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_stable_tail_gap_router.py` | `41560da77ed343fccb2cb4247b647697cb0294cc9d7e70732a24950789c3d5a4` |
| `docs/monograph/prime-matrix-firstbreak-lowstep-tail-capacity-router.json` | `a3dd4c8f63dec374475a41dfa3b6439bf2c62823e30576ef870b05e713f752f0` |
| `docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json` | `239ad1e89e72ffed043aeaa5087190a2714c04038f7a7743c563405442e389a8` |
| `docs/monograph/prime-matrix-no-loss-return-accounting-router.md` | `9215c5f0e251cd7170759c2cc51c02ddfc9fdfda469a0ff35f26b524ea6cc692` |
| `docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json` | `e5c371d3a6176d81ee48272332c77e73dab552a2aec026249f687dbd55cbe7aa` |
