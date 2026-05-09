# Prime Matrix xi 边界 winding 三包聚合闭合路由器

**状态：** `xi_boundary_winding_and_lowheight_rectangle_count_self_contained_closed`

winding 原子已自足闭合：节点下界、导数管道和多边形整数绕数三包完成聚合，真实 xi 边界曲线绕原点次数为 0。结合 xi 整函数、边界非零与 argument principle，低高度矩形 xi 零点计数也闭合为 0。本步不声称完整行列定理闭合，而是关闭此前唯一最窄的低高度 xi/winding 输入包。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
winding_self_contained_closed=true
lowheight_rectangle_count_self_contained_closed=true
row_column_self_contained_closed=false
winding_aggregation_root_hash=a5e0f343cc64fcb63a5689db8c97b0118db96b95a755de6ef3520ad9644419dc
```

## 1. 闭合链

| step | input | output |
| --- | --- | --- |
| MeshCompression | XiBoundaryArgumentVariationDyadicTraceLedger0To14Mesh8192 | XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000 AND XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12 AND XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768 |
| NodeLowerBound | 32769 个边界节点 xi 区间值 | 所有节点 \|xi\|>=1/6000 |
| DerivativeTube | 32768 条边段 xi' 区间管道 | 所有边段 \|xi'\|<=1/12 |
| PolygonInteger | 函数方程、共轭对称、底边正实、顶边中心正实 | 离散多边形绕数整数为 0 |
| Homotopy | \|xi\| 下界 + \|xi'\| 上界 + 多边形绕数 0 | 真实边界曲线 winding=0 |
| ArgumentPrinciple | xi 整函数 + 边界非零 + winding=0 | 低高度矩形内 xi 零点计数为 0 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WindingAggregationGateActive` | `true` | `true` | 多边形包闭合后，当前目标是聚合回原 winding 原子。 | XiBoundaryWindingNumberZeroIntervalCertificate0To14 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 聚合仍只使用假设链条中的解析证书，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `MeshCompressionImported` | `true` | `true` | winding trace 已被压缩为节点下界、导数管道、多边形整数绕数三包。 | XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000 AND XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12 AND XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768 |
| `NodeLowerBoundPackageClosed` | `true` | `true` | 节点下界 root 已闭合，提供边界离原点的离散距离。 | XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000 |
| `DerivativeTubePackageClosed` | `true` | `true` | 导数管道 root 已闭合，提供从离散节点到整段曲线的同伦管道。 | XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12 |
| `PolygonIntegerWindingClosed` | `true` | `true` | 多边形整数绕数由对称角变化配平闭合为 0。 | XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768 |
| `HomotopyNoCrossingClosed` | `true` | `true` | 1/6000-(1/12)*(14/8192)>0，真实边界曲线与离散多边形同伦且不穿过 0。 | continuous boundary winding equals polygon winding. |
| `XiBoundaryWindingNumberZeroIntervalCertificate0To14` | `true` | `true` | 三包 root 聚合完成，winding=0；聚合 root=a5e0f343cc64fcb63a5689db8c97b0118db96b95a755de6ef3520ad9644419dc。 | XiBoundaryWindingNumberZeroSelfContainedClosedMesh32768RootHash |
| `LowHeightRectangleCountZero` | `true` | `true` | xi 区间引擎、边界非零、winding=0、xi 整函数和 argument principle 齐备，低高度矩形零点计数为 0。 | LowHeightXiRectangleZeroCountZero0To14SelfContainedClosed |
| `RowColumnTheoremStillSeparate` | `false` | `false` | 这关闭低高度 xi 边界/winding 包；完整行列定理仍需后续筛法全局包接力。 | global row-column sieve closure remains outside this xi package. |

## 3. 下一步

当前 xi 低高度包之后的下一层：`GlobalRowColumnSieveClosureAfterLowHeightXiPackage`。

判定：低高度 xi 边界/winding 输入包已关闭，但完整行列命题仍需后续全局筛法链条接上。
