# Prime Matrix strict 冷核心非持久供给与 Lambda 平衡路由器

**状态：** `cold_core_nonpersistent_supply_balance_same_parameter_ledger_closed_positive_margin_open`

冷核心非持久供给侧的自由调参已经被锁入同一个终端预算余量。缩小 Lambda 或 PDEC 阈值会减少 U_cold，但会把更多质量推入命名回流；放大 Lambda 或阈值会减少回流，却增大历史字母表或单历史允许容量。因此冷供给平衡不再是独立黑箱，而是同参数标量 D_prefix-E_named-U_cold>0 的正余量问题。当前仍未证明该余量为正，所以无条件闭合仍未达成。

```text
terminal_no_silent_collapse_imported=true
cold_supply_upper_envelope_closed=true
same_parameter_lambda_schedule_closed=true
adaptive_lambda_no_free_lunch_dichotomy_closed=true
single_parameter_margin_ledger_closed=true
cold_core_nonpersistent_supply_upper_bound_and_adaptive_lambda_balance_proved=false
cold_supply_upper_bound_beats_load=false
unified_terminal_budget_strict_inequality_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 同参数余量

当前终端矛盾只允许在同一组参数下比较：

```text
D_prefix = ((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z)
U_cold  <= sum_W (T_PDEC(W)-1) C_core(W)
contradiction if D_prefix - E_named - U_cold > 0.
```

不能用一组参数放大 `D_prefix`，再用另一组参数缩小 `U_cold`。

## 2. 组件表

| component | formula | discipline | status |
| --- | --- | --- | --- |
| `demand` | D_prefix=((P-1)W^-(z,D)-TV(lambda^-))/ceil(P/z) | same z,D and same lower-weight convention | `open_margin_input` |
| `named deduction` | E_named=E_PDEC+E_SAE+E_ColumnCRT+E_hot+E_fixed+E_quotient | same return alphabet, no hidden exit | `registered_open` |
| `cold supply` | U_cold<=sum_W (T_PDEC(W)-1) C_core(W) | same Lambda schedule and same PDEC threshold | `upper_envelope_closed` |
| `strict margin` | D_prefix-E_named-U_cold>0 | all three terms evaluated under one parameter ledger | `open_positive_margin` |

## 3. 调参二分

| knob | gain | cost | no_free_lunch |
| --- | --- | --- | --- |
| `Lambda_i smaller` | history alphabet A_i<=8 Lambda_i^2 shrinks | more core windows cross hot threshold and enter E_named | cannot lower U_cold without increasing named-return obligations. |
| `Lambda_i larger` | fewer hot-core returns after coarser cold classification | history alphabet and U_cold grow at least through product A_i | cannot suppress E_named by moving mass into an unbounded cold budget. |
| `T_PDEC(W) larger` | fewer histories become persistent PDEC | nonpersistent allowance (T_PDEC(W)-1)C_core(W) grows | raising persistence threshold weakens the desired strict margin. |
| `T_PDEC(W) smaller` | cold supply allowance decreases | more histories become fixed-history PDEC or ColumnCRT named returns | the saved supply reappears as E_named unless that return is excluded. |

## 4. 定理边界

| name | proved | statement | role |
| --- | --- | --- | --- |
| `SameParameterColdSupplyLedger` | `true` | 冷供给、历史数、PDEC 阈值、命名扣除与 prefix demand 必须在同一 z,D,Lambda,T 账本下比较。 | 禁止用不同参数口径分别优化需求和供给。 |
| `AdaptiveLambdaNoFreeLunchDichotomy` | `true` | 调小 Lambda 或阈值会增加命名回流，调大 Lambda 或阈值会增加 U_cold；两类变化都必须进入同一个余量式。 | 把调参自由度转成显式预算守恒，而不是新出口。 |
| `ColdBalancePositiveMargin` | `false` | 尚未证明 D_prefix-E_named-U_cold>0。 | 这是反例链与真实链终端矛盾的剩余标量目标。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 本步仍只在早期零行反例链内比较终端需求与冷供给。 | 保持 row_column_unconditional_closed=false。 |
| `TerminalNoSilentCollapseImported` | `true` | `true` | prefix 标签投影到稀疏终端历史时按重数守恒，未投影部分进入命名回流。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ColdSupplyEnvelopeClosed` | `true` | `true` | 非持久冷供给可统一写成 sum_W (T_PDEC(W)-1)C_core(W)。 | ColdCoreNonpersistentSupplyUpperBoundAndAdaptiveLambdaBalance |
| `AdaptiveLambdaDisciplineClosed` | `true` | `true` | Lambda 与 PDEC 阈值调节不能作为自由优化，必须同步进入 E_named 或 U_cold。 | SingleParameterTerminalBudgetMarginLedger |
| `SingleParameterMarginLedgerClosed` | `true` | `false` | 终局矛盾已固定为同参数余量 D_prefix-E_named-U_cold>0。 | NormalizedPrefixResidualPotentialLowerBound AND FiniteBoundaryAndCommonParameterSynchronizationLedger AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ColdBalancePositiveMarginProved` | `false` | `false` | 当前仍未证明该余量严格为正。 | SingleParameterTerminalBudgetMarginLedger AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion |
| `UnifiedBudgetStrictInequalityProved` | `false` | `false` | 同参数纪律已闭合，但最终供需反超还缺正下界、命名回流排斥和有限同步。 | UnifiedTerminalBudgetStrictInequality |

## 6. 下一真正最窄点

首攻：

```text
SingleParameterTerminalBudgetMarginLedger
```

并行保留：

```text
NormalizedPrefixResidualPotentialLowerBound AND FiniteBoundaryAndCommonParameterSynchronizationLedger AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND SelfContainedDusartReciprocalPrimeProofAppendixXGe10372 AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件关闭冷供给与 Lambda 调参纪律；尚未证明统一预算正余量。
