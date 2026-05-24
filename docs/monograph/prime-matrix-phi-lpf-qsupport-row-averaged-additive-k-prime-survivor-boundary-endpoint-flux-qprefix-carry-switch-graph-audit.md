# Prime Matrix Phi-LPF q-prefix carry switch graph 审计

**状态：** `qprefix_carry_letter_words_have_finite_switch_graph_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=117 raw letters, 256 signed letters, and 147799 adjacent letter pairs
raw_switch=L_i=(g_i,c_i) -> L_{i+1}=(g_{i+1},c_{i+1})
signed_switch=L_i^+ -> L_{i+1}^+ with A-step signs
dominant_shape=connected high-branch finite switch graph rather than deterministic low-branch law
remaining=switch-graph exponential-sum saving or completion to a trace/Kloosterman family
```

## 2. switch graph 有限审计

```text
max_prime=1009
carry_switch_atom_count_total=15439
multiq_atom_count=14277
singleton_q_atom_count=1162
successor_transition_count_total=162076
adjacent_letter_pair_count_inside_atoms=147799
raw_switch_pair_count_total=147799
signed_switch_pair_count_total=147799
switch_graph_decomposition_closed=true
per_atom_switch_count_median/max=9/35
raw_graph_nodes/edges/density=117/1161/0.08481262327416174
signed_graph_nodes/edges/density=256/4017/0.0612945556640625
raw_outdegree_min/median/max=0/8/54
signed_outdegree_min/median/max=0/10.0/100
raw_largest_weak/scc=117/115
signed_largest_weak/scc=255/250
raw_changed_letter_pair_count/ratio=142197/0.962097172511316
changed_gap_pair_count/ratio=136761/0.9253174919992693
changed_carry_pair_count/ratio=140789/0.9525707210468272
changed_A_step_sign_pair_count/ratio=91187/0.6169662852928639
deterministic_switching_law_closed=false
finite_switch_graph_phase_saving_closed=false
row_column_unconditional_closed=false
```

最高频 raw switch edges：

| raw_switch | count |
| --- | --- |
| g=2,c=2 -> g=4,c=4 | 2093 |
| g=4,c=4 -> g=2,c=2 | 1890 |
| g=6,c=6 -> g=6,c=6 | 1439 |
| g=4,c=4 -> g=6,c=6 | 1436 |
| g=2,c=3 -> g=4,c=6 | 1359 |
| g=4,c=6 -> g=6,c=9 | 1336 |
| g=4,c=6 -> g=2,c=3 | 1317 |
| g=6,c=6 -> g=4,c=4 | 1212 |
| g=6,c=6 -> g=2,c=2 | 1166 |
| g=4,c=3 -> g=6,c=4 | 1090 |
| g=8,c=12 -> g=4,c=6 | 1044 |
| g=2,c=3 -> g=6,c=9 | 1002 |
| g=4,c=4 -> g=8,c=8 | 944 |
| g=6,c=9 -> g=6,c=9 | 920 |
| g=8,c=8 -> g=4,c=4 | 905 |
| g=6,c=7 -> g=6,c=7 | 893 |
| g=2,c=1 -> g=4,c=3 | 890 |
| g=2,c=2 -> g=4,c=5 | 883 |
| g=6,c=9 -> g=2,c=3 | 879 |
| g=6,c=4 -> g=6,c=4 | 863 |

最高频 signed switch edges：

| signed_switch | count |
| --- | --- |
| g=2,c=2,A=negative -> g=4,c=4,A=negative | 820 |
| g=4,c=4,A=negative -> g=2,c=2,A=negative | 785 |
| g=2,c=2,A=positive -> g=4,c=4,A=positive | 761 |
| g=4,c=4,A=positive -> g=2,c=2,A=positive | 670 |
| g=6,c=6,A=negative -> g=6,c=6,A=negative | 545 |
| g=4,c=4,A=negative -> g=6,c=6,A=negative | 512 |
| g=4,c=4,A=positive -> g=6,c=6,A=positive | 505 |
| g=2,c=2,A=negative -> g=4,c=5,A=positive | 502 |
| g=6,c=6,A=positive -> g=6,c=6,A=positive | 464 |
| g=4,c=3,A=positive -> g=6,c=4,A=negative | 444 |
| g=6,c=6,A=negative -> g=4,c=4,A=negative | 443 |
| g=2,c=3,A=positive -> g=4,c=6,A=positive | 442 |
| g=6,c=6,A=positive -> g=4,c=4,A=positive | 436 |
| g=2,c=2,A=negative -> g=4,c=4,A=positive | 428 |
| g=6,c=6,A=negative -> g=2,c=2,A=negative | 424 |
| g=4,c=5,A=positive -> g=2,c=2,A=negative | 409 |
| g=4,c=6,A=positive -> g=2,c=3,A=positive | 405 |
| g=6,c=5,A=negative -> g=2,c=2,A=positive | 402 |
| g=4,c=6,A=negative -> g=6,c=9,A=positive | 387 |
| g=6,c=6,A=positive -> g=2,c=2,A=positive | 386 |

最高频 raw delta：

