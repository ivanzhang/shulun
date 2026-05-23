# Prime Matrix Phi-LPF unique odd candidate LPF partition closure 审计

**状态：** `unique_odd_candidate_lpf_partition_closed_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQUniqueOddCandidateLPFSubsetPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | UniqueOddCandidateFiveWayLPFPartition | true | the existing omega(q) map has an immediate disjoint LPF partition and isolates the wheel-30 survivor prime/composite split |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | not a one-line closure after the omega(q) projection |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a Phi-LPF LPF-partition gate |

本轮继续选择行/列 Phi-LPF，因为上一层已经把对象压成 `omega_{P,k}(q)`。最快可闭合的真子门不是再改写旧等价命题，而是把 LPF 子集谓词拆成互斥的五个点态状态。

## 2. LPF 五分划正规形

```text
five_cells=no_odd_candidate, prime, small_lpf_3, small_lpf_5, residual_lpf_ge_7_composite
pointwise_identity=For each prime q in (P/2,P), exactly one of the five cells holds.
candidate_identity=1_{omega exists}=1_{prime}+1_{LPF=3}+1_{LPF=5}+1_{residual_lpf_ge_7_composite}.
wheel30_identity=1_{gcd(omega,30)=1}=1_{prime}+1_{residual_lpf_ge_7_composite} on the candidate support.
residual_identity=Residual edges are exactly omega exists, gcd(omega,30)=1, and omega composite.
phase_decomposition=S_candidate(h)=S_prime(h)+S_LPF3(h)+S_LPF5(h)+S_residual(h), with phase e(-hD(q)/q).
not_enough=The remaining hard point is the signed/oscillatory separation of composite 30-wheel survivors from prime survivors.
```

证明要点很短：上一层给出唯一奇候选；奇数的 `LPF<7` 只能是 `3` 或 `5`。因此 `LPF>=7` 合成候选正是 `gcd(omega,30)=1` 的合成幸存者。这个闭合删除了小素因子噪声，但没有解决 wheel-30 幸存者内部的素数/合数分离。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_prime_q_instances=3874554
total_odd_candidate_instances=1266932
actual_total_edges_R30=299977
predicted_total_edges_R30=299977
reason_totals={'no_odd_candidate': 2607622, 'prime': 374384, 'small_lpf_3': 423339, 'small_lpf_5': 169232, 'residual_lpf_ge_7_composite': 299977}
wheel30_survivor_candidate_total=674361
prime_candidate_total=374384
residual_lpf_ge_7_composite_total=299977
forced_composite_by_30wheel_total=592571
branch_totals_on_candidates={'both': 390129, 'upper': 436002, 'lower': 440801}
window_width_totals={'-1': 2214518, '0': 783233, '1': 876803}
max_odd_candidates_per_q=1
five_way_partition_total=3874554
candidate_partition_total=1266932
unique_odd_candidate_per_q=true
five_way_partition_exhaustive=true
candidate_partition_exhaustive=true
wheel30_survivor_identity_verified=true
forced_composite_identity_verified=true
residual_cell_equals_actual_edges=true
all_candidate_displacements_in_1_to_Pminus1=true
bad_candidate_total=0
bad_candidate_displacement_total=0
bad_small_lpf_partition_total=0
bad_five_way_partition_total=0
bad_candidate_partition_total=0
bad_wheel30_split_total=0
missing_edge_total=0
extra_edge_total=0
```

有限审计只验证实现和账本一致性；全局闭合来自唯一奇候选与 `LPF<7` 的小素数穷尽。

代表行：

