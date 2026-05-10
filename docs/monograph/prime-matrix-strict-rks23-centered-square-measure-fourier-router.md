# Prime Matrix strict RKS2/RKS3 中心化平方测度 Fourier 谱包证书

**状态：** `centered_square_measure_deviation_reduced_to_nonzero_quadratic_fourier_packets`

中心化短平方测度偏差可以完全 Fourier 化。由于 `nu_D` 已中心化，零频项为 0；非零频率的系数就是差盒上的短二次和 `sum_{d2 in Delta} e_P(-r*d2^2)`。剩余内层是 `x,u,d1` 根盒上的有理二次相位 `(u/x)d1^2+u(u-x)`。因此当前唯一剩余变成非零频率根盒有理二次 Fourier 谱包的固定幂节省。

```text
fourier_expansion_closed=true
zero_frequency_removed=true
nonzero_frequency_root_box_quadratic_fourier_packet_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 非零 Fourier 谱包

| field | value |
| --- | --- |
| `centered_measure` | nu_D=mu_D-\|Delta\|/P |
| `zero_frequency` | hat(nu_D)(0)=0 |
| `nonzero_coefficient` | for r!=0, hat(nu_D)(r)=sum_{d2 in Delta} e_P(-r*d2^2) |
| `slope_to_t_variables` | lambda=u/x with x,u in T and x!=u |
| `phase_argument` | lambda*d1^2+lambda(lambda-1)*x^2 = (u/x)*d1^2+u(u-x) |
| `deviation_formula` | Dev=(1/P) sum_{r!=0} hat(nu_D)(r) sum_{x,u in T,x!=u} sum_{d1 in Delta} e_P(r*((u/x)*d1^2+u(u-x))) |
| `opened_inner_packet` | short quadratic d2-Fourier weight coupled to rational quadratic root-box phase in (x,u,d1) |
| `why_narrower` | all main terms and zero frequency are gone; only nonzero oscillatory packets remain |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CenteredSquareMeasureTargetActive` | `true` | `true` | 上一证书已把曲线束剩余压成中心化短平方测度偏差。 | CenteredShortSquareMeasureOnSlopeConicBundlePowerSaving |
| `FourierExpansionClosed` | `true` | `true` | 中心化偏差可精确展开为 `r!=0` 的 Fourier 谱包。 | NonzeroFrequencyRootBoxQuadraticFourierPacketPowerSaving |
| `ZeroFrequencyRemoved` | `true` | `true` | `nu_D` 的零频为 0；此前均匀主项已完全吸收。 | removed |
| `NonzeroFourierCoefficientIdentified` | `true` | `true` | 非零系数就是差盒上的短二次 Fourier 和。 | ShortSquareFourierWeightAgainstRationalQuadraticRootBoxPhase |
| `NonzeroFrequencyRootBoxQuadraticFourierPacketPowerSaving` | `false` | `false` | 仓库内尚未证明该非零频率根盒有理二次相位谱包有固定幂节省。 | ShortSquareFourierWeightAgainstRationalQuadraticRootBoxPhase |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只完成 Fourier 化与零频移除，未证明非零谱包估计。 | NonzeroFrequencyRootBoxQuadraticFourierPacketPowerSaving |

## 3. 下一最窄自足目标

```text
NonzeroFrequencyRootBoxQuadraticFourierPacketPowerSaving
```
