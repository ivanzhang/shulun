# Prime Matrix strict RKS2/RKS3 角色矩 Burgess 阈值分解证书

**状态：** `four_interval_character_moment_split_into_large_burgess_packets_and_thin_packets`

四短区间非主角色乘积矩进一步压成 Burgess 阈值二分。在四个区间都长于 `P^(1/4+epsilon)` 的大包分支中，只要内部化 Burgess 点态角色和节省，就可直接推出固定幂矩节省。所有剩余包对必含一个短于 Burgess 阈值的薄边；这部分不能凭直觉丢弃，还需要一个 Cauchy 尺度下的薄包总质量吸收账本。因此当前自足闭合还剩两个具体子输入：大包 Burgess 内部化与薄包质量吸收。

```text
dyadic_side_length_ledger_closed=true
burgess_large_packet_implication_closed=true
burgess_pointwise_input_internalized=false
thin_dyadic_packet_mass_absorption_proved=false
four_interval_character_moment_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 阈值二分

| field | value |
| --- | --- |
| `four_intervals` | A0,A1,B0,B1 from one dyadic rectangular packet pair |
| `side_lengths` | H_A0,H_A1,H_B0,H_B1 |
| `burgess_threshold` | H_i >= P^(1/4+epsilon_B) for all four sides |
| `large_packet_branch` | all four intervals are above the Burgess threshold |
| `thin_packet_branch` | at least one side is below P^(1/4+epsilon_B) |
| `dichotomy` | every packet pair lies in exactly one of these branches |
| `polylog_loss` | dyadic packet counting contributes only P^o(1), harmless after any fixed power saving |

## 2. 大包 Burgess 分支

| field | value |
| --- | --- |
| `assumed_pointwise_input` | for every nonprincipal chi and every interval I with \|I\|>=P^(1/4+epsilon_B), \|S_I(chi)\|<=\|I\| P^(-delta_B) |
| `moment` | sum_{chi!=chi0}\|S_A0 S_A1 S_B0 S_B1\|^2 |
| `direct_sup_bound` | using the pointwise input on all four factors gives <= P * prod_i \|I_i\|^2 * P^(-8 delta_B) |
| `normalized_l2` | after the 1/(P-1) Plancherel factor this gives prod_i \|I_i\|^2 * P^(-8 delta_B+o(1)) |
| `consequence` | large packets satisfy the fixed-power centered convolution L2 saving |
| `not_yet_internal` | the current corpus has not supplied a self-contained Burgess proof with constants for all packet intervals |

## 3. 薄包分支

| field | value |
| --- | --- |
| `definition` | some side length H_i<P^(1/4+epsilon_B) |
| `why_not_automatic` | a thin side reduces packet mass, but without an explicit Cauchy-scale mass ledger it cannot be discarded |
| `needed_ledger` | sum all thin packet-pair contributions and prove they are below the required centered L2 scale by a fixed power |
| `possible_routes` | geometric packing of Whitney boundary boxes OR a direct small-side divisor/energy estimate |
| `current_status` | not proved in the current corpus |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FourIntervalCharacterMomentHardpointActive` | `true` | `true` | 上一证书已把剩余固定为非主角色四短区间乘积矩。 | FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving |
| `DyadicSideLengthLedgerClosed` | `true` | `true` | 每个矩形包对有四个边长，可按 Burgess 阈值做互斥分支。 | BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment |
| `BurgessLargePacketImplicationClosed` | `true` | `true` | 若四个边长均超过 `P^(1/4+epsilon)` 且 Burgess 点态界可用，则该包对的角色矩有固定幂节省。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |
| `BurgessPointwiseInputInternalized` | `false` | `false` | 仓库内尚未给出适配全部 dyadic 包的自足 Burgess 点态证明与常数账本。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |
| `ThinPacketBranchIsOnlyNonBurgessBranch` | `true` | `true` | 不满足大边长条件的包对必含一个 Burgess 阈值以下的短边。 | ThinDyadicRectanglePacketMassAbsorptionAtCauchyScale |
| `ThinDyadicPacketMassAbsorptionProved` | `false` | `false` | 仓库内尚未证明所有薄包对总贡献在 Cauchy 尺度下可固定幂吸收。 | ThinDyadicRectanglePacketMassAbsorptionAtCauchyScale |
| `BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment` | `false` | `false` | 需要同时内部化大包 Burgess 输入并完成薄包质量吸收，才能闭合四区间角色矩。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals AND ThinDyadicRectanglePacketMassAbsorptionAtCauchyScale |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是 Burgess 阈值分解和大包充分推导，不是最终角色矩节省。 | BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment |

## 5. 下一最窄自足目标

```text
BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment
```
