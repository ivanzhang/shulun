# Prime Matrix Phi-LPF two-prime ordered no-swap 证书

**状态：** `phi_lpf_two_prime_signed_kernel_no_swap_symmetry_exit_removed`

two-prime signed kernel 不能从交换对称 `p*q=q*p` 中获得。LPF owner source domain 只接纳 canonical ordered edge `(p,q)` with `p<q`；reverse edge `(q,p)` 不在同一 source domain。于是 product symmetry 在 signed kernel 之前已经被 LPF owner 顺序擦除，剩余必须是 edge-local two-prime signed interaction formula 或命名 return。

```text
two_prime_signed_kernel_target_imported=true
lpf_owner_ordered_no_swap_identity_proved=true
product_symmetry_signed_emission_proved=false
edge_local_two_prime_signed_formula_proved=false
two_prime_signed_interaction_kernel_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TwoPrimeSignedKernelTargetImported | `true` | `false` | 上一层已把 pure atom 剩余压到 two-prime signed interaction kernel。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| LPFOwnerOrderedNoSwapIdentity | `true` | `true` | 每个 offdiagonal semiprime product 只有 canonical `(p,q)` source edge，没有 reverse edge。 | PhiLPFOffDiagonalTwoPrimeOrderedLPFOwnerNoSwapSymmetryLedgerBeforePushforward |
| ProductSymmetryCannotEmitSign | `true` | `true` | `p*q=q*p` 不提供第二个 pre-Cauchy source row，不能定义 signed cancellation。 | PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward |
| EdgeLocalSignedFormulaCurrentCorpusProved | `false` | `false` | 当前语料没有为 canonical ordered edge `(p,q)` 提交 signed interaction formula 或 return。 | PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward |
| TwoPrimeSignedKernelCurrentCorpusProved | `false` | `false` | no-swap 只删除交换伪出口，不证明 two-prime signed kernel。 | PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward |
| OffDiagonalOrientationParityStillOpen | `true` | `false` | edge-local formula 仍需 orientation parity/branch side 同边绑定。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward |
| OffDiagonalExactUVReturnStillOpen | `true` | `false` | ExactUV fixed pair/source entropy/fiber 与 return tag 仍是并行门。 | PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| InternalTransitionStillPairedGate | `true` | `false` | tail lift 与完整 support key 的 signed compatibility 仍依赖 internal transition。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| PointwisePhiLPFTableStillParallel | `true` | `false` | 逐点 signed table 仍可替代 edge-local formula，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| CompleteBranchTraceWouldSupplyEdgeFormula | `true` | `true` | 完整 branch trace 可给 ordered edge 的 signed value、orientation、ExactUV 与 return tag。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| AtomicTraceWouldSupplyEdgeFormula | `true` | `true` | atomic trace signed coefficient 公式可把 edge-local formula 作为 trace 字段读取。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步不证明三命题无条件闭合；它只删除 two-prime kernel 的 swap-symmetry 伪出口。 | PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |

## 2. no-swap 字段

| field | status | meaning |
| --- | --- | --- |
| `canonical_lpf_owner_order` | `closed_unsigned` | 每个 distinct semiprime `p*q` 只进入 `(min(p,q),max(p,q))`。 |
| `reverse_edge_absence` | `closed_unsigned` | `(q,p)` 不属于同一 LPF owner source domain，不能用作 cancellation partner。 |
| `product_symmetry_erased_before_signed_kernel` | `closed_unsigned` | `p*q=q*p` 只证明同一整数值，不产生第二个 signed source row。 |
| `edge_local_signed_formula` | `open_signed` | 仍需为 canonical ordered edge `(p,q)` 正向给出 signed interaction formula 或 return。 |

## 3. 样本审计摘要

| N | ordered edges | unordered products | reverse edges | duplicates | small-q | large-q | no-swap ok | sign log10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| 30 | 7 | 7 | 0 | 0 | 3 | 4 | `true` | 2.10721 |
| 100 | 30 | 30 | 0 | 0 | 6 | 24 | `true` | 9.0309 |
| 997 | 287 | 287 | 0 | 0 | 55 | 232 | `true` | 86.395609 |
| 5003 | 1347 | 1347 | 0 | 0 | 171 | 1176 | `true` | 405.487404 |
| 10000 | 2600 | 2600 | 0 | 0 | 300 | 2300 | `true` | 782.677989 |

## 4. edge product 样本

| N | first products | last products |
| --- | --- | --- |
| 30 | (p=2,q=3,n=6), (p=2,q=5,n=10), (p=2,q=7,n=14), (p=2,q=11,n=22) | (p=2,q=11,n=22), (p=2,q=13,n=26), (p=3,q=5,n=15), (p=3,q=7,n=21) |
| 100 | (p=2,q=3,n=6), (p=2,q=5,n=10), (p=2,q=7,n=14), (p=2,q=11,n=22) | (p=5,q=17,n=85), (p=5,q=19,n=95), (p=7,q=11,n=77), (p=7,q=13,n=91) |
| 997 | (p=2,q=3,n=6), (p=2,q=5,n=10), (p=2,q=7,n=14), (p=2,q=11,n=22) | (p=23,q=37,n=851), (p=23,q=41,n=943), (p=23,q=43,n=989), (p=29,q=31,n=899) |
| 5003 | (p=2,q=3,n=6), (p=2,q=5,n=10), (p=2,q=7,n=14), (p=2,q=11,n=22) | (p=61,q=73,n=4453), (p=61,q=79,n=4819), (p=67,q=71,n=4757), (p=67,q=73,n=4891) |
| 10000 | (p=2,q=3,n=6), (p=2,q=5,n=10), (p=2,q=7,n=14), (p=2,q=11,n=22) | (p=89,q=107,n=9523), (p=89,q=109,n=9701), (p=97,q=101,n=9797), (p=97,q=103,n=9991) |

## 5. 最新保留基

```text
((PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
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
PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
```

行/列命题仍未无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_two_prime_ordered_no_swap_router.py` | `224b900fc2b4d62afdc3220e57a0b2b252c8cf4d84979a3010ea1458e6c5e919` |
| `docs/monograph/prime-matrix-phi-lpf-pure-pair-ferrers-support-router.json` | `6ff12d29bab4ff0a9a9fad5794ecf6c74210ef7c51cee0c41b0f99ea1f2bab38` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
