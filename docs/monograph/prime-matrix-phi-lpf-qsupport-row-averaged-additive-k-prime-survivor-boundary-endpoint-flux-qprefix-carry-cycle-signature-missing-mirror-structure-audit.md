# Prime Matrix Phi-LPF q-prefix carry cycle signature missing-mirror structure 审计

**状态：** `missing_mirror_structure_ledger_closed_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=missing-mirror signed-child residual carriers
operation=strip/endpoint/A-class/length/P-support/raw-base structure audit
dominant_shape=missing-mirror mass is mostly mixed-sign and one-strip endpoint support, not yet a trace family
remaining=phase saving for missing-mirror endpoint carriers and completion to an admissible trace/Kloosterman family
```

## 2. missing-mirror structure 审计

```text
max_prime=1009
missing_mirror_structure_ledger_closed=true
missing_mirror_edge_mass=62980
missing_mirror_pair_count=7156
missing_raw_base_count=5114
single_P_missing_edge_mass=26797
single_P_missing_edge_ratio=0.4254842807240394
single_strip_missing_edge_mass=62952
single_strip_missing_edge_ratio=0.9995554144172754
wing_single_shell_missing_edge_mass=30538
wing_single_shell_missing_edge_ratio=0.48488409018736106
right_tail_missing_edge_mass=32442
right_tail_missing_edge_ratio=0.5151159098126389
missing_raw_base_share_min/median/max=0.004761904761904762/1.0/1.0
row_column_unconditional_closed=false
```

missing strip edge mass：

| strip | edge_mass | edge_ratio |
| --- | --- | --- |
| right_tail | 32442 | 0.5151159098126389 |
| upper_wing | 20318 | 0.32261035249285486 |
| lower_wing | 10220 | 0.1622737376945062 |

missing endpoint group edge mass：

| endpoint_group | edge_mass | edge_ratio |
| --- | --- | --- |
| right_tail_two_sided_collar | 21925 | 0.348126389329946 |
| upper_wing_single_shell | 20318 | 0.32261035249285486 |
| lower_wing_single_shell | 10220 | 0.1622737376945062 |
| right_tail_right_collar | 5091 | 0.08083518577326135 |
| right_tail_left_collar | 3925 | 0.06232137186408383 |
| right_tail_terminal_full_interval | 1501 | 0.02383296284534773 |

missing A-class edge mass：

| A_class | edge_mass | edge_ratio |
| --- | --- | --- |
| mixed_positive_negative | 61317 | 0.9735947919974595 |
| all_positive | 742 | 0.011781517942203874 |
| all_negative | 517 | 0.008208955223880597 |
| mixed_with_zero | 404 | 0.006414734836456017 |

missing cycle length edge mass：

| cycle_length | edge_mass | edge_ratio |
| --- | --- | --- |
| 4 | 16296 | 0.25874880914576054 |
| 3 | 12663 | 0.20106382978723406 |
| 5 | 12290 | 0.19514131470308035 |
| 6 | 8730 | 0.13861543347094316 |
| 7 | 5621 | 0.0892505557319784 |
| 2 | 2892 | 0.04591933947284852 |
| 8 | 2376 | 0.03772626230549381 |
| 9 | 1125 | 0.017862813591616386 |
| 10 | 650 | 0.010320736741822802 |
| 11 | 209 | 0.0033185138139091774 |
| 12 | 96 | 0.0015242934264845982 |
| 14 | 14 | 0.00022229279136233725 |
| 13 | 13 | 0.000206414734836456 |
| 1 | 5 | 7.939028262940616e-05 |

missing P-width bucket edge mass：

| P_width_bucket | edge_mass | edge_ratio |
| --- | --- | --- |
| single_P | 26797 | 0.4254842807240394 |
| P_width_2_to_4 | 20380 | 0.3235947919974595 |
| P_width_5_to_16 | 12741 | 0.20230231819625277 |
| P_width_17_to_64 | 3062 | 0.04861860908224833 |

最高 missing signed-child carriers：

