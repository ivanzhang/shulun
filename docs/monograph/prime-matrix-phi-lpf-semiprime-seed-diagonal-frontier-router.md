# Prime Matrix Phi-LPF semiprime seed diagonal frontier 证书

**状态：** `phi_lpf_semiprime_first_seed_split_to_diagonal_common_packet_and_offdiag_seed_open`

semiprime first-edge signed seed table 可按 `p=q` 与 `p<q` 强制拆分。diagonal `(p,p)` 正是 square-base root，既有证书已排除它的私有 signed 出口，但它回到 common pre-Cauchy source packet 后仍未闭合。offdiagonal `(p,q), p<q` 没有现成 signed seed 表。因而最新最窄主攻是 `PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`，同时仍需 diagonal common packet 和 internal prime-adjoin transition law。

```text
semiprime_first_edge_signed_seed_target_imported=true
diagonal_offdiagonal_support_split_proved=true
diagonal_square_base_private_signed_escape_removed=true
diagonal_common_packet_signed_source_proved=false
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
semiprime_first_edge_signed_seed_table_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SemiprimeFirstSeedTargetImported | `true` | `false` | 上一层已把 first-edge slab 的 signed 缺口命名为 semiprime first-edge signed seed table。 | PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward |
| DiagonalOffDiagonalSupportSplit | `true` | `true` | semiprime first-edge seed 类型唯一分成 diagonal `p=q` 与 offdiagonal `p<q`。 | PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| DiagonalSquareBasePrivateEscapeAlreadyRemoved | `true` | `true` | diagonal `(p,p)` 已由 square-base source packet reduction 证明没有私有 signed 出口。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| DiagonalCommonPacketStillOpen | `true` | `false` | diagonal square seed 回到 common packet；该 packet 仍不是已闭合 signed 来源。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| OffDiagonalSeedTableCurrentCorpusProved | `false` | `false` | 当前材料没有为所有 `p<q` ordered semiprime first edges 提交 signed seed 表。 | PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| SemiprimeFirstSeedTableCurrentCorpusProved | `false` | `false` | diagonal common packet 与 offdiagonal seed table 均未给出完整 signed first seed 表。 | PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward |
| PointwisePhiLPFTableStillParallel | `true` | `false` | 逐点 signed value table 可替代 seed 表，但当前仍未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| CompleteBranchTraceWouldSupplySemiprimeSeed | `true` | `true` | 完整 branch trace 可为 diagonal/offdiagonal seed 同时给 signed value、return tag 与 ExactUV。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| AtomicTraceWouldSupplySemiprimeSeed | `true` | `true` | atomic trace signed coefficient 公式可把 semiprime seed 作为 trace 字段读取。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| InternalTransitionStillPairedGate | `true` | `false` | 即使 semiprime seed 表存在，内部 prime-adjoin transition law 仍是配套门。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| ExactUVStillParallelGate | `true` | `false` | seed/transition 表即使存在，ExactUV source entropy/fiber 仍是并行门。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只把 semiprime seed 拆成 diagonal common-packet 与 offdiagonal seed；未证明三命题无条件闭合。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |

## 2. 样本审计摘要

| N | first types | diag types | offdiag types | first occ | diag occ | offdiag occ | diag type share | diag occ share | ok |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 30 | 10 | 3 | 7 | 19 | 10 | 9 | 0.3 | 0.526315789474 | `true` |
| 100 | 34 | 4 | 30 | 74 | 33 | 41 | 0.117647058824 | 0.445945945946 | `true` |
| 997 | 298 | 11 | 287 | 828 | 330 | 498 | 0.036912751678 | 0.398550724638 | `true` |
| 5003 | 1366 | 19 | 1347 | 4332 | 1652 | 2680 | 0.013909224012 | 0.38134810711 | `true` |
| 10000 | 2625 | 25 | 2600 | 8770 | 3302 | 5468 | 0.009523809524 | 0.376510832383 | `true` |

## 3. 最新保留基

```text
((PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket AND PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward
```

配套仍需：

```text
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

行/列命题仍未无条件闭合。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_semiprime_seed_diagonal_frontier_router.py` | `7ac5f7e77e6797b815957f3999ba080f578e7fee1eb162059c6e9c2eb8973684` |
| `docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.json` | `111cc0440f1f16e47cb791878a70f328fdff5122717efe007d08c0d704d62bfa` |
| `docs/monograph/prime-matrix-phi-lpf-square-base-source-packet-reduction-router.json` | `3ce843ba5d0230fd98f027fcfd85230e2e348069f0886a027b5969a5215209a1` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
