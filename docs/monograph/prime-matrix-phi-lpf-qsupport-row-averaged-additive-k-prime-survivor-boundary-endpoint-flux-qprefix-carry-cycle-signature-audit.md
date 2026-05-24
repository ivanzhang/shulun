# Prime Matrix Phi-LPF q-prefix carry cycle signature 审计

**状态：** `qprefix_cycle_core_has_finite_signature_ledger_weighted_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=loop-erased raw/signed cycle packets from 13355 switch atoms
operation=canonical rotation signature plus length/load/sign shape bucketing
dominant_shape=many short recurrent templates with no single template carrying enough mass for trivial cancellation
remaining=weighted phase saving by cycle signature, endpoint residual summation, and trace/Kloosterman completion
```

## 2. cycle-signature 审计

```text
max_prime=1009
cycle_signature_atom_count_total=15439
switch_atom_count=13355
non_switch_atom_count=2084
adjacent_letter_pair_count_inside_atoms=147799
cycle_signature_decomposition_closed=true
raw_cycle_packet_count=45178
raw_cycle_edge_mass=117733
raw_cycle_signature_count=3546
raw_cycle_shape_count=2718
raw_cycle_length_min/median/max=1/2.0/10
raw_self_loop_cycle_count=5602
raw_template_max_edge_ratio=0.0161212234462725
raw_template_top20_edge_ratio=0.13926426745262585
raw_template_top100_edge_ratio=0.34888264123058105
signed_cycle_packet_count=36330
signed_cycle_edge_mass=107677
signed_cycle_signature_count=8691
signed_cycle_shape_count=5905
signed_cycle_length_min/median/max=1/2.0/14
signed_self_loop_cycle_count=3360
signed_A_sign_variable_cycle_count=26038
signed_template_max_edge_ratio=0.006909553572257771
signed_template_top20_edge_ratio=0.06297538007188165
signed_template_top100_edge_ratio=0.18002916128792593
cycle_signature_weighted_phase_saving_closed=false
row_column_unconditional_closed=false
```

strip cycle edge mass：

| strip | raw_cycle_edge_mass | signed_cycle_edge_mass |
| --- | --- | --- |
| lower_wing | 19267 | 17498 |
| right_tail | 59321 | 54281 |
| upper_wing | 39145 | 35898 |

最高质量 raw cycle templates：

| template | cycle_count | edge_mass | shape |
| --- | --- | --- | --- |
| g=2,c=2 -> g=4,c=4 | 949 | 1898 | len=2,sum_g=6,sum_c=6,g=[2,4],c=[2,4] |
| g=6,c=6 | 1439 | 1439 | len=1,sum_g=6,sum_c=6,g=[6,6],c=[6,6] |
| g=2,c=3 -> g=4,c=6 | 482 | 964 | len=2,sum_g=6,sum_c=9,g=[2,4],c=[3,6] |
| g=6,c=9 | 920 | 920 | len=1,sum_g=6,sum_c=9,g=[6,6],c=[9,9] |
| g=6,c=7 | 893 | 893 | len=1,sum_g=6,sum_c=7,g=[6,6],c=[7,7] |
| g=4,c=6 -> g=6,c=9 | 444 | 888 | len=2,sum_g=10,sum_c=15,g=[4,6],c=[6,9] |
| g=6,c=4 | 863 | 863 | len=1,sum_g=6,sum_c=4,g=[6,6],c=[4,4] |
| g=4,c=3 -> g=6,c=4 | 386 | 772 | len=2,sum_g=10,sum_c=7,g=[4,6],c=[3,4] |
| g=4,c=4 -> g=6,c=6 | 373 | 746 | len=2,sum_g=10,sum_c=10,g=[4,6],c=[4,6] |
| g=4,c=4 -> g=8,c=8 | 365 | 730 | len=2,sum_g=12,sum_c=12,g=[4,8],c=[4,8] |
| g=2,c=3 -> g=6,c=9 | 363 | 726 | len=2,sum_g=8,sum_c=12,g=[2,6],c=[3,9] |
| g=2,c=1 -> g=4,c=3 | 354 | 708 | len=2,sum_g=6,sum_c=4,g=[2,4],c=[1,3] |
| g=2,c=2 -> g=6,c=6 | 351 | 702 | len=2,sum_g=8,sum_c=8,g=[2,6],c=[2,6] |
| g=2,c=2 -> g=4,c=5 | 329 | 658 | len=2,sum_g=6,sum_c=7,g=[2,4],c=[2,5] |
| g=6,c=5 | 655 | 655 | len=1,sum_g=6,sum_c=5,g=[6,6],c=[5,5] |
| g=2,c=3 -> g=4,c=7 | 296 | 592 | len=2,sum_g=6,sum_c=10,g=[2,4],c=[3,7] |
| g=4,c=6 -> g=8,c=12 | 295 | 590 | len=2,sum_g=12,sum_c=18,g=[4,8],c=[6,12] |
| g=4,c=4 -> g=8,c=8 -> g=6,c=6 | 196 | 588 | len=3,sum_g=18,sum_c=18,g=[4,8],c=[4,8] |
| g=2,c=1 -> g=6,c=4 | 269 | 538 | len=2,sum_g=8,sum_c=5,g=[2,6],c=[1,4] |
| g=10,c=7 -> g=6,c=4 | 263 | 526 | len=2,sum_g=16,sum_c=11,g=[6,10],c=[4,7] |

