# Prime Matrix Phi-LPF dominant-sign-word repeated-step P-switch cut 审计

**状态：** `repeated_step_p_switch_cut_ledger_closed_family_bound_open`
**核验日期：** `2026-05-25`

## 1. 当前对象

```text
input=the two mixed-P source-sink graph paths
operation=localize every P-switch to its switch node and adjacent edge pair
dominant_shape=two 739->607 cuts, exactly one at each repeated node
remaining=prove a uniform bound for repeated-node P-switch cuts or replace them by PDEC/SAE certificates
```

## 2. P-switch cut 审计

```text
max_prime=1009
repeated_step_p_switch_cut_ledger_closed=true
path_switch_cut_count=2
switch_node_count=2
switch_nodes=['g=2,c=2,A=negative', 'g=6,c=7,A=positive']
repeated_switch_node_cover_complete=true
neighbor_switch_node_count=0
all_switches_at_repeated_nodes=true
all_switches_high_to_low=true
all_switches_739_to_607=true
switch_pair_edge_mass_total=40
switch_edge_incidence_count=4
switch_edge_incidence_mass=40
switch_edge_unique_count=4
non_switch_edge_unique_count=1
p_switch_cut_uniform_family_bound_proved=false
row_column_unconditional_closed=false
```

summary rows：

| P_transition | mass | ratio |
| --- | --- | --- |
| 739_to_607 | 40 | 1.0 |

| P_direction | mass | ratio |
| --- | --- | --- |
| high_to_low | 40 | 1.0 |

| switch_node_class | mass | ratio |
| --- | --- | --- |
| repeated | 40 | 1.0 |

| switch_role | mass | ratio |
| --- | --- | --- |
| negative_repeated_node_entry_to_exit_cut | 20 | 0.5 |
| positive_repeated_node_bridge_to_exit_cut | 20 | 0.5 |

switch rows：

| switch_id | path_id | switch_node | switch_role | P_transition | P_delta | left_edge_class | right_edge_class | switch_pair_edge_mass | touches_repeated_bridge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| path_1:switch_after_edge_1 | path_1 | g=2,c=2,A=negative | negative_repeated_node_entry_to_exit_cut | 739_to_607 | -132 | neighbor_to_repeated | repeated_to_neighbor | 20 | False |
| path_2:switch_after_edge_2 | path_2 | g=6,c=7,A=positive | positive_repeated_node_bridge_to_exit_cut | 739_to_607 | -132 | repeated_to_repeated | repeated_to_neighbor | 20 | True |

switch node rows：

| node | node_class | switch_count | switch_pair_edge_mass | roles | is_switch_node |
| --- | --- | --- | --- | --- | --- |
| g=2,c=2,A=negative | repeated | 1 | 20 | ['negative_repeated_node_entry_to_exit_cut'] | True |
| g=6,c=7,A=positive | repeated | 1 | 20 | ['positive_repeated_node_bridge_to_exit_cut'] | True |
| g=4,c=5,A=negative | neighbor | 0 | 0 | [] | False |
| g=6,c=6,A=positive | neighbor | 0 | 0 | [] | False |
| g=8,c=10,A=negative | neighbor | 0 | 0 | [] | False |

switch edge rows：

| edge_key | P | edge_class | transition_role | switch_membership_count | switch_incidence_mass | is_switch_edge |
| --- | --- | --- | --- | --- | --- | --- |
| g=2,c=2,A=negative -> g=4,c=5,A=negative | 607 | repeated_to_neighbor | initial_exit | 1 | 10 | True |
| g=2,c=2,A=negative -> g=6,c=7,A=positive | 739 | repeated_to_repeated | repeated_bridge | 1 | 10 | True |
| g=6,c=6,A=positive -> g=2,c=2,A=negative | 739 | neighbor_to_repeated | internal_entry | 1 | 10 | True |
| g=6,c=7,A=positive -> g=8,c=10,A=negative | 607 | repeated_to_neighbor | internal_exit | 1 | 10 | True |
| g=4,c=5,A=negative -> g=6,c=7,A=positive | 607 | neighbor_to_repeated | internal_entry | 0 | 0 | False |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SourceSinkPathCoverImported | True | True | The exact two-path mixed-P source-sink cover is imported. | none for import |
| PSwitchCutLedger | True | True | Every mixed-P path switch is localized to a repeated node and adjacent edge pair. | none for the finite P-switch cut ledger |
| RepeatedNodeSwitchCover | True | True | The two switch nodes are exactly the two repeated nodes. | uniform proof must control repeated-node switch cuts, not just graph paths |
| PSwitchCutUniformFamilyBound | False | False | Control the 739->607 repeated-node switch cuts uniformly. | finite switch-cut localization gives exact data but no global theorem |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=the P-switch cut is still a local repeated-node stitching event, not yet a trace family
prime_gap_inputs=the switch cuts are signed grammar events, not prime-gap existence statements
short_interval_prime_inputs=theta=0.52 does not control these repeated-node 739->607 cuts
```

结论：mixed-P path-cover 的 P-switch cut 已经局部化到两个 repeated nodes。
但该局部 cut 仍不是 trace/Kloosterman 可求和族，也不是单一 P-orbit 修复。

## 5. 最新最窄口

```text
RepeatedStepRepeatedNodePSwitchCutUniformBound(two 739->607 cuts)
AND RepeatedStepMixedPSourceSinkPathCoverUniformBoundOutsideSwitchCuts
AND RepeatedStepDirectedIncidenceGraphUniformBoundOutsidePathCover
AND RepeatedStepUniformFamilyBoundOutsideDirectedIncidenceGraph
AND DominantSignWordStepTransitionUniformFamilyBound(--+-+ grammar outside repeated atoms)
AND OtherLargestAtomTemplateWitnessFamilyBounds
AND OtherCoreRouteCycleSwitchAtomBounds
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
repeated_step_p_switch_cut_ledger_closed=true
p_switch_cut_uniform_family_bound_proved=false
single_p_orbit_repair_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
