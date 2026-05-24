# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two sign-cycle 审计

**状态：** `top_two_exact_route_sign_cycle_ledger_closed_collision_bounds_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=the two largest gap2/gap4 exact route classes
operation=split them by pairwise occurrence, sign word, sign-switch count, and cycle length
dominant_shape=all top-two templates are pairwise mixed-sign occurrences with cycle length at most 8
remaining=prove sign-cycle collision bounds or route each packet to PDEC/SAE
```

## 2. top-two exact-route sign-cycle 分类审计

```text
max_prime=1009
top_two_exact_route_sign_cycle_ledger_closed=true
top_two_exact_route_template_count=48
top_two_exact_route_edge_mass=470
gap4_right_tail_two_sided_edge_mass=258
gap2_upper_wing_edge_mass=212
all_top_two_templates_pairwise_occurrence=true
occurrence_count_two_edge_mass=470
occurrence_count_gt2_edge_mass=0
all_top_two_templates_mixed_positive_negative=true
mixed_positive_negative_edge_mass=470
all_positive_edge_mass=0
cycle_length_min=2
cycle_length_max=8
sign_switch_count_max=6
cycle_4_5_6_edge_mass=362
cycle_4_5_6_edge_ratio=0.7702127659574468
sign_switch_le3_edge_mass=332
sign_switch_le3_edge_ratio=0.7063829787234043
cycle_4_5_6_and_switch_le3_edge_mass=270
cycle_4_5_6_and_switch_le3_edge_ratio=0.574468085106383
row_column_unconditional_closed=false
```

route class edge mass：

| adjacent_pair_gap_class | route_class | template_count | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 25 | 258 | 0.548936170212766 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 23 | 212 | 0.451063829787234 |

cycle-length edge mass：

| cycle_length | edge_mass | edge_ratio |
| --- | --- | --- |
| 5 | 170 | 0.3617021276595745 |
| 4 | 96 | 0.20425531914893616 |
| 6 | 96 | 0.20425531914893616 |
| 7 | 42 | 0.08936170212765958 |
| 8 | 32 | 0.06808510638297872 |
| 3 | 30 | 0.06382978723404255 |
| 2 | 4 | 0.00851063829787234 |

sign-switch edge mass：

| sign_switch_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 3 | 174 | 0.3702127659574468 |
| 1 | 86 | 0.1829787234042553 |
| 2 | 72 | 0.15319148936170213 |
| 5 | 66 | 0.14042553191489363 |
| 4 | 56 | 0.11914893617021277 |
| 6 | 16 | 0.03404255319148936 |

sign-word edge mass：

| sign_word | edge_mass | edge_ratio |
| --- | --- | --- |
| --+-+ | 40 | 0.0851063829787234 |
| +-+-+- | 24 | 0.05106382978723404 |
| +--+ | 24 | 0.05106382978723404 |
| -+-+- | 20 | 0.0425531914893617 |
| +-+- | 16 | 0.03404255319148936 |
| -+-+ | 16 | 0.03404255319148936 |
| -+-++-+- | 16 | 0.03404255319148936 |
| --+-++-+ | 16 | 0.03404255319148936 |
| ++-+-+- | 14 | 0.029787234042553193 |
| -+++-++ | 14 | 0.029787234042553193 |
| -++-+++ | 14 | 0.029787234042553193 |
| +-+++- | 12 | 0.02553191489361702 |
| +-+--+ | 12 | 0.02553191489361702 |
| +-- | 12 | 0.02553191489361702 |
| +--+-+ | 12 | 0.02553191489361702 |
| -+-+++ | 12 | 0.02553191489361702 |
| -+-++- | 12 | 0.02553191489361702 |
| -+-+-+ | 12 | 0.02553191489361702 |
| ++++- | 10 | 0.02127659574468085 |
| +++-+ | 10 | 0.02127659574468085 |
| +++-- | 10 | 0.02127659574468085 |
| +-++- | 10 | 0.02127659574468085 |
| +-+-- | 10 | 0.02127659574468085 |
| +--+- | 10 | 0.02127659574468085 |
| +---+ | 10 | 0.02127659574468085 |
| +---- | 10 | 0.02127659574468085 |
| -++-+ | 10 | 0.02127659574468085 |
| -+-++ | 10 | 0.02127659574468085 |
| ---++ | 10 | 0.02127659574468085 |
| +++- | 8 | 0.01702127659574468 |

cycle-switch edge mass：

| cycle_length | sign_switch_count | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| 5 | 3 | 90 | 0.19148936170212766 |
| 4 | 2 | 40 | 0.0851063829787234 |
| 5 | 1 | 40 | 0.0851063829787234 |
| 6 | 4 | 36 | 0.07659574468085106 |
| 6 | 5 | 36 | 0.07659574468085106 |
| 4 | 3 | 32 | 0.06808510638297872 |
| 7 | 3 | 28 | 0.059574468085106386 |
| 4 | 1 | 24 | 0.05106382978723404 |
| 6 | 3 | 24 | 0.05106382978723404 |
| 5 | 2 | 20 | 0.0425531914893617 |
| 5 | 4 | 20 | 0.0425531914893617 |
| 3 | 1 | 18 | 0.03829787234042553 |
| 8 | 5 | 16 | 0.03404255319148936 |
| 8 | 6 | 16 | 0.03404255319148936 |
| 7 | 5 | 14 | 0.029787234042553193 |
| 3 | 2 | 12 | 0.02553191489361702 |
| 2 | 1 | 4 | 0.00851063829787234 |

