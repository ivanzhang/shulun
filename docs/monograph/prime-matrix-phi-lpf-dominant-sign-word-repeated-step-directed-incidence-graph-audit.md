# Prime Matrix Phi-LPF dominant-sign-word repeated-step directed-incidence graph 审计

**状态：** `repeated_step_directed_incidence_graph_ledger_closed_family_bound_open`
**核验日期：** `2026-05-25`

## 1. 当前对象

```text
input=five touching transitions around two repeated signed step atoms
operation=view touching transitions as a directed incidence graph
dominant_shape=one acyclic weak component with two repeated nodes, three neighbor nodes, and one repeated-to-repeated bridge
remaining=upgrade the finite acyclic carrier to a uniform directed-incidence family bound or PDEC/SAE certificate
```

## 2. directed incidence graph 审计

```text
max_prime=1009
repeated_step_directed_incidence_graph_ledger_closed=true
node_count=5
repeated_node_count=2
neighbor_node_count=3
directed_edge_count=5
directed_edge_mass=50
repeated_endpoint_incidence_count=6
repeated_endpoint_incidence_mass=60
weak_component_count=1
directed_acyclic=true
source_nodes=['g=6,c=6,A=positive']
sink_nodes=['g=8,c=10,A=negative']
longest_directed_path_length=4
longest_directed_path_nodes=['g=6,c=6,A=positive', 'g=2,c=2,A=negative', 'g=4,c=5,A=negative', 'g=6,c=7,A=positive', 'g=8,c=10,A=negative']
cross_repeated_bridge_edge_count=1
cross_repeated_bridge_edge_mass=10
row_column_unconditional_closed=false
```

edge-class and role summaries：

| edge_class | mass | ratio |
| --- | --- | --- |
| neighbor_to_repeated | 20 | 0.4 |
| repeated_to_neighbor | 20 | 0.4 |
| repeated_to_repeated | 10 | 0.2 |

| transition_role | mass | ratio |
| --- | --- | --- |
| internal_entry | 20 | 0.4 |
| initial_exit | 10 | 0.2 |
| internal_exit | 10 | 0.2 |
| repeated_bridge | 10 | 0.2 |

| sign_pair | mass | ratio |
| --- | --- | --- |
| +- | 20 | 0.4 |
| -+ | 20 | 0.4 |
| -- | 10 | 0.2 |

node rows：

| node | node_class | in_degree | out_degree | total_degree | in_mass | out_mass | is_source | is_sink | occurrence_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g=2,c=2,A=negative | repeated | 1 | 2 | 3 | 10 | 20 | False | False | ['P607:step1:[769, 773]:above_P', 'P739:step4:[757, 761]:above_P'] |
| g=4,c=5,A=negative | neighbor | 1 | 1 | 2 | 10 | 10 | False | False | [] |
| g=6,c=6,A=positive | neighbor | 0 | 1 | 1 | 0 | 10 | True | False | [] |
| g=6,c=7,A=positive | repeated | 2 | 1 | 3 | 20 | 10 | False | False | ['P607:step3:[769, 773]:above_P', 'P739:step5:[757, 761]:above_P'] |
| g=8,c=10,A=negative | neighbor | 1 | 0 | 1 | 10 | 0 | False | True | [] |

directed edge rows：

| edge_id | m_pair | from_atom | to_atom | edge_class | transition_role | sign_pair | edge_mass | repeated_endpoint_incidence_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P607:step1-2 | [769, 773] | g=2,c=2,A=negative | g=4,c=5,A=negative | repeated_to_neighbor | initial_exit | -- | 10 | 1 |
| P607:step2-3 | [769, 773] | g=4,c=5,A=negative | g=6,c=7,A=positive | neighbor_to_repeated | internal_entry | -+ | 10 | 1 |
| P607:step3-4 | [769, 773] | g=6,c=7,A=positive | g=8,c=10,A=negative | repeated_to_neighbor | internal_exit | +- | 10 | 1 |
| P739:step3-4 | [757, 761] | g=6,c=6,A=positive | g=2,c=2,A=negative | neighbor_to_repeated | internal_entry | +- | 10 | 1 |
| P739:step4-5 | [757, 761] | g=2,c=2,A=negative | g=6,c=7,A=positive | repeated_to_repeated | repeated_bridge | -+ | 10 | 2 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RepeatedStepOccurrenceImported | True | True | The repeated-step occurrence/touching-transition ledger is imported. | none for import |
| DirectedIncidenceGraphLedger | True | True | The five touching transitions form an exact directed node/edge graph. | none for the finite graph ledger |
| AcyclicCarrierLedger | True | True | The finite carrier is a DAG with one source and one sink. | none for the finite acyclicity ledger |
| DirectedIncidenceUniformFamilyBound | False | False | Control this acyclic carrier uniformly in the full Phi-LPF family. | finite graph audit gives exact structure but no global theorem |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=the acyclic finite graph is not yet a complete trace, bilinear, or Kloosterman summation family
prime_gap_inputs=the directed source/sink structure is local grammar data, not a prime-gap existence result
short_interval_prime_inputs=theta=0.52 remains an external scale bound and does not imply this directed-incidence family estimate
```

结论：repeated-step touching carrier 已经闭合为一个有限有向无环图。
该账本仍不是全局 uniform family bound。

## 5. 最新最窄口

```text
RepeatedStepDirectedIncidenceGraphUniformBound(acyclic two-repeated-node carrier)
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
repeated_step_directed_incidence_graph_ledger_closed=true
repeated_step_directed_incidence_graph_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
