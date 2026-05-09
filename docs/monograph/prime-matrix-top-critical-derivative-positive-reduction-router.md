# Prime Matrix 顶边临界半段导数正号压缩路由器

**状态：** `top_derivative_positive_reduced_to_endpoint_derivative_and_second_negative_open`

导数正号输入已进一步压缩：只需端点 Im zeta'(1+14i)>=1/16 和全段 Im zeta''(sigma+14i)<=-1/8。侦察显示端点导数约 0.097214，二阶导数最大约 -0.152777。严格自足仍需这两个 replay 证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
derivative_positive_reduced_to_endpoint_and_second_negative=true
top_critical_segment_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 侦察余量

| item | value |
| --- | ---: |
| endpoint derivative imag | `0.097213771726` |
| derivative floor | `0.062500000000` |
| endpoint derivative margin | `0.034713771726` |
| max second derivative imag | `-0.152776518407` |
| second ceiling | `-0.125000000000` |
| second negative margin | `0.027776518407` |
| max second derivative sigma | `1.000000000000` |
| min third derivative imag | `0.200257629159` |

## 2. 证明合同

1. 证明端点导数不等式 Im zeta'(1+14i)>=1/16。
2. 证明全段二阶导数不等式 Im zeta''(sigma+14i)<=-1/8。
3. 由二阶导数负号，Im zeta'(sigma+14i) 随 sigma 递减，最小值在 sigma=1。
4. 因此全段 Im zeta'(sigma+14i)>=Im zeta'(1+14i)>=1/16。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DerivativePositiveGateActive` | `true` | `true` | 上一层把中心表压成端点负号和全段导数正号。 | TopCriticalImagDerivativePositiveLedgerT14HalfToOneFloor1Over16 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只压缩低高度解析证书，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `FloatAuditSupportsConcavityRoute` | `true` | `false` | 侦察端点导数虚部 0.097213771726>1/16，二阶导数虚部最大 -0.152776518407<-1/8。 | 不能作为自足证明，只用于确定压缩方向。 |
| `DerivativePositiveFromEndpointAndConcavity` | `true` | `true` | 端点导数正号加二阶导数负号推出全段导数正号。 | TopCriticalImagDerivativePositiveLedgerT14HalfToOneFloor1Over16 |
| `EndpointDerivativeReplayStillMissing` | `false` | `false` | 需用有理区间 EM replay 证明 Im zeta'(1+14i)>=1/16。 | TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16 |
| `SecondDerivativeNegativeStillMissing` | `false` | `false` | 需用有理区间 EM replay 证明全段 Im zeta''<=-1/8。 | TopCriticalImagSecondDerivativeNegativeLedgerT14HalfToOneFloorMinus1Over8 |
| `TopCriticalImagDerivativePositiveLedgerT14HalfToOneFloor1Over16` | `false` | `false` | 导数正号账本已压缩为端点导数正号和二阶导数负号。 | TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16 AND TopCriticalImagSecondDerivativeNegativeLedgerT14HalfToOneFloorMinus1Over8 |

## 4. 下一步

优先攻：`TopCriticalImagSecondDerivativeNegativeLedgerT14HalfToOneFloorMinus1Over8`。
随后补：`TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16`。
端点负号：`TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40`。
顶边完成后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：导数正号已降为二阶负号和端点导数。
