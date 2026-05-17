# Prime Matrix Large Splitting Beta-gap Router

**状态：** `large_splitting_mass_routed_to_beta_gap_and_zero_packet_budget_open`

本步继续下钻 `LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale`。高区间分裂门等价于 `1-|Hchi|/H0 > 4P log P/H0`。若用显式公式预算 `|Hchi|/H0 <= R_beta(P)+E_zero(P)`，则需要 `R_beta(P)+E_zero(P)` 小于 `1-4PlogP/H0`。无剩余零包的实零模型给出临界 `1-beta` 约为 `2/P`。因此持久失败必须是 beta 贴近 1 到 `1/P` 级，或非实零/端点残差同向相干吃掉同一 slack。这把剩余硬点压成有效 beta-gap 加零包残差预算；当前仍未自足闭合。

```text
high_projection_equivalence_closed=true
beta_gap_critical_scale_identified=true
beta_gap_and_zero_packet_budget_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2
pdec_fallback_target=UltraCloseRealZeroOrCoherentZeroPacketLargeSplittingPDEC
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `high interval halfclass` | `G_s(P)=sum_{P<ell<=P^2, chi_P(ell)=s} log ell` |
| `high projection` | `H0=G_++G_-, Hchi=G_+-G_-` |
| `large splitting gate` | `min_s G_s(P)>2P log P iff 1-\|Hchi\|/H0 > 4P log P/H0` |
| `explicit formula budget shape` | `if \|Hchi\|/H0 <= R_beta(P)+E_zero(P), it suffices that R_beta(P)+E_zero(P)<1-4PlogP/H0` |
| `real zero high-interval shadow` | `R_beta(P)=(P^(2beta)-P^beta)/(beta H0), beta=1-delta` |
| `critical beta gap` | `delta_crit solves R_(1-delta)(P)=1-4PlogP/H0; asymptotically delta_crit ~ 2/P when H0~P^2` |
| `failure shape` | `persistent failure requires beta=1-O(1/P) or a coherent nonreal/endpoint residual consuming the same slack` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale` | SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2 | budget factorization | 大素数二次分裂门等价于高区间角色投影必须留出 4PlogP/H0 的缺口。 |
| `real quadratic zero shadow` | SelfContainedEffectivePrimeModulusQuadraticBetaGapAtScaleOneOverP | quantified threshold | 若实零影子负责失败，则 beta 必须贴近 1 到约 1/P 级。 |
| `nonreal zeros and endpoint/prime-power corrections` | NonrealZeroPacketResidualBelowLargeSplittingSlackAtP2 | still open | 即便实零影子不足，非实零同向相干或端点误差仍需有独立预算排斥。 |
| `classical ineffective Siegel theorem` | IneffectiveSiegelTheoremFiniteBaseGap | external asymptotic only | 任取 epsilon<1 的 Siegel 型 gap 可渐近压过 1/P，但常数无效，不能给出本稿自足全 P 有限基。 |
| `persistent failure` | UltraCloseRealZeroOrCoherentZeroPacketLargeSplittingPDEC | named fallback | 长期失败必须成为超近实零或非实零包同向相干的显式 PDEC/Siegel 出口。 |

## 3. 有限诊断

有限扫描只用于定位 beta-gap 临界尺度，不作为无限证明输入。

```text
min_p=7
max_p=1000
prime_moduli_checked=165
large_splitting_gate_failure_moduli=[7, 11, 13]
min_high_minority_to_required_ratio=0.5973261904113458
min_high_minority_to_required_ratio_for_P_ge_17=1.2504140082035853
max_critical_beta_gap_times_P=9.135807071199574
max_critical_beta_gap_times_P_for_P_ge_17=5.072468572399141
max_critical_beta_gap_times_P_for_P_ge_101=2.7065999766476923
min_critical_beta_gap_times_P_for_P_ge_101=2.2492763319844737
```

### 3.1 高区间少数半类最接近阈值记录

