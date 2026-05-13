# Prime Matrix strict 兄弟 collar 宽度 LCM/共同核压缩路由器

**状态：** `collar_width_lcm_kernel_compression_closed_exits_open`

`SiblingCollarWidthLCMKernelCompressionLedger` 的结构压缩可以关闭。在同一 dyadic 子乘子层 `Y<g<=2Y` 中，`C_col(g)<2g<=4Y`，所以若 collar 宽度总量过大，就强制该层有许多兼容子乘子。这些子乘子都整除同一父前缀频率 `H_U`，因此可直接接入短窗口除数密度的 LCM 乘子纪律：要么 LCM 增长超过正式频率高度，要么大量低乘子共同核出现。共同核持久化进入固定历史/ColumnCRT/PDEC，非持久则进入有限字母表 SAE。本步关闭的是宽度过大到 LCM/共同核的压缩，不排斥这些出口，因此行/列命题仍未无条件闭合。

```text
width_lcm_target_imported=true
dyadic_width_to_count_proved=true
same_prefix_divisor_anchor_imported=true
short_window_lcm_discipline_imported=true
width_lcm_kernel_compression_proved=true
low_multiplier_common_kernel_excluded=false
sibling_collar_width_budget_absorbed=false
row_column_unconditional_closed=false
```

## 压缩引理

| lemma | statement | effect |
|---|---|---|
| `dyadic width to count` | if Y<g<=2Y, then C_col(g)<2g<=4Y; hence sum C_col>=B implies N_Y>=B/(4Y) | 宽度总量过大强制同一 dyadic 层内子乘子个数过多。 |
| `same prefix divisor anchor` | all child multipliers g in a sibling family divide the same H_U | 同层子乘子集合可接入短窗口除数密度 LCM 纪律。 |
| `LCM or kernel` | large N_Y forces either many LCM multipliers or many low-multiplier common kernels | 宽度过大不能保持无名；必须进入 LCM 高度或共同核回流。 |
| `persistent kernel route` | repeated quotient/kernel type routes to fixed-history ColumnCRT/PDEC | 共同核持久复现不能留在非持久冷供给。 |
| `nonpersistent kernel route` | bounded quotient types without persistence are SAE-countable | 非持久共同核回到有限字母表 SAE 预算。 |

## 有限样本

| Y | dyadic range | child count | width cap | count lower | valid |
|---:|---|---:|---:|---:|---:|
| 10 | `[10, 20]` | 4 | 120 | 3 | `true` |
| 20 | `[20, 40]` | 4 | 240 | 3 | `true` |
| 40 | `[40, 80]` | 9 | 1030 | 6 | `true` |
| 80 | `[80, 160]` | 14 | 3272 | 10 | `true` |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `WidthLCMTargetImported` | `true` | `true` | 上一层已把粗宽度吸收失败压成 LCM/共同核压缩。 | `SiblingCollarWidthLCMKernelCompressionLedger` |
| `DyadicWidthToCountProved` | `true` | `true` | 同一 dyadic 乘子层中，宽度总量下界给出子乘子个数下界。 | `SiblingCollarWidthLCMKernelCompressionLedger` |
| `SamePrefixDivisorAnchorImported` | `true` | `true` | 同一 sibling family 的子乘子都整除同一个 H_U。 | `SiblingCollarWidthLCMKernelCompressionLedger` |
| `LCMKernelDichotomyImported` | `true` | `true` | 子乘子密集后无第四出口：LCM 高度或低乘子共同核。 | `DenseShortWindowLCMLowerBoundAfterKernelCompression OR LowMultiplierCommonKernelColumnCRTOrPDECRoute` |
| `WidthLCMKernelCompressionProved` | `true` | `false` | 宽度过大已压成既有 LCM/共同核出口，但出口本身尚未排斥。 | `DenseShortWindowLCMLowerBoundAfterKernelCompression AND FormalFrequencyHeightCeilingForEndpointPDEC OR LowMultiplierCommonKernelColumnCRTOrPDECRoute` |
| `SameParameterWidthFiniteSumTableProved` | `false` | `false` | 仍可走直接有限总和表路线，但本步未提交该表。 | `SameParameterSiblingCollarWidthFiniteSumTable` |
| `LowMultiplierKernelExcluded` | `false` | `false` | 低乘子共同核还需 ColumnCRT/PDEC 或 SAE 吸收。 | `LowMultiplierCommonKernelColumnCRTOrPDECRoute AND BoundedQuotientTypeSAEAbsorption` |
| `SiblingCollarWidthBudgetAbsorbed` | `false` | `false` | 结构压缩完成，但 LCM 高度/共同核出口仍未排斥。 | `DenseShortWindowLCMLowerBoundAfterKernelCompression AND FormalFrequencyHeightCeilingForEndpointPDEC AND LowMultiplierCommonKernelColumnCRTOrPDECRoute` |
| `SiblingColdCoreThresholdNumericEnvelopeProved` | `false` | `false` | 仍需处理共同核、overlap、PDEC 阈值和热回流。 | `LowMultiplierCommonKernelColumnCRTOrPDECRoute AND SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion AND SameParameterPDECThresholdNumericTable` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | `LowMultiplierCommonKernelColumnCRTOrPDECRoute AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`LowMultiplierCommonKernelColumnCRTOrPDECRoute`。
- 并行保留：
  - `DenseShortWindowLCMLowerBoundAfterKernelCompression`
  - `FormalFrequencyHeightCeilingForEndpointPDEC`
  - `FixedTypeHistoryPDECExclusion`
  - `BoundedQuotientTypeSAEAbsorption`
  - `SameParameterSiblingCollarWidthFiniteSumTable`
  - `ParentSiblingDilatedWindowHotCorePDECorSAEExclusion`
  - `SiblingOverlapMultiplicityFixedReturnOrColumnCRTExclusion`
  - `SameParameterPDECThresholdNumericTable`
  - `SiblingColdCoreThresholdNumericEnvelopeTable`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `experiments/prime_matrix_strict_sibling_collar_width_lcm_kernel_router.py` | `f8194bdd7b7a165a58832730bfca92cf79ea305151218c52153559c26fdcdf3e` |
| `docs/monograph/prime-matrix-strict-sibling-collar-width-budget-router.json` | `2c18a7c8d032867b48f888ac76af6131053d76aa95390833d5087ea056cf06e1` |
| `docs/monograph/prime-matrix-strict-short-window-divisor-density-lcm-router.json` | `b91aa168a84ba29a3c9e6bfb51ad0968b75d625a8864ad9e1d8033574f2ea21e` |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-large-pair-kernel-difference-router.json` | `fc58ab04aae06d90742f61628fa0240994fc110225ce6a1dbce763eb05efe7cc` |
| `docs/monograph/prime-matrix-strict-multisource-fanin-small-quotient-router.json` | `89d82ac6d13034c0b3db3d67585df32e9cc2ad534ddec16ddc9c6eb89c22eda4` |
