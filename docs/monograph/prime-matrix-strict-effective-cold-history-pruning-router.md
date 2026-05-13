# Prime Matrix strict 有效冷历史剪枝路由器

**状态：** `effective_cold_history_pruning_reduced_to_divisor_compatible_tree_packing_open`

`EffectiveColdHistoryPruningOrHotFixedReturnTheorem` 已压成除数兼容树打包界。每个冷历史词 W 不只是形式字母串，必须满足 `D(W)|h_0`，并且终端核心落在 `H_W=h_0/D(W)` 的冷除数窗口内；不满足冷条件则回流热核心，持久同型复现回流固定历史 PDEC/ColumnCRT，过密除数窗口回流 LCM/共同核。当前真正未证的是：在这些兼容条件下，冷历史树的加权总量是否足够小。这个缺口精确命名为 `DivisorCompatibleColdHistoryTreePackingBound`。

```text
effective_pruning_interface_closed=true
divisor_compatible_cold_history_tree_packing_bound_proved=false
effective_cold_history_pruning_proved=false
row_column_unconditional_closed=false
```

## 剪枝方程

| name | formula | status | meaning |
|---|---|---|---|
| `history_product` | `D(W)=prod_i b_i c_i` | `closed` | 每个历史词对应一个确定商型乘积。 |
| `divisor_compatibility` | `D(W)\|h_0 and H_W=h_0/D(W)` | `closed_interface` | 能存活到终端的冷历史必须兼容同一个 formal-unit 频率。 |
| `cold_condition` | `N_{H_W}(I_W)<=C_core(W)` | `closed_dichotomy` | 不满足冷条件的历史进入热核心回流。 |
| `effective_cold_supply` | `U_np<=sum_{W in C_cold(h_0)} (T_PDEC(W)-1)C_core(W)` | `open_bound` | 必须对兼容冷历史树求和，而不是对全部形式历史求和。 |
| `tree_packing_goal` | `sum_{W in C_cold(h_0)} (T_PDEC(W)-1)C_core(W) <= U0(P,z) < M#` | `open_target` | 这是有效剪枝闭合后应提供的数值包。 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `EffectivePruningTargetImported` | `true` | `false` | 上一层已判定粗 full-depth 历史包不足，主攻转为有效冷历史剪枝。 | `EffectiveColdHistoryPruningOrHotFixedReturnTheorem` |
| `DivisorCompatibilityInterfaceClosed` | `true` | `true` | 每个终端历史词 W 必须满足 D(W)\|h_0，且容量落在 H_W=h_0/D(W) 的除数窗口。 | `DivisorCompatibleColdHistoryTreePackingBound` |
| `ColdHotDichotomyImported` | `true` | `true` | 不冷的终端窗口不是供给容量，而是热核心回流。 | `TerminalCoreHotDivisorWindowPDECorSAE` |
| `FiniteDepthProductLedgerImported` | `true` | `true` | 固定商型链严格降高，不能无限递归；阈值坍缩已归入稀疏终端历史。 | `DivisorCompatibleColdHistoryTreePackingBound` |
| `FixedHistoryReturnRegistered` | `true` | `false` | 同一历史或固定商型持久复现进入固定历史 PDEC/ColumnCRT。 | `FixedTypeHistoryPDECExclusion` |
| `LCMKernelReturnRegistered` | `true` | `false` | 除数窗口过密时，LCM 爆炸或低乘子共同核回流已登记。 | `DenseLCMOrLowMultiplierCommonKernelReturn` |
| `DensityLossLedgerAvailable` | `true` | `true` | 固定商型密度传递的显式损耗已登记，可作为树打包权重。 | `DivisorCompatibleColdHistoryTreePackingBound` |
| `DivisorCompatibleColdHistoryTreePackingBoundProved` | `false` | `false` | 尚未证明兼容同一 h_0 且保持冷条件的历史树有足够小的加权总量。 | `DivisorCompatibleColdHistoryTreePackingBound` |
| `ColdHistoryPrefixBranchingHotOrFixedReturnProved` | `false` | `false` | 尚未证明任一前缀下过多冷分叉必触发热核心、LCM 共同核或固定历史回流。 | `ColdHistoryPrefixBranchingHotOrFixedReturnLemma` |
| `EffectiveColdHistoryPruningProved` | `false` | `false` | 接口和回流路线已闭合，但核心树打包/分叉剪枝界尚未证明。 | `DivisorCompatibleColdHistoryTreePackingBound AND ColdHistoryPrefixBranchingHotOrFixedReturnLemma` |
| `ColdSupplyNumericEnvelopeProved` | `false` | `false` | 即便剪枝完成，仍需 C_core 与 T_PDEC 的同参数数值表。 | `DivisorCompatibleColdHistoryTreePackingBound AND ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `DivisorCompatibleColdHistoryTreePackingBound AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`DivisorCompatibleColdHistoryTreePackingBound`。
- 并行保留：
  - `ColdHistoryPrefixBranchingHotOrFixedReturnLemma`
  - `ColdCoreThresholdFunctionNumericTable`
  - `SameParameterPDECThresholdNumericTable`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `DenseLCMOrLowMultiplierCommonKernelReturn`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json` | `86ba2fbc9abd9d917a940525fde0a9db0dd4e70ee94f745a56382fee896d8255` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-density-transfer-router.json` | `f2b0c000ddb05b2504eb547a318d94a219fd70ac27ff34089b01524caa1688f7` |
| `docs/monograph/prime-matrix-strict-fixed-quotient-type-columncrt-router.json` | `2604e2de93bc17bbe7678dddccf958b8a747714286d2c1ab8d5734246be78733` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json` | `2c0a5401dc9e7f7158cd30e758f88f5a07f68460712f611452ff609ae3b7ddbb` |
| `docs/monograph/prime-matrix-strict-iterated-scaled-core-density-router.json` | `5e2e4c2cac4e9f0e2afcad98e083f52bf5b4e980b7c516d186a934b65ba4f64f` |
| `docs/monograph/prime-matrix-strict-iterated-threshold-collapse-router.json` | `22c87665aa776cfb358736a8c6624361ad9cba95830f46c56ad95bc40ff99e74` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-short-window-divisor-density-lcm-router.json` | `b91aa168a84ba29a3c9e6bfb51ad0968b75d625a8864ad9e1d8033574f2ea21e` |
| `experiments/prime_matrix_strict_effective_cold_history_pruning_router.py` | `f205039960f2678ff0d69dcafa37a259a3c8639008d3cb370fc721c317716691` |
