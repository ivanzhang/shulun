# Prime Matrix Phi-LPF dominant-sign-word repeated-step occurrence splice 审计

**状态：** `repeated_step_occurrence_splice_ledger_closed_family_bound_open`
**核验日期：** `2026-05-25`

## 1. 当前对象

```text
input=the two 739->607 repeated-node P-switch cuts
operation=identify the occurrence on each side of every switch cut
dominant_shape=two same-signed-atom occurrence splices from P739/[757,761] to P607/[769,773]
remaining=prove a uniform bound for same-atom cross-witness occurrence splices or replace them by PDEC/SAE certificates
```

## 2. occurrence splice 审计

```text
max_prime=1009
repeated_step_occurrence_splice_ledger_closed=true
occurrence_splice_count=2
occurrence_splice_mass_total=40
occurrence_splice_endpoint_count=4
occurrence_splice_endpoint_mass=40
occurrence_splice_endpoint_cover_complete=true
all_splices_same_signed_atom=true
all_splices_same_gap_carry=true
all_splices_same_sign=true
all_splices_same_orientation=true
all_splices_739_to_607=true
all_splices_m_pair_delta_12_12=true
all_splices_q_delta_minus_21=true
all_splices_step_rewind=true
step_rewind_total=5
occurrence_splice_uniform_family_bound_proved=false
row_column_unconditional_closed=false
```

summary rows：

| P_transition | mass | ratio |
| --- | --- | --- |
| 739_to_607 | 40 | 1.0 |

| m_pair_delta | mass | ratio |
| --- | --- | --- |
| [12, 12] | 40 | 1.0 |

| q_delta | mass | ratio |
| --- | --- | --- |
| -21 | 40 | 1.0 |

| step_splice_kind | mass | ratio |
| --- | --- | --- |
| rewind | 40 | 1.0 |

| position_transition | mass | ratio |
| --- | --- | --- |
| internal_to_initial | 20 | 0.5 |
| terminal_to_internal | 20 | 0.5 |

splice rows：

| splice_id | switch_node | P_transition | left_q | right_q | m_pair_delta | left_step | right_step | step_splice_kind | position_transition | splice_occurrence_mass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| path_1:splice_after_edge_1 | g=2,c=2,A=negative | 739_to_607 | 28 | 7 | [12, 12] | 4 | 1 | rewind | internal_to_initial | 20 |
| path_2:splice_after_edge_2 | g=6,c=7,A=positive | 739_to_607 | 28 | 7 | [12, 12] | 5 | 3 | rewind | terminal_to_internal | 20 |

occurrence endpoint rows：

| occurrence_key | signed_step_signature | P | step | m_pair | position_class | splice_membership_count | splice_sides |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P607:step1:[769, 773]:above_P | g=2,c=2,A=negative | 607 | 1 | [769, 773] | initial | 1 | ['right'] |
| P607:step3:[769, 773]:above_P | g=6,c=7,A=positive | 607 | 3 | [769, 773] | internal | 1 | ['right'] |
| P739:step4:[757, 761]:above_P | g=2,c=2,A=negative | 739 | 4 | [757, 761] | internal | 1 | ['left'] |
| P739:step5:[757, 761]:above_P | g=6,c=7,A=positive | 739 | 5 | [757, 761] | terminal | 1 | ['left'] |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PSwitchCutImported | True | True | The repeated-node P-switch cut ledger is imported. | none for import |
| OccurrenceSpliceLedger | True | True | Each P-switch cut is resolved into its left and right repeated-step occurrences. | none for the finite occurrence-splice ledger |
| SameAtomCrossWitnessSpliceDetected | True | True | Every splice keeps the same signed atom but changes P, q, m-pair and step slot. | uniform proof must control cross-witness occurrence splices |
| OccurrenceSpliceUniformFamilyBound | False | False | Control same-atom P739-to-P607 occurrence splices uniformly. | finite occurrence-splice localization gives exact data but no global theorem |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=the occurrence splice is still a two-witness local gluing datum, not a completed bilinear family
prime_gap_inputs=the splice keeps a signed atom but changes witness P/q/m-pair, so it is not a prime-gap existence statement
short_interval_prime_inputs=theta=0.52 does not control same-atom cross-witness occurrence splices
```

结论：P-switch cut 已经进一步局部化为 same signed atom 的 cross-witness occurrence splice。
但这仍只是有限局部拼接账本，不是 uniform family bound。

## 5. 最新最窄口

```text
RepeatedStepSameAtomOccurrenceSpliceUniformBound(two P739-to-P607 splices)
AND RepeatedStepRepeatedNodePSwitchCutUniformBoundOutsideOccurrenceSplice
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
repeated_step_occurrence_splice_ledger_closed=true
occurrence_splice_uniform_family_bound_proved=false
single_occurrence_orbit_repair_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
