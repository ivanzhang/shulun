# Prime Matrix Phi-LPF matched displacement phase closure 审计

**状态：** `matched_displacement_phase_normal_form_closed_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQMatchingSubsetReciprocalPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | MatchedDisplacementPhaseNormalForm | true | exact integer displacement identity after matching graph closure; no new prime theorem required |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | still needs Buchstab transfer and denominator audit |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a closable phase-normal-form gate |

matching graph 闭合后，本轮继续选择行/列 Phi-LPF 的 phase normal-form 子门。该门只用整数恒等式与端点窗口，可完全闭合；它不证明后续相位和抵消。

## 2. matched displacement phase 正规形

```text
displacement=For every matched edge (q,m), define d=q*m-kP; then 1<=d<P.
phase_identity=For every integer h, e(h*kP/q)=e(-h*d/q), since h*kP/q=h*m-h*d/q.
q_endpoint_selector=m is one of the two clipped endpoints max(q,floor(kP/q)+1) or min(2P-1,floor(((k+1)P-1)/q)).
m_endpoint_selector=q is one of the two clipped reverse endpoints max(P/2+1,floor(kP/m)+1) or min(P-1,m,floor(((k+1)P-1)/m)).
normal_form=The finite phase is a matched displacement sum over edges (q,m,d), not an unnormalised large-numerator reciprocal phase.
not_enough=The displacement d is still a moving, LPF-selected residue; cancellation for the matched displacement sum remains open.
```

关键点是：每条匹配边满足 `kP<qm<(k+1)P`，所以 `d=qm-kP` 自动落在 `[1,P-1]`。又因为 `kP=qm-d`，对任意整数 `h` 有 `h*kP/q=h*m-h*d/q`，指数相位中的整数项消失，得到 `e(hkP/q)=e(-hd/q)`。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_edges_R30=299977
global_min_displacement=1
global_max_displacement=1008
all_displacements_in_1_to_Pminus1=true
all_phase_congruences_verified=true
all_endpoint_selectors_verified=true
q_endpoint_totals={'lower': 104807, 'upper': 103674, 'both': 91496}
m_endpoint_totals={'lower': 18261, 'upper': 17930, 'both': 263786}
bad_displacement_total=0
bad_phase_total=0
bad_endpoint_total=0
bad_edge_total=0
```

有限审计只验证实现和账本一致性；全局闭合来自上面的整数位移恒等式。

代表行：

| P | k | edge_count_R30 | min_displacement | max_displacement | q_endpoint_lower | q_endpoint_upper | q_endpoint_both | m_endpoint_lower | m_endpoint_upper | m_endpoint_both | sample_edges |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 1 | 53 | 53 | 0 | 0 | 1 | 0 | 0 | 1 | q=71,m=143,d=53 |
| 257 | 256 | 3 | 21 | 195 | 2 | 1 | 0 | 0 | 0 | 3 | q=137,m=481,d=105; q=151,m=437,d=195; q=193,m=341,d=21 |
| 971 | 936 | 23 | 17 | 967 | 4 | 8 | 11 | 0 | 0 | 23 | q=491,m=1853,d=967; q=503,m=1807,d=65; q=523,m=1739,d=641; q=541,m=1681,d=565; q=557,m=1633,d=725 |
| 1009 | 1008 | 9 | 95 | 685 | 4 | 1 | 4 | 0 | 0 | 9 | q=563,m=1807,d=269; q=577,m=1763,d=179; q=617,m=1649,d=361; q=647,m=1573,d=659; q=743,m=1369,d=95 |

## 4. 外部前沿匹配

| source | useful_part | accepted_for_this_gate | closes_phase_saving | reason_not_direct |
| --- | --- | --- | --- | --- |
| Elementary integer phase reduction | closes e(hkP/q)=e(-hd/q) on every matched edge | true | false | normalises the phase only; gives no cancellation over moving displacements |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | arbitrary-modulus bilinear Kloosterman power savings after completion | false | false | matched displacement phase is not yet a completed Kloosterman bilinear form |
| Pascadi 2025 arXiv:2511.08445 | non-abelian amplification for composite-modulus Kloosterman sums | false | false | does not estimate this fixed-row matched real phase directly |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | Kloosterman sums over square-free and smooth parameters | false | false | requires finite-field Kloosterman completion first |

外部 Kloosterman/Type-II 前沿仍是后续相位门候选；本层只把大分子 reciprocal phase 精确改写为 matched displacement phase。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| MatchedDisplacementPhaseNormalForm | true | true | Every matched edge has d=qm-kP in [1,P-1] and e(hkP/q)=e(-hd/q). | none |
| TwoSidedEndpointSelectorNormalForm | true | true | Each matched edge lies on a q-side endpoint and an m-side reverse endpoint. | none |
| PrimeQMatchedDisplacementPhaseSaving | false | false | For \|h\|<=polylog(P), prove cancellation for sum over matched edges e(-h*d(q)/q). | matched displacement phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the matched displacement graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQMatchedDisplacementPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
matched_displacement_phase_normal_form_closed=true
weighted_reciprocal_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
