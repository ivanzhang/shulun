# Prime Matrix strict 命名回流排斥压缩路由器

**状态：** `named_return_exclusion_compressed_persistent_or_budget_open`

命名回流排斥已被压缩：命名出口字母表本身不再是数学硬点。持久回流接回全局 PDEC-CAP/内部 CleanKLS 终端包；非持久回流接入统一终端预算严格不等式。因此下一步最适合直接攻有不等式形态的 UnifiedTerminalBudgetStrictInequality。

```text
named_return_compression_closed=true
persistent_named_return_reduced_to_global_terminal=true
nonpersistent_named_return_reduced_to_unified_budget=true
hot_core_fixed_history_absorbed=true
persistent_named_return_excluded=false
nonpersistent_named_return_excluded=false
named_return_exclusion_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 压缩表

| return_type | persistence | compression | meaning |
| --- | --- | --- | --- |
| `PDEC / ColumnCRT` | persistent finite signature or fixed displacement | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve | 持久相位/列位移缺陷不再作为单独终端，而是进入全局 PDEC-CAP 或 clean KLS/DLS 终端包。 |
| `SAE / isolated endpoint` | nonpersistent sparse packet | UnifiedTerminalBudgetStrictInequality | 孤立或不持久坏窗只能消耗有限 SAE 供给；是否矛盾由统一预算严格不等式判定。 |
| `HotCore` | terminal core divisor window over threshold | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR UnifiedTerminalBudgetStrictInequality | 热核心若持久就是 PDEC/ColumnCRT，若不持久则进入冷/热预算，不允许作为自由容量保留。 |
| `FixedHistory` | same sparse history word above threshold | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve | 固定历史持久复现就是有限签名 PDEC/ColumnCRT；未持久则已在 sparse SAE 预算中计数。 |
| `Rankin / finite core` | promotion or finite ledger return | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance | 最终 DStructure/Rankin 晋级门仍是独立验收，不由本命名回流压缩自动关闭。 |

## 2. 定理边界

| name | proved | statement | role |
| --- | --- | --- | --- |
| `NamedReturnCompressionTheorem` | `true` | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion 不是新的单体数学估计；它等价压缩为持久命名回流的 PersistentNamedReturnGlobalTerminalExclusion 与非持久命名回流的 NonpersistentNamedReturnUnifiedBudgetContradiction。 | 删除命名出口字母表自身作为硬点的歧义。 |
| `PersistentReturnReduction` | `true` | 持久 PDEC/ColumnCRT/FixedHistory/HotCore 回流必须进入 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve 或 DStructure/Rankin 晋级门。 | 把持久缺陷接回既有全局终端家族，而不是生成新分支。 |
| `NonpersistentReturnReduction` | `true` | 非持久 SAE/sparse/hot-core 供给必须进入 UnifiedTerminalBudgetStrictInequality 的供需比较。 | 把孤立缺陷转成可攻的终端预算不等式。 |
| `NamedReturnExclusionUnconditional` | `false` | 完整排斥命名回流仍需证明 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve 与 UnifiedTerminalBudgetStrictInequality，并处理 DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。 | 这是仍未闭合的全局排斥边界。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍只在假设早期零行反例链内压缩命名回流，不使用真实缺席样本。 | 无。 |
| `NoLossNamedReturnAlphabetImported` | `true` | `true` | no-loss 账本保证所有失败对象都保留为命名 return 记录，不能消失。 | 终端排斥仍未证明。 |
| `NamedReturnCompressionClosed` | `true` | `true` | 命名回流字母表已压成持久全局终端包与非持久统一预算二分。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND UnifiedTerminalBudgetStrictInequality |
| `PersistentNamedReturnExcluded` | `false` | `false` | 持久 PDEC/ColumnCRT/FixedHistory 仍需全局 PDEC-CAP 或内部 CleanKLS/DLS 证明。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| `NonpersistentNamedReturnExcluded` | `false` | `false` | 非持久 sparse/SAE/hot-core 仍需统一终端预算严格反超。 | UnifiedTerminalBudgetStrictInequality |
| `NamedReturnExclusionProved` | `false` | `false` | 命名回流已不再是模糊目标，但其两个压缩后的真输入尚未全部完成。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND UnifiedTerminalBudgetStrictInequality AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一真正最窄点

首攻：

```text
UnifiedTerminalBudgetStrictInequality
```

并行：

```text
PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
```

独立晋级门：

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件只删除命名回流字母表的歧义；它没有证明全局 PDEC/CleanKLS，也没有证明统一预算严格不等式。
