# Prime Matrix strict source declaration / payload / ExactUV 合流路由器

**状态：** `strict_payload_and_exactuv_reduced_to_common_precauchy_source_declaration_packet_open`

本步把 signed payload 线与 ActualEmitterExactUV 线合流到同一个 `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket`。payload 需要它给出非循环 basis word/signed coefficient 来源恒等式；ExactUV 需要它给出 source-domain entropy 与 fixed exact (u,v) fiber bound。当前语料没有该 packet，所以这只是最新硬点压缩，不是行/列命题无条件闭合。

```text
common_packet=PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket
common_packet_proved=false
atomic_signed_payload_constructor_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
row_column_unconditional_closed=false
```

## 1. 共同 packet 字段

| field | feeds | requirement |
| --- | --- | --- |
| `declaration_line` | payload + ExactUV | 在 Cauchy/Phi/payment 前声明 actual noncanonical pre-Cauchy emitter，而不是从零行或 payment 反推。 |
| `source_tuple_domain_entropy` | ExactUV | 给出 primitive source tuple 支撑下界，足以支持 actual emitter source-domain entropy。 |
| `primitive_summand_rows` | payload + ExactUV | 逐行列出 branch key、basis word、sign、local factor、exact (u,v) 与 return tag。 |
| `basis_word_signed_coefficient_identity` | payload | 证明 basis word 到 signed coefficient 的来源恒等式先于推前，且不调用 row-level 表。 |
| `alpha_delta_prepushforward_identity` | payload + final source lane | 证明这些 primitive rows 在推前前求和等于 actual alpha/delta 贡献。 |
| `fixed_exact_uv_fiber_bound` | ExactUV | 在固定 exact (u,v) 与 branch/sign/local-factor refinement 后，证明 primitive 原像数为 polylog 级。 |
| `no_downstream_recovery` | acyclicity | 显式排除从 payment、零行覆盖、Gamma 图、Cauchy 后表达式或 canonical 表倒推出 source row。 |
| `named_return_partition` | failure ledger | 缺声明、缺 row、符号冲突、local factor 为零、fiber collapse、entropy deficit、超预算、canonical 泄漏均命名回流。 |

## 2. 证据同步表

| id | role | status | next/after |
| --- | --- | --- | --- |
| `atomic_payload_origin` | signed payload 被压到非循环 basis-word/signed-coefficient 来源恒等式 | atomic_signed_payload_reduced_to_noncircular_origin_identity_open | NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `atomic_branch_trace_payload` | atomic branch trace 的可见坐标与 signed payload 分裂 | exact_atomic_branch_trace_reduced_to_signed_payload_constructor_open | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |
| `branch_trace_cycle` | branch trace signed payload 回到 row-level origin table | branch_trace_formula_split_visible_coordinate_closed_signed_payload_loops_open |  |
| `exact_uv_rank` | ExactUV map rank 被压到 actual emitter bounded incidence | strict_exact_uv_map_rank_reduced_to_actual_emitter_bounded_multiplicity_incidence_open | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `actual_emitter_entropy` | bounded incidence 被拆成 source entropy 与 fixed-pair fiber bound | strict_actual_emitter_bounded_incidence_reduced_to_source_entropy_and_fixed_pair_fiber_bound_open | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `actual_emitter_source_table` | actual emitter 源表被拆成 declaration/rows/identity/return | strict_actual_emitter_source_table_reduced_to_precauchy_declaration_rows_identity_return_open | PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter |
| `final_open_input` | 最终开放输入把 source lane 压到 ExactUV 支撑或外部 FullS | final_open_input_reduced_to_exact_uv_or_external_fulls_plus_dstructure_open |  |
| `global_crt_signed_payload` | global CRT 可见骨架不能生成 signed payload | global_crt_internal_route_reduced_to_signed_payload_with_external_pdec_retained | AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `AtomicPayloadReducedToNoncircularOriginIdentity` | true | false | signed payload 的第一生产字段已压到 atomic basis word/signed coefficient 来源恒等式。 | NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward |
| `ExactUVIncidenceReducedToEntropyAndFiber` | true | false | ActualEmitterExactUV 有界重数已拆成 source-domain entropy 与 fixed-pair fiber bound。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `SourceTableFirstLinePinned` | true | false | actual emitter 源表的第一合法字段是 pre-Cauchy declaration line。 | PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter AND PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND AlphaDeltaCoefficientIdentityBeforePushforwardLedger AND SourceTableNoDownstreamRecoveryAndNamedReturnLedger |
| `VisibleCRTTraceCannotEmitSignedRows` | true | true | CRT/trace 可给可见坐标，但不能给 orientation、local factor、signed coefficient 与 source row。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| `PayloadNeedsCommonDeclarationPacket` | true | false | 非循环 signed coefficient 来源恒等式必须由同一 pre-Cauchy actual source row 正向给出。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| `ExactUVNeedsCommonDeclarationPacket` | true | false | 没有 source rows，就无法同时证明 source entropy 与 fixed exact (u,v) polylog fiber。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| `CommonPacketWouldCloseInternalSourceLaneConditionally` | true | true | 若共同 packet 的字段全部给出，则 signed payload 与 ActualEmitterExactUV 两条内部 source lane 同时获得所需输入。 | prove PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| `CurrentCorpusCommonPacketProved` | false | false | 当前仓库没有提交该 pre-Cauchy actual source declaration packet。 | PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |
| `RowColumnUnconditionalClosureReached` | false | false | 本步只合流两个硬点，不关闭 AP 零点包、same-set PDEC、模型余量、RatePreservation 与 DStructure/Rankin 门。 | PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget OR AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `payload_exactuv_common_source_root` | `closed_routing` | Atomic signed payload and ActualEmitterExactUV incidence both require a pre-Cauchy actual noncanonical source declaration packet when the proof is kept self-contained. |
| `common_packet_conditional_sufficiency` | `conditional` | A packet containing declaration rows, signed coefficient identities, prepushforward equality, source entropy, fixed-pair fiber bounds, and named returns would close the internal source lane. |
| `row_column_unconditional_closure` | `open` | The packet is not present in the current corpus, and AP zero-packet, same-set PDEC, rate/model, and D-structure inputs remain outside this routing step. |

