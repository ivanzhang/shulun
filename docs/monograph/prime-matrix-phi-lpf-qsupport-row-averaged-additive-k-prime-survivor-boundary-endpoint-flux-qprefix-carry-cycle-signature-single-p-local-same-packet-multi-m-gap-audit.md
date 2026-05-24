# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local same-packet multi-m gap 审计

**状态：** `single_p_local_same_packet_multi_m_gap_ledger_closed_uniform_bound_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=the 78 single-P repeated templates whose occurrences stay in one packet but use multiple m-values
operation=classify selected m-values by integer gaps and prime-index gaps
dominant_shape=adjacent prime-pair collisions carry almost all same-packet multi-m mass
remaining=prove local adjacent-prime-pair collision bounds or route excess to PDEC/SAE
```

## 2. same-packet multi-m gap 分类审计

```text
max_prime=1009
single_P_local_same_packet_multi_m_gap_ledger_closed=true
same_packet_multi_m_template_count=78
same_packet_multi_m_edge_mass=720
adjacent_prime_pair_collision_template_count=71
adjacent_prime_pair_collision_edge_mass=662
nonadjacent_prime_pair_collision_template_count=6
nonadjacent_prime_pair_collision_edge_mass=50
adjacent_prime_chain_collision_template_count=1
adjacent_prime_chain_collision_edge_mass=8
bad_same_packet_template_count=0
same_packet_multi_m_occurrence_count_max=4
same_packet_multi_m_selected_m_support_count_max=4
same_packet_multi_m_prime_index_gap_max=3
same_packet_multi_m_integer_gap_max=18
observed_same_packet_multi_m_prime_index_gap_le_3=true
observed_same_packet_multi_m_selected_support_le_4=true
observed_same_packet_multi_m_occurrence_count_le_4=true
observed_adjacent_prime_pair_dominant=true
row_column_unconditional_closed=false
```

same-packet gap class template count：

| same_packet_gap_class | template_count | template_ratio |
| --- | --- | --- |
| adjacent_prime_pair_collision | 71 | 0.9102564102564102 |
| nonadjacent_prime_pair_collision | 6 | 0.07692307692307693 |
| adjacent_prime_chain_collision | 1 | 0.01282051282051282 |

same-packet gap class edge mass：

| same_packet_gap_class | edge_mass | edge_ratio |
| --- | --- | --- |
| adjacent_prime_pair_collision | 662 | 0.9194444444444444 |
| nonadjacent_prime_pair_collision | 50 | 0.06944444444444445 |
| adjacent_prime_chain_collision | 8 | 0.011111111111111112 |

same-packet gap class route edge mass：

| same_packet_gap_class | route_class | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| adjacent_prime_pair_collision | pure_right_tail_two_sided_collar | 288 | 0.4 |
| adjacent_prime_pair_collision | pure_upper_wing_single_shell | 260 | 0.3611111111111111 |
| adjacent_prime_pair_collision | pure_lower_wing_single_shell | 84 | 0.11666666666666667 |
| adjacent_prime_pair_collision | pure_right_tail_left_collar | 30 | 0.041666666666666664 |
| nonadjacent_prime_pair_collision | pure_right_tail_two_sided_collar | 26 | 0.03611111111111111 |
| nonadjacent_prime_pair_collision | pure_upper_wing_single_shell | 14 | 0.019444444444444445 |
| nonadjacent_prime_pair_collision | pure_right_tail_right_collar | 10 | 0.013888888888888888 |
| adjacent_prime_chain_collision | pure_upper_wing_single_shell | 8 | 0.011111111111111112 |

integer m-gap vector rows：

| integer_gap_vector | template_count | template_ratio | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| [4] | 31 | 0.3974358974358974 | 316 | 0.4388888888888889 |
| [2] | 33 | 0.4230769230769231 | 296 | 0.4111111111111111 |
| [6] | 8 | 0.10256410256410256 | 60 | 0.08333333333333333 |
| [8] | 3 | 0.038461538461538464 | 26 | 0.03611111111111111 |
| [4, 2, 4] | 1 | 0.01282051282051282 | 8 | 0.011111111111111112 |
| [10] | 1 | 0.01282051282051282 | 8 | 0.011111111111111112 |
| [18] | 1 | 0.01282051282051282 | 6 | 0.008333333333333333 |

