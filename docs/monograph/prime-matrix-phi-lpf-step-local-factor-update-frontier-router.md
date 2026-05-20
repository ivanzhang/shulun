# Prime Matrix Phi-LPF step local factor update frontier 证书

**状态：** `phi_lpf_step_local_factor_update_reduced_to_edge_signed_multiplier_table_open`

ordered LPF path 已闭合后，`PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward` 不再是路径选择问题，而是逐 ordered edge 的 signed multiplier 表问题。对每条 `(p,prefix,q,prefix*q)` 边，必须正向给出 sign/local-factor/truncation 乘子、orientation parity 增量、alpha/delta branch 与 exact-UV 转移、非零或命名回流，以及沿路径乘积的推前前恒等式。`prefix=1` 的第一边也必须由该表给出，不能读取 Phi 中被排除的 prime row 或 payment 原像。因此最新直接主攻收窄为 `PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward`；条件生成器是 exact branch trace / atomic trace / primitive origin identity，并行替代仍是逐 Phi-LPF key signed value table。

```text
ordered_lpf_edge_path_imported=true
step_update_reduced_to_edge_multiplier_table=true
edge_signed_multiplier_table_proved=false
rough_cofactor_step_local_factor_update_law_proved=false
pointwise_phi_lpf_bucket_signed_value_table_proved=false
row_column_unconditional_closed=false
```

## 1. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| StepLocalFactorUpdateTargetImported | `true` | `false` | 上一层已把 ordered coherence 移除，最新直接缺口就是 step local factor update。 | PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward |
| OrderedLPFEdgePathImported | `true` | `true` | LPF 最小素因子剥离已给出同一 owner bucket 内唯一 ordered edge path。 | path/order already paid |
| StepUpdateEquivalentToEdgeMultiplierTable | `true` | `true` | 路径固定后，step update 等价于在每条 ordered edge 上给 signed multiplier，并沿路径相乘。 | PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward |
| FirstEdgeCannotUsePrimeRowLeak | `true` | `true` | `prefix=1` 的第一边是 multiplier 表字段；不能把 Phi 公式排除的 prime row 当作 composite signed seed。 | PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward |
| PhiLPFCountsDoNotDetermineMultipliers | `true` | `true` | 同一 support/order 可形式承载独立 edge sign decorations；LPF/Phi 只给 domain，不给奇 signed 数据。 | PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward |
| CompleteBranchTraceWouldSupplyMultipliers | `true` | `true` | 若 exact actual noncanonical branch trace 存在，orientation、local factor、branch key 与 return tag 可同 trace 给出。 | ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn |
| AtomicTraceWouldSupplySameRowSignedValue | `true` | `true` | 若 atomic branch trace signed coefficient 公式存在，edge multiplier 与逐点 signed value 可作为同一 trace 的字段读取。 | ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |
| PrimitiveOriginIdentityStillOpen | `true` | `false` | primitive summand 的 signed coefficient 来源恒等式仍未给出，不能反向生成 edge multiplier。 | PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward |
| ExactUVStillParallelGate | `true` | `false` | 即使 edge multiplier 表存在，ExactUV source entropy/fiber 或 bounded incidence 仍是并行门。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| PointwisePhiLPFTableStillOpen | `true` | `false` | 直接提交逐 Phi-LPF key signed value table 仍是并行替代，但当前未证明。 | PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward |
| EdgeMultiplierTableCurrentCorpusProved | `false` | `false` | 当前材料没有逐 ordered edge 的 signed multiplier、非零 local factor、branch/ExactUV 转移和推前前乘积恒等式表。 | PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步只把 step update 压成 edge multiplier 表；未证明三命题无条件闭合。 | PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn OR ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn |

## 2. edge multiplier 字段合同

| field | meaning |
| --- | --- |
| `edge_key` | 同一 owner bucket 内的有序边 `(p, prefix, q, prefix*q)`。 |
| `source_tuple_or_trace_id` | 该边所属的 pre-Cauchy actual source tuple 或 branch trace，不是推后 payment 原像。 |
| `signed_multiplier_formula` | 从 `a_p(prefix)` 到 `a_p(prefix*q)` 的 sign/local-factor/truncation 乘子。 |
| `first_edge_policy` | `prefix=1` 的第一边也必须由同表正向给出，不得读取 Phi 中被减掉的 prime row。 |
| `orientation_parity_increment` | 乘入 `q` 对 orientation parity 与 signed coefficient 符号的增量规则。 |
| `local_factor_nonzero_or_return` | local factor 非零、截断兼容；失败时进入命名回流。 |
| `alpha_delta_branch_exactuv_transition` | 同一边同步更新 alpha/delta side、branch key 和 exact `(u,v)` 输出。 |
| `path_product_identity_before_pushforward` | 沿 ordered edge 乘积在 Phi/payment 推前前等于该 support key 的 signed coefficient。 |
| `no_downstream_recovery` | 不得由 payment skeleton、零行覆盖、origin table 固定点或 terminal 反推恢复乘子。 |

## 3. 样本审计摘要

| N | support keys | edge steps | first edges | internal edges | distinct edges | max depth | distinct sign log10 | occurrence sign log10 | ok |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 30 | 19 | 30 | 19 | 11 | 19 | 3 | 5.71957 | 9.0309 | `true` |
| 100 | 74 | 140 | 74 | 66 | 74 | 5 | 22.27622 | 42.144199 | `true` |
| 997 | 828 | 1869 | 828 | 1041 | 828 | 8 | 249.252836 | 562.625062 | `true` |
| 5003 | 4332 | 10571 | 4332 | 6239 | 4332 | 11 | 1304.061941 | 3182.188084 | `true` |
| 10000 | 8770 | 21986 | 8770 | 13216 | 8770 | 12 | 2640.033062 | 6618.445485 | `true` |

## 4. 最新保留基

```text
(PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward OR PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward OR AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND ExplicitModelGapAndFiniteDPRCLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

下一直接主攻：

```text
PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward
```

条件生成器：

```text
ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn
ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn
PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward
```

并行直接入口：

```text
PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward
```

行/列命题仍未无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_step_local_factor_update_frontier_router.py` | `40a5f90ca0bbb4295f8e4ea96e767e8a047b4ec1cb332cd3b67d97f8e606c4ea` |
| `docs/monograph/prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json` | `f976e98574efb9522fb37341b9a8c62636a0903fd569f118e9059a361245acc4` |
| `docs/monograph/prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json` | `c78bc14420695f82fbb46cc5c3de28dbf38c85ba678d9aa4ffe0fb0f1c98d868` |
| `docs/monograph/prime-matrix-strict-orientation-law-branch-trace-router.json` | `bb8aed1a370f0de4ee4407787110b9cf3e379437e32f1a9d755997fca7acd7a5` |
| `docs/monograph/prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json` | `2f8b25613865c4e79e23a78ac7ed2b52e603ad3652c2a4865bc1b9ae50138bdb` |
| `docs/monograph/prime-matrix-strict-primitive-summand-signed-expression-router.json` | `b0b1264cf6f3fbad60724a440f0dc9872dbc577376ed466e5dcac0cf66caa5ff` |
| `docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json` | `657649a5067934b15c9a8847c27e297f01aac84bc9b1cef77ca2377c2a7ef8cf` |