| P | high minority / required | tau | actual gap | beta gap crit | P*crit |
| --- | --- | --- | --- | --- | --- |
| `7` | `0.597326190411` | `1.529927638044` | `0.913865847638` | `none` | `none` |
| `11` | `0.928299183860` | `1.062246188920` | `0.986082270233` | `none` | `none` |
| `13` | `0.958303332523` | `0.941778197711` | `0.902509185365` | `0.702754390092` | `9.135807071200` |
| `17` | `1.250414008204` | `0.746155144698` | `0.933002845223` | `0.298380504259` | `5.072468572399` |
| `19` | `1.368906207852` | `0.701528229919` | `0.960326348920` | `0.256481599565` | `4.873150391733` |
| `23` | `1.625281996249` | `0.600594709445` | `0.976135768304` | `0.180847018949` | `4.159481435833` |
| `31` | `1.887211058147` | `0.479040725440` | `0.904050954353` | `0.117262615059` | `3.635141066819` |
| `29` | `1.892455594703` | `0.498545348679` | `0.943474934321` | `0.124795967530` | `3.619083058369` |
| `37` | `2.290785775090` | `0.415248803303` | `0.951246051729` | `0.090730526490` | `3.357029480131` |
| `43` | `2.573338092179` | `0.369362811262` | `0.950495392056` | `0.074646039533` | `3.209779699898` |
| `41` | `2.604731360403` | `0.379275977508` | `0.987912032864` | `0.076674485115` | `3.143653889713` |
| `47` | `2.896700828418` | `0.345051011142` | `0.999509549820` | `0.067056796712` | `3.151669445458` |

### 3.2 临界 beta-gap 归一化最高记录

| P | P*crit | crit | tau | R(2/P) | 2/P suffices in model |
| --- | --- | --- | --- | --- | --- |
| `13` | `9.135807071200` | `0.702754390092` | `0.941778197711` | `0.567437250401` | `false` |
| `17` | `5.072468572399` | `0.298380504259` | `0.746155144698` | `0.597829599420` | `false` |
| `19` | `4.873150391733` | `0.256481599565` | `0.701528229919` | `0.631672873245` | `false` |
| `23` | `4.159481435833` | `0.180847018949` | `0.600594709445` | `0.659314202072` | `false` |
| `31` | `3.635141066819` | `0.117262615059` | `0.479040725440` | `0.712130801224` | `false` |
| `29` | `3.619083058369` | `0.124795967530` | `0.498545348679` | `0.693061872322` | `false` |
| `37` | `3.357029480131` | `0.090730526490` | `0.415248803303` | `0.736077703647` | `false` |
| `43` | `3.209779699898` | `0.074646039533` | `0.369362811262` | `0.758697670057` | `false` |
| `47` | `3.151669445458` | `0.067056796712` | `0.345051011142` | `0.772678659246` | `false` |
| `41` | `3.143653889713` | `0.076674485115` | `0.379275977508` | `0.743663347540` | `false` |
| `59` | `2.966315954412` | `0.050276541600` | `0.287757521565` | `0.801317779041` | `false` |
| `53` | `2.904031251396` | `0.054793042479` | `0.309450837561` | `0.777915191698` | `false` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LargeSplittingTargetImported` | `true` | `true` | 上一层已把二次投影缺口压成大素数二次分裂少数质量门。 | LargePrimeQuadraticSplittingMinorityMassBeatsTwoPLogPAtSquareScale |
| `HighProjectionEquivalenceClosed` | `true` | `true` | 大分裂质量门等价于高区间二次角色投影缺口。 | none |
| `BetaGapCriticalScaleIdentified` | `true` | `true` | 实零影子若单独造成失败，必须达到 beta=1-O(1/P) 的临界贴近。 | none |
| `ClassicalSiegelAsymptoticButIneffective` | `true` | `false` | 经典 Siegel gap 可给渐近方向，但常数无效，不能替代自足有限基。 | IneffectiveSiegelTheoremFiniteBaseGap |
| `BetaGapAndZeroPacketBudgetProved` | `false` | `false` | 当前语料尚未自足证明有效 beta-gap 与非实零包残差预算。 | SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2 |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只量化解析临界尺度，不证明行/列命题。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((ChebyshevPrincipalMassLowerBoundAtP2 AND (QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale OR (SelfContainedEffectivePrimeModulusQuadraticBetaGapAtScaleOneOverP AND NonrealZeroPacketResidualBelowLargeSplittingSlackAtP2) OR UltraCloseRealZeroOrCoherentZeroPacketLargeSplittingPDEC)))) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明有效无 Siegel 零点、Linnik=2、非实零包抵消或行/列命题；它只把大素数二次分裂失败所需的实零贴近尺度与零包残差预算量化。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-quadratic-projection-large-splitting-router.json` | `04192e7fe4736b47ef60657151339de69027de55c406c9b8bcde89301b754af2` |
| `docs/monograph/claim-status-table.md` | `8f5501f1e54e5896ec326c74d4c63349371f6035d877a5de3bd5e58525bad615` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `21a945110a74c161889a7e87b8f7ee06c164049e874c0431e6d5f0b5823120b2` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `c9a2e2dc5566b2c9476741c58430ea9753a4148513acffa015511f7942760c62` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `14b0cbd3ee159ebf390b6950a858d482b9fea665de65c17fc643f38d388c2ebc` |
