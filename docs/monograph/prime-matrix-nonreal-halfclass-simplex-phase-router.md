# Prime Matrix Nonreal Half-class Simplex Phase Router

**状态：** `nonreal_zero_packet_routed_to_halfclass_simplex_rankone_phase_open`

本步继续下钻 `NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2`。删除主角色和二次角色后，非实 evaluation 向量不再是一个未解析残差，而是分裂为两个正交的二次半类 simplex。零列若存在，非实包必须在对应半类的单个 rank-one 方向提供至少 `(1-r_quad)T0` 的负投影。Cauchy 能量地板只是必要条件；真正剩余是 `NonrealHalfClassSimplexRankOneProjectionExclusionAtP2`。

```text
halfclass_simplex_geometry_closed=true
zero_requirement_after_quadratic_removal_closed=true
nonreal_energy_floor_closed=true
nonreal_rankone_projection_exclusion_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=NonrealHalfClassSimplexRankOneProjectionExclusionAtP2
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `nonreal residual packet` | `R_a=(P-1)theta_a(P)-T0(P)-chi_2(a)T_2(P)` |
| `zero-column requirement after quadratic removal` | `theta_a=0 implies R_a=-T0(P)-chi_2(a)T_2(P)` |
| `minimum required nonreal projection` | `min_a \|T0+chi_2(a)T_2\|/T0 = 1-\|T_2\|/T0` |
| `nonreal evaluation norm` | `\|\|w_a\|\|^2=P-3 after removing principal and quadratic characters` |
| `halfclass simplex inner product` | `<w_a,w_b>=P-3 if a=b; -2 if a!=b and chi_2(a)=chi_2(b); 0 if chi_2(a)!=chi_2(b)` |
| `capacity floor after quadratic removal` | `zero column forces E_nonreal >= T0^2*(1-\|T_2\|/T0)^2/(P-3)` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2` | NonrealHalfClassSimplexRankOneProjectionExclusionAtP2 | open | 非实零包不是无结构残差；它是两个正交二次半类 simplex 上的 rank-one 投影问题。 |
| `capacity-only after quadratic removal` | nonreal energy below floor would exclude zero columns | insufficient in current frontier | 能量超过地板仍不迫使能量集中到某个 residue evaluation 方向。 |
| `NonrealHalfClassSimplexRankOneProjectionExclusionAtP2` | exclude rank-one negative projection of size at least (1-r_quad)T0 in both halfclass simplexes | not proved in corpus | 这是当前解析 AP 路线的非实相位硬点。 |

## 3. 有限诊断

有限扫描只用于定位容量/相位分离，不作为无限证明输入。

```text
min_p=7
max_p=1000
prime_moduli_checked=165
capacity_false_positive_after_quadratic_removal_count=161
max_actual_negative_nonreal_projection_ratio=0.68968303124307
max_negative_ratio_modulus=73
max_nonreal_energy_to_zero_floor_ratio=4.868669254524807
max_energy_ratio_modulus=877
```

### 3.1 非实负投影最高记录

| P | required min | actual negative | slack | energy/floor | worst residue | chi |
| --- | --- | --- | --- | --- | --- | --- |
| `73` | `0.997004839219` | `0.689683031243` | `0.313312129538` | `2.393326750807` | `72` | `1` |
| `19` | `0.975233778200` | `0.585410377065` | `0.439355844735` | `1.399950211300` | `12` | `-1` |
| `43` | `0.952994404140` | `0.554757535507` | `0.398236868633` | `1.556098248417` | `15` | `1` |
| `31` | `0.897427662541` | `0.540062658337` | `0.546540202074` | `1.365768120236` | `24` | `-1` |
| `7` | `0.869729637136` | `0.500957976137` | `0.368771661000` | `0.379870124320` | `4` | `1` |
| `13` | `0.870422563924` | `0.498075198667` | `0.372347365258` | `1.211082548356` | `12` | `1` |
| `131` | `0.971245133093` | `0.482144508088` | `0.546610358819` | `2.500074639089` | `31` | `-1` |
| `199` | `0.983298305824` | `0.477528638495` | `0.505769667328` | `3.365369503196` | `9` | `1` |
| `101` | `0.995267166401` | `0.454356175948` | `0.540910990453` | `2.786860563088` | `30` | `1` |
| `97` | `0.986994176440` | `0.452094911076` | `0.560910912484` | `2.804673886963` | `14` | `-1` |
| `139` | `0.996610367856` | `0.445030536759` | `0.558359095385` | `2.236702497310` | `34` | `1` |
| `71` | `0.975793729412` | `0.443266182401` | `0.532527547011` | `2.032960010677` | `48` | `1` |

