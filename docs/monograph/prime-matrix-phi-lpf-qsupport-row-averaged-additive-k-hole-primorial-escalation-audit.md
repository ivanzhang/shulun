# Prime Matrix Phi-LPF q-support row-averaged additive-k hole primorial escalation 审计

**状态：** `primorial_escalation_inert_until_prime_oracle_cutoff`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
blocker_lpf_spectrum=LPF(m_h) in {2,3,5} or m_h prime
wheel_cutoff_rule=cutoff y kills blocker iff LPF(m_h)<=y
fixed_primorial_result=210, 2310, ... add no rough-composite blocker shell after 30
sqrt_cutoff_result=sqrt(2P-1) is below every prime blocker, so it equals 30-wheel on blockers
oracle_cutoff_result=2P-1 kills all blockers only by including each prime blocker itself
```

## 2. primorial escalation 有限审计

```text
max_prime=1009
P_value_count=165
blocker_count_total=1302951
previous_blocking_cofactor_count_total=1302951
small_lpf_blocker_count_total=947032
prime_blocker_count_total=355919
prime_blocker_min=53
prime_blocker_max=1987
prime_blocker_le_P_total=140983
prime_blocker_gt_P_total=214936
counts_match_previous_blocker_audit=true
thirty_wheel_kills_all_small_lpf_blockers=true
fixed_210_2310_and_beyond_new_rough_shell_count_total=0
fixed_primorial_extra_kills_over_30_total=0
sqrt_cutoff_killed_count=947032
sqrt_cutoff_extra_killed_over_30=0
sqrt_cutoff_same_as_30_verified=true
P_cutoff_prime_killed_total=140983
P_cutoff_prime_survived_total=214936
full_2P_minus_1_cutoff_closes_all=true
full_2P_minus_1_cutoff_is_prime_oracle=true
nonoracle_primorial_escalation_closes_target=false
```

primorial cutoff 层：

| level | cutoff_rule | oracle_strength | killed_count | survivor_count | prime_killed_count | prime_survived_count | extra_killed_over_30 | closes_all_blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W_5=30 | 5 | fixed_finite_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_7=210 | 7 | fixed_finite_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_11=2310 | 11 | fixed_finite_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_13=30030 | 13 | fixed_finite_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_17=510510 | 17 | fixed_finite_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_19=9699690 | 19 | fixed_finite_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_23=223092870 | 23 | fixed_finite_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_29=6469693230 | 29 | fixed_finite_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_31=200560490130 | 31 | fixed_finite_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_sqrt(2P-1) | floor(sqrt(2P-1)) | dynamic_sqrt_wheel | 947032 | 355919 | 0 | 355919 | 0 | false |
| W_P | P | uses_primes_up_to_row_scale | 1088015 | 214936 | 140983 | 214936 | 140983 | false |
| W_{2P-1} | 2P-1 | full_blocker_prime_oracle | 1302951 | 0 | 355919 | 0 | 355919 | true |

代表 P：

| P | blockers | small_lpf_blockers | prime_blockers | prime_blockers_le_P | prime_blockers_gt_P | sqrt_cutoff | sqrt_cutoff_equals_30_kill |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 302 | 206 | 96 | 26 | 70 | 14 | true |
| 257 | 1948 | 1357 | 591 | 224 | 367 | 22 | true |
| 971 | 23383 | 17177 | 6206 | 2431 | 3775 | 44 | true |
| 1009 | 24457 | 18043 | 6414 | 2504 | 3910 | 44 | true |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PrimorialCutoffActionOnBlockers | true | true | A cutoff y deletes exactly blockers with LPF(m_h)<=y. | none |
| NoNewRoughCompositeShellAfter30 | true | true | No blocker has LPF 7,11,13,... as a composite shell. | none |
| SqrtPrimorialEqualsThirtyWheelOnBlockers | true | true | The dynamic sqrt(2P-1) wheel kills no prime blocker. | none |
| NonOraclePrimorialEscalationClosure | false | false | Close the prime blocker packet without including the blocker primes themselves as wheel factors. | prime-blocker phase saving, trace embedding, or new non-wheel theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3=still relevant only after the prime blocker floor selector becomes a trace-function family
Milicevic_Qin_Wu_2025_arXiv_2511_07550=arbitrary-modulus Kloosterman bounds do not bypass the prime-blocker selector
Pascadi_2025_arXiv_2511_08445=composite Type-II amplification has no new LPF 7/11 composite shell to act on here
Wright_2026_arXiv_2604_25177=unbalanced convolution estimates still require a completed convolution form rather than primorial escalation
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree Kloosterman sums do not control surviving prime blockers by wheel refinement alone
```

结论：30-wheel 之后的 210、2310、... 不会产生新的 composite LPF shell；sqrt 级动态 wheel 仍等同于 30-wheel。只有 cutoff 达到 prime blocker 本身才会继续删除，而 `2P-1` 全删是 prime oracle，不是独立证明。

## 5. 最新最窄口

```text
PrimeBlockerNonWheelPhaseSavingOrTraceEmbedding
AND NonOracleControlOfPrimeBlockerDynamicSqrtSieve
AND FiniteThirtyWheelSmallLPFBlockerPacketControl
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
primorial_cutoff_action_closed=true
no_new_rough_composite_shell_after_30_closed=true
sqrt_primorial_equals_30_on_blockers_closed=true
nonoracle_primorial_escalation_closes_target=false
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
