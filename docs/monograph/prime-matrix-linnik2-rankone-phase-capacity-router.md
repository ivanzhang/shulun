# Prime Matrix Linnik=2 rank-one 相位容量路由

**状态：** `pointwise_nonprincipal_projection_reduced_to_rankone_phase_coherence_open`

点态非主投影界不能只靠总能量容量闭合。零列确实强制 `||T_nonprincipal||_2^2>=T_0^2/(P-2)`，但总能量超过该地板只是必要条件，不是矛盾；真正需要排斥的是某一个 residue evaluation simplex 方向上的 rank-one 负投影达到 `-T_0`。因此最新剩余接口收缩为 `RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2`。

```text
energy_floor_necessary_condition_closed=true
energy_capacity_only_route_not_enough=true
evaluation_vector_simplex_geometry_closed=true
rankone_phase_coherence_exclusion_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2
```

## 1. 公式账本

| item | formula |
| --- | --- |
| `projection_ratio` | `rho_a(P)=-N_a(P)/T_0(P)=1-theta_a(P)/average_theta(P)` |
| `zero_column` | `theta_a(P)=0 iff rho_a(P)=1` |
| `energy_floor` | `zero column implies \|\|T_nonprincipal\|\|_2^2 >= T_0(P)^2/(P-2)` |
| `energy_only_sufficient_exclusion` | `\|\|T_nonprincipal\|\|_2^2 < T_0(P)^2/(P-2) excludes zero columns` |
| `energy_only_limitation` | `if \|\|T_nonprincipal\|\|_2^2 >= T_0(P)^2/(P-2), capacity alone gives no contradiction` |
| `rankone_projection` | `N_a(P)=<T_nonprincipal,v_a>, \|\|v_a\|\|_2^2=P-2` |
| `simplex_inner_product` | `<v_a,v_b>=P-2 for a=b and -1 for a!=b` |

## 2. 容量/相位路由链

| from | to |
| --- | --- |
| `PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2` | `for every a, -N_a(P)/T_0(P)<1` |
| `zero column at a` | `-N_a(P)/T_0(P)=1` |
| `energy-only exclusion` | `requires sum_{chi!=chi0}\|T_chi\|^2<T_0(P)^2/(P-2)` |
| `energy above the floor` | `not a contradiction; one still needs rank-one projection phase control` |
| `evaluation vectors v_a` | `<v_a,v_b>=P-2 if a=b, otherwise -1; residue tests are simplex directions` |
| `remaining proof target` | `RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2` |

## 3. 有限样本（P <= 3000）

- 检查素数模数：`429`。
- theta 零剩余类总数：`0`。
- 容量-only 不能排除的样本数：`423`。
- 容量-only 可直接排除的样本数：`6`。
- 最大负投影比例：`0.686688`，出现于 `P=73`。
- 最大总能量/零列地板比例：`5.751979`，出现于 `P=2953`。

### 3.1 负投影最危险样本

| P | min residue | min theta | rho=max(-N/T0) | phase margin | energy/floor | projection energy fraction |
| --- | --- | --- | --- | --- | --- | --- |
| 73 | 72 | 22.693951 | 0.686688 | 0.313312 | 2.413634 | 0.195365 |
| 7 | 4 | 2.397895 | 0.631228 | 0.368772 | 0.444033 | 0.897341 |
| 13 | 12 | 4.634729 | 0.627653 | 0.372347 | 1.194008 | 0.329937 |
| 43 | 15 | 16.923312 | 0.601763 | 0.398237 | 1.539168 | 0.235269 |
| 19 | 12 | 8.106816 | 0.560644 | 0.439356 | 1.425110 | 0.220560 |
| 199 | 9 | 100.518771 | 0.494230 | 0.505770 | 3.325447 | 0.073453 |
| 71 | 48 | 37.722403 | 0.467472 | 0.532528 | 2.004627 | 0.109013 |
| 101 | 30 | 54.650723 | 0.459089 | 0.540911 | 2.790930 | 0.075517 |
| 5 | 1 | 2.397895 | 0.455446 | 0.544554 | 0.504083 | 0.411503 |
| 31 | 4 | 16.605352 | 0.453460 | 0.546540 | 1.444353 | 0.142365 |
| 131 | 31 | 71.435758 | 0.453390 | 0.546610 | 2.483451 | 0.082773 |
| 139 | 34 | 77.233849 | 0.441641 | 0.558359 | 2.239474 | 0.087095 |

### 3.2 总能量最大样本

| P | rho=max(-N/T0) | energy/floor | phase margin | capacity false positive |
| --- | --- | --- | --- | --- |
| 2953 | 0.139565 | 5.751979 | 0.860435 | `True` |
| 2633 | 0.151194 | 5.697251 | 0.848806 | `True` |
| 2789 | 0.143634 | 5.682254 | 0.856366 | `True` |
| 2963 | 0.150150 | 5.680462 | 0.849850 | `True` |
| 2879 | 0.154416 | 5.670151 | 0.845584 | `True` |
| 2969 | 0.155870 | 5.666913 | 0.844130 | `True` |
| 2819 | 0.153843 | 5.666181 | 0.846157 | `True` |
| 2687 | 0.188235 | 5.662114 | 0.811765 | `True` |
| 2897 | 0.142934 | 5.646972 | 0.857066 | `True` |
| 2647 | 0.158030 | 5.644279 | 0.841970 | `True` |
| 2593 | 0.170355 | 5.636384 | 0.829645 | `True` |
| 2999 | 0.144681 | 5.634559 | 0.855319 | `True` |

这些样本只用于定位误出口：很多实例总能量已经超过零列必要地板，但仍没有零列。因此容量地板不能替代 rank-one 相位排斥。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PointwiseProjectionBarrierImported` | `true` | `false` | 上一层已把 Linnik=2 零列缺陷压成逐 residue 的非主负投影界。 | PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2 |
| `EnergyFloorNecessaryConditionClosed` | `true` | `true` | 零列必然使非主总能量超过 T0^2/(P-2)，这是 Cauchy 的必要条件。 | none |
| `EnergyCapacityAloneSufficientOnlyBelowFloor` | `true` | `true` | 若能证明总能量严格低于该地板，则可排除零列；这是容量路线的唯一直接出口。 | global L2 bound below zero floor |
| `EnergyCapacityRouteNotEnoughInCurrentFrontier` | `true` | `true` | 当前对象需要排斥 rank-one 负投影；总能量在地板以上并不构成矛盾。 | RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2 |
| `EvaluationVectorSimplexGeometryClosed` | `true` | `true` | 各 residue 的非主 evaluation 向量形成正则 simplex，零列是其中一个方向的极端负投影。 | RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2 |
| `RankOnePhaseCoherenceExclusionProved` | `false` | `false` | 当前语料没有证明 rho_a(P)<1 的统一余量；这正是点态 AP 问题的相位形式。 | RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2 |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭容量-only 误出口，把剩余压成 rank-one 负投影相位极化排斥。 | (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明 rank-one 负投影相位极化排斥；它只证明容量-only 线路不能作为当前无条件闭合，并把剩余精确定位到 evaluation simplex 的点态方向。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-linnik2-nonprincipal-character-obstruction-router.json` | `9923c5fda90f30ef0bd67ada6e63fe8eaf0feaa88e07b6f557792bec22a1befe` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-V.md` | `78f11a07a2894ee935f18a8a87baf914cad1c75a82282266ff2ba909092c7589` |
| `docs/prime-density-waves-VIII.md` | `b7f072df8c7b33babe19ca00bc5a795030148041c1051ee884a2bdfc01e37988` |
