# Prime Matrix Phi-LPF offdiagonal pure semiprime seed atom 证书

**状态：** `phi_lpf_offdiagonal_source_tuple_signed_formula_split_to_pure_pair_atom_and_tail_lift_open`

offdiagonal source tuple signed seed formula 进一步强制拆成 pure semiprime pair `tail=1` seed atom 与 `tail>1` q-rough continuation lift。每个 ordered type `(p,q), p<q` 恰有一个 pure atom `p*q`；所有 tail 非单位 occurrence 不是新的 first seed，只能由同一 pure atom 加 internal transition lift 解释。剩余最新窄口因此变为 `PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward`，并仍需 orientation parity、ExactUV return、internal transition 与 common packet。

```text
offdiagonal_source_tuple_signed_seed_target_imported=true
pure_semiprime_pair_seed_atom_bijection_proved=true
tail_nonunit_reduced_to_internal_transition_lift=true
tail_lift_phi_minus_one_mass_formula_proved=true
pure_semiprime_pair_signed_seed_atom_proved=false
offdiagonal_source_tuple_signed_seed_formula_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| OffDiagonalSourceTupleSignedFormulaTargetImported | `true` | `false` | 上一层已把 offdiagonal seed 的 signed 缺口压到 source tuple signed seed formula。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward |
| PureSemiprimePairSeedAtomBijection | `true` | `true` | 每个 offdiagonal type `(p,q)` 恰有一个 tail=1 pure semiprime seed atom。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| TailNonunitNotNewFirstSeed | `true` | `true` | `tail>1` occurrences 共享同一 first seed type，只增加 internal transition lift。 | PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward |
| PhiMinusOneTailLiftMassFormula | `true` | `true` | 每个 `(p,q)` 的 tail-lift mass 为 `Phi(floor(N/(p*q)),q)-1`。 | PhiLPFOffDiagonalQRoughTailLiftInternalTransitionCompatibilityBeforePushforward |
| PureSeedSignedValueCurrentCorpusProved | `false` | `false` | 当前语料没有给出 pure pair `(p,q)` 的 prepushforward signed seed atom。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward |
| TailLiftSignedCompatibilityNeedsInternalTransition | `true` | `false` | tail lift 的 signed compatibility 仍依赖 internal prime-adjoin transition law。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| OffDiagonalOrientationParityStillOpen | `true` | `false` | pure atom 仍需 orientation parity、branch side 与 local factor law。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward |
| OffDiagonalExactUVReturnStillOpen | `true` | `false` | ExactUV fixed pair/source entropy/fiber 与 return tag 仍是并行门。 | PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| PointwisePhiLPFTableStillParallel | `true` | `false` | 逐点 signed table 仍可替代 pure atom formula，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| CompleteBranchTraceWouldSupplyPureAtom | `true` | `true` | 完整 branch trace 可给 pure atom signed value、orientation、ExactUV 和 return tag。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| AtomicTraceWouldSupplyPureAtom | `true` | `true` | atomic trace signed coefficient 公式可把 pure semiprime pair seed 作为 trace 字段读取。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| OffDiagonalSourceTupleSignedFormulaCurrentCorpusProved | `false` | `false` | 本步只把 source tuple signed formula 拆成 pure atom 与 tail lift，没有证明 signed formula。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步不证明三命题无条件闭合；它只把 offdiagonal signed formula 的 first-seed 原子定位到 pure semiprime pair。 | PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |

## 2. pure atom 字段

| field | status | meaning |
| --- | --- | --- |
| `pure_pair_key` | `closed_unsigned` | ordered pair `(p,q)` with `p<q` and value `p*q`。 |
| `tail_identity_t_equals_1` | `closed_unsigned` | 每个 offdiagonal type 的 first seed atom 是唯一 tail=1 occurrence。 |
| `tail_lift_mass` | `closed_unsigned` | `Phi(floor(N/(p*q)),q)-1`，不是新 first seed，只能由 internal transition lift 处理。 |
| `pure_pair_signed_value` | `open_signed` | 必须由 source tuple 在 pushforward 前正向发射。 |
| `orientation_and_exactuv` | `open_signed_exactuv` | orientation parity、branch side、ExactUV fixed pair 与 return tag 仍未闭合。 |

## 3. 样本审计摘要

| N | types | pure atoms | tail lift | total occ | pure share | tail share | pure ok | tail ok | pure sign log10 | tail transition log10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: |
| 30 | 7 | 7 | 2 | 9 | 0.777777777778 | 0.222222222222 | `true` | `true` | 2.10721 | 0.60206 |
| 100 | 30 | 30 | 11 | 41 | 0.731707317073 | 0.268292682927 | `true` | `true` | 9.0309 | 3.31133 |
| 997 | 287 | 287 | 211 | 498 | 0.576305220884 | 0.423694779116 | `true` | `true` | 86.395609 | 63.517329 |
| 5003 | 1347 | 1347 | 1333 | 2680 | 0.502611940299 | 0.497388059701 | `true` | `true` | 405.487404 | 401.272984 |
| 10000 | 2600 | 2600 | 2868 | 5468 | 0.475493782004 | 0.524506217996 | `true` | `true` | 782.677989 | 863.354028 |

## 4. 最大 tail-lift 纤维

| N | top tail lifts |
| --- | --- |
| 30 | (p=2,q=3,lift=2) |
| 100 | (p=2,q=3,lift=7), (p=2,q=5,lift=2), (p=2,q=7,lift=1), (p=3,q=5,lift=1) |
| 997 | (p=2,q=3,lift=82), (p=2,q=5,lift=32), (p=3,q=5,lift=21), (p=2,q=7,lift=18) |
| 5003 | (p=2,q=3,lift=416), (p=2,q=5,lift=166), (p=3,q=5,lift=110), (p=2,q=7,lift=94) |
| 10000 | (p=2,q=3,lift=832), (p=2,q=5,lift=332), (p=3,q=5,lift=221), (p=2,q=7,lift=190) |

## 5. 最新保留基

```text
((PhiLPFOffDiagonalPureSemiprimePairSignedSeedAtomBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
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
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_offdiagonal_pure_semiprime_seed_atom_router.py` | `87745abdfbead6bcc1a5c926fd4a57c14ef9310200a916cb3dce8c976a424e50` |
| `docs/monograph/prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json` | `f9b2e9eaf8020cde5952237044a1d62308564951b9e00f4cf163ab46d5b62ccf` |
| `docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.json` | `111cc0440f1f16e47cb791878a70f328fdff5122717efe007d08c0d704d62bfa` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
