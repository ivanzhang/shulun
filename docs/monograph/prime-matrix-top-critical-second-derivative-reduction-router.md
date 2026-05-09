# Prime Matrix 顶边临界半段二阶导数负号压缩路由器

**状态：** `top_second_derivative_negative_reduced_to_endpoint_second_and_third_positive_open`

二阶负号输入已进一步压缩：只需端点 Im zeta''(1+14i)<=-1/8 和全段 Im zeta'''(sigma+14i)>=1/8。侦察显示端点二阶约 -0.152777，三阶导数最小约 0.200258。严格自足仍需这两个 replay/符号证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
second_derivative_negative_reduced_to_endpoint_and_third_positive=true
top_critical_segment_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 侦察余量

| item | value |
| --- | ---: |
| endpoint second derivative imag | `-0.152776518407` |
| second ceiling | `-0.125000000000` |
| endpoint second margin | `0.027776518407` |
| max second derivative imag | `-0.152776518407` |
| max second derivative sigma | `1.000000000000` |
| min third derivative imag | `0.200257629159` |
| third floor | `0.125000000000` |
| third positive margin | `0.075257629159` |

## 2. 证明合同

1. 证明端点二阶不等式 Im zeta''(1+14i)<=-1/8。
2. 证明全段三阶导数不等式 Im zeta'''(sigma+14i)>=1/8。
3. 由三阶导数正号，Im zeta''(sigma+14i) 随 sigma 递增，最大值在 sigma=1。
4. 因此全段 Im zeta''(sigma+14i)<=Im zeta''(1+14i)<=-1/8。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SecondDerivativeGateActive` | `true` | `true` | 上一层把导数正号压成端点导数正号和全段二阶负号。 | TopCriticalImagSecondDerivativeNegativeLedgerT14HalfToOneFloorMinus1Over8 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只压缩低高度解析证书，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `FloatAuditSupportsThirdDerivativeRoute` | `true` | `false` | 侦察端点二阶虚部 -0.152776518407<-1/8，三阶导数虚部最小 0.200257629159>1/8。 | 不能作为自足证明，只用于确定压缩方向。 |
| `SecondNegativeFromEndpointAndThirdPositive` | `true` | `true` | 端点二阶负号加三阶正号推出全段二阶负号。 | TopCriticalImagSecondDerivativeNegativeLedgerT14HalfToOneFloorMinus1Over8 |
| `EndpointSecondReplayStillMissing` | `false` | `false` | 需用有理区间 EM replay 证明 Im zeta''(1+14i)<=-1/8。 | TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8 |
| `ThirdDerivativePositiveStillMissing` | `false` | `false` | 需用有理区间 EM replay 或 Taylor 符号梯证明全段 Im zeta'''>=1/8。 | TopCriticalImagThirdDerivativePositiveLedgerT14HalfToOneFloor1Over8 |
| `TopCriticalImagSecondDerivativeNegativeLedgerT14HalfToOneFloorMinus1Over8` | `false` | `false` | 二阶负号账本已压缩为端点二阶负号和三阶导数正号。 | TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8 AND TopCriticalImagThirdDerivativePositiveLedgerT14HalfToOneFloor1Over8 |

## 4. 下一步

优先攻：`TopCriticalImagThirdDerivativePositiveLedgerT14HalfToOneFloor1Over8`。
随后补：`TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8`。
再补端点导数：`TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16`。
再补端点虚部：`TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40`。
顶边完成后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：二阶负号已降为三阶正号和端点二阶负号。
