# Prime Matrix xi 边界 winding 网格合同压缩路由器

**状态：** `winding_trace_reduced_to_node_tube_polygon_contracts_open`

winding trace 已进一步压缩为三项有限合同：节点 |xi|>=1/6000、边段 |xi'|<=1/12、离散多边形绕数为 0。有理管道余量为正；浮点侦察支持这些常数。严格自足仍需把三包实际 interval trace/hash 物化。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
winding_trace_mesh_contracts_selected=true
winding_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 网格侦察与合同

| item | value |
| --- | ---: |
| edge count | `32768` |
| node count | `32769` |
| trace root hash | `82194b686d5363957b7350e1e39f67559c472945e5b4f3bd98395d1d9eb6cf93` |
| winding float | `-1.064623900396e-15` |
| max step angle | `0.002927157640` |
| min abs value | `2.012944442353e-04` |
| node floor | `1/6000` |
| node floor audit margin | `3.462777756860e-05` |
| max adjacent displacement ratio | `0.073874161047` |
| derivative contract | `1/12` |
| derivative contract audit margin | `0.009459172287` |
| tube loss under contract | `1.424153645833e-04` |
| tube margin after node floor | `2.425130208333e-05` |

## 2. 证明合同

1. 在 32768 条 dyadic 边界小段上登记 xi 节点区间值，并证明每个节点 |xi|>=1/6000。
2. 在每条小段上登记 xi' 区间包络，并证明 |xi'|<=1/12。
3. 最大边界小段长度为 14/8192，因此任意段内偏移至多 (1/12)*(14/8192)。
4. 有理余量 1/6000-(1/12)*(14/8192)>0，所以整段像不穿过 0。
5. 离散多边形的每步辐角增量由点积/叉积有理区间确定，总和落在 (-pi,pi) 且整数绕数为 0。
6. 节点下界、导数管道和多边形绕数三项齐备时，XiBoundaryWindingNumberZeroIntervalCertificate0To14 闭合。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WindingTraceMeshGateActive` | `true` | `true` | 上一层已把 winding 压成有限 dyadic argument-variation trace。 | XiBoundaryArgumentVariationDyadicTraceLedger0To14Mesh8192 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只压缩假设链条中的有限 trace 证书。 | 保持 row_column_self_contained_closed=false。 |
| `FloatAuditSupportsMeshContracts` | `true` | `false` | 侦察 min\|xi\|=2.012944e-04>1/6000，max adjacent ratio=0.073874<1/12，polygon winding=0。 | 不能作为自足证明，只用于确定合同常数。 |
| `TubeMarginArithmeticClosed` | `true` | `true` | 1/6000-(1/12)*(14/8192)>0，节点下界加导数管道足以排除段内穿零。 | integer arithmetic closed. |
| `NodeLowerBoundStillMissing` | `false` | `false` | 需 interval trace/hash 逐节点证明 \|xi\|>=1/6000。 | XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000 |
| `DerivativeTubeStillMissing` | `false` | `false` | 需 interval trace/hash 逐段证明 \|xi'\|<=1/12。 | XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12 |
| `PolygonWindingIntegerStillMissing` | `false` | `false` | 需有理点积/叉积区间累加证明离散多边形绕数整数为 0。 | XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768 |
| `XiBoundaryArgumentVariationDyadicTraceLedger0To14Mesh8192` | `false` | `false` | winding trace 已压成节点下界、导数管道和多边形整数绕数三包。 | XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000 AND XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12 AND XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768 |

## 4. 下一步

优先攻：`XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000`。
随后攻：`XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12`。
最后聚合：`XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768`。

判定：最后剩余已经从 winding 泛命题压成三个有限 trace 子证书。
