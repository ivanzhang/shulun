# Prime Matrix strict 终端冷窗口反级联攻坚路由器

**状态：** `terminal_cold_window_anticascade_reduced_to_sibling_charging_ledger_open`

`TerminalColdWindowCompatibilityAntiCascadeLemma` 的最窄缺口已定位：现有材料已经规范化端点和 C_core，也关闭了单源小素数幂与多源 fan-in，但局部冷条件 `N_H(I)<=C_core` 本身不能推出兄弟窗口或相邻前缀的全局求和界。若有许多兄弟窗口各自只含 1 个核心且 `C_core>=1`，每个窗口都冷，总冷收费仍可随兄弟数增长。要完成反级联，必须新增 `CanonicalColdWindowSiblingChargingOrHotReturnLedger`：证明兄弟冷窗口的 C_core 总收费可被父级预算控制，或者重叠/过密必回流热核心、固定历史或 PDEC/ColumnCRT。本步给出的是精确剩余原子，不声称反级联或行/列命题已闭合。

```text
effective_pruning_latest_sync_closed=true
canonical_threshold_and_window_imported=true
old_cascade_modes_removed=true
local_cold_predicate_insufficient_for_global_anticascade=true
canonical_cold_window_sibling_charging_isolated=true
terminal_cold_window_anticascade_proved=false
effective_cold_history_pruning_proved=false
row_column_unconditional_closed=false
```

## 局部冷条件不足见证

| siblings | per-window count | C_core | all cold | total cold charge | parent bound without charging |
|---:|---:|---:|---:|---:|---|
| 2 | 1 | 1 | `true` | 2 | `unbounded in sibling_count` |
| 4 | 1 | 1 | `true` | 4 | `unbounded in sibling_count` |
| 8 | 1 | 1 | `true` | 8 | `unbounded in sibling_count` |
| 16 | 1 | 1 | `true` | 16 | `unbounded in sibling_count` |

## 必需账本

| input | statement | status |
|---|---|---|
| `canonical sibling family` | all children of a fixed prefix U are grouped by the same H_U and normalized product-window scale | `available qualitatively` |
| `charging inequality` | sum_child C_core(child) <= C_parent_budget + named hot/fixed/PDEC returns | `missing quantitative ledger` |
| `overlap discipline` | a terminal core charged to multiple child windows must create a fixed-history or ColumnCRT return | `registered but not proved as global bound` |
| `same-parameter numeric table` | C_core and T_PDEC must be evaluated under the same Lambda/PDEC ledger | `open numeric companion` |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `EffectivePruningFrontierImported` | `true` | `true` | 有效剪枝前沿已压缩到终端冷窗口反级联。 | `EffectiveColdHistoryPruningOrHotFixedReturnTheorem` |
| `CanonicalThresholdAndWindowImported` | `true` | `true` | product-window 端点和 C_core 注册键已规范化。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `OldCascadeModesRemoved` | `true` | `true` | 单源小素数幂和多源 fan-in 已不再是独立反级联阻塞。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235 AND MultiSourceKernelFanInSAEOrPDECExclusion` |
| `LocalColdPredicateInsufficient` | `true` | `true` | 局部 N_H(I)<=C_core 不能推出兄弟冷窗口求和界。 | `CanonicalColdWindowSiblingChargingOrHotReturnLedger` |
| `SiblingChargingLedgerIsolated` | `true` | `true` | 必须补兄弟窗口收费或重叠回流账本，才能关闭反级联。 | `CanonicalColdWindowSiblingChargingOrHotReturnLedger` |
| `TerminalColdWindowAntiCascadeProved` | `false` | `false` | 缺少 sum_child C_core(child) 的同参数求和控制。 | `CanonicalColdWindowSiblingChargingOrHotReturnLedger` |
| `EffectiveColdHistoryPruningProved` | `false` | `false` | 反级联、热核心和固定历史排斥仍未完成。 | `CanonicalColdWindowSiblingChargingOrHotReturnLedger AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion` |
| `ColdSupplyNumericEnvelopeProved` | `false` | `false` | 还需 C_core/T_PDEC 同参数数值表接回最终供需余量。 | `ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的最终矛盾。 | `CanonicalColdWindowSiblingChargingOrHotReturnLedger AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`CanonicalColdWindowSiblingChargingOrHotReturnLedger`。
- 并行保留：
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `ColdCoreThresholdFunctionNumericTable`
  - `SameParameterPDECThresholdNumericTable`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json` | `7c34a1965c8ddc44a43cafb902ae668fb7ed21db3fc6f73cb42716be37c213be` |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json` | `c93a11c1f9f9a11728fb454eb16ead7a4cc308bdfcf2647af6dcb20d6f405602` |
| `docs/monograph/prime-matrix-strict-effective-pruning-latest-sync-router.json` | `ed70b01806e4ff545cc7ab3d3d051009e33cf6e1e43190141f5278ed9d73c126` |
| `docs/monograph/prime-matrix-strict-multisource-fanin-small-quotient-router.json` | `89d82ac6d13034c0b3db3d67585df32e9cc2ad534ddec16ddc9c6eb89c22eda4` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json` | `e72a9d55dd3a27c1f9d6287afd6a8debc00a0ebe241977e72e0394bc02c04abf` |
| `experiments/prime_matrix_strict_terminal_cold_window_anticascade_attack_router.py` | `3c639f4338b4fa7e6d00d049932341a2eb62ea5ed0b1787d531d3f9c361d5a6d` |