| signed_child | missing_mirror_child | raw_base_template | missing_edge_mass | cycle_length | A_class | P_support_width | P_width_bucket | strip_profile | endpoint_profile | raw_base_child_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g=2,c=4,A=positive -> g=4,c=6,A=negative | g=2,c=4,A=negative -> g=4,c=6,A=positive | g=2,c=4 -> g=4,c=6 | 208 | 2 | mixed_positive_negative | 50 | P_width_17_to_64 | upper_wing:208 | upper_wing_single_contiguous_endpoint_shell:208 | 2 |
| g=2,c=2,A=positive -> g=4,c=2,A=negative | g=2,c=2,A=negative -> g=4,c=2,A=positive | g=2,c=2 -> g=4,c=2 | 202 | 2 | mixed_positive_negative | 54 | P_width_17_to_64 | lower_wing:202 | lower_wing_single_contiguous_endpoint_shell:202 | 3 |
| g=2,c=2,A=positive -> g=6,c=6,A=positive -> g=6,c=5,A=negative | g=2,c=2,A=negative -> g=6,c=6,A=negative -> g=6,c=5,A=positive | g=2,c=2 -> g=6,c=6 -> g=6,c=5 | 141 | 3 | mixed_positive_negative | 29 | P_width_17_to_64 | right_tail:141 | right_tail_left_collar_only_no_P_puncture:30,right_tail_left_collar_only_with_P_puncture:9,right_tail_terminal_full_interval_no_P_puncture:3,right_tail_terminal_full_interval_with_P_puncture:6,right_tail_two_sided_left_and_right_collars_no_P_puncture:87,right_tail_two_sided_left_and_right_collars_with_P_puncture:6 | 4 |
| g=14,c=15,A=positive -> g=4,c=4,A=negative | g=14,c=15,A=negative -> g=4,c=4,A=positive | g=14,c=15 -> g=4,c=4 | 134 | 2 | mixed_positive_negative | 23 | P_width_17_to_64 | right_tail:134 | right_tail_right_collar_only_no_P_puncture:42,right_tail_right_collar_only_with_P_puncture:6,right_tail_terminal_full_interval_no_P_puncture:2,right_tail_two_sided_left_and_right_collars_no_P_puncture:80,right_tail_two_sided_left_and_right_collars_with_P_puncture:4 | 3 |
| g=4,c=2,A=negative -> g=8,c=6,A=positive | g=4,c=2,A=positive -> g=8,c=6,A=negative | g=4,c=2 -> g=8,c=6 | 124 | 2 | mixed_positive_negative | 36 | P_width_17_to_64 | lower_wing:124 | lower_wing_single_contiguous_endpoint_shell:124 | 3 |
| g=4,c=6,A=negative -> g=8,c=14,A=positive | g=4,c=6,A=positive -> g=8,c=14,A=negative | g=4,c=6 -> g=8,c=14 | 124 | 2 | mixed_positive_negative | 29 | P_width_17_to_64 | upper_wing:124 | upper_wing_single_contiguous_endpoint_shell:124 | 3 |
| g=4,c=7,A=positive -> g=8,c=12,A=negative | g=4,c=7,A=negative -> g=8,c=12,A=positive | g=4,c=7 -> g=8,c=12 | 122 | 2 | mixed_positive_negative | 32 | P_width_17_to_64 | upper_wing:122 | upper_wing_single_contiguous_endpoint_shell:122 | 3 |
| g=4,c=6,A=positive -> g=6,c=8,A=negative -> g=8,c=12,A=negative | g=4,c=6,A=negative -> g=6,c=8,A=positive -> g=8,c=12,A=positive | g=4,c=6 -> g=6,c=8 -> g=8,c=12 | 117 | 3 | mixed_positive_negative | 27 | P_width_17_to_64 | upper_wing:117 | upper_wing_single_contiguous_endpoint_shell:117 | 3 |
| g=2,c=2,A=negative -> g=6,c=6,A=negative -> g=6,c=7,A=positive | g=2,c=2,A=positive -> g=6,c=6,A=positive -> g=6,c=7,A=negative | g=2,c=2 -> g=6,c=6 -> g=6,c=7 | 108 | 3 | mixed_positive_negative | 21 | P_width_17_to_64 | right_tail:108 | right_tail_right_collar_only_no_P_puncture:18,right_tail_terminal_full_interval_with_P_puncture:12,right_tail_two_sided_left_and_right_collars_no_P_puncture:69,right_tail_two_sided_left_and_right_collars_with_P_puncture:9 | 2 |
| g=4,c=4,A=negative -> g=8,c=9,A=positive -> g=6,c=6,A=negative | g=4,c=4,A=positive -> g=8,c=9,A=negative -> g=6,c=6,A=positive | g=4,c=4 -> g=8,c=9 -> g=6,c=6 | 108 | 3 | mixed_positive_negative | 22 | P_width_17_to_64 | right_tail:108 | right_tail_right_collar_only_no_P_puncture:24,right_tail_terminal_full_interval_with_P_puncture:3,right_tail_two_sided_left_and_right_collars_no_P_puncture:72,right_tail_two_sided_left_and_right_collars_with_P_puncture:9 | 4 |
| g=4,c=4,A=positive -> g=8,c=7,A=negative -> g=6,c=6,A=positive | g=4,c=4,A=negative -> g=8,c=7,A=positive -> g=6,c=6,A=negative | g=4,c=4 -> g=8,c=7 -> g=6,c=6 | 105 | 3 | mixed_positive_negative | 25 | P_width_17_to_64 | right_tail:105 | right_tail_left_collar_only_no_P_puncture:30,right_tail_left_collar_only_with_P_puncture:3,right_tail_terminal_full_interval_no_P_puncture:3,right_tail_terminal_full_interval_with_P_puncture:6,right_tail_two_sided_left_and_right_collars_no_P_puncture:63 | 4 |
| g=10,c=10,A=positive -> g=14,c=13,A=negative -> g=4,c=4,A=positive -> g=2,c=2,A=positive | g=10,c=10,A=negative -> g=14,c=13,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=negative | g=10,c=10 -> g=14,c=13 -> g=4,c=4 -> g=2,c=2 | 100 | 4 | mixed_positive_negative | 17 | P_width_17_to_64 | right_tail:100 | right_tail_left_collar_only_no_P_puncture:20,right_tail_left_collar_only_with_P_puncture:4,right_tail_terminal_full_interval_with_P_puncture:4,right_tail_two_sided_left_and_right_collars_no_P_puncture:60,right_tail_two_sided_left_and_right_collars_with_P_puncture:12 | 3 |
| g=4,c=7,A=positive -> g=6,c=9,A=negative | g=4,c=7,A=negative -> g=6,c=9,A=positive | g=4,c=7 -> g=6,c=9 | 94 | 2 | mixed_positive_negative | 27 | P_width_17_to_64 | upper_wing:94 | upper_wing_single_contiguous_endpoint_shell:94 | 4 |
| g=4,c=4,A=negative -> g=8,c=9,A=positive -> g=6,c=7,A=positive | g=4,c=4,A=positive -> g=8,c=9,A=negative -> g=6,c=7,A=negative | g=4,c=4 -> g=8,c=9 -> g=6,c=7 | 93 | 3 | mixed_positive_negative | 17 | P_width_17_to_64 | right_tail:93 | right_tail_right_collar_only_no_P_puncture:30,right_tail_two_sided_left_and_right_collars_no_P_puncture:63 | 5 |
| g=4,c=2,A=negative -> g=6,c=5,A=positive | g=4,c=2,A=positive -> g=6,c=5,A=negative | g=4,c=2 -> g=6,c=5 | 92 | 2 | mixed_positive_negative | 34 | P_width_17_to_64 | lower_wing:92 | lower_wing_single_contiguous_endpoint_shell:92 | 1 |
| g=10,c=10,A=negative -> g=14,c=15,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=negative | g=10,c=10,A=positive -> g=14,c=15,A=negative -> g=4,c=4,A=positive -> g=2,c=2,A=positive | g=10,c=10 -> g=14,c=15 -> g=4,c=4 -> g=2,c=2 | 84 | 4 | mixed_positive_negative | 16 | P_width_5_to_16 | right_tail:84 | right_tail_right_collar_only_no_P_puncture:20,right_tail_right_collar_only_with_P_puncture:12,right_tail_terminal_full_interval_with_P_puncture:4,right_tail_two_sided_left_and_right_collars_no_P_puncture:40,right_tail_two_sided_left_and_right_collars_with_P_puncture:8 | 4 |
| g=2,c=3,A=positive -> g=6,c=6,A=negative -> g=6,c=6,A=positive | g=2,c=3,A=negative -> g=6,c=6,A=positive -> g=6,c=6,A=negative | g=2,c=3 -> g=6,c=6 -> g=6,c=6 | 84 | 3 | mixed_positive_negative | 19 | P_width_17_to_64 | right_tail:84 | right_tail_right_collar_only_no_P_puncture:21,right_tail_terminal_full_interval_with_P_puncture:3,right_tail_two_sided_left_and_right_collars_no_P_puncture:54,right_tail_two_sided_left_and_right_collars_with_P_puncture:6 | 2 |
| g=10,c=10,A=negative -> g=12,c=13,A=positive -> g=2,c=2,A=negative | g=10,c=10,A=positive -> g=12,c=13,A=negative -> g=2,c=2,A=positive | g=10,c=10 -> g=12,c=13 -> g=2,c=2 | 81 | 3 | mixed_positive_negative | 15 | P_width_5_to_16 | right_tail:81 | right_tail_right_collar_only_no_P_puncture:24,right_tail_terminal_full_interval_no_P_puncture:3,right_tail_terminal_full_interval_with_P_puncture:3,right_tail_two_sided_left_and_right_collars_no_P_puncture:45,right_tail_two_sided_left_and_right_collars_with_P_puncture:6 | 2 |
| g=2,c=3,A=negative -> g=6,c=9,A=negative -> g=6,c=10,A=positive | g=2,c=3,A=positive -> g=6,c=9,A=positive -> g=6,c=10,A=negative | g=2,c=3 -> g=6,c=9 -> g=6,c=10 | 81 | 3 | mixed_positive_negative | 14 | P_width_5_to_16 | upper_wing:81 | upper_wing_single_contiguous_endpoint_shell:81 | 4 |
| g=10,c=10,A=negative -> g=2,c=2,A=negative -> g=12,c=13,A=positive | g=10,c=10,A=positive -> g=2,c=2,A=positive -> g=12,c=13,A=negative | g=10,c=10 -> g=2,c=2 -> g=12,c=13 | 78 | 3 | mixed_positive_negative | 17 | P_width_17_to_64 | right_tail:78 | right_tail_right_collar_only_no_P_puncture:15,right_tail_terminal_full_interval_no_P_puncture:6,right_tail_terminal_full_interval_with_P_puncture:6,right_tail_two_sided_left_and_right_collars_no_P_puncture:48,right_tail_two_sided_left_and_right_collars_with_P_puncture:3 | 5 |

