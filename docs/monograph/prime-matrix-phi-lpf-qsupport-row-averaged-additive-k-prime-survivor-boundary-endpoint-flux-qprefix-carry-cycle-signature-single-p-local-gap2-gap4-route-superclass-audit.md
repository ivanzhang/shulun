# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 route-superclass 审计

**状态：** `single_p_local_gap2_gap4_route_superclass_ledger_closed_collision_bounds_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=the 64 gap2/gap4 adjacent-prime-pair repeated templates
operation=classify dominant adjacent-pair collisions by route superclass
dominant_shape=gap2 is wing-dominant while gap4 is right-tail-dominant
remaining=prove signed collision bounds for the route-superclass carriers or route them to PDEC/SAE
```

## 2. gap2/gap4 route-superclass 分类审计

```text
max_prime=1009
single_P_local_gap2_gap4_route_superclass_ledger_closed=true
gap2_gap4_template_count=64
gap2_gap4_edge_mass=612
gap2_twin_template_count=33
gap2_twin_edge_mass=296
gap2_wing_template_count=32
gap2_wing_edge_mass=290
gap2_right_tail_template_count=1
gap2_right_tail_edge_mass=6
gap4_cousin_template_count=31
gap4_cousin_edge_mass=316
gap4_right_tail_template_count=28
gap4_right_tail_edge_mass=288
gap4_wing_template_count=3
gap4_wing_edge_mass=28
dominant_aligned_edge_mass=578
dominant_aligned_edge_ratio=0.9444444444444444
offdominant_residual_edge_mass=34
offdominant_residual_edge_ratio=0.05555555555555555
gap2_wing_edge_ratio_within_gap2=0.9797297297297297
gap4_right_tail_edge_ratio_within_gap4=0.9113924050632911
dominant_aligned_mixed_positive_negative_edge_mass=578
all_positive_edge_mass=12
duplicate_raw_base_count=3
duplicate_raw_base_edge_mass=48
row_column_unconditional_closed=false
```

route-superclass template count：

| adjacent_pair_gap_class | route_superclass | template_count | template_ratio |
| --- | --- | --- | --- |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 32 | 0.5 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 28 | 0.4375 |
| gap4_cousin_adjacent_pair_collision | wing_single_P_local | 3 | 0.046875 |
| gap2_twin_adjacent_pair_collision | right_tail_single_P_local | 1 | 0.015625 |

route-superclass edge mass：

| adjacent_pair_gap_class | route_superclass | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 290 | 0.4738562091503268 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 288 | 0.47058823529411764 |
| gap4_cousin_adjacent_pair_collision | wing_single_P_local | 28 | 0.0457516339869281 |
| gap2_twin_adjacent_pair_collision | right_tail_single_P_local | 6 | 0.00980392156862745 |

route-class edge mass：

| adjacent_pair_gap_class | route_class | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 258 | 0.4215686274509804 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 212 | 0.3464052287581699 |
| gap2_twin_adjacent_pair_collision | pure_lower_wing_single_shell | 78 | 0.12745098039215685 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_left_collar | 30 | 0.049019607843137254 |
| gap4_cousin_adjacent_pair_collision | pure_upper_wing_single_shell | 22 | 0.03594771241830065 |
| gap2_twin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | pure_lower_wing_single_shell | 6 | 0.00980392156862745 |

route-superclass A-class edge mass：

| adjacent_pair_gap_class | route_superclass | A_class | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | mixed_positive_negative | 290 | 0.4738562091503268 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | mixed_positive_negative | 288 | 0.47058823529411764 |
| gap4_cousin_adjacent_pair_collision | wing_single_P_local | mixed_positive_negative | 16 | 0.026143790849673203 |
| gap4_cousin_adjacent_pair_collision | wing_single_P_local | all_positive | 12 | 0.0196078431372549 |
| gap2_twin_adjacent_pair_collision | right_tail_single_P_local | mixed_positive_negative | 6 | 0.00980392156862745 |

route-superclass cycle-length edge mass：

| adjacent_pair_gap_class | route_superclass | cycle_length | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 5 | 110 | 0.17973856209150327 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 5 | 100 | 0.16339869281045752 |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 4 | 88 | 0.1437908496732026 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 6 | 72 | 0.11764705882352941 |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 6 | 48 | 0.0784313725490196 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 4 | 40 | 0.06535947712418301 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 8 | 32 | 0.05228758169934641 |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 3 | 30 | 0.049019607843137254 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 7 | 28 | 0.0457516339869281 |
| gap4_cousin_adjacent_pair_collision | wing_single_P_local | 8 | 16 | 0.026143790849673203 |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 7 | 14 | 0.02287581699346405 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 3 | 12 | 0.0196078431372549 |
| gap4_cousin_adjacent_pair_collision | wing_single_P_local | 3 | 12 | 0.0196078431372549 |
| gap2_twin_adjacent_pair_collision | right_tail_single_P_local | 3 | 6 | 0.00980392156862745 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 2 | 4 | 0.006535947712418301 |

route-superclass P-band edge mass：

| adjacent_pair_gap_class | route_superclass | P_band | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 700<=P<900 | 142 | 0.23202614379084968 |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | P<700 | 120 | 0.19607843137254902 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | P>=900 | 116 | 0.1895424836601307 |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 700<=P<900 | 106 | 0.17320261437908496 |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | P>=900 | 64 | 0.10457516339869281 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | P<700 | 30 | 0.049019607843137254 |
| gap4_cousin_adjacent_pair_collision | wing_single_P_local | 700<=P<900 | 16 | 0.026143790849673203 |
| gap4_cousin_adjacent_pair_collision | wing_single_P_local | P<700 | 12 | 0.0196078431372549 |
| gap2_twin_adjacent_pair_collision | right_tail_single_P_local | P>=900 | 6 | 0.00980392156862745 |

