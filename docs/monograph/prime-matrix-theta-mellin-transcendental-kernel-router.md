# Prime Matrix theta-Mellin 超越函数 Taylor 核路由器

**状态：** `theta_mellin_transcendental_templates_closed_range_boxes_open`

theta-Mellin 超越函数核的通用部分已经可闭合：log/trig、exp range reduction、complex power 和 Gaussian negative exponential 都能由有理 Taylor 外包模板处理。真正剩余不是再找特殊函数黑箱，而是为低高度矩形和积分分段列出有限有理范围盒，再登记每类调用的 Taylor 截断阶数和尾界。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
transcendental_templates_closed=true
theta_mellin_transcendental_kernel_closed=false
row_column_self_contained_closed=false
```

## 1. 核替换

```text
ThetaMellinElementaryTranscendentalTaylorKernel0To14 => (RationalLogTrigTaylorOracleTemplateClosed AND RationalExpTaylorRangeReductionTemplateClosed AND ThetaMellinComplexPowerTemplateClosed AND GaussianRealExpNegativeTemplateClosed AND ThetaMellinCompactRangeBoxLedger0To14 AND ThetaMellinTaylorTailOrderLedger0To14)
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ThetaMellinTranscendentalKernelGateActive` | `true` | `true` | 复球核压缩后首要数学实现点是 theta-Mellin 专用超越函数 Taylor 外包。 | ThetaMellinElementaryTranscendentalTaylorKernel0To14 |
| `RationalLogTrigTemplateAvailable` | `true` | `true` | 已有 atanh-log、Machin-pi、sin/cos Taylor 有理外包模板，半径远小于当前需求。 | RationalLogTrigTaylorOracleTemplateClosed |
| `RationalExpRangeReductionTemplateClosed` | `true` | `true` | exp 可用有理 range reduction：x=m log2+r，\|r\|<=log2/2，再对 exp(r) 用正项 Taylor 尾界。 | RationalExpTaylorRangeReductionTemplateClosed |
| `ComplexPowerTemplateClosed` | `true` | `true` | t^z=exp(Re z log t)*(cos(Im z log t)+i sin(Im z log t))，由 log/trig/exp 三模板组合。 | ThetaMellinComplexPowerTemplateClosed |
| `GaussianNegativeExpTemplateClosed` | `true` | `true` | exp(-pi n^2 t) 是负实指数，range reduction 与正项 Taylor 直接给向外上界。 | GaussianRealExpNegativeTemplateClosed |
| `CompactRangeBoxLedgerStillOpen` | `false` | `false` | 还需由矩形边界与积分分段给出所有 log t、Im z log t、pi n^2 t 的有限有理范围盒。 | ThetaMellinCompactRangeBoxLedger0To14 |
| `TaylorTailOrderLedgerStillOpen` | `false` | `false` | 有了范围盒后，还需列出每类调用的截断阶数 N 和统一尾界，形成可复核表。 | ThetaMellinTaylorTailOrderLedger0To14 |
| `TraceAndThetaDownstream` | `false` | `false` | 超越核实例化后仍需调用轨迹、theta 尾界和紧致积分分段证书。 | IntervalOperationTraceHashLedger AND GaussianThetaTailBoundLedger AND CompactThetaMellinQuadratureSubdivisionLedger0To14 |

## 3. 下一步

当前最窄点：`ThetaMellinCompactRangeBoxLedger0To14`。
随后补 `ThetaMellinTaylorTailOrderLedger0To14`。
完成后回到 `IntervalOperationTraceHashLedger AND GaussianThetaTailBoundLedger AND CompactThetaMellinQuadratureSubdivisionLedger0To14`。

判定：超越函数公式模板已闭合，剩余变成有限范围盒和尾阶表，不再是开放特殊函数理论问题。
