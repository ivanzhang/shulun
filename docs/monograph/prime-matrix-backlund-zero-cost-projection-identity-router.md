# Prime Matrix Backlund 零成本镜像投影身份路由器

**状态：** `backlund_zero_cost_projection_reduced_to_half_average_identity_open`

零成本镜像投影不能用“坐标投影回原 trace”伪闭合；那样没有任何 crossing 抵消。真正需要证明的是半镜像平均身份：原始 Backlund trace 等于 xi 对称半平均加已预算的 Gamma/初等偶部，同时 crossing branch_jump 全部落入镜像奇部并逐项抵消。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
zero_cost_projection_reduction_closed=true
zero_cost_projection_identity_closed=false
budget_preserving_doubling_closed=false
backlund_local_crossing_trace_closed=false
row_column_self_contained_closed=false
```

## 1. 投影模式

| mode | effect |
| --- | --- |
| `coordinate_projection` | 保留原始 Backlund trace，但镜像不会自动抵消原 trace 的 crossing 成本。 |
| `symmetric_half_average` | 可让镜像奇部抵消，但必须先证明半平均严格等于原始目标加已预算的偶部余项。 |

## 2. 自足替换

```text
BacklundZeroCostMirrorProjectionIdentityLedger
  =>
(BacklundOriginalTraceHalfMirrorAverageIdentityLedger AND BacklundMirrorOddJumpCancellationIdentityLedger AND BacklundEvenGammaElementaryRemainderBudgetLedger)
```

| atom | role |
| --- | --- |
| `BacklundOriginalTraceHalfMirrorAverageIdentityLedger` | 证明原始 Backlund trace 等于 xi 镜像半平均加显式 Gamma/初等偶部余项。 |
| `BacklundMirrorOddJumpCancellationIdentityLedger` | 证明 crossing branch_jump 属于镜像奇部，因此在半平均中逐项抵消。 |
| `BacklundEvenGammaElementaryRemainderBudgetLedger` | 证明镜像偶部只剩 Gamma/初等连续相位，并已由既有预算吸收。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ZeroCostProjectionGateActive` | `true` | `true` | doubling 容量纪律后，当前最窄点是零成本镜像投影身份。 | BacklundZeroCostMirrorProjectionIdentityLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条的解析恒等式，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `ZetaXiJumpTransportAvailable` | `true` | `true` | zeta branch_jump 已搬运到 xi；因此镜像奇偶分解可以在 xi 语言中表达。 | BacklundMirrorOddJumpCancellationIdentityLedger |
| `LeftRightFunctionalEquationBridgeAvailable` | `true` | `true` | 左/右边界函数方程桥已闭合，提供半镜像平均的边界身份基础。 | BacklundOriginalTraceHalfMirrorAverageIdentityLedger |
| `CoordinateProjectionFalseClosureBlocked` | `true` | `true` | 只投影回原 trace 虽然零成本，但不能带来抵消；必须证明半平均身份。 | BacklundOriginalTraceHalfMirrorAverageIdentityLedger |
| `ZeroCostProjectionReducedToHalfAverageIdentity` | `true` | `false` | 零成本投影已压成半镜像平均身份、奇部跳变抵消、偶部 Gamma 余项预算三包。 | BacklundOriginalTraceHalfMirrorAverageIdentityLedger AND BacklundMirrorOddJumpCancellationIdentityLedger AND BacklundEvenGammaElementaryRemainderBudgetLedger |
| `BacklundOriginalTraceHalfMirrorAverageIdentityLedger` | `false` | `false` | 尚未证明原始 Backlund 目标等于半镜像平均加已预算偶部。 | BacklundOriginalTraceHalfMirrorAverageIdentityLedger |
| `BacklundMirrorOddJumpCancellationIdentityLedger` | `false` | `false` | 尚未证明所有 crossing branch_jump 都进入镜像奇部并逐项抵消。 | BacklundMirrorOddJumpCancellationIdentityLedger |
| `BacklundEvenGammaElementaryRemainderBudgetLedger` | `false` | `false` | 尚未证明半平均留下的 Gamma/初等偶部不新增预算。 | BacklundEvenGammaElementaryRemainderBudgetLedger |
| `BacklundZeroCostMirrorProjectionIdentityLedger` | `false` | `false` | 三包闭合后才可继续半权归一化和无重复扣费验收。 | BacklundHalfWeightSymmetricTraceNormalizationLedger AND BacklundNoDoubleCountingMirrorBoundaryLedger |

## 4. 下一步

当前真正最窄点：`BacklundOriginalTraceHalfMirrorAverageIdentityLedger`。
奇部跳变验收：`BacklundMirrorOddJumpCancellationIdentityLedger`。
偶部 Gamma 预算验收：`BacklundEvenGammaElementaryRemainderBudgetLedger`。
随后归一化验收：`BacklundHalfWeightSymmetricTraceNormalizationLedger`。
随后无重复扣费验收：`BacklundNoDoubleCountingMirrorBoundaryLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：零成本镜像投影已压到半镜像平均身份；命题尚未自足闭合。
