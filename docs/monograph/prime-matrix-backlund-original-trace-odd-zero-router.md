# Prime Matrix Backlund 原始 trace 奇部为零审查路由器

**状态：** `backlund_original_trace_odd_zero_rejected_indent_correction_next`

`BacklundOriginalTraceOddPartZeroLedger` 不能作为全局闭合目标。它等价于原始 Backlund trace 没有 crossing branch jump；但高高度零点、端点重数 convention、近零分离和 Jensen 计数都说明 jump 必须被记账而不是删除。因此内部路线必须回到 `BacklundOddMirrorCorrectionCostLedger`，也就是凹口成本的自足证明；若接受外部经典 Backlund 缩进引理，则可由外部路线继续闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
original_trace_odd_zero_rejected=true
original_trace_odd_zero_closed=false
half_average_identity_closed=false
backlund_local_crossing_trace_closed=false
row_column_self_contained_closed=false
```

## 1. 不可作为全局目标的原因

| reason | detail |
| --- | --- |
| `actual_zeros_exist` | zeta/xi 的非平凡零点存在；当高度命中零点 ordinates 时，原始 trace 的 branch jump 不能被宣布为 0。 |
| `endpoint_convention_is_not_absence` | 端点 convention 只规定避开后取极限并按重数计数，不证明 jump 消失。 |
| `near_zero_separation_is_assignment` | eta=1/16 近零分离只是把近零点交给凹口成本账本，不证明近零点集合为空。 |
| `jensen_count_allows_zeros` | Jensen C16 是数量上界，允许 O(log T) 个局部零点；它不支持奇部恒为 0。 |

## 2. 自足替换

```text
BacklundOriginalTraceOddPartZeroLedger
  =>
rejected_as_global_target; use (BacklundOddMirrorCorrectionCostLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted)
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `OriginalTraceOddZeroGateActive` | `true` | `true` | 半镜像平均障碍后，当前候选最窄点是证明原始 trace 奇部为 0。 | BacklundOriginalTraceOddPartZeroLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只审查假设链条中的解析输入，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `ZetaXiJumpTransportAvailable` | `true` | `true` | branch jump 已可无损搬运到 xi，因此奇部为零等价于原始 trace 没有 crossing jump。 | BacklundZeroAvoidingShiftWithoutJumpLedger |
| `LowHeightClosedButIrrelevantToHighTrace` | `true` | `true` | 0<t<=14 低高度已闭合，但 Backlund 高度 trace 的零点 crossing 仍可能存在。 | BacklundZeroProximityIndentationCostLedger |
| `NearZeroAssignedNotEliminated` | `true` | `true` | 近零分离把 eta 内零点交给凹口账本，不证明原始奇部为 0。 | BacklundZeroProximityIndentationCostLedger |
| `EndpointConventionCountsJumps` | `true` | `true` | 端点避零与重数 convention 处理落零极限，但按重数保留 jump，而不是删除 jump。 | BacklundZeroProximityIndentationCostLedger |
| `GlobalOddPartZeroRejected` | `true` | `true` | 原始奇部为零不能作为全局自足定理；它只有在额外零避让或缩进成本已处理后才成立。 | BacklundOddMirrorCorrectionCostLedger |
| `BacklundOriginalTraceOddPartZeroLedger` | `false` | `false` | 该目标与高高度零点 crossing 的真实解析结构不兼容，不能关闭父级半平均路线。 | BacklundZeroAvoidingShiftWithoutJumpLedger with cost control OR BacklundOddMirrorCorrectionCostLedger |
| `BacklundOddMirrorCorrectionCostLedger` | `false` | `false` | 剩余必须转为奇部修正成本，也就是 Backlund 凹口成本的自足证明或外部引理。 | BacklundZeroProximityIndentationCostLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted |

## 4. 下一步

当前真正最窄点：`BacklundOddMirrorCorrectionCostLedger`。
等价成本目标：`BacklundZeroProximityIndentationCostLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。
被阻断父级：`BacklundOriginalTraceHalfMirrorAverageIdentityLedger`。

判定：奇部为零路线被全局解析结构阻断；必须证明奇部修正成本或接受外部 Backlund 缩进引理。
