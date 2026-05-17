# Prime Matrix Half-class Ratio Fourier Lock Router

**状态：** `halfclass_compensation_routed_to_ratio_fourier_lock_open`

本步继续下钻 `HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC`。固定假想缺孔 `a0` 后，同半类列可由二次剩余子群 ratio `u=a0^{-1}a` 统一参数化。半类方差超过单点地板的部分，精确等于非孔 ratio 列偏离最佳平铺补偿的二次量；而平铺补偿又等价于二次剩余子群上所有非平凡 Fourier 系数同时锁到同一值。因此最新硬点压成 `HalfClassRatioFourierLockExclusionOrColumnCRTPDEC`。

```text
ratio_normalization_closed=true
one_point_variance_excess_identity_closed=true
flat_compensator_fourier_lock_equivalence_closed=true
capacity_or_variance_only_sufficiency_rejected=true
persistent_ratio_fourier_lock_excluded=false
row_column_unconditional_closed=false
next_direct_attack_target=HalfClassRatioFourierLockExclusionOrColumnCRTPDEC
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `ratio normalization` | `Q=quadratic residues mod P; f_{a0}(u)=theta(P^2;P,a0*u), u in Q` |
| `punctured flat compensator` | `c_{a0}=(sum_{u!=1} f_{a0}(u))/(h-1), h=(P-1)/2` |
| `one-point variance excess identity` | `sum R_a^2 - (P-1)^2(theta_{a0}-mu)^2*h/(h-1) = (P-1)^2*sum_{u!=1}(f_{a0}(u)-c_{a0})^2` |
| `flat zero compensator` | `theta_{a0}=0 and zero excess iff f_{a0}(u)=c_{a0} for every u!=1` |
| `subgroup Fourier lock` | `flat profile iff every nontrivial Fourier coefficient on Q equals theta_{a0}-c_{a0}` |
| `Parseval lock defect` | `sum_{psi!=1} \|F_psi-(theta_{a0}-c_{a0})\|^2 = h*sum_{u!=1}(f_{a0}(u)-c_{a0})^2` |
| `new hardpoint` | `exclude persistent all-frequency ratio lock, or register it as ColumnCRT/PDEC/moving-family` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC` | HalfClassRatioFourierLockExclusionOrColumnCRTPDEC | sharpened but open | 补偿质量非平铺被改写为二次剩余 ratio 坐标上的全非平凡频率同相锁定排斥。 |
| `near-flat compensation` | all nontrivial Fourier coefficients on the QR subgroup nearly equal | closed as equivalent structure | 这不是随机噪声，而是高度刚性的乘法相位锁。 |
| `non-flat compensation` | positive Parseval lock defect / named compensation dispersion packet | registered return, not excluded | 非平铺本身也不是矛盾；它必须接入 PDEC/SAE/Rankin 或实际源熵预算。 |
| `HalfClassRatioFourierLockExclusionOrColumnCRTPDEC` | exclude persistent ratio-Fourier lock or route every persistent lock to ColumnCRT/PDEC | not proved in corpus | 这是半类补偿分支的最新最窄自足接口。 |

## 3. 有限诊断

有限扫描只用于定位 ratio-Fourier 锁误差，不作为无限证明输入。

```text
min_p=7
max_p=1000
prime_moduli_checked=165
puncture_records_checked=75952
min_residue_puncture_records_checked=330
max_one_point_variance_excess_identity_abs_error=0.180908203125
max_one_point_variance_excess_identity_relative_error=1.186787962344205e-13
near_flat_counts_relative_to_energy={'0.001': 1, '0.01': 65541, '0.05': 75861, '0.1': 75942}
near_flat_min_residue_counts_relative_to_energy={'0.001': 1, '0.01': 211, '0.05': 328, '0.1': 330}
min_punctured_flatness_relative_to_energy=0.00045571844422404815
min_punctured_flatness_relative_to_energy_modulus=7
min_residue_best_flatness_relative_to_energy=0.00045571844422404815
min_residue_best_flatness_modulus=7
```

### 3.1 全部 puncture 中最接近平铺的记录

| P | halfclass | puncture | is min | rel energy | rel flat | theta puncture | flat level | max dev/flat |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `quadratic_residue` | `4` | `True` | `0.000455718444` | `0.000455926218` | `2.397895272798` | `7.284027627407` | `0.021352428860` |
| `983` | `quadratic_nonresidue` | `543` | `True` | `0.003952374058` | `0.003968057305` | `787.283611138890` | `987.289559188300` | `0.183842108167` |
| `983` | `quadratic_nonresidue` | `396` | `False` | `0.003967335745` | `0.003983138191` | `805.784165256263` | `987.251802955407` | `0.202550343507` |
| `983` | `quadratic_nonresidue` | `454` | `False` | `0.003979651077` | `0.003995551980` | `1159.104914273346` | `986.530740202311` | `0.201967481543` |
| `983` | `quadratic_nonresidue` | `962` | `False` | `0.003991233623` | `0.004007227404` | `839.963427712194` | `987.182049358558` | `0.202493996269` |
| `983` | `quadratic_nonresidue` | `403` | `False` | `0.003991796489` | `0.004007794791` | `1140.796486697080` | `986.568104340222` | `0.201997705302` |
| `983` | `quadratic_nonresidue` | `560` | `False` | `0.003992861725` | `0.004008868583` | `842.578075538447` | `987.176713342586` | `0.202489685486` |
| `983` | `quadratic_nonresidue` | `924` | `False` | `0.003998141619` | `0.004014190923` | `851.393852342134` | `987.158721961354` | `0.202475150526` |
| `983` | `quadratic_nonresidue` | `232` | `False` | `0.003998387375` | `0.004014438656` | `851.817789274175` | `987.157856783942` | `0.202474451549` |
| `983` | `quadratic_nonresidue` | `498` | `False` | `0.003998707043` | `0.004014760895` | `1129.301251140824` | `986.591564004622` | `0.202016680598` |
| `983` | `quadratic_nonresidue` | `451` | `False` | `0.004001082018` | `0.004017154984` | `1125.123317752200` | `986.600090399293` | `0.202023576928` |
| `983` | `quadratic_nonresidue` | `270` | `False` | `0.004002504246` | `0.004018588665` | `859.122058401811` | `987.142950112253` | `0.202462408257` |

