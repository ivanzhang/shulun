# Prime Matrix Phi-LPF q-support row-averaged additive-k support 审计

**状态：** `additive_k_character_relabeling_closed_sparse_k_support_completion_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
phase_relabeling=D=qm-kP gives D == -kP (mod q), hence e(-hD/q)=e(hPk/q)
character_modulus=q
character_variable=k mod q
support=k=floor(qm/P) for residual LPF cofactors m in the selected q-bucket
remaining_obstruction=the q-bucket k-support is sparse and generally not a complete interval
```

## 2. additive-k 支撑审计

```text
max_prime=1009
P_value_count=165
total_selected_edges=299977
previous_row_averaged_selected_edges=299977
selected_edges_match_previous_total=true
selected_q_bucket_count_total=6020
phase_congruence_checked_total=299977
phase_congruence_mismatch_total=0
floor_cell_membership_mismatch_total=0
floor_cell_odd_candidate_mismatch_total=0
bad_floor_cell_odd_count_total=0
bad_zero_displacement_total=0
max_q_to_k_fiber=192
max_q_to_kmod_fiber=174
q_buckets_with_kmod_collision_total=1237
total_kmod_collision_edges=6664
first_kmod_collision=P=71,q=37,k=62,kmod=25
q_buckets_with_noncomplete_k_interval_total=5920
total_k_support_count=299977
total_k_span_length=1602928
total_k_interval_holes=1302951
max_k_support_count_per_q=192
max_k_span_length_per_q=748
max_k_interval_holes_per_q=556
first_noncomplete_k_support=P=43,q=23,min_k=26,max_k=41,count=2,span=16,holes=14
additive_character_phase_relabeling_closed=true
complete_interval_additive_character_sum_available=false
sparse_lpf_k_support_completion_closed=false
```

代表 P：

