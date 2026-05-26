# Prime Matrix Phi-LPF parity barrier noncircular kernel sync 路由

**状态：** `phi_lpf_parity_barrier_synced_to_noncircular_signed_kernel_open`
**核验日期：** `2026-05-26`

本步把上一轮 atom-cut 前沿继续同步到真正非循环的 signed kernel 门。constructor edge signed fields 经过 same-trace/key return、new payload、source entropy 后会进入 payload/source-entropy 回环；row-level 表沿 signed-source 展开也会回到自身。strict kernel 再剥掉 LPF/Phi 无符号找行和容量后，内部最快主攻是 PhiLPFBucketSignedCoefficientLawBeforePushforward，并同时支付 signed survival 与 row-mass/no-heavy-row。并行可审稿路线是 alpha-row/source-rank 三原子、逐点 signed table、点态 theta/psi 平方根行输入或命名 PDEC/外部 source-keyed trace/Type-II family。

```text
noncircular_kernel_sync_closed=true
lpf_phi_unsigned_scope_exhausted=true
pointwise_phi_lpf_bucket_signed_value_table_proved=false
noncircular_signed_emission_kernel_proved=false
phi_lpf_bucket_signed_coefficient_law_proved=false
alpha_row_anchor_phase_emission_formula_proved=false
external_trace_typeii_family_directly_attaches_now=false
row_column_unconditional_closed=false
```

## 1. 压缩链

| from | to | meaning |
| --- | --- | --- |
| `PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` | `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` | 同一 trace key 与 named return 矩阵删除匿名 signed-field 缺口；生产性出口只能是新 primitive payload/trace。 |
| `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` | `ActualPreCauchySourceDomainAbsoluteEntropyLedger` | 新 payload 若不是 signed-lane 改名，必须携带 actual source-rank/no-collapse 包，第一原子为 source entropy。 |
| `ActualPreCauchySourceDomainAbsoluteEntropyLedger` | `FreshIndependentPreCauchyJointDeclarationLineOutsideConstructorPayloadLoop` | 沿 constructor source-entropy downstream 展开会回到 joint declaration；原回环被切掉，必须提交 fresh independent joint declaration。 |
| `RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands` | `NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows` | row-level 表沿 signed-source 展开会固定点自证；删除固定点后只剩非循环 pre-Cauchy signed emission kernel。 |
| `NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows` | `PhiLPFBucketSignedCoefficientLawBeforePushforward` | strict kernel 的找行/容量部分由 LPF/Phi support stripping 支付；剩余是每个 `(p,m)` bucket 的 signed coefficient law。 |
| `NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | source-rank 收敛支路把 trace/new-payload 出口汇入 alpha-row/source-rank 三原子。 |

## 2. 当前真正前沿

| priority | frontier | type | requires | proved | why |
| ---: | --- | --- | --- | --- | --- |
| 1 | `PhiLPFBucketSignedCoefficientLawBeforePushforward` | bucket signed law | NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger | `false` | 这是 noncircular kernel 剥掉 LPF/Phi 无符号支撑容量后剩下的最小正向 signed coefficient law。 |
| 2 | `NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows` | internal signed kernel discipline | PhiLPFBucketSignedCoefficientLawBeforePushforward on all support keys without downstream recovery | `false` | kernel 纪律仍是禁止回读 row-level 表、source-entropy payload 环或 Phi/payment 下游。 |
| 3 | `AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` | source-rank pointwise kernel | same formal-unit primitive alpha/delta kernel table | `false` | trace/new-payload/source-rank 线在逐 primitive alpha/delta 核表上汇合。 |
| 4 | `PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward` | direct pointwise bypass | complete signed values on fixed Phi-LPF support before pushforward | `false` | 若直接给出逐点 signed table，就绕开 LPF 无符号奇偶障碍。 |
| 5 | `PointwiseThetaPsiCOneInput` | external prime-distribution bypass | theta((kP,(k+1)P))>0 or psi(I)>PrimePowerTail(I) for every strict row | `false` | 这是直接数素数的平方根行尺度输入。 |
| 6 | `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR ExternalDIBFIKuznetsovDispersionTheoremMatch` | controlled return or external dispersion | same-set PDEC scope or source-keyed signed coefficient family suitable for dispersion/Kuznetsov | `false` | 外部谱工具不能吃无符号 LPF support；必须先有 admissible signed family。 |

## 3. 外部输入边界

| input | supplies | missing interface | direct close now | source |
| --- | --- | --- | --- | --- |
| Guth--Maynard zero-density / short intervals | PNT in short intervals of length x^(17/30+o(1)) via zero-density estimates | Prime Matrix strict rows have length P near x=P^2, i.e. x^(1/2) | `false` | https://arxiv.org/abs/2405.20552 |
| Le Duc Hieu short-interval APs of primes | many k-term arithmetic progressions of primes in every interval [x,x+x^theta] once theta>17/30 | this transfers the same theta>17/30 threshold, still above the pointwise row scale x^(1/2) | `false` | https://arxiv.org/abs/2509.04883 |
| Runbo Li Harman-sieve short intervals | prime existence in intervals [x-x^0.52,x] for large x | 0.52 remains above the required 1/2 row scale | `false` | https://arxiv.org/abs/2308.04458 |
| Fouvry--Kowalski--Michel--Sawin trace functions | bilinear trace-function bounds below Polya-Vinogradov under monodromy hypotheses | no ell-adic trace-function family has been constructed from the Prime Matrix source key | `false` | https://arxiv.org/abs/2511.09459 |
| Milicevic--Qin--Wu Kloosterman bilinear forms | power-saving bilinear Kloosterman bounds modulo arbitrary q | no two-variable Kloosterman coefficient family is emitted by the current signed kernel | `false` | https://arxiv.org/abs/2511.07550 |
| Wright trilinear Kloosterman fractions | trilinear Kloosterman-fraction estimates for unbalanced convolution shapes | no trilinear beta sequence or source-key convolution exists yet | `false` | https://arxiv.org/abs/2604.25177 |
| Pascadi non-abelian / Type-II inputs | composite-modulus Type-II/Kloosterman technology | current LPF buckets are unsigned and not well-factorable signed coefficients | `false` | https://arxiv.org/abs/2511.08445 |

## 4. 下一手

```text
chosen_internal_primary_attack_target=PhiLPFBucketSignedCoefficientLawBeforePushforward
chosen_kernel_discipline_target=NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows
chosen_parallel_source_rank_attack_target=AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows
parallel_direct_bypass=PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

