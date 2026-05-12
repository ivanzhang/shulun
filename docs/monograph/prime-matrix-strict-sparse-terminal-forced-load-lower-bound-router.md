# Prime Matrix strict 稀疏终端强制负载下界路由器

**状态：** `forced_load_lower_bound_reduced_to_normalized_prefix_potential_terminal_anticollapse_named_return_exclusion_open`

早期零行强制负载下界已被压成一个守恒型不等式：prefix 残洞经容量乘子归一化后形成 M#_{x,z}，这些加权义务沿固定商型/历史递归要么进入 sparse terminal history，要么以 PDEC、SAE、ColumnCRT、热核心、固定历史或 quotient/reuse 的命名方式回流。因此 L_forced 至少等于 M# 扣除命名回流后的质量。真正未闭合的是 M# 的全局正下界、终端历史投影抗塌缩，以及命名回流排斥；这些完成后才能触发 L_forced>U_cold。

```text
prefix_weighted_source_imported=true
terminal_projection_no_loss_or_named_return_closed=true
forced_load_criterion_closed=true
budget_gap_composition_closed=true
unified_field_prefix_to_terminal_load_factor_registered=true
normalized_prefix_potential_lower_bound_proved=false
terminal_history_anticollapse_proved=false
named_return_exclusion_proved=false
sparse_terminal_forced_load_lower_bound_proved=false
forced_terminal_load_beats_cold_supply_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 负载守恒式

在假设早期零行存在时，prefix 残洞给出

```text
M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)}.
```

沿历史递归与终端投影，有无损账本

```text
M#_{x,z} <= L_terminal
          + E_PDEC + E_SAE + E_ColumnCRT
          + E_hot + E_fixed + E_quotient.
```

所以若命名回流都被排斥或被上游终端门吸收，则

```text
L_forced >= M#_{x,z}.
```

更一般地，可用

```text
L_forced >= M#_{x,z}-E_named.
```

与冷核心供给上界合成：

```text
M#_{x,z}-E_named > U_cold  ==>  L_forced > U_cold.
```

## 2. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `prefix_weighted_obligation_source` | Assume EarlyZeroRowWithinP.  M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)}. | `imported_closed` | 早期零行把 prefix 残洞转成容量归一化的加权义务。 |
| `terminal_projection_accounting` | M#_{x,z} <= L_terminal + E_PDEC + E_SAE + E_ColumnCRT + E_hot + E_fixed + E_quotient. | `closed_as_no_loss_accounting` | 义务沿历史递归进入终端；不能进入终端的质量必须以命名回流出现。 |
| `sparse_terminal_forced_load_criterion` | If all named returns vanish or are excluded, then L_forced >= M#_{x,z}. | `closed_criterion` | 这给出从早期零行到稀疏终端负载的精确条件下界。 |
| `budget_gap_composition` | If M#_{x,z}-E_named > U_cold, then L_forced > U_cold. | `closed_composition` | 把本轮负载下界直接接到冷核心供需矛盾口。 |
| `anticollapse_boundary` | Weighted mass does not yet imply enough distinct terminal history instances without anti-collapse. | `open_boundary_named` | 仍需防止 prefix 标签支撑在 sparse terminal history 投影下塌缩。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 所有结论都在假设早期零行反例链内推导，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| `PrefixWeightedSourceImported` | `true` | `true` | prefix 残洞选择子、容量乘子和 M# 加权义务已由前置路由闭合。 | NormalizedPrefixResidualPotentialLowerBound |
| `TerminalProjectionNoLossClosed` | `true` | `true` | 每个加权义务沿历史递归只有终端、热核心、固定历史、PDEC/SAE/ColumnCRT 或 quotient 回流几类出口。 | PrefixObligationToSparseTerminalHistoryProjectionNoLossOrNamedReturn |
| `ForcedLoadCriterionClosed` | `true` | `true` | 若命名回流被排斥，则 L_forced 至少为 M# 的未回流部分。 | NormalizedPrefixResidualPotentialLowerBound AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `TerminalHistoryAntiCollapseOpen` | `false` | `false` | 加权质量还不能自动变成足够多的不同 sparse terminal history 实例。 | PrefixLabelSupportToSparseTerminalHistoryAntiCollapse |
| `SparseTerminalForcedLoadLowerBoundProved` | `false` | `false` | 尚未证明 M# 足够大、命名回流可排斥、且终端历史投影不塌缩。 | NormalizedPrefixResidualPotentialLowerBound AND PrefixLabelSupportToSparseTerminalHistoryAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ColdCoreBudgetContradictionReached` | `false` | `false` | 尚未得到 L_forced>U_cold，因此冷核心供需矛盾尚未最终触发。 | ForcedTerminalLoadBeatsColdCoreNonpersistentSupply |
| `UnifiedFieldFactorRegistered` | `true` | `false` | prefix 到终端负载的无损/回流因子已接入统一矛盾场，但还不是终局矛盾。 | UnifiedContradictionFieldPrefixToTerminalLoadFactor |

## 4. 下一最窄点

```text
NormalizedPrefixResidualPotentialLowerBound
```

并行保留：

```text
PrefixLabelSupportToSparseTerminalHistoryAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND ForcedTerminalLoadBeatsColdCoreNonpersistentSupply AND UnifiedContradictionFieldPrefixToTerminalLoadFactor
```

审稿边界：本步闭合 prefix 加权义务到 sparse terminal load 的无损/命名回流账本；尚未证明归一化 prefix 势足够大、终端历史投影抗塌缩或命名回流全部可排斥。
