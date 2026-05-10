# Prime Matrix strict RKS2/RKS3 微薄边质量路由证书

**状态：** `microscopic_thin_side_reduced_to_endpoint_strip_weighted_packing_ledger`

微薄边分支的解析部分已被压到底：对最短边做 Plancherel 后，`H_min<P^kappa` 的所有包贡献由四个带权短边和控制，形式为 `sum_{H_s<T} H_s*prod_{j!=s}H_j^2`。因此剩余不再是角色和估计，而是一个精确的 Whitney/端点 strip packing 账本：必须证明微薄边 strip 的带权总质量相对 Cauchy 尺度有固定幂余量。已有 bounded-overlap 不能替代它，因为 Plancherel 后短边只剩一个 `H_s` 幂。

```text
packetwise_analytic_reduction_to_weighted_side_ledger_closed=true
endpoint_strip_source_identified_from_rectangularization=true
raw_bounded_overlap_insufficient=true
microscopic_side_whitney_packing_mass_ledger_proved=false
endpoint_strip_multiplicity_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 定义

| field | value |
| --- | --- |
| `packet` | Q=(I1,I2,I3,I4) with side lengths H_j=\|I_j\| |
| `micro_cutoff` | T=P^kappa, with fixed kappa>0 chosen below the needed packing margin |
| `microscopic_condition` | H_min(Q)=min_j H_j<T |
| `packet_l2` | L(Q)=(1/(P-1))*sum_{chi!=chi0} prod_j \|S_Ij(chi)\|^2 |
| `cauchy_scale` | the centered product-ratio L2 scale required by the earlier Cauchy reduction |
| `allowed_losses` | dyadic and endpoint labels may cost only P^o(1), already registered as polylog losses |

## 2. 解析归约

| field | value |
| --- | --- |
| `shortest_side_plancherel` | if H_s=H_min(Q), then L(Q)<=H_s*prod_{j!=s} H_j^2 |
| `micro_union_bound` | sum_{Q:H_min<T} L(Q) <= sum_{s=1}^4 sum_{Q:H_s<T} H_s*prod_{j!=s} H_j^2 |
| `exact_remaining_ledger` | prove sum_s sum_{Q:H_s<T} H_s*prod_{j!=s}H_j^2 <= CauchyScale*P^(-eta) after polylog losses |
| `conditional_closure` | this weighted side ledger immediately absorbs all microscopic thin packets |
| `why_this_is_narrow` | no character cancellation remains in the micro branch after this reduction |

## 3. 不能闭合的原因

| field | value |
| --- | --- |
| `naive_small_length_fails` | H_s<T alone does not give fixed power saving when H_s is O(1) |
| `bounded_overlap_fails` | bounded overlap controls packet membership, not the one-power weighted sum H_s*prod_{j!=s}H_j^2 |
| `natural_mass_mismatch` | natural packet mass has H_s^2, while the Plancherel bound has only H_s |
| `possible_bad_case` | many unit-width side packets repeated across endpoint phases can saturate the Cauchy scale unless strip multiplicity is bounded |
| `therefore_needed` | EndpointStripMultiplicityBoundForMicroscopicProductPackets |

## 4. 下一个最窄几何输入

| field | value |
| --- | --- |
| `source` | the previous rectangularization splits by signs, parity, and distances to strip boundaries |
| `required_structure` | every H_s<T packet must be charged to an endpoint/boundary strip of comparable width with bounded signed multiplicity |
| `sufficient_bound` | for each side s and T=P^kappa, the total weighted strip mass is <= CauchyScale*P^(-eta) for some eta>0 |
| `model_margin` | if the ambient side scale is P^theta and endpoint strips have total width O(T*P^o(1)), then any theta>kappa gives fixed power room |
| `unproved_part` | the current corpus has not registered the endpoint-strip multiplicity and ambient-scale margin with exact constants |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MicroscopicThinSideAtomActive` | `true` | `true` | 上一证书已把薄包唯一剩余隔离为 `H_min<P^kappa` 的微薄边包。 | MicroscopicThinSidePacketMassAbsorptionAtCauchyScale |
| `NonmicroscopicComplementAlreadyAbsorbed` | `true` | `true` | 非微观薄包已由最短边 Plancherel 地板吸收。 | absorbed |
| `PacketwiseAnalyticReductionToWeightedSideLedgerClosed` | `true` | `true` | 对最短边做 Plancherel 后，微薄包总贡献被精确压到 `H_s*prod_{j!=s}H_j^2` 的带权短边账本。 | MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale |
| `FourSideUnionBoundClosed` | `true` | `true` | `H_min<T` 被四个事件 `H_s<T` 覆盖，只损失常数 4。 | MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale |
| `EndpointStripSourceIdentifiedFromRectangularization` | `true` | `true` | 已有矩形化说明短边来自符号、奇偶和边界距离拆包；真正需要的是端点 strip 重数账本。 | EndpointStripMultiplicityBoundForMicroscopicProductPackets |
| `RawBoundedOverlapInsufficient` | `true` | `true` | 已有 bounded-overlap/polylog 只控制拆包数，不能替代 `H_s` 单幂带权质量下界。 | EndpointStripMultiplicityBoundForMicroscopicProductPackets |
| `MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale` | `false` | `false` | 仓库内尚未证明微薄边带权 Whitney packing 质量相对 Cauchy 尺度有固定幂余量。 | EndpointStripMultiplicityBoundForMicroscopicProductPackets |
| `EndpointStripMultiplicityBoundForMicroscopicProductPackets` | `false` | `false` | 仓库内尚未给出每个微薄边端点/边界 strip 的严格重数和环境尺度余量。 | EndpointStripMultiplicityBoundForMicroscopicProductPackets |
| `ThinDyadicPacketMassAbsorptionProved` | `false` | `false` | 薄包分支需要非微观吸收与微薄边账本同时成立；当前只完成前者和解析归约。 | MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale |
| `BurgessPointwiseInputStillOpen` | `true` | `false` | 大包分支的 Burgess 点态角色和输入仍是并行开放项。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步是内部自足线的微薄边压缩证书，不宣称行/列命题无条件闭合。 | EndpointStripMultiplicityBoundForMicroscopicProductPackets AND SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 6. 下一最窄自足目标

```text
EndpointStripMultiplicityBoundForMicroscopicProductPackets
```

审稿边界：本证书只关闭微薄边的解析归约和精确账本定位；没有证明端点 strip 重数账本，
没有内部化 Burgess 点态输入，也不声明行/列命题无条件闭合。
