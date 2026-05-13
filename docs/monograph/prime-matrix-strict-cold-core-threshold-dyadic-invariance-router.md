# Prime Matrix strict 冷核心阈值 dyadic 顺序不变性绑定路由器

**状态：** `cold_core_threshold_dyadic_invariance_closed_dyadic_cascade_closed_odd_cases_open`

`ColdCoreThresholdDyadicOrderInvarianceBindingLedger` 可以关闭：旧 `C_core(W)` 统一绑定为规范终端除数窗口对象的函数 `C_core^*`，其注册键只含奇核、累计 `v2`、`H_W`、规范化 `I_W` 和全局参数账本，不含 dyadic 子步顺序。由已闭合的端点生成器和取整结合律，同总 `v2` 的 dyadic 重排给出同一 `H_W`、同一 `I_W`、同一阈值，所以冷/热判定也同一。于是 product-window 公式绑定、dyadic 端点交换律和 dyadic 顺序规范化可接回；p=2 的 Fibonacci 有序路径过计数折叠为线性 valuation states，且在 P>=3001 时被 P^0.43 预算吸收。行/列命题仍未无条件闭合，剩余转为 p=3 微小节省与 p=5 大块降阶，以及终端反级联和 DStructure/Rankin 验收门。

```text
legacy_product_window_notation_equivalence_proved=true
endpoint_generator_and_rounding_imported=true
canonical_cold_core_threshold_registry_defined=true
cold_core_threshold_dyadic_order_invariance_proved=true
product_window_endpoint_formula_binding_proved=true
dyadic_product_window_endpoint_commutativity_ledger_proved=true
dyadic_valuation_order_canonicalization_or_phase_defect_proved=true
dyadic_prime_power_cold_window_cascade_excluded=true
small_prime_power_cascade_table_proved=false
row_column_unconditional_closed=false
```

## 阈值注册规范

| field | definition | role |
|---|---|---|
| `canonical_window_key` | (odd kernel, total v2, H_W, normalized I_W, global parameter ledger) | 冷核心阈值的唯一索引；禁止使用 dyadic 子步顺序。 |
| `C_core^*(canonical_window_key)` | registered cap for N_{H_W}(I_W) under the canonical terminal divisor window | 旧 C_core(W) 统一解释为该规范函数值。 |
| `cold predicate` | N_{H_W}(I_W)<=C_core^*(canonical_window_key) | 同总 v2 重排有同一除数宇宙、同一窗口、同一阈值。 |
| `defect return` | any unregistered path-order dependence routes to boundary phase/PDEC/hot core | 阈值绑定失败不能成为自由容量。 |

## dyadic 重排样本

| odd_kernel | base_window | multiset | permutations | windows_equal | keys_equal | canonical_window |
|---|---|---|---:|---:|---:|---|
| `odd-core-A` | `[37, 10000]` | `[2, 4, 8]` | 6 | `true` | `true` | `[0, 157]` |
| `odd-core-B` | `[111, 77777]` | `[2, 2, 16]` | 3 | `true` | `true` | `[1, 1216]` |
| `odd-core-C` | `[5, 4097]` | `[4, 8, 8]` | 3 | `true` | `true` | `[0, 17]` |

## 线性 valuation states 吸收

