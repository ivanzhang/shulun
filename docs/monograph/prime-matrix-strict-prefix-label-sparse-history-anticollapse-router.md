# Prime Matrix strict prefix 标签到稀疏终端历史抗塌缩路由器

**状态：** `prefix_label_sparse_history_no_silent_collapse_closed_strong_injection_unneeded_budget_gap_open`

PrefixLabelSupportToSparseTerminalHistoryAntiCollapse 的强注入版本并非统一预算所必需。在早期零行反例链内，每个 prefix 加权 atom 要么投影到某个稀疏终端历史并按重数计入 L_forced，要么进入 PDEC、SAE、ColumnCRT、固定历史、热核心或 quotient 的命名回流桶。因此同一历史词上的塌缩不是负载消失，而是进入冷核心供给预算或命名回流。本步关闭的是终端预算所需的无静默塌缩抗塌缩；最终无条件矛盾仍需冷供给平衡、命名回流排斥、有限参数同步和 prefix 需求下界。

```text
weighted_prefix_atom_domain_imported=true
terminal_map_no_loss_imported=true
strong_distinct_sparse_history_injection_proved=false
strong_distinct_sparse_history_injection_needed_for_unified_budget=false
multiplicity_conservation_anticollapse_closed=true
persistent_collapse_routed_to_named_return=true
nonpersistent_collapse_absorbed_by_cold_budget=true
prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget=true
terminal_projection_anticollapse_closed=true
unified_terminal_budget_strict_inequality_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 关键重写

强注入命题

```text
#distinct sparse terminal histories >= M#_{x,z}
```

不是统一预算真正需要的命题。统一预算只需要负载守恒：

```text
L_forced = sum_W Load(W) >= M#_{x,z}-E_named.
```

若多个 prefix 标签落到同一个历史词 `W`，它们构成 `Load(W)` 的多重负载；这只会增加该历史词要支付的冷核心容量，而不会把需求消掉。

## 2. 塌缩分支

| case | formula | route | status | meaning |
| --- | --- | --- | --- | --- |
| `injective_or_low_collision` | sum_W Load(W)=M#_{x,z}-E_named | terminal multiplicity ledger | `closed` | 不同 prefix atom 即使落到同一历史词，也按终端重数计入负载，而不是消失。 |
| `bounded_nonpersistent_collision` | Load(W)<=C_cold(W)(T_PDEC(W)-1) | ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance | `open_budget` | 非持久塌缩可由冷核心/历史重数供给预算支付；剩余是不等式反超。 |
| `persistent_same_history_collision` | Load(W)>C_cold(W)(T_PDEC(W)-1) | FixedHistoryPDECOrHotCoreNamedReturn | `registered_named_return` | 同一历史词过阈值持久复现不是自由出口，必须登记为 PDEC、ColumnCRT、固定历史或热核心回流。 |
| `quotient_or_phase_drift` | terminal map undefined or changes phase key | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion | `registered_named_return` | 若投影无法稳定落到终端历史，则由 no-loss 账本进入命名回流桶。 |

## 3. 定理边界

| name | proved | statement | role |
| --- | --- | --- | --- |
| `NoSilentCollapseTerminalMultiplicityLedger` | `true` | 在早期零行反例链内，prefix 加权义务投影到稀疏终端时不会静默损失；未命名回流的部分按终端历史重数守恒。 | 把抗塌缩从强互异历史注入改成统一预算真正需要的重数守恒。 |
| `StrongDistinctSparseHistoryInjection` | `false` | 当前不证明 #distinct sparse histories >= M#_{x,z}。 | 这是过强命题；同一历史多重命中应由容量预算处理。 |
| `TerminalProjectionAntiCollapseForUnifiedBudget` | `true` | 统一预算中需要的是 L_forced>=M#_{x,z}-E_named；同历史塌缩只会进入 U_cold 或 E_named，不会削弱该负载守恒。 | 关闭 PrefixLabelSupportToSparseTerminalHistoryAntiCollapse 的无静默塌缩版本。 |
| `UnconditionalTerminalContradiction` | `false` | 仍需证明 M# 下界、命名回流排斥、冷供给上界与有限参数同步后得到 D_prefix-E_named-U_cold>0。 | 行/列命题仍不能升级为作者侧无条件闭合。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步只在假设早期零行反例链内工作，不用真实零行缺席或统计样本。 | 保持 row_column_unconditional_closed=false。 |
| `WeightedPrefixAtomDomainImported` | `true` | `true` | prefix 残洞 atom、canonical tau_z 标签与 1/mu_tau 容量权重已由前置路由闭合。 | 无。 |
| `TerminalMapNoLossImported` | `true` | `true` | 每个 atom 的出口只能是稀疏终端历史、固定历史、PDEC/SAE/ColumnCRT、热核心或 quotient 回流。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `StrongDistinctHistoryInjectionRejectedAsUnneeded` | `true` | `true` | 统一预算不需要互异历史词注入；同一历史词的多重命中正是终端负载。 | StrongDistinctSparseHistoryInjectionAntiCollapse |
| `MultiplicityConservationAntiCollapseClosed` | `true` | `true` | 按终端历史分组后，总负载等于 prefix 加权质量扣除命名回流。 | PrefixLabelSupportToSparseTerminalMultiplicityNoSilentCollapse |
| `PersistentCollapseRoutedToNamedReturn` | `true` | `false` | 若同一历史词过阈值持久复现，它必须进入固定历史/PDEC/热核心命名桶。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `NonpersistentCollapseAbsorbedByColdBudget` | `true` | `false` | 若所有同历史塌缩均未持久，则总量由冷核心历史重数预算吸收。 | ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance |
| `PrefixLabelSupportToSparseTerminalHistoryAntiCollapseClosedForBudget` | `true` | `true` | 对统一预算所需的投影负载而言，prefix 标签支撑不会塌缩成无负载。 | 强互异历史注入未证但不再是必要输入。 |
| `UnifiedBudgetStrictInequalityProved` | `false` | `false` | 抗塌缩已转成重数守恒，但仍缺冷供给平衡、有限参数同步、命名回流排斥与自足 B3 尾段。 | ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance AND FiniteBoundaryAndCommonParameterSynchronizationLedger AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |

## 5. 下一真正最窄点

首攻：

```text
ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance
```

并行保留：

```text
FiniteBoundaryAndCommonParameterSynchronizationLedger AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND NormalizedPrefixResidualPotentialLowerBound AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件关闭的是统一预算所需的无静默塌缩/重数守恒版本；它没有证明强互异历史注入，也没有证明最终正余量。
