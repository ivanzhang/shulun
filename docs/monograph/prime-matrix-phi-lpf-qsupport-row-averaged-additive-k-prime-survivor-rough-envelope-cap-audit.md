# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor rough-envelope cap 审计

**状态：** `qprefix_unimodal_cap_explained_by_nested_residual_rough_envelope_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
selected_residual_formula=m in R_P and q<=m and q*m<P^2
envelope=R_{P,q}=R_P cap [q,P^2/q), A_q=min R_{P,q}, B_q=max R_{P,q}
prime_survivor_identity=M_prime(P,q)={prime m in [A_q,B_q]}\{P}
cap_formula=Q*(P,m)=min(max{q:A_q<m}, max{q:B_q>m})
remaining=exploit the nested envelope cap analytically through trace/Type-II/convolution phase saving
```

## 2. rough-envelope cap 有限审计

```text
max_prime=1009
q_checked_count=6115
nonempty_envelope_q_count=6020
selected_formula_m_count_total=299977
selected_existing_m_count_total=299977
selected_envelope_formula_mismatch_count=0
actual_prime_edge_count_total=355919
previous_prime_survivor_edge_count_total=355919
predicted_prime_edge_count_total=355919
prime_envelope_missing_count=0
prime_envelope_extra_count=0
prime_envelope_bad_q_count=0
A_monotonicity_bad_step_count=0
B_monotonicity_bad_step_count=0
pm_bucket_count=16328
previous_pm_bucket_count_total=16328
cap_threshold_empty_side_count=0
cap_min_threshold_mismatch_count=0
predicted_qprefix_mismatch_count=0
active_P_count=155
previous_active_P_count=155
cap_unimodality_bad_row_count=0
cap_turn_count_total=154
total_bad_rough_envelope_cap_count=0
selected_residual_envelope_formula_verified=true
prime_survivor_rough_envelope_identity_verified=true
rough_envelope_endpoint_monotonicity_verified=true
cap_min_threshold_identity_verified=true
global_qprefix_unimodal_structure_explained=true
prefix_cap_trace_or_typeii_embedding_closed=false
```

代表 envelope：

| P | q | A | B | residual_count | prime_edges | bad_formula | bad_prime_envelope |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 29 | 17 | 49 | 49 | 1 | 0 | 0 | 0 |
| 31 | 17 | 49 | 49 | 1 | 0 | 0 | 0 |
| 31 | 19 | 49 | 49 | 1 | 0 | 0 | 0 |
| 37 | 19 | 49 | 49 | 1 | 0 | 0 | 0 |
| 37 | 23 | 49 | 49 | 1 | 0 | 0 | 0 |
| 41 | 23 | 49 | 49 | 1 | 0 | 0 | 0 |
| 41 | 29 | 49 | 49 | 1 | 0 | 0 | 0 |
| 41 | 31 | 49 | 49 | 1 | 0 | 0 | 0 |
| 43 | 23 | 49 | 77 | 2 | 6 | 0 | 0 |
| 43 | 29 | 49 | 49 | 1 | 0 | 0 | 0 |

代表行：

| P | pm_buckets | edge_count | A_bad_steps | B_bad_steps | turn_count | bad_after_down_increase | max_cap_q | peak_m_min | peak_m_max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 20 | 96 | 0 | 0 | 1 | 0 | 83 | 97 | 113 |
| 257 | 61 | 591 | 0 | 0 | 1 | 0 | 241 | 251 | 251 |
| 971 | 198 | 6206 | 0 | 0 | 1 | 0 | 953 | 967 | 983 |
| 1009 | 202 | 6414 | 0 | 0 | 1 | 0 | 991 | 1013 | 1021 |

cap threshold 样本：