最高质量 signed cycle templates：

| template | cycle_count | edge_mass | shape |
| --- | --- | --- | --- |
| g=2,c=2,A=negative -> g=4,c=4,A=negative | 372 | 744 | len=2,sum_g=6,sum_c=6,g=[2,4],c=[2,4],A(-,0,+)=(2,0,0) |
| g=2,c=2,A=positive -> g=4,c=4,A=positive | 334 | 668 | len=2,sum_g=6,sum_c=6,g=[2,4],c=[2,4],A(-,0,+)=(0,0,2) |
| g=6,c=6,A=negative | 545 | 545 | len=1,sum_g=6,sum_c=6,g=[6,6],c=[6,6],A(-,0,+)=(1,0,0) |
| g=6,c=6,A=positive | 464 | 464 | len=1,sum_g=6,sum_c=6,g=[6,6],c=[6,6],A(-,0,+)=(0,0,1) |
| g=6,c=7,A=positive | 334 | 334 | len=1,sum_g=6,sum_c=7,g=[6,6],c=[7,7],A(-,0,+)=(0,0,1) |
| g=4,c=4,A=negative -> g=8,c=9,A=positive | 150 | 300 | len=2,sum_g=12,sum_c=13,g=[4,8],c=[4,9],A(-,0,+)=(1,0,1) |
| g=2,c=2,A=negative -> g=4,c=5,A=positive | 147 | 294 | len=2,sum_g=6,sum_c=7,g=[2,4],c=[2,5],A(-,0,+)=(1,0,1) |
| g=2,c=3,A=positive -> g=4,c=6,A=positive | 144 | 288 | len=2,sum_g=6,sum_c=9,g=[2,4],c=[3,6],A(-,0,+)=(0,0,2) |
| g=4,c=3,A=positive -> g=6,c=4,A=negative | 143 | 286 | len=2,sum_g=10,sum_c=7,g=[4,6],c=[3,4],A(-,0,+)=(1,0,1) |
| g=4,c=4,A=negative -> g=8,c=8,A=negative | 143 | 286 | len=2,sum_g=12,sum_c=12,g=[4,8],c=[4,8],A(-,0,+)=(2,0,0) |
| g=6,c=4,A=negative | 275 | 275 | len=1,sum_g=6,sum_c=4,g=[6,6],c=[4,4],A(-,0,+)=(1,0,0) |
| g=4,c=6,A=positive -> g=6,c=9,A=positive | 132 | 264 | len=2,sum_g=10,sum_c=15,g=[4,6],c=[6,9],A(-,0,+)=(0,0,2) |
| g=6,c=5,A=negative | 263 | 263 | len=1,sum_g=6,sum_c=5,g=[6,6],c=[5,5],A(-,0,+)=(1,0,0) |
| g=4,c=4,A=positive -> g=6,c=6,A=positive | 131 | 262 | len=2,sum_g=10,sum_c=10,g=[4,6],c=[4,6],A(-,0,+)=(0,0,2) |
| g=6,c=9,A=positive | 260 | 260 | len=1,sum_g=6,sum_c=9,g=[6,6],c=[9,9],A(-,0,+)=(0,0,1) |
| g=4,c=4,A=negative -> g=6,c=6,A=negative | 130 | 260 | len=2,sum_g=10,sum_c=10,g=[4,6],c=[4,6],A(-,0,+)=(2,0,0) |
| g=4,c=4,A=positive -> g=8,c=7,A=negative | 127 | 254 | len=2,sum_g=12,sum_c=11,g=[4,8],c=[4,7],A(-,0,+)=(1,0,1) |
| g=2,c=1,A=positive -> g=4,c=3,A=negative | 123 | 246 | len=2,sum_g=6,sum_c=4,g=[2,4],c=[1,3],A(-,0,+)=(1,0,1) |
| g=4,c=4,A=positive -> g=8,c=8,A=positive | 123 | 246 | len=2,sum_g=12,sum_c=12,g=[4,8],c=[4,8],A(-,0,+)=(0,0,2) |
| g=2,c=2,A=negative -> g=6,c=6,A=negative | 121 | 242 | len=2,sum_g=8,sum_c=8,g=[2,6],c=[2,6],A(-,0,+)=(2,0,0) |

