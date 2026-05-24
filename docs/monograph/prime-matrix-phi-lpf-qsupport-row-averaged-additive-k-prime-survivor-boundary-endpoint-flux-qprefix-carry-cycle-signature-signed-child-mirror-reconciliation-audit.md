# Prime Matrix Phi-LPF q-prefix carry cycle signature signed-child mirror reconciliation 审计

**状态：** `signed_child_mirror_pairing_ledger_closed_reconciliation_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=signed children of each raw cycle-signature base
operation=A-step sign mirror positive<->negative pairing and edge-mass imbalance audit
dominant_shape=mirror pairing leaves a large imbalance rather than closing raw-base signed-child reconciliation
remaining=signed mirror-imbalance phase saving, thin support summation, residual endpoints, and trace/Kloosterman completion
```

## 2. signed-child mirror 审计

```text
max_prime=1009
signed_child_mirror_reconciliation_ledger_closed=true
atom_count_total=15439
switch_atom_count=13355
non_switch_atom_count=2084
adjacent_letter_pair_count_inside_atoms=147799
signed_cycle_packet_count=36330
signed_cycle_edge_mass=107677
signed_cycle_signature_count=8691
raw_base_signed_refinement_count=5359
raw_base_with_multiple_signed_children_count=1823
raw_base_multi_child_signed_edge_ratio=0.7569583105027071
mirror_balanced_edge_mass=31334
mirror_balanced_edge_ratio=0.2909999349907594
mirror_imbalance_edge_mass=76343
mirror_imbalance_edge_ratio=0.7090000650092406
missing_mirror_edge_ratio=0.5848974247053689
raw_base_exact_mirror_balance_count=25
raw_base_exact_mirror_balance_ratio=0.0046650494495241645
raw_base_mirror_imbalance_ratio_min/median/max=0.0/1.0/1.0
mirror_pairing_enough_for_reconciliation_closed=false
row_column_unconditional_closed=false
```

signed A-class edge mass：

| A_class | edge_mass | edge_ratio |
| --- | --- | --- |
| all_negative | 9169 | 0.08515281815057997 |
| all_positive | 9980 | 0.0926846030257158 |
| mixed_positive_negative | 88124 | 0.8184106169376932 |
| mixed_with_zero | 404 | 0.0037519618860109402 |

最高 mirror-imbalance raw bases：

| raw_base_template | signed_child_count | signed_edge_mass | mirror_balanced_edge_mass | mirror_imbalance_edge_mass | mirror_imbalance_ratio | top_child_edge_share | top_signed_child |
| --- | --- | --- | --- | --- | --- | --- | --- |
| g=4,c=4 -> g=8,c=9 | 4 | 378 | 116 | 262 | 0.6931216931216931 | 0.7936507936507936 | g=4,c=4,A=negative -> g=8,c=9,A=positive |
| g=10,c=11 -> g=2,c=2 | 4 | 294 | 36 | 258 | 0.8775510204081632 | 0.7278911564625851 | g=10,c=11,A=positive -> g=2,c=2,A=negative |
| g=10,c=9 -> g=2,c=2 | 4 | 254 | 16 | 238 | 0.937007874015748 | 0.8031496062992126 | g=10,c=9,A=negative -> g=2,c=2,A=positive |
| g=2,c=2 -> g=4,c=2 | 3 | 256 | 20 | 236 | 0.921875 | 0.7890625 | g=2,c=2,A=positive -> g=4,c=2,A=negative |
| g=2,c=4 -> g=4,c=6 | 2 | 236 | 0 | 236 | 1.0 | 0.8813559322033898 | g=2,c=4,A=positive -> g=4,c=6,A=negative |
| g=2,c=2 -> g=4,c=5 | 5 | 408 | 192 | 216 | 0.5294117647058824 | 0.7205882352941176 | g=2,c=2,A=negative -> g=4,c=5,A=positive |
| g=4,c=3 -> g=6,c=4 -> g=8,c=6 | 5 | 213 | 6 | 207 | 0.971830985915493 | 0.3380281690140845 | g=4,c=3,A=positive -> g=6,c=4,A=negative -> g=8,c=6,A=positive |
| g=4,c=4 -> g=8,c=7 | 4 | 330 | 124 | 206 | 0.6242424242424243 | 0.7696969696969697 | g=4,c=4,A=positive -> g=8,c=7,A=negative |
| g=10,c=16 -> g=2,c=3 | 4 | 298 | 92 | 206 | 0.6912751677852349 | 0.7114093959731543 | g=10,c=16,A=positive -> g=2,c=3,A=negative |
| g=2,c=2 -> g=6,c=6 -> g=6,c=5 | 4 | 201 | 0 | 201 | 1.0 | 0.7014925373134329 | g=2,c=2,A=positive -> g=6,c=6,A=positive -> g=6,c=5,A=negative |
| g=10,c=14 -> g=2,c=3 | 3 | 256 | 64 | 192 | 0.75 | 0.6640625 | g=10,c=14,A=negative -> g=2,c=3,A=positive |
| g=4,c=4 -> g=8,c=7 -> g=6,c=6 | 4 | 189 | 0 | 189 | 1.0 | 0.5555555555555556 | g=4,c=4,A=positive -> g=8,c=7,A=negative -> g=6,c=6,A=positive |
| g=4,c=4 -> g=8,c=9 -> g=6,c=7 | 5 | 198 | 12 | 186 | 0.9393939393939394 | 0.4696969696969697 | g=4,c=4,A=negative -> g=8,c=9,A=positive -> g=6,c=7,A=positive |
| g=4,c=6 -> g=6,c=8 -> g=8,c=12 | 3 | 177 | 0 | 177 | 1.0 | 0.6610169491525424 | g=4,c=6,A=positive -> g=6,c=8,A=negative -> g=8,c=12,A=negative |
| g=4,c=4 -> g=8,c=9 -> g=6,c=6 | 4 | 174 | 0 | 174 | 1.0 | 0.6206896551724138 | g=4,c=4,A=negative -> g=8,c=9,A=positive -> g=6,c=6,A=negative |
| g=10,c=11 -> g=8,c=8 | 5 | 222 | 52 | 170 | 0.7657657657657657 | 0.8468468468468469 | g=10,c=11,A=positive -> g=8,c=8,A=negative |
| g=10,c=9 -> g=8,c=8 | 4 | 230 | 76 | 154 | 0.6695652173913044 | 0.8 | g=10,c=9,A=negative -> g=8,c=8,A=positive |
| g=2,c=2 -> g=6,c=7 | 4 | 336 | 188 | 148 | 0.44047619047619047 | 0.5952380952380952 | g=2,c=2,A=negative -> g=6,c=7,A=positive |
| g=10,c=10 -> g=14,c=15 -> g=4,c=4 -> g=2,c=2 | 4 | 148 | 0 | 148 | 1.0 | 0.5675675675675675 | g=10,c=10,A=negative -> g=14,c=15,A=positive -> g=4,c=4,A=negative -> g=2,c=2,A=negative |
| g=12,c=17 -> g=8,c=12 -> g=4,c=6 | 5 | 153 | 6 | 147 | 0.9607843137254902 | 0.37254901960784315 | g=12,c=17,A=negative -> g=8,c=12,A=positive -> g=4,c=6,A=positive |

