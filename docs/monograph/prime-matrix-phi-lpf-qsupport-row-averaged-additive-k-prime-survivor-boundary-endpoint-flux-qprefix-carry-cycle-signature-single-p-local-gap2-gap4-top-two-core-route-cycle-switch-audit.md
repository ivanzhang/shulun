# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core route-cycle-switch 审计

**状态：** `top_two_core_route_cycle_switch_ledger_closed_atom_bounds_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=cycle 4/5/6 and sign-switch <=3 core inside the top-two exact routes
operation=split the 270 edge mass by route, cycle length, and sign-switch count
dominant_shape=the core splits into 11 route-cycle-switch atoms; the largest atom has edge mass 70
remaining=prove one of the atom collision bounds, aggregate atoms through PDEC/SAE, or complete the endpoint trace family
```

## 2. core route-cycle-switch 分类审计

```text
max_prime=1009
top_two_core_route_cycle_switch_ledger_closed=true
core_definition=cycle_length in {4,5,6} and sign_switch_count <= 3
core_template_count=29
core_edge_mass=270
core_edge_ratio_inside_top_two=0.574468085106383
noncore_top_two_edge_mass=200
route_cycle_switch_atom_count=11
largest_route_cycle_switch_atom_edge_mass=70
largest_route_cycle_switch_atom_ratio_inside_core=0.25925925925925924
gap2_upper_wing_core_edge_mass=140
gap4_right_tail_two_sided_core_edge_mass=130
cycle5_core_edge_mass=150
cycle4_core_edge_mass=96
cycle6_core_edge_mass=24
sign_switch3_core_edge_mass=146
sign_switch1_core_edge_mass=64
sign_switch2_core_edge_mass=60
all_core_templates_pairwise_occurrence=true
all_core_templates_mixed_positive_negative=true
row_column_unconditional_closed=false
```

route edge mass：

| route_label | template_count | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| gap2_upper_wing | 15 | 140 | 0.5185185185185185 |
| gap4_right_tail_two_sided | 14 | 130 | 0.48148148148148145 |

route-cycle-switch atom edge mass：

| route_label | cycle_length | sign_switch_count | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap4_right_tail_two_sided | 5 | 3 | 70 | 0.25925925925925924 |
| gap2_upper_wing | 4 | 2 | 40 | 0.14814814814814814 |
| gap2_upper_wing | 6 | 3 | 24 | 0.08888888888888889 |
| gap4_right_tail_two_sided | 4 | 3 | 24 | 0.08888888888888889 |
| gap2_upper_wing | 5 | 1 | 20 | 0.07407407407407407 |
| gap2_upper_wing | 5 | 2 | 20 | 0.07407407407407407 |
| gap2_upper_wing | 5 | 3 | 20 | 0.07407407407407407 |
| gap4_right_tail_two_sided | 5 | 1 | 20 | 0.07407407407407407 |
| gap4_right_tail_two_sided | 4 | 1 | 16 | 0.05925925925925926 |
| gap2_upper_wing | 4 | 1 | 8 | 0.02962962962962963 |
| gap2_upper_wing | 4 | 3 | 8 | 0.02962962962962963 |

cycle edge mass：

| cycle_length | edge_mass | edge_ratio |
| --- | --- | --- |
| 5 | 150 | 0.5555555555555556 |
| 4 | 96 | 0.35555555555555557 |
| 6 | 24 | 0.08888888888888889 |

sign-switch edge mass：

| sign_switch_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 3 | 146 | 0.5407407407407407 |
| 1 | 64 | 0.23703703703703705 |
| 2 | 60 | 0.2222222222222222 |

cycle-switch edge mass：

| cycle_length | sign_switch_count | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| 5 | 3 | 90 | 0.3333333333333333 |
| 4 | 2 | 40 | 0.14814814814814814 |
| 5 | 1 | 40 | 0.14814814814814814 |
| 4 | 3 | 32 | 0.11851851851851852 |
| 4 | 1 | 24 | 0.08888888888888889 |
| 6 | 3 | 24 | 0.08888888888888889 |
| 5 | 2 | 20 | 0.07407407407407407 |

q-prefix / m-shell bands：

| q_prefix_band | edge_mass | edge_ratio |
| --- | --- | --- |
| q<=20 | 110 | 0.4074074074074074 |
| q<=10 | 108 | 0.4 |
| q>20 | 52 | 0.1925925925925926 |

| m_shell_band | edge_mass | edge_ratio |
| --- | --- | --- |
| m<=8 | 116 | 0.42962962962962964 |
| m<=4 | 106 | 0.3925925925925926 |
| m>8 | 48 | 0.17777777777777778 |

最高 core templates：

