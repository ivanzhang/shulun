# Prime Matrix Phi-LPF q-prefix carry cycle signature mirror-imbalance support 审计

**状态：** `mirror_imbalance_support_ledger_closed_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=mirror-imbalance signed-child carriers from the q-prefix carry cycle-signature ledger
operation=split residual mass into missing-mirror and unequal-mirror-pair carriers, with P/strip/endpoint support
dominant_shape=most imbalance is missing-mirror mass; unequal pairs form the smaller but still nonzero residual
remaining=phase saving for missing-mirror and unequal-pair residual carriers plus thin-support and completion losses
```

## 2. mirror-imbalance support 审计

```text
max_prime=1009
mirror_imbalance_support_ledger_closed=true
signed_cycle_edge_mass=107677
mirror_balanced_edge_mass_imported=31334
mirror_imbalance_edge_mass=76343
mirror_imbalance_edge_ratio=0.7090000650092406
missing_mirror_edge_mass=62980
missing_mirror_within_imbalance_ratio=0.824961031135795
unequal_mirror_pair_residual_edge_mass=13363
unequal_mirror_pair_within_imbalance_ratio=0.17503896886420497
missing_mirror_pair_count=7156
unequal_mirror_pair_residual_count=639
residual_raw_base_count=5334
residual_raw_base_share_min/median/max=0.014925373134328358/1.0/1.0
residual_carrier_count=7795
multi_P_residual_edge_ratio=0.6484419003706954
P_support_width_min/median/max=1/1/94
multi_strip_residual_edge_ratio=0.006326709717983312
strip_support_width_min/median/max=1/1/2
row_column_unconditional_closed=false
```

residual type edge mass：

| residual_type | pair_count | edge_mass | within_imbalance_ratio |
| --- | --- | --- | --- |
| missing_mirror | 7156 | 62980 | 0.824961031135795 |
| unequal_mirror_pair | 639 | 13363 | 0.17503896886420497 |

residual A-class edge mass：

| A_class | edge_mass | within_imbalance_ratio |
| --- | --- | --- |
| all_negative | 1751 | 0.02293596007492501 |
| all_positive | 2562 | 0.033559068938868 |
| mixed_positive_negative | 71626 | 0.9382130647210615 |
| mixed_with_zero | 404 | 0.005291906265145462 |

最高 residual signed-child carriers：

