# Prime Matrix Phi-LPF boundary endpoint-flux q-prefix phase normal-form 审计

**状态：** `qprefix_line_atoms_have_phase_normal_form_completed_trace_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=15439 fixed-m q-prefix line atoms carrying 177515 edges
identity=q*m=k*P+D with e(h*k*P/q)=e(-h*D/q)=e(h*A(q)/q)
dominant_shape=moving Beatty numerator A(q) on a prime-q prefix
remaining=phase saving for moving-numerator prime-q reciprocal orbits and no-loss aggregation
```

## 2. 相位正规形有限审计

```text
max_prime=1009
previous_qprefix_line_atom_count_total=15439
previous_qprefix_line_atom_edge_count_total=177515
phase_normal_form_atom_count_total=15439
phase_normal_form_edge_count_total=177515
product_division_mismatch_count=0
phase_congruence_mismatch_count=0
q_not_prime_count=0
m_not_prime_count=0
m_equals_P_count=0
k_out_of_strict_row_range_count=0
D_out_of_range_count=0
A_zero_count=0
k_nonincreasing_step_count=0
phase_normal_form_identity_verified=true
q_prefix_count_min/median_atom_weighted/max=1/10/37
k_span_min/median/max=1/62/318
k_distinct_count_min/median/max=1/10/37
k_step_min/median/max=1/6.0/33
phase_normal_form_closed=true
qprefix_line_atom_phase_saving_closed=false
```

atom strip 分桶：

| strip | atom_count | edge_weight_sum |
| --- | --- | --- |
| lower_wing | 2466 | 29144 |
| right_tail | 6962 | 86751 |
| upper_wing | 6011 | 61620 |

k-orbit 分桶：

| k_orbit_class | atom_count | edge_weight_sum |
| --- | --- | --- |
| singleton_q | 1162 | 1162 |
| strict_beatty_k_multiq | 14277 | 176353 |

normalized numerator motion 分桶：

| numerator_motion_class | atom_count | edge_weight_sum |
| --- | --- | --- |
| constant_normalized_numerator | 1164 | 1166 |
| moving_beatty_numerator | 14275 | 176349 |

endpoint-flux class 分桶：

| endpoint_flux_class | atom_count | edge_weight_sum |
| --- | --- | --- |
| lower_wing_single_contiguous_endpoint_shell | 2466 | 29144 |
| right_tail_left_collar_only_no_P_puncture | 633 | 8652 |
| right_tail_left_collar_only_with_P_puncture | 54 | 776 |
| right_tail_right_collar_only_no_P_puncture | 1237 | 12879 |
| right_tail_right_collar_only_with_P_puncture | 42 | 708 |
| right_tail_terminal_full_interval_no_P_puncture | 131 | 2487 |
| right_tail_terminal_full_interval_with_P_puncture | 267 | 4864 |
| right_tail_two_sided_left_and_right_collars_no_P_puncture | 4398 | 52957 |
| right_tail_two_sided_left_and_right_collars_with_P_puncture | 200 | 3428 |
| upper_wing_single_contiguous_endpoint_shell | 6011 | 61620 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| QPrefixLineAtomLedgerImported | True | True | The fixed-m q-prefix atom ledger is inherited. | none for support import |
| ProductDivisionPhaseNormalForm | True | True | Every edge has q*m=k*P+D with 1<=k<P and 1<=D<P. | none for deterministic division normal form |
| ReciprocalPhaseRelabeling | True | True | The endpoint phase is exactly e(-h*D/q)=e(h*A(q)/q). | none for formal phase relabeling |
| BeattyKOrbitMonotonicity | True | True | On every multi-q atom, k(q)=floor(q*m/P) is strictly increasing along the prime prefix. | none for finite orbit monotonicity |
| FixedNumeratorCompletedKloostermanInput | False | False | Most atoms have a moving Beatty numerator A(q), so the normalized family is not a fixed-numerator completed Kloosterman input. | need a moving-numerator completion or a new reciprocal-orbit estimate |
| QPrefixLineAtomPhaseSaving | False | False | Prove cancellation on moving-numerator fixed-m prime-q prefix reciprocal orbits. | new completed trace/Kloosterman or Vaughan-Type-II bridge required |
| NoLossQPrefixAtomAggregation | False | False | Aggregate atom-level phase estimates across all 15439 atoms without losing the boundary gain. | requires analytic aggregation discipline |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | trace bilinear input would need a completed moving-q family, not just the real reciprocal normal form |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | arbitrary-modulus Kloosterman estimates require an inverse-fraction or completed trace variable after normalization |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | one-dimensional q-prefix orbits with moving numerator are not direct composite Type-II rectangles |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced Kloosterman fractions become relevant only after converting A(q)/q to an admissible completed family |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval prime existence does not estimate the fixed-m q-prefix reciprocal phase orbit |

```text
FKMS_trace_bilinear=normal form gives explicit reciprocal phases, but not a completed moving-q trace family
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=no direct inverse-fraction Kloosterman variable is produced by e(A(q)/q)
Pascadi_composite_Type_II=q-prefix line atoms remain one-dimensional after fixed-m normalization
Wright_unbalanced_Kloosterman=closest candidate after converting moving numerator A(q) into an admissible completed family
Li_short_interval_x_052=prime existence in short intervals does not estimate the normalized reciprocal phase
```

结论：fixed-m q-prefix atom 的 endpoint phase 已经正规化为移动分子
`A(q)/q` 的 prime-q reciprocal orbit。该层关闭的是确定性相位正规形，
不关闭相位节省、completed trace/Kloosterman 输入或全局无损聚合。

## 5. 最新最窄口

```text
MovingBeattyNumeratorPrimeQPrefixReciprocalPhaseSaving
AND CompletionOfA(q)/qToExternalTraceOrKloostermanFamily
AND NoLossAggregationAcross15439QPrefixPhaseAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
phase_normal_form_closed=true
fixed_numerator_completed_kloosterman_input_available=false
moving_q_denominator_completed_trace_closed=false
qprefix_line_atom_phase_saving_closed=false
no_loss_qprefix_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
