# Prime Matrix strict RKS2/RKS3 乘积比值角色矩证书

**状态：** `dyadic_rectangular_convolution_l2_reduced_to_nonprincipal_character_product_moment`

dyadic 矩形卷积 L2 已被精确对角化到乘法角色侧。principal character 恰好产生 `(|R0||R1|)/(P-1)` 的均匀主项，中心化后完全消失。每个非主角色的 Fourier 系数因子化为四个短区间角色和 `S_A0,S_A1,S_B0,S_B1` 的乘积。因此下一真正自足硬点不是抽象卷积，而是证明非主角色四短区间乘积矩具有 Cauchy 所需的固定幂节省。

```text
multiplicative_fourier_on_fstar_closed=true
principal_character_uniform_term_removed=true
cross_ratio_fourier_factorization_closed=true
centered_l2_equals_nonprincipal_four_interval_moment=true
four_short_interval_character_product_moment_saving_proved=false
row_column_unconditional_closed=false
```

## 1. F_P^* 乘法 Fourier

| field | value |
| --- | --- |
| `group` | G=F_P^* with \|G\|=P-1 |
| `packet_pair` | R0=A0 x B0 and R1=A1 x B1 |
| `cross_product_ratio` | C_R0,R1(rho)=#{(r0,r1): a1*b1=rho*a0*b0} |
| `centered_ratio` | C^circ(rho)=C_R0,R1(rho)-(\|R0\|*\|R1\|)/(P-1) |
| `multiplicative_fourier` | hat f(chi)=sum_{rho in G} f(rho) chi(rho) |
| `principal_character` | chi0 gives hat C(chi0)=\|R0\|*\|R1\| and is exactly removed by centering |
| `plancherel` | sum_rho \|C^circ(rho)\|^2=(1/(P-1))*sum_{chi!=chi0}\|hat C(chi)\|^2 |

## 2. 非主角色矩因子化

| field | value |
| --- | --- |
| `interval_character_sum` | S_I(chi)=sum_{n in I} chi(n) |
| `a_cross_ratio_transform` | hat R_A0,A1(chi)=S_A1(chi)*conj(S_A0(chi)) |
| `b_cross_ratio_transform` | hat R_B0,B1(chi)=S_B1(chi)*conj(S_B0(chi)) |
| `product_transform` | hat C(chi)=S_A1(chi)conj(S_A0(chi))S_B1(chi)conj(S_B0(chi)) |
| `l2_character_moment` | sum_rho \|C^circ(rho)\|^2=(1/(P-1))*sum_{chi!=chi0} \|S_A0(chi)S_A1(chi)S_B0(chi)S_B1(chi)\|^2 |
| `required_saving` | prove this nonprincipal four-short-interval character product moment is below the Cauchy scale by a fixed power |
| `external_sufficient_route` | classical Burgess/BG-style character-sum input would be sufficient if accepted with the needed uniform packet constants |
| `internal_gap` | the current corpus has not internalized that character-moment proof for all dyadic rectangle packets |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DyadicRectangularConvolutionHardpointActive` | `true` | `true` | 上一证书已把当前剩余固定为 dyadic 矩形包对的中心化乘法卷积 L2 节省。 | DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale |
| `MultiplicativeFourierOnFStarClosed` | `true` | `true` | 在 `F_P^*` 上对乘积比值谱做乘法 Fourier 是精确等式。 | FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving |
| `PrincipalCharacterUniformTermRemoved` | `true` | `true` | principal character 正好给出 `(\|R0\|\|R1\|)/(P-1)` 均匀主项，已由中心化扣除。 | FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving |
| `CrossRatioFourierFactorizationClosed` | `true` | `true` | 乘积交叉比值谱的 Fourier 变换总计因子化为四个短区间角色和的乘积。 | FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving |
| `CenteredL2EqualsNonprincipalFourIntervalMoment` | `true` | `true` | 中心化卷积 L2 精确等于非主角色上四个短区间角色和乘积的二阶矩。 | FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving |
| `ExternalBurgessBGWouldBeSufficientButNotInternalized` | `true` | `false` | Burgess/BG 型角色和输入若带所需统一常数可作为充分外部闭合；本证书未把它内部化。 | SelfContainedBurgessOrBourgainGaraevCharacterMomentForRKS23Rectangles |
| `FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving` | `false` | `false` | 仓库内尚未给出该非主角色四短区间乘积矩的严格内部固定幂节省证明。 | SelfContainedBurgessOrBourgainGaraevCharacterMomentForRKS23Rectangles |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是乘法 Fourier/角色矩等式，不是角色矩节省本身。 | FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving |

## 4. 下一最窄自足目标

```text
FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving
```