| signed_child | raw_base_template | residual_edge_mass | A_class | distinct_P_count | strip_edge_profile | endpoint_edge_profile |
| --- | --- | --- | --- | --- | --- | --- |
| g=4,c=4,A=negative -> g=8,c=9,A=positive | g=4,c=4 -> g=8,c=9 | 256 | mixed_positive_negative | 57 | right_tail:300 | right_tail_right_collar_only_no_P_puncture:100,right_tail_right_collar_only_with_P_puncture:4,right_tail_terminal_full_interval_no_P_puncture:2,right_tail_terminal_full_interval_with_P_puncture:4,right_tail_two_sided_left_and_right_collars_no_P_puncture:184,right_tail_two_sided_left_and_right_collars_with_P_puncture:6 |
| g=2,c=2,A=negative -> g=4,c=5,A=positive | g=2,c=2 -> g=4,c=5 | 214 | mixed_positive_negative | 66 | right_tail:294 | right_tail_right_collar_only_no_P_puncture:74,right_tail_terminal_full_interval_with_P_puncture:6,right_tail_two_sided_left_and_right_collars_no_P_puncture:208,right_tail_two_sided_left_and_right_collars_with_P_puncture:6 |
| g=2,c=4,A=positive -> g=4,c=6,A=negative | g=2,c=4 -> g=4,c=6 | 208 | mixed_positive_negative | 50 | upper_wing:208 | upper_wing_single_contiguous_endpoint_shell:208 |
| g=2,c=2,A=positive -> g=4,c=2,A=negative | g=2,c=2 -> g=4,c=2 | 202 | mixed_positive_negative | 54 | lower_wing:202 | lower_wing_single_contiguous_endpoint_shell:202 |
| g=10,c=11,A=positive -> g=2,c=2,A=negative | g=10,c=11 -> g=2,c=2 | 200 | mixed_positive_negative | 41 | right_tail:214 | right_tail_right_collar_only_no_P_puncture:68,right_tail_right_collar_only_with_P_puncture:2,right_tail_terminal_full_interval_with_P_puncture:16,right_tail_two_sided_left_and_right_collars_no_P_puncture:108,right_tail_two_sided_left_and_right_collars_with_P_puncture:20 |
| g=10,c=9,A=negative -> g=2,c=2,A=positive | g=10,c=9 -> g=2,c=2 | 198 | mixed_positive_negative | 45 | right_tail:204 | right_tail_left_collar_only_no_P_puncture:52,right_tail_terminal_full_interval_no_P_puncture:2,right_tail_terminal_full_interval_with_P_puncture:12,right_tail_two_sided_left_and_right_collars_no_P_puncture:114,right_tail_two_sided_left_and_right_collars_with_P_puncture:24 |
| g=4,c=4,A=positive -> g=8,c=7,A=negative | g=4,c=4 -> g=8,c=7 | 196 | mixed_positive_negative | 53 | right_tail:254 | right_tail_left_collar_only_no_P_puncture:68,right_tail_left_collar_only_with_P_puncture:2,right_tail_terminal_full_interval_no_P_puncture:2,right_tail_two_sided_left_and_right_collars_no_P_puncture:182 |
| g=10,c=16,A=positive -> g=2,c=3,A=negative | g=10,c=16 -> g=2,c=3 | 168 | mixed_positive_negative | 37 | upper_wing:212 | upper_wing_single_contiguous_endpoint_shell:212 |
| g=10,c=11,A=positive -> g=8,c=8,A=negative | g=10,c=11 -> g=8,c=8 | 166 | mixed_positive_negative | 36 | right_tail:188 | right_tail_right_collar_only_no_P_puncture:56,right_tail_right_collar_only_with_P_puncture:4,right_tail_terminal_full_interval_with_P_puncture:12,right_tail_two_sided_left_and_right_collars_no_P_puncture:116 |
| g=10,c=9,A=negative -> g=8,c=8,A=positive | g=10,c=9 -> g=8,c=8 | 154 | mixed_positive_negative | 33 | right_tail:184 | right_tail_left_collar_only_no_P_puncture:66,right_tail_terminal_full_interval_no_P_puncture:2,right_tail_terminal_full_interval_with_P_puncture:2,right_tail_two_sided_left_and_right_collars_no_P_puncture:106,right_tail_two_sided_left_and_right_collars_with_P_puncture:8 |
| g=2,c=2,A=positive -> g=6,c=6,A=positive -> g=6,c=5,A=negative | g=2,c=2 -> g=6,c=6 -> g=6,c=5 | 141 | mixed_positive_negative | 29 | right_tail:141 | right_tail_left_collar_only_no_P_puncture:30,right_tail_left_collar_only_with_P_puncture:9,right_tail_terminal_full_interval_no_P_puncture:3,right_tail_terminal_full_interval_with_P_puncture:6,right_tail_two_sided_left_and_right_collars_no_P_puncture:87,right_tail_two_sided_left_and_right_collars_with_P_puncture:6 |
| g=10,c=14,A=negative -> g=2,c=3,A=positive | g=10,c=14 -> g=2,c=3 | 138 | mixed_positive_negative | 35 | upper_wing:170 | upper_wing_single_contiguous_endpoint_shell:170 |
| g=14,c=15,A=positive -> g=4,c=4,A=negative | g=14,c=15 -> g=4,c=4 | 134 | mixed_positive_negative | 23 | right_tail:134 | right_tail_right_collar_only_no_P_puncture:42,right_tail_right_collar_only_with_P_puncture:6,right_tail_terminal_full_interval_no_P_puncture:2,right_tail_two_sided_left_and_right_collars_no_P_puncture:80,right_tail_two_sided_left_and_right_collars_with_P_puncture:4 |
| g=2,c=2,A=negative -> g=6,c=7,A=positive | g=2,c=2 -> g=6,c=7 | 134 | mixed_positive_negative | 29 | right_tail:200 | right_tail_right_collar_only_no_P_puncture:50,right_tail_two_sided_left_and_right_collars_no_P_puncture:148,right_tail_two_sided_left_and_right_collars_with_P_puncture:2 |
| g=2,c=2,A=positive -> g=6,c=5,A=negative | g=2,c=2 -> g=6,c=5 | 128 | mixed_positive_negative | 27 | right_tail:200 | right_tail_left_collar_only_no_P_puncture:56,right_tail_terminal_full_interval_no_P_puncture:2,right_tail_two_sided_left_and_right_collars_no_P_puncture:142 |
| g=2,c=2,A=negative -> g=6,c=4,A=negative -> g=6,c=4,A=positive | g=2,c=2 -> g=6,c=4 -> g=6,c=4 | 126 | mixed_positive_negative | 23 | lower_wing:132 | lower_wing_single_contiguous_endpoint_shell:132 |
| g=10,c=11,A=negative -> g=6,c=7,A=positive | g=10,c=11 -> g=6,c=7 | 124 | mixed_positive_negative | 21 | right_tail:162 | right_tail_right_collar_only_no_P_puncture:72,right_tail_two_sided_left_and_right_collars_no_P_puncture:90 |
| g=4,c=2,A=negative -> g=8,c=6,A=positive | g=4,c=2 -> g=8,c=6 | 124 | mixed_positive_negative | 36 | lower_wing:124 | lower_wing_single_contiguous_endpoint_shell:124 |
| g=4,c=6,A=negative -> g=8,c=14,A=positive | g=4,c=6 -> g=8,c=14 | 124 | mixed_positive_negative | 29 | upper_wing:124 | upper_wing_single_contiguous_endpoint_shell:124 |
| g=4,c=7,A=positive -> g=8,c=12,A=negative | g=4,c=7 -> g=8,c=12 | 122 | mixed_positive_negative | 32 | upper_wing:122 | upper_wing_single_contiguous_endpoint_shell:122 |