最高 missing raw bases：

| raw_base_template | missing_edge_mass | raw_base_signed_edge_mass | missing_share_inside_raw_base | signed_child_count | strip_profile | endpoint_group_profile |
| --- | --- | --- | --- | --- | --- | --- |
| g=2,c=4 -> g=4,c=6 | 236 | 236 | 1.0 | 2 | upper_wing:236 | upper_wing_single_shell:236 |
| g=2,c=2 -> g=4,c=2 | 202 | 256 | 0.7890625 | 3 | lower_wing:202 | lower_wing_single_shell:202 |
| g=2,c=2 -> g=6,c=6 -> g=6,c=5 | 201 | 201 | 1.0 | 4 | right_tail:201 | right_tail_left_collar:51,right_tail_terminal_full_interval:9,right_tail_two_sided_collar:141 |
| g=4,c=4 -> g=8,c=7 -> g=6,c=6 | 189 | 189 | 1.0 | 4 | right_tail:189 | right_tail_left_collar:54,right_tail_terminal_full_interval:9,right_tail_two_sided_collar:126 |
| g=4,c=3 -> g=6,c=4 -> g=8,c=6 | 183 | 213 | 0.8591549295774648 | 5 | lower_wing:183 | lower_wing_single_shell:183 |
| g=4,c=6 -> g=6,c=8 -> g=8,c=12 | 177 | 177 | 1.0 | 3 | upper_wing:177 | upper_wing_single_shell:177 |
| g=4,c=4 -> g=8,c=9 -> g=6,c=6 | 174 | 174 | 1.0 | 4 | right_tail:174 | right_tail_right_collar:42,right_tail_terminal_full_interval:3,right_tail_two_sided_collar:129 |
| g=10,c=10 -> g=14,c=15 -> g=4,c=4 -> g=2,c=2 | 148 | 148 | 1.0 | 4 | right_tail:148 | right_tail_right_collar:48,right_tail_terminal_full_interval:8,right_tail_two_sided_collar:92 |
| g=2,c=3 -> g=6,c=9 -> g=6,c=10 | 147 | 147 | 1.0 | 4 | upper_wing:147 | upper_wing_single_shell:147 |
| g=4,c=4 -> g=8,c=9 -> g=6,c=7 | 144 | 198 | 0.7272727272727273 | 5 | right_tail:144 | right_tail_right_collar:51,right_tail_two_sided_collar:93 |
| g=2,c=2 -> g=6,c=6 -> g=6,c=7 | 138 | 138 | 1.0 | 2 | right_tail:138 | right_tail_right_collar:18,right_tail_terminal_full_interval:12,right_tail_two_sided_collar:108 |
| g=10,c=10 -> g=2,c=2 -> g=12,c=11 | 135 | 135 | 1.0 | 3 | right_tail:135 | right_tail_left_collar:36,right_tail_terminal_full_interval:12,right_tail_two_sided_collar:87 |
| g=14,c=15 -> g=4,c=4 | 134 | 150 | 0.8933333333333333 | 3 | right_tail:134 | right_tail_right_collar:48,right_tail_terminal_full_interval:2,right_tail_two_sided_collar:84 |
| g=4,c=4 -> g=8,c=8 -> g=6,c=7 | 132 | 132 | 1.0 | 3 | right_tail:132 | right_tail_right_collar:48,right_tail_two_sided_collar:84 |
| g=2,c=2 -> g=6,c=7 -> g=6,c=6 | 129 | 129 | 1.0 | 4 | right_tail:129 | right_tail_right_collar:42,right_tail_two_sided_collar:87 |
| g=2,c=2 -> g=4,c=4 -> g=6,c=5 -> g=6,c=6 | 128 | 128 | 1.0 | 4 | right_tail:128 | right_tail_left_collar:28,right_tail_terminal_full_interval:12,right_tail_two_sided_collar:88 |
| g=4,c=2 -> g=8,c=6 | 124 | 148 | 0.8378378378378378 | 3 | lower_wing:124 | lower_wing_single_shell:124 |
| g=4,c=6 -> g=8,c=14 | 124 | 144 | 0.8611111111111112 | 3 | upper_wing:124 | upper_wing_single_shell:124 |
| g=4,c=7 -> g=8,c=12 | 122 | 150 | 0.8133333333333334 | 3 | upper_wing:122 | upper_wing_single_shell:122 |
| g=4,c=4 -> g=6,c=6 -> g=8,c=9 | 117 | 117 | 1.0 | 3 | right_tail:117 | right_tail_right_collar:36,right_tail_terminal_full_interval:3,right_tail_two_sided_collar:78 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| MirrorImbalanceSupportLedgerImported | True | True | The previous mirror-imbalance support ledger is imported. | none for import |
| MissingMirrorStructureLedger | True | True | Every missing-mirror edge is assigned strip, endpoint, sign, length, P-support, and raw-base structure. | none for the finite structure ledger |
| MissingMirrorCarrierPhaseSaving | False | False | Prove cancellation or positivity for the missing-mirror carrier family. | requires analytic phase input on the exposed endpoint support |
| MissingMirrorTraceCompletion | False | False | Complete the missing-mirror endpoint carriers to admissible trace/Kloosterman sums. | requires an explicit completion map and no-loss aggregation |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | sub-Pólya-Vinogradov bilinear trace-function input, but only after missing carriers become trace sums |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | power-saving bilinear Kloosterman sums for arbitrary q, but requires explicit Kloosterman variables |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | composite-modulus Type-II Kloosterman amplification, not matched to missing signed-child templates |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced convolution/Kloosterman-fraction input, candidate only after endpoint carriers are completed |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence at exponent 0.52, still not a signed-carrier phase estimate |

```text
FKMS_trace_bilinear=not directly applicable before missing-mirror endpoint carriers become trace-function sums
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=not directly applicable before explicit Kloosterman variables are extracted
Pascadi_composite_Type_II=not matched because missing-mirror support is not a composite-modulus Type-II box
Wright_unbalanced_Kloosterman=candidate only after the endpoint support is converted to unbalanced Kloosterman fractions
Li_short_interval_x_052=does not estimate signed missing-mirror carrier phases
```

结论：missing-mirror 主体已经从匿名 residual mass 压成 endpoint/strip/P-support
结构账本。它仍不是 trace/Kloosterman family，也没有给出 phase saving。

## 5. 最新最窄口

```text
MissingMirrorEndpointCarrierPhaseSaving
AND MissingMirrorTraceKloostermanCompletion
AND UnequalMirrorPairResidualPhaseSaving
AND ThinPSupportCarrierSummationWithoutLoss
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
missing_mirror_structure_ledger_closed=true
missing_mirror_carrier_phase_saving_closed=false
missing_mirror_to_trace_completion_closed=false
unequal_mirror_pair_residual_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
