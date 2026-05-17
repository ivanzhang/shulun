# Prime Matrix Half-class Twist-pair Character Lock Router

**状态：** `ratio_fourier_lock_routed_to_quadratic_twist_pair_character_orbit_lock_open`

本步继续下钻 `HalfClassRatioFourierLockExclusionOrColumnCRTPDEC`。二次剩余子群 Q 上的每个非平凡频率都对应模 P 的一对二次扭曲 Dirichlet 角色 `chi, chi*chi_2`。平铺补偿要求 `chi(a0)*(T_chi+s*T_{chi chi_2})/2` 对所有配对角色同时等于同一个实目标 `theta_a0-c_a0`。因此最新硬点压成 `QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC`。

```text
subgroup_character_extension_closed=true
twist_pair_projection_identity_closed=true
orbit_lock_reformulation_closed=true
single_character_or_capacity_sufficiency_rejected=true
persistent_twist_pair_orbit_lock_excluded=false
row_column_unconditional_closed=false
next_direct_attack_target=QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `subgroup character extension` | `every nontrivial psi on Q has two extensions chi and chi*chi_2 to F_P^*` |
| `paired projection` | `F_psi(a0)=chi(a0)*(T_chi+s*T_{chi chi_2})/2 for a0 in H_s` |
| `orbit lock` | `flat compensation forces chi(a0)*(T_chi+s*T_{chi chi_2})/2 = theta_{a0}-c_{a0} for every psi!=1` |
| `explicit zero-packet form` | `each T_chi is a signed explicit-formula zero packet plus controlled finite terms` |
| `Parseval lock defect` | `sum_{psi!=1}\|chi(a0)*(T_chi+s*T_{chi chi_2})/2-(theta_{a0}-c_{a0})\|^2 = h*punctured_flatness` |
| `new hardpoint` | `exclude persistent quadratic-twist pair orbit lock, or register ColumnCRT/PDEC/moving-family` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `HalfClassRatioFourierLockExclusionOrColumnCRTPDEC` | QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC | sharpened but open | ratio-Fourier 全频率锁被改写为每一对二次扭曲 Dirichlet 角色的同一轨道锁。 |
| `Q-Fourier coefficients` | paired character projections T_chi+s*T_{chi chi_2} | closed as algebraic identity | Q 子群频率没有引入新黑箱；它们正是模 P 角色按二次扭曲配对后的投影。 |
| `persistent orbit lock` | explicit zero-packet phase coherence across all twist-pairs | not proved in corpus | 若反例持久，则不是单个角色异常，而是全部配对角色同步相位。 |
| `QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC` | exclude all-pair orbit lock or route to ColumnCRT/PDEC/moving-family | not proved in corpus | 这是当前非实 AP 分支的最新最窄接口。 |

## 3. 有限诊断

有限扫描只用于定位配对角色锁误差，不作为无限证明输入。

```text
min_p=7
max_p=1000
prime_moduli_checked=165
min_residue_halfclass_records_checked=330
max_parseval_identity_relative_error=1.83912923470421e-13
max_twist_pair_formula_abs_error=4.4958882062908615e-08
min_relative_lock_defect_to_target_energy=0.0030396846953873284
min_relative_lock_defect_modulus=7
max_lock_target_abs=256.5597214780484
max_lock_target_abs_modulus=751
```

### 3.1 最接近配对轨道锁的最小 residue 记录

| P | halfclass | puncture | target | rel lock defect | max pair error | max pair j | formula err |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `quadratic_residue` | `4` | `-4.886132354608` | `0.003039684695` | `0.269388774937` | `2` | `1.132e-14` |
| `11` | `quadratic_residue` | `5` | `-5.579668549390` | `0.173946022704` | `2.418501079565` | `2` | `1.676e-14` |
| `13` | `quadratic_nonresidue` | `2` | `-6.538567876237` | `0.242532145613` | `4.823854667463` | `4` | `4.197e-14` |
| `7` | `quadratic_nonresidue` | `6` | `-1.606397241094` | `0.313276028948` | `0.899117668689` | `1` | `8.663e-15` |
| `19` | `quadratic_nonresidue` | `12` | `-12.151974481295` | `0.582453685457` | `12.918426771128` | `7` | `1.887e-13` |
| `11` | `quadratic_nonresidue` | `10` | `-2.682476508047` | `0.636182295810` | `2.625654246626` | `4` | `1.311e-14` |
| `17` | `quadratic_residue` | `15` | `-6.888654457828` | `0.699077579976` | `8.208684758560` | `4` | `7.957e-14` |
| `31` | `quadratic_nonresidue` | `24` | `-17.580586265926` | `0.793837279977` | `22.298320473193` | `7` | `6.577e-13` |
| `13` | `quadratic_residue` | `12` | `-7.439645160306` | `1.738885299545` | `10.179182798444` | `1` | `5.281e-14` |
| `73` | `quadratic_residue` | `72` | `-51.382697609882` | `2.261015728816` | `150.459992410091` | `7` | `1.033e-11` |
| `43` | `quadratic_nonresidue` | `39` | `-13.302212678537` | `2.281233425544` | `28.957154865282` | `15` | `3.566e-12` |
| `23` | `quadratic_residue` | `13` | `-5.240290052116` | `2.418405317972` | `11.653917768963` | `3` | `2.317e-13` |

### 3.2 锁目标绝对值最高记录

| P | halfclass | puncture | |target| | target | max pair abs | max pair abs j |
| --- | --- | --- | --- | --- | --- | --- |
| `751` | `quadratic_residue` | `236` | `256.559721478048` | `-256.559721478048` | `2596.181100882925` | `116` |
| `911` | `quadratic_nonresidue` | `182` | `256.449417597771` | `-256.449417597771` | `3441.548875902141` | `427` |
| `967` | `quadratic_residue` | `660` | `248.102158820989` | `-248.102158820989` | `2982.493524842312` | `218` |
| `971` | `quadratic_residue` | `678` | `244.406022081199` | `-244.406022081199` | `3444.340050911394` | `53` |
| `997` | `quadratic_nonresidue` | `951` | `239.900653121012` | `-239.900653121012` | `3522.546405991060` | `249` |
| `947` | `quadratic_residue` | `202` | `231.901282415620` | `-231.901282415620` | `2972.772219276035` | `145` |
| `859` | `quadratic_nonresidue` | `715` | `229.428159041798` | `-229.428159041798` | `2668.361182576139` | `66` |
| `991` | `quadratic_nonresidue` | `388` | `228.341438798976` | `-228.341438798976` | `3352.015116440320` | `67` |
| `809` | `quadratic_nonresidue` | `775` | `228.272062424128` | `-228.272062424128` | `2856.915139193158` | `230` |
| `977` | `quadratic_nonresidue` | `778` | `227.872598436605` | `-227.872598436605` | `3685.256929838869` | `105` |
| `919` | `quadratic_nonresidue` | `394` | `225.944762034593` | `-225.944762034593` | `3850.660072271563` | `113` |
| `683` | `quadratic_nonresidue` | `448` | `220.942213306360` | `-220.942213306360` | `2237.427627296965` | `150` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousRatioFourierTargetImported` | `true` | `false` | 上一层把补偿平铺压成二次剩余子群上的全频率锁。 | HalfClassRatioFourierLockExclusionOrColumnCRTPDEC |
| `SubgroupCharacterExtensionClosed` | `true` | `true` | Q 上每个非平凡频率都有两条 Dirichlet 扩张，彼此相差二次角色。 | none |
| `TwistPairProjectionIdentityClosed` | `true` | `true` | Q-Fourier 系数精确等于 T_chi 与 T_chi chi2 的半类配对投影。 | none |
| `OrbitLockReformulationClosed` | `true` | `true` | 平铺补偿等价于全部二次扭曲角色对落在同一 a0 相位轨道。 | none |
| `SingleCharacterOrCapacitySufficiencyRejected` | `true` | `true` | 一个角色异常或总能量不够；持久反例需要全配对角色同步锁。 | QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC |
| `PersistentTwistPairOrbitLockExcluded` | `false` | `false` | 当前语料尚未排斥全部二次扭曲角色对的持久同步轨道锁。 | QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只完成角色配对化，不证明行/列命题。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale) AND QuadraticTwistPairCharacterOrbitLockExclusionOrColumnCRTPDEC)) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明持久二次扭曲配对角色轨道锁不可能，也没有排斥相应 ColumnCRT/PDEC/moving-family 出口；它只把 ratio-Fourier 锁接回标准 Dirichlet 角色投影语言。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-halfclass-ratio-fourier-lock-router.json` | `59af5b66fc0a0beec9168743d20a95339e546f96aed9185a2fed627ac137f184` |
| `docs/monograph/prime-matrix-nonreal-halfclass-compensation-variance-router.json` | `f7b6163f53b1799725cba43f852700d727e7629b528e31481497f3e9b86803a8` |
| `docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.json` | `3f007fcc90e0ac1d54f6f85bdf691c52468bdd688634e360c8a2193f22acfd77` |
| `docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json` | `11a035a79778851ceb5e852bb80587a455411b199bd6ec33208ce7b022aed2c4` |
| `docs/monograph/claim-status-table.md` | `96af5955bdee717dfee8e348a6eac1943e23bcde9b50e062b515a2b54f43a1a5` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-VIII.md` | `b7f072df8c7b33babe19ca00bc5a795030148041c1051ee884a2bdfc01e37988` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `0fabac34925098950b599baaf5a441732589fe8ce38d28cfeb4530f783d61c53` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `ac306e4e6cdc72a802e891ae34f905da5456731c823bd47b4d48cb45f15e1756` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `71803c9b02f87a33b262a0caf245a4efa29bb16c99c7a728884c89d2d711b31f` |
