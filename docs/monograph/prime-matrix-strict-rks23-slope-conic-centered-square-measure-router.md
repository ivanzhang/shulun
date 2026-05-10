# Prime Matrix strict RKS2/RKS3 中心化短平方测度前沿证书

**状态：** `slope_conic_bundle_reduced_to_centered_short_square_measure_deviation`

斜率二次曲线束可拆成短平方测度的均匀主项与中心化偏差。定义 `mu_D(y)=#{d in Delta: d^2=y}`，写作 `mu_D=|Delta|/P+nu_D`。均匀主项在所有斜率上总量至多 `|T|^2|Delta|^2/P=N^{2+o(1)}`，已经被固定幂目标吸收。当前唯一剩余就是中心化短平方测度 `nu_D` 沿相位 `lambda*d1^2+lambda(lambda-1)*x^2` 的局部推前偏差。

```text
short_square_measure_expansion_closed=true
uniform_main_term_absorbed=true
centered_short_square_measure_deviation_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 测度展开

| field | value |
| --- | --- |
| `difference_box` | Delta={d: d is an allowed signed root-box difference}, \|Delta\|=O(N) |
| `square_measure` | mu_D(y)=#{d in Delta: d^2=y mod P} |
| `centered_measure` | nu_D(y)=mu_D(y)-\|Delta\|/P |
| `slope_x_box` | X_lambda={x in T: lambda*x in T} |
| `conic_count` | R_lambda=sum_{x in X_lambda} sum_{d1 in Delta} mu_D(lambda*d1^2+lambda(lambda-1)*x^2) |
| `main_term` | (\|Delta\|/P)*\|X_lambda\|*\|Delta\| |
| `global_main_sum` | sum_lambda main <= \|T\|^2*\|Delta\|^2/P = N^{2+o(1)} in the square-root collar |
| `main_absorption` | N^{2+o(1)} <= N^(3-delta) for every fixed delta<1 and large P |
| `remaining_deviation` | sum_lambda sum_{x in X_lambda,d1 in Delta} nu_D(lambda*d1^2+lambda(lambda-1)*x^2) |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SlopeConicBundleTargetActive` | `true` | `true` | 上一证书已把剩余压成非平凡斜率局部二次曲线束。 | NontrivialSlopeLocalizedTernaryConicBundlePowerSaving |
| `ShortSquareMeasureExpansionClosed` | `true` | `true` | 用 `mu_D=\|Delta\|/P+nu_D` 精确展开 `d2` 的短平方命中测度。 | CenteredShortSquareMeasureOnSlopeConicBundlePowerSaving |
| `UniformMainTermAbsorbed` | `true` | `true` | 所有斜率主项总和为 `N^{2+o(1)}`，低于固定幂能量目标。 | absorbed |
| `CenteredDeviationIsOnlyRemainingInput` | `true` | `true` | 剩余完全是中心化短平方测度沿非退化二次相位的局部推前偏差。 | CenteredShortSquareMeasureOnSlopeConicBundlePowerSaving |
| `CenteredShortSquareMeasureOnSlopeConicBundlePowerSaving` | `false` | `false` | 仓库内尚未证明该中心化偏差总和有固定幂节省。 | LocalizedQuadraticPushforwardSquareMeasureDeviationPowerSaving |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只吸收主项并定位偏差输入，未证明偏差估计。 | CenteredShortSquareMeasureOnSlopeConicBundlePowerSaving |

## 3. 下一最窄自足目标

```text
CenteredShortSquareMeasureOnSlopeConicBundlePowerSaving
```
