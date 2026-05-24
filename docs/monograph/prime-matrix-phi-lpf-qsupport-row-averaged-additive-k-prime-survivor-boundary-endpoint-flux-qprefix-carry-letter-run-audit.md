# Prime Matrix Phi-LPF q-prefix carry letter/run 审计

**状态：** `qprefix_carry_words_have_finite_letter_run_decomposition_phase_saving_open`
**核验日期：** `2026-05-24`

## 1. 当前对象

```text
input=15439 fixed-m carry atoms and 162076 adjacent prime-q transitions
raw_letter=L=(q_next-q, k_next-k)
signed_letter=L_plus=(q_next-q, k_next-k, sign(A_next-A))
dominant_shape=finite alphabet with highly fragmented one-step runs
remaining=exponential-sum saving for finite carry-letter words or conversion to an external trace/Kloosterman family
```

## 2. 有限字母与 run 审计

```text
max_prime=1009
carry_letter_atom_count_total=15439
multiq_atom_count=14277
singleton_q_atom_count=1162
successor_transition_count_total=162076
raw_letter_run_length_sum=162076
signed_letter_run_length_sum=162076
letter_run_decomposition_closed=true
distinct_q_gap_count=9
distinct_carry_delta_k_count=33
distinct_A_step_sign_count=3
raw_carry_letter_alphabet_count/capacity=117/297
signed_carry_letter_alphabet_count/capacity=256/891
raw_constant/variable_letter_atom_count=946/13331
signed_constant/variable_letter_atom_count=934/13343
raw_run_count_total=156474
signed_run_count_total=158716
raw_run_length_min/median/max=1/1.0/3
signed_run_length_min/median/max=1/1.0/3
raw_switch_count/ratio=142197/0.962097172511316
signed_switch_count/ratio=144439/0.9772664226415605
finite_letter_exponential_sum_saving_closed=false
row_column_unconditional_closed=false
```

最高频 raw carry letters：

| raw_letter | count |
| --- | --- |
| g=2,c=2 | 12515 |
| g=2,c=3 | 9894 |
| g=4,c=4 | 9877 |
| g=6,c=6 | 9045 |
| g=6,c=9 | 7217 |
| g=4,c=6 | 6897 |
| g=4,c=3 | 6133 |
| g=6,c=7 | 6043 |
| g=6,c=4 | 6024 |
| g=6,c=5 | 5667 |
| g=4,c=5 | 5121 |
| g=6,c=10 | 4549 |
| g=2,c=1 | 4512 |
| g=4,c=7 | 4225 |
| g=6,c=8 | 3626 |
| g=8,c=8 | 3420 |
| g=10,c=10 | 2990 |
| g=8,c=9 | 2690 |
| g=10,c=11 | 2376 |
| g=8,c=7 | 2307 |

最高频 signed carry letters：

| signed_letter | count |
| --- | --- |
| g=2,c=2,A=negative | 6280 |
| g=2,c=2,A=positive | 6235 |
| g=4,c=4,A=negative | 5091 |
| g=2,c=3,A=positive | 5018 |
| g=2,c=3,A=negative | 4876 |
| g=4,c=4,A=positive | 4786 |
| g=6,c=6,A=negative | 4593 |
| g=6,c=6,A=positive | 4452 |
| g=6,c=9,A=positive | 3703 |
| g=6,c=9,A=negative | 3514 |
| g=4,c=6,A=negative | 3504 |
| g=4,c=6,A=positive | 3393 |
| g=6,c=7,A=positive | 3299 |
| g=4,c=3,A=positive | 3274 |
| g=6,c=4,A=negative | 3061 |
| g=6,c=4,A=positive | 2963 |
| g=6,c=5,A=negative | 2903 |
| g=4,c=3,A=negative | 2859 |
| g=4,c=5,A=positive | 2761 |
| g=6,c=5,A=positive | 2749 |

raw run length 分布：

| run_length | run_count |
| --- | --- |
| 1 | 151027 |
| 2 | 5292 |
| 3 | 155 |

signed run length 分布：

| run_length | run_count |
| --- | --- |
| 1 | 155434 |
| 2 | 3204 |
| 3 | 78 |

每 atom 的 raw distinct letter 数：

| distinct_raw_letters | atom_count |
| --- | --- |
| 1 | 946 |
| 2 | 1092 |
| 3 | 1164 |
| 4 | 1410 |
| 5 | 1607 |
| 6 | 1612 |
| 7 | 1602 |
| 8 | 1651 |
| 9 | 1334 |
| 10 | 1023 |
| 11 | 527 |
| 12 | 247 |
| 13 | 59 |
| 14 | 3 |

