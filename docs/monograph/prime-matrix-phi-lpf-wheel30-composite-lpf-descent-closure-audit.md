# Prime Matrix Phi-LPF wheel30 composite LPF descent closure 审计

**状态：** `wheel30_composite_lpf_descent_closed_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQUniqueOddCandidateWheel30CompositeSurvivorPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | Wheel30CompositeLPFDescentUniqueRoughQuotient | true | the composite survivor has an immediate least-prime-factor descent with a unique quotient candidate for each (q,r) |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | slower than the deterministic LPF descent now available inside the Phi-LPF branch |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a closable wheel-30 composite descent gate |

本轮继续选择行/列 Phi-LPF，因为上一层留下的对象已经是 `30`-wheel survivor 的 composite 部分。最快可闭合的真子门是把该 composite survivor 按最小素因子 `r` 递降为唯一 rough quotient 候选。

## 2. LPF 递降正规形

```text
factorization=residual omega=r*a with r=LPF(omega), 7<=r<=sqrt(2P-1), a>=r, LPF(a)>=r.
unique_quotient_candidate=For fixed (q,r), alpha=floor(kP/(q*r))+1 is the only possible quotient because P/(q*r)<2/r<1.
edge_equivalence=A residual edge is exactly a prime pair (q,r) with alpha<=floor(((k+1)P-1)/(q*r)), alpha>=r, q<=r*alpha<=2P-1, and LPF(alpha)>=r.
phase=The residual phase is e(-hD(q,r)/q), D(q,r)=q*r*alpha_{P,k}(q,r)-kP.
normal_form=The residual q-subset becomes a sparse prime-q/small-prime-r rough-quotient candidate graph with 0/1 coefficients.
not_enough=The remaining hard point is cancellation or signed separation on this rough-quotient graph.
```

这一步是真推进：`omega(q)` 的 composite 判断不再是黑箱，而被替换为小素数 `r<=sqrt(2P-1)` 与唯一商 `alpha=floor(kP/(q*r))+1` 的 0/1 图。相位节省仍未得到。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
total_prime_q_instances=3874554
total_lpf_r_row_instances=638542
total_qr_pair_instances=34664566
actual_total_edges_R30=299977
predicted_total_edges_R30=299977
predicted_total_triples=299977
reason_totals_on_qr={'no_integer_quotient': 31685737, 'quotient_below_lpf': 894284, 'residual_lpf_descent_triple': 299977, 'quotient_not_r_rough': 918968, 'cofactor_clip_fail': 865600}
lpf_r_bucket_totals={'7': 96700, '11': 52080, '13': 44104, '17': 34414, '19': 29723, '23': 22368, '29': 11815, '31': 6916, '37': 1559, '41': 262, '43': 36}
distinct_lpf_r_count=11
max_lpf_r_seen=43
max_quotient_interval_points=1
max_reverse_m_multiplicity=1
quotient_interval_unique_for_each_qr=true
predicted_edges_equal_actual_edges=true
predicted_triples_equal_edges=true
all_predicted_displacements_in_1_to_Pminus1=true
all_predicted_triples_have_lpf_descent=true
reverse_m_multiplicity_le_1=true
bad_quotient_interval_total=0
bad_displacement_total=0
bad_lpf_descent_total=0
missing_edge_total=0
extra_edge_total=0
```

有限审计只验证实现和账本一致性；全局闭合来自 `P/(q*r)<2/r<1` 与最小素因子分解。

代表行：

