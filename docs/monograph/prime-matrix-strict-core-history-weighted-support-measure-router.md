# Prime Matrix strict 冷历史加权支撑测度路由器

**状态：** `weighted_support_measure_reduced_to_depth_telescoping_open`

`CoreHistoryWeightedSupportMeasureTable` 的单层结构可以下钻到前缀树兄弟收费：同父兄弟冷收费投影到父除数支撑，父支撑落入单个扩张父窗口，collar/LCM/共同核爆发不能免费回流，单素数幂和多源 fan-in 也不再是独立无名出口。但这仍不是全深度加权支撑测度证明：单层 envelope 只能控制每个父节点的一层孩子，不能自动控制沿前缀树所有深度的累计支撑，也不能处理 `T_PDEC` 权重。因此最新最窄剩余是 `ColdSupportDepthTelescopingContractionOrLogAbsorptionTable`：必须证明跨层总支撑可由根势能、可吸收对数因子或命名回流控制。

```text
support_measure_target_imported=true
actual_cold_prefix_tree_domain_closed=true
sibling_layer_projection_ledger_imported=true
collar_and_kernel_return_discipline_imported=true
prime_power_and_fanin_independent_exits_removed=true
single_layer_support_envelope_closed=true
depth_telescoping_gap_certified=true
cold_support_depth_telescoping_contraction_or_log_absorption_table_proved=false
core_history_weighted_support_measure_table_proved=false
row_column_unconditional_closed=false
```

## 1. 前缀树分解

| piece | formula | status | meaning |
| --- | --- | --- | --- |
| `prefix tree` | nodes U, children W=U*g, residual H_U=h_0/D(U) | `closed_interface` | 实际冷历史支撑可以按前缀树分层，而不是无结构形式词集合。 |
| `sibling layer charge` | sum_{g child of U} C_core(U*g) <= C_sib(U)+E_hot/fixed/PDEC(U) | `ledger_closed_numeric_open` | 同父兄弟族必须整体收费，超额不再留在冷供给。 |
| `parent projection` | C_sib(U)=\|pi(F_U)\|, pi(g,k)=gk, plus overlap debt | `identity_closed` | 兄弟收费可投回父频率除数支撑，重复投影进入命名回流。 |
| `dilated parent window` | pi(F_U) subset {d\|H_U: d in [L_*,R_*]} | `geometry_closed` | 父投影支撑落入单个 collar 扩张父窗口。 |
| `cross-depth summation` | sum_depth sum_U C_sib(U) needs contraction or log absorption | `open` | 单层收费闭合后，还要控制沿前缀树所有深度的累计支撑。 |

## 2. 深度缺口见证

| depth | per level parent support | single level valid | total support | root support | shows gap |
| ---: | ---: | --- | ---: | ---: | --- |
| 4 | 1 | `true` | 4 | 1 | `true` |
| 8 | 1 | `true` | 8 | 1 | `true` |
| 16 | 1 | `true` | 16 | 1 | `true` |
| 32 | 1 | `true` | 32 | 1 | `true` |

## 3. 对数吸收样本

| P | floor(log2 P)+1 | P^0.43 | absorbed | margin |
| ---: | ---: | ---: | --- | ---: |
| 100000 | 17 | 141.253754 | `true` | 124.253754 |
| 1000000 | 20 | 380.189396 | `true` | 360.189396 |
| 10000000 | 24 | 1023.292992 | `true` | 999.292992 |
| 1000000000 | 30 | 7413.102413 | `true` | 7383.102413 |

## 4. 剩余 envelope

