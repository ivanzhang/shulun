# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local template multiplicity 审计

**状态：** `single_p_local_template_multiplicity_factor_ledger_closed_uniform_bound_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=single-P local endpoint signed-child templates
operation=factor local template edge mass into cycle length times occurrence count
dominant_shape=almost all width-one templates occur once; repeated templates are sparse and low-mass
remaining=global cycle-length and occurrence-product bounds or a PDEC/SAE return route
```

## 2. local template multiplicity 因式审计

```text
max_prime=1009
single_P_local_template_multiplicity_factor_ledger_closed=true
single_P_local_endpoint_edge_mass=26753
single_P_local_endpoint_template_count=4915
single_occurrence_template_count=4818
single_occurrence_edge_mass=25881
repeated_template_count=97
repeated_template_edge_mass=872
multi_packet_template_count=17
multi_packet_template_edge_mass=136
multi_m_value_template_count=95
multi_m_value_template_edge_mass=856
high_edge_gt12_template_count=10
high_edge_gt12_edge_mass=146
template_edge_mass_min/median/max=1/5/16
cycle_length_min/median/max=1/5/14
occurrence_count_min/median/max=1/1/4
observed_template_edge_mass_le_16=true
observed_occurrence_count_le_4=true
observed_cycle_length_le_14=true
row_column_unconditional_closed=false
```

occurrence template count：

| occurrence_count | template_count | template_ratio |
| --- | --- | --- |
| 1 | 4818 | 0.980264496439471 |
| 2 | 93 | 0.018921668362156665 |
| 3 | 3 | 0.0006103763987792472 |
| 4 | 1 | 0.0002034587995930824 |

occurrence edge mass：

| occurrence_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 1 | 25881 | 0.9674055246140619 |
| 2 | 828 | 0.030949800022427393 |
| 3 | 36 | 0.0013456434792359735 |
| 4 | 8 | 0.00029903188427466077 |

cycle length template count：

| cycle_length | template_count | template_ratio |
| --- | --- | --- |
| 5 | 1199 | 0.2439471007121058 |
| 4 | 1178 | 0.23967446592065106 |
| 6 | 945 | 0.19226856561546288 |
| 7 | 654 | 0.13306205493387588 |
| 3 | 420 | 0.08545269582909461 |
| 8 | 249 | 0.05066124109867752 |
| 9 | 117 | 0.023804679552390642 |
| 2 | 62 | 0.01261444557477111 |
| 10 | 59 | 0.01200406917599186 |
| 11 | 19 | 0.0038657171922685655 |
| 12 | 8 | 0.0016276703967446592 |
| 1 | 3 | 0.0006103763987792472 |
| 13 | 1 | 0.0002034587995930824 |
| 14 | 1 | 0.0002034587995930824 |

packet support edge mass：

| packet_support_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 1 | 26617 | 0.9949164579673307 |
| 2 | 136 | 0.0050835420326692336 |

m-value support edge mass：

| m_value_support_count | edge_mass | edge_ratio |
| --- | --- | --- |
| 1 | 25897 | 0.9680035883826112 |
| 2 | 812 | 0.03035173625387807 |
| 3 | 36 | 0.0013456434792359735 |
| 4 | 8 | 0.00029903188427466077 |

cycle-occurrence factor rows：

| cycle_length | occurrence_count | template_edge_mass | template_count | template_ratio |
| --- | --- | --- | --- | --- |
| 5 | 1 | 5 | 1172 | 0.23845371312309258 |
| 4 | 1 | 4 | 1151 | 0.23418107833163784 |
| 6 | 1 | 6 | 935 | 0.19023397761953204 |
| 7 | 1 | 7 | 650 | 0.13224821973550355 |
| 3 | 1 | 3 | 399 | 0.08118006103763988 |
| 8 | 1 | 8 | 246 | 0.05005086469989827 |
| 9 | 1 | 9 | 117 | 0.023804679552390642 |
| 10 | 1 | 10 | 59 | 0.01200406917599186 |
| 2 | 1 | 2 | 57 | 0.011597151576805697 |
| 4 | 2 | 8 | 26 | 0.005289928789420142 |
| 5 | 2 | 10 | 26 | 0.005289928789420142 |
| 3 | 2 | 6 | 20 | 0.004069175991861648 |
| 11 | 1 | 11 | 19 | 0.0038657171922685655 |
| 6 | 2 | 12 | 10 | 0.002034587995930824 |
| 12 | 1 | 12 | 8 | 0.0016276703967446592 |
| 2 | 2 | 4 | 4 | 0.0008138351983723296 |
| 7 | 2 | 14 | 4 | 0.0008138351983723296 |
| 1 | 1 | 1 | 3 | 0.0006103763987792472 |
| 8 | 2 | 16 | 3 | 0.0006103763987792472 |
| 2 | 4 | 8 | 1 | 0.0002034587995930824 |
| 3 | 3 | 9 | 1 | 0.0002034587995930824 |
| 4 | 3 | 12 | 1 | 0.0002034587995930824 |
| 13 | 1 | 13 | 1 | 0.0002034587995930824 |
| 14 | 1 | 14 | 1 | 0.0002034587995930824 |
| 5 | 3 | 15 | 1 | 0.0002034587995930824 |

