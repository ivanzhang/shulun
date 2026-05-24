# Prime Matrix Phi-LPF boundary endpoint-flux q-prefix atom 审计

**状态：** `boundary_endpoint_flux_split_into_qprefix_line_atoms_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=5106 boundary endpoint-flux packets carrying 177515 edges
identity=each endpoint-flux packet is a disjoint union of {m} x contiguous prime-q prefix line atoms
remaining=phase saving on fixed-m prime-q prefix reciprocal orbits and no-loss aggregation
```

## 2. q-prefix line atom 有限审计

```text
max_prime=1009
shell_step_packet_count_total=5106
previous_boundary_endpoint_flux_packet_count=5106
previous_boundary_endpoint_flux_edge_count=177515
qprefix_line_atom_count_total=15439
qprefix_line_atom_edge_count_total=177515
expanded_edge_set_size=177515
duplicate_atom_edge_count=0
qprefix_line_atom_identity_verified=true
bad_qprefix_atom_count=0
packet_support_count_min=1
packet_support_count_median=3.0
packet_support_count_max=12
q_prefix_count_min=1
q_prefix_count_median=11.0
q_prefix_count_max=37
qprefix_line_atomization_closed=true
qprefix_line_atom_phase_saving_closed=false
```

atom strip 分桶：

| strip | atom_count | edge_weight_sum |
| --- | --- | --- |
| lower_wing | 2466 | 29144 |
| right_tail | 6962 | 86751 |
| upper_wing | 6011 | 61620 |

atom endpoint-flux class 分桶：

| endpoint_flux_class | atom_count | edge_weight_sum |
| --- | --- | --- |
| lower_wing_single_contiguous_endpoint_shell | 2466 | 29144 |
| right_tail_left_collar_only_no_P_puncture | 633 | 8652 |
| right_tail_left_collar_only_with_P_puncture | 54 | 776 |
| right_tail_right_collar_only_no_P_puncture | 1237 | 12879 |
| right_tail_right_collar_only_with_P_puncture | 42 | 708 |
| right_tail_terminal_full_interval_no_P_puncture | 131 | 2487 |
| right_tail_terminal_full_interval_with_P_puncture | 267 | 4864 |
| right_tail_two_sided_left_and_right_collars_no_P_puncture | 4398 | 52957 |
| right_tail_two_sided_left_and_right_collars_with_P_puncture | 200 | 3428 |
| upper_wing_single_contiguous_endpoint_shell | 6011 | 61620 |

atom q-prefix 分桶：

| q_prefix_bin | atom_count | edge_weight_sum |
| --- | --- | --- |
| 17<=q<=37 | 4052 | 93081 |
| 2<=q<=4 | 2525 | 7452 |
| 5<=q<=8 | 3220 | 20877 |
| 9<=q<=16 | 4480 | 54943 |
| q=1 | 1162 | 1162 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| BoundaryEndpointFluxImported | True | True | The unified endpoint-flux packet ledger is inherited. | none for support import |
| QPrefixContiguousPrimeIntervalIdentity | True | True | Every atom uses a contiguous prime-q prefix interval. | none for finite q-prefix support |
| EndpointFluxQPrefixLineAtomization | True | True | All endpoint-flux edges expand disjointly into fixed-m q-prefix line atoms. | none for finite atom support |
| QPrefixLineAtomPhaseSaving | False | False | Prove cancellation on fixed-m prime-q prefix reciprocal orbits. | new completed trace or reciprocal-orbit estimate required |
| NoLossQPrefixAtomAggregation | False | False | Aggregate q-prefix atom phase savings without losing the endpoint-flux gain. | requires analytic aggregation discipline |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | q-prefix line atoms are trace-shaped only after the moving denominator is completed |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | fixed-m q-prefix atoms still require a completed Kloosterman variable in q |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | one-dimensional q-prefix atoms are not direct composite Type-II rectangles |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced Kloosterman fractions are closest after the q-prefix atom phase is normalized |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval prime existence does not control q-prefix reciprocal orbit phases |

```text
FKMS_trace_bilinear=q-prefix atoms are explicit but still need completed moving-denominator trace normalization
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=arbitrary-modulus estimates do not start until the atom denominator is a valid Kloosterman variable
Pascadi_composite_Type_II=line atoms are one-dimensional q-prefix objects, not Type-II rectangles
Wright_unbalanced_Kloosterman=unbalanced estimates become plausible only after q-prefix reciprocal-orbit normalization
Li_short_interval_x_052=prime existence in short intervals does not supply reciprocal q-prefix phase cancellation
```

结论：boundary endpoint-flux 已无重叠展开为固定 m 的 q-prefix line atoms。
该层关闭的是支撑原子化，不关闭 q-prefix reciprocal orbit 的相位节省。

## 5. 最新最窄口

```text
QPrefixLineAtomReciprocalOrbitPhaseSaving
AND MovingPrimeQDenominatorCompletedTraceFamilyOnFixedMAtoms
AND NoLossAggregationAcross15439QPrefixLineAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
qprefix_line_atomization_closed=true
qprefix_line_atom_phase_saving_closed=false
moving_q_denominator_completed_trace_closed=false
no_loss_qprefix_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
