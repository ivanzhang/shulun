# Prime Matrix Backlund crossing trace 容量收缩路由器

**状态：** `backlund_crossing_trace_capacity_reduced_to_signed_pairing_open`

crossing trace 的下层最窄目标已从“付凹口成本”收缩为“证明带符号 crossing 精确配对”。原因是剩余稳定余量只有 5/64，而 Jensen C16 规模的未配对零点按 pi 粗付会产生约 50.187 的系数缺口。所以自足路线不能再走正比例残留预算，只能证明未配对 crossing 的 log(T) 系数为 0，或明确接受外部经典 Backlund 凹口引理。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
trace_capacity_reduction_closed=true
backlund_local_crossing_trace_closed=false
backlund_indent_self_contained_closed=false
row_column_self_contained_closed=false
```

## 1. 系数容量

| item | value |
| --- | ---: |
| `zero_count_coefficient` | `16.000000000000` |
| `per_unpaired_crossing_cost` | `3.141592653590` |
| `naive_indentation_coefficient` | `50.265482457437` |
| `available_stability_margin` | `0.078125000000` |
| `max_unpaired_crossing_coefficient` | `0.024867959858` |
| `allowed_fraction_of_jensen_count` | `0.001554247491` |
| `naive_margin_deficit` | `50.187357457437` |

核心不等式：

```text
unpaired_crossing_coefficient * pi <= 5/64
so unpaired_crossing_coefficient <= 0.024867959858
but Jensen near-zero coefficient available is 16.
```

这说明：若未配对 crossing 仍有任何 Jensen 规模的正比例残留，预算立即失败；自足路线必须把残余 log(T) 系数压到 0。

## 2. 自足替换

```text
BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger
  =>
(BacklundCanonicalNearZeroClusterBoxLedger AND BacklundSignedCrossingPairingInvolutionLedger AND BacklundResidualIndentCoefficientZeroLedger)
```

| atom | role |
| --- | --- |
| `BacklundCanonicalNearZeroClusterBoxLedger` | 把 eta=1/16 内所有近零点按窗口和重数做 canonical box 账本。 |
| `BacklundSignedCrossingPairingInvolutionLedger` | 在同一 formal unit 内给出带符号 crossing 的配对 involution。 |
| `BacklundResidualIndentCoefficientZeroLedger` | 由配对证明未配对 crossing 的 log(T) 系数为 0，而不是小的正数。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CrossingTraceCapacityGateActive` | `true` | `true` | 上一层已把凹口成本二选一压成局部 crossing trace 单原子。 | BacklundLocalZeroCrossingTraceAndIndentHomotopyLedger |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在早期零行反例假设链条内做解析容量收缩，不使用真实零行缺席。 | 保持 row_column_self_contained_closed=false。 |
| `NaiveResidualBudgetImpossible` | `true` | `true` | 若允许 Jensen C16 规模的未配对 crossing 粗付 pi 成本，系数缺口约 50.187。 | BacklundSignedCrossingPairingInvolutionLedger |
| `PositiveCoefficientResidualForbidden` | `true` | `true` | 余量只允许不到 Jensen 近零数量上界的 0.2% 留作未配对成本；这不是稳健闭合路径。 | BacklundSignedCrossingPairingInvolutionLedger |
| `ExactCancellationIsNecessary` | `true` | `true` | 自足路线若不调用外部 Backlund 凹口引理，就必须证明 log(T) 级未配对 crossing 系数为 0。 | BacklundSignedCrossingPairingInvolutionLedger AND BacklundResidualIndentCoefficientZeroLedger |
| `ClusterBoxSchemaAvailable` | `true` | `true` | 上一层 trace schema 已指定 window_id、zero_cluster_box、homotopy_arc、branch_jump 等字段。 | BacklundCanonicalNearZeroClusterBoxLedger |
| `BacklundCanonicalNearZeroClusterBoxLedger` | `false` | `false` | 尚未生成每个近零窗口的 canonical cluster box 与 multiplicity hash。 | BacklundCanonicalNearZeroClusterBoxLedger |
| `BacklundSignedCrossingPairingInvolutionLedger` | `false` | `false` | 尚未证明所有 branch_jump 都在同一 formal unit 中成对抵消。 | BacklundSignedCrossingPairingInvolutionLedger |
| `BacklundResidualIndentCoefficientZeroLedger` | `false` | `false` | 只有配对 involution 完成后，残余凹口系数才能降为 0 并落入 5/64 余量。 | BacklundResidualIndentCoefficientZeroLedger |

## 4. 下一步

当前下层最窄点：`BacklundSignedCrossingPairingInvolutionLedger`。
支撑账本：`BacklundCanonicalNearZeroClusterBoxLedger`。
配对完成后验收：`BacklundResidualIndentCoefficientZeroLedger`。
外部可接受逃逸门：`ClassicalBacklundZeroIndentationCostExternalAccepted`。
并行保留晋级门：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。

判定：trace 容量收缩已完成；命题尚未自足闭合。
