# Prime Matrix exact-UV fiber 最新非循环同步路由证书

**状态：** `exactuv_fiber_branch_reduced_to_source_rank_atoms_open`

exact-UV fiber 首攻点被同步为 source-rank/no-collapse 原子包。确定性蕴含已经闭合：源域绝对熵、complete key 分区与固定 key 局部 O(1) 重数合取即可推出 fiber 非集中。真正未证的是 pre-Cauchy signed row 系数律、actual emitter 源表/complete key 预算、固定 key 局部重数；继续沿 strict 链下钻会回到逐 primitive kernel 表和 new-joint/terminal 前沿。

```text
preterminal_fiber_atomization_imported=true
deterministic_source_atom_implication_closed=true
source_entropy_reduced_to_signed_rows=true
complete_key_reduced_to_actual_source_table=true
fixed_pair_fiber_formal_inequality_closed=true
map_rank_equivalent_to_bounded_incidence=true
nonterminal_exactuv_fiber_aperiodicity_proved=false
row_column_unconditional_closed=false
```

## 1. 同步结论

`NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource` 不是 CRT 位置刚性问题。
它是同一 actual formal unit 内 pre-Cauchy source 的源域熵与 exact `(u,v)` 映射无坍缩问题。
当前已闭合的是形式蕴含：

```text
source entropy + complete key partition + fixed-key O(1) multiplicity
=> exact-UV fiber aperiodicity / no-collapse.
```

未闭合的是这三个 actual 源侧输入本身。

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ExactUVTargetImportedFromQ1Q2 | `true` | `false` | Q1/Q2 同步后，纯 CRT 位置刚性剩余被压到 actual pre-Cauchy source 的 exact-UV fiber 非集中。 | NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource |
| PreterminalFiberAtomizationImported | `true` | `false` | preterminal exact-UV fiber 分散已被原子化为源域 rank/no-collapse 包。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| DeterministicSourceAtomImplicationClosed | `true` | `true` | 源域绝对熵、complete key 多对数分区、固定 key 局部 O(1) 重数三者合取即可推出 exact-UV fiber 非集中。 | ActualPreCauchySourceDomainAbsoluteEntropyLedger AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| SourceEntropyReducedToSignedRows | `true` | `false` | 源域绝对熵不是 CRT 计数；它需要 pre-Cauchy signed primitive rows、行质量无重原子和支撑下界。 | AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger |
| CompleteKeyReducedToActualSourceTable | `true` | `false` | complete key 不能后验补标签；必须来自 actual noncanonical primitive emitter 源表及预算/refinement/return 纪律。 | ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND CompleteEmitterTraceKeyBudgetLedger AND SignLocalFactorRefinementNoCancellationLedger AND OverBudgetOrUnregisteredReturnLedger |
| FixedPairFiberFormalInequalityClosed | `true` | `true` | 若 complete key 数为 log^O(1)，且固定 key 与固定 exact (u,v) 只有 O(1) 原像，则 fixed-pair fiber 上界形式推出。 | RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger |
| MapRankEquivalentToBoundedIncidence | `true` | `false` | exact-UV map rank/no-collapse 的正面内容是 actual emitter 到 exact (u,v) 的有界重数 incidence；朴素因子-余数 incidence 已被内部 fiber 阻断。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| FalseExactUVSourcesRejected | `true` | `true` | CRT 位置、payment skeleton、DLS 可逆变量、signed-only 相消和 canonical cross-import 都不能生成 exact-UV fiber 非集中。 | ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger |
| SourceRankConvergesToPointwiseKernel | `true` | `false` | post-antisplit 同步显示 source-rank/no-collapse、new primitive 与 terminal descent 均汇到同 formal-unit 逐 primitive alpha/delta 核表。 | PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate |
| StrictDownstreamStillOpen | `true` | `false` | 继续下钻 pointwise kernel 会回到 alpha/signed-source/terminal 叶子或新 joint 公式；当前没有独立闭合。 | NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact |
| RowColumnUnconditionalClosureReached | `false` | `false` | 本步关闭 exact-UV 作为纯 CRT/位置问题的误出口；未证明 signed row、source table、fixed-key multiplicity、new joint、模型、Rate 或 DStructure。 | ((AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger) AND (ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND CompleteEmitterTraceKeyBudgetLedger AND SignLocalFactorRefinementNoCancellationLedger AND OverBudgetOrUnregisteredReturnLedger) AND FixedKeyExactUVLocalMultiplicityO1Ledger) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 源域原子基

