# Prime Matrix Phi-LPF q-support complementary pair radial tensor 审计

**状态：** `complementary_pair_radial_two_cylinder_normal_form_closed_direct_trace_input_rejected`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
local_factor=rho_l(n)=1 if l|n, else -1/(l-1)
pair_kernel_normal_form=K_q(n)=mu(q)*prod_{l|q}rho_l(n)+mu(W/q)*prod_{l|W/q}rho_l(n)
unit_orbit_radiality=K_q(un)=K_q(n) for every unit u mod W_P
two_cylinder_rank=rank 2 when both q and W_P/q are nontrivial; rank 1 only for the endpoint pair {1,W_P}
bridge_obstruction=the raw support kernel has no reciprocal inverse phase and is not itself a Kloosterman/trace-function input
```

## 2. Radial two-cylinder 审计

```text
max_prime=1009
P_value_count=165
pair_count_total=32554
rank_one_endpoint_pair_total=165
rank_two_nontrivial_pair_total=32389
max_complementary_pair_count=1024
max_rank_two_nontrivial_pair_count=1023
radial_bad_total=0
reciprocal_phase_present_total=0
all_pair_kernels_unit_orbit_radial=true
all_nonendpoint_pairs_rank_two=true
direct_kloosterman_trace_input_available_for_any_pair=false
previous_pair_count_total=32554
previous_identity_zero_pair_total=0
```

代表 P：

| P | W_P | sqrt_sieve_prime_count | complementary_pair_count | rank_one_endpoint_pair_count | rank_two_nontrivial_pair_count | radial_bad_count | reciprocal_phase_present_count | sample_pairs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 210 | 4 | 8 | 1 | 7 | 0 | 0 | {'q': 1, 'q_complement': 210, 'q_prime_count': 0, 'complement_prime_count': 4, 'row_state_count': 1, 'column_state_count': 16, 'q_cylinder_value_count': 1, 'complement_cylinder_value_count': 16, 'q_cylinder_value_range': '1..1', 'complement_cylinder_value_range': '-1..1', 'two_cylinder_matrix_rank': 1, 'endpoint_pair_rank_one': True, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 2, 'q_complement': 105, 'q_prime_count': 1, 'complement_prime_count': 3, 'row_state_count': 2, 'column_state_count': 8, 'q_cylinder_value_count': 2, 'complement_cylinder_value_count': 8, 'q_cylinder_value_range': '-1..1', 'complement_cylinder_value_range': '-1/2..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 6, 'q_complement': 35, 'q_prime_count': 2, 'complement_prime_count': 2, 'row_state_count': 4, 'column_state_count': 4, 'q_cylinder_value_count': 4, 'complement_cylinder_value_count': 4, 'q_cylinder_value_range': '-1..1', 'complement_cylinder_value_range': '-1/4..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 14, 'q_complement': 15, 'q_prime_count': 2, 'complement_prime_count': 2, 'row_state_count': 4, 'column_state_count': 4, 'q_cylinder_value_count': 4, 'complement_cylinder_value_count': 4, 'q_cylinder_value_range': '-1..1', 'complement_cylinder_value_range': '-1/2..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} |
| 257 | 30030 | 6 | 32 | 1 | 31 | 0 | 0 | {'q': 1, 'q_complement': 30030, 'q_prime_count': 0, 'complement_prime_count': 6, 'row_state_count': 1, 'column_state_count': 64, 'q_cylinder_value_count': 1, 'complement_cylinder_value_count': 52, 'q_cylinder_value_range': '1..1', 'complement_cylinder_value_range': '-1..1', 'two_cylinder_matrix_rank': 1, 'endpoint_pair_rank_one': True, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 2, 'q_complement': 15015, 'q_prime_count': 1, 'complement_prime_count': 5, 'row_state_count': 2, 'column_state_count': 32, 'q_cylinder_value_count': 2, 'complement_cylinder_value_count': 30, 'q_cylinder_value_range': '-1..1', 'complement_cylinder_value_range': '-1/2..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 35, 'q_complement': 858, 'q_prime_count': 2, 'complement_prime_count': 4, 'row_state_count': 4, 'column_state_count': 16, 'q_cylinder_value_count': 4, 'complement_cylinder_value_count': 16, 'q_cylinder_value_range': '-1/4..1', 'complement_cylinder_value_range': '-1..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 165, 'q_complement': 182, 'q_prime_count': 3, 'complement_prime_count': 3, 'row_state_count': 8, 'column_state_count': 8, 'q_cylinder_value_count': 8, 'complement_cylinder_value_count': 8, 'q_cylinder_value_range': '-1/2..1', 'complement_cylinder_value_range': '-1..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} |
| 971 | 200560490130 | 11 | 1024 | 1 | 1023 | 0 | 0 | {'q': 1, 'q_complement': 200560490130, 'q_prime_count': 0, 'complement_prime_count': 11, 'row_state_count': 1, 'column_state_count': 2048, 'q_cylinder_value_count': 1, 'complement_cylinder_value_count': 1152, 'q_cylinder_value_range': '1..1', 'complement_cylinder_value_range': '-1..1', 'two_cylinder_matrix_rank': 1, 'endpoint_pair_rank_one': True, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 2, 'q_complement': 100280245065, 'q_prime_count': 1, 'complement_prime_count': 10, 'row_state_count': 2, 'column_state_count': 1024, 'q_cylinder_value_count': 2, 'complement_cylinder_value_count': 752, 'q_cylinder_value_range': '-1..1', 'complement_cylinder_value_range': '-1/2..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 24738, 'q_complement': 8107385, 'q_prime_count': 5, 'complement_prime_count': 6, 'row_state_count': 32, 'column_state_count': 64, 'q_cylinder_value_count': 32, 'complement_cylinder_value_count': 64, 'q_cylinder_value_range': '-1..1', 'complement_cylinder_value_range': '-1/4..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 447051, 'q_complement': 448630, 'q_prime_count': 5, 'complement_prime_count': 6, 'row_state_count': 32, 'column_state_count': 64, 'q_cylinder_value_count': 32, 'complement_cylinder_value_count': 64, 'q_cylinder_value_range': '-1/2..1', 'complement_cylinder_value_range': '-1..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} |
| 1009 | 200560490130 | 11 | 1024 | 1 | 1023 | 0 | 0 | {'q': 1, 'q_complement': 200560490130, 'q_prime_count': 0, 'complement_prime_count': 11, 'row_state_count': 1, 'column_state_count': 2048, 'q_cylinder_value_count': 1, 'complement_cylinder_value_count': 1152, 'q_cylinder_value_range': '1..1', 'complement_cylinder_value_range': '-1..1', 'two_cylinder_matrix_rank': 1, 'endpoint_pair_rank_one': True, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 2, 'q_complement': 100280245065, 'q_prime_count': 1, 'complement_prime_count': 10, 'row_state_count': 2, 'column_state_count': 1024, 'q_cylinder_value_count': 2, 'complement_cylinder_value_count': 752, 'q_cylinder_value_range': '-1..1', 'complement_cylinder_value_range': '-1/2..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 24738, 'q_complement': 8107385, 'q_prime_count': 5, 'complement_prime_count': 6, 'row_state_count': 32, 'column_state_count': 64, 'q_cylinder_value_count': 32, 'complement_cylinder_value_count': 64, 'q_cylinder_value_range': '-1..1', 'complement_cylinder_value_range': '-1/4..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} / {'q': 447051, 'q_complement': 448630, 'q_prime_count': 5, 'complement_prime_count': 6, 'row_state_count': 32, 'column_state_count': 64, 'q_cylinder_value_count': 32, 'complement_cylinder_value_count': 64, 'q_cylinder_value_range': '-1/2..1', 'complement_cylinder_value_range': '-1..1', 'two_cylinder_matrix_rank': 2, 'endpoint_pair_rank_one': False, 'unit_orbit_radial': True, 'depends_only_on_gcd_with_W': True, 'reciprocal_inverse_phase_present': False, 'direct_kloosterman_trace_input_available': False} |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ComplementaryPairLocalRamanujanTensorNormalForm | true | true | Every complementary pair kernel has the exact local product sum K_q(n)=mu(q)prod rho_l + mu(W/q)prod rho_l. | none |
| ComplementaryPairUnitOrbitRadiality | true | true | The pair kernel depends only on gcd(n,W_P) and is invariant under multiplication by units modulo W_P. | none |
| ComplementaryPairTwoCylinderRankLedger | true | true | Non-endpoint complementary pairs have exact two-cylinder matrix rank 2; the endpoint pair has rank 1. | none |
| DirectKloostermanTraceInputFromPairKernelRejected | true | true | The raw pair kernel contains no reciprocal inverse phase and cannot be directly fed to Kloosterman/trace bilinear theorems. | none |
| ComplementaryConductorPairPhaseMatchingOrTraceFamilyBridge | false | false | Introduce a genuine same-object reciprocal/trace phase coupled to the radial pair kernels. | new phase-matching bridge theorem |
| UniformCancellationAcrossComplementaryPrimorialConductorPairs | false | false | Prove uniform cancellation after the phase bridge, across all dynamic primorial complementary pairs. | new pair-uniform cancellation theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3=requires an l-adic trace-function family with suitable monodromy; the radial divisor-lattice kernel alone is not such a packaged input
Milicevic_Qin_Wu_2025_arXiv_2511_07550=requires genuine Kloosterman sums modulo q and bilinear coefficient ranges; no reciprocal inverse phase is present in the raw pair kernel
Pascadi_2025_arXiv_2511_08445=composite-modulus non-abelian amplification needs Type-II Kloosterman organisation, not only a radial gcd kernel
Wright_2026_arXiv_2604_25177=unbalanced Kloosterman-fraction convolution becomes relevant only after the radial kernel is coupled to a completed reciprocal phase
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=squarefree/smooth modulus sums are adjacent to W_P but do not by themselves supply the missing phase matching
Dong_Robles_Zeindler_2026_arXiv_2601_00292=withdrawn and remains unusable as a closing input
```

结论：互补配对核已经完全压成 radial two-cylinder divisor-lattice 函数。它保留结构信息，但自身没有 reciprocal inverse phase；因此不能直接调用 Kloosterman/trace-function 外部定理。

## 5. 最新最窄口

```text
RadialPairKernelToReciprocalTracePhaseCouplingBridge
AND UniformCancellationAcrossComplementaryPrimorialConductorPairsAfterCoupling
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
complementary_pair_local_tensor_normal_form_closed=true
complementary_pair_unit_orbit_radiality_closed=true
complementary_pair_two_cylinder_rank_ledger_closed=true
direct_kloosterman_trace_input_from_pair_kernel_rejected=true
radial_pair_to_reciprocal_trace_phase_bridge_closed=false
uniform_complementary_pair_cancellation_after_coupling_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