```text
P=101: left 79->min(73,89)=73, 83->min(73,89)=73, 89->min(73,89)=73, 97->min(89,83)=83, 103->min(89,83)=83, 107->min(89,83)=83; right 157->min(89,61)=61, 163->min(89,59)=59, 167->min(89,59)=59, 173->min(89,53)=53, 179->min(89,53)=53, 181->min(89,53)=53
P=257: left 137->min(131,251)=131, 139->min(131,251)=131, 149->min(139,251)=139, 151->min(139,251)=139, 157->min(139,251)=139, 163->min(157,251)=157; right 461->min(251,139)=139, 463->min(251,139)=139, 467->min(251,139)=139, 479->min(251,137)=137, 487->min(251,131)=131, 491->min(251,131)=131
P=971: left 499->min(491,967)=491, 503->min(491,967)=491, 509->min(491,967)=491, 521->min(509,967)=509, 523->min(509,967)=509, 541->min(523,967)=523; right 1877->min(967,499)=499, 1879->min(967,499)=499, 1889->min(967,491)=491, 1901->min(967,491)=491, 1907->min(967,491)=491, 1913->min(967,491)=491
P=1009: left 521->min(509,997)=509, 523->min(509,997)=509, 541->min(523,997)=523, 547->min(523,997)=523, 557->min(547,997)=547, 563->min(557,997)=557; right 1933->min(997,523)=523, 1949->min(997,509)=509, 1951->min(997,509)=509, 1973->min(997,509)=509, 1979->min(997,509)=509, 1987->min(997,509)=509
```

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SelectedResidualRoughEnvelopeFormula | true | true | The selected residual support is exactly R_P intersected with q<=m and q*m<P^2. | none for the structural identity |
| PrimeSurvivorRoughEnvelopeIdentity | true | true | Prime survivors are precisely primes inside [A_q,B_q] after removing the diagonal m=P. | none for the structural identity |
| NestedEnvelopeEndpointMonotonicity | true | true | A_q is nondecreasing and B_q is nonincreasing because R_{P,q} is nested as q increases. | none for the structural identity |
| QPrefixUnimodalCapStructureExplained | true | true | The q-prefix and unimodal cap follow from the two monotone endpoint thresholds. | none for the support-shape reduction |
| PrefixCapTraceOrTypeIIPhaseSaving | false | false | Use the nested rough-envelope cap to obtain cancellation or a completed bilinear/trace family. | new analytic embedding still required |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | candidate only after the rough-envelope cap is converted into a trace bilinear family |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | candidate after completed Kloosterman variables replace the moving floor denominator |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | candidate after splitting the rough-envelope cap into genuine Type-II fibres |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | candidate if the cap can be reorganised as an unbalanced convolution |
| Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman | https://arxiv.org/abs/2411.12113 | candidate after matching smooth/squarefree parameters; not direct here |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | still does not provide the pointwise theta=1/2 closure needed here |

```text
FKMS_trace_function_bilinear=the support shape is now nested, but no trace-family sheaf or completed sum has been produced
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=the moving denominator q is not yet transformed into a completed Kloosterman variable
Pascadi_composite_Type_II=nested support may help split fibres, but Type-II lengths and weights remain unproved
Wright_unbalanced_convolution=the cap is compatible with an unbalanced viewpoint, but no convolution identity is closed
Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman=additional smooth/squarefree parameter matching remains absent
Li_short_interval_x_052=short-interval theta=0.52 remains above the required pointwise half-scale
```

结论：q-prefix 与单峰 cap 的来源已压到 nested residual rough envelope：`R_{P,q}=R_P cap [q,P^2/q)`。这关闭了支撑形状来源，但没有产生相位节省；剩余是把该 nested cap 转成 completed trace/Kloosterman/Type-II 输入。

## 5. 最新最窄口

```text
PrefixCapTraceOrTypeIIPhaseSavingFromNestedRoughEnvelope
AND CompletedTraceOrKloostermanVariableForMovingPrimeDenominator
AND DiagonalPGhostSubtractionDiscipline
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
selected_residual_rough_envelope_formula_closed=true
prime_survivor_rough_envelope_identity_closed=true
nested_envelope_endpoint_monotonicity_closed=true
global_qprefix_unimodal_structure_explained=true
prefix_cap_trace_or_typeii_embedding_closed=false
completed_trace_or_kloosterman_variable_closed=false
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