| P | selected_edges | selected_q_bucket_count | phase_congruence_mismatch | max_q_to_k_fiber | q_buckets_with_noncomplete_k_interval | total_k_interval_holes | max_k_interval_holes_per_q | first_noncomplete_k_support | sample_edges |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 48 | 9 | 0 | 9 | 8 | 302 | 50 | q=53,min_k=40,max_k=98,count=9,span=59,holes=50 | q=53,m=77,r=7,beta=11,k=40,D=41,Dmodq=41,-kPmodq=41,phase=e(h*48*k/53); q=53,m=91,r=7,beta=13,k=47,D=76,Dmodq=23,-kPmodq=23,phase=e(h*48*k/53); q=53,m=119,r=7,beta=17,k=62,D=45,Dmodq=45,-kPmodq=45,phase=e(h*48*k/53); q=53,m=121,r=11,beta=11,k=63,D=50,Dmodq=50,-kPmodq=50,phase=e(h*48*k/53); q=53,m=133,r=7,beta=19,k=69,D=80,Dmodq=27,-kPmodq=27,phase=e(h*48*k/53); q=53,m=143,r=11,beta=13,k=75,D=4,Dmodq=4,-kPmodq=4,phase=e(h*48*k/53); q=53,m=161,r=7,beta=23,k=84,D=49,Dmodq=49,-kPmodq=49,phase=e(h*48*k/53); q=53,m=169,r=13,beta=13,k=88,D=69,Dmodq=16,-kPmodq=16,phase=e(h*48*k/53) |
| 257 | 377 | 23 | 0 | 36 | 23 | 1948 | 151 | q=131,min_k=67,max_k=253,count=36,span=187,holes=151 | q=131,m=133,r=7,beta=19,k=67,D=204,Dmodq=73,-kPmodq=73,phase=e(h*126*k/131); q=131,m=143,r=11,beta=13,k=72,D=229,Dmodq=98,-kPmodq=98,phase=e(h*126*k/131); q=131,m=161,r=7,beta=23,k=82,D=17,Dmodq=17,-kPmodq=17,phase=e(h*126*k/131); q=131,m=169,r=13,beta=13,k=86,D=37,Dmodq=37,-kPmodq=37,phase=e(h*126*k/131); q=131,m=187,r=11,beta=17,k=95,D=82,Dmodq=82,-kPmodq=82,phase=e(h*126*k/131); q=131,m=203,r=7,beta=29,k=103,D=122,Dmodq=122,-kPmodq=122,phase=e(h*126*k/131); q=131,m=209,r=11,beta=19,k=106,D=137,Dmodq=6,-kPmodq=6,phase=e(h*126*k/131); q=131,m=217,r=7,beta=31,k=110,D=157,Dmodq=26,-kPmodq=26,phase=e(h*126*k/131) |
| 971 | 5672 | 71 | 0 | 184 | 70 | 23383 | 540 | q=487,min_k=247,max_k=966,count=184,span=720,holes=536 | q=487,m=493,r=17,beta=29,k=247,D=254,Dmodq=254,-kPmodq=254,phase=e(h*484*k/487); q=487,m=497,r=7,beta=71,k=249,D=260,Dmodq=260,-kPmodq=260,phase=e(h*484*k/487); q=487,m=511,r=7,beta=73,k=256,D=281,Dmodq=281,-kPmodq=281,phase=e(h*484*k/487); q=487,m=517,r=11,beta=47,k=259,D=290,Dmodq=290,-kPmodq=290,phase=e(h*484*k/487); q=487,m=527,r=17,beta=31,k=264,D=305,Dmodq=305,-kPmodq=305,phase=e(h*484*k/487); q=487,m=529,r=23,beta=23,k=265,D=308,Dmodq=308,-kPmodq=308,phase=e(h*484*k/487); q=487,m=533,r=13,beta=41,k=267,D=314,Dmodq=314,-kPmodq=314,phase=e(h*484*k/487); q=487,m=539,r=7,beta=77,k=270,D=323,Dmodq=323,-kPmodq=323,phase=e(h*484*k/487) |
| 1009 | 5901 | 72 | 0 | 192 | 72 | 24457 | 556 | q=509,min_k=257,max_k=1004,count=192,span=748,holes=556 | q=509,m=511,r=7,beta=73,k=257,D=786,Dmodq=277,-kPmodq=277,phase=e(h*500*k/509); q=509,m=517,r=11,beta=47,k=260,D=813,Dmodq=304,-kPmodq=304,phase=e(h*500*k/509); q=509,m=527,r=17,beta=31,k=265,D=858,Dmodq=349,-kPmodq=349,phase=e(h*500*k/509); q=509,m=529,r=23,beta=23,k=266,D=867,Dmodq=358,-kPmodq=358,phase=e(h*500*k/509); q=509,m=533,r=13,beta=41,k=268,D=885,Dmodq=376,-kPmodq=376,phase=e(h*500*k/509); q=509,m=539,r=7,beta=77,k=271,D=912,Dmodq=403,-kPmodq=403,phase=e(h*500*k/509); q=509,m=551,r=19,beta=29,k=277,D=966,Dmodq=457,-kPmodq=457,phase=e(h*500*k/509); q=509,m=553,r=7,beta=79,k=278,D=975,Dmodq=466,-kPmodq=466,phase=e(h*500*k/509) |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| MixedModulusPhaseToKAdditiveCharacterRelabeling | true | true | The row-averaged phase can be written as a q-modulus additive character in k. | none |
| RowAveragedSelectedEdgeConsistency | true | true | The additive-k support contains exactly the previously audited row-averaged selected edges. | none |
| DirectCompleteIntervalAdditiveCharacterCompletionRejected | true | true | The k-support in q-buckets is sparse and not a complete interval, so complete interval additive-character cancellation is not directly available. | none |
| SparseLPFKSupportCompletionOrDispersion | false | false | Complete or estimate the sparse LPF-induced k-support without changing the object. | new sparse-support dispersion theorem |
| UniformCancellationAcrossSparseKSupportRadialKernels | false | false | Prove cancellation uniformly across the sparse k-support and coupled radial kernels. | new phase-saving theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459=the phase is now an additive character in k mod q, but the support is an LPF-induced sparse set rather than a standard trace-family interval
Milicevic_Qin_Wu_2025_arXiv_2511_07550=Kloosterman bilinear estimates still need a bilinear/convolution support; the current k-support is sparse and graph-defined
Pascadi_2025_arXiv_2511_08445=composite Type-II amplification remains downstream of a sparse-support completion theorem
Wright_2026_arXiv_2604_25177=unbalanced convolution estimates are relevant only after the sparse k-support is converted into a controlled convolution family
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=smooth/squarefree parameter inputs do not by themselves remove the LPF-induced k-support holes
```

结论：混合模数相位可重标记为 `k mod q` 的加性角色，这是推进；但 q-bucket 内的 k 支撑由 LPF residual 集诱导，存在大量区间孔洞。下一步真口不是相位重标记，而是 sparse LPF k-support 的 completion/dispersion。

## 5. 最新最窄口

```text
SparseLPFKSupportCompletionOrDispersion
AND UniformCancellationAcrossSparseKSupportRadialKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
mixed_modulus_phase_to_k_additive_character_relabeling_closed=true
row_averaged_selected_edge_consistency_closed=true
direct_complete_interval_additive_character_completion_rejected=true
sparse_lpf_k_support_completion_or_dispersion_closed=false
uniform_cancellation_across_sparse_k_support_radial_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
