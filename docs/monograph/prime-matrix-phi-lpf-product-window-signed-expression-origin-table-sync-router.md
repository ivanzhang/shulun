# Prime Matrix Phi-LPF product-window signed-expression origin-table sync 证书

**状态：** `product_window_signed_expression_reduced_to_row_level_origin_table_open`
**核验日期：** `2026-05-26`

本步把 product-window 最新第一硬点 `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward` 接入 strict signed-expression、strict origin-identity 与 Phi-LPF signed-survival origin-table 证书。结论是：signed expression 不能作为证明终点；它必须正向给出 pre-Cauchy signed coefficient 来源恒等式，而该来源恒等式又等价于逐行 clean-core 原始生成表。LPF/Phi 候选 row ownership 继续保留，但仍不能生成 signed coefficient origin。

```text
primitive_expression_reduced_to_origin_identity=true
origin_identity_reduced_to_row_level_generation=true
phi_lpf_signed_survival_origin_table_imported=true
lpf_candidate_ownership_carried=true
product_window_signed_expression_removed_from_first_target=true
next_primary_attack_target=RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
row_column_unconditional_closed=false
```

## 1. 下游同步链

| from | to | meaning |
| --- | --- | --- |
| `ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward` | `PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward` | signed expression 不是证明；必须给 pre-Cauchy signed coefficient 来源恒等式。 |
| `PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward` | `RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands` | 来源恒等式等价于同一 formal unit 的逐行 clean-core 原始生成表。 |
| `LPF/Phi candidate row ownership` | `unsigned candidate address only` | 最小素因子分桶继续支付候选 row 地址，但不产生 signed coefficient origin。 |
| `RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands` | `signed coefficient, local factor, exact (u,v), branch key, prepushforward sum identity, named return` | row-level 表必须正向同时给出 actual primitive summand 的所有 signed 字段。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ProductWindowSignedExpressionActiveBeforeSync` | `true` | `false` | 上一层 product-window explicit alpha/delta 同步把第一硬点推进到 signed primitive summand expression。 | ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward |
| `StrictSignedExpressionRouterImported` | `true` | `false` | strict signed-expression 证书说明表达式名不能自证；必须给 signed coefficient 来源恒等式。 | PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward |
| `StrictOriginIdentityRouterImported` | `true` | `false` | strict origin-identity 证书把来源恒等式继续压到 row-level clean-core 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `PhiLPFSignedSurvivalOriginTableSyncImported` | `true` | `false` | Phi-LPF signed-survival 线已经独立确认同一压缩：候选容量不能生成 signed origin。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `LPFCandidateOwnershipCarriedButNotSignedOrigin` | `true` | `true` | LPF/Phi 最小素因子候选 row ownership 继续可用，但只给无符号地址和 skeleton。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `RowLevelCleanCoreOriginGenerationStillOpen` | `true` | `false` | 当前材料还没有逐 actual noncanonical primitive summand 的 signed coefficient 原始生成表。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `NonzeroSignedSurvivalStillOpen` | `true` | `false` | 没有 row-level signed origin table，候选 row 的非零 signed survival 仍不能推出。 | NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward |
| `SameFormalUnitRowMassStillIndependent` | `true` | `false` | 即使 row-level 表存在，仍需同一 formal unit 的 row-mass/no-heavy-row 归一化账本。 | SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| `ProductWindowSignedExpressionRemovedFromFirstTarget` | `true` | `false` | product-window 第一主攻不应停在 signed expression 字段名；应推进到 row-level origin generation table。 | RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本证书只同步 signed expression 的来源表前沿，不证明该表、row-mass、ExactUV、orientation 或终端排斥。 | row_column_unconditional_closed=false |

## 3. 最新保留基

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward AND CompletePrimitiveEmitterKeyPartitionLedger AND ActualNoncanonicalAlphaSourceTupleDomainLedger AND AlphaPrimitiveCoefficientWeightFormulaLedger AND AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger AND AlphaPrimitiveRuleFailureNamedReturnLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPairingCompatibilityBeforeCauchyLedger AND PrimitiveRuleNonzeroSignLocalFactorLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands
```

并行仍需：

```text
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
CompletePrimitiveEmitterKeyPartitionLedger
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

严格含义：本证书只同步 signed expression 到 row-level origin table，不证明行/列命题。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-lpf-candidate-row-map-alpha-rule-router.json` | `735c6efd0580444f1b541b01a5a7184dff79497191657bb2da6bf0b6b1d3778f` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-explicit-alpha-delta-signed-summand-sync-router.json` | `c68dc27f633a43ba92d06d4f4b534b9b162ecbef161dc5d45ca65e65ffcefdc2` |
| `docs/monograph/prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json` | `2a1b6082621d0c9d8ddd1acfa69d12f9c3f3a38cebe422ba3d14b196661b5a30` |
| `docs/monograph/prime-matrix-strict-primitive-summand-origin-identity-router.json` | `0dff99f81fe37cfe92e28ac6c798f4bba60d3c46bf7ce9fc14b8c6603c10032d` |
| `docs/monograph/prime-matrix-strict-primitive-summand-signed-expression-router.json` | `b0b1264cf6f3fbad60724a440f0dc9872dbc577376ed466e5dcac0cf66caa5ff` |
| `experiments/prime_matrix_phi_lpf_product_window_signed_expression_origin_table_sync_router.py` | `6cb083d2864830c7850d1257c7441dbebf90b0c7062e1e976d19fa7843a6cc7f` |
