# Prime Matrix Phi-LPF matching graph closure 审计

**状态：** `reciprocal_graph_is_matching_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQBooleanSubsetReciprocalPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | ReciprocalResidualGraphIsPartialMatching | true | reverse-fibre parity sharpening after boolean q-projection; no new prime theorem required |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | still needs Buchstab transfer and denominator audit |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a closable reciprocal graph fibre gate |

boolean q-projection 后，本轮继续选择行/列 Phi-LPF 的反向纤维子门。该门只用 fixed-m thin window 与 prime parity，可完全闭合；它不证明后续相位和抵消。

## 2. 部分匹配定理

```text
q_side=Previous gate gives each q at most one residual cofactor m.
m_reverse_window=For fixed residual m>P/2, possible q lie in an integer interval of length P/m<2.
prime_parity=If two integer q candidates are present, they are consecutive; since q>P/2>2 and q is prime, at most one can be prime.
matching_conclusion=The residual (q,m) graph has maximum degree 1 on both sides; it is a partial matching.
phase_reduction=The finite sawtooth object is a sum over matched edges q<->m, equivalently over a prime subset Q_{P,k} with a unique residual cofactor map m(q).
not_enough=A matching graph still does not imply cancellation for sum_{q in Q_{P,k}} e(hkP/q); completion/dispersion remains open.
```

关键点是：固定 `m` 后，满足 `kP<q*m<(k+1)P` 的整数 `q` 落在长度 `<2` 的窗口内；若有两个候选，它们连续。由于 `q>P/2>2` 且 `q` 为素数，候选 prime `q` 至多一个。结合上一层每个 `q` 至多一个 residual `m`，整个 `(q,m)` 图是部分匹配。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_edges_R30=299977
max_q_degree_seen=1
max_m_degree_seen=1
max_reverse_q_window_size_seen=2
total_two_point_reverse_windows_on_edges=36191
all_rows_matching_graph=true
violation_count=0
```

有限审计只验证实现和账本一致性；全局闭合来自上面的反向窗口长度与 prime parity 论证。

代表行：

| P | k | edge_count_R30 | distinct_q_vertices | distinct_m_vertices | max_q_degree | max_m_degree | max_reverse_q_window_size | matching_graph | sample_edges |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 1 | 1 | 1 | 1 | 1 | 1 | true | q=71,m=143 |
| 257 | 256 | 3 | 3 | 3 | 1 | 1 | 1 | true | q=137,m=481; q=151,m=437; q=193,m=341 |
| 971 | 936 | 23 | 23 | 23 | 1 | 1 | 1 | true | q=491,m=1853; q=503,m=1807; q=523,m=1739; q=541,m=1681; q=557,m=1633 |
| 1009 | 1008 | 9 | 9 | 9 | 1 | 1 | 1 | true | q=563,m=1807; q=577,m=1763; q=617,m=1649; q=647,m=1573; q=743,m=1369 |

## 4. 外部前沿匹配

| source | useful_part | accepted_for_this_gate | closes_phase_saving | reason_not_direct |
| --- | --- | --- | --- | --- |
| Classical parity and twin-prime exception observation | two consecutive integers above 2 cannot both be prime | true | false | turns the graph into a matching only; no exponential-sum cancellation follows |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | arbitrary-modulus bilinear Kloosterman power savings for later completed matching sums | false | false | requires inverse/Kloosterman completion of the matching graph |
| Pascadi 2025 arXiv:2511.08445 | composite-modulus Type-II Kloosterman amplification | false | false | not a pointwise fixed-row real reciprocal matching theorem |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | Kloosterman sums over square-free and smooth parameters | false | false | useful after finite-field completion, not direct for the real reciprocal matching graph |

外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把 reciprocal graph 从双向 thin graph 缩成部分匹配。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ReversePrimeQFiberBooleanForResidualM | true | true | For each residual cofactor m, at most one prime q in (P/2,P) can satisfy kP<qm<(k+1)P. | none |
| ReciprocalResidualGraphIsPartialMatching | true | true | Combining q-side and m-side booleanity, the residual graph has degree at most 1 on both sides. | none |
| PrimeQMatchingSubsetReciprocalPhaseSaving | false | false | For \|h\|<=polylog(P), prove cancellation for the matched prime subset sum over Q_{P,k}. | matching subset reciprocal phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the same-row matching graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQMatchingSubsetReciprocalPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
reciprocal_residual_graph_matching_closed=true
weighted_reciprocal_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