| delta_gap | delta_carry | count |
| --- | --- | --- |
| 2 | 2 | 12265 |
| 2 | 3 | 9842 |
| -2 | -2 | 9665 |
| -2 | -3 | 7197 |
| 2 | 1 | 5907 |
| 0 | 0 | 5602 |
| -4 | -4 | 5322 |
| -4 | -5 | 4732 |
| -2 | -1 | 4488 |
| 4 | 4 | 4421 |
| -4 | -6 | 4359 |
| -4 | -3 | 4346 |
| 4 | 5 | 4031 |
| 4 | 3 | 3894 |
| 2 | 4 | 3653 |
| 4 | 6 | 3460 |
| -4 | -7 | 2764 |
| 0 | 1 | 2740 |
| 0 | -1 | 2696 |
| 4 | 7 | 2040 |

switch class 分桶：

| switch_class | count |
| --- | --- |
| changed_carry | 140789 |
| changed_gap | 136761 |
| changed_raw_letter | 142197 |
| same_carry | 7010 |
| same_gap | 11038 |
| same_raw_letter | 5602 |

A-step sign switch 分桶：

| sign_switch_class | count |
| --- | --- |
| changed_A_step_sign | 91187 |
| same_A_step_sign | 56612 |

strip switch 分桶：

| strip | switch_count |
| --- | --- |
| lower_wing | 24352 |
| right_tail | 73375 |
| upper_wing | 50072 |

raw outdegree 分布：

| outdegree | node_count |
| --- | --- |
| 0 | 2 |
| 1 | 2 |
| 2 | 21 |
| 3 | 11 |
| 4 | 5 |
| 5 | 4 |
| 6 | 6 |
| 7 | 7 |
| 8 | 3 |
| 9 | 8 |
| 10 | 5 |
| 11 | 8 |
| 12 | 5 |
| 13 | 5 |
| 14 | 1 |
| 15 | 4 |
| 16 | 2 |
| 19 | 1 |
| 20 | 1 |
| 22 | 3 |
| 23 | 4 |
| 24 | 1 |
| 26 | 2 |
| 27 | 1 |
| 28 | 2 |
| 34 | 1 |
| 50 | 1 |
| 54 | 1 |

signed outdegree 分布：

| outdegree | node_count |
| --- | --- |
| 0 | 5 |
| 1 | 15 |
| 2 | 11 |
| 3 | 11 |
| 4 | 40 |
| 5 | 8 |
| 6 | 6 |
| 7 | 8 |
| 8 | 10 |
| 9 | 9 |
| 10 | 6 |
| 11 | 4 |
| 12 | 3 |
| 13 | 5 |
| 14 | 9 |
| 15 | 7 |
| 16 | 6 |
| 17 | 7 |
| 18 | 11 |
| 19 | 8 |
| 20 | 9 |
| 21 | 7 |
| 22 | 3 |
| 23 | 3 |
| 24 | 2 |
| 25 | 1 |
| 26 | 1 |
| 27 | 1 |
| 29 | 3 |
| 30 | 2 |
| 32 | 2 |
| 36 | 1 |
| 38 | 2 |
| 39 | 3 |
| 40 | 2 |
| 41 | 2 |
| 42 | 4 |
| 43 | 3 |
| 45 | 1 |
| 46 | 1 |
| 49 | 3 |
| 50 | 1 |
| 52 | 1 |
| 53 | 1 |
| 54 | 1 |
| 55 | 1 |
| 58 | 1 |
| 67 | 1 |
| 91 | 1 |
| 92 | 1 |
| 96 | 1 |
| 100 | 1 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CarryLetterRunLedgerImported | True | True | The previous finite carry-letter and run decomposition is imported. | none for import |
| FiniteCarrySwitchGraphLedger | True | True | All adjacent letter pairs are encoded as raw and signed directed switch edges. | none for current finite switch graph ledger |
| LowBranchOrDeterministicSwitchingLaw | False | False | The observed graph has large branching: raw max outdegree 54 and signed max outdegree 100. | a new analytic law is required; the graph is not deterministic |
| FiniteSwitchGraphPhaseSaving | False | False | Prove cancellation for paths in the finite switch graph along prime q. | new exponential-sum input or trace/Kloosterman completion required |
| NoLossQPrefixSwitchAtomAggregation | False | False | Aggregate any switch-graph saving across all fixed-m atoms without losing the boundary gain. | requires analytic aggregation discipline |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | the switch graph is not yet a trace-function family over a complete summation box |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | high-branch switch graph data does not by itself create Kloosterman inverse variables |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | switch graph paths remain one-dimensional prime-q words rather than balanced Type-II rectangles |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced Kloosterman input remains candidate only after switch paths are completed into admissible fractions |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | prime existence in short intervals does not estimate carry-letter switch graph phases |

```text
FKMS_trace_bilinear=switch edges are not yet trace functions over complete boxes
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=branching switch graph does not by itself expose inverse Kloosterman variables
Pascadi_composite_Type_II=switch paths remain one-dimensional and do not form balanced composite Type-II packets
Wright_unbalanced_Kloosterman=could apply only after switch paths are converted to admissible unbalanced fractions
Li_short_interval_x_052=prime existence in intervals does not estimate switch-graph reciprocal phases
```

结论：carry-letter word 的相邻切换已经被压成有限有向图。
但 raw/signed 图具有高分支节点，且大强连通块占据主要字母质量；
因此本层没有给出 deterministic switching law，也没有给出相位节省。

## 5. 最新最窄口

```text
FiniteSwitchGraphPathExponentialSumSaving
AND TraceKloostermanCompletionOfHighBranchCarrySwitchGraph
AND NoLossAggregationAcross15439QPrefixSwitchAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
finite_switch_graph_closed=true
deterministic_switching_law_closed=false
low_branch_switch_graph_available=false
finite_switch_graph_phase_saving_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_switch_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