| P | k | q_count | odd_candidate_count | wheel30_survivor_candidate_count | forced_composite_by_30wheel_count | actual_edge_count_R30 | reason_counter | sample_residual_edges |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 10 | 7 | 5 | 2 | 1 | no_odd_candidate:3, prime:4, residual_lpf_ge_7_composite:1, small_lpf_3:2 | q=71,omega=143,branch=both,d=53,lpf=11 |
| 257 | 256 | 23 | 16 | 9 | 7 | 3 | no_odd_candidate:7, prime:6, residual_lpf_ge_7_composite:3, small_lpf_3:4, small_lpf_5:3 | q=137,omega=481,branch=lower,d=105,lpf=13; q=151,omega=437,branch=upper,d=195,lpf=19; q=193,omega=341,branch=lower,d=21,lpf=11 |
| 971 | 936 | 71 | 49 | 35 | 14 | 23 | no_odd_candidate:22, prime:12, residual_lpf_ge_7_composite:23, small_lpf_3:6, small_lpf_5:8 | q=491,omega=1853,branch=upper,d=967,lpf=17; q=503,omega=1807,branch=lower,d=65,lpf=13; q=523,omega=1739,branch=upper,d=641,lpf=37; q=541,omega=1681,branch=upper,d=565,lpf=41; q=557,omega=1633,branch=upper,d=725,lpf=23 |
| 1009 | 1008 | 72 | 54 | 28 | 26 | 9 | no_odd_candidate:18, prime:19, residual_lpf_ge_7_composite:9, small_lpf_3:20, small_lpf_5:6 | q=563,omega=1807,branch=lower,d=269,lpf=13; q=577,omega=1763,branch=lower,d=179,lpf=41; q=617,omega=1649,branch=lower,d=361,lpf=17; q=647,omega=1573,branch=upper,d=659,lpf=11; q=743,omega=1369,branch=lower,d=95,lpf=37 |

## 4. 外部前沿匹配

| source | source_url | verified_status | useful_part | closes_this_gate | reason_not_direct |
| --- | --- | --- | --- | --- | --- |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | https://arxiv.org/abs/2511.07550 | submitted 2025-11-10; bilinear Kloosterman sums modulo arbitrary q | candidate input after a completion from omega(q) phases to bilinear Kloosterman sums | false | does not supply the missing prime/composite split inside the wheel-30 survivor q-subset |
| Pascadi 2025 arXiv:2511.08445 | https://arxiv.org/abs/2511.08445 | submitted 2025-11-11; Type-II Kloosterman sums with composite moduli | candidate external Type-II source after a valid completion identity | false | the present q-moduli are prime and the LPF partition is a fixed-row subset problem |
| Shao--Shparlinski--Wijaya 2024 arXiv:2411.12113 | https://arxiv.org/abs/2411.12113 | submitted 2024-11-18; Kloosterman sums over square-free and smooth parameters | possible comparison source for arithmetic-function-twisted Kloosterman sums | false | requires a prior finite-field/completion bridge from omega(q) to their parameter family |
| Dong--Robles--Zeindler 2026 arXiv:2601.00292 | https://arxiv.org/abs/2601.00292 | withdrawn on arXiv v2 after a missing factor was reported | near-miss diagnostic only | false | withdrawn papers cannot be used as valid external input |

这些外部 Kloosterman/Type-II 结果仍是后续 completion 的候选工具；本层的五分划闭合是内部确定性门，不把任何外部前沿误用为 Phi-LPF 闭合。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| UniqueOddCandidateFiveWayLPFPartition | true | true | Each prime q falls in exactly one of no-candidate, prime, LPF=3, LPF=5, or residual composite LPF>=7. | none |
| LPFResidualAsWheel30CompositeSurvivor | true | true | The residual cell is exactly the composite part of the unique odd candidate with gcd(omega,30)=1. | none |
| CandidatePhaseFourTermExactDecomposition | true | true | The candidate phase sum splits exactly into prime, LPF=3, LPF=5, and residual terms. | none |
| PrimeQUniqueOddCandidateWheel30CompositeSurvivorPhaseSaving | false | false | Prove cancellation or positivity control for the composite wheel-30 survivor q-subset. | wheel-30 survivor prime/composite separation theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the omega(q) survivor phase to an external DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQUniqueOddCandidateWheel30CompositeSurvivorPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
unique_odd_candidate_lpf_partition_closed=true
wheel30_survivor_prime_composite_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
