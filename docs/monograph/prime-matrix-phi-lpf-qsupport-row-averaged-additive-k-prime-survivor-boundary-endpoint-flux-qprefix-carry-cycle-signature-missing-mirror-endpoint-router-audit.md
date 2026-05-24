# Prime Matrix Phi-LPF q-prefix carry cycle signature missing-mirror endpoint-router 审计

**状态：** `missing_mirror_endpoint_router_ledger_closed_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=missing-mirror signed-child endpoint support
operation=pure-endpoint versus mixed-endpoint template routing
dominant_shape=most mass is pure endpoint; the mixed mass stays in right-tail endpoint mixtures
remaining=pure endpoint phase saving, right-tail mixed endpoint no-loss routing, and trace/Kloosterman completion
```

## 2. endpoint-router 审计

```text
max_prime=1009
missing_mirror_endpoint_router_ledger_closed=true
missing_mirror_edge_mass=62980
missing_mirror_template_count=7156
pure_endpoint_template_edge_mass=48636
pure_endpoint_template_edge_ratio=0.7722451571927597
mixed_endpoint_template_edge_mass=14344
mixed_endpoint_template_edge_ratio=0.2277548428072404
mixed_right_tail_endpoint_edge_mass=14316
mixed_right_tail_endpoint_edge_ratio=0.22731025722451573
mixed_wing_tail_endpoint_edge_mass=28
mixed_wing_tail_endpoint_edge_ratio=0.0004445855827246745
single_strip_pure_endpoint_edge_mass=48636
single_strip_pure_endpoint_edge_ratio=0.7722451571927597
endpoint_group_width_min/median/max=1/1.0/3
row_column_unconditional_closed=false
```

endpoint route edge mass：

| route_class | template_count | edge_mass | edge_ratio | P_support_width_min | P_support_width_median | P_support_width_max |
| --- | --- | --- | --- | --- | --- | --- |
| pure_upper_wing_single_shell | 2439 | 20314 | 0.32254684026675134 | 1 | 1 | 50 |
| mixed_right_tail_endpoint | 746 | 14316 | 0.22731025722451573 | 1 | 3.0 | 29 |
| pure_right_tail_two_sided_collar | 1974 | 13310 | 0.2113369323594792 | 1 | 1.0 | 9 |
| pure_lower_wing_single_shell | 1177 | 10208 | 0.1620832010161956 | 1 | 1 | 54 |
| pure_right_tail_right_collar | 400 | 2347 | 0.03726579866624325 | 1 | 1.0 | 5 |
| pure_right_tail_left_collar | 291 | 1769 | 0.028088281994283898 | 1 | 1 | 3 |
| pure_right_tail_terminal_full_interval | 127 | 688 | 0.010924102889806287 | 1 | 1 | 4 |
| mixed_wing_and_tail_endpoint | 2 | 28 | 0.0004445855827246745 | 4 | 4.5 | 5 |

最高 endpoint-route templates：