## 5. 结论边界

- 本步只合流 strict 内部 source lane 的两个活动硬点。
- `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` 是下一直接主攻对象。
- AP 零点包、same-set PDEC、模型余量、RatePreservation 与 DStructure/Rankin 验收门仍独立开放。
- 不能把该合流路由解读为行/列命题无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_strict_source_declaration_payload_exactuv_unification_router.py` | `339df50dc152ea40dfad54526fc7acb23f86d153dab35bddca2f5f3d2a5e49cc` |
| `docs/monograph/prime-matrix-strict-atomic-payload-origin-identity-router.json` | `b5e6909a3aab66eef258b360a1dc599dc6bdd28cf415f6c21f630abe989ce65a` |
| `docs/monograph/prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json` | `fe1d86442d7936662a55cd5b8279e339f5bfd21142bd079ec80280c06423df92` |
| `docs/monograph/prime-matrix-strict-branch-trace-signed-payload-cycle-router.json` | `67da3805e5bdb503d768a79b95a3408bbdfede3254557e2e89080e2229d0e3b0` |
| `docs/monograph/prime-matrix-strict-exact-uv-map-rank-incidence-router.json` | `101917e6a573efb2d6c921b2056ac92120e41f1b10ae2549f394ac0fa3d1b54c` |
| `docs/monograph/prime-matrix-strict-actual-emitter-incidence-entropy-router.json` | `36b03764e66ea8e57d010d38829004c62a1ab72c363f1e73a9cce92126f6ab7d` |
| `docs/monograph/prime-matrix-strict-actual-emitter-source-table-router.json` | `e327b1a80aef83a36279378e5892334fa305d92d5ac1bcbb8601eaab2f18ab3e` |
| `docs/monograph/prime-matrix-final-open-input-direct-attack-router.json` | `5e240384ea00a833f0569af8999466ebf02d357c58cfd5e11ef31241bf7bd8c9` |
| `docs/monograph/prime-matrix-global-crt-signed-payload-sync-router.json` | `969459391db184ef4250b42c88f9947e1884ac92523320b47f887f729e8c6c56` |
| `data/prime-matrix-strict-source-declaration-payload-exactuv-unification-ledger.json` | `c0385095667b1cc83bd3e56487422892ee7a544fb55712fce6ecc68a00c48cca` |
