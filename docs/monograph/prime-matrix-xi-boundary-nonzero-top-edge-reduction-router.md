# Prime Matrix xi 边界非零顶边压缩路由器

**状态：** `boundary_nonzero_reduced_to_top_edge_box_cover_external_closed`

边界非零的自足路线已压缩到唯一顶边账本：右边、左边和底边有结构性非零证明；真正剩余是给 Im(s)=14 顶边的有限 xi 区间盒覆盖。若接受外部首零点/Turing 完备性证书，边界非零和 winding=0 可条件闭合，但严格自足版仍未闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
boundary_nonzero_three_sides_structurally_closed=true
boundary_nonzero_self_contained_closed=false
boundary_nonzero_external_closed=true
winding_external_closed=true
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 四边分解

| side | status | reason |
| --- | --- | --- |
| `right_edge_sigma_2` | `closed` | Re(s)=2>1，Euler product 给 zeta(s) 非零；xi 的显式因子在 2+it 上非零。 |
| `left_edge_sigma_minus_1` | `closed` | 函数方程 xi(s)=xi(1-s) 把 -1+it 映到 2-it，继承右边界非零。 |
| `bottom_edge_t_0` | `closed` | 实轴 [-1,2] 上 zeta 的实值符号、Gamma 极点抵消和 xi 的 s(s-1) 因子给 xi(s) 非零；s=0,1 为可去点且 xi 值非零。 |
| `top_edge_t_14` | `open_self_contained` | 顶边穿过临界带最高处；自足路线必须给 sigma in [-1,2] 的有限区间盒并逐盒证明 0 不在 xi 盒内。 |

## 2. 顶边盒证书合同

| field | meaning |
| --- | --- |
| `box_id` | 按 sigma 区间稳定排序的 dyadic 编号。 |
| `sigma_interval` | 顶边上的 dyadic 闭区间 [a/2^k,b/2^k]，全部覆盖 [-1,2]。 |
| `xi_rect_interval` | 用已闭合 xi 区间求值引擎输出的复矩形盒。 |
| `nonzero_witness` | 证明 0 不在复盒内：例如 Re 盒离 0、Im 盒离 0，或盒到原点距离下界为正。 |
| `parent_trace_hash` | 引用每盒求值 trace root，保证可复放。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BoundaryNonzeroGateActive` | `true` | `true` | 求值引擎闭合后，当前最窄点是 xi 低高度矩形边界非零证书。 | XiBoundaryIntervalNonzeroCertificate0To14 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步处理低高度解析证书，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `SelfContainedXiIntervalEngineAvailable` | `true` | `true` | theta-Mellin 区间求值引擎已经闭合，可生成顶边有限区间盒。 | SelfContainedXiIntervalEvaluationEngine0To14 |
| `RightLeftBottomEdgesClosedStructurally` | `true` | `true` | 右边界由 Euler product，左边界由函数方程，底边由实轴非零和可去点值关闭。 | only top edge remains. |
| `TopEdgeBoxCoverStillMissing` | `false` | `false` | 自足路线还必须实际给出 Im(s)=14, -1<=Re(s)<=2 的有限区间盒覆盖并逐盒排除 0。 | TopEdgeXiIntervalBoxCoverLedgerT14SigmaMinus1To2 |
| `ExternalNoZeroBelow14ClosesBoundary` | `true` | `false` | 若接受外部首零点/Turing 完备性证书，矩形内无零点，边界非零与 winding=0 同时成立。 | XiBoundaryIntervalNonzeroCertificate0To14 AND XiBoundaryWindingNumberZeroIntervalCertificate0To14 |
| `XiBoundaryIntervalNonzeroCertificate0To14` | `false` | `false` | 严格自足边界非零尚未闭合；已压缩为唯一顶边盒覆盖账本。 | TopEdgeXiIntervalBoxCoverLedgerT14SigmaMinus1To2 |

## 4. 下一步

严格自足最窄点：`TopEdgeXiIntervalBoxCoverLedgerT14SigmaMinus1To2`。
随后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：外部路线可条件闭合；严格自足路线现在只差顶边有限盒证书。
