# Prime Matrix arrival quotient 纤维重数证书

**状态：** `arrival_quotient_reduced_to_fiber_envelope_and_raw_mass_open`

distinct arrival quotient 的乘数纪律被精确化。固定 arrival incidence (t,q,a) 的原像只能来自零块中同一 AP 行类和同一列剩余类，因此纤维大小至多 ceil(L/q)ceil((P-1)/q)。这给出加权 image 下界 |image(pi)| >= sum 1/F(pi(u))。剩余不是口径问题，而是 raw arrival mass 是否足够，以及若 image 过小是否能把高纤维集中登记并排斥为 dense low-carrier/PDEC/SAE。

```text
source_tagged_unit_incidence_imported=true
arrival_quotient_map_imported=true
fiber_row_factor_closed=true
fiber_column_factor_closed=true
arrival_fiber_envelope_closed=true
weighted_image_lower_bound_formula_closed=true
raw_arrival_mass_after_nonarrival_removal_proved=false
high_fiber_concentration_registered=true
high_fiber_collision_pdec_excluded=false
distinct_arrival_quotient_lower_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 纤维公式

令 `A` 为 source-tagged arrivals，商化映射为

```text
pi: A -> (t_next,q,a).
```

固定一个 image 点 `(t,q,a)`。其源行 `s` 必须在零块 `B=[x0,y-1]` 中满足

```text
s == t mod q.
```

所以行因子

```text
R_B(t,q) = #{s in B: s == t mod q} <= ceil(L/q).
```

源列 `c` 必须满足

```text
1 <= c < P,   c == a mod q,
```

所以列因子

```text
C_P(a,q) <= ceil((P-1)/q).
```

因此原像纤维满足

```text
|pi^{-1}(t,q,a)| <= ceil(L/q) ceil((P-1)/q).
```

## 2. 加权 image 下界

记 `F(t,q,a)=ceil(L/q)ceil((P-1)/q)`。纤维上界给出严格的商化下界：

```text
|image(pi)| >= sum_{u in A} 1/F(pi(u)).
```

特别地，若 `Fmax=max F(pi(u))`，则

```text
|image(pi)| >= |A|/Fmax.
```

这一步关闭的是乘数纪律：任何把许多源义务压到同一 arrival incidence 的行为都必须由上述纤维解释；
若超过纤维 envelope，则是重复登记或碰撞 return。

## 3. 新硬点

因此

```text
DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC
  -> ArrivalQuotientFiberMultiplicityEnvelopeLedger
  AND ArrivalRawSourceMassAfterNonarrivalRemoval
  AND WeightedArrivalImageLowerBoundFromFiberEnvelope
  AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn
