# Prime Matrix strict 统一预算严格不等式主攻路由器

**状态：** `unified_budget_strict_inequality_normal_form_closed_margin_inputs_open`

统一预算严格不等式已压成同参数单标量余量：D_prefix-E_named-U_cold>0。外部 B3/TV 路线可条件供给 prefix demand，但终端投影抗塌缩和冷供给 Lambda 平衡仍未闭合。当前最窄结构硬点是 PrefixLabelSupportToSparseTerminalHistoryAntiCollapse。

```text
same_parameter_budget_normal_form_closed=true
external_b3_prefix_demand_lane_available=true
strict_self_contained_prefix_demand_closed=false
terminal_projection_anticollapse_closed=false
cold_supply_lambda_balance_closed=false
unified_terminal_budget_strict_inequality_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 标准形

```text
D_prefix = ((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z)
L_forced >= D_prefix-E_named
U_cold <= sum_W (T_PDEC(W)-1)C_core(W)
terminal contradiction if D_prefix-E_named-U_cold > 0
```

| component | symbol | closed_part | open_part |
| --- | --- | --- | --- |
| `prefix demand` | D_prefix=((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z) | 统一方程和容量乘子归一化已闭合。 | PrefixDemandNumeratorSurplusLedger |
| `terminal projection` | L_forced >= D_prefix-E_named | no-loss 投影和命名回流字母表已闭合。 | PrefixLabelSupportToSparseTerminalHistoryAntiCollapse |
| `cold supply` | U_cold <= sum_W (T_PDEC(W)-1)C_core(W) | 非持久历史供给公式和冷/热分裂已闭合。 | ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance |
| `strict gap` | D_prefix-E_named-U_cold>0 | 代数组合已闭合，若该式成立即 L_forced>U_cold。 | FiniteBoundaryAndCommonParameterSynchronizationLedger |

## 2. 定理边界

| name | proved | statement | role |
| --- | --- | --- | --- |
| `UnifiedBudgetNormalFormTheorem` | `true` | 早期零行反例链的终端预算严格矛盾等价于同参数正余量 D_prefix-E_named-U_cold>0。 | 把统一预算从口头供需矛盾改写为单一标量不等式。 |
| `ExternalB3PrefixDemandLane` | `false` | 若接受外部 Mertens/Dusart 输入，prefix demand 的 B3/TV 部分可条件进入该标量式；严格自足版仍需内联 Mertens 尾段。 | 区分外部条件路线与严格自足路线。 |
| `UnconditionalUnifiedBudgetGap` | `false` | 要证明 UnifiedTerminalBudgetStrictInequality，还必须补齐 PrefixLabelSupportToSparseTerminalHistoryAntiCollapse、ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance 与 FiniteBoundaryAndCommonParameterSynchronizationLedger。 | 这是当前终端矛盾的真剩余输入基。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 统一预算只在假设早期零行反例链内比较需求与供给。 | 无。 |
| `SameParameterNormalFormClosed` | `true` | `true` | 同一 z、D、Lambda schedule、PDEC 阈值下的预算标准形已固定为 D_prefix-E_named-U_cold>0。 | UnifiedTerminalBudgetStrictInequality |
| `PrefixDemandExternalLaneAvailable` | `true` | `false` | 接受外部 Mertens/Dusart 时，B3 TV 项可条件关闭；严格自足仍缺 Mertens 尾段。 | SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 |
| `TerminalProjectionAntiCollapseClosed` | `false` | `false` | 当前仍需证明 prefix 标签支撑不会在 sparse terminal history 投影下大量塌缩。 | PrefixLabelSupportToSparseTerminalHistoryAntiCollapse |
| `ColdSupplyLambdaBalanceClosed` | `false` | `false` | 当前仍需给出冷核心阈值、历史数和 Lambda schedule 的同参数反超。 | ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance |
| `UnifiedBudgetStrictInequalityProved` | `false` | `false` | 需求下界、投影抗塌缩、命名扣除和冷供给上界尚未合成正余量。 | PrefixLabelSupportToSparseTerminalHistoryAntiCollapse AND ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance AND FiniteBoundaryAndCommonParameterSynchronizationLedger |

## 4. 下一真正最窄点

首攻：

```text
PrefixLabelSupportToSparseTerminalHistoryAntiCollapse
```

并行：

```text
ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance AND FiniteBoundaryAndCommonParameterSynchronizationLedger AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件闭合统一预算的同参数标准形；尚未证明正余量，因此不能声明行/列命题无条件闭合。
