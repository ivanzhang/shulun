# Prime Matrix Phi-LPF q-prefix carry cycle signature weight-carrier 审计

**状态：** `qprefix_cycle_signature_weight_carrier_ledger_closed_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=raw/signed cycle signatures from the loop-erased carry-switch core
operation=support and fragmentation audit for the combinatorial weights carried by signatures
dominant_shape=high-mass signed carriers are thin in P/strip support, while raw bases fragment across signed children
remaining=weighted phase saving must reconcile signed refinements, thin carriers, residual endpoints, and trace/Kloosterman completion
```

## 2. weight-carrier 审计

```text
max_prime=1009
cycle_signature_atom_count_total=15439
switch_atom_count=13355
non_switch_atom_count=2084
adjacent_letter_pair_count_inside_atoms=147799
cycle_signature_weight_carrier_ledger_closed=true
raw_cycle_packet_count=45178
raw_cycle_edge_mass=117733
raw_cycle_signature_count=3546
signed_cycle_packet_count=36330
signed_cycle_edge_mass=107677
signed_cycle_signature_count=8691
raw_base_signed_refinement_count=5359
raw_base_with_multiple_signed_children_count=1823
raw_base_fragmented_signed_edge_ratio=0.7569583105027071
raw_base_max_child_edge_share_min/median/max=0.16666666666666666/1.0/1.0
cycle_signature_weighted_phase_saving_closed=false
row_column_unconditional_closed=false
```

raw carrier support：

```text
signature_count=3546
multi_P_signature_count=2109
multi_P_edge_mass=109981
multi_P_edge_ratio=0.9341560989697026
multi_strip_signature_count=33
multi_strip_edge_mass=5187
multi_strip_edge_ratio=0.04405731613056662
P_support_width_min/median/max=1/2.0/101
strip_support_width_min/median/max=1/1.0/2
```

signed carrier support：

```text
signature_count=8691
multi_P_signature_count=3388
multi_P_edge_mass=79526
multi_P_edge_ratio=0.7385606954131337
multi_strip_signature_count=38
multi_strip_edge_mass=1555
multi_strip_edge_ratio=0.014441338447393594
P_support_width_min/median/max=1/1/95
strip_support_width_min/median/max=1/1/2
```

signed A-class edge mass：

| A_class | cycle_count | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| all_negative | 4981 | 9169 | 0.08515281815057997 |
| all_positive | 5311 | 9980 | 0.0926846030257158 |
| mixed_positive_negative | 25951 | 88124 | 0.8184106169376932 |
| mixed_with_zero | 87 | 404 | 0.0037519618860109402 |

最高质量 raw carriers：

