# Prime Matrix strict finite-prefix / named-return 耦合正余量账本路由器

**状态：** `coupled_margin_schema_closed_numeric_certificate_open`

`FinitePrefixNamedReturnCoupledPositiveMarginLedger` 的逻辑形态已闭合：最后只需要同一参数表中的 D0、E0、U0 三项和严格差值。现有材料只有代数公式、外部 B3 条件前沿、冷供给上界公式和命名回流压缩二分；尚没有 concrete same-parameter margin table，也没有有限 prefix hash、E_named 同参数扣除表、或 SparseHistoryDemandExceedsNonpersistentSupplyBudget 的数值反超。因此当前仍不能推出终端直接矛盾。

```text
b3_external_lane_imported=true
coupled_margin_schema_closed=true
concrete_parameter_table_present=false
prefix_numeric_lower_bound_present=false
finite_boundary_prefix_open=true
finite_boundary_hash_present=false
named_return_numeric_bound_present=false
cold_supply_numeric_bound_present=true
sparse_history_demand_exceeds_budget_proved=false
persistent_named_return_excluded=false
nonpersistent_named_return_excluded=false
coupled_positive_margin_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 必需字段

| field | present | meaning | needed_for |
| --- | --- | --- | --- |
| `parameter_id` | `false` | 同一组 z,D,Lambda,T_PDEC；禁止需求和供给分开调参。 | same-parameter discipline |
| `D0_prefix_lower_bound` | `false` | 由 B3 外部前沿和有限 prefix 证书给出的 D_prefix 统一显式下界。 | FiniteBoundaryPrefixRoughCountCertificate |
| `E0_named_return_deduction` | `false` | 命名回流扣除项；持久回流需进入 PDEC/CleanKLS，非持久回流进统一预算。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `U0_cold_supply_bound` | `true` | 非持久冷/稀疏历史供给的同参数显式上界。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget |
| `margin_delta` | `false` | 严格差值 D0-E0-U0>0，或失败时登记具体回流。 | FinitePrefixNamedReturnCoupledPositiveMarginLedger |
| `finite_boundary_hash` | `false` | 所有有限 P 边界的可复核证书 hash。 | FiniteBoundaryPrefixRoughCountCertificate |

## 2. 终端二分

| case | criterion | closed_as_logic | proved_for_current_corpus | consequence |
| --- | --- | --- | --- | --- |
| `positive margin` | D0(P,z)-E0(P,z)-U0(P,z)>0 | `true` | `false` | 非持久冷/SAE 供给无法支付反例链义务，得到终端供需矛盾。 |
| `nonpositive margin with persistent return` | E0_named contains persistent PDEC/ColumnCRT/FixedHistory/HotCore | `true` | `false` | 必须回流到 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve 或 DStructure/Rankin。 |
| `nonpositive margin with nonpersistent overload` | U0_cold too large or sparse history supply absorbs demand | `true` | `false` | 必须证明 SparseHistoryDemandExceedsNonpersistentSupplyBudget，或暴露 Lambda/阈值失败源。 |
| `finite boundary undecided` | finite prefix certificate missing | `false` | `false` | 不能把渐近 B3 余量推广成全局定理。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链内做终端供需比较，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| `CoupledMarginSchemaClosed` | `true` | `true` | 最后正余量账本的必需字段已完全列出。 | ConcreteSameParameterMarginTableCertificate |
| `B3ExternalLaneImported` | `true` | `false` | 外部 B3/Mertens 版可供给 D0 的解析尾段。 | finite boundary and same-parameter table |
| `ConcreteSameParameterTablePresent` | `false` | `false` | 当前还没有把 D0、E0、U0 写入同一可比较表。 | ConcreteSameParameterMarginTableCertificate |
| `FiniteBoundaryPrefixCertificatePresent` | `false` | `false` | 有限 P 边界仍未物化。 | FiniteBoundaryPrefixRoughCountCertificate |
| `NamedReturnNumericallyRegistered` | `false` | `false` | E_named 仍没有同参数上界或排斥证书。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ColdSupplyNumericDominanceRegistered` | `false` | `false` | U_cold 有公式，但尚未和 D0-E0 做严格数值反超。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget |
| `DirectTerminalContradictionReached` | `false` | `false` | 耦合账本尚未给出正余量或强制回流矛盾。 | ConcreteSameParameterMarginTableCertificate AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
ConcreteSameParameterMarginTableCertificate AND FiniteBoundaryPrefixRoughCountCertificate AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一步应直接生成 `ConcreteSameParameterMarginTableCertificate`：同一 `parameter_id` 下列出 `D0_prefix_lower_bound`、`E0_named_return_deduction`、`U0_cold_supply_bound`、`margin_delta` 和 `finite_boundary_hash`。若 `margin_delta>0`，进入终端供需矛盾；若不为正，失败行必须登记为持久 PDEC/CleanKLS、非持久 SAE 超供给、热核心或固定历史 PDEC。

审稿边界：本文件闭合耦合账本 schema，不闭合数值正余量。
