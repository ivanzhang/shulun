# Prime Matrix strict 终端缺陷耗尽路由器

**状态：** `terminal_defect_no_free_exit_closed_unconditional_exclusion_open`

本次硬攻关闭的是“缺陷是否还有自由逃逸”这一层：容量失败后的强 TV/端点缺陷，沿现有真实结构链必进入低模、dyadic Fourier、共同核、固定历史、SAE 或冷核心预算，不存在未命名第四出口。但这不是无条件排斥缺陷；真正剩余压成命名回流排斥与统一终端预算严格不等式。

```text
terminal_defect_no_free_exit_closed=true
alpha_prefix_tv_endpoint_defect_exhausted_to_named_exits=true
conditional_terminal_contradiction_after_exhaustion_closed=true
named_return_exclusion_proved=false
unified_terminal_budget_strict_inequality_proved=false
alpha_prefix_tv_or_pdec_defect_excluded=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 缺陷耗尽链

| layer | input | forced | exit | status |
| --- | --- | --- | --- | --- |
| `capacity failure` | No alpha-capacity surplus under EarlyZeroRowWithinP | TV_alpha >= (P-1)W^-_alpha-2(pi(P)-pi(alpha P)) | signed endpoint defect | `closed` |
| `signed endpoint` | E_alpha<=-G_alpha | low / dyadic / far-tail split; middle mass gives dyadic PDEC certificate | LowMod OR DyadicEndpointPDEC OR FarTailCore/SAE | `closed_as_split` |
| `dyadic endpoint` | positive endpoint hit deficit or negative hit surplus | centered zero-mean CRT test function and nonzero Fourier energy | Fourier/PDEC or isolated SAE | `closed_as_inputization` |
| `Fourier upper` | large nonzero endpoint spectrum | low effective modulus, large-effective geometric decay, or Bohr-cap large spectrum | LowEffectiveMod PDEC/ColumnCRT OR decay budget OR Bohr-cap PDEC | `closed_as_three_way_route` |
| `low effective modulus` | many active d with small d/gcd(h,d) | weighted reciprocal common-divisor envelope and hot short divisor window | short-window divisor density | `closed_as_reduction` |
| `short divisor window` | many g in (Y,2Y] divide the same frequency h | LCM explosion or low-multiplier common-kernel recurrence | ColumnCRT/PDEC/SAE or dense LCM pressure | `closed_as_dichotomy` |
| `threshold collapse` | kernel recursion loses dense-window mass | finite sparse terminal history word | fixed-history PDEC or nonpersistent SAE budget | `closed_as_sparse_terminal` |
| `cold-core supply` | nonpersistent sparse terminal histories | U_cold <= sum_W (T_PDEC(W)-1)C_core(W) | unified terminal budget gap | `closed_as_budget_upper` |

## 2. 定理边界

| name | proved | statement | role |
| --- | --- | --- | --- |
| `TerminalDefectNoFreeExitTheorem` | `true` | 在假设早期零行且容量反超没有发生时，强 TV/端点缺陷不能作为第四类自由逃逸；它必沿低模、dyadic Fourier、共同核、固定历史、SAE 或冷核心预算之一登记。 | 把反例链与真实结构链的终端交点从抽象缺陷压成命名出口集合。 |
| `ConditionalTerminalContradictionAfterExhaustion` | `true` | 若 NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion 被排斥，且 UnifiedTerminalBudgetStrictInequality 成立，则容量失败分支也无法支付早期零行义务，故早期零行反例不存在。 | 这是本轮新增的条件闭合口，直接接到统一终端预算方程。 |
| `UnconditionalTerminalDefectExclusion` | `false` | 要把 AlphaPrefixTotalVariationOrEndpointPDECDefectExclusion 升级为无条件排斥，仍必须证明命名回流排斥和统一预算严格不等式，或取得 DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance 独立晋级。 | 这是仍未闭合的作者侧全局命题边界。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CounterexampleBranchGuardPreserved` | `true` | `true` | 只在假设早期零行反例链内追踪容量失败后的缺陷，不使用真实零行缺席。 | 无。 |
| `TerminalDefectNoFreeExitClosed` | `true` | `true` | 强 TV/端点缺陷已被耗尽到低模、dyadic、共同核、固定历史、SAE、冷核心预算等命名出口。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion OR UnifiedTerminalBudgetStrictInequality |
| `NamedReturnAlphabetClosed` | `true` | `false` | 所有逃逸口都已命名，不存在未登记第四出口；但命名出口本身尚未全部排斥。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `UnifiedBudgetConditionalContradictionClosed` | `true` | `true` | 若命名回流消失且统一预算严格反超，则得到 L_forced>U_cold 的终端供需矛盾。 | UnifiedTerminalBudgetStrictInequality |
| `AlphaPrefixTVOrPDECDefectExcluded` | `false` | `false` | 缺陷已耗尽为命名出口，但尚未证明所有命名出口或预算失败不可能发生。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND UnifiedTerminalBudgetStrictInequality |
| `DirectUnconditionalContradictionFound` | `false` | `false` | 当前仍没有单点无条件终端矛盾；全局行/列命题不能升级。 | (NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND UnifiedTerminalBudgetStrictInequality) OR DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一真正最窄点

首攻：

```text
NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion
```

并行：

```text
UnifiedTerminalBudgetStrictInequality
```

独立晋级门：

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

审稿边界：本文件证明的是终端缺陷没有自由逃逸，并给出条件矛盾口；它没有证明命名回流排斥，也没有证明统一预算严格不等式，因此不能声明行/列命题无条件闭合。
