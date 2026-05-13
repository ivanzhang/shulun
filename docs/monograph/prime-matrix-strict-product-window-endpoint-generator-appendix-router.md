# Prime Matrix strict product-window 端点生成器定义附录路由器

**状态：** `generator_appendix_closed_formula_binding_reduced_to_legacy_equivalence_and_threshold_binding_open`

`ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix` 已由本步补齐：端点生成器采用整数端点外向更新 `left'=floor(left/m)`、`right'=ceil(right/m)`，dyadic 子步 `m=2^e` 因取整结合律只依赖总指数；样本账本已落盘并哈希。但这还没有把旧文所有 `I_W` 记号等价到该生成器，也没有证明 `C_core(W)` 只依赖规范窗口尺度。因此公式绑定的最新剩余为 `LegacyProductWindowNotationEquivalenceAudit` 与 `ColdCoreThresholdDyadicOrderInvarianceBindingLedger`。

```text
endpoint_update_schema_defined=true
generator_sample_ledger_written=true
product_window_endpoint_generator_artifact_or_definition_appendix_closed=true
legacy_product_window_notation_equivalence_proved=false
cold_core_threshold_dyadic_order_invariance_proved=false
row_column_unconditional_closed=false
```

## 生成器 schema

| field | definition | status |
|---|---|---|
| `base_window` | I_empty=(L_0,R_0] represented by integer numerators and common scale_den | `defined` |
| `history_multiplier` | each child contributes a positive integer multiplier m; dyadic child has m=2^e | `defined` |
| `endpoint_update` | left'=floor(left/m), right'=ceil(right/m), scale_den unchanged | `defined` |
| `normalization` | after each update endpoints are stored in the same integer numerator schema | `defined` |
| `dyadic_commutativity` | for dyadic multipliers, final window depends only on sum e_i | `proved_by_rounding_associativity` |
| `defect_return` | any historical use of I_W not matching this generator is a boundary phase defect | `registered_route` |

## 样本账本

- 路径：`data/product-window-endpoint-generator-sample-ledger.json`
- rows: `18`
- sha256: `7a8cd5b0992165d1967c2f9d025d276b1b72250c780fa445d03b47c428575a2b`
- all_step_equals_once: `true`
- all_same_product_equal: `true`

## 判定表

| gate | closed | proved | meaning | remaining |
|---|---:|---:|---|---|
| `GeneratorAppendixTargetImported` | `true` | `false` | 上一层已把 product-window 公式绑定压成生成器或定义附录。 | `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix` |
| `EndpointUpdateSchemaDefined` | `true` | `true` | 本附录定义 base_window、history_multiplier、endpoint_update 与 normalization。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `DyadicRoundingLemmaImported` | `true` | `true` | dyadic 外向取整结合律已由上一层闭合。 | `DyadicProductWindowEndpointCommutativityLedger` |
| `GeneratorSampleLedgerWritten` | `true` | `true` | 样本账本确认逐步更新等于按总乘子一次更新。 | `ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix` |
| `GeneratorArtifactOrDefinitionAppendixClosed` | `true` | `true` | 生成器定义附录和样本账本已落盘，可作为后续公式绑定对象。 | `ProductWindowEndpointDyadicUpdateFormulaBindingLedger` |
| `LegacyNotationEquivalenceProved` | `false` | `false` | 尚未证明旧文中所有 I_W 使用均等同本生成器，或全部缺口已登记为边界缺陷。 | `LegacyProductWindowNotationEquivalenceAudit` |
| `ColdCoreThresholdBindingProved` | `false` | `false` | C_core(W) 尚未绑定为规范窗口尺度函数。 | `ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `ProductWindowEndpointDyadicUpdateFormulaBindingProved` | `false` | `false` | 生成器附录已补齐，但旧记号等价与阈值绑定仍未闭合。 | `LegacyProductWindowNotationEquivalenceAudit AND ColdCoreThresholdDyadicOrderInvarianceBindingLedger` |
| `DyadicPrimePowerColdWindowCascadeExcluded` | `false` | `false` | 公式绑定未完全接回，dyadic 级联仍未排除。 | `DyadicPrimePowerColdWindowCascadeExclusionLemma` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `LegacyProductWindowNotationEquivalenceAudit AND ColdCoreThresholdDyadicOrderInvarianceBindingLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 下一步

- 主攻：`LegacyProductWindowNotationEquivalenceAudit`。
- 并行保留：
  - `ColdCoreThresholdDyadicOrderInvarianceBindingLedger`
  - `DyadicBoundaryRoundingPhaseDefectPDECRoute`
  - `ProductWindowEndpointDyadicUpdateFormulaBindingLedger`
  - `DyadicProductWindowEndpointCommutativityLedger`
  - `DyadicPrimePowerColdWindowCascadeExclusionLemma`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 证据哈希

| file | sha256 |
|---|---|
| `data/product-window-endpoint-generator-sample-ledger.json` | `7a8cd5b0992165d1967c2f9d025d276b1b72250c780fa445d03b47c428575a2b` |
| `docs/monograph/prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json` | `defb123fedb4526b578e6dc01d989c696788e013fcd9db77f4b0f609186c52ea` |
| `docs/monograph/prime-matrix-strict-product-window-endpoint-formula-binding-router.json` | `aaf78bf3a8b79226fc17487b5e64b6bf3781fdd0d3a0e6bba26eb911e0d5af36` |
| `docs/monograph/prime-matrix-strict-scaled-terminal-core-divisor-window-router.json` | `a689365ed710e4e9239a844479f62f45f1cbd1c2f6a1410a349153ddee1b06c0` |
| `experiments/prime_matrix_strict_product_window_endpoint_generator_appendix_router.py` | `bbdf92b82ce2c12d579fd88ac1ce92c5ff8d3bd31bd18d7ed1d29815424b6fc2` |
