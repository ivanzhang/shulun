# Prime Matrix Backlund 内部证明义务终局路由器

**状态：** `backlund_internal_proof_obligation_unique_remaining_open`

严格自足路线的唯一剩余已经不能再压成权重吸收、点态转移、Stieltjes 免费转移或镜像抵消。这些路线均已被阻断或终端归并。最新精确定名的剩余是 `ClassicalBacklundZeroIndentationCostInternalProofLedger`，它等价于旧的 `BacklundZeroProximityIndentationCostLedger`，但明确要求作者侧完整重证经典 Backlund 零点缩进成本。在该内部证明或外部引理接受之前，行/列命题不能声明无条件自足闭合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
strict_self_contained_unique_remaining=ClassicalBacklundZeroIndentationCostInternalProofLedger
equivalent_old_remaining=BacklundZeroProximityIndentationCostLedger
row_column_self_contained_closed=false
row_column_external_backlund_closed=false
```

## 1. 已阻断或归并路线

| route | status | reason |
| --- | --- | --- |
| `LittlewoodWeightAbsorption` | `blocked` | 横向权重 beta-a 不能统一支付贴边界点态跳变。 |
| `PointwiseCoreTransfer` | `blocked` | 矩形平均层无法无乘子转成短窗口点态核心。 |
| `BoundaryStieltjesFreeTransfer` | `terminal_equivalent` | 形式跳变公式可闭合，但预算保持正是凹口成本本身。 |
| `HalfMirrorAverageCancellation` | `blocked` | 半平均不能证明原始 trace 奇部为 0。 |
| `OddCorrectionRoute` | `terminal_equivalent` | 奇部修正成本已经归并为 Backlund 近零凹口成本。 |

## 2. 内部证明不可压缩义务

| obligation | must prove | why needed |
| --- | --- | --- |
| `LocalContourDeformationWithZeros` | 对每个短窗口和每个近零 cluster，给出避零轮廓、缩进弧、极限方向和解析重数登记。 | 端点 convention 只定义极限；它不证明移动窗口中的近零核心预算。 |
| `BudgetPreservingJumpAccounting` | 未配对 jump 的 log(T) 系数为 0，或等价地证明所有正比例跳变已在同一恒等式中抵消。 | 任何 Jensen C16 规模的未配对 jump 都产生约 50.265 的系数，远超 5/64 余量。 |
| `NoRVMCircularity` | 证明不得使用由待证 Backlund C_S 推出的 RVM/C_N=16 局部计数。 | RVM->CN16 已明确依赖原始 arg zeta 常数 C_S=8；反向调用会循环。 |
| `NoDoubleCountingAcrossJensenAndIndent` | 近零点不能同时在 Jensen 计数、RVM 端点计数和凹口成本中重复扣费。 | C_S=8 是紧等号，窗口稳定余量只有 5/64，没有多余正预算。 |
| `C8ReaggregationPreserved` | 缩进内部证明完成后，仍能保持 bridge factor=1/2 与 C_boundary=16 合成 C_S=8。 | 若缩进证明引入任何额外常数，Backlund 外层常数立即失配。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `OldIndentCostRemainingActive` | `true` | `true` | 旧最终状态中的严格自足剩余仍是 Backlund 近零凹口成本。 | BacklundZeroProximityIndentationCostLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只做假设链条内解析证明义务审查，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `WeightAbsorptionReducedNotClosed` | `true` | `true` | 零点权重吸收已压成经典缩进引理内部化，而非直接闭合。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| `PointwiseSupportMismatchClosed` | `true` | `true` | 点态核心转移的直接乘子路线已被横向支撑/纵向跳变不匹配阻断。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| `StieltjesRouteTerminal` | `true` | `true` | 边界 Stieltjes 形式层闭合，预算层终端等价于经典缩进成本。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| `OddCorrectionTerminalImported` | `true` | `true` | 原始奇部修正没有新自由度，已归并回凹口成本。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| `ClassicalBacklundZeroIndentationCostInternalProofLedger` | `false` | `false` | 当前仓库没有完成经典 Backlund 零点缩进成本的作者侧内部证明。 | ClassicalBacklundZeroIndentationCostInternalProofLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted |
| `RowColumnSelfContainedClosed` | `false` | `false` | 严格自足行/列命题仍未闭合；不能作者侧声明完整无条件证明。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |

## 4. 下一步

严格自足唯一剩余：`ClassicalBacklundZeroIndentationCostInternalProofLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。
外部路线仍需独立验收门：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。

判定：这是当前作者侧证明链条的真正终端硬点；尚未闭合。
