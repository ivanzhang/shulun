# Prime Matrix strict product-window 端点公式绑定路由器

**状态：** `product_window_formula_binding_reduced_to_generator_artifact_or_definition_appendix_open`

`ProductWindowEndpointDyadicUpdateFormulaBindingLedger` 不能由当前语料直接闭合。现有材料只说 `I_W` 的端点继承自 product window ledger，但没有给出 machine-readable 的端点更新公式、舍入方向、规范化表示和 `C_core(W)` 阈值绑定。已闭合的 dyadic 取整交换律可作为后端引理，但还需要新增 `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix`，否则公式失败必须进入边界相位缺陷路由。

```text
terminal_window_object_exists=true
descriptive_product_window_references_found=true
machine_readable_endpoint_generator_found=false
product_window_endpoint_formula_binding_proved=false
cold_core_threshold_order_invariance_proved=false
row_column_unconditional_closed=false
```

## 语料命中

| file | needle | binding_strength |
|---|---|---|
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | `product window ledger` | `descriptive_reference_only` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | `I_W` | `descriptive_reference_only` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.md` | `Y_W` | `descriptive_reference_only` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | `product window ledger` | `descriptive_reference_only` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.md` | `I_W` | `descriptive_reference_only` |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | `product window ledger` | `descriptive_reference_only` |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | `I_W` | `descriptive_reference_only` |
| `experiments/prime_matrix_strict_scaled_terminal_core_divisor_window_router.py` | `Y_W` | `descriptive_reference_only` |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | `product window ledger` | `descriptive_reference_only` |
| `experiments/prime_matrix_strict_formal_unit_sparse_history_multiplicity_router.py` | `I_W` | `descriptive_reference_only` |

## 需要补齐的生成器 schema

| field | required_content | why_needed |
|---|---|---|
| `base_window` | base endpoints Y_0^-,Y_0^+ with integer or dyadic-rational representation | 确定所有 I_W 的共同来源。 |
| `history_update` | for each child multiplier m, exact endpoint update rule and rounding direction | 判断不同历史顺序是否可能改变端点。 |
| `dyadic_specialization` | for m=2^e, update reduces to outward scaling by 2^e | 把 dyadic 取整结合律接到当前 I_W。 |
| `normalization` | all stepwise endpoints are normalized to the same final representation | 排除因中间舍入格式造成的伪顺序差异。 |
| `threshold_binding` | C_core(W) is a function of normalized final window scale, or defects are registered | 不仅端点要交换，冷阈值也要随 dyadic 重排不变。 |
| `defect_return` | if any field fails, discrepancy routes to boundary phase defect/PDEC/hot core | 避免公式绑定失败变成自由容量。 |

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `FormulaBindingTargetImported` | `true` | `false` | 上一层已把 dyadic 端点交换律压成 product-window 端点公式绑定。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `TerminalWindowExists` | `true` | `true` | I_W 已作为终端核心窗口对象存在。 | `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix` |
| `DescriptiveProductWindowReferencesFound` | `true` | `true` | 现有语料有 product-window 文字引用，但不是端点生成器。 | `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix` |
| `DyadicRoundingConditionalLemmaImported` | `true` | `true` | 若端点公式绑定到 dyadic 外向缩放，交换律已经由取整结合律支付。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `MachineReadableEndpointGeneratorFound` | `false` | `false` | 当前语料没有可复核的端点更新公式/生成器/hash。 | `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix` |
| `ThresholdBindingFound` | `false` | `false` | 当前语料没有把 C_core(W) 绑定到规范化终端窗口尺度。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `FormulaFailureDefectRouteRegistered` | `true` | `false` | 若生成器不能满足 dyadic 外向缩放，差异必须回流边界相位缺陷。 | `DyadicBoundaryRoundingPhaseDefectPDECRoute` |
| `ProductWindowEndpointDyadicUpdateFormulaBindingProved` | `false` | `false` | 生成器/定义附录和阈值绑定未补齐，公式绑定不能关闭。 | `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix AND ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `DyadicProductWindowEndpointCommutativityLedgerProved` | `false` | `false` | 公式绑定未闭合，因此端点交换律仍未无条件接回 I_W。 | `DyadicProductWindowEndpointCommutativityLedger` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix AND DyadicPathDependentColdWindowPhaseDefectPDECRoute AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix`。
- 并行保留：
  - `ColdCoreThresholdDyadicOrderInvarianceBindingLedger`
  - `DyadicBoundaryRoundingPhaseDefectPDECRoute`
  - `DyadicPathDependentColdWindowPhaseDefectPDECRoute`
  - `DyadicProductWindowEndpointCommutativityLedger`
  - `DyadicPrimePowerColdWindowCascadeExclusionLemma`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `docs/monograph/prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json` | `defb123fedb4526b578e6dc01d989c696788e013fcd9db77f4b0f609186c52ea` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json` | `2c0a5401dc9e7f7158cd30e758f88f5a07f68460712f611452ff609ae3b7ddbb` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `experiments/prime_matrix_strict_product_window_endpoint_formula_binding_router.py` | `345882f63f0806775de127066b5a4ce2b4501455e60241360daced59152fb46a` |
