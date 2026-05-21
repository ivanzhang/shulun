# Prime Matrix Phi-LPF latest constructor pure-pair Ferrers support rebase sync 证书

**状态：** `phi_lpf_latest_constructor_pure_pair_ferrers_support_rebased_open`

本步把最新 rebase 后的 constructor `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward` 接入 Ferrers support 证书。pure pair 支撑和 degree 已由 `p<q<=N/p`、prime table 与 `floor(N/p)` 完全支付；剩余不再是容量问题，而是每条 `(p,q)` 边上的 `PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward`。

```text
latest_rebased_pure_pair_atom_imported=true
existing_constructor_ferrers_reusable=true
ferrers_support_router_imported=true
ferrers_support_and_degree_ledger_closed=true
ferrers_support_does_not_emit_signed_kernel=true
source_atoms_carried_forward=true
pure_pair_ferrers_support_rebased=true
two_prime_signed_interaction_kernel_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestRebasedPurePairAtomImported` | `true` | `false` | 上一层 rebase 已把最新 constructor 窄口压到 pure semiprime pair signed atom。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| `ExistingConstructorFerrersReusable` | `true` | `false` | 旧 constructor Ferrers 同步证书输入相同，可在新 rebase 前沿复用。 | PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward AND PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| `FerrersSupportRouterImported` | `true` | `true` | Ferrers 证书把 pure pair atom 的无符号支撑剥离出来。 | PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward |
| `FerrersSupportAndDegreeLedgerClosed` | `true` | `true` | 边条件 `p<q<=N/p`、嵌套邻域和 left/right degree 均由 prime table 决定。 | PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward |
| `FerrersSupportDoesNotEmitSignedKernel` | `true` | `true` | Ferrers 图只关闭支撑和度数，不产生 signed seed、orientation 或 local factor。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| `SourceAtomsCarriedForward` | `true` | `false` | source 三原子仍作为 carried input 保留，不能由 Ferrers 支撑自证。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `PurePairFerrersSupportRebased` | `true` | `false` | 最新 pure pair atom 已同步为 Ferrers support ledger 与 two-prime signed kernel。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| `TwoPrimeSignedKernelStillOpen` | `true` | `false` | 当前材料没有给出每条 `(p,q)` 边的 signed interaction kernel。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| `OrientationExactUVTransitionStillOpen` | `true` | `false` | orientation、ExactUV return 与 internal transition 仍是独立门。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只做 rebase 同步；未证明 two-prime signed kernel、orientation、ExactUV、internal transition 或 source 三原子。 | ((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 导入样本读数

| N | left layers | right vertices | edges | max left degree | max right degree | Ferrers ok |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 10000 | 25 | 668 | 2600 | 668 | 25 | `true` |

## 3. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
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
| `experiments/prime_matrix_phi_lpf_latest_constructor_pure_pair_ferrers_support_rebase_sync_router.py` | `2356c0b2f824c3c1bf7ba824cf3a663664f40fc7e04999ec2d88c41f8bf983b8` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-atom-rebase-sync-router.json` | `a71bdb861877413ce3c1971679a6038253709075965f29e909667731ddb8363c` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-sync-router.json` | `ea6cb0d17c81863843e33d2deb20bfb6e4de86f96566e41dc636a1b9051a6799` |
| `docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json` | `6ff12d29bab4ff0a9a9fad5794ecf6c74210ef7c51cee0c41b0f99ea1f2bab38` |
| `docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json` | `9e344cf591570de1916132778441e76bc05d6c6b72e5a1cae11366dc8e965f9b` |
