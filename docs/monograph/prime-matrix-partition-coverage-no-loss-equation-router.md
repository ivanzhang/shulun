# Prime Matrix partition coverage no-loss equation 路由器

**状态：** `partition_no_loss_equation_closed_disjointness_open`

PartitionCoverageNoLossEquationLemma 已闭合：因为 canonical key 是 O(w) 上的总函数，O(w) 等于所有 key-fibers 的并，命名回流记录也作为 obligations 保留。下一最窄点是 `PartitionDisjointnessAndBoundaryReturnLemma`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
partition_coverage_no_loss_equation_closed=true
formal_unit_partition_coverage_lemma_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
PartitionCoverageNoLossEquationLemma => PartitionCoverageNoLossEquationClosed AND PartitionDisjointnessAndBoundaryReturnLemma.
```

## 2. 覆盖等式

| name | formula |
| --- | --- |
| total_key_map | key: O(w) -> K is defined for every obligation after domain canonicalization。 |
| fiber_definition | O_k={o in O(w): key(o)=k}。 |
| cover_equation | O(w)=union_{k in key(O(w))} O_k。 |
| return_inclusion | return records are obligations in O(w) with branch_type in named_return/quotient/reuse。 |
| no_loss_scope | 本引理只证明覆盖不漏；同一物理原子是否重复计数交给 disjointness/boundary-return 引理。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| NoLossEquationGateActive | `true` | `false` | 上一层已把最窄点推进到 partition coverage no-loss 等式。 | PartitionCoverageNoLossEquationLemma |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行 witness 的 O(w)，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| CanonicalDomainImported | `true` | `true` | O(w) 已是有限规范义务域。 | 无义务域格式剩余。 |
| TotalFiniteKeyImported | `true` | `true` | 每个 obligation 都有 canonical finite key。 | key map 是总函数。 |
| PartitionInterfaceImported | `true` | `true` | partition coverage 接口已要求 no-loss 覆盖等式。 | 本步证明覆盖不漏。 |
| PartitionCoverageNoLossEquationClosed | `true` | `true` | 由总函数 key 的 fiber 分解，O(w) 等于所有 key-fibers 的并；return records 已包含在 O(w)。 | PartitionCoverageNoLossEquationClosed |
| PartitionCoverageNoLossEquationLemma | `true` | `true` | no-loss 覆盖等式已闭合；剩余是同坐标重复、边界交叠和回流记录的不交化。 | PartitionDisjointnessAndBoundaryReturnLemma |

## 4. 下一步

当前唯一最窄点更新为 `PartitionDisjointnessAndBoundaryReturnLemma`。

审稿边界：本步只证明 key-fiber 覆盖不漏；不证明不交化，也不关闭行列无条件定理。
