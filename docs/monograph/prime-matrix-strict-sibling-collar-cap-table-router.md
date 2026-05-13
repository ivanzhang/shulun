# Prime Matrix strict 兄弟 collar 同参数 cap 表路由器

**状态：** `same_parameter_collar_cap_table_closed_width_budget_open`

`SameParameterSiblingCollarShortDivisorCapTable` 可以关闭：左 collar 和右 collar 都是同一父窗口扩张产生的整数短区间，所以除数个数分别不超过区间长度；总 cap 为 `C_col(U)=(L-L_*)+(R_*-R)<2g_max(U)`。这给出完全同参数的 collar cap 表，并把扩张父窗口阈值写成 `C_dil(U)=C_core^*(U;[L,R])+C_col(U)`。但该长度 cap 可能太粗，尚未证明其在最终统一预算中可吸收；若不能吸收，必须用短窗口 LCM/共同核/PDEC 路由锐化。因此本步关闭 collar cap 表本身，不关闭行/列无条件命题。

```text
collar_cap_target_imported=true
integer_length_collar_cap_proved=true
same_parameter_collar_short_divisor_cap_table_proved=true
parent_sibling_dilated_window_cold_core_threshold_table_proved=true
collar_width_budget_absorbed=false
parent_scaled_child_union_support_numeric_envelope_proved=false
row_column_unconditional_closed=false
```

## cap 公式

| name | formula | role |
|---|---|---|
| `left collar cap` | `N_H([L_*,L-1]) <= max(0,L-L_*)` | 整数区间长度上界，同参数可计算。 |
| `right collar cap` | `N_H([R+1,R_*]) <= max(0,R_*-R)` | 整数区间长度上界，同参数可计算。 |
| `total collar cap` | `C_col(U)=max(0,L-L_*)+max(0,R_*-R) < 2 g_max(U)` | 给出左右 collar 的统一 cap。 |
| `dilated cold threshold` | `C_dil(U)=C_core^*(U;[L,R])+C_col(U)` | 在原父窗口冷分支中，扩张父窗口 cap 可计算。 |
| `sharpness warning` | `if sum_U C_col(U) is too large, use LCM/PDEC sharpening, not free deletion` | 宽度 cap 可能太粗，必须进入同参数总预算或命名回流。 |

## 有限样本

| parent window | union interval | g_max | left length | right length | collar cap | cap < 2gmax |
|---|---|---:|---:|---:|---:|---:|
| `[20, 180]` | `[18, 180]` | 6 | 2 | 0 | 2 | `true` |
| `[30, 240]` | `[28, 245]` | 7 | 2 | 5 | 7 | `true` |
| `[50, 420]` | `[45, 423]` | 9 | 5 | 3 | 8 | `true` |
| `[60, 720]` | `[54, 721]` | 10 | 6 | 1 | 7 | `true` |
| `[401, 4001]` | `[390, 4012]` | 23 | 11 | 11 | 22 | `true` |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `CollarCapTargetImported` | `true` | `true` | 上一层已把扩张表剩余压成同参数 collar cap。 | `SameParameterSiblingCollarShortDivisorCapTable` |
| `IntegerLengthCollarCapProved` | `true` | `true` | 任何 collar 内除数个数不超过该整数区间长度。 | `SameParameterSiblingCollarShortDivisorCapTable` |
| `SameParameterCollarCapTableProved` | `true` | `true` | 左右 collar 长度由同一父窗口和子乘子账本计算，不引入新参数。 | `SameParameterSiblingCollarShortDivisorCapTable` |
| `DilatedColdThresholdTableProved` | `true` | `false` | 在原父窗口冷分支中，可用 C_core^*+C_col 作为扩张窗口阈值。 | `ParentSiblingDilatedWindowColdCoreThresholdTable` |
| `CollarWidthBudgetAbsorbed` | `false` | `false` | 尚未证明 sum_U C_col(U) 在最终同参数预算中可吸收。 | `SiblingCollarWidthBudgetAbsorptionLedger` |
| `CollarLCMSharpeningStillOpen` | `false` | `false` | 若宽度 cap 太粗，需要短窗口 LCM/共同核/PDEC 锐化。 | `SiblingCollarShortDivisorBurstLCMOrPDECRoute` |
| `ParentDilatedWindowHotReturnExcluded` | `false` | `false` | 原父窗口热或扩张后热回流仍未排斥。 | `ParentSiblingDilatedWindowHotCorePDECorSAEExclusion` |
| `ParentSupportNumericEnvelopeProved` | `false` | `false` | collar cap 表闭合，但宽度预算吸收和热回流排斥仍未完成。 | `SiblingCollarWidthBudgetAbsorptionLedger AND ParentSiblingDilatedWindowHotCorePDECorSAEExclusion` |
| `SiblingColdCoreThresholdNumericEnvelopeProved` | `false` | `false` | 还需 overlap、PDEC 阈值和最终宽度预算吸收。 | `SiblingCollarWidthBudgetAbsorptionLedger AND SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion AND SameParameterPDECThresholdNumericTable` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | `SiblingCollarWidthBudgetAbsorptionLedger AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`SiblingCollarWidthBudgetAbsorptionLedger`。
- 并行保留：
  - `SiblingCollarShortDivisorBurstLCMOrPDECRoute`
  - `ParentSiblingDilatedWindowHotCorePDECorSAEExclusion`
  - `ColdCoreThresholdFunctionNumericTable`
  - `SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion`
  - `SameParameterPDECThresholdNumericTable`
  - `SiblingColdCoreThresholdNumericEnvelopeTable`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `experiments/prime_matrix_strict_sibling_collar_cap_table_router.py` | `fbe82f4358a3716dcce819bb62a366abf40ef5d0132f719f4c5f84833aba9edc` |
| `docs/monograph/prime-matrix-strict-parent-dilated-window-threshold-router.json` | `8ffa039a50039111d1158d985512d9ef1acd10716e08a6efc2f89100c770371b` |
| `docs/monograph/prime-matrix-strict-parent-support-numeric-envelope-router.json` | `c6fe6dcdc47b377c9a55915560031ec8b37d528f6d9980eedbce671a2ee8d653` |
| `docs/monograph/prime-matrix-strict-short-window-divisor-density-lcm-router.json` | `b91aa168a84ba29a3c9e6bfb51ad0968b75d625a8864ad9e1d8033574f2ea21e` |
