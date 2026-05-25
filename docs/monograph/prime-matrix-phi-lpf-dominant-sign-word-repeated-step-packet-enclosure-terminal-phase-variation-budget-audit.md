# Prime Matrix Phi-LPF repeated-step terminal phase variation-budget 审计

**状态：** `terminal_phase_variation_budget_closed_phase_saving_open`
**核验日期：** `2026-05-25`

## 1. 当前对象

```text
input=terminal phase-turn word audit
identity=total variation = positive variation + negative variation; net displacement = positive variation - negative variation
```

## 2. variation budget 有限审计

```text
previous_terminal_phase_turn_word_closed=true
terminal_phase_variation_budget_closed=true
terminal_phase_variation_atom_count_total=7
terminal_phase_variation_transition_count_total=126
terminal_phase_variation_run_count_total=59
selected_terminal_transition_count=66
selected_terminal_phase_run_count=35
selected_terminal_phase_run_max_length=6
selected_terminal_positive_transition_count=17
selected_terminal_negative_transition_count=49
selected_terminal_positive_variation=8.261301579660 (76267896679486572971372265243720452221010528916079563987190173/9231946799674751816365196223540916671310700482028663035764901)
selected_terminal_negative_variation=9.717867552237 (9950454878587640089507829653560449297788227640865029853815370356082608/1023933988099770462723506583596845526698662565115878981568636879953733)
selected_terminal_total_variation=17.979169131897 (18409482351943445293965578391556725137299870717352700685388218401134317/1023933988099770462723506583596845526698662565115878981568636879953733)
selected_terminal_net_phase_displacement=-1.456565972578 (-114539441491/78636631397)
selected_terminal_negative_variation_excess=1.456565972578 (114539441491/78636631397)
extra_transition_count=60
extra_phase_run_count=24
extra_total_variation=14.109301881162 (27768758142307772418840319934041830802744822617132968593977647725/1968117088725958506051611620121066252424277248250429833368124847)
extra_net_phase_displacement=-0.907719323182 (-71379989829/78636631397)
bad_atom_variation_identity_count=0
bad_role_variation_identity_count=0
phase_variation_budget_phase_saving_proved=false
row_column_unconditional_closed=false
```

role variation rows：

| role | transitions | runs | max_run | positive_turns | negative_turns | pos_var | neg_var | net | total_var | dominant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| extra_shell | 60 | 24 | 8 | 27 | 33 | 6.600791278990 (89375667135224732842579294705573709213366931607063726519/13540144409611167359882043326758564235011339562652178391) | 7.508510602172 (14777628027014548257473022291700918764250186339695668956706267102/1968117088725958506051611620121066252424277248250429833368124847) | -0.907719323182 (-71379989829/78636631397) | 14.109301881162 (27768758142307772418840319934041830802744822617132968593977647725/1968117088725958506051611620121066252424277248250429833368124847) | negative |
| selected_terminal | 66 | 35 | 6 | 17 | 49 | 8.261301579660 (76267896679486572971372265243720452221010528916079563987190173/9231946799674751816365196223540916671310700482028663035764901) | 9.717867552237 (9950454878587640089507829653560449297788227640865029853815370356082608/1023933988099770462723506583596845526698662565115878981568636879953733) | -1.456565972578 (-114539441491/78636631397) | 17.979169131897 (18409482351943445293965578391556725137299870717352700685388218401134317/1023933988099770462723506583596845526698662565115878981568636879953733) | negative |

atom variation rows：

