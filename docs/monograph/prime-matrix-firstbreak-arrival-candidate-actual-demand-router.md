# Prime Matrix arrival candidate 到 actual demand 证书

**状态：** `arrival_candidate_actual_demand_reduced_to_unit_incidence_and_quotient_lower_bound_open`

arrival candidate 到 actual demand 的接口被拆开：源侧标记的到达候选确实给出一个低 carrier AP row-incidence 单位，且不使用 envelope 饱和反推；但 raw 到达候选不能直接当作聚合需求。必须对 source-tagged arrivals 按 (t_next,q,a) 商化，证明 distinct image 足够大；若大量源义务碰撞到少数 incidence，则该碰撞必须登记为 PDEC/ColumnCRT/SAE/duplicate return。

```text
arrival_candidate_imported=true
no_envelope_recycling_guard_imported=true
source_tagged_unit_incidence_closed=true
arrival_quotient_map_defined=true
no_loss_collision_return_imported=true
arrival_collision_return_registered=true
distinct_arrival_quotient_lower_bound_proved=false
arrival_collision_return_excluded=false
arrival_candidate_actual_demand_injection_proved=false
row_column_unconditional_closed=false
```

## 1. 单位注入

arrival candidate 不是从 AP 表容量反推出来的。它带有零块源侧 history tag，并满足

```text
t_next == -a P^{-1} mod q,   y <= t_next <= P-1.
```

因此它给出一个低 carrier AP row-incidence 单位：

```text
(source tag, t_next, q, a) -> incidence(t_next,q,a).
```

这一步是非循环的，因为它只使用源侧到达标记和同余等式，不使用 AP envelope 是否接近饱和。

## 2. 为什么 raw candidate 不能直接计数

actual demand 下界不能数 raw source-tagged arrivals。必须先商化：

```text
pi: source-tagged arrivals -> (t_next,q,a).
```

真正可与 AP envelope 比较的是 distinct incidence 数 `|image(pi)|`。如果多个源义务映到同一
`(t_next,q,a)`，这些重合不能被删除，也不能当作多个独立 demand；它们必须进入 quotient、weighted return、
duplicate/collision PDEC、ColumnCRT 或 SAE。

## 3. 新硬点

因此

```text
ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse
  -> SourceTaggedArrivalUnitIncidenceLedger
  AND DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC
  AND ArrivalCollisionOrDuplicatePaymentReturnLedger
```

当前真正剩余是证明去重后的 arrival image 足够大；若 image 过小，则必须把塌缩解释为命名碰撞/重复支付终端。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ArrivalCandidateInjectionImported | `true` | `false` | 上一层把稳定 history 的到达分支直接主攻设为 arrival candidate 到 actual demand 的非循环注入。 | ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse |
| ArrivalCandidateImported | `true` | `true` | AP 后继二分已登记：当 t_next=t_*+q 落入 [y,P-1] 时形成 post-break arrival candidate。 | StableHistoryAPSuccessorDichotomyLedger |
| NoEnvelopeRecyclingGuardImported | `true` | `true` | actual demand 下界必须来自源侧到达标记，不能从 AP envelope 接近饱和反推。 | NoAPEnvelopeRecyclingDemandGuard |
| SourceTaggedUnitIncidenceClosed | `true` | `true` | 源侧 arrival candidate 继承零块 history tag，并满足 t_next==-aP^{-1} mod q；因此它给出一个低 carrier AP row-incidence 单位。 | SourceTaggedArrivalUnitIncidenceLedger |
| RawCandidateNotAggregateDemandGuard | `true` | `true` | raw arrival candidate 数不能直接当成 demand 下界；actual demand 只计去重后的 post-break row/cell incidence。 | DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC |
| ArrivalQuotientMapDefined | `true` | `true` | 定义商化映射 pi: source-tagged arrivals -> (t_next,q,a)。actual demand 至少是 image(pi) 的 distinct incidence 数。 | DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC |
| NoLossCollisionReturnImported | `true` | `true` | 若多个源义务映到同一 (t,q,a)，重复不能删除；只能商化、加权或登记 duplicate/collision return。 | ArrivalCollisionOrDuplicatePaymentReturnLedger |
| ArrivalCollisionReturnRegistered | `true` | `false` | 大规模碰撞、重复支付或换源吸收必须进入 PDEC/ColumnCRT/SAE/duplicate return，而不是免费容量。 | ArrivalCollisionOrDuplicatePaymentReturnLedger |
| DistinctArrivalQuotientLowerBoundOpen | `false` | `false` | 仍未证明去重后的 image(pi) 足够大，可以和 AP envelope gap 比较；这是新的聚合硬点。 | DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC |
| ArrivalCandidateInjectionReduced | `true` | `false` | ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse 被压成单位 source-tagged incidence、distinct quotient 下界和碰撞 return 三项。 | SourceTaggedArrivalUnitIncidenceLedger AND DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC AND ArrivalCollisionOrDuplicatePaymentReturnLedger |
| ArrivalCandidateInjectionProved | `false` | `false` | 本步只闭合单位注入，不证明聚合 actual demand 下界，也不排斥碰撞终端。 | DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC AND ArrivalCollisionOrDuplicatePaymentReturnLedger |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、短块 SAE、distinct arrival quotient 下界、terminal nonarrival 排斥、history switch 排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书不证明聚合 actual demand 下界。
- 本证书只证明 source-tagged arrival 的单位 incidence 注入，并建立去重口径。
- `DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC` 与 `ArrivalCollisionOrDuplicatePaymentReturnLedger` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_arrival_candidate_actual_demand_router.py` | `a4e4c04ecc399e5179fc74737dabeac4ead65cd71f52127ca557a527380f7620` |
| `docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.json` | `93c614915d07bfaebb5b3dca9ccb7720e877fe545e0b3bb157f7edb8abcf16e2` |
| `docs/monograph/prime-matrix-firstbreak-actual-demand-source-cut-router.json` | `c6166b673207c6fdc19307de71a6fe1f5b7ed887130b6c5e7e8ad28e030bd5f2` |
| `docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.json` | `2f378d9d29b8bf471ebc203240de29b701774395089998c1477c1af85c384d6f` |
| `docs/monograph/prime-matrix-no-loss-return-accounting-router.md` | `9215c5f0e251cd7170759c2cc51c02ddfc9fdfda469a0ff35f26b524ea6cc692` |
| `docs/monograph/prime-matrix-strict-forced-obligation-lower-bound-router.md` | `46375c4117cd44e681cacc3d31d90bc0555eaed7a6d12ecf4e511fd91671027b` |
| `docs/monograph/prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.md` | `08244ac0b2a2c56467ef6f22422ff3a2ebb103e7aed313edba16f8edde35f598` |
