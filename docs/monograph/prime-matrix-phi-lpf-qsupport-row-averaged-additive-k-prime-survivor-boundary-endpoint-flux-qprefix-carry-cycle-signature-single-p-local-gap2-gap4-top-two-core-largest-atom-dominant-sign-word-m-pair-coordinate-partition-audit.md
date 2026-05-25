# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom dominant-sign-word m-pair coordinate partition 审计

**状态：** `dominant_sign_word_m_pair_coordinate_partition_ledger_closed_family_bound_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=all three path witnesses of dominant sign word --+-+
operation=split the full 30 edge mass into m-pair/offset/orientation coordinate witnesses
dominant_shape=three mass-10 coordinate witnesses across two m-pairs and two endpoint orientations
remaining=prove a uniform endpoint-coordinate family bound or route the three witnesses through PDEC/SAE
```

## 2. m-pair coordinate partition 审计

```text
max_prime=1009
dominant_sign_word_m_pair_coordinate_partition_ledger_closed=true
target_sign_word=--+-+
path_template_count=3
path_edge_mass=30
all_path_edge_mass_equals_10=true
all_path_integer_gap_equals_4=true
all_path_occurrence_count_equals_2=true
all_path_m_shell_band_m_le_4=true
all_path_cycle_length_equals_5=true
all_path_sign_word_is_target=true
distinct_m_pair_count=2
dominant_m_pair=[769, 773]
dominant_m_pair_edge_mass=20
residual_singleton_m_pair=[757, 761]
residual_singleton_m_pair_edge_mass=10
residual_singleton_coordinate_closed=true
above_P_edge_mass=20
below_P_edge_mass=10
q_prefix_band_q_le_10_edge_mass=20
q_prefix_band_q_gt_20_edge_mass=10
distinct_coordinate_fingerprint_count=3
row_column_unconditional_closed=false
```

coordinate witnesses：

| witness_id | P | P_band | packet_index | edge_mass | m_pair | endpoint_orientation | m_offsets_from_P | q_prefix_count | q_prefix_band | m_shell_prime_count | sign_word | sign_switch_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P607_packet1887_q7_mpair_769_773 | 607 | P<=700 | 1887 | 10 | [769, 773] | above_P | [162, 166] | 7 | q<=10 | 3 | --+-+ | 3 |
| P739_packet2842_q28_mpair_757_761 | 739 | P<=850 | 2842 | 10 | [757, 761] | above_P | [18, 22] | 28 | q>20 | 4 | --+-+ | 3 |
| P953_packet4601_q10_mpair_769_773 | 953 | P>850 | 4601 | 10 | [769, 773] | below_P | [-184, -180] | 10 | q<=10 | 4 | --+-+ | 3 |

subledgers：

| m_pair | edge_mass | edge_ratio |
| --- | --- | --- |
| [769, 773] | 20 | 0.6666666666666666 |
| [757, 761] | 10 | 0.3333333333333333 |

| endpoint_orientation | edge_mass | edge_ratio |
| --- | --- | --- |
| above_P | 20 | 0.6666666666666666 |
| below_P | 10 | 0.3333333333333333 |

| q_prefix_band | edge_mass | edge_ratio |
| --- | --- | --- |
| q<=10 | 20 | 0.6666666666666666 |
| q>20 | 10 | 0.3333333333333333 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DominantSignWordPathLedgerImported | True | True | The 3-path dominant sign-word ledger is imported. | none for import |
| DominantMPairEndpointCoordinatePathLedgerImported | True | True | The [769,773] endpoint-coordinate subledger is imported. | none for import |
| ResidualSingletonMPairCoordinateLedger | True | True | The [757,761] singleton witness is fixed at P=739 with offsets [18,22]. | none for the finite singleton coordinate |
| DominantSignWordMPairCoordinatePartitionLedger | True | True | The full --+-+ mass 30 is split into three endpoint-coordinate witnesses. | none for the finite coordinate partition |
| DominantSignWordEndpointCoordinateUniformFamilyBound | False | False | Control the three coordinate witnesses as a uniform family. | finite coordinate partition gives exact witnesses but no global theorem |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=the three fixed coordinate witnesses still need completion into a nonlocal trace or bilinear family
prime_gap_inputs=gap4 adjacency labels remain structural; prime-gap existence theorems do not bound signed template equality
short_interval_prime_inputs=theta=0.52 does not imply a pointwise half-scale endpoint coordinate estimate
```

结论：dominant sign word `--+-+` 的 30 质量已经完整落到 3 个 m-pair endpoint-coordinate witness。
该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
DominantSignWordEndpointCoordinateUniformFamilyBound(--+-+; m_pair partition)
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
dominant_sign_word_m_pair_coordinate_partition_ledger_closed=true
dominant_sign_word_endpoint_coordinate_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
