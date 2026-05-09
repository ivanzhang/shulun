# Prime Matrix Backlund xi 对称 formal unit 轮廓路由器

**状态：** `backlund_xi_formal_unit_reduced_to_budget_preserving_doubling_open`

`BacklundXiSymmetricFormalUnitContourLedger` 不能直接由低高度 xi winding 证书推出。本步把它收缩为一个更窄的预算保持 doubling 问题：必须把原始 Backlund 移动凹口 trace 和 xi 镜像 trace 放入同一 formal unit，并证明镜像弧反向、回投无损且无重复计费。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
formal_unit_reduction_closed=true
xi_symmetric_formal_unit_closed=false
signed_pairing_involution_closed=false
backlund_local_crossing_trace_closed=false
row_column_self_contained_closed=false
```

## 1. 自足替换

```text
BacklundXiSymmetricFormalUnitContourLedger
  =>
(BacklundBudgetPreservingXiSymmetricContourDoublingLedger AND BacklundMirrorIndentArcOrientationLedger AND BacklundOriginalTraceProjectionNoLossLedger)
```

| atom | role |
| --- | --- |
| `BacklundBudgetPreservingXiSymmetricContourDoublingLedger` | 把原始 Backlund 移动凹口 trace 与 xi 镜像 trace 合成同一 formal unit，且不改变目标预算。 |
| `BacklundMirrorIndentArcOrientationLedger` | 证明镜像凹口弧的方向与 branch_jump 符号正好相反。 |
| `BacklundOriginalTraceProjectionNoLossLedger` | 从对称 doubled unit 投影回原始 Backlund trace 时不丢失、不重复计算成本。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `XiFormalUnitGateActive` | `true` | `true` | zeta-xi 跳变搬运闭合后，剩余是把移动凹口注册成 xi 对称 formal unit。 | BacklundXiSymmetricFormalUnitContourLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条中的 contour/homotopy 账本，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `BacklundRectangleIdentityAvailable` | `true` | `true` | Littlewood 矩形恒等式已闭合，说明原始 Backlund trace 可以按边界和零点权重精确记账。 | 无矩形恒等式剩余。 |
| `LeftRightFunctionalEquationBridgeAvailable` | `true` | `true` | 左边界可经函数方程回到右边界，这提供 formal unit 对称化的解析桥。 | 无左边界函数方程剩余。 |
| `LowHeightXiSymmetricUnitModelAvailable` | `true` | `true` | 低高度 xi 多边形给出成功的对称 formal unit 模型，但不自动覆盖移动凹口。 | 只能作为模型输入。 |
| `MovingIndentDirectSymmetryNotRegistered` | `true` | `true` | 现有账本尚未证明原始移动凹口和其 xi 镜像属于同一预算单位。 | BacklundBudgetPreservingXiSymmetricContourDoublingLedger |
| `FormalUnitReducedToBudgetPreservingDoubling` | `true` | `false` | formal unit 硬点已压成预算保持的 xi 对称 doubling、镜像弧方向、原 trace 投影三包。 | BacklundBudgetPreservingXiSymmetricContourDoublingLedger AND BacklundMirrorIndentArcOrientationLedger AND BacklundOriginalTraceProjectionNoLossLedger |
| `BacklundBudgetPreservingXiSymmetricContourDoublingLedger` | `false` | `false` | 尚未构造预算保持的 doubled contour/homotopy 账本。 | BacklundBudgetPreservingXiSymmetricContourDoublingLedger |
| `BacklundMirrorIndentArcOrientationLedger` | `false` | `false` | 尚未证明镜像凹口弧方向使 branch_jump 成反号配对。 | BacklundMirrorIndentArcOrientationLedger |
| `BacklundOriginalTraceProjectionNoLossLedger` | `false` | `false` | 尚未证明 doubled formal unit 回投到原始 trace 时不重复、不漏记。 | BacklundOriginalTraceProjectionNoLossLedger |
| `BacklundXiSymmetricFormalUnitContourLedger` | `false` | `false` | 三包闭合后才可把 xi 对称 formal unit 交给 mirror orbit hash 与 signed pairing。 | BacklundMirrorOrbitMultiplicityHashLedger AND BacklundSignedCrossingPairingInvolutionLedger |

## 3. 下一步

当前真正最窄点：`BacklundBudgetPreservingXiSymmetricContourDoublingLedger`。
方向验收：`BacklundMirrorIndentArcOrientationLedger`。
投影验收：`BacklundOriginalTraceProjectionNoLossLedger`。
mirror hash 支撑：`BacklundMirrorOrbitMultiplicityHashLedger`。
父级配对账本：`BacklundSignedCrossingPairingInvolutionLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：formal unit 已压到预算保持对称 doubling；命题尚未自足闭合。
