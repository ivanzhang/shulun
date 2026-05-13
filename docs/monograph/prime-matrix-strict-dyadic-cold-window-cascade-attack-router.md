# Prime Matrix strict dyadic 冷窗口级联攻坚路由器

**状态：** `dyadic_cascade_reduced_to_order_canonicalization_or_phase_defect_open`

`DyadicPrimePowerColdWindowCascadeExclusionLemma` 的主爆炸源已定位：危险的 Fibonacci 数量来自把同一个 `2^a` 预算有序切成 `1/2` 步，而不是来自不同的 2-adic 终态。若冷可容许性只依赖累计 `v2` 和同一奇核，则所有有序路径必须压缩到 `a+1` 个 valuation states，指数爆炸消失；若两个同总 `v2` 的顺序不能合并，它们必在相位、冷窗口或标签上产生可登记差异，进入 PDEC/ColumnCRT/热核心。因此 dyadic 主硬点被压成 `DyadicValuationOrderCanonicalizationOrPhaseDefectLedger`。

```text
dyadic_dichotomy_closed=true
dyadic_valuation_order_canonicalization_proved=false
dyadic_path_dependent_phase_defect_pdec_route_proved=false
dyadic_prime_power_cold_window_cascade_excluded=false
row_column_unconditional_closed=false
```

## 有序路径过计数

| a=v2(h0) | ordered_one_two_paths | valuation_states | overcount_ratio | asymptotic_exponent | beats_alpha |
|---:|---:|---:|---:|---:|---:|
| 8 | 34 | 9 | 3.777778 | 0.694242 | `true` |
| 16 | 1597 | 17 | 93.941176 | 0.694242 | `true` |
| 24 | 75025 | 25 | 3001.000000 | 0.694242 | `true` |
| 32 | 3524578 | 33 | 106805.393939 | 0.694242 | `true` |
| 40 | 165580141 | 41 | 4038540.024390 | 0.694242 | `true` |
| 48 | 7778742049 | 49 | 158749837.734694 | 0.694242 | `true` |
| 56 | 365435296162 | 57 | 6411145546.701755 | 0.694242 | `true` |
| 64 | 17167680177565 | 65 | 264118156577.923065 | 0.694242 | `true` |

## 二选一路由

| branch | condition | consequence | remaining |
|---|---|---|---|
| `order_canonical` | cold admissibility depends only on cumulative v2 and odd core | ordered Fibonacci paths collapse to at most a+1 valuation states | `PureDyadicValuationStateCompressionLedger` |
| `path_dependent` | two orders with same total v2 give different cold windows or labels | the difference is a phase/window defect, hence must route to PDEC/ColumnCRT/hot core | `DyadicPathDependentColdWindowPhaseDefectPDECRoute` |
| `odd_leakage` | dyadic child contains odd leakage or alternates with odd prime blocks | it exits pure dyadic cascade and returns to p=3/5 epsilon ledger or fan-in budget | `DyadicOddCoreLeakageToOddPrimeEpsilonLedger` |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `DyadicTargetImported` | `true` | `false` | 上一层确认 p=2 是唯一强主危险。 | `DyadicPrimePowerColdWindowCascadeExclusionLemma` |
| `P2PrimaryRiskPinned` | `true` | `true` | 一二步 dyadic Fibonacci 模型仍给 P^0.694，明显超过 alpha=0.43。 | `DyadicPrimePowerColdWindowCascadeExclusionLemma` |
| `DyadicOvercountSourceIdentified` | `true` | `true` | 指数爆炸来自有序分割 2^a 的路径数，而不是来自不同 2-adic 终态数。 | `DyadicValuationOrderCanonicalizationOrPhaseDefectLedger` |
| `PureValuationStateCompressionWouldSuffice` | `true` | `false` | 若冷窗口只依赖累计 v2 和奇核，Fibonacci 路径可压成线性 a+1 个状态。 | `PureDyadicValuationStateCompressionLedger` |
| `PathDependenceForcesPhaseDefect` | `true` | `false` | 若不同顺序不可合并，则必存在相位/窗口/标签差异，可进入 PDEC/ColumnCRT/热核心。 | `DyadicPathDependentColdWindowPhaseDefectPDECRoute` |
| `ColdHotGateImported` | `true` | `false` | dyadic 级联造成过密终端窗口时，必须回流热核心。 | `TerminalCoreHotDivisorWindowPDECorSAE` |
| `FixedHistoryRouteImported` | `true` | `false` | 同一 dyadic 商型持久复现时进入固定历史 PDEC/ColumnCRT。 | `FixedTypeHistoryPDECExclusion` |
| `DyadicDichotomyClosed` | `true` | `true` | 纯 dyadic 级联只剩规范化折叠或路径相位缺陷两类，奇因子泄漏回到 p=3/5。 | `DyadicValuationOrderCanonicalizationOrPhaseDefectLedger` |
| `DyadicValuationOrderCanonicalizationProved` | `false` | `false` | 尚未证明真实冷窗口对 dyadic 顺序不敏感，或给出顺序敏感的缺陷路由证书。 | `DyadicValuationOrderCanonicalizationOrPhaseDefectLedger` |
| `DyadicPrimePowerColdWindowCascadeExcluded` | `false` | `false` | dyadic 主危险已压到规范化/相位缺陷二选一，但二选一未闭合。 | `DyadicValuationOrderCanonicalizationOrPhaseDefectLedger AND TerminalColdWindowCompatibilityAntiCascadeLemma` |
| `SmallPrimePowerCascadeTableProved` | `false` | `false` | dyadic 未闭合，故 p=2,3,5 小素数表仍未闭合。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235` |
| `PrefixBranchingKernelMultiplicityBudgetProved` | `false` | `false` | 小素数幂表未闭合，共同核重数预算仍未闭合。 | `PrefixBranchingKernelMultiplicityBudgetLedger` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `DyadicValuationOrderCanonicalizationOrPhaseDefectLedger AND TerminalColdWindowCompatibilityAntiCascadeLemma AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`DyadicValuationOrderCanonicalizationOrPhaseDefectLedger`。
- 并行保留：
  - `DyadicPathDependentColdWindowPhaseDefectPDECRoute`
  - `PureDyadicValuationStateCompressionLedger`
  - `DyadicOddCoreLeakageToOddPrimeEpsilonLedger`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `DivisorCompatibleColdHistoryTreePackingBound`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-type-columncrt-router.json` | `2604e2de93bc17bbe7678dddccf958b8a747714286d2c1ab8d5734246be78733` |
| `docs/monograph/prime-matrix-strict-prefix-branching-kernel-budget-attack-router.json` | `e23de7a05131cc7f1bfd46de5f14e5168fd0c9819cf61bfa2e32804fba127814` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-small-prime-power-cascade-attack-router.json` | `f15e9de9844e1bdbe6a18639043a667a26c58c7b8118a7d473cbae0dac336cab` |
| `experiments/prime_matrix_strict_dyadic_cold_window_cascade_attack_router.py` | `c677be9c7ec10a7d8a0c207e9c34ddfb0d516deee04177889d8d06f1c81f8b4f` |
