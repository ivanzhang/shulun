# Prime Matrix strict 同参数核心阈值求和优势路由器

**状态：** `core_threshold_summation_reduced_to_weighted_support_measure_open`

`SameParameterCoreThresholdSummationDominanceTable` 不能由上一层的点态 `C_core` 定义表直接闭合。本步把它压成严格的同参数三原子：第一，实际冷历史族的加权支撑测度 `CoreHistoryWeightedSupportMeasureTable`；第二，同一账本下的 `SameParameterPDECThresholdNumericTable`；第三，需求端 `SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow`。点态长度 cap 只能控制单个窗口，不能控制冷历史数量、持久阈值权重或需求端下界；若求和优势失败，失败源必须回流到前缀分叉/LCM 共同核、终端热核心、固定历史/PDEC 或统一终端预算缺口。

```text
core_summation_target_imported=true
same_parameter_cold_supply_formula_imported=true
actual_cold_history_domain_imported=true
pointwise_cap_not_enough_certified=true
weighted_support_reduction_closed=true
core_history_weighted_support_measure_table_proved=false
same_parameter_pdec_threshold_numeric_table_proved=false
sparse_terminal_forced_load_lower_bound_proved=false
core_threshold_summation_dominance_proved=false
row_column_unconditional_closed=false
```

## 1. 求和对象

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `actual_cold_history_domain` | C_cold(h_0)={W: D(W)\|h_0, H_W=h_0/D(W), W remains nonpersistent cold} | `closed_domain_open_size` | 求和只能在实际存活冷历史族上做，不能对全部形式历史求和。 |
| `nonpersistent_supply_bound` | U_np <= sum_{W in C_cold(h_0)} (T_PDEC(W)-1) C_core(W) | `imported_closed_bound` | 非持久冷供给上界已经闭合；当前缺的是右侧是否足够小。 |
| `length_envelope` | N_{H_W}(I_W) <= \|I_W\| | `closed_pointwise_cap` | 点态长度 cap 可作上界组件，但不能控制历史数量或 T_PDEC 权重。 |
| `weighted_support_measure` | Sigma_core(h_0)=sum_{W in C_cold(h_0)} (T_PDEC(W)-1) C_core(W) | `open_numeric_measure` | 这是本层必须生成的同参数加权支撑测度表。 |
| `dominance_target` | Sigma_core(h_0) < L_forced(P,z,D)-E_named | `open_strict_dominance` | 若成立，则早期零行反例链的非持久冷供给不足，形成终端矛盾。 |

## 2. 点态 cap 的不足

| model | assumption | consequence | obstruction | needed input |
| --- | --- | --- | --- | --- |
| `free_support_count` | only C_core(W)<=1 and T_PDEC(W)-1<=1 | sum_W(T_PDEC(W)-1)C_core(W)=#C_cold(h_0) | 若没有 #C_cold(h_0) 支撑界，右侧可任意大。 | CoreHistoryWeightedSupportMeasureTable |
| `large_persistence_threshold` | #C_cold(h_0) bounded but T_PDEC(W) unbounded | 同一支撑可被持久阈值权重放大。 | 必须用同一参数账本固定 T_PDEC，不能事后调参。 | SameParameterPDECThresholdNumericTable |
| `weak_forced_load` | cold supply bounded but L_forced lower bound missing | 无法推出 L_forced>U_np。 | 反例链需求端必须给出同参数强制负载下界。 | SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow |

## 3. 失败源回流矩阵

