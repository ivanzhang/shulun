# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor boundary strip decomposition 审计

**状态：** `bulk_boundary_decomposed_into_three_monotone_strips_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
bulk=largest complete prime q x prime m rectangle inside each fixed-P survivor row
boundary_decomposition=boundary=lower_wing disjoint union upper_wing disjoint union right_tail; left_tail vanishes
strip_shape=each active strip is a contiguous q-block of complete prime intervals with nonincreasing fibre lengths
remaining=phase saving or completion for the three monotone strip packets without losing a boundary-sized main term
```

## 2. boundary strip 有限审计

```text
max_prime=1009
active_P_count=155
bulk_edge_count_total=178404
previous_bulk_edge_count_total=178404
boundary_edge_count_total=177515
previous_boundary_edge_count_total=177515
strip_boundary_count_total=177515
left_tail_count_total=0
lower_wing_count_total=29144
upper_wing_count_total=61620
right_tail_count_total=86751
lower_wing_fraction_of_boundary=0.164177675126
upper_wing_fraction_of_boundary=0.347125595020
right_tail_fraction_of_boundary=0.488696729854
q_start_not_row_first_count=0
q_end_not_row_last_count=150
left_tail_active_row_count=0
lower_wing_active_row_count=136
upper_wing_active_row_count=153
right_tail_active_row_count=150
strip_prime_interval_mismatch_count_total=0
noncontiguous_strip_count_total=0
strip_length_monotonicity_bad_steps_total=0
bad_strip_decomposition_row_count=0
total_bad_boundary_strip_decomposition_count=0
bulk_prefix_start_verified=true
left_tail_vanishes_verified=true
boundary_three_strip_identity_verified=true
boundary_strips_are_monotone_prime_interval_packets=true
boundary_phase_saving_closed=false
```

代表行：

| P | q_start | q_end | m_start | m_end | boundary_edge_count | left_tail_count | lower_wing_count | upper_wing_count | right_tail_count | strip_prime_interval_mismatch_count | strip_length_monotonicity_bad_steps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 43 | 23 | 23 | 53 | 73 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 53 | 29 | 31 | 59 | 73 | 3 | 0 | 0 | 3 | 0 | 0 | 0 |
| 59 | 31 | 43 | 53 | 73 | 6 | 0 | 0 | 6 | 0 | 0 | 0 |
| 61 | 31 | 47 | 53 | 73 | 12 | 0 | 0 | 12 | 0 | 0 | 0 |
| 67 | 37 | 47 | 53 | 89 | 6 | 0 | 0 | 6 | 0 | 0 | 0 |
| 71 | 37 | 47 | 53 | 89 | 17 | 0 | 0 | 14 | 3 | 0 | 0 |
| 73 | 37 | 43 | 53 | 113 | 15 | 0 | 0 | 4 | 11 | 0 | 0 |
| 79 | 41 | 47 | 53 | 113 | 16 | 0 | 0 | 8 | 8 | 0 | 0 |
| 101 | 53 | 71 | 79 | 139 | 36 | 0 | 0 | 16 | 20 | 0 | 0 |
| 257 | 131 | 181 | 191 | 359 | 272 | 0 | 47 | 107 | 118 | 0 | 0 |
| 971 | 487 | 701 | 709 | 1327 | 3146 | 0 | 533 | 1119 | 1494 | 0 | 0 |
| 1009 | 509 | 761 | 769 | 1327 | 3255 | 0 | 713 | 1349 | 1193 | 0 | 0 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BulkPrefixStart | True | True | The maximal bulk rectangle starts at the first eligible q in every audited row. | none for the audited rows; follows from nested interval monotonicity as a structural guide |
| BoundaryThreeStripIdentity | True | True | The boundary is exactly lower_wing plus upper_wing plus right_tail; left_tail is zero. | none for the strip identity |
| BoundaryStripPrimeIntervalCompleteness | True | True | Each strip fibre is a complete prime interval segment, not a sparse arbitrary set. | none for the support identity |
| BoundaryStripLengthMonotonicity | True | True | The strip fibre lengths are nonincreasing along q. | none for the monotone support ledger |
| BoundaryStripPhaseSaving | False | False | Obtain cancellation or a completed trace family for the three monotone strip packets. | new analytic estimate still required |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | monotone strips are closer to summation by parts around bilinear trace estimates, but no boundary estimate is supplied |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | strip endpoints still need a completed Kloosterman variable or endpoint cancellation |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | a strip-by-strip Type-II packet remains conditional on boundary completion |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | the monotone right tail is an unbalanced candidate only after endpoint weights are controlled |
| Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman | https://arxiv.org/abs/2411.12113 | strip variables still do not directly match smooth/squarefree hypotheses |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval theta=0.52 does not close monotone strip phase saving at theta=1/2 |

```text
FKMS_trace_function_bilinear=the boundary is no longer arbitrary, but monotone strip packets still need a trace-family completion
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=moving q denominators remain uncompleted on strip endpoints
Pascadi_composite_Type_II=strip packets are Type-II-like only after endpoint weights are absorbed
Wright_unbalanced_convolution=right_tail gives an unbalanced candidate, not a closed convolution theorem
Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman=no direct match for strip weights
Li_short_interval_x_052=does not close the needed theta=1/2 strip endpoint control
```

结论：bulk 之外的 boundary 不再是任意剩余集合；它精确分解为三条单调 prime-interval strip。
但三条 strip 总量仍为 `177515` 条边，仍需要新的边界相消、endpoint summation-by-parts 或 completed trace family。

## 5. 最新最窄口

```text
BoundaryPhaseSavingForThreeMonotonePrimeIntervalStrips
AND CompletedTraceFamilyForPrimePrimeBulkRectangle
AND StripEndpointSummationByPartsWithoutComparableLoss
AND DiagonalPGhostSubtractionDiscipline
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
bulk_prefix_start_verified=true
left_tail_vanishes_verified=true
boundary_three_strip_identity_verified=true
boundary_strips_are_monotone_prime_interval_packets=true
boundary_phase_saving_closed=false
strip_completion_without_loss_closed=false
completed_trace_or_kloosterman_variable_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
