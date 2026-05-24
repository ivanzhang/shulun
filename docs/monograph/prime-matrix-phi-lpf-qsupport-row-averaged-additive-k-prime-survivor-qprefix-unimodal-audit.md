# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor q-prefix unimodal 审计

**状态：** `prime_survivor_floor_graph_refined_to_finite_qprefix_unimodal_cap_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
q_prefix_identity=for audited (P,m), Q_prime(P,m)={prime q: q0(P)<=q<=Q*(P,m)}
row_cap_shape=for audited rows, Q*(P,m) along prime m is unimodal
phase_packet=S_prime-survivor=sum_m sum_{q0(P)<=q<=Q*(P,m), q prime} e(hP floor(qm/P)/q)
meaning=the remaining graph is a prefix-cap graph rather than a generic sparse point cloud
remaining=prove or exploit this shape globally and embed it into trace/Type-II/convolution estimates
```

## 2. q-prefix / unimodal cap 有限审计

```text
max_prime=1009
prime_survivor_edge_count_total=355919
previous_prime_survivor_edge_count_total=355919
pm_bucket_count_total=16328
q_prefix_count_total=355919
lower_endpoint_not_row_first_total=0
q_prefix_missing_count_total=0
q_prefix_extra_count_total=0
bad_q_prefix_identity_count=0
max_q_prefix_phase_error=0.000e+00
active_P_count=155
previous_P_count=165
cap_unimodality_bad_row_count=0
cap_turn_count_total=154
total_bad_qprefix_unimodal_count=0
counts_match_previous_floor_span=true
q_prefix_identity_verified_on_finite_audit=true
row_cap_unimodality_verified_on_finite_audit=true
q_prefix_phase_packet_rewrite_verified_on_finite_audit=true
global_qprefix_theorem_proved=false
```

turn count distribution:

```text
{"0": 1, "1": 154}
```

peak plateau distribution:

```text
{"1": 42, "2": 36, "3": 37, "4": 17, "5": 12, "6": 6, "7": 3, "8": 1, "9": 1}
```

代表行：

| P | active_m_count | edge_count | first_m | last_m | max_cap_q | peak_m_min | peak_m_max | peak_plateau_prime_count | turn_count | bad_after_down_increase |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 20 | 96 | 79 | 181 | 83 | 97 | 113 | 5 | 1 | 0 |
| 257 | 61 | 591 | 137 | 491 | 241 | 251 | 251 | 1 | 1 | 0 |
| 971 | 198 | 6206 | 499 | 1913 | 953 | 967 | 983 | 3 | 1 | 0 |
| 1009 | 202 | 6414 | 521 | 1987 | 991 | 1013 | 1021 | 3 | 1 | 0 |

代表 prefix：

| P | m | q0 | cap | q_count | prefix_count | bad |
| --- | --- | --- | --- | --- | --- | --- |
| 43 | 53 | 23 | 23 | 1 | 1 | 0 |
| 43 | 59 | 23 | 23 | 1 | 1 | 0 |
| 43 | 61 | 23 | 23 | 1 | 1 | 0 |
| 43 | 67 | 23 | 23 | 1 | 1 | 0 |
| 43 | 71 | 23 | 23 | 1 | 1 | 0 |
| 43 | 73 | 23 | 23 | 1 | 1 | 0 |
| 53 | 59 | 29 | 31 | 2 | 2 | 0 |
| 53 | 61 | 29 | 31 | 2 | 2 | 0 |
| 53 | 67 | 29 | 31 | 2 | 2 | 0 |
| 53 | 71 | 29 | 31 | 2 | 2 | 0 |

cap path 样本：

```text
P=101: left 79->73, 83->73, 89->73, 97->83, 103->83, 107->83, 109->83, 113->83; right 149->61, 151->61, 157->61, 163->59, 167->59, 173->53, 179->53, 181->53
P=257: left 137->131, 139->131, 149->139, 151->139, 157->139, 163->157, 167->157, 173->167; right 449->139, 457->139, 461->139, 463->139, 467->139, 479->137, 487->131, 491->131
P=971: left 499->491, 503->491, 509->491, 521->509, 523->509, 541->523, 547->523, 557->547; right 1871->499, 1873->499, 1877->499, 1879->499, 1889->491, 1901->491, 1907->491, 1913->491
P=1009: left 521->509, 523->509, 541->523, 547->523, 557->547, 563->557, 569->557, 571->557; right 1913->523, 1931->523, 1933->523, 1949->509, 1951->509, 1973->509, 1979->509, 1987->509
```

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FiniteQPrefixNeighbourhoodAudit | true | true | For P<=1009, every fixed (P,m) q-neighbourhood is a prime-q prefix from q0(P). | global proof or direct analytic exploitation |
| FiniteUnimodalCapAudit | true | true | For P<=1009, the cap Q*(P,m) is unimodal in the ordered prime m-list of each active row. | global proof or Type-II split along the cap |
| PrefixCapPhasePacketRewrite | true | true | On the audited range, the phase packet equals the q-prefix cap packet exactly. | uniform analytic estimate for the rewritten packet |
| GlobalQPrefixUnimodalTheorem | false | false | Promote the finite prefix/unimodal audit to a global deterministic theorem. | not proved in this layer |
| PrefixCapTraceOrTypeIIEmbedding | false | false | Use the prefix-cap graph to obtain phase saving or a completed bilinear/trace family. | new embedding theorem still required |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | candidate after the q-prefix cap graph is promoted to a trace-function bilinear family |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | candidate after a completed Kloosterman variable is built from the prefix-cap graph |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | candidate if the prefix-cap graph is split into Type-II fibres with usable lengths |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | candidate for a future unbalanced convolution model of the prefix cap |
| Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman | https://arxiv.org/abs/2411.12113 | candidate parameter input after the arithmetic weights are fitted to their hypotheses |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | still above the theta=1/2 pointwise scale and not a direct closure for this graph |

```text
FKMS_trace_function_bilinear=the prefix cap is closer to a bilinear trace object but still lacks the completed trace family
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=the denominator q remains a moving prime prefix cap, not yet a completed Kloosterman variable
Pascadi_composite_Type_II=the prefix graph suggests a Type-II split, but usable long fibres are not yet constructed
Wright_unbalanced_convolution=the unimodal cap may fit a future unbalanced convolution model, not available here
Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman=requires additional smoothing/squarefree parameter matching beyond this finite cap shape
Li_short_interval_x_052=does not close the pointwise theta=1/2 requirement
```

结论：在有限审计范围内，prime survivor floor graph 从一般稀疏二部图压成 q-prefix cap graph，且每行 cap 是单峰帽函数。这缩小了需要嵌入外部 trace/Type-II 的对象，但尚未给出全局证明或相位节省。

## 5. 最新最窄口

```text
GlobalPrimeSurvivorQPrefixUnimodalCapProofOrReplacement
AND PrefixCapTraceOrTypeIIPhaseSaving
AND DiagonalPGhostSubtractionDiscipline
AND DenseRectangleCompletionOrBilinearTraceEmbeddingForPrimePrimeFloorGraph
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
finite_q_prefix_neighbourhood_audit_closed=true
finite_unimodal_cap_audit_closed=true
prefix_cap_phase_packet_rewrite_closed_on_audited_range=true
global_qprefix_unimodal_theorem_proved=false
prefix_cap_trace_or_typeii_embedding_closed=false
full_prime_prime_rectangle_completion_closed=false
prime_floor_span_trace_or_typeii_phase_saving_closed=false
small_lpf_blocker_packet_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
