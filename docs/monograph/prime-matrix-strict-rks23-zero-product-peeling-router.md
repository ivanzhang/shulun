# Prime Matrix strict RKS2/RKS3 零乘积剥离证书

**状态：** `zero_product_diagonal_exactly_peeled_nonzero_product_ratio_core_remains`

零乘积层现在被精确剥离：在 `x,u` 非零的支撑上，`u*h1+x*h2=0` 中只要一个 `h_i=0`，另一个也必须为零，所以零层是同步对角主项 `|T|^2 W0^2`。它不是自动可吸收的小误差；在平方根颈部可处于自然尺度。因此自足线下一步必须先扣除该对角主项，再证明全非零乘积比值谱 `C(-lambda)` 与区间比值谱 `L(lambda)` 的联合非集中。

```text
zero_product_diagonal_main_ledger_closed=true
zero_product_layer_power_saving_absorbable=false
nonzero_product_ratio_normal_form_closed=true
diagonal_main_subtracted_nonzero_product_ratio_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 零乘积对角账本

| field | value |
| --- | --- |
| `square_difference` | h(d,e)=d^2-e^2 |
| `zero_mass` | W0=#{(d,e) in Delta^2: h(d,e)=0}=#{d=e or d=-e, with endpoint conventions} |
| `mixed_product_equation` | u*a1*b1+x*a2*b2=0 mod P, where h_i=a_i*b_i |
| `nonzero_uv_support` | x,u in T subset F_P^*, inherited from the unique-ratio ledger sum_lambda L(lambda)=\|T\|^2 |
| `forcing` | h1=0 or h2=0 implies h1=h2=0 |
| `raw_zero_layer_count` | \|T\|^2 * W0^2 |
| `centered_zero_layer_count` | \|T\|^2 * (W0^2-\|Delta\|^4/P) in the Q_circ normalization |
| `final_energy_diagonal_piece` | if not separately subtracted, P*(W0^2-\|Delta\|^4/P) per slope before the final square-root correlation |
| `scale_warning` | this can sit at the natural N^4 correlation scale in the square-root collar |
| `conclusion` | zero layer is exactly peelable, but not automatically power-saving absorbable |

## 2. 非零乘积比值核心

| field | value |
| --- | --- |
| `nonzero_product_measure` | mu(z)=#{(a,b): a*b=z, a*b!=0, with root-box/parity restrictions} |
| `product_ratio_spectrum` | C(rho)=sum_{z!=0} mu(z)*mu(rho*z) |
| `interval_ratio_spectrum` | L(lambda)=#{(x,u) in T^2: u=lambda*x} |
| `nonzero_equation` | u*z1+x*z2=0 with z1,z2!=0 |
| `ratio_normal_form` | z2/z1=-u/x=-lambda |
| `nonzero_core_count` | sum_lambda C(-lambda)*L(lambda), after the zero diagonal ledger is removed |
| `needed_saving` | prove the diagonal-main-subtracted centered correlation has a fixed power saving |
| `why_narrower` | the remaining object no longer contains the h=0 diagonal; all variables are nonzero product fibers |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ProductIncidenceHardpointActive` | `true` | `true` | 上一证书已把当前内部硬点固定为零层剥离加非零乘积入射节省。 | ZeroProductPeeledNonzeroBilinearProductMixedIncidencePowerSaving |
| `ZeroProductLayerPreviouslyIsolated` | `true` | `true` | `h=0` 已被精确识别为 `a*b=0`，即 `d=e` 或 `d=-e`。 | ZeroProductDiagonalMainTermExactLedger |
| `ZeroProductForcesSynchronousDiagonal` | `true` | `true` | 因 `x,u` 非零，混合方程中一侧平方差为零会强迫另一侧也为零。 | ZeroProductDiagonalMainTermExactLedger |
| `ZeroProductDiagonalMainLedgerClosed` | `true` | `true` | 零层贡献精确为 `\|T\|^2 W0^2`，中心化后为 `\|T\|^2(W0^2-\|Delta\|^4/P)`。 | diagonal main term must be subtracted before nonzero savings |
| `ZeroProductLayerNotAutomaticallyAbsorbable` | `true` | `true` | 尺度审计显示该同步对角层可达自然尺度，不能直接当作固定幂小误差。 | DiagonalMainSubtractedNonzeroProductRatioSpectrumJointPowerSaving |
| `NonzeroProductRatioNormalFormClosed` | `true` | `true` | 剥离零层后，剩余入射等价于乘积比值谱 `C(-lambda)` 与区间比值谱 `L(lambda)` 的相关。 | NonzeroBilinearProductRatioSpectrumAgainstIntervalRatioSpectrumNonconcentration |
| `DiagonalMainSubtractedNonzeroProductRatioSpectrumJointPowerSaving` | `false` | `false` | 仓库内尚未证明扣除零乘积对角主项后的非零乘积比值谱相关固定幂节省。 | NonzeroBilinearProductRatioSpectrumAgainstIntervalRatioSpectrumNonconcentration |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是零层精确剥离与非零核心正规形，不是最终相关节省。 | DiagonalMainSubtractedNonzeroProductRatioSpectrumJointPowerSaving |

## 4. 下一最窄自足目标

```text
DiagonalMainSubtractedNonzeroProductRatioSpectrumJointPowerSaving
```
