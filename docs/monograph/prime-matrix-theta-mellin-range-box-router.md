# Prime Matrix theta-Mellin 紧致范围盒路由器

**状态：** `theta_mellin_compact_range_boxes_closed_tail_orders_open`

theta-Mellin 超越函数核的范围盒已可保守关闭：低高度矩形、主积分窗口、有限 theta 项窗口、log/power 参数和 Gaussian 指数参数都被有理区间包住。本步不证明 t>64 或 n>20 的尾项足够小，也不证明积分分段误差；这些仍由后续账本承担。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
range_box_closed=true
theta_mellin_transcendental_kernel_closed=false
row_column_self_contained_closed=false
```

## 1. 范围盒

| item | range |
| --- | --- |
| `s_rectangle_sigma` | `['-1', '2']` |
| `s_rectangle_tau` | `['0', '14']` |
| `theta_mellin_t_window` | `['1', '64']` |
| `theta_finite_n_window` | `[1, 20]` |
| `log_t_range_safe` | `['0', '6']` |
| `z_plus_re_range` | `['-3/2', '0']` |
| `z_minus_re_range` | `['-3/2', '0']` |
| `z_im_abs_bound` | `7` |
| `re_z_log_t_abs_bound` | `9` |
| `im_z_log_t_abs_bound` | `42` |
| `gaussian_pi_n2_t_range_safe` | `['3', '102400']` |
| `pi_safe_range` | `['3', '4']` |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `RangeBoxGateActive` | `true` | `true` | 上一层已把超越函数核的唯一活动缺口压成紧致范围盒。 | ThetaMellinCompactRangeBoxLedger0To14 |
| `TranscendentalTemplatesAvailable` | `true` | `true` | log/trig/exp/complex power/Gaussian exp 的 Taylor 模板已闭合。 | 只需给它们有限参数盒。 |
| `LowHeightRectangleBoxFixed` | `true` | `true` | 取保守矩形 -1<=Re s<=2, 0<=Im s<=14，覆盖低高度非平凡零点计数区域。 | sigma in [-1,2], tau in [0,14] |
| `ThetaMellinTAndNWindowsFixed` | `true` | `true` | 固定积分主窗口 1<=t<=64 和有限 theta 项 1<=n<=20；这里只登记范围，不证明尾项足够小。 | tail adequacy remains in GaussianThetaTailBoundLedger |
| `LogAndPowerArgumentBoxesClosed` | `true` | `true` | 由 log t<=6 和 \|Im z\|<=7 得 \|Im z log t\|<=42，\|Re z log t\|<=9。 | ThetaMellinCompactRangeBoxClosed0To14T64N20 |
| `GaussianExponentBoxClosed` | `true` | `true` | 用 3<pi<4 得 pi n^2 t 落在 [3,102400]，足以供负指数 range reduction。 | ThetaMellinCompactRangeBoxClosed0To14T64N20 |
| `TailAndQuadratureStillDownstream` | `false` | `false` | 范围盒不证明截断误差、积分分段误差或操作轨迹。 | ThetaMellinTaylorTailOrderLedger0To14 AND IntervalOperationTraceHashLedger AND GaussianThetaTailBoundLedger AND CompactThetaMellinQuadratureSubdivisionLedger0To14 |

## 3. 下一步

当前最窄点：`ThetaMellinTaylorTailOrderLedger0To14`。
并行审计点：`IntervalOperationTraceHashLedger`。
后续仍需 `GaussianThetaTailBoundLedger AND CompactThetaMellinQuadratureSubdivisionLedger0To14`。

判定：范围盒已闭合，剩余变成 Taylor 尾阶表、调用轨迹、Gaussian 尾项和积分分段。
