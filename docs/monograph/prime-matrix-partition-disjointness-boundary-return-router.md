# Prime Matrix partition disjointness and boundary return 路由器

**状态：** `partition_disjointness_boundary_return_closed_partition_ready`

PartitionDisjointnessAndBoundaryReturnLemma 已闭合：key-fibers 按函数纤维不交，重复物理原子由 quotient/weighted/reuse return 处理，边界异常保留为 named return records。下一步可回收关闭 `FormalUnitPartitionCoverageLemma`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
partition_disjointness_boundary_return_closed=true
formal_unit_partition_coverage_lemma_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
PartitionDisjointnessAndBoundaryReturnLemma => PartitionDisjointnessAndBoundaryReturnClosed AND FormalUnitPartitionCoverageLemma.
```

## 2. 不交化律

| law | meaning |
| --- | --- |
| key_fiber_disjointness | 若 k1 != k2，则 O_k1 与 O_k2 不交，因为 key 是函数。 |
| same_coordinate_quotient | 同一物理坐标重复出现时，O(w) 中只保留 quotient record 或 weighted/reuse return。 |
| boundary_return_not_loss | 边界、端点、ColumnCRT、SAE、PDEC 记录仍属于 O(w)，但 branch_type 标记为 return。 |
| no_double_payment | 同一 physical filler atom 不能同时作为普通 payment 和 return payment 重复计数。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PartitionDisjointnessGateActive | `true` | `false` | 上一层已把最窄点推进到 partition disjointness/boundary return。 | PartitionDisjointnessAndBoundaryReturnLemma |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只整理假设早期零行 witness 的 partition 账本，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| NoLossEquationImported | `true` | `true` | key-fibers 已覆盖 O(w) 且不漏。 | 本步只处理不交化和边界回流。 |
| CanonicalDomainImported | `true` | `true` | O(w) 已含 quotient records 与 named return records。 | 重复对象已有承载位置。 |
| MultiplicityStitchingImported | `true` | `true` | 同坐标重复只能 quotient、weighted 或 reuse return，不能作为第五出口。 | 不重复计数。 |
| NamedBoundaryReturnImported | `true` | `true` | 边界和终端异常已按命名 return schema 登记。 | 不是无名丢失项。 |
| PartitionDisjointnessAndBoundaryReturnClosed | `true` | `true` | key-fibers 因 key 函数不交；重复物理原子已 quotient/return；边界项保留为 return records。 | PartitionDisjointnessAndBoundaryReturnClosed |
| PartitionDisjointnessAndBoundaryReturnLemma | `true` | `true` | 不交化和边界回流引理闭合；partition coverage 四个子门已经齐备。 | FormalUnitPartitionCoverageLemma |

## 4. 下一步

当前回收目标为 `FormalUnitPartitionCoverageLemma`：重新运行 partition coverage 路由，吸收四个已闭合子门。

审稿边界：本步不排斥任何 PDEC/SAE/Rankin 终端，只保证 partition 账本不重不漏。