route-cycle edge mass：

| adjacent_pair_gap_class | route_class | cycle_length | edge_mass | edge_ratio |
| --- | --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 5 | 100 | 0.2127659574468085 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 5 | 70 | 0.14893617021276595 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 4 | 56 | 0.11914893617021277 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 6 | 48 | 0.10212765957446808 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 6 | 48 | 0.10212765957446808 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 4 | 40 | 0.0851063829787234 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 8 | 32 | 0.06808510638297872 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 7 | 28 | 0.059574468085106386 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 3 | 24 | 0.05106382978723404 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 7 | 14 | 0.029787234042553193 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 3 | 6 | 0.01276595744680851 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 2 | 4 | 0.00851063829787234 |

最高 top-two sign-cycle templates：

| adjacent_pair_gap_class | route_class | P | packet_index | edge_mass | cycle_length | sign_word | sign_switch_count | m_pair | q_prefix_count | m_shell_prime_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 971 | 4742 | 16 | 8 | -+-++-+- | 6 | [907, 911] | 28 | 5 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 809 | 3316 | 16 | 8 | --+-++-+ | 5 | [739, 743] | 24 | 6 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 613 | 1948 | 14 | 7 | -+++-++ | 3 | [1049, 1051] | 9 | 2 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 977 | 4807 | 14 | 7 | ++-+-+- | 5 | [877, 881] | 23 | 8 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 919 | 4307 | 14 | 7 | -++-+++ | 3 | [883, 887] | 27 | 6 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 1009 | 5099 | 12 | 6 | +-+++- | 3 | [1481, 1483] | 27 | 6 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 883 | 4082 | 12 | 6 | +-+-+- | 5 | [1487, 1489] | 12 | 8 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 823 | 3502 | 12 | 6 | -+-+++ | 3 | [1289, 1291] | 17 | 9 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 821 | 3443 | 12 | 6 | -+-++- | 4 | [1319, 1321] | 16 | 3 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 947 | 4550 | 12 | 6 | +-+-+- | 5 | [877, 881] | 26 | 10 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 769 | 3101 | 12 | 6 | +-+--+ | 4 | [823, 827] | 28 | 5 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 823 | 3478 | 12 | 6 | +--+-+ | 4 | [937, 941] | 16 | 4 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 733 | 2788 | 12 | 6 | -+-+-+ | 5 | [673, 677] | 25 | 3 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 883 | 4084 | 10 | 5 | +++-+ | 2 | [1427, 1429] | 15 | 5 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 613 | 1957 | 10 | 5 | +++-- | 1 | [881, 883] | 20 | 4 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 907 | 4196 | 10 | 5 | +---+ | 2 | [1619, 1621] | 9 | 6 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 887 | 4138 | 10 | 5 | +---- | 1 | [1451, 1453] | 13 | 11 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 919 | 4324 | 10 | 5 | -+-++ | 3 | [1427, 1429] | 18 | 9 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 617 | 1994 | 10 | 5 | -+-+- | 4 | [1031, 1033] | 10 | 6 |
| gap2_twin_adjacent_pair_collision | pure_upper_wing_single_shell | 617 | 1994 | 10 | 5 | --+-+ | 3 | [1019, 1021] | 10 | 6 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 613 | 1929 | 10 | 5 | ++++- | 1 | [757, 761] | 7 | 6 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 619 | 2017 | 10 | 5 | +-++- | 3 | [739, 743] | 10 | 5 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 773 | 3157 | 10 | 5 | +-+-- | 3 | [823, 827] | 28 | 6 |
| gap4_cousin_adjacent_pair_collision | pure_right_tail_two_sided_collar | 823 | 3485 | 10 | 5 | +--+- | 3 | [859, 863] | 26 | 5 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| Gap2Gap4ExactRouteClassLedgerImported | True | True | The exact route-class ledger is imported. | none for import |
| TopTwoExactRouteSignCycleLedger | True | True | The two largest exact routes are split by sign/cycle signatures. | none for the finite top-two sign-cycle ledger |
| Gap4RightTailTwoSidedSignCycleCollisionBound | False | False | Control sign-cycle packets inside the largest exact route. | finite audit shows 258 edge mass but no global theorem |
| Gap2UpperWingSignCycleCollisionBound | False | False | Control sign-cycle packets inside the second largest exact route. | finite audit shows 212 edge mass but no global theorem |
| ResidualExactRouteCollisionBounds | False | False | Control lower wing, left collar, and other exact-route residuals. | carried forward from the exact-route ledger |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=still need completion from local sign-cycle words to a usable bilinear family
prime_gap_theorems=do not see the signed word or cycle-length carrier
short_interval_prime_inputs=do not estimate fixed endpoint-packet sign-cycle equality
```

结论：两个最大 exact routes 已被压成 pairwise mixed-sign sign-cycle packets。
该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
LocalCycleLengthUniformBound
AND Gap4RightTailTwoSidedCousinSignCycleCollisionBound
AND Gap2UpperWingTwinSignCycleCollisionBound
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
top_two_exact_route_sign_cycle_ledger_closed=true
gap4_right_tail_two_sided_sign_cycle_bound_proved=false
gap2_upper_wing_sign_cycle_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
