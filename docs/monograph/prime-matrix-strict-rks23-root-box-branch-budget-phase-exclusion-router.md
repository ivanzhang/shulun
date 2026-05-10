# Prime Matrix strict RKS2/RKS3 根定位盒分支预算排除证书

**状态：** `low_branch_budget_phases_absorbed_central_root_box_high_spectrum_remains`

根定位小差盒继续被分支预算压缩。对有符号相位 `gamma`，`ab-gamma(a+b)=kP` 的分支数满足 `B(gamma)<=1+(U^2+2|gamma|U)/P`；固定分支再由除数界控制。因此低分支预算相位不能进入固定幂高谱。任何假设高纤维都被迫满足中央相位必要条件 `|gamma| >= (P/U)N^(1-eta-o(1))`，剩余只剩中央相位的大分支供给是否能同步命中根定位盒。

```text
low_branch_budget_phase_high_spectrum_excluded=true
high_fiber_forces_central_phase_condition=true
central_phase_root_localized_graph_box_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 分支预算

| field | value |
| --- | --- |
| `signed_phase` | gamma is the signed representative of c |
| `box_height` | U=max J with U<=P^(1/2)log^236(P) |
| `integer_lift` | ab-gamma(a+b)=kP |
| `branch_budget` | B(gamma)<=1+(U^2+2\|gamma\|U)/P |
| `per_branch_factorization` | (a-gamma)(b-gamma)=gamma^2+kP |
| `divisor_envelope` | r_gamma<=B(gamma)*P^o(1) |
| `high_threshold` | r_gamma>N^(1-eta) for some fixed eta>0 |
| `necessary_central_condition` | \|gamma\| >= (P/U)*N^(1-eta-o(1)) unless the phase is already absorbed |

## 2. 压缩结果

| field | value |
| --- | --- |
| `absorbed_phases` | all phases with B(gamma)<=N^(1-eta-o(1)) |
| `remaining_phases` | central signed phases whose branch budget itself is high enough to support a high fiber |
| `why_this_is_narrower` | the proof no longer has to handle every interior phase; only central phases with large lift-branch supply remain |
| `still_missing` | large branch supply does not by itself create many root-localized hits; it only keeps the counterexample alive |
| `next_direct_attack` | CentralPhaseRootLocalizedGraphBoxFiberPowerSaving |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RootLocalizedGraphBoxTargetActive` | `true` | `true` | 上一证书已把剩余固定为根定位小差盒的有理相位映射高重数排斥。 | RootLocalizedQuadraticGraphBoxFiberPowerSaving |
| `BranchBudgetEnvelopeClosed` | `true` | `true` | `ab-gamma(a+b)=kP` 给出 `B(gamma)<=1+(U^2+2\|gamma\|U)/P`。 | LowBranchBudgetPhaseHighSpectrumExclusion |
| `PerBranchDivisorEnvelopeClosed` | `true` | `true` | 固定分支化为一条整数乘积方程，所以每分支由除数界控制。 | LowBranchBudgetPhaseHighSpectrumExclusion |
| `LowBranchBudgetPhaseHighSpectrumExcluded` | `true` | `true` | 若分支预算低于高谱阈值，则 `r_gamma<=B(gamma)P^o(1)` 直接排除高重数。 | absorbed |
| `HighFiberForcesCentralPhaseCondition` | `true` | `true` | 任何幸存高纤维必须满足 `\|gamma\| >= (P/U)N^(1-eta-o(1))` 的中央相位必要条件。 | CentralPhaseRootLocalizedGraphBoxFiberPowerSaving |
| `CentralPhaseRootLocalizedGraphBoxFiberPowerSaving` | `false` | `false` | 中央相位仍可能有足够分支预算；还需证明这些分支不能同步命中根定位小差盒。 | CentralBranchRootBoxIncidencePowerSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只排除低分支预算相位，没有证明中央相位排斥。 | CentralPhaseRootLocalizedGraphBoxFiberPowerSaving |

## 4. 下一最窄自足目标

```text
CentralPhaseRootLocalizedGraphBoxFiberPowerSaving
```
