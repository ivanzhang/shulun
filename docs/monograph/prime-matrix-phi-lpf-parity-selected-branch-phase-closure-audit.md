# Prime Matrix Phi-LPF parity selected branch phase closure 审计

**状态：** `parity_selected_branch_normal_form_closed_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQFloorResidueBranchPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | PrimeQParitySelectedFloorResidueBranchNormalForm | true | two-point floor windows plus LPF>=7 oddness determine the branch; no new prime theorem required |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | still needs Buchstab transfer and denominator audit |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a closable parity-selected branch gate |

floor-residue branch 闭合后，本轮继续选择行/列 Phi-LPF 的 parity-selected branch 子门。该门只用二点窗口和 `LPF(m)>=7` 的奇性闭合；它不证明后续相位和抵消。

## 2. parity-selected branch 正规形

```text
floor_window=After cap removal, L=floor(kP/q)+1 and U=floor(((k+1)P-1)/q), with U-L in {0,1} on every edge.
singleton=If U=L, the edge is simultaneously lower and upper and both residue formulae give the same d.
two_point_selector=If U=L+1, the residual cofactor is odd, so the edge is lower exactly when L is odd and upper exactly when U is odd.
phase_formula=The selected branch phase uses d=q-(kP mod q) on lower and d=P-1-(((k+1)P-1) mod q) on upper.
not_enough=Parity selects the endpoint side but gives no cancellation over the remaining LPF-selected prime q set.
```

写 `L=floor(kP/q)+1`、`U=floor(((k+1)P-1)/q)`。若 `U=L+1`，则两个候选端点连续；residual cofactor 必为奇数，因此分支由 `L` 的奇偶性决定。若 `U=L`，该边同时是 lower 与 upper。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_edges_R30=299977
width_totals={'singleton_width_0': 91496, 'two_point_width_1': 208481}
actual_branch_totals={'lower': 104807, 'upper': 103674, 'both': 91496}
predicted_branch_totals={'lower': 104807, 'upper': 103674, 'both': 91496}
all_edges_width_zero_or_one=true
all_two_point_branches_parity_selected=true
all_residual_cofactors_odd=true
all_branch_phase_formulas_verified=true
all_singleton_branch_formulas_consistent=true
bad_width_total=0
bad_parity_total=0
bad_prediction_total=0
bad_phase_formula_total=0
bad_singleton_formula_total=0
```

有限审计只验证实现和账本一致性；全局闭合来自二点窗口与奇偶端点选择。

代表行：

| P | k | edge_count_R30 | width_0_singleton_edges | width_1_two_point_edges | branch_lower | branch_upper | branch_both | sample_edges |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 1 | 1 | 0 | 0 | 0 | 1 | q=71,m=143,L=143,U=143,branch=both,pred=both,d=53 |
| 257 | 256 | 3 | 0 | 3 | 2 | 1 | 0 | q=137,m=481,L=481,U=482,branch=lower,pred=lower,d=105; q=151,m=437,L=436,U=437,branch=upper,pred=upper,d=195; q=193,m=341,L=341,U=342,branch=lower,pred=lower,d=21 |
| 971 | 936 | 23 | 11 | 12 | 4 | 8 | 11 | q=491,m=1853,L=1852,U=1853,branch=upper,pred=upper,d=967; q=503,m=1807,L=1807,U=1808,branch=lower,pred=lower,d=65; q=523,m=1739,L=1738,U=1739,branch=upper,pred=upper,d=641; q=541,m=1681,L=1680,U=1681,branch=upper,pred=upper,d=565; q=557,m=1633,L=1632,U=1633,branch=upper,pred=upper,d=725 |
| 1009 | 1008 | 9 | 4 | 5 | 4 | 1 | 4 | q=563,m=1807,L=1807,U=1808,branch=lower,pred=lower,d=269; q=577,m=1763,L=1763,U=1764,branch=lower,pred=lower,d=179; q=617,m=1649,L=1649,U=1650,branch=lower,pred=lower,d=361; q=647,m=1573,L=1572,U=1573,branch=upper,pred=upper,d=659; q=743,m=1369,L=1369,U=1370,branch=lower,pred=lower,d=95 |

## 4. 外部前沿匹配

| source | useful_part | accepted_for_this_gate | closes_phase_saving | reason_not_direct |
| --- | --- | --- | --- | --- |
| Euler 2-wheel parity plus floor-window algebra | closes endpoint-side selection in every two-point q-window | true | false | endpoint selection is deterministic, but cancellation over selected q remains open |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | power-saving bilinear Kloosterman estimates for arbitrary moduli | false | false | the parity-selected branch is not yet a completed bilinear Kloosterman sum |
| Pascadi 2025 arXiv:2511.08445 | Type-II Kloosterman sums with composite moduli via non-abelian amplification | false | false | does not estimate this fixed-row prime-q branch phase directly |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | Kloosterman sums parametrised by square-free and smooth integers | false | false | still requires a completion identity from floor residues to Kloosterman sums |
| Dong--Robles--Zeindler 2026 arXiv:2601.00292 | Kloosterman-fraction bilinear-form near miss | false | false | withdrawn on arXiv; cannot be cited as a valid external input |

外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把 floor-residue branch 精确拆成由 parity selector 决定的 branch phase。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| TwoPointFloorWindowParitySelector | true | true | When U=L+1, the residual endpoint is the unique odd endpoint. | none |
| SingletonBothBranchConsistency | true | true | When U=L, lower and upper residue formulae agree on the same displacement d. | none |
| PrimeQParitySelectedFloorResidueBranchPhaseSaving | false | false | For \|h\|<=polylog(P), prove cancellation after replacing branch choice by the parity selector. | parity-selected branch phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the parity-selected branch graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQParitySelectedFloorResidueBranchPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
parity_selected_branch_normal_form_closed=true
parity_selected_branch_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
