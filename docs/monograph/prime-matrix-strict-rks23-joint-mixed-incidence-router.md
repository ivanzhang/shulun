# Prime Matrix strict RKS2/RKS3 混合入射正规形证书

**状态：** `joint_nonconcentration_reduced_to_centered_mixed_square_difference_ratio_incidence`

最终相关原子可以展开成一个具体混合入射。设 `h_i=d_i^2-e_i^2`，同一个斜率同时满足 `h2=-lambda*h1` 与 `u=lambda*x`，消去 `lambda` 得 `u*h1+x*h2=0 mod P`。扣除 `|Delta|^4/P` 的均匀项后，若联合非集中目标失败，就会在某个 dyadic 斜率包上产生过大的中心化六变量混合入射。

```text
mixed_incidence_identity_closed=true
centered_uniform_term_subtracted=true
dyadic_centered_mixed_incidence_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 混合入射正规形

| field | value |
| --- | --- |
| `square_difference` | h_i=d_i^2-e_i^2 |
| `slope_ratio` | lambda=u/x |
| `same_slope_constraint` | h2=-lambda*h1 and u=lambda*x |
| `mixed_incidence_equation` | u*(d1^2-e1^2)+x*(d2^2-e2^2)=0 mod P |
| `raw_identity` | sum_lambda Q(lambda)L(lambda) equals the weighted count of this six-variable equation |
| `centered_spectrum` | Q_circ(lambda)=Q(lambda)-\|Delta\|^4/P |
| `centered_mixed_count` | sum_lambda Q_circ(lambda)L(lambda)=raw_count-(\|Delta\|^4/P)\|T\|^2 |
| `dyadic_failure_extraction` | if the sqrt-weight joint target fails, a dyadic packet of slopes has large centered mixed incidence after log^O(P) loss |
| `why_narrower` | the remaining target is a concrete centered six-variable incidence, not an abstract correlation phrase |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `JointNonconcentrationTargetActive` | `true` | `true` | 上一证书已把严格内部剩余固定为平方差谱与区间比值谱的联合非集中。 | JointNonconcentrationOfSquareDifferenceSpectrumAndIntervalRatioSpectrum |
| `MixedIncidenceIdentityClosed` | `true` | `true` | `Q(lambda)L(lambda)` 精确展开为 `u h1+x h2=0` 的混合入射计数。 | CenteredSixVariableSquareDifferenceRatioIncidenceSaving |
| `CenteredUniformTermSubtracted` | `true` | `true` | `Q(lambda)-\|Delta\|^4/P` 的均匀项扣除与 `sum L=\|T\|^2` 同口径。 | CenteredSixVariableSquareDifferenceRatioIncidenceSaving |
| `DyadicFailurePacketExtractionClosed` | `true` | `true` | 若联合平方根目标失败，必有一个 dyadic 斜率包给出过大的中心化混合入射。 | DyadicCenteredMixedSquareDifferenceRatioIncidencePowerSaving |
| `DyadicCenteredMixedSquareDifferenceRatioIncidencePowerSaving` | `false` | `false` | 仓库内尚未证明所有 dyadic 斜率包的中心化混合入射都有固定幂节省。 | CenteredSixVariableSquareDifferenceRatioIncidenceSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只完成混合入射正规形与 dyadic 失败抽取，未证明入射节省。 | DyadicCenteredMixedSquareDifferenceRatioIncidencePowerSaving |

## 3. 下一最窄自足目标

```text
DyadicCenteredMixedSquareDifferenceRatioIncidencePowerSaving
```