| route_class | signed_child | raw_base_template | edge_mass | A_class | P_support_width | strip_profile | endpoint_group_profile |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pure_upper_wing_single_shell | g=2,c=4,A=positive -> g=4,c=6,A=negative | g=2,c=4 -> g=4,c=6 | 208 | mixed_positive_negative | 50 | upper_wing:208 | upper_wing_single_shell:208 |
| pure_lower_wing_single_shell | g=2,c=2,A=positive -> g=4,c=2,A=negative | g=2,c=2 -> g=4,c=2 | 202 | mixed_positive_negative | 54 | lower_wing:202 | lower_wing_single_shell:202 |
| mixed_right_tail_endpoint | g=2,c=2,A=positive -> g=6,c=6,A=positive -> g=6,c=5,A=negative | g=2,c=2 -> g=6,c=6 -> g=6,c=5 | 141 | mixed_positive_negative | 29 | right_tail:141 | right_tail_left_collar:39,right_tail_terminal_full_interval:9,right_tail_two_sided_collar:93 |
| mixed_right_tail_endpoint | g=14,c=15,A=positive -> g=4,c=4,A=negative | g=14,c=15 -> g=4,c=4 | 134 | mixed_positive_negative | 23 | right_tail:134 | right_tail_right_collar:48,right_tail_terminal_full_interval:2,right_tail_two_sided_collar:84 |
| pure_lower_wing_single_shell | g=4,c=2,A=negative -> g=8,c=6,A=positive | g=4,c=2 -> g=8,c=6 | 124 | mixed_positive_negative | 36 | lower_wing:124 | lower_wing_single_shell:124 |
| pure_upper_wing_single_shell | g=4,c=6,A=negative -> g=8,c=14,A=positive | g=4,c=6 -> g=8,c=14 | 124 | mixed_positive_negative | 29 | upper_wing:124 | upper_wing_single_shell:124 |
| pure_upper_wing_single_shell | g=4,c=7,A=positive -> g=8,c=12,A=negative | g=4,c=7 -> g=8,c=12 | 122 | mixed_positive_negative | 32 | upper_wing:122 | upper_wing_single_shell:122 |
| pure_upper_wing_single_shell | g=4,c=6,A=positive -> g=6,c=8,A=negative -> g=8,c=12,A=negative | g=4,c=6 -> g=6,c=8 -> g=8,c=12 | 117 | mixed_positive_negative | 27 | upper_wing:117 | upper_wing_single_shell:117 |
| mixed_right_tail_endpoint | g=2,c=2,A=negative -> g=6,c=6,A=negative -> g=6,c=7,A=positive | g=2,c=2 -> g=6,c=6 -> g=6,c=7 | 108 | mixed_positive_negative | 21 | right_tail:108 | right_tail_right_collar:18,right_tail_terminal_full_interval:12,right_tail_two_sided_collar:78 |
| mixed_right_tail_endpoint | g=4,c=4,A=negative -> g=8,c=9,A=positive -> g=6,c=6,A=negative | g=4,c=4 -> g=8,c=9 -> g=6,c=6 | 108 | mixed_positive_negative | 22 | right_tail:108 | right_tail_right_collar:24,right_tail_terminal_full_interval:3,right_tail_two_sided_collar:81 |
| mixed_right_tail_endpoint | g=4,c=4,A=positive -> g=8,c=7,A=negative -> g=6,c=6,A=positive | g=4,c=4 -> g=8,c=7 -> g=6,c=6 | 105 | mixed_positive_negative | 25 | right_tail:105 | right_tail_left_collar:33,right_tail_terminal_full_interval:9,right_tail_two_sided_collar:63 |
| mixed_right_tail_endpoint | g=10,c=10,A=positive -> g=14,c=13,A=negative -> g=4,c=4,A=positive -> g=2,c=2,A=positive | g=10,c=10 -> g=14,c=13 -> g=4,c=4 -> g=2,c=2 | 100 | mixed_positive_negative | 17 | right_tail:100 | right_tail_left_collar:24,right_tail_terminal_full_interval:4,right_tail_two_sided_collar:72 |
| pure_upper_wing_single_shell | g=4,c=7,A=positive -> g=6,c=9,A=negative | g=4,c=7 -> g=6,c=9 | 94 | mixed_positive_negative | 27 | upper_wing:94 | upper_wing_single_shell:94 |
| mixed_right_tail_endpoint | g=4,c=4,A=negative -> g=8,c=9,A=positive -> g=6,c=7,A=positive | g=4,c=4 -> g=8,c=9 -> g=6,c=7 | 93 | mixed_positive_negative | 17 | right_tail:93 | right_tail_right_collar:30,right_tail_two_sided_collar:63 |
| pure_lower_wing_single_shell | g=4,c=2,A=negative -> g=6,c=5,A=positive | g=4,c=2 -> g=6,c=5 | 92 | mixed_positive_negative | 34 | lower_wing:92 | lower_wing_single_shell:92 |
| mixed_right_tail_endpoint | g=2,c=3,A=positive -> g=6,c=6,A=negative -> g=6,c=6,A=positive | g=2,c=3 -> g=6,c=6 -> g=6,c=6 | 84 | mixed_positive_negative | 19 | right_tail:84 | right_tail_right_collar:21,right_tail_terminal_full_interval:3,right_tail_two_sided_collar:60 |
| mixed_right_tail_endpoint | g=10,c=10,A=negative -> g=14,c=15,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=negative | g=10,c=10 -> g=14,c=15 -> g=4,c=4 -> g=2,c=2 | 84 | mixed_positive_negative | 16 | right_tail:84 | right_tail_right_collar:32,right_tail_terminal_full_interval:4,right_tail_two_sided_collar:48 |
| mixed_right_tail_endpoint | g=10,c=10,A=negative -> g=12,c=13,A=positive -> g=2,c=2,A=negative | g=10,c=10 -> g=12,c=13 -> g=2,c=2 | 81 | mixed_positive_negative | 15 | right_tail:81 | right_tail_right_collar:24,right_tail_terminal_full_interval:6,right_tail_two_sided_collar:51 |
| pure_upper_wing_single_shell | g=2,c=3,A=negative -> g=6,c=9,A=negative -> g=6,c=10,A=positive | g=2,c=3 -> g=6,c=9 -> g=6,c=10 | 81 | mixed_positive_negative | 14 | upper_wing:81 | upper_wing_single_shell:81 |
| mixed_right_tail_endpoint | g=10,c=10,A=negative -> g=2,c=2,A=negative -> g=12,c=13,A=positive | g=10,c=10 -> g=2,c=2 -> g=12,c=13 | 78 | mixed_positive_negative | 17 | right_tail:78 | right_tail_right_collar:15,right_tail_terminal_full_interval:12,right_tail_two_sided_collar:51 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| MissingMirrorStructureLedgerImported | True | True | The previous missing-mirror structure ledger is imported. | none for import |
| MissingMirrorEndpointRouterLedger | True | True | Each missing-mirror signed template is routed as pure endpoint or mixed endpoint support. | none for the finite router ledger |
| PureEndpointCarrierPhaseSaving | False | False | Prove phase saving on pure endpoint missing-mirror carriers. | requires analytic phase input after route isolation |
| MixedRightTailEndpointNoLossRouter | False | False | Split mixed right-tail endpoint templates without losing the signed-child accounting. | requires endpoint-level rather than template-level completion |
| MissingMirrorTraceCompletion | False | False | Complete endpoint-routed carriers to admissible trace/Kloosterman families. | requires explicit completion variables |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | needs endpoint-routed missing carriers to be completed as trace-function sums |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | needs explicit bilinear Kloosterman variables after endpoint routing |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | still requires composite Type-II boxes, not just endpoint-routed signed templates |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | candidate only after right-tail routed carriers become unbalanced Kloosterman fractions |

```text
FKMS_trace_bilinear=candidate only after pure/mixed endpoint routes are completed to trace sums
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=candidate only after endpoint-routed Kloosterman variables are explicit
Pascadi_composite_Type_II=not matched to endpoint-routed signed-template carriers
Wright_unbalanced_Kloosterman=candidate for right-tail routes only after unbalanced fraction variables appear
```

结论：missing-mirror endpoint carriers 已分成纯 endpoint 模板和 right-tail
内部混合 endpoint 模板。该路由账本仍不提供 phase saving，也不完成到
trace/Kloosterman family。

## 5. 最新最窄口

```text
PureEndpointMissingMirrorCarrierPhaseSaving
AND MixedRightTailEndpointRouterNoLoss
AND MissingMirrorTraceKloostermanCompletion
AND UnequalMirrorPairResidualPhaseSaving
AND ThinPSupportCarrierSummationWithoutLoss
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
missing_mirror_endpoint_router_ledger_closed=true
pure_endpoint_carrier_phase_saving_closed=false
mixed_right_tail_endpoint_router_no_loss_closed=false
missing_mirror_trace_completion_closed=false
unequal_mirror_pair_residual_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
