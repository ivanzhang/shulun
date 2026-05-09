# Prime Matrix 当前活跃最终输入归约路由器

**状态：** `active_final_inputs_reduced_to_noncanonical_math_plus_dstructure_open`

最终开放输入已收窄：PDEC 与 sparse 只是未来新增实例时的显式 schema 防火墙，当前没有已物化对象可攻。现在真正活跃的最终输入只剩 noncanonical 二选一数学输入，另加 DStructure/Rankin 晋级独立验收；完整无条件闭合仍未成立。

```text
active_final_inputs_boundary_closed=true
all_active_final_inputs_proved_or_accepted=false
row_column_unconditional_closed=false
```

## 1. 收缩公式

```text
FinalOpenInputs = inactive_future_schema(PDEC,sparse) + (ActualFullSNonAPSourceCapacityAntiAtomForActualSource OR CDependentResidueWeightSpectralCancellationInput) + DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance.
```

## 2. 判定表

| gate | active_now | boundary_closed | proved_or_accepted | meaning | remaining |
| --- | --- | --- | --- | --- | --- |
| CurrentMaterializedPDECSparseFrontierZero | `false` | `true` | `true` | 当前已物化 PDEC/sparse 终端前沿清零；它们不是当前活跃硬点。 | 若未来新增实例，才触发显式 schema。 |
| FutureExplicitPrimitivePDECSchema | `false` | `true` | `false` | PDEC future schema 是防火墙义务，不是当前已有待排斥对象。 | new materialized PDEC family only if proposed |
| FutureExplicitSparsePacketExtractorSchema | `false` | `true` | `false` | Sparse future schema 是防火墙义务，不是当前已有待排斥对象。 | new materialized sparse route only if proposed |
| NoncanonicalTwoLaneMathInput | `true` | `true` | `false` | 当前数学硬点是 noncanonical 二选一：实际源反原子，或 c-dependent 完成型谱抵消。 | ActualFullSNonAPSourceCapacityAntiAtomForActualSource OR CDependentResidueWeightSpectralCancellationInput |
| DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | `true` | `true` | `false` | 最终晋级硬点是 DStructure/Tail-log4/finite verification/Rankin 子账本的独立接受。 | independent promotion acceptance |

## 3. 下一步

数学最窄点：`NoncanonicalTwoLaneMathInput`。
并行晋级验收点：`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。
