# Prime Matrix 顶边临界半段水平导数上界路由器

**状态：** `top_critical_derivative_bound_closed_center_values_next`

顶边临界半段的水平导数合同已闭合：Euler-Maclaurin 逐项导数上界约 21.9574，远小于 64。于是剩余不再包含传播控制，只剩 1024 个中心值的有理区间 replay 表。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
top_critical_derivative_bound_closed=true
top_critical_segment_self_contained_closed=false
lowheight_rectangle_count_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 导数界分解

| component | bound |
| --- | ---: |
| finite sum | `20.198886835613` |
| pole tail | `1.429230277657` |
| endpoint half | `0.306330669834` |
| Bernoulli corrections | `0.022933497160` |
| remainder budget | `1.000000000000e-06` |
| total | `21.957382280264` |
| contract | `64.000000000000` |
| actual half-cell loss | `0.005360689033` |
| margin if centers pass | `0.094639310967` |

## 2. 证明链

1. 在 1/2<=sigma<=1, t=14 上，对 Euler-Maclaurin 公式逐项求 s 导数；水平导数就是 d/ds。
2. 有限和部分由 sum_{n<32} log(n)n^{-sigma} <= sum log(n)/sqrt(n) 控制。
3. N^(1-s)/(s-1) 的导数用 |s-1|>=14 与 N^(1-sigma)<=sqrt(N) 控制。
4. 1/2*N^{-s} 的导数用 (1/2)log(N)/sqrt(N) 控制。
5. Bernoulli 修正项 c_k (s)_{2k-1} N^{-s-2k+1} 的导数由 product bound 乘以 sum reciprocal plus log(N) 控制。
6. Euler-Maclaurin 余项导数给 1e-6 冗余预算；总上界约 21.9574，小于合同 64。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DerivativeBoundGateActive` | `true` | `true` | 上一层把顶边临界段压成中心值加导数传播的 Euler-Maclaurin replay。 | TopCriticalSegmentEulerMaclaurinDyadicReplayLedgerN32P8Mesh2048 |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只证明解析上界，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `EulerMaclaurinDerivativeFormulaBounded` | `true` | `true` | 逐项绝对值上界给 \|zeta'\|<=21.957382280264<64。 | TopCriticalSegmentHorizontalDerivativeBoundClosed64 |
| `PropagationMarginImproved` | `true` | `true` | 若中心值 >=0.1，实际导数上界带来的半段损失约 0.005360689033，剩余 0.094639310967。 | center values remain. |
| `CenterValueReplayStillMissing` | `false` | `false` | 还需 1024 个中心点的有理区间 Euler-Maclaurin 值证明 \|zeta\|>=0.1。 | TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1 AND DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger |
| `TopCriticalSegmentEulerMaclaurinDyadicReplayLedgerN32P8Mesh2048` | `false` | `false` | 原 replay 账本已关闭导数半边，剩余是中心值 replay 表。 | TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1 |

## 4. 下一步

严格自足最窄点：`TopCriticalSegmentCenterValueEMReplayLedgerN32P8Mesh2048Floor0p1`。
并行实现门：`DyadicComplexIntervalEulerMaclaurinReplayRoundingLedger`。
之后仍需：`XiBoundaryWindingNumberZeroIntervalCertificate0To14`。

判定：导数传播已闭合，中心值 replay 表成为唯一顶边数值剩余。
