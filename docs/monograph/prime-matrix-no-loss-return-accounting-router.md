# Prime Matrix no-loss return accounting 路由器

**状态：** `no_loss_return_accounting_closed_hash_stability_open`

NoLossReturnAccountingLemma 已闭合：未进入普通来源族的义务都显式保留为 PDEC/SAE/ColumnCRT/Rankin/constant-gap/downstream-parameter 等命名 return。下一最窄点是 `CanonicalFormalUnitHashStabilityLemma`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
no_loss_return_accounting_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
NoLossReturnAccountingLemma => PartitionNoLossAndDisjointness AND SourceFamilyAssignmentTotality AND EmitterDownstreamReturn AND TerminalSchemaReconciliation AND MultiplicityAbsorption.
```

## 2. 守恒等式

```text
O(w)=SourceRecords disjoint_union NamedReturnRecords; Lost(O)=empty.
```

## 3. 守恒律

| law | formula | meaning |
| --- | --- | --- |
| finite_obligation_domain | O(w) is finite and canonically partitioned. | partition coverage 给出有限义务域，所有后续记账只在 O(w) 内发生。 |
| total_source_assignment | assign: O(w) -> SourceFamilies union NamedReturns is total. | source assignment totality 已保证每个 obligation 有登记来源族或命名回流归宿。 |
| named_return_totality | Return(o) in {PDEC, SAE, ColumnCRT, Rankin, ConstantGap, CleanKLS/DLS, DownstreamParameter}. | 失败、边界和终端对象保留为命名 return，不允许进入无名 sink。 |
| multiplicity_absorption | duplicates -> weighted PDEC or quotient or reuse return. | 同坐标重复和跨层复用不会形成第五出口，只能商化、加权或回流。 |
| no_terminal_erasure | TerminalNotProved(o) means open return record, not deleted obligation. | PDEC/SAE/Rankin 未排斥时仍作为打开的终端记录存在，不能被当作已证明或丢弃。 |
| conservation_equation | O(w)=disjoint_union(SourceRecords) disjoint_union(NamedReturnRecords), Lost(O)=empty. | 本引理只证明不漏账；不证明任何终端族不存在。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| NoLossReturnAccountingGateActive | `true` | `false` | 上一层已把最窄点推进到 no-loss return accounting。 | NoLossReturnAccountingLemma |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步只整理假设早期零行 witness 的义务账本，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| PartitionNoLossAndDisjointnessImported | `true` | `true` | O(w) 覆盖不漏、key-fibers 不交，重复和边界项已有 return 承载位置。 | 无义务域丢失口。 |
| SourceFamilyAssignmentTotalityImported | `true` | `true` | 每个 formal unit obligation 已落入已登记来源族或父级 named return payload。 | 无未分配 obligation。 |
| EmitterDownstreamReturnImported | `true` | `true` | 七个来源族均有 downstream/return 目标，失败时不进入无名 sink。 | 具体参数账本仍可下游打开。 |
| TerminalSchemaReconciliationImported | `true` | `true` | 抽象终端包已调和为全局 PDEC/sparse/SAE/ColumnCRT/Rankin 等命名终端桶。 | 终端排斥仍未证明。 |
| MultiplicityStitchingAbsorbed | `true` | `true` | 口径不一致、同坐标重复和跨层复用只允许 weighted/quotient/reuse return。 | 不产生第五出口。 |
| TerminalExclusionNotUsed | `true` | `false` | no-loss 只要求终端对象被保留为打开记录，不要求 PDEC/SAE/Rankin 已被排斥。 | GlobalPDECorSparseTerminalExclusion 仍保留给后续。 |
| NoLossReturnAccountingLemma | `true` | `true` | 所有 obligation 都在 SourceRecords 或 NamedReturnRecords 中守恒；Lost(O)=empty。 | CanonicalFormalUnitHashStabilityLemma |

## 5. 下一步

当前唯一最窄点更新为 `CanonicalFormalUnitHashStabilityLemma`。

审稿边界：本步只证明不漏账；不证明 PDEC/SAE/ColumnCRT/Rankin 终端排斥，也不关闭行列无条件定理。
