# Prime Matrix strict 稀疏终端历史 SAE 预算比较路由器

**状态：** `sparse_terminal_history_sae_budget_formula_closed_gap_open`

稀疏终端 SAE 预算公式已经闭合。若没有任何历史词 W 持久复现进入 PDEC，则总稀疏供给满足 U_sparse <= sum_W (T_PDEC(W)-1) Cap(W)。历史词数量由有限深度和有限字母表控制；单历史容量交给 formal-unit 重数上界。因此稀疏终端分支只剩一个明确供需不等式：证明早期零行强制负载 L_forced 严格超过非持久历史供给预算，或排斥持久历史 PDEC。

```text
nonpersistent_sae_budget_formula_closed=true
history_count_inserted=true
forced_load_comparison_criterion_closed=true
sparse_terminal_pdec_or_budget_gap_closed=true
sparse_history_demand_exceeds_budget_proved=false
forced_load_lower_bound_proved=false
formal_unit_sparse_history_multiplicity_cap_proved=false
fixed_type_history_pdec_excluded=false
sparse_terminal_history_sae_budget_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 非持久 SAE 供给

若所有历史词 `W` 都未达到 PDEC 持久阈值，则

```text
U_sparse <= sum_W (T_PDEC(W)-1) Cap(W).
```

历史词集合满足

```text
#W <= sum_{r<=R} prod_{i<=r} A_{Lambda_i},
A_{Lambda_i} <= 8 Lambda_i^2.
```

所以当前缺口不是“稀疏终端是什么”，而是供给预算是否小于早期零行强制负载。

## 2. 供需矛盾口

若能证明

```text
L_forced > sum_W (T_PDEC(W)-1) Cap(W),
```

则非持久 SAE 分支无法支付早期零行反例链的终端义务；若同一历史持久化，则进入 PDEC/ColumnCRT。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `nonpersistent_budget_formula` | If no history W is persistent, U_sparse <= sum_W (T_PDEC(W)-1) Cap(W). | `closed` | 非持久稀疏历史的总供给上界已写成显式求和。 |
| `history_count_inserted` | sum_W may be bounded by sum_{r<=R} prod_{i<=r} A_{Lambda_i}, A_{Lambda_i}<=8Lambda_i^2. | `closed` | 历史词数量上界已接入 SAE 预算。 |
| `single_history_capacity_slot` | Cap(W) is controlled by formal-unit multiplicity and the terminal core interval for h/D(W). | `registered_input` | 单历史容量不再无名，交给 FormalUnitSparseHistoryMultiplicityCap。 |
| `forced_load_comparison` | If L_forced > U_sparse, then nonpersistent SAE supply cannot pay the early-zero-row obligation. | `closed_criterion` | 供给小于需求时直接形成反例链矛盾。 |
| `pdec_or_budget_gap` | Every sparse terminal packet is either persistent PDEC or must satisfy L_forced <= U_sparse. | `closed_dichotomy` | 稀疏终端不再是开放黑箱，只剩 PDEC 排斥或预算缺口。 |
| `budget_gap_input` | Prove L_forced > sum_W (T_PDEC(W)-1) Cap(W) after choosing Lambda schedule. | `open_input` | 最新最窄硬点是需求下界与非持久供给上界的显式比较。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的稀疏终端历史 SAE 分支内。 | 保持 row_column_unconditional_closed=false。 |
| `NonpersistentSAEBudgetFormulaClosed` | `true` | `true` | 若无持久历史 PDEC，总供给由历史求和上界控制。 | FormalUnitSparseHistoryMultiplicityCap |
| `ForcedLoadComparisonCriterionClosed` | `true` | `true` | `L_forced>U_sparse` 时得到供给-需求矛盾。 | SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow |
| `SparseTerminalPDECOrBudgetGapClosed` | `true` | `true` | 稀疏终端历史只剩持久 PDEC 或非持久预算比较。 | FixedTypeHistoryPDECExclusion OR SparseHistoryDemandExceedsNonpersistentSupplyBudget |
| `SparseHistoryDemandExceedsBudgetProved` | `false` | `false` | 尚未证明早期零行强制负载严格超过非持久历史供给预算。 | SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND FormalUnitSparseHistoryMultiplicityCap AND AdaptiveLambdaBalanceForIteratedCoreDensity |
| `SparseTerminalHistorySAEBudgetProved` | `false` | `false` | 预算公式闭合，但关键不等式和固定历史 PDEC 排斥尚未完成。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND FixedTypeHistoryPDECExclusion |

## 5. 下一步最窄点

```text
SparseHistoryDemandExceedsNonpersistentSupplyBudget
```

并行输入：

```text
SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND FormalUnitSparseHistoryMultiplicityCap AND AdaptiveLambdaBalanceForIteratedCoreDensity AND FixedTypeHistoryPDECExclusion
```

审稿边界：本步闭合 SAE 预算公式和供需判据；未证明需求大于供给，也未排斥固定历史 PDEC。
