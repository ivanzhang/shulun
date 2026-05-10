# Prime Matrix strict RKS2/RKS3 薄包 Plancherel 地板证书

**状态：** `nonmicroscopic_thin_packets_absorbed_microscopic_side_packets_remain`

薄包分支已经进一步缩窄。设四个边长为 `H_j`，最短边为 `H_min`。对最短边用乘法角色 Plancherel、其余三边用平凡上界，得到归一化 L2 `<= (prod H_j^2)/H_min`。因此只要 `H_min>=P^kappa`，就有 `P^-kappa` 固定幂节省，非微观薄包可内部吸收。真正剩余只剩 `H_min<P^kappa` 的微薄边包总质量账本；同时大包分支的 Burgess 点态输入仍需单独内部化。

```text
shortest_side_plancherel_estimate_closed=true
nonmicroscopic_thin_packets_absorbed=true
microscopic_thin_packets_isolated=true
microscopic_thin_side_packet_mass_absorption_proved=false
burgess_pointwise_input_still_open=true
row_column_unconditional_closed=false
```

## 1. 薄包地板分解

| field | value |
| --- | --- |
| `four_intervals` | I1,I2,I3,I4 = A0,A1,B0,B1 |
| `side_lengths` | H_j=\|I_j\| and H_min=min_j H_j |
| `burgess_upper_thin_condition` | thin branch has H_min<P^(1/4+epsilon_B) |
| `new_power_floor` | choose fixed kappa>0; split thin packets by H_min>=P^kappa or H_min<P^kappa |
| `nonmicroscopic_thin_packet` | P^kappa <= H_min < P^(1/4+epsilon_B) |
| `microscopic_thin_packet` | H_min<P^kappa |
| `why_this_is_narrower` | all fixed-power-length thin packets are absorbed by Plancherel; only microscopic side packets remain |

## 2. 最短边 Plancherel 估计

| field | value |
| --- | --- |
| `moment` | M=sum_{chi!=chi0}\|S_I1(chi)S_I2(chi)S_I3(chi)S_I4(chi)\|^2 |
| `plancherel_on_shortest_side` | sum_chi \|S_min(chi)\|^2 <= (P-1)H_min |
| `trivial_on_other_sides` | \|S_I(chi)\|<=H_I |
| `raw_bound` | M <= (P-1) H_min * prod_{j!=min} H_j^2 |
| `normalized_l2_bound` | (1/(P-1))M <= H_min * prod_{j!=min} H_j^2 |
| `relative_to_natural_packet_scale` | H_min * prod_{j!=min} H_j^2 = (prod_j H_j^2)/H_min |
| `fixed_power_saving` | if H_min>=P^kappa then normalized L2 <= prod_j H_j^2 * P^(-kappa) |
| `conclusion` | nonmicroscopic thin packets satisfy the Cauchy-scale fixed-power saving without Burgess |

## 3. 剩余

| field | value |
| --- | --- |
| `microscopic_side_problem` | prove the total contribution of packet pairs with H_min<P^kappa is absorbable |
| `why_not_closed_here` | when H_min is below every fixed power, the Plancherel gain 1/H_min is not a fixed power |
| `possible_next_routes` | Whitney packing mass ledger, endpoint strip counting, or divisor-energy estimate for microscopic sides |
| `global_parallel_open` | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ThinPacketSubatomActive` | `true` | `true` | 上一证书已把闭合义务之一固定为薄包总质量吸收。 | ThinDyadicRectanglePacketMassAbsorptionAtCauchyScale |
| `ShortestSidePlancherelEstimateClosed` | `true` | `true` | 对最短边用角色 Plancherel，其余边用平凡上界，得到 `prod H_j^2/H_min`。 | nonmicroscopic thin packets |
| `NonmicroscopicThinPacketsAbsorbed` | `true` | `true` | 若 `H_min>=P^kappa`，则相对自然包尺度得到 `P^-kappa` 固定幂节省。 | absorbed |
| `MicroscopicThinPacketsIsolated` | `true` | `true` | 薄包中唯一未被该初等 Plancherel 估计吸收的是 `H_min<P^kappa` 的微薄边包。 | MicroscopicThinSidePacketMassAbsorptionAtCauchyScale |
| `MicroscopicThinSidePacketMassAbsorptionAtCauchyScale` | `false` | `false` | 仓库内尚未证明微薄边包对的总贡献可在 Cauchy 尺度下固定幂吸收。 | WhitneyBoundaryPacking OR MicroscopicSideDivisorEnergy |
| `BurgessPointwiseInputStillOpen` | `true` | `false` | 大包分支仍需自足 Burgess 点态角色和输入；本证书只推进薄包分支。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |
| `ThinDyadicPacketMassAbsorptionProved` | `false` | `false` | 薄包分支已去掉非微观部分，但微薄边总质量账本尚未完成。 | MicroscopicThinSidePacketMassAbsorptionAtCauchyScale |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是非微观薄包吸收，不是 Burgess 阈值总闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals AND MicroscopicThinSidePacketMassAbsorptionAtCauchyScale |

## 5. 下一最窄自足目标

```text
MicroscopicThinSidePacketMassAbsorptionAtCauchyScale
```