| input | role | status |
| --- | --- | --- |
| `ColdSupportDepthTelescopingContractionOrLogAbsorptionTable` | 把单层 sibling envelope 沿前缀树求和，证明总支撑不超过根势能、对数吸收项或命名回流。 | `open` |
| `SameParameterPDECThresholdNumericTable` | 把未加权支撑升级为 (T_PDEC(W)-1) 加权支撑，并保持同一参数账本。 | `open` |
| `FiniteColdHistorySummationRunnerOrAnalyticEnvelope` | 在有限边界/低 P 区段对实际冷历史族直接枚举或用解析 envelope 补齐。 | `open` |
| `SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow` | 将支撑供给上界与早期零行反例链强制负载作同参数严格比较。 | `open` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SupportMeasureTargetImported` | `true` | `true` | 上一层已把核心阈值求和优势压成实际冷历史加权支撑测度。 | CoreHistoryWeightedSupportMeasureTable |
| `ActualColdPrefixTreeDomainClosed` | `true` | `true` | 有效剪枝接口给出 D(W)\|h_0 与 H_W=h_0/D(W)，故支撑可按前缀树组织。 | CoreHistoryWeightedSupportMeasureTable |
| `SiblingLayerProjectionLedgerImported` | `true` | `true` | 同父兄弟族的单层收费已投影到父支撑、overlap、collar 和命名回流。 | CanonicalColdWindowSiblingChargingOrHotReturnLedger AND ParentScaledChildUnionSupportNumericEnvelope |
| `CollarAndKernelReturnDisciplineImported` | `true` | `true` | collar 宽度爆发和共同核回流已不能作为免费冷供给循环。 | SiblingCollarWidthLCMKernelCompressionLedger AND LowMultiplierCommonKernelColumnCRTOrPDECRoute AND CommonKernelReturnCycleDescentOrPDECLedger |
| `PrimePowerAndFanInIndependentExitsRemoved` | `true` | `true` | 单素数幂形式爆炸已规范化，多源 fan-in 已压成有界小商 SAE/PDEC。 | SmallPrimePowerCascadeColdWindowExclusionTableForP235 AND MultiSourceKernelFanInSAEOrPDECExclusion |
| `SingleLayerSupportEnvelopeClosed` | `true` | `true` | 每个父前缀的一层兄弟冷支撑已经没有无名出口。 | ColdSupportDepthTelescopingContractionOrLogAbsorptionTable |
| `DepthTelescopingGapCertified` | `true` | `true` | 单层 envelope 不能自动推出全深度总支撑；需要收缩或对数吸收表。 | ColdSupportDepthTelescopingContractionOrLogAbsorptionTable |
| `CoreHistoryWeightedSupportMeasureTableProved` | `false` | `false` | 尚未证明跨层总支撑测度在同参数预算内足够小。 | ColdSupportDepthTelescopingContractionOrLogAbsorptionTable AND SameParameterPDECThresholdNumericTable AND FiniteColdHistorySummationRunnerOrAnalyticEnvelope |
| `CoreThresholdSummationDominanceProved` | `false` | `false` | 支撑测度、T_PDEC 权重和需求端下界仍未完成闭合比较。 | CoreHistoryWeightedSupportMeasureTable AND SameParameterPDECThresholdNumericTable AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | ColdSupportDepthTelescopingContractionOrLogAbsorptionTable AND SameParameterPDECThresholdNumericTable AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一步最窄点

- 主攻：`ColdSupportDepthTelescopingContractionOrLogAbsorptionTable`。
- 并行：`SameParameterPDECThresholdNumericTable`、`SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow`、`FiniteColdHistorySummationRunnerOrAnalyticEnvelope`。
- 边界：本步关闭的是单层支撑 envelope 与深度缺口定位，不提交最终全深度加权测度证明。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json` | `be05fb4b2dee03515ca4eea8e086eff6341c0e04d69da9501072cccf74414591` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-effective-cold-history-pruning-router.json` | `72d7aeeb5a09864efcb9cd729d4d5331b1adfb780ec33b3a1ae29dfe6e67431b` |
| `docs/monograph/prime-matrix-strict-multisource-fanin-small-quotient-router.json` | `89d82ac6d13034c0b3db3d67585df32e9cc2ad534ddec16ddc9c6eb89c22eda4` |
| `docs/monograph/prime-matrix-strict-parent-dilated-window-threshold-router.json` | `8ffa039a50039111d1158d985512d9ef1acd10716e08a6efc2f89100c770371b` |
| `docs/monograph/prime-matrix-strict-parent-support-numeric-envelope-router.json` | `c6fe6dcdc47b377c9a55915560031ec8b37d528f6d9980eedbce671a2ee8d653` |
| `docs/monograph/prime-matrix-strict-same-parameter-core-threshold-summation-router.json` | `1cc2717fe5d08bdea447f23044a214316ff2f4dd1f13426922f016ce20beba74` |
| `docs/monograph/prime-matrix-strict-sibling-collar-cap-table-router.json` | `04affb2be59db89256bbc83cb022d0808a473268dff3de85d9f2230214a06b42` |
| `docs/monograph/prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json` | `973a1c986598cb27dd132354715b336eae7938103c89d09da451123f2ade08de` |
| `docs/monograph/prime-matrix-strict-sibling-numeric-envelope-attack-router.json` | `52bd322127d85f72df347da33b5ccc71b6ef2c023539db38244793e6d8d3448c` |
| `docs/monograph/prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json` | `e72a9d55dd3a27c1f9d6287afd6a8debc00a0ebe241977e72e0394bc02c04abf` |
| `experiments/prime_matrix_strict_core_history_weighted_support_measure_router.py` | `2f84767b37085ffeadbd9777c472efd4a13ff99b98183f28d5d84432b21f44f9` |