### 3.2 非实能量地板最高记录

| P | energy/floor | required min | actual negative | capacity false positive |
| --- | --- | --- | --- | --- |
| `877` | `4.868669254525` | `0.999094010293` | `0.246921394514` | `True` |
| `857` | `4.721646136288` | `0.999231061957` | `0.216972033903` | `True` |
| `991` | `4.624857318964` | `0.999535368646` | `0.230029478665` | `True` |
| `701` | `4.622152446626` | `0.996635146756` | `0.259770723291` | `True` |
| `661` | `4.584490833904` | `0.999275328396` | `0.313992667230` | `True` |
| `809` | `4.571680196926` | `0.997350052060` | `0.281586881348` | `True` |
| `947` | `4.570821753560` | `0.997424471852` | `0.244322782382` | `True` |
| `911` | `4.561831558889` | `0.998258642042` | `0.280858707727` | `True` |
| `881` | `4.527147310321` | `0.998736217688` | `0.241384632089` | `True` |
| `757` | `4.515961968288` | `0.998300895398` | `0.214201373053` | `True` |
| `907` | `4.504535730400` | `0.999694997948` | `0.197680321002` | `True` |
| `743` | `4.503912593630` | `0.997722320429` | `0.261643045303` | `True` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NonrealBranchImported` | `true` | `false` | 上一层确认二次半类余量之后仍必须处理非实零包相位。 | NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2 |
| `HalfclassSimplexGeometryClosed` | `true` | `true` | 删除主角色和二次角色后，evaluation 向量分裂为两个正交半类 simplex。 | none |
| `ZeroRequirementAfterQuadraticRemovalClosed` | `true` | `true` | 零列要求非实残差在对应半类方向提供至少 (1-r_quad)T0 的负投影。 | NonrealHalfClassSimplexRankOneProjectionExclusionAtP2 |
| `NonrealEnergyFloorNecessaryConditionClosed` | `true` | `true` | Cauchy 给出删除二次角色后的非实能量必要地板。 | none |
| `NonrealCapacityAloneSufficient` | `false` | `false` | 当前语料没有证明非实能量低于地板；能量高于地板也不是相位矛盾。 | NonrealHalfClassSimplexRankOneProjectionExclusionAtP2 |
| `NonrealRankOneProjectionExclusionProved` | `false` | `false` | 当前语料没有排斥两个半类 simplex 中的单方向同相负投影。 | NonrealHalfClassSimplexRankOneProjectionExclusionAtP2 |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合非实残差的几何和容量地板，不证明行/列命题。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale) AND NonrealHalfClassSimplexRankOneProjectionExclusionAtP2)) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明非实 rank-one 投影排斥、二次半类余量定理或行/列命题；它只把非实残差的几何结构和容量地板严格化。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-siegel-quadratic-halfclass-margin-router.json` | `11a035a79778851ceb5e852bb80587a455411b199bd6ec33208ce7b022aed2c4` |
| `docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.json` | `5c277929e4739d9e6829a9137d4115f974fc1df3260c7f31e57f6a7f3bc879db` |
| `docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json` | `5c1a653d7367788f233fb0ca0eee1147b75a2c1ae8c614919bb0a78be7e0a2c4` |
| `docs/monograph/claim-status-table.md` | `d625d9d62da1d4d3987df7b468639fee85c396671bc6601d4e67030a00553055` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-VIII.md` | `b7f072df8c7b33babe19ca00bc5a795030148041c1051ee884a2bdfc01e37988` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `8b72afec82e32a8e92e07e65c01e9ab01ae48c54c451de834e48d5779d25d337` |
