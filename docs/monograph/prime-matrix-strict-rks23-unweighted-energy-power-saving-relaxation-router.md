# Prime Matrix strict RKS2/RKS3 能量目标固定幂节省放松证书

**状态：** `unweighted_reciprocal_energy_log_saving_reduced_to_any_fixed_power_saving`

当前唯一内部自足剩余继续压窄：无需直接证明 `log^-472` 级加性能量节省。由于平衡颈部满足 `|J|>=P^(1/2)/log^236(P)`，任意固定正幂节省 `E_+(J^{-1})<=|J|^(3-delta_E)` 都会在大 P 区间压过全部固定对数损失；小 P 端仍交给既有有限验证/P0 通道。于是下一真正硬点变为固定幂节省版倒数区间能量。

```text
fixed_power_saving_implies_required_log_saving=true
fixed_power_saving_energy_proved=false
row_column_unconditional_closed=false
```

## 1. 放松公式

| field | value |
| --- | --- |
| `old_required_bound` | E_+(J^{-1}) <= \|J\|^3/log^(472+C_weight)(P) |
| `collar_lower_bound` | \|J\| >= P^(1/2)/log^236(P) |
| `sufficient_new_bound` | there exists fixed delta_E>0 such that E_+(J^{-1}) <= \|J\|^(3-delta_E) |
| `absorption_check` | \|J\|^delta_E >= P^(delta_E/2)/log^(236 delta_E)(P), which dominates every fixed log power for sufficiently large P |
| `finite_transition` | large-P transition can be delegated to the existing finite/P0 verification lane once constants are supplied |
| `new_core_advantage` | the remaining input is power saving, not a huge explicit log^472 saving |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LogEnergyTargetActive` | `true` | `true` | 上一证书已把唯一剩余写成纯倒数区间加性能量对数节省。 | UnweightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23 |
| `FixedPowerSavingImpliesRequiredLogSaving` | `true` | `true` | 在平方根对数颈部，任何固定幂节省最终压过固定对数损失。 | UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23 |
| `IncidenceSumProductRouteStillAligned` | `true` | `true` | Rudnev/RNRS/sum-product 路线自然提供的正是固定幂节省形态。 | RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving |
| `UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23` | `false` | `false` | 仓库内尚未给出 `E_+(J^{-1}) <= \|J\|^(3-delta_E)` 的自足证明。 | OneParameterMobiusIntervalOverlapPowerSavingForReciprocalEnergy OR RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只把目标从固定对数节省放松为固定幂节省；行/列无条件闭合仍不能声明。 | UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23 |

## 3. 下一最窄自足目标

```text
UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23
```
