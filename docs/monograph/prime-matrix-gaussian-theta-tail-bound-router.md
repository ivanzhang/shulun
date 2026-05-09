# Prime Matrix Gaussian theta 尾界账本路由器

**状态：** `gaussian_theta_tail_bound_closed_quadrature_next`

GaussianThetaTailBoundLedger 已闭合：在 theta-Mellin 对称积分中，低高度矩形不会放大 Gaussian 尾；n>20 和 t>64 的 xi 级总尾界小于 1e-80。剩余集中到 [1,64] 紧致窗口的积分分段/求积账本。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
gaussian_theta_tail_bound_closed=true
theta_mellin_interval_engine_closed=false
row_column_self_contained_closed=false
```

## 1. 尾界参数

| item | value |
| --- | ---: |
| n cutoff | `20` |
| t cutoff | `64` |
| n-tail Lambda bound | `8.107754E-578` |
| t-tail Lambda bound | `5.500450E-84` |
| total Lambda tail | `5.500450E-84` |
| xi multiplier | `1.125000E+2` |
| total xi tail | `6.188006E-82` |
| target | `1.000000E-80` |
| margin factor | `1.616029E+1` |

## 2. 证明链

1. theta_0(t)=2*sum_{n>=1} exp(-pi*n^2*t).
2. 在 -1<=sigma<=2 且 t>=1 上，|t^(s/2-1)|<=1 且 |t^((1-s)/2-1)|<=1。
3. 因此 Lambda 对称积分的尾误差不超过被删去 theta_0(t) 的积分。
4. n>N 的级数尾：int_1^infty 2*sum_{n>=N+1} exp(-pi*n^2*t) dt <= 4/(3*(N+1)^2)*exp(-3*(N+1)^2)。
5. t>T 的积分尾：int_T^infty 2*sum_{n>=1} exp(-pi*n^2*t) dt <= 4/3*exp(-3*T)。
6. |s|<=15 且 |s-1|<=15，所以 xi(s)=1/2*s*(s-1)*Lambda(s) 的尾误差乘子 <=225/2。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `GaussianThetaTailGateActive` | `true` | `true` | trace/hash 闭合后，当前最窄点是 theta 级数和 t 积分截断尾界。 | GaussianThetaTailBoundLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只是解析尾界，不使用真实零行缺席或数值采样代替证明。 | 保持 row_column_self_contained_closed=false。 |
| `ThetaMellinFormulaImported` | `true` | `true` | 已闭合 Lambda(s) 的 [1,infty) 对称 theta-Mellin 积分公式。 | Lambda symmetric integral available. |
| `FiniteWindowImported` | `true` | `true` | 范围盒固定主窗口 1<=t<=64 与有限 theta 项 1<=n<=20。 | n>20 and t>64 are exactly the tails paid here. |
| `PowerWeightsDoNotAmplifyTail` | `true` | `true` | 在 -1<=Re(s)<=2, t>=1 上两个 Mellin 幂权模长均不超过 1，总权重不超过 2。 | tail reduces to Gaussian theta_0 integral. |
| `SeriesTailNGreater20Closed` | `true` | `true` | 用 pi>3 与几何比<1/2 得 n>20 对 Lambda 的贡献 <= 8.107754E-578。 | GaussianThetaTailBoundClosedN20T64Xi1eMinus80 |
| `IntegralTailTGreater64Closed` | `true` | `true` | 用 pi>3 与几何比<1/2 得 t>64 对 Lambda 的贡献 <= 5.500450E-84。 | GaussianThetaTailBoundClosedN20T64Xi1eMinus80 |
| `XiMultiplierTailStillTiny` | `true` | `true` | 乘上 \|s(s-1)\|/2<=225/2 后 xi 总尾界 <= 6.188006E-82 < 1.000000E-80。 | GaussianThetaTailBoundClosedN20T64Xi1eMinus80 |
| `GaussianThetaTailBoundLedger` | `true` | `true` | Gaussian theta 截断尾项账本已闭合，有限引擎可只处理 n<=20 与 1<=t<=64。 | GaussianThetaTailBoundClosedN20T64Xi1eMinus80 |
| `QuadratureStillDownstream` | `false` | `false` | 本步不支付 [1,64] 紧致区间上的积分分段/求积误差。 | CompactThetaMellinQuadratureSubdivisionLedger0To14 |

## 4. 下一步

当前最窄点：`CompactThetaMellinQuadratureSubdivisionLedger0To14`。
后续进入：`XiBoundaryIntervalNonzeroCertificate0To14 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：theta 尾项已支付；仍需紧致积分分段账本，不能据此直接宣称低高度矩形证书闭合。
