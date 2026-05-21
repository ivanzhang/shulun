# Prime Matrix Phi-LPF latest constructor two-prime no-swap rebase sync 证书

**状态：** `phi_lpf_latest_constructor_two_prime_no_swap_rebased_open`

本步把最新 rebase 后的 constructor `PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward` 接入 ordered no-swap 证书。LPF owner source domain 只保留 canonical ordered edge `(p,q)`，`p<q`；交换对称 `pq=qp` 不能供应反向 signed row 或 cancellation partner。最新直接主攻推进到 `PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward`。

```text
latest_rebased_two_prime_kernel_imported=true
existing_constructor_no_swap_reusable=true
no_swap_router_imported=true
lpf_owner_ordered_no_swap_closed=true
product_symmetry_does_not_emit_signed_kernel=true
source_atoms_carried_forward=true
two_prime_no_swap_rebased=true
edge_local_two_prime_signed_formula_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestRebasedTwoPrimeKernelImported` | `true` | `false` | 上一层 rebase 已把最新 constructor 窄口压到 two-prime signed interaction kernel。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| `ExistingConstructorNoSwapReusable` | `true` | `false` | 旧 constructor no-swap 同步证书输入相同，可在新 rebase 前沿复用。 | PhiLPFOffDiagonalTwoPrimeOrderedLPFOwnerNoSwapSymmetryLedgerBeforePushforward AND PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward |
| `NoSwapRouterImported` | `true` | `true` | no-swap 证书剥离 LPF owner canonical order。 | PhiLPFOffDiagonalTwoPrimeOrderedLPFOwnerNoSwapSymmetryLedgerBeforePushforward |
| `LPFOwnerOrderedNoSwapClosed` | `true` | `true` | 每个 distinct semiprime product 只有 canonical `(p,q)` source edge，无 reverse `(q,p)` source row。 | PhiLPFOffDiagonalTwoPrimeOrderedLPFOwnerNoSwapSymmetryLedgerBeforePushforward |
| `ProductSymmetryDoesNotEmitSignedKernel` | `true` | `true` | `pq=qp` 只识别整数值，不能供应第二个 pre-Cauchy signed source。 | PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward |
| `SourceAtomsCarriedForward` | `true` | `false` | source 三原子仍作为 carried input 保留，不能由 no-swap 自证。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `TwoPrimeNoSwapRebased` | `true` | `false` | 最新 two-prime kernel 已同步为 canonical edge-local signed formula 或 named return。 | PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward |
| `EdgeLocalFormulaStillOpen` | `true` | `false` | 当前材料没有给出 canonical `(p,q)` edge-local signed formula 或 named return。 | PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward |
| `OrientationExactUVTransitionStillOpen` | `true` | `false` | orientation、ExactUV return 与 internal transition 仍是独立门。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只做 rebase 同步；未证明 edge-local formula、orientation、ExactUV、internal transition 或 source 三原子。 | ((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 2. 导入样本读数

| N | ordered edges | unordered products | reverse edges | duplicates | no-swap ok |
| --- | ---: | ---: | ---: | ---: | --- |
| 10000 | 2600 | 2600 | 0 | 0 | `true` |

## 3. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward
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
| `experiments/prime_matrix_phi_lpf_latest_constructor_two_prime_no_swap_rebase_sync_router.py` | `f300fcaca9ad2305e4f1ec01ae017fbce01447e6f275468834b38f533a9664df` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-pure-pair-ferrers-support-rebase-sync-router.json` | `e927fb5a8462ffdfe1b6d5c85b041a63898f5f8263effe16c846cc0fb9c1cb1d` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-two-prime-no-swap-sync-router.json` | `0c6ee05daf873e7545f9380fa351f5a44f5e4122b811e3fc18eb8f918dea2cf9` |
| `docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json` | `68844af913e21b39317b6f47244070c96d3c5e4b630a00b1a0c7a029f66148f6` |
| `docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json` | `9e344cf591570de1916132778441e76bc05d6c6b72e5a1cae11366dc8e965f9b` |
