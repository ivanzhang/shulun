# Prime Matrix Phi-LPF q-prefix carry cycle signature single-P local gap2/gap4 top-two core largest-atom dominant-sign-word step-transition 审计

**状态：** `dominant_sign_word_step_transition_ledger_closed_family_bound_open`
**核验日期：** `2026-05-25`

## 1. 当前对象

```text
input=three m-pair coordinate witnesses of sign word --+-+
operation=split length-5 signed coordinate paths into step atoms and adjacent transition atoms
dominant_shape=15 signed step atoms and 12 adjacent transition atoms with fixed sign-position law
remaining=turn the step-transition grammar into a uniform signed collision bound or a PDEC/SAE certificate
```

## 2. signed step/transition 审计

```text
max_prime=1009
dominant_sign_word_step_transition_ledger_closed=true
target_sign_word=--+-+
coordinate_witness_count=3
coordinate_witness_edge_mass=30
step_atom_count=15
step_atom_mass=150
transition_atom_count=12
transition_atom_mass=120
all_witness_length_equals_5=true
all_step_atom_mass_equals_10=true
all_transition_atom_mass_equals_10=true
all_initial_steps_negative=true
all_terminal_steps_positive=true
sign_word_position_law_closed=true
transition_sign_law_closed=true
negative_step_mass=90
positive_step_mass=60
same_sign_transition_mass=30
sign_switch_transition_mass=90
distinct_signed_step_atom_count=13
repeated_signed_step_atom_count=2
repeated_signed_step_atoms={'g=2,c=2,A=negative': 20, 'g=6,c=7,A=positive': 20}
row_column_unconditional_closed=false
```

signed step atom subledger：

| signed_step_atom | mass | ratio |
| --- | --- | --- |
| g=2,c=2,A=negative | 20 | 0.13333333333333333 |
| g=6,c=7,A=positive | 20 | 0.13333333333333333 |
| g=10,c=10,A=negative | 10 | 0.06666666666666667 |
| g=10,c=8,A=negative | 10 | 0.06666666666666667 |
| g=4,c=3,A=negative | 10 | 0.06666666666666667 |
| g=4,c=5,A=negative | 10 | 0.06666666666666667 |
| g=4,c=6,A=positive | 10 | 0.06666666666666667 |
| g=6,c=5,A=positive | 10 | 0.06666666666666667 |
| g=6,c=6,A=negative | 10 | 0.06666666666666667 |
| g=6,c=6,A=positive | 10 | 0.06666666666666667 |
| g=8,c=10,A=negative | 10 | 0.06666666666666667 |
| g=8,c=6,A=negative | 10 | 0.06666666666666667 |
| g=8,c=7,A=positive | 10 | 0.06666666666666667 |

sign-position and transition-sign laws：

| sign_position | mass | ratio |
| --- | --- | --- |
| step1:- | 30 | 0.2 |
| step2:- | 30 | 0.2 |
| step3:+ | 30 | 0.2 |
| step4:- | 30 | 0.2 |
| step5:+ | 30 | 0.2 |

| sign_pair | mass | ratio |
| --- | --- | --- |
| -+ | 60 | 0.5 |
| +- | 30 | 0.25 |
| -- | 30 | 0.25 |

carry/gap delta transition subledgers：

| carry_delta | mass | ratio |
| --- | --- | --- |
| -4 | 30 | 0.25 |
| -2 | 20 | 0.16666666666666666 |
| 3 | 20 | 0.16666666666666666 |
| -1 | 10 | 0.08333333333333333 |
| 0 | 10 | 0.08333333333333333 |
| 2 | 10 | 0.08333333333333333 |
| 4 | 10 | 0.08333333333333333 |
| 5 | 10 | 0.08333333333333333 |

| gap_delta | mass | ratio |
| --- | --- | --- |
| -2 | 30 | 0.25 |
| -4 | 30 | 0.25 |
| 2 | 30 | 0.25 |
| 4 | 20 | 0.16666666666666666 |
| 0 | 10 | 0.08333333333333333 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| DominantSignWordCoordinatePartitionImported | True | True | The full --+-+ m-pair coordinate partition is imported. | none for import |
| SignedStepAtomLedger | True | True | The three paths are split into 15 signed step atoms. | none for the finite step ledger |
| AdjacentTransitionAtomLedger | True | True | The three paths are split into 12 adjacent transition atoms. | none for the finite transition ledger |
| StepTransitionUniformFamilyBound | False | False | Control the step-transition grammar as a uniform family. | finite grammar audit gives exact atoms but no global theorem |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear input; still not a local gap2-wing or gap4-tail equality theorem |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | useful after Kloosterman completion; does not prove fixed packet route-superclass collision control |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | average inverse-fraction input; not pointwise for one gap2/gap4 carrier |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | prime-gap existence input; not a signed Phi-LPF route-superclass theorem |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence input; does not estimate local adjacent-pair template equality |

```text
trace_or_kloosterman_inputs=step atoms still need aggregation into a nonlocal trace or bilinear sum before these theorems apply
prime_gap_inputs=the gap labels are local path grammar data, not prime-gap existence estimates
short_interval_prime_inputs=theta=0.52 remains above the endpoint half-scale and does not estimate this fixed grammar
```

结论：dominant sign word `--+-+` 的三条坐标路径已拆成 15 个 signed step atoms 与 12 个 adjacent transition atoms。
该账本仍是有限结构结果，尚未给出全局 signed collision bound。

## 5. 最新最窄口

```text
DominantSignWordStepTransitionUniformFamilyBound(--+-+ grammar)
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
dominant_sign_word_step_transition_ledger_closed=true
dominant_sign_word_step_transition_family_bound_proved=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
