# Prime Matrix 紧致 theta-Mellin 求积细分账本路由器

**状态：** `compact_theta_mellin_quadrature_closed_boundary_certificates_next`

CompactThetaMellinQuadratureSubdivisionLedger0To14 已闭合：用半径 1/2 解析管道、1/16 dyadic 细分和 80 阶 Taylor 积分，xi 级求积误差小于 1e-80。因此自足 xi 区间求值引擎闭合；剩余转为边界非零证书和 winding=0 证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
compact_theta_mellin_quadrature_subdivision_closed=true
self_contained_xi_interval_engine_closed=true
lowheight_rectangle_count_closed=false
row_column_self_contained_closed=false
```

## 1. 求积参数

| item | value |
| --- | ---: |
| t window | `['1', '64']` |
| segment count | `1008` |
| segment width | `1/16` |
| Cauchy radius | `1/2` |
| Cauchy ratio | `1/16` |
| Taylor degree | `80` |
| integrand sup bound | `1.000000E+6` |
| Lambda quadrature error | `1.966304E-90` |
| xi quadrature error | `2.212092E-88` |
| target | `1.000000E-80` |
| margin factor | `4.520607E+7` |

## 2. 证明链

1. 在 [1,64] 的每个实点取半径 1/2 的复圆盘；该圆盘不碰负实轴，log 与 t^a 单值分支固定。
2. 若 z 在这些圆盘内，则 Re z>=1/2, |z|>=1/2, |arg z|<=pi/4。
3. 对 a=s/2-1 或 a=(1-s)/2-1，低高度盒给 Re a in [-3/2,0], |Im a|<=7。
4. 于是 |z^a|<=|z|^Re(a)*exp(|Im(a)||arg z|)<3*exp(7)<1e4。
5. 有限 theta 项只有 n<=20，Lambda 对称积分的有限核至多 40 个这样的项，统一取解析管道上界 1e6。
6. 每段宽 1/16，中心到端点半径 1/32；相对 Cauchy 半径比 r=(1/32)/(1/2)=1/16。
7. 80 阶 Taylor 积分余项在全区间上 <=63*1e6*r^81/(1-r)，再乘 |s(s-1)|/2<=225/2。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CompactQuadratureGateActive` | `true` | `true` | Gaussian theta 尾项闭合后，唯一剩余实现点是 [1,64] 紧致积分分段误差。 | CompactThetaMellinQuadratureSubdivisionLedger0To14 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只是构造可复核的 xi 区间求值引擎，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `TraceAndTailInputsImported` | `true` | `true` | 复球核 trace/hash 和 Gaussian theta 尾项已经闭合，求积只处理有限紧致核。 | finite compact integrand only. |
| `CompactWindowAndFiniteThetaImported` | `true` | `true` | 范围盒固定 1<=t<=64、n<=20、低高度 s 矩形；求积对象为有限解析函数。 | compact analytic finite sum. |
| `AnalyticTubeSupBoundClosed` | `true` | `true` | 半径 1/2 的复管道内 log 分支固定，有限 theta-Mellin 核统一上界取 1e6。 | Cauchy bound available. |
| `DyadicSubdivisionTaylorRemainderClosed` | `true` | `true` | 1008 段、每段宽 1/16、80 阶 Taylor 积分给 xi 求积误差 <= 2.212092E-88。 | CompactThetaMellinQuadratureSubdivisionClosedH16Deg80Xi1eMinus80 |
| `PolynomialIntegralTraceable` | `true` | `true` | 每段 Taylor 多项式积分只含 dyadic 区间、exp/log/trig 节点和父哈希，可进入已闭合 trace 账本。 | IntervalOperationTraceHashLedgerClosedCanonicalDAGv1 |
| `CompactThetaMellinQuadratureSubdivisionLedger0To14` | `true` | `true` | 紧致 theta-Mellin 求积细分账本已闭合，xi 区间求值引擎的三大实现输入齐全。 | CompactThetaMellinQuadratureSubdivisionClosedH16Deg80Xi1eMinus80 |
| `BoundaryCertificatesStillDownstream` | `false` | `false` | 求值引擎闭合不等于边界非零或 winding=0；后者仍需单独证书。 | XiBoundaryIntervalNonzeroCertificate0To14 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14 |

## 4. 下一步

当前最窄点：`XiBoundaryIntervalNonzeroCertificate0To14`。
随后补：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：求值引擎已经闭合；低高度矩形零点计数仍需边界非零和 winding 两张证书。