prime-index gap vector rows：

| prime_index_gap_vector | template_count | template_ratio | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| [1] | 71 | 0.9102564102564102 | 662 | 0.9194444444444444 |
| [2] | 5 | 0.0641025641025641 | 44 | 0.06111111111111111 |
| [1, 1, 1] | 1 | 0.01282051282051282 | 8 | 0.011111111111111112 |
| [3] | 1 | 0.01282051282051282 | 6 | 0.008333333333333333 |

occurrence count edge mass：

| occurrence_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 2 | 712 | 0.9888888888888889 |
| 4 | 8 | 0.011111111111111112 |

selected m-support edge mass：

| selected_m_support_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 2 | 712 | 0.9888888888888889 |
| 4 | 8 | 0.011111111111111112 |

m-shell prime count edge mass：

| m_shell_prime_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 4 | 150 | 0.20833333333333334 |
| 6 | 138 | 0.19166666666666668 |
| 3 | 102 | 0.14166666666666666 |
| 5 | 100 | 0.1388888888888889 |
| 2 | 78 | 0.10833333333333334 |
| 9 | 68 | 0.09444444444444444 |
| 7 | 36 | 0.05 |
| 8 | 26 | 0.03611111111111111 |
| 10 | 12 | 0.016666666666666666 |
| 11 | 10 | 0.013888888888888888 |

m-span edge mass：

| m_span | edge_mass | edge_ratio |
| --- | --- | --- |
| 4 | 316 | 0.4388888888888889 |
| 2 | 296 | 0.4111111111111111 |
| 6 | 60 | 0.08333333333333333 |
| 8 | 26 | 0.03611111111111111 |
| 10 | 16 | 0.022222222222222223 |
| 18 | 6 | 0.008333333333333333 |

最高 same-packet multi-m templates：