| template | cycle_count | edge_mass | distinct_P_count | strip_profile | endpoint_profile |
| --- | --- | --- | --- | --- | --- |
| g=2,c=2 -> g=4,c=4 | 949 | 1898 | 101 | right_tail:949 | right_tail_left_collar_only_no_P_puncture:78,right_tail_left_collar_only_with_P_puncture:37,right_tail_right_collar_only_no_P_puncture:72,right_tail_right_collar_only_with_P_puncture:12,right_tail_terminal_full_interval_no_P_puncture:86,right_tail_terminal_full_interval_with_P_puncture:171,right_tail_two_sided_left_and_right_collars_no_P_puncture:392,right_tail_two_sided_left_and_right_collars_with_P_puncture:101 |
| g=6,c=6 | 1439 | 1439 | 99 | right_tail:1439 | right_tail_left_collar_only_no_P_puncture:128,right_tail_left_collar_only_with_P_puncture:26,right_tail_right_collar_only_no_P_puncture:88,right_tail_right_collar_only_with_P_puncture:28,right_tail_terminal_full_interval_no_P_puncture:154,right_tail_terminal_full_interval_with_P_puncture:284,right_tail_two_sided_left_and_right_collars_no_P_puncture:586,right_tail_two_sided_left_and_right_collars_with_P_puncture:145 |
| g=2,c=3 -> g=4,c=6 | 482 | 964 | 72 | upper_wing:482 | upper_wing_single_contiguous_endpoint_shell:482 |
| g=6,c=9 | 920 | 920 | 83 | upper_wing:920 | upper_wing_single_contiguous_endpoint_shell:920 |
| g=6,c=7 | 893 | 893 | 76 | right_tail:893 | right_tail_right_collar_only_no_P_puncture:266,right_tail_right_collar_only_with_P_puncture:2,right_tail_two_sided_left_and_right_collars_no_P_puncture:623,right_tail_two_sided_left_and_right_collars_with_P_puncture:2 |
| g=4,c=6 -> g=6,c=9 | 444 | 888 | 67 | upper_wing:444 | upper_wing_single_contiguous_endpoint_shell:444 |
| g=6,c=4 | 863 | 863 | 83 | lower_wing:863 | lower_wing_single_contiguous_endpoint_shell:863 |
| g=4,c=3 -> g=6,c=4 | 386 | 772 | 71 | lower_wing:386 | lower_wing_single_contiguous_endpoint_shell:386 |
| g=4,c=4 -> g=6,c=6 | 373 | 746 | 74 | right_tail:373 | right_tail_left_collar_only_no_P_puncture:28,right_tail_left_collar_only_with_P_puncture:9,right_tail_right_collar_only_no_P_puncture:19,right_tail_right_collar_only_with_P_puncture:12,right_tail_terminal_full_interval_no_P_puncture:46,right_tail_terminal_full_interval_with_P_puncture:98,right_tail_two_sided_left_and_right_collars_no_P_puncture:111,right_tail_two_sided_left_and_right_collars_with_P_puncture:50 |
| g=4,c=4 -> g=8,c=8 | 365 | 730 | 72 | right_tail:365 | right_tail_left_collar_only_no_P_puncture:26,right_tail_left_collar_only_with_P_puncture:13,right_tail_right_collar_only_no_P_puncture:33,right_tail_right_collar_only_with_P_puncture:12,right_tail_terminal_full_interval_no_P_puncture:52,right_tail_terminal_full_interval_with_P_puncture:69,right_tail_two_sided_left_and_right_collars_no_P_puncture:115,right_tail_two_sided_left_and_right_collars_with_P_puncture:45 |
| g=2,c=3 -> g=6,c=9 | 363 | 726 | 46 | upper_wing:363 | upper_wing_single_contiguous_endpoint_shell:363 |
| g=2,c=1 -> g=4,c=3 | 354 | 708 | 78 | lower_wing:351,right_tail:3 | lower_wing_single_contiguous_endpoint_shell:351,right_tail_two_sided_left_and_right_collars_no_P_puncture:3 |
| g=2,c=2 -> g=6,c=6 | 351 | 702 | 52 | right_tail:351 | right_tail_left_collar_only_no_P_puncture:28,right_tail_left_collar_only_with_P_puncture:10,right_tail_right_collar_only_no_P_puncture:20,right_tail_right_collar_only_with_P_puncture:6,right_tail_terminal_full_interval_no_P_puncture:46,right_tail_terminal_full_interval_with_P_puncture:80,right_tail_two_sided_left_and_right_collars_no_P_puncture:127,right_tail_two_sided_left_and_right_collars_with_P_puncture:34 |
| g=2,c=2 -> g=4,c=5 | 329 | 658 | 78 | right_tail:329 | right_tail_right_collar_only_no_P_puncture:89,right_tail_terminal_full_interval_with_P_puncture:6,right_tail_two_sided_left_and_right_collars_no_P_puncture:223,right_tail_two_sided_left_and_right_collars_with_P_puncture:11 |
| g=6,c=5 | 655 | 655 | 63 | lower_wing:2,right_tail:653 | lower_wing_single_contiguous_endpoint_shell:2,right_tail_left_collar_only_no_P_puncture:150,right_tail_two_sided_left_and_right_collars_no_P_puncture:503 |
| g=2,c=3 -> g=4,c=7 | 296 | 592 | 57 | upper_wing:296 | upper_wing_single_contiguous_endpoint_shell:296 |
| g=4,c=6 -> g=8,c=12 | 295 | 590 | 45 | upper_wing:295 | upper_wing_single_contiguous_endpoint_shell:295 |
| g=4,c=4 -> g=8,c=8 -> g=6,c=6 | 196 | 588 | 32 | right_tail:196 | right_tail_left_collar_only_no_P_puncture:13,right_tail_left_collar_only_with_P_puncture:2,right_tail_right_collar_only_no_P_puncture:7,right_tail_right_collar_only_with_P_puncture:4,right_tail_terminal_full_interval_no_P_puncture:34,right_tail_terminal_full_interval_with_P_puncture:66,right_tail_two_sided_left_and_right_collars_no_P_puncture:45,right_tail_two_sided_left_and_right_collars_with_P_puncture:25 |
| g=2,c=1 -> g=6,c=4 | 269 | 538 | 36 | lower_wing:269 | lower_wing_single_contiguous_endpoint_shell:269 |
| g=10,c=7 -> g=6,c=4 | 263 | 526 | 25 | lower_wing:263 | lower_wing_single_contiguous_endpoint_shell:263 |

