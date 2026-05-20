# Prime Matrix Phi-LPF offdiagonal semiprime seed tuple-fields 证书

**状态：** `phi_lpf_offdiagonal_semiprime_seed_reduced_to_source_tuple_signed_formula_open`

offdiagonal `(p,q), p<q` first seed 的无符号来源字段可以完全闭合：每个 occurrence 唯一写成 `(owner_p, first_q, q_rough_tail_t)`，且总质量等于 `sum Phi(floor(N/(p*q)),q)`。这排除了 diagonal/square-base alias，也把 Phi-LPF 的贡献精确限定为支撑、纤维和 tuple 字段。剩余不能从这些字段反推，而必须正向提交 offdiagonal source tuple 的 signed seed formula、orientation parity/branch side、ExactUV fixed pair/return tag，并配套 internal prime-adjoin transition。

```text
offdiagonal_seed_target_imported=true
offdiagonal_source_tuple_bijection_proved=true
offdiagonal_phi_tail_fiber_mass_proved=true
offdiagonal_unsigned_tuple_fields_closed=true
offdiagonal_signed_seed_formula_proved=false
offdiagonal_orientation_parity_law_proved=false
offdiagonal_exactuv_fixed_pair_return_ledger_proved=false
offdiagonal_ordered_semiprime_signed_seed_table_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| OffDiagonalSeedTargetImported | `true` | `false` | 上一层已把最新窄口定位为 offdiagonal ordered semiprime first seed signed table。 | PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| OffDiagonalSourceTupleBijection | `true` | `true` | 每个 offdiagonal occurrence 唯一写成 `(p,q,t)`，其中 `p<q` 且 `t` 为 q-rough。 | PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward |
| PhiTailFiberMassMatchesTupleLedger | `true` | `true` | tuple occurrence 总数等于 `sum_{p<q} Phi(floor(N/(p*q)),q)`。 | PhiLPFOffDiagonalQRoughTailFiberMassLedger |
| DiagonalAliasRemoved | `true` | `true` | `q>p` 将 offdiagonal source tuple 与 square-base diagonal common packet 分离。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| UnsignedTupleFieldsDoNotEmitSign | `true` | `true` | LPF/Phi 字段只给 owner、first prime、tail 与容量；不含 signed seed 或 orientation parity。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward |
| OffDiagonalSignedSeedFormulaCurrentCorpusProved | `false` | `false` | 当前语料尚未给出 `(p,q)` source tuple 的 prepushforward signed seed 公式。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward |
| OffDiagonalOrientationParityCurrentCorpusProved | `false` | `false` | 当前语料尚未给出 offdiagonal seed 的 orientation parity、branch side 与 local factor law。 | PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward |
| OffDiagonalExactUVReturnCurrentCorpusProved | `true` | `false` | ExactUV fixed pair/source entropy/fiber 与 return tag 仍是并行门。 | PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |
| InternalTransitionStillPairedGate | `true` | `false` | offdiagonal first seed 即使给出，tail 非单位 occurrence 仍需要内部 prime-adjoin transition law。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| PointwisePhiLPFTableStillParallel | `true` | `false` | 逐点 signed table 仍可替代本 seed formula，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| CompleteBranchTraceWouldSupplyTupleFields | `true` | `true` | 完整 branch trace 可一次给 source tuple、signed value、orientation、ExactUV 和 return tag。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| AtomicTraceWouldSupplyTupleFields | `true` | `true` | atomic trace signed coefficient 公式可把 offdiagonal seed 作为 trace 字段读取。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| OffDiagonalSeedTableCurrentCorpusProved | `false` | `false` | 本步只关闭 offdiagonal source tuple 的无符号字段账本，没有证明 signed seed table。 | PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步不证明三命题无条件闭合；它只把 offdiagonal seed 缺口压到 signed formula/orientation/ExactUV 字段。 | PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward |

## 2. source tuple 字段

| field | status | meaning |
| --- | --- | --- |
| `owner_prime_p` | `closed_unsigned` | LPF owner bucket；composite value 的最小素因子为 p。 |
| `first_rough_prime_q` | `closed_unsigned` | cofactor value/p 的最小素因子，且严格 q>p。 |
| `q_rough_tail_t` | `closed_unsigned` | tail t 满足所有素因子不小于 q；纤维质量由 Phi(floor(N/(p*q)),q) 支付。 |
| `offdiagonal_type_key` | `closed_unsigned` | ordered pair (p,q)，不与 diagonal square-base packet 混同。 |
| `signed_seed_value` | `open_signed` | 必须在 pushforward 前由 source tuple 正向给出，不能从 Phi 计数或 tail mass 反推。 |
| `orientation_parity_branch_side` | `open_signed` | alpha/delta side、orientation parity 与 branch trace 仍需独立字段。 |
| `exactuv_fixed_pair_return_tag` | `open_exactuv` | ExactUV fixed pair、source entropy/fiber 与失败 return tag 仍需并行证明。 |

## 3. 样本审计摘要

| N | types | tuple occ | Phi sum | tail=1 | tail>1 | max tail | tuple ok | type sign log10 | occurrence shadow log10 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 30 | 7 | 9 | 9 | 7 | 2 | 5 | `true` | 2.10721 | 2.70927 |
| 100 | 30 | 41 | 41 | 30 | 11 | 15 | `true` | 9.0309 | 12.34223 |
| 997 | 287 | 498 | 498 | 287 | 211 | 165 | `true` | 86.395609 | 149.912938 |
| 5003 | 1347 | 2680 | 2680 | 1347 | 1333 | 833 | `true` | 405.487404 | 806.760388 |
| 10000 | 2600 | 5468 | 5468 | 2600 | 2868 | 1665 | `true` | 782.677989 | 1646.032016 |

## 4. 最大 offdiagonal 纤维

| N | top fibers |
| --- | --- |
| 30 | (p=2,q=3,mass=3), (p=2,q=5,mass=1), (p=2,q=7,mass=1), (p=2,q=11,mass=1) |
| 100 | (p=2,q=3,mass=8), (p=2,q=5,mass=3), (p=2,q=7,mass=2), (p=3,q=5,mass=2) |
| 997 | (p=2,q=3,mass=83), (p=2,q=5,mass=33), (p=3,q=5,mass=22), (p=2,q=7,mass=19) |
| 5003 | (p=2,q=3,mass=417), (p=2,q=5,mass=167), (p=3,q=5,mass=111), (p=2,q=7,mass=95) |
| 10000 | (p=2,q=3,mass=833), (p=2,q=5,mass=333), (p=3,q=5,mass=222), (p=2,q=7,mass=191) |

## 5. 最新保留基

```text
((PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward AND PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward AND PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward
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
| `experiments/prime_matrix_phi_lpf_offdiagonal_semiprime_seed_tuple_fields_router.py` | `b1c832e551e954a40557bbe5dcd4d37c84695b5773b8a53b928cf05128ebd486` |
| `docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json` | `10b88bb8d80a793ab8ed16263cbe5efc4d47c72fdcc544ed7d97e559bda6788d` |
| `docs/monograph/prime-matrix-phi-lpf-first-edge-slab-frontier-router.json` | `111cc0440f1f16e47cb791878a70f328fdff5122717efe007d08c0d704d62bfa` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
