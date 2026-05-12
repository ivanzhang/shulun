# Prime Matrix strict actual constructor formula line 路由器

**状态：** `strict_actual_constructor_formula_line_reduced_to_explicit_alpha_delta_rule_open`

`ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter` 被压到显式 `alpha/delta` primitive constructor rule 及其域准入、行输出和失败回流字段。当前最窄点是 `ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter`；没有这个规则，源表第一行仍不能成立。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
actual_constructor_formula_line_router_closed=true
explicit_alpha_delta_primitive_constructor_rule_proved=false
actual_noncanonical_primitive_constructor_formula_line_proved=false
pre_cauchy_constructor_declaration_line_proved=false
actual_noncanonical_primitive_emitter_source_table_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 公式律

The actual constructor formula line must be an explicit rule that, before Cauchy/dispersion, maps each admissible source tuple to alpha/delta primitive summands and emits `(u,v)`, branch key, sign and local factor. It cannot be recovered from payment data, zero-row geometry, or external spectral estimates.

## 2. 公式行内部拆分

拆分前：

```text
ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter
```

拆分后：

```text
ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND ConstructorDomainCleanCoreMembershipLedger AND ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND ConstructorFormulaFailureReturnTagsLedger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ActualConstructorFormulaLineTargetActive` | `true` | `false` | 上一层 declaration line 已把 strict 自足可用来源压到 actual noncanonical constructor formula line。 | ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter |
| `FormulaLineIsNotExistenceName` | `true` | `true` | 公式行必须是可展开的显式 constructor rule，不是“存在某 source”的标签。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND ConstructorDomainCleanCoreMembershipLedger AND ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND ConstructorFormulaFailureReturnTagsLedger |
| `ExternalLemmasDoNotEmitRowsImported` | `true` | `true` | 外部 DI/BFI/Kuznetsov 处理给定系数后的平均，不能输出 alpha/delta primitive rows。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。 |
| `ReversePaymentCannotDefineFormulaImported` | `true` | `true` | 从 Gamma/payment/fiber skeleton 反推公式不唯一；不能把后验原像选择当 constructor rule。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。 |
| `ZeroRowGeometryCannotDefineFormulaImported` | `true` | `true` | 早期零行几何只给 unsigned covering/Phi 基底，不定义 signed alpha/delta constructor rule。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。 |
| `SourceLoopCannotSelfGenerateFormula` | `true` | `true` | constructor、formula、emitter、origin ledger 的等价环不能生成 formula line。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。 |
| `ActualNoncanonicalConstructorFormulaCurrentCorpusProved` | `false` | `false` | 当前材料尚未写出 actual noncanonical primitive constructor 的显式 alpha/delta 规则。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter。 |
| `DomainCleanCoreMembershipCurrentCorpusProved` | `false` | `false` | 公式规则的定义域必须正好是当前 clean-core noncanonical emitter 域；当前未证明。 | ConstructorDomainCleanCoreMembershipLedger。 |
| `FormulaEmitsUVKeyRowsCurrentCorpusProved` | `false` | `false` | 当前未证明公式逐行输出 `(u,v)`、branch key、sign 和 local factor。 | ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger。 |
| `FormulaFailureReturnTagsCurrentCorpusProved` | `false` | `false` | 公式不适用、超预算、thin/rejected 或抵消分支的 return tags 尚未逐项闭合。 | ConstructorFormulaFailureReturnTagsLedger。 |
| `ActualConstructorFormulaLineCurrentCorpusProved` | `false` | `false` | 显式规则、域准入、行输出和失败回流四项尚未合取证明。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND ConstructorDomainCleanCoreMembershipLedger AND ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND ConstructorFormulaFailureReturnTagsLedger |

## 4. 下一主攻点

```text
ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter
```
