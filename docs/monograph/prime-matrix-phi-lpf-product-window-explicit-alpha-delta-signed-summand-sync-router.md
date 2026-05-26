# Prime Matrix Phi-LPF product-window explicit alpha/delta signed-summand sync 证书

**状态：** `product_window_explicit_alpha_delta_reduced_to_signed_summand_expression_open`
**核验日期：** `2026-05-26`

本步把 product-window 最新第一硬点 `ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter` 接入 strict explicit-rule、alpha-side primitive rule、deterministic alpha map、LPF candidate-row map 和 pointwise signed weight formula 证书。结论是：LPF/Phi 的精确最小素因子分桶还能支付 alpha 侧候选 row ownership/几何索引；但 actual signed primitive summand expression before pushforward 仍未构造，delta/pairing/nonzero、ExactUV、orientation 和 terminal 验收仍并行开放。

```text
strict_explicit_rule_imported=true
alpha_side_primitive_rule_imported=true
deterministic_alpha_map_imported=true
lpf_candidate_row_map_closed=true
primitive_summand_signed_expression_still_open=true
explicit_alpha_delta_removed_from_product_window_first_target=true
next_primary_attack_target=ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
row_column_unconditional_closed=false
```

## 1. 下游同步链

| from | to | meaning |
| --- | --- | --- |
| `ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter` | `ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND PrimitiveRuleNonzeroSignLocalFactorLedger` | 显式 alpha/delta 规则先拆成 alpha-side、delta-side、配对兼容和非零 local factor。 |
| `ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger` | `DeterministicAlphaPrimitiveRowEmissionMapLedger` | alpha-side primitive rule 的第一生产性字段是确定性 alpha primitive row 发射映射。 |
| `DeterministicAlphaPrimitiveRowEmissionMapLedger` | `LPFOwnershipAlphaCandidateRowEmissionMapLedger AND ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward` | LPF ownership 支付候选 row ownership/几何索引；actual row 仍需 signed summand 表达式。 |
| `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward` | `primitive summand row, side, signed weight, local factor, exact (u,v), branch key, failure return` | signed summand 表达式必须在 Phi/payment 推前前逐行给出所有 signed 字段。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ProductWindowExplicitAlphaDeltaActiveBeforeSync` | `true` | `false` | 上一层 product-window declaration/LPF ownership 同步把第一硬点推进到显式 alpha/delta constructor rule。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter |
| `StrictExplicitRuleImported` | `true` | `false` | strict explicit-rule 证书把显式规则拆成 alpha-side、delta-side、配对兼容和非零 local factor。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND PrimitiveRuleNonzeroSignLocalFactorLedger |
| `AlphaSidePrimitiveRuleImported` | `true` | `false` | alpha-side primitive rule 继续拆成定义域、确定性 row 发射、权重、输出和失败回流。 | ActualNoncanonicalAlphaSourceTupleDomainLedger AND DeterministicAlphaPrimitiveRowEmissionMapLedger AND AlphaPrimitiveCoefficientWeightFormulaLedger AND AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaPrimitiveRuleFailureNamedReturnLedger |
| `DeterministicAlphaMapImported` | `true` | `false` | 确定性 alpha row 发射映射仍需前推前 row formula；不能从 payment 或外部谱反选。 | DeterministicAlphaPrimitiveRowEmissionMapLedger |
| `LPFCandidateRowMapClosed` | `true` | `true` | LPF ownership 可支付候选合数 row 的唯一 p 层/cofactor 索引与 unsigned skeleton 兼容性。 | LPFOwnershipAlphaCandidateRowEmissionMapLedger |
| `LPFCandidateMapNotSignedPrimitiveMap` | `true` | `true` | 候选 row map 只给 ownership 和几何索引，不给 signed weight、local factor 或 primitive summand 表达式。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| `PrimitiveSummandSignedExpressionStillOpen` | `true` | `false` | 逐行 signed 权重公式已经压到 actual noncanonical primitive summand signed expression before pushforward。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| `AlphaTerminalSyncImportedButNotProof` | `true` | `false` | productive alpha-side 下游会接到 PDEC/CleanKLS 与模型余量，但这不是 signed summand 表达式证明。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger |
| `SiblingFieldsStillOpen` | `true` | `false` | delta-side、pairing、nonzero/local-factor、fixed-key ExactUV、orientation 和 internal transition 仍并行开放。 | ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND PrimitiveRuleNonzeroSignLocalFactorLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| `ExplicitAlphaDeltaRemovedFromProductWindowFirstTarget` | `true` | `false` | 显式 alpha/delta 旧名已被拆到 signed summand 表达式与并行兄弟字段，不应继续作为单名第一主攻。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本证书只同步 product-window constructor 前沿，不证明 signed expression、delta/pairing、ExactUV 或终端排斥。 | row_column_unconditional_closed=false |

## 3. 最新保留基

```text
ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward AND ActualNoncanonicalAlphaSourceTupleDomainLedger AND AlphaPrimitiveCoefficientWeightFormulaLedger AND AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaPrimitiveRuleFailureNamedReturnLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND PrimitiveRuleNonzeroSignLocalFactorLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward
```

并行仍需：

```text
ActualNoncanonicalAlphaSourceTupleDomainLedger
AlphaPrimitiveCoefficientWeightFormulaLedger
AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger
AlphaPrimitiveRuleFailureNamedReturnLedger
ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger
AlphaDeltaPairingCompatibilityBeforeCauchyLedger
PrimitiveRuleNonzeroSignLocalFactorLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

严格含义：本证书只同步 explicit alpha/delta 到 signed summand 接口，不证明行/列命题。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json` | `735c6efd0580444f1b541b01a5a7184dff79497191657bb2da6bf0b6b1d3778f` |
| `docs/monograph/prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.json` | `b29335cbb7c029994260284c3e3c6c07e896329a51ca8446ec60b832ca6b8357` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-precauchy-declaration-lpf-ownership-sync-router.json` | `b4654226570c8f103b772be51502b017095fbca8449a7ff36052164bc090a063` |
| `docs/monograph/prime-matrix-strict-alpha-side-primitive-rule-router.json` | `08b79049d746549d3c3d069a1501f8d79ee24b78b40faf0683d695271ff0c5a8` |
| `docs/monograph/prime-matrix-strict-deterministic-alpha-row-emission-map-router.json` | `d980647c15a9fd16b0e4255b5af3f2ce69ab5575dbe0d7a80a8b1ade70b0d177` |
| `docs/monograph/prime-matrix-strict-explicit-alpha-delta-rule-router.json` | `2de491d0a24986746199d7c96965b56f444643bf6aa15074bd705d7bf544531c` |
| `docs/monograph/prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json` | `fb392c7ecb2613c000b1c8696ff285c12cb91c815a08dad700e24c21fec6b66f` |
| `experiments/prime_matrix_phi_lpf_product_window_explicit_alpha_delta_signed_summand_sync_router.py` | `bb6bf650ac342e346d51cb3a9e9f74d1c3c7ee3cb13456683a678a53b5e99fd5` |
