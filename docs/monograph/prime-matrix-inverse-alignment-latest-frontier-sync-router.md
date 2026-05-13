# Prime Matrix 逆元对齐到最新终端前沿同步路由器

**状态：** `inverse_alignment_row_phase_synced_to_latest_sparse_budget_frontier_open`

逆元最小对齐解思路已经可以被当前前沿充分利用：在假设早期零行存在的反例链中，行号 x 本身生成全部小素数覆盖相位 rho_q(x)=-xP mod q，进而精确生成 R_{x,z}、tau_z(c)、mu_q 与 M#_{x,z}。这关闭的是反例链的行号源和 prefix demand 字段非后验性。但直接用该系统证明 min x>P 会回到短区间素数输入；当前更可用的主线是在 z=P^0.43 的非循环窗口中接入 finite-prefix/row-free/命名回流前沿。同步后，D0 与类型旧阻塞不再是当前最窄点；真正剩余回到非持久稀疏预算的有效冷历史剪枝、持久 moving atom 排斥和 DStructure/Rankin 验收。

```text
inverse_alignment_row_phase_to_latest_frontier_synced=true
normalized_prefix_potential_current_contract_available=true
finite_prefix_strict_first_principles_lower_sieve_closed=false
positive_margin_frontier_after_inverse_alignment_synced=true
sparse_budget_refinement_imported=true
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 逆元恒等式进入前沿

| name | formula | meaning | status |
| --- | --- | --- | --- |
| `inverse_class` | q \| xP+c iff c == rho_q(x)=-xP mod q. | 零行位置 x 给出每个小素数 q 的唯一覆盖相位。 | `closed` |
| `prefix_residual_set` | R_{x,z}={1<=c<P: c != rho_q(x) mod q for every q<=z}. | prefix 残洞不再是抽象集合，而是逆元相位向量的剩余列。 | `closed` |
| `canonical_tau` | tau_z(c)=min{q: z<q<P and c == rho_q(x) mod q}. | 在早期零行假设下，R_{x,z} 中每列都有规范后缀覆盖标签。 | `closed` |
| `capacity_multiplier` | mu_q=#{1<=c<P: c == rho_q(x) mod q} <= ceil(P/q) <= ceil(P/z). | 逆元相位源与容量乘子纪律完全同字段匹配。 | `closed` |
| `weighted_demand` | M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)} >= \|R_{x,z}\|/ceil(P/z). | 用户的最小对齐解系统直接成为统一预算左端需求源。 | `closed_as_formula` |

## 2. 前沿迁移

| stage | before | after | remaining |
| --- | --- | --- | --- |
| `row_position` | 早期零行 x 是抽象反例行号。 | x 等价于所有列的逆元覆盖对齐解。 | none |
| `prefix_demand` | NormalizedPrefixResidualPotentialLowerBound 缺少具体行相位源。 | R_{x,z}, tau_z(c), mu_q, M# 均由 rho_q(x) 生成。 | strict first-principles lower-sieve appendix if demanded |
| `finite_prefix_contract` | finite-prefix D0 曾卡在 runner/tail/Mertens。 | 当前 standard/external 合同下已可用；Mertens 粗原子已回接。 | BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| `projection` | formal-unit 类型阈值像固定常数硬点。 | 预算版 row-free 无静默塌缩已闭合；丢标签必须命名回流。 | named return absorption/exclusion |
| `terminal_budget` | 正余量仍混合 D0、类型、回流、冷供给。 | D0/类型旧阻塞移出，非持久分支压入稀疏预算，持久分支压入 moving atom。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `sparse_budget_refinement` | SparseHistoryDemandExceedsNonpersistentSupplyBudget 仍是粗名。 | 已有最新同步把它压到冷历史有效剪枝、同参数冷数值表、热/固定回流。 | EffectiveColdHistoryPruningOrHotFixedReturnTheorem plus cold numeric/hot/fixed gates |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `InverseAlignmentRowPhaseImported` | `true` | `true` | 早期零行 x 的逆元相位向量已成为 prefix demand 的实际行号源。 | none for row-phase interface |
| `MinXGreaterThanPRouteStillShortInterval` | `false` | `false` | 若直接证明所有最小对齐解 x>P，仍等价要求长度 P 短区间含素数。 | PrimeGapBelowP2ForAllPBlocks |
| `NormalizedPrefixPotentialCurrentContractAvailable` | `true` | `false` | 在当前 standard/external lower-sieve 合同下，finite-prefix D0/M# 需求侧可接入。 | BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| `StrictFirstPrinciplesLowerSieveClosed` | `false` | `false` | 若要求 beta-sieve lower weights 也完全从零内联，该附录仍未完成。 | BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000 |
| `PositiveMarginFrontierSynced` | `true` | `true` | D0/row-free/命名回流前沿与逆元行号源同字段同步。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| `SparseBudgetRefinedToEffectivePruning` | `true` | `false` | 非持久预算不是抽象黑箱，已由旧材料压到冷历史有效剪枝和同参数数值表。 | EffectiveColdHistoryPruningOrHotFixedReturnTheorem |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 尚未同时完成非持久预算反超、持久 moving atom 排斥和 DStructure/Rankin 验收。 | EffectiveColdHistoryPruningOrHotFixedReturnTheorem AND ColdSupplySameParameterNumericEnvelope AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一最窄点

```text
EffectiveColdHistoryPruningOrHotFixedReturnTheorem
```

并行保留：

```text
ColdSupplySameParameterNumericEnvelope AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance AND BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000
```

审稿边界：本步不声明 `min x>P`、不使用真实零行缺席，也不声明行/列命题无条件闭合；它只把用户的逆元零行方程组并入当前统一预算前沿，并给出同步后的精确剩余。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-inverse-alignment-covering-system-router.json` | `09be6a101dd2775a057577a1ef960270dbd88b03dd5e5cec4d1bddec67eb1acf` |
| `docs/monograph/prime-matrix-inverse-alignment-prefix-demand-bridge-router.json` | `369bf801b153a8cb792ef4a0971d5156020eb6604c2cdd31808d81cd4770c70a` |
| `docs/monograph/prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.json` | `8e77ecf35bc897c4b39202582b59286394d4afcf77149ea56cdfd265ec4a1ca9` |
| `docs/monograph/prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json` | `7fd3d57383dc86ebf277117fc120cc42b2c43371ddd07612c16a0f0fd7bb1d55` |
| `docs/monograph/prime-matrix-strict-formal-unit-type-threshold-sync-router.json` | `1ef03a6b801aa5cf34ee8510bf3470091e3ba27501009d91174f137a954b5649` |
| `docs/monograph/prime-matrix-strict-normalized-prefix-potential-router.json` | `4f86ea29ee34a43e365527b3c6e030050418f872c893c8ba470d8997ed66d6da` |
| `docs/monograph/prime-matrix-strict-positive-margin-after-finite-prefix-terminal-sync-router.json` | `af81fc5d50b443926cf97bbb4698d5b4ca7e4d29a82251d64de76a9a588611ea` |
| `docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.json` | `f480a9407780a2cc2a9f8e6fc742d6f2db1fa6875fe3de58f687f585abef12e6` |
| `docs/monograph/prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json` | `128ed6ff8a907a492a29bcafedf5c6c7a1a1c90b6014aab9b4d63fa89001c7b9` |
| `docs/monograph/prime-matrix-strict-terminal-hot-core-return-frontier-router.json` | `bb4818efdb6673899bc0e2eb86174244ef0f80568301c8ca34a57dc380bda909` |
| `docs/monograph/prime-matrix-strict-unified-budget-after-named-sync-router.json` | `17ebb6fdd134cb1ec15518763ec426a0509da1f7432254a4fa16e02dbefb1dc0` |
| `docs/monograph/prime-matrix-strict-uniform-prefix-rough-count-router.json` | `565216b00f151a42a0105b48eb3f09b4d1968f923d698fdb2ba1bdecd906afee` |
| `experiments/prime_matrix_inverse_alignment_latest_frontier_sync_router.py` | `990c901ed74a71c863544985f59e175497396271598a5f8a7aaedd469ee83dc2` |
