# Prime Matrix 复球区间算术核压缩路由器

**状态：** `complex_ball_kernel_algebra_closed_transcendental_kernel_open`

复球区间核不是一个不可拆黑箱。dyadic 有理区间和复矩形传播可由整数端点不等式自足闭合，已有 trig/log Taylor oracle 可作为模板复用。真正剩余是 theta-Mellin 专用的超越函数 Taylor 外包和操作 trace/hash 账本；完整复球核尚未闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
dyadic_algebra_core_closed=true
certified_complex_ball_kernel_closed=false
trig_log_oracle_half_radius=2.3333375863797428e-67
row_column_self_contained_closed=false
```

## 1. 核替换

```text
CertifiedComplexBallArithmeticKernel => (DyadicRationalIntervalArithmeticCoreClosed AND ComplexRectangularIntervalPropagationClosed AND RationalLogTrigTaylorOracleTemplateClosed AND ThetaMellinElementaryTranscendentalTaylorKernel0To14 AND IntervalOperationTraceHashLedger)
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CertifiedComplexBallKernelGateActive` | `true` | `true` | theta-Mellin xi 区间引擎的首要缺口正是复球/区间算术核。 | CertifiedComplexBallArithmeticKernel |
| `DyadicRationalIntervalCoreClosed` | `true` | `true` | 用整数端点 dyadic 区间 [a/2^k,b/2^k]，加减乘除都由有限整数不等式给出外包。 | DyadicRationalIntervalArithmeticCoreClosed |
| `ComplexRectangularPropagationClosed` | `true` | `true` | 复数盒写成 Re 区间 x Im 区间；加乘除退化为有限个实区间端点组合和不含零检查。 | ComplexRectangularIntervalPropagationClosed |
| `ExistingRationalTrigLogTemplateReusable` | `true` | `true` | 已有 trig/log 有理 Taylor oracle 证明模板，半径约 2.33e-67；可复用其 Machin/atanh/Taylor 结构。 | RationalLogTrigTaylorOracleTemplateClosed |
| `ThetaMellinTranscendentalKernelStillOpen` | `false` | `false` | theta-Mellin 引擎需要把 exp(-pi n^2 t)、t^z、sin/cos 的 Taylor 外包统一到 0<=Im z<=14 的紧致盒。 | ThetaMellinElementaryTranscendentalTaylorKernel0To14 |
| `OperationTraceHashLedgerStillOpen` | `false` | `false` | 每个区间调用必须输出端点、截断阶数、尾界、父节点 hash，供矩形边界证书复核。 | IntervalOperationTraceHashLedger |
| `ThetaTailAndQuadratureRemainDownstream` | `false` | `false` | 复球核压缩后，theta 尾界与紧致积分分段仍是独立后续账本。 | GaussianThetaTailBoundLedger AND CompactThetaMellinQuadratureSubdivisionLedger0To14 |

## 3. 下一步

当前最窄数学实现点：`ThetaMellinElementaryTranscendentalTaylorKernel0To14`。
审计并行点：`IntervalOperationTraceHashLedger`。
完成后回到 `GaussianThetaTailBoundLedger AND CompactThetaMellinQuadratureSubdivisionLedger0To14`。

判定：代数核已剥离并闭合；完整区间引擎仍需超越函数外包和调用轨迹。