| signed_child | P | packet_index | edge_mass | cycle_length | occurrence_count | selected_m_values | integer_gap_vector | prime_index_gap_vector | same_packet_gap_class | q_prefix_count | m_shell_prime_count | route_class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=positive -> g=4,c=6,A=negative -> g=6,c=9,A=positive -> g=8,c=13,A=negative -> g=4,c=6,A=positive -> g=2,c=3,A=negative | 829 | 3622 | 16 | 8 | 2 | [1303, 1307] | [4] | [1] | adjacent_prime_pair_collision | 19 | 9 | pure_upper_wing_single_shell |
| g=10,c=9,A=negative -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive -> g=4,c=3,A=positive -> g=8,c=8,A=negative -> g=4,c=4,A=positive -> g=14,c=13,A=negative | 971 | 4742 | 16 | 8 | 2 | [907, 911] | [4] | [1] | adjacent_prime_pair_collision | 28 | 5 | pure_right_tail_two_sided_collar |
| g=2,c=1,A=negative -> g=6,c=6,A=negative -> g=6,c=5,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=positive -> g=4,c=4,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive | 809 | 3316 | 16 | 8 | 2 | [739, 743] | [4] | [1] | adjacent_prime_pair_collision | 24 | 6 | pure_right_tail_two_sided_collar |
| g=10,c=10,A=negative -> g=8,c=8,A=positive -> g=10,c=9,A=positive -> g=8,c=8,A=negative -> g=6,c=6,A=positive -> g=4,c=4,A=positive -> g=8,c=7,A=positive | 919 | 4307 | 14 | 7 | 2 | [883, 887] | [4] | [1] | adjacent_prime_pair_collision | 27 | 6 | pure_right_tail_two_sided_collar |
| g=10,c=17,A=negative -> g=2,c=4,A=positive -> g=4,c=7,A=positive -> g=2,c=3,A=positive -> g=4,c=7,A=negative -> g=14,c=24,A=positive -> g=6,c=10,A=positive | 613 | 1948 | 14 | 7 | 2 | [1049, 1051] | [2] | [1] | adjacent_prime_pair_collision | 9 | 2 | pure_upper_wing_single_shell |
| g=4,c=3,A=positive -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=4,c=4,A=positive -> g=8,c=7,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative | 977 | 4807 | 14 | 7 | 2 | [877, 881] | [4] | [1] | adjacent_prime_pair_collision | 23 | 8 | pure_right_tail_two_sided_collar |
| g=10,c=11,A=positive -> g=2,c=3,A=negative -> g=4,c=4,A=negative -> g=6,c=7,A=positive -> g=2,c=2,A=negative -> g=12,c=14,A=positive | 823 | 3478 | 12 | 6 | 2 | [937, 941] | [4] | [1] | adjacent_prime_pair_collision | 16 | 4 | pure_right_tail_two_sided_collar |
| g=10,c=11,A=positive -> g=6,c=6,A=negative -> g=6,c=7,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=negative -> g=12,c=13,A=positive | 769 | 3101 | 12 | 6 | 2 | [823, 827] | [4] | [1] | adjacent_prime_pair_collision | 28 | 5 | pure_right_tail_two_sided_collar |
| g=10,c=15,A=positive -> g=6,c=9,A=negative -> g=6,c=9,A=positive -> g=2,c=3,A=positive -> g=18,c=27,A=positive -> g=6,c=8,A=negative | 1009 | 5099 | 12 | 6 | 2 | [1481, 1483] | [2] | [1] | adjacent_prime_pair_collision | 27 | 6 | pure_upper_wing_single_shell |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=negative -> g=8,c=13,A=positive -> g=4,c=6,A=positive -> g=2,c=3,A=negative | 821 | 3443 | 12 | 6 | 2 | [1319, 1321] | [2] | [1] | adjacent_prime_pair_collision | 16 | 3 | pure_upper_wing_single_shell |
| g=10,c=8,A=negative -> g=8,c=6,A=positive -> g=10,c=9,A=positive -> g=8,c=6,A=negative -> g=6,c=5,A=positive -> g=8,c=7,A=positive | 937 | 4419 | 12 | 6 | 2 | [769, 773] | [4] | [1] | adjacent_prime_pair_collision | 14 | 2 | pure_right_tail_left_collar |
| g=10,c=9,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative -> g=2,c=2,A=positive -> g=18,c=16,A=negative -> g=6,c=6,A=positive | 733 | 2788 | 12 | 6 | 2 | [673, 677] | [4] | [1] | adjacent_prime_pair_collision | 25 | 3 | pure_right_tail_two_sided_collar |
| g=10,c=9,A=positive -> g=2,c=1,A=negative -> g=4,c=4,A=negative -> g=6,c=5,A=negative -> g=6,c=5,A=positive -> g=8,c=7,A=positive | 883 | 4061 | 12 | 6 | 2 | [769, 773] | [4] | [1] | adjacent_prime_pair_collision | 21 | 2 | pure_right_tail_left_collar |
| g=10,c=9,A=positive -> g=8,c=8,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative -> g=4,c=4,A=positive -> g=8,c=7,A=negative | 947 | 4550 | 12 | 6 | 2 | [877, 881] | [4] | [1] | adjacent_prime_pair_collision | 26 | 10 | pure_right_tail_two_sided_collar |
| g=12,c=20,A=positive -> g=8,c=14,A=negative -> g=4,c=7,A=positive -> g=6,c=10,A=negative -> g=8,c=13,A=positive -> g=4,c=7,A=negative | 883 | 4082 | 12 | 6 | 2 | [1487, 1489] | [2] | [1] | adjacent_prime_pair_collision | 12 | 8 | pure_upper_wing_single_shell |
| g=2,c=3,A=negative -> g=6,c=9,A=positive -> g=4,c=6,A=negative -> g=6,c=10,A=positive -> g=8,c=12,A=positive -> g=4,c=7,A=positive | 823 | 3502 | 12 | 6 | 2 | [1289, 1291] | [2] | [1] | adjacent_prime_pair_collision | 17 | 9 | pure_upper_wing_single_shell |
| g=10,c=10,A=negative -> g=6,c=6,A=negative -> g=2,c=2,A=negative -> g=18,c=18,A=positive -> g=6,c=7,A=positive | 727 | 2741 | 10 | 5 | 2 | [739, 743] | [4] | [1] | adjacent_prime_pair_collision | 29 | 3 | pure_right_tail_two_sided_collar |
| g=10,c=10,A=negative -> g=6,c=6,A=negative -> g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=6,c=7,A=positive | 739 | 2842 | 10 | 5 | 2 | [757, 761] | [4] | [1] | adjacent_prime_pair_collision | 28 | 4 | pure_right_tail_two_sided_collar |
| g=10,c=10,A=positive -> g=8,c=7,A=negative -> g=6,c=6,A=positive -> g=6,c=5,A=negative -> g=8,c=7,A=positive | 829 | 3600 | 10 | 5 | 2 | [751, 757] | [6] | [1] | adjacent_prime_pair_collision | 21 | 4 | pure_right_tail_two_sided_collar |
| g=10,c=11,A=positive -> g=2,c=2,A=negative -> g=4,c=4,A=negative -> g=2,c=3,A=positive -> g=12,c=12,A=negative | 823 | 3485 | 10 | 5 | 2 | [859, 863] | [4] | [1] | adjacent_prime_pair_collision | 26 | 5 | pure_right_tail_two_sided_collar |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RepeatedTemplateOccurrenceClassImported | True | True | The previous repeated-template occurrence class ledger is imported. | none for import |
| SamePacketMultiMGapLedger | True | True | The same-packet multi-m collision class is split by selected m prime gaps. | none for the finite gap ledger |
| AdjacentPrimePairCollisionBound | False | False | Promote adjacent prime-pair dominance to a global local collision bound. | finite audit shows 71 templates / 662 edge mass but gives no theorem |
| NonAdjacentPrimePairCollisionBound | False | False | Control the six nonadjacent same-packet prime-pair collisions. | finite audit shows 6 templates / 50 edge mass but no global exclusion |
| AdjacentPrimeChainCollisionBound | False | False | Control the only observed adjacent prime chain collision. | finite audit shows 1 template / 8 edge mass but no global suppression |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; not a same-packet adjacent-m collision theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | arbitrary-modulus Kloosterman input; needs extracted bilinear variables |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced average input; does not bound local m-gap template collisions |
| Pascadi_2025_nonabelian_amplification_kloosterman | https://arxiv.org/abs/2511.08445 | composite Type-II input; still requires a nonlocal bilinear family |
| Shao_Shparlinski_Wijaya_2025_squarefree_smooth_kloosterman | https://arxiv.org/abs/2411.12113 | parameter-sum input; not a fixed-packet m-gap collision bound |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | prime existence input; does not estimate signed same-packet collisions |

