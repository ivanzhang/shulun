# Prime Matrix strict Terminal Hot Core Return 前沿路由器

**状态：** `terminal_hot_core_independent_hardpoint_removed_budget_or_persistent_open`

`TerminalCoreHotDivisorWindowPDECorSAE` 已同步到命名回流终端饱和边界：热核心不是独立第三出口。非持久热窗口进入同参数正余量/非持久预算通道；持久热窗口进入 PDEC-CAP、internal CleanKLS 或 actual noncanonical moving atom 终端族。本步删除热核心作为独立硬点，但不排斥两条终端通道，因此行/列命题仍未无条件闭合。

```text
terminal_hot_core_frontier_closed=true
terminal_core_hot_divisor_window_independent_hardpoint_removed=true
terminal_core_hot_divisor_window_pdec_or_sae_excluded=false
row_column_unconditional_closed=false
```

## 1. 终端通道

| lane | trigger | route | status |
| --- | --- | --- | --- |
| `nonpersistent_hot_core` | 热窗口只孤立或低频出现，没有同一 finite signature 的持久复现。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget -> ExplicitPositiveTerminalBudgetMarginInequality | budget_open |
| `persistent_hot_core` | 同一热窗口键、商型、列位移或 finite signature 在 formal unit 中持久复现。 | IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore / PDEC-CAP / internal CleanKLS | terminal_family_open |
| `carrier_or_lcm_hot_core` | 热窗口来自 carrier-lcm source/valuation overflow 或低乘子共同核。 | carrier-lcm return frontier, then budget-or-persistent split | frontier_closed_exclusion_open |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `HotCoreTargetImported` | `true` | `true` | 精确超预算、缩频核心窗口和短窗口密度异常都会登记为热核心命名回流。 | TerminalCoreHotDivisorWindowPDECorSAE |
| `HotCoreNamedAlphabetCompressionImported` | `true` | `true` | HotCore 已在命名回流压缩表中分成持久终端与非持久预算两类。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `HotCoreTerminalSaturationClosed` | `true` | `true` | 热核心不再是独立第三出口；它按持久性进入正余量预算或 acyclic 终端族。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget OR IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `NonpersistentHotCoreAbsorbed` | `false` | `false` | 非持久热窗口还没有被同参数正余量严格吸收。 | ExplicitPositiveTerminalBudgetMarginInequality |
| `PersistentHotCoreExcluded` | `false` | `false` | 持久热窗口还没有被 PDEC-CAP、internal CleanKLS 或 moving atom 排斥。 | IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `TerminalCoreHotDivisorWindowPDECorSAEExcluded` | `false` | `false` | 本步删除独立热核心硬点，但不证明两条终端通道已排斥。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的最终矛盾。 | SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步最窄点

- 主攻：`SparseHistoryDemandExceedsNonpersistentSupplyBudget`。
- 并行守门：`IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` 与 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。
- 边界：本步不排斥热核心终端，只删除其作为独立硬点的地位。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json` | `4162412458fa176a590493f6d2e9bfec6c72169a893e81716c5b6d496ffece1e` |
| `docs/monograph/prime-matrix-strict-named-return-exclusion-compression-router.json` | `7e54f4f456a2108e28a8100a147c9491951f9367c633dd51972e908291d127c2` |
| `docs/monograph/prime-matrix-strict-named-return-terminal-saturation-sync-router.json` | `79eceb8ea54fc81313431a8bfb450e519e3125c88fa34f3058aa3eba4338bde5` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-sparse-budget-positive-margin-latest-sync-router.json` | `128ed6ff8a907a492a29bcafedf5c6c7a1a1c90b6014aab9b4d63fa89001c7b9` |
| `docs/monograph/prime-matrix-strict-windowed-reciprocal-divisor-density-router.json` | `1a367725b5a64d16447823d3bd619ac9955dd634eba4f31ad09326be20ccf57c` |
| `experiments/prime_matrix_strict_terminal_hot_core_return_frontier_router.py` | `f8360c2aca29caf29cfb2e80afa4cfe449528c4bc3c7bf1236ef80c3ae8df32f` |