最高质量 signed carriers：

| template | cycle_count | edge_mass | distinct_P_count | strip_profile | endpoint_profile |
| --- | --- | --- | --- | --- | --- |
| g=2,c=2,A=negative -> g=4,c=4,A=negative | 372 | 744 | 94 | right_tail:372 | right_tail_left_collar_only_with_P_puncture:1,right_tail_right_collar_only_no_P_puncture:49,right_tail_right_collar_only_with_P_puncture:12,right_tail_terminal_full_interval_no_P_puncture:54,right_tail_terminal_full_interval_with_P_puncture:84,right_tail_two_sided_left_and_right_collars_no_P_puncture:135,right_tail_two_sided_left_and_right_collars_with_P_puncture:37 |
| g=2,c=2,A=positive -> g=4,c=4,A=positive | 334 | 668 | 95 | right_tail:334 | right_tail_left_collar_only_no_P_puncture:47,right_tail_left_collar_only_with_P_puncture:26,right_tail_terminal_full_interval_no_P_puncture:25,right_tail_terminal_full_interval_with_P_puncture:69,right_tail_two_sided_left_and_right_collars_no_P_puncture:119,right_tail_two_sided_left_and_right_collars_with_P_puncture:48 |
| g=6,c=6,A=negative | 545 | 545 | 94 | right_tail:545 | right_tail_right_collar_only_no_P_puncture:51,right_tail_right_collar_only_with_P_puncture:22,right_tail_terminal_full_interval_no_P_puncture:91,right_tail_terminal_full_interval_with_P_puncture:130,right_tail_two_sided_left_and_right_collars_no_P_puncture:189,right_tail_two_sided_left_and_right_collars_with_P_puncture:62 |
| g=6,c=6,A=positive | 464 | 464 | 88 | right_tail:464 | right_tail_left_collar_only_no_P_puncture:68,right_tail_left_collar_only_with_P_puncture:24,right_tail_terminal_full_interval_no_P_puncture:54,right_tail_terminal_full_interval_with_P_puncture:117,right_tail_two_sided_left_and_right_collars_no_P_puncture:153,right_tail_two_sided_left_and_right_collars_with_P_puncture:48 |
| g=6,c=7,A=positive | 334 | 334 | 71 | right_tail:334 | right_tail_right_collar_only_no_P_puncture:92,right_tail_right_collar_only_with_P_puncture:2,right_tail_two_sided_left_and_right_collars_no_P_puncture:240 |
| g=4,c=4,A=negative -> g=8,c=9,A=positive | 150 | 300 | 57 | right_tail:150 | right_tail_right_collar_only_no_P_puncture:50,right_tail_right_collar_only_with_P_puncture:2,right_tail_terminal_full_interval_no_P_puncture:1,right_tail_terminal_full_interval_with_P_puncture:2,right_tail_two_sided_left_and_right_collars_no_P_puncture:92,right_tail_two_sided_left_and_right_collars_with_P_puncture:3 |
| g=2,c=2,A=negative -> g=4,c=5,A=positive | 147 | 294 | 66 | right_tail:147 | right_tail_right_collar_only_no_P_puncture:37,right_tail_terminal_full_interval_with_P_puncture:3,right_tail_two_sided_left_and_right_collars_no_P_puncture:104,right_tail_two_sided_left_and_right_collars_with_P_puncture:3 |
| g=2,c=3,A=positive -> g=4,c=6,A=positive | 144 | 288 | 60 | upper_wing:144 | upper_wing_single_contiguous_endpoint_shell:144 |
| g=4,c=3,A=positive -> g=6,c=4,A=negative | 143 | 286 | 59 | lower_wing:143 | lower_wing_single_contiguous_endpoint_shell:143 |
| g=4,c=4,A=negative -> g=8,c=8,A=negative | 143 | 286 | 66 | right_tail:143 | right_tail_right_collar_only_no_P_puncture:19,right_tail_right_collar_only_with_P_puncture:11,right_tail_terminal_full_interval_no_P_puncture:27,right_tail_terminal_full_interval_with_P_puncture:31,right_tail_two_sided_left_and_right_collars_no_P_puncture:36,right_tail_two_sided_left_and_right_collars_with_P_puncture:19 |
| g=6,c=4,A=negative | 275 | 275 | 64 | lower_wing:275 | lower_wing_single_contiguous_endpoint_shell:275 |
| g=4,c=6,A=positive -> g=6,c=9,A=positive | 132 | 264 | 58 | upper_wing:132 | upper_wing_single_contiguous_endpoint_shell:132 |
| g=6,c=5,A=negative | 263 | 263 | 59 | right_tail:263 | right_tail_left_collar_only_no_P_puncture:68,right_tail_two_sided_left_and_right_collars_no_P_puncture:195 |
| g=4,c=4,A=positive -> g=6,c=6,A=positive | 131 | 262 | 64 | right_tail:131 | right_tail_left_collar_only_no_P_puncture:13,right_tail_left_collar_only_with_P_puncture:8,right_tail_terminal_full_interval_no_P_puncture:19,right_tail_terminal_full_interval_with_P_puncture:34,right_tail_two_sided_left_and_right_collars_no_P_puncture:42,right_tail_two_sided_left_and_right_collars_with_P_puncture:15 |
| g=6,c=9,A=positive | 260 | 260 | 66 | upper_wing:260 | upper_wing_single_contiguous_endpoint_shell:260 |
| g=4,c=4,A=negative -> g=6,c=6,A=negative | 130 | 260 | 64 | right_tail:130 | right_tail_right_collar_only_no_P_puncture:11,right_tail_right_collar_only_with_P_puncture:10,right_tail_terminal_full_interval_no_P_puncture:23,right_tail_terminal_full_interval_with_P_puncture:40,right_tail_two_sided_left_and_right_collars_no_P_puncture:29,right_tail_two_sided_left_and_right_collars_with_P_puncture:17 |
| g=4,c=4,A=positive -> g=8,c=7,A=negative | 127 | 254 | 53 | right_tail:127 | right_tail_left_collar_only_no_P_puncture:34,right_tail_left_collar_only_with_P_puncture:1,right_tail_terminal_full_interval_no_P_puncture:1,right_tail_two_sided_left_and_right_collars_no_P_puncture:91 |
| g=2,c=1,A=positive -> g=4,c=3,A=negative | 123 | 246 | 62 | lower_wing:121,right_tail:2 | lower_wing_single_contiguous_endpoint_shell:121,right_tail_two_sided_left_and_right_collars_no_P_puncture:2 |
| g=4,c=4,A=positive -> g=8,c=8,A=positive | 123 | 246 | 57 | right_tail:123 | right_tail_left_collar_only_no_P_puncture:14,right_tail_left_collar_only_with_P_puncture:9,right_tail_terminal_full_interval_no_P_puncture:17,right_tail_terminal_full_interval_with_P_puncture:29,right_tail_two_sided_left_and_right_collars_no_P_puncture:38,right_tail_two_sided_left_and_right_collars_with_P_puncture:16 |
| g=2,c=2,A=negative -> g=6,c=6,A=negative | 121 | 242 | 44 | right_tail:121 | right_tail_right_collar_only_no_P_puncture:10,right_tail_right_collar_only_with_P_puncture:4,right_tail_terminal_full_interval_no_P_puncture:22,right_tail_terminal_full_interval_with_P_puncture:34,right_tail_two_sided_left_and_right_collars_no_P_puncture:39,right_tail_two_sided_left_and_right_collars_with_P_puncture:12 |