最高 residual raw bases：

| raw_base_template | residual_edge_mass | raw_base_signed_edge_mass | residual_share_inside_raw_base | signed_child_count | residual_type_profile |
| --- | --- | --- | --- | --- | --- |
| g=4,c=4 -> g=8,c=9 | 262 | 378 | 0.6931216931216931 | 4 | unequal_mirror_pair:262 |
| g=10,c=11 -> g=2,c=2 | 258 | 294 | 0.8775510204081632 | 4 | unequal_mirror_pair:258 |
| g=10,c=9 -> g=2,c=2 | 238 | 254 | 0.937007874015748 | 4 | unequal_mirror_pair:238 |
| g=2,c=2 -> g=4,c=2 | 236 | 256 | 0.921875 | 3 | missing_mirror:202,unequal_mirror_pair:34 |
| g=2,c=4 -> g=4,c=6 | 236 | 236 | 1.0 | 2 | missing_mirror:236 |
| g=2,c=2 -> g=4,c=5 | 216 | 408 | 0.5294117647058824 | 5 | missing_mirror:2,unequal_mirror_pair:214 |
| g=4,c=3 -> g=6,c=4 -> g=8,c=6 | 207 | 213 | 0.971830985915493 | 5 | missing_mirror:183,unequal_mirror_pair:24 |
| g=4,c=4 -> g=8,c=7 | 206 | 330 | 0.6242424242424243 | 4 | unequal_mirror_pair:206 |
| g=10,c=16 -> g=2,c=3 | 206 | 298 | 0.6912751677852349 | 4 | unequal_mirror_pair:206 |
| g=2,c=2 -> g=6,c=6 -> g=6,c=5 | 201 | 201 | 1.0 | 4 | missing_mirror:201 |
| g=10,c=14 -> g=2,c=3 | 192 | 256 | 0.75 | 3 | missing_mirror:54,unequal_mirror_pair:138 |
| g=4,c=4 -> g=8,c=7 -> g=6,c=6 | 189 | 189 | 1.0 | 4 | missing_mirror:189 |
| g=4,c=4 -> g=8,c=9 -> g=6,c=7 | 186 | 198 | 0.9393939393939394 | 5 | missing_mirror:144,unequal_mirror_pair:42 |
| g=4,c=6 -> g=6,c=8 -> g=8,c=12 | 177 | 177 | 1.0 | 3 | missing_mirror:177 |
| g=4,c=4 -> g=8,c=9 -> g=6,c=6 | 174 | 174 | 1.0 | 4 | missing_mirror:174 |
| g=10,c=11 -> g=8,c=8 | 170 | 222 | 0.7657657657657657 | 5 | missing_mirror:2,unequal_mirror_pair:168 |
| g=10,c=9 -> g=8,c=8 | 154 | 230 | 0.6695652173913044 | 4 | unequal_mirror_pair:154 |
| g=2,c=2 -> g=6,c=7 | 148 | 336 | 0.44047619047619047 | 4 | unequal_mirror_pair:148 |
| g=10,c=10 -> g=14,c=15 -> g=4,c=4 -> g=2,c=2 | 148 | 148 | 1.0 | 4 | missing_mirror:148 |
| g=12,c=17 -> g=8,c=12 -> g=4,c=6 | 147 | 153 | 0.9607843137254902 | 5 | missing_mirror:114,unequal_mirror_pair:33 |

