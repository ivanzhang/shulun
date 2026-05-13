# Prime Matrix strict 兄弟 collar 宽度预算吸收路由器

**状态：** `collar_width_budget_naive_absorption_rejected_lcm_kernel_open`

`SiblingCollarWidthBudgetAbsorptionLedger` 不能由粗宽度 cap 直接关闭。虽然每个 collar 有 `C_col(U)<2g_max(U)`，但若没有进一步限制 sibling family 数量和 `g_max` 的总和，形式上 `sum_U C_col(U)` 可达到超过 `P^0.43` 的阶，不能保证被最终需求余量吸收。合法下一步是二分：要么提交同参数宽度有限总和表，要么证明宽度过大强制同前缀大乘子密集，从而由 LCM 乘子纪律产生频率高度矛盾，或进入低乘子共同核、固定历史/PDEC/SAE 回流。本步关闭的是粗吸收不可用和宽度失败二分，不关闭最终命题。

```text
width_absorption_target_imported=true
crude_width_cap_imported=true
naive_width_absorption_rejected=true
width_dichotomy_registered=true
same_parameter_width_finite_sum_table_proved=false
width_lcm_kernel_compression_proved=false
sibling_collar_width_budget_absorbed=false
row_column_unconditional_closed=false
```

## 粗吸收阻塞模型

| family exponent | gmax exponent | width exponent | alpha | absorbed |
|---:|---:|---:|---:|---:|
| 0.10 | 0.10 | 0.20 | 0.43 | `true` |
| 0.20 | 0.20 | 0.40 | 0.43 | `true` |
| 0.30 | 0.20 | 0.50 | 0.43 | `false` |
| 0.43 | 0.43 | 0.86 | 0.43 | `false` |

## 宽度失败二分

| case | criterion | route |
|---|---|---|
| `finite width sum table` | sum_U (T_U-1) C_col(U) <= U_col,0(P,z,Lambda) | 若 U_col,0 与既有 U_cold 合并后仍小于需求余量，则宽度预算吸收。 |
| `many large g_max` | 同一前缀下大 g_max 频繁出现 | LCM 乘子纪律迫使频率高度爆炸，或产生低乘子共同核。 |
| `low-multiplier kernel` | g_t 与既有 lcm 共享大共同核 | 进入大成对差值锁、多源 fan-in、固定历史 PDEC 或 SAE。 |
| `persistent width packet` | 同一 collar shape/formal unit 重复超阈值 | 进入固定历史/ColumnCRT/PDEC，不留在非持久冷供给。 |
| `nonpersistent sparse width` | 所有宽度包均不持久 | 进入有限历史 SAE 求和，回到同参数 U_cold 正余量。 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `WidthAbsorptionTargetImported` | `true` | `true` | 上一层已把 collar cap 后的剩余压成宽度预算吸收。 | `SiblingCollarWidthBudgetAbsorptionLedger` |
| `CrudeWidthCapImported` | `true` | `true` | 每个 collar 宽度满足 C_col(U)<2g_max(U)。 | `SameParameterSiblingCollarShortDivisorCapTable` |
| `NaiveWidthAbsorptionRejected` | `true` | `true` | 仅靠 sum 2g_max 的粗估可超过 alpha=0.43 需求阶。 | `SiblingCollarWidthLCMKernelCompressionLedger` |
| `WidthDichotomyRegistered` | `true` | `false` | 宽度预算失败只能来自大 g_max、共同核、持久包或非持久 SAE。 | `SiblingCollarWidthLCMKernelCompressionLedger` |
| `SameParameterWidthFiniteSumTableProved` | `false` | `false` | 尚未给出 sum_U (T_U-1)C_col(U) 的同参数有限总和表。 | `SameParameterSiblingCollarWidthFiniteSumTable` |
| `WidthLCMKernelCompressionProved` | `false` | `false` | 尚未证明宽度过大必触发 LCM 高度矛盾或共同核回流。 | `SiblingCollarWidthLCMKernelCompressionLedger` |
| `SiblingCollarWidthBudgetAbsorbed` | `false` | `false` | 宽度 cap 表闭合，但总预算吸收/锐化仍未完成。 | `SameParameterSiblingCollarWidthFiniteSumTable OR SiblingCollarWidthLCMKernelCompressionLedger` |
| `ParentSupportNumericEnvelopeProved` | `false` | `false` | 父支撑仍需宽度吸收和热回流排斥。 | `SiblingCollarWidthBudgetAbsorptionLedger AND ParentSiblingDilatedWindowHotCorePDECorSAEExclusion` |
| `SiblingColdCoreThresholdNumericEnvelopeProved` | `false` | `false` | 还需 overlap、PDEC 阈值、宽度预算与热回流。 | `SiblingCollarWidthBudgetAbsorptionLedger AND SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion AND SameParameterPDECThresholdNumericTable` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | `SiblingCollarWidthLCMKernelCompressionLedger AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`SiblingCollarWidthLCMKernelCompressionLedger`。
- 并行保留：
  - `SameParameterSiblingCollarWidthFiniteSumTable`
  - `SiblingCollarShortDivisorBurstLCMOrPDECRoute`
  - `ParentSiblingDilatedWindowHotCorePDECorSAEExclusion`
  - `FixedTypeHistoryPDECExclusion`
  - `SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion`
  - `SameParameterPDECThresholdNumericTable`
  - `SiblingColdCoreThresholdNumericEnvelopeTable`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `experiments/prime_matrix_strict_sibling_collar_width_budget_router.py` | `888964b7176b291dd4936e47abe02f42ae224dc10734c5a2b3c4bd163c371bd6` |
| `docs/monograph/prime-matrix-strict-sibling-collar-cap-table-router.json` | `04affb2be59db89256bbc83cb022d0808a473268dff3de85d9f2230214a06b42` |
| `docs/monograph/prime-matrix-strict-parent-dilated-window-threshold-router.json` | `8ffa039a50039111d1158d985512d9ef1acd10716e08a6efc2f89100c770371b` |
| `docs/monograph/prime-matrix-strict-short-window-divisor-density-lcm-router.json` | `b91aa168a84ba29a3c9e6bfb51ad0968b75d625a8864ad9e1d8033574f2ea21e` |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-large-pair-kernel-difference-router.json` | `fc58ab04aae06d90742f61628fa0240994fc110225ce6a1dbce763eb05efe7cc` |
