# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor floor-span completion 审计

**状态：** `prime_survivor_singleton_layer_rewritten_as_floor_prime_span_with_diagonal_P_ghost_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
floor_span_identity=for each active (P,q), M_prime(P,q)={prime m in [L_{P,q},U_{P,q}]}\{P}
phase_packet=S_prime-survivor=sum_q sum_{m prime in [L_q,U_q],m!=P} e(hP floor(qm/P)/q)
diagonal_ghost=m=P gives k=q and D=0, so it is a completion ghost, not a blocker
rectangle_obstruction=the union of span intervals is not the full prime-prime rectangle in (q,m)
remaining=phase saving or trace/Type-II/convolution embedding for the prime-prime floor graph
```

## 2. floor-span completion 有限审计

```text
max_prime=1009
P_count=165
prime_survivor_edge_count_total=355919
previous_prime_singleton_terms_total=355919
previous_prime_blocker_count_total=355919
q_bucket_count_total=5848
span_prime_count_total=361626
raw_missing_count_total=5707
raw_extra_count_total=0
diagonal_ghost_count_total=5707
bucket_with_only_diagonal_ghost_count=5707
bucket_with_no_raw_missing_count=141
expected_missing_after_diagonal_subtraction_total=0
expected_extra_after_diagonal_subtraction_total=0
bad_span_identity_bucket_count=0
max_span_completion_phase_error=1.421e-14
total_bad_prime_survivor_floor_span_count=0
counts_match_previous_mobius_singleton_layer=true
prime_survivor_floor_span_identity_verified=true
raw_completion_tax_is_only_diagonal_P=true
diagonal_subtracted_span_equals_survivor_edges=true
q_eligible_prime_count_total=6115
m_eligible_prime_count_total=17464
m_eligible_prime_count_without_diagonal_total=17299
full_prime_prime_rectangle_edge_count_including_diagonal_total=855449
full_prime_prime_rectangle_edge_count_without_diagonal_total=849334
prime_survivor_to_full_rectangle_including_diagonal_density=0.41606104
prime_survivor_to_full_rectangle_without_diagonal_density=0.41905658
dense_rectangle_completion_missing_edge_count_including_diagonal=499530
dense_rectangle_completion_missing_edge_count_without_diagonal=493415
full_prime_prime_rectangle_completion_available_directly=false
```

代表 P：

| P | edges | q_buckets | distinct_m | eligible_q_primes | eligible_m_primes | eligible_m_primes_without_diagonal | full_rectangle | full_rectangle_without_diagonal | density | density_without_diagonal | max_q_to_m | max_m_to_q | max_k_to_q | diagonal_ghosts | bad_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 96 | 8 | 20 | 10 | 31 | 30 | 310 | 300 | 0.3097 | 0.3200 | 20 | 8 | 4 | 8 | 0 |
| 257 | 591 | 22 | 61 | 23 | 66 | 65 | 1518 | 1495 | 0.3893 | 0.3953 | 61 | 22 | 9 | 19 | 0 |
| 971 | 6206 | 70 | 198 | 71 | 203 | 202 | 14413 | 14342 | 0.4306 | 0.4327 | 198 | 70 | 21 | 70 | 0 |
| 1009 | 6414 | 71 | 202 | 72 | 210 | 209 | 15120 | 15048 | 0.4242 | 0.4262 | 202 | 71 | 19 | 70 | 0 |

代表 q-bucket：

| P | q | L | U | edges | span_primes | raw_missing_count | diagonal_ghost | phase_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | 23 | 53 | 73 | 6 | 6 | 0 | none | 0.000e+00 |
| 53 | 29 | 59 | 89 | 8 | 8 | 0 | none | 0.000e+00 |
| 53 | 31 | 59 | 73 | 5 | 5 | 0 | none | 0.000e+00 |
| 59 | 31 | 53 | 89 | 8 | 9 | 1 | 59 | 2.220e-16 |
| 59 | 37 | 53 | 89 | 8 | 9 | 1 | 59 | 2.220e-16 |
| 59 | 41 | 53 | 73 | 5 | 6 | 1 | 59 | 1.110e-16 |
| 59 | 43 | 53 | 73 | 5 | 6 | 1 | 59 | 2.220e-16 |
| 61 | 31 | 53 | 113 | 14 | 15 | 1 | 61 | 0.000e+00 |

