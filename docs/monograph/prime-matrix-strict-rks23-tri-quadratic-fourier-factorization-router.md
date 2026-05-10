# Prime Matrix strict RKS2/RKS3 三短二次 Fourier 因子化证书

**状态：** `nonzero_root_box_fourier_packet_factorized_into_three_short_quadratic_sums`

非零频率根盒谱包可精确因子化。令 `A(s)=sum_{d in Delta} e_P(s*d^2)`，再把 `u` 写成 `lambda*x`，则 `u(u-x)=lambda(lambda-1)x^2`，整个偏差变为 `Dev=(1/P) sum_{r!=0} A(-r) sum_{lambda!=1} A(r*lambda) B_lambda(r*lambda*(lambda-1))`。这里 `B_lambda` 是 `X_lambda={x in T:lambda*x in T}` 上的短二次和。因此当前唯一剩余是三短二次 Fourier 和的相关包固定幂节省。

```text
tri_quadratic_factorization_closed=true
tri_short_quadratic_fourier_correlation_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 三因子谱包

| field | value |
| --- | --- |
| `difference_quadratic_sum` | A(s)=sum_{d in Delta} e_P(s*d^2) |
| `x_quadratic_sum` | B_lambda(s)=sum_{x in X_lambda} e_P(s*x^2), where X_lambda={x in T: lambda*x in T} |
| `slope_change` | u=lambda*x with lambda!=1 |
| `phase_factorization` | (u/x)d1^2+u(u-x)=lambda*d1^2+lambda(lambda-1)*x^2 |
| `exact_packet` | Dev=(1/P) sum_{r!=0} A(-r) sum_{lambda!=1} A(r*lambda) B_lambda(r*lambda*(lambda-1)) |
| `zero_frequency_status` | r=0 removed; lambda=1 removed by the diagonal gate |
| `support_geometry` | lambda is constrained by X_lambda nonempty, i.e. T and lambda^{-1}T overlap |
| `why_narrower` | the remaining input is a tri-linear correlation of three short quadratic Fourier sums, not an unfactored rational phase |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NonzeroFrequencyPacketTargetActive` | `true` | `true` | 上一证书已把剩余压成非零频率根盒有理二次 Fourier 谱包。 | NonzeroFrequencyRootBoxQuadraticFourierPacketPowerSaving |
| `SlopeChangeOfVariablesClosed` | `true` | `true` | 用 `u=lambda*x` 精确保留根盒约束为 `X_lambda={x in T:lambda*x in T}`。 | TriShortQuadraticFourierCorrelationPowerSaving |
| `TriQuadraticFactorizationClosed` | `true` | `true` | 相位拆成 `d2`、`d1`、`x` 三个短二次 Fourier 因子。 | TriShortQuadraticFourierCorrelationPowerSaving |
| `DiagonalAndZeroFrequencyStillRemoved` | `true` | `true` | `r=0` 和 `lambda=1` 已由前序主项/对角门移除。 | removed |
| `TriShortQuadraticFourierCorrelationPowerSaving` | `false` | `false` | 仓库内尚未证明该三短二次 Fourier 相关包有固定幂节省。 | NonzeroFrequencySlopeFactorizedThreeQuadraticSumPacket |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只完成谱包因子化，未证明三因子相关估计。 | TriShortQuadraticFourierCorrelationPowerSaving |

## 3. 下一最窄自足目标

```text
TriShortQuadraticFourierCorrelationPowerSaving
```
