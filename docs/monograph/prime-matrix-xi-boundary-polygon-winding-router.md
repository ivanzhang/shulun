# Prime Matrix xi 边界离散多边形绕数路由器

**状态：** `xi_boundary_trace_polygon_winding_zero_closed_winding_aggregation_next`

离散多边形绕数整数账本已闭合：底边角变化为 0，左右竖边由函数方程/共轭对称配平，顶边关于 sigma=1/2 对称并经过正实中心点，故四边角变化强制为 0。复放审计得到 winding=8.993360488158e-16，root=37be1e9977e0047951702c2bb8ec0e13183d5386f8fc6db7f7c1765b2bdb4330。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
polygon_winding_zero_closed=true
winding_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 绕数摘要

| item | value |
| --- | ---: |
| node count | `32769` |
| edge count | `32768` |
| polygon trace root hash | `941a77e7541d73eedebe9068dcd173dc9aaa63765879bf0612ea50f2a58dd64b` |
| polygon symmetry root hash | `7418be9e06c98be923637c5253795b08e7270495b3573d2d6eaee5d23bc073f2` |
| polygon winding root hash | `37be1e9977e0047951702c2bb8ec0e13183d5386f8fc6db7f7c1765b2bdb4330` |
| winding float | `8.993360488158e-16` |
| winding rounded | `0` |
| total angle | `5.650695048136e-15` |
| max step angle | `0.002927157640` |
| branch angle ceiling | `1.024572482473` |
| branch margin | `149/6144000` |

## 2. 四边角变化

| side | angle | winding share |
| --- | ---: | ---: |
| bottom | `-1.224646799147e-16` | `-1.949085916260e-17` |
| right | `2.332498124695e+00` | `3.712286062978e-01` |
| top | `-4.664996249390e+00` | `-7.424572125956e-01` |
| left | `2.332498124695e+00` | `3.712286062978e-01` |

## 3. 对称残差审计

| item | value |
| --- | ---: |
| top symmetry residual | `5.391871155989e-16` |
| vertical symmetry residual | `6.011900484457e-12` |
| bottom max abs imag | `6.412235645774e-17` |
| bottom min real | `4.971207781883e-01` |
| top center re | `2.012944442353e-04` |
| top center im | `7.142181811248e-18` |
| max balance residual | `7.904787935331e-14` |

## 4. 证明合同

1. 沿同一 32768 段 dyadic 边界取 xi 节点值，使用节点下界 root 和导数管道 root 保证短角分支唯一。
2. 由 |xi|>=1/6000 与 |xi'|<=1/12，最大段长 14/8192 给出段内位移 <=(1/12)(14/8192)<1/6000。
3. 因此每条边段不会穿过 0，每个相邻节点的主支短角增量是同伦稳定的。
4. 底边在实轴上且 xi 为正实值，所以底边角变化为 0。
5. 左右竖边由 xi(s)=xi(1-s) 和 xi(conj s)=conj xi(s) 配对，左边角变化等于右边角变化。
6. 顶边关于 sigma=1/2 共轭对称，且中心点 xi(1/2+14i)>0，因此顶边角变化等于右边角变化的 -2 倍。
7. 四边相加得到 Delta_bottom+Delta_right+Delta_top+Delta_left=0，故离散多边形绕数整数为 0。

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PolygonWindingGateActive` | `true` | `true` | 导数管道闭合后，当前唯一最窄点是离散多边形绕数整数账本。 | XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只物化假设链条中的边界绕数 trace，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `NodeLowerBoundImported` | `true` | `true` | 节点 \|xi\|>=1/6000 已闭合，提供短角分支的原点距离下界。 | XiBoundaryTraceNodeLowerBoundClosedMesh32768Floor1Over6000RootHash |
| `DerivativeTubeImported` | `true` | `true` | 边段 \|xi'\|<=1/12 已闭合，提供段内位移上界。 | XiBoundaryTraceSegmentDerivativeTubeClosedMesh32768C1Over12RootHash |
| `BranchSafetyArithmeticClosed` | `true` | `true` | 有理余量 1/6000-(1/12)*(14/8192)>0，短角上界 1.024572482473<pi/2。 | short-argument branch fixed. |
| `BoundaryNonzeroImported` | `true` | `true` | 整个 xi 边界非零已闭合，多边形同伦到真实边界曲线时不穿 0。 | XiBoundaryIntervalNonzeroCertificate0To14Closed |
| `XiSymmetryAnglePairingClosed` | `true` | `true` | 函数方程/共轭对称给出角变化配平：bottom=0, left=right, top=-2*right。 | Delta_total=0. |
| `XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768` | `true` | `true` | 离散多边形绕数整数账本已闭合；绕数为 0。 | XiBoundaryTracePolygonWindingZeroClosedMesh32768SymmetryRootHash |
| `WindingAggregationStillMissing` | `false` | `false` | 仍需把节点下界、导数管道和多边形绕数三包聚合回 winding 原子。 | XiBoundaryWindingNumberZeroIntervalCertificate0To14 |

## 6. 下一步

当前最窄点更新为：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：多边形绕数包关闭，剩余是把三包聚合回 winding 原子。
