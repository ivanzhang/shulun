# Prime Matrix strict 稀疏预算正余量最新同步路由器

**状态：** `sparse_budget_latest_synced_to_cold_numeric_effective_pruning_open`

`SparseHistoryDemandExceedsNonpersistentSupplyBudget` 已在最新正余量前沿下同步：它不再是独立黑箱，而是经同参数稀疏供需严格余量压到 `ColdSupplySameParameterNumericEnvelope`。冷供给数值包已证明粗 full-depth 历史包不可用，下一真正最窄点是 `EffectiveColdHistoryPruningOrHotFixedReturnTheorem`，并行需要 `ColdCoreThresholdFunctionNumericTable` 与 `SameParameterPDECThresholdNumericTable`。热核心、固定历史、moving atom、DStructure 和严格第一性 beta-sieve 附录仍保留。

```text
sparse_budget_positive_margin_latest_sync_closed=true
same_parameter_sparse_margin_reduced_to_cold_numeric=true
cold_supply_same_parameter_numeric_envelope_proved=false
effective_cold_history_pruning_proved=false
cold_core_threshold_numeric_table_proved=false
same_parameter_pdec_threshold_numeric_table_proved=false
sparse_history_demand_exceeds_nonpersistent_supply_budget_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 同步后分解

```text
SparseHistoryDemandExceedsNonpersistentSupplyBudget
  =>
EffectiveColdHistoryPruningOrHotFixedReturnTheorem AND ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

| lane | reduction | status | meaning |
| --- | --- | --- | --- |
| `pure nonpersistent sparse lane` | SparseHistoryDemandExceedsNonpersistentSupplyBudget -> SameParameterSparseDemandColdSupplyStrictMarginCertificate -> ColdSupplySameParameterNumericEnvelope | `structure_closed_numeric_open` | 需求项、非持久回流吸收、冷供给公式和 Lambda 纪律已锁同参数；剩余是冷供给数值包。 |
| `cold numeric envelope` | ColdSupplySameParameterNumericEnvelope -> EffectiveColdHistoryPruningOrHotFixedReturnTheorem AND ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable | `open` | 粗 full-depth 历史包过大，必须用有效剪枝或同参数数值表缩小 U_np。 |
| `hot/fixed escape` | TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion | `parallel_open` | 热核心和固定历史不能记入非持久冷供给；它们仍需排斥或登记终端回流。 |
| `persistent terminal family` | IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore | `parallel_open` | 持久命名回流仍需 actual noncanonical moving atom / acyclic 终端族排斥。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SparseBudgetTargetImportedFromPositiveMargin` | `true` | `false` | 正余量最新同步后，当前最窄主攻点就是非持久稀疏预算反超。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget |
| `SparseBudgetNormalFormImported` | `true` | `true` | SparseHistoryDemand... 已等价压成同参数稀疏供需严格余量。 | SameParameterSparseDemandColdSupplyStrictMarginCertificate |
| `SameParameterSparseMarginReducedToColdNumeric` | `true` | `true` | 纯非持久分支内部剩余已压成 ColdSupplySameParameterNumericEnvelope。 | ColdSupplySameParameterNumericEnvelope |
| `ColdNumericEnvelopeReducedToEffectivePruningAndTables` | `true` | `false` | 粗历史数包已被证明过宽；必须证明有效冷历史剪枝或给出 C_core/T_PDEC 数值表。 | EffectiveColdHistoryPruningOrHotFixedReturnTheorem AND ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable |
| `CarrierReturnFrontierAligned` | `true` | `true` | carrier-lcm return 分支已按非持久预算或持久终端二分登记，不能作为独立局部硬点。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `NamedTerminalSaturationImported` | `true` | `true` | 命名回流终端饱和同步已导入，非持久/持久通道保持分离。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `SparseBudgetPositiveMarginLatestSyncClosed` | `true` | `true` | 稀疏预算在正余量最新前沿下已同步到冷供给数值包与并行终端出口。 | EffectiveColdHistoryPruningOrHotFixedReturnTheorem AND ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable |
| `EffectiveColdHistoryPruningProved` | `false` | `false` | 尚未证明大多数形式冷历史因除数不兼容、LCM 高度、热核心或固定历史回流而退出冷供给。 | EffectiveColdHistoryPruningOrHotFixedReturnTheorem |
| `ColdCoreAndPDECNumericTablesProved` | `false` | `false` | 尚未给出同参数 C_core(W) 与 T_PDEC(W) 的可求和数值表。 | ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable |
| `SparseHistoryDemandExceedsNonpersistentSupplyBudgetProved` | `false` | `false` | 非持久预算反超仍未证明；只是独立黑箱已被删除。 | EffectiveColdHistoryPruningOrHotFixedReturnTheorem AND ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 持久终端族、DStructure/Rankin 和严格第一性 beta-sieve 附录仍未全部完成。 | IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一最窄点

```text
EffectiveColdHistoryPruningOrHotFixedReturnTheorem
```

并行保留：

```text
ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance AND BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000
```

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json` | `a2d4e9a4d5d5f8d377571fc39d9c94e1ddb97d2afae30ef9e4c9e18296677307` |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json` | `5be154f20bb3ff27a7c356dc2fc1d9b2a963be039e3c4f94ec2d941a7e47f721` |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json` | `86ba2fbc9abd9d917a940525fde0a9db0dd4e70ee94f745a56382fee896d8255` |
| `docs/monograph/prime-matrix-strict-named-return-terminal-saturation-sync-router.json` | `79eceb8ea54fc81313431a8bfb450e519e3125c88fa34f3058aa3eba4338bde5` |
| `docs/monograph/prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.json` | `af81fc5d50b443926cf97bbb4698d5b4ca7e4d29a82251d64de76a9a588611ea` |
| `docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-attack-router.json` | `b5d97d9049f35ae7649c8d27932977e68c162e97373651f96fe4d97c90619447` |
| `docs/monograph/prime-matrix-strict-sparse-budget-after-unified-sync-router.json` | `70ca92ae2e350fdeba4eb1d386a9c31835da97f91a7252e3d0fee445a0e79f08` |
| `experiments/prime_matrix_strict_sparse_budget_positive_margin_latest_sync_router.py` | `969fa167d258e8b094c36c4ff58d3ddca629207da4615f6fac46360c3eae9b4d` |
