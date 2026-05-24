# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local adjacent prime pair gap class 审计

**状态：** `single_p_local_adjacent_prime_pair_gap_class_ledger_closed_uniform_bound_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=the 71 same-packet adjacent-prime-pair repeated templates
operation=classify adjacent pairs by exact integer prime gap 2, 4, 6, or >=8
dominant_shape=gap 2 and gap 4 together carry almost all adjacent-pair collision mass
remaining=prove signed collision bounds for gap-2/gap-4 adjacent pairs or route excess to PDEC/SAE
```

## 2. adjacent prime pair exact-gap 分类审计

```text
max_prime=1009
single_P_local_adjacent_prime_pair_gap_class_ledger_closed=true
adjacent_prime_pair_template_count=71
adjacent_prime_pair_edge_mass=662
gap2_twin_adjacent_pair_template_count=33
gap2_twin_adjacent_pair_edge_mass=296
gap4_cousin_adjacent_pair_template_count=31
gap4_cousin_adjacent_pair_edge_mass=316
gap6_sexy_adjacent_pair_template_count=5
gap6_sexy_adjacent_pair_edge_mass=36
gap_ge8_adjacent_pair_template_count=2
gap_ge8_adjacent_pair_edge_mass=14
bad_adjacent_pair_template_count=0
adjacent_pair_gap_min/max=2/10
duplicate_raw_base_count=3
duplicate_raw_base_edge_mass=48
observed_gap2_or_gap4_edge_mass=612
observed_gap2_or_gap4_edge_ratio=0.9244712990936556
observed_gap2_or_gap4_dominant=true
row_column_unconditional_closed=false
```

adjacent pair gap class template count：

| adjacent_pair_gap_class | template_count | template_ratio |
| --- | --- | --- |
| gap2_twin_adjacent_pair_collision | 33 | 0.4647887323943662 |
| gap4_cousin_adjacent_pair_collision | 31 | 0.43661971830985913 |
| gap6_sexy_adjacent_pair_collision | 5 | 0.07042253521126761 |
| gap_ge8_adjacent_pair_collision | 2 | 0.028169014084507043 |

adjacent pair gap class edge mass：

| adjacent_pair_gap_class | edge_mass | edge_ratio |
| --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | 316 | 0.4773413897280967 |
| gap2_twin_adjacent_pair_collision | 296 | 0.4471299093655589 |
| gap6_sexy_adjacent_pair_collision | 36 | 0.054380664652567974 |
| gap_ge8_adjacent_pair_collision | 14 | 0.021148036253776436 |

exact integer gap edge mass：

| integer_gap | edge_mass | edge_ratio |
| --- | --- | --- |
| 4 | 316 | 0.4773413897280967 |
| 2 | 296 | 0.4471299093655589 |
| 6 | 36 | 0.054380664652567974 |
| 10 | 8 | 0.012084592145015106 |
| 8 | 6 | 0.00906344410876133 |

gap class route edge mass：

| adjacent_pair_gap_class | route_class | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 258 | 0.38972809667673713 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 212 | 0.3202416918429003 |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 78 | 0.11782477341389729 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_left_collar | 30 | 0.045317220543806644 |
| gap6_sexy_adjacent_pair_collision | pure_right_tail_two_sided_collar | 24 | 0.03625377643504532 |
| gap4_cousin_adjacent_pair_collision | pure_upper_wing_single_shell | 22 | 0.03323262839879154 |
| gap_ge8_adjacent_pair_collision | pure_upper_wing_single_shell | 14 | 0.021148036253776436 |
| gap6_sexy_adjacent_pair_collision | pure_upper_wing_single_shell | 12 | 0.01812688821752266 |
| gap2_twin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 6 | 0.00906344410876133 |
| gap4_cousin_adjacent_pair_collision | pure_lower_wing_single_shell | 6 | 0.00906344410876133 |

gap class A-class edge mass：

| adjacent_pair_gap_class | A_class | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | mixed_positive_negative | 304 | 0.459214501510574 |
| gap2_twin_adjacent_pair_collision | mixed_positive_negative | 296 | 0.4471299093655589 |
| gap6_sexy_adjacent_pair_collision | mixed_positive_negative | 36 | 0.054380664652567974 |
| gap4_cousin_adjacent_pair_collision | all_positive | 12 | 0.01812688821752266 |
| gap_ge8_adjacent_pair_collision | all_positive | 8 | 0.012084592145015106 |
| gap_ge8_adjacent_pair_collision | mixed_positive_negative | 6 | 0.00906344410876133 |

