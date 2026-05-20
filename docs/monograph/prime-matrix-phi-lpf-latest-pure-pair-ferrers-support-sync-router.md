# Prime Matrix Phi-LPF latest pure-pair Ferrers support sync 证书

**状态：** `phi_lpf_latest_pure_pair_atom_synced_to_ferrers_support_open`

本步把最新 `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward` 接入 Ferrers support 拆解。pure pair 支撑由 `p<q<=N/p` 完全决定，left/right degree 和 edge 总数已由 LPF/Phi/素数表支付；因此 pure-pair 剩余不再是支撑或容量问题，而是每条 `(p,q)` 边上的 two-prime signed interaction kernel，并仍需 orientation、ExactUV return、internal transition 与 source 三原子。

```text
latest_pure_pair_atom_imported=true
ferrers_support_router_imported=true
ferrers_support_rule_synced=true
ferrers_degree_ledger_synced=true
support_graph_signed_kernel_emission_proved=false
latest_basis_replaces_pure_atom_with_two_prime_kernel=true
two_prime_signed_interaction_kernel_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward` | `PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward AND PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward` | pure pair atom 先剥离 Ferrers 支撑/度数账本，剩余才是每条边的 signed kernel。 |
| `PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward` | `closed edge rule p<q<=N/p and nested left neighborhoods` | 支撑边集、left/right degree 与总边数均由素数表和 floor(N/p) 决定。 |
| `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | Ferrers 支撑不处理 common packet；该义务仍由 source 三原子携带。 |
| `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward` | `PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward plus PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward, PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward, PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward, and carried source atoms` | 最新 pure-pair atom 被收窄为 two-prime signed interaction kernel 与配套字段。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LatestPurePairAtomImported | `true` | `false` | 上一层最新 pure-pair sync 已把直接硬点定位到 pure semiprime pair signed atom。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| FerrersSupportRouterImported | `true` | `true` | 既有 Ferrers support 证书可直接作用在最新 pure-pair atom 入口。 | PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward |
| FerrersSupportRuleSynced | `true` | `true` | pure pair 支撑边条件为 `p<q<=N/p`，左邻域嵌套下降。 | PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward |
| FerrersDegreeLedgerSynced | `true` | `true` | left/right degree 与 edge 总数由素数表和 `floor(N/p)` 支付。 | PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward |
| SupportDoesNotEmitSignedKernel | `true` | `true` | Ferrers 图只关闭支撑和度数，不产生 signed value、orientation 或 local factor。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| SourceAtomsCarriedForward | `true` | `false` | common packet 义务继续以 source 三原子携带，本步不证明这三原子。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| LatestBasisReplacesPureAtomWithTwoPrimeKernel | `true` | `false` | 最新 pure-pair atom 被收窄为 two-prime signed interaction kernel 与配套字段。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| TwoPrimeSignedKernelStillOpen | `true` | `false` | 当前语料没有提交 `(p,q)` 两素数交互 signed kernel。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| OrientationParityStillOpen | `true` | `false` | two-prime kernel 仍需 orientation parity、branch side 与 local factor law。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward |
| ExactUVReturnStillOpen | `true` | `false` | ExactUV fixed pair、source entropy/fiber 与 return tag 仍是独立门。 | PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| InternalTransitionStillPaired | `true` | `false` | tail-lift 与完整 support key 的 signed compatibility 仍依赖 internal transition。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| PointwiseSignedTableStillParallel | `true` | `false` | 逐点 Phi-LPF signed value table 仍是并行旁路，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只同步 Ferrers support 剥离；未证明三命题无条件闭合。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |

## 3. 导入样本读数

| N | left layers | right vertices | edges | max left deg | max right deg | Ferrers | degree ok |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 10000 | 25 | 668 | 2600 | 668 | 25 | `true` | `true` |

## 4. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
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
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_latest_pure_pair_ferrers_support_sync_router.py` | `9c03d804711a46aedbbf80d1309e007aa53d499143aa1d8c76fefc7bbf711acc` |
| `docs/monograph/prime-matrix-phi-lpf-latest-offdiagonal-pure-pair-atom-sync-router.json` | `2ef53f76c04a047c30b1afad82054c641e751ec5b4e6dfeedecb3c318a2486e9` |
| `docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json` | `6ff12d29bab4ff0a9a9fad5794ecf6c74210ef7c51cee0c41b0f99ea1f2bab38` |
| `docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json` | `9e344cf591570de1916132778441e76bc05d6c6b72e5a1cae11366dc8e965f9b` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
