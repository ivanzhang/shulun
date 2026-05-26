# Prime Matrix Phi-LPF product-window terminal/modelgap frontier 证书

**状态：** `product_window_terminal_modelgap_frontier_synced_modelgap_open`
**核验日期：** `2026-05-26`

本步把 product-window alpha/kernel 前沿留下的旧终端门 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 接入当前 canonical-source 终端晋级闭合路由，并导入 moving-block/DPRC 兼容性闭合接口。这样 product-window 路线不应继续把旧终端名作为第一主攻；终端侧真正剩余是 `ExplicitModelGapAndFiniteDPRCLedger`。这仍不是三命题无条件闭合，因为模型余量账本、DStructure/Rankin、pre-Cauchy identity、same-unit rank/multiplicity 与 product-window signed payload 仍未证明。

```text
product_window_old_terminal_gate_active=true
canonical_source_terminal_promotion_imported=true
moving_block_dprc_compatibility_imported=true
explicit_model_gap_and_finite_dprc_ledger_proved=false
terminal_gap_before_router=PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve
terminal_gap_after_router=NoFurtherCanonicalSourceTerminalPromotionGap
next_primary_attack_target=ExplicitModelGapAndFiniteDPRCLedger
row_column_unconditional_closed=false
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `product-window alpha/kernel frontier` | `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` | 上一 product-window 证书把 alpha 入口下钻到旧终端容量门、模型余量和 DStructure。 |
| `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` | `NoFurtherCanonicalSourceTerminalPromotionGap` | 当前终端晋级调和证书在 canonical-source 自足边界内关闭旧终端晋级缺口。 |
| `ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock` | `NoAdditionalDPRCLedgerGapAfterTerminalPromotionReconciliation` | moving-block/DPRC 兼容性证书说明终端替换没有引入新的 DPRC 账本对象。 |
| `product-window terminal side` | `NoFurtherCanonicalSourceTerminalPromotionGap AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` | 旧终端名不再是 product-window 第一主攻；真正剩余主门是模型余量/有限 DPRC 账本。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ProductWindowOldTerminalGateActive | `true` | `false` | product-window alpha/kernel 前沿的最新直接主攻仍登记为旧终端容量门。 | PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve |
| CanonicalSourceTerminalPromotionImported | `true` | `true` | 旧终端门已在 canonical-source 自足边界内接到无进一步终端晋级缺口。 | NoFurtherCanonicalSourceTerminalPromotionGap |
| GenericExternalDIBFIBranchKeptOpen | `true` | `true` | generic/external DI-BFI 宽口径没有被 canonical 闭合吸收，防止外推成全局定理。 | DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY |
| MovingBlockDPRCCompatibilityImported | `true` | `true` | moving-block 到终端晋级的替换不改变 ExplicitModelGapAndFiniteDPRCLedger 的对象口径。 | NoAdditionalDPRCLedgerGapAfterTerminalPromotionReconciliation |
| ExplicitModelGapAndFiniteDPRCLedgerStillOpen | `false` | `false` | 本步没有证明模型余量/有限 DPRC 账本本身；它成为 product-window 终端侧第一硬点。 | ExplicitModelGapAndFiniteDPRCLedger |
| DStructureRankinStillOpen | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |
| ProductWindowSignedPayloadStillOpen | `false` | `false` | pre-Cauchy identity、same-unit rank、offdiagonal signed formula、orientation、ExactUV 与 internal transition 仍未闭合。 | IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本证书只完成 product-window 终端/模型余量前沿同步；三命题仍未无条件闭合。 | ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新保留基

终端侧：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

product-window 总保留基：

```text
((PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND NoFurtherCanonicalSourceTerminalPromotionGap AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients OR PointwiseSqrtPrimeInputCOne OR ExternalDIBFIKuznetsovDispersionTheoremMatch) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND RatePreservationLedger_FOR_moving_atom_packet
```

下一直接主攻：

```text
ExplicitModelGapAndFiniteDPRCLedger
```

并行仍需：

```text
IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger
SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate
AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate
ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients
PointwiseSqrtPrimeInputCOne
DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY
```

严格含义：本证书只删除旧终端名作为 product-window 第一主攻，并不证明模型余量、signed payload 或行/列命题。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-current-terminal-promotion-reconciliation-router.json` | `b3844a7166966f8b49c81d6abfa3479f6aab777a0fb0509b0bb81d4fe3741f92` |
| `docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.json` | `231294a3f0a9cfe6d8af17db958a40f71b1bbfdabcefe3dc5d7c2d1a7a15b72a` |
| `docs/monograph/prime-matrix-moving-block-dprc-ledger-compatibility-router.json` | `c58be99083b0ddf69b3f7254bf9f4e8b9fc1df7ce16d5feeb38e727d865cef73` |
| `docs/monograph/prime-matrix-phi-lpf-product-window-alpha-kernel-frontier-router.json` | `9a09679103b90e105872ce5d8079ef711c1baaa66dc557623750d33fb9ce6258` |
| `experiments/prime_matrix_phi_lpf_product_window_terminal_modelgap_frontier_router.py` | `e64e243b01cd0846ba364252c11d68ea68a1f48c407e2bc22b4a010f05891188` |
