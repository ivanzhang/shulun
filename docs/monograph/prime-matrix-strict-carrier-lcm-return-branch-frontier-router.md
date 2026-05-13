# Prime Matrix strict carrier-lcm return 分支前沿路由器

**状态：** `carrier_lcm_return_branch_reduced_to_sparse_budget_and_persistent_terminal_open`

`CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption` 已压缩为全局二门：source-defect、valuation-overflow、共同核、热核心和固定历史等 return 分支均不是第四类出口；非持久 return 必须进入 `SparseHistoryDemandExceedsNonpersistentSupplyBudget`，持久 return 必须进入 `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`。因此 carrier-lcm 兼容的剩余不再是局部整除问题，而是非持久预算反超与持久终端族排斥。

```text
return_branch_alphabet_frontier_closed=true
carrier_lcm_compatibility_return_branch_independent_hardpoint_removed=true
carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved=false
sparse_history_demand_exceeds_nonpersistent_supply_budget_proved=false
persistent_terminal_family_excluded=false
cold_prefix_product_divides_carrier_lcm_h0_ledger_global_proved=false
row_column_unconditional_closed=false
```

## 1. Return 分支前沿

| return_branch | nonpersistent_route | persistent_route | meaning |
| --- | --- | --- | --- |
| source_domain_defect_return | SparseHistoryDemandExceedsNonpersistentSupplyBudget | IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore | 单步来源域缺陷不能留在 no-return 分支；非持久则进预算，持久则进终端族。 |
| valuation_overflow_return | SparseHistoryDemandExceedsNonpersistentSupplyBudget | IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore | 累计 p-token 溢出已命名；非持久由 U_cold/稀疏历史吸收，持久进入 PDEC/CleanKLS/固定历史。 |
| hot_or_fixed_or_common_kernel_return | SparseHistoryDemandExceedsNonpersistentSupplyBudget | IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore | 共同核、热核心、固定历史没有第四出口；仍归入同一二分。 |

## 2. 样本账本

- path: `data/carrier-lcm-return-branch-sample-ledger.json`
- sha256: `55193fb7bea2149006a9dd4f22fea2c47fa3174eacdc9ea63cc17b5dca383f09`

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ReturnBranchTargetImported` | `true` | `true` | 上一层已把全局 carrier-lcm 兼容剩余压成 return 分支排斥或吸收。 | CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption |
| `NoReturnBranchAlreadyClosed` | `true` | `true` | 无回流分支上的 D(U)\|h0^car 与整数残频已闭合。 | no-return branch closed |
| `ReturnBranchAlphabetFrontierClosed` | `true` | `true` | 所有 carrier-lcm return 分支均归入非持久预算吸收或持久终端族。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget OR IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `CarrierLCMCompatibilityReturnBranchIndependentHardpointRemoved` | `true` | `true` | return 分支不再是独立黑箱，已压成两个全局终端门。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `CarrierLCMCompatibilityReturnBranchExclusionOrAbsorptionProved` | `false` | `false` | 非持久预算反超与持久终端族排斥仍未完成。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `ColdPrefixProductDividesCarrierLCMH0LedgerGlobalProved` | `false` | `false` | 全局整除还差 return 分支排斥或吸收。 | CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`SparseHistoryDemandExceedsNonpersistentSupplyBudget`。
- 并行守门：`IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` 与 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。
- 边界：本步压缩 return 分支，不证明非持久预算反超或持久终端族排斥。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/carrier-lcm-return-branch-sample-ledger.json` | `55193fb7bea2149006a9dd4f22fea2c47fa3174eacdc9ea63cc17b5dca383f09` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json` | `818c17bd920eb69eaa05f2cca96099ad4637c8ab960afd843ec6a53872d392d3` |
| `docs/monograph/prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.json` | `57c89a464750db6a120968e60975cbf30f2836d6967e9c35875b35508af78f6e` |
| `docs/monograph/prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json` | `94229062234848b5e5e20ffaf940e7d4447b8ec957a0b3e8b2bf85d3e55a1a3f` |
| `docs/monograph/prime-matrix-strict-unified-budget-after-named-sync-router.json` | `17ebb6fdd134cb1ec15518763ec426a0509da1f7432254a4fa16e02dbefb1dc0` |
| `experiments/prime_matrix_strict_carrier_lcm_return_branch_frontier_router.py` | `bc86ad0be3de39ac7450f530e3e0cbd487afbf04c2e27ba80f8cf6220631b1da` |
