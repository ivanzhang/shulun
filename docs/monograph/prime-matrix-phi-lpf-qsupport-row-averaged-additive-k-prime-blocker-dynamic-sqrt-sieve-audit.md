# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-blocker dynamic sqrt-sieve 审计

**状态：** `prime_blocker_packet_rewritten_as_dynamic_sqrt_sieve_survivors_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
prime_blocker_identity=m_h prime iff m_h is not 0 modulo every prime ell<=sqrt(m_h)
dynamic_packet=S_{prime-blocker}=S_{sqrt-sieve-survivor}
thirty_wheel_relation=all non-survivors are exactly LPF 2/3/5 blockers already in the 30-wheel packet
moving_primorial=W(m_h)=prod_{ell<=sqrt(m_h)} ell varies with m_h
remaining=phase saving or trace/Type-II embedding for the moving survivor packet
```

## 2. dynamic sqrt-sieve 有限审计

```text
max_prime=1009
blocker_count_total=1302951
previous_blocker_count_total=1302951
small_lpf_blocker_count_total=947032
previous_small_lpf_blocker_count_total=947032
prime_blocker_count_total=355919
previous_prime_blocker_count_total=355919
sqrt_sieve_survivor_count_total=355919
sqrt_sieve_rejected_count_total=947032
bad_prime_survivor_mismatch_total=0
bad_composite_survivor_total=0
bad_prime_rejected_total=0
rough_composite_rejection_after_5_total=0
q_bucket_with_prime_blocker_count=5848
q_bucket_prime_phase_mismatch_count=0
max_prime_packet_phase_identity_error=0.000e+00
total_bad_dynamic_sqrt_sieve_count=0
counts_match_previous_primorial_escalation=true
prime_blocker_equals_dynamic_sqrt_survivor_verified=true
sqrt_sieve_rejections_are_exactly_lpf_2_3_5=true
max_pi_sqrt_all=14
max_pi_sqrt_prime_blocker=14
max_mobius_terms_per_blocker=16384
prime_blocker_full_sqrt_tests_total=3373946
small_lpf_short_circuit_tests_total=1684031
prime_blocker_mobius_terms_full_expansion_total=399176624
distinct_sqrt_limits_seen=38
distinct_largest_sqrt_prime_seen=11
max_W_sqrt_bits=54
max_W_sqrt_over_P=13814953887719.144531
```

obstruction counts:

```text
{"2": 373676, "3": 409713, "5": 163643, "none": 355919}
```

逐层 cutoff 摘要：

| cutoff | rejected_count | survivor_count | prime_survivor_count | small_lpf_rejected_count | new_rejections_after_5 |
| --- | --- | --- | --- | --- | --- |
| 2 | 373676 | 929275 | 355919 | 373676 | 0 |
| 3 | 783389 | 519562 | 355919 | 783389 | 0 |
| 5 | 947032 | 355919 | 355919 | 947032 | 0 |
| 7 | 947032 | 355919 | 355919 | 947032 | 0 |
| 11 | 947032 | 355919 | 355919 | 947032 | 0 |
| 13 | 947032 | 355919 | 355919 | 947032 | 0 |
| 17 | 947032 | 355919 | 355919 | 947032 | 0 |
| 19 | 947032 | 355919 | 355919 | 947032 | 0 |
| 23 | 947032 | 355919 | 355919 | 947032 | 0 |
| 29 | 947032 | 355919 | 355919 | 947032 | 0 |
| 31 | 947032 | 355919 | 355919 | 947032 | 0 |
| 37 | 947032 | 355919 | 355919 | 947032 | 0 |
| 41 | 947032 | 355919 | 355919 | 947032 | 0 |
| 43 | 947032 | 355919 | 355919 | 947032 | 0 |

代表 P：