| route_label | P | packet_index | edge_mass | cycle_length | sign_switch_count | sign_word | m_pair | q_prefix_count | m_shell_prime_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gap2_upper_wing | 1009 | 5099 | 12 | 6 | 3 | +-+++- | [1481, 1483] | 27 | 6 |
| gap2_upper_wing | 823 | 3502 | 12 | 6 | 3 | -+-+++ | [1289, 1291] | 17 | 9 |
| gap2_upper_wing | 613 | 1957 | 10 | 5 | 1 | +++-- | [881, 883] | 20 | 4 |
| gap2_upper_wing | 887 | 4138 | 10 | 5 | 1 | +---- | [1451, 1453] | 13 | 11 |
| gap2_upper_wing | 883 | 4084 | 10 | 5 | 2 | +++-+ | [1427, 1429] | 15 | 5 |
| gap2_upper_wing | 907 | 4196 | 10 | 5 | 2 | +---+ | [1619, 1621] | 9 | 6 |
| gap2_upper_wing | 919 | 4324 | 10 | 5 | 3 | -+-++ | [1427, 1429] | 18 | 9 |
| gap2_upper_wing | 617 | 1994 | 10 | 5 | 3 | --+-+ | [1019, 1021] | 10 | 6 |
| gap4_right_tail_two_sided | 613 | 1929 | 10 | 5 | 1 | ++++- | [757, 761] | 7 | 6 |
| gap4_right_tail_two_sided | 727 | 2741 | 10 | 5 | 1 | ---++ | [739, 743] | 29 | 3 |
| gap4_right_tail_two_sided | 619 | 2017 | 10 | 5 | 3 | +-++- | [739, 743] | 10 | 5 |
| gap4_right_tail_two_sided | 773 | 3157 | 10 | 5 | 3 | +-+-- | [823, 827] | 28 | 6 |
| gap4_right_tail_two_sided | 823 | 3485 | 10 | 5 | 3 | +--+- | [859, 863] | 26 | 5 |
| gap4_right_tail_two_sided | 991 | 4931 | 10 | 5 | 3 | -++-+ | [859, 863] | 16 | 7 |
| gap4_right_tail_two_sided | 607 | 1887 | 10 | 5 | 3 | --+-+ | [769, 773] | 7 | 3 |
| gap4_right_tail_two_sided | 739 | 2842 | 10 | 5 | 3 | --+-+ | [757, 761] | 28 | 4 |
| gap4_right_tail_two_sided | 953 | 4601 | 10 | 5 | 3 | --+-+ | [769, 773] | 10 | 4 |
| gap2_upper_wing | 739 | 2851 | 8 | 4 | 1 | -+++ | [1229, 1231] | 12 | 4 |
| gap2_upper_wing | 761 | 3061 | 8 | 4 | 2 | ++-+ | [1277, 1279] | 10 | 9 |
| gap2_upper_wing | 919 | 4324 | 8 | 4 | 2 | +-++ | [1451, 1453] | 18 | 9 |
| gap2_upper_wing | 331 | 531 | 8 | 4 | 2 | +--+ | [461, 463] | 13 | 4 |
| gap2_upper_wing | 659 | 2320 | 8 | 4 | 2 | +--+ | [1019, 1021] | 16 | 4 |
| gap2_upper_wing | 853 | 3735 | 8 | 4 | 2 | +--+ | [1451, 1453] | 13 | 3 |
| gap2_upper_wing | 997 | 5021 | 8 | 4 | 3 | +-+- | [1787, 1789] | 7 | 5 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TopTwoExactRouteSignCycleLedgerImported | True | True | The top-two exact-route sign-cycle ledger is imported. | none for import |
| TopTwoCoreRouteCycleSwitchLedger | True | True | The 270-mass cycle 4/5/6 and switch<=3 core is split into route-cycle-switch atoms. | none for the finite core atom ledger |
| LargestCoreAtomCollisionBound | False | False | Control the largest 70-mass route-cycle-switch atom. | finite audit identifies the atom but gives no global theorem |
| AllCoreAtomCollisionBoundsOrPDEC | False | False | Control all 11 core atoms or route them through PDEC/SAE. | requires signed equality, aggregation, or endpoint trace completion |
| NonCoreTopTwoSignCycleResidual | False | False | Control the remaining 200 edge mass outside the core. | carried forward from the top-two sign-cycle ledger |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=still need completion from route-cycle-switch atoms to a bilinear or trace-family object
prime_gap_theorems=identify possible prime gaps but do not control signed local atom equality
short_interval_prime_inputs=remain above theta=1/2 and do not see fixed endpoint sign-cycle atoms
```

结论：top-two sign-cycle 的 270 核心已被压成 11 个 route-cycle-switch 原子。
该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
LocalCycleLengthUniformBound
AND Gap4RightTailTwoSidedCousinCoreRouteCycleSwitchAtomBound
AND Gap2UpperWingTwinCoreRouteCycleSwitchAtomBound
AND TopTwoNonCoreSignCycleResidualBound
AND Gap2LowerWingTwinCollisionBound
AND Gap2RightTailTwoSidedTwinResidualCollisionBound
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
top_two_core_route_cycle_switch_ledger_closed=true
core_route_cycle_switch_collision_bound_proved=false
largest_core_atom_collision_bound_proved=false
top_two_noncore_residual_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
