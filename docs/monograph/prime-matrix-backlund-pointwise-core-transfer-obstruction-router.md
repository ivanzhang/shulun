# Prime Matrix Backlund 点态近零核心转移障碍路由器

**状态：** `backlund_pointwise_core_transfer_blocked_by_support_mismatch_open`

点态近零核心不能由 Littlewood 矩形零点权重直接吸收。结构原因是支撑不匹配：矩形权重是横向的 beta-a，贴左边界时可任意小；而点态高度跳变在固定短窗口内仍保持正量。所以当前最窄点从普通权重转移改写为局部 Stieltjes 跳变/缩进账本；这仍未关闭严格自足路线，但排除了一个关键伪闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
pointwise_core_transfer_closed=false
support_mismatch_obstruction_closed=true
indent_cost_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 局部模型

```text
setup: zero rho=a+epsilon+iT, pointwise line sigma=a, window |u|<=H
H=0.001953125000
pointwise_jump=2*atan(H/epsilon)
littlewood_weight=2*pi*epsilon
needed_multiplier=atan(H/epsilon)/(pi*epsilon)
```

| epsilon | pointwise jump | Littlewood weight | needed multiplier |
| ---: | ---: | ---: | ---: |
| 0.062500000000 | 0.062479666861 | 0.392699081699 | 0.159103165177 |
| 0.015625000000 | 0.248709989094 | 0.098174770425 | 2.533339146276 |
| 0.003906250000 | 0.927295218002 | 0.024543692606 | 37.781406118511 |
| 0.000976562500 | 2.214297435588 | 0.006135923152 | 360.874375525956 |
| 0.000244140625 | 2.892882664496 | 0.001533980788 | 1885.866294638324 |

结论：`epsilon -> 0` 时，Littlewood 横向权重趋近 `0`，但点态跳变不随同趋近 `0`；
因此不存在独立于零点贴边界距离的固定容量乘子。

## 2. 障碍引理

| lemma | content |
| --- | --- |
| `HorizontalWeightVsVerticalJumpMismatch` | Littlewood 矩形零点项按横向权重 beta-a 计；点态近零核心按高度方向的 arg 跳变计。当 beta-a=epsilon 趋近 0 时，前者趋近 0，后者在固定窗口内可保持正量。 |
| `NoUniformCapacityMultiplier` | 若试图用 K * 2*pi*(beta-a) 支付点态跳变，则 K 至少随 1/epsilon 发散；因此 RegisteredCapacityMultiplierDiscipline 禁止直接转移。 |
| `BoundaryZeroSupportLowerBoundWouldBeTooStrong` | 除非额外证明所有近零核心满足 beta-a>=delta>0，否则权重吸收不能推出点态核心预算；这等于排除贴边界零点，不是当前输入基已有事实。 |
| `StieltjesJumpTransferIsTheRealAtom` | 剩余不能再是普通零点权重吸收，而必须是局部 Stieltjes 跳变/缩进引理：把边界贴近零点的点态跳变作为同一轮廓极限项登记，并证明不重复扣 Jensen/RVM 预算。 |

## 3. 自足替换

```text
BacklundPointwiseNearZeroCoreTransferLedger
  =>
BacklundBoundaryStieltjesJumpTransferLedger
```

| option | atom | status | reason |
| --- | --- | --- | --- |
| `support_lower_bound` | `BacklundBoundaryZeroSupportLowerBoundLedger` | `not_available` | 需要 beta-a>=delta 的统一左边界支撑下界；这会排除或强约束临界线/贴线零点。 |
| `local_stieltjes_jump_transfer` | `BacklundBoundaryStieltjesJumpTransferLedger` | `next_internal_atom` | 用局部轮廓同伦和 Stieltjes 跳变账本替代权重乘子，可能与经典 Backlund 缩进引理等价。 |
| `external_backlund_indent` | `ClassicalBacklundZeroIndentationCostExternalAccepted` | `external_escape` | 接受经典 Backlund 缩进处理即可关闭本分析缺口，但不是严格自足证明。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PointwiseCoreTransferGateActive` | `true` | `true` | 凹口成本内部化后的最窄点正是把矩形零点权重吸收转到点态近零核心。 | BacklundPointwiseNearZeroCoreTransferLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条中的解析障碍，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `LittlewoodRectangleWeightAvailable` | `true` | `true` | Littlewood 矩形层已有零点横向权重项。 | 仅可作为矩形平均层输入。 |
| `NearZeroCoreStillAssignedToIndent` | `true` | `true` | eta=1/16 内零点没有被倒距离和吸收，仍属于凹口/点态核心。 | BacklundZeroProximityIndentationCostLedger |
| `EndpointLimitConventionAvailable` | `true` | `true` | 端点落零可由极限 convention 定义，但该 convention 不提供点态预算。 | BacklundBoundaryStieltjesJumpTransferLedger |
| `BacklundPointwiseCoreSupportMismatchLemmaClosed` | `true` | `true` | 横向权重 beta-a 可趋近 0，而点态高度跳变在同一固定窗口内仍为正量。 | BacklundBoundaryStieltjesJumpTransferLedger |
| `DirectLittlewoodToPointwiseMultiplierBlocked` | `true` | `true` | 任何固定容量乘子都无法把 2*pi*(beta-a) 统一转成点态近零跳变预算。 | BacklundBoundaryStieltjesJumpTransferLedger |
| `C8BudgetCannotAbsorbResidualMultiplier` | `true` | `true` | C_S=8 后续为紧等号，5/64 余量也只属于窗口稳定性；不能容纳发散乘子或正比例残差。 | BacklundC8BudgetPreservingIndentReaggregationLedger |
| `BacklundPointwiseNearZeroCoreTransferLedger` | `false` | `false` | 直接权重吸收转移已被结构性阻断；必须改证局部 Stieltjes 跳变/缩进账本。 | BacklundBoundaryStieltjesJumpTransferLedger AND BacklundZeroWeightNoDoubleCountingLedger AND BacklundC8BudgetPreservingIndentReaggregationLedger |

## 5. 下一步

当前真正最窄点：`BacklundBoundaryStieltjesJumpTransferLedger`。
支撑下界备选：`BacklundBoundaryZeroSupportLowerBoundLedger`，但该路线会要求贴边界零点支撑下界。
无重复扣费纪律：`BacklundZeroWeightNoDoubleCountingLedger`。
常数重聚合：`BacklundC8BudgetPreservingIndentReaggregationLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：直接 Littlewood 权重转移被结构性阻断；下一步只能攻局部 Stieltjes 跳变/缩进账本。
