# Prime Matrix strict RKS2/RKS3 斜率比值谱前沿证书

**状态：** `slope_overlap_rewritten_as_low_l2_interval_ratio_spectrum`

斜率重叠也可以完全组合化。`L(lambda)` 就是短区间 `T` 的比值谱 `R_T(lambda)=#{(x,u):u=lambda*x}`。其一阶矩为 `|T|^2`；二阶矩等于短盒乘法能量，可由 `x1*u2-x2*u1=kP` 的整数提升和除数界控制为 `|T|^2 P^o(1)`。因此当前唯一剩余是平方差乘法谱是否能与这个低 L2 斜率比值谱产生异常相关。

```text
slope_overlap_ratio_spectrum_identity_closed=true
slope_overlap_l2_divisor_ledger_closed=true
square_difference_against_low_l2_ratio_spectrum_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 斜率比值谱账本

| field | value |
| --- | --- |
| `slope_overlap` | L(lambda)=\|X_lambda\|=#{x in T: lambda*x in T} |
| `ratio_spectrum` | R_T(lambda)=#{(x,u) in T^2: u=lambda*x mod P} |
| `identity` | L(lambda)=R_T(lambda) |
| `first_moment` | sum_lambda L(lambda)=\|T\|^2 |
| `second_moment` | sum_lambda L(lambda)^2=#{x1*u2=x2*u1 mod P: xi,ui in T} |
| `integer_lift` | x1*u2-x2*u1=kP with \|k\|<=log^O(P) in the square-root collar |
| `divisor_l2_bound` | sum_lambda L(lambda)^2 <= \|T\|^2 P^o(1) |
| `meaning` | the interval slope spectrum has low multiplicative energy; any remaining failure must be true correlation with the square-difference spectrum |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WeightedSquareDifferenceTargetActive` | `true` | `true` | 上一证书已把 `M_A(lambda)` 打开为平方差乘法谱。 | WeightedSquareDifferenceRatioOverlapAgainstSlopeOverlapPowerSaving |
| `SlopeOverlapRatioSpectrumIdentityClosed` | `true` | `true` | `L(lambda)` 精确等于短区间 `T` 的比值谱 `R_T(lambda)`。 | SquareDifferenceSpectrumAgainstLowL2IntervalRatioSpectrumPowerSaving |
| `SlopeOverlapFirstMomentClosed` | `true` | `true` | `sum_lambda L(lambda)=\|T\|^2`。 | ledger |
| `SlopeOverlapL2DivisorLedgerClosed` | `true` | `true` | 短盒乘法能量由整数提升和除数界给 `sum L(lambda)^2<=\|T\|^2 P^o(1)`。 | ledger |
| `SquareDifferenceSpectrumAgainstLowL2IntervalRatioSpectrumPowerSaving` | `false` | `false` | 仓库内尚未证明平方差谱不能与这个低 L2 比值谱发生固定幂级异常相关。 | WeightedSquareDifferenceRatioSpectrumCorrelationWithIntervalRatioSpectrum |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合斜率谱账本，未证明最终相关节省。 | SquareDifferenceSpectrumAgainstLowL2IntervalRatioSpectrumPowerSaving |

## 3. 下一最窄自足目标

```text
SquareDifferenceSpectrumAgainstLowL2IntervalRatioSpectrumPowerSaving
```
