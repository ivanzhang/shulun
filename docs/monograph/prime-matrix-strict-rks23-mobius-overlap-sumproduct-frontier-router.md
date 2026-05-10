# Prime Matrix strict RKS2/RKS3 Möbius 重叠到反演 sum-product 前沿证书

**状态：** `mobius_overlap_spectrum_reduced_to_inverse_sumproduct_energy_frontier`

一参数 Möbius 高重叠谱已进一步压缩为反演 sum-product 核心：`sum_s r_J(s)^2` 正是 `A=J^{-1}` 的加性能量，而 `A^{-1}=J` 是区间，所以反演侧天然有 `|A^{-1}+A^{-1}|<=2|A|-1` 的小和集刚性。因此当前真正内部自足剩余是证明：在平方根对数颈部，反演小和集集合不可能有 `E_+(A)` 的近最大能量。该输入可由 RNRS/Rudnev 型外部 sum-product 能量定理关闭；严格自足线仍需把这一定理或其特殊情形内联证明。

```text
energy_mobius_sumproduct_dictionary_closed=true
inverse_small_doubling_rigidity_closed=true
self_contained_inverse_sumproduct_proved=false
row_column_unconditional_closed=false
```

## 1. 反演 sum-product 字典

| field | value |
| --- | --- |
| `original_spectrum` | r_J(s)=#{a in J: a/(s*a-1) in J} |
| `fiber_equation` | s*a*b-a-b=0, equivalently s=a^(-1)+b^(-1) |
| `energy_identity` | sum_s r_J(s)^2 = E_+(J^(-1)) |
| `cross_multiplied_quadruple` | (a+b)c d=(c+d)a b mod P |
| `set_substitution` | A=J^(-1) |
| `inverse_small_sumset` | A^(-1)=J, hence \|A^(-1)+A^(-1)\|<=2\|J\|-1 |
| `needed_power_saving` | E_+(A)<=\|A\|^(3-delta) for \|A\| in the square-root log collar |
| `contradiction_shape` | large E_+(A) plus small \|A^(-1)+A^(-1)\| is exactly the inverse sum-product obstruction |

## 2. 恒等式自检

| p | start | length | E_pair | E_mobius | E_cross | pass |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 101 | 13 | 10 | 270 | 270 | 270 | `true` |
| 211 | 17 | 14 | 506 | 506 | 506 | `true` |
| 509 | 25 | 22 | 1450 | 1450 | 1450 | `true` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MobiusOverlapSpectrumTargetActive` | `true` | `true` | 上一证书已把唯一内部剩余压成一参数 Möbius 区间重叠谱。 | OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving |
| `EnergyMobiusSumProductDictionaryClosed` | `true` | `true` | `r_J(s)`、`E_+(J^{-1})` 与交叉乘法四元组完全等价；小素数只作恒等式自检。 | dictionary closed |
| `InverseSmallDoublingRigidityClosed` | `true` | `true` | 令 `A=J^{-1}` 后，`A^{-1}=J` 是区间，故反演侧和集大小至多 `2\|J\|-1`。 | SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar |
| `ElementaryWeilCompletionBarrierConfirmed` | `true` | `true` | 已有账本确认平方根临界颈部中 Weil/双完成只能给自然尺度，不能给固定幂节省。 | SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar |
| `RNRSRudnevExternalRouteMatches` | `true` | `true` | Roche-Newton/Rudnev/Shkredov 型反演 sum-product 能量估计正匹配该硬点。 | RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving |
| `SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar` | `false` | `false` | 仓库内尚未内联证明反演小和集情形的固定幂加性能量节省。 | internalize inverse sum-product or accept RNRS/Rudnev route |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是字典与刚性定位，不是反演 sum-product 定理本身。 | SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar |

## 4. 下一最窄自足目标

```text
SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar
```
