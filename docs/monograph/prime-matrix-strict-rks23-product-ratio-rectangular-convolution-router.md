# Prime Matrix strict RKS2/RKS3 乘积比值矩形卷积证书

**状态：** `product_ratio_l2_hardpoint_reduced_to_dyadic_rectangular_ratio_convolution_l2`

八变量乘积比值能量的支撑现在被正规化：`a=d-e,b=d+e` 把根盒变成短线性根盒，按符号、奇偶和边界距离可拆成 `log^O(P)` 个矩形包。固定幂目标允许这种多对数损失。在每个矩形包对 `A0 x B0, A1 x B1` 上，交叉乘积比值谱不是黑箱对象，而是两个交叉短区间比值谱的乘法卷积。因此下一真正剩余是证明这些 dyadic 矩形卷积的中心化 L2 有 Cauchy 所需的固定幂节省。

```text
rotated_root_box_support_geometry_closed=true
dyadic_rectangularization_closed_up_to_polylog=true
rectangular_product_ratio_convolution_identity_closed=true
dyadic_rectangular_product_ratio_convolution_l2_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 支撑矩形化

| field | value |
| --- | --- |
| `product_coordinates` | a=d-e, b=d+e with d=(a+b)/2 and e=(b-a)/2 |
| `support_shape` | intersection of O(N)-scale linear strips, plus parity and endpoint restrictions |
| `nonzero_condition` | a*b!=0 after the zero-product diagonal has been peeled |
| `dyadic_cover` | split by signs, parity, and distances to strip boundaries into log^O(P) rectangular packets A_i x B_i |
| `bounded_overlap` | each original support point belongs to O(log^O(P)) packets, harmless for fixed-power targets |
| `energy_after_cover` | after expanding mu=sum_i mu_i, it is enough to prove the required L2 saving for every dyadic rectangular packet pair, losing only log^O(P) |
| `warning` | this is a support decomposition, not a cancellation estimate |

## 2. 矩形包卷积恒等式

| field | value |
| --- | --- |
| `rectangular_packet_pair` | R0=A0 x B0 and R1=A1 x B1, with Ai,Bi short intervals/progressions inside F_P^* |
| `a_cross_ratio_spectrum` | R_A0,A1(alpha)=#{(a0,a1) in A0 x A1: a1=alpha*a0} |
| `b_cross_ratio_spectrum` | R_B0,B1(beta)=#{(b0,b1) in B0 x B1: b1=beta*b0} |
| `product_cross_ratio_spectrum` | C_R0,R1(rho)=#{(r0,r1) in R0 x R1: a1*b1=rho*a0*b0} |
| `convolution_identity` | C_R0,R1 = R_A0,A1 *_mult R_B0,B1 |
| `centered_packet_pair` | C_R0,R1^circ(rho)=C_R0,R1(rho)-(\|R0\|*\|R1\|)/(P-1) |
| `packet_pair_l2_target` | sum_rho \|C_R0,R1^circ(rho)\|^2 must have the Cauchy-required fixed-power saving |
| `existing_l2_marginals` | divisor lifting gives low L2 for R_A and R_B separately, but this alone does not yield the needed centered convolution L2 saving |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CenteredProductRatioL2HardpointActive` | `true` | `true` | 上一证书已把当前剩余固定为 `C_*^circ` 的 L2 节省。 | CenteredNonzeroProductRatioL2PowerSavingAtCauchyRequiredScale |
| `EightVariableEnergyExpansionImported` | `true` | `true` | 八变量非零乘积比值能量展开已闭合。 | ledger |
| `RotatedRootBoxSupportGeometryClosed` | `true` | `true` | `a=d-e,b=d+e` 支撑为短线性根盒，可按符号、奇偶和边界距离拆包。 | DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale |
| `DyadicRectangularizationClosedUpToPolylog` | `true` | `true` | 多对数个矩形包和有限奇偶类只造成 `P^o(1)` 损失，不影响固定幂目标。 | DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale |
| `RectangularProductRatioConvolutionIdentityClosed` | `true` | `true` | 在每个矩形包对 `A0 x B0, A1 x B1` 上，交叉乘积比值谱等于两个交叉短区间比值谱的乘法卷积。 | MultiplicativeConvolutionOfTwoShortIntervalRatioSpectraCenteredL2PowerSaving |
| `SeparateRatioL2MarginalsInsufficient` | `true` | `true` | 分别控制 `R_A`、`R_B` 的 L2 只给边际账本，尚不能推出中心化卷积 L2 固定幂节省。 | DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale |
| `DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale` | `false` | `false` | 仓库内尚未证明所有 dyadic 矩形包的中心化乘法卷积比值谱 L2 固定幂节省。 | MultiplicativeConvolutionOfTwoShortIntervalRatioSpectraCenteredL2PowerSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是支撑矩形化和卷积恒等式，不是卷积 L2 节省本身。 | DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale |

## 4. 下一最窄自足目标

```text
DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale
```
