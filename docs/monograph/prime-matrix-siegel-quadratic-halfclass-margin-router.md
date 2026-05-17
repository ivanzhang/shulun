# Prime Matrix Siegel Quadratic Half-class Margin Router

**状态：** `siegel_branch_routed_to_quadratic_halfclass_margin_open`

本步继续下钻 `SiegelExceptionalBiasExclusionAtSquareScale`：实二次零点偏置在 prime modulus 下被压成二次角色投影比例 `r_quad(P)=|T_chi(P)|/T0(P)`。危险半类的平均主项余量正比于 `1-r_quad(P)`。因此 Siegel 分支若要闭合，必须自足证明 `QuadraticHalfClassSquareScaleBiasMarginTheorem`，或接受足够强且独立认证的无 Siegel 零点/beta-gap 输入。当前二者均未完成，非实零包相位抵消也仍需另证。

```text
quadratic_projection_identity_closed=true
halfclass_margin_theorem_proved=false
effective_no_siegel_input_accepted=false
siegel_branch_closed=false
row_column_unconditional_closed=false
next_direct_attack_target=QuadraticHalfClassSquareScaleBiasMarginTheorem
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `quadratic character projection` | `T_chi(P)=sum_{ell<=P^2, ell prime, ell!=P} chi_P(ell) log ell` |
| `principal mass` | `T0(P)=sum_{ell<=P^2, ell prime, ell!=P} log ell` |
| `real-projection ratio` | `r_quad(P)=\|T_chi(P)\|/T0(P)` |
| `half-class main margin` | `dangerous half-class average weight is proportional to 1-r_quad(P)` |
| `exceptional-zero heuristic` | `if beta=1-lambda/log P, then r_quad(P) has square-scale size about exp(-2 lambda)/beta` |
| `needed theorem` | `prove r_quad(P)<=1-eta(P) with enough eta(P) to dominate nonreal and finite packets` |

## 2. 分支压缩

| branch | route | status | meaning |
| --- | --- | --- | --- |
| `SiegelExceptionalBiasExclusionAtSquareScale` | QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale | open | 实零偏置被精确改写为二次角色投影比例接近 1 的风险。 |
| `QuadraticHalfClassSquareScaleBiasMarginTheorem` | prove \|T_chi\|/T0 is bounded away from 1 at square scale with explicit margin | not proved in corpus | 这是自足线需要的新点态实角色余量，不是平均 AP 定理。 |
| `EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale` | accept an independently certified no-Siegel-zero or beta-gap theorem strong enough at x=P^2 | not available as unconditional peer-certified input here | 经典零点排斥可作为结构组织，但不能替代该输入。 |
| `NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2` | still required after real half-class margin | open | 即使二次半类保留主项余量，非实零包仍可能在单个 residue 方向上造成点态缺口。 |

## 3. 有限诊断

有限扫描只用于定位风险，不作为无限证明输入。

```text
max_p=1000
min_p=7
prime_moduli_checked=165
max_abs_quadratic_projection_ratio=0.13027036286351173
max_abs_ratio_modulus=7
min_halfclass_margin_ratio=0.8697296371364882
```

| P | abs ratio | signed ratio | halfclass margin | dangerous halfclass |
| --- | --- | --- | --- | --- |
| `7` | `0.130270362864` | `-0.130270362864` | `0.869729637136` | `quadratic_residue` |
| `13` | `0.129577436076` | `-0.129577436076` | `0.870422563924` | `quadratic_residue` |
| `31` | `0.102572337459` | `-0.102572337459` | `0.897427662541` | `quadratic_residue` |
| `17` | `0.078553531940` | `-0.078553531940` | `0.921446468060` | `quadratic_residue` |
| `37` | `0.059318103239` | `-0.059318103239` | `0.940681896761` | `quadratic_residue` |
| `29` | `0.056057812149` | `-0.056057812149` | `0.943942187851` | `quadratic_residue` |
| `43` | `0.047005595860` | `-0.047005595860` | `0.952994404140` | `quadratic_residue` |
| `23` | `0.037946518317` | `-0.037946518317` | `0.962053481683` | `quadratic_residue` |
| `131` | `0.028754866907` | `-0.028754866907` | `0.971245133093` | `quadratic_residue` |
| `19` | `0.024766221800` | `-0.024766221800` | `0.975233778200` | `quadratic_residue` |
| `71` | `0.024206270588` | `-0.024206270588` | `0.975793729412` | `quadratic_residue` |
| `173` | `0.023731625273` | `-0.023731625273` | `0.976268374727` | `quadratic_residue` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SiegelBranchImported` | `true` | `false` | 上一层已把 AP 零点包拆出 Siegel 实零偏置分支。 | SiegelExceptionalBiasExclusionAtSquareScale |
| `QuadraticProjectionIdentityClosed` | `true` | `true` | 实二次角色贡献等于 QR/NQR 半类权重差，危险半类余量由 1-\|T_chi\|/T0 控制。 | QuadraticHalfClassSquareScaleBiasMarginTheorem |
| `FiniteDiagnosticLedgerGenerated` | `true` | `true` | 有限扫描只作风险定位；它不作为无限证明输入。 | none |
| `HalfClassMarginTheoremProved` | `false` | `false` | 当前语料没有证明 square-scale 二次投影比例全局远离 1。 | QuadraticHalfClassSquareScaleBiasMarginTheorem |
| `EffectiveNoSiegelInputAccepted` | `false` | `false` | 当前没有可作为合著稿无条件输入的全局无 Siegel 零点或足够强 beta-gap 定理。 | EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale |
| `SiegelBranchClosed` | `false` | `false` | 本步只把 Siegel 分支压缩为半类余量门或外部 beta-gap 门。 | QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale |
| `RowColumnUnconditionalClosed` | `false` | `false` | 非实零包、结构 PDEC/signed payload、ExactUV、RatePreservation 与 DStructure 仍未全部闭合。 | global final inputs remain open |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ((QuadraticHalfClassSquareScaleBiasMarginTheorem OR EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale) AND NonrealZeroPacketResiduePhaseCancellationAtXEqualsP2)) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明无 Siegel 零点、二次半类余量定理、非实零包相位抵消或行/列命题；它只把 Siegel 实零分支压成可复核的二次角色投影余量门。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-explicit-ap-zero-packet-siegel-split-router.json` | `5c277929e4739d9e6829a9137d4115f974fc1df3260c7f31e57f6a7f3bc879db` |
| `docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.json` | `9923c5fda90f30ef0bd67ada6e63fe8eaf0feaa88e07b6f557792bec22a1befe` |
| `docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json` | `5c1a653d7367788f233fb0ca0eee1147b75a2c1ae8c614919bb0a78be7e0a2c4` |
| `docs/monograph/claim-status-table.md` | `989e661ccd2c5248e9d85ca7f2d2e9627b07c3b0d13a38c1bc0c3fab4a2e8467` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-VIII.md` | `b7f072df8c7b33babe19ca00bc5a795030148041c1051ee884a2bdfc01e37988` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `743155d875944ee4029e800efbd5611a4f47ec737e359021781c475080eb222e` |
