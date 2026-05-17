# Prime Matrix Quadratic Projection Large Splitting Router

**状态：** `quadratic_projection_gap_routed_to_large_prime_splitting_mass_open`

本步继续下钻 `QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale`。二次投影缺口阈值等价于少数二次半类质量 `min_s Theta_s(P)>2P log P`。把 `Theta_s` 精确拆为低 CRT 层 `ell<P` 与大素数分裂层 `P<ell<=P^2` 后，低 CRT 层总质量由平凡估计即被压到 `<=P log P`，不超过所需阈值的一半。因此低轮/有限 CRT 相位不能单独闭合本接口；真正剩余硬点是大素数二次半类分裂质量，或把 ultra-near-one 投影缺陷登记为大分裂荒漠/Siegel/ColumnCRT-PDEC 出口。

```text
minority_mass_equivalence_closed=true
low_crt_capacity_insufficiency_closed=true
large_prime_quadratic_splitting_mass_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale
pdec_fallback_target=UltraNearOneQuadraticProjectionDefectToLargeSplittingPDECOrSiegelPacket
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `minority mass form` | `Delta(P)=1-\|T_chi\|/T0=2 min_s Theta_s(P)/T0(P)` |
| `capacity threshold` | `Delta(P)>4P log P/T0(P) iff min_s Theta_s(P)>2P log P` |
| `low CRT layer` | `L_s(P)=sum_{ell<P, chi_P(ell)=s} log ell` |
| `large splitting layer` | `G_s(P)=sum_{P<ell<=P^2, chi_P(ell)=s} log ell` |
| `exact split` | `Theta_s(P)=L_s(P)+G_s(P)` |
| `elementary low cap` | `L_+(P)+L_-(P)=theta(P-1) <= P log P = (2P log P)/2 < 2P log P` |
| `failure shape` | `if the capacity gate fails then some s has L_s(P)+G_s(P)<=2P log P; the low CRT layer can be fully absorbed by this allowance` |
| `new hardpoint` | `prove min_s G_s(P)>2P log P, or register the persistent large-splitting desert as PDEC/Siegel packet` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale` | minority mass threshold | equivalent reformulation | 投影缺口击穿阈值等价于少数二次半类 Chebyshev 质量超过 2PlogP。 |
| `low CRT / ell<P phase constraints` | capacity-insufficient | closed negative route | 整个低 CRT 层总质量至多 PlogP，不能单独推出容量门，也不能强制低相位矛盾。 |
| `large prime splitting layer P<ell<=P^2` | LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale | new direct target | 剩余有效质量必须来自大素数在二次半类中的分裂；这不是有限低轮 CRT 可直接闭合的对象。 |
| `persistent ultra-near-one projection` | UltraNearOneQuadraticProjectionDefectToLargeSplittingPDECOrSiegelPacket | named fallback | 若大素数少数半类长期只有 O(PlogP) 质量，则登记为大分裂荒漠/Siegel 包/ColumnCRT-PDEC 出口。 |

## 3. 有限诊断

有限扫描只用于定位分裂质量硬点，不作为无限证明输入。

```text
min_p=7
max_p=1000
prime_moduli_checked=165
capacity_gate_failure_moduli=[7, 11, 13]
large_splitting_gate_failure_moduli=[7, 11, 13]
min_total_minority_to_required_ratio=0.6227695609190618
min_total_minority_to_required_ratio_for_P_ge_17=1.284236511887034
min_high_minority_to_required_ratio=0.5973261904113458
min_high_minority_to_required_ratio_for_P_ge_17=1.2504140082035853
max_low_total_to_required_ratio=0.12484783546489416
max_low_total_modulus=7
```

### 3.1 低 CRT 层容量最高记录