最高质量 raw length/load shapes：

| shape | cycle_count | edge_mass |
| --- | --- | --- |
| len=2,sum_g=6,sum_c=6,g=[2,4],c=[2,4] | 949 | 1898 |
| len=1,sum_g=6,sum_c=6,g=[6,6],c=[6,6] | 1439 | 1439 |
| len=2,sum_g=6,sum_c=9,g=[2,4],c=[3,6] | 482 | 964 |
| len=1,sum_g=6,sum_c=9,g=[6,6],c=[9,9] | 920 | 920 |
| len=1,sum_g=6,sum_c=7,g=[6,6],c=[7,7] | 893 | 893 |
| len=2,sum_g=10,sum_c=15,g=[4,6],c=[6,9] | 444 | 888 |
| len=1,sum_g=6,sum_c=4,g=[6,6],c=[4,4] | 863 | 863 |
| len=2,sum_g=10,sum_c=7,g=[4,6],c=[3,4] | 386 | 772 |
| len=2,sum_g=10,sum_c=10,g=[4,6],c=[4,6] | 373 | 746 |
| len=2,sum_g=12,sum_c=12,g=[4,8],c=[4,8] | 365 | 730 |
| len=2,sum_g=8,sum_c=12,g=[2,6],c=[3,9] | 363 | 726 |
| len=2,sum_g=6,sum_c=4,g=[2,4],c=[1,3] | 354 | 708 |
| len=2,sum_g=8,sum_c=8,g=[2,6],c=[2,6] | 351 | 702 |
| len=3,sum_g=18,sum_c=18,g=[4,8],c=[4,8] | 231 | 693 |
| len=2,sum_g=6,sum_c=7,g=[2,4],c=[2,5] | 329 | 658 |
| len=1,sum_g=6,sum_c=5,g=[6,6],c=[5,5] | 655 | 655 |
| len=2,sum_g=6,sum_c=10,g=[2,4],c=[3,7] | 296 | 592 |
| len=2,sum_g=12,sum_c=18,g=[4,8],c=[6,12] | 295 | 590 |
| len=2,sum_g=8,sum_c=5,g=[2,6],c=[1,4] | 269 | 538 |
| len=2,sum_g=16,sum_c=11,g=[6,10],c=[4,7] | 263 | 526 |

最高质量 signed length/load/sign shapes：

