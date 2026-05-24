# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom template-witness 审计

**状态：** `largest_core_atom_template_witness_ledger_closed_family_bound_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=largest route-cycle-switch atom inside the top-two core
operation=split the 70 edge mass into exact template witnesses and sign/q/m subledgers
dominant_shape=7 equal-mass template witnesses; the largest sign word --+-+ carries edge mass 30
remaining=turn these finite witnesses into a uniform family bound or route the family through PDEC/SAE
```

## 2. largest atom template-witness 分类审计

```text
max_prime=1009
largest_atom_template_witness_ledger_closed=true
target_route=gap4_right_tail_two_sided
target_cycle_length=5
target_sign_switch_count=3
previous_largest_atom_edge_mass=70
witness_template_count=7
witness_edge_mass=70
all_witness_edge_mass_equals_10=true
distinct_sign_word_count=5
dominant_sign_word=--+-+
dominant_sign_word_edge_mass=30
dominant_sign_word_ratio=0.42857142857142855
q_prefix_band_q_le_10_edge_mass=30
q_prefix_band_q_le_20_edge_mass=10
q_prefix_band_q_gt_20_edge_mass=30
m_shell_band_m_le_4_edge_mass=30
m_shell_band_m_le_8_edge_mass=40
row_column_unconditional_closed=false
```

sign-word edge mass：

| sign_word | edge_mass | edge_ratio |
| --- | --- | --- |
| --+-+ | 30 | 0.42857142857142855 |
| +-++- | 10 | 0.14285714285714285 |
| +-+-- | 10 | 0.14285714285714285 |
| +--+- | 10 | 0.14285714285714285 |
| -++-+ | 10 | 0.14285714285714285 |

q-prefix bands：

| q_prefix_band | edge_mass | edge_ratio |
| --- | --- | --- |
| q<=10 | 30 | 0.42857142857142855 |
| q>20 | 30 | 0.42857142857142855 |
| q<=20 | 10 | 0.14285714285714285 |

m-shell bands：

| m_shell_band | edge_mass | edge_ratio |
| --- | --- | --- |
| m<=8 | 40 | 0.5714285714285714 |
| m<=4 | 30 | 0.42857142857142855 |

sign/q and sign/m bands：

| sign_word | q_prefix_band | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| --+-+ | q<=10 | 20 | 0.2857142857142857 |
| +-++- | q<=10 | 10 | 0.14285714285714285 |
| +-+-- | q>20 | 10 | 0.14285714285714285 |
| +--+- | q>20 | 10 | 0.14285714285714285 |
| -++-+ | q<=20 | 10 | 0.14285714285714285 |
| --+-+ | q>20 | 10 | 0.14285714285714285 |

| sign_word | m_shell_band | edge_mass | edge_ratio |
| --- | --- | --- | --- |
| --+-+ | m<=4 | 30 | 0.42857142857142855 |
| +-++- | m<=8 | 10 | 0.14285714285714285 |
| +-+-- | m<=8 | 10 | 0.14285714285714285 |
| +--+- | m<=8 | 10 | 0.14285714285714285 |
| -++-+ | m<=8 | 10 | 0.14285714285714285 |

template witnesses：

| P | packet_index | edge_mass | sign_word | sign_balance | m_pair | q_prefix_count | q_prefix_band | m_shell_prime_count | m_shell_band | P_band |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 607 | 1887 | 10 | --+-+ | plus=2,minus=3 | [769, 773] | 7 | q<=10 | 3 | m<=4 | P<=700 |
| 619 | 2017 | 10 | +-++- | plus=3,minus=2 | [739, 743] | 10 | q<=10 | 5 | m<=8 | P<=700 |
| 739 | 2842 | 10 | --+-+ | plus=2,minus=3 | [757, 761] | 28 | q>20 | 4 | m<=4 | P<=850 |
| 773 | 3157 | 10 | +-+-- | plus=2,minus=3 | [823, 827] | 28 | q>20 | 6 | m<=8 | P<=850 |
| 823 | 3485 | 10 | +--+- | plus=2,minus=3 | [859, 863] | 26 | q>20 | 5 | m<=8 | P<=850 |
| 953 | 4601 | 10 | --+-+ | plus=2,minus=3 | [769, 773] | 10 | q<=10 | 4 | m<=4 | P>850 |
| 991 | 4931 | 10 | -++-+ | plus=3,minus=2 | [859, 863] | 16 | q<=20 | 7 | m<=8 | P>850 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TopTwoCoreRouteCycleSwitchLedgerImported | True | True | The 11-atom top-two core ledger is imported. | none for import |
| LargestCoreAtomTemplateWitnessLedger | True | True | The 70-mass largest atom is split into 7 template witnesses. | none for the finite witness ledger |
| DominantSignWordFamilyBound | False | False | Control the dominant --+-+ sign-word family. | finite audit shows mass 30 but no global theorem |
| AllSevenWitnessFamiliesOrPDEC | False | False | Control the seven witness templates uniformly or route them through PDEC/SAE. | requires a uniform lift beyond the finite audit range |
| ResidualCoreAtomBounds | False | False | Control the other 10 route-cycle-switch atoms and the top-two noncore residual. | carried forward from the core atom ledger |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
FKMS_trace_bilinear=nontrivial below Polya-Vinogradov range after sheaf/trace completion; still not a fixed template witness theorem
Milicevic_Qin_Wu_Kloosterman=arbitrary-modulus bilinear Kloosterman power saving after completion; no direct local witness equality
Wright_unbalanced_Kloosterman=useful for unbalanced convolution ranges; does not estimate one fixed endpoint packet
Li_short_intervals=x^0.52 short interval prime existence is above theta=1/2 and does not see the signed template witness
```

结论：最大 core atom 已被压成 7 个等质量模板见证。
该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
DominantLargestAtomSignWordFamilyBound(--+-+)
AND OtherLargestAtomTemplateWitnessFamilyBounds
AND OtherCoreRouteCycleSwitchAtomBounds
AND TopTwoNonCoreSignCycleResidualBound
AND Gap2LowerWingTwinCollisionBound
AND Gap2RightTailTwoSidedTwinResidualCollisionBound
AND Gap4RightTailLeftCollarCousinCollisionBound
AND Gap4UpperWingCousinResidualCollisionBound
AND Gap4LowerWingCousinResidualCollisionBound
AND Gap6SexyAdjacentPairCollisionBound
AND GapGe8AdjacentPairCollisionBound
AND NonAdjacentPrimePairCollisionBound
AND AdjacentPrimeChainCollisionBound
AND MultiPacketDuplicateTransportBound
AND SinglePacketSingleMMultiCycleSuppression
AND RepeatedOccurrenceAggregationOrPDEC
AND CycleOccurrenceProductBoundOrPDEC
AND SinglePSliceEndpointPacketSummationOrPDEC
AND MultiPPureEndpointTraceKloostermanCompletion
AND PureEndpointCarrierPhaseSaving
AND MixedRightTailEndpointRouterNoLoss
AND UnequalMirrorPairResidualPhaseSaving
AND ThinPSupportCarrierSummationWithoutLoss
AND ResidualEndpointPathSummationWithoutBoundaryLoss
AND NoLossAggregationAcross15439QPrefixFlowAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
largest_atom_template_witness_ledger_closed=true
largest_atom_template_family_bound_proved=false
dominant_sign_word_family_bound_proved=false
all_seven_witness_families_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
