# Prime Matrix Backlund 边界 Stieltjes 跳变转移终端路由器

**状态：** `backlund_boundary_stieltjes_jump_transfer_terminal_open`

边界 Stieltjes 跳变公式本身可以自足登记：避零、应用 argument principle、再按重数取极限。但这只说明跳变在哪里，并不支付跳变预算。由于半镜像免费抵消和原始奇部为零都已被阻断，预算保持的 Stieltjes 转移与 Backlund 近零凹口成本等价。因此严格自足路线没有新的更小逃逸口；唯一剩余就是内部证明经典 Backlund 零点缩进成本，或明确接受外部经典 Backlund 缩进引理。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
formal_stieltjes_jump_formula_closed=true
budget_preserving_stieltjes_jump_transfer_closed=false
indent_cost_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 形式恒等式与预算差别

```text
d arg F(a+it) = continuous log-derivative variation + pi * dN_boundary(t)
boundary zeros are first avoided, then counted by analytic multiplicity in the limit
```

这条公式只登记跳变测度；若要闭合 `C_S=8`，还必须证明跳变测度不产生新的正比例成本。

## 2. 跳变预算压力

| item | value |
| --- | ---: |
| Jensen zero-count coefficient | `16.000000000000` |
| per unpaired jump cost | `3.141592653590` |
| naive jump coefficient | `50.265482457437` |
| available stability margin | `0.078125000000` |
| allowed unpaired coefficient | `0.024867959858` |
| deficit | `50.187357457437` |

结论：任何 Jensen 规模的未配对 Stieltjes 跳变都会立即超过稳定余量；预算保持必须是零系数级。

## 3. Stieltjes 拆解

| atom | status | role |
| --- | --- | --- |
| `BacklundBoundaryStieltjesJumpFormulaClosed` | `closed` | 避零后取极限，把边界 arg 变化写成连续 log-derivative 变差加按重数计的跳变测度。 |
| `BacklundBudgetPreservingStieltjesJumpTransferLedger` | `open` | 证明该跳变测度不新增 C_S 或窗口余量成本；这要求精确抵消或外部缩进引理。 |
| `BacklundSignedCrossingPairingInvolutionLedger` | `blocked_by_prior_reviews` | 此前半镜像/奇部为零路线已证明不能免费消掉原始 trace 的奇部。 |
| `ClassicalBacklundZeroIndentationCostInternalProofLedger` | `only_strict_internal_remaining` | 若坚持完全自足，必须直接内部证明经典 Backlund 缩进成本，而不是再做权重或镜像转移。 |

## 4. 终端等价

```text
BacklundBoundaryStieltjesJumpTransferLedger => BacklundBoundaryStieltjesJumpFormulaClosed AND BacklundBudgetPreservingStieltjesJumpTransferLedger
BacklundBudgetPreservingStieltjesJumpTransferLedger => ClassicalBacklundZeroIndentationCostInternalProofLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted
ClassicalBacklundZeroIndentationCostInternalProofLedger => BacklundZeroProximityIndentationCostLedger
```

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BoundaryStieltjesJumpGateActive` | `true` | `true` | 点态支撑不匹配后，唯一剩余被压成边界 Stieltjes 跳变/缩进账本。 | BacklundBoundaryStieltjesJumpTransferLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只处理假设链条中的解析 trace，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `BacklundBoundaryStieltjesJumpFormulaClosed` | `true` | `true` | 端点避零和重数极限 convention 足以给出跳变测度的形式登记。 | BacklundBudgetPreservingStieltjesJumpTransferLedger |
| `ZetaXiJumpTransportAlreadyClosed` | `true` | `true` | 跳变可从 arg zeta 搬运到 xi 零点重数；Gamma/初等因子不产生 crossing jump。 | BacklundSignedCrossingPairingInvolutionLedger |
| `HalfMirrorFreeCancellationBlocked` | `true` | `true` | 半镜像平均只能消掉平均 trace 的奇偶组合，不能证明原始 trace 奇部为零。 | BacklundOddMirrorCorrectionCostLedger |
| `OddCorrectionEqualsIndentCost` | `true` | `true` | 原始 trace 的未配对跳变成本已终端归并为 Backlund 近零凹口成本。 | BacklundZeroProximityIndentationCostLedger |
| `CS8HasNoResidualBudget` | `true` | `true` | 外部 C_S=8 已是 16*1/2 的紧等号；自足路线不能新增任何正比例 Stieltjes 跳变成本。 | BacklundBudgetPreservingStieltjesJumpTransferLedger |
| `BacklundBudgetPreservingStieltjesJumpTransferLedger` | `false` | `false` | 形式跳变公式不等于预算保持；预算保持正是经典 Backlund 缩进成本本身。 | ClassicalBacklundZeroIndentationCostInternalProofLedger |
| `BacklundBoundaryStieltjesJumpTransferLedger` | `false` | `false` | Stieltjes 路线没有产生新闭合自由度，终端回到内部证明经典缩进引理或接受外部引理。 | ClassicalBacklundZeroIndentationCostInternalProofLedger OR ClassicalBacklundZeroIndentationCostExternalAccepted |

## 6. 下一步

严格自足唯一剩余：`ClassicalBacklundZeroIndentationCostInternalProofLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。
并行保留晋级门：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。

判定：Stieltjes 形式层已闭合，预算层未闭合；它终端等价于 Backlund 近零凹口成本。
