# Prime Matrix Nonreal Half-class Compensation Variance Router

**状态：** `nonreal_halfclass_simplex_sharpened_to_compensation_variance_open`

本步继续下钻 `NonrealHalfClassSimplexRankOneProjectionExclusionAtP2`。在每个二次半类内，非实残差恰为 `R_a=(P-1)(theta_a-mu_s)`，所以自动中心化。零列若出现，不仅要求一个 residue 给出 rank-one 负投影，还要求同半类其余 residue 承担等量正补偿。Cauchy 方差地板是尖锐必要条件，平铺补偿等号态说明纯容量论证不能闭合；最新硬点压成 `HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC`。

```text
halfclass_centering_identity_closed=true
zero_column_compensation_mass_closed=true
sharp_one_hole_variance_floor_closed=true
capacity_only_sufficiency_rejected=true
actual_prime_compensation_nonconcentration_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `halfclass mean after removing principal/quadratic` | `mu_s=(T0+sT2)/(P-1), s in {+1,-1}` |
| `centered nonreal residual` | `R_a=(P-1)(theta_a-mu_s) for chi_2(a)=s` |
| `halfclass centering` | `sum_{chi_2(a)=s} R_a=0` |
| `zero column compensation mass` | `theta_a=0 implies R_a=-(P-1)mu_s and sum_{b!=a, chi_2(b)=s} R_b=(P-1)mu_s` |
| `sharp one-hole variance floor` | `sum_{chi_2(b)=s} R_b^2 >= ((P-1)mu_s)^2*h/(h-1), h=(P-1)/2` |
| `flat extremizer` | `equality occurs when all non-hole residues in the same halfclass have theta_b=mu_s*h/(h-1)` |
| `new hardpoint` | `exclude the flat/near-flat compensation profile by actual prime phase, or register ColumnCRT/PDEC` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `NonrealHalfClassSimplexRankOneProjectionExclusionAtP2` | HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC | sharpened but open | rank-one 负投影被改写为同半类一个缺孔与其余列的等量正补偿。 |
| `capacity-only variance argument` | sharp one-hole floor is necessary and convexly sharp | closed as insufficient | 方差地板达到或超过并不排除零列；平铺补偿向量本身非负且满足半类中心化。 |
| `HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC` | prove true prime-induced compensation cannot remain flat without persistent CRT phase defect | not proved in corpus | 这是非实 AP 分支的最新最窄自足接口。 |
| `persistent flat compensation` | ColumnCRT/PDEC or moving-family SAE/Rankin return | registered return, not excluded | 若真实反例链复现同一补偿相位，应形成可审查的持久相位缺陷。 |

## 3. 有限诊断

有限扫描只用于定位补偿/容量误差形态，不作为无限证明输入。

```text
min_p=7
max_p=1000
prime_moduli_checked=165
halfclass_records_checked=330
max_halfclass_centering_abs_error=4.782123141922057e-08
max_half_mass_identity_abs_error=5.820766091346741e-11
capacity_false_positive_for_zero_floor_count=297
max_actual_negative_to_zero_projection_ratio=0.6876234883389729
max_deficit_ratio_modulus=73
max_deficit_ratio_halfclass=quadratic_residue
max_halfclass_square_to_zero_floor_ratio=2.618556739497602
max_variance_ratio_modulus=877
flat_zero_lift_ratio_range=[1.0020120724346075, 1.5]
```

### 3.1 缺孔比例最高记录

| P | halfclass | min residue | actual/zero | min theta | zero projection | square/floor |
| --- | --- | --- | --- | --- | --- | --- |
| `73` | `quadratic_residue` | `72` | `0.687623488339` | `22.693950973318` | `5230.753302770585` | `1.541893224248` |
| `43` | `quadratic_residue` | `15` | `0.582120454325` | `16.923311929235` | `1700.918622086609` | `1.235000091999` |
| `7` | `quadratic_residue` | `4` | `0.575992762287` | `2.397895272798` | `33.931901055223` | `0.332776131292` |
| `13` | `quadratic_residue` | `12` | `0.572222296744` | `4.634728988230` | `130.013199461820` | `0.896816102195` |
| `19` | `quadratic_nonresidue` | `12` | `0.571262366588` | `8.106816038947` | `340.354280401770` | `0.516419029947` |
| `31` | `quadratic_nonresidue` | `24` | `0.489820613114` | `17.090547675268` | `1004.972845703955` | `0.430385033582` |
| `199` | `quadratic_residue` | `9` | `0.485639643298` | `100.518771236699` | `38694.110938993435` | `1.782895590820` |
| `19` | `quadratic_residue` | `6` | `0.469308314478` | `9.549594449972` | `323.903133945535` | `0.829740813194` |
| `131` | `quadratic_nonresidue` | `31` | `0.468668021506` | `71.435757721535` | `17478.053043458534` | `1.318714745703` |
| `101` | `quadratic_residue` | `30` | `0.456516793969` | `54.650723050811` | `10055.641544094615` | `1.510400218691` |
| `71` | `quadratic_residue` | `48` | `0.454262175540` | `37.722402625150` | `4838.528805243467` | `1.159982793056` |
| `97` | `quadratic_nonresidue` | `14` | `0.446290535120` | `54.254334700544` | `9406.406177974673` | `1.423194230043` |

### 3.2 半类方差地板最高记录

| P | halfclass | square/floor | actual/zero | flat lift | capacity false positive |
| --- | --- | --- | --- | --- | --- |
| `877` | `quadratic_nonresidue` | `2.618556739498` | `0.246697888766` | `1.002288329519` | `True` |
| `661` | `quadratic_residue` | `2.483179393237` | `0.314220373812` | `1.003039513678` | `True` |
| `857` | `quadratic_nonresidue` | `2.437580399484` | `0.217139000342` | `1.002341920375` | `True` |
| `787` | `quadratic_nonresidue` | `2.420224774598` | `0.210034490524` | `1.002551020408` | `True` |
| `757` | `quadratic_nonresidue` | `2.407997329453` | `0.213838039856` | `1.002652519894` | `True` |
| `743` | `quadratic_residue` | `2.404296076357` | `0.262240344779` | `1.002702702703` | `True` |
| `983` | `quadratic_residue` | `2.392623056260` | `0.178806247608` | `1.002040816327` | `True` |
| `691` | `quadratic_residue` | `2.388135011394` | `0.198573354278` | `1.002906976744` | `True` |
| `911` | `quadratic_residue` | `2.373724366258` | `0.223502098348` | `1.002202643172` | `True` |
| `991` | `quadratic_nonresidue` | `2.373536297813` | `0.229922649393` | `1.002024291498` | `True` |
| `491` | `quadratic_nonresidue` | `2.367695272058` | `0.283440164991` | `1.004098360656` | `True` |
| `997` | `quadratic_residue` | `2.364325748151` | `0.209053958707` | `1.002012072435` | `True` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousNonrealSimplexTargetImported` | `true` | `false` | 上一层把非实零点包压成半类 simplex 的单方向负投影排斥。 | NonrealHalfClassSimplexRankOneProjectionExclusionAtP2 |
| `HalfclassCenteringIdentityClosed` | `true` | `true` | 每个二次半类内的非实残差严格中心化，和为零。 | none |
| `ZeroColumnCompensationMassClosed` | `true` | `true` | 零列强制同半类其它 residue 总正补偿质量等于缺失的主/二次质量。 | none |
| `SharpOneHoleVarianceFloorClosed` | `true` | `true` | 尖孔方差地板由 Cauchy 给出且有平铺补偿等号态，因此只是必要条件。 | none |
| `CapacityOnlySufficiencyRejected` | `true` | `true` | 纯方差/容量不能排除零列；必须加入真实素数相位或 CRT 持久缺陷机制。 | HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC |
| `ActualPrimeCompensationNonconcentrationProved` | `false` | `false` | 当前语料还没有证明真实素数诱导的补偿不能近似平铺在同一半类。 | HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只关闭非实分支的补偿恒等式和误出口，不证明行/列命题。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale) AND HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC)) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明真实素数补偿质量的非平铺定理、二次半类余量定理或行/列命题；它只关闭非实半类分支中的中心化、补偿、尖锐方差地板和容量误出口。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.json` | `3f007fcc90e0ac1d54f6f85bdf691c52468bdd688634e360c8a2193f22acfd77` |
| `docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json` | `11a035a79778851ceb5e852bb80587a455411b199bd6ec33208ce7b022aed2c4` |
| `docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.json` | `5c277929e4739d9e6829a9137d4115f974fc1df3260c7f31e57f6a7f3bc879db` |
| `docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json` | `5c1a653d7367788f233fb0ca0eee1147b75a2c1ae8c614919bb0a78be7e0a2c4` |
| `docs/monograph/claim-status-table.md` | `71a396ed2e0b4ed59045abb76538dcbf287349ea62c7336c3ed60f07ff6dacfd` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-VIII.md` | `b7f072df8c7b33babe19ca00bc5a795030148041c1051ee884a2bdfc01e37988` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `283c40bd6e56ae5a8255812806b9fd23995ff2dcae97cda6e349a9fdb077fa4a` |
