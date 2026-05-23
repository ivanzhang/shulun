# Prime Matrix Phi-LPF q-support row-averaged additive-k completion tax 审计

**状态：** `complete_interval_replacement_rejected_completion_correction_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
true_support=K_{P,q}={floor(qm/P): m is a selected residual LPF cofactor in the q-bucket}
tempting_completion=[min K_{P,q}, max K_{P,q}]
completion_decomposition=complete interval = true sparse support disjoint union completion holes
hole_classification=each hole has no odd product-cell candidate, or its unique odd candidate is not a residual LPF cofactor
remaining_obstruction=control the completion correction without changing the Phi-LPF selector
```

## 2. completion tax 有限审计

```text
max_prime=1009
P_value_count=165
selected_q_bucket_count_total=6020
previous_selected_q_bucket_count_total=6020
real_k_count_total=299977
previous_total_k_support_count=299977
completion_span_total=1602928
previous_total_k_span_length=1602928
completion_holes_total=1302951
previous_total_k_interval_holes=1302951
completion_holes_match_previous_total=true
real_k_count_matches_previous_total=true
completion_span_matches_previous_total=true
completion_tax_ratio_total=4.343503
holes_without_odd_candidate_total=373676
holes_with_nonresidual_odd_candidate_total=929275
holes_with_residual_candidate_total=0
bad_odd_count_over_one_total=0
odd_candidate_prime_total=355919
odd_candidate_small_lpf_3_total=409713
odd_candidate_small_lpf_5_total=163643
odd_candidate_other_nonresidual_total=0
max_completion_holes_per_q=556
max_completion_tax_ratio_per_q=11.500000
first_completion_hole=P=43,q=23,k=27,I=[51,52],m=51,class=odd_candidate_small_lpf_3
first_residual_candidate_hole=none
residual_candidate_holes_absent=true
complete_interval_replacement_object_preserving=false
completion_correction_control_closed=false
```

代表 P：

| P | selected_q_bucket_count | real_k_count | completion_span | completion_holes | completion_tax_ratio | holes_without_odd_candidate | holes_with_nonresidual_odd_candidate | odd_candidate_prime | odd_candidate_small_lpf_3 | odd_candidate_small_lpf_5 | max_completion_holes_per_q | first_completion_hole |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 9 | 48 | 350 | 302 | 6.291666666666667 | 82 | 220 | 96 | 88 | 36 | 50 | P=101,q=53,k=41,I=[79,80],m=79,class=odd_candidate_prime |
| 257 | 23 | 377 | 2325 | 1948 | 5.16710875331565 | 520 | 1428 | 591 | 602 | 235 | 151 | P=257,q=131,k=68,I=[134,135],m=135,class=odd_candidate_small_lpf_3 |
| 971 | 71 | 5672 | 29055 | 23383 | 4.1225317348378 | 6786 | 16597 | 6206 | 7422 | 2969 | 540 | P=971,q=487,k=248,I=[495,496],m=495,class=odd_candidate_small_lpf_3 |
| 1009 | 72 | 5901 | 30358 | 24457 | 4.144551770886291 | 7275 | 17182 | 6414 | 7693 | 3075 | 556 | P=1009,q=509,k=258,I=[512,513],m=513,class=odd_candidate_small_lpf_3 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SparseKCompletionTaxLedger | true | true | Completing each q-bucket to its full k interval adds an explicit disjoint correction set. | none |
| ResidualCandidateHoleExclusion | true | true | A completion hole cannot contain a selected residual LPF cofactor; otherwise it would already be in K_{P,q}. | none |
| DirectCompleteIntervalObjectPreservation | false | false | The completed interval is not the same object because the correction is much larger than the true support. | requires loss-controlled correction theorem |
| CompletionCorrectionCancellationOrAbsorption | false | false | Bound the fake completion correction, including no-odd, prime-candidate, and small-LPF candidate holes. | new correction cancellation/absorption theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3=trace-function bilinear bounds are relevant only after the sparse support plus correction is embedded in a genuine trace-family bilinear form
Milicevic_Qin_Wu_2025_arXiv_2511_07550=arbitrary-modulus Kloosterman bilinear savings do not by themselves bound the non-Kloosterman completion-hole correction
Pascadi_2025_arXiv_2511_08445=composite Type-II Kloosterman amplification needs a true bilinear Kloosterman object, not a completed interval plus fake nonresidual holes
Wright_2026_arXiv_2604_25177=unbalanced convolution/Kloosterman-fraction inputs require controlled convolution support and small-modulus equidistribution; the completion holes are not yet such a support
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree Kloosterman-parameter estimates do not remove the prime and small-LPF hole correction
```

结论：完整区间 completion 的相消若直接使用，会把真实 sparse LPF 支撑替换成一个大得多的对象。补入 correction 全部来自无奇候选或非 residual LPF 奇候选；这正是下一步必须控制的非循环硬点。

## 5. 最新最窄口

```text
CompletionCorrectionCancellationOrAbsorptionForSparseLPFKSupport
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
sparse_k_completion_tax_ledger_closed=true
residual_candidate_hole_exclusion_closed=true
direct_complete_interval_object_preservation_closed=false
completion_correction_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
