# Prime Matrix Linnik=2 非主角色障碍路由

**状态：** `linnik2_zero_column_reduced_to_nonprincipal_character_projection_barrier_open`

Linnik=2 零列缺陷可以精确改写为非主 Dirichlet 角色的负相位投影障碍：若某个非零 residue class `a mod P` 在 `P^2` 前没有素数，则 theta 权 `theta_a(P)=0`，从而非主投影 `N_a(P)` 必须等于 `-T_0(P)`。这迫使非主角色能量达到显式下界，但该能量/相位尖峰本身并未在当前语料中被排斥。因此本步把点态 AP 屏障压成 `PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2`，不是行/列命题的无条件闭合。

```text
theta_character_expansion_exact=true
zero_column_forces_negative_projection=true
zero_column_forces_energy_spike=true
pointwise_projection_bound_proved=false
row_column_unconditional_closed=false
next_direct_attack_target=PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2
```

## 1. 精确公式账本

| item | formula |
| --- | --- |
| `theta_class` | `theta_a(P)=sum_{ell<=P^2, ell prime, ell=a mod P} log ell` |
| `character_sum` | `T_chi(P)=sum_{a in F_P^*} chi(a) theta_a(P)=sum_{ell<=P^2, ell!=P} chi(ell) log ell` |
| `orthogonality` | `theta_a(P)=(1/(P-1))*sum_chi conjugate(chi(a))*T_chi(P)` |
| `principal_mass` | `T_0(P)=sum_{a in F_P^*} theta_a(P)` |
| `nonprincipal_projection` | `N_a(P)=sum_{chi!=chi0} conjugate(chi(a))*T_chi(P)=(P-1)theta_a(P)-T_0(P)` |
| `zero_column_implication` | `theta_a(P)=0 => N_a(P)=-T_0(P)` |
| `energy_floor` | `theta_a(P)=0 => sum_{chi!=chi0}\|T_chi(P)\|^2 >= T_0(P)^2/(P-2)` |
| `pointwise_sufficient_exclusion` | `if N_a(P)>-T_0(P) for every a, then every nonzero column has a prime <=P^2` |

## 2. 精确路由链

| from | to |
| --- | --- |
| `PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2` | `not Linnik2ZeroColumnDefect` |
| `Linnik2ZeroColumnDefect` | `theta_a(P)=0 for some a in F_P^*` |
| `theta_a=(T_0+N_a)/(P-1)` | `N_a=(P-1)theta_a-T_0` |
| `theta_a=0` | `N_a=-T_0 exact negative nonprincipal projection` |
| `N_a=-T_0` | `sum_{chi!=chi0}\|T_chi\|^2 >= T_0^2/(P-2)` |
| `exclude zero column` | `PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2` |

## 3. 有限 theta 样本（P <= 3000）

- 检查素数模数：`429`。
- theta 零剩余类总数：`0`。
- 最大负缺口比例：`0.686688`，出现于 `P=73`。

| P | min residue | min theta | avg theta | deficit/avg | nonprincipal energy / zero floor | zero classes |
| --- | --- | --- | --- | --- | --- | --- |
| 73 | 72 | 22.693951 | 72.432405 | 0.686688 | 2.413634 | 0 |
| 7 | 4 | 2.397895 | 6.502385 | 0.631228 | 0.444033 | 0 |
| 13 | 12 | 4.634729 | 12.447326 | 0.627653 | 1.194008 | 0 |
| 43 | 15 | 16.923312 | 42.495593 | 0.601763 | 1.539168 | 0 |
| 19 | 12 | 8.106816 | 18.451595 | 0.560644 | 1.425110 | 0 |
| 199 | 9 | 100.518771 | 198.744167 | 0.494230 | 3.325447 | 0 |
| 71 | 48 | 37.722403 | 70.836528 | 0.467472 | 2.004627 | 0 |
| 101 | 30 | 54.650723 | 101.034595 | 0.459089 | 2.790930 | 0 |
| 5 | 1 | 2.397895 | 4.403415 | 0.455446 | 0.504083 | 0 |
| 31 | 4 | 16.605352 | 30.382673 | 0.453460 | 1.444353 | 0 |
| 131 | 31 | 71.435758 | 130.688628 | 0.453390 | 2.483451 | 0 |
| 139 | 34 | 77.233849 | 138.322900 | 0.441641 | 2.239474 | 0 |

样本只说明当前有限范围内没有 theta 零列；证明不依赖经验无反例。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `Linnik2BarrierImported` | `true` | `false` | 上一层已把局部化 P-CRT 列转移压成 prime-modulus 点态 AP/Linnik=2 屏障。 | PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2 |
| `ThetaCharacterExpansionExact` | `true` | `true` | 对 F_P^* 上的 theta residue vector 使用 Dirichlet 角色正交展开，公式完全有限且不依赖渐近。 | none |
| `ZeroColumnForcesNegativeProjection` | `true` | `true` | 若某非零列在 P^2 前无素数，则该列非主角色投影必须精确等于 -T_0。 | NonprincipalCharacterEnergySpikeForLinnik2Defect |
| `ZeroColumnForcesEnergySpike` | `true` | `true` | 由 Cauchy，零列缺陷迫使非主角色总能量至少达到 T_0^2/(P-2)，且至少一个非主角色大小达到 T_0/(P-2)。 | NonprincipalCharacterEnergySpikeForLinnik2Defect |
| `AverageCRTStillInsufficient` | `true` | `true` | 完整 CRT 均匀性对应 principal mass；零列排斥需要控制每个 a 的非主投影负相位。 | PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2 |
| `NonprincipalSpikeContradictionFound` | `false` | `false` | 当前语料没有证明所有非主投影都严格高于 -T_0，也没有给出排斥 Siegel/大偏差相位的无条件点态界。 | PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2 |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把 Linnik=2 缺陷转写为精确角色相位/能量障碍，尚未排斥该障碍。 | (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 最新活动基

```text
(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn OR PointwiseNonprincipalProjectionBoundBelowPrincipalMassAtXEqualsP2) AND ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件没有证明点态 AP/Linnik=2 定理，也没有证明排斥所有非主角色负相位投影的无条件界；它只给出有限群角色正交下的精确障碍形式。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json` | `98232747aaf27a93f4cc68cc5bc8d29d80c5d0786bfeead635a6b42293ba6107` |
| `docs/final-proof-draft.md` | `c8958bc1f15441975c2f7c2b206609eb88fa43adc21313e26742b3bb1addea9b` |
| `docs/prime-density-waves-V.md` | `78f11a07a2894ee935f18a8a87baf914cad1c75a82282266ff2ba909092c7589` |
| `docs/prime-density-waves-VIII.md` | `b7f072df8c7b33babe19ca00bc5a795030148041c1051ee884a2bdfc01e37988` |
| `docs/prime-density-waves-X.md` | `512245acdfc1bf8085de9e6de6580f41acdb1c05d9039ea44f84cf82751626fe` |