gap class cycle-length edge mass：

| adjacent_pair_gap_class | cycle_length | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| gap2_twin_adjacent_pair_collision | 5 | 110 | 0.1661631419939577 |
| gap4_cousin_adjacent_pair_collision | 5 | 100 | 0.1510574018126888 |
| gap2_twin_adjacent_pair_collision | 4 | 88 | 0.13293051359516617 |
| gap4_cousin_adjacent_pair_collision | 6 | 72 | 0.10876132930513595 |
| gap2_twin_adjacent_pair_collision | 6 | 48 | 0.07250755287009064 |
| gap4_cousin_adjacent_pair_collision | 8 | 48 | 0.07250755287009064 |
| gap4_cousin_adjacent_pair_collision | 4 | 40 | 0.06042296072507553 |
| gap2_twin_adjacent_pair_collision | 3 | 36 | 0.054380664652567974 |
| gap4_cousin_adjacent_pair_collision | 7 | 28 | 0.04229607250755287 |
| gap4_cousin_adjacent_pair_collision | 3 | 24 | 0.03625377643504532 |
| gap6_sexy_adjacent_pair_collision | 3 | 18 | 0.027190332326283987 |
| gap2_twin_adjacent_pair_collision | 7 | 14 | 0.021148036253776436 |
| gap6_sexy_adjacent_pair_collision | 5 | 10 | 0.015105740181268883 |
| gap6_sexy_adjacent_pair_collision | 4 | 8 | 0.012084592145015106 |
| gap_ge8_adjacent_pair_collision | 4 | 8 | 0.012084592145015106 |
| gap_ge8_adjacent_pair_collision | 3 | 6 | 0.00906344410876133 |
| gap4_cousin_adjacent_pair_collision | 2 | 4 | 0.006042296072507553 |

最高 adjacent-pair templates：

