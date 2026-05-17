# Three Claims Frontier / Rank-one Explicit Formula Router

**状态：** `three_claim_frontiers_synthesized_rankone_routed_to_explicit_ap_zero_packet_open`

三个命题的当前前沿必须分开看：行/列链最新硬点是 `RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2`；二次筛链仍需要 I3-Core/true-residual total incidence 或外部 DI/BFI-KLS；RH 链仍是待独立审稿的验证包。继续攻击行/列最新硬点可得精确等价：rank-one 排斥就是 `theta(P^2;P,a)>0` 对每个非零类成立。显式公式把它压成带符号零点包必须逐类小于主项的屏障；当前 GRH 形状、BV 平均、完整 CRT 均匀性和标准 Linnik 都不足以给出该 sharp P^2 正性。

```text
rankone_equivalent_to_theta_ap_positivity=true
explicit_formula_barrier_identified=true
current_classical_inputs_sufficient=false
row_column_unconditional_closed=false
two_point_unconditional_closed=false
rh_unconditional_closed=false
next_direct_attack_target=ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2
```

## 1. 三个命题前沿

| claim | target | latest open | unconditional closed |
| --- | --- | --- | --- |
| `Prime Matrix row/column` | 奇素数 P x P 方阵中每行和 P 列外每列都有素数 | `RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2` | `false` |
| `Two-point / quadratic secondary sieve` | 后半方阵中存在差/和为任意固定偶数的素数对候选之一 | `I3CoreTrueResidualTotalLargeIncidenceOrExternalDIBFIKLSWindow` | `false` |
| `RH contradiction field` | ζ(s) 的非平凡零点实部均为 1/2 | `IndependentRefereeAcceptanceOfAllRHControlledExits` | `false` |

## 2. 行/列最新链条

- A/B counterexample reduction to Structured-EHPD
- complete P-wheel non-P column uniformity is global average only
- localized P-CRT transfer equals least prime in every nonzero class mod P below P^2
- Linnik=2 zero column forces nonprincipal projection N_a=-T_0
- energy capacity-only route rejected; latest hard point is rank-one evaluation phase coherence

## 3. 二次筛最新链条

- two-point rough-pair condition p∤x(x-w) would imply fixed-gap prime pairs
- secondary-sieve field decomposes into TLI/BST/BMD/WBE2/BE2-3K/KLS-window
- external DI/BFI-Kloosterman large-sieve route can close BMD as an external-deep-theorem chain
- fully self-contained route still needs I3-Core / true-residual total large-incidence estimate

## 4. RH 最新链条

- off-critical zero creates smooth prime anomaly
- anomaly is routed through sparse/dense/tail/internal/global controlled exits
- current manuscript is a verification package under recorded local theorems and restricted external inputs
- final promotion requires independent line-by-line referee verification of controlled exits

## 5. Rank-one 到显式公式屏障

| from | to |
| --- | --- |
| `RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2` | `rho_a(P)<1 for every a in F_P^*` |
| `rho_a(P)=1-theta_a(P)/(T_0(P)/(P-1))` | `theta_a(P)>0 for every a in F_P^*` |
| `theta_a(P)>0` | `SharpPointwiseThetaAPPositivityAtXEqualsP2ForPrimeModuli` |
| `character explicit formula` | `ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2` |
| `GRH-shape error O(P log^2 P)` | `not enough to beat main term of size about P at x=P^2` |
| `BV / mean AP / complete CRT uniformity` | `average only; cannot remove a single exceptional residue direction` |

## 6. 显式公式账本

| item | formula |
| --- | --- |
| `theta_class` | `theta(P^2;P,a)=sum_{ell<=P^2, ell prime, ell=a mod P} log ell` |
| `main_term` | `T_0(P)/(P-1) ~ P` |
| `rankone_ratio` | `rho_a(P)=1-theta(P^2;P,a)/(T_0(P)/(P-1))` |
| `zero_column` | `rho_a(P)=1 iff theta(P^2;P,a)=0` |
| `explicit_formula_shape` | `theta(P^2;P,a)=main - (1/(P-1))*sum_{chi!=chi0} conjugate(chi(a))*sum_{rho_chi} P^(2 rho_chi)/rho_chi + controlled trivial terms` |
| `needed_bound` | `for every a, the signed zero packet plus trivial terms must be strictly smaller than the main term` |
| `grh_shape_not_enough` | `sqrt(x) log^2(Px)=P log^2(P^3) is larger than the main term scale P` |
| `linnik2_barrier` | `standard Linnik gives P^L with L>2; it does not imply positivity at P^2` |

## 7. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ThreeClaimFrontierSynthesisClosed` | `true` | `true` | 三个命题的最前沿状态已按行/列、二次筛、RH 分离，避免状态串用。 | none |
| `RankOneHardPointImported` | `true` | `false` | 上一层已关闭 L2 capacity-only 误出口，并把行/列列侧硬点压到 rank-one evaluation 相位。 | RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2 |
| `RankOneEquivalentToThetaAPPositivity` | `true` | `true` | rho_a<1 等价于 theta(P^2;P,a)>0；这就是每个非零 AP 类在 P^2 前有素数。 | SharpPointwiseThetaAPPositivityAtXEqualsP2ForPrimeModuli |
| `ExplicitFormulaBarrierIdentified` | `true` | `true` | 显式公式显示需要逐 residue 的带符号零点包小于主项，而不是平均能量控制。 | ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2 |
| `CurrentClassicalInputsInsufficient` | `true` | `true` | GRH 形状、BV 平均、完整 CRT 均匀性和标准 Linnik 均不推出 x=P^2 的逐类正性。 | ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2 |
| `TargetUnconditionallyClosed` | `false` | `false` | 本步没有证明 sharp pointwise AP positivity；行/列、二次筛、RH 均仍不能称无条件终稿。 | (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 8. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明 sharp pointwise AP positivity，也没有把二次筛或 RH 提升为无条件终稿；它只完成三命题前沿同步并关闭若干误用路线。

## 9. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-linnik2-rankone-phase-capacity-router.json` | `5c1a653d7367788f233fb0ca0eee1147b75a2c1ae8c614919bb0a78be7e0a2c4` |
| `docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.json` | `9923c5fda90f30ef0bd67ada6e63fe8eaf0feaa88e07b6f557792bec22a1befe` |
| `docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json` | `98232747aaf27a93f4cc68cc5bc8d29d80c5d0786bfeead635a6b42293ba6107` |
| `docs/monograph/claim-status-table.md` | `2fd5a1d773cb2d35ae32190704a1e6c465ef35a33db909a3d73092233606464b` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-V.md` | `78f11a07a2894ee935f18a8a87baf914cad1c75a82282266ff2ba909092c7589` |
| `docs/prime-density-waves-VIII.md` | `b7f072df8c7b33babe19ca00bc5a795030148041c1051ee884a2bdfc01e37988` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `1631fa90eccbac064615471c9a74f6e3766f383e1c562e2f4db7816888ef4dec` |
