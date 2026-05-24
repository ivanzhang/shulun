# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom dominant-sign-word dominant-m-pair path 审计

**状态：** `dominant_m_pair_endpoint_coordinate_path_ledger_closed_family_bound_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=dominant m-pair [769,773] inside sign word --+-+
operation=split its 20 edge mass into exact endpoint coordinate path witnesses
dominant_shape=two mass-10 witnesses: one above-P endpoint path and one below-P endpoint path
remaining=prove a uniform endpoint-coordinate family bound or route the two witnesses through PDEC/SAE
```

## 2. dominant m-pair endpoint-coordinate 审计

```text
max_prime=1009
dominant_m_pair_endpoint_coordinate_path_ledger_closed=true
target_sign_word=--+-+
target_m_pair=[769, 773]
previous_dominant_m_pair_edge_mass=20
endpoint_coordinate_witness_count=2
endpoint_coordinate_edge_mass=20
all_endpoint_edge_mass_equals_10=true
all_endpoint_integer_gap_equals_4=true
all_endpoint_occurrence_count_equals_2=true
all_endpoint_q_prefix_band_q_le_10=true
all_endpoint_m_shell_band_m_le_4=true
all_endpoint_cycle_length_equals_5=true
all_endpoint_sign_word_is_target=true
all_endpoint_sign_switch_count_equals_3=true
all_endpoint_sign_balance_plus2_minus3=true
distinct_raw_base_template_count=2
distinct_signed_child_count=2
row_column_unconditional_closed=false
```

endpoint coordinate witnesses：

| witness_id | P | P_band | packet_index | edge_mass | endpoint_orientation | m_pair | m_offsets_from_P | integer_gap | q_prefix_count | m_shell_prime_count | sign_word | sign_switch_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P607_packet1887_q7_mpair_769_773 | 607 | P<=700 | 1887 | 10 | above_P | [769, 773] | [162, 166] | 4 | 7 | 3 | --+-+ | 3 |
| P953_packet4601_q10_mpair_769_773 | 953 | P>850 | 4601 | 10 | below_P | [769, 773] | [-184, -180] | 4 | 10 | 4 | --+-+ | 3 |

orientation and q-prefix subledgers：

| endpoint_orientation | edge_mass | edge_ratio |
| --- | --- | --- |
| above_P | 10 | 0.5 |
| below_P | 10 | 0.5 |

| q_prefix_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 10 | 10 | 0.5 |
| 7 | 10 | 0.5 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DominantSignWordPathLedgerImported | True | True | The 3-path dominant sign-word ledger is imported. | none for import |
| DominantMPairEndpointCoordinatePathLedger | True | True | The [769,773] mass-20 block is split into two endpoint coordinate witnesses. | none for the finite coordinate ledger |
| DominantMPairEndpointCoordinateUniformFamilyBound | False | False | Control the two coordinate witnesses as a uniform family. | finite coordinate audit gives exact witnesses but no global theorem |
| OtherDominantSignWordMPairBound | False | False | Control the non-dominant m-pair [757,761] witness in the sign word. | carried forward from the 3-path ledger |
| OtherLargestAtomTemplateWitnessFamilyBounds | False | False | Control the other sign-word witnesses inside the largest atom. | carried forward from the 7-witness ledger |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=the two endpoint coordinate witnesses still need a nonlocal completion into a trace or bilinear family
prime_gap_inputs=the fixed m-pair gap4 label is structural and is not controlled by prime-gap existence theorems
short_interval_prime_inputs=theta=0.52 does not yield a fixed [769,773] endpoint signed equality estimate
```

结论：dominant m-pair `[769, 773]` 已被压成 2 个端点坐标路径见证。
该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
DominantMPairEndpointCoordinateUniformFamilyBound([769,773])
AND OtherDominantSignWordMPairBound([757,761])
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
dominant_m_pair_endpoint_coordinate_path_ledger_closed=true
dominant_m_pair_endpoint_coordinate_family_bound_proved=false
dominant_sign_word_path_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
