# Prime Matrix Phi-LPF q-prefix carry cycle signature pure endpoint phase-interface 审计

**状态：** `pure_endpoint_phase_interface_ledger_closed_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=pure endpoint missing-mirror signed-child templates
operation=single-P versus multi-P phase-interface routing
dominant_shape=pure endpoint mass splits into local single-P packets and multi-P trace candidates
remaining=local packet estimates, multi-P trace/Kloosterman completion, and phase saving
```

## 2. pure endpoint phase-interface 审计

```text
max_prime=1009
pure_endpoint_phase_interface_ledger_closed=true
pure_endpoint_edge_mass=48636
pure_endpoint_template_count=6408
single_P_pure_endpoint_edge_mass=26753
single_P_pure_endpoint_edge_ratio=0.5500657948844477
multi_P_pure_endpoint_edge_mass=21883
multi_P_pure_endpoint_edge_ratio=0.44993420511555227
multi_P_right_tail_pure_endpoint_edge_mass=4901
multi_P_right_tail_pure_endpoint_edge_ratio=0.1007689777119829
multi_P_wing_pure_endpoint_edge_mass=16982
multi_P_wing_pure_endpoint_edge_ratio=0.34916522740356937
P_support_width_min/median/max=1/1.0/54
row_column_unconditional_closed=false
```

phase-interface edge mass：

| phase_interface_class | edge_mass | edge_ratio |
| --- | --- | --- |
| single_P_local_endpoint_packet | 26753 | 0.5500657948844477 |
| multi_P_wing_endpoint_trace_candidate | 16982 | 0.34916522740356937 |
| multi_P_right_tail_endpoint_trace_candidate | 4901 | 0.1007689777119829 |

pure endpoint route edge mass：

| route_class | edge_mass | edge_ratio |
| --- | --- | --- |
| pure_upper_wing_single_shell | 20314 | 0.4176741508347726 |
| pure_right_tail_two_sided_collar | 13310 | 0.2736655974997944 |
| pure_lower_wing_single_shell | 10208 | 0.20988568138827207 |
| pure_right_tail_right_collar | 2347 | 0.04825643556213505 |
| pure_right_tail_left_collar | 1769 | 0.03637223455876305 |
| pure_right_tail_terminal_full_interval | 688 | 0.014145900156262851 |

pure endpoint P-width edge mass：

| P_width_bucket | edge_mass | edge_ratio |
| --- | --- | --- |
| single_P_local_packet | 26753 | 0.5500657948844477 |
| multi_P_width_2_to_4 | 13984 | 0.2875236450365984 |
| multi_P_width_5_to_16 | 6043 | 0.12424952709926804 |
| multi_P_width_17_to_64 | 1856 | 0.03816103297968583 |

pure endpoint A-class edge mass：

| A_class | edge_mass | edge_ratio |
| --- | --- | --- |
| mixed_positive_negative | 47217 | 0.9708240809277079 |
| all_positive | 623 | 0.01280944156591825 |
| mixed_with_zero | 404 | 0.008306604161526442 |
| all_negative | 392 | 0.008059873344847437 |

最高 pure endpoint templates：