| P | k | q_count | r_count | actual_edge_count_R30 | predicted_edge_count_R30 | reason_counter_on_qr | r_bucket_counter | sample_descent_triples |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 10 | 3 | 1 | 1 | no_integer_quotient:27, quotient_below_lpf:1, quotient_not_r_rough:1, residual_lpf_descent_triple:1 | 11:1 | q=71,r=11,a=13,m=143,d=53 |
| 257 | 256 | 23 | 5 | 3 | 3 | no_integer_quotient:101, quotient_below_lpf:1, quotient_not_r_rough:10, residual_lpf_descent_triple:3 | 11:1, 13:1, 19:1 | q=137,r=13,a=37,m=481,d=105; q=151,r=19,a=23,m=437,d=195; q=193,r=11,a=31,m=341,d=21 |
| 971 | 936 | 71 | 11 | 23 | 23 | no_integer_quotient:710, quotient_below_lpf:8, quotient_not_r_rough:40, residual_lpf_descent_triple:23 | 11:4, 13:2, 17:6, 19:1, 23:2, 37:1, 41:1, 7:6 | q=491,r=17,a=109,m=1853,d=967; q=503,r=13,a=139,m=1807,d=65; q=523,r=37,a=47,m=1739,d=641; q=541,r=41,a=41,m=1681,d=565; q=557,r=23,a=71,m=1633,d=725 |
| 1009 | 1008 | 72 | 11 | 9 | 9 | no_integer_quotient:731, quotient_below_lpf:9, quotient_not_r_rough:43, residual_lpf_descent_triple:9 | 11:1, 13:2, 17:1, 23:1, 31:1, 37:1, 41:1, 7:1 | q=563,r=13,a=139,m=1807,d=269; q=577,r=41,a=43,m=1763,d=179; q=617,r=17,a=97,m=1649,d=361; q=647,r=11,a=143,m=1573,d=659; q=743,r=37,a=37,m=1369,d=95 |

## 4. 外部前沿匹配

| source | source_url | verified_status | useful_part | closes_this_gate | reason_not_direct |
| --- | --- | --- | --- | --- | --- |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | https://arxiv.org/abs/2511.07550 | power-saving bilinear Kloosterman estimates modulo arbitrary q | a target theorem after turning the (q,r,alpha) graph into a genuine bilinear Kloosterman form | false | the present phase still has a floor-defined rough quotient and a fixed-row LPF predicate |
| Pascadi 2025 arXiv:2511.08445 | https://arxiv.org/abs/2511.08445 | non-abelian amplification for Type-II Kloosterman sums with composite moduli | candidate completion technology if the rough quotient graph is reorganised into composite-modulus Type-II sums | false | does not estimate the pointwise prime-q/small-r graph directly |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | https://arxiv.org/abs/2411.12113 | Kloosterman sums parametrised by square-free and smooth integers; journal version appeared online in 2025 | relevant to arithmetic-function-twisted Kloosterman sums after a completion bridge | false | rough quotient candidates are neither their square-free/smooth parameter family nor already completed Kloosterman sums |
| Dong--Robles--Zeindler 2026 arXiv:2601.00292 | https://arxiv.org/abs/2601.00292 | withdrawn on arXiv v2 after a missing factor was reported | near-miss diagnostic only | false | withdrawn papers cannot be used as an admissible external theorem |

这些外部 Kloosterman/Type-II 结果仍只是 completion 后的候选工具；本层闭合的是内部 LPF 递降与唯一商正规形。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| Wheel30CompositeLPFDescentUniqueRoughQuotient | true | true | Every residual wheel-30 composite survivor is uniquely r*a with r=LPF and a r-rough. | none |
| FixedPrimeQSmallRQuotientIntervalSingleton | true | true | For fixed q and r, the quotient interval has length <1 and has at most one integer alpha. | none |
| ResidualAsPrimeQSmallRoughQuotientCandidateGraph | true | true | Residual edges are exactly the 0/1 graph of prime q, small prime r, and the unique rough quotient alpha. | none |
| PrimeQSmallRoughQuotientCandidatePhaseSaving | false | false | Prove cancellation or signed separation over the resulting prime-q/small-r rough-quotient graph. | rough quotient graph phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the rough-quotient graph phase to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQSmallRoughQuotientCandidatePhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
wheel30_composite_lpf_descent_closed=true
rough_quotient_graph_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
