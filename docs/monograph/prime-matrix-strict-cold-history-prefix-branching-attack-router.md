# Prime Matrix strict 冷历史前缀分叉攻坚路由器

**状态：** `prefix_branching_reduced_to_kernel_multiplicity_and_cold_window_anticascade_open`

`ColdHistoryPrefixBranchingHotOrFixedReturnLemma` 的结构部分可以闭合：固定前缀 `U` 后，所有子分叉是同一 `H_U=h_0/D(U)` 的短窗口除数，因此其 LCM 被 `H_U` 锚定；增量乘子纪律迫使每个新子分叉要么增加 LCM 高度，要么进入低乘子共同核；低乘子共同核再拆成大成对差值锁或多源 fan-in；超过冷阈值的窗口回流热核心，同商型持久复现回流固定历史。但这还没有给出定量树打包界，因为小素数幂/低乘子级联可能在冷窗口内制造大量低乘子事件。最新最窄剩余是 `PrefixBranchingKernelMultiplicityBudgetLedger`，并必须与 `PrimePowerCascadeColdWindowExclusionOrCapacityTable` 和 `TerminalColdWindowCompatibilityAntiCascadeLemma` 同步闭合。

```text
prefix_branching_structural_dichotomy_closed=true
prefix_branching_kernel_multiplicity_budget_proved=false
prime_power_cascade_excluded=false
terminal_cold_window_anticascade_proved=false
cold_history_prefix_branching_hot_or_fixed_return_proved=false
row_column_unconditional_closed=false
```

## 前缀对象

| name | formula | status | meaning |
|---|---|---|---|
| `prefix_residual_frequency` | `H_U=h_0/D(U)` | `closed_interface` | 同一前缀 U 下，所有子分叉共享同一个缩频 formal unit。 |
| `child_divisor_set` | `A_U(Y)={g: Y<g<=2Y, g\|H_U, U*g remains cold-admissible}` | `closed_definition` | 前缀分叉不是任意字母表，而是 H_U 的短窗口除数子集。 |
| `lcm_anchor` | `lcm(A_U(Y)) \| H_U` | `imported_closed` | 同前缀子分叉的 LCM 被锚定在同一 H_U 上。 |
| `incremental_multiplier_split` | `mu_t=g_t/gcd(g_t,L_{t-1})` | `imported_closed` | 分叉要么贡献新 LCM 乘子，要么产生低乘子共同核。 |
| `cold_hot_gate` | `N_{H_U}(I_U)<=C_core(U) or hot-core return` | `imported_dichotomy` | 超过冷阈值的窗口不能留在冷供给内，必须回流热核心。 |
| `prefix_branching_bound_needed` | `\|A_U(Y)\| <= floor(log H_U/log Lambda)+K_kernel(U,Y,Lambda)+K_fixed(U)+C_core(U)` | `open_quantitative_bound` | 需要定量限制低乘子共同核、固定历史与冷窗口容量，才能关闭分叉引理。 |

## 阻塞形态