```text
(ActualPreCauchySourceDomainAbsoluteEntropyLedger AND RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全原子化后内部基为：

```text
((AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward AND SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger) AND (ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND CompleteEmitterTraceKeyBudgetLedger AND SignLocalFactorRefinementNoCancellationLedger AND OverBudgetOrUnregisteredReturnLedger) AND FixedKeyExactUVLocalMultiplicityO1Ledger) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

若导入既有 strict 下游同步，内部剩余进一步压到：

```text
NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

条件外部保留线：

```text
(ExternalDIBFIKuznetsovDispersionTheoremMatch OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND HighSegmentModelGapAlpha043C3AnalyticLedger AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 4. 下一直接主攻

```text
AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward
```

并行保留：

```text
ActualNoncanonicalPrimitiveEmitterSourceTableLedger OR FixedKeyExactUVLocalMultiplicityO1Ledger OR NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR ExternalDIBFIKuznetsovDispersionTheoremMatch
```

## 5. 诚实边界

- 本证书不证明 exact-UV fiber 非集中。
- 本证书只把 exact-UV 首攻点压成 actual 源域三原子，并排除 CRT/payment/DLS 位置刚性替代证明。
- 行/列命题仍未全局无条件闭合。

## 6. 上游状态

| file | status |
| --- | --- |
| `prime-matrix-q1q2-transport-latest-noncycle-sync-router.json` | `q1q2_transport_branch_synced_to_q2_ladder_and_source_frontier_open` |
| `prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json` | `strict_preterminal_fiber_dispersion_reduced_to_source_rank_atom_package_open` |
| `prime-matrix-strict-actual-source-domain-entropy-atom-router.json` | `strict_actual_source_domain_entropy_reduced_to_signed_row_mass_entropy_open` |
| `prime-matrix-strict-complete-emitter-key-partition-router.json` | `strict_complete_emitter_key_partition_reduced_to_actual_source_table_budget_refinement_return_open` |
| `prime-matrix-strict-fixed-pair-fiber-bound-router.json` | `strict_fixed_pair_fiber_bound_reduced_to_complete_key_partition_and_fixed_key_multiplicity_open` |
| `prime-matrix-strict-exact-uv-map-rank-incidence-router.json` | `strict_exact_uv_map_rank_reduced_to_actual_emitter_bounded_multiplicity_incidence_open` |
| `prime-matrix-strict-post-antisplit-source-rank-convergence-router.json` | `post_antisplit_source_rank_paths_converge_to_pointwise_kernel_open` |
| `prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json` | `post_antisplit_alpha_frontier_synced_to_terminal_leaf_open` |
| `prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json` | `seed_cycle_cut_branch_saturated_to_pdec_scope_or_new_joint_formula_open` |
| `prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json` | `pdec_scope_branch_saturated_internal_noncycle_exit_reduced_to_new_joint_formula_open` |

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_exactuv_fiber_latest_noncycle_sync_router.py` | `063f3c71160970d7f61d3a0a9923ad8fa7ff67704c22c84413eb6206b3dd7005` |
| `docs/monograph/prime-matrix-q1q2-transport-latest-noncycle-sync-router.json` | `ef287465a10d1e06753941f289d68b9411396c40b774d574345e9ecb5edea781` |
| `docs/monograph/prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json` | `62c6b5b1712c00216487e7c68b72d8cb97a61e58ba78f08538f697c49232142a` |
| `docs/monograph/prime-matrix-strict-actual-source-domain-entropy-atom-router.json` | `0eaacb65ce36ad81475e8fb8806bdd90570f24939b224d6f59c38262cf2374a9` |
| `docs/monograph/prime-matrix-strict-complete-emitter-key-partition-router.json` | `8eb78dba1a3383b509b4b968fc51daaadbb683830ea480eb1cc418ca92e426c8` |
| `docs/monograph/prime-matrix-strict-fixed-pair-fiber-bound-router.json` | `ca413ebdcac1df1baf57319fbfe828d92bc272ef1b326215de5cd514316d49bd` |
| `docs/monograph/prime-matrix-strict-exact-uv-map-rank-incidence-router.json` | `101917e6a573efb2d6c921b2056ac92120e41f1b10ae2549f394ac0fa3d1b54c` |
| `docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.json` | `3359bdbe51404005aec41ec0378840a4d114c235f20354ef488e2592e3f692c7` |
| `docs/monograph/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json` | `ddc914dc34fbb242fd18ca888633de65b0a5aaa08ebea2086a9352ce65f2c3d9` |
| `docs/monograph/prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json` | `d374690b63ed1b8b60b5261607a84a9c83d7dfa19fb0d3803904f5f011d80c56` |
| `docs/monograph/prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json` | `3c7602bf11d29d837d1a05964368f085de2c10dc5e786bd518b55a85b4ce3cbf` |
