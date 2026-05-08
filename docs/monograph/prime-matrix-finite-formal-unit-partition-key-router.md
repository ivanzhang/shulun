# Prime Matrix finite formal unit partition key 路由器

**状态：** `finite_formal_unit_partition_key_closed_no_loss_equation_open`

FiniteFormalUnitPartitionKeyLemma 已闭合：O(w) 的每个 obligation 都有 canonical finite key，同 key 对象就是一个 formal unit fiber。剩余不再是能否切分，而是 no-loss 覆盖等式 `PartitionCoverageNoLossEquationLemma`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
finite_formal_unit_partition_key_closed=true
formal_unit_partition_coverage_lemma_closed=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
FiniteFormalUnitPartitionKeyLemma => FiniteFormalUnitPartitionKeyClosed AND PartitionCoverageNoLossEquationLemma.
```

## 2. Key 字段

| field | source |
| --- | --- |
| formal_unit_id | 由 witness_id 与 source record canonical hash 给出。 |
| source_family_id | 来自已闭合的有限来源族 taxonomy。 |
| branch_type | physical、phase_defect、carry_cofactor、return、quotient 等有限分支。 |
| P_or_P_range | 继承 witness 或 source tuple。 |
| window_id | CLB 行窗、端点窗、走廊窗或 return packet 窗。 |
| D0,K,Omega | 若该义务有核心尺度/omega 截断/重叠阈值则继承；无则写 null。 |
| phase_key | 相位、residue、anchor、fixed_core 或 identity。 |
| source_tuple_hash | 锁定上述字段的 canonical hash。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FinitePartitionKeyGateActive | `true` | `false` | 上一层已把最窄点推进到 finite formal-unit key。 | FiniteFormalUnitPartitionKeyLemma |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理任意假设早期零行 witness 的 O(w)，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| CanonicalObligationDomainImported | `true` | `true` | O(w) 已规范化为有限 physical/return/quotient records。 | 可逐 obligation 指派 key。 |
| SourceTupleAndRecordSchemasImported | `true` | `true` | source tuple 与 formal unit source record 的字段、哈希纪律已固定。 | key 字段来源固定。 |
| FiniteSourceFamilyImported | `true` | `true` | source_family_id 只能来自有限来源族，记录发射器无新类型。 | key 的 family 坐标有限。 |
| FiniteFormalUnitPartitionKeyClosed | `true` | `true` | 每个 obligation 都可用固定字段生成 canonical finite key；同 key 的对象形成一个 formal unit fiber。 | FiniteFormalUnitPartitionKeyClosed |
| FiniteFormalUnitPartitionKeyLemma | `true` | `true` | finite key 引理闭合；下一步要证明 key-fibers 与 return records 对 O(w) 的 no-loss 覆盖等式。 | PartitionCoverageNoLossEquationLemma |

## 4. 下一步

当前唯一最窄点更新为 `PartitionCoverageNoLossEquationLemma`。

审稿边界：本步只证明 finite key 存在；不证明 no-loss 覆盖等式，也不关闭行列无条件定理。
