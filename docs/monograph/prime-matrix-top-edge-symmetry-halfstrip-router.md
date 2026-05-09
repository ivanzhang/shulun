# Prime Matrix 顶边临界半段压缩路由器

**状态：** `top_edge_reduced_to_critical_half_segment_external_still_closed`

顶边全段盒覆盖已进一步压缩：左半由函数方程和共轭对称转移，右外段由 Euler product 关闭。严格自足唯一剩余变成 Im(s)=14, 1/2<=Re(s)<=1 的临界半段盒证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
top_edge_full_segment_compressed=true
top_edge_self_contained_closed=false
top_edge_external_closed=true
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 顶边分段

| segment | status | reason |
| --- | --- | --- |
| `sigma in [-1,1/2]` | `reduced_by_functional_and_conjugate_symmetry` | xi(s)=xi(1-s) 且 xi(conj s)=conj xi(s)，非零性转移到 sigma in [1/2,2] 的同一高度。 |
| `sigma in (1,2]` | `closed_by_euler_product` | Re(s)>1 时 zeta(s) 的 Euler product 非零，xi 显式因子也非零。 |
| `sigma in [1/2,1]` | `open_self_contained` | 这是顶边穿过临界带的唯一剩余半段，需要有限区间盒逐段证明 0 不在 xi 盒内。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TopEdgeGateActive` | `true` | `true` | 上一层已把严格自足边界非零压缩到顶边盒覆盖。 | TopEdgeXiIntervalBoxCoverLedgerT14SigmaMinus1To2 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只用 xi 的函数方程、共轭对称和 Euler product，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `LeftHalfTopEdgeReducedBySymmetry` | `true` | `true` | 顶边 sigma<=1/2 由 xi(s)=xi(1-s) 与共轭对称转移到 sigma>=1/2。 | no separate boxes on [-1,1/2]. |
| `RightOuterTopEdgeClosedByEulerProduct` | `true` | `true` | 顶边 sigma>1 处 Re(s)>1，zeta Euler product 排除零点。 | no boxes needed on (1,2]. |
| `CriticalHalfSegmentStillMissing` | `false` | `false` | 严格自足路线只剩顶边临界半段 1/2<=sigma<=1 的有限区间盒覆盖。 | TopCriticalSegmentXiBoxCoverLedgerT14SigmaHalfToOne |
| `ExternalRouteAlreadyClosesTopEdge` | `true` | `false` | 若接受外部低高度无零点证书，顶边全段和 winding 已条件闭合。 | TopEdgeXiIntervalBoxCoverLedgerT14SigmaMinus1To2 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14 |
| `TopEdgeXiIntervalBoxCoverLedgerT14SigmaMinus1To2` | `false` | `false` | 旧顶边全段账本已被压缩，但严格自足闭合还需临界半段盒证书。 | TopCriticalSegmentXiBoxCoverLedgerT14SigmaHalfToOne |

## 3. 下一步

严格自足唯一剩余：`TopCriticalSegmentXiBoxCoverLedgerT14SigmaHalfToOne`。
随后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：现在不再需要全顶边盒，只需要临界半段盒。
