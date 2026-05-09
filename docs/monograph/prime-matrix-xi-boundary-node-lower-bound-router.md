# Prime Matrix xi 边界节点下界包路由器

**状态：** `xi_boundary_trace_node_lower_bound_closed_derivative_tube_next`

节点下界包已闭合：32769 个边界节点全部满足 |xi|>=1/6000。最坏节点是 index=20480，位于 top_t14，|xi|≈2.012944442353e-04；扣除 2^-40 求值半径后仍有 3.462777665910e-05 的正余量。下一步转入边段导数管道包。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
node_lower_bound_closed=true
winding_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 节点账本摘要

| item | value |
| --- | ---: |
| node count | `32769` |
| edge count | `32768` |
| leaf hash count | `32769` |
| node Merkle/root hash | `0ee537fe85fb7b57ca3d42530919431acffeb29134df2bbf16e2bcb7af823458` |
| node floor | `1/6000` |
| eval radius | `1/1099511627776` |
| min abs value | `2.012944442353e-04` |
| min index | `20480` |
| min side | `top_t14` |
| raw margin | `3.462777756860e-05` |
| certified margin | `3.462777665910e-05` |

## 2. 每边最小值

| side | index | point | abs value | certified margin |
| --- | ---: | --- | ---: | ---: |
| bottom_t0 | `4096` | `(0.500000, 0.000000)` | `4.971207781883e-01` | `4.969541115207e-01` |
| right_sigma2 | `16384` | `(2.000000, 14.000000)` | `2.423522315875e-03` | `2.256855648299e-03` |
| top_t14 | `20480` | `(0.500000, 14.000000)` | `2.012944442353e-04` | `3.462777665910e-05` |
| left_sigma_minus1 | `24577` | `(-1.000000, 13.998291)` | `2.426096615078e-03` | `2.259429947502e-03` |

## 3. 最坏节点前 16 个

| rank | index | side | point | abs value | certified margin |
| ---: | ---: | --- | --- | ---: | ---: |
| 1 | `20480` | top_t14 | `(0.500000, 14.000000)` | `2.012944442353e-04` | `3.462777665910e-05` |
| 2 | `20481` | top_t14 | `(0.499634, 14.000000)` | `2.012951887794e-04` | `3.462852120320e-05` |
| 3 | `20479` | top_t14 | `(0.500366, 14.000000)` | `2.012951887794e-04` | `3.462852120320e-05` |
| 4 | `20482` | top_t14 | `(0.499268, 14.000000)` | `2.012974223952e-04` | `3.463075481903e-05` |
| 5 | `20478` | top_t14 | `(0.500732, 14.000000)` | `2.012974223952e-04` | `3.463075481903e-05` |
| 6 | `20483` | top_t14 | `(0.498901, 14.000000)` | `2.013011450334e-04` | `3.463447745727e-05` |
| 7 | `20477` | top_t14 | `(0.501099, 14.000000)` | `2.013011450334e-04` | `3.463447745727e-05` |
| 8 | `20484` | top_t14 | `(0.498535, 14.000000)` | `2.013063566119e-04` | `3.463968903572e-05` |
| 9 | `20476` | top_t14 | `(0.501465, 14.000000)` | `2.013063566119e-04` | `3.463968903572e-05` |
| 10 | `20485` | top_t14 | `(0.498169, 14.000000)` | `2.013130570154e-04` | `3.464638943929e-05` |
| 11 | `20475` | top_t14 | `(0.501831, 14.000000)` | `2.013130570154e-04` | `3.464638943929e-05` |
| 12 | `20474` | top_t14 | `(0.502197, 14.000000)` | `2.013212460962e-04` | `3.465457852004e-05` |
| 13 | `20486` | top_t14 | `(0.497803, 14.000000)` | `2.013212460962e-04` | `3.465457852004e-05` |
| 14 | `20473` | top_t14 | `(0.502563, 14.000000)` | `2.013309236734e-04` | `3.466425609721e-05` |
| 15 | `20487` | top_t14 | `(0.497437, 14.000000)` | `2.013309236734e-04` | `3.466425609721e-05` |
| 16 | `20488` | top_t14 | `(0.497070, 14.000000)` | `2.013420895333e-04` | `3.467542195718e-05` |

## 4. 证明合同

1. 沿矩形边界生成 32769 个 dyadic 节点，与 winding mesh 合同使用同一顺序。
2. 每个节点调用已闭合的 SelfContainedXiIntervalEvaluationEngine0To14，给出 xi(s_j) 的复区间盒。
3. 复盒半径统一收敛到 2^-40；该半径远大于 theta-Mellin 求积误差 1e-80，且仍小于最小余量。
4. 对每个节点登记 leaf hash：index、节点坐标、xi 盒中心、模长审计值和余量。
5. 逐节点验证 |xi(s_j)| - 2^-40 >= 1/6000；最坏节点在 top_t14 的 sigma=1/2。
6. 所有 leaf hash 的 Merkle/root hash 固定整张节点下界账本，后续 winding trace 只引用该 root。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NodeLowerBoundGateActive` | `true` | `true` | 上一层唯一最窄点是 32769 个边界节点的 xi 下界。 | XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只物化假设链条中的有限求值 trace，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `XiIntervalEngineImported` | `true` | `true` | 紧致 theta-Mellin 求积账本已把 SelfContainedXiIntervalEvaluationEngine0To14 关闭。 | SelfContainedXiIntervalEvaluationEngine0To14Closed |
| `TraceHashDisciplineImported` | `true` | `true` | 节点 leaf/root hash 服从已闭合 canonical DAG trace 纪律。 | IntervalOperationTraceHashLedgerClosedCanonicalDAGv1 |
| `NodeEvaluationRadiusBudgetClosed` | `true` | `true` | 最小 \|xi\|=2.012944442353e-04，扣除 2^-40 后仍高于 1/6000，余量 3.462777665910e-05。 | XiBoundaryTraceNodeLowerBoundClosedMesh32768Floor1Over6000RootHash |
| `XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000` | `true` | `true` | 节点下界账本已闭合；所有边界节点均满足 \|xi\|>=1/6000。 | XiBoundaryTraceNodeLowerBoundClosedMesh32768Floor1Over6000RootHash |
| `DerivativeTubeStillMissing` | `false` | `false` | 节点下界不替代边段导数管道。 | XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12 |
| `PolygonWindingStillMissing` | `false` | `false` | 节点下界不替代离散多边形绕数整数校验。 | XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768 |

## 6. 下一步

当前最窄点更新为：`XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12`。
之后聚合：`XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768`。

判定：节点下界包关闭，剩余转为边段导数管道。
