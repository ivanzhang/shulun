# Prime Matrix Backlund 对称 doubling 容量纪律路由器

**状态：** `backlund_symmetric_doubling_reduced_to_zero_cost_projection_open`

预算保持 xi 对称 doubling 不能按普通双份轮廓付费。因为 Backlund C_S=8 已是紧等号，任何正的 doubling 乘子都会把 C_S 从 8 推到 16。所以当前最窄点被压成 `BacklundZeroCostMirrorProjectionIdentityLedger`：必须证明对称化是在恒等式层完成的零成本投影，并配套半权归一化与无重复扣费纪律。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
doubling_capacity_reduction_closed=true
budget_preserving_doubling_closed=false
xi_symmetric_formal_unit_closed=false
backlund_local_crossing_trace_closed=false
row_column_self_contained_closed=false
```

## 1. 容量纪律

| item | value |
| --- | ---: |
| `C_S_target` | `8.000000000000` |
| `C_S_result` | `8.000000000000` |
| `C_S_slack` | `0.000000000000` |
| `paid_doubling_multiplier` | `2.000000000000` |
| `paid_doubling_C_S_result` | `16.000000000000` |

结论：doubling 只能是恒等式级零成本投影，不能是付费复制轮廓。

## 2. 自足替换

```text
BacklundBudgetPreservingXiSymmetricContourDoublingLedger
  =>
(BacklundZeroCostMirrorProjectionIdentityLedger AND BacklundHalfWeightSymmetricTraceNormalizationLedger AND BacklundNoDoubleCountingMirrorBoundaryLedger)
```

| atom | role |
| --- | --- |
| `BacklundZeroCostMirrorProjectionIdentityLedger` | 证明 xi 对称 doubling 是恒等式级投影，不产生任何新增 log(T) 预算项。 |
| `BacklundHalfWeightSymmetricTraceNormalizationLedger` | 若使用 doubled trace，必须同步使用 1/2 归一化，使边界常数不从 16 变 32。 |
| `BacklundNoDoubleCountingMirrorBoundaryLedger` | 证明镜像边界、镜像凹口和原边界没有被重复扣费。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SymmetricDoublingCapacityGateActive` | `true` | `true` | formal unit 路由后，当前最窄点是预算保持的 xi 对称 doubling。 | BacklundBudgetPreservingXiSymmetricContourDoublingLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条中的容量纪律，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `CS8SlackIsTight` | `true` | `true` | Backlund C_S=8 余量是紧等号，slack=0；不能支付任何正的 doubling 乘子。 | BacklundZeroCostMirrorProjectionIdentityLedger |
| `TraceResidualMarginAlreadyTiny` | `true` | `true` | crossing trace 容量已证明凹口残余必须是零系数；不能让 doubled unit 新增正比例残留。 | BacklundZeroCostMirrorProjectionIdentityLedger |
| `PaidDoublingForbidden` | `true` | `true` | 如果 doubling 把边界或凹口预算乘以 2，则 C_S 由 8 变 16，立即破坏闭合目标。 | BacklundZeroCostMirrorProjectionIdentityLedger |
| `DoublingReducedToZeroCostProjection` | `true` | `false` | 预算保持 doubling 已压成零成本镜像投影、半权归一化、无重复扣费三包。 | BacklundZeroCostMirrorProjectionIdentityLedger AND BacklundHalfWeightSymmetricTraceNormalizationLedger AND BacklundNoDoubleCountingMirrorBoundaryLedger |
| `BacklundZeroCostMirrorProjectionIdentityLedger` | `false` | `false` | 尚未证明 doubled formal unit 是恒等式级投影而非新预算项。 | BacklundZeroCostMirrorProjectionIdentityLedger |
| `BacklundHalfWeightSymmetricTraceNormalizationLedger` | `false` | `false` | 尚未证明 doubled trace 的 1/2 归一化与原始 Backlund 目标严格等价。 | BacklundHalfWeightSymmetricTraceNormalizationLedger |
| `BacklundNoDoubleCountingMirrorBoundaryLedger` | `false` | `false` | 尚未证明镜像边界和镜像凹口不会重复扣费。 | BacklundNoDoubleCountingMirrorBoundaryLedger |
| `BacklundBudgetPreservingXiSymmetricContourDoublingLedger` | `false` | `false` | 三包闭合后才可继续验收镜像弧方向和原 trace 投影。 | BacklundMirrorIndentArcOrientationLedger AND BacklundOriginalTraceProjectionNoLossLedger |

## 4. 下一步

当前真正最窄点：`BacklundZeroCostMirrorProjectionIdentityLedger`。
归一化验收：`BacklundHalfWeightSymmetricTraceNormalizationLedger`。
无重复扣费验收：`BacklundNoDoubleCountingMirrorBoundaryLedger`。
doubling 后方向验收：`BacklundMirrorIndentArcOrientationLedger`。
原 trace 投影验收：`BacklundOriginalTraceProjectionNoLossLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：对称 doubling 已压到零成本镜像投影；命题尚未自足闭合。
