# Prime Matrix strict 前缀分叉共同核重数预算攻坚路由器

**状态：** `kernel_budget_reduced_to_small_prime_power_cascade_and_fanin_open`

`PrefixBranchingKernelMultiplicityBudgetLedger` 继续压缩为小素数幂级联表。若只看单素数幂 `p^a` 的全有序分组，形式历史数指数为 `log_p 2`；超过 `alpha=0.43` 的底数只有 `p=2,3,5`。若只允许 `p` 与 `p^2` 两种步长，历史数为 Fibonacci(a)，指数为 `log_p phi`，超过 alpha 的底数只有 `p=2,3`。因此大素数幂尾部不再是最窄阻塞；真正危险集中在 `2/3/5` 小素数幂冷窗口级联，以及多源 fan-in 共同核容量预算。当前仍不能声明共同核预算或行/列命题闭合。

```text
prime_power_exponent_screen_closed=true
dangerous_bases_all_grouped_blocks=[2, 3, 5]
dangerous_bases_one_two_blocks=[2, 3]
small_prime_power_cascade_table_proved=false
fanin_kernel_capacity_budget_proved=false
prefix_branching_kernel_multiplicity_budget_proved=false
row_column_unconditional_closed=false
```

## 素数幂指数筛选表

| p | all_grouped_blocks_exponent | all_exceeds_alpha | one_two_blocks_exponent | one_two_exceeds_alpha | alpha |
|---:|---:|---:|---:|---:|---:|
| 2 | 1.000000 | `true` | 0.694242 | `true` | 0.430000 |
| 3 | 0.630930 | `true` | 0.438018 | `true` | 0.430000 |
| 5 | 0.430677 | `true` | 0.298994 | `false` | 0.430000 |
| 7 | 0.356207 | `false` | 0.247294 | `false` | 0.430000 |
| 11 | 0.289065 | `false` | 0.200681 | `false` | 0.430000 |
| 13 | 0.270238 | `false` | 0.187611 | `false` | 0.430000 |
| 17 | 0.244651 | `false` | 0.169847 | `false` | 0.430000 |
| 19 | 0.235409 | `false` | 0.163431 | `false` | 0.430000 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `KernelBudgetTargetImported` | `true` | `false` | 上一层已把前缀分叉的定量缺口压成共同核重数预算。 | `PrefixBranchingKernelMultiplicityBudgetLedger` |
| `PrefixStructuralDichotomyImported` | `true` | `true` | 同前缀分叉无第四出口：LCM、共同核、热核心或固定历史。 | `PrefixBranchingKernelMultiplicityBudgetLedger` |
| `LowKernelPairFanInSplitImported` | `true` | `false` | 共同核已拆为大成对差值锁与多源 fan-in，但两者仍需计数/排斥。 | `MultiSourceKernelFanInSAEOrPDECExclusion AND BoundedQuotientTypeSAEAbsorption` |
| `FiniteQuotientAlphabetImported` | `true` | `false` | 大成对核给 O(Lambda^2) 有限商型；持久型进入固定历史。 | `FixedTypeHistoryPDECExclusion` |
| `PrimePowerExponentScreenClosed` | `true` | `true` | 单素数幂有序分组的指数阈值可显式计算。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235` |
| `AllBlockDangerousBasesReduced` | `true` | `true` | 全分组模型中，超过 alpha=0.43 的单素数底数只剩 2、3、5。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235` |
| `OneTwoBlockDangerousBasesReduced` | `true` | `true` | 只允许 p 与 p^2 的 Fibonacci 模型中，危险底数只剩 2、3。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235` |
| `LargePrimePowerTailSubcriticalInModel` | `true` | `true` | 对 p>=7 的全分组单素数幂模型，指数低于 alpha；它不是最窄阻塞。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235` |
| `PrimePowerCascadeColdWindowExclusionProved` | `false` | `false` | 仍未证明 p=2,3,5 的小素数幂级联不能在冷窗口层叠。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235 AND TerminalColdWindowCompatibilityAntiCascadeLemma` |
| `FanInKernelCapacityBudgetProved` | `false` | `false` | 多源 fan-in 共同核仍缺 SAE/PDEC 容量预算。 | `MultiSourceKernelFanInSAEOrPDECExclusion` |
| `PrefixBranchingKernelMultiplicityBudgetProved` | `false` | `false` | 指数筛选缩小了危险域，但小素数幂表与 fan-in 预算未闭合。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235 AND MultiSourceKernelFanInSAEOrPDECExclusion` |
| `ColdHistoryPrefixBranchingHotOrFixedReturnProved` | `false` | `false` | 共同核预算未闭合，因此前缀分叉引理仍未闭合。 | `ColdHistoryPrefixBranchingHotOrFixedReturnLemma` |
| `DivisorCompatibleColdHistoryTreePackingBoundProved` | `false` | `false` | 前缀分叉与冷窗口反级联未完成，树打包界不能关闭。 | `DivisorCompatibleColdHistoryTreePackingBound` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235 AND TerminalColdWindowCompatibilityAntiCascadeLemma AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`SmallPrimePowerCascadeColdWindowExclusionTableForP235`。
- 并行保留：
  - `MultiSourceKernelFanInSAEOrPDECExclusion`
  - `BoundedQuotientTypeSAEAbsorption`
  - `FixedTypeHistoryPDECExclusion`
  - `PrimePowerCascadeColdWindowExclusionOrCapacityTable`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json` | `dbc983163e64456b63a6be5e99375fabb7ddaf8aa17490fd9fdf42d664c6e129` |
| `docs/monograph/prime-matrix-strict-large-pair-kernel-difference-router.json` | `fc58ab04aae06d90742f61628fa0240994fc110225ce6a1dbce763eb05efe7cc` |
| `docs/monograph/prime-matrix-strict-low-multiplier-common-kernel-router.json` | `314a0d156a5301b0a4eaedfe4c782f06b69c02ff5f2bd8d575e7c3c57e2f54a8` |
| `docs/monograph/prime-matrix-strict-short-window-divisor-density-lcm-router.json` | `b91aa168a84ba29a3c9e6bfb51ad0968b75d625a8864ad9e1d8033574f2ea21e` |
| `experiments/prime_matrix_strict_prefix_branching_kernel_budget_attack_router.py` | `14dad8a1b91961bac8d0410c5852ca0bc68ffb2cb66b3b2e1995af8d816349b2` |
