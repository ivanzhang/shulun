# Prime Matrix strict alpha 侧 primitive rule 路由器

**状态：** `strict_alpha_side_primitive_rule_reduced_to_domain_map_weight_output_return_open`

`ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger` 被继续压成定义域、确定性 alpha row 发射映射、alpha 系数权重公式、逐行 `(u,v)`/key/sign/local-factor 输出和失败命名回流五项。当前最窄点是 `DeterministicAlphaPrimitiveRowEmissionMapLedger`；source tuple 和 formal-unit 数据只锁定输入容器，仍没有生成 alpha primitive rows 的实际规则。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
alpha_side_primitive_rule_router_closed=true
actual_noncanonical_alpha_side_primitive_rule_proved=false
actual_noncanonical_delta_side_primitive_rule_proved=false
explicit_alpha_delta_primitive_constructor_rule_proved=false
actual_noncanonical_primitive_constructor_formula_line_proved=false
actual_noncanonical_primitive_emitter_source_table_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. alpha 规则律

An alpha-side primitive rule is not a source tuple schema and not a disintegration identity. It must, before Cauchy/dispersion and within the same formal unit, take an actual noncanonical source tuple, emit a finite list of alpha primitive rows, assign coefficient weights, output exact `(u,v)`, branch key, sign/local factor, and return every non-admissible case by name.

## 2. alpha 侧内部拆分

拆分前：

```text
ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger
```

拆分后：

```text
ActualNoncanonicalAlphaSourceTupleDomainLedger AND DeterministicAlphaPrimitiveRowEmissionMapLedger AND AlphaPrimitiveCoefficientWeightFormulaLedger AND AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaPrimitiveRuleFailureNamedReturnLedger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AlphaSidePrimitiveRuleTargetActive` | `true` | `false` | 上一层显式 alpha/delta 规则已把当前最窄点固定为 alpha 侧 primitive row 规则。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger |
| `SourceTupleDomainSchemaImported` | `true` | `true` | source tuple/anchor 参数字段、哈希和同 formal unit 纪律可用。 | 这只是定义域容器，不产生 alpha primitive row。 |
| `FormalUnitAndAnchorDisciplineImported` | `true` | `true` | formal-unit source record 与 anchor reconstruction 可锁定 A、D0/K/Omega、phase_rule。 | 仍需把这些字段送入 alpha 行生成算子。 |
| `PreCauchySourceLawFieldsImported` | `true` | `true` | pre-Cauchy 来源律要求 branch key、u/v、sign/local factor 和命名回流字段。 | ActualNoncanonicalAlphaSourceTupleDomainLedger AND DeterministicAlphaPrimitiveRowEmissionMapLedger AND AlphaPrimitiveCoefficientWeightFormulaLedger AND AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaPrimitiveRuleFailureNamedReturnLedger |
| `DisintegrationFormalButNotEmitterImported` | `true` | `true` | signed 解积分只在 actual source measure 已给定后形式闭合，不能生成 alpha 行。 | DeterministicAlphaPrimitiveRowEmissionMapLedger。 |
| `ReversePaymentRecoveryBlockedImported` | `true` | `true` | 不能从 payment Gamma 或有限投影反推唯一 pre-Cauchy primitive summand。 | DeterministicAlphaPrimitiveRowEmissionMapLedger。 |
| `CanonicalTemplateLeakBlocked` | `true` | `true` | canonical RIW/Buchstab 与 formal-unit key 模板只能作作用域内参考，不能跨入 noncanonical alpha 规则。 | AlphaPrimitiveRuleFailureNamedReturnLedger。 |
| `ActualNoncanonicalAlphaSourceTupleDomainCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明 alpha 规则的定义域正好等于 actual noncanonical clean-core source tuples。 | ActualNoncanonicalAlphaSourceTupleDomainLedger。 |
| `DeterministicAlphaPrimitiveRowMapCurrentCorpusProved` | `false` | `false` | 当前材料尚未给出从每个 source tuple 到有限 alpha primitive rows 的确定性发射映射。 | DeterministicAlphaPrimitiveRowEmissionMapLedger。 |
| `AlphaCoefficientWeightFormulaCurrentCorpusProved` | `false` | `false` | 当前材料尚未给出 alpha primitive row 的系数权重公式及其与原始构造量的等式。 | AlphaPrimitiveCoefficientWeightFormulaLedger。 |
| `AlphaRowUVKeySignLocalFactorOutputCurrentCorpusProved` | `false` | `false` | 当前材料尚未证明每条 alpha row 同步输出 exact `(u,v)`、branch key、sign 和 local factor。 | AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger。 |
| `AlphaFailureNamedReturnCurrentCorpusProved` | `false` | `false` | 当前材料尚未逐类关闭 canonical 泄漏、未登记、超预算、thin/rejected/cancelling 的失败回流。 | AlphaPrimitiveRuleFailureNamedReturnLedger。 |
| `AlphaSidePrimitiveRuleCurrentCorpusProved` | `false` | `false` | 定义域、发射映射、权重公式、输出字段和失败回流五项尚未合取证明。 | ActualNoncanonicalAlphaSourceTupleDomainLedger AND DeterministicAlphaPrimitiveRowEmissionMapLedger AND AlphaPrimitiveCoefficientWeightFormulaLedger AND AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaPrimitiveRuleFailureNamedReturnLedger |

## 4. 下一主攻点

```text
DeterministicAlphaPrimitiveRowEmissionMapLedger
```
