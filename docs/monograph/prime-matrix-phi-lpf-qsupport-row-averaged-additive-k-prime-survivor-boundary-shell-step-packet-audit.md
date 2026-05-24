# Prime Matrix Phi-LPF q-support row-averaged additive-k prime-survivor boundary shell-step packet 审计

**状态：** `boundary_layercake_rectangles_aggregated_to_shell_step_packets_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=6190 boundary layer-cake rectangles
aggregation=same row, strip, q-prefix count, q-start and q-end are merged into one shell-step packet
remaining=short shell phase saving, moving prime q denominator completion, and no-loss packet aggregation
```

## 2. shell-step packet 有限审计

```text
max_prime=1009
previous_layer_rectangle_count_total=6190
shell_step_packet_count_total=5106
rectangle_to_packet_reduction=1084
edge_count_total=177515
previous_edge_count_total=177515
packet_identity_verified=true
q_prefix_count_min=1
q_prefix_count_median=11.0
q_prefix_count_max=37
q_prefix_count_average=12.339992166079
m_shell_prime_count_min=1
m_shell_prime_count_median=3.0
m_shell_prime_count_max=12
m_shell_prime_count_average=3.023697610654
packet_edge_count_min=1
packet_edge_count_median=24.0
packet_edge_count_max=261
packet_edge_count_average=34.765961613788
m_block_count_min=1
m_block_count_median=1.0
m_block_count_max=3
multi_block_packet_count=1083
internal_prime_gap_packet_count=1083
internal_prime_gap_count_total=1084
source_rectangle_count_max=3
sum_sqrt_packet_edges=27183.603112015346
sqrt_total_edges=421.325290007614
naive_packet_sqrt_loss_factor=64.519277044879
previous_layer_sqrt_loss_factor=71.553080825699
sqrt_loss_factor_improvement=7.033803780820
all_packets_have_at_most_three_m_blocks=true
all_packets_have_m_shell_size_le_12=true
no_large_balanced_packet_ge_16=true
short_shell_phase_saving_closed=false
```

m-block 分桶：

| m_block_count | packet_count | edge_count |
| --- | --- | --- |
| 1 | 4023 | 116221 |
| 2 | 1082 | 61258 |
| 3 | 1 | 36 |

strip 分桶：

| strip | packet_count | edge_count |
| --- | --- | --- |
| lower_wing | 1032 | 29144 |
| right_tail | 2107 | 86751 |
| upper_wing | 1967 | 61620 |

source rectangle 合并数：

| source_rectangle_count | packet_count | edge_count |
| --- | --- | --- |
| 1 | 4023 | 116221 |
| 2 | 1082 | 61258 |
| 3 | 1 | 36 |

双侧阈值：

| threshold | packet_count | edge_count |
| --- | --- | --- |
| both>=2 | 3613 | 159156 |
| both>=3 | 2294 | 126736 |
| both>=4 | 1391 | 91549 |
| both>=5 | 644 | 52477 |
| both>=8 | 64 | 9152 |
| both>=10 | 5 | 959 |
| both>=16 | 0 | 0 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ShellStepPacketSupportAggregation | True | True | The 6190 layer rectangles are grouped into 5106 q-prefix shell-step packets without changing total edge mass. | none for the finite support aggregation |
| AtMostThreeMBlocksPerPacket | True | True | Every audited packet has at most three prime-m blocks. | none for the finite block-count ledger |
| LayerSqrtLossReduced | True | True | The naive square-root summation factor drops from 71.553080825699 to 64.519277044879 after packet aggregation. | this is only a finite accounting improvement, not analytic cancellation |
| UniformShortShellPhaseSaving | False | False | Prove cancellation for q-prefix packets whose m side has at most 12 primes and up to three blocks. | new short-shell completion or unbalanced trace estimate required |
| NoLossPacketSummation | False | False | Aggregate all 5106 packet estimates without comparable endpoint or Cauchy loss. | uniform packet-level summation principle remains required |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | packet aggregation reduces layer count but still leaves short m-shell packets outside a direct long bilinear input |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | each packet still needs a completed moving prime q denominator before Kloosterman input applies |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | multi-block short packets remain endpoint objects rather than a single long Type-II box |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | the q-long/m-short packet form is a plausible unbalanced interface after the exact phase model is completed |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval prime existence does not control these fixed-row short shell packets |

```text
FKMS_trace_bilinear=packet aggregation helps bookkeeping but still leaves short m-shells outside a direct long bilinear theorem
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=moving q denominators still need completion at packet level
Pascadi_composite_Type_II=multi-block packets remain endpoint shells rather than single long boxes
Wright_unbalanced_Kloosterman=q-long/m-short packet geometry is a candidate interface after exact phase modeling
Li_short_interval_x_052=does not supply packet-level fixed-row positivity or short-shell cancellation
```

结论：同一 q-prefix step 的 m-blocks 可以无损聚合，层数从 `6190` 降到 `5106`。
每个 packet 的 m 侧最多由 `3` 个 prime blocks 组成，m-shell 总大小仍不超过 `12`。
这压缩了求和账本并暴露 multi-block endpoint 结构；但短 shell 相位节省、移动 q 分母 completion 与 packet 级无损求和仍未闭合。

## 5. 最新最窄口

```text
UniformShortShellPhaseSavingForAtMostThreeBlockPackets
AND MovingPrimeQDenominatorCompletedTraceFamilyOnShellStepPackets
AND NoLossAggregationAcross5106ShellStepPackets
AND EndpointSummationByPartsForQPrefixLinePackets
AND DiagonalPGhostSubtractionDiscipline
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
packet_identity_verified=true
layer_aggregation_support_closed=true
short_shell_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_layer_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