| signed_child | P | packet_index | edge_mass | cycle_length | m_pair | integer_gap | adjacent_pair_gap_class | q_prefix_count | m_shell_prime_count | route_class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=positive -> g=4,c=6,A=negative -> g=6,c=9,A=positive -> g=8,c=13,A=negative -> g=4,c=6,A=positive -> g=2,c=3,A=negative | 829 | 3622 | 16 | 8 | [1303, 1307] | 4 | gap4_cousin_adjacent_pair_collision | 19 | 9 | pure_upper_wing_single_shell |
| g=10,c=9,A=negative -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive -> g=4,c=3,A=positive -> g=8,c=8,A=negative -> g=4,c=4,A=positive -> g=14,c=13,A=negative | 971 | 4742 | 16 | 8 | [907, 911] | 4 | gap4_cousin_adjacent_pair_collision | 28 | 5 | pure_right_tail_two_sided_collar |
| g=2,c=1,A=negative -> g=6,c=6,A=negative -> g=6,c=5,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=positive -> g=4,c=4,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive | 809 | 3316 | 16 | 8 | [739, 743] | 4 | gap4_cousin_adjacent_pair_collision | 24 | 6 | pure_right_tail_two_sided_collar |
| g=10,c=10,A=negative -> g=8,c=8,A=positive -> g=10,c=9,A=positive -> g=8,c=8,A=negative -> g=6,c=6,A=positive -> g=4,c=4,A=positive -> g=8,c=7,A=positive | 919 | 4307 | 14 | 7 | [883, 887] | 4 | gap4_cousin_adjacent_pair_collision | 27 | 6 | pure_right_tail_two_sided_collar |
| g=10,c=17,A=negative -> g=2,c=4,A=positive -> g=4,c=7,A=positive -> g=2,c=3,A=positive -> g=4,c=7,A=negative -> g=14,c=24,A=positive -> g=6,c=10,A=positive | 613 | 1948 | 14 | 7 | [1049, 1051] | 2 | gap2_twin_adjacent_pair_collision | 9 | 2 | pure_upper_wing_single_shell |
| g=4,c=3,A=positive -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=4,c=4,A=positive -> g=8,c=7,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative | 977 | 4807 | 14 | 7 | [877, 881] | 4 | gap4_cousin_adjacent_pair_collision | 23 | 8 | pure_right_tail_two_sided_collar |
| g=10,c=11,A=positive -> g=2,c=3,A=negative -> g=4,c=4,A=negative -> g=6,c=7,A=positive -> g=2,c=2,A=negative -> g=12,c=14,A=positive | 823 | 3478 | 12 | 6 | [937, 941] | 4 | gap4_cousin_adjacent_pair_collision | 16 | 4 | pure_right_tail_two_sided_collar |
| g=10,c=11,A=positive -> g=6,c=6,A=negative -> g=6,c=7,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=negative -> g=12,c=13,A=positive | 769 | 3101 | 12 | 6 | [823, 827] | 4 | gap4_cousin_adjacent_pair_collision | 28 | 5 | pure_right_tail_two_sided_collar |
| g=10,c=15,A=positive -> g=6,c=9,A=negative -> g=6,c=9,A=positive -> g=2,c=3,A=positive -> g=18,c=27,A=positive -> g=6,c=8,A=negative | 1009 | 5099 | 12 | 6 | [1481, 1483] | 2 | gap2_twin_adjacent_pair_collision | 27 | 6 | pure_upper_wing_single_shell |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=negative -> g=8,c=13,A=positive -> g=4,c=6,A=positive -> g=2,c=3,A=negative | 821 | 3443 | 12 | 6 | [1319, 1321] | 2 | gap2_twin_adjacent_pair_collision | 16 | 3 | pure_upper_wing_single_shell |
| g=10,c=8,A=negative -> g=8,c=6,A=positive -> g=10,c=9,A=positive -> g=8,c=6,A=negative -> g=6,c=5,A=positive -> g=8,c=7,A=positive | 937 | 4419 | 12 | 6 | [769, 773] | 4 | gap4_cousin_adjacent_pair_collision | 14 | 2 | pure_right_tail_left_collar |
| g=10,c=9,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative -> g=2,c=2,A=positive -> g=18,c=16,A=negative -> g=6,c=6,A=positive | 733 | 2788 | 12 | 6 | [673, 677] | 4 | gap4_cousin_adjacent_pair_collision | 25 | 3 | pure_right_tail_two_sided_collar |
| g=10,c=9,A=positive -> g=2,c=1,A=negative -> g=4,c=4,A=negative -> g=6,c=5,A=negative -> g=6,c=5,A=positive -> g=8,c=7,A=positive | 883 | 4061 | 12 | 6 | [769, 773] | 4 | gap4_cousin_adjacent_pair_collision | 21 | 2 | pure_right_tail_left_collar |
| g=10,c=9,A=positive -> g=8,c=8,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative -> g=4,c=4,A=positive -> g=8,c=7,A=negative | 947 | 4550 | 12 | 6 | [877, 881] | 4 | gap4_cousin_adjacent_pair_collision | 26 | 10 | pure_right_tail_two_sided_collar |
| g=12,c=20,A=positive -> g=8,c=14,A=negative -> g=4,c=7,A=positive -> g=6,c=10,A=negative -> g=8,c=13,A=positive -> g=4,c=7,A=negative | 883 | 4082 | 12 | 6 | [1487, 1489] | 2 | gap2_twin_adjacent_pair_collision | 12 | 8 | pure_upper_wing_single_shell |
| g=2,c=3,A=negative -> g=6,c=9,A=positive -> g=4,c=6,A=negative -> g=6,c=10,A=positive -> g=8,c=12,A=positive -> g=4,c=7,A=positive | 823 | 3502 | 12 | 6 | [1289, 1291] | 2 | gap2_twin_adjacent_pair_collision | 17 | 9 | pure_upper_wing_single_shell |
| g=10,c=10,A=negative -> g=6,c=6,A=negative -> g=2,c=2,A=negative -> g=18,c=18,A=positive -> g=6,c=7,A=positive | 727 | 2741 | 10 | 5 | [739, 743] | 4 | gap4_cousin_adjacent_pair_collision | 29 | 3 | pure_right_tail_two_sided_collar |
| g=10,c=10,A=negative -> g=6,c=6,A=negative -> g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=6,c=7,A=positive | 739 | 2842 | 10 | 5 | [757, 761] | 4 | gap4_cousin_adjacent_pair_collision | 28 | 4 | pure_right_tail_two_sided_collar |
| g=10,c=10,A=positive -> g=8,c=7,A=negative -> g=6,c=6,A=positive -> g=6,c=5,A=negative -> g=8,c=7,A=positive | 829 | 3600 | 10 | 5 | [751, 757] | 6 | gap6_sexy_adjacent_pair_collision | 21 | 4 | pure_right_tail_two_sided_collar |
| g=10,c=11,A=positive -> g=2,c=2,A=negative -> g=4,c=4,A=negative -> g=2,c=3,A=positive -> g=12,c=12,A=negative | 823 | 3485 | 10 | 5 | [859, 863] | 4 | gap4_cousin_adjacent_pair_collision | 26 | 5 | pure_right_tail_two_sided_collar |
| g=10,c=11,A=positive -> g=6,c=6,A=negative -> g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=6,c=7,A=negative | 773 | 3157 | 10 | 5 | [823, 827] | 4 | gap4_cousin_adjacent_pair_collision | 28 | 6 | pure_right_tail_two_sided_collar |
| g=10,c=12,A=negative -> g=6,c=7,A=positive -> g=6,c=7,A=negative -> g=2,c=3,A=positive -> g=6,c=6,A=negative | 761 | 3042 | 10 | 5 | [877, 881] | 4 | gap4_cousin_adjacent_pair_collision | 19 | 7 | pure_right_tail_two_sided_collar |
| g=10,c=14,A=positive -> g=2,c=3,A=positive -> g=4,c=6,A=positive -> g=14,c=20,A=negative -> g=6,c=9,A=negative | 613 | 1957 | 10 | 5 | [881, 883] | 2 | gap2_twin_adjacent_pair_collision | 20 | 4 | pure_upper_wing_single_shell |
| g=10,c=16,A=negative -> g=2,c=4,A=positive -> g=4,c=6,A=negative -> g=14,c=24,A=positive -> g=6,c=10,A=negative | 617 | 1994 | 10 | 5 | [1031, 1033] | 2 | gap2_twin_adjacent_pair_collision | 10 | 6 | pure_upper_wing_single_shell |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SamePacketMultiMGapLedgerImported | True | True | The previous same-packet multi-m gap ledger is imported. | none for import |
| AdjacentPrimePairGapClassLedger | True | True | Adjacent-prime-pair collisions are split by exact prime gap. | none for the finite gap-class ledger |
| Gap2TwinAdjacentPairCollisionBound | False | False | Control signed template equality across adjacent m-pairs of gap 2. | finite audit shows 33 templates / 296 edge mass but gives no global theorem |
| Gap4CousinAdjacentPairCollisionBound | False | False | Control signed template equality across adjacent m-pairs of gap 4. | finite audit shows 31 templates / 316 edge mass but gives no global theorem |
| Gap6AndLargeAdjacentPairCollisionBound | False | False | Control gap 6 and gap >=8 adjacent-pair collisions. | finite audit shows 7 templates / 50 edge mass but no global suppression |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; not a fixed-packet adjacent-pair equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | arbitrary-modulus Kloosterman input; no local gap-2/gap-4 signed template bound |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced average input; not a pointwise adjacent-pair collision bound |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence theorem; does not control signed template equality on adjacent m-pairs |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; not a local collision theorem |

```text
trace_or_kloosterman_inputs=need nonlocal summation variables and do not directly bound fixed-packet gap-2/gap-4 signed collisions
prime_gap_theorems=describe existence or density of prime gaps, not equality of Phi-LPF signed templates
short_interval_prime_inputs=do not estimate adjacent-m template collision classes
```

结论：adjacent-prime-pair collisions 已被拆成 gap-2、gap-4、gap-6 与 gap>=8
四个局部类。该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
LocalCycleLengthUniformBound
AND Gap2TwinAdjacentPairCollisionBound
AND Gap4CousinAdjacentPairCollisionBound
AND Gap6SexyAdjacentPairCollisionBound
AND GapGe8AdjacentPairCollisionBound
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
single_P_local_adjacent_prime_pair_gap_class_ledger_closed=true
gap2_twin_adjacent_pair_collision_bound_proved=false
gap4_cousin_adjacent_pair_collision_bound_proved=false
gap6_sexy_adjacent_pair_collision_bound_proved=false
gap_ge8_adjacent_pair_collision_bound_proved=false
adjacent_prime_pair_collision_bound_proved=false
local_occurrence_multiplicity_uniform_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
