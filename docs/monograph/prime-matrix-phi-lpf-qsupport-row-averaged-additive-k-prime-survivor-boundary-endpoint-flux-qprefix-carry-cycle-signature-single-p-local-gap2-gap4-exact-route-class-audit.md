# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 exact route-class 审计

**状态：** `single_p_local_gap2_gap4_exact_route_class_ledger_closed_collision_bounds_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=the 64 gap2/gap4 adjacent-prime-pair repeated templates
operation=classify dominant route-superclass carriers by exact route class
dominant_shape=gap4 two-sided right-tail collar and gap2 upper wing are the two largest exact routes
remaining=prove signed collision bounds for exact route classes or route them to PDEC/SAE
```

## 2. gap2/gap4 exact route-class 分类审计

```text
max_prime=1009
single_P_local_gap2_gap4_exact_route_class_ledger_closed=true
gap2_gap4_template_count=64
gap2_gap4_edge_mass=612
gap4_right_tail_two_sided_template_count=25
gap4_right_tail_two_sided_edge_mass=258
gap2_upper_wing_template_count=23
gap2_upper_wing_edge_mass=212
gap2_lower_wing_template_count=9
gap2_lower_wing_edge_mass=78
gap4_right_tail_left_collar_template_count=3
gap4_right_tail_left_collar_edge_mass=30
gap4_upper_wing_template_count=2
gap4_upper_wing_edge_mass=22
gap2_right_tail_two_sided_template_count=1
gap2_right_tail_two_sided_edge_mass=6
gap4_lower_wing_template_count=1
gap4_lower_wing_edge_mass=6
top_two_route_edge_mass=470
top_two_route_edge_ratio=0.7679738562091504
residual_route_edge_mass=142
residual_route_edge_ratio=0.23202614379084968
gap2_upper_share_within_gap2=0.7162162162162162
gap4_two_sided_share_within_gap4=0.8164556962025317
mixed_positive_negative_edge_mass=600
all_positive_edge_mass=12
duplicate_raw_base_count=3
duplicate_raw_base_edge_mass=48
row_column_unconditional_closed=false
```

exact route-class template count：

| adjacent_pair_gap_class | route_class | template_count | template_ratio |
| --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 25 | 0.390625 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 23 | 0.359375 |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 9 | 0.140625 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_left_collar | 3 | 0.046875 |
| gap4_cousin_adjacent_pair_collision | pure_upper_wing_single_shell | 2 | 0.03125 |
| gap2_twin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 1 | 0.015625 |
| gap4_cousin_adjacent_pair_collision | pure_lower_wing_single_shell | 1 | 0.015625 |

exact route-class edge mass：

| adjacent_pair_gap_class | route_class | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 258 | 0.4215686274509804 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 212 | 0.3464052287581699 |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 78 | 0.12745098039215685 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_left_collar | 30 | 0.049019607843137254 |
| gap4_cousin_adjacent_pair_collision | pure_upper_wing_single_shell | 22 | 0.03594771241830065 |
| gap2_twin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | pure_lower_wing_single_shell | 6 | 0.00980392156862745 |

exact route-class A-class edge mass：

| adjacent_pair_gap_class | route_class | A_class | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | mixed_positive_negative | 258 | 0.4215686274509804 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | mixed_positive_negative | 212 | 0.3464052287581699 |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | mixed_positive_negative | 78 | 0.12745098039215685 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_left_collar | mixed_positive_negative | 30 | 0.049019607843137254 |
| gap4_cousin_adjacent_pair_collision | pure_upper_wing_single_shell | mixed_positive_negative | 16 | 0.026143790849673203 |
| gap2_twin_adjacent_pair_collision | pure_right_tail_two_sided_collar | mixed_positive_negative | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | pure_lower_wing_single_shell | all_positive | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | pure_upper_wing_single_shell | all_positive | 6 | 0.00980392156862745 |

exact route-class cycle-length edge mass：

| adjacent_pair_gap_class | route_class | cycle_length | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 5 | 100 | 0.16339869281045752 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 5 | 70 | 0.11437908496732026 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 4 | 56 | 0.0915032679738562 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 6 | 48 | 0.0784313725490196 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 6 | 48 | 0.0784313725490196 |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 5 | 40 | 0.06535947712418301 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 4 | 40 | 0.06535947712418301 |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 4 | 32 | 0.05228758169934641 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 8 | 32 | 0.05228758169934641 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 7 | 28 | 0.0457516339869281 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 3 | 24 | 0.0392156862745098 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_left_collar | 6 | 24 | 0.0392156862745098 |
| gap4_cousin_adjacent_pair_collision | pure_upper_wing_single_shell | 8 | 16 | 0.026143790849673203 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 7 | 14 | 0.02287581699346405 |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 3 | 6 | 0.00980392156862745 |
| gap2_twin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 3 | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | pure_lower_wing_single_shell | 3 | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_left_collar | 3 | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 3 | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | pure_upper_wing_single_shell | 3 | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 2 | 4 | 0.006535947712418301 |

