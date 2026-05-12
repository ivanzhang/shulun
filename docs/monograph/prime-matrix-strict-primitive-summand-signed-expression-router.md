# Prime Matrix strict primitive summand signed expression 路由器

**状态：** `primitive_summand_signed_expression_reduced_to_origin_identity_open`

本步把 `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward` 继续压缩为 `PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward`。原因是：表达式本身不是证明；必须正向说明每个 actual noncanonical primitive summand 的 signed coefficient 从哪个 pre-Cauchy source tuple 产生，并在 Phi/payment 推前之前等于 alpha/delta 系数贡献。现有 canonical、外部谱、零行覆盖和 payment 反推路径都不能生成该表达式。因此当前仍未得到无条件终端矛盾。

```text
primitive_summand_signed_expression_router_closed=true
primitive_summand_signed_coefficient_origin_identity_proved=false
primitive_summand_signed_weight_expression_proved=false
pointwise_nonrecursive_signed_alpha_weight_formula_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 破坏输入

`PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward` 若被证明，将同时给出 exact signed weight、primitive coefficient formula、constructor row 的 sign/local factor 和推前前 alpha/delta identity，因此是当前循环中的真正破坏输入。

## 2. 来源恒等式字段

| field | meaning |
| --- | --- |
| `primitive_row_id` | 同一 formal unit 内的 actual noncanonical primitive summand 行标识。 |
| `source_tuple_origin` | 该行的 pre-Cauchy source tuple 来源，而不是推后 payment 原像。 |
| `signed_coefficient_formula` | signed coefficient 的正向表达式，包含符号、筛权、branch/local factor。 |
| `prepushforward_identity` | 证明该表达式在 Phi/payment 推前之前等于 actual alpha/delta 系数贡献。 |
| `nonzero_or_named_return` | 非零局部因子成立；若失败则进入同 formal unit 的命名回流。 |
| `no_import_leak` | 不借用 canonical scoped 公式、外部谱估计、零行覆盖或 terminal 反推。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PrimitiveSummandExpressionTargetActive` | `true` | `false` | 上一层已把逐行 signed alpha 权重公式压到 primitive summand 推前前表达式。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| `ExpressionMustBeOriginIdentity` | `true` | `true` | 表达式不能只是字段名；必须给出 pre-Cauchy signed coefficient 来源恒等式。 | PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward |
| `ExactAlphaWeightFormulaStillOpen` | `true` | `false` | alpha signed weight law 仍未给 exact signed weight formula。 | ExactAlphaSignedWeightFormulaLedger 被吸收到来源恒等式中。 |
| `AlphaPrimitiveCoefficientFormulaStillOpen` | `true` | `false` | alpha primitive rule 仍未给 primitive coefficient weight formula。 | AlphaPrimitiveCoefficientWeightFormulaLedger 被吸收到来源恒等式中。 |
| `ConstructorFormulaStillDoesNotEmitSignedRows` | `true` | `false` | actual constructor formula line 未给出带 sign/local factor 的 summand 行。 | 显式 constructor 行输出须由同一个来源恒等式生成。 |
| `SourceTableStillNeedsPrimitiveRows` | `true` | `false` | source table 已说明需要 primitive rows 与 coefficient identity before pushforward。 | 不能用 source table 反向证明来源恒等式。 |
| `IndependentIdentityRouteStillFixedPoint` | `true` | `false` | 独立恒等式路线仍经 moving-block/NCBLK 回到 PDEC/CleanKLS 终端门。 | 需要非递归来源恒等式破环。 |
| `ExternalSpectralLemmasDoNotEmitPrimitiveCoefficients` | `true` | `true` | DI/BFI/Kuznetsov 等外部估计处理给定系数后的平均，不生成推前前 summand 系数。 | 外部谱不能替代自足来源恒等式。 |
| `CanonicalRIWBuchstabScopedOnly` | `true` | `true` | canonical RIW/Buchstab 公式只在 canonical source 分支内有效，不能跨入 actual noncanonical summand。 | 若借用 canonical 公式，必须先证明同分支准入；当前没有。 |
| `ZeroRowAndPaymentReverseRecoveryBlocked` | `true` | `true` | 早期零行 unsigned cover 与 payment skeleton 都不能反向恢复 signed coefficient。 | 只能正向提交来源恒等式。 |
| `OriginIdentityCurrentCorpusProved` | `false` | `false` | 当前材料没有提交每个 actual primitive summand 的 signed coefficient 来源恒等式。 | PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward |
| `PrimitiveSummandExpressionCurrentCorpusProved` | `false` | `false` | 没有来源恒等式，primitive summand signed expression 仍未证明。 | PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward |

## 4. 下一真正单点

```text
PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
```
