# Prime Matrix Phi-LPF q-support floor-cell radial support 审计

**状态：** `floor_cell_radial_support_normal_form_closed_completion_bridge_open`
**核验日期：** `2026-05-23`

## 1. 当前对象

```text
reverse_denominator=Q_{P,k}(m)=least odd integer in [max(P/2+1,floor(kP/m)+1), min(P-1,m,floor(((k+1)P-1)/m))]
forward_floor_cell=I_{P,k}(q)=[max(P/2+1,q,floor(kP/q)+1), min(2P-1,floor(((k+1)P-1)/q))]
cell_equivalence=Q_{P,k}(m)=q iff m in I_{P,k}(q), q odd, and m is the residual rough cofactor
selected_atom=1_{gcd(q,W_P)=1} * 1_{m in I_{P,k}(q)} * e(h*k*P/q)
radial_support=the paired Ramanujan/radial selector is evaluated at the same q coordinate, not at a new completed variable
remaining_obstruction=floor cells reconstruct the support exactly, but no cancellation or completed trace family is produced
```

## 2. Floor-cell 审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_actual_phase_atoms=299977
total_floor_cell_selected_terms=299977
total_reverse_selected_terms=299977
total_product_cell_residual_atoms=951378
total_reverse_odd_residual_atoms=951378
floor_cell_terms_equal_actual_phase_atoms=true
floor_cell_terms_equal_reverse_selected_terms=true
product_cell_atoms_equal_reverse_odd_atoms=true
product_cell_to_reverse_mismatch_total=0
reverse_to_product_cell_mismatch_total=0
bad_product_cell_window_size_total=0
bad_product_cell_odd_count_total=0
bad_reverse_window_size_total=0
bad_reverse_odd_count_total=0
bad_unit_q_not_prime_total=0
q_floor_cells_checked_total=12532624
max_product_cell_window_size=2
max_product_cell_odd_count=1
max_reverse_window_size=2
max_reverse_odd_count=1
floor_cell_denominator_is_original_prime_q_coordinate=true
completed_trace_or_kloosterman_family_available=false
```

代表 P：

| P | k | actual_phase_atoms | floor_cell_selected_terms | reverse_selected_terms | product_cell_residual_atoms | reverse_odd_residual_atoms | product_cell_to_reverse_checked | reverse_to_product_cell_checked | bad_unit_q_not_prime | sample_floor_cells |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 1 | 1 | 1 | 3 | 3 | 3 | 3 | 0 | q=71,m=143,r=11,beta=13,I_q=[143,143],phase=e(h*100*101/71),qmodW=71 |
| 257 | 256 | 3 | 3 | 3 | 8 | 8 | 8 | 8 | 0 | q=137,m=481,r=13,beta=37,I_q=[481,482],phase=e(h*256*257/137),qmodW=137; q=151,m=437,r=19,beta=23,I_q=[436,437],phase=e(h*256*257/151),qmodW=151; q=193,m=341,r=11,beta=31,I_q=[341,342],phase=e(h*256*257/193),qmodW=193 |
| 971 | 936 | 23 | 23 | 23 | 49 | 49 | 49 | 49 | 0 | q=491,m=1853,r=17,beta=109,I_q=[1852,1853],phase=e(h*936*971/491),qmodW=491; q=503,m=1807,r=13,beta=139,I_q=[1807,1808],phase=e(h*936*971/503),qmodW=503; q=523,m=1739,r=37,beta=47,I_q=[1738,1739],phase=e(h*936*971/523),qmodW=523; q=541,m=1681,r=41,beta=41,I_q=[1680,1681],phase=e(h*936*971/541),qmodW=541; q=557,m=1633,r=23,beta=71,I_q=[1632,1633],phase=e(h*936*971/557),qmodW=557; q=601,m=1513,r=17,beta=89,I_q=[1513,1513],phase=e(h*936*971/601),qmodW=601; q=619,m=1469,r=13,beta=113,I_q=[1469,1469],phase=e(h*936*971/619),qmodW=619; q=631,m=1441,r=11,beta=131,I_q=[1441,1441],phase=e(h*936*971/631),qmodW=631 |
| 1009 | 1008 | 9 | 9 | 9 | 51 | 51 | 51 | 51 | 0 | q=563,m=1807,r=13,beta=139,I_q=[1807,1808],phase=e(h*1008*1009/563),qmodW=563; q=577,m=1763,r=41,beta=43,I_q=[1763,1764],phase=e(h*1008*1009/577),qmodW=577; q=617,m=1649,r=17,beta=97,I_q=[1649,1650],phase=e(h*1008*1009/617),qmodW=617; q=647,m=1573,r=11,beta=143,I_q=[1572,1573],phase=e(h*1008*1009/647),qmodW=647; q=743,m=1369,r=37,beta=37,I_q=[1369,1370],phase=e(h*1008*1009/743),qmodW=743; q=761,m=1337,r=7,beta=191,I_q=[1337,1337],phase=e(h*1008*1009/761),qmodW=761; q=887,m=1147,r=31,beta=37,I_q=[1147,1147],phase=e(h*1008*1009/887),qmodW=887; q=941,m=1081,r=23,beta=47,I_q=[1081,1081],phase=e(h*1008*1009/941),qmodW=941 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FloorDenominatorCellDecompositionNormalForm | true | true | The reverse denominator condition Q_{P,k}(m)=q is exactly the forward product-floor cell condition on m. | none |
| ReverseForwardFloorCellEquivalence | true | true | Every residual odd q-cell atom matches the reverse floor denominator atom, and conversely. | none |
| FloorCellRadialSupportExactReconstruction | true | true | After the W_P unit selector, the floor-cell support equals both the actual prime-q phase support and the coupled reverse support. | none |
| FloorCellToCompletedTraceFamilyBridge | false | false | Convert the exact floor cells with radial pair kernels into a completed trace/Kloosterman or Type-II family. | new completion bridge theorem |
| UniformCancellationAcrossFloorCellsWithRadialPairKernels | false | false | Prove phase saving uniformly over the exact floor cells and all coupled radial pair kernels. | new phase-saving theorem |

## 4. 外部 theorem 影响

```text
Fouvry_Kowalski_Michel_Sawin_2025_arXiv_2511_09459=still needs a trace-function family after the floor cells are completed; the present cell identity is deterministic only
Milicevic_Qin_Wu_2025_arXiv_2511_07550=requires genuine bilinear Kloosterman sums, while the current object is an exact short floor-cell support
Pascadi_2025_arXiv_2511_08445=could help only after a composite-modulus Type-II organisation is built from the cells
Wright_2026_arXiv_2604_25177=relevant only after the floor-cell discrepancy is converted into an unbalanced Kloosterman-fraction convolution
Shao_Shparlinski_Wijaya_2024_arXiv_2411_12113=squarefree/smooth-modulus estimates remain adjacent to W_P but do not directly estimate the real reciprocal phase e(hkP/q)
Dong_Robles_Zeindler_2026_arXiv_2601_00292=withdrawn and not used as a closing input
```

结论：floor denominator 已被压回正向 q-cell 支撑；这排除了“floor 变量本身就是新完成相位”的误读，但也确认下一步必须证明完成桥和相消，而不能只在等价正规形之间循环。

## 5. 最新最窄口

```text
FloorCellRadialSupportToCompletedTraceFamilyBridge
AND UniformCancellationAcrossFloorCellsWithRadialPairKernels
AND RoughBetaSiegelWalfiszUniformityOrReplacement
AND PointwisePKUniformTransferFromExternalAverageEstimate
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
floor_denominator_cell_decomposition_closed=true
reverse_forward_floor_cell_equivalence_closed=true
floor_cell_radial_support_exact_reconstruction_closed=true
floor_cell_to_completed_trace_family_bridge_closed=false
uniform_cancellation_across_floor_cells_with_radial_pair_kernels_closed=false
rough_beta_siegel_walfisz_factor_extracted=false
pointwise_pk_transfer_closed=false
q_support_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
