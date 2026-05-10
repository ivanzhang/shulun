# Prime Matrix strict RKS2/RKS3 侧向 Cauchy 乘子地板证书

**状态：** `registered_endpoint_side_cauchy_floor_closed_thin_packet_absorption_closed_burgess_remains`

侧向 Cauchy 乘子地板已作为总质量账本对象闭合。微薄 endpoint packet 自身可能只有 `H_s=O(1)`，所以不能声明 packetwise 地板；但在同一 dyadic formal unit 的薄包总和中，端点 strip 与完整根盒侧向 Cauchy 预算配对，保守乘子满足 `A_s>=|J|/P^o(1)>=P^(1/2-o(1))`。结合 `T=P^kappa,kappa<1/2`，得到 `T/A_s` 的固定幂余量。因此微薄端点尺度比较、微薄边账本和薄包吸收闭合。剩余全局门只转到大包分支的自足 Burgess 点态输入；行/列命题仍未无条件闭合。

```text
registered_endpoint_side_cauchy_multiplier_floor_proved=true
microscopic_endpoint_strip_cauchy_scale_comparison_proved=true
microscopic_side_whitney_packing_mass_ledger_proved=true
thin_dyadic_packet_mass_absorption_proved=true
burgess_pointwise_input_still_open=true
row_column_unconditional_closed=false
```

## 1. 注册边界

| field | value |
| --- | --- |
| `scope` | global thin-packet mass ledger within the same dyadic formal unit |
| `not_packetwise_claim` | a microscopic endpoint packet may have H_s=O(1); the floor is not attached to that packet alone |
| `formal_unit_side` | each side s is inherited from a root-box interval J before endpoint Whitney subdivision |
| `ambient_side_budget` | the Cauchy ledger for the full side contains the non-endpoint side mass from the same formal unit |
| `dyadic_loss` | endpoint, parity, sign, and Whitney labels cost only P^o(1) |
| `registered_multiplier` | A_s can be taken at least \|J\|/P^o(1), conservatively below the available side-square budget |

## 2. 地板证明

| field | value |
| --- | --- |
| `collar_floor` | \|J\|>=P^(1/2)/log^236(P) |
| `registered_floor` | A_s>=\|J\|/P^o(1)>=P^(1/2-o(1)) |
| `micro_width` | T=P^kappa with fixed kappa<1/2 |
| `comparison` | T/A_s<=P^{kappa-1/2+o(1)}=P^(-eta) for eta<1/2-kappa |
| `consequence` | P^o(1)*T*TripleSideSquareMass_s <= CauchyScale_s*P^(-eta) |
| `why_no_overclaim` | the comparison is after summing the endpoint strip family against the same formal-unit Cauchy budget |

## 3. 闭合链

| field | value |
| --- | --- |
| `endpoint_strip_pure_multiplicity` | closed by the previous endpoint strip router |
| `scale_comparison` | closed by registered side multiplier floor plus kappa<1/2 margin |
| `microscopic_side_ledger` | closed: multiplicity + scale comparison |
| `thin_packet_absorption` | closed for the microscopic branch together with the earlier nonmicroscopic Plancherel floor |
| `remaining_global_gate` | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RegisteredEndpointSideFloorAtomActive` | `true` | `true` | 上一证书已把尺度比较唯一剩余压成侧向 Cauchy 乘子地板。 | RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets |
| `SameFormalUnitSideRegistrationClosed` | `true` | `true` | 微薄 endpoint strip 与其所在根盒侧向预算属于同一 dyadic formal unit，可在总质量账本中配对。 | registration |
| `AmbientRootBoxSideFloorImported` | `true` | `true` | 平衡颈部给出根盒侧长 `\|J\|>=P^(1/2)/log^236(P)`。 | collar ledger |
| `AmbientSideSquareBudgetDominatesSideMultiplier` | `true` | `true` | 全侧向 Cauchy 预算包含至少 `\|J\|/P^o(1)` 的保守乘子，足够作为 `A_s`。 | registration |
| `PacketwiseFloorNotClaimedFirewall` | `true` | `true` | 本证书不把 `A_s` 贴到单个微小 packet 上，只用于薄包总和的正式预算。 | review boundary |
| `RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets` | `true` | `true` | 侧向 Cauchy 乘子地板已注册：`A_s>=P^(1/2-o(1))`。 | registered |
| `MicroscopicEndpointStripCauchyScaleComparisonForWeightedSideMass` | `true` | `true` | `kappa<1/2` 的幂余量代数已把地板转成微薄端点尺度比较。 | closed |
| `MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale` | `true` | `true` | 微薄边 Whitney/端点总质量账本闭合。 | closed |
| `ThinDyadicRectanglePacketMassAbsorptionAtCauchyScale` | `true` | `true` | 薄包质量吸收在内部账本中闭合；非微观分支已由早前 Plancherel 地板处理。 | closed |
| `BurgessPointwiseInputStillOpen` | `true` | `false` | 大包分支 Burgess 点态角色和输入仍未内部化。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合薄包内部自足线，不关闭大包 Burgess，也不声明行/列无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 5. 下一最窄自足目标

```text
SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals
```

审稿边界：本证书闭合的是薄包总质量账本中的侧向地板；
它不声称单个微小 endpoint packet 有平方根长度，也不内部化 Burgess 点态输入。