| P | blockers | small_lpf_blockers | prime_blockers | sqrt_sieve_survivors | sqrt_sieve_rejections | bad_mismatch | max_pi_sqrt | max_W_sqrt_bits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 302 | 206 | 96 | 96 | 206 | 0 | 6 | 15 |
| 257 | 1948 | 1357 | 591 | 591 | 1357 | 0 | 8 | 24 |
| 971 | 23383 | 17177 | 6206 | 6206 | 17177 | 0 | 14 | 54 |
| 1009 | 24457 | 18043 | 6414 | 6414 | 18043 | 0 | 14 | 54 |

prime-blocker 样本：

```text
P=43,q=23,k=28,m=53,sqrt=7,pi_sqrt=4,W_bits=8
P=43,q=23,k=31,m=59,sqrt=7,pi_sqrt=4,W_bits=8
P=43,q=23,k=32,m=61,sqrt=7,pi_sqrt=4,W_bits=8
P=43,q=23,k=35,m=67,sqrt=8,pi_sqrt=4,W_bits=8
P=43,q=23,k=37,m=71,sqrt=8,pi_sqrt=4,W_bits=8
P=43,q=23,k=39,m=73,sqrt=8,pi_sqrt=4,W_bits=8
P=53,q=29,k=32,m=59,sqrt=7,pi_sqrt=4,W_bits=8
P=53,q=29,k=33,m=61,sqrt=7,pi_sqrt=4,W_bits=8
```

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PrimeBlockerDynamicSqrtSieveIdentity | true | true | The prime-blocker indicator equals the dynamic sqrt-sieve survivor indicator on every blocker. | none |
| PrimeBlockerPhasePacketPushforward | true | true | The additive prime-blocker packet equals the additive survivor packet bucket by bucket. | none |
| NoRoughCompositeSqrtRejectionAfterThirtyWheel | true | true | After LPF 2/3/5 rejections, no LPF 7/11/... composite blocker remains. | none |
| MovingPrimorialMobiusCompression | false | false | Compress the moving sqrt-sieve survivor product into a usable completed bilinear/trace family. | new compression or trace embedding theorem |
| PrimeBlockerSurvivorPhaseSaving | false | false | Prove cancellation or absorption for the survivor packet itself. | non-wheel phase saving beyond parity |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | candidate trace-function bilinear input after a genuine blocker-to-trace embedding |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | candidate arbitrary-modulus Kloosterman input after completion of the moving sqrt-sieve packet |
| Pascadi_2025_composite_type_II | https://arxiv.org/abs/2511.08445 | candidate composite Type-II input only after the packet is reorganised into bilinear fibres |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | candidate unbalanced convolution input after a completed convolution model exists |
| Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman | https://arxiv.org/abs/2411.12113 | candidate smooth/squarefree parameter input, not a direct prime-blocker selector estimate |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval prime input remains above the theta=1/2 pointwise scale needed for direct closure |

```text
FKMS_trace_function_bilinear=not directly applicable until the moving sqrt-sieve survivor packet is embedded into a trace-function family
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=does not by itself compress W(m_h)-moving local congruence constraints into a completed Kloosterman sum
Pascadi_composite_Type_II=may help only after the blocker support is reorganised as long bilinear fibres
Wright_unbalanced_convolution=requires a completed convolution/Kloosterman-fraction form, not just the pointwise primality sieve
Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman=does not directly estimate the prime-blocker survivor selector
Li_short_interval_x_052=theta=0.52 remains above the pointwise theta=1/2 scale, so it does not close this packet
```

结论：prime-blocker packet 已被改写成动态 sqrt-sieve survivor packet；所有非幸存者正好是 30-wheel 的 LPF 2/3/5 blocker。剩余不再是素性判定，而是 moving primorial survivor packet 的相位节省、Mobius 压缩或 trace/Type-II 嵌入。

## 5. 最新最窄口

```text
PrimeBlockerSqrtSieveSurvivorPhaseSavingOrTraceEmbedding
AND MovingPrimorialMobiusExpansionCompression
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
prime_blocker_dynamic_sqrt_sieve_identity_closed=true
prime_blocker_phase_packet_pushforward_closed=true
no_rough_composite_sqrt_rejection_after_30_closed=true
moving_primorial_mobius_compression_closed=false
prime_blocker_survivor_phase_saving_closed=false
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
