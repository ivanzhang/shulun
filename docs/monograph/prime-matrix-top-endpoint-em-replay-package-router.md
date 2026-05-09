# Prime Matrix 顶边端点 Euler-Maclaurin replay 包路由器

**状态：** `top_endpoint_em_replay_package_closed`

端点 EM replay 包已闭合：端点虚部负号、端点一阶正号、端点二阶负号、3-10 阶交替符号和 11-13 阶例外粗界全部有正余量。下一步只需把这些端点包沿前面已闭合的单调/Taylor 压缩链做一次聚合，即可关闭顶边临界半段。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
endpoint_em_replay_package_closed=true
top_critical_segment_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 端点检查表

| order | claim | value | radius | target | margin | closed |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| 0 | imag <= -1/40 | `-0.030678124321` | `6.428e-19` | `-0.025000000000` | `0.005678124321` | `true` |
| 1 | imag >= 1/16 | `0.097213771726` | `2.889e-18` | `0.062500000000` | `0.034713771726` | `true` |
| 2 | imag <= -1/8 | `-0.152776518407` | `1.295e-17` | `-0.125000000000` | `0.027776518407` | `true` |
| 3 | alternating signed imag >= 3/16 | `0.200257629159` | `5.790e-17` | `0.187500000000` | `0.012757629159` | `true` |
| 4 | alternating signed imag >= 1/16 | `-0.240487563659` | `2.582e-16` | `0.062500000000` | `0.177987563659` | `true` |
| 5 | alternating signed imag >= 1/16 | `0.272301631828` | `1.148e-15` | `0.062500000000` | `0.209801631828` | `true` |
| 6 | alternating signed imag >= 1/16 | `-0.292464962584` | `5.093e-15` | `0.062500000000` | `0.229964962584` | `true` |
| 7 | alternating signed imag >= 1/16 | `0.295547880252` | `2.254e-14` | `0.062500000000` | `0.233047880252` | `true` |
| 8 | alternating signed imag >= 1/16 | `-0.273880335056` | `9.951e-14` | `0.062500000000` | `0.211380335056` | `true` |
| 9 | alternating signed imag >= 1/16 | `0.217777592054` | `4.383e-13` | `0.062500000000` | `0.155277592054` | `true` |
| 10 | alternating signed imag >= 1/16 | `-0.116322088754` | `1.926e-12` | `0.062500000000` | `0.053822088752` | `true` |
| 11 | abs imag <= 1/16 | `-0.040893033936` | `8.448e-12` | `0.062500000000` | `0.021606966056` | `true` |
| 12 | abs imag <= 1/3 | `0.260517692344` | `3.697e-11` | `0.333333333333` | `0.072815640953` | `true` |
| 13 | abs imag <= 1 | `-0.540041942120` | `1.614e-10` | `1.000000000000` | `0.459958057719` | `true` |

## 2. 证明合同

1. 在 s=1+14i, N=32, P=8 处写出 zeta 及各阶导数的 Euler-Maclaurin 公式。
2. 有限和、极点补偿项、半端点项、Bernoulli 修正项逐项求导到 13 阶。
3. 余项用 |B_16({x})|<=|B_16| 和 Leibniz 公式给显式绝对值半径。
4. 所有 log/trig/exp 调用由已闭合 EM replay 舍入纪律和 trace/hash 账本向外取整。
5. 逐项比较区间端点：0 阶、1 阶、2 阶和 3 到 13 阶所需全部不等式均有正余量。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EndpointPackageGateActive` | `true` | `true` | 上一层最窄点是端点 3 到 10 阶符号梯 replay。 | TopEndpointImagDerivativeAlternatingSignReplaySigma1T14Orders3To10 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只处理低高度解析证书，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `EMRoundingDisciplineImported` | `true` | `true` | 端点 EM replay 的 log/trig/exp 与复区间舍入纪律已由 canonical DAG 账本覆盖。 | no new arithmetic primitive. |
| `TopEndpointImagDerivativeAlternatingSignReplaySigma1T14Orders3To10` | `true` | `true` | 3 到 10 阶端点导数交替符号闭合，其中 3 阶强到 >=3/16。 | TopEndpointImagDerivativeAlternatingSignReplaySigma1T14Orders3To10Closed |
| `TopEndpointImagDerivativeExceptionBoundReplaySigma1T14Orders11To13` | `true` | `true` | 11 到 13 阶端点例外粗绝对值界闭合。 | TopEndpointImagDerivativeExceptionBoundReplaySigma1T14Orders11To13Closed |
| `TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8` | `true` | `true` | 端点二阶负号闭合。 | TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8Closed |
| `TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16` | `true` | `true` | 端点一阶导数正号闭合。 | TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16Closed |
| `TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40` | `true` | `true` | 端点虚部负号闭合。 | TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40Closed |

## 4. 下一步

当前最窄点：`TopCriticalSegmentEndpointTaylorChainAggregationLedger`。
随后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：端点输入包已闭合，剩余是链式聚合与 winding 证书。
