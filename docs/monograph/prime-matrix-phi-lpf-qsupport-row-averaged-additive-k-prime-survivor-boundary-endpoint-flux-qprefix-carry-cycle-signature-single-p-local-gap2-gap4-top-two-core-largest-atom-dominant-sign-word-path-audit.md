# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom dominant-sign-word path 审计

**状态：** `dominant_largest_atom_sign_word_path_ledger_closed_family_bound_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=dominant sign word --+-+ inside the largest core atom
operation=split its 30 edge mass into exact raw-base and signed-child path witnesses
dominant_shape=3 equal-mass path witnesses with distinct raw-base templates and shared gap4/m<=4 structure
remaining=turn the three path witnesses into a uniform family bound or route the family through PDEC/SAE
```

## 2. dominant sign-word path 分类审计

```text
max_prime=1009
dominant_sign_word_path_ledger_closed=true
target_sign_word=--+-+
previous_dominant_sign_word_edge_mass=30
path_template_count=3
path_edge_mass=30
all_path_edge_mass_equals_10=true
all_path_occurrence_count_equals_2=true
all_path_integer_gap_equals_4=true
all_path_m_shell_band_m_le_4=true
all_path_sign_balance_plus2_minus3=true
distinct_raw_base_template_count=3
distinct_signed_child_count=3
distinct_m_pair_count=2
dominant_m_pair=[769, 773]
dominant_m_pair_edge_mass=20
q_prefix_band_q_le_10_edge_mass=20
q_prefix_band_q_gt_20_edge_mass=10
row_column_unconditional_closed=false
```

path witnesses：

| P | P_band | packet_index | edge_mass | integer_gap | occurrence_count | m_pair | q_prefix_count | q_prefix_band | m_shell_prime_count | m_shell_band | raw_base_template | signed_child |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 607 | P<=700 | 1887 | 10 | 4 | 2 | [769, 773] | 7 | q<=10 | 3 | m<=4 | g=2,c=2 -> g=4,c=5 -> g=6,c=7 -> g=8,c=10 -> g=4,c=6 | g=2,c=2,A=negative -> g=4,c=5,A=negative -> g=6,c=7,A=positive -> g=8,c=10,A=negative -> g=4,c=6,A=positive |
| 739 | P<=850 | 2842 | 10 | 4 | 2 | [757, 761] | 28 | q>20 | 4 | m<=4 | g=10,c=10 -> g=6,c=6 -> g=6,c=6 -> g=2,c=2 -> g=6,c=7 | g=10,c=10,A=negative -> g=6,c=6,A=negative -> g=6,c=6,A=positive -> g=2,c=2,A=negative -> g=6,c=7,A=positive |
| 953 | P>850 | 4601 | 10 | 4 | 2 | [769, 773] | 10 | q<=10 | 4 | m<=4 | g=10,c=8 -> g=8,c=6 -> g=6,c=5 -> g=4,c=3 -> g=8,c=7 | g=10,c=8,A=negative -> g=8,c=6,A=negative -> g=6,c=5,A=positive -> g=4,c=3,A=negative -> g=8,c=7,A=positive |

m-pair and q-prefix subledgers：

| m_pair | edge_mass | edge_ratio |
| --- | --- | --- |
| [769, 773] | 20 | 0.6666666666666666 |
| [757, 761] | 10 | 0.3333333333333333 |

| q_prefix_band | edge_mass | edge_ratio |
| --- | --- | --- |
| q<=10 | 20 | 0.6666666666666666 |
| q>20 | 10 | 0.3333333333333333 |

raw-base templates：

| raw_base_template | edge_mass | edge_ratio |
| --- | --- | --- |
| g=10,c=10 -> g=6,c=6 -> g=6,c=6 -> g=2,c=2 -> g=6,c=7 | 10 | 0.3333333333333333 |
| g=10,c=8 -> g=8,c=6 -> g=6,c=5 -> g=4,c=3 -> g=8,c=7 | 10 | 0.3333333333333333 |
| g=2,c=2 -> g=4,c=5 -> g=6,c=7 -> g=8,c=10 -> g=4,c=6 | 10 | 0.3333333333333333 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LargestAtomTemplateWitnessLedgerImported | True | True | The 7-witness largest atom ledger is imported. | none for import |
| DominantSignWordPathLedger | True | True | The --+-+ subfamily is split into three path witnesses. | none for the finite path ledger |
| DominantSignWordUniformFamilyBound | False | False | Control the three path witnesses as a uniform family. | finite audit gives exact paths but no global theorem |
| OtherLargestAtomTemplateWitnessFamilyBounds | False | False | Control the other sign-word witnesses inside the largest atom. | carried forward from the 7-witness ledger |
| ResidualCoreAndTopTwoBounds | False | False | Control remaining core atoms and top-two noncore residuals. | carried forward from the core atom ledger |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=need a nonlocal completion from these three path witnesses to a bilinear or trace-family sum
prime_gap_inputs=the gap4 label is structural here but prime-gap existence theorems do not bound signed local equality
short_interval_prime_inputs=theta=0.52 remains above the endpoint half-scale and does not see the path witnesses
```

结论：dominant sign word `--+-+` 已被压成 3 个等质量路径见证。
该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
DominantLargestAtomPathWitnessUniformFamilyBound(--+-+)
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
dominant_sign_word_path_ledger_closed=true
dominant_sign_word_path_family_bound_proved=false
other_largest_atom_template_witness_family_bounds_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
