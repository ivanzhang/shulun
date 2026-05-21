# Prime Matrix Phi-LPF latest constructor pure-pair atom sync 证书

**状态：** `phi_lpf_latest_constructor_source_tuple_synced_to_pure_pair_atom_open`

本步把 constructor 最新 `PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward` 接入 pure semiprime atom 拆解。每个 ordered type `(p,q), p<q` 的 first seed 原子是唯一 `tail=1` pure pair `p*q`；`tail>1` 的 Phi 质量为 `Phi(floor(N/(p*q)),q)-1`，只能作为 internal transition lift，而不是新 first seed。剩余直接硬点收窄为 pure pair signed seed atom，并仍需 orientation、ExactUV return、internal transition、source 三原子、signed survival 与 row-mass/no-heavy-row。

```text
latest_constructor_source_tuple_signed_formula_imported=true
constructor_side_gates_carried=true
pure_pair_atom_router_imported=true
pure_pair_atom_bijection_synced=true
tail_lift_phi_minus_one_synced=true
tail_lift_no_new_first_seed_closed=true
latest_basis_replaces_tuple_formula_with_pure_atom=true
pure_semiprime_pair_signed_seed_atom_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward` | `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward` | constructor source tuple signed formula 的 first-seed 部分强制落到 tail=1 pure pair；tail>1 是 continuation lift。 |
| `PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward` | `PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward` | `Phi(floor(N/(p*q)),q)-1` 的 tail-lift 质量不是新 first seed，只能交给 internal transition compatibility。 |
| `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | pure-pair 路线中的 common packet 义务在 constructor 最新基中仍由 source 三原子携带。 |
| `PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward` | `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward plus PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward, PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward, PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward, SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger, signed survival, and carried source atoms` | constructor 最新 source tuple formula 被收窄为 pure-pair signed atom 与配套 signed/ExactUV/transition/source 字段。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LatestConstructorSourceTupleSignedFormulaImported | `true` | `false` | 上一层 constructor tuple sync 已把直接硬点定位到 source tuple signed seed formula。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward |
| ConstructorSideGatesCarried | `true` | `false` | 本层只替换 source tuple formula；signed survival 与 row-mass/no-heavy-row 仍是 constructor 侧门。 | NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| PurePairAtomRouterImported | `true` | `true` | 既有 pure semiprime atom 证书可直接作用在 constructor 最新 source tuple formula 入口。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward |
| PurePairAtomBijectionSynced | `true` | `true` | 每个 ordered type `(p,q), p<q` 恰有一个 tail=1 pure pair seed atom。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| TailLiftPhiMinusOneSynced | `true` | `true` | tail continuation 质量为 `Phi(floor(N/(p*q)),q)-1`。 | PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward |
| TailLiftNoNewFirstSeedClosed | `true` | `true` | tail>1 occurrence 不是新 first seed，只能作为同一 pure atom 的 internal transition lift。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| SourceAtomsCarriedForward | `true` | `false` | common packet 义务继续以 source 三原子携带，本步不证明这三原子。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| LatestBasisReplacesTupleFormulaWithPureAtom | `true` | `false` | constructor 最新 source tuple formula 被收窄为 pure-pair signed atom 与 tail-lift/internal-transition 配套。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| PurePairSignedAtomStillOpen | `true` | `false` | LPF/Phi 和 tail=1 定位不给 pure pair 的 signed seed value。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| OrientationParityStillOpen | `true` | `false` | pure atom 仍需 orientation parity、branch side 与 local factor law。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward |
| ExactUVReturnStillOpen | `true` | `false` | ExactUV fixed pair、source entropy/fiber 与 return tag 仍是独立门。 | PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| InternalTransitionStillPaired | `true` | `false` | tail-lift compatibility 仍依赖 internal prime-adjoin signed transition law。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| PointwiseSignedTableStillParallel | `true` | `false` | 逐点 Phi-LPF signed value table 仍是并行旁路，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只同步 constructor pure-pair atom 拆解；未证明三命题无条件闭合。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |

## 3. 导入样本读数

| N | types | pure atoms | tail lift | total occ | pure share | tail share | ok |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10000 | 2600 | 2600 | 2868 | 5468 | 0.475493782004 | 0.524506217996 | `true` |

## 4. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
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

并行 constructor 侧门：

```text
NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger
```

行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_latest_constructor_pure_pair_atom_sync_router.py` | `cbefedfb984f90ba0ca38db793980ca63f2fe21e6f5b43c3c599d1c100b0a9a3` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-offdiagonal-seed-tuple-sync-router.json` | `b39a5e6b837ce8f8c1734aa3035fb723748fd31d2c5e64efa4e6efbc3cea78c8` |
| `docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json` | `608a8f088d6c14b5f3ffd1d5be01aef4555d0753e4ae7d70bcd2f986373dd315` |
| `docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json` | `9e344cf591570de1916132778441e76bc05d6c6b72e5a1cae11366dc8e965f9b` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