| P | valuation_states_upper | P^alpha | absorbed | margin |
|---:|---:|---:|---:|---:|
| 3001 | 12 | 31.276949 | `true` | 19.276949 |
| 10007 | 14 | 52.496540 | `true` | 38.496540 |
| 100000 | 17 | 141.253754 | `true` | 124.253754 |
| 1000000 | 20 | 380.189396 | `true` | 360.189396 |
| 1000000000 | 30 | 7413.102413 | `true` | 7383.102413 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `LegacyEquivalenceImported` | `true` | `true` | 旧 I_W/Y_W 记号已等价到规范端点生成器。 | `LegacyProductWindowNotationEquivalenceAudit` |
| `EndpointGeneratorAndRoundingImported` | `true` | `true` | 端点生成器与 dyadic 外向取整结合律均已可引用。 | `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix` |
| `CanonicalColdCoreThresholdRegistryDefined` | `true` | `true` | C_core(W) 被绑定为规范终端除数窗口对象的函数。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `ThresholdKeyIgnoresDyadicOrder` | `true` | `true` | 注册键含总 v2 和规范窗口，不含 dyadic 子步排列。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `ColdHotPredicateOrderInvariant` | `true` | `true` | 同总 v2 重排给出同一 N_{H_W}(I_W) 与同一 C_core 值。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `ProductWindowEndpointFormulaBindingProved` | `true` | `true` | 生成器、旧记号等价、阈值绑定三项已经合并。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `DyadicProductWindowEndpointCommutativityLedgerProved` | `true` | `true` | dyadic 重排不改变终端窗口端点和冷阈值。 | `DyadicProductWindowEndpointCommutativityLedger` |
| `DyadicValuationOrderCanonicalizationProved` | `true` | `true` | 纯 dyadic 有序路径折叠为累计 v2 的 valuation states。 | `DyadicValuationOrderCanonicalizationOrPhaseDefectLedger` |
| `DyadicLinearStatesAbsorbed` | `true` | `true` | 对 P>=3001，线性 valuation states 小于 P^alpha。 | `DyadicPrimePowerColdWindowCascadeExclusionLemma` |
| `DyadicPrimePowerColdWindowCascadeExcluded` | `true` | `true` | p=2 Fibonacci 级过计数已消失；纯 dyadic 主危险关闭。 | `OddPrimePowerCascadeEpsilonSavingLedgerForP3P5 AND PrimePowerBlockSizeReductionToOneTwoStepLedger` |
| `SmallPrimePowerCascadeTableProved` | `false` | `false` | p=3 微小 epsilon 与 p=5 大块降阶仍未闭合。 | `OddPrimePowerCascadeEpsilonSavingLedgerForP3P5 AND PrimePowerBlockSizeReductionToOneTwoStepLedger` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 这只关闭 dyadic 主危险，尚未得到早期零行反例的最终矛盾。 | `SmallPrimePowerCascadeColdWindowExclusionTableForP235 AND TerminalColdWindowCompatibilityAntiCascadeLemma AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`OddPrimePowerCascadeEpsilonSavingLedgerForP3P5`。
- 并行保留：
  - `PrimePowerBlockSizeReductionToOneTwoStepLedger`
  - `TerminalColdWindowCompatibilityAntiCascadeLemma`
  - `SmallPrimePowerCascadeColdWindowExclusionTableForP235`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-dyadic-cold-window-cascade-attack-router.json` | `d5290090d5795c0bc5bb07b97fd80e6abff01e418cf622d478be09d28906c2ff` |
| `docs/monograph/prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json` | `defb123fedb4526b578e6dc01d989c696788e013fcd9db77f4b0f609186c52ea` |
| `docs/monograph/prime-matrix-strict-dyadic-order-canonicalization-attack-router.json` | `79546568237d185e80dbdda61925d826d911b95389b2966ffc575d87cb77140e` |
| `docs/monograph/prime-matrix-strict-legacy-product-window-equivalence-router.json` | `d713760f063f00117cf6564c911523cf43033f612fb2d51e62a37425156f769e` |
| `docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.json` | `a1061abb510efd9743123d49a9e85775f9b27985a51957ab1b976ae3399e1a42` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `docs/monograph/prime-matrix-strict-small-prime-power-cascade-attack-router.json` | `f15e9de9844e1bdbe6a18639043a667a26c58c7b8118a7d473cbae0dac336cab` |
| `experiments/prime_matrix_strict_cold_core_threshold_dyadic_invariance_router.py` | `e0f5c8b84010ea93b56569a723055c337d57dc3e0501b1c0ae3a1b307c714f2f` |
