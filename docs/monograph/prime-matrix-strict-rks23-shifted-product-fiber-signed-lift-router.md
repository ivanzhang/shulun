# Prime Matrix strict RKS2/RKS3 shifted product fiber 有符号提升证书

**状态：** `signed_small_shifted_product_phases_absorbed_interior_high_spectrum_remains`

shifted product fiber 的当前剩余可先按相位的有符号代表拆开。当 `|gamma|<=max J` 时，方程 `ab-gamma(a+b)=kP` 只有 `log^O(P)` 个整数分支，每个分支化为一个普通除数计数 `(a-gamma)(b-gamma)=gamma^2+kP`，因此该部分只有 `N^o(1)` 点态质量，不能进入固定幂高谱。真正剩余被压缩为内部相位 `min(c,P-c)>max J` 的平均型高谱排斥。

```text
signed_small_phase_divisor_lift_sublinear_bound_proved=true
interior_shifted_product_high_spectrum_proved=false
row_column_unconditional_closed=false
```

## 1. 有符号小相位提升

| field | value |
| --- | --- |
| `dyadic_collar_model` | J=[A,A+N] with U=max J and U<=P^(1/2)log^236(P) |
| `signed_phase_scope` | take the signed representative gamma of c with \|gamma\|<=U |
| `integer_lift` | ab-gamma(a+b)=kP |
| `branch_budget` | \|k\|<=3U^2/P<=3log^472(P) in the square-root collar |
| `factor_identity_per_branch` | (a-gamma)(b-gamma)=gamma^2+kP |
| `divisor_count` | for each k, the number of pairs is <= tau(\|gamma^2+kP\|) |
| `sublinear_consequence` | r_gamma<=log^O(P) P^o(1)=N^o(1), hence below N^(1-eta) for every fixed eta<1 and large P |
| `finite_transition` | explicit small-P constants remain in the existing finite/P0 verification lane |

## 2. 新前沿

| field | value |
| --- | --- |
| `absorbed_part` | all nonzero phases whose signed representative satisfies \|gamma\|<=max J |
| `why_this_is_progress` | the near-zero and near-P phases no longer need incidence or BG machinery |
| `why_pointwise_guard_is_retired` | a global pointwise target is stronger than required; the proof only needs high-spectrum energy control |
| `remaining_phase_scope` | interior phases with min(c,P-c)>max J |
| `remaining_obstruction` | for interior c, the integer branch range can be O(U), so a plain per-branch divisor sum is too weak |
| `next_required_input` | InteriorPhaseBranchSlopeIncidenceOrAverageDivisorPacketBound |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ShiftedProductFiberTargetActive` | `true` | `true` | 上一证书已把非零 PGL2 剩余改写为 shifted product fiber 高谱。 | ShiftedIntervalModularProductFiberHighSpectrumPowerSavingForSquareRootCollar |
| `SignedSmallPhaseIntegerLiftClosed` | `true` | `true` | `\|gamma\|<=max J` 时整数分支数只有 `log^O(P)`，每分支由除数界给 `P^o(1)`。 | SignedSmallPhaseDivisorLiftSublinearBound |
| `SignedSmallPhaseHighSpectrumAbsorbed` | `true` | `true` | 小有符号相位满足 `r_gamma=N^o(1)`，不会进入任何固定幂高谱层。 | absorbed |
| `UniformPointwiseFiberBoundRetiredAsNecessaryGate` | `true` | `true` | 全体 `c` 的点态次线性界足够但非必要；当前只保留高谱能量所需输入。 | InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar |
| `InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar` | `false` | `false` | 内部相位 `min(c,P-c)>max J` 仍需平均型分支/斜率 incidence 或除数包估计。 | InteriorPhaseBranchSlopeIncidenceOrAverageDivisorPacketBound |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只吸收有符号小相位并精确缩窄剩余；未证明内部相位高谱排斥。 | InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar |

## 4. 下一最窄自足目标

```text
InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar
```
