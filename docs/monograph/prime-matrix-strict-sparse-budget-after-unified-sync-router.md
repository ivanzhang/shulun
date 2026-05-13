# Prime Matrix strict 统一预算后稀疏供需缺口同步路由器

**状态：** `sparse_budget_synced_to_same_parameter_margin_hot_fixed_moving_open`

`SparseHistoryDemandExceedsNonpersistentSupplyBudget` 已被同步到最新统一预算前沿：非持久历史预算公式、prefix/row-free 无静默塌缩、finite-prefix 需求侧、冷供给同参数纪律、以及单历史容量的冷/热分裂都已接入。剩余不再是宽泛的“稀疏历史是什么”，而是同一参数下的严格标量缺口 `M#_{x,z}-E_registered>U_np`。当前尚未证明该严格正余量；热核心、固定历史和持久终端族仍需作为并行出口排斥，行/列命题不能升级为无条件闭合。

```text
sparse_budget_latest_sync_closed=true
same_parameter_sparse_demand_cold_supply_normal_form_closed=true
same_parameter_sparse_demand_cold_supply_strict_margin_proved=false
sparse_history_demand_exceeds_nonpersistent_supply_budget_proved=false
row_column_unconditional_closed=false
```

## 同参数供需方程

| name | formula | status | meaning |
|---|---|---|---|
| `demand_accounting` | `L_forced >= M#_{x,z}-E_registered` | `closed_normal_form` | 早期零行产生的 prefix 加权义务，要么进入终端负载，要么登记为命名回流。 |
| `nonpersistent_supply` | `U_np <= sum_W (T_PDEC(W)-1) C_core(W)` | `closed_upper_envelope` | 所有非持久稀疏历史的冷供给已被同一 Lambda/PDEC 阈值上界控制。 |
| `sparse_budget_gap` | `M#_{x,z}-E_registered > U_np` | `open_strict_margin` | 这是 SparseHistoryDemandExceedsNonpersistentSupplyBudget 的同参数标量形态。 |
| `hot_or_persistent_escape` | `large N_{H_W}(I_W) or repeated W -> hot/fixed/PDEC terminal return` | `registered_open` | 热核心或固定历史不是自由容量；但仍需独立排斥或回流验收。 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `SparseBudgetTargetImportedFromUnifiedBudget` | `true` | `false` | 统一预算最新前沿已把非持久分支精确钉到 SparseHistoryDemandExceedsNonpersistentSupplyBudget。 | `SparseHistoryDemandExceedsNonpersistentSupplyBudget` |
| `NonpersistentBudgetFormulaClosed` | `true` | `true` | 若没有持久历史，U_np 已写成历史词求和；若 L_forced>U_np 就得到供需矛盾。 | `SameParameterSparseDemandColdSupplyStrictMarginCertificate` |
| `NoSilentProjectionCollapseImported` | `true` | `true` | prefix 义务到 row-free/稀疏终端历史的预算版无静默塌缩已闭合。 | `closed for budget form; strong injection not asserted` |
| `DemandSideAvailableUnderCurrentContract` | `true` | `false` | 在当前 standard/external lower-sieve 合同下，finite-prefix 需求侧和强制负载守恒可用。 | `SameParameterSparseDemandColdSupplyStrictMarginCertificate` |
| `FirstPrinciplesLowerSieveStillSeparate` | `false` | `false` | 若要求 lower-sieve 基本引理从零内联，beta-sieve 三项附录仍未完成。 | `BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000` |
| `ColdSupplySameParameterDisciplineClosed` | `true` | `true` | 冷供给上界、Lambda 调节纪律和供需矛盾判据已锁到同一参数账本。 | `SameParameterSparseDemandColdSupplyStrictMarginCertificate` |
| `SingleHistoryCapacityReducedToColdOrHot` | `true` | `false` | 单历史重数已压到缩频核心窗口；冷窗口进 U_np，热窗口必须命名回流。 | `SameParameterSparseDemandColdSupplyStrictMarginCertificate AND TerminalCoreHotDivisorWindowPDECorSAE` |
| `NamedReturnAlphabetCompressed` | `true` | `false` | 非持久回流必须进入统一预算，持久回流进入终端族；没有无名出口。 | `SameParameterSparseDemandColdSupplyStrictMarginCertificate AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` |
| `SameParameterSparseDemandColdSupplyNormalFormClosed` | `true` | `false` | SparseHistoryDemandExceedsNonpersistentSupplyBudget 等价压成同参数标量缺口 M#-E_registered>U_np。 | `SameParameterSparseDemandColdSupplyStrictMarginCertificate` |
| `SameParameterSparseDemandColdSupplyStrictMarginProved` | `false` | `false` | 当前材料尚未给出 M#_{x,z}-E_registered-U_np 的严格正余量证书。 | `SameParameterSparseDemandColdSupplyStrictMarginCertificate` |
| `HotFixedPersistentEscapesExcluded` | `false` | `false` | 热核心、固定历史和持久终端族仍未被独立排斥；它们不能作为非持久 U_np 免费容量。 | `TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` |
| `SparseHistoryDemandExceedsNonpersistentSupplyBudgetProved` | `false` | `false` | 预算结构、供需口和同参数纪律已闭合，但严格余量和热/持久出口排斥仍未完成。 | `SameParameterSparseDemandColdSupplyStrictMarginCertificate AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步没有得到排除早期零行反例链的终端矛盾；DStructure/Rankin 晋级门仍保留。 | `SameParameterSparseDemandColdSupplyStrictMarginCertificate AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`SameParameterSparseDemandColdSupplyStrictMarginCertificate`。
- 并行保留：
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DirectAcyclicSameSetPDECCapDualCertificate`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`
  - `BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json` | `7c34a1965c8ddc44a43cafb902ae668fb7ed21db3fc6f73cb42716be37c213be` |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-budget-gap-router.json` | `dc5db9c8aa57f3b8c29354615714c6c124f8b8326b288d3b8c7cccec57db62cf` |
| `docs/monograph/prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json` | `7fd3d57383dc86ebf277117fc120cc42b2c43371ddd07612c16a0f0fd7bb1d55` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json` | `2c0a5401dc9e7f7158cd30e758f88f5a07f68460712f611452ff609ae3b7ddbb` |
| `docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json` | `818c17bd920eb69eaa05f2cca96099ad4637c8ab960afd843ec6a53872d392d3` |
| `docs/monograph/prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json` | `94229062234848b5e5e20ffaf940e7d4447b8ec957a0b3e8b2bf85d3e55a1a3f` |
| `docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.json` | `f480a9407780a2cc2a9f8e6fc742d6f2db1fa6875fe3de58f687f585abef12e6` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json` | `3fabe3f3825c980842551045d9ca8714df0b3bb6fd1b92e39ba5e7e70daea1af` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-history-sae-budget-router.json` | `8f077e91bd0f02d25e6598256b5ebe958579e779abe1ecc41dd6861207e09523` |
| `docs/monograph/prime-matrix-strict-unified-budget-after-named-sync-router.json` | `17ebb6fdd134cb1ec15518763ec426a0509da1f7432254a4fa16e02dbefb1dc0` |
| `experiments/prime_matrix_strict_sparse_budget_after_unified_sync_router.py` | `72a828b3112932eb3d8a7b55d3d52c8aac982169447c5f3b0fadf7ab946d5977` |
