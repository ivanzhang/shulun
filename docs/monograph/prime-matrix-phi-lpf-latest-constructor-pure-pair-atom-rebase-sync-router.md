# Prime Matrix Phi-LPF latest constructor pure-pair atom rebase sync 证书

**状态：** `phi_lpf_latest_constructor_pure_pair_atom_rebased_open`

本步把最新 rebase 后的 constructor `PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward` 接入既有 pure-pair atom 证书。`tail=1` 是唯一 pure semiprime pair seed atom；`tail>1` 的 Phi-minus-one 质量不是新 first seed，只能进入 internal transition lift。最新直接主攻推进到 `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward`。

```text
latest_rebased_source_tuple_signed_formula_imported=true
existing_constructor_pure_pair_reusable=true
pure_pair_atom_router_imported=true
pure_pair_atom_bijection_synced=true
tail_lift_phi_minus_one_synced=true
tail_lift_no_new_first_seed_closed=true
source_atoms_carried_forward=true
pure_pair_atom_rebased=true
pure_semiprime_pair_signed_seed_atom_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestRebasedSourceTupleSignedFormulaImported` | `true` | `false` | 上一层 rebase 已把最新 constructor 窄口压到 offdiagonal source tuple signed formula。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward |
| `ExistingConstructorPurePairReusable` | `true` | `false` | 旧 constructor pure-pair atom 同步证书输入相同，可在新 rebase 前沿复用。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward |
| `PurePairAtomRouterImported` | `true` | `true` | pure atom 证书把 source tuple formula 的 first-seed 部分定位到 tail=1 pure pair。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| `PurePairAtomBijectionSynced` | `true` | `true` | 每个 ordered `(p,q), p<q` 只有一个 tail=1 pure semiprime seed atom。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| `TailLiftPhiMinusOneSynced` | `true` | `true` | tail>1 continuation 质量为 `Phi(floor(N/(p*q)),q)-1`。 | PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward |
| `TailLiftNoNewFirstSeedClosed` | `true` | `true` | tail>1 不是新 first seed，必须归入 internal transition lift。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| `SourceAtomsCarriedForward` | `true` | `false` | source 三原子仍作为 carried input 保留，不能由 pure atom 层自证。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `PurePairAtomRebased` | `true` | `false` | 最新 source tuple formula 已同步为 pure-pair signed atom 与 tail-lift/internal-transition 配套。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| `PurePairSignedAtomStillOpen` | `true` | `false` | tail=1 定位不给 pure pair signed seed value。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| `OrientationExactUVTransitionStillOpen` | `true` | `false` | orientation、ExactUV return 与 internal transition 仍是独立门。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只做 rebase 同步；未证明 pure-pair signed atom、orientation、ExactUV、internal transition 或 source 三原子。 | ((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 导入样本读数

| N | pure atoms | tail lift mass | ok |
| --- | ---: | ---: | --- |
| 10000 | 2600 | 2868 | `true` |

## 3. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
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
| `experiments/prime_matrix_phi_lpf_latest_constructor_pure_pair_atom_rebase_sync_router.py` | `0ccc881b2867f98501f65be96f3eed00e916e2b3c42b833ce5712ba7455614e0` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-rebase-sync-router.json` | `9a9088ecd443efa9c5a7b0d686abfbaf1a4b9f0bde2c6ae3d3705badbda0c083` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-sync-router.json` | `feacbace24860bc526675cca12216af302560d0b18e0565b6af6443bdf1d2bfb` |
| `docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json` | `608a8f088d6c14b5f3ffd1d5be01aef4555d0753e4ae7d70bcd2f986373dd315` |
| `docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json` | `9e344cf591570de1916132778441e76bc05d6c6b72e5a1cae11366dc8e965f9b` |