### 3.2 最小 residue puncture 中最接近平铺的记录

| P | halfclass | puncture | rel energy | rel flat | theta puncture | flat level | max dev/flat |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `quadratic_residue` | `4` | `0.000455718444` | `0.000455926218` | `2.397895272798` | `7.284027627407` | `0.021352428860` |
| `983` | `quadratic_nonresidue` | `543` | `0.003952374058` | `0.003968057305` | `787.283611138890` | `987.289559188300` | `0.183842108167` |
| `997` | `quadratic_nonresidue` | `951` | `0.004082827012` | `0.004099564826` | `753.912997379626` | `993.813650500638` | `0.221489620593` |
| `977` | `quadratic_residue` | `176` | `0.004122326361` | `0.004139390279` | `788.138647600081` | `976.835123627605` | `0.294924479756` |
| `967` | `quadratic_nonresidue` | `355` | `0.004180445786` | `0.004197995278` | `783.618512960326` | `971.945326977600` | `0.194685854958` |
| `971` | `quadratic_nonresidue` | `8` | `0.004204444271` | `0.004222196260` | `791.087224271206` | `970.762125333547` | `0.203708753108` |
| `937` | `quadratic_residue` | `200` | `0.004261392195` | `0.004279629374` | `755.254321786285` | `937.845440259324` | `0.186395423565` |
| `887` | `quadratic_nonresidue` | `61` | `0.004315081042` | `0.004333781661` | `728.903662311734` | `887.637503624853` | `0.181584859675` |
| `7` | `quadratic_nonresidue` | `6` | `0.004315579146` | `0.004334284092` | `6.278521424166` | `7.884918665260` | `0.065835279993` |
| `941` | `quadratic_residue` | `245` | `0.004430721527` | `0.004450440188` | `760.009661246209` | `939.732224665579` | `0.202958189393` |
| `929` | `quadratic_nonresidue` | `146` | `0.004439782394` | `0.004459581968` | `753.289903252381` | `930.219879920911` | `0.223659125764` |
| `991` | `quadratic_residue` | `122` | `0.004459159534` | `0.004479132701` | `799.818143992899` | `990.581349988740` | `0.192269207522` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousCompensationTargetImported` | `true` | `false` | 上一层把非实分支压成真实补偿质量非平铺或 ColumnCRT/PDEC。 | HalfClassCompensationMassNonconcentrationOrColumnCRTPDEC |
| `RatioNormalizationClosed` | `true` | `true` | 固定假想缺孔 a0 后，同半类被 a0^{-1} 归一化为二次剩余子群 Q。 | none |
| `OnePointVarianceExcessIdentityClosed` | `true` | `true` | 半类方差超过单点地板的部分，精确等于 punctured flatness 二次量。 | none |
| `FlatCompensatorFourierLockEquivalenceClosed` | `true` | `true` | 平铺补偿等价于 Q 上所有非平凡 Fourier 系数同时锁到同一值。 | none |
| `CapacityOrVarianceOnlySufficiencyRejected` | `true` | `true` | 方差超额只测量非平铺；零超额只给 Fourier 锁，都不是自动矛盾。 | HalfClassRatioFourierLockExclusionOrColumnCRTPDEC |
| `PersistentRatioFourierLockExcluded` | `false` | `false` | 当前语料尚未排斥真实素数向量的持久 ratio-Fourier 锁。 | HalfClassRatioFourierLockExclusionOrColumnCRTPDEC |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只关闭补偿平铺的 Fourier 等价与误出口，不证明行/列命题。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale) AND HalfClassRatioFourierLockExclusionOrColumnCRTPDEC)) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明持久 ratio-Fourier 锁不可能，也没有排斥相应 ColumnCRT/PDEC/moving-family 出口；它只把半类补偿平铺和非平铺的结构边界严格化。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-nonreal-halfclass-compensation-variance-router.json` | `f7b6163f53b1799725cba43f852700d727e7629b528e31481497f3e9b86803a8` |
| `docs/monograph/prime-matrix-nonreal-halfclass-simplex-phase-router.json` | `3f007fcc90e0ac1d54f6f85bdf691c52468bdd688634e360c8a2193f22acfd77` |
| `docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json` | `11a035a79778851ceb5e852bb80587a455411b199bd6ec33208ce7b022aed2c4` |
| `docs/monograph/claim-status-table.md` | `ed800ce3320aae84657aaa6a467dae651a825f6a73d58eecd9cb668e34e2a4c1` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-VIII.md` | `b7f072df8c7b33babe19ca00bc5a795030148041c1051ee884a2bdfc01e37988` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `b28e81f7a5d93bc048ce153a380c8514fbe2af6c8b562ece47b2d025190f9bfe` |
