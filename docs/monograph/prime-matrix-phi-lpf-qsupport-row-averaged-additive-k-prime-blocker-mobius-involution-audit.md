# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-blocker Mobius involution 审计

**状态：** `moving_mobius_expansion_reduced_to_euler_involution_and_prime_singletons_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
mobius_expansion=1_prime(m_h)=sum_{d|m_h,d|W(m_h)} mu(d)
small_lpf_mechanism=if first obstruction is s, terms pair by d <-> s*d and cancel pointwise
prime_survivor_mechanism=prime blockers have no nontrivial d and remain as the singleton d=1 layer
phase_identity=prime-blocker phase equals the Mobius-weighted all-blocker phase bucket by bucket
remaining=the singleton prime-survivor layer still needs phase saving or trace/Type-II embedding
```

## 2. Euler--Mobius involution 有限审计

```text
max_prime=1009
blocker_count_total=1302951
previous_blocker_count_total=1302951
small_lpf_blocker_count_total=947032
previous_small_lpf_blocker_count_total=947032
prime_blocker_count_total=355919
previous_prime_blocker_count_total=355919
mobius_survivor_weight_total=355919
previous_sqrt_sieve_survivor_count_total=355919
active_divisor_terms_total=4321483
prime_singleton_terms_total=355919
composite_cancelled_terms_total=3965564
composite_involution_pair_count_total=1982782
previous_prime_blocker_mobius_terms_full_expansion_total=399176624
active_terms_vs_previous_formal_ratio=0.01082599
max_basis_size=4
max_active_terms=16
max_pair_count=8
bad_prime_active_singleton_total=0
bad_composite_without_obstruction_total=0
bad_mobius_sum_identity_total=0
bad_involution_pairing_total=0
bad_first_obstruction_not_small_lpf_total=0
q_bucket_mobius_phase_mismatch_count=0
max_mobius_packet_phase_identity_error=0.000e+00
total_bad_mobius_involution_count=0
counts_match_previous_dynamic_sqrt_sieve=true
mobius_expansion_identity_verified=true
euler_involution_cancels_all_rejected_blockers=true
prime_survivors_are_singleton_d1_layer=true
```

basis size counts:

```text
{"0": 355919, "1": 457984, "2": 268999, "3": 193398, "4": 26651}
```

first obstruction counts:

```text
{"2": 373676, "3": 409713, "5": 163643, "none": 355919}
```

top basis counts:

```text
{"2": 127623, "2*11": 10363, "2*3": 61829, "2*3*5": 12481, "2*5": 29433, "2*7": 20361, "3": 217625, "3*11": 9863, "3*5": 46999, "3*7": 32552, "5": 112736, "prime_singleton": 355919}
```

代表 P：

| P | blockers | small_lpf_blockers | prime_blockers | mobius_survivor_weight | active_terms | cancelled_pairs | bad_mismatch | max_basis_size | max_active_terms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 302 | 206 | 96 | 96 | 746 | 325 | 0 | 3 | 8 |
| 257 | 1948 | 1357 | 591 | 591 | 5549 | 2479 | 0 | 4 | 16 |
| 971 | 23383 | 17177 | 6206 | 6206 | 80668 | 37231 | 0 | 4 | 16 |
| 1009 | 24457 | 18043 | 6414 | 6414 | 85070 | 39328 | 0 | 4 | 16 |

involution 样本：

```text
P=43,q=23,k=27,m=51,basis=3,first=3,terms=2,pairs=1
P=43,q=23,k=29,m=55,basis=5,first=5,terms=2,pairs=1
P=43,q=23,k=30,m=57,basis=3,first=3,terms=2,pairs=1
P=43,q=23,k=33,m=63,basis=3*7,first=3,terms=4,pairs=2
P=43,q=23,k=34,m=65,basis=5,first=5,terms=2,pairs=1
P=43,q=23,k=36,m=69,basis=3,first=3,terms=2,pairs=1
P=43,q=23,k=38,m=72,basis=2*3,first=2,terms=4,pairs=2
P=43,q=23,k=40,m=75,basis=3*5,first=3,terms=4,pairs=2
```

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| MovingMobiusDivisorExpansionIdentity | true | true | The dynamic sqrt-sieve survivor indicator equals the squarefree divisor Mobius sum. | none |
| EulerInvolutionCancelsRejectedBlockers | true | true | Every rejected blocker has a first obstruction s and its Mobius terms pair by d <-> s*d. | none |
| PrimeSurvivorSingletonLayerReduction | true | true | Every prime blocker contributes only the d=1 Mobius layer. | none |
| MovingMobiusExpansionSelfCompressionPhaseSaving | false | false | Obtain nontrivial cancellation from the Mobius expansion itself after the pointwise involution. | not available; requires new phase saving or embedding |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | below-Polya-Vinogradov trace bilinear input, still requiring a trace-family embedding |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | arbitrary-modulus Kloosterman bilinear input, still requiring completed Kloosterman form |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | composite-modulus Type-II amplification, not directly a pointwise Mobius involution estimate |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced convolution/Kloosterman-fraction input after convolution completion |
| Shao_Shparlinski_Wijaya_2024_squarefree_smooth_kloosterman | https://arxiv.org/abs/2411.12113 | smooth/squarefree Kloosterman parameter input, not direct survivor phase saving |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | pointwise short interval exponent remains above theta=1/2 |

```text
FKMS_trace_function_bilinear=still requires a nontrivial embedding of the prime singleton survivor layer into trace functions
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=still requires completed Kloosterman variables; the involution is pointwise, not bilinear
Pascadi_composite_Type_II=does not act on the already pointwise-cancelled small-LPF Mobius pairs
Wright_unbalanced_convolution=needs a convolution model for the survivor layer
Shao_Shparlinski_Wijaya_smooth_squarefree_Kloosterman=smooth/squarefree parameter estimates do not by themselves create survivor phase saving
Li_short_interval_x_052=short-interval theta=0.52 remains above the pointwise half-scale requirement
```

结论：moving Mobius 展开已拆成 Euler 首阻碍成对抵消和 prime survivor 的 `d=1` 单层。该展开本身不提供新的相位节省；真正剩余是 prime survivor singleton layer 的相消或 trace/Type-II 嵌入。

## 5. 最新最窄口

```text
PrimeSurvivorSingletonLayerPhaseSavingOrTraceEmbedding
AND NonPointwiseCompressionBeyondEulerMobiusInvolution
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
moving_mobius_divisor_expansion_identity_closed=true
euler_involution_cancels_rejected_blockers_closed=true
prime_survivor_singleton_layer_reduction_closed=true
moving_mobius_expansion_self_compression_phase_saving_closed=false
prime_survivor_singleton_layer_phase_saving_closed=false
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
