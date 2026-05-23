# Prime Matrix Phi-LPF boolean q-projection closure 审计

**状态：** `prime_q_lpf_projection_boolean_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQBoundedLPFCoefficientReciprocalPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | PrimeQBooleanProjectionForLPFShellResidual | true | pure parity plus thin-window sharpening after bounded coefficient extraction; no new prime theorem required |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | still needs Buchstab transfer and denominator audit |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a closable prime-q projection gate |

bounded coefficient 抽取后，本轮继续选择行/列 Phi-LPF 的 prime-q 投影子门。该门只用 thin window 与奇偶性，可完全闭合；它不证明后续相位和抵消。

## 2. 布尔投影定理

```text
window_bound=For q>P/2, I_q(P,k) has at most two integers; if two occur they are consecutive.
residual_parity=If m is composite and LPF(m)>=7, then m is odd and coprime to 2,3,5.
boolean_projection=Therefore b_{P,k}(q)=# {m in I_q(P,k): m composite, LPF(m)>=7} belongs to {0,1}.
phase_reduction=Finite sawtooth modes reduce to sums over a subset Q_{P,k} of primes q in (P/2,P), not to a multi-weighted prime sequence.
not_enough=Boolean coefficients alone do not prove cancellation; a prime-q subset reciprocal phase theorem or a completion theorem is still needed.
```

关键点是：`I_q(P,k)` 最多两个点；若有两个点，它们是连续整数。LPF residual 要求 `LPF(m)>=7` 且 `m` 合成，所以 `m` 不可被 `2` 整除。两个连续整数至多一个奇数，因此每个 prime `q` 对 residual 的贡献最多为一个。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_R30=299977
max_window_size_seen=2
total_two_point_windows=876803
total_two_point_windows_with_residual=208481
max_projected_q_weight_seen=1
all_projected_q_weights_boolean=true
violation_count=0
```

有限审计只验证实现和账本一致性；全局闭合来自上面的两点窗口加奇偶论证。

代表行：

| P | k | q_count | R30 | max_window_size | two_point_windows | two_point_windows_with_residual | max_projected_q_weight | sample_q_residuals |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 10 | 1 | 2 | 4 | 0 | 1 | q=71:m=143 |
| 257 | 256 | 23 | 3 | 2 | 11 | 3 | 1 | q=137:m=481; q=151:m=437; q=193:m=341 |
| 971 | 936 | 71 | 23 | 2 | 27 | 12 | 1 | q=491:m=1853; q=503:m=1807; q=523:m=1739; q=541:m=1681; q=557:m=1633 |
| 1009 | 1008 | 72 | 9 | 2 | 29 | 5 | 1 | q=563:m=1807; q=577:m=1763; q=617:m=1649; q=647:m=1573; q=743:m=1369 |

## 4. 外部前沿匹配

| source | useful_part | accepted_for_this_gate | closes_phase_saving | reason_not_direct |
| --- | --- | --- | --- | --- |
| Classical parity/2-wheel observation | closes the q-projected multiplicity gate because residual m are odd | true | false | removes double weights only; does not estimate exponential sums over the resulting prime subset |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | arbitrary-modulus bilinear Kloosterman power savings for a later completed form | false | false | requires inverse/Kloosterman completion, not merely boolean q-coefficients |
| Pascadi 2025 arXiv:2511.08445 | composite-modulus Type-II Kloosterman amplification | false | false | not a fixed-row real reciprocal phase theorem |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | Kloosterman sums over square-free and smooth parameters | false | false | useful after finite-field completion, not direct for Q_{P,k} prime subsets |

外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把系数从 bounded multiplicity 缩成 prime-q 布尔子集。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PrimeQBooleanProjectionForLPFShellResidual | true | true | The projected LPF residual coefficient b_{P,k}(q) is 0 or 1, not merely bounded by 2. | none |
| NoDoubleMultiplicityPrimeQNoise | true | true | Two-point reciprocal windows cannot contribute two LPF residual cofactors because one of two consecutive integers is even. | none |
| PrimeQBooleanSubsetReciprocalPhaseSaving | false | false | For \|h\|<=polylog(P), prove cancellation for sum_{q in Q_{P,k}} e(hkP/q). | boolean prime-q subset reciprocal phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the same-row boolean subset phase to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQBooleanSubsetReciprocalPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
prime_q_boolean_projection_closed=true
weighted_reciprocal_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