diagonal ghost 样本：

```text
P=59,q=31,m-span=[53,89],edges=8,span_primes=9,ghost=59
P=59,q=37,m-span=[53,89],edges=8,span_primes=9,ghost=59
P=59,q=41,m-span=[53,73],edges=5,span_primes=6,ghost=59
P=59,q=43,m-span=[53,73],edges=5,span_primes=6,ghost=59
P=61,q=31,m-span=[53,113],edges=14,span_primes=15,ghost=61
P=61,q=37,m-span=[53,89],edges=8,span_primes=9,ghost=61
```

无 diagonal ghost 样本：

```text
P=43,q=23,m-span=[53,73],edges=6,span_primes=6,ghost=none
P=53,q=29,m-span=[59,89],edges=8,span_primes=8,ghost=none
P=53,q=31,m-span=[59,73],edges=5,span_primes=5,ghost=none
P=71,q=53,m-span=[79,89],edges=3,span_primes=3,ghost=none
P=73,q=53,m-span=[79,89],edges=3,span_primes=3,ghost=none
P=79,q=53,m-span=[83,89],edges=2,span_primes=2,ghost=none
```

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PrimeSurvivorFloorSpanIdentity | true | true | In each active q-bucket, prime survivors fill the prime m-span after subtracting the diagonal m=P ghost. | none |
| DiagonalPGhostCompletionTax | true | true | The only raw span-completion missing prime is m=P, where D=0 and no blocker exists. | none |
| PrimeSurvivorPhasePacketSpanRewrite | true | true | The additive packet equals the prime interval span packet minus the diagonal ghost bucket by bucket. | none |
| FullPrimePrimeRectangleCompletion | false | false | Upgrade the span graph to a dense prime-prime rectangle suitable for standard bilinear estimates. | not available; many prime-prime rectangle edges are absent |
| PrimeFloorSpanTraceOrTypeIIPhaseSaving | false | false | Obtain nontrivial cancellation for the prime-prime floor-span graph. | requires new trace/Type-II/convolution embedding or new phase theorem |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | candidate trace bilinear input only after the floor-span survivor graph is embedded into a trace family |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | candidate arbitrary-modulus Kloosterman input after a completed inverse-variable model exists |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | candidate composite Type-II input after dense enough bilinear fibres are constructed |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | candidate unbalanced convolution input after the prime-prime floor graph is converted to a convolution packet |
| Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman | https://arxiv.org/abs/2411.12113 | candidate smooth/squarefree parameter input, not a direct prime interval floor-span estimate |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | theta=0.52 short-interval prime input remains above the pointwise half-scale required for direct closure |

```text
FKMS_trace_function_bilinear=promising only after the prime floor-span packet is converted into an actual trace-function bilinear family
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=requires a completed Kloosterman variable; the present graph has floor denominator q and sparse span support
Pascadi_composite_Type_II=requires a genuine Type-II factorisation; the audited graph is not a full dense rectangle
Wright_unbalanced_convolution=requires a convolution/Kloosterman-fraction model for the floor-span graph
Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman=does not directly estimate this prime interval floor-span selector
Li_short_interval_x_052=does not lower to the required pointwise theta=1/2 window for this packet
```

结论：prime survivor singleton layer 已被写成 prime interval floor-span packet，原始 span completion 唯一缺口是对角 `m=P` ghost。它仍不是完整 prime-prime rectangle，也未给出相位节省；真正剩余是该 floor graph 的 trace/Type-II/convolution 嵌入或新的直接相消。

## 5. 最新最窄口

```text
PrimeSurvivorPrimeIntervalFloorSpanPhaseSavingOrTraceEmbedding
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
prime_survivor_floor_span_identity_closed=true
diagonal_P_ghost_completion_tax_closed=true
prime_survivor_phase_packet_span_rewrite_closed=true
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