| failure | rigidity route | named exit |
| --- | --- | --- |
| too many cold histories under one prefix | same-prefix LCM anchor and incremental multiplier split | ColdHistoryPrefixBranchingHotOrFixedReturnLemma / PrefixBranchingKernelMultiplicityBudgetLedger / LowMultiplierCommonKernelColumnCRTOrPDECRoute |
| collar or short-window support expands too much | sibling collar width LCM compression | SiblingCollarWidthLCMKernelCompressionLedger / TerminalCoreHotDivisorWindowPDECorSAE / FixedTypeHistoryPDECExclusion |
| terminal cold windows stay crowded without becoming hot | cold-hot split plus terminal anti-cascade | TerminalColdWindowCompatibilityAntiCascadeLemma / TerminalCoreHotDivisorWindowPDECorSAE |
| same history repeats beyond nonpersistent allowance | multiplicity threshold converts persistence into named return | SameParameterPDECThresholdNumericTable / FixedTypeHistoryPDECExclusion |
| supply is bounded but still not below demand | unified terminal budget gap | SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CoreSummationTargetImported` | `true` | `true` | 上一层已把 C_core 定义表后的主攻点指向同参数求和优势。 | SameParameterCoreThresholdSummationDominanceTable |
| `SameParameterColdSupplyFormulaImported` | `true` | `true` | 非持久冷供给公式和同参数账本已从回流后数值包继承。 | SameParameterCoreThresholdSummationDominanceTable |
| `ActualColdHistoryDomainImported` | `true` | `true` | 有效剪枝接口给出实际冷历史族 C_cold(h_0)，并禁止对全部形式历史求和。 | CoreHistoryWeightedSupportMeasureTable |
| `PointwiseCapNotEnoughCertified` | `true` | `true` | 仅有 C_core 点态 cap 无法控制历史支撑数、T_PDEC 权重和需求端负载。 | CoreHistoryWeightedSupportMeasureTable AND SameParameterPDECThresholdNumericTable AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow |
| `WeightedSupportReductionClosed` | `true` | `true` | 求和优势被精确压成同参数加权支撑测度表加需求端严格比较。 | CoreHistoryWeightedSupportMeasureTable AND FiniteColdHistorySummationRunnerOrAnalyticEnvelope AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow |
| `SameParameterPDECThresholdNumericTableProved` | `false` | `false` | 有限 FO-PDEC ledger 只是投影阈值账本，不是全局同参数 T_PDEC 表。 | SameParameterPDECThresholdNumericTable |
| `CoreHistoryWeightedSupportMeasureTableProved` | `false` | `false` | 尚未证明实际冷历史族的加权支撑测度足够小。 | CoreHistoryWeightedSupportMeasureTable |
| `CoreThresholdSummationDominanceProved` | `false` | `false` | 缺支撑测度、T_PDEC 表和需求端严格下界的闭合比较。 | CoreHistoryWeightedSupportMeasureTable AND SameParameterPDECThresholdNumericTable AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | CoreHistoryWeightedSupportMeasureTable AND SameParameterPDECThresholdNumericTable AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步最窄点

- 主攻：`CoreHistoryWeightedSupportMeasureTable`。
- 并行：`SameParameterPDECThresholdNumericTable`、`SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow`、`FiniteColdHistorySummationRunnerOrAnalyticEnvelope`。
- 边界：本步关闭的是求和优势的结构化降解与失败源登记，不提交最终数值反超。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-budget-gap-router.json` | `dc5db9c8aa57f3b8c29354615714c6c124f8b8326b288d3b8c7cccec57db62cf` |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-function-table-router.json` | `17d7ee987e51872094edd8c3dc0210b6b87d4751d04864d5d66a162770f3cffc` |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json` | `5be154f20bb3ff27a7c356dc2fc1d9b2a963be039e3c4f94ec2d941a7e47f721` |
| `docs/monograph/prime-matrix-strict-effective-cold-history-pruning-router.json` | `72d7aeeb5a09864efcb9cd729d4d5331b1adfb780ec33b3a1ae29dfe6e67431b` |
| `docs/monograph/prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json` | `94229062234848b5e5e20ffaf940e7d4447b8ec957a0b3e8b2bf85d3e55a1a3f` |
| `docs/monograph/prime-matrix-strict-unified-terminal-budget-equation-router.json` | `034515ed984e8ce3bac42dc02b08faf7caa43fd58554a3bd9d87f00419f0eded` |
| `docs/monograph/prime-matrix-wsh-fo-pdec-threshold-ledger.json` | `5013d7efece4e7df59a967b990b3def147604029d9196a3e05df270787f148bc` |
| `experiments/prime_matrix_strict_same_parameter_core_threshold_summation_router.py` | `274d7bb648365aabe6ae9dd203cf396660e138956b0652306fd57468f9d91d7b` |
