# Prime Matrix strict RKS2/RKS3 加权能量到纯四元组核心证书

**状态：** `weighted_energy_reduced_to_unweighted_reciprocal_interval_fourtuple_energy`

加权能量输入继续剥离成功：divisor-bounded Vaughan 权重只造成固定对数损失，已经由 RKS 账本收费。因此当前真正内部自足剩余可写成纯四元组计数：`J^{-1}` 在 `F_P` 中的加性能量必须满足 `E_+(J^{-1})<=|J|^3/log^(472+C_weight)(P)`。这比完整 BG 多线性定理窄得多，但仓库内仍未给出该能量估计的自足证明。

```text
divisor_weighted_to_unweighted_reduction_closed=true
unweighted_reciprocal_interval_energy_proved=false
row_column_unconditional_closed=false
```

## 1. 纯计数核心

| field | value |
| --- | --- |
| `set` | B=J^{-1}={n^{-1} mod P: n in J} |
| `collar` | J is a dyadic interval with \|J\|=N and P^(1/2)/log^236(P)<=N<=P^(1/2)log^236(P) |
| `unweighted_energy` | E_+(B)=#{b1+b2=b3+b4 mod P: bi in B} |
| `equivalent_original_variables` | #{n1^(-1)+n2^(-1)=n3^(-1)+n4^(-1) mod P: ni in J} |
| `weighted_transfer` | E_+(B;beta)<=log^C(P) E_+(B) for divisor-bounded Vaughan weights after dyadic level splitting |
| `sufficient_unweighted_bound` | E_+(J^{-1}) <= \|J\|^3/log^(472+C_weight)(P) |
| `why_this_is_narrower_than_bg` | It is a single reciprocal-interval four-tuple energy estimate, not the full BG multilinear theorem. |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WeightedEnergyTargetActive` | `true` | `true` | 上一证书已把平衡颈部压成加权倒数区间加性能量输入。 | WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23 |
| `PreviousL2EnergyReductionClosed` | `true` | `true` | Cauchy/L2/correlation/Plancherel 归约已经闭合，能量输入的所需 log 指数为 472。 | WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23 |
| `DivisorWeightedToUnweightedReductionClosed` | `true` | `true` | Vaughan/divisor-bounded 权重可由 dyadic level splitting 与 RKS 对数账本吸收。 | UnweightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23 |
| `IncidenceSumProductRouteRecovered` | `true` | `true` | 旧材料已定位 Rudnev/RNRS/sum-product 能量路线；它正对应当前纯四元组核心。 | RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving |
| `UnweightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23` | `false` | `false` | 尚未在仓库内给出 `E_+(J^{-1}) <= \|J\|^3/log^(472+C)(P)` 的自足证明。 | RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving OR SelfContainedBourgainGaraevSumProductEnergyProofForRKS23BalancedCollar |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只去权重并固定纯计数核心；行/列无条件闭合仍不能声明。 | UnweightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23 |

## 3. 下一最窄自足目标

```text
UnweightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23
```
