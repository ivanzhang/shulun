# Prime Matrix 顶边临界半段三阶导数正号 Taylor 符号梯路由器

**状态：** `top_third_derivative_positive_reduced_to_endpoint_taylor_ladder_open`

三阶正号输入不再需要继续做全段逐阶单调递归：10 阶端点 Taylor 符号梯加 14 阶 EM 包络即可推出 Im zeta'''(sigma+14i)>=1/8。14 阶包络已在本路由内闭合到 <2^30；严格自足剩余变成两个端点 replay：3-10 阶交替符号与 11-13 阶粗绝对值界。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
third_derivative_positive_reduced_to_endpoint_taylor_ladder=true
order14_euler_maclaurin_envelope_closed=true
top_critical_segment_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. Taylor 有理预算

| item | value |
| --- | ---: |
| endpoint third floor | `3/16` |
| target floor | `1/8` |
| exception bound | `181/22295347200` |
| exception bound float | `0.000000008118` |
| order14 remainder bound | `2048/155925` |
| order14 remainder float | `0.013134519801` |
| certified margin | `12106823737/245248819200` |
| certified margin float | `0.049365472081` |

## 2. 14 阶包络

| component | value |
| --- | ---: |
| finite sum | `39382290.325728` |
| pole tail | `20263796.060915` |
| endpoint half | `3188097.028518` |
| Bernoulli corrections | `301759.448228` |
| remainder budget | `100000000.000000` |
| total bound | `163135942.863389` |
| contract 2^30 | `1073741824` |

## 3. 端点侦察

| order | Im derivative | alternating signed imag |
| ---: | ---: | ---: |
| 3 | `0.200257629159` | `0.200257629159` |
| 4 | `-0.240487563659` | `0.240487563659` |
| 5 | `0.272301631827` | `0.272301631827` |
| 6 | `-0.292464962583` | `0.292464962583` |
| 7 | `0.295547880244` | `0.295547880244` |
| 8 | `-0.273880335018` | `0.273880335018` |
| 9 | `0.217777591868` | `0.217777591868` |
| 10 | `-0.116322087867` | `0.116322087867` |
| 11 | `-0.040893038210` | `-0.040893038210` |
| 12 | `0.260517713080` | `-0.260517713080` |
| 13 | `-0.540042042106` | `-0.540042042106` |

## 4. 证明合同

1. 令 h=1-sigma，0<=h<=1/2，对 Im zeta'''(1-h+14i) 在 sigma=1 处作 10 阶 Taylor 展开。
2. 端点 replay 证明 Im zeta'''(1+14i)>=3/16。
3. 端点 replay 证明 4 到 10 阶虚部导数交替符号，使 Taylor 的 1 到 7 阶修正项全部非负，可直接丢弃。
4. 端点 replay 证明 |Im zeta^(11)|<=1/16、|Im zeta^(12)|<=1/3、|Im zeta^(13)|<=1。
5. Euler-Maclaurin 高阶包络证明全段 |zeta^(14)(sigma+14i)|<=2^30。
6. 有理预算给 3/16-1/8-exception-remainder>0，因此全段 Im zeta'''(sigma+14i)>=1/8。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ThirdDerivativeGateActive` | `true` | `true` | 上一层把二阶负号压成端点二阶负号和全段三阶正号。 | TopCriticalImagThirdDerivativePositiveLedgerT14HalfToOneFloor1Over8 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只压缩解析证书，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `FloatAuditSupportsTaylorLadder` | `true` | `false` | 侦察支持 3 到 10 阶端点交替符号、11 到 13 阶例外粗界和 14 阶包络。 | 不能作为自足证明，只用于确定压缩方向。 |
| `Order14EulerMaclaurinEnvelopeClosed` | `true` | `true` | EM 绝对值包络给 order14 总界 163135942.863389<2^30。 | TopCriticalDerivativeOrder14EulerMaclaurinEnvelopeBound2Pow30 |
| `TaylorBudgetStrictlyPositive` | `true` | `true` | 有理余量 12106823737/245248819200 > 0，足够推出三阶正号地板。 | Taylor arithmetic closed once endpoint intervals are supplied. |
| `EndpointSignLadderStillMissing` | `false` | `false` | 需端点 EM replay 证明 3 到 10 阶虚部导数的交替符号。 | TopEndpointImagDerivativeAlternatingSignReplaySigma1T14Orders3To10 |
| `EndpointExceptionBoundsStillMissing` | `false` | `false` | 需端点 EM replay 证明 11 到 13 阶例外项的粗绝对值界。 | TopEndpointImagDerivativeExceptionBoundReplaySigma1T14Orders11To13 |
| `TopCriticalImagThirdDerivativePositiveLedgerT14HalfToOneFloor1Over8` | `false` | `false` | 三阶正号账本已压缩为端点 Taylor 符号梯、例外界和 14 阶包络。 | TopEndpointImagDerivativeAlternatingSignReplaySigma1T14Orders3To10 AND TopEndpointImagDerivativeExceptionBoundReplaySigma1T14Orders11To13 AND TopCriticalDerivativeOrder14EulerMaclaurinEnvelopeBound2Pow30 |

## 6. 下一步

优先攻：`TopEndpointImagDerivativeAlternatingSignReplaySigma1T14Orders3To10`。
随后补：`TopEndpointImagDerivativeExceptionBoundReplaySigma1T14Orders11To13`。
再补端点二阶：`TopEndpointImagSecondDerivativeNegativeEMReplaySigma1T14FloorMinus1Over8`。
再补端点导数：`TopEndpointImagDerivativePositiveEMReplaySigma1T14Floor1Over16`。
再补端点虚部：`TopEndpointImagNegativeEMReplayLedgerSigma1T14FloorMinus1Over40`。
顶边完成后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：三阶正号已降为两个端点 replay 与一个已闭合 14 阶包络。
