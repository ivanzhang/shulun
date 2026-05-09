# Prime Matrix 经典 Backlund 缩进内部证明脊柱路由器

**状态：** `backlund_classical_indent_spine_reduced_to_sign_change_absorption_open`

经典 Backlund 内部化的正确脊柱不是证明近零 jump 消失，而是把水平 trace 的 arg 净变化/振幅改写为实部 sign-change 计数；缩进弧在避零极限中按解析重数登记为同一类事件。本步自足关闭了 sign-change 净变化引理和局部缩进登记引理，排除了逐零点额外付费的重复扣费。严格自足的新唯一剩余是证明该 sign-change 登记表精确注入既有 Jensen C16 局部计数，不遗漏端点、重零、贴线极限，也不调用外部 Backlund 引理。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
parent_internal_target=ClassicalBacklundZeroIndentationCostInternalProofLedger
previous_unique_remaining=BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger
new_unique_internal_remaining=BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger
sign_change_lemma_closed=true
indent_arc_registry_closed=true
row_column_self_contained_closed=false
row_column_external_route_closed=false
```

## 1. 本步闭合的经典局部引理

| lemma | statement | proof note |
| --- | --- | --- |
| `BacklundRealTraceVariationBySignChangesClosed` | 若连续可微曲线 f(x) 在区间上不为 0，且 arg 分支从右端固定，则 arg f 的净变化/振幅可由 Re(e^{-i theta} f(x)) 的零点/sign-change 次数控制。 | 在两个相邻实部零点之间，曲线留在同一开半平面，arg 净摆幅小于 pi；逐段相加。 |
| `BacklundIndentArcLimitRegisteredAsSignChangeZerosClosed` | 当路径命中解析零点 rho 时，先以小半圆避开再取极限；局部模型 f(s)=(s-rho)^m g(s) 把缩进弧 jump 精确登记为 m 个 sign-change/重数事件。 | g(rho) 非零只给连续相位；全部离散跳变来自 (s-rho)^m，按解析重数登记。 |

## 2. 预算压力

| item | value |
| --- | ---: |
| Jensen count coefficient | `16.000000000000` |
| per jump cost | `3.141592653590` |
| naive jump coefficient | `50.265482457437` |
| available stability margin | `0.078125000000` |
| deficit if double counted | `50.187357457437` |

解释：若把 sign-change/Jensen 已计入的近零事件再逐零点额外付 `pi`，会产生约 `50.187357` 的系数缺口。因此经典 Backlund 内部化必须证明“同一登记表吸收”，而不是添加一个新的缩进成本项。

## 3. 新的精确剩余

```text
BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger
  =>
(BacklundRealTraceVariationBySignChangesClosed AND BacklundIndentArcLimitRegisteredAsSignChangeZerosClosed AND BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger)
```

其中前两项本步关闭，唯一未闭合项是 `BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger`。

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只重排假设链条里的解析缩进成本，不使用真实零行缺席。 | 保持自足与外部链条分离。 |
| `ParentInternalTargetStillLocked` | `true` | `true` | 内部主攻仍是经典 Backlund 缩进成本内部证明。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| `PreviousZeroCoefficientAtomActive` | `true` | `true` | 上一层把内部硬点写成未配对 jump 的 log(T) 零系数。 | BacklundBudgetPreservingJumpAccountingZeroCoefficientLedger |
| `ClassicalBacklundSignChangeLemmaClosed` | `true` | `true` | 经典 Backlund 的实变量骨架可自足证明：arg 净变化/振幅由实部 sign-change 数控制。 | BacklundRealTraceVariationBySignChangesClosed |
| `IndentArcLimitRegisteredAsSignChangeZeros` | `true` | `true` | 局部缩进弧的 jump 不是额外对象；在避零极限中按解析重数登记为同一 sign-change/零点事件。 | BacklundIndentArcLimitRegisteredAsSignChangeZerosClosed |
| `LittlewoodRectangleIdentityAvailable` | `true` | `true` | Littlewood 矩形恒等式已可登记零点横向权重和边界积分。 | BacklundLittlewoodRectangleArgumentClosed |
| `ExternalJensenC16AvailableForAbsorptionTest` | `true` | `false` | 外部低高度输入下 Jensen C16 计数可作为对接参照；严格自足低高度仍未全部闭合。 | BacklundIndependentJensenZeroCountC16AggregationExternalClosed |
| `SeparateIndentChargeWouldDoubleCount` | `true` | `true` | 若 sign-change 零点已进入 Jensen C16 计数，再额外逐零点付 pi 缩进成本就是重复扣费。 | NoDoubleCounting discipline |
| `SignChangeToJensenAbsorptionExactness` | `false` | `false` | 仍需证明 sign-change 登记表逐项注入既有 Jensen C16 局部计数，且不遗漏端点、重零和贴线极限。 | BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger |
| `CS8ReaggregationAfterAbsorption` | `true` | `true` | 若上面的无重复吸收对接闭合，则 C_boundary=16 与桥因子 1/2 的 C_S=8 验收不再新增成本。 | BacklundCS8SlackAfterBridgeClosedTightHalf |
| `EndpointMultiplicityCompatible` | `true` | `true` | 端点落零先避开再取极限，正好提供 sign-change 登记的重数 convention。 | EndpointZeroAvoidanceMultiplicityConventionClosedByLimit |
| `InternalClassicalBacklundIndentClosed` | `false` | `false` | 经典脊柱已建立，但 sign-change 到 Jensen C16 的精确无重复对接仍未闭合。 | BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger |
| `ExternalBacklundEscapeStillAvailable` | `true` | `false` | 接受外部经典 Backlund 缩进引理可绕过该内部对接证明。 | ClassicalBacklundZeroIndentationCostExternalAccepted |
| `RowColumnExternalRouteStillNeedsDStructure` | `false` | `false` | 外部 Backlund 包接上后，最终仍需 DStructure/Rankin 独立验收。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步

内部唯一最窄点：`BacklundRealPartSignChangeJensenAbsorptionNoDoubleCountLedger`。
外部逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。
外部路线最终仍需：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。

判定：经典 Backlund 内部证明已缩成“sign-change 登记表无重复注入 Jensen C16”的精确对接命题；尚未严格自足闭合。
