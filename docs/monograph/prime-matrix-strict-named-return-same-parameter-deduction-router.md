# Prime Matrix strict 命名回流同参数扣除表路由器

**状态：** `named_return_same_parameter_schema_closed_numeric_table_open`

`NamedReturnSameParameterDeductionTable` 已被直接展开。它不是一个可凭空填写的常数表；在同一 parameter_id 下，持久命名回流只有在 strict acyclic terminal family 被排斥后才能记为 0，非持久命名回流只有在 SparseHistoryDemandExceedsNonpersistentSupplyBudget 与冷供给同参数上界闭合后才可由 U_cold 吸收。因此本步关闭的是 E_named 的表结构和收费纪律，不是数值表。下一最窄数学主攻点转为同一坏窗集合上的 DirectAcyclicSameSetPDECCapDualCertificate；并行保留 canonical-lock、direct clean KLS、SAE budget、finite prefix 和 DStructure/Rankin。

```text
parameter_id=alpha043_pge100000_external_b3_pending_finite_prefix_named_return
named_return_same_parameter_schema_closed=true
persistent_named_return_numeric_zero_available=false
nonpersistent_named_return_absorbed_by_budget=false
named_return_same_parameter_deduction_table_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. E_named 分量表

| component | same_parameter_rule | current_value | numeric_available | remaining |
| --- | --- | --- | --- | --- |
| `E_persistent` | persistent PDEC/ColumnCRT/FixedHistory/HotCore must be excluded in the same terminal scope | 0 only after strict terminal family is proved; otherwise branch returns | `false` | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `E_nonpersistent` | nonpersistent SAE/sparse/hot-core is not a separate E0 term after it is counted in U_cold | absorbed by U_cold only after sparse budget gap is proved | `false` | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND ColdSupplySameParameterNumericEnvelope |
| `E_floor_charge` | sawtooth/near-square failure uses the same formal-unit terminal alphabet | inherits E_persistent or E_nonpersistent according to persistence | `false` | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily OR SparseHistoryDemandExceedsNonpersistentSupplyBudget |
| `E_finite_boundary` | finite prefix undecided is not an E0 deduction; it blocks D0 directly | not counted in E_named | `false` | FiniteBoundaryPrefixRoughCountCertificate |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍只在早期零行反例链内整理命名回流扣除，不使用真实缺席样本。 | 保持 row_column_unconditional_closed=false。 |
| `TerminalChargeImported` | `true` | `true` | Rosser floor/sawtooth 失败态已被强制登记为命名终端收费。 | NamedReturnSameParameterDeductionTable |
| `NamedReturnAlphabetCompressed` | `true` | `true` | 命名回流字母表已压成持久全局终端与非持久统一预算二分。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND SparseHistoryDemandExceedsNonpersistentSupplyBudget |
| `SameParameterDeductionSchemaClosed` | `true` | `false` | 同一 parameter_id 下的 E_named 只能由持久终端排斥和非持久预算吸收两类规则生成。 | schema closed; numeric fields open. |
| `PersistentNamedReturnNumericZero` | `false` | `false` | 只有 strict 终端家族排斥后，持久命名回流才能在 E0 表中记为 0。 | AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn |
| `NonpersistentNamedReturnAbsorbedByBudget` | `false` | `false` | 只有非持久 SAE/cold budget 被证明反超，非持久回流才可由 U_cold 吸收。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND ColdSupplySameParameterNumericEnvelope |
| `NamedReturnSameParameterDeductionTableProved` | `false` | `false` | 同参数扣除表 schema 已闭合，但数值表仍未生成。 | (AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn) AND SparseHistoryDemandExceedsNonpersistentSupplyBudget |
| `DirectTerminalContradictionReached` | `false` | `false` | 仍未形成 D0-E0-U0>0 与 DStructure/Rankin 同时闭合的终端矛盾。 | FiniteBoundaryPrefixRoughCountCertificate AND (PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily OR NamedReturnSameParameterDeductionTable) AND ColdSupplySameParameterNumericEnvelope AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一真正最窄点

首攻：

```text
DirectAcyclicSameSetPDECCapDualCertificate
```

并行保留：

```text
AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn OR SparseHistoryDemandExceedsNonpersistentSupplyBudget OR ColdSupplySameParameterNumericEnvelope OR FiniteBoundaryPrefixRoughCountCertificate OR DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只关闭同参数 E_named 的结构表；它没有证明持久终端排斥、非持久预算反超或行/列命题无条件闭合。
