# Prime Matrix strict 冷窗口兄弟收费/热回流账本路由器

**状态：** `cold_window_sibling_charging_ledger_closed_numeric_envelope_open`

`CanonicalColdWindowSiblingChargingOrHotReturnLedger` 可作为账本规则关闭：同一父前缀 `U` 下，所有兄弟窗口不能只逐个检查局部冷，而必须整体比较 `sum_child C_core(W)` 与父级整族预算 `C_sib(U)`。若整族收费超出预算，超出部分必须回流热核心、固定历史或 PDEC/ColumnCRT；若同一终端核心被多个孩子重复收费，重叠债也必须登记为命名回流。这样反级联的逻辑出口闭合，但还没有给出 `C_sib(U)` 的同参数数值表，所以终端反级联和行/列命题仍未无条件闭合。

```text
sibling_charging_target_imported=true
family_cold_predicate_defined=true
family_hot_return_registered=true
overlap_return_registered=true
canonical_cold_window_sibling_charging_ledger_closed=true
sibling_cold_core_threshold_numeric_envelope_proved=false
terminal_cold_window_anticascade_proved=false
row_column_unconditional_closed=false
```

## 账本规则

| rule | definition | effect |
|---|---|---|
| `sibling family` | children W=U*g sharing the same prefix U and residual frequency H_U | all sibling cold charges are compared in one parameter ledger |
| `family cold` | sum_{W child of U} C_core(W) <= C_sib(U) | the whole sibling family may remain in cold supply |
| `family hot return` | sum_{W child of U} C_core(W) > C_sib(U) | the excess is not cold supply; it routes to hot core/PDEC/SAE |
| `overlap return` | same terminal core charged through multiple child windows | overlap debt is registered as fixed-history or ColumnCRT return |
| `same-parameter discipline` | C_core(W), C_sib(U), and T_PDEC(W) use the same Lambda/PDEC ledger | prevents optimizing local and family budgets under different parameters |

## 样本收费

| child count | per child C_core | local all cold | C_sib(parent) | family charge | family cold | registered return |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 1 | `true` | 6 | 4 | `true` | 0 |
| 8 | 1 | `true` | 6 | 8 | `false` | 2 |
| 8 | 1 | `true` | 10 | 8 | `true` | 0 |
| 16 | 1 | `true` | 10 | 16 | `false` | 6 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `SiblingChargingTargetImported` | `true` | `false` | 上一层已把终端反级联压成兄弟窗口收费账本。 | `CanonicalColdWindowSiblingChargingOrHotReturnLedger` |
| `FamilyColdPredicateDefined` | `true` | `true` | 同父前缀兄弟窗口必须整体比较 sum C_core。 | `CanonicalColdWindowSiblingChargingOrHotReturnLedger` |
| `FamilyHotReturnRegistered` | `true` | `true` | 整族收费超过 C_sib(U) 时不能继续进入冷供给。 | `TerminalCoreHotDivisorWindowPDECorSAE OR FixedTypeHistoryPDECExclusion` |
| `OverlapReturnRegistered` | `true` | `true` | 重复收费同一终端核心会登记为固定历史/ColumnCRT 回流。 | `FixedTypeHistoryPDECExclusion` |
| `CanonicalColdWindowSiblingChargingClosed` | `true` | `true` | 兄弟窗口从局部冷升级为整族收费/热回流二分。 | `SiblingColdCoreThresholdNumericEnvelopeTable` |
| `SiblingNumericEnvelopeProved` | `false` | `false` | 尚未给出 C_sib(U) 的同参数数值表或全局求和界。 | `SiblingColdCoreThresholdNumericEnvelopeTable` |
| `TerminalColdWindowAntiCascadeProved` | `false` | `false` | 收费账本闭合，但数值包、热核心和固定历史排斥仍未完成。 | `SiblingColdCoreThresholdNumericEnvelopeTable AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的最终矛盾。 | `SiblingColdCoreThresholdNumericEnvelopeTable AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`SiblingColdCoreThresholdNumericEnvelopeTable`。
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
| `docs/monograph/prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json` | `c2ef211342a04f992f35f62a595d3c1647663d1a9fde5d1e78ff57c735bf63d6` |
| `experiments/prime_matrix_strict_cold_window_sibling_charging_router.py` | `c8fd343d79fdec4fe73d058d50c03fb9dcdb1bc17ac198d96b4885363fc4cdf0` |
