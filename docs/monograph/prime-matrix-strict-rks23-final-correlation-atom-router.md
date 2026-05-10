# Prime Matrix strict RKS2/RKS3 最终相关原子证书

**状态：** `rks23_strict_internal_frontier_reduced_to_joint_nonconcentration_atom`

当前严格内部 RKS23 线已收束为一个最终相关原子：平方差谱 `Q(lambda)=sum_h W(h)W(-lambda*h)` 与短区间比值谱 `L(lambda)=#{(x,u):u=lambda*x}` 不能在同一批斜率上同时集中。两个边际账本已闭合，但它们单独只给自然尺度；真正剩余是联合非集中。

```text
square_difference_spectrum_ready=true
interval_ratio_spectrum_l2_ready=true
joint_nonconcentration_atom_proved=false
row_column_unconditional_closed=false
```

## 1. 最终相关原子

| field | value |
| --- | --- |
| `square_difference_measure` | W(h)=#{(d,e) in Delta^2: d^2-e^2=h} |
| `square_difference_spectrum` | Q(lambda)=sum_h W(h)W(-lambda*h) |
| `slope_ratio_spectrum` | L(lambda)=#{(x,u) in T^2: u=lambda*x} |
| `closed_marginal_1` | sum_lambda L(lambda)=\|T\|^2 |
| `closed_marginal_2` | sum_lambda L(lambda)^2<=\|T\|^2 P^o(1) |
| `closed_marginal_3` | M_A(lambda)=P*Q(lambda)-\|Delta\|^4 |
| `required_joint_saving` | sum_lambda sqrt((P*Q(lambda)-\|Delta\|^4)*L(lambda)) <= P*N^2*N^(-delta) |
| `why_single_spectrum_bounds_fail` | Plancherel and the L2 ledger separately reach the natural scale; fixed power saving requires joint nonconcentration |
| `forbidden_shortcuts` | do not claim closure from average Q alone, average L alone, or plain Cauchy/Plancherel |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FinalCorrelationTargetActive` | `true` | `true` | 上一证书已把剩余固定为平方差谱与低 L2 比值谱的相关节省。 | SquareDifferenceSpectrumAgainstLowL2IntervalRatioSpectrumPowerSaving |
| `SquareDifferenceSpectrumReady` | `true` | `true` | `M_A(lambda)` 已完全打开为平方差谱 `Q(lambda)`。 | closed marginal |
| `IntervalRatioSpectrumL2Ready` | `true` | `true` | `L(lambda)` 的一阶与二阶账本已由短盒整数提升闭合。 | closed marginal |
| `OnlyJointNonconcentrationRemains` | `true` | `true` | 所有边际估计只能到自然尺度；剩余是两个谱不能同位集中。 | JointNonconcentrationOfSquareDifferenceSpectrumAndIntervalRatioSpectrum |
| `JointNonconcentrationOfSquareDifferenceSpectrumAndIntervalRatioSpectrum` | `false` | `false` | 仓库内尚未证明平方差谱峰值不能落在区间比值谱的大重叠斜率上。 | new internal hardpoint |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只完成最终相关原子收束，未证明该原子。 | JointNonconcentrationOfSquareDifferenceSpectrumAndIntervalRatioSpectrum |

## 3. 下一最窄自足目标

```text
JointNonconcentrationOfSquareDifferenceSpectrumAndIntervalRatioSpectrum
```
