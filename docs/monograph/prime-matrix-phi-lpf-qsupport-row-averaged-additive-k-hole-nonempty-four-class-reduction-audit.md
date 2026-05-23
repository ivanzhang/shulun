# Prime Matrix Phi-LPF q-support row-averaged additive-k hole nonempty four-class reduction 审计

**状态：** `empty_hole_class_eliminated_four_class_phase_control_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
carrier_interval=M_{P,q}=[max(P/2+1,q),2P-1]∩Z
carrier_floor_map=m -> floor(qm/P) is monotone and has adjacent increments 0 or 1 because q<P
empty_class_elimination=every k between min K_{P,q} and max K_{P,q} has a carrier integer m, so completion holes are nonempty
four_class_phase=S_H=S_even+S_prime+S_lpf3+S_lpf5
remaining_obstruction=prove cancellation or absorption for the four nonempty class phase packets
```

## 2. four-class reduction 有限审计

```text
max_prime=1009
P_value_count=165
q_bucket_count_total=6020
previous_q_bucket_count_total=6020
real_k_count_total=299977
previous_real_k_count_total=299977
hole_count_total=1302951
previous_hole_count_total=1302951
four_class_hole_count_total=1302951
carrier_gap_count_total=0
selected_span_missing_count_total=0
empty_hole_count_total=0
previous_empty_hole_count_total=0
forbidden_hole_count_total=0
max_carrier_fiber_size=2
counts_match_previous_hole_class_audit=true
carrier_floor_map_no_skip_verified=true
selected_span_nonempty_verified=true
empty_class_eliminated=true
four_class_reduction_closed=true
count_even_singleton_total=373676
count_odd_candidate_prime_total=355919
count_odd_candidate_lpf3_total=409713
count_odd_candidate_lpf5_total=163643
four_class_phase_control_closed=false
```

代表 P：

| P | q_bucket_count | hole_count | carrier_gap_count | selected_span_missing_count | empty_hole_count | count_even_singleton | count_odd_candidate_prime | count_odd_candidate_lpf3 | count_odd_candidate_lpf5 | max_carrier_fiber_size |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 9 | 302 | 0 | 0 | 0 | 82 | 96 | 88 | 36 | 2 |
| 257 | 23 | 1948 | 0 | 0 | 0 | 520 | 591 | 602 | 235 | 2 |
| 971 | 71 | 23383 | 0 | 0 | 0 | 6786 | 6206 | 7422 | 2969 | 2 |
| 1009 | 72 | 24457 | 0 | 0 | 0 | 7275 | 6414 | 7693 | 3075 | 2 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CarrierFloorMapNoSkip | true | true | The carrier floor map has no missing intermediate k-values. | none |
| SelectedSpanNonempty | true | true | Every k in the selected span [minK,maxK] has a nonempty product cell. | none |
| EmptyHoleClassEliminated | true | true | The empty-cell packet is identically zero for the row-averaged q-buckets. | none |
| FourClassHolePhaseControl | false | false | Control the even, prime, LPF3, and LPF5 hole phase packets. | new four-class cancellation/absorption theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3=trace-function bilinear bounds would need an embedding of one of the four nonempty hole packets into a trace family
Milicevic_Qin_Wu_2025_arXiv_2511_07550=arbitrary-modulus Kloosterman bilinear estimates still require a Kloosterman-type phase for the four packets
Pascadi_2025_arXiv_2511_08445=composite Type-II input is relevant only after a four-class packet becomes a Type-II/Kloosterman object
Wright_2026_arXiv_2604_25177=unbalanced convolution estimates require controlled convolution support; four-class locality alone is not enough
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree Kloosterman-parameter estimates do not directly control the even/prime/LPF3/LPF5 packets
```

结论：empty-cell packet 被结构性消除，hole correction 从五类压为四类。剩余不是 carrier 是否存在，而是 even/prime/LPF3/LPF5 四个非空相位包的统一相消或吸收。

## 5. 最新最窄口

```text
FourClassHolePhaseCancellationOrAbsorption
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
carrier_floor_map_no_skip_closed=true
selected_span_nonempty_closed=true
empty_hole_class_eliminated=true
four_class_hole_phase_identity_closed=true
four_class_phase_control_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
