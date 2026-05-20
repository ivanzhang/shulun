# Prime Matrix Phi-LPF first-edge slab frontier 证书

**状态：** `phi_lpf_edge_multiplier_table_split_into_first_seed_and_internal_transition_open`

逐 edge signed multiplier 表可严格拆成两个子表：第一边 `(p,1,q,q)` 的 semiprime signed seed slab，以及 `prefix>1` 的内部 prime-adjoin signed transition law。LPF/Phi 对第一边给出精确 q-rough continuation 纤维公式 `mass(p,q)=Phi(floor(N/(p*q)),q)`，但该公式只支付支撑和 occurrence mass，不产生 first seed signed value，也不产生内部 transition 的非零 local factor。因此下一直接主攻为 semiprime first-edge signed seed table；同时必须配套内部 prime-adjoin transition law，或改由逐点 signed table / branch trace / atomic trace 提供。

```text
edge_signed_multiplier_table_imported=true
edge_table_split_into_first_seed_and_internal_transition=true
first_edge_phi_fiber_formula_proved=true
semiprime_first_edge_signed_seed_table_proved=false
internal_prime_adjoin_signed_transition_law_proved=false
edge_signed_multiplier_table_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EdgeMultiplierTableTargetImported | `true` | `false` | 上一层已把 step update 压到逐 ordered edge signed multiplier 表。 | PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward |
| EdgeTableSplitsIntoFirstSeedAndInternalTransition | `true` | `true` | 每条 LPF path 唯一分成第一边 seed slab 与后续内部 prime-adjoin transitions。 | PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| FirstEdgePhiFiberFormula | `true` | `true` | 第一边 `(p,q)` 的 occurrence mass 精确为 Phi(floor(N/(p*q)),q)，即 q-rough tail fiber。 | PhiLPFFirstEdgeQRoughContinuationFiberLedger |
| FirstEdgeSeedCannotBeRecoveredFromCounts | `true` | `true` | Phi/LPF 只给 `(p,q)` 纤维大小；不赋 first seed signed value、branch trace 或 ExactUV。 | PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward |
| InternalTransitionCannotBeRecoveredByDivision | `true` | `true` | 内部 transition 需要非零前缀或命名回流，不能用未知 pointwise signed value 作后验除法。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| FirstSeedTableCurrentCorpusProved | `false` | `false` | 当前材料没有为所有 semiprime first edges 提交 prepushforward signed seed 表。 | PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward |
| InternalPrimeAdjoinTransitionCurrentCorpusProved | `false` | `false` | 当前材料没有为所有内部 prime-adjoin edges 提交 signed local-factor transition law。 | PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |
| CompleteBranchTraceWouldSupplyBothSlabs | `true` | `true` | 完整 branch trace 可同时给 first seed、内部 transition、return tag 与 ExactUV 字段。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| AtomicTraceWouldSupplyBothSlabs | `true` | `true` | atomic trace signed coefficient 公式可把两张表作为同一 trace 的字段读取。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| PointwisePhiLPFTableStillParallel | `true` | `false` | 逐点 signed value table 仍是直接替代，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| ExactUVStillParallelGate | `true` | `false` | 两张 edge 表即使存在，ExactUV source entropy/fiber 仍是并行门。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只把 edge multiplier 表拆成 first seed slab 与 internal transition；未证明三命题无条件闭合。 | PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward |

## 2. first-edge seed slab 字段合同

| field | meaning |
| --- | --- |
| `semiprime_edge_key` | 第一边 `(p,1,q,q)`，对应真实 composite key `p*q` 与 q-rough tail fiber。 |
| `first_seed_signed_value` | 从 virtual unit 到 `q` 的 signed seed；不能从 Phi 的 prime row 或 payment 原像读取。 |
| `q_rough_tail_fiber_lift` | 同一 `(p,q)` seed 对所有 q-rough tail 的继续传输规则。 |
| `source_trace_or_return_tag` | pre-Cauchy source trace、branch key、ExactUV 输出；失败时进入命名回流。 |

## 3. internal transition 字段合同

| field | meaning |
| --- | --- |
| `internal_edge_key` | 内部边 `(p,prefix,q,prefix*q)`，其中 `prefix>1` 且二者都在同一 owner bucket。 |
| `signed_adjoin_multiplier` | 乘入下一素因子 `q` 的 sign/local-factor/truncation 乘子。 |
| `nonzero_predecessor_or_return` | 若前缀 signed value 为零或 local factor 消失，必须给命名 return，而不是继续除法。 |
| `path_product_compatibility` | first seed 与内部乘子相乘后，等于最终 support key 的 signed coefficient。 |

## 4. 样本审计摘要

| N | support | first occ | internal occ | first types | max depth | Phi fiber ok | first type sign log10 | first occ sign log10 | internal occ sign log10 |
| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |
| 30 | 19 | 19 | 11 | 10 | 3 | `true` | 3.0103 | 5.71957 | 3.31133 |
| 100 | 74 | 74 | 66 | 34 | 5 | `true` | 10.23502 | 22.27622 | 19.86798 |
| 997 | 828 | 828 | 1041 | 298 | 8 | `true` | 89.706939 | 249.252836 | 313.372225 |
| 5003 | 4332 | 4332 | 6239 | 1366 | 11 | `true` | 411.206974 | 1304.061941 | 1878.126143 |
| 10000 | 8770 | 8770 | 13216 | 2625 | 12 | `true` | 790.203739 | 2640.033062 | 3978.412423 |

## 5. 最大 first-edge 纤维

| N | top fibers |
| --- | --- |
| 30 | (p=2,q=2,mass=7), (p=2,q=3,mass=3), (p=3,q=3,mass=2), (p=2,q=5,mass=1) |
| 100 | (p=2,q=2,mass=25), (p=2,q=3,mass=8), (p=3,q=3,mass=6), (p=2,q=5,mass=3) |
| 997 | (p=2,q=2,mass=249), (p=2,q=3,mass=83), (p=3,q=3,mass=55), (p=2,q=5,mass=33) |
| 5003 | (p=2,q=2,mass=1250), (p=2,q=3,mass=417), (p=3,q=3,mass=278), (p=2,q=5,mass=167) |
| 10000 | (p=2,q=2,mass=2500), (p=2,q=3,mass=833), (p=3,q=3,mass=556), (p=2,q=5,mass=333) |

## 6. 最新保留基

```text
((PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward AND PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward) OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward
PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward
```

并行直接入口：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

行/列命题仍未无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_first_edge_slab_frontier_router.py` | `ec9445a3906d6d729b0dfeae076a81ed90518ae7f00aba0d759018736e5e37a5` |
| `docs/monograph/prime-matrix-phi-lpf-step-local-factor-update-frontier-router.json` | `c4346bdf5a7500f4d6c50f9abd0255bd916ff288dcae000cd2caa87434f38392` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
