# Prime Matrix Phi-LPF pure pair Ferrers support 证书

**状态：** `phi_lpf_pure_pair_signed_atom_reduced_to_two_prime_signed_interaction_kernel_open`

offdiagonal pure pair atom 的支撑已经完全退化为二素数 Ferrers 图：左侧 `p<=sqrt(N)`，右侧素数 `q`，边条件为 `p<q<=N/p`。随着 `p` 增大，邻域嵌套下降，left/right degree 与总边数全由 prime table 和 `floor(N/p)` 决定。因此 pure atom 剩余不再是支撑或度数问题，而是每条 `(p,q)` 边上的 two-prime signed interaction kernel、orientation parity、ExactUV return 与 internal transition。

```text
pure_pair_signed_atom_target_imported=true
pure_pair_ferrers_support_rule_proved=true
pure_pair_degree_ledger_proved=true
support_graph_signed_kernel_emission_proved=false
two_prime_signed_interaction_kernel_proved=false
pure_semiprime_pair_signed_seed_atom_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PurePairSignedAtomTargetImported | `true` | `false` | 上一层已把 latest seed 原子压到 offdiagonal pure semiprime pair。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| PurePairFerrersSupportRuleClosed | `true` | `true` | pure pair 支撑等价于边条件 `p<q<=N/p`，左邻域按 `p` 递增嵌套下降。 | PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward |
| PurePairDegreeLedgerClosed | `true` | `true` | edge count、left degrees、right degrees 均由 prime table 和 `floor(N/p)` 决定。 | PhiLPFOffDiagonalPurePairFerrersSupportAndDegreeLedgerBeforePushforward |
| SupportGraphDoesNotEmitSignedKernel | `true` | `true` | Ferrers 支撑只排除支撑/度数缺口；不产生每条边的 sign、orientation 或 local factor。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| TwoPrimeSignedInteractionKernelCurrentCorpusProved | `false` | `false` | 当前语料没有提交 `(p,q)` 两素数交互 signed kernel。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| OffDiagonalOrientationParityStillOpen | `true` | `false` | 两素数 kernel 即使存在，orientation parity/branch side 仍需同边绑定。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward |
| OffDiagonalExactUVReturnStillOpen | `true` | `false` | ExactUV fixed pair/source entropy/fiber 与 return tag 仍是并行门。 | PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| InternalTransitionStillPairedGate | `true` | `false` | tail lift 与完整 support key 的 signed compatibility 仍依赖 internal transition。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| PointwisePhiLPFTableStillParallel | `true` | `false` | 逐点 signed table 仍可替代两素数 kernel，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| CompleteBranchTraceWouldSupplyKernel | `true` | `true` | 完整 branch trace 可给每条 `(p,q)` 边的 signed kernel、orientation、ExactUV 与 return tag。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| AtomicTraceWouldSupplyKernel | `true` | `true` | atomic trace signed coefficient 公式可把两素数交互 kernel 作为 trace 字段读取。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| PurePairSignedAtomCurrentCorpusProved | `false` | `false` | 本步只关闭 pure pair 支撑图和度数账本，没有证明 signed seed atom。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步不证明三命题无条件闭合；它只把 pure atom 缺口压到两素数 signed interaction kernel。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |

## 2. 支撑字段

| field | status | meaning |
| --- | --- | --- |
| `left_owner_prime` | `closed_unsigned` | `p <= sqrt(N)` 的 LPF owner layer。 |
| `right_first_prime` | `closed_unsigned` | pure pair 的 second prime `q`，满足 `p<q<=N/p`。 |
| `ferrers_neighbor_rule` | `closed_unsigned` | `N(p)={q prime: p<q<=N/p}`，且 `p` 递增时邻域嵌套下降。 |
| `degree_ledgers` | `closed_unsigned` | left/right degree 和 edge 总数完全由 prime tables 与 floor(N/p) 决定。 |
| `two_prime_signed_interaction_value` | `open_signed` | 每条 `(p,q)` 边的 signed seed/local factor/orientation 仍未由支撑图产生。 |

## 3. 样本审计摘要

| N | left layers | right vertices | edges | nonempty left | max left deg | max right deg | Ferrers | degree ok | sign log10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |
| 30 | 3 | 5 | 7 | 2 | 5 | 2 | `true` | `true` | 2.10721 |
| 100 | 4 | 14 | 30 | 4 | 14 | 4 | `true` | `true` | 9.0309 |
| 997 | 11 | 93 | 287 | 10 | 93 | 10 | `true` | `true` | 86.395609 |
| 5003 | 19 | 366 | 1347 | 19 | 366 | 19 | `true` | `true` | 405.487404 |
| 10000 | 25 | 668 | 2600 | 25 | 668 | 25 | `true` | `true` | 782.677989 |

## 4. 度数摘要

| N | top left degrees | top right degrees | tail left degrees |
| --- | --- | --- | --- |
| 30 | (p=2,deg=5), (p=3,deg=2), (p=5,deg=0) | (q=5,deg=2), (q=7,deg=2), (q=3,deg=1), (q=11,deg=1) | (p=2,deg=5), (p=3,deg=2), (p=5,deg=0) |
| 100 | (p=2,deg=14), (p=3,deg=9), (p=5,deg=5), (p=7,deg=2) | (q=11,deg=4), (q=13,deg=4), (q=7,deg=3), (q=17,deg=3) | (p=2,deg=14), (p=3,deg=9), (p=5,deg=5), (p=7,deg=2) |
| 997 | (p=2,deg=93), (p=3,deg=65), (p=5,deg=43), (p=7,deg=30) | (q=31,deg=10), (q=29,deg=9), (q=37,deg=9), (q=41,deg=9) | (p=17,deg=9), (p=19,deg=7), (p=23,deg=5), (p=29,deg=1), (p=31,deg=0) |
| 5003 | (p=2,deg=366), (p=3,deg=260), (p=5,deg=165), (p=7,deg=123) | (q=71,deg=19), (q=73,deg=19), (q=67,deg=18), (q=79,deg=18) | (p=47,deg=12), (p=53,deg=8), (p=59,deg=6), (p=61,deg=4), (p=67,deg=2) |
| 10000 | (p=2,deg=668), (p=3,deg=468), (p=5,deg=300), (p=7,deg=221) | (q=101,deg=25), (q=103,deg=25), (q=97,deg=24), (q=107,deg=24) | (p=73,deg=11), (p=79,deg=8), (p=83,deg=7), (p=89,deg=5), (p=97,deg=2) |

## 5. 最新保留基

```text
((PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
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
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_pure_pair_ferrers_support_router.py` | `4a1b9ea6207cb61bf9b23f6510918196c8805129e24daf1b5c27a80e6ca40e35` |
| `docs/monograph/prime-matrix-phi-lpf-offdiagonal-pure-semiprime-seed-atom-router.json` | `608a8f088d6c14b5f3ffd1d5be01aef4555d0753e4ae7d70bcd2f986373dd315` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
