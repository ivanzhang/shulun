# Prime Matrix Backlund 半镜像平均身份障碍路由器

**状态：** `backlund_half_mirror_average_obstruction_closed_odd_part_zero_next`

半镜像平均路线存在纯代数障碍：设原始 branch-jump 为 A、镜像为 M。半平均只给 E=(A+M)/2；原始 trace 是 E+O，其中 O=(A-M)/2。若镜像抵消条件 M=-A 成立，则 E=0 但 O=A，原始 crossing 成本并没有消失。因此要想零成本闭合，必须另证 `BacklundOriginalTraceOddPartZeroLedger`；否则只能保留奇部修正并回到凹口成本/外部 Backlund 引理。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
half_average_obstruction_closed=true
half_average_identity_closed=false
zero_cost_projection_identity_closed=false
backlund_local_crossing_trace_closed=false
row_column_self_contained_closed=false
```

## 1. 代数分解

| symbol | meaning |
| --- | --- |
| `A` | 原始 Backlund trace 的局部 branch-jump 贡献。 |
| `M` | xi 镜像 trace 的对应 branch-jump 贡献。 |
| `E=(A+M)/2` | 镜像偶部，也就是半镜像平均能保留的部分。 |
| `O=(A-M)/2` | 镜像奇部；若 M=-A，则 O=A，正是原始 crossing 贡献。 |

关键判断：若 `M=-A`，半平均 `E=0`，但原始 trace 的奇部 `O=A`，所以原始成本没有被消灭。

## 2. 自足替换

```text
BacklundOriginalTraceHalfMirrorAverageIdentityLedger
  =>
(BacklundMirrorEvenPartIdentityClosed AND (BacklundOriginalTraceOddPartZeroLedger OR BacklundOddMirrorCorrectionCostLedger))
```

## 3. 后续路线

| route | meaning |
| --- | --- |
| `BacklundOriginalTraceOddPartZeroLedger` | 证明原始 trace 的奇部为 0；这等价于无 crossing/零避让在本 formal unit 中成立。 |
| `BacklundOddMirrorCorrectionCostLedger` | 保留奇部修正并支付其成本；这回到凹口成本/外部 Backlund 引理路线。 |
| `ClassicalBacklundZeroIndentationCostExternalAccepted` | 接受经典 Backlund 零点缩进引理，绕开内部半平均配对路线。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `HalfMirrorAverageGateActive` | `true` | `true` | 上一层把零成本投影压到原始 trace 与半镜像平均的身份。 | BacklundOriginalTraceHalfMirrorAverageIdentityLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只分析假设链条中的解析 trace，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `ZetaXiJumpTransportAvailable` | `true` | `true` | branch-jump 已可在 xi 语言中讨论，镜像奇偶分解合法。 | 无对象搬运剩余。 |
| `TraceCapacityRequiresZeroOddCoefficient` | `true` | `true` | 容量收缩已证明任何 Jensen 规模正比例奇部残留都会超出 5/64 余量。 | BacklundOriginalTraceOddPartZeroLedger |
| `HalfAverageAlgebraObstructionClosed` | `true` | `true` | 若镜像跳变反号，半平均消掉的是奇部；但原始 trace 等于偶部加奇部，除非奇部先为 0。 | BacklundOriginalTraceOddPartZeroLedger |
| `EvenPartIdentityClosed` | `true` | `true` | A=(A+M)/2+(A-M)/2 是恒等式；只能闭合偶部定义，不能闭合原始 trace。 | BacklundMirrorEvenPartIdentityClosed |
| `BacklundOriginalTraceHalfMirrorAverageIdentityLedger` | `false` | `false` | 半镜像平均不能单独替代原始 trace；必须额外证明奇部为 0 或支付奇部修正成本。 | BacklundOriginalTraceOddPartZeroLedger OR BacklundOddMirrorCorrectionCostLedger |
| `BacklundOriginalTraceOddPartZeroLedger` | `false` | `false` | 尚未证明原始 trace 没有 crossing 奇部；这是新的唯一最窄内部目标。 | BacklundZeroAvoidingShiftWithoutJumpLedger |
| `BacklundOddMirrorCorrectionCostLedger` | `false` | `false` | 若不能证明奇部为 0，就必须恢复成本账本；这不会给出零成本自足闭合。 | ClassicalBacklundZeroIndentationCostExternalAccepted |

## 5. 下一步

当前真正最窄点：`BacklundOriginalTraceOddPartZeroLedger`。
等价旧目标：`BacklundZeroAvoidingShiftWithoutJumpLedger`。
若失败则回到：`BacklundOddMirrorCorrectionCostLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。

判定：半镜像平均身份不能直接闭合；必须证明原始奇部为 0。
