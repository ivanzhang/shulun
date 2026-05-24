# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local template occurrence class 审计

**状态：** `single_p_local_template_occurrence_class_ledger_closed_uniform_bound_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=the 97 single-P local endpoint templates with occurrence_count>1
operation=classify repeated occurrences by packet, m-value and local cycle support
dominant_shape=all repeated templates stay inside one strip; most are same-packet multi-m collisions
remaining=prove uniform collision bounds or route repeated excess to PDEC/SAE
```

## 2. repeated occurrence 分类审计

```text
max_prime=1009
single_P_local_template_occurrence_class_ledger_closed=true
single_P_local_endpoint_edge_mass=26753
single_P_local_endpoint_template_count=4915
repeated_template_count=97
repeated_template_edge_mass=872
repeated_template_edge_ratio=0.03259447538593802
single_packet_multi_m_repeated_template_count=78
single_packet_multi_m_repeated_edge_mass=720
multi_packet_repeated_template_count=17
multi_packet_repeated_edge_mass=136
single_packet_single_m_multi_cycle_template_count=2
single_packet_single_m_multi_cycle_edge_mass=16
unclassified_repeated_template_count=0
repeated_template_packet_support_count_max=2
repeated_template_m_value_support_count_max=4
repeated_template_q_prefix_support_count_max=2
repeated_template_m_shell_support_count_max=2
repeated_template_strip_support_count_max=1
repeated_template_occurrence_count_max=4
observed_repeated_templates_single_strip=true
observed_repeated_packet_support_le_2=true
observed_repeated_m_value_support_le_4=true
observed_repeated_occurrence_count_le_4=true
row_column_unconditional_closed=false
```

occurrence class template count：

| occurrence_class | template_count | template_ratio |
| --- | --- | --- |
| single_packet_multi_m_repeated_template | 78 | 0.8041237113402062 |
| multi_packet_repeated_template | 17 | 0.17525773195876287 |
| single_packet_single_m_multi_cycle_template | 2 | 0.020618556701030927 |

occurrence class edge mass：

| occurrence_class | edge_mass | edge_ratio |
| --- | --- | --- |
| single_packet_multi_m_repeated_template | 720 | 0.8256880733944955 |
| multi_packet_repeated_template | 136 | 0.1559633027522936 |
| single_packet_single_m_multi_cycle_template | 16 | 0.01834862385321101 |

occurrence class route edge mass：

| occurrence_class | route_class | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| single_packet_multi_m_repeated_template | pure_right_tail_two_sided_collar | 314 | 0.36009174311926606 |
| single_packet_multi_m_repeated_template | pure_upper_wing_single_shell | 282 | 0.32339449541284404 |
| single_packet_multi_m_repeated_template | pure_lower_wing_single_shell | 84 | 0.0963302752293578 |
| multi_packet_repeated_template | pure_right_tail_two_sided_collar | 62 | 0.07110091743119266 |
| multi_packet_repeated_template | pure_upper_wing_single_shell | 48 | 0.05504587155963303 |
| single_packet_multi_m_repeated_template | pure_right_tail_left_collar | 30 | 0.034403669724770644 |
| multi_packet_repeated_template | pure_lower_wing_single_shell | 26 | 0.02981651376146789 |
| single_packet_multi_m_repeated_template | pure_right_tail_right_collar | 10 | 0.011467889908256881 |
| single_packet_single_m_multi_cycle_template | pure_right_tail_left_collar | 10 | 0.011467889908256881 |
| single_packet_single_m_multi_cycle_template | pure_upper_wing_single_shell | 6 | 0.006880733944954129 |

support signature rows：

