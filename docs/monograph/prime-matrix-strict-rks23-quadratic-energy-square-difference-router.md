# Prime Matrix strict RKS2/RKS3 平方差谱前沿证书

**状态：** `quadratic_fourier_energy_opened_as_square_difference_multiplicative_overlap`

二次 Fourier 能量自相关可以完全组合化。令 `W(h)=#{(d,e):d^2-e^2=h}`，则 `|A(r)|^2` 是 `W` 的 Fourier 变换，并且 `M_A(lambda)=P*sum_h W(h)W(-lambda*h)-|Delta|^4`。所以当前剩余不再是抽象 Fourier 能量，而是平方差测度的乘法重叠谱与根盒斜率重叠谱之间的相关节省。

```text
square_difference_measure_identity_closed=true
m_autocorrelation_opened=true
weighted_square_difference_slope_correlation_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 平方差谱展开

| field | value |
| --- | --- |
| `quadratic_sum` | A(s)=sum_{d in Delta} e_P(s*d^2) |
| `square_difference_measure` | W(h)=#{(d,e) in Delta^2: d^2-e^2=h mod P} |
| `fourier_identity` | \|A(r)\|^2=sum_h W(h)e_P(r*h) |
| `energy_autocorrelation` | M_A(lambda)=sum_{r!=0}\|A(r)\|^2\|A(lambda*r)\|^2 |
| `opened_formula` | M_A(lambda)=P*sum_h W(h)W(-lambda*h)-\|Delta\|^4 |
| `meaning` | large M_A(lambda) is exactly a large multiplicative overlap of the square-difference measure W with its lambda-dilate |
| `correlation_target` | sum_lambda sqrt((P*<W,lambda W>-\|Delta\|^4)*L(lambda)) |
| `new_language` | weighted square-difference ratio spectrum correlated with the interval slope-overlap spectrum |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CorrelatedEnergyOverlapTargetActive` | `true` | `true` | 上一证书已把剩余压成 `M_A(lambda)` 与 `L(lambda)` 的相关节省。 | CorrelatedQuadraticFourierEnergyOverlapPowerSaving |
| `SquareDifferenceMeasureIdentityClosed` | `true` | `true` | `\|A(r)\|^2` 精确等于平方差测度 `W` 的 Fourier 变换。 | WeightedSquareDifferenceRatioOverlapAgainstSlopeOverlapPowerSaving |
| `MAutocorrelationOpened` | `true` | `true` | `M_A(lambda)=P*sum_h W(h)W(-lambda*h)-\|Delta\|^4`，无隐藏解析输入。 | WeightedSquareDifferenceRatioOverlapAgainstSlopeOverlapPowerSaving |
| `ZeroFrequencySubtractionAccounted` | `true` | `true` | `-\|Delta\|^4` 正是去掉 `r=0` 后的零频扣除。 | accounted |
| `WeightedSquareDifferenceRatioOverlapAgainstSlopeOverlapPowerSaving` | `false` | `false` | 仓库内尚未证明平方差乘法谱与斜率重叠谱之间有固定幂相关节省。 | SquareDifferenceMultiplicativeSpectrumSlopeCorrelationSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只把 Fourier 能量改写为平方差谱，未证明相关节省。 | WeightedSquareDifferenceRatioOverlapAgainstSlopeOverlapPowerSaving |

## 3. 下一最窄自足目标

```text
WeightedSquareDifferenceRatioOverlapAgainstSlopeOverlapPowerSaving
```