```

真正剩余是证明 terminal nonarrival 去除后的 raw arrival mass 足够大；若 weighted image 仍然太小，
则压力集中在小 q/高纤维或重复碰撞上，必须回流到 dense low-carrier/PDEC/SAE。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DistinctArrivalQuotientImported | `true` | `false` | 上一层把聚合 actual demand 的直接主攻设为 distinct arrival quotient 下界或 collision PDEC。 | DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC |
| SourceTaggedUnitIncidenceImported | `true` | `true` | source-tagged arrival 已给出低 carrier AP incidence 单位。 | SourceTaggedArrivalUnitIncidenceLedger |
| ArrivalQuotientMapImported | `true` | `true` | 商化映射 pi: source-tagged arrivals -> (t_next,q,a) 已定义。 | pi(source arrival)=(t_next,q,a) |
| FiberRowFactorClosed | `true` | `true` | 固定 arrival incidence (t,q,a) 的源行 s 必须满足 s==t mod q 且 s in [x0,y-1]，所以行因子至多 ceil(L/q)。 | R_B(t,q)<=ceil(L/q) |
| FiberColumnFactorClosed | `true` | `true` | 固定 q,a 的源列 c 必须满足 1<=c<P 且 c==a mod q，所以列因子至多 ceil((P-1)/q)。 | C_P(a,q)<=ceil((P-1)/q) |
| ArrivalFiberEnvelopeClosed | `true` | `true` | 同一 (t,q,a) 的原像纤维至多 ceil(L/q)ceil((P-1)/q)；超过该值只能是口径错误或重复登记 return。 | ArrivalQuotientFiberMultiplicityEnvelopeLedger |
| WeightedImageLowerBoundFormulaClosed | `true` | `true` | 由纤维上界，\|image(pi)\| >= sum_{arrival u} 1/F(pi(u))；均匀版本为 \|image(pi)\|>=\|A\|/Fmax。 | WeightedArrivalImageLowerBoundFromFiberEnvelope |
| RawArrivalMassStillOpen | `false` | `false` | 仍未证明 terminal nonarrival 去除后 raw source-tagged arrival mass 足够大。 | ArrivalRawSourceMassAfterNonarrivalRemoval |
| HighFiberConcentrationRegistered | `true` | `false` | 若 weighted image 下界不足，压力必须集中在小 q/高纤维或重复碰撞上，登记为 dense low-carrier/PDEC/SAE return。 | HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn |
| CollisionReturnStillOpen | `false` | `false` | 已登记碰撞/重复支付 return，但尚未排斥或求和吸收。 | ArrivalCollisionOrDuplicatePaymentReturnLedger |
| DistinctArrivalQuotientReduced | `true` | `false` | DistinctArrivalQuotientDemandLowerBoundOrCollisionPDEC 被压成纤维 envelope、raw arrival mass、加权 image 下界和高纤维碰撞回流。 | ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalRawSourceMassAfterNonarrivalRemoval AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn |
| DistinctArrivalQuotientProved | `false` | `false` | 本步只关闭 quotient 纤维乘数纪律；不证明 image(pi) 已足够大，也不排斥高纤维碰撞。 | ArrivalRawSourceMassAfterNonarrivalRemoval AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、短块 SAE、raw arrival mass、terminal nonarrival 排斥、高纤维碰撞排斥、history switch 排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalRawSourceMassAfterNonarrivalRemoval AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalRawSourceMassAfterNonarrivalRemoval AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND ShortZeroBlockSingletonSAESummability AND ZeroBlockHistoryProjectionNoLossLedger AND StableLowCarrierPaymentTableOrHistorySwitchPDEC AND StableHistoryAPSuccessorDichotomyLedger AND SourceTaggedArrivalUnitIncidenceLedger AND ArrivalQuotientFiberMultiplicityEnvelopeLedger AND ArrivalRawSourceMassAfterNonarrivalRemoval AND WeightedArrivalImageLowerBoundFromFiberEnvelope AND HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn AND ArrivalCollisionOrDuplicatePaymentReturnLedger AND TerminalNonarrivalLargeStepEscapePDECOrSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书不证明 distinct arrival demand 已足够大。
- 本证书只证明 arrival quotient 的纤维 envelope 和加权 image 下界公式。
- `ArrivalRawSourceMassAfterNonarrivalRemoval` 与 `HighFiberArrivalCollisionPDECOrDenseLowCarrierReturn` 仍未闭合。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_arrival_quotient_fiber_router.py` | `386fdb314c9e21858d7c7e26fb6cf00a7f545c58aa94f263d4e867350afcad7c` |
| `docs/monograph/prime-matrix-firstbreak-arrival-candidate-actual-demand-router.json` | `cf9a8c0880194eb2054d4b2275f32664cad594c462e533543e80f9fbcf9807b5` |
| `docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.json` | `93c614915d07bfaebb5b3dca9ccb7720e877fe545e0b3bb157f7edb8abcf16e2` |
| `docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.json` | `2f378d9d29b8bf471ebc203240de29b701774395089998c1477c1af85c384d6f` |
| `docs/monograph/prime-matrix-no-loss-return-accounting-router.md` | `9215c5f0e251cd7170759c2cc51c02ddfc9fdfda469a0ff35f26b524ea6cc692` |
| `docs/monograph/prime-matrix-strict-active-prefix-product-fiber-multiplicity-router.md` | `08244ac0b2a2c56467ef6f22422ff3a2ebb103e7aed313edba16f8edde35f598` |
