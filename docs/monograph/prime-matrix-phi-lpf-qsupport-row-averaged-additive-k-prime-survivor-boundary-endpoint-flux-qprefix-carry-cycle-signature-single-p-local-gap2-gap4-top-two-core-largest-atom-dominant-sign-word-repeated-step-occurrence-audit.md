# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom dominant-sign-word repeated-step occurrence 审计

**状态：** `dominant_sign_word_repeated_step_occurrence_ledger_closed_family_bound_open`
**核验日期：** `2026-05-25`

## 1. 当前对象

```text
input=two repeated signed step atoms inside the --+-+ step-transition ledger
operation=split repeated atoms into occurrence positions and touching adjacent transitions
dominant_shape=4 repeated-step occurrences and 5 touching transitions, with 6 repeated-endpoint incidences
remaining=turn this finite collision carrier into a uniform signed collision bound or PDEC/SAE certificate
```

## 2. repeated-step occurrence 审计

```text
max_prime=1009
dominant_sign_word_repeated_step_occurrence_ledger_closed=true
target_sign_word=--+-+
repeated_signed_step_atom_count=2
repeated_signed_step_atoms={'g=2,c=2,A=negative': 20, 'g=6,c=7,A=positive': 20}
repeated_step_occurrence_count=4
repeated_step_occurrence_mass=40
endpoint_role_law_closed=true
touching_transition_count=5
touching_transition_mass=50
touching_transition_repeated_endpoint_incidence_count=6
touching_transition_repeated_endpoint_incidence_mass=60
row_column_unconditional_closed=false
```

repeated atom summary：

| repeated_signed_step_atom | occurrence_count | occurrence_mass | initial_occurrence_count | internal_occurrence_count | terminal_occurrence_count | incoming_transition_count | outgoing_transition_count | touching_transition_incidence_count | P_support | m_pair_support |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g=2,c=2,A=negative | 2 | 20 | 1 | 1 | 0 | 1 | 2 | 3 | [607, 739] | ['[757, 761]', '[769, 773]'] |
| g=6,c=7,A=positive | 2 | 20 | 0 | 1 | 1 | 2 | 1 | 3 | [607, 739] | ['[757, 761]', '[769, 773]'] |

occurrence position rows：

| P | m_pair | endpoint_orientation | step | position_class | signed_step_signature | occurrence_mass | witness_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 607 | [769, 773] | above_P | 1 | initial | g=2,c=2,A=negative | 10 | P607_packet1887_q7_mpair_769_773 |
| 607 | [769, 773] | above_P | 3 | internal | g=6,c=7,A=positive | 10 | P607_packet1887_q7_mpair_769_773 |
| 739 | [757, 761] | above_P | 4 | internal | g=2,c=2,A=negative | 10 | P739_packet2842_q28_mpair_757_761 |
| 739 | [757, 761] | above_P | 5 | terminal | g=6,c=7,A=positive | 10 | P739_packet2842_q28_mpair_757_761 |

touching transition rows：

| P | m_pair | from_step | to_step | transition_signature | touch_side | touched_repeated_atoms | sign_pair | touching_transition_mass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 607 | [769, 773] | 1 | 2 | g=2,c=2,A=negative -> g=4,c=5,A=negative | from | ['g=2,c=2,A=negative'] | -- | 10 |
| 607 | [769, 773] | 2 | 3 | g=4,c=5,A=negative -> g=6,c=7,A=positive | to | ['g=6,c=7,A=positive'] | -+ | 10 |
| 607 | [769, 773] | 3 | 4 | g=6,c=7,A=positive -> g=8,c=10,A=negative | from | ['g=6,c=7,A=positive'] | +- | 10 |
| 739 | [757, 761] | 3 | 4 | g=6,c=6,A=positive -> g=2,c=2,A=negative | to | ['g=2,c=2,A=negative'] | +- | 10 |
| 739 | [757, 761] | 4 | 5 | g=2,c=2,A=negative -> g=6,c=7,A=positive | both | ['g=2,c=2,A=negative', 'g=6,c=7,A=positive'] | -+ | 10 |

position/touch side summaries：

| position_class | mass | ratio |
| --- | --- | --- |
| internal | 20 | 0.5 |
| initial | 10 | 0.25 |
| terminal | 10 | 0.25 |

| touch_side | mass | ratio |
| --- | --- | --- |
| from | 20 | 0.4 |
| to | 20 | 0.4 |
| both | 10 | 0.2 |

| sign_pair | mass | ratio |
| --- | --- | --- |
| +- | 20 | 0.4 |
| -+ | 20 | 0.4 |
| -- | 10 | 0.2 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DominantSignWordStepTransitionImported | True | True | The full --+-+ signed step/transition ledger is imported. | none for import |
| RepeatedSignedStepOccurrenceLedger | True | True | The two repeated signed step atoms are split into four exact occurrence positions. | none for the finite occurrence ledger |
| RepeatedStepTouchingTransitionLedger | True | True | All adjacent transitions touching the repeated atoms are listed. | none for the finite touching-transition ledger |
| RepeatedStepUniformFamilyBound | False | False | Control repeated signed step collisions uniformly in the full family. | finite occurrence ledger gives exact witnesses but no global theorem |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=touching-transition rows are still finite local grammar data, not a completed trace/bilinear family
prime_gap_inputs=the endpoint/internal roles are not prime-gap existence estimates
short_interval_prime_inputs=theta=0.52 does not imply a half-scale statement for this repeated-step carrier
```

结论：两个 repeated signed step atoms 已经完全定位到四个 occurrence，并列出五条 touching transition。
该账本仍是有限结构结果，尚未给出全局 uniform family bound。

## 5. 最新最窄口

```text
RepeatedStepUniformFamilyBound(g=2,c=2,A=negative and g=6,c=7,A=positive)
AND DominantSignWordStepTransitionUniformFamilyBound(--+-+ grammar outside repeated atoms)
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
dominant_sign_word_repeated_step_occurrence_ledger_closed=true
dominant_sign_word_repeated_step_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
