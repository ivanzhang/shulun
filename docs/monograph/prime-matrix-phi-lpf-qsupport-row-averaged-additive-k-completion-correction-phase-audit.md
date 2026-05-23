# Prime Matrix Phi-LPF q-support row-averaged additive-k completion correction phase 审计

**状态：** `complete_interval_geometric_phase_closed_hole_correction_phase_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
phase_identity=S_K(h)=S_C(h)-S_H(h), with S_C a finite geometric progression
phase_h_tested=h=1 for finite magnitude diagnostics; the symbolic identity holds for every integer h
complete_interval_term=explicit geometric additive-character sum on [min K_{P,q},max K_{P,q}]
hole_correction=non-object holes from no-odd, prime-candidate, and small-LPF candidate cells
remaining_obstruction=prove cancellation or absorption for S_H without changing the Phi-LPF selector
```

## 2. correction phase 有限审计

```text
max_prime=1009
P_value_count=165
q_bucket_count_total=6020
previous_selected_q_bucket_count_total=6020
real_k_count_total=299977
previous_real_k_count_total=299977
complete_span_total=1602928
previous_completion_span_total=1602928
hole_count_total=1302951
previous_completion_holes_total=1302951
phase_identity_counts_match_completion_tax=true
geometric_formula_verified=true
correction_phase_identity_verified=true
max_geometric_formula_error=3.329e-11
max_correction_identity_error=1.641e-13
sum_abs_sparse_sum_h1=53897.476591
sum_abs_complete_geometric_sum_h1=12232.215742
sum_abs_hole_correction_sum_h1=56664.077674
max_abs_sparse_sum_h1=57.946684
max_abs_complete_geometric_sum_h1=158.704702
max_abs_hole_correction_sum_h1=118.782265
max_hole_over_complete_abs_ratio_h1=4699.709076
hole_abs_gt_complete_abs_bucket_count_h1=5150
sparse_abs_gt_complete_abs_bucket_count_h1=5000
complete_near_zero_with_nonzero_hole_bucket_count_h1=10
hole_label_no_odd_candidate_total=373676
hole_label_odd_candidate_prime_total=355919
hole_label_odd_candidate_small_lpf_3_total=409713
hole_label_odd_candidate_small_lpf_5_total=163643
hole_label_residual_candidate_total=0
first_hole_dominates_complete=P=43,q=23,holes=14,abs_complete=0.677199,abs_hole=1.304173,abs_sparse=1.981372
complete_interval_geometric_part_closed=true
hole_correction_phase_control_closed=false
```

代表 P：

| P | q_bucket_count | real_k_count | complete_span | hole_count | sum_abs_sparse_sum_h1 | sum_abs_complete_geometric_sum_h1 | sum_abs_hole_correction_sum_h1 | hole_abs_gt_complete_abs_bucket_count_h1 | max_hole_over_complete_abs_ratio_h1 | first_hole_dominates_complete |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 9 | 48 | 350 | 302 | 19.640376500422985 | 9.474317894272271 | 17.385923950981883 | 5 | 10.072897778193902 | P=101,q=59,holes=47,abs_complete=0.586220,abs_hole=3.278769,abs_sparse=3.597167 |
| 257 | 23 | 377 | 2325 | 1948 | 67.43461750420927 | 33.42505688282972 | 71.30962995871994 | 18 | 13.908583828425138 | P=257,q=139,holes=147,abs_complete=0.295822,abs_hole=3.555999,abs_sparse=3.837487 |
| 971 | 71 | 5672 | 29055 | 23383 | 990.2102732616503 | 162.98386767824434 | 1034.8263203515262 | 61 | 952.2908045479197 | P=971,q=491,holes=540,abs_complete=7.435712,abs_hole=11.407849,abs_sparse=5.635265 |
| 1009 | 72 | 5901 | 30358 | 24457 | 1070.3740507279103 | 120.96062219843084 | 1083.574586746076 | 66 | 391.34887899828055 | P=1009,q=509,holes=556,abs_complete=11.737606,abs_hole=14.142103,abs_sparse=3.314197 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CompleteIntervalGeometricPhaseFormula | true | true | The completed k-interval contribution is an explicit geometric additive-character sum. | none |
| SparseSupportMinusHoleCorrectionIdentity | true | true | The true sparse sum equals the complete interval sum minus the completion-hole correction. | none |
| HoleCorrectionPhaseCancellationOrAbsorption | false | false | Control the correction phase sum from no-odd, prime-candidate, and small-LPF holes. | new correction phase theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3=the complete interval part is now elementary; trace-function input would have to control or bypass the non-trace hole correction
Milicevic_Qin_Wu_2025_arXiv_2511_07550=arbitrary-modulus Kloosterman bilinear estimates do not apply directly to the additive hole correction S_H
Pascadi_2025_arXiv_2511_08445=composite Type-II amplification is downstream of converting S_H into a true Kloosterman/Type-II family
Wright_2026_arXiv_2604_25177=unbalanced convolution estimates become relevant only after the hole correction is embedded in a controlled convolution support
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree parameter estimates do not absorb the prime and small-LPF hole phases automatically
```

结论：完整区间相位项已退化为显式几何和；真实难点完全落到 completion-hole correction 的相位控制。有限账本中很多 q-bucket 的 hole correction 幅度大于完整区间几何项，因此不能把 correction 当作可忽略误差。

## 5. 最新最窄口

```text
HoleCorrectionPhaseCancellationOrAbsorptionForNoOddPrimeSmallLPFCells
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
complete_interval_geometric_phase_closed=true
sparse_support_minus_hole_correction_identity_closed=true
hole_correction_phase_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
