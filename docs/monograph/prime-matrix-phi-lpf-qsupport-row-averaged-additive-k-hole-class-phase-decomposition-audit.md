# Prime Matrix Phi-LPF q-support row-averaged additive-k hole-class phase decomposition 审计

**状态：** `hole_class_phase_decomposition_closed_class_phase_control_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
phase_decomposition=S_H=S_empty+S_even+S_prime+S_lpf3+S_lpf5
classification_law=hole cells have length <2; an odd nonresidual candidate is either prime or has LPF 3 or 5
remaining_obstruction=prove cancellation or absorption for the five class phase packets without changing the selector
```

## 2. hole-class phase 有限审计

```text
max_prime=1009
P_value_count=165
q_bucket_count_total=6020
previous_q_bucket_count_total=6020
real_k_count_total=299977
previous_real_k_count_total=299977
hole_count_total=1302951
previous_hole_count_total=1302951
classified_hole_count_total=1302951
counts_match_previous_correction_phase=true
hole_class_identity_verified=true
max_class_identity_error=9.664e-14
forbidden_class_count_total=0
only_empty_even_prime_lpf3_lpf5_classes_seen=true
count_empty_cell_total=0
count_even_singleton_total=373676
count_odd_candidate_prime_total=355919
count_odd_candidate_lpf3_total=409713
count_odd_candidate_lpf5_total=163643
sum_abs_empty_cell_sum_h1=0.000000
sum_abs_even_singleton_sum_h1=178003.033657
sum_abs_odd_candidate_prime_sum_h1=61696.864692
sum_abs_odd_candidate_lpf3_sum_h1=65968.241426
sum_abs_odd_candidate_lpf5_sum_h1=30865.060099
dominant_hole_phase_class_bucket_counts_h1={"even_singleton": 5166, "none": 100, "odd_candidate_lpf3": 200, "odd_candidate_lpf5": 189, "odd_candidate_prime": 365}
class_phase_control_closed=false
```

代表 P：

| P | q_bucket_count | hole_count | count_empty_cell | count_even_singleton | count_odd_candidate_prime | count_odd_candidate_lpf3 | count_odd_candidate_lpf5 | dominant_class_counts_h1 | max_class_identity_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 9 | 302 | 0 | 82 | 96 | 88 | 36 | {"even_singleton": 4, "none": 1, "odd_candidate_lpf3": 3, "odd_candidate_prime": 1} | 2.220446049250313e-15 |
| 257 | 23 | 1948 | 0 | 520 | 591 | 602 | 235 | {"even_singleton": 20, "odd_candidate_lpf3": 1, "odd_candidate_lpf5": 2} | 8.188600426433445e-15 |
| 971 | 71 | 23383 | 0 | 6786 | 6206 | 7422 | 2969 | {"even_singleton": 62, "none": 1, "odd_candidate_lpf3": 2, "odd_candidate_lpf5": 2, "odd_candidate_prime": 4} | 6.469085794915281e-14 |
| 1009 | 72 | 24457 | 0 | 7275 | 6414 | 7693 | 3075 | {"even_singleton": 62, "odd_candidate_lpf3": 1, "odd_candidate_lpf5": 2, "odd_candidate_prime": 7} | 6.771159118751029e-14 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| HoleClassPartition | true | true | Every completion hole belongs to a deterministic local class. | none |
| OddHolePrimeOrSmallLPFReduction | true | true | An odd nonresidual completion-hole candidate is prime or has least prime factor 3 or 5. | none |
| HoleClassPhaseIdentity | true | true | The hole correction phase sum decomposes as the sum of the class phase packets. | none |
| FiveClassPhaseCancellationOrAbsorption | false | false | Control empty, even, prime, LPF3, and LPF5 hole phase packets. | new class-wise phase theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3=trace-function bilinear bounds would need a trace-family model for one of the five hole packets; the class split alone does not provide it
Milicevic_Qin_Wu_2025_arXiv_2511_07550=arbitrary-modulus Kloosterman bilinear estimates still require a Kloosterman phase, not merely the five local hole classes
Pascadi_2025_arXiv_2511_08445=composite Type-II input is downstream of converting prime/LPF3/LPF5 packets into a Type-II object
Wright_2026_arXiv_2604_25177=unbalanced convolution may be relevant only after a class packet is embedded in a controlled convolution support
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree Kloosterman-parameter estimates do not directly treat empty/even or prime/small-LPF additive hole packets
```

结论：`S_H` 的同对象 correction 已被压成五类局部 packet；这关闭了“hole correction 是黑箱残差”的粗口，但仍未证明五类 packet 的相消或吸收。

## 5. 最新最窄口

```text
FiveClassHolePhaseCancellationOrAbsorption
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
hole_class_partition_closed=true
odd_hole_prime_or_small_lpf_reduction_closed=true
hole_class_phase_identity_closed=true
five_class_phase_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
