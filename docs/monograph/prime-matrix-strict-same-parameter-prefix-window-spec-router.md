# Prime Matrix strict 同参数 prefix 窗口规格路由器

**状态：** `same_parameter_prefix_window_spec_closed_runner_tail_type_threshold_open`

`SameParameterPrefixWindowSpecification` 可按结构规格关闭：D0 的 prefix 粗筛余公式、M# 的容量归一化、终端预算方程、冷供给 Lambda/T_PDEC 纪律与 row-free type key 都已登记在同一个 alpha=0.43, P>=100000, z=floor(P^0.43) 窗口内。但这不生成 D0/E0/U0 数值，也不关闭 runner/hash、解析尾段桥、类型阈值或最终正余量。

```text
same_parameter_window_specification_proved=true
d0_msharp_terminal_same_z_d_lambda_alphabet_closed=true
same_parameter_numeric_margin_proved=false
runner_hash_ledger_proved=false
analytic_tail_bridge_proved=false
formal_unit_type_threshold_ledger_proved=false
finite_boundary_prefix_certificate_proved=false
row_column_unconditional_closed=false
```

## 1. Canonical Window

| field | value |
| --- | --- |
| `parameter_id` | alpha043_pge100000_external_b3_pending_finite_prefix_named_return |
| `P_range` | P>=100000 |
| `alpha` | 0.43 |
| `s` | 2.3255813953488373 |
| `z` | z=floor(P^0.43) |
| `prefix_interval` | 1<=c<P |
| `rough_set` | R_{x,z}={c: 1<=c<P and xP+c avoids all prescribed classes modulo q<=z} |
| `D_rule` | one lower-sieve level D with squarefree d<P in supp(lambda^-_{z,D}) |
| `lower_weight_family` | lambda^-_{z,D}, W^-(z,D), TV(lambda^-) |
| `capacity_label` | tau_z(c), mu_tau(c), M#_{x,z}=sum_{c in R_{x,z}}1/mu_tau(c) |
| `terminal_ledger` | D_prefix-E_named-U_cold under the same z,D,lambda^-,Lambda,T_PDEC ledger |
| `type_alphabet` | row-free type key uses the same source/window/phase/label skeleton; threshold comparison remains separate |

## 2. 同窗口对账

| slot | closed | proved | formula | remaining |
| --- | --- | --- | --- | --- |
| `parameter_window` | `true` | `true` | alpha043_pge100000_external_b3_pending_finite_prefix_named_return; P>=100000; z=floor(P^0.43); 1<=c<P | 无；该项只锁定窗口，不给 D0 数值。 |
| `D0_prefix_demand_formula` | `true` | `true` | \|R_{x,z}\| >= (P-1)W^-(z,D) - sum_{d in supp lambda^-}\|lambda_d^-\|. | B3 main/TV/finite certificate still open; this is formula alignment only. |
| `Msharp_capacity_window` | `true` | `true` | M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)}. | NormalizedPrefixResidualPotentialLowerBound remains numeric/open. |
| `D0_to_Msharp_budget_link` | `true` | `true` | M#_{x,z} >= \|R_{x,z}\|/ceil(P/z). | 需要粗筛余数值下界和 finite runner/hash。 |
| `terminal_budget_same_window` | `true` | `true` | ((P-1)W^- - TV)/ceil(P/z) - E_named > sum_W (T_PDEC(W)-1)C_core(W). | 严格正余量仍未证明。 |
| `Lambda_TPDEC_cold_supply_discipline` | `true` | `true` | U_cold<=sum_W (T_PDEC(W)-1)C_core(W), with the same Lambda schedule and PDEC threshold ledger | ColdPositiveDominance / UnifiedTerminalBudgetStrictInequality remains open. |
| `terminal_projection_no_silent_collapse` | `true` | `true` | L_forced>=M#_{x,z}-E_named | NamedReturn exclusion and cold budget comparison remain open. |
| `row_free_type_alphabet_key` | `true` | `true` | row-free type key: source family, branch, window shape, phase, anchor, carry/cofactor, label skeleton | FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse still require threshold/entropy and label-preserving anti-collapse. |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SameParameterWindowTargetImported` | `true` | `false` | 上一层已把 range manifest 后的首字段定为同参数窗口规格。 | SameParameterPrefixWindowSpecification |
| `D0MsharpTerminalSameWindowClosed` | `true` | `true` | D0 公式、M# 容量归一化、终端预算、Lambda/T_PDEC 与 row-free type key 已登记在同一窗口。 | numeric margin and finite prefix certificate are separate inputs. |
| `NoNumericPromotion` | `true` | `true` | 同参数窗口闭合不等于 D0/E0/U0 已数值化；candidate row 仍显式无效。 | ConcreteSameParameterMarginTableCertificate |
| `RunnerHashLedgerStillOpen` | `false` | `false` | 当前没有可复核 runner/hash 账本来支撑 finite prefix rough-count。 | ReproduciblePrefixRoughCountRunnerHashLedger |
| `AnalyticTailBridgeStillOpen` | `false` | `false` | tail object interface 已匹配，但从解析尾段到有限边界的单调桥仍未证明。 | AnalyticTailToFiniteBoundaryMonotoneBridge |
| `TypeThresholdStillOpen` | `false` | `false` | row-free type key 定义已闭合，但类型阈值/保标签商熵亏损仍未证明。 | FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse |

## 4. 下一最窄点

```text
ReproduciblePrefixRoughCountRunnerHashLedger
```

并行保留：

```text
FormalUnitTypeThresholdLedger AND PrefixLabelSupportToRowFreeTypeAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本步只关闭同参数窗口规格；没有生成 finite prefix runner/hash，没有证明解析尾段桥，也没有推出行/列命题无条件闭合。
