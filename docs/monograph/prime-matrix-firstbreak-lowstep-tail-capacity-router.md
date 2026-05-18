# Prime Matrix low-step/tail 容量证书

**状态：** `lowstep_mass_reduced_to_total_minus_large_step_tail_envelope_gap_open`

低步长稳定质量硬点被压到显式 tail envelope。设 H=P-y，B=[x0,y-1]，S 为稳定 source-tagged history 层。q<=H 的层必到达；q>H 的 terminal tail 若最后命中为 t_*，则 t_* 必在 B∩[P-q,y-1]，窗口长度至多 min(L,q-H)。固定 q,t_* 后源列 c 至多有 ceil((P-1)/q) 个。因此 |S_{q>H}| 有显式 C_tail 上界，进而 |S_{q<=H}|>=|S|-C_tail。剩余硬点变为证明该差额足够，或证明 tail envelope 近饱和/重复就是 PDEC/SAE。

```text
lowstep_mass_imported=true
raw_layer_balance_imported=true
stable_low_tail_partition_closed=true
terminal_tail_row_window_closed=true
tail_column_multiplicity_closed=true
large_step_tail_envelope_closed=true
lowstep_mass_from_total_minus_tail_closed=true
large_step_tail_no_small_lcm_replay_imported=true
stable_total_minus_tail_envelope_gap_proved=false
large_step_tail_saturation_pdec_excluded=false
lowstep_stable_history_mass_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 低步长/尾部恒等式

设 `H=P-y`，零块 `B=[x0,y-1]`，`L=y-x0`。稳定源层满足

```text
S = S_{q<=H} disjoint_union S_{q>H}.
|S_{q<=H}| = |S| - |S_{q>H}|.
```

上一层已证明 `q<=H` 的稳定源必到达，因此关键是控制 `q>H` 的 terminal tail。

## 2. q>H 的 terminal row window

若 `u in S_{q>H}` 是 terminal nonarrival，最后零块命中行为 `t_*`，则

```text
t_*+q >= P,    t_* in B.
```

所以

```text
t_* in T_q := B ∩ [P-q, y-1].
|T_q| <= min(L, q-H).
```

固定 `q` 和 terminal 行 `t` 后，源列必须满足

```text
c == -tP mod q,    1 <= c < P,
```

所以列数至多

```text
ceil((P-1)/q).
```

## 3. tail envelope 与低步长下界

因此非重复 tail source records 满足

```text
C_tail = sum_{H<q<P} |B ∩ [P-q,y-1]| ceil((P-1)/q)
       <= sum_{H<q<P} min(L,q-H) ceil((P-1)/q),
|S_{q>H}| <= C_tail.
```

从而得到

```text
|S_{q<=H}| >= |S| - C_tail.
```

若出现超过该 envelope 的重复使用，或必须把 tail envelope 压到近饱和才能逃避低步长质量，
则它是命名的 `LargeStepTail` 容量饱和/PDEC/SAE 回流。

## 4. 新硬点

因此

```text
LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC
  -> StableHistoryLowTailMassPartitionLedger
  AND LargeStepTailTerminalWindowEnvelopeLedger
  AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope
  AND StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC
```

本步把低步长质量问题压成一个显式差额问题：证明 `|S|-C_tail` 足够，
或证明 tail 近饱和/重复就是 PDEC/SAE。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LowStepMassImported | `true` | `false` | 上一层把 raw arrival mass 的剩余压成低步长稳定源质量，或 q>H 大步长尾逃逸。 | LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC |
| RawLayerBalanceImported | `true` | `true` | 稳定源层已按 q<=H 到达层和 q>H terminal tail 层分割。 | ArrivalNonarrivalSourceLayerBalanceLedger |
| LowTailPartitionClosed | `true` | `true` | S=S_{q<=H} disjoint_union S_{q>H}，且 \|S_{q<=H}\|=\|S\|-\|S_{q>H}\|。 | StableHistoryLowTailMassPartitionLedger |
| TerminalTailRowWindowClosed | `true` | `true` | 对 q>H 的 terminal nonarrival，最后零块命中 t_* 必在 B∩[P-q,y-1]，该窗口长度至多 min(L,q-H)。 | LargeStepTailTerminalWindowEnvelopeLedger |
| TailColumnMultiplicityClosed | `true` | `true` | 固定 q 和 terminal 行 t 后，源列必须满足 c==-tP mod q；1<=c<P 中至多 ceil((P-1)/q) 个。 | LargeStepTailTerminalWindowEnvelopeLedger |
| LargeStepTailEnvelopeClosed | `true` | `true` | 因此非重复 tail source records 满足 \|S_{q>H}\|<=sum_{H<q<P} \|B∩[P-q,y-1]\| ceil((P-1)/q)。 | LargeStepTailTerminalWindowEnvelopeLedger |
| LowStepMassFromTotalMinusTailClosed | `true` | `true` | 在无 tail 重复/饱和 defect 时，\|S_{q<=H}\|>=\|S\|-C_tail。 | LowStepStableMassLowerBoundFromTotalMinusTailEnvelope |
| LargeStepTailNoSmallLCMReplayImported | `true` | `true` | 若 q>H，则任何包含该 q 的固定 carrier 复现 LCM 已超过 H；它不能隐藏在 small-LCM replay 中。 | q>H => lcm>=q>H |
| TailSaturationReturnRegistered | `true` | `false` | 若低步长质量仍不足，则必须证明 \|S\|-C_tail 不够，或把 tail envelope 近饱和/重复登记为 PDEC/SAE。 | StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC |
| LowStepMassReduced | `true` | `false` | LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC 被压成低/尾分割、tail window envelope、总量减尾容量下界和 tail saturation gap。 | StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC |
| LowStepMassProved | `false` | `false` | 本步没有证明 \|S\|-C_tail 已超过所需需求；只关闭 q>H tail 的显式容量 envelope。 | StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需稳定源总量减 tail envelope 的正间隙，或 tail 近饱和 PDEC/SAE 排斥，并行还需高纤维、碰撞、history switch、strict-gap 与 source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 6. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND StableHistoryLowTailMassPartitionLedger AND LargeStepTailTerminalWindowEnvelopeLedger AND LowStepStableMassLowerBoundFromTotalMinusTailEnvelope AND StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 诚实边界

- 本证书不证明低步长稳定源质量已经足够。
- 本证书只关闭 q>H terminal tail 的 row-window/column-multiplicity envelope。
- `StableTotalMinusTailEnvelopeGapOrLargeStepTailSaturationPDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_lowstep_tail_capacity_router.py` | `10200af9b67b5f7b51b9fd523bcb04253b3e9f8f49f4b64632c09c687e7a868a` |
| `docs/monograph/prime-matrix-firstbreak-arrival-raw-mass-layer-router.json` | `14c7ff4e6754e6dba6f8801ebc0ee8c9fa775dcf7a81669765f0aa0d9369fc49` |
| `docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json` | `239ad1e89e72ffed043aeaa5087190a2714c04038f7a7743c563405442e389a8` |
| `docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.json` | `93c614915d07bfaebb5b3dca9ccb7720e877fe545e0b3bb157f7edb8abcf16e2` |
| `docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.json` | `747ab2d8f1f4569ed1bd9e00f868e26f33a7a22c8310e0776580ee8ad571dad9` |
| `docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json` | `5bd12e6d5f2553e041f20f2b0c1b86ba145c05425b0aa89d973f7707ac4925e2` |
| `docs/monograph/prime-matrix-no-loss-return-accounting-router.md` | `9215c5f0e251cd7170759c2cc51c02ddfc9fdfda469a0ff35f26b524ea6cc692` |
