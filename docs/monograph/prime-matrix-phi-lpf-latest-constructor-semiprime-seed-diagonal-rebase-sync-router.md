# Prime Matrix Phi-LPF latest constructor semiprime seed diagonal rebase sync 证书

**状态：** `phi_lpf_latest_constructor_semiprime_seed_diagonal_rebased_open`

本步把最新 rebase 后的 constructor `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` 重新接入既有 semiprime diagonal/offdiagonal 拆分。diagonal `(p,p)` 的私有 signed 出口已被移除，只能由 source-packet 三原子承接；因此最新 seed-side 主攻收窄为 `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`。internal transition、signed survival 与 row-mass/no-heavy-row 仍保留；行/列命题仍未无条件闭合。

```text
latest_rebased_first_seed_imported=true
existing_constructor_semiprime_diagonal_reusable=true
semiprime_diagonal_router_imported=true
diagonal_private_escape_removed=true
common_packet_cycle_guard_carried_forward=true
semiprime_seed_diagonal_rebased=true
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` | `PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward` | LPF first-edge seed 按 p=q 与 p<q 唯一分解。 |
| `PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward` | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | diagonal square-base 不能保留私有 signed 出口，只能回到 common source-packet 三原子。 |
| `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` | `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | 在最新 rebase 基中，FIRST_SEED 的新增 signed 缺口收窄为 offdiagonal seed。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `LatestRebasedFirstSeedImported` | `true` | `false` | 上一层 rebase 已把最新 constructor edge 路线压到 semiprime first-edge signed seed。 | PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward |
| `ExistingConstructorSemiprimeDiagonalReusable` | `true` | `false` | 旧 constructor semiprime diagonal 同步证书的目标输入相同，可以在新 rebase 前沿复用。 | PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `SemiprimeDiagonalRouterImported` | `true` | `true` | semiprime seed diagonal 证书给出 p=q 与 p<q 的无重叠拆分。 | PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| `DiagonalPrivateEscapeRemoved` | `true` | `true` | diagonal square-base lane 不生成独立 signed seed；它回到 common packet。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `CommonPacketCycleGuardCarriedForward` | `true` | `true` | common packet 自证环已被切断，不能用 diagonal lane 自证 source atoms。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `SemiprimeSeedDiagonalRebased` | `true` | `false` | 最新 FIRST_SEED 入口已同步为 offdiagonal seed 与 source 三原子。 | PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| `OffDiagonalSeedCurrentCorpusProved` | `false` | `false` | 当前材料没有为 p<q ordered semiprime first edges 给出 signed seed table。 | PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| `InternalPrimeAdjoinTransitionStillPaired` | `true` | `false` | first seed 收窄后，prefix>1 internal prime-adjoin transition 仍是同一 LPF 递推的配套硬点。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| `SourceAndSideGatesStillParallel` | `true` | `false` | source 三原子、signed survival 与 row-mass/no-heavy-row 仍随 constructor 前沿保留。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本层只做 rebase 同步；未证明 offdiagonal seed、internal transition、source 三原子、signed survival、row-mass 或 ExactUV。 | ((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND HarmonicWindowAlpha043PGe3001Upper0850Ledger AND DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

配套必需：

```text
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

已携带 source-packet 三原子：

```text
AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
```

行/列命题仍未无条件闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_latest_constructor_semiprime_seed_diagonal_rebase_sync_router.py` | `eb4e2bd5f48f5b51ec8178aee1b6a82fdad12458a9e832fd0fd8bd697b740376` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-rebase-sync-router.json` | `e03a42717182a7084869f1466470746cac9f5f91e078df34e488136cf959f508` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-semiprime-seed-diagonal-sync-router.json` | `f4495092313510b650081cab21a641b9ee06342a392fb83012cd3f89ad38c274` |
| `docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json` | `10b88bb8d80a793ab8ed16263cbe5efc4d47c72fdcc544ed7d97e559bda6788d` |
| `docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json` | `9e344cf591570de1916132778441e76bc05d6c6b72e5a1cae11366dc8e965f9b` |
