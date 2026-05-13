# Prime Matrix strict 小素数幂冷窗口级联攻坚路由器

**状态：** `small_prime_cascade_reduced_to_dyadic_primary_and_odd_epsilon_open`

`SmallPrimePowerCascadeColdWindowExclusionTableForP235` 进一步拆成三层风险。`p=5` 的全分组指数只比 alpha 多约 0.000677，且一二步模型已低于 alpha，所以它主要需要大块分组降阶账本。`p=3` 的一二步指数只多约 0.008018，需要很小的奇素数节省或冷窗口反级联。`p=2` 即使在一二步 Fibonacci 模型中仍为 `P^0.694`，比 alpha 多约 0.264242，是当前唯一强主危险。因此下一最窄主攻点应集中到 `DyadicPrimePowerColdWindowCascadeExclusionLemma`。

```text
p235_dangerous_set_identified=true
p5_block_size_sensitive_only=true
p3_epsilon_sensitive_odd_case=true
p2_primary_dyadic_case=true
dyadic_cascade_exclusion_proved=false
small_prime_power_cascade_table_proved=false
row_column_unconditional_closed=false
```

## p=2,3,5 风险分层

| p | all_grouped_exponent | all_gap | one_two_exponent | one_two_gap | risk_level | needed_input |
|---:|---:|---:|---:|---:|---|---|
| 2 | 1.000000 | 0.570000 | 0.694242 | 0.264242 | `primary_dyadic` | `DyadicPrimePowerColdWindowCascadeExclusionLemma` |
| 3 | 0.630930 | 0.200930 | 0.438018 | 0.008018 | `epsilon_sensitive_odd` | `OddPrimePowerCascadeEpsilonSavingLedgerForP3P5` |
| 5 | 0.430677 | 0.000677 | 0.298994 | -0.131006 | `block_size_sensitive` | `PrimePowerBlockSizeReductionToOneTwoStepLedger` |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `SmallPrimePowerTargetImported` | `true` | `false` | 上一层已把共同核预算主攻点压成 p=2,3,5 小素数幂级联表。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235` |
| `P235DangerousSetIdentified` | `true` | `true` | 全分组模型中超过 alpha 的底数恰为 2、3、5。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235` |
| `ColdHotGateAvailable` | `true` | `false` | 任何小素数幂级联若造成终端窗口过密，应回流热核心而不是留在冷供给。 | `TerminalColdWindowCompatibilityAntiCascadeLemma` |
| `P5ReducedToBlockSizeControl` | `true` | `true` | p=5 只在任意大块分组模型中刚越过阈值；一二步模型已低于 alpha。 | `PrimePowerBlockSizeReductionToOneTwoStepLedger` |
| `P3ReducedToSmallEpsilonSaving` | `true` | `true` | p=3 在一二步模型只超出 alpha 约 0.008018，是弱奇素数危险。 | `OddPrimePowerCascadeEpsilonSavingLedgerForP3P5` |
| `P2PrimaryCascadeIdentified` | `true` | `true` | p=2 在一二步模型仍超出 alpha 约 0.264242，是唯一强主危险。 | `DyadicPrimePowerColdWindowCascadeExclusionLemma` |
| `BlockSizeReductionProved` | `false` | `false` | 尚未证明冷历史可统一降到一二步，或大块必触发热/固定回流。 | `PrimePowerBlockSizeReductionToOneTwoStepLedger` |
| `OddPrimeEpsilonSavingProved` | `false` | `false` | 尚未给出 p=3 所需的微小指数节省或冷窗口反级联。 | `OddPrimePowerCascadeEpsilonSavingLedgerForP3P5` |
| `DyadicCascadeExclusionProved` | `false` | `false` | 尚未排除 dyadic 冷窗口级联；这是当前最窄主硬点。 | `DyadicPrimePowerColdWindowCascadeExclusionLemma` |
| `SmallPrimePowerCascadeTableProved` | `false` | `false` | p=2 主危险与 p=3/5 辅助账本未闭合。 | `DyadicPrimePowerColdWindowCascadeExclusionLemma AND OddPrimePowerCascadeEpsilonSavingLedgerForP3P5 AND PrimePowerBlockSizeReductionToOneTwoStepLedger` |
| `PrefixBranchingKernelMultiplicityBudgetProved` | `false` | `false` | 小素数幂表未闭合，因此共同核重数预算仍未闭合。 | `PrefixBranchingKernelMultiplicityBudgetLedger` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `DyadicPrimePowerColdWindowCascadeExclusionLemma AND TerminalColdWindowCompatibilityAntiCascadeLemma AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`DyadicPrimePowerColdWindowCascadeExclusionLemma`。
- 并行保留：
  - `OddPrimePowerCascadeEpsilonSavingLedgerForP3P5`
  - `PrimePowerBlockSizeReductionToOneTwoStepLedger`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `PrefixBranchingKernelMultiplicityBudgetLedger`
  - `ColdHistoryPrefixBranchingHotOrFixedReturnLemma`
  - `DivisorCompatibleColdHistoryTreePackingBound`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json` | `dbc983163e64456b63a6be5e99375fabb7ddaf8aa17490fd9fdf42d664c6e129` |
| `docs/monograph/prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json` | `e23de7a05131cc7f1bfd46de5f14e5168fd0c9819cf61bfa2e32804fba127814` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `experiments/prime_matrix_strict_small_prime_power_cascade_attack_router.py` | `540bf7e83e618da74cf612b7e519d93b7db06089b189ba58304518736de686a6` |