最高 residual mirror pairs：

| residual_type | raw_base_template | dominant_signed_child | minority_or_missing_child | larger_child_edge_mass | smaller_or_missing_edge_mass | residual_edge_mass | dominant_distinct_P_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| unequal_mirror_pair | g=4,c=4 -> g=8,c=9 | g=4,c=4,A=negative -> g=8,c=9,A=positive | g=4,c=4,A=positive -> g=8,c=9,A=negative | 300 | 44 | 256 | 57 |
| unequal_mirror_pair | g=2,c=2 -> g=4,c=5 | g=2,c=2,A=negative -> g=4,c=5,A=positive | g=2,c=2,A=positive -> g=4,c=5,A=negative | 294 | 80 | 214 | 66 |
| missing_mirror | g=2,c=4 -> g=4,c=6 | g=2,c=4,A=positive -> g=4,c=6,A=negative | g=2,c=4,A=negative -> g=4,c=6,A=positive | 208 | 0 | 208 | 50 |
| missing_mirror | g=2,c=2 -> g=4,c=2 | g=2,c=2,A=positive -> g=4,c=2,A=negative | g=2,c=2,A=negative -> g=4,c=2,A=positive | 202 | 0 | 202 | 54 |
| unequal_mirror_pair | g=10,c=11 -> g=2,c=2 | g=10,c=11,A=positive -> g=2,c=2,A=negative | g=10,c=11,A=negative -> g=2,c=2,A=positive | 214 | 14 | 200 | 41 |
| unequal_mirror_pair | g=10,c=9 -> g=2,c=2 | g=10,c=9,A=negative -> g=2,c=2,A=positive | g=10,c=9,A=positive -> g=2,c=2,A=negative | 204 | 6 | 198 | 45 |
| unequal_mirror_pair | g=4,c=4 -> g=8,c=7 | g=4,c=4,A=positive -> g=8,c=7,A=negative | g=4,c=4,A=negative -> g=8,c=7,A=positive | 254 | 58 | 196 | 53 |
| unequal_mirror_pair | g=10,c=16 -> g=2,c=3 | g=10,c=16,A=positive -> g=2,c=3,A=negative | g=10,c=16,A=negative -> g=2,c=3,A=positive | 212 | 44 | 168 | 37 |
| unequal_mirror_pair | g=10,c=11 -> g=8,c=8 | g=10,c=11,A=positive -> g=8,c=8,A=negative | g=10,c=11,A=negative -> g=8,c=8,A=positive | 188 | 22 | 166 | 36 |
| unequal_mirror_pair | g=10,c=9 -> g=8,c=8 | g=10,c=9,A=negative -> g=8,c=8,A=positive | g=10,c=9,A=positive -> g=8,c=8,A=negative | 184 | 30 | 154 | 33 |
| missing_mirror | g=2,c=2 -> g=6,c=6 -> g=6,c=5 | g=2,c=2,A=positive -> g=6,c=6,A=positive -> g=6,c=5,A=negative | g=2,c=2,A=negative -> g=6,c=6,A=negative -> g=6,c=5,A=positive | 141 | 0 | 141 | 29 |
| unequal_mirror_pair | g=10,c=14 -> g=2,c=3 | g=10,c=14,A=negative -> g=2,c=3,A=positive | g=10,c=14,A=positive -> g=2,c=3,A=negative | 170 | 32 | 138 | 35 |
| unequal_mirror_pair | g=2,c=2 -> g=6,c=7 | g=2,c=2,A=negative -> g=6,c=7,A=positive | g=2,c=2,A=positive -> g=6,c=7,A=negative | 200 | 66 | 134 | 29 |
| missing_mirror | g=14,c=15 -> g=4,c=4 | g=14,c=15,A=positive -> g=4,c=4,A=negative | g=14,c=15,A=negative -> g=4,c=4,A=positive | 134 | 0 | 134 | 23 |
| unequal_mirror_pair | g=2,c=2 -> g=6,c=5 | g=2,c=2,A=positive -> g=6,c=5,A=negative | g=2,c=2,A=negative -> g=6,c=5,A=positive | 200 | 72 | 128 | 27 |
| unequal_mirror_pair | g=2,c=2 -> g=6,c=4 -> g=6,c=4 | g=2,c=2,A=negative -> g=6,c=4,A=negative -> g=6,c=4,A=positive | g=2,c=2,A=positive -> g=6,c=4,A=positive -> g=6,c=4,A=negative | 132 | 6 | 126 | 23 |
| unequal_mirror_pair | g=10,c=11 -> g=6,c=7 | g=10,c=11,A=negative -> g=6,c=7,A=positive | g=10,c=11,A=positive -> g=6,c=7,A=negative | 162 | 38 | 124 | 21 |
| missing_mirror | g=4,c=2 -> g=8,c=6 | g=4,c=2,A=negative -> g=8,c=6,A=positive | g=4,c=2,A=positive -> g=8,c=6,A=negative | 124 | 0 | 124 | 36 |
| missing_mirror | g=4,c=6 -> g=8,c=14 | g=4,c=6,A=negative -> g=8,c=14,A=positive | g=4,c=6,A=positive -> g=8,c=14,A=negative | 124 | 0 | 124 | 29 |
| missing_mirror | g=4,c=7 -> g=8,c=12 | g=4,c=7,A=positive -> g=8,c=12,A=negative | g=4,c=7,A=negative -> g=8,c=12,A=positive | 122 | 0 | 122 | 32 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SignedChildMirrorLedgerImported | True | True | The previous signed-child mirror pairing ledger is imported. | none for import |
| MirrorImbalanceSupportLedger | True | True | Every mirror-imbalance edge is assigned to missing-mirror or unequal-mirror-pair support. | none for the finite support ledger |
| MissingMirrorCarrierPhaseSaving | False | False | Prove cancellation or a positive lower bound after the missing-mirror carriers are isolated. | requires analytic phase input on carriers with no sign mirror |
| UnequalMirrorPairResidualPhaseSaving | False | False | Prove cancellation for the residual after unequal mirror-pair cancellation. | requires analytic phase input on the heavier signed-child side |
| TraceKloostermanCompletion | False | False | Convert the isolated residual carriers to admissible trace/Kloosterman families. | requires a new completion map and no-loss aggregation |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | candidate only after missing/unequal mirror carriers become trace-function sums |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | candidate only after residual carriers are completed to Kloosterman variables |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | requires Type-II boxes; this ledger exposes residual signed-child support only |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | candidate after the residual support is converted to admissible unbalanced fractions |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval prime existence does not estimate mirror-imbalance phase |

```text
FKMS_trace_bilinear=candidate only after missing/unequal residual carriers become trace sums
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=candidate only after residual carriers expose bilinear Kloosterman variables
Pascadi_composite_Type_II=not directly matched to signed-child mirror-imbalance support
Wright_unbalanced_Kloosterman=candidate only after dominant-side residuals become admissible unbalanced fractions
Li_short_interval_x_052=does not estimate the mirror-imbalance support ledger
```

结论：mirror-imbalance 已被继续拆成 missing-mirror 与 unequal-mirror-pair
两类 residual carriers。多数剩余来自没有符号镜像的 signed child；这压缩了
目标对象，但尚未给出任何相位节省或 trace/Kloosterman 完成。

## 5. 最新最窄口

```text
MissingMirrorCarrierPhaseSaving
AND UnequalMirrorPairResidualPhaseSaving
AND ThinPSupportCarrierSummationWithoutLoss
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND TraceKloostermanCompletionOfMirrorImbalanceAndResidualPackets
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
mirror_imbalance_support_ledger_closed=true
missing_mirror_carrier_phase_saving_closed=false
unequal_mirror_pair_residual_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
