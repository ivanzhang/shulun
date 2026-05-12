# Prime Matrix strict 逐行 signed alpha 权重公式路由器

**状态：** `pointwise_signed_alpha_weight_formula_reduced_to_primitive_summand_expression_open`

本步继续硬攻逐行 signed 权重公式。结论是：当前材料只有权重律的字段分解和反推禁令，没有 primitive summand 级 signed coefficient 表达式。source table、constructor formula 和 pre-Cauchy declaration 都指向同一个前推前原始表达式缺口；独立恒等式路线则回到终端固定点。因此最新最精确单点是 actual noncanonical primitive summand signed weight expression before pushforward。

```text
pointwise_signed_alpha_weight_formula_router_closed=true
exact_alpha_signed_weight_formula_proved=false
alpha_primitive_coefficient_weight_formula_proved=false
actual_noncanonical_primitive_constructor_formula_line_proved=false
primitive_summand_signed_weight_expression_proved=false
pointwise_nonrecursive_signed_alpha_weight_formula_proved=false
pointwise_signed_alpha_coefficient_value_table_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 前沿压缩

PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow 不能由权重律名称、source table 名称或独立恒等式分类自动推出；它必须先提交 `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`，也就是在 Phi/payment 推前之前给出 actual noncanonical primitive summand 的 signed coefficient 表达式。

## 2. primitive summand 表达式字段

| field | meaning |
| --- | --- |
| `primitive_summand_row` | pre-pushforward、pre-Cauchy 的 actual noncanonical primitive summand 行。 |
| `alpha_delta_side` | 标明该行属于 alpha 侧或 delta 侧，并给出配对规则。 |
| `signed_weight_expression` | 该 summand 的 signed coefficient 的闭式表达式或有限递推式。 |
| `local_factor_product` | 符号、筛因子、截断因子、branch local factor 的乘积口径。 |
| `uv_key_output` | 同一行同时输出 exact `(u,v)` 与 branch key。 |
| `identity_before_pushforward` | 证明表达式在 Phi/payment 推前之前已经成立。 |
| `no_canonical_or_external_leak` | 证明没有借用 canonical scoped 模板、外部谱黑箱或 terminal 反推。 |
| `failure_return` | 公式不适用、local factor 为零、符号冲突或超预算时的命名回流。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PointwiseWeightFormulaTargetActive` | `true` | `false` | 上一层已把 signed value table 的首字段压成逐行 signed alpha 权重公式。 | PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow |
| `ExactWeightFormulaStillOpen` | `true` | `false` | alpha signed weight law 已明确需要 ExactAlphaSignedWeightFormulaLedger。 | ExactAlphaSignedWeightFormulaLedger。 |
| `PrimitiveCoefficientFormulaStillOpen` | `true` | `false` | alpha primitive rule 仍缺 coefficient weight formula 和 row/output/local factor 同步。 | AlphaPrimitiveCoefficientWeightFormulaLedger。 |
| `ConstructorFormulaLineStillOpen` | `true` | `false` | actual constructor formula line 尚未给出可发射 signed row 的原始公式。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter |
| `PreCauchyDeclarationStillOpen` | `true` | `false` | pre-Cauchy declaration line 尚未锁定同 formal-unit 时间戳、noncanonical 来源和无泄漏。 | ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter |
| `SourceTableNeedsSamePrimitiveRows` | `true` | `false` | actual emitter source table 需要 primitive summand rows 和 alpha/delta coefficient identity before pushforward。 | PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND AlphaDeltaCoefficientIdentityBeforePushforwardLedger。 |
| `IndependentIdentityRouteNotProof` | `true` | `false` | 独立恒等式陈述已被分类到 actual moving-block/NC-BLK，并回到终端门，不能证明逐行权重公式。 | 需要非递归 primitive summand expression。 |
| `ReverseRecoveryBlocked` | `true` | `true` | 不能从 payment skeleton、零行覆盖或 terminal certificate 反向恢复 signed weight。 | 必须在 pushforward 前正向给出表达式。 |
| `PrimitiveSummandSignedWeightExpressionCurrentCorpusProved` | `false` | `false` | 当前材料没有 actual noncanonical primitive summand 的 signed weight expression before pushforward。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| `PointwiseSignedWeightFormulaCurrentCorpusProved` | `false` | `false` | 没有 primitive summand signed expression，就无法给每条 carry-shell skeleton row 赋权。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |

## 4. 下一真正单点

```text
ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
```
