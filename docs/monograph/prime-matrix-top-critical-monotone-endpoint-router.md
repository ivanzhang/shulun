# Prime Matrix 顶边临界半段单调端点压缩路由器

**状态：** `top_center_imag_table_reduced_to_endpoint_and_derivative_positive_open`

1024 个中心虚部 replay 表已被压缩为更结构化的两个输入：端点 Im zeta(1+14i)<=-1/40，以及全段 Im zeta_sigma'(sigma+14i)>=1/16。侦察显示端点虚部约 -0.030678，导数虚部最小约 0.097214，余量足够；严格自足仍需这两个有理区间 replay 证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
center_imag_table_compressed_to_monotone_endpoint=true
top_critical_segment_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 单调侦察

| item | value |
| --- | ---: |
| endpoint imag | `-0.030678124321` |
| imag floor | `-0.025000000000` |
| endpoint margin below floor | `0.005678124321` |
| min derivative imag | `0.097213771726` |
| derivative floor | `0.062500000000` |
| derivative margin above floor | `0.034713771726` |
| min derivative sigma | `1.000000000000` |
| max zeta imag sigma | `1.000000000000` |
| second derivative imag range | `[-0.289484114340, -0.152776518407]` |
| endpoint third derivative imag | `0.200257629159` |

## 2. 证明合同

1. 证明端点不等式 Im zeta(1+14i)<=-1/40。
2. 证明全段导数不等式 Im d/dsigma zeta(sigma+14i)>=1/16。
3. 由导数正号，Im zeta(sigma+14i) 在 1/2<=sigma<=1 上递增，最大值在 sigma=1。
4. 因此整段 Im zeta<=Im zeta(1+14i)<=-1/40<0，顶边临界半段无零。
5. 这样 1024 个中心虚部表可被一个端点值 replay 和一个导数正号 replay 替代。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MonotoneEndpointGateActive` | `true` | `true` | 上一层唯一剩余是 1024 个中心点虚部负号 replay。 | TopCriticalSegmentCenterImagNegativeEMReplayLedgerN32P8Mesh2048FloorMinus1Over40 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只做解析证书压缩，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `FloatAuditSupportsMonotoneEndpoint` | `true` | `false` | 侦察给端点虚部 -0.030678124321<-1/40，导数虚部最小 0.097213771726>1/16。 | 不能作为自足证明，只用于确定压缩方向。 |
| `MonotoneEndpointLemmaClosed` | `true` | `true` | 端点负号加全段导数正号推出整段虚部为负。 | TopCriticalSegmentXiNonzeroClosedByMonotoneEndpointT14HalfToOne |
| `EndpointImagReplayStillMissing` | `false` | `false` | 需用有理区间 EM replay 证明 Im zeta(1+14i)<=-1/40。 | TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40 |
| `DerivativePositiveReplayStillMissing` | `false` | `false` | 需用有理区间 EM replay 证明全段 Im zeta_sigma'(sigma+14i)>=1/16。 | TopCriticalImagDerivativePositiveLedgerT14HalfToOneFloor1Over16 |
| `TopCriticalSegmentCenterImagNegativeEMReplayLedgerN32P8Mesh2048FloorMinus1Over40` | `false` | `false` | 1024 中心负号表已压缩为端点负号和导数正号两个证书。 | TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40 AND TopCriticalImagDerivativePositiveLedgerT14HalfToOneFloor1Over16 |

## 4. 下一步

优先攻：`TopCriticalImagDerivativePositiveLedgerT14HalfToOneFloor1Over16`。
随后补：`TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40`。
顶边完成后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：1024 点表已降为单调性证书加一个端点证书。
