# Prime Matrix Phi-LPF edge-local two-prime field-cut 证书

**状态：** `phi_lpf_edge_local_unsigned_edge_labels_closed_signed_atom_fields_open`

edge-local formula-or-return 的无符号边标签已经闭合：每条 canonical `(p,q)` edge 的 owner、product、LPF bucket、Ferrers rank/degree 与 atom multiplicity 均由 LPF/Phi/Ferrers 账本确定。剩余不再是支撑或容量问题，而是逐 edge 的 signed atom fields：signed value、local factor、orientation/branch side、ExactUV fixed pair 与 pre-Cauchy source row，或对应的命名 return tag。

```text
edge_local_formula_target_imported=true
edge_local_closed_unsigned_label_ledger_proved=true
edge_label_bijection_proved=true
lpf_bucket_product_fields_proved=true
ferrers_rank_degree_fields_proved=true
edge_atom_multiplicity_one_proved=true
signed_atom_field_table_proved=false
orientation_parity_branch_side_proved=false
exactuv_fixed_pair_return_tag_proved=false
edge_local_signed_interaction_formula_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EdgeLocalFormulaTargetImported | `true` | `false` | 上一层已删除 swap-symmetry 伪出口，直接剩余为 edge-local formula-or-return。 | PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward |
| CanonicalEdgeLabelBijectionClosed | `true` | `true` | 每个 canonical `(p,q)` pure atom 有唯一 closed edge label。 | PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward |
| LPFBucketAndProductFieldsClosed | `true` | `true` | `product=pq` 与 `LPF(product)=p` 已在 edge label 中固定。 | PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward |
| FerrersRankDegreeFieldsClosed | `true` | `true` | row/column rank-degree 字段由 Ferrers 支撑和 prime-count floor 公式给出。 | PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward |
| AtomMultiplicityOneClosed | `true` | `true` | 每个 distinct product `pq` 只带一个 pure-pair source atom。 | PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward |
| LPFPhiFieldsAreUnsignedOnly | `true` | `true` | 闭合字段只含 owner、prime、product、rank、degree、multiplicity，不含 sign/local-factor/orientation/ExactUV 槽。 | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward |
| EdgeLocalSignedAtomFieldsCurrentCorpusProved | `false` | `false` | 当前语料没有提交逐 edge 的 signed seed/local factor 表或命名 return tag 表。 | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward |
| OrientationParityStillOpen | `true` | `false` | orientation parity 可由完整 branch trace 条件性供给，但当前不是已证明字段。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward |
| ExactUVReturnTagStillOpen | `true` | `false` | ExactUV fixed pair/fiber/return tag 仍是独立命名门。 | PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| CommonSourcePacketStillOpen | `true` | `false` | signed value 必须来自 pre-Cauchy source row；closed label 不是 source packet。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| PointwiseTableStillParallel | `true` | `false` | 逐点 Phi-LPF signed table 仍可替代本 edge-local 表，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| TraceGeneratorsStillConditional | `true` | `true` | complete branch trace 或 atomic trace 若提交，可同时供给 signed/orientation/ExactUV 字段。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| EdgeLocalSignedInteractionFormulaCurrentCorpusProved | `false` | `false` | 本步只关闭 edge label；不证明 edge-local signed interaction formula。 | PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步不证明三命题无条件闭合；它把最新剩余压到 signed atom fields 或 named return。 | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward |

## 2. 已闭合 edge label 字段

| field | status | meaning |
| --- | --- | --- |
| `owner_p` | `closed_unsigned` | LPF owner prime，满足 `p <= sqrt(N)`。 |
| `first_q` | `closed_unsigned` | offdiagonal pure pair 的第二素数，满足 `p<q<=N/p`。 |
| `product_pq` | `closed_unsigned` | atom integer value `pq`，其最小素因子为 `p`。 |
| `ferrers_row_rank_and_degree` | `closed_unsigned` | row rank 与 degree `pi(floor(N/p))-pi(p)`。 |
| `ferrers_column_rank_and_degree` | `closed_unsigned` | column degree `pi(min(q-1,floor(N/q)))`。 |
| `edge_atom_multiplicity` | `closed_unsigned` | 每个 canonical product `pq` 只有一个 pure atom label。 |

## 3. 仍开放 signed/return 字段

| field | remaining | meaning |
| --- | --- | --- |
| `signed_seed_value` | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward | canonical edge 自身的 signed atom 值。 |
| `local_factor_multiplier` | PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward | first-edge local factor 或 zero/return 标签。 |
| `orientation_parity` | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward | 同一 `(p,q)` 边上的 orientation parity 与 branch side。 |
| `alpha_delta_side` | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward | alpha/delta 分支侧别和符号方向。 |
| `exactuv_fixed_pair` | PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward | edge-local ExactUV fixed pair、fiber 与 return tag。 |
| `pre_cauchy_source_row` | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket | 真正发出 signed coefficient 的 pre-Cauchy source row。 |

## 4. 样本审计摘要

| N | edges | labels | products | LPF ok | row deg ok | col deg ok | atom x1 | sign log10 |
| --- | ---: | ---: | ---: | --- | --- | --- | --- | ---: |
| 30 | 7 | 7 | 7 | `true` | `true` | `true` | `true` | 2.10721 |
| 100 | 30 | 30 | 30 | `true` | `true` | `true` | `true` | 9.0309 |
| 997 | 287 | 287 | 287 | `true` | `true` | `true` | `true` | 86.395609 |
| 5003 | 1347 | 1347 | 1347 | `true` | `true` | `true` | `true` | 405.487404 |
| 10000 | 2600 | 2600 | 2600 | `true` | `true` | `true` | `true` | 782.677989 |

## 5. edge label 样本

| N | sample labels |
| --- | --- |
| 30 | (p=2,q=3,n=6,rd=5,cd=1), (p=2,q=5,n=10,rd=5,cd=2), (p=2,q=7,n=14,rd=5,cd=2), (p=2,q=11,n=22,rd=5,cd=1) |
| 100 | (p=2,q=3,n=6,rd=14,cd=1), (p=2,q=5,n=10,rd=14,cd=2), (p=2,q=7,n=14,rd=14,cd=3), (p=2,q=11,n=22,rd=14,cd=4) |
| 997 | (p=2,q=3,n=6,rd=93,cd=1), (p=2,q=5,n=10,rd=93,cd=2), (p=2,q=7,n=14,rd=93,cd=3), (p=2,q=11,n=22,rd=93,cd=4) |
| 5003 | (p=2,q=3,n=6,rd=366,cd=1), (p=2,q=5,n=10,rd=366,cd=2), (p=2,q=7,n=14,rd=366,cd=3), (p=2,q=11,n=22,rd=366,cd=4) |
| 10000 | (p=2,q=3,n=6,rd=668,cd=1), (p=2,q=5,n=10,rd=668,cd=2), (p=2,q=7,n=14,rd=668,cd=3), (p=2,q=11,n=22,rd=668,cd=4) |

## 6. 最新保留基

```text
((PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward
```

配套仍需：

```text
PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward
PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_edge_local_two_prime_field_cut_router.py` | `459043b00944af519872ffa1e26723df11f64d0aaaddd65e96f9f772d8b1ffc2` |
| `docs/monograph/prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json` | `68844af913e21b39317b6f47244070c96d3c5e4b630a00b1a0c7a029f66148f6` |
| `docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json` | `6ff12d29bab4ff0a9a9fad5794ecf6c74210ef7c51cee0c41b0f99ea1f2bab38` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
