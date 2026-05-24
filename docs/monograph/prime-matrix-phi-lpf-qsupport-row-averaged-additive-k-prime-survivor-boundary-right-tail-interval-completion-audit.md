# Prime Matrix Phi-LPF right-tail interval completion 审计

**状态：** `right_tail_fibres_and_multi_block_gaps_completed_to_p_punctured_intervals_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=right-tail fibres and 1083 right-tail multi-block shell-step packets
identity=right-tail fibres are prime intervals punctured only at P; multi-block shells complete to prime intervals by adding successor core and P
remaining=phase saving on punctured interval differences, single-block endpoint summation, moving q denominator completion
```

## 2. punctured interval 有限审计

```text
max_prime=1009
shell_step_packet_count_total=5106
edge_count_total=177515
packet_identity_inherited=true
right_tail_fibre_count_total=3011
right_tail_fibre_edge_proxy_total=86751
right_tail_fibre_contiguous_count=138
right_tail_fibre_p_punctured_count=2873
right_tail_fibre_other_holes_count=0
all_right_tail_fibres_are_punctured_intervals=true
right_tail_fibre_interval_length_min=1
right_tail_fibre_interval_length_median=26
right_tail_fibre_interval_length_max=91
right_tail_multi_block_packet_count=1083
multi_block_edge_count=61294
multi_block_interval_completion_packet_count=1083
multi_block_interval_completion_edge_count=61294
multi_block_completion_other_holes_packet_count=0
all_multi_block_packets_complete_to_intervals=true
shell_prime_count_min=2
shell_prime_count_median=4
shell_prime_count_max=12
completed_interval_prime_count_min=3
completed_interval_prime_count_median=31
completed_interval_prime_count_max=87
successor_core_count_min=0
successor_core_count_median=25
successor_core_count_max=78
completion_missing_after_core_count_min=1
completion_missing_after_core_count_median=1
completion_missing_after_core_count_max=1
right_tail_fibre_punctured_interval_identity_closed=true
right_tail_multi_block_successor_core_interval_completion_closed=true
right_tail_punctured_interval_phase_saving_closed=false
```

right-tail fibre class 分桶：

| fibre_class | fibre_count | edge_weight_sum |
| --- | --- | --- |
| contiguous_prime_interval | 138 | 245 |
| p_punctured_prime_interval | 2873 | 86506 |

multi-block completion class 分桶：

| completion_class | packet_count | edge_weight_sum |
| --- | --- | --- |
| shell_successor_core_plus_p_completes_interval | 1083 | 61294 |

q-prefix packet 分桶：

| q_prefix_bin | packet_count | edge_weight_sum |
| --- | --- | --- |
| 17<=q<=37 | 365 | 35129 |
| 2<=q<=4 | 117 | 1756 |
| 5<=q<=8 | 213 | 6709 |
| 9<=q<=16 | 328 | 17318 |
| q=1 | 60 | 382 |

completed interval size 分桶：

| completed_interval_bin | packet_count | edge_weight_sum |
| --- | --- | --- |
| 17<=interval<=32 | 273 | 18559 |
| 1<=interval<=4 | 46 | 2817 |
| 33<=interval<=90 | 516 | 20038 |
| 5<=interval<=8 | 92 | 6901 |
| 9<=interval<=16 | 156 | 12979 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RightTailDiagonalCoreImported | True | True | The successor-core plus diagonal-P decomposition is inherited. | none for support import |
| RightTailFibrePuncturedIntervalIdentity | True | True | Every right-tail fibre is a contiguous prime interval, possibly with P removed. | none for the finite right-tail fibre ledger |
| RightTailMultiBlockSuccessorCoreIntervalCompletion | True | True | Every multi-block shell plus successor core and P completes to one prime interval. | none for finite support completion |
| RightTailPuncturedIntervalPhaseSaving | False | False | Prove cancellation on nested P-punctured interval differences with moving q denominator. | new endpoint/unbalanced trace estimate required |
| SingleBlockEndpointPhaseSaving | False | False | Prove cancellation or summation-by-parts for the single-block packets. | moving q denominator and packet aggregation remain open |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | right-tail support is now a punctured interval difference, but trace input still needs a completed phase family |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | arbitrary-modulus Kloosterman bounds become relevant only after the moving prime q denominator is completed on punctured intervals |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | composite Type-II savings still do not directly cover a nested endpoint punctured-interval difference |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced Kloosterman fractions are the closest candidate once the q-long punctured interval phase is completed |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval prime existence does not supply fixed-row punctured-interval reciprocal phase cancellation |

```text
FKMS_trace_bilinear=punctured intervals are simpler support, but no completed trace family is yet supplied
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=arbitrary q Kloosterman input still requires completing the moving prime denominator
Pascadi_composite_Type_II=endpoint punctured interval differences are not direct long Type-II boxes
Wright_unbalanced_Kloosterman=q-long punctured intervals are the most plausible unbalanced interface after exact phase modeling
Li_short_interval_x_052=short-interval existence at exponent 0.52 remains above the half-scale and does not give reciprocal phase saving
```

结论：successor core 不是任意稀疏残差；它把 right-tail multi-block shell 补回一个 `P`-punctured prime interval。
因此 right-tail multi-block 的支撑硬点从 gap/core 分类压成 nested punctured interval difference。
剩余仍是相位节省、移动分母 completion 与 packet 无损聚合。

## 5. 最新最窄口

```text
RightTailPuncturedIntervalDifferencePhaseSaving
AND SingleBlockEndpointPacketSummationByParts
AND MovingPrimeQDenominatorCompletedTraceFamilyOnPuncturedIntervalsAndSingleBlockPackets
AND NoLossAggregationAcross5106ShellStepPackets
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
right_tail_fibre_punctured_interval_identity_closed=true
right_tail_multi_block_successor_core_interval_completion_closed=true
right_tail_punctured_interval_phase_saving_closed=false
single_block_packet_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_packet_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
