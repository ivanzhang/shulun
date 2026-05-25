# Prime Matrix Phi-LPF dominant-sign-word repeated-step source-sink path cover 审计

**状态：** `repeated_step_source_sink_path_cover_ledger_closed_family_bound_open`
**核验日期：** `2026-05-25`

## 1. 当前对象

```text
input=the 5-edge acyclic repeated-step directed incidence graph
operation=enumerate source-sink graph paths and classify shared/branch/bridge edges
dominant_shape=two source-sink graph paths, both mixed-P, with a branch-join diamond between the repeated nodes
remaining=turn mixed-P graph stitching into a uniform family bound or replace it by a PDEC/SAE certificate
```

## 2. source-sink path cover 审计

```text
max_prime=1009
repeated_step_source_sink_path_cover_ledger_closed=true
source_node=g=6,c=6,A=positive
sink_node=g=8,c=10,A=negative
source_sink_path_count=2
source_sink_path_edge_incidence_count=7
source_sink_path_edge_incidence_mass=70
edge_cover_complete=true
shared_edge_count=2
shared_edge_mass=20
shared_edge_path_incidence_mass=40
single_witness_source_sink_path_count=0
mixed_witness_source_sink_path_count=2
all_source_sink_paths_mixed_P=true
all_source_sink_paths_have_one_P_switch=true
diamond_decomposition_closed=true
single_witness_orbit_interpretation_valid=false
row_column_unconditional_closed=false
```

path-kind and witness-support summaries：

| path_kind | mass | ratio |
| --- | --- | --- |
| long_neighbor_corridor | 40 | 0.5714285714285714 |
| bridge_shortcut_corridor | 30 | 0.42857142857142855 |

| witness_support | mass | ratio |
| --- | --- | --- |
| mixed_P | 70 | 1.0 |

| bridge_usage | mass | ratio |
| --- | --- | --- |
| avoids_bridge | 40 | 0.5714285714285714 |
| uses_bridge | 30 | 0.42857142857142855 |

source-sink path rows：

| path_id | path_kind | edge_count | path_edge_mass | P_sequence | P_support | P_switch_count | single_witness_path | uses_repeated_bridge | path_signature |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| path_1 | long_neighbor_corridor | 4 | 40 | [739, 607, 607, 607] | [607, 739] | 1 | False | False | g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=4,c=5,A=negative -> g=6,c=7,A=positive -> g=8,c=10,A=negative |
| path_2 | bridge_shortcut_corridor | 3 | 30 | [739, 739, 607] | [607, 739] | 1 | False | True | g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=6,c=7,A=positive -> g=8,c=10,A=negative |

edge membership rows：

| edge_key | edge_class | edge_mass | path_membership_count | path_incidence_mass | shared_by_all_paths | path_ids |
| --- | --- | --- | --- | --- | --- | --- |
| g=6,c=6,A=positive -> g=2,c=2,A=negative | neighbor_to_repeated | 10 | 2 | 20 | True | ['path_1', 'path_2'] |
| g=6,c=7,A=positive -> g=8,c=10,A=negative | repeated_to_neighbor | 10 | 2 | 20 | True | ['path_1', 'path_2'] |
| g=2,c=2,A=negative -> g=4,c=5,A=negative | repeated_to_neighbor | 10 | 1 | 10 | False | ['path_1'] |
| g=2,c=2,A=negative -> g=6,c=7,A=positive | repeated_to_repeated | 10 | 1 | 10 | False | ['path_2'] |
| g=4,c=5,A=negative -> g=6,c=7,A=positive | neighbor_to_repeated | 10 | 1 | 10 | False | ['path_1'] |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DirectedIncidenceGraphImported | True | True | The 5-node repeated-step DAG is imported. | none for import |
| SourceSinkPathCoverLedger | True | True | All source-sink graph paths and edge memberships are enumerated. | none for the finite path-cover ledger |
| MixedPWitnessStitchingDetected | True | True | Every source-sink graph path mixes P=607 and P=739. | uniform proof must not treat graph paths as single-witness orbits |
| SourceSinkPathCoverUniformFamilyBound | False | False | Control the mixed-P source-sink path cover uniformly. | finite path cover gives exact stitching data but no global theorem |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=mixed-P graph stitching is not yet a completed trace, bilinear, or Kloosterman family
prime_gap_inputs=the source-sink graph paths are signature paths, not prime-gap existence statements
short_interval_prime_inputs=theta=0.52 does not produce a half-scale or mixed-P stitching estimate here
```

结论：source-sink path cover 已经闭合，但两条图路径均为 mixed-P stitching。
因此不能把图路径解释为单一 witness orbit；这正是新的有限硬点边界。

## 5. 最新最窄口

```text
RepeatedStepMixedPSourceSinkPathCoverUniformBound(two mixed-P graph paths)
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
repeated_step_source_sink_path_cover_ledger_closed=true
repeated_step_source_sink_path_cover_family_bound_proved=false
single_witness_orbit_interpretation_valid=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