```text
trace_or_kloosterman_inputs=need nonlocal summation variables and do not directly bound same-packet m-gap collisions
prime_gap_inputs=ordinary prime-gap information does not control signed template equality across adjacent m-values
short_interval_prime_inputs=do not estimate local signed same-packet collision classes
```

结论：same-packet multi-m repeated templates 已被拆成相邻素数对、非相邻素数对
与相邻素数链三个局部 m-gap 类。该账本仍是有限结构结果，尚未给出全局
collision bound，也尚未完成 PDEC/SAE 回流。

## 5. 最新最窄口

```text
LocalCycleLengthUniformBound
AND AdjacentPrimePairCollisionBound
AND NonAdjacentPrimePairCollisionBound
AND AdjacentPrimeChainCollisionBound
AND MultiPacketDuplicateTransportBound
AND SinglePacketSingleMMultiCycleSuppression
AND RepeatedOccurrenceAggregationOrPDEC
AND CycleOccurrenceProductBoundOrPDEC
AND SinglePSliceEndpointPacketSummationOrPDEC
AND MultiPPureEndpointTraceKloostermanCompletion
AND PureEndpointCarrierPhaseSaving
AND MixedRightTailEndpointRouterNoLoss
AND UnequalMirrorPairResidualPhaseSaving
AND ThinPSupportCarrierSummationWithoutLoss
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
single_P_local_same_packet_multi_m_gap_ledger_closed=true
adjacent_prime_pair_collision_bound_proved=false
nonadjacent_prime_pair_collision_bound_proved=false
adjacent_prime_chain_collision_bound_proved=false
same_packet_multi_m_collision_bound_proved=false
multi_packet_duplicate_transport_bound_proved=false
single_packet_single_m_multi_cycle_suppression_proved=false
local_occurrence_multiplicity_uniform_bound_proved=false
single_P_slice_endpoint_packet_summation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
