# Prime Matrix strict RKS2/RKS3 根定位判别式通道证书

**状态：** `discriminant_corridor_refined_to_root_localized_small_difference_phase_map`

判别式通道还必须加入根定位约束。设 `t=a+b`、`d=a-b`，则真实纤维不是单纯的 `Delta_c(t)` 为平方，而是小差盒中的 `d^2=t(t-4c) mod P`，等价于同一有理相位映射 `c=(t^2-d^2)/(4t)` 出现高重数。因此当前最窄剩余是证明该根定位小盒子映射没有固定幂级高重数；单纯二次字符平方返回路线和朴素分支除数路线都不足以闭合。

```text
root_localized_difference_identity_closed=true
quadratic_square_return_only_route_insufficient=true
root_localized_graph_box_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 根定位小差通道

| field | value |
| --- | --- |
| `variables` | t=a+b and d=a-b |
| `root_cut` | a=(t+d)/2 in J and b=(t-d)/2 in J |
| `small_difference_box` | \|d\|<=\|J\|-1 as an ordinary signed integer |
| `equation` | d^2=t(t-4c) mod P |
| `phase_map` | c=(t^2-d^2)/(4t) mod P |
| `fiber_form` | r_c is bounded by the number of (t,d) in the root-localized box with phase_map(t,d)=c |
| `high_fiber_implication` | r_c>N^(1-eta) forces one value of the harmonic-mean map to have >N^(1-eta) preimages in a thin (t,d) box |
| `same_target_preserved` | InteriorQuadraticDiscriminantCorridorHighSpectrumPowerSaving |

## 2. 路线审查

| field | value |
| --- | --- |
| `square_return_only` | insufficient |
| `reason` | Delta_c(t) being a quadratic residue normally occurs on about half of J+J; that is much larger than the desired N^(1-eta) high-spectrum threshold |
| `needed_extra_rigidity` | the square root must equal a small signed difference d=a-b with both reconstructed roots inside J |
| `plain_character_sum_role` | Burgess/Weil cancellation for chi(t(t-4c)) alone does not close the fiber problem |
| `branch_lift_barrier` | for middle interior c, the lift ab-c(a+b)=kP has O(max J) possible k, so per-branch divisor counting loses the required power |
| `next_method` | prove high-multiplicity exclusion for the rational map (t,d)->(t^2-d^2)/(4t) on the short root-localized box |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `InteriorDiscriminantTargetActive` | `true` | `true` | 上一证书已把剩余压成内部相位的判别式通道。 | InteriorQuadraticDiscriminantCorridorHighSpectrumPowerSaving |
| `RootLocalizedDifferenceIdentityClosed` | `true` | `true` | `a,b in J` 等价给出 `t=a+b` 与小差 `d=a-b`，并满足 `d^2=t(t-4c)`。 | RootLocalizedQuadraticGraphBoxFiberPowerSaving |
| `HarmonicMeanPhaseMapIdentityClosed` | `true` | `true` | 同一相位可写为 `c=(t^2-d^2)/(4t)`，剩余是该有理映射的小盒子高重数排斥。 | SmallDifferenceHarmonicMeanMapHighMultiplicityExclusion |
| `QuadraticSquareReturnOnlyRouteInsufficient` | `true` | `true` | 仅证明 `Delta_c(t)` 很少为平方不可能成立到所需强度；必须使用小差根定位。 | RootLocalizedQuadraticGraphBoxFiberPowerSaving |
| `MiddleInteriorBranchDivisorLiftBarrierQuantified` | `true` | `true` | 中心内部相位有多达 `O(max J)` 个整数分支，朴素分支除数界不能给固定幂节省。 | RootLocalizedQuadraticGraphBoxFiberPowerSaving |
| `RootLocalizedQuadraticGraphBoxFiberPowerSaving` | `false` | `false` | 仓库内尚未证明根定位有理相位映射在短盒子上的高重数固定幂排斥。 | SmallDifferenceHarmonicMeanMapHighMultiplicityExclusion |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步关闭的是通道精化和假捷径排除；最终高重数排斥仍未证明。 | RootLocalizedQuadraticGraphBoxFiberPowerSaving |

## 4. 下一最窄自足目标

```text
RootLocalizedQuadraticGraphBoxFiberPowerSaving
```