| side | packet | role | m | transitions | runs | max_run | pos_var | neg_var | net | total_var | dominant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| left | 2842 | extra_shell | 719 | 27 | 10 | 6 | 3.478975075583 (26739673357718428729175749722/7686077875461867926109901813) | 3.835403775504 (38633570019545065319372724473/10072882095568325988192089437) | -0.356428699921 (-136715/383569) | 7.314378851086 (39859189791196246306766250492791/5449429213702464359611920385417) | negative |
| left | 2842 | extra_shell | 751 | 27 | 9 | 8 | 1.951365193439 (36492733961628521825208/18701129898353446329889) | 2.413832181126 (17314837503337011625539557284/7173173693981533055309193841) | -0.462466987687 (-177388/383569) | 4.365197374565 (31312318976264902113512764636/7173173693981533055309193841) | negative |
| left | 2842 | selected_terminal | 757 | 27 | 11 | 6 | 3.500038894105 (28313452871161762139041768932/8089468068154145262473835811) | 3.538571726529 (10979725142385964208889475560764888/3102869177433817344181826728189459) | -0.038532832424 (-14780/383569) | 7.038610620634 (21839887946724610150799587828243196/3102869177433817344181826728189459) | negative |
| left | 2842 | selected_terminal | 761 | 27 | 14 | 5 | 3.990334664333 (4880392466294506765315837397898390217147/1223053422039360293197855815003646026667) | 3.957581756772 (3693400064380864170521634540136979181962/933246687338919490296248231194601552083) | 0.032752907560 (12563/383569) | 7.947916421105 (5258912969911360856935706921220147347487585/661671901323293918620039995916972500426847) | positive |
| right | 1887 | extra_shell | 479 | 6 | 5 | 2 | 1.170451009968 (49047901777/41905130039) | 1.259274645543 (10818549905018291/8591096424685507) | -0.088823635574 (-18210/205013) | 2.429725655511 (20874007392026392/8591096424685507) | negative |
| right | 1887 | selected_terminal | 769 | 6 | 5 | 2 | 0.430216234104 (18028267235/41905130039) | 1.031256168157 (8859621179184674/8591096424685507) | -0.601039934053 (-123221/205013) | 1.461472402260 (12555650329833729/8591096424685507) | negative |
| right | 1887 | selected_terminal | 773 | 6 | 5 | 2 | 0.340711787118 (14277571745/41905130039) | 1.190457900779 (10227338615121836/8591096424685507) | -0.849746113661 (-174209/205013) | 1.531169687897 (13154426431279521/8591096424685507) | negative |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TerminalPhaseTurnWordImported | True | True | The two-lift phase-turn word is imported. | none for import |
| SignedVariationBudgetIdentity | True | True | Every atom and role satisfies total=positive+negative and net=positive-negative. | none for finite variation ledger |
| SelectedTerminalVariationLedger | True | True | The selected terminal word has exact positive/negative variation and run budgets. | none for finite selected variation ledger |
| VariationBudgetPhaseSaving | False | False | Use the variation budget to prove phase saving. | requires analytic monotone-run cap or PDEC/SAE certificate |
| ExtraVariationBudgetAbsorption | False | False | Absorb extra variation budgets without losing selected gain. | requires dominance or summable absorption |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear_v3 | https://arxiv.org/abs/2511.09459 | trace bilinear estimates need a completed averaging family; this audit only gives finite variation budgets |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | Kloosterman estimates need an admissible summation variable and do not act on the finite run ledger directly |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | the variation ledger is one-dimensional, not a Type-II rectangle |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced Kloosterman fractions remain candidate input only after an averaged fraction family is built |
| Dong_Robles_Zeindler_2026_bilinear_kloosterman_fractions_withdrawn | https://arxiv.org/abs/2601.00292 | withdrawn on arXiv; recorded only as a non-usable boundary, not as an input |
| Li_2023_short_interval_primes_x_052_v8 | https://arxiv.org/abs/2308.04458 | short-interval prime existence does not estimate signed variation imbalance |
| Maynard_2015_small_gaps_prime_gaps | https://doi.org/10.4007/annals.2015.181.1.7 | bounded gaps do not control total variation or run-level cancellation |

```text
FKMS_trace_bilinear=variation budgets are not completed trace/bilinear sums
Milicevic_Qin_Wu_Kloosterman=no Kloosterman summation variable follows from a finite variation ledger
Pascadi_Type_II=no Type-II rectangle is created
Wright_unbalanced_Kloosterman=requires an averaged fraction family absent here
Dong_Robles_Zeindler_2026=withdrawn on arXiv and not used
Li_short_interval_x_052=does not estimate signed variation
Maynard_small_gaps=does not estimate run-level cancellation
```

结论：phase-turn word 已被压成 signed variation budget。selected terminal
部分的负变差严格超过正变差，净位移约为 `-1.456565972578`，总变差
约为 `17.979169131897`。这仍不是 phase saving，也不是无条件闭合。

## 5. 最新最窄口

```text
SelectedTerminalNegativeVariationExcessPhaseSaving(total variation 17.979169131897; net -1.456565972578; 35 runs; max run 6)
AND ExtraNegativeVariationBudgetAbsorption(total variation 14.109301881162; net -0.907719323182; 24 runs)
AND SelectedTerminalAwrapPhaseTurnWordSavingOutsideVariationBudget
AND RepeatedStepPacketEnclosureTerminalLineAtomUniformBoundOutsidePhaseNormalForm
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
terminal_phase_variation_budget_closed=true
selected_terminal_variation_budget_closed=true
phase_variation_budget_phase_saving_proved=false
extra_variation_budget_absorption_proved=false
summable_family_created=false
trace_or_kloosterman_completion_ready=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