每 atom 的 signed distinct letter 数：

| distinct_signed_letters | atom_count |
| --- | --- |
| 1 | 934 |
| 2 | 979 |
| 3 | 1036 |
| 4 | 1138 |
| 5 | 1301 |
| 6 | 1228 |
| 7 | 1154 |
| 8 | 1157 |
| 9 | 1081 |
| 10 | 1045 |
| 11 | 935 |
| 12 | 733 |
| 13 | 575 |
| 14 | 430 |
| 15 | 286 |
| 16 | 154 |
| 17 | 83 |
| 18 | 21 |
| 19 | 4 |
| 20 | 2 |
| 21 | 1 |

strip 分桶：

| strip | atom_count | transition_count |
| --- | --- | --- |
| lower_wing | 2466 | 26678 |
| right_tail | 6962 | 79789 |
| upper_wing | 6011 | 55609 |

max run 样本：

```text
max_raw_run_sample={'P': 307, 'strip': 'right_tail', 'm': 311, 'raw_letter': 'g=6,c=6', 'run_length': 3, 'transition_count': 15}
max_signed_run_sample={'P': 307, 'strip': 'right_tail', 'm': 311, 'signed_letter': 'g=6,c=6,A=negative', 'run_length': 3, 'transition_count': 15}
```

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| SuccessorCarryDynamicsImported | True | True | The previous exact carry identity is imported. | none for import |
| FiniteCarryLetterAlphabet | True | True | All transitions are encoded by raw and signed finite carry letters. | none for current finite alphabet ledger |
| CarryRunLengthLedger | True | True | The run lengths reconstruct all adjacent prime-q transitions without loss. | none for current run ledger |
| LongConstantLetterBlockReduction | False | False | The observed maximum raw/signed run length is only 3. | there is no long constant-letter block to exploit as a constant rotation |
| FiniteCarryLetterWordExponentialSumSaving | False | False | Prove cancellation for the finite-letter carry words along prime q. | new exponential-sum input or trace/Kloosterman completion required |
| NoLossQPrefixLetterAtomAggregation | False | False | Aggregate any letter-word saving across all fixed-m atoms without losing the boundary gain. | requires analytic aggregation discipline |

## 4. 外部 theorem 影响

| key | url | role |
| --- | --- | --- |
| Fouvry_Kowalski_Michel_Sawin_2025_trace_bilinear | https://arxiv.org/abs/2511.09459 | finite carry letters still need completion to trace functions before trace bilinear estimates apply |
| Milicevic_Qin_Wu_2025_arbitrary_modulus_kloosterman | https://arxiv.org/abs/2511.07550 | the letter word is not yet an inverse-fraction Kloosterman family modulo q |
| Pascadi_2025_nonabelian_composite_type_II | https://arxiv.org/abs/2511.08445 | run words are one-dimensional prime-q strings, not balanced composite Type-II boxes |
| Wright_2026_unbalanced_kloosterman_fractions | https://arxiv.org/abs/2604.25177 | unbalanced Kloosterman input remains candidate only after the letter word is converted to an admissible reciprocal family |
| Li_2023_short_interval_primes_x_052 | https://arxiv.org/abs/2308.04458 | short interval prime existence does not estimate finite carry-letter reciprocal phases |

```text
FKMS_trace_bilinear=finite letters are not yet trace functions over a completed family
Milicevic_Qin_Wu_arbitrary_modulus_Kloosterman=the word does not yet expose an inverse variable with a usable modulus family
Pascadi_composite_Type_II=run decomposition remains one-dimensional and short-shell weighted
Wright_unbalanced_Kloosterman=candidate only after a completed unbalanced reciprocal family is constructed
Li_short_interval_x_052=existence of primes in intervals does not control carry-letter phase cancellation
```

结论：successor carry word 已经进一步压成有限 raw/signed carry letter
和 run-length ledger；但是 run 的中位长度为 1、最大长度仅为 3，
主质量仍是频繁切换的有限字母词，而不是可直接求和的长常步长旋转。

## 5. 最新最窄口

```text
FiniteCarryLetterWordExponentialSumSaving
AND PrimeGapCarrySwitchingLawOrTraceKloostermanCompletion
AND NoLossAggregationAcross15439QPrefixCarryLetterAtoms
AND PrimeQSupportSetReciprocalPhaseSavingBeyondParity
```

状态边界：

```text
finite_carry_letter_alphabet_closed=true
long_constant_letter_block_route_available=false
finite_letter_exponential_sum_saving_closed=false
completion_to_external_trace_or_kloosterman_closed=false
no_loss_qprefix_letter_atom_aggregation_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