| packet_support_count | m_value_support_count | q_prefix_support_count | m_shell_support_count | strip_support_count | occurrence_count | cycle_length | template_edge_mass | template_count | template_ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1 | 1 | 1 | 2 | 5 | 10 | 25 | 0.25773195876288657 |
| 1 | 2 | 1 | 1 | 1 | 2 | 4 | 8 | 19 | 0.1958762886597938 |
| 1 | 2 | 1 | 1 | 1 | 2 | 3 | 6 | 16 | 0.16494845360824742 |
| 1 | 2 | 1 | 1 | 1 | 2 | 6 | 12 | 10 | 0.10309278350515463 |
| 2 | 2 | 2 | 2 | 1 | 2 | 4 | 8 | 6 | 0.061855670103092786 |
| 1 | 2 | 1 | 1 | 1 | 2 | 7 | 14 | 3 | 0.030927835051546393 |
| 1 | 2 | 1 | 1 | 1 | 2 | 8 | 16 | 3 | 0.030927835051546393 |
| 2 | 2 | 2 | 2 | 1 | 2 | 2 | 4 | 2 | 0.020618556701030927 |
| 2 | 2 | 2 | 2 | 1 | 2 | 3 | 6 | 2 | 0.020618556701030927 |
| 1 | 1 | 1 | 1 | 1 | 2 | 3 | 6 | 1 | 0.010309278350515464 |
| 1 | 1 | 1 | 1 | 1 | 2 | 5 | 10 | 1 | 0.010309278350515464 |
| 1 | 2 | 1 | 1 | 1 | 2 | 2 | 4 | 1 | 0.010309278350515464 |
| 1 | 4 | 1 | 1 | 1 | 4 | 2 | 8 | 1 | 0.010309278350515464 |
| 2 | 2 | 2 | 1 | 1 | 2 | 2 | 4 | 1 | 0.010309278350515464 |
| 2 | 2 | 2 | 1 | 1 | 2 | 3 | 6 | 1 | 0.010309278350515464 |
| 2 | 2 | 2 | 1 | 1 | 2 | 4 | 8 | 1 | 0.010309278350515464 |
| 2 | 2 | 2 | 2 | 1 | 2 | 7 | 14 | 1 | 0.010309278350515464 |
| 2 | 3 | 2 | 2 | 1 | 3 | 3 | 9 | 1 | 0.010309278350515464 |
| 2 | 3 | 2 | 2 | 1 | 3 | 4 | 12 | 1 | 0.010309278350515464 |
| 2 | 3 | 2 | 2 | 1 | 3 | 5 | 15 | 1 | 0.010309278350515464 |

q-prefix support edge mass：

| q_prefix_support_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 1 | 736 | 0.8440366972477065 |
| 2 | 136 | 0.1559633027522936 |

m-shell support edge mass：

| m_shell_support_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 1 | 754 | 0.8646788990825688 |
| 2 | 118 | 0.1353211009174312 |

strip support edge mass：

| strip_support_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 1 | 872 | 1.0 |

top repeated P rows：

| P | edge_mass | edge_ratio |
| --- | --- | --- |
| 1009 | 50 | 0.05733944954128441 |
| 991 | 42 | 0.0481651376146789 |
| 997 | 38 | 0.04357798165137615 |
| 977 | 36 | 0.04128440366972477 |
| 607 | 35 | 0.040137614678899085 |
| 613 | 34 | 0.0389908256880734 |
| 823 | 34 | 0.0389908256880734 |
| 883 | 34 | 0.0389908256880734 |
| 919 | 32 | 0.03669724770642202 |
| 617 | 28 | 0.03211009174311927 |
| 773 | 28 | 0.03211009174311927 |
| 821 | 26 | 0.02981651376146789 |
| 829 | 26 | 0.02981651376146789 |
| 887 | 26 | 0.02981651376146789 |
| 809 | 24 | 0.027522935779816515 |
| 769 | 22 | 0.02522935779816514 |
| 971 | 22 | 0.02522935779816514 |
| 619 | 20 | 0.022935779816513763 |
| 449 | 18 | 0.020642201834862386 |
| 691 | 18 | 0.020642201834862386 |

最高 repeated templates：

