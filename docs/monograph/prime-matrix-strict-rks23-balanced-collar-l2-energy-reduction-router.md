# Prime Matrix strict RKS2/RKS3 平衡颈部 L2/能量归约证书

**状态：** `balanced_collar_reduced_to_weighted_reciprocal_interval_additive_energy`

当前唯一内部自足线继续缩窄：RKS2/RKS3 对数平衡颈部不必再表述成泛泛的 BG 重证。对 alpha 侧 Cauchy 后，只需证明倒数区间 `J^{-1}` 的 divisor-bounded 加权加性能量 `E_+<=|J|^3/log^472(P)`，即可经 Plancherel 推出 L2 restriction `log^-236`，再推出原始双线性和 `log^-118`。这个能量输入正是 BG/sum-product 或 Baker 大谱平均的核心位置；当前仍未证明。

```text
cauchy_to_l2_restriction_reduction_closed=true
l2_to_correlation_kernel_expansion_closed=true
plancherel_energy_transfer_closed=true
weighted_reciprocal_interval_energy_input_proved=false
row_column_unconditional_closed=false
```

## 1. 精确归约链

| field | value |
| --- | --- |
| `balanced_bilinear_sum` | S=sum_{m in I}sum_{n in J} alpha_m beta_n e_P(xi*(mn)^(-1)), MN≈P |
| `balanced_collar` | P^(1/2)/log^236(P) <= M,N <= P^(1/2)log^236(P) |
| `cauchy_l2_target` | R_I(beta)=sum_{a in I^{-1}} \|sum_{b in J^{-1}} beta_b e_P(xi*a*b)\|^2 <= \|I\|\|J\|^2/log^236(P) |
| `correlation_expansion` | R_I(beta)=sum_h C_J(h) K_I(xi*h), with C_J(h)=sum_{b1-b2=h} beta_b1 conjugate(beta_b2) |
| `plancherel_energy_transfer` | offdiag <= E_+(J^{-1};beta)^(1/2) * (P\|I\|)^(1/2) |
| `sufficient_energy_input` | E_+(J^(-1);beta) <= \|J\|^3/log^472(P), plus charged divisor losses |
| `output_if_input_holds` | \|S\| <= MN/log^118(P) on every balanced RKS2/RKS3 collar block |
| `diagonal_absorption` | h=0 term is O(\|I\|\|J\|log^C P), smaller than \|I\|\|J\|^2/log^236(P) in the collar for large P |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BalancedCollarTargetActive` | `true` | `true` | 上一证书已把唯一内部硬点压到 RKS2/RKS3 的对数平衡颈部。 | SelfContainedBGRKS2RKS3LogBalancedCollarSumProductEnergySaving |
| `ExactLog118BilinearTargetImported` | `true` | `true` | 双线性目标 `\|S\|<=MN/log^118(P)` 已由前序精确定理固定。 | target imported |
| `CauchyToL2RestrictionReductionClosed` | `true` | `true` | 对 alpha 侧 Cauchy 后，问题化为倒数频率集 `I^{-1}` 上的 beta-Fourier L2 restriction。 | L2 restriction ledger |
| `L2ToCorrelationKernelExpansionClosed` | `true` | `true` | L2 restriction 展开为 `J^{-1}` 的差分相关 `C_J(h)` 与 `I^{-1}` 的短倒数和 `K_I(h)` 的耦合。 | correlation-kernel identity |
| `PlancherelEnergyTransferClosed` | `true` | `true` | 再用 Cauchy 与 Plancherel，得到加性能量输入足以推出所需 L2 节省。 | WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23 |
| `HistoricalEnergyRouteRecovered` | `true` | `true` | 旧 Baker/BG 研究中的 DFI-4、Rudnev、sum-product、能量路线与当前颈部核一致。 | SelfContainedBourgainGaraevSumProductEnergyProofForRKS23BalancedCollar OR BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23` | `false` | `false` | 仍未证明 divisor-bounded 加权倒数区间的 `log^-472` 加性能量节省。 | SelfContainedBourgainGaraevSumProductEnergyProofForRKS23BalancedCollar OR BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是归约链，不是能量输入本身；不能宣称行/列无条件闭合。 | WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23 |

## 3. 下一最窄自足目标

```text
WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23
```
