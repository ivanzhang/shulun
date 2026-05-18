# Prime Matrix 稳定 history 的 AP 到达二分证书

**状态：** `stable_history_injection_reduced_to_ap_arrival_dichotomy_open`

稳定 history 到 post-break AP demand 的注入被压到 AP 后继二分：同一 history key 的零块最后命中 t_* 后，下一次同余行精确为 t_*+q；若 t_*+q<=P-1，则得到 post-break AP arrival candidate；若 t_*+q>=P，则该 key 在平方锚前没有支撑，必须登记为 terminal nonarrival/large-step escape。到达候选仍未自动成为 actual demand。

```text
stable_history_route_imported=true
ap_row_class_formula_closed=true
last_prebreak_hit_successor_closed=true
arrival_nonarrival_dichotomy_closed=true
terminal_nonarrival_large_step_registered=true
arrival_candidate_registered=true
arrival_candidate_actual_demand_proved=false
terminal_nonarrival_excluded=false
postbreak_ap_demand_injection_proved=false
row_column_unconditional_closed=false
```

## 1. 后继行精确公式

对稳定 history key `kappa=(q,a)`，低 carrier AP 行类为

```text
t == -a P^{-1} mod q.
```

令 `t_*` 是该 key 在零块 `B=[x0,y-1]` 中的最后一次命中。因为同一行类的相邻命中相差 `q`，
下一次同 key 行精确为

```text
t_next = t_* + q.
```

由 `t_*` 的最后性，若 `t_next<y` 就仍在零块内并矛盾，因此必有 `t_next>=y`。

## 2. 到达/越界二分

post-break 支撑为 `I_y=[y,P-1]`，宽度 `H=P-y`。于是

```text
arrival candidate      <=> t_*+q <= P-1 <=> q <= P-1-t_*,
terminal nonarrival   <=> t_*+q >= P   <=> q >= P-t_*.
```

这给出稳定 history 注入的精确相位门。到达只是 AP cell 候选；未到达不是需求，而是 AP 周期超过
平方锚前支撑宽度的 large-step escape，必须进入 `PDEC/SAE` 或 moving/terminal 账本。

## 3. 新硬点

因此

```text
PostBreakAPDemandInjectionFromStableHistory
  -> StableHistoryAPSuccessorDichotomyLedger
  AND ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse
  AND TerminalNonarrivalLargeStepEscapePDECOrSAE
```

当前真正剩余是：到达候选如何不借用 envelope 饱和而变成 actual demand；以及未到达 large-step 出口如何排斥或求和。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PostBreakInjectionImported | `true` | `false` | 上一层把长零块稳定 history 分支的直接主攻设为 post-break AP demand 注入。 | PostBreakAPDemandInjectionFromStableHistory |
| StableHistoryRouteImported | `true` | `true` | 稳定低 carrier/residue 支付表已经从长零块无损投影中分离出来。 | StableLowCarrierPaymentTableOrHistorySwitchPDEC |
| APRowClassFormulaClosed | `true` | `true` | 对 history key kappa=(q,a)，因 (P,q)=1，行集合精确为 t==-a P^{-1} mod q。 | StableHistoryAPSuccessorDichotomyLedger |
| LastPrebreakHitSuccessorClosed | `true` | `true` | 若 t_* 是同 key 在零块 B=[x0,y-1] 中的最后一次命中，则下一次同 key 行必为 t_*+q；且由最后性知 t_*+q>=y。 | StableHistoryAPSuccessorDichotomyLedger |
| ArrivalNonarrivalDichotomyClosed | `true` | `true` | 同 key 后继命中落入 post-break 支撑 I_y=[y,P-1] 当且仅当 q<=P-1-t_*；否则 q>=P-t_*，成为 terminal nonarrival。 | ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse OR TerminalNonarrivalLargeStepEscapePDECOrSAE |
| TerminalNonarrivalLargeStepRegistered | `true` | `false` | 未到达不是 demand：它精确表示 AP 步长超过平方锚前剩余支撑宽度，必须登记为 large-step escape/PDEC/SAE。 | TerminalNonarrivalLargeStepEscapePDECOrSAE |
| ArrivalCandidateRegistered | `true` | `false` | 到达事件只给 post-break AP cell 候选；仍需证明该候选确实承担 actual demand，且不通过 envelope 饱和反推。 | ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse |
| ArrivalCollisionReturnRegistered | `true` | `false` | 若到达候选被重复支付、碰撞或换源吸收，则必须回到 duplicate/collision return 账本，不能删除。 | ArrivalCollisionOrDuplicatePaymentReturnLedger |
| PostBreakInjectionReduced | `true` | `false` | PostBreakAPDemandInjectionFromStableHistory 被压成 AP 后继二分、到达候选 actual 注入、未到达 large-step 出口三项。 | StableHistoryAPSuccessorDichotomyLedger AND ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse AND TerminalNonarrivalLargeStepEscapePDECOrSAE |
| PostBreakInjectionProved | `false` | `false` | 本步没有证明稳定 history 已产生 actual demand 下界；只关闭了 AP 后继到达/越界的精确二分。 | ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse AND TerminalNonarrivalLargeStepEscapePDECOrSAE |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、短块 SAE、到达候选 actual 注入、terminal nonarrival 排斥、history switch 排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书不证明稳定 history 已经注入 actual demand。
- 本证书只证明每个稳定 key 的下一 AP 行有精确到达/越界二分。
- `ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse` 与 `TerminalNonarrivalLargeStepEscapePDECOrSAE` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_stable_history_ap_arrival_router.py` | `120cf6c17fd19d1d3d333aabeeadc322a3718c69b1b317e7d9d5f244aaa3cb53` |
| `docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json` | `239ad1e89e72ffed043aeaa5087190a2714c04038f7a7743c563405442e389a8` |
| `docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.json` | `2f378d9d29b8bf471ebc203240de29b701774395089998c1477c1af85c384d6f` |
| `docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.json` | `c6166b673207c6fdc19307de71a6fe1f5b7ed887130b6c5e7e8ad28e030bd5f2` |
| `docs/monograph/prime-matrix-no-loss-return-accounting-router.md` | `9215c5f0e251cd7170759c2cc51c02ddfc9fdfda469a0ff35f26b524ea6cc692` |
| `docs/monograph/prime-matrix-inverse-alignment-prefix-demand-bridge-router.md` | `b24c6b66e0c23671e7be814d2b06d405bb240da70b3930e6d37be6241e67ab37` |