最新开放口：

```text
AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND (AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR (PhiLPFBucketSignedCoefficientLawBeforePushforward AND NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger) OR (AlphaRowAnchorPhaseEmissionFormulaLedger AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR PointwiseThetaPsiCOneInput OR ExternalSourceKeyedTraceTypeIIFamily) AND CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/claim-status-table.md` | `77139b71d1a8681a36269845bc2797bfe6e994f0eac579943121461b6e34f6d8` |
| `docs/monograph/external-theorem-index.md` | `1e1253e511cd7bc7893d43087624dbbf1f445da0b7b3db3f3ff9915edb6783b4` |
| `docs/monograph/frontier-honest-status-and-true-side-theorems-20260522.md` | `5d451038506325af7bc61deb91b7e8c8edc44897be66786562c56eee51f0ff98` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-new-payload-source-atom-alignment-rebase-sync-router.json` | `724bca876f0e9b299cad7c96b49bb054abca988a9db166029c304d81dc234dd9` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-noncircular-kernel-bucket-signed-law-sync-router.json` | `38daa9f5a040d5fad3d28a8f43dc506c89e46439a40dd11ec22716b493e41291` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.json` | `7f2888e974e74673edf61a93e53296526b0a4edbf52d59cebb9f114fc3252e3a` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-rebase-sync-router.json` | `4eff08348ce7bfe7b6833bad0a43be65f9e05afd519707012c523a5a47e408f8` |
| `docs/monograph/prime-matrix-phi-lpf-latest-constructor-source-entropy-payload-loop-cut-sync-router.json` | `d2c842e1e6a0fb6f3a99cd370bb18739ac0e72130b688e11b86b400c034dd9b0` |
| `docs/monograph/prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json` | `e639d4fd829cce129de043a48d3f002f620b3050560253739825b9cb02323ed8` |
| `docs/monograph/prime-matrix-phi-lpf-parity-barrier-atom-cut-frontier-router.json` | `bd9f84a201f392fa18f2a536569b045cbde6bba02402e1acdfd46c19f1bdf91d` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/three-claims-actual-load-closure-contracts.md` | `56ef0b7cac6b408c0dc3cb4189de6f90414a0b0736e17ea31f10f7113ee0a85f` |
| `docs/monograph/three-claims-breakthrough-route-synthesis-20260525.md` | `84e0082a95cdc954c48d32d33a37e220635b69b24ceae8b1816cb56bb4e83482` |
| `docs/monograph/three-claims-formal-to-actual-critical-load-frontier.md` | `3e99e3b18c5b877e5634d9d0adfef7607689800ad2223749293b2516ef6b1b52` |
| `experiments/prime_matrix_phi_lpf_parity_barrier_noncircular_kernel_sync_router.py` | `1445be13a1dad302ca039dc114f5e62e738280eb6cbb7c400a9c788c4aec127d` |
| `paper/contradiction-field-monograph/contradiction-field-monograph.tex` | `6ab12357667720b1e6d76d5be564ccf4fa9e9fd509e2fd62f3ba7cefc979cb31` |
