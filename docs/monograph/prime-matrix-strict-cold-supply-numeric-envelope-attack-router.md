# Prime Matrix strict 冷供给同参数数值包攻坚路由器

**状态：** `cold_supply_numeric_envelope_reduced_to_effective_pruning_and_numeric_tables_open`

`ColdSupplySameParameterNumericEnvelope` 不能由现有粗历史数包直接闭合。虽然 U_np<=sum_W(T_PDEC(W)-1)C_core(W) 和 Lambda/PDEC 调参纪律已经闭合，但 full-depth 历史数上界 `sum prod A_Lambda` 太宽：即使按最粗常数 Lambda=1，深度 R≈log_2 P 时也给出约 P^3 级别的历史包，远大于 alpha=0.43 的需求阶。因此下一真正硬点不是再调一个常数，而是证明有效冷历史剪枝：大多数形式历史必须因除数窗口不兼容、LCM 高度、热核心或固定历史回流而退出冷供给；同时还要给出 C_core 与 T_PDEC 的同参数数值表。

```text
cold_supply_formula_sync_closed=true
crude_full_depth_history_envelope_rejected_as_sufficient=true
effective_cold_history_pruning_proved=false
cold_supply_same_parameter_numeric_envelope_proved=false
row_column_unconditional_closed=false
```

## 粗包增长审计

| lambda_floor | alphabet_cap_per_layer | full_depth_R_log2P_history_exponent | demand_exponent_alpha | beats_demand_by_crude_count |
|---:|---:|---:|---:|---:|
| 1 | 8 | 3.000000 | 0.430000 | `false` |
| 2 | 32 | 5.000000 | 0.430000 | `false` |
| 4 | 128 | 7.000000 | 0.430000 | `false` |

## 组件表

| component | current_formula | attack_result | next |
|---|---|---|---|
| `history_count` | sum_{r<=R} prod_{i<=r} A_{Lambda_i}, A_{Lambda_i}<=8Lambda_i^2 | crude full-depth envelope is too large | `SameParameterColdHistoryEffectiveDepthCap` |
| `cold_core_capacity` | C_core(W) bounds N_{H_W}(I_W) in the cold branch | formula exists but no same-parameter numeric table | `ColdCoreThresholdFunctionNumericTable` |
| `persistence_threshold` | nonpersistent allowance is (T_PDEC(W)-1)C_core(W) | threshold tradeoff is disciplined but not numeric | `SameParameterPDECThresholdNumericTable` |
| `large or incompatible histories` | hot window or fixed-history recurrence must return to named exits | this is the only way to shrink the crude sum without cheating | `EffectiveColdHistoryPruningOrHotFixedReturnTheorem` |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `ColdNumericTargetImported` | `true` | `false` | 上一层已把纯非持久内部缺口压成冷供给同参数数值包。 | `ColdSupplySameParameterNumericEnvelope` |
| `ColdSupplyFormulaClosed` | `true` | `true` | U_np 的求和公式和历史数粗包已经闭合。 | `ColdSupplySameParameterNumericEnvelope` |
| `SameParameterDisciplineClosed` | `true` | `true` | Lambda/PDEC 阈值不能自由调参；调参成本已锁入同一账本。 | `ColdSupplySameParameterNumericEnvelope` |
| `IteratedProductLedgerImported` | `true` | `true` | 历史深度和字母表损耗由 prod A_Lambda 显式登记。 | `EffectiveColdHistoryPruningOrHotFixedReturnTheorem` |
| `ColdHotSplitImported` | `true` | `true` | 单历史容量已拆成冷窗口或热核心回流。 | `ColdCoreThresholdFunctionNumericTable OR TerminalCoreHotDivisorWindowPDECorSAE` |
| `CrudeFullDepthHistoryEnvelopeRejected` | `true` | `true` | 只用 full-depth 历史数粗包，增长阶远大于 alpha=0.43 的需求阶，不能证明数值反超。 | `EffectiveColdHistoryPruningOrHotFixedReturnTheorem` |
| `EffectiveColdHistoryPruningProved` | `false` | `false` | 尚未证明大多数形式历史因除数窗口不兼容、LCM 高度、热核心或固定历史而退出冷供给。 | `EffectiveColdHistoryPruningOrHotFixedReturnTheorem` |
| `ColdCoreThresholdNumericTableProved` | `false` | `false` | 尚未给出同参数 C_core(W) 的可求和数值表。 | `ColdCoreThresholdFunctionNumericTable` |
| `PDECThresholdNumericTableProved` | `false` | `false` | 尚未给出同参数 T_PDEC(W) 的数值表。 | `SameParameterPDECThresholdNumericTable` |
| `ColdSupplySameParameterNumericEnvelopeProved` | `false` | `false` | 冷供给公式闭合，但有效剪枝、C_core 表、T_PDEC 表都未完成。 | `EffectiveColdHistoryPruningOrHotFixedReturnTheorem AND ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | `EffectiveColdHistoryPruningOrHotFixedReturnTheorem AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`EffectiveColdHistoryPruningOrHotFixedReturnTheorem`。
- 并行保留：
  - `ColdCoreThresholdFunctionNumericTable`
  - `SameParameterPDECThresholdNumericTable`
  - `TerminalCoreHotDivisorWindowPDECorSAE`
  - `FixedTypeHistoryPDECExclusion`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json` | `7c34a1965c8ddc44a43cafb902ae668fb7ed21db3fc6f73cb42716be37c213be` |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-budget-gap-router.json` | `dc5db9c8aa57f3b8c29354615714c6c124f8b8326b288d3b8c7cccec57db62cf` |
| `docs/monograph/prime-matrix-strict-iterated-scaled-core-density-router.json` | `5e2e4c2cac4e9f0e2afcad98e083f52bf5b4e980b7c516d186a934b65ba4f64f` |
| `docs/monograph/prime-matrix-strict-iterated-threshold-collapse-router.json` | `22c87665aa776cfb358736a8c6624361ad9cba95830f46c56ad95bc40ff99e74` |
| `docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-attack-router.json` | `b5d97d9049f35ae7649c8d27932977e68c162e97373651f96fe4d97c90619447` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `experiments/prime_matrix_strict_cold_supply_numeric_envelope_attack_router.py` | `df74c0c24f868226692fdefa3c9fa22e80004c5bbae4342c999883d54835efe8` |
