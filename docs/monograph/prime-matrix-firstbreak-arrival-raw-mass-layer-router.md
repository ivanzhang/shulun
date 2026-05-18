# Prime Matrix arrival raw mass 层平衡证书

**状态：** `arrival_raw_mass_reduced_to_low_step_history_mass_or_large_step_tail_escape_open`

raw arrival mass 的 terminal nonarrival 去除被压成精确层平衡。设 H=P-y，稳定 history 源标签的最后零块命中为 t_*。若 q<=H，则 t_*+q<=P-1，所以该源必到达；若 terminal nonarrival 发生，则 q>=H+1。因此 |A|>=|S_{q<=H}|，剩余硬点不是去除口径，而是证明低步长稳定源质量足够；若不足，反例链必须集中在 q>H 的大步长尾逃逸并登记为 PDEC/SAE。

```text
raw_arrival_mass_imported=true
ap_successor_dichotomy_imported=true
source_layer_universe_defined=true
arrival_nonarrival_source_layer_balance_closed=true
low_step_always_arrives_closed=true
terminal_escape_tail_cutoff_closed=true
raw_arrival_lower_bound_formula_closed=true
low_step_stable_history_mass_lower_bound_proved=false
large_step_tail_escape_registered=true
large_step_tail_escape_excluded=false
raw_arrival_mass_after_nonarrival_removal_proved=false
row_column_unconditional_closed=false
```

## 1. 层平衡定义

令 `S` 为 no-loss 与 history-switch 处理后仍留在稳定表中的 source-tagged history 记录。
对 `u in S`，记其 carrier 为 `q(u)`，同 key 在零块 `B=[x0,y-1]` 中的最后命中行为 `t_*(u)`。
稳定 AP 后继二分给出：

```text
t_next(u)=t_*(u)+q(u).
A={u in S: t_next(u)<=P-1}
E={u in S: t_next(u)>=P}
S=A disjoint_union E.
```

这里 `A` 是 source-tagged arrivals，`E` 是 terminal nonarrival。

## 2. 精确阈值 H=P-y

设首破裂后支撑宽度为

```text
H=P-y.
```

由于每个最后零块命中都满足 `t_*(u)<=y-1`，若 `q(u)<=H`，则

```text
t_*(u)+q(u) <= y-1+H = P-1.
```

所以低步长层必定到达：

```text
S_{q<=H} subset A.
```

反过来，若发生 terminal nonarrival，则

```text
t_*(u)+q(u)>=P
=> q(u)>=P-t_*(u)>=P-(y-1)=H+1.
```

因此 terminal nonarrival 全部位于大步长尾部：

```text
E subset S_{q>H}.
```

## 3. raw arrival 下界

上述阈值给出非循环 raw mass 下界：

```text
|A| >= |S_{q<=H}|.
```

所以 `terminal nonarrival` 的去除不会吞掉任何 `q<=H` 的稳定源质量。真正剩余是证明
`S_{q<=H}` 足够厚；若它不够厚，则稳定质量被迫集中在 `q>H` 的大步长尾部，必须作为
`LargeStepTailTerminalEscapePDECOrSAE` 登记。

## 4. 新硬点

因此

```text
ArrivalRawSourceMassAfterNonarrivalRemoval
  -> ArrivalNonarrivalSourceLayerBalanceLedger
  AND LowStepStableHistoryAlwaysArrivesLedger
  AND RawArrivalMassLowerBoundFromLowStepHistory
  AND LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC
```

