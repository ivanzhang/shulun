# Prime Matrix 顶边临界段端点链聚合路由器

**状态：** `boundary_nonzero_self_contained_closed_winding_next`

顶边临界半段已由端点单调/Taylor 链闭合，进而顶边全段闭合；结合右、左、底三边结构非零，XiBoundaryIntervalNonzeroCertificate0To14 已自足闭合。当前严格自足路线的唯一剩余更新为 XiBoundaryWindingNumberZeroIntervalCertificate0To14，即边界绕数/低高度零点计数证书。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
top_critical_segment_self_contained_closed=true
top_edge_self_contained_closed=true
boundary_nonzero_self_contained_closed=true
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 闭合链

| step | input | output |
| --- | --- | --- |
| EndpointPackage | 端点 EM replay 包 | 0、1、2 阶端点不等式，3-10 阶符号梯，11-13 阶例外界全部闭合 |
| ThirdPositive | 端点符号梯 + 例外界 + 14 阶包络 | 全段 Im zeta'''(sigma+14i)>=1/8 |
| SecondNegative | 端点二阶负号 + 全段三阶正号 | 全段 Im zeta''(sigma+14i)<=-1/8 |
| DerivativePositive | 端点一阶正号 + 全段二阶负号 | 全段 Im zeta'(sigma+14i)>=1/16 |
| ImaginaryNegative | 端点虚部负号 + 全段一阶正号 | 全段 Im zeta(sigma+14i)<=-1/40<0 |
| TopCriticalNonzero | 临界半段 zeta 虚部严格负 | xi 在顶边临界半段非零 |
| TopEdgeAndBoundary | 顶边对称压缩 + 右外段 Euler product + 三边结构非零 | XiBoundaryIntervalNonzeroCertificate0To14 闭合 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 聚合只使用假设链条中的解析证书，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `EndpointReplayPackageClosed` | `true` | `true` | 端点虚部、一阶、二阶、3-10 阶符号梯和 11-13 阶例外界全部闭合。 | endpoint atoms closed. |
| `ThirdDerivativePositiveClosed` | `true` | `true` | 端点 Taylor 符号梯与 14 阶包络推出全段三阶导数正号。 | TopCriticalImagThirdDerivativePositiveLedgerT14HalfToOneFloor1Over8Closed |
| `SecondDerivativeNegativeClosed` | `true` | `true` | 端点二阶负号加全段三阶正号推出全段二阶负号。 | TopCriticalImagSecondDerivativeNegativeLedgerT14HalfToOneFloorMinus1Over8Closed |
| `DerivativePositiveClosed` | `true` | `true` | 端点一阶正号加全段二阶负号推出全段一阶正号。 | TopCriticalImagDerivativePositiveLedgerT14HalfToOneFloor1Over16Closed |
| `MonotoneEndpointImagNegativeClosed` | `true` | `true` | 端点虚部负号加全段一阶正号推出临界半段虚部严格负。 | TopCriticalSegmentXiNonzeroClosedByMonotoneEndpointT14HalfToOne |
| `TopCriticalSegmentXiBoxCoverLedgerT14SigmaHalfToOne` | `true` | `true` | 顶边临界半段 1/2<=sigma<=1 已由单调端点链闭合，无需 1024 中心表。 | TopCriticalSegmentXiNonzeroClosedByMonotoneEndpointT14HalfToOne |
| `TopEdgeXiIntervalBoxCoverLedgerT14SigmaMinus1To2` | `true` | `true` | 顶边左半由函数方程/共轭对称转移，右外段由 Euler product，临界半段已闭合。 | TopEdgeXiIntervalNonzeroClosedT14SigmaMinus1To2 |
| `XiBoundaryIntervalNonzeroCertificate0To14` | `true` | `true` | 右、左、底三边结构非零，加顶边闭合，得到整个低高度矩形边界非零。 | XiBoundaryIntervalNonzeroCertificate0To14Closed |
| `XiBoundaryWindingNumberZeroIntervalCertificate0To14` | `false` | `false` | 边界非零不自动给出绕数为 0；低高度零点计数仍需独立 winding/argument certificate。 | XiBoundaryWindingNumberZeroIntervalCertificate0To14 |

## 3. 下一步

严格自足唯一剩余：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：边界非零已经闭合；剩余是绕数/低高度零点计数，而不是顶边非零。
