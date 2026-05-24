# Prime Matrix Phi-LPF q-prefix carry switch flow decomposition 审计

**状态：** `qprefix_switch_paths_have_loop_erased_cycle_flow_core_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=147799 adjacent carry-letter switch edges across 13355 switch atoms
operation=deterministic loop erasure of each raw and signed switch path
dominant_shape=majority cycle-flow core plus short endpoint residual paths
remaining=phase saving on cycle packets, residual endpoint summation, and trace/Kloosterman completion
```

## 2. loop-erased cycle/residual 审计

```text
max_prime=1009
flow_decomposition_atom_count_total=15439
switch_atom_count=13355
non_switch_atom_count=2084
adjacent_letter_pair_count_inside_atoms=147799
loop_erased_flow_decomposition_closed=true
raw_cycle_packet_count=45178
raw_cycle_edge_mass=117733
raw_residual_edge_mass=30066
raw_cycle_edge_ratio=0.7965750783158209
raw_cycle_length_min/median/max=1/2.0/10
raw_residual_length_min/median/max=0/2/9
signed_cycle_packet_count=36330
signed_cycle_edge_mass=107677
signed_residual_edge_mass=40122
signed_cycle_edge_ratio=0.7285367289359197
signed_cycle_length_min/median/max=1/2.0/14
signed_residual_length_min/median/max=0/3/15
cycle_packet_phase_saving_closed=false
residual_endpoint_path_summation_closed=false
row_column_unconditional_closed=false
```

raw cycle length 分布：

| cycle_length | cycle_count |
| --- | --- |
| 1 | 5602 |
| 2 | 21446 |
| 3 | 8645 |
| 4 | 5967 |
| 5 | 2078 |
| 6 | 1129 |
| 7 | 233 |
| 8 | 64 |
| 9 | 11 |
| 10 | 3 |

raw residual length 分布：

| residual_length | atom_count |
| --- | --- |
| 0 | 1589 |
| 1 | 3313 |
| 2 | 3197 |
| 3 | 2558 |
| 4 | 1471 |
| 5 | 775 |
| 6 | 295 |
| 7 | 112 |
| 8 | 33 |
| 9 | 12 |

signed cycle length 分布：

| cycle_length | cycle_count |
| --- | --- |
| 1 | 3360 |
| 2 | 15401 |
| 3 | 7145 |
| 4 | 5052 |
| 5 | 2557 |
| 6 | 1489 |
| 7 | 810 |
| 8 | 297 |
| 9 | 125 |
| 10 | 65 |
| 11 | 19 |
| 12 | 8 |
| 13 | 1 |
| 14 | 1 |

signed residual length 分布：

| residual_length | atom_count |
| --- | --- |
| 0 | 1056 |
| 1 | 2573 |
| 2 | 2603 |
| 3 | 2386 |
| 4 | 1827 |
| 5 | 1255 |
| 6 | 762 |
| 7 | 439 |
| 8 | 249 |
| 9 | 128 |
| 10 | 51 |
| 11 | 14 |
| 12 | 9 |
| 13 | 2 |
| 15 | 1 |

strip flow 分桶：

| strip | switch_edge_count | raw_cycle_edge_mass | raw_residual_edge_mass | signed_cycle_edge_mass | signed_residual_edge_mass |
| --- | --- | --- | --- | --- | --- |
| lower_wing | 24352 | 19267 | 5085 | 17498 | 6854 |
| right_tail | 73375 | 59321 | 14054 | 54281 | 19094 |
| upper_wing | 50072 | 39145 | 10927 | 35898 | 14174 |

最高频 raw residual endpoint pairs：

| start | end | count |
| --- | --- | --- |
| g=2,c=3 | g=2,c=3 | 143 |
| g=4,c=6 | g=2,c=3 | 139 |
| g=4,c=3 | g=6,c=4 | 115 |
| g=4,c=4 | g=4,c=4 | 110 |
| g=2,c=3 | g=6,c=9 | 104 |
| g=6,c=6 | g=4,c=4 | 100 |
| g=2,c=3 | g=4,c=7 | 98 |
| g=4,c=6 | g=6,c=9 | 94 |
| g=4,c=4 | g=2,c=2 | 91 |
| g=4,c=7 | g=2,c=3 | 91 |
| g=6,c=4 | g=6,c=4 | 90 |
| g=6,c=10 | g=6,c=10 | 88 |
| g=6,c=10 | g=2,c=3 | 87 |
| g=2,c=1 | g=6,c=4 | 87 |
| g=4,c=5 | g=4,c=5 | 83 |
| g=4,c=7 | g=2,c=4 | 83 |
| g=4,c=7 | g=6,c=10 | 82 |
| g=4,c=3 | g=4,c=3 | 82 |
| g=4,c=4 | g=6,c=6 | 79 |
| g=4,c=6 | g=4,c=6 | 77 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FiniteCarrySwitchGraphImported | True | True | The previous finite switch graph ledger is imported. | none for import |
| LoopErasedCycleFlowDecomposition | True | True | Every switch path is split into peeled cycles and one endpoint residual path. | none for current deterministic ledger |
| CyclePacketPhaseSaving | False | False | Prove cancellation for the peeled cycle packets. | requires new exponential-sum or trace/Kloosterman input |
| ResidualEndpointPathSummation | False | False | Control the loop-erased endpoint residual paths without losing the boundary gain. | requires residual endpoint summation or analytic compression |
| NoLossQPrefixFlowAtomAggregation | False | False | Aggregate cycle and residual estimates across all fixed-m atoms. | requires no-loss aggregation discipline |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | cycle packets still need conversion to trace functions before trace bilinear estimates apply |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | cycle-flow packets are not yet inverse-variable Kloosterman sums modulo q |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | loop-erased cycles remain one-dimensional path packets, not balanced composite Type-II rectangles |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced Kloosterman input remains candidate only after cycle/residual paths become admissible fractions |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short interval prime existence does not estimate loop-erased switch-cycle phases |

```text
FKMS_trace_bilinear=cycle packets still need trace-function completion
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=loop cycles are not yet Kloosterman inverse families
Pascadi_composite_Type_II=cycle/residual paths remain one-dimensional rather than Type-II boxes
Wright_unbalanced_Kloosterman=candidate only after paths are converted to admissible unbalanced fractions
Li_short_interval_x_052=prime existence does not estimate cycle/residual reciprocal phases
```

结论：high-branch switch paths 已经被确定性分成 loop-erased cycle core
与 endpoint residual path。该层是结构分解，不是相位相消。

## 5. 最新最窄口

```text
CyclePacketPhaseSavingForLoopErasedCarrySwitchCore
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND TraceKloostermanCompletionOfCycleAndResidualPackets
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
loop_erased_cycle_flow_core_closed=true
cycle_packet_phase_saving_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_flow_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
