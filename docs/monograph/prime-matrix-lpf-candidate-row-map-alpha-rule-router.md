# Prime Matrix LPF candidate-row map alpha-rule 证书

**状态：** `lpf_candidate_row_map_closed_signed_summand_expression_open`

LPF ownership 进一步支付 alpha-side primitive rule 中的非后验候选 row 发射映射：每个候选合数 row 由唯一最小素因子层 p 与 cofactor m 索引，且与已闭合 unsigned skeleton 兼容。但 candidate row map 仍不是 actual signed primitive row map；最新硬点转为 `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`。

```text
alpha_side_primitive_rule_imported=true
deterministic_alpha_map_gap_imported=true
lpf_ownership_declaration_imported=true
lpf_candidate_row_emission_map_closed=true
pointwise_signed_alpha_value_table_proved=false
primitive_summand_signed_weight_expression_proved=false
row_column_unconditional_closed=false
```

## 1. 桥接公式

```text
DeterministicAlphaPrimitiveRowEmissionMapLedger
  ->
LPFOwnershipAlphaCandidateRowEmissionMapLedger
AND ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
```

含义：LPF ownership 只关闭候选 row 的唯一来源索引；actual alpha primitive row 仍需要前推前 signed summand 表达式。

## 2. 新 alpha-side 剩余基

```text
ActualNoncanonicalAlphaSourceTupleDomainLedger AND LPFOwnershipAlphaCandidateRowEmissionMapLedger AND ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward AND AlphaPrimitiveCoefficientWeightFormulaLedger AND AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaPrimitiveRuleFailureNamedReturnLedger
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| AlphaSidePrimitiveRuleTargetImported | `true` | `false` | 显式 alpha/delta 规则的当前首个侧向硬点是 alpha-side primitive rule。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger |
| DeterministicAlphaMapGapImported | `true` | `false` | alpha-side rule 内部首缺口是 source tuple 到 alpha primitive rows 的确定性发射映射。 | DeterministicAlphaPrimitiveRowEmissionMapLedger |
| LPFOwnershipDeclarationImported | `true` | `true` | 上一层已证明升序最小素因子 ownership 分桶和 pre-Cauchy unsigned declaration 字段。 | LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger |
| LPFCompositeBucketToCandidateRowsClosed | `true` | `true` | 每个候选合数行可由唯一 p 层和 cofactor m 索引；不同 p 层不重叠，不需要 payment 反推选原像。 | LPFOwnershipAlphaCandidateRowEmissionMapLedger |
| UnsignedSkeletonCompatibilityImported | `true` | `true` | carry-shell、P 列锚、phase rule 与 layered-wheel 可承接 LPF candidate row 的几何坐标。 | AlphaRowUnsignedSkeletonLedger |
| LPFCandidateMapIsNotSignedPrimitiveMap | `true` | `true` | LPF candidate map 只确定候选 row ownership 和几何索引；它不赋 signed weight、local factor 或 primitive summand 表达式。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| SignedValueTableStillOpen | `true` | `false` | 逐 skeleton row 的 signed alpha value table 仍未证明。 | PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton |
| PrimitiveSummandSignedExpressionStillOpen | `true` | `false` | 逐行 signed 权重公式已压到 actual noncanonical primitive summand signed expression before pushforward。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| DeterministicAlphaMapReducedToLPFCandidateAndSignedExpression | `true` | `false` | 确定性发射映射的非后验候选索引由 LPF ownership 支付；要成为 actual alpha primitive row，还必须给 signed summand expression。 | ActualNoncanonicalAlphaSourceTupleDomainLedger AND LPFOwnershipAlphaCandidateRowEmissionMapLedger AND ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward AND AlphaPrimitiveCoefficientWeightFormulaLedger AND AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaPrimitiveRuleFailureNamedReturnLedger |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步不证明 signed expression、delta-side rule、pairing compatibility、ExactUV fixed-key 或终端排斥。 | ActualNoncanonicalAlphaSourceTupleDomainLedger AND LPFOwnershipAlphaCandidateRowEmissionMapLedger AND ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward AND AlphaPrimitiveCoefficientWeightFormulaLedger AND AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaPrimitiveRuleFailureNamedReturnLedger |

## 4. 诚实边界

- 本证书没有证明 signed alpha value table。
- 本证书没有证明 actual noncanonical primitive summand signed weight expression before pushforward。
- 本证书没有证明 delta-side primitive rule、alpha/delta pairing compatibility 或 ExactUV fixed-key multiplicity。
- 行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_lpf_candidate_row_map_alpha_rule_router.py` | `89c0df8a72f946d4e8e40c25d47efe0dbad4095aaf02b3dcf0937463b621b48a` |
| `docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.json` | `2857cbdeab08a400b1bce9099500290e8c59439ec11553ca0e5678335a5e6806` |
| `docs/monograph/prime-matrix-strict-alpha-side-primitive-rule-router.json` | `08b79049d746549d3c3d069a1501f8d79ee24b78b40faf0683d695271ff0c5a8` |
| `docs/monograph/prime-matrix-strict-pointwise-signed-alpha-value-table-router.json` | `c44a6e986d59cd068f19cdb58427f779721bb1cf984ff1edb4d67be28cb6dc8c` |
| `docs/monograph/prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json` | `fb392c7ecb2613c000b1c8696ff285c12cb91c815a08dad700e24c21fec6b66f` |
| `docs/monograph/prime-matrix-strict-alpha-row-unsigned-skeleton-router.json` | `98f6fa7be381de7d3170bc0abf7e37bde6b1f87351c3ad4bc2c2d4ce62e71c87` |
