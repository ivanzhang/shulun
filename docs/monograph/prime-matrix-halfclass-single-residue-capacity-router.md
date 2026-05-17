# Prime Matrix Half-class Single-residue Capacity Router

**状态：** `zero_support_degeneracy_routed_to_halfclass_single_residue_capacity_gap_open`

本步继续下钻 `PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC`。若同一二次半类除缺孔外全无 `P^2` 内素数到达，则该半类全部 Chebyshev 质量只能落在一个 residue。而单个 residue 在 `P^2` 前至多有 `P` 个候选位置，因此权重不超过 `2P log P`。所以只要证明 `min_s Theta_s(P)>2P log P`，即 `T0(P)*(1-|T_chi(P)|/T0(P))>4P log P`，就排除该退化。最新硬点压成 `QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2`。

```text
single_residue_deterministic_capacity_closed=true
zero_support_degeneracy_implies_capacity_failure_closed=true
quadratic_halfclass_mass_beats_single_residue_capacity_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `half-class mass` | `Theta_s(P)=sum_{chi_P(a)=s} theta(P^2;P,a)=(T0+s*T_chi)/2` |
| `single residue deterministic capacity` | `theta(P^2;P,a)<=P*log(P^2)=2P log P` |
| `zero-support degeneracy implication` | `punctured half-class zero support implies Theta_s(P)=theta(P^2;P,a0)<=2P log P` |
| `capacity exclusion gate` | `min_s Theta_s(P)>2P log P excludes punctured half-class zero-support degeneracy` |
| `quadratic projection form` | `T0(P)*(1-\|T_chi(P)\|/T0(P))>4P log P` |
| `new hardpoint` | `prove QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2 or route capacity failure to ColumnCRT/PDEC` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC` | QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2 | sharpened but open | 半类全零支撑若存在，则对应半类质量不能超过单 residue 的确定性容量。 |
| `single-residue capacity` | theta(P^2;P,a)<=2P log P | closed as counting bound | 一个 residue 在 P^2 前至多有 P 个候选位置，每个素数权重至多 2 log P。 |
| `QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2` | T0(P)*(1-\|T_chi\|/T0)>4P log P | not proved in corpus | 剩余是二次半类总 Chebyshev 质量必须击穿单 residue 容量。 |
| `capacity failure` | ColumnCRT/PDEC/moving-family registration | not proved in corpus | 若容量门失败，则反例链已被压成半类总质量过低的显式二次角色缺陷。 |

## 3. 有限诊断

有限扫描只用于定位容量门风险，不作为无限证明输入。

```text
min_p=7
max_p=1000
prime_moduli_checked=165
min_mass_to_capacity_ratio=0.6227695609190617
min_mass_to_capacity_modulus=7
min_mass_to_capacity_ratio_for_P_ge_17=1.284236511887034
deterministic_capacity_failures_found=3
deterministic_capacity_failure_moduli=[7, 11, 13]
actual_support_degeneracies_found=0
```

### 3.1 半类质量最接近单 residue 容量的记录

| P | dangerous halfclass | min mass | capacity | ratio | surplus | actual support surplus | margin surplus |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `quadratic_residue` | `16.965950527612` | `27.242742086774` | `0.622769560919` | `-10.276791559163` | `9.526391218478` | `-0.526821658423` |
| `13` | `quadratic_residue` | `65.006599730910` | `66.688683294000` | `0.974777076409` | `-1.682083563090` | `46.735416836341` | `-0.022522689908` |
| `11` | `quadratic_residue` | `51.679263144938` | `52.753696001564` | `0.979633031653` | `-1.074432856626` | `39.356078800159` | `-0.020529535865` |
| `17` | `quadratic_residue` | `123.709544761687` | `96.329253697911` | `1.284236511887` | `27.380291063776` | `103.781944195591` | `0.203941195837` |
| `19` | `quadratic_residue` | `161.951566972767` | `111.888681208325` | `1.447434764838` | `50.062885764443` | `134.622201084899` | `0.301466778891` |
| `23` | `quadratic_residue` | `238.775574557278` | `144.232733932741` | `1.655488099315` | `94.542840624537` | `211.540844852473` | `0.380923673452` |
| `31` | `quadratic_residue` | `408.993769023370` | `212.907206678079` | `1.920995420516` | `196.086562345291` | `365.528854279146` | `0.430259624056` |
| `29` | `quadratic_residue` | `378.858345918593` | `195.303158139215` | `1.939847514645` | `183.555187779378` | `340.499091529600` | `0.457335802182` |
| `37` | `quadratic_residue` | `617.558532518893` | `267.207925535673` | `2.311153500709` | `350.350606983221` | `568.937585364807` | `0.533663541436` |
| `43` | `quadratic_residue` | `850.459311043305` | `323.463209949646` | `2.629230419050` | `526.996101093658` | `792.297044488978` | `0.590533055285` |
| `41` | `quadratic_residue` | `805.657309369579` | `304.512909469753` | `2.645724645213` | `501.144399899826` | `751.901255665623` | `0.612872866580` |
| `47` | `quadratic_residue` | `1058.538021130940` | `361.913874560746` | `2.924834043502` | `696.624146570194` | `1000.455552182785` | `0.652620751879` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousZeroSupportDegeneracyImported` | `true` | `true` | 上一层把精确轨道锁压成 punctured 半类全零支撑退化。 | PuncturedHalfClassZeroSupportDegeneracyExclusionOrColumnCRTPDEC |
| `SingleResidueDeterministicCapacityClosed` | `true` | `true` | 固定 residue 在 P^2 前的 theta 权重至多 2P log P。 | none |
| `ZeroSupportDegeneracyImpliesCapacityFailureClosed` | `true` | `true` | 若同半类除缺孔外全零，则该半类总质量必须不超过单 residue 容量。 | none |
| `FiniteBaseSupportDegeneracyAbsentInDiagnostic` | `true` | `false` | 有限诊断中 P<=13 的确定性容量门不全通过，但实际支撑退化为零；有限读数不替代无限证明。 | none |
| `QuadraticHalfClassMassBeatsSingleResidueCapacityProved` | `false` | `false` | 当前语料尚未自足证明每个二次半类总质量都超过 2P log P。 | QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2 |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只把零支撑退化压成半类质量容量门，不证明行/列命题。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale) AND QuadraticHalfClassMassBeatsSingleResidueCapacityAtP2)) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明二次半类总质量必然超过单 residue 容量；它只给出从零支撑退化到该容量门的严格蕴含。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-halfclass-log-independence-degeneracy-router.json` | `dc8218de70bb40817415b17c0869aac99b13c14f95dca566455ff73658ca8757` |
| `docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json` | `11a035a79778851ceb5e852bb80587a455411b199bd6ec33208ce7b022aed2c4` |
| `docs/monograph/claim-status-table.md` | `f705e7704b696438d9184061dcf0de261bf4639cdbd8302e0a9c005bea3bef96` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `7c4df6d956e7df9940dedcc073679f1c91a10d9f55827cf14c7a8070fe03f62a` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `85a1684e29348f69ad6d8e968acc63fb75cfb61a7343abfd3a1032d5323ab8d1` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `5afc3f1b4c1a3fc08457ce17071b0f233d25d93107b08cbbe15cbd09d5eaa502` |
