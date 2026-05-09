# Prime Matrix Backlund 凹口成本内部攻坚路由器

**状态：** `backlund_indent_internal_reduced_to_crossing_trace_open`

Backlund 凹口成本的内部二选一已压成一个更窄的统一原子：`BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger`。零避让只是该 trace 的空穿越特例；跳变抵消是非空穿越特例。当前仍未自足闭合，因为还缺每个近零窗口的零点盒、缩进弧、跳变量、抵消配对和残余成本 hash 账本。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
indent_or_package_compressed=true
backlund_local_crossing_trace_closed=false
backlund_indent_self_contained_closed=false
row_column_self_contained_closed=false
naive_indentation_coefficient=50.265482457437
available_stability_margin=0.078125000000
naive_margin_deficit=50.187357457437
```

## 1. 二选一压缩律

| old | new | reason |
| --- | --- | --- |
| `BacklundZeroAvoidingShiftWithoutJumpLedger` | `BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger` | 选择避让平移本身必须证明穿越零点集合为空；这正是 crossing trace 的空穿越特例。 |
| `BacklundNearZeroJumpCancellationSubHalfLedger` | `BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger` | 跳变抵消必须登记每个近零点的符号、重数和配对；这正是 crossing trace 的非空穿越特例。 |
| `BacklundZeroProximityIndentationCostLedger` | `BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger` | 凹口成本不能由零点数量粗付关闭，只能由局部同伦 trace 证明残余成本可预算。 |

## 2. crossing trace 字段

| field | meaning |
| --- | --- |
| `window_id` | Backlund 短窗口编号，与 h=1/512 的窗口尺度一致。 |
| `zero_cluster_box` | 近零点核心 \|s-rho\|<eta 的区间盒与 multiplicity 账本。 |
| `contour_side` | 零点相对移动 contour 的左右/上下侧，决定缩进方向。 |
| `homotopy_arc` | 局部缩进圆弧或避让平移的参数化区间。 |
| `branch_jump` | arg zeta 或 arg xi 的局部跳变量，带符号和重数。 |
| `paired_cancellation` | 若不避让，必须登记与相邻零点/边界/对称点的抵消配对。 |
| `residual_cost` | 抵消后仍需扣除的成本，必须小于全局稳定余量。 |
| `trace_hash` | 窗口、零点盒、缩进弧、跳变量和剩余成本的 canonical hash。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `IndentInternalAttackActive` | `true` | `true` | 低高度 xi 子包闭合后，当前严格自足解析最窄点正是凹口成本内部替代包。 | (BacklundZeroAvoidingShiftWithoutJumpLedger OR BacklundNearZeroJumpCancellationSubHalfLedger) |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条中的解析记账，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `LowHeightAnchorImported` | `true` | `true` | 0<t<=14 的低高度零点计数已闭合，可作为 Backlund/Jensen 低端 anchor。 | LowHeightXiRectangleZeroCountZero0To14SelfContainedClosed。 |
| `NearZeroPartitionImported` | `true` | `false` | eta=1/16 内近零点已从倒距离和切出，交给凹口成本账本。 | BacklundZeroProximityIndentationCostLedger |
| `EndpointMultiplicityConventionImported` | `true` | `true` | 端点碰零按重数与极限 convention 处理，但这不提供数量级预算。 | EndpointZeroAvoidanceMultiplicityConventionClosed。 |
| `SafeAnnuliAndWindowImported` | `true` | `false` | eta 外倒距离和与窗口尺度已有外部分支账本；内部缺口只剩 eta 内穿越 trace。 | BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger |
| `NaiveCostContradictionLocked` | `true` | `true` | 朴素逐零点凹口成本缺口为 50.187357457437，所以粗数量界路线被排除。 | BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger |
| `ShiftOrCancellationUnified` | `true` | `true` | 零避让是空穿越 trace；跳变抵消是非空穿越 trace。二选一可压成同一个局部同伦账本。 | BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger |
| `BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger` | `false` | `false` | 当前尚未给出每个近零窗口的零点盒、缩进弧、跳变量和残余成本 hash 账本。 | BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger |
| `BacklundIndentCostSelfContainedClosed` | `false` | `false` | 只有 crossing trace 证明残余成本小于稳定余量后，内部凹口成本才可关闭。 | BacklundLocalZeroCrossingTraceAndIndentHomotopyClosed |

## 4. 下一步

当前严格自足最窄点：`BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger`。
该 trace 完成后进入：`BacklundCS8SlackAfterBridgeLedger`。
并行保留晋级门：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。

判定：凹口成本从二选一缩成单原子 trace；尚未完成自足闭合。
