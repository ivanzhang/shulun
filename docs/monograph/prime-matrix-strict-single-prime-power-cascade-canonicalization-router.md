# Prime Matrix strict 单素数幂级联规范化路由器

**状态：** `single_prime_power_cascade_canonicalized_small_p235_table_closed_fanin_open`

`OddPrimePowerCascadeEpsilonSavingLedgerForP3P5` 与 `PrimePowerBlockSizeReductionToOneTwoStepLedger` 可合并关闭：端点外向取整结合律对任意正整数乘子成立，因此同一素数底 `p` 的任意指数拆分或重排都等价于一次乘以 `p^a`。旧的 p=3 微小 epsilon 风险和 p=5 大块风险都是形式历史顺序过计数；规范化后每个底数只剩 `a+1=O(log P)` 个 valuation states，且对 `P>=3001` 被 `P^0.43` 吸收。所以 `SmallPrimePowerCascadeColdWindowExclusionTableForP235` 在单源素数幂层面关闭。这仍不等于行/列命题闭合，下一真实剩余是多源 fan-in 共同核容量预算及终端反级联。

```text
dyadic_prime_power_cold_window_cascade_excluded=true
general_integer_endpoint_associativity_imported=true
same_prime_power_valuation_canonicalization_closed=true
odd_prime_power_cascade_epsilon_saving_proved=true
prime_power_block_size_reduction_proved=true
small_prime_power_cascade_table_proved=true
prefix_branching_kernel_multiplicity_budget_proved=false
row_column_unconditional_closed=false
```

## 风险指数与规范化后状态

| p | all grouped exponent | one-two exponent | formal exceeds alpha | canonical growth | absorbed |
|---:|---:|---:|---:|---|---:|
| 2 | 1.000000 | 0.694242 | `true` | `O(log P)` | `true` |
| 3 | 0.630930 | 0.438018 | `true` | `O(log P)` | `true` |
| 5 | 0.430677 | 0.298994 | `true` | `O(log P)` | `true` |

## 同素数幂拆分样本

| p | total exponent | ordered compositions | valuation states | windows equal | keys equal | canonical window |
|---:|---:|---:|---:|---:|---:|---|
| 2 | 6 | 32 | 7 | `true` | `true` | `[0, 157]` |
| 3 | 5 | 16 | 6 | `true` | `true` | `[0, 83]` |
| 5 | 4 | 8 | 5 | `true` | `true` | `[0, 80]` |

## valuation states 吸收

| p | P | max exponent | valuation states | P^alpha | absorbed | margin |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3001 | 11 | 12 | 31.276949 | `true` | 19.276949 |
| 2 | 10007 | 13 | 14 | 52.496540 | `true` | 38.496540 |
| 2 | 100000 | 16 | 17 | 141.253754 | `true` | 124.253754 |
| 2 | 1000000 | 19 | 20 | 380.189396 | `true` | 360.189396 |
| 3 | 3001 | 7 | 8 | 31.276949 | `true` | 23.276949 |
| 3 | 10007 | 8 | 9 | 52.496540 | `true` | 43.496540 |
| 3 | 100000 | 10 | 11 | 141.253754 | `true` | 130.253754 |
| 3 | 1000000 | 12 | 13 | 380.189396 | `true` | 367.189396 |
| 5 | 3001 | 4 | 5 | 31.276949 | `true` | 26.276949 |
| 5 | 10007 | 5 | 6 | 52.496540 | `true` | 46.496540 |
| 5 | 100000 | 7 | 8 | 141.253754 | `true` | 133.253754 |
| 5 | 1000000 | 8 | 9 | 380.189396 | `true` | 371.189396 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `DyadicCascadeClosureImported` | `true` | `true` | p=2 主危险已由 dyadic 阈值绑定和 valuation 折叠关闭。 | `DyadicPrimePowerColdWindowCascadeExclusionLemma` |
| `GeneralIntegerEndpointAssociativityImported` | `true` | `true` | floor/ceil 外向端点结合律对任意正整数乘子成立，不只对 2 的幂成立。 | `SinglePrimePowerValuationCanonicalizationLedgerForP235` |
| `SamePrimePowerCanonicalizationClosed` | `true` | `true` | 同一素数底 p 的任意指数拆分只依赖总指数。 | `SinglePrimePowerValuationCanonicalizationLedgerForP235` |
| `P3EpsilonNeedRemoved` | `true` | `true` | p=3 的 0.008018 形式缺口来自顺序拆分过计数，折叠后不再需要额外 epsilon。 | `OddPrimePowerCascadeEpsilonSavingLedgerForP3P5` |
| `P5BlockSizeNeedRemoved` | `true` | `true` | p=5 的大块全分组风险同样折叠到总指数状态。 | `PrimePowerBlockSizeReductionToOneTwoStepLedger` |
| `SmallPrimePowerCascadeTableProved` | `true` | `true` | p=2,3,5 的单素数幂冷窗口级联表已由 valuation 规范化关闭。 | `MultiSourceKernelFanInSAEOrPDECExclusion AND TerminalColdWindowCompatibilityAntiCascadeLemma` |
| `PrefixBranchingKernelMultiplicityBudgetProved` | `false` | `false` | 小素数幂单源危险关闭后，多源 fan-in 共同核容量预算仍开放。 | `MultiSourceKernelFanInSAEOrPDECExclusion AND BoundedQuotientTypeSAEAbsorption` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 共同核 fan-in、终端反级联和 DStructure/Rankin 门仍未完成。 | `PrefixBranchingKernelMultiplicityBudgetLedger AND TerminalColdWindowCompatibilityAntiCascadeLemma AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`MultiSourceKernelFanInSAEOrPDECExclusion`。
- 并行保留：
  - `BoundedQuotientTypeSAEAbsorption`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `PrefixBranchingKernelMultiplicityBudgetLedger`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json` | `c93a11c1f9f9a11728fb454eb16ead7a4cc308bdfcf2647af6dcb20d6f405602` |
| `docs/monograph/prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json` | `defb123fedb4526b578e6dc01d989c696788e013fcd9db77f4b0f609186c52ea` |
| `docs/monograph/prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json` | `e23de7a05131cc7f1bfd46de5f14e5168fd0c9819cf61bfa2e32804fba127814` |
| `docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.json` | `a1061abb510efd9743123d49a9e85775f9b27985a51957ab1b976ae3399e1a42` |
| `docs/monograph/prime-matrix-strict-small-prime-power-cascade-attack-router.json` | `f15e9de9844e1bdbe6a18639043a667a26c58c7b8118a7d473cbae0dac336cab` |
| `experiments/prime_matrix_strict_single_prime_power_cascade_canonicalization_router.py` | `9a61b227a60f534ee499c87e6f9585c1539a042ce92d96ddc5473b37b45e62f1` |
