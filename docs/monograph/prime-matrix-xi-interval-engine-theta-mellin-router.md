# Prime Matrix xi 区间求值引擎 theta-Mellin 路由器

**状态：** `xi_interval_engine_routed_to_theta_mellin_open`

xi 区间求值引擎不用再固定为 Riemann-Siegel 路线。由于 theta-Poisson、theta-Mellin 和 xi 整函数层已闭合，低高度紧致矩形可改用 theta-Mellin 对称积分的复球区间引擎。真正剩余变成可实现的球算术核、高斯 theta 尾界和紧致积分分段证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
theta_mellin_interval_engine_route_selected=true
self_contained_xi_interval_engine_closed=false
row_column_self_contained_closed=false
```

## 1. 引擎替换

```text
SelfContainedXiIntervalEvaluationEngine0To14 => (ThetaMellinXiCompactIntervalEngine0To14 AND CertifiedComplexBallArithmeticKernel AND GaussianThetaTailBoundLedger AND CompactThetaMellinQuadratureSubdivisionLedger0To14)
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RectangleCountNeedsXiEngine` | `true` | `true` | 矩形计数单原子当前首要缺口是 xi 区间求值引擎。 | SelfContainedXiIntervalEvaluationEngine0To14 |
| `ThetaMellinAndXiInputsAvailable` | `true` | `true` | theta-Mellin 延拓、函数方程、xi 整函数性和增长层均已在仓库内闭合。 | 可用 theta-Mellin 紧致积分构造 xi 区间引擎。 |
| `RiemannSiegelEngineNotPrimary` | `true` | `true` | 低高度 0<=t<=14 是紧致小盒；用 theta-Mellin 对称积分比从零实现 Riemann-Siegel 更贴合已有自足材料。 | ThetaMellinXiCompactIntervalEngine0To14 |
| `CertifiedBallArithmeticKernelMissing` | `false` | `false` | 仍需复球区间加减乘除、exp/log/Gamma 或 theta 项指数的向外舍入实现与审计。 | CertifiedComplexBallArithmeticKernel |
| `GaussianThetaTailBoundMissing` | `false` | `false` | theta 尾项需要显式高斯尾界，保证截断到有限 n 与有限积分段后仍有严格外包。 | GaussianThetaTailBoundLedger |
| `CompactQuadratureSubdivisionMissing` | `false` | `false` | 边界曲线上的 xi 值需要有限分段积分/求和证书，并给每段误差半径。 | CompactThetaMellinQuadratureSubdivisionLedger0To14 |
| `BoundaryAndWindingStillDownstream` | `false` | `false` | 引擎完成后才可证明边界非零和 winding=0。 | XiBoundaryIntervalNonzeroCertificate0To14 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14 |

## 3. 下一步

先攻 `CertifiedComplexBallArithmeticKernel`，再攻 `GaussianThetaTailBoundLedger` 与 `CompactThetaMellinQuadratureSubdivisionLedger0To14`。
完成引擎后进入 `XiBoundaryIntervalNonzeroCertificate0To14 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：本步把求值引擎路线换成可复用已有 theta-Mellin 材料的自足路线，但尚未给出区间实现。