最高 mirror-pair 残差：

| raw_base_template | signed_child | mirror_child | child_edge_mass | mirror_edge_mass | balanced_edge_mass | imbalance_edge_mass |
| --- | --- | --- | --- | --- | --- | --- |
| g=4,c=4 -> g=8,c=9 | g=4,c=4,A=negative -> g=8,c=9,A=positive | g=4,c=4,A=positive -> g=8,c=9,A=negative | 300 | 44 | 88 | 256 |
| g=2,c=2 -> g=4,c=5 | g=2,c=2,A=negative -> g=4,c=5,A=positive | g=2,c=2,A=positive -> g=4,c=5,A=negative | 294 | 80 | 160 | 214 |
| g=2,c=4 -> g=4,c=6 | g=2,c=4,A=positive -> g=4,c=6,A=negative | g=2,c=4,A=negative -> g=4,c=6,A=positive | 208 | 0 | 0 | 208 |
| g=2,c=2 -> g=4,c=2 | g=2,c=2,A=positive -> g=4,c=2,A=negative | g=2,c=2,A=negative -> g=4,c=2,A=positive | 202 | 0 | 0 | 202 |
| g=10,c=11 -> g=2,c=2 | g=10,c=11,A=positive -> g=2,c=2,A=negative | g=10,c=11,A=negative -> g=2,c=2,A=positive | 214 | 14 | 28 | 200 |
| g=10,c=9 -> g=2,c=2 | g=10,c=9,A=negative -> g=2,c=2,A=positive | g=10,c=9,A=positive -> g=2,c=2,A=negative | 204 | 6 | 12 | 198 |
| g=4,c=4 -> g=8,c=7 | g=4,c=4,A=negative -> g=8,c=7,A=positive | g=4,c=4,A=positive -> g=8,c=7,A=negative | 58 | 254 | 116 | 196 |
| g=10,c=16 -> g=2,c=3 | g=10,c=16,A=positive -> g=2,c=3,A=negative | g=10,c=16,A=negative -> g=2,c=3,A=positive | 212 | 44 | 88 | 168 |
| g=10,c=11 -> g=8,c=8 | g=10,c=11,A=positive -> g=8,c=8,A=negative | g=10,c=11,A=negative -> g=8,c=8,A=positive | 188 | 22 | 44 | 166 |
| g=10,c=9 -> g=8,c=8 | g=10,c=9,A=negative -> g=8,c=8,A=positive | g=10,c=9,A=positive -> g=8,c=8,A=negative | 184 | 30 | 60 | 154 |
| g=2,c=2 -> g=6,c=6 -> g=6,c=5 | g=2,c=2,A=positive -> g=6,c=6,A=positive -> g=6,c=5,A=negative | g=2,c=2,A=negative -> g=6,c=6,A=negative -> g=6,c=5,A=positive | 141 | 0 | 0 | 141 |
| g=10,c=14 -> g=2,c=3 | g=10,c=14,A=positive -> g=2,c=3,A=negative | g=10,c=14,A=negative -> g=2,c=3,A=positive | 32 | 170 | 64 | 138 |
| g=2,c=2 -> g=6,c=7 | g=2,c=2,A=positive -> g=6,c=7,A=negative | g=2,c=2,A=negative -> g=6,c=7,A=positive | 66 | 200 | 132 | 134 |
| g=14,c=15 -> g=4,c=4 | g=14,c=15,A=positive -> g=4,c=4,A=negative | g=14,c=15,A=negative -> g=4,c=4,A=positive | 134 | 0 | 0 | 134 |
| g=2,c=2 -> g=6,c=5 | g=2,c=2,A=positive -> g=6,c=5,A=negative | g=2,c=2,A=negative -> g=6,c=5,A=positive | 200 | 72 | 144 | 128 |
| g=2,c=2 -> g=6,c=4 -> g=6,c=4 | g=2,c=2,A=positive -> g=6,c=4,A=positive -> g=6,c=4,A=negative | g=2,c=2,A=negative -> g=6,c=4,A=negative -> g=6,c=4,A=positive | 6 | 132 | 12 | 126 |
| g=10,c=11 -> g=6,c=7 | g=10,c=11,A=negative -> g=6,c=7,A=positive | g=10,c=11,A=positive -> g=6,c=7,A=negative | 162 | 38 | 76 | 124 |
| g=4,c=2 -> g=8,c=6 | g=4,c=2,A=negative -> g=8,c=6,A=positive | g=4,c=2,A=positive -> g=8,c=6,A=negative | 124 | 0 | 0 | 124 |
| g=4,c=6 -> g=8,c=14 | g=4,c=6,A=negative -> g=8,c=14,A=positive | g=4,c=6,A=positive -> g=8,c=14,A=negative | 124 | 0 | 0 | 124 |
| g=4,c=7 -> g=8,c=12 | g=4,c=7,A=positive -> g=8,c=12,A=negative | g=4,c=7,A=negative -> g=8,c=12,A=positive | 122 | 0 | 0 | 122 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CycleSignatureWeightCarrierImported | True | True | The previous weight-carrier ledger is imported. | none for import |
| SignedChildMirrorPairingLedger | True | True | Every signed child is compared with its A-step sign mirror inside the same raw base. | none for current deterministic mirror ledger |
| MirrorPairingEnoughForReconciliation | False | False | Use sign-mirror pairing alone to reconcile raw-base signed-child weights. | fails at the exposed mirror imbalance mass |
| MirrorImbalancePhaseSaving | False | False | Prove cancellation for the mirror-imbalance residue. | requires analytic phase input on the imbalanced signed-child carriers |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | could matter only after mirror-imbalance carriers are realized as trace-function sums |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | does not by itself provide signed-child mirror balance |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | requires Type-II boxes rather than signed-child mirror packets |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | requires admissible fraction families after mirror imbalance is isolated |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | prime existence does not balance signed-child mirror masses |

```text
FKMS_trace_bilinear=not directly applicable before mirror-imbalance carriers become trace sums
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=does not supply signed-child mirror balance
Pascadi_composite_Type_II=not matched to the signed-child mirror ledger
Wright_unbalanced_Kloosterman=candidate only after mirror residues become admissible fractions
Li_short_interval_x_052=does not estimate mirror-pair imbalance
```

结论：同 raw-base 内的 A-step 符号镜像配对已成账，但镜像配平本身
不足以关闭 raw-base/signed-child reconciliation。剩余对象被压到
mirror-imbalance signed-child carriers。

## 5. 最新最窄口

```text
SignedChildMirrorImbalancePhaseSaving
AND NonMirrorSignedChildCarrierControl
AND ThinPSupportCarrierSummationWithoutLoss
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND TraceKloostermanCompletionOfMirrorImbalanceAndResidualPackets
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
signed_child_mirror_reconciliation_ledger_closed=true
mirror_pairing_enough_for_reconciliation_closed=false
raw_base_to_signed_child_weight_reconciliation_closed=false
signed_child_mirror_imbalance_phase_saving_closed=false
thin_P_support_carrier_summation_closed=false
residual_endpoint_path_summation_closed=false
completion_to_external_trace_or_kloosterman_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
