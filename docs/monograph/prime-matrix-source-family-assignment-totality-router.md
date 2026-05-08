# Prime Matrix source family assignment totality 路由器

**状态：** `source_family_assignment_totality_closed_no_loss_return_open`

SourceFamilyAssignmentTotalityLemma 已闭合：命名 return、quotient/reuse、colored corridor 与 raw physical filler atom 都已归入已登记来源族或父级 named return payload。下一最窄点是 `NoLossReturnAccountingLemma`。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
source_family_assignment_interface_closed=true
source_family_assignment_totality_closed=true
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
SourceFamilyAssignmentTotalityLemma => SourceFamilyAssignmentInterfaceClosed AND PhysicalFillerAtomSourceFamilyEmbeddingLemma.
```

## 2. Assignment 表

| obligation_kind | assignment | status |
| --- | --- | --- |
| named_return_records | 按 return source_family_id 直接进入 Endpoint/TailAnchor/HighOverlap/SmoothCore/Sparse/RankinConstant 等已登记族。 | closed_schema |
| quotient_reuse_records | 按 Multiplicity-Stitching 回流到 CoordinateQuotient、ReuseDefect、ColumnCRT/SAE/TailAnchor/PDEC。 | closed_schema |
| colored_corridor_records | 进入 ColoredDisjointCorridorBudgetViolation。 | closed_schema |
| raw_physical_filler_atoms | 必须证明每个 canonical (c,q_*(c),m_*(c)) 可作为某个已登记 source family 的 payload 或 named return 字段。 | closed_payload_embedding |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SourceFamilyAssignmentGateActive | `true` | `false` | 上一层已把最窄点推进到 source family assignment totality。 | SourceFamilyAssignmentTotalityLemma |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设早期零行 witness 的 formal units，不使用真实缺席。 | 保持 row_column_unconditional_closed=false。 |
| PartitionAndDomainImported | `true` | `true` | partition coverage 与 O(w) 规范化已闭合。 | 每个 obligation 已有 key 与类型。 |
| FiniteTaxonomyEmitterImported | `true` | `true` | 有限来源族 taxonomy 与记录发射器已闭合。 | assignment 的目标族固定。 |
| NamedReturnAssignmentClosed | `true` | `true` | phase defect、PDEC/SAE/ColumnCRT 和终端回流都已有命名 return schema。 | NamedReturnSourceFamilyAssignmentClosed |
| QuotientReuseSourceFamilyAssignmentClosed | `true` | `true` | quotient/reuse 记录作为 named return 处理，不要求新增来源族。 | QuotientReuseSourceFamilyAssignmentClosed |
| SourceFamilyAssignmentInterfaceClosed | `true` | `true` | source family assignment 的输入域、目标 taxonomy 与已闭合 schema 已固定。 | SourceFamilyAssignmentInterfaceClosed |
| PhysicalFillerAtomSourceFamilyEmbeddingAvailable | `true` | `true` | raw physical filler atom 到已登记 source family 的嵌入证明状态。 | PhysicalFillerAtomSourceFamilyEmbeddingLemma |
| SourceFamilyAssignmentTotalityLemma | `true` | `true` | raw physical filler atom embedding 已闭合，因此 assignment totality 闭合。 | NoLossReturnAccountingLemma |

## 4. 下一步

当前唯一最窄点更新为 `NoLossReturnAccountingLemma`。

审稿边界：本步只关闭 source family assignment totality；不证明 no-loss return、终端排斥，也不关闭行列无条件定理。
