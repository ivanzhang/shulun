# Prime Matrix Phi-LPF boundary endpoint-flux q-prefix carry dynamics 审计

**状态：** `qprefix_phase_atoms_have_successor_carry_dynamics_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=15439 fixed-m phase atoms and 162076 adjacent prime-q transitions
identity=D_next=D+m*(q_next-q)-P*(k_next-k), carry=floor((D+m*(q_next-q))/P)
dominant_shape=variable prime-gap carry words and mixed A(q) sawtooth motion
remaining=phase saving for prime-gap-driven moving numerator or completion to an external trace/Kloosterman family
```

## 2. successor carry 有限审计

```text
max_prime=1009
previous_phase_normal_form_atom_count_total=15439
previous_phase_normal_form_edge_count_total=177515
carry_dynamics_atom_count_total=15439
multiq_atom_count=14277
singleton_q_atom_count=1162
expected_successor_transition_count_total=162076
successor_transition_count_total=162076
carry_formula_mismatch_count=0
D_successor_mismatch_count=0
A_successor_mismatch_count=0
q_gap_nonpositive_count=0
carry_nonpositive_count=0
A_step_zero_count=148
successor_carry_identity_verified=true
q_gap_min/median/max=2/6.0/20
carry_delta_k_min/median/max=1/6.0/33
D_step_min/median/max=-984/2.0/994
A_step_min/median/max=-871/6.0/877
distinct_q_gap_count=9
distinct_carry_delta_k_count=33
successor_carry_dynamics_closed=true
moving_numerator_phase_saving_closed=false
```

atom carry word 分桶：

| carry_word_class | atom_count |
| --- | --- |
| constant_carry_word | 960 |
| singleton_q_no_transition | 1162 |
| variable_carry_word | 13317 |

atom prime-gap word 分桶：

| prime_gap_word_class | atom_count |
| --- | --- |
| constant_prime_gap_word | 962 |
| singleton_q_no_transition | 1162 |
| variable_prime_gap_word | 13315 |

atom A-motion 分桶：

| A_motion_class | atom_count |
| --- | --- |
| A_constant | 2 |
| A_mixed_sawtooth | 12895 |
| A_strict_decreasing | 598 |
| A_strict_increasing | 782 |
| singleton_q_no_transition | 1162 |

strip 分桶：

| strip | atom_count | transition_count |
| --- | --- | --- |
| lower_wing | 2466 | 26678 |
| right_tail | 6962 | 79789 |
| upper_wing | 6011 | 55609 |

D-step sign 分桶：

| D_step_sign | count |
| --- | --- |
| negative | 80672 |
| positive | 81404 |

A-step sign 分桶：

| A_step_sign | count |
| --- | --- |
| negative | 79136 |
| positive | 82792 |
| zero | 148 |

carry delta-k 分桶：

| carry_delta_k | count |
| --- | --- |
| 1 | 4512 |
| 2 | 14606 |
| 3 | 17066 |
| 4 | 18208 |
| 5 | 12620 |
| 6 | 18307 |
| 7 | 14469 |
| 8 | 9405 |
| 9 | 12783 |
| 10 | 9330 |
| 11 | 6138 |
| 12 | 4935 |
| 13 | 3813 |
| 14 | 3572 |
| 15 | 2970 |
| 16 | 1886 |
| 17 | 1657 |
| 18 | 1376 |
| 19 | 973 |
| 20 | 882 |
| 21 | 647 |
| 22 | 411 |
| 23 | 204 |
| 24 | 171 |
| 25 | 188 |
| 26 | 223 |
| 27 | 202 |
| 28 | 144 |
| 29 | 140 |
| 30 | 108 |
| 31 | 74 |
| 32 | 43 |
| 33 | 13 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| QPrefixPhaseNormalFormImported | True | True | The fixed-m A(q)/q normal form is inherited. | none for import |
| SuccessorCarryIdentity | True | True | Every adjacent prime-q transition obeys the exact carry formula. | none for deterministic successor dynamics |
| PrimeGapDrivenCarryWordLedger | True | True | Each atom has an explicit q-gap word, carry word, and A-step word. | none for finite carry ledger |
| ConstantStepRotationReduction | False | False | The dominant mass is not a constant-step fixed-denominator rotation. | variable q-gaps and carry words must be estimated |
| MovingNumeratorPrimeQPrefixPhaseSaving | False | False | Prove cancellation for the prime-gap-driven A(q)/q orbit. | new carry-word exponential sum or completed trace/Kloosterman input required |
| NoLossQPrefixPhaseAtomAggregation | False | False | Aggregate carry-orbit estimates across all fixed-m atoms without losing the boundary gain. | requires analytic aggregation discipline |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | carry dynamics must still be completed to a trace family before trace bilinear estimates apply |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | prime-gap carry words do not by themselves create an inverse-fraction Kloosterman variable |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | successor carry words are one-dimensional along q and not direct composite Type-II boxes |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced Kloosterman input remains a candidate only after the carry word is completed into an admissible family |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short-interval prime existence does not estimate prime-gap-driven reciprocal carry phases |

```text
FKMS_trace_bilinear=successor dynamics is explicit but not a completed trace family
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=carry words do not directly supply inverse Kloosterman variables
Pascadi_composite_Type_II=successor orbits remain one-dimensional and boundary-weighted
Wright_unbalanced_Kloosterman=could become relevant only after carry words are completed into an admissible unbalanced family
Li_short_interval_x_052=prime existence does not estimate carry-driven reciprocal phases
```

结论：moving numerator 的相邻 q 演化已经压成 prime-gap carry word。
该层关闭确定性 successor 动力学；但 dominant atoms 具有 variable carry word
和 mixed sawtooth A-motion，因此仍未得到相位节省或 completed trace/Kloosterman 输入。

## 5. 最新最窄口

```text
PrimeGapDrivenCarryWordExponentialSumSaving
AND CompletionOfSuccessorCarryDynamicsToTraceOrKloostermanFamily
AND NoLossAggregationAcross15439QPrefixCarryAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
successor_carry_dynamics_closed=true
constant_step_rotation_reduction_available=false
moving_numerator_phase_saving_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_phase_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
