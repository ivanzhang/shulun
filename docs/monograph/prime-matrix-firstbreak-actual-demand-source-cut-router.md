# Prime Matrix 首破裂 actual demand 源侧切口证书

**状态：** `firstbreak_actual_demand_cut_to_source_amplification_open`

Actual demand 的源侧下界被切开：首破裂释放非空只给出单位需求 D_y>=1，不足以超过 AP exact-envelope；真正需要证明的是释放质量沿反例链放大到可与 H 比较，并且这些压力非循环地注入同一低 carrier AP table。若无法放大，则只能登记为 singleton/sparse SAE；若无法注入，则回流到高秩、moving carrier、PDEC 或 SAE 出口。

```text
firstbreak_release_set_imported=true
unit_release_demand_lower_bound_closed=true
unit_demand_not_gap_sufficient=true
no_envelope_recycling_guard=true
release_mass_amplification_proved=false
low_carrier_payment_injection_proved=false
actual_low_carrier_row_incidence_demand_proved=false
row_column_unconditional_closed=false
```

## 1. 源侧切口

上一层已经给出 AP exact-envelope；因此 actual demand 下界必须来自反例链的源侧，而不能从 AP table 的
容量饱和反推。首破裂分裂只保证：若平方锚分支不接管，则存在首个非零行 `y`，且释放列集非空。

```text
R_y != empty  =>  D_y >= 1.
```

这是严格的 actual demand 下界，但它只是单位下界。

## 2. 为什么单位需求不够

AP exact-envelope 中，任意一个低 carrier residue cell `(q,a)` 在 `I_y` 中最多有 `ceil(H/q)` 个发生位。
只要该 cell 与区间相交，envelope 已能容纳一个单位事件。因此

```text
D_y >= 1
```

不能推出

```text
D_y > U_T(I_y).
```

容量矛盾需要的是源侧释放质量放大，例如沿反例链强制产生可与 `H=P-y` 比较的一族行发生需求；若没有放大，
该释放只能作为 singleton/sparse SAE 计费。

## 3. 新硬点

因此

```text
ActualLowCarrierRowIncidenceDemandLowerBound
  -> FirstBreakReleaseMassAmplificationOrSingletonSAE
  AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse
```

- `FirstBreakReleaseMassAmplificationOrSingletonSAE`：证明首破裂释放不是孤立单位事件，而会沿反例链放大；若不放大，则进入 singleton/sparse SAE。
- `LowCarrierActualPaymentInjectionWithoutEnvelopeReuse`：证明放大的源侧压力确实注入同一低 carrier AP table，且证明不使用 AP envelope 饱和本身。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ActualDemandImported | `true` | `false` | 上一层 AP exact-envelope 证书把容量比较剩余压到 actual row-incidence demand 下界。 | ActualLowCarrierRowIncidenceDemandLowerBound |
| FirstBreakReleaseSetImported | `true` | `true` | early-to-square 分裂已证明：若 square-anchor 分支不接管，则首破裂行 y 有非空释放列集。 | FirstBreakUnitReleaseDemandLowerBound |
| UnitReleaseDemandLowerBoundClosed | `true` | `true` | 释放列非空只给出 D_y>=1 的单位 actual demand；这是源侧事实，不使用 AP envelope。 | FirstBreakUnitReleaseDemandLowerBound |
| UnitDemandNotGapSufficient | `true` | `true` | 单位需求不足以超过 AP envelope：单个 residue cell 已可提供至少一个发生位，因此不能由 D_y>=1 得到容量矛盾。 | FirstBreakReleaseMassAmplificationOrSingletonSAE |
| NoEnvelopeRecyclingGuard | `true` | `true` | actual demand 下界必须来自首破裂/零行源侧，不能从 AP table 接近饱和反推需求；否则论证循环。 | NoAPEnvelopeRecyclingDemandGuard |
| PaymentInjectionSeparated | `true` | `false` | 即使源侧释放质量被放大，还必须证明这些压力注入同一低 carrier AP table；若不能注入，则回流到高秩、moving carrier、PDEC 或 SAE。 | LowCarrierActualPaymentInjectionWithoutEnvelopeReuse |
| ActualDemandReduced | `true` | `false` | ActualLowCarrierRowIncidenceDemandLowerBound 被切成源侧释放质量放大和非循环支付注入两项。 | FirstBreakReleaseMassAmplificationOrSingletonSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse |
| ActualDemandProved | `false` | `false` | 本步没有证明 Ω(H) 或超 envelope 的 actual demand；只排除了把单位释放误当成容量矛盾的路线。 | FirstBreakReleaseMassAmplificationOrSingletonSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse |
| RowColumnUnconditionalClosureReached | `false` | `false` | 行/列命题仍需 square-anchor 输入、释放质量放大、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。 | (NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND FirstBreakReleaseMassAmplificationOrSingletonSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch |

## 5. 新活动基

inverse-alignment 回流分支更新为：

```text
NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND FirstBreakReleaseMassAmplificationOrSingletonSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion
```

合并 exact-UV/source-rank 前沿后的活动基：

```text
((NoZeroRowAtXEqualsP_PlusOneRowAfterSquare AND FirstBreakReleaseMassAmplificationOrSingletonSAE AND LowCarrierActualPaymentInjectionWithoutEnvelopeReuse AND LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC AND DenseLowCarrierResidueTablePDECExclusion AND SparseLowCarrierResidueCellSAESummability AND LowCarrierNonpersistentSparseSAESummability AND HighCarrierRankDeficitCapacityBoundOrSingletonSAE AND NonreplaySparseFirstBreakSAESummability AND MovingCarrierPhaseSlipPDECExclusion) OR (AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 诚实边界

- 本证书不证明 actual demand 下界已经足以超过 AP envelope。
- 本证书只关闭单位释放下界与非循环需求来源纪律。
- 最新主攻变为释放质量放大或 singleton/sparse SAE 排斥，以及低 carrier actual payment 注入。
- 行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_firstbreak_actual_demand_source_cut_router.py` | `7759dc15959ad468de284efcfa462b140a5bbc16c6932c91a171c5cc6b408b26` |
| `docs/monograph/prime-matrix-firstbreak-low-carrier-ap-envelope-router.json` | `2f378d9d29b8bf471ebc203240de29b701774395089998c1477c1af85c384d6f` |
| `docs/monograph/prime-matrix-firstbreak-low-carrier-residue-ap-router.json` | `03248e0defb00a2419e713cb229d804f725d8c44e86a277d51a613abb5d6b94c` |
| `docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.json` | `747ab2d8f1f4569ed1bd9e00f868e26f33a7a22c8310e0776580ee8ad571dad9` |
| `docs/monograph/prime-matrix-early-to-square-phase-transfer-split-router.json` | `54575ef141b22648dd85608f8db9144e24ef013b69df9a130147857c28840c2f` |
| `docs/monograph/prime-matrix-early-zero-phase-defect-schema-router.json` | `b38bc33611a384f5d925c2005c5e9df9cff5fee0af0b8bc5da4acc8bff88b681` |
