# Prime Matrix Phi-LPF floor residue branch phase closure 审计

**状态：** `floor_residue_branch_normal_form_closed_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQMatchedDisplacementPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | PrimeQFloorResidueBranchNormalForm | true | exact floor-residue algebra after matched displacement closure; no new prime theorem required |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | still needs Buchstab transfer and denominator audit |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a closable floor-residue phase gate |

matched displacement 闭合后，本轮继续选择行/列 Phi-LPF 的 q-side floor-residue branch 子门。该门只用整数端点与余数恒等式闭合；它不证明后续相位和抵消。

## 2. floor-residue branch 正规形

```text
lower_cap_absence=A residual edge cannot be supported by the q-side lower cap m>=q: m=q is prime and the only other possible point q+1 is even.
upper_cap_absence=A residual edge cannot be supported by the q-side upper cap m<=2P-1: q(2P-1)>P^2 for every integer q>P/2.
lower_branch=If m=floor(kP/q)+1, then d=q-(kP mod q), with 1<=d<=q.
upper_branch=If m=floor(((k+1)P-1)/q), then d=P-1-(((k+1)P-1) mod q), with P-q<=d<=P-1.
normal_form=The matched phase is a sum over lower/upper floor-residue branches, not over unclipped endpoint labels.
not_enough=The lower/upper branch residues still move with the LPF-selected matching graph; no cancellation follows from this identity alone.
```

设 `rho=(kP mod q)`、`sigma=(((k+1)P-1) mod q)`。lower floor branch 给 `d=q-rho`；upper floor branch 给 `d=P-1-sigma`。若一个点同时是 lower 与 upper，则两个公式给出同一个 `d`。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_edges_R30=299977
branch_totals={'lower': 104807, 'upper': 103674, 'both': 91496, 'interior': 0}
all_q_side_boundary_caps_absent=true
all_edges_floor_branch_covered=true
all_floor_residue_formulas_verified=true
bad_cap_total=0
bad_floor_coverage_total=0
bad_residue_formula_total=0
```

有限审计只验证实现和账本一致性；全局闭合来自 q-side cap 排除和 floor-residue 恒等式。

代表行：

| P | k | edge_count_R30 | branch_lower | branch_upper | branch_both | min_lower_or_both_displacement | max_lower_or_both_displacement | min_upper_or_both_displacement | max_upper_or_both_displacement | sample_edges |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 1 | 0 | 0 | 1 | 53 | 53 | 53 | 53 | q=71,m=143,d=53,branch=both,rho=18,sigma=47 |
| 257 | 256 | 3 | 2 | 1 | 0 | 21 | 105 | 195 | 195 | q=137,m=481,d=105,branch=lower,rho=32,sigma=14; q=151,m=437,d=195,branch=upper,rho=107,sigma=61; q=193,m=341,d=21,branch=lower,rho=172,sigma=42 |
| 971 | 936 | 23 | 4 | 8 | 11 | 17 | 865 | 275 | 967 | q=491,m=1853,d=967,branch=upper,rho=15,sigma=3; q=503,m=1807,d=65,branch=lower,rho=438,sigma=402; q=523,m=1739,d=641,branch=upper,rho=405,sigma=329; q=541,m=1681,d=565,branch=upper,rho=517,sigma=405; q=557,m=1633,d=725,branch=upper,rho=389,sigma=245 |
| 1009 | 1008 | 9 | 4 | 1 | 4 | 95 | 685 | 149 | 685 | q=563,m=1807,d=269,branch=lower,rho=294,sigma=176; q=577,m=1763,d=179,branch=lower,rho=398,sigma=252; q=617,m=1649,d=361,branch=lower,rho=256,sigma=30; q=647,m=1573,d=659,branch=upper,rho=635,sigma=349; q=743,m=1369,d=95,branch=lower,rho=648,sigma=170 |

## 4. 外部前沿匹配

| source | useful_part | accepted_for_this_gate | closes_phase_saving | reason_not_direct |
| --- | --- | --- | --- | --- |
| Elementary floor-residue algebra | closes the q-side cap-free lower/upper residue branch formulas | true | false | normalises branches only; gives no cancellation over LPF-selected primes |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | power-saving bilinear Kloosterman estimates for arbitrary moduli | false | false | floor-residue branches are not yet completed bilinear Kloosterman sums |
| Pascadi 2025 arXiv:2511.08445 | Type-II Kloosterman sums with composite moduli via non-abelian amplification | false | false | the current modulus is prime q and the graph is a fixed-row matched subset |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | Kloosterman sums parametrised by square-free and smooth integers | false | false | requires finite-field/Kloosterman completion before it can see these floor residues |
| Dong--Robles--Zeindler 2026 arXiv:2601.00292 | Kloosterman-fraction bilinear-form near miss | false | false | withdrawn on arXiv; cannot be cited as a valid external input |

外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把 matched displacement phase 精确拆成 lower/upper floor-residue branch phase。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PrimeQBoundaryCapFreeForResidualEdges | true | true | Residual edges cannot arise from q-side lower cap m=q or upper cap m=2P-1. | none |
| PrimeQFloorResidueBranchNormalForm | true | true | Every residual edge belongs to a lower and/or upper floor-residue branch with the exact d formulas. | none |
| PrimeQFloorResidueBranchPhaseSaving | false | false | For \|h\|<=polylog(P), prove cancellation over the lower/upper floor-residue branch sums. | floor-residue branch phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the floor-residue branch graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQFloorResidueBranchPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
floor_residue_branch_normal_form_closed=true
floor_residue_branch_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
