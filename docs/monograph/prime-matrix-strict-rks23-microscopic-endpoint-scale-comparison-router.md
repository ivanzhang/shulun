# Prime Matrix strict RKS2/RKS3 微薄端点尺度比较证书

**状态：** `microscopic_endpoint_scale_comparison_reduced_to_registered_side_multiplier_floor`

微薄端点尺度比较继续缩窄。端点 strip 重数已给 `P^o(1)*T*TripleSideSquareMass_s`；若 Cauchy 尺度中同一侧登记了 `CauchyScale_s>=A_s*TripleSideSquareMass_s`，则比较只需 `A_s` 大于 `T` 一个固定幂。已有平方根颈部给 `|J|>=P^(1/2)/log^236(P)`，所以只要该环境尺度确实注册为每个微薄端点兼容侧的 Cauchy 乘子，任意 `kappa<1/2` 都能支付微观宽度。当前唯一剩余因此压成侧向乘子地板的注册问题。

```text
side_multiplier_normalization_closed=true
kappa_below_half_power_margin_algebra_closed=true
registered_endpoint_side_cauchy_multiplier_floor_proved=false
microscopic_endpoint_strip_cauchy_scale_comparison_proved=false
row_column_unconditional_closed=false
```

## 1. 归一化

| field | value |
| --- | --- |
| `post_multiplicity_bound` | micro contribution <= P^o(1)*T*TripleSideSquareMass_s |
| `needed_comparison` | P^o(1)*T*TripleSideSquareMass_s <= CauchyScale_s*P^(-eta) |
| `side_multiplier_definition` | CauchyScale_s >= A_s*TripleSideSquareMass_s |
| `equivalent_floor` | need A_s >= T*P^(eta+o(1)) |
| `new_atomic_floor` | RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets |
| `why_this_is_exact` | after cancelling the common TripleSideSquareMass_s, only the side multiplier A_s remains |

## 2. 颈部幂余量

| field | value |
| --- | --- |
| `collar_lower_bound` | \|J\|>=P^(1/2)/log^236(P) |
| `micro_width` | T=P^kappa |
| `parameter_choice` | fix any kappa<1/2 and then take eta<(1/2-kappa) |
| `algebra` | T/(P^(1/2)/log^236 P)=P^{kappa-1/2}log^236(P)=P^{-eta-o(1)} |
| `large_p_absorption` | fixed log powers are absorbed by the positive gap 1/2-kappa |
| `finite_transition` | small P remains in the existing finite/P0 lane once constants are supplied |

## 3. 新最窄输入

| field | value |
| --- | --- |
| `name` | RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets |
| `statement` | for each microscopic endpoint-compatible side s, the Cauchy-scale ledger contains a side multiplier A_s with A_s >= P^(1/2)/log^236(P), or an equivalent registered floor |
| `why_needed` | pure strip multiplicity gives T, but only this floor compares T to the actual Cauchy scale |
| `not_currently_in_corpus` | existing files state root-box collar scale, but do not yet bind that scale to every endpoint-compatible side multiplier A_s |
| `what_would_close` | this floor plus the power-margin algebra closes the microscopic endpoint scale comparison |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MicroscopicEndpointScaleComparisonActive` | `true` | `true` | 上一证书已把微薄边剩余压成 `T*TripleSideSquareMass_s` 与 CauchyScale 的比较。 | MicroscopicEndpointStripCauchyScaleComparisonForWeightedSideMass |
| `SquareRootCollarFloorImported` | `true` | `true` | RKS23 平衡颈部已有 `\|J\|>=P^(1/2)/log^236(P)` 的环境尺度下界。 | collar ledger |
| `SideMultiplierNormalizationClosed` | `true` | `true` | 把 CauchyScale 写作 `A_s*TripleSideSquareMass_s` 后，尺度比较等价于侧向乘子地板。 | RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets |
| `KappaBelowHalfPowerMarginAlgebraClosed` | `true` | `true` | 若 `A_s>=P^(1/2)/log^236(P)` 且 `T=P^kappa,kappa<1/2`，则 `T/A_s` 有固定幂节省。 | RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets |
| `RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets` | `false` | `false` | 仓库内尚未把平方根颈部环境尺度注册为每个微薄端点兼容侧的 Cauchy 乘子 `A_s`。 | RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets |
| `MicroscopicEndpointStripCauchyScaleComparisonForWeightedSideMass` | `false` | `false` | 尺度比较需要侧向乘子地板；当前只闭合了归一化和幂余量代数。 | RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets |
| `MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale` | `false` | `false` | 微薄边总质量吸收仍等待侧向乘子地板。 | RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets |
| `BurgessPointwiseInputStillOpen` | `true` | `false` | 大包分支 Burgess 点态输入仍为并行开放项。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只关闭尺度比较的代数归一化，不关闭行/列无条件命题。 | RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets AND SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 5. 下一最窄自足目标

```text
RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets
```

审稿边界：本证书只关闭尺度比较的侧向归一化和 `kappa<1/2` 的幂余量代数；
尚未证明端点兼容侧向 Cauchy 乘子地板，也不声明薄包或行/列命题闭合。
