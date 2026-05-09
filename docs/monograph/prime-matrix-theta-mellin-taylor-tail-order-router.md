# Prime Matrix theta-Mellin Taylor 尾阶账本路由器

**状态：** `theta_mellin_taylor_tail_orders_closed_trace_theta_quadrature_open`

theta-Mellin 超越函数调用的 Taylor 尾阶账本已闭合：log、pi、trig、exp 都给出保守阶数，最大模板尾界小于 1e-60。剩余不再是 Taylor 理论，而是把这些调用实际登记成 trace/hash，并证明 Gaussian theta 尾项和紧致积分分段误差。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
tail_orders_closed=true
theta_mellin_transcendental_kernel_closed=false
max_tail_bound_float=9.637027e-118
row_column_self_contained_closed=false
```

## 1. 尾界表

| call | order | tail bound |
| --- | ---: | ---: |
| log atanh | 120 | `9.637027e-118` |
| pi Machin | 120 | `2.346021e-170` |
| sin/cos Taylor | 120 | `8.731317e-129` |
| exp Taylor | 80 | `2.853761e-145` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TaylorTailOrderGateActive` | `true` | `true` | 范围盒闭合后，当前最窄点是为每类 Taylor 调用指定截断阶数与尾界。 | ThetaMellinTaylorTailOrderLedger0To14 |
| `RangeBoxesAvailable` | `true` | `true` | log/power/trig/exp 的有理范围盒已闭合。 | ThetaMellinCompactRangeBoxClosed0To14T64N20 |
| `LogTailOrderClosed` | `true` | `true` | log 使用 atanh 级数 120 项，缩放后 z<=1/3，尾界 9.637027e-118。 | ThetaMellinTaylorTailOrdersClosedLog120Pi120Trig120Exp80 |
| `PiTailOrderClosed` | `true` | `true` | pi 使用 Machin 公式 120 项，主尾界 2.346021e-170。 | ThetaMellinTaylorTailOrdersClosedLog120Pi120Trig120Exp80 |
| `TrigTailOrderClosed` | `true` | `true` | sin/cos range reduction 到 \|x\|<=pi<4 后用 120 阶，尾界 8.731317e-129。 | ThetaMellinTaylorTailOrdersClosedLog120Pi120Trig120Exp80 |
| `ExpTailOrderClosed` | `true` | `true` | exp range reduction 到 \|r\|<=1/2 后用 80 阶，尾界 2.853761e-145。 | ThetaMellinTaylorTailOrdersClosedLog120Pi120Trig120Exp80 |
| `TraceThetaQuadratureStillDownstream` | `false` | `false` | 尾阶表不替代实际调用轨迹、Gaussian theta 尾项或积分分段误差。 | IntervalOperationTraceHashLedger AND GaussianThetaTailBoundLedger AND CompactThetaMellinQuadratureSubdivisionLedger0To14 |

## 3. 下一步

当前最窄点：`IntervalOperationTraceHashLedger`。
随后补 `GaussianThetaTailBoundLedger` 与 `CompactThetaMellinQuadratureSubdivisionLedger0To14`。

判定：Taylor 尾阶已闭合，剩余是可复核调用日志、theta 尾项和积分分段。
