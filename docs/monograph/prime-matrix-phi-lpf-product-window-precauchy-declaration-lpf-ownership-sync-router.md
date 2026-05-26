# Prime Matrix Phi-LPF product-window pre-Cauchy declaration LPF ownership sync 证书

**状态：** `product_window_precauchy_declaration_unsigned_ownership_closed_signed_constructor_open`
**核验日期：** `2026-05-26`

本步把 product-window same-unit rank ExactUV atomization sync 留下的 `PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter` 接入 LPF ownership sieve source declaration 证书。结论是：declaration line 的无符号 ownership 字段已由最小素因子唯一分桶与素数计数恒等式支付；它不产生 signed alpha/delta coefficient、local factor 或 ExactUV fixed-key 重数。因此 product-window 第一主攻推进为 `ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter`。本证书不证明三命题无条件闭合。

```text
lpf_ownership_unsigned_declaration_imported=true
lpf_ownership_unsigned_declaration_line_closed=true
precauchy_declaration_removed_from_product_window_first_target=true
next_primary_attack_target=ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter
row_column_unconditional_closed=false
```

## 1. 下游同步链

| from | to | meaning |
| --- | --- | --- |
| `PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter` | `LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger AND ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter` | LPF ownership 支付 declaration line 的无符号 ownership 字段；signed alpha/delta lift 仍开放。 |
| `LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger` | `ascending least-prime-factor disjoint bucket identity` | 每个合数按唯一最小素因子进入且只进入一个筛层，素数计数恒等式由此闭合。 |
| `ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter` | `ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPreCauchyPairingCompatibilityLedger AND PrimitiveRowNonzeroSignLocalFactorLedger` | 显式 alpha/delta constructor 规则需分别生成 alpha/delta primitive rows，并给出 Cauchy 前配对兼容与非零 local factor。 |
| `ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger` | `DeterministicAlphaPrimitiveRowEmissionMapLedger` | alpha-side primitive rule 的第一生产性字段是确定性 alpha primitive row 发射映射。 |
| `DeterministicAlphaPrimitiveRowEmissionMapLedger` | `AlphaRowAnchorPhaseEmissionFormulaLedger` | 确定性发射映射继续压到 alpha row anchor/phase emission formula。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ProductWindowPreCauchyDeclarationActiveBeforeSync | `true` | `false` | 上一 product-window same-unit rank 证书把第一硬点推进到 pre-Cauchy constructor declaration。 | PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter |
| SourceTableFirstLineImported | `true` | `false` | actual emitter source table 已把首字段钉为 pre-Cauchy declaration line。 | PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter |
| LPFOwnershipUnsignedDeclarationImported | `true` | `true` | LPF ownership sieve 证明最小素因子唯一分桶和素数计数恒等式，可支付 unsigned ownership declaration 字段。 | LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger |
| SignedAlphaDeltaLiftStillOpen | `true` | `false` | LPF ownership 不产生 signed alpha/delta coefficient、orientation、local factor 或 ExactUV fixed-key 重数。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter |
| ExplicitAlphaDeltaRuleRouterImported | `true` | `false` | 显式 alpha/delta constructor rule 已被拆成 alpha-side、delta-side、配对兼容和非零 local factor。 | ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger AND ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger AND AlphaDeltaPreCauchyPairingCompatibilityLedger AND PrimitiveRowNonzeroSignLocalFactorLedger |
| AlphaSidePrimitiveRuleImported | `true` | `false` | alpha-side primitive rule 继续压到确定性 alpha row 发射映射等字段。 | DeterministicAlphaPrimitiveRowEmissionMapLedger |
| DeterministicAlphaEmissionImported | `true` | `false` | 确定性 alpha row 发射映射的当前最窄点是 alpha row anchor/phase emission formula。 | AlphaRowAnchorPhaseEmissionFormulaLedger |
| PreCauchyDeclarationRemovedFromProductWindowFirstTarget | `true` | `false` | pre-Cauchy declaration 旧名的 unsigned ownership 字段已支付；第一主攻转为显式 signed constructor rule。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter |
| ExplicitAlphaDeltaRuleStillOpen | `true` | `false` | 当前材料尚未写出 actual noncanonical primitive constructor 的 signed alpha/delta 规则。 | ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter |
| FixedKeyAndSignedSideStillOpen | `true` | `false` | fixed-key local multiplicity、orientation、ExactUV return 与 internal transition 仍未证明。 | FixedKeyExactUVLocalMultiplicityO1Ledger AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本证书只同步 declaration 到 LPF ownership/signed constructor 接口，不证明三命题无条件闭合。 | row_column_unconditional_closed=false |

## 3. 最新保留基

```text
(LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger AND ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND ConstructorDomainCleanCoreMembershipLedger AND ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND ConstructorFormulaFailureReturnTagsLedger AND SourceDeclarationNoDownstreamRecoveryAndNamedReturnLedger AND PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND AlphaDeltaCoefficientIdentityBeforePushforwardLedger AND SourceTableNoDownstreamRecoveryAndNamedReturnLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward) AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

仍开放的实际负载摘要：

```text
ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter AND ConstructorDomainCleanCoreMembershipLedger AND ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger AND ConstructorFormulaFailureReturnTagsLedger AND SourceDeclarationNoDownstreamRecoveryAndNamedReturnLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter
```

并行仍需：

```text
ConstructorDomainCleanCoreMembershipLedger
ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger
ConstructorFormulaFailureReturnTagsLedger
SourceDeclarationNoDownstreamRecoveryAndNamedReturnLedger
FixedKeyExactUVLocalMultiplicityO1Ledger
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
RatePreservationLedger_FOR_moving_atom_packet
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

严格含义：本证书只同步 declaration 到 LPF ownership/signed constructor 接口，不证明行/列命题。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-lpf-ownership-sieve-source-declaration-router.json` | `2857cbdeab08a400b1bce9099500290e8c59439ec11553ca0e5678335a5e6806` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-same-unit-rank-exactuv-atomization-sync-router.json` | `e6967f398f640b180f664959d98584db21fe4385447c58cb5dcabacfbf66c393` |
| `docs/monograph/prime-matrix-strict-actual-emitter-source-table-router.json` | `e327b1a80aef83a36279378e5892334fa305d92d5ac1bcbb8601eaab2f18ab3e` |
| `docs/monograph/prime-matrix-strict-alpha-side-primitive-rule-router.json` | `08b79049d746549d3c3d069a1501f8d79ee24b78b40faf0683d695271ff0c5a8` |
| `docs/monograph/prime-matrix-strict-deterministic-alpha-row-emission-map-router.json` | `d980647c15a9fd16b0e4255b5af3f2ce69ab5575dbe0d7a80a8b1ade70b0d177` |
| `docs/monograph/prime-matrix-strict-explicit-alpha-delta-rule-router.json` | `2de491d0a24986746199d7c96965b56f444643bf6aa15074bd705d7bf544531c` |
| `experiments/prime_matrix_phi_lpf_product_window_precauchy_declaration_lpf_ownership_sync_router.py` | `4410e918e6afe19d642d1499cf1ef23695201a91a936271b073c9361245987b2` |