最高 local templates：

| signed_child | raw_base_template | P | edge_mass | cycle_length | occurrence_count | packet_support_count | m_value_support_count | route_class | A_class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=positive -> g=4,c=6,A=negative -> g=6,c=9,A=positive -> g=8,c=13,A=negative -> g=4,c=6,A=positive -> g=2,c=3,A=negative | g=10,c=16 -> g=2,c=3 -> g=6,c=10 -> g=4,c=6 -> g=6,c=9 -> g=8,c=13 -> g=4,c=6 -> g=2,c=3 | 829 | 16 | 8 | 2 | 1 | 2 | pure_upper_wing_single_shell | mixed_positive_negative |
| g=10,c=9,A=negative -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive -> g=4,c=3,A=positive -> g=8,c=8,A=negative -> g=4,c=4,A=positive -> g=14,c=13,A=negative | g=10,c=9 -> g=8,c=8 -> g=6,c=5 -> g=6,c=6 -> g=4,c=3 -> g=8,c=8 -> g=4,c=4 -> g=14,c=13 | 971 | 16 | 8 | 2 | 1 | 2 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=2,c=1,A=negative -> g=6,c=6,A=negative -> g=6,c=5,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=positive -> g=4,c=4,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive | g=2,c=1 -> g=6,c=6 -> g=6,c=5 -> g=4,c=4 -> g=2,c=2 -> g=4,c=4 -> g=6,c=5 -> g=6,c=6 | 809 | 16 | 8 | 2 | 1 | 2 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=2,c=2,A=negative -> g=4,c=3,A=negative -> g=6,c=5,A=positive -> g=8,c=6,A=negative -> g=4,c=3,A=positive | g=2,c=2 -> g=4,c=3 -> g=6,c=5 -> g=8,c=6 -> g=4,c=3 | 607 | 15 | 5 | 3 | 2 | 3 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=10,c=10,A=negative -> g=8,c=8,A=positive -> g=10,c=9,A=positive -> g=8,c=8,A=negative -> g=6,c=6,A=positive -> g=4,c=4,A=positive -> g=8,c=7,A=positive | g=10,c=10 -> g=8,c=8 -> g=10,c=9 -> g=8,c=8 -> g=6,c=6 -> g=4,c=4 -> g=8,c=7 | 919 | 14 | 7 | 2 | 1 | 2 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=10,c=17,A=negative -> g=2,c=4,A=positive -> g=4,c=7,A=positive -> g=2,c=3,A=positive -> g=4,c=7,A=negative -> g=14,c=24,A=positive -> g=6,c=10,A=positive | g=10,c=17 -> g=2,c=4 -> g=4,c=7 -> g=2,c=3 -> g=4,c=7 -> g=14,c=24 -> g=6,c=10 | 613 | 14 | 7 | 2 | 1 | 2 | pure_upper_wing_single_shell | mixed_positive_negative |
| g=10,c=9,A=negative -> g=2,c=2,A=positive -> g=4,c=3,A=negative -> g=6,c=5,A=negative -> g=4,c=3,A=positive -> g=2,c=2,A=negative -> g=12,c=10,A=positive | g=10,c=9 -> g=2,c=2 -> g=4,c=3 -> g=6,c=5 -> g=4,c=3 -> g=2,c=2 -> g=12,c=10 | 821 | 14 | 7 | 2 | 2 | 2 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=4,c=3,A=positive -> g=8,c=8,A=positive -> g=6,c=5,A=negative -> g=4,c=4,A=positive -> g=8,c=7,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative | g=4,c=3 -> g=8,c=8 -> g=6,c=5 -> g=4,c=4 -> g=8,c=7 -> g=6,c=5 -> g=6,c=6 | 977 | 14 | 7 | 2 | 1 | 2 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=10,c=10,A=positive -> g=12,c=11,A=negative -> g=2,c=2,A=positive -> g=10,c=9,A=negative -> g=8,c=7,A=positive -> g=6,c=6,A=negative -> g=6,c=6,A=positive -> g=4,c=3,A=positive -> g=8,c=8,A=negative -> g=6,c=5,A=positive -> g=4,c=4,A=negative -> g=8,c=8,A=positive -> g=4,c=3,A=negative -> g=14,c=13,A=negative | g=10,c=10 -> g=12,c=11 -> g=2,c=2 -> g=10,c=9 -> g=8,c=7 -> g=6,c=6 -> g=6,c=6 -> g=4,c=3 -> g=8,c=8 -> g=6,c=5 -> g=4,c=4 -> g=8,c=8 -> g=4,c=3 -> g=14,c=13 | 947 | 14 | 14 | 1 | 1 | 1 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=12,c=12,A=negative -> g=8,c=7,A=positive -> g=4,c=4,A=negative -> g=8,c=8,A=positive -> g=4,c=3,A=positive -> g=6,c=6,A=negative -> g=12,c=12,A=positive -> g=2,c=1,A=negative -> g=18,c=18,A=positive -> g=6,c=5,A=negative -> g=6,c=6,A=positive -> g=2,c=2,A=positive -> g=4,c=3,A=negative | g=12,c=12 -> g=2,c=1 -> g=18,c=18 -> g=6,c=5 -> g=6,c=6 -> g=2,c=2 -> g=4,c=3 -> g=12,c=12 -> g=8,c=7 -> g=4,c=4 -> g=8,c=8 -> g=4,c=3 -> g=6,c=6 | 619 | 13 | 13 | 1 | 1 | 1 | pure_right_tail_left_collar | mixed_positive_negative |
| g=12,c=17,A=negative -> g=4,c=5,A=positive -> g=6,c=9,A=positive -> g=2,c=2,A=negative | g=12,c=17 -> g=4,c=5 -> g=6,c=9 -> g=2,c=2 | 991 | 12 | 4 | 3 | 2 | 3 | pure_upper_wing_single_shell | mixed_positive_negative |
| g=10,c=11,A=positive -> g=2,c=3,A=negative -> g=4,c=4,A=negative -> g=6,c=7,A=positive -> g=2,c=2,A=negative -> g=12,c=14,A=positive | g=10,c=11 -> g=2,c=3 -> g=4,c=4 -> g=6,c=7 -> g=2,c=2 -> g=12,c=14 | 823 | 12 | 6 | 2 | 1 | 2 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=10,c=11,A=positive -> g=6,c=6,A=negative -> g=6,c=7,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=negative -> g=12,c=13,A=positive | g=10,c=11 -> g=6,c=6 -> g=6,c=7 -> g=4,c=4 -> g=2,c=2 -> g=12,c=13 | 769 | 12 | 6 | 2 | 1 | 2 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=10,c=15,A=positive -> g=6,c=9,A=negative -> g=6,c=9,A=positive -> g=2,c=3,A=positive -> g=18,c=27,A=positive -> g=6,c=8,A=negative | g=10,c=15 -> g=6,c=9 -> g=6,c=9 -> g=2,c=3 -> g=18,c=27 -> g=6,c=8 | 1009 | 12 | 6 | 2 | 1 | 2 | pure_upper_wing_single_shell | mixed_positive_negative |
| g=10,c=16,A=negative -> g=2,c=3,A=positive -> g=6,c=10,A=negative -> g=8,c=13,A=positive -> g=4,c=6,A=positive -> g=2,c=3,A=negative | g=10,c=16 -> g=2,c=3 -> g=6,c=10 -> g=8,c=13 -> g=4,c=6 -> g=2,c=3 | 821 | 12 | 6 | 2 | 1 | 2 | pure_upper_wing_single_shell | mixed_positive_negative |
| g=10,c=8,A=negative -> g=8,c=6,A=positive -> g=10,c=9,A=positive -> g=8,c=6,A=negative -> g=6,c=5,A=positive -> g=8,c=7,A=positive | g=10,c=8 -> g=8,c=6 -> g=10,c=9 -> g=8,c=6 -> g=6,c=5 -> g=8,c=7 | 937 | 12 | 6 | 2 | 1 | 2 | pure_right_tail_left_collar | mixed_positive_negative |
| g=10,c=9,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative -> g=2,c=2,A=positive -> g=18,c=16,A=negative -> g=6,c=6,A=positive | g=10,c=9 -> g=6,c=5 -> g=6,c=6 -> g=2,c=2 -> g=18,c=16 -> g=6,c=6 | 733 | 12 | 6 | 2 | 1 | 2 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=10,c=9,A=positive -> g=2,c=1,A=negative -> g=4,c=4,A=negative -> g=6,c=5,A=negative -> g=6,c=5,A=positive -> g=8,c=7,A=positive | g=10,c=9 -> g=2,c=1 -> g=4,c=4 -> g=6,c=5 -> g=6,c=5 -> g=8,c=7 | 883 | 12 | 6 | 2 | 1 | 2 | pure_right_tail_left_collar | mixed_positive_negative |
| g=10,c=9,A=positive -> g=8,c=8,A=negative -> g=6,c=5,A=positive -> g=6,c=6,A=negative -> g=4,c=4,A=positive -> g=8,c=7,A=negative | g=10,c=9 -> g=8,c=8 -> g=6,c=5 -> g=6,c=6 -> g=4,c=4 -> g=8,c=7 | 947 | 12 | 6 | 2 | 1 | 2 | pure_right_tail_two_sided_collar | mixed_positive_negative |
| g=12,c=20,A=positive -> g=8,c=14,A=negative -> g=4,c=7,A=positive -> g=6,c=10,A=negative -> g=8,c=13,A=positive -> g=4,c=7,A=negative | g=12,c=20 -> g=8,c=14 -> g=4,c=7 -> g=6,c=10 -> g=8,c=13 -> g=4,c=7 | 883 | 12 | 6 | 2 | 1 | 2 | pure_upper_wing_single_shell | mixed_positive_negative |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SinglePLocalEndpointStructureImported | True | True | The previous single-P local endpoint packet ledger is imported. | none for import |
| LocalTemplateMultiplicityFactorLedger | True | True | Each single-P template edge mass is factored as cycle_length times occurrence_count. | none for the finite factor ledger |
| LocalCycleLengthUniformBound | False | False | Promote the observed cycle-length cap to a global structural bound. | finite audit shows cycle_length<=14 but does not prove it globally |
| LocalOccurrenceMultiplicityUniformBound | False | False | Promote the observed occurrence cap to a global structural bound. | finite audit shows occurrence_count<=4 but does not prove it globally |
| CycleOccurrenceProductBoundOrPDEC | False | False | Control the product cycle_length*occurrence_count, or route excess to PDEC/SAE. | finite audit shows edge_mass<=16 but no global excess-return proof is supplied |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | average trace input; does not prove local occurrence multiplicity for a width-one template |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | requires extracted Kloosterman variables, not just a local signed cycle template |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced average input; not a local template occurrence bound |
| Xu_Zhang_2026_generalized_kloosterman_arbitrary_sets | https://doi.org/10.1016/j.jnt.2025.09.027 | published arbitrary-set bilinear input; still not a local cycle occurrence theorem |

```text
trace_Kloosterman_average_inputs=do not prove local cycle occurrence multiplicity without a completed averaging variable
Xu_Zhang_arbitrary_sets=requires explicit finite-field sets; not a local signed-cycle multiplicity theorem
```

结论：local template multiplicity 已被拆成 cycle length、occurrence count
与二者乘积三个门。该账本仍是有限结构结果，尚未给出全局均匀界。

## 5. 最新最窄口

```text
LocalCycleLengthUniformBound
AND LocalOccurrenceMultiplicityUniformBound
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
single_P_local_template_multiplicity_factor_ledger_closed=true
local_cycle_length_uniform_bound_proved=false
local_occurrence_multiplicity_uniform_bound_proved=false
cycle_occurrence_product_bound_proved=false
local_template_multiplicity_uniform_bound_proved=false
single_P_slice_endpoint_packet_summation_closed=false
single_P_local_endpoint_packet_bound_closed=false
multi_P_trace_completion_closed=false
pure_endpoint_carrier_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