duplicate raw-base rows：

| adjacent_pair_gap_class | route_superclass | template_count | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 2 | 20 | 0.032679738562091505 |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | 2 | 16 | 0.026143790849673203 |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | 2 | 12 | 0.0196078431372549 |

最高 gap2/gap4 templates：

| adjacent_pair_gap_class | route_superclass | route_class | P | packet_index | edge_mass | cycle_length | m_pair | q_prefix_count | m_shell_prime_count | A_class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_two_sided_collar | 809 | 3316 | 16 | 8 | [739, 743] | 24 | 6 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_two_sided_collar | 971 | 4742 | 16 | 8 | [907, 911] | 28 | 5 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 829 | 3622 | 16 | 8 | [1303, 1307] | 19 | 9 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 613 | 1948 | 14 | 7 | [1049, 1051] | 9 | 2 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_two_sided_collar | 919 | 4307 | 14 | 7 | [883, 887] | 27 | 6 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_two_sided_collar | 977 | 4807 | 14 | 7 | [877, 881] | 23 | 8 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 821 | 3443 | 12 | 6 | [1319, 1321] | 16 | 3 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 823 | 3502 | 12 | 6 | [1289, 1291] | 17 | 9 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 883 | 4082 | 12 | 6 | [1487, 1489] | 12 | 8 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 1009 | 5099 | 12 | 6 | [1481, 1483] | 27 | 6 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_two_sided_collar | 733 | 2788 | 12 | 6 | [673, 677] | 25 | 3 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_two_sided_collar | 769 | 3101 | 12 | 6 | [823, 827] | 28 | 5 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_two_sided_collar | 823 | 3478 | 12 | 6 | [937, 941] | 16 | 4 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_left_collar | 883 | 4061 | 12 | 6 | [769, 773] | 21 | 2 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_left_collar | 937 | 4419 | 12 | 6 | [769, 773] | 14 | 2 | mixed_positive_negative |
| gap4_cousin_adjacent_pair_collision | right_tail_single_P_local | pure_right_tail_two_sided_collar | 947 | 4550 | 12 | 6 | [877, 881] | 26 | 10 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_lower_wing_single_shell | 607 | 1882 | 10 | 5 | [431, 433] | 20 | 2 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 613 | 1957 | 10 | 5 | [881, 883] | 20 | 4 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 617 | 1994 | 10 | 5 | [1019, 1021] | 10 | 6 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 617 | 1994 | 10 | 5 | [1031, 1033] | 10 | 6 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_lower_wing_single_shell | 677 | 2432 | 10 | 5 | [431, 433] | 14 | 2 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_lower_wing_single_shell | 773 | 3131 | 10 | 5 | [461, 463] | 11 | 4 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_upper_wing_single_shell | 883 | 4084 | 10 | 5 | [1427, 1429] | 15 | 5 | mixed_positive_negative |
| gap2_twin_adjacent_pair_collision | wing_single_P_local | pure_lower_wing_single_shell | 887 | 4106 | 10 | 5 | [659, 661] | 32 | 3 | mixed_positive_negative |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| AdjacentPrimePairExactGapLedgerImported | True | True | The adjacent-prime-pair exact-gap ledger is imported. | none for import |
| Gap2Gap4RouteSuperclassLedger | True | True | Gap2/gap4 adjacent-pair collisions are split by route-superclass. | none for the finite route-superclass ledger |
| Gap2WingTwinAdjacentPairCollisionBound | False | False | Control the dominant wing carrier for gap-2 adjacent pairs. | finite audit shows 32 templates / 290 edge mass but no global theorem |
| Gap4RightTailCousinAdjacentPairCollisionBound | False | False | Control the dominant right-tail carrier for gap-4 adjacent pairs. | finite audit shows 28 templates / 288 edge mass but no global theorem |
| Gap2Gap4OffdominantResidualBound | False | False | Control the residual gap2-tail and gap4-wing carriers. | finite audit shows 34 residual edge mass but no global suppression theorem |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=still need a completed nonlocal trace family; they do not bound one fixed gap2-wing or gap4-tail packet
prime_gap_theorems=classify or produce prime gaps but do not control route-superclass signed template equality
short_interval_prime_inputs=do not estimate this finite local collision carrier
```

结论：gap2/gap4 主量已被拆成 gap2-wing、gap2-right-tail、gap4-right-tail、gap4-wing
四个 route-superclass carrier。该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
LocalCycleLengthUniformBound
AND Gap2WingTwinAdjacentPairCollisionBound
AND Gap2RightTailTwinResidualCollisionBound
AND Gap4RightTailCousinAdjacentPairCollisionBound
AND Gap4WingCousinResidualCollisionBound
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
single_P_local_gap2_gap4_route_superclass_ledger_closed=true
gap2_wing_twin_collision_bound_proved=false
gap2_right_tail_twin_residual_bound_proved=false
gap4_right_tail_cousin_collision_bound_proved=false
gap4_wing_cousin_residual_bound_proved=false
gap2_twin_adjacent_pair_collision_bound_proved=false
gap4_cousin_adjacent_pair_collision_bound_proved=false
adjacent_prime_pair_collision_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