| case | shape | why_dangerous | required_input |
|---|---|---|---|
| `prime_power_cascade` | `g_t in {2,4,8,...} or repeated small-prime blocks` | LCM 增长慢，低乘子共同核多，正是前一步 Fibonacci/P^0.694 阻塞的树形版本。 | `PrimePowerCascadeColdWindowExclusionOrCapacityTable` |
| `large_pair_same_quotient` | `g_i=k b, g_t=k(b+a) with fixed small (b,a)` | 同一有限商型若持久复现，就不是冷分叉，而是固定历史 ColumnCRT/PDEC。 | `FixedTypeHistoryPDECExclusion` |
| `fanin_kernel_cloud` | `K_t divides lcm_i gcd(g_t,g_i) but no single pair dominates` | 多源扇入可能绕开单对差值锁，必须有 SAE/PDEC 容量账本。 | `MultiSourceKernelFanInSAEOrPDECExclusion` |
| `terminal_cold_window_crowding` | `many compatible children stay below hot threshold in adjacent windows` | 如果冷窗口之间没有反级联限制，局部冷可能层叠成全局过大树。 | `TerminalColdWindowCompatibilityAntiCascadeLemma` |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `PrefixBranchingTargetImported` | `true` | `false` | 上一层把除数兼容树打包压到前缀分叉/冷窗口反级联。 | `ColdHistoryPrefixBranchingHotOrFixedReturnLemma` |
| `SamePrefixLCMAnchorClosed` | `true` | `true` | 同一前缀 U 下的全部子分叉除数 LCM 整除同一个 H_U。 | `ShortWindowLCMMultiplierDisciplineForFrequencyH` |
| `IncrementalMultiplierSplitClosed` | `true` | `true` | 子分叉要么推动 LCM 高度，要么产生低乘子共同核。 | `DenseShortWindowLCMLowerBoundAfterKernelCompression OR LowMultiplierCommonKernelColumnCRTOrPDECRoute` |
| `LowMultiplierKernelSplitImported` | `true` | `false` | 低乘子共同核已拆成大成对差值锁或多源 fan-in，但两者尚未排斥。 | `LargePairKernelDifferenceColumnCRTExclusion OR MultiSourceKernelFanInSAEOrPDECExclusion` |
| `FiniteQuotientFixedHistoryRouteImported` | `true` | `false` | 大成对核同商型持久复现进入固定历史 PDEC/ColumnCRT。 | `FixedTypeHistoryPDECExclusion` |
| `ColdHotGateImported` | `true` | `false` | 超过冷阈值的终端窗口回流热核心，不能继续计入冷历史树。 | `TerminalCoreHotDivisorWindowPDECorSAE` |
| `PrefixBranchingStructuralDichotomyClosed` | `true` | `true` | 同前缀过多分叉已无第四出口：LCM、低乘子共同核、热核心或固定历史。 | `PrefixBranchingKernelMultiplicityBudgetLedger` |
| `PrefixBranchingKernelMultiplicityBudgetProved` | `false` | `false` | 尚未给出低乘子共同核/多源扇入在冷窗口内的统一计数预算。 | `PrefixBranchingKernelMultiplicityBudgetLedger` |
| `PrimePowerCascadeExcluded` | `false` | `false` | 素数幂和小乘子级联仍是最危险反例形态，必须用冷窗口反级联或容量表排除。 | `PrimePowerCascadeColdWindowExclusionOrCapacityTable` |
| `ColdHistoryPrefixBranchingHotOrFixedReturnProved` | `false` | `false` | 结构三分法已闭合，定量预算和素数幂反级联未闭合。 | `PrefixBranchingKernelMultiplicityBudgetLedger AND PrimePowerCascadeColdWindowExclusionOrCapacityTable AND TerminalColdWindowCompatibilityAntiCascadeLemma` |
| `DivisorCompatibleColdHistoryTreePackingBoundProved` | `false` | `false` | 前缀分叉引理未闭合，因此树打包界不能关闭。 | `ColdHistoryPrefixBranchingHotOrFixedReturnLemma AND TerminalColdWindowCompatibilityAntiCascadeLemma` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `PrefixBranchingKernelMultiplicityBudgetLedger AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`PrefixBranchingKernelMultiplicityBudgetLedger`。
- 并行保留：
  - `PrimePowerCascadeColdWindowExclusionOrCapacityTable`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `LowMultiplierCommonKernelColumnCRTOrPDECRoute`
  - `LargePairKernelDifferenceColumnCRTExclusion`
  - `MultiSourceKernelFanInSAEOrPDECExclusion`
  - `FixedTypeHistoryPDECExclusion`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json` | `dbc983163e64456b63a6be5e99375fabb7ddaf8aa17490fd9fdf42d664c6e129` |
| `docs/monograph/prime-matrix-strict-effective-cold-history-pruning-router.json` | `72d7aeeb5a09864efcb9cd729d4d5331b1adfb780ec33b3a1ae29dfe6e67431b` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-density-transfer-router.json` | `f2b0c000ddb05b2504eb547a318d94a219fd70ac27ff34089b01524caa1688f7` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-type-columncrt-router.json` | `2604e2de93bc17bbe7678dddccf958b8a747714286d2c1ab8d5734246be78733` |
| `docs/monograph/prime-matrix-strict-large-pair-kernel-difference-router.json` | `fc58ab04aae06d90742f61628fa0240994fc110225ce6a1dbce763eb05efe7cc` |
| `docs/monograph/prime-matrix-strict-low-multiplier-common-kernel-router.json` | `314a0d156a5301b0a4eaedfe4c782f06b69c02ff5f2bd8d575e7c3c57e2f54a8` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-short-window-divisor-density-lcm-router.json` | `b91aa168a84ba29a3c9e6bfb51ad0968b75d625a8864ad9e1d8033574f2ea21e` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-history-router.json` | `6cbb750d3888d20ef1c7267231ddfb8490b1efc92b0edda308ec96f1d40905b2` |
| `experiments/prime_matrix_strict_cold_history_prefix_branching_attack_router.py` | `fa98cb3e58e06a4754ad29c3a747cefe82363abbc7d9363261a3e02b2e5d78a5` |
