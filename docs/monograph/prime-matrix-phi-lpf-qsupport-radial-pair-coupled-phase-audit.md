# Prime Matrix Phi-LPF q-support radial pair coupled phase 审计

**状态：** `radial_pair_coupled_floor_reciprocal_phase_normal_form_closed_trace_bridge_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
fixed_cofactor=m=r*beta, with r>=7 prime and beta r-rough
floor_denominator=Q_{P,k}(m)=least odd integer in [max(P/2+1,floor(kP/m)+1), min(P-1,m,floor(((k+1)P-1)/m))]
paired_selector=1_{gcd(Q,W_P)=1}=phi(W_P)/W_P * sum_{unordered {d,W_P/d}} K_d(Q)
coupled_phase=each selected atom carries e(h*k*P/Q_{P,k}(m))
normal_form=sum over residual m of paired radial Ramanujan selector times floor-reciprocal phase
remaining_obstruction=Q_{P,k}(m) is a floor-defined denominator and not a completed trace/Kloosterman variable
```

## 2. Coupled phase 审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_actual_phase_atoms=299977
total_coupled_selected_phase_atoms=299977
actual_phase_atoms_equal_coupled_phase_atoms=true
missing_actual_phase_atoms_total=0
extra_coupled_phase_atoms_total=0
windows_with_odd_candidate_total=951378
local_coupled_identity_checked_total=951378
local_coupled_identity_mismatch_total=0
paired_kernel_identity_sample_checked_total=27
paired_kernel_identity_sample_mismatch_total=0
bad_selected_denominator_not_prime_total=0
max_complementary_pair_kernels_per_candidate=1024
max_full_ramanujan_divisor_terms_per_candidate=2048
max_full_additive_modes_per_candidate=200560490130
phase_denominator_is_floor_defined_Q_odd=true
direct_trace_or_kloosterman_family_available=false
```

代表 P：

| P | k | actual_phase_atoms | coupled_selected_phase_atoms | windows_with_odd_candidate | local_coupled_identity_checked | paired_kernel_identity_sample_checked | paired_kernel_identity_sample_mismatch | complementary_pair_kernels_per_candidate | sample_pair_kernel_values | sample_phase_atoms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 1 | 1 | 3 | 3 | 3 | 0 | 8 | m=119,Q=85,expected=0,paired=0,phase=e(h*100*101/85); m=143,Q=71,expected=1,paired=1,phase=e(h*100*101/71); m=161,Q=63,expected=0,paired=0,phase=e(h*100*101/63) | q=71,m=143,r=11,beta=13,phase=e(h*100*101/71),QmodW=71 |
| 257 | 256 | 3 | 3 | 8 | 8 | 8 | 0 | 32 | m=259,Q=255,expected=0,paired=0,phase=e(h*256*257/255); m=301,Q=219,expected=0,paired=0,phase=e(h*256*257/219); m=319,Q=207,expected=0,paired=0,phase=e(h*256*257/207); m=341,Q=193,expected=1,paired=1,phase=e(h*256*257/193); m=377,Q=175,expected=0,paired=0,phase=e(h*256*257/175); m=437,Q=151,expected=1,paired=1,phase=e(h*256*257/151); m=481,Q=137,expected=1,paired=1,phase=e(h*256*257/137); m=511,Q=129,expected=0,paired=0,phase=e(h*256*257/129) | q=193,m=341,r=11,beta=31,phase=e(h*256*257/193),QmodW=193; q=151,m=437,r=19,beta=23,phase=e(h*256*257/151),QmodW=151; q=137,m=481,r=13,beta=37,phase=e(h*256*257/137),QmodW=137 |
| 971 | 936 | 23 | 23 | 49 | 49 | 8 | 0 | 1024 | m=973,Q=935,expected=0,paired=0,phase=e(h*936*971/935); m=979,Q=929,expected=1,paired=1,phase=e(h*936*971/929); m=989,Q=919,expected=1,paired=1,phase=e(h*936*971/919); m=1003,Q=907,expected=1,paired=1,phase=e(h*936*971/907); m=1007,Q=903,expected=0,paired=0,phase=e(h*936*971/903); m=1027,Q=885,expected=0,paired=0,phase=e(h*936*971/885); m=1037,Q=877,expected=1,paired=1,phase=e(h*936*971/877); m=1079,Q=843,expected=0,paired=0,phase=e(h*936*971/843) | q=929,m=979,r=11,beta=89,phase=e(h*936*971/929),QmodW=929; q=919,m=989,r=23,beta=43,phase=e(h*936*971/919),QmodW=919; q=907,m=1003,r=17,beta=59,phase=e(h*936*971/907),QmodW=907; q=877,m=1037,r=17,beta=61,phase=e(h*936*971/877),QmodW=877; q=827,m=1099,r=7,beta=157,phase=e(h*936*971/827),QmodW=827 |
| 1009 | 1008 | 9 | 9 | 51 | 51 | 8 | 0 | 1024 | m=1027,Q=991,expected=1,paired=1,phase=e(h*1008*1009/991); m=1037,Q=981,expected=0,paired=0,phase=e(h*1008*1009/981); m=1057,Q=963,expected=0,paired=0,phase=e(h*1008*1009/963); m=1079,Q=943,expected=0,paired=0,phase=e(h*1008*1009/943); m=1081,Q=941,expected=1,paired=1,phase=e(h*1008*1009/941); m=1127,Q=903,expected=0,paired=0,phase=e(h*1008*1009/903); m=1139,Q=893,expected=0,paired=0,phase=e(h*1008*1009/893); m=1147,Q=887,expected=1,paired=1,phase=e(h*1008*1009/887) | q=991,m=1027,r=13,beta=79,phase=e(h*1008*1009/991),QmodW=991; q=941,m=1081,r=23,beta=47,phase=e(h*1008*1009/941),QmodW=941; q=887,m=1147,r=31,beta=37,phase=e(h*1008*1009/887),QmodW=887; q=761,m=1337,r=7,beta=191,phase=e(h*1008*1009/761),QmodW=761; q=743,m=1369,r=37,beta=37,phase=e(h*1008*1009/743),QmodW=743 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RadialPairKernelToActualReciprocalPhaseCouplingNormalForm | true | true | The actual phase atoms equal the residual-cofactor sum with paired radial Ramanujan selector and phase e(hkP/Q_{P,k}(m)). | none |
| ComplementaryPairGroupedRamanujanSelectorIdentity | true | true | The dynamic primorial unit selector is exactly the sum over unordered complementary conductor pair kernels. | none |
| FloorDenominatorPhaseLedger | true | true | The denominator coupled to the phase is the unique odd floor-map Q_{P,k}(m). | none |
| DirectTraceFamilyFromCoupledFloorRadialPhaseRejected | true | true | The coupled normal form still has a floor-defined real reciprocal denominator, not a completed Kloosterman/trace-family variable. | none |
| FloorRadialReciprocalPhaseToTraceFamilyBridge | false | false | Convert the floor-radial reciprocal phase into a same-object trace/Kloosterman or Type-II family. | new completion bridge theorem |
| UniformCancellationAcrossCoupledFloorRadialPairKernels | false | false | Prove cancellation uniformly across the coupled pair kernels after a valid completion bridge. | new phase-saving theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459_v3=could apply only after the floor-radial phase is packaged as an l-adic trace family
Milicevic_Qin_Wu_2025_arXiv_2511_07550=could apply only after producing genuine Kloosterman sums with bilinear ranges from Q_{P,k}(m)
Pascadi_2025_arXiv_2511_08445=needs a composite-modulus Type-II Kloosterman organisation, not just the floor denominator normal form
Wright_2026_arXiv_2604_25177=unbalanced convolution is relevant only after converting the floor map to an AP/convolution discrepancy with SW input
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=squarefree/smooth parameter estimates remain adjacent because W_P is squarefree/smooth, but no completed phase has been produced
Dong_Robles_Zeindler_2026_arXiv_2601_00292=withdrawn and unusable as a closing input
```

结论：actual q-support phase 已经和互补 radial pair kernel 精确耦合；剩余不是“是否耦合”，而是 floor-radial real reciprocal phase 能否完成为同对象 trace/Kloosterman/Type-II family。

## 5. 最新最窄口

```text
FloorRadialReciprocalPhaseToTraceFamilyBridge
AND UniformCancellationAcrossCoupledFloorRadialPairKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
radial_pair_coupled_phase_normal_form_closed=true
complementary_pair_grouped_ramanujan_selector_identity_closed=true
floor_denominator_phase_ledger_closed=true
direct_trace_family_from_coupled_floor_radial_phase_rejected=true
floor_radial_reciprocal_phase_to_trace_family_bridge_closed=false
uniform_cancellation_across_coupled_floor_radial_pair_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