| signed_child | raw_base_template | edge_mass | route_class | phase_interface_class | A_class | P_support_width | P_width_bucket |
| --- | --- | --- | --- | --- | --- | --- | --- |
| g=2,c=4,A=positive -> g=4,c=6,A=negative | g=2,c=4 -> g=4,c=6 | 208 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 50 | multi_P_width_17_to_64 |
| g=2,c=2,A=positive -> g=4,c=2,A=negative | g=2,c=2 -> g=4,c=2 | 202 | pure_lower_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 54 | multi_P_width_17_to_64 |
| g=4,c=2,A=negative -> g=8,c=6,A=positive | g=4,c=2 -> g=8,c=6 | 124 | pure_lower_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 36 | multi_P_width_17_to_64 |
| g=4,c=6,A=negative -> g=8,c=14,A=positive | g=4,c=6 -> g=8,c=14 | 124 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 29 | multi_P_width_17_to_64 |
| g=4,c=7,A=positive -> g=8,c=12,A=negative | g=4,c=7 -> g=8,c=12 | 122 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 32 | multi_P_width_17_to_64 |
| g=4,c=6,A=positive -> g=6,c=8,A=negative -> g=8,c=12,A=negative | g=4,c=6 -> g=6,c=8 -> g=8,c=12 | 117 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 27 | multi_P_width_17_to_64 |
| g=4,c=7,A=positive -> g=6,c=9,A=negative | g=4,c=7 -> g=6,c=9 | 94 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 27 | multi_P_width_17_to_64 |
| g=4,c=2,A=negative -> g=6,c=5,A=positive | g=4,c=2 -> g=6,c=5 | 92 | pure_lower_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 34 | multi_P_width_17_to_64 |
| g=2,c=3,A=negative -> g=6,c=9,A=negative -> g=6,c=10,A=positive | g=2,c=3 -> g=6,c=9 -> g=6,c=10 | 81 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 14 | multi_P_width_5_to_16 |
| g=4,c=6,A=positive -> g=6,c=9,A=positive -> g=8,c=11,A=negative | g=4,c=6 -> g=6,c=9 -> g=8,c=11 | 78 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 20 | multi_P_width_17_to_64 |
| g=10,c=16,A=negative -> g=2,c=4,A=positive | g=10,c=16 -> g=2,c=4 | 74 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 21 | multi_P_width_17_to_64 |
| g=4,c=3,A=positive -> g=6,c=4,A=negative -> g=8,c=6,A=positive | g=4,c=3 -> g=6,c=4 -> g=8,c=6 | 72 | pure_lower_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 19 | multi_P_width_17_to_64 |
| g=2,c=2,A=negative -> g=6,c=9,A=positive | g=2,c=2 -> g=6,c=9 | 70 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 27 | multi_P_width_17_to_64 |
| g=10,c=14,A=negative -> g=6,c=8,A=positive -> g=6,c=9,A=negative | g=10,c=14 -> g=6,c=8 -> g=6,c=9 | 69 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 15 | multi_P_width_5_to_16 |
| g=2,c=1,A=positive -> g=6,c=5,A=positive -> g=6,c=4,A=negative | g=2,c=1 -> g=6,c=5 -> g=6,c=4 | 69 | pure_lower_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 17 | multi_P_width_17_to_64 |
| g=2,c=3,A=negative -> g=4,c=8,A=positive | g=2,c=3 -> g=4,c=8 | 68 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 15 | multi_P_width_5_to_16 |
| g=2,c=4,A=positive -> g=6,c=9,A=negative | g=2,c=4 -> g=6,c=9 | 68 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 18 | multi_P_width_17_to_64 |
| g=4,c=3,A=positive -> g=6,c=4,A=positive -> g=8,c=6,A=negative | g=4,c=3 -> g=6,c=4 -> g=8,c=6 | 66 | pure_lower_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 17 | multi_P_width_17_to_64 |
| g=4,c=3,A=positive -> g=6,c=3,A=negative | g=4,c=3 -> g=6,c=3 | 62 | pure_lower_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 18 | multi_P_width_17_to_64 |
| g=4,c=5,A=negative -> g=8,c=12,A=positive | g=4,c=5 -> g=8,c=12 | 62 | pure_upper_wing_single_shell | multi_P_wing_endpoint_trace_candidate | mixed_positive_negative | 24 | multi_P_width_17_to_64 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| MissingMirrorEndpointRouterImported | True | True | The previous endpoint router ledger is imported. | none for import |
| PureEndpointPhaseInterfaceLedger | True | True | Pure endpoint mass is routed into single-P local packets and multi-P trace candidates. | none for the finite interface ledger |
| SinglePLocalEndpointPacketBound | False | False | Control pure endpoint packets with only one supporting P. | requires local signed packet bounds not supplied by the ledger |
| MultiPTraceKloostermanCompletion | False | False | Complete multi-P pure endpoint packets to trace/Kloosterman sums. | requires explicit completion variables and sheaf/Kloosterman admissibility |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | candidate for multi-P pure endpoint trace sums after sheaf/trace realization |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | candidate for multi-P pure endpoint Kloosterman variables after completion |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | candidate for unbalanced right-tail pure endpoint fractions after variable extraction |
| Dong_Robles_Zeindler_2026_kloosterman_fractions | https://arxiv.org/abs/2601.00292 | withdrawn near-miss; not an admissible external input |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | does not estimate pure endpoint signed-carrier phases |

```text
FKMS_trace_bilinear=candidate only for multi-P pure endpoint trace candidates after sheaf realization
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=candidate only after bilinear Kloosterman variables are extracted
Wright_unbalanced_Kloosterman=candidate only for right-tail multi-P packets after fraction variables are explicit
Li_short_interval_x_052=does not control signed pure endpoint carrier phases
```

结论：pure endpoint 主体已拆成 single-P local packets 与 multi-P trace
candidates。该接口账本尚未给出本地包估计、trace/Kloosterman completion 或相消。

## 5. 最新最窄口

```text
SinglePLocalPureEndpointPacketBound
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
pure_endpoint_phase_interface_ledger_closed=true
single_P_local_endpoint_packet_bound_closed=false
multi_P_trace_completion_closed=false
pure_endpoint_carrier_phase_saving_closed=false
mixed_right_tail_endpoint_router_no_loss_closed=false
unequal_mirror_pair_residual_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
