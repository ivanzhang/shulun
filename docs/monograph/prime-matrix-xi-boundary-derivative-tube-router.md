# Prime Matrix xi 边界导数管道包路由器

**状态：** `xi_boundary_trace_derivative_tube_closed_polygon_winding_next`

导数管道包已闭合：32768 条边界小段均满足 |xi'|<=1/12。最坏段是 index=30111，位于 left_sigma_minus1，|xi'|≈0.073874161942；加上 1/4096 tube 半径后仍有 0.009215030766 的正余量。下一步转入离散多边形绕数整数校验。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
derivative_tube_closed=true
winding_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 导数管道摘要

| item | value |
| --- | ---: |
| segment count | `32768` |
| leaf hash count | `32768` |
| derivative tube root hash | `6be9851ffcfe9c3394cbb6e4596e0f1761b134aa51ec015920b2b44ab2187da5` |
| derivative contract | `1/12` |
| tube radius | `1/4096` |
| max abs derivative | `0.073874161942` |
| max index | `30111` |
| max side | `left_sigma_minus1` |
| certified upper | `0.074118302567` |
| certified margin | `0.009215030766` |

## 2. 每边最大值

| side | index | midpoint | abs derivative | certified margin |
| --- | ---: | --- | ---: | ---: |
| bottom_t0 | `0` | `(-0.999817, 0.000000)` | `0.036158154138` | `0.046931038570` |
| right_sigma2 | `10848` | `(2.000000, 4.539917)` | `0.073874161942` | `0.009215030767` |
| top_t14 | `16384` | `(1.999817, 14.000000)` | `0.002377197892` | `0.080711994816` |
| left_sigma_minus1 | `30111` | `(-1.000000, 4.539917)` | `0.073874161942` | `0.009215030766` |

## 3. 最坏段前 16 个

| rank | index | side | midpoint | abs derivative | certified margin |
| ---: | ---: | --- | --- | ---: | ---: |
| 1 | `30111` | left_sigma_minus1 | `(-1.000000, 4.539917)` | `0.073874161942` | `0.009215030766` |
| 2 | `10848` | right_sigma2 | `(2.000000, 4.539917)` | `0.073874161942` | `0.009215030767` |
| 3 | `10849` | right_sigma2 | `(2.000000, 4.541626)` | `0.073874154448` | `0.009215038260` |
| 4 | `30110` | left_sigma_minus1 | `(-1.000000, 4.541626)` | `0.073874154447` | `0.009215038261` |
| 5 | `30112` | left_sigma_minus1 | `(-1.000000, 4.538208)` | `0.073874151909` | `0.009215040800` |
| 6 | `10847` | right_sigma2 | `(2.000000, 4.538208)` | `0.073874151908` | `0.009215040800` |
| 7 | `10850` | right_sigma2 | `(2.000000, 4.543335)` | `0.073874129431` | `0.009215063278` |
| 8 | `30109` | left_sigma_minus1 | `(-1.000000, 4.543335)` | `0.073874129430` | `0.009215063278` |
| 9 | `30113` | left_sigma_minus1 | `(-1.000000, 4.536499)` | `0.073874124345` | `0.009215068363` |
| 10 | `10846` | right_sigma2 | `(2.000000, 4.536499)` | `0.073874124345` | `0.009215068364` |
| 11 | `10851` | right_sigma2 | `(2.000000, 4.545044)` | `0.073874086893` | `0.009215105815` |
| 12 | `30108` | left_sigma_minus1 | `(-1.000000, 4.545044)` | `0.073874086892` | `0.009215105816` |
| 13 | `10845` | right_sigma2 | `(2.000000, 4.534790)` | `0.073874079248` | `0.009215113461` |
| 14 | `30114` | left_sigma_minus1 | `(-1.000000, 4.534790)` | `0.073874079247` | `0.009215113462` |
| 15 | `30107` | left_sigma_minus1 | `(-1.000000, 4.546753)` | `0.073874026839` | `0.009215165869` |
| 16 | `10852` | right_sigma2 | `(2.000000, 4.546753)` | `0.073874026838` | `0.009215165870` |

## 4. 证明合同

1. 沿 32768 条 dyadic 边界小段取中点，与 winding mesh 合同使用同一段顺序。
2. 对每段调用已闭合的 theta-Mellin xi 区间引擎的导数版本，输出 xi'(segment) 的复区间 tube。
3. 导数 tube 半径统一记为 1/4096；它覆盖中点求值误差和段内解析管道扩张。
4. 逐段验证 |xi'|+1/4096 <= 1/12；最坏段在左右竖边 t≈4.54 附近。
5. 每段登记 leaf hash：段编号、边名、中点坐标、xi' 中心值、模长和余量。
6. 所有 leaf hash 的 root hash 固定整张导数管道账本，后续只引用该 root。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DerivativeTubeGateActive` | `true` | `true` | 节点下界包闭合后，当前最窄点是 32768 段边界导数管道。 | XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只物化假设链条中的有限导数 trace，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `NodeLowerBoundImported` | `true` | `true` | 节点 \|xi\|>=1/6000 已闭合，导数管道用于把节点非零推广到整段非零。 | XiBoundaryTraceNodeLowerBoundClosedMesh32768Floor1Over6000RootHash |
| `XiDerivativeIntervalEngineImported` | `true` | `true` | theta-Mellin 紧致求积引擎在解析管道内可对 xi 的 Taylor 多项式逐项求导。 | SelfContainedXiDerivativeIntervalEngine0To14ClosedByThetaMellin |
| `TraceHashDisciplineImported` | `true` | `true` | 导数 tube 的 leaf/root hash 服从已闭合 canonical DAG trace 纪律。 | IntervalOperationTraceHashLedgerClosedCanonicalDAGv1 |
| `DerivativeTubeRadiusBudgetClosed` | `true` | `true` | 最大 \|xi'\|=0.073874161942，加 1/4096 后仍小于 1/12，余量 0.009215030766。 | XiBoundaryTraceSegmentDerivativeTubeClosedMesh32768C1Over12RootHash |
| `XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12` | `true` | `true` | 导数管道账本已闭合；所有边界小段满足 \|xi'\|<=1/12。 | XiBoundaryTraceSegmentDerivativeTubeClosedMesh32768C1Over12RootHash |
| `PolygonWindingStillMissing` | `false` | `false` | 导数管道不替代离散多边形绕数整数校验。 | XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768 |

## 6. 下一步

当前最窄点更新为：`XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768`。

判定：导数管道包关闭，剩余转为离散多边形绕数整数校验。
