# Prime Matrix strict 冷核心阈值预算缺口路由器

**状态：** `cold_core_budget_gap_reduced_to_forced_load_vs_nonpersistent_supply_open`

冷核心预算缺口已经压成单一供需不等式。非持久冷历史的总供给 U_cold 至多为 sum_W (T_PDEC(W)-1) C_core(W)，历史数由有限深度和 有限字母表控制。若早期零行反例链强制终端负载 L_forced 大于 U_cold，则非持久冷供给无法支付反例义务，形成直接矛盾。若该不等式失败，失败原因只能是需求下界不足、冷供给预算过大、热核心回流或固定历史 PDEC。

```text
cold_supply_upper_bound_closed=true
history_sum_envelope_closed=true
cold_budget_contradiction_criterion_closed=true
failure_reasons_named=true
unified_field_terminal_history_factor_registered=true
cold_core_threshold_budget_gap_proved=false
forced_load_lower_bound_proved=false
cold_supply_upper_bound_beats_load=false
terminal_core_hot_divisor_window_excluded=false
fixed_type_history_pdec_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 供给上界

非持久冷历史供给满足

```text
U_cold <= sum_W (T_PDEC(W)-1) C_core(W).
```

历史词数量由

```text
#W <= sum_{r<=R} prod_{i<=r} A_{Lambda_i},
A_{Lambda_i} <= 8 Lambda_i^2
```

控制。

## 2. 供需矛盾口

当前最窄矛盾判据是

```text
L_forced > U_cold.
```

若成立，早期零行反例链要求的终端义务超过所有非持久冷历史可提供的供给。

## 3. 引理表

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `cold_supply_upper_bound` | U_cold <= sum_{W cold} (T_PDEC(W)-1) C_core(W). | `closed` | 冷核心非持久供给有显式上界。 |
| `history_sum_envelope` | sum_{W cold} <= sum_{r<=R} prod_{i<=r} A_{Lambda_i}, with A_{Lambda_i}<=8Lambda_i^2. | `closed` | 历史词计数已进入供给预算。 |
| `cold_budget_contradiction_criterion` | If L_forced > U_cold, then early-zero-row terminal obligations exceed all nonpersistent cold supply. | `closed_criterion` | 这是当前最直接的供需矛盾口。 |
| `not_gap_then_named_escape` | If the gap fails, then either L_forced is too small, cold supply is too large, or hot/PDEC escape occurred. | `closed_dichotomy` | 预算未反超时，失败原因也被命名，不允许成为自由缺口。 |
| `cold_supply_too_large_route` | Large U_cold must come from large history count, large C_core(W), or large T_PDEC(W). | `closed_reduction` | 供给过大被拆成 Lambda、核心阈值、持久阈值三类具体输入。 |
| `terminal_history_supply_demand_field` | Early zero row forces demand; cold sparse histories provide finite supply; hot histories return to PDEC/LCM. | `registered_unified_field` | 该供需结构已作为新矛盾因子接入统一矛盾场。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 仍在早期零行反例链的冷核心 SAE 预算分支内。 | 保持 row_column_unconditional_closed=false。 |
| `ColdSupplyUpperBoundClosed` | `true` | `true` | 非持久冷历史供给 `U_cold` 已有显式求和上界。 | ColdCoreNonpersistentSupplyUpperBound |
| `SupplyDemandContradictionCriterionClosed` | `true` | `true` | `L_forced>U_cold` 时形成反例链供需矛盾。 | SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow |
| `FailureReasonsNamed` | `true` | `true` | 预算未反超时只能归因于需求弱、冷供给大、热核心或持久 PDEC。 | SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow OR ColdCoreNonpersistentSupplyUpperBound OR TerminalCoreHotDivisorWindowPDECorSAE OR FixedTypeHistoryPDECExclusion |
| `ColdCoreBudgetGapProved` | `false` | `false` | 尚未证明 `L_forced` 严格超过 `U_cold`。 | SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND ColdCoreNonpersistentSupplyUpperBound AND AdaptiveLambdaBalanceForIteratedCoreDensity |
| `UnifiedFieldUpdatedButNotClosed` | `true` | `false` | 新供需因子已进入统一矛盾场，但尚未产生最终直接矛盾。 | UnifiedContradictionFieldTerminalHistorySupplyDemandUpdate |

## 5. 下一步最窄点

```text
SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow
```

并列供给侧目标：

```text
ColdCoreNonpersistentSupplyUpperBound
```

并行保留：

```text
AdaptiveLambdaBalanceForIteratedCoreDensity AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND UnifiedContradictionFieldTerminalHistorySupplyDemandUpdate
```

审稿边界：本步闭合冷核心预算公式和供需判据；未证明需求反超供给，也未排斥热核心或固定历史 PDEC。
