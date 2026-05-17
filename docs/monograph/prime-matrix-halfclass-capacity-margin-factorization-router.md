# Prime Matrix Half-class Capacity Margin Factorization Router

**状态：** `halfclass_capacity_gate_factored_to_log_over_p_quadratic_projection_gap_open`

本步继续下钻 `QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2`。半类容量门等价于二次投影缺口 `1-|T_chi|/T0` 大于显式阈值 `4P log P/T0`。一旦主质量有 `T0>=c0(P)P^2` 的 Chebyshev 级下界，所需缺口只有 `4 log P/(c0(P)P)`。因此持久失败不再是普通半类偏置，而是二次投影接近主质量到 `logP/P` 级的极端异常。最新硬点压成 `QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale`。

```text
projection_gap_equivalence_closed=true
log_over_p_threshold_reduction_closed=true
quadratic_projection_gap_beats_threshold_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `capacity gate` | `min_s Theta_s(P)>2P log P` |
| `projection gap form` | `1-\|T_chi(P)\|/T0(P) > 4P log P / T0(P)` |
| `principal mass factorization` | `if T0(P)>=c0(P)P^2 then it suffices that 1-\|T_chi\|/T0 > 4 log P/(c0(P)P)` |
| `failure shape` | `capacity failure plus T0 lower bound forces \|T_chi\|/T0 >= 1-O(log P/P)` |
| `stronger existing input` | `QuadraticHalfClassSquareScaleBiasMarginTheorem gives this gate if its eta(P) beats 4P log P/T0(P)` |
| `new hardpoint` | `prove QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale or register ultra-near-one quadratic projection as ColumnCRT/PDEC` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2` | QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale | equivalent reformulation | 半类质量击穿单 residue 容量等价于二次投影缺口击穿显式阈值。 |
| `ChebyshevPrincipalMassLowerBoundAtP2` | turn threshold into O(log P/P) | standard but not re-proved in this certificate | 一旦主质量 T0 有 P^2 级下界，容量门所需二次缺口只有 logP/P 级。 |
| `QuadraticHalfClassSquareScaleBiasMarginTheorem` | QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale | stronger than needed for this gate if eta(P)>4PlogP/T0(P) | 原 Siegel 半类余量门可作为更强输入，但本步暴露所需余量其实很小。 |
| `capacity failure` | ultra-near-one quadratic projection defect | not excluded in corpus | 若反例链持久，则二次角色投影必须接近主质量到 logP/P 级别。 |

## 3. 有限诊断

有限扫描只用于定位投影缺口阈值，不作为无限证明输入。

```text
min_p=7
max_p=1000
prime_moduli_checked=165
min_actual_gap_to_required_gap_ratio=0.6227695609190618
min_ratio_modulus=7
min_actual_gap_to_required_gap_ratio_for_P_ge_17=1.2842365118870342
max_required_projection_gap=1.3965512955594221
max_required_projection_gap_modulus=7
max_required_projection_gap_for_P_ge_17=0.717505272222736
capacity_gate_failure_moduli=[7, 11, 13]
```

### 3.1 投影缺口最接近阈值的记录

| P | actual gap | required gap | ratio | T0/P^2 | required/(logP/P) | capacity pass |
| --- | --- | --- | --- | --- | --- | --- |
| `7` | `0.869729637136` | `1.396551295559` | `0.622769560919` | `0.796210393516` | `5.023797770756` | `false` |
| `13` | `0.870422563924` | `0.892945253832` | `0.974777076409` | `0.883833788829` | `4.525737814688` | `false` |
| `11` | `0.987452384433` | `1.007981920298` | `0.979633031653` | `0.865057100552` | `4.623972218076` | `false` |
| `17` | `0.921446468060` | `0.717505272223` | `1.284236511887` | `0.929105972741` | `4.305213955517` | `true` |
| `19` | `0.975233778200` | `0.673766999309` | `1.447434764838` | `0.920024119595` | `4.347712103203` | `true` |
| `23` | `0.962053481683` | `0.581129808231` | `1.655488099315` | `0.938350320664` | `4.262800269701` | `true` |
| `31` | `0.897427662541` | `0.467168038485` | `1.920995420516` | `0.948470543054` | `4.217316003424` | `true` |
| `29` | `0.943942187851` | `0.486606385670` | `1.939847514645` | `0.954476987803` | `4.190776782589` | `true` |
| `37` | `0.940681896761` | `0.407018355325` | `2.311153500709` | `0.959095576312` | `4.170595818386` | `true` |
| `43` | `0.952994404140` | `0.362461348855` | `2.629230419050` | `0.965286592998` | `4.143847049173` | `true` |
| `41` | `0.985275910043` | `0.372403043463` | `2.645724645213` | `0.972869905830` | `4.111546647737` | `true` |
| `47` | `0.991673749244` | `0.339052997365` | `2.924834043502` | `0.966433386115` | `4.138929860524` | `true` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousCapacityGateImported` | `true` | `true` | 上一层把零支撑退化压成半类总质量超过单 residue 容量。 | QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2 |
| `ProjectionGapEquivalenceClosed` | `true` | `true` | 容量门等价于 1-\|T_chi\|/T0 > 4PlogP/T0。 | none |
| `LogOverPThresholdReductionClosed` | `true` | `true` | 给定任意 T0>=c0(P)P^2，下游阈值就是 4logP/(c0(P)P)。 | ChebyshevPrincipalMassLowerBoundAtP2 |
| `FixedPositiveQuadraticMarginSufficesEventually` | `true` | `true` | 任意固定正二次投影缺口都会在大 P 上远强于容量门。 | finite base plus ChebyshevPrincipalMassLowerBoundAtP2 |
| `QuadraticProjectionGapBeatsThresholdProved` | `false` | `false` | 当前语料尚未自足证明二次投影缺口击穿 4PlogP/T0。 | QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只做等价分解与阈值缩小，不证明行/列命题。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((ChebyshevPrincipalMassLowerBoundAtP2 AND (QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale OR QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale)))) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明二次投影缺口击穿阈值；它只把容量门化为一个 `logP/P` 级投影缺口问题。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-halfclass-single-residue-capacity-router.json` | `361e53166d6e76a3f47cd32b3085772db0aa75156883bb6dde9bf06042e0d31a` |
| `docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json` | `11a035a79778851ceb5e852bb80587a455411b199bd6ec33208ce7b022aed2c4` |
| `docs/monograph/claim-status-table.md` | `f705e7704b696438d9184061dcf0de261bf4639cdbd8302e0a9c005bea3bef96` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `7c4df6d956e7df9940dedcc073679f1c91a10d9f55827cf14c7a8070fe03f62a` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `85a1684e29348f69ad6d8e968acc63fb75cfb61a7343abfd3a1032d5323ab8d1` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `5afc3f1b4c1a3fc08457ce17071b0f233d25d93107b08cbbe15cbd09d5eaa502` |
