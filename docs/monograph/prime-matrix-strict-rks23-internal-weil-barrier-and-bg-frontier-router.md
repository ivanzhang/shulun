# Prime Matrix strict RKS2/RKS3 内部 Cauchy-Weil 屏障与 BG 前沿证书

**状态：** `rks23_internal_frontier_reduced_to_log_balanced_bg_collar`

唯一内部自足硬点没有换题，而是进一步缩窄：RKS2/RKS3 的双线性或分组多线性块中，若某个二分组相对 `P^(1/2)` 偏离至少 `log^236(P)`，一次 Cauchy-Weil 的平方根损失已经足以支付 `log^-118(P)`。真正不能由这种内部初等谱估计处理的，只剩 `M,N` 都落在 `P^(1/2) log^±236(P)` 的对数平衡颈部。该颈部正是 BG/sum-product 能量定理或 Baker 大谱平均必须进入的位置；当前仍未证明，所以行/列无条件闭合仍不能宣称。

```text
exact_log118_input_imported=true
elementary_cauchy_weil_computation_closed=true
balanced_collar_is_only_deep_part=true
self_contained_bg_balanced_collar_proved=false
row_column_unconditional_closed=false
```

## 1. Cauchy-Weil 可达边界

| field | value |
| --- | --- |
| `bilinear_sum` | S(M,N)=sum_{m~M}sum_{n~N} a_m b_n e_P(xi*(mn)^(-1)), MN≈P |
| `one_sided_cauchy_weil_ratio` | \|S\|/(MN) << (1/N + P^(1/2)/M)^(1/2) |
| `symmetric_ratio` | \|S\|/(MN) << (1/M + P^(1/2)/N)^(1/2) |
| `needed_log_saving` | log^-118(P) |
| `log_separation_sufficient_schema` | if max(M,N) >= P^(1/2) log^236(P), the square-root loss can pay log^-118(P) up to absolute constants |
| `critical_collar` | P^(1/2)/log^236(P) <= M,N <= P^(1/2) log^236(P) |
| `balanced_barrier` | at M≈N≈P^(1/2), the elementary ratio is O(1), not log^-118 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RKS23BGHardpointActive` | `true` | `true` | 上一证书已把唯一内部硬点压成 RKS2/RKS3 的 BG 型倒数 Kloosterman 固定对数节省。 | SelfContainedBGRKS2RKS3ReciprocalKloostermanLogSaving |
| `ExactLog118InputImported` | `true` | `true` | 精确输入定理和 log^-118 目标已经固定。 | MultilinearReciprocalKloostermanFixedLogSavingForRKSBlocks |
| `ElementaryCauchyWeilComputationClosed` | `true` | `true` | 一次 Cauchy 加不完全倒数和 Weil 的可得边界已显式化。 | formula ledger closed |
| `PowerSeparatedBlocksReducedAway` | `true` | `true` | 若某个二分组远离平方根超过 log^236，平方根损失可支付 log^-118；深点只剩对数平衡颈部。 | SelfContainedBGRKS2RKS3LogBalancedCollarSumProductEnergySaving |
| `BalancedCauchyWeilBarrier` | `true` | `true` | 在 M≈N≈P^(1/2) 的临界颈部，Cauchy-Weil 只给 O(MN)，不能给固定对数节省。 | SelfContainedBourgainGaraevSumProductEnergyProofForRKS23BalancedCollar OR BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `BakerAverageStillOpen` | `true` | `true` | Baker 单频率结果不能直接通过绝对值后的 d/frequency coherent 平均。 | BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `SelfContainedBGRKS2RKS3LogBalancedCollarSumProductEnergySaving` | `false` | `false` | 严格内部自足证明仍需在对数平衡颈部补 BG/sum-product 能量节省，或补 Baker 大谱平均替代。 | SelfContainedBourgainGaraevSumProductEnergyProofForRKS23BalancedCollar OR BakerFrequencyLargeSieveOrDBGAverageReplacement |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只压缩内部剩余硬点，没有宣称无条件闭合。 | SelfContainedBGRKS2RKS3LogBalancedCollarSumProductEnergySaving |

## 3. 下一最窄自足目标

```text
SelfContainedBGRKS2RKS3LogBalancedCollarSumProductEnergySaving
```
