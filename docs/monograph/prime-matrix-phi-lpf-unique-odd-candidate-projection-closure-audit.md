# Prime Matrix Phi-LPF unique odd candidate projection closure 审计

**状态：** `unique_odd_candidate_projection_closed_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQParitySelectedFloorResidueBranchPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | PrimeQUniqueOddCandidateProjection | true | two-point clipped q-windows have a unique odd candidate; LPF becomes a q-subset predicate |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | still needs Buchstab transfer and denominator audit |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a closable q-candidate projection gate |

parity-selected branch 闭合后，本轮继续选择行/列 Phi-LPF 的 q 单值候选投影门。该门只用 clipped reciprocal window 与奇偶性闭合；它不证明后续相位和抵消。

## 2. unique odd candidate 正规形

```text
candidate=For each prime q in (P/2,P), the clipped window J_q contains at most one odd integer omega_{P,k}(q).
edge_equivalence=(q,m) is a residual edge iff omega exists, m=omega, omega is composite, and LPF(omega)>=7.
phase=On a residual q, the phase is e(-hD(q)/q), where D(q)=q*omega_{P,k}(q)-kP.
normal_form=The residual graph is a q-subset of a single-valued odd-candidate map, not a branch graph.
not_enough=The subset predicate LPF(omega)>=7 is still parity-sensitive and no cancellation over q follows.
```

换言之，LPF residual graph 已被压成 q 上的单值函数 `omega(q)` 及其 LPF 子集谓词。后续难点不再是端点/分支/多重性，而是这个 LPF 选择的 q 子集是否有相位抵消。

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
branch_totals_on_candidates={'both': 390129, 'upper': 436002, 'lower': 440801}
window_width_totals={'-1': 2214518, '0': 783233, '1': 876803}
max_odd_candidates_per_q=1
unique_odd_candidate_per_q=true
predicted_edges_equal_actual_edges=true
all_predicted_displacements_in_1_to_Pminus1=true
bad_candidate_total=0
bad_phase_displacement_total=0
missing_edge_total=0
extra_edge_total=0
```

有限审计只验证实现和账本一致性；全局闭合来自 clipped window 长度 `<2` 与 residual cofactor 的奇性。

代表行：

| P | k | q_count | odd_candidate_count | actual_edge_count_R30 | predicted_edge_count_R30 | reason_counter | sample_predicted_edges |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 10 | 7 | 1 | 1 | no_odd_candidate:3, prime:4, residual_lpf_ge_7_composite:1, small_lpf_3:2 | q=71,omega=143,branch=both,d=53,lpf=11 |
| 257 | 256 | 23 | 16 | 3 | 3 | no_odd_candidate:7, prime:6, residual_lpf_ge_7_composite:3, small_lpf_3:4, small_lpf_5:3 | q=137,omega=481,branch=lower,d=105,lpf=13; q=151,omega=437,branch=upper,d=195,lpf=19; q=193,omega=341,branch=lower,d=21,lpf=11 |
| 971 | 936 | 71 | 49 | 23 | 23 | no_odd_candidate:22, prime:12, residual_lpf_ge_7_composite:23, small_lpf_3:6, small_lpf_5:8 | q=491,omega=1853,branch=upper,d=967,lpf=17; q=503,omega=1807,branch=lower,d=65,lpf=13; q=523,omega=1739,branch=upper,d=641,lpf=37; q=541,omega=1681,branch=upper,d=565,lpf=41; q=557,omega=1633,branch=upper,d=725,lpf=23 |
| 1009 | 1008 | 72 | 54 | 9 | 9 | no_odd_candidate:18, prime:19, residual_lpf_ge_7_composite:9, small_lpf_3:20, small_lpf_5:6 | q=563,omega=1807,branch=lower,d=269,lpf=13; q=577,omega=1763,branch=lower,d=179,lpf=41; q=617,omega=1649,branch=lower,d=361,lpf=17; q=647,omega=1573,branch=upper,d=659,lpf=11; q=743,omega=1369,branch=lower,d=95,lpf=37 |

## 4. 外部前沿匹配

| source | useful_part | accepted_for_this_gate | closes_phase_saving | reason_not_direct |
| --- | --- | --- | --- | --- |
| Euler parity plus clipped reciprocal window algebra | closes the unique odd candidate projection | true | false | turns residual edges into a q-subset, but gives no cancellation on that subset |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | power-saving bilinear Kloosterman estimates for arbitrary moduli | false | false | the q-subset odd-candidate phase is not yet a completed bilinear Kloosterman sum |
| Pascadi 2025 arXiv:2511.08445 | Type-II Kloosterman sums with composite moduli via non-abelian amplification | false | false | does not estimate this fixed-row prime-q LPF-subset phase directly |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | Kloosterman sums parametrised by square-free and smooth integers | false | false | still requires a completion identity from odd candidates to Kloosterman sums |
| Dong--Robles--Zeindler 2026 arXiv:2601.00292 | Kloosterman-fraction bilinear-form near miss | false | false | withdrawn on arXiv; cannot be cited as a valid external input |

外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把 parity-selected branch phase 精确改写为 q 单值 odd-candidate LPF-subset phase。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PrimeQUniqueOddCandidateProjection | true | true | Every prime q has at most one odd candidate omega in its clipped reciprocal window. | none |
| LPFResidualAsQSubsetPredicate | true | true | Residual edges are exactly q with omega composite and LPF(omega)>=7. | none |
| PrimeQUniqueOddCandidateLPFSubsetPhaseSaving | false | false | For \|h\|<=polylog(P), prove cancellation over q with LPF(omega(q))>=7 composite. | unique odd candidate LPF-subset phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the odd-candidate q-subset phase to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQUniqueOddCandidateLPFSubsetPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
unique_odd_candidate_projection_closed=true
unique_odd_candidate_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
