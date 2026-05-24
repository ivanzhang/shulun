# Prime Matrix Phi-LPF right-tail endpoint collar 审计

**状态：** `right_tail_punctured_interval_differences_split_into_endpoint_collars_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=2107 right-tail shell-step packets carrying 86751 edges
identity=each right-tail shell is a left collar, right collar, two endpoint collars, or terminal full interval, minus optional P
remaining=phase saving on endpoint collar flux with moving q denominator
```

## 2. endpoint collar 有限审计

```text
max_prime=1009
shell_step_packet_count_total=5106
edge_count_total=177515
packet_identity_inherited=true
right_tail_packet_count=2107
right_tail_edge_count=86751
right_tail_single_block_packet_count=1024
right_tail_multi_block_packet_count=1083
right_tail_endpoint_collar_identity_verified=true
bad_endpoint_collar_packet_count=0
terminal_full_interval_packet_count=150
two_sided_collar_packet_count=1007
one_sided_collar_packet_count=950
p_punctured_packet_count=146
left_collar_count_min=0
left_collar_count_median=1
left_collar_count_max=10
right_collar_count_min=0
right_collar_count_median=2
right_collar_count_max=9
completed_collar_count_min=1
completed_collar_count_median=3
completed_collar_count_max=13
right_tail_endpoint_collar_flux_identity_closed=true
right_tail_endpoint_collar_phase_saving_closed=false
```

collar class 分桶：

| collar_class | packet_count | edge_weight_sum |
| --- | --- | --- |
| left_collar_only_no_P_puncture | 314 | 8652 |
| left_collar_only_with_P_puncture | 19 | 776 |
| right_collar_only_no_P_puncture | 604 | 12879 |
| right_collar_only_with_P_puncture | 13 | 708 |
| terminal_full_interval_no_P_puncture | 75 | 2487 |
| terminal_full_interval_with_P_puncture | 75 | 4864 |
| two_sided_left_and_right_collars_no_P_puncture | 968 | 52957 |
| two_sided_left_and_right_collars_with_P_puncture | 39 | 3428 |

collar class x m-block 分桶：

| collar_class | m_block_count | packet_count | edge_weight_sum |
| --- | --- | --- | --- |
| left_collar_only_no_P_puncture | 1 | 314 | 8652 |
| left_collar_only_with_P_puncture | 1 | 18 | 731 |
| left_collar_only_with_P_puncture | 2 | 1 | 45 |
| right_collar_only_no_P_puncture | 1 | 604 | 12879 |
| right_collar_only_with_P_puncture | 1 | 13 | 708 |
| terminal_full_interval_no_P_puncture | 1 | 75 | 2487 |
| terminal_full_interval_with_P_puncture | 2 | 75 | 4864 |
| two_sided_left_and_right_collars_no_P_puncture | 2 | 968 | 52957 |
| two_sided_left_and_right_collars_with_P_puncture | 2 | 38 | 3392 |
| two_sided_left_and_right_collars_with_P_puncture | 3 | 1 | 36 |

q-prefix packet 分桶：

| q_prefix_bin | packet_count | edge_weight_sum |
| --- | --- | --- |
| 17<=q<=37 | 698 | 50142 |
| 2<=q<=4 | 278 | 2834 |
| 5<=q<=8 | 395 | 8933 |
| 9<=q<=16 | 616 | 24294 |
| q=1 | 120 | 548 |

completed collar size 分桶：

| completed_collar_bin | packet_count | edge_weight_sum |
| --- | --- | --- |
| 1<=collar<=2 | 840 | 16942 |
| 3<=collar<=4 | 736 | 33867 |
| 5<=collar<=8 | 490 | 34223 |
| 9<=collar<=13 | 41 | 1719 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RightTailPuncturedIntervalImported | True | True | Right-tail fibres are inherited as P-punctured prime intervals. | none for support import |
| RightTailEndpointCollarFluxIdentity | True | True | Every right-tail shell-step packet is an endpoint collar flux minus optional P. | none for finite endpoint-collar support |
| RightTailEndpointCollarPhaseSaving | False | False | Prove cancellation on left/right/terminal endpoint collar flux packets. | new completed trace or unbalanced endpoint estimate required |
| MovingPrimeQDenominatorCompletion | False | False | Complete the moving q denominator on endpoint collar packets. | not supplied by the support ledger |
| NoLossPacketAggregation | False | False | Aggregate endpoint collar phase savings over all shell-step packets without comparable loss. | requires analytic summation discipline |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | endpoint-collar support is simpler, but trace bilinear estimates still need a completed moving-denominator phase family |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | collar flux still has prime q denominators moving with the row before arbitrary-modulus Kloosterman input applies |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | endpoint collars are short flux packets, not a direct long composite Type-II rectangle |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | q-long endpoint collars are the closest unbalanced Kloosterman candidate after exact phase completion |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | prime existence in x^0.52 intervals still does not supply endpoint-collar reciprocal phase cancellation |

```text
FKMS_trace_bilinear=endpoint collar support is explicit but no completed trace family is supplied
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=moving prime q denominators remain the central completion problem
Pascadi_composite_Type_II=short endpoint collar flux is not a direct long Type-II input
Wright_unbalanced_Kloosterman=q-long endpoint collars are the nearest unbalanced Kloosterman target after completion
Li_short_interval_x_052=short-interval prime existence does not imply fixed-row endpoint-collar reciprocal phase saving
```

结论：right-tail punctured interval difference 已经压成左右 endpoint collar flux 与 terminal full interval flux。
multi-block 主要来自 two-sided collar，少数来自 P-punctured collar；没有其他支撑误差。
剩余仍是 endpoint collar 相位节省与 moving q denominator completion。

## 5. 最新最窄口

```text
RightTailEndpointCollarFluxPhaseSaving
AND SingleBlockEndpointPacketSummationByParts
AND MovingPrimeQDenominatorCompletedTraceFamilyOnEndpointCollarsAndSingleBlockPackets
AND NoLossAggregationAcross5106ShellStepPackets
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
right_tail_endpoint_collar_flux_identity_closed=true
right_tail_endpoint_collar_phase_saving_closed=false
single_block_packet_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_packet_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