raw-base 到 signed-child fragmentation：

| raw_base_template | signed_child_count | signed_cycle_count | signed_edge_mass | max_child_edge_share | top_signed_child |
| --- | --- | --- | --- | --- | --- |
| g=2,c=2 -> g=4,c=4 | 4 | 736 | 1472 | 0.5054347826086957 | g=2,c=2,A=negative -> g=4,c=4,A=negative |
| g=6,c=6 | 2 | 1009 | 1009 | 0.5401387512388504 | g=6,c=6,A=negative |
| g=2,c=3 -> g=4,c=6 | 4 | 356 | 712 | 0.4044943820224719 | g=2,c=3,A=positive -> g=4,c=6,A=positive |
| g=4,c=6 -> g=6,c=9 | 4 | 310 | 620 | 0.4258064516129032 | g=4,c=6,A=positive -> g=6,c=9,A=positive |
| g=4,c=4 -> g=8,c=8 | 4 | 293 | 586 | 0.4880546075085324 | g=4,c=4,A=negative -> g=8,c=8,A=negative |
| g=4,c=3 -> g=6,c=4 | 4 | 290 | 580 | 0.49310344827586206 | g=4,c=3,A=positive -> g=6,c=4,A=negative |
| g=6,c=7 | 2 | 560 | 560 | 0.5964285714285714 | g=6,c=7,A=positive |
| g=4,c=4 -> g=6,c=6 | 4 | 268 | 536 | 0.48880597014925375 | g=4,c=4,A=positive -> g=6,c=6,A=positive |
| g=4,c=6 -> g=8,c=12 | 4 | 264 | 528 | 0.3106060606060606 | g=4,c=6,A=positive -> g=8,c=12,A=positive |
| g=4,c=4 -> g=8,c=8 -> g=6,c=6 | 7 | 170 | 510 | 0.45294117647058824 | g=4,c=4,A=negative -> g=8,c=8,A=negative -> g=6,c=6,A=negative |
| g=6,c=4 | 2 | 508 | 508 | 0.5413385826771654 | g=6,c=4,A=negative |
| g=2,c=1 -> g=4,c=3 | 4 | 254 | 508 | 0.484251968503937 | g=2,c=1,A=positive -> g=4,c=3,A=negative |
| g=2,c=2 -> g=6,c=6 | 4 | 247 | 494 | 0.4898785425101215 | g=2,c=2,A=negative -> g=6,c=6,A=negative |
| g=6,c=9 | 2 | 477 | 477 | 0.5450733752620545 | g=6,c=9,A=positive |
| g=2,c=3 -> g=6,c=9 | 4 | 235 | 470 | 0.44680851063829785 | g=2,c=3,A=positive -> g=6,c=9,A=positive |
| g=2,c=3 -> g=4,c=7 | 4 | 220 | 440 | 0.4 | g=2,c=3,A=negative -> g=4,c=7,A=positive |
| g=6,c=5 | 2 | 431 | 431 | 0.6102088167053364 | g=6,c=5,A=negative |
| g=2,c=1 -> g=6,c=4 | 4 | 214 | 428 | 0.4532710280373832 | g=2,c=1,A=negative -> g=6,c=4,A=positive |
| g=4,c=3 -> g=8,c=5 | 5 | 210 | 420 | 0.4714285714285714 | g=4,c=3,A=positive -> g=8,c=5,A=negative |
| g=10,c=15 -> g=2,c=3 | 4 | 209 | 418 | 0.32057416267942584 | g=10,c=15,A=positive -> g=2,c=3,A=positive |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FiniteCycleSignatureLedgerImported | True | True | The previous finite cycle-signature ledger is imported. | none for import |
| CycleSignatureWeightCarrierLedger | True | True | Every raw/signed signature is assigned P-support, strip-support, endpoint class, and signed fragmentation data. | none for current deterministic carrier ledger |
| CycleSignatureWeightedPhaseSaving | False | False | Prove cancellation for the weighted carriers exposed here. | requires analytic phase input after signed refinement and thin-support handling |
| SignedRefinementWeightReconciliation | False | False | Reconcile raw-base cycle weights after signed A-step refinement. | requires cancellation or exact transfer across signed children of the same raw base |
| TraceKloostermanCompletion | False | False | Convert the weighted carriers to an admissible trace/Kloosterman family. | requires a new completion map, not supplied by this ledger |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | needs a trace-function realization of the weighted carrier, not only finite signatures |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | needs bilinear Kloosterman variables modulo q; the carrier is still signature/P/strip incidence |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | needs composite Type-II boxes; the carrier remains a path-template incidence ledger |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | needs admissible unbalanced convolution fractions; the carrier is not yet such a family |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | prime existence in short intervals does not control signature carrier phases |

```text
FKMS_trace_bilinear=candidate only after weighted carriers are realized as trace-function sums
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=candidate only after inverse-variable Kloosterman variables appear
Pascadi_composite_Type_II=not matched because carriers are not composite Type-II boxes
Wright_unbalanced_Kloosterman=not matched because carriers are not unbalanced convolution fractions
Li_short_interval_x_052=does not estimate the exposed signature carrier phases
```

结论：weighted phase saving 的组合载体已经被定位到 signed carriers、
raw-base/signed-child fragmentation 与 thin P-support carriers。该层不是
相位相消证明。

## 5. 最新最窄口

```text
SignedCycleSignatureCarrierWeightedPhaseSaving
AND RawBaseToSignedChildWeightReconciliation
AND ThinPSupportCarrierSummationWithoutLoss
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND TraceKloostermanCompletionOfCycleSignatureAndResidualPackets
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
cycle_signature_weight_carrier_closed=true
cycle_signature_weighted_phase_saving_closed=false
signed_refinement_weight_reconciliation_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_flow_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
