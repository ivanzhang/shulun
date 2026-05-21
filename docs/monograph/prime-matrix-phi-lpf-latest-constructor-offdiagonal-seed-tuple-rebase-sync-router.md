# Prime Matrix Phi-LPF latest constructor offdiagonal seed tuple rebase sync 证书

**状态：** `phi_lpf_latest_constructor_offdiagonal_seed_tuple_rebased_open`

本步把最新 rebase 后的 constructor `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward` 接入既有 tuple-fields 证书。LPF/Phi 已关闭 owner prime、first rough prime、q-rough tail 与 Phi tail-fiber mass 的无符号支撑账，但这些字段不能推出 signed seed、orientation 或 ExactUV return。最新直接主攻推进到 `PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward`。

```text
latest_rebased_offdiagonal_seed_imported=true
existing_constructor_offdiagonal_tuple_reusable=true
offdiagonal_tuple_fields_router_imported=true
offdiagonal_source_tuple_bijection_synced=true
offdiagonal_phi_tail_fiber_mass_synced=true
lpf_phi_unsigned_scope_exhausted_for_offdiag_seed=true
source_atoms_carried_forward=true
offdiagonal_seed_tuple_rebased=true
offdiagonal_signed_seed_formula_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestRebasedOffDiagonalSeedImported` | `true` | `false` | 上一层 rebase 已把最新 constructor seed-side 窄口压到 offdiagonal ordered semiprime seed。 | PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| `ExistingConstructorOffDiagonalTupleReusable` | `true` | `false` | 旧 constructor offdiagonal tuple 同步证书的输入相同，可在新 rebase 前沿复用。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| `OffDiagonalTupleFieldsRouterImported` | `true` | `true` | tuple-fields 证书把 offdiagonal seed 拆成无符号 tuple 字段和 signed payload 字段。 | PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward |
| `OffDiagonalSourceTupleBijectionSynced` | `true` | `true` | 每个 offdiagonal occurrence 唯一写成 owner p、first rough q 与 q-rough tail。 | PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward |
| `OffDiagonalPhiTailFiberMassSynced` | `true` | `true` | Phi-LPF 桶恒等式只支付 q-rough tail occurrence mass。 | PhiLPFOffDiagonalQRoughTailFiberMassLedger |
| `LPFPhiUnsignedScopeExhausted` | `true` | `true` | LPF/Phi 无符号信息已用尽，不能推出 signed seed、orientation 或 ExactUV return。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| `SourceAtomsCarriedForward` | `true` | `false` | diagonal/common packet 义务仍由 source 三原子携带。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `OffDiagonalSeedTupleRebased` | `true` | `false` | 最新 offdiagonal seed 入口已同步为 source tuple signed formula 与配套字段。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| `OffDiagonalSignedFormulaStillOpen` | `true` | `false` | 当前材料没有给出 source tuple signed seed formula。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward |
| `OrientationAndExactUVStillOpen` | `true` | `false` | orientation parity、branch side、ExactUV fixed pair 与 return tag 仍未证明。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| `InternalTransitionStillPaired` | `true` | `false` | tail 非单位 continuation 仍需要 internal prime-adjoin signed transition。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只做 rebase 同步；未证明 signed formula、orientation、ExactUV、internal transition 或 source 三原子。 | ((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 导入样本读数

| N | offdiag types | tuple occ | Phi sum | tail=1 | tail>1 | max tail | ok |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10000 | 2600 | 5468 | 5468 | 2600 | 2868 | 1665 | `true` |

## 3. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
```

配套仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

行/列命题仍未无条件闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_latest_constructor_offdiagonal_seed_tuple_rebase_sync_router.py` | `6654c87d8b290c5f00ad30619a07f8af0b81f946a30f2242126e5ee3d5b42853` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-rebase-sync-router.json` | `c5438c99e29b137fa6be0f9392a34ce7908cc7b70edbaf2d5d535f3bd82f5600` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-router.json` | `b39a5e6b837ce8f8c1734aa3035fb723748fd31d2c5e64efa4e6efbc3cea78c8` |
| `docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json` | `f9b2e9eaf8020cde5952237044a1d62308564951b9e00f4cf163ab46d5b62ccf` |
| `docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json` | `9e344cf591570de1916132778441e76bc05d6c6b72e5a1cae11366dc8e965f9b` |