本步把“nonarrival 去除后 raw mass 是否足够”的问题改写为低步长层质量问题。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RawMassImported | `true` | `false` | 上一层把 distinct arrival quotient 的直接主攻压到 terminal nonarrival 去除后的 raw source mass。 | ArrivalRawSourceMassAfterNonarrivalRemoval |
| APSuccessorDichotomyImported | `true` | `true` | 稳定 history 的 AP 后继二分已闭合：每个稳定源标签只能到达或成为 terminal nonarrival。 | StableHistoryAPSuccessorDichotomyLedger |
| SourceLayerUniverseDefined | `true` | `true` | 令 S 为 no-loss 与 history-switch 处理后仍留在稳定表中的 source-tagged history 记录。 | S=stable source-tagged history layer |
| ArrivalNonarrivalBalanceClosed | `true` | `true` | 对 S 中每个记录，以最后零块命中 t_* 和 carrier q 定义后继 t_*+q；于是 S=A disjoint_union E。 | ArrivalNonarrivalSourceLayerBalanceLedger |
| LowStepAlwaysArrivesClosed | `true` | `true` | 设 H=P-y。因 t_*<=y-1，若 q<=H，则 t_*+q<=P-1，所以该源标签必在 post-break 支撑内到达。 | LowStepStableHistoryAlwaysArrivesLedger |
| TerminalEscapeTailCutoffClosed | `true` | `true` | 若 t_*+q>=P，则 q>=P-t_*>=H+1；terminal nonarrival 全部位于 q>H 的大步长尾部。 | LargeStepTailTerminalEscapePDECOrSAE |
| RawArrivalLowerBoundFormulaClosed | `true` | `true` | 由低步长必到达，raw arrival mass 满足 \|A\|>=\|S_{q<=H}\|；扣除 nonarrival 不会损失低步长层。 | RawArrivalMassLowerBoundFromLowStepHistory |
| LowStepMassStillOpen | `false` | `false` | 仍未证明稳定源层在 q<=H 上有足够质量；若没有，则质量集中到 q>H 大步长尾部。 | LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC |
| LargeStepTailEscapeRegistered | `true` | `false` | 若低步长质量不足以支撑 raw arrival 下界，则反例链必须解释为 q>H tail escape/PDEC/SAE。 | LargeStepTailTerminalEscapePDECOrSAE |
| RawArrivalMassReduced | `true` | `false` | ArrivalRawSourceMassAfterNonarrivalRemoval 被压成 source-layer 平衡、低步长必到达、raw 下界公式和低步长质量/大步长尾逃逸。 | ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC |
| RawArrivalMassProved | `false` | `false` | 本步只关闭 terminal nonarrival 去除的精确阈值与质量恒等式；不证明 q<=H 层已有足够质量。 | LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需低步长稳定质量下界或大步长尾逃逸排斥、高纤维碰撞排斥、history switch 排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 6. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalNonarrivalSourceLayerBalanceLedger AND LowStepStableHistoryAlwaysArrivesLedger AND RawArrivalMassLowerBoundFromLowStepHistory AND LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 诚实边界

- 本证书不证明 raw arrival mass 已足够大。
- 本证书只证明低步长稳定源必到达、terminal nonarrival 必在 q>H 大步长尾部。
- `LowStepStableHistoryMassLowerBoundOrLargeStepTailEscapePDEC` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_arrival_raw_mass_layer_router.py` | `7d1b6b1c05fa66341e8f695e167897a6a4384dc8115073dc0d3d2c761c5e57cd` |
| `docs/monograph/prime-matrix-firstbreak-arrival-quotient-fiber-router.json` | `31bc34c50e0032154758f6ca75fd2bc9f0fffcf9d6f1de7cd71ac07489793da5` |
| `docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.json` | `93c614915d07bfaebb5b3dca9ccb7720e877fe545e0b3bb157f7edb8abcf16e2` |
| `docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json` | `239ad1e89e72ffed043aeaa5087190a2714c04038f7a7743c563405442e389a8` |
| `docs/monograph/prime-matrix-no-loss-return-accounting-router.md` | `9215c5f0e251cd7170759c2cc51c02ddfc9fdfda469a0ff35f26b524ea6cc692` |
| `docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json` | `e5c371d3a6176d81ee48272332c77e73dab552a2aec026249f687dbd55cbe7aa` |
