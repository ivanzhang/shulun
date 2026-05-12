# Prime Matrix strict 显式 alpha/delta 规则路由器

**状态：** `strict_explicit_alpha_delta_rule_reduced_to_two_side_rules_pairing_nonzero_open`

`ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter` 被继续压成 alpha-side 规则、delta-side 规则、Cauchy 前配对兼容和 primitive row 非零/符号/local factor 四项。当前最窄点是 `ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger`；没有 alpha 侧行生成规则，显式构造规则不能开始。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
explicit_alpha_delta_rule_router_closed=true
actual_noncanonical_alpha_side_primitive_rule_proved=false
actual_noncanonical_delta_side_primitive_rule_proved=false
explicit_alpha_delta_primitive_constructor_rule_proved=false
actual_noncanonical_primitive_constructor_formula_line_proved=false
actual_noncanonical_primitive_emitter_source_table_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 规则律

A genuine alpha/delta primitive constructor rule must be two-sided: one rule emits alpha-side primitive rows, one emits delta-side primitive rows, and a pre-Cauchy pairing identity proves they form the actual emitter coefficient. Source tuples and formal-unit records are only containers; signed disintegration is formal only after the source measure exists.

## 2. 显式规则内部拆分

拆分前：

```text
ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter
```

拆分后：

```text
ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND PrimitiveRuleNonzeroSignLocalFactorLedger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ExplicitAlphaDeltaRuleTargetActive` | `true` | `false` | 上一层 actual constructor formula line 已把当前最窄点压成显式 alpha/delta primitive constructor rule。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter |
| `SourceRecordSchemaAvailableButNotRule` | `true` | `true` | formal unit source record 和 source tuple 字段可用，但它们只给参数容器，不给 alpha/delta 生成算子。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger。 |
| `SourceTupleParametersAvailableButNotRows` | `true` | `true` | source tuple/anchor 参数账本可复算几何参数；不能自动生成 signed primitive rows。 | 两侧 primitive rule。 |
| `PreCauchySourceLawFieldImported` | `true` | `true` | pre-Cauchy 来源律已说明规则必须输出 branch key、u/v、sign、local factor 和回流。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND PrimitiveRuleNonzeroSignLocalFactorLedger |
| `PathPartitionCannotReplaceRule` | `true` | `true` | 路径分割依赖已有 alpha/delta 规则；不能反过来作为规则本身。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND PrimitiveRuleNonzeroSignLocalFactorLedger |
| `DisintegrationFormalButNeedsMeasure` | `true` | `true` | 给定 signed source 后解积分形式闭合；但该形式步骤不生成 actual noncanonical signed source measure。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger。 |
| `AlphaSideRuleCurrentCorpusProved` | `false` | `false` | 当前材料未给出 source tuple 到 alpha-side primitive summand 的确定性规则。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger。 |
| `DeltaSideRuleCurrentCorpusProved` | `false` | `false` | 当前材料未给出 source tuple 到 delta-side primitive summand 的确定性规则。 | ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger。 |
| `PairingCompatibilityCurrentCorpusProved` | `false` | `false` | 当前材料未证明 alpha/delta 两侧规则在 Cauchy 前配对成同一个 actual emitter 系数。 | AlphaDeltaPairingCompatibilityBeforeCauchyLedger。 |
| `PrimitiveRuleNonzeroSignLocalFactorCurrentCorpusProved` | `false` | `false` | 当前材料未证明每条 primitive row 的非零、符号和 local factor 规则。 | PrimitiveRuleNonzeroSignLocalFactorLedger。 |
| `ExplicitAlphaDeltaRuleCurrentCorpusProved` | `false` | `false` | 两侧规则、配对兼容和行级非零/符号/local factor 尚未合取证明。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND PrimitiveRuleNonzeroSignLocalFactorLedger |

## 4. 下一主攻点

```text
ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger
```
