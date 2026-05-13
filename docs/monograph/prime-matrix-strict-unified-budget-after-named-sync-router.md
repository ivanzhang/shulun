# Prime Matrix strict 命名回流后统一预算同步路由器

**状态：** `unified_budget_synced_to_sparse_budget_and_moving_atom_open`

`UnifiedTerminalBudgetStrictInequality` 已同步到最新前沿：D0 prefix 需求在当前 standard/external lower-sieve 合同下可用，row-free 无静默塌缩与冷供给调参纪律已闭合，命名回流也已拆成非持久预算吸收和持久终端族排斥。剩余不再是旧 Mertens、类型阈值或命名字母表，而是两个真实输入：`SparseHistoryDemandExceedsNonpersistentSupplyBudget` 与 `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`。

```text
unified_budget_latest_sync_closed=true
sparse_history_demand_exceeds_nonpersistent_supply_budget_proved=false
persistent_terminal_family_excluded=false
row_column_unconditional_closed=false
```

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `UnifiedBudgetTargetImported` | `true` | `false` | 命名回流压缩后，下一主攻点为同参数统一预算严格不等式。 | `UnifiedTerminalBudgetStrictInequality` |
| `SingleParameterNormalFormAlreadyClosed` | `true` | `true` | 终局矛盾已固定为同一参数下的 D_prefix-E_named-U_cold>0，字段合同已列全。 | `ConcreteSameParameterMarginTableCertificate` |
| `D0PrefixDemandAvailableUnderCurrentContract` | `true` | `false` | 在当前 standard/external lower-sieve 合同下，finite-prefix D0/M# 需求侧已不再卡 Mertens 或类型阈值。 | `closed under accepted standard/external lower-sieve contract` |
| `FirstPrinciplesLowerSieveStillSeparate` | `false` | `false` | 若要求 Rosser-Iwaniec lower-sieve 也从零内联，beta-sieve 三项附录仍未完成。 | `BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000` |
| `RowFreeNoSilentCollapseImported` | `true` | `false` | prefix 标签到 row-free/终端投影的预算所需无静默塌缩已闭合。 | `closed for budget form` |
| `NamedReturnAlphabetCompressed` | `true` | `false` | 命名回流已分成非持久预算吸收与持久终端族排斥。 | `SparseHistoryDemandExceedsNonpersistentSupplyBudget AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily` |
| `ColdSupplyDisciplineImported` | `true` | `true` | 冷供给、Lambda schedule 和无免费调参二分已锁入同一参数账本。 | `SparseHistoryDemandExceedsNonpersistentSupplyBudget` |
| `ConcreteMarginTableStillNotProved` | `true` | `false` | 同参数表旧尝试仍未给出 E0/U0 数值吸收和持久终端排斥。 | `SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` |
| `NonpersistentBudgetIsNowNarrowestInequality` | `true` | `false` | 非持久命名回流是否能由 U_cold 吸收，已压成 SparseHistoryDemandExceedsNonpersistentSupplyBudget。 | `SparseHistoryDemandExceedsNonpersistentSupplyBudget` |
| `PersistentTerminalFamilyStillParallel` | `true` | `false` | 持久命名回流仍需 actual noncanonical moving atom/PDEC-CAP 终端排斥。 | `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` |
| `UnifiedTerminalBudgetStrictInequalityCurrentCorpusProved` | `false` | `false` | D0 条件可用、row-free 与冷纪律闭合后，仍未同时证明非持久预算反超和持久终端排斥。 | `SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 统一预算尚未给出最终直接矛盾；DStructure/Rankin 独立门仍保留。 | `SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`SparseHistoryDemandExceedsNonpersistentSupplyBudget`。
- 并行保留：
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DirectAcyclicSameSetPDECCapDualCertificate`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`
  - `BetaSieveLowerWeightRecursiveConstructionLedger AND BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json` | `7c34a1965c8ddc44a43cafb902ae668fb7ed21db3fc6f73cb42716be37c213be` |
| `docs/monograph/prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json` | `e8e2be8c87352d9c984f6f9339c010f851108db941a41c78e477bd0cc4bb1116` |
| `docs/monograph/prime-matrix-strict-explicit-positive-margin-latest-drilldown-router.json` | `a1f751511b011c2bd64b4fe717c36436c18d3946c2407fa0d4cdb4b3338cd31c` |
| `docs/monograph/prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json` | `7fd3d57383dc86ebf277117fc120cc42b2c43371ddd07612c16a0f0fd7bb1d55` |
| `docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json` | `818c17bd920eb69eaa05f2cca96099ad4637c8ab960afd843ec6a53872d392d3` |
| `docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.json` | `f480a9407780a2cc2a9f8e6fc742d6f2db1fa6875fe3de58f687f585abef12e6` |
| `docs/monograph/prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json` | `81ec38d8b42838b270454600184d385487f3c5453b7c4758920d3e0c8a5c22fa` |
| `experiments/prime_matrix_strict_unified_budget_after_named_sync_router.py` | `ecdc9d4013d496d0b5d1d21773a9f71089d132895d31fec3e44b21a80d99d4f9` |
