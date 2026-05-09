# Prime Matrix Backlund 临界线小半径 anchor 终端路由器

**状态：** `backlund_critical_line_scale_anchor_terminal_equivalent_to_indent_open`

临界线小半径 anchor 路线终端归并。固定临界线圆心没有统一非零下界；移动圆心避零会重新产生 Stieltjes 跳变/缩进成本；平均选点又需要先证明胶囊零点密度。因此该路线没有新自由度，最终回到 `ClassicalBacklundZeroIndentationCostInternalProofLedger`，也就是旧的 `BacklundZeroProximityIndentationCostLedger`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
critical_line_anchor_terminal_equivalence_closed=true
critical_line_anchor_self_contained_closed=false
strict_self_contained_unique_remaining=ClassicalBacklundZeroIndentationCostInternalProofLedger
row_column_self_contained_closed=false
```

## 1. 终端分叉

| route | verdict | reason |
| --- | --- | --- |
| `fixed_critical_center` | `blocked` | 固定靠近临界线的圆心无法给出统一非零下界；圆心可与零点或零点簇任意接近。 |
| `moving_center_avoidance` | `loops_to_indent_cost` | 移动圆心避零必须记录穿越、绕行和跳变；这正是 Backlund 近零缩进成本。 |
| `cartan_average_center` | `requires_capsule_density_first` | 平均/Cartan 选点需要先控制例外小圆盘总量；该控制就是胶囊零点密度。 |
| `external_backlund_indent` | `external_escape` | 接受经典 Backlund 缩进引理可直接关闭该终端缺口。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CriticalLineScaleAnchorGateActive` | `true` | `true` | 右边界 anchor 半径障碍后，唯一剩余变成临界线附近小半径 anchor。 | BacklundCriticalLineScaleAnchorAvoidanceLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条内的解析 anchor，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `FixedCriticalAnchorBlocked` | `true` | `true` | 靠近临界线的固定圆心没有 Euler product 下界；若圆心碰零或贴近零点，下界失效。 | BacklundMovingCenterZeroAvoidanceWithoutCostLedger |
| `EndpointLimitDoesNotPayAnchor` | `true` | `true` | 端点极限 convention 只定义重数和极限，不给临界线圆心非零下界。 | BacklundMovingCenterZeroAvoidanceWithoutCostLedger |
| `MovingCenterLoopsToStieltjesIndent` | `true` | `true` | 移动圆心避零产生的穿越/跳变账本已经终端等价于缩进成本。 | BacklundZeroProximityIndentationCostLedger |
| `CartanAverageRequiresDensity` | `true` | `true` | 用平均或 Cartan 选好圆心，需要先知道零点例外集密度；这正是父级胶囊密度目标。 | BacklundIndependentCapsuleZeroDensityCoefficientLedger |
| `TerminalEquivalenceImported` | `true` | `true` | 仓库已登记经典内部证明义务等价于旧 Backlund 近零凹口成本。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| `BacklundCriticalLineScaleAnchorAvoidanceLedger` | `false` | `false` | 临界线小半径 anchor 没有产生新自由度，终端回到缩进成本内部证明或外部引理。 | ClassicalBacklundZeroIndentationCostInternalProofLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted |

## 3. 下一步

严格自足唯一剩余回到：`ClassicalBacklundZeroIndentationCostInternalProofLedger`。
等价旧剩余：`BacklundZeroProximityIndentationCostLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：临界线小半径 anchor 不是新闭合路线；它终端等价于 Backlund 缩进成本。
