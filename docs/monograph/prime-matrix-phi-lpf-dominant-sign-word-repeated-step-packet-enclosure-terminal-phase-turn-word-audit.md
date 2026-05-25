# Prime Matrix Phi-LPF repeated-step terminal phase-turn word 审计

**状态：** `terminal_phase_turn_word_closed_phase_saving_open`
**核验日期：** `2026-05-25`

## 1. 当前对象

```text
input=terminal phase carry-orbit audit
identity=A(q)=lambda(q)*q-D(q), lambda(q) in {1,2}; phase direction is audited by sign(A(q')/q'-A(q)/q)
```

## 2. phase-turn 有限审计

```text
previous_terminal_phase_carry_orbit_closed=true
terminal_phase_turn_word_closed=true
terminal_phase_turn_atom_count_total=7
terminal_phase_turn_transition_count_total=126
terminal_phase_turn_run_count_total=59
selected_terminal_transition_count=66
selected_terminal_positive_transition_count=17
selected_terminal_negative_transition_count=49
selected_terminal_phase_run_count=35
selected_terminal_phase_run_max_length=6
extra_transition_count=60
extra_positive_transition_count=27
extra_negative_transition_count=33
extra_phase_run_count=24
extra_phase_run_max_length=8
phase_direction_Awrap_mismatch_count=0
lift_identity_mismatch_count=0
zero_phase_delta_count=0
phase_turn_word_phase_saving_proved=false
row_column_unconditional_closed=false
```

atom phase-turn rows：

| side | packet | role | m | transitions | positive | negative | runs | max_run | lift1_edges | lift2_edges | turn_words |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| left | 2842 | extra_shell | 719 | 27 | 21 | 6 | 10 | 6 | 24 | 4 | 13 |
| left | 2842 | extra_shell | 751 | 27 | 4 | 23 | 9 | 8 | 22 | 6 | 13 |
| left | 2842 | selected_terminal | 757 | 27 | 6 | 21 | 11 | 6 | 24 | 4 | 12 |
| left | 2842 | selected_terminal | 761 | 27 | 7 | 20 | 14 | 5 | 24 | 4 | 12 |
| right | 1887 | extra_shell | 479 | 6 | 2 | 4 | 5 | 2 | 6 | 1 | 5 |
| right | 1887 | selected_terminal | 769 | 6 | 2 | 4 | 5 | 2 | 5 | 2 | 5 |
| right | 1887 | selected_terminal | 773 | 6 | 2 | 4 | 5 | 2 | 5 | 2 | 5 |

role direction rows：

| role | direction | transition_count |
| --- | --- | --- |
| extra_shell | positive | 27 |
| extra_shell | negative | 33 |
| extra_shell | zero | 0 |
| selected_terminal | positive | 17 |
| selected_terminal | negative | 49 |
| selected_terminal | zero | 0 |

role lift edge rows：

| role | lift_class | edge_count |
| --- | --- | --- |
| extra_shell | lift1 | 52 |
| extra_shell | lift2 | 11 |
| extra_shell | other | 0 |
| selected_terminal | lift1 | 58 |
| selected_terminal | lift2 | 12 |
| selected_terminal | other | 0 |

role lift transition rows：

| role | lift_transition | transition_count |
| --- | --- | --- |
| extra_shell | L1to1_negative | 24 |
| extra_shell | L1to1_positive | 19 |
| extra_shell | L1to2_negative | 1 |
| extra_shell | L1to2_positive | 5 |
| extra_shell | L2to1_negative | 5 |
| extra_shell | L2to1_positive | 2 |
| extra_shell | L2to2_negative | 3 |
| extra_shell | L2to2_positive | 1 |
| selected_terminal | L1to1_negative | 43 |
| selected_terminal | L1to1_positive | 4 |
| selected_terminal | L1to2_positive | 7 |
| selected_terminal | L2to1_negative | 1 |
| selected_terminal | L2to1_positive | 6 |
| selected_terminal | L2to2_negative | 5 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TerminalPhaseCarryOrbitImported | True | True | The deterministic carry orbit is imported. | none for import |
| TwoLiftNumeratorRepresentation | True | True | Every edge satisfies A=lambda*q-D with lambda in {1,2}. | none for finite lift ledger |
| PhaseDirectionAwrapEquivalence | True | True | Every phase decrease is exactly an A-wrap and every no-wrap is a phase increase. | none for finite phase-turn ledger |
| SelectedTerminalPhaseRunLedger | True | True | The selected terminal word has 66 transitions, 35 monotone runs, and max run length 6. | none for finite selected run ledger |
| PhaseTurnWordPhaseSaving | False | False | Prove cancellation for the selected A-wrap phase-turn word. | requires analytic phase saving or a PDEC/SAE cap |
| ExtraPhaseTurnRunAbsorption | False | False | Absorb the extra phase-turn runs without losing selected gain. | requires summable absorption or explicit dominance certificate |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear estimates require a completed averaging family, not a finite phase-turn word |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | arbitrary-modulus Kloosterman bounds need an admissible summation variable |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | the phase-turn word is not a composite Type-II rectangle |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced fraction bounds may help only after a trilinear or averaged fraction family is built |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence does not estimate signed A-wrap phase turns |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | bounded prime gaps do not control the signed phase-turn run imbalance |

```text
FKMS_trace_bilinear=the phase-turn word is finite and not a completed trace/bilinear family
Milicevic_Qin_Wu_Kloosterman=no admissible Kloosterman summation variable is created by the run ledger
Pascadi_Type_II=the selected object is a one-dimensional word, not a Type-II box
Wright_unbalanced_Kloosterman=could matter only after promoting runs to an averaged trilinear fraction family
Li_short_interval_x_052=prime existence does not estimate signed A-wrap imbalance
Maynard_small_gaps=bounded gaps do not control the phase-turn run signs
```

结论：carry orbit 已被进一步压成 two-lift phase-turn word。有限账本中
`A(q)/q` 的相位下降恰好等于 `A_wrap`，相位上升恰好等于 no-wrap。
这仍不是相位节省定理，也不是 row/column Phi-LPF 无条件闭合。

## 5. 最新最窄口

```text
SelectedTerminalAwrapPhaseTurnWordSaving(66 transitions: 49 negative/A-wrap, 17 positive/no-wrap; 35 runs; max run 6)
AND ExtraPhaseTurnRunAbsorption(60 transitions: 33 negative, 27 positive; 24 runs)
AND SelectedTerminalPrimeGapCarryWordPhaseSavingOutsidePhaseTurnLedger
AND RepeatedStepPacketEnclosureTerminalLineAtomUniformBoundOutsidePhaseNormalForm
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
terminal_phase_turn_word_closed=true
selected_terminal_phase_turn_word_closed=true
phase_turn_word_phase_saving_proved=false
extra_phase_turn_run_absorption_proved=false
summable_family_created=false
trace_or_kloosterman_completion_ready=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