duplicate raw-base rows：

| adjacent_pair_gap_class | route_class | template_count | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 2 | 20 | 0.032679738562091505 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 2 | 16 | 0.026143790849673203 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 2 | 12 | 0.0196078431372549 |

最高 exact-route templates：

| adjacent_pair_gap_class | route_class | P | packet_index | edge_mass | cycle_length | m_pair | q_prefix_count | m_shell_prime_count | A_class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 809 | 3316 | 16 | 8 | [739, 743] | 24 | 6 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 971 | 4742 | 16 | 8 | [907, 911] | 28 | 5 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_upper_wing_single_shell | 829 | 3622 | 16 | 8 | [1303, 1307] | 19 | 9 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 613 | 1948 | 14 | 7 | [1049, 1051] | 9 | 2 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 919 | 4307 | 14 | 7 | [883, 887] | 27 | 6 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 977 | 4807 | 14 | 7 | [877, 881] | 23 | 8 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 821 | 3443 | 12 | 6 | [1319, 1321] | 16 | 3 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 823 | 3502 | 12 | 6 | [1289, 1291] | 17 | 9 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 883 | 4082 | 12 | 6 | [1487, 1489] | 12 | 8 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 1009 | 5099 | 12 | 6 | [1481, 1483] | 27 | 6 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_left_collar | 883 | 4061 | 12 | 6 | [769, 773] | 21 | 2 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_left_collar | 937 | 4419 | 12 | 6 | [769, 773] | 14 | 2 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 733 | 2788 | 12 | 6 | [673, 677] | 25 | 3 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 769 | 3101 | 12 | 6 | [823, 827] | 28 | 5 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 823 | 3478 | 12 | 6 | [937, 941] | 16 | 4 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 947 | 4550 | 12 | 6 | [877, 881] | 26 | 10 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 607 | 1882 | 10 | 5 | [431, 433] | 20 | 2 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 677 | 2432 | 10 | 5 | [431, 433] | 14 | 2 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 773 | 3131 | 10 | 5 | [461, 463] | 11 | 4 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 887 | 4106 | 10 | 5 | [659, 661] | 32 | 3 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 613 | 1957 | 10 | 5 | [881, 883] | 20 | 4 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 617 | 1994 | 10 | 5 | [1019, 1021] | 10 | 6 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 617 | 1994 | 10 | 5 | [1031, 1033] | 10 | 6 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 883 | 4084 | 10 | 5 | [1427, 1429] | 15 | 5 | mixed_positive_negative |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| Gap2Gap4RouteSuperclassLedgerImported | True | True | The gap2/gap4 route-superclass ledger is imported. | none for import |
| Gap2Gap4ExactRouteClassLedger | True | True | Gap2/gap4 carriers are split by exact route class. | none for the finite exact-route ledger |
| Gap4RightTailTwoSidedCousinCollisionBound | False | False | Control the largest exact route: gap4 right-tail two-sided collar. | finite audit shows 258 edge mass but no global theorem |
| Gap2UpperWingTwinCollisionBound | False | False | Control the second largest exact route: gap2 upper wing. | finite audit shows 212 edge mass but no global theorem |
| ResidualExactRouteCollisionBounds | False | False | Control lower wing, left-collar, and small off-route residuals. | finite audit shows 142 edge mass outside the two largest exact routes |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=do not directly control a fixed upper-wing or two-sided-collar signed template equality
prime_gap_theorems=do not distinguish Phi-LPF exact route classes
short_interval_prime_inputs=do not estimate these local carrier collisions
```

结论：gap2/gap4 route-superclass 主量已进一步拆成 exact route-class carrier。
该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
LocalCycleLengthUniformBound
AND Gap2UpperWingTwinCollisionBound
AND Gap2LowerWingTwinCollisionBound
AND Gap2RightTailTwoSidedTwinResidualCollisionBound
AND Gap4RightTailTwoSidedCousinCollisionBound
AND Gap4RightTailLeftCollarCousinCollisionBound
AND Gap4UpperWingCousinResidualCollisionBound
AND Gap4LowerWingCousinResidualCollisionBound
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
single_P_local_gap2_gap4_exact_route_class_ledger_closed=true
gap2_upper_wing_twin_collision_bound_proved=false
gap2_lower_wing_twin_collision_bound_proved=false
gap2_right_tail_twin_residual_bound_proved=false
gap4_right_tail_two_sided_cousin_collision_bound_proved=false
gap4_right_tail_left_collar_cousin_collision_bound_proved=false
gap4_wing_cousin_residual_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
