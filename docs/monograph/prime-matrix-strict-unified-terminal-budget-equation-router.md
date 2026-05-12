# Prime Matrix strict 统一终端预算方程路由器

**状态：** `unified_terminal_budget_equation_built_strict_gap_open`

统一终端预算方程已经建立：在早期零行反例链内，prefix 粗筛余质量经容量乘子转成 M#，M# 经终端投影守恒转成 L_forced，冷核心历史给出 U_cold 上界。因此最终矛盾只需证明一个严格不等式：((P-1)W^- - TV)/ceil(P/z) - E_named > sum_W (T_PDEC(W)-1)C_core(W)。该式失败时，失败源只能落入 B3/TV/有限证书、终端抗塌缩/命名回流、冷供给/Lambda 平衡三组输入。

```text
algebraic_composition_closed=true
prefix_rough_lower_reduction_imported=true
capacity_multiplier_normalization_imported=true
terminal_projection_balance_imported=true
cold_core_supply_bound_imported=true
unified_terminal_budget_strict_inequality_proved=false
b3_prefix_mass_inputs_proved=false
terminal_projection_inputs_proved=false
cold_supply_parameter_inputs_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 统一方程

```text
|R_{x,z}| >= (P-1)W^-(z,D)-TV(lambda^-)
M#_{x,z} >= |R_{x,z}|/ceil(P/z)
L_forced >= M#_{x,z}-E_named
U_cold <= sum_W (T_PDEC(W)-1)C_core(W)
```

合成得到终局预算判据：

```text
((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z)
    - E_named
  > sum_W (T_PDEC(W)-1)C_core(W)
```

若该不等式成立，则 `L_forced>U_cold`，非持久冷核心供给无法支付早期零行反例链。

## 2. 方程表

| name | formula | status | depends_on |
| --- | --- | --- | --- |
| `prefix_rough_lower_bound` | \|R_{x,z}\| >= (P-1)W^-(z,D)-TV(lambda^-). | `closed_as_reduction` | B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND B3RemainderTotalVariationBudgetForLengthP AND FiniteBoundaryPrefixRoughCountCertificate |
| `capacity_multiplier_normalization` | M#_{x,z} >= \|R_{x,z}\|/ceil(P/z). | `closed` | RegisteredPrefixCapacityMultiplierDiscipline |
| `terminal_projection_balance` | L_forced >= M#_{x,z}-E_named. | `closed_as_no_loss_or_named_return` | PrefixLabelSupportToSparseTerminalHistoryAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `cold_core_supply_bound` | U_cold <= sum_W (T_PDEC(W)-1)C_core(W). | `closed_as_upper_bound` | ColdCoreNonpersistentSupplyUpperBound AND AdaptiveLambdaBalanceForIteratedCoreDensity |
| `unified_terminal_budget_gap` | ((P-1)W^- - TV)/ceil(P/z) - E_named > sum_W (T_PDEC(W)-1)C_core(W). | `open_strict_inequality` | UnifiedTerminalBudgetStrictInequality |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 统一方程只在假设早期零行反例链内使用，不借真实缺席样本。 | 保持 row_column_unconditional_closed=false。 |
| `AlgebraicCompositionClosed` | `true` | `true` | 粗筛余、容量乘子、终端负载、冷供给四段不等式可以无损合成为一个终端预算缺口。 | UnifiedTerminalBudgetStrictInequality |
| `B3PrefixMassInputsOpen` | `false` | `false` | prefix 残洞质量仍依赖 B3 主项、TV 预算和有限边界证书。 | B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND B3RemainderTotalVariationBudgetForLengthP AND FiniteBoundaryPrefixRoughCountCertificate |
| `TerminalProjectionInputsOpen` | `false` | `false` | 终端投影仍需抗塌缩和命名回流排斥，不能把加权质量直接当作终端实例数。 | PrefixLabelSupportToSparseTerminalHistoryAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ColdSupplyParameterInputsOpen` | `false` | `false` | 冷供给上界的具体反超还需要 Lambda 平衡与核心阈值供给预算比较。 | ColdCoreNonpersistentSupplyUpperBound AND AdaptiveLambdaBalanceForIteratedCoreDensity |
| `UnifiedTerminalBudgetContradictionProved` | `false` | `false` | 尚未证明统一严格不等式，因此没有最终直接矛盾。 | UnifiedTerminalBudgetStrictInequality |

## 4. 下一最窄点

```text
B3RemainderTotalVariationBudgetForLengthP
```

并行保留：

```text
B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError AND FiniteBoundaryPrefixRoughCountCertificate AND PrefixLabelSupportToSparseTerminalHistoryAntiCollapse AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND ColdCoreNonpersistentSupplyUpperBound AND AdaptiveLambdaBalanceForIteratedCoreDensity
```

审稿边界：本步只完成统一终端预算方程的代数组合；尚未证明该严格不等式，不能升级为无条件闭合。
