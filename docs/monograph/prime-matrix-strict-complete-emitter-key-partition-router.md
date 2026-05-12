# Prime Matrix strict complete emitter key partition 路由器

**状态：** `strict_complete_emitter_key_partition_reduced_to_actual_source_table_budget_refinement_return_open`

`RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger` 被拆为 actual 源表、complete trace/key 预算、符号/local refinement 与超预算/未登记回流四项。已有材料只闭合了“源表若存在则给 complete key”的形式蕴含；actual noncanonical primitive emitter 源表本身仍未证明，所以 fixed-pair 纤维链继续开放。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
complete_emitter_key_partition_router_closed=true
source_table_to_complete_key_implication_closed=true
actual_noncanonical_primitive_emitter_source_table_proved=false
complete_emitter_trace_key_budget_proved=false
registered_complete_primitive_emitter_key_partition_polylog_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 字段律

A complete primitive emitter key partition exists only after the actual noncanonical pre-Cauchy source table is fixed. The key is not a post-hoc label: it must be generated with each primitive summand and must include branch trace, exact `(u,v)` convention, sign/local factor and dyadic/truncation state. Polylog cardinality and return tags are part of the same table.

## 2. 原子化

拆分前：

```text
RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger
```

拆分后：

```text
ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND CompleteEmitterTraceKeyBudgetLedger AND SignLocalFactorRefinementNoCancellationLedger AND OverBudgetOrUnregisteredReturnLedger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CompleteKeyPartitionTargetActive` | `true` | `false` | 上一层已把 fixed-pair fiber bound 的首要实际障碍压成 complete primitive emitter key 分区。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger |
| `SourceTableToCompleteKeyImplicationClosed` | `true` | `true` | 若 actual 原始生成表存在，则 branch key、u/v map、dyadic/truncation、sign/local factor 可组成 complete key。 | 该蕴含不证明 actual noncanonical 源表存在。 |
| `PathPartitionNeedsPreCauchySourceImported` | `true` | `true` | 路径分割必须建立在 Cauchy/dispersion 前的 actual 系数公式上，不能从后验 payment 图补标签。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger。 |
| `CanonicalTemplateCrossImportBlocked` | `true` | `true` | canonical RIW/Buchstab 决策树只在 canonical-source 分支闭合，不能跨导入 noncanonical complete key。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger。 |
| `GenericWFDNotAKeyEmitter` | `true` | `true` | generic WFD 是形式约束，不是 primitive summand emitter，不能生成 complete key 表。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger。 |
| `OriginAdmissionStillOpen` | `false` | `false` | 当前材料尚未证明 noncanonical clean-core 候选都有 pre-Cauchy primitive source constructor。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger。 |
| `CompleteTraceBudgetStillOpen` | `false` | `false` | 当前材料没有证明 complete trace/key 数满足 log^O(1) 预算；几何标签不能自动成为 actual source key。 | CompleteEmitterTraceKeyBudgetLedger。 |
| `SignLocalFactorRefinementStillOpen` | `false` | `false` | 同一 complete key 下非零 local factor 与符号细分仍依赖 actual 生成表，当前未证明。 | SignLocalFactorRefinementNoCancellationLedger。 |
| `ReturnLedgerForOverBudgetOrUnregisteredOpen` | `false` | `false` | 超预算、未登记、thin/rejected 或抵消分支必须命名回流；当前未在 actual emitter key 表内完成。 | OverBudgetOrUnregisteredReturnLedger。 |
| `CompleteEmitterKeyPartitionCurrentCorpusProved` | `false` | `false` | actual 源表、complete trace 预算、符号/local refinement 与回流纪律尚未合取证明。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND CompleteEmitterTraceKeyBudgetLedger AND SignLocalFactorRefinementNoCancellationLedger AND OverBudgetOrUnregisteredReturnLedger |

## 4. 下一主攻点

```text
ActualNoncanonicalPrimitiveEmitterSourceTableLedger
```