| shape | cycle_count | edge_mass |
| --- | --- | --- |
| len=2,sum_g=6,sum_c=6,g=[2,4],c=[2,4],A(-,0,+)=(2,0,0) | 372 | 744 |
| len=2,sum_g=6,sum_c=6,g=[2,4],c=[2,4],A(-,0,+)=(0,0,2) | 334 | 668 |
| len=1,sum_g=6,sum_c=6,g=[6,6],c=[6,6],A(-,0,+)=(1,0,0) | 545 | 545 |
| len=2,sum_g=10,sum_c=7,g=[4,6],c=[3,4],A(-,0,+)=(1,0,1) | 239 | 478 |
| len=1,sum_g=6,sum_c=6,g=[6,6],c=[6,6],A(-,0,+)=(0,0,1) | 464 | 464 |
| len=2,sum_g=6,sum_c=4,g=[2,4],c=[1,3],A(-,0,+)=(1,0,1) | 217 | 434 |
| len=2,sum_g=6,sum_c=7,g=[2,4],c=[2,5],A(-,0,+)=(1,0,1) | 187 | 374 |
| len=2,sum_g=8,sum_c=5,g=[2,6],c=[1,4],A(-,0,+)=(1,0,1) | 183 | 366 |
| len=2,sum_g=12,sum_c=8,g=[4,8],c=[3,5],A(-,0,+)=(1,0,1) | 174 | 348 |
| len=2,sum_g=12,sum_c=13,g=[4,8],c=[4,9],A(-,0,+)=(1,0,1) | 172 | 344 |
| len=1,sum_g=6,sum_c=7,g=[6,6],c=[7,7],A(-,0,+)=(0,0,1) | 334 | 334 |
| len=2,sum_g=6,sum_c=10,g=[2,4],c=[3,7],A(-,0,+)=(1,0,1) | 165 | 330 |
| len=2,sum_g=16,sum_c=11,g=[6,10],c=[4,7],A(-,0,+)=(1,0,1) | 160 | 320 |
| len=2,sum_g=12,sum_c=11,g=[4,8],c=[4,7],A(-,0,+)=(1,0,1) | 156 | 312 |
| len=2,sum_g=6,sum_c=9,g=[2,4],c=[3,6],A(-,0,+)=(0,0,2) | 144 | 288 |
| len=3,sum_g=18,sum_c=18,g=[4,8],c=[4,8],A(-,0,+)=(3,0,0) | 96 | 288 |
| len=2,sum_g=12,sum_c=12,g=[4,8],c=[4,8],A(-,0,+)=(2,0,0) | 143 | 286 |
| len=3,sum_g=14,sum_c=13,g=[2,6],c=[2,6],A(-,0,+)=(1,0,2) | 93 | 279 |
| len=3,sum_g=18,sum_c=19,g=[4,8],c=[4,9],A(-,0,+)=(2,0,1) | 92 | 276 |
| len=1,sum_g=6,sum_c=4,g=[6,6],c=[4,4],A(-,0,+)=(1,0,0) | 275 | 275 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LoopErasedCycleFlowImported | True | True | The previous cycle/residual decomposition ledger is imported. | none for import |
| FiniteCycleSignatureLedger | True | True | Every peeled cycle packet is assigned a canonical directed signature and a length/load/sign shape. | none for current deterministic ledger |
| CycleSignatureWeightedPhaseSaving | False | False | Prove cancellation after grouping by cycle signature and analytic weight. | requires new exponential-sum or trace/Kloosterman input on the weighted buckets |
| ResidualEndpointPathSummation | False | False | Control the endpoint residual paths from the previous flow ledger. | requires residual endpoint summation without boundary loss |
| NoLossQPrefixFlowAtomAggregation | False | False | Aggregate signature and residual estimates across all fixed-m atoms. | requires no-loss aggregation discipline over 15439 atoms |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | cycle signatures still need conversion to trace-function weights before bilinear trace estimates apply |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | cycle signatures are not yet inverse-variable Kloosterman families modulo q |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | signature buckets remain path templates rather than balanced composite Type-II boxes |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | candidate only after signatures are completed to admissible unbalanced fractions |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short interval prime existence does not estimate weighted cycle-signature phases |

```text
FKMS_trace_bilinear=finite signatures still need trace-function weights
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=signature buckets are not yet inverse-variable Kloosterman sums
Pascadi_composite_Type_II=signature buckets are path templates rather than composite Type-II boxes
Wright_unbalanced_Kloosterman=candidate only after signature templates become admissible unbalanced fractions
Li_short_interval_x_052=short interval existence gives no cycle-signature phase estimate
```

结论：cycle core 已经进一步拆成 finite directed signatures 与
length/load/sign buckets。该层是结构账本，不是相位相消。

## 5. 最新最窄口

```text
CycleSignatureWeightedPhaseSavingForLoopErasedCarrySwitchCore
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND TraceKloostermanCompletionOfCycleSignatureAndResidualPackets
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
cycle_signature_ledger_closed=true
cycle_signature_weighted_phase_saving_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_flow_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