| signed_child | P | edge_mass | cycle_length | occurrence_count | occurrence_class | packet_support_count | m_value_support_count | q_prefix_support_count | m_shell_support_count | route_class | occurrence_locations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=positive -> g=4,c=6,A=negative -> g=6,c=9,A=positive -> g=8,c=13,A=negative -> g=4,c=6,A=positive -> g=2,c=3,A=negative | 829 | 16 | 8 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_upper_wing_single_shell | pkt=3622,m=1303,q=19,s=9; pkt=3622,m=1307,q=19,s=9 |
| g=10,c=9,A=negative -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive -> g=4,c=3,A=positive -> g=8,c=8,A=negative -> g=4,c=4,A=positive -> g=14,c=13,A=negative | 971 | 16 | 8 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_two_sided_collar | pkt=4742,m=907,q=28,s=5; pkt=4742,m=911,q=28,s=5 |
| g=2,c=1,A=negative -> g=6,c=6,A=negative -> g=6,c=5,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=positive -> g=4,c=4,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive | 809 | 16 | 8 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_two_sided_collar | pkt=3316,m=739,q=24,s=6; pkt=3316,m=743,q=24,s=6 |
| g=2,c=2,A=negative -> g=4,c=3,A=negative -> g=6,c=5,A=positive -> g=8,c=6,A=negative -> g=4,c=3,A=positive | 607 | 15 | 5 | 3 | multi_packet_repeated_template | 2 | 3 | 2 | 2 | pure_right_tail_two_sided_collar | pkt=1887,m=479,q=7,s=3; pkt=1888,m=487,q=8,s=5; pkt=1888,m=491,q=8,s=5 |
| g=10,c=10,A=negative -> g=8,c=8,A=positive -> g=10,c=9,A=positive -> g=8,c=8,A=negative -> g=6,c=6,A=positive -> g=4,c=4,A=positive -> g=8,c=7,A=positive | 919 | 14 | 7 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_two_sided_collar | pkt=4307,m=883,q=27,s=6; pkt=4307,m=887,q=27,s=6 |
| g=10,c=17,A=negative -> g=2,c=4,A=positive -> g=4,c=7,A=positive -> g=2,c=3,A=positive -> g=4,c=7,A=negative -> g=14,c=24,A=positive -> g=6,c=10,A=positive | 613 | 14 | 7 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_upper_wing_single_shell | pkt=1948,m=1049,q=9,s=2; pkt=1948,m=1051,q=9,s=2 |
| g=10,c=9,A=negative -> g=2,c=2,A=positive -> g=4,c=3,A=negative -> g=6,c=5,A=negative -> g=4,c=3,A=positive -> g=2,c=2,A=negative -> g=12,c=10,A=positive | 821 | 14 | 7 | 2 | multi_packet_repeated_template | 2 | 2 | 2 | 2 | pure_right_tail_two_sided_collar | pkt=3417,m=701,q=15,s=3; pkt=3418,m=709,q=16,s=2 |
| g=4,c=3,A=positive -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=4,c=4,A=positive -> g=8,c=7,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative | 977 | 14 | 7 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_two_sided_collar | pkt=4807,m=877,q=23,s=8; pkt=4807,m=881,q=23,s=8 |
| g=12,c=17,A=negative -> g=4,c=5,A=positive -> g=6,c=9,A=positive -> g=2,c=2,A=negative | 991 | 12 | 4 | 3 | multi_packet_repeated_template | 2 | 3 | 2 | 2 | pure_upper_wing_single_shell | pkt=4968,m=1367,q=33,s=2; pkt=4968,m=1373,q=33,s=2; pkt=4969,m=1361,q=34,s=1 |
| g=10,c=11,A=positive -> g=2,c=3,A=negative -> g=4,c=4,A=negative -> g=6,c=7,A=positive -> g=2,c=2,A=negative -> g=12,c=14,A=positive | 823 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_two_sided_collar | pkt=3478,m=937,q=16,s=4; pkt=3478,m=941,q=16,s=4 |
| g=10,c=11,A=positive -> g=6,c=6,A=negative -> g=6,c=7,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=negative -> g=12,c=13,A=positive | 769 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_two_sided_collar | pkt=3101,m=823,q=28,s=5; pkt=3101,m=827,q=28,s=5 |
| g=10,c=15,A=positive -> g=6,c=9,A=negative -> g=6,c=9,A=positive -> g=2,c=3,A=positive -> g=18,c=27,A=positive -> g=6,c=8,A=negative | 1009 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_upper_wing_single_shell | pkt=5099,m=1481,q=27,s=6; pkt=5099,m=1483,q=27,s=6 |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=negative -> g=8,c=13,A=positive -> g=4,c=6,A=positive -> g=2,c=3,A=negative | 821 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_upper_wing_single_shell | pkt=3443,m=1319,q=16,s=3; pkt=3443,m=1321,q=16,s=3 |
| g=10,c=8,A=negative -> g=8,c=6,A=positive -> g=10,c=9,A=positive -> g=8,c=6,A=negative -> g=6,c=5,A=positive -> g=8,c=7,A=positive | 937 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_left_collar | pkt=4419,m=769,q=14,s=2; pkt=4419,m=773,q=14,s=2 |
| g=10,c=9,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative -> g=2,c=2,A=positive -> g=18,c=16,A=negative -> g=6,c=6,A=positive | 733 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_two_sided_collar | pkt=2788,m=673,q=25,s=3; pkt=2788,m=677,q=25,s=3 |
| g=10,c=9,A=positive -> g=2,c=1,A=negative -> g=4,c=4,A=negative -> g=6,c=5,A=negative -> g=6,c=5,A=positive -> g=8,c=7,A=positive | 883 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_left_collar | pkt=4061,m=769,q=21,s=2; pkt=4061,m=773,q=21,s=2 |
| g=10,c=9,A=positive -> g=8,c=8,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative -> g=4,c=4,A=positive -> g=8,c=7,A=negative | 947 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_two_sided_collar | pkt=4550,m=877,q=26,s=10; pkt=4550,m=881,q=26,s=10 |
| g=12,c=20,A=positive -> g=8,c=14,A=negative -> g=4,c=7,A=positive -> g=6,c=10,A=negative -> g=8,c=13,A=positive -> g=4,c=7,A=negative | 883 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_upper_wing_single_shell | pkt=4082,m=1487,q=12,s=8; pkt=4082,m=1489,q=12,s=8 |
| g=2,c=3,A=negative -> g=6,c=9,A=positive -> g=4,c=6,A=negative -> g=6,c=10,A=positive -> g=8,c=12,A=positive -> g=4,c=7,A=positive | 823 | 12 | 6 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_upper_wing_single_shell | pkt=3502,m=1289,q=17,s=9; pkt=3502,m=1291,q=17,s=9 |
| g=10,c=10,A=negative -> g=6,c=6,A=negative -> g=2,c=2,A=negative -> g=18,c=18,A=positive -> g=6,c=7,A=positive | 727 | 10 | 5 | 2 | single_packet_multi_m_repeated_template | 1 | 2 | 1 | 1 | pure_right_tail_two_sided_collar | pkt=2741,m=739,q=29,s=3; pkt=2741,m=743,q=29,s=3 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SinglePLocalTemplateMultiplicityImported | True | True | The previous cycle_length times occurrence_count factor ledger is imported. | none for import |
| RepeatedTemplateOccurrenceClassLedger | True | True | Every repeated template is classified as same-packet multi-m, multi-packet, or same-m multi-cycle. | none for the finite classification ledger |
| SinglePacketMultiMCollisionBound | False | False | Promote same-packet multi-m collision sparsity to a structural bound. | finite audit shows 78 templates / 720 edge mass but gives no global theorem |
| MultiPacketDuplicateTransportBound | False | False | Control repeated templates transported across packets. | finite audit shows 17 templates / 136 edge mass but no global transport bound |
| SinglePacketSingleMMultiCycleSuppression | False | False | Suppress multiple cycles inside one packet and one m-value. | finite audit shows 2 templates / 16 edge mass but no global exclusion |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | bilinear trace input; does not prove local repeated-template collision bounds |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | arbitrary-modulus Kloosterman average; needs extracted bilinear variables |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced convolution input; does not bound width-one occurrence collisions |
| Pascadi_2025_nonabelian_amplification_kloosterman | https://arxiv.org/abs/2511.08445 | composite-modulus Type-II input; still needs a bilinear family, not a single local collision |
| Shao_Shparlinski_Wijaya_2025_squarefree_smooth_kloosterman | https://arxiv.org/abs/2411.12113 | square-free/smooth parameter input; does not control repeated signed local templates |
| Xu_Zhang_2026_generalized_kloosterman_arbitrary_sets | https://doi.org/10.1016/j.jnt.2025.09.027 | arbitrary-set bilinear input; still requires explicit finite-field set variables |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | prime existence input; not an occurrence-collision theorem |

```text
trace_or_kloosterman_average_inputs=do not directly control width-one local repeated-template collisions
arbitrary_set_inputs=need explicit finite-field sets and a summation variable not present in a single local collision
short_interval_prime_inputs=do not estimate signed endpoint occurrence classes
```

结论：repeated occurrence 已拆成三个可审计局部类。该账本仍是有限结构结果，
尚未给出全局 collision bound，也尚未完成 PDEC/SAE 回流。

## 5. 最新最窄口

```text
LocalCycleLengthUniformBound
AND SinglePacketMultiMCollisionBound
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
single_P_local_template_occurrence_class_ledger_closed=true
single_packet_multi_m_collision_bound_proved=false
multi_packet_duplicate_transport_bound_proved=false
single_packet_single_m_multi_cycle_suppression_proved=false
repeated_occurrence_aggregation_or_pdec_closed=false
local_occurrence_multiplicity_uniform_bound_proved=false
local_template_multiplicity_uniform_bound_proved=false
single_P_slice_endpoint_packet_summation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