| P | low total / required | total minority / required | high minority / required |
| --- | --- | --- | --- |
| `7` | `0.124847835465` | `0.622769560919` | `0.597326190411` |
| `19` | `0.117466443997` | `1.447434764838` | `1.368906207852` |
| `13` | `0.116136687980` | `0.974777076409` | `0.958303332523` |
| `23` | `0.111539205044` | `1.655488099315` | `1.625281996249` |
| `17` | `0.107028257411` | `1.284236511887` | `1.250414008204` |
| `31` | `0.106104414607` | `1.920995420516` | `1.887211058147` |
| `43` | `0.103099427348` | `2.629230419050` | `2.573338092179` |
| `47` | `0.102538406063` | `2.924834043502` | `2.896700828418` |
| `11` | `0.101359865488` | `0.979633031653` | `0.928299183860` |
| `29` | `0.098426973139` | `1.939847514645` | `1.892455594703` |
| `73` | `0.098316729284` | `4.150266781381` | `4.096289316389` |
| `61` | `0.097717743529` | `3.573378573996` | `3.541912331036` |

### 3.2 少数半类最接近阈值的记录

| P | total minority / required | high minority / required | low total / required | capacity pass | large split pass |
| --- | --- | --- | --- | --- | --- |
| `7` | `0.622769560919` | `0.597326190411` | `0.124847835465` | `false` | `false` |
| `13` | `0.974777076409` | `0.958303332523` | `0.116136687980` | `false` | `false` |
| `11` | `0.979633031653` | `0.928299183860` | `0.101359865488` | `false` | `false` |
| `17` | `1.284236511887` | `1.250414008204` | `0.107028257411` | `true` | `true` |
| `19` | `1.447434764838` | `1.368906207852` | `0.117466443997` | `true` | `true` |
| `23` | `1.655488099315` | `1.625281996249` | `0.111539205044` | `true` | `true` |
| `31` | `1.920995420516` | `1.887211058147` | `0.106104414607` | `true` | `true` |
| `29` | `1.939847514645` | `1.892455594703` | `0.098426973139` | `true` | `true` |
| `37` | `2.311153500709` | `2.290785775090` | `0.097393749390` | `true` | `true` |
| `43` | `2.629230419050` | `2.573338092179` | `0.103099427348` | `true` | `true` |
| `41` | `2.645724645213` | `2.604731360403` | `0.097320339223` | `true` | `true` |
| `47` | `2.924834043502` | `2.896700828418` | `0.102538406063` | `true` | `true` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ProjectionGapTargetImported` | `true` | `true` | 上一层已把半类容量门化成 logP/P 级二次投影缺口。 | QuadraticProjectionGapBeatsLogOverPThresholdAtSquareScale |
| `MinorityMassEquivalenceClosed` | `true` | `true` | 二次投影缺口阈值等价于 min_s Theta_s(P)>2PlogP。 | none |
| `LowCRTCapacityInsufficiencyClosed` | `true` | `true` | ell<P 的完整低 CRT 层总质量最多 PlogP，不超过所需少数质量的一半。 | none |
| `LargeSplittingLayerIdentified` | `true` | `true` | 反例链若继续存在，真实负载必须表现为大素数二次半类分裂荒漠。 | LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale |
| `LargePrimeQuadraticSplittingMassProved` | `false` | `false` | 当前语料尚未自足证明 P<ell<=P^2 中两半类各有超过 2PlogP 的素数权重。 | LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步关闭低 CRT 直推误出口，但不证明行/列命题。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((ChebyshevPrincipalMassLowerBoundAtP2 AND (QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale OR LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale OR UltraNearOneQuadraticProjectionDefectToLargeSplittingPDECOrSiegelPacket)))) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件证明的是低 CRT 层不足以闭合投影缺口门，并把硬点定位到大素数二次分裂质量；它没有证明该大素数分裂质量下界，因此不声明行/列命题无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-halfclass-capacity-margin-factorization-router.json` | `1731f400706c1e17c3e267ad421435854f7cb71a27249805b5c048f702e19841` |
| `docs/monograph/claim-status-table.md` | `64c4b82c235a332a9075008ee057e9c86b628d67872e2d5a8e0b498cb8d4a734` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `07a89f31946210131bee45edcb9b1d93981e37bfebe105c847f900f9a2ac7bff` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `ce99ad5a1c818745a8969bffa3f2b391296322b03518439e32594a148a4829c4` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `beeb9394d78c15fc2a8325d4e2de0f3e2b09e08457a7c3f6cf085afe0c8335bc` |
