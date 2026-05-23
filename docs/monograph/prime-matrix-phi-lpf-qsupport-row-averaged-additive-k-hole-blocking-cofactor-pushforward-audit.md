# Prime Matrix Phi-LPF q-support row-averaged additive-k hole blocking-cofactor pushforward 审计

**状态：** `four_class_hole_correction_pushed_to_blocking_cofactor_two_family_phase_control_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
blocking_selector=odd candidate if present, otherwise the even singleton carrier
blocker_lpf_classes=LPF(m)=2,3,5 or m is prime
two_family_phase=S_H=S_{30-wheel-blocker}+S_{prime-blocker}
small_lpf_packet=finite 30-wheel rejection packet with LPF 2,3,5
prime_packet=dynamic prime blocker packet; still needs phase saving or absorption
```

## 2. blocking-cofactor pushforward 有限审计

```text
max_prime=1009
P_value_count=165
q_bucket_count_total=6020
previous_q_bucket_count_total=6020
real_k_count_total=299977
previous_real_k_count_total=299977
hole_count_total=1302951
previous_hole_count_total=1302951
blocking_cofactor_count_total=1302951
small_lpf_blocker_count_total=947032
prime_blocker_count_total=355919
small_lpf_blocker_ratio=0.726836
prime_blocker_ratio=0.273164
count_blocker_lpf2_even_total=373676
count_blocker_lpf3_total=409713
count_blocker_lpf5_total=163643
count_blocker_prime_total=355919
bad_empty_total=0
bad_odd_multiplicity_total=0
bad_floor_mismatch_total=0
bad_residual_blocker_total=0
bad_class_mismatch_total=0
duplicate_blocker_m_total=0
total_bad_pushforward_count=0
max_pushforward_identity_error=9.334e-14
pushforward_identity_verified=true
counts_match_previous_four_class_reduction=true
unique_blocker_per_hole_verified=true
two_family_split_closed=true
sum_abs_small_lpf_blocker_sum_h1=104345.004183
sum_abs_prime_blocker_sum_h1=61696.864692
dominant_two_family_bucket_counts_h1={"prime_blocker": 757, "small_lpf_blocker": 5263}
two_family_phase_control_closed=false
```

代表 P：

| P | q_bucket_count | hole_count | blocking_cofactor_count | small_lpf_blocker_count | prime_blocker_count | bad_empty | bad_floor_mismatch | bad_residual_blocker | duplicate_blocker_m | max_pushforward_identity_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 9 | 302 | 302 | 206 | 96 | 0 | 0 | 0 | 0 | 2.6645352591003757e-15 |
| 257 | 23 | 1948 | 1948 | 1357 | 591 | 0 | 0 | 0 | 0 | 8.188600426433445e-15 |
| 971 | 71 | 23383 | 23383 | 17177 | 6206 | 0 | 0 | 0 | 0 | 6.820493206571139e-14 |
| 1009 | 72 | 24457 | 24457 | 18043 | 6414 | 0 | 0 | 0 | 0 | 5.728578676879116e-14 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| UniqueBlockingCofactorForEveryHole | true | true | Every completion hole has one selected blocker cofactor m_h. | none |
| HolePhasePushforwardToBlockingCofactors | true | true | The phase e(hPk/q) equals e(hP floor(qm_h/P)/q) under the blocker map. | none |
| ThirtyWheelVsPrimeBlockerSplit | true | true | Blockers split into finite 30-wheel LPF 2/3/5 rejections and prime blockers. | none |
| TwoFamilyBlockerPhaseControl | false | false | Control or absorb the small-LPF blocker packet and the prime blocker packet. | new two-family cancellation/absorption theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3=trace-function bilinear estimates still require converting the blocker floor phase into a trace family
Milicevic_Qin_Wu_2025_arXiv_2511_07550=arbitrary-modulus Kloosterman bounds do not directly see the floor blocker selector
Pascadi_2025_arXiv_2511_08445=composite Type-II input may become relevant only after the blocker support is reorganised into long bilinear fibres
Wright_2026_arXiv_2604_25177=unbalanced convolution/Kloosterman-fraction estimates still need a completed convolution support
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree Kloosterman-parameter estimates do not control the prime blocker selector by themselves
```

结论：每个 completion hole 被一个唯一 blocking cofactor 推前；四类 correction 变成 30-wheel 小 LPF 阻塞包与 prime 阻塞包。剩余不是 blocker 是否存在，而是两个 packet 的相消、吸收或 trace/Type-II 嵌入。

## 5. 最新最窄口

```text
TwoFamilyBlockerPhaseCancellationOrAbsorption
AND PrimeBlockerDynamicSqrtSieveOrTraceEmbedding
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
unique_blocking_cofactor_closed=true
hole_phase_pushforward_closed=true
thirty_wheel_vs_prime_blocker_split_closed=true
two_family_phase_control_closed=false
prime_blocker_trace_embedding_closed=false
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
