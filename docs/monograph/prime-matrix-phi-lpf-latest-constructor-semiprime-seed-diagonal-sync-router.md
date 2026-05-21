# Prime Matrix Phi-LPF latest constructor semiprime seed diagonal sync 证书

**状态：** `phi_lpf_latest_constructor_semiprime_seed_synced_to_offdiag_and_source_atoms_open`

本步把 constructor-latest `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` 接入既有 diagonal/offdiagonal 拆分。diagonal `(p,p)` 已无私有 signed 出口，并由 source-packet 三原子承接；因此 FIRST_SEED 的新增 signed 缺口收窄为 `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`。internal transition、signed survival 与 row-mass/no-heavy-row 仍保留；行/列命题仍未无条件证明。

```text
latest_constructor_first_seed_hardpoint_imported=true
constructor_side_gates_carried=true
semiprime_diagonal_router_imported=true
diagonal_offdiagonal_support_split_closed=true
diagonal_private_escape_removed=true
common_packet_cycle_guard_carried_forward=true
latest_basis_replaces_first_seed_with_offdiag_seed=true
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
nonzero_signed_row_survival_proved=false
same_formal_unit_row_mass_normalization_proved=false
row_column_unconditional_closed=false
next_primary_attack_target=PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

## 1. 同步链

| from | to | meaning |
| --- | --- | --- |
| `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` | `PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward` | semiprime first-edge seed 类型按 p=q 与 p<q 唯一拆分。 |
| `PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward` | `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` | diagonal `(p,p)` 是 square-base root；私有 signed 出口已移除，只能回到 common packet。 |
| `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | common packet 的自证环已被切断；constructor 最新前沿把其非循环需求携带为 source 三原子。 |
| `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward` | `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward plus carried source atoms` | FIRST_SEED 的 diagonal 义务由 source 三原子承接后，新增 seed 窄口是 offdiagonal 表。 |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LatestConstructorFirstSeedHardpointImported | `true` | `false` | 上一层 constructor edge slab 同步已把 FIRST_SEED 登记为直接主攻点。 | PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward |
| ConstructorSideGatesCarried | `true` | `false` | 本层只替换 FIRST_SEED；signed survival 与 row-mass/no-heavy-row 仍是 constructor 侧门。 | NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger |
| SemiprimeDiagonalRouterImported | `true` | `true` | 既有 semiprime diagonal/offdiagonal 证书可作为 FIRST_SEED 的直接下游。 | PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| DiagonalOffDiagonalSupportSplitClosed | `true` | `true` | LPF/Phi first-edge seed 类型唯一分成 p=q diagonal 与 p<q offdiagonal。 | PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| DiagonalPrivateEscapeRemoved | `true` | `true` | diagonal `(p,p)` 不再是独立 signed lane；它已回到 common source packet。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| CommonPacketCycleGuardCarriedForward | `true` | `true` | common packet 不能用 signed-lane 固定点自证；latest constructor 前沿已把它携带为 source 三原子。 | AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows |
| LatestBasisReplacesFirstSeedWithOffdiagSeed | `true` | `false` | 在 constructor 最新基中，FIRST_SEED 的 diagonal 义务由 source 三原子承接，新增 seed 缺口收窄到 offdiagonal 表。 | PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| OffDiagonalSeedStillOpen | `true` | `false` | 当前材料没有为所有 p<q ordered semiprime first edges 给出 signed seed 表。 | PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| InternalTransitionStillPaired | `true` | `false` | FIRST_SEED 收窄后，internal prime-adjoin transition 仍是同一递推路线的配套硬点。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| PointwiseSignedTableStillParallel | `true` | `false` | 逐点 Phi-LPF signed value table 仍是并行直接旁路，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只同步 FIRST_SEED 的 diagonal/offdiagonal 拆分；未证明 offdiagonal seed、internal transition、source 三原子、signed survival、row-mass 或 ExactUV。 | row/column theorem still open |

## 3. 导入样本读数

| N | first types | diag types | offdiag types | first occ | diag occ | offdiag occ | ok |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 10000 | 2625 | 25 | 2600 | 8770 | 3302 | 5468 | `true` |

## 4. 最新保留基

```text
((AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

配套仍需：

```text
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

已携带 source-packet 三原子：

```text
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
| `experiments/prime_matrix_phi_lpf_latest_constructor_semiprime_seed_diagonal_sync_router.py` | `e5b38597cd78d48cadc6477ac44692b7db924ac765ddff1ba7ac73d04f2e94e8` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-edge-multiplier-slab-sync-router.json` | `0a8763089c7ccabcf04f32c9f1ba9093059c14283e4fefda35469f4ef33f7ec4` |
| `docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json` | `10b88bb8d80a793ab8ed16263cbe5efc4d47c72fdcc544ed7d97e559bda6788d` |
| `docs/monograph/prime-matrix-phi-lpf-source-packet-cycle-guard-sync-router.json` | `9e344cf591570de1916132778441e76bc05d6c6b72e5a1cae11366dc8e965f9b` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
