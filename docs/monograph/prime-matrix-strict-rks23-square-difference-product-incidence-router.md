# Prime Matrix strict RKS2/RKS3 平方差乘积入射证书

**状态：** `centered_mixed_incidence_factorized_into_product_form_with_zero_layer_isolated`

混合平方差入射可进一步乘积化。令 `a=d-e,b=d+e`，则 `d^2-e^2=a*b`，原方程 `u h1+x h2=0` 化为 `u*a1*b1+x*a2*b2=0 mod P`。同时 `h=0` 精确变成零乘积层 `a*b=0`，即 `d=e` 或 `d=-e`。因此下一真正剩余是先把零乘积对角层正确回扣，再证明非零乘积核心的中心化混合入射节省。

```text
square_difference_product_coordinates_closed=true
zero_product_layer_isolated=true
zero_product_peeled_nonzero_product_incidence_power_saving_proved=false
row_column_unconditional_closed=false
```

## 1. 乘积入射正规形

| field | value |
| --- | --- |
| `change_of_variables` | a=d-e, b=d+e; since 2 is invertible, d=(a+b)/2 and e=(b-a)/2 |
| `square_difference_factorization` | d^2-e^2=a*b |
| `box_constraints` | a,b lie in short O(N) boxes with parity/root-box endpoint restrictions |
| `mixed_equation_before` | u*(d1^2-e1^2)+x*(d2^2-e2^2)=0 mod P |
| `mixed_equation_after` | u*a1*b1+x*a2*b2=0 mod P |
| `zero_product_layer` | h=0 iff a*b=0, i.e. d=e or d=-e |
| `why_zero_layer_matters` | this is a structured diagonal layer; it must be peeled/accounted before claiming random-like mixed incidence |
| `nonzero_core` | a1*b1 and a2*b2 both nonzero; the remaining equation is a genuine bilinear-product ratio incidence |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DyadicMixedIncidenceTargetActive` | `true` | `true` | 上一证书已把最终相关失败压成 dyadic 中心化混合平方差-比值入射。 | DyadicCenteredMixedSquareDifferenceRatioIncidencePowerSaving |
| `SquareDifferenceProductCoordinatesClosed` | `true` | `true` | `d^2-e^2=(d-e)(d+e)` 在奇素数模下给出可逆变量替换。 | CenteredBilinearProductRatioIncidenceAfterSquareDifferenceFactorization |
| `MixedIncidenceProductFormClosed` | `true` | `true` | 六变量混合入射化为 `u*a1*b1+x*a2*b2=0` 的乘积型入射。 | CenteredBilinearProductRatioIncidenceAfterSquareDifferenceFactorization |
| `ZeroProductLayerIsolated` | `true` | `true` | `h=0` 精确等价于 `a*b=0`，该对角层已被显式隔离。 | ZeroProductPeeledNonzeroBilinearProductMixedIncidencePowerSaving |
| `ZeroProductPeeledNonzeroBilinearProductMixedIncidencePowerSaving` | `false` | `false` | 仓库内尚未完成零乘积层回扣与非零乘积混合入射的固定幂节省。 | CenteredBilinearProductRatioIncidenceAfterSquareDifferenceFactorization |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只完成乘积化与零层隔离，未证明最终入射节省。 | ZeroProductPeeledNonzeroBilinearProductMixedIncidencePowerSaving |

## 3. 下一最窄自足目标

```text
ZeroProductPeeledNonzeroBilinearProductMixedIncidencePowerSaving
```
