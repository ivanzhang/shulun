# Prime Matrix Phi-LPF rough quotient second LPF split closure 审计

**状态：** `rough_quotient_second_lpf_split_closed_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQSmallRoughQuotientCandidatePhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | RoughQuotientSecondLPFSplitAndUniqueBeta | true | the rough quotient alpha has an immediate prime/composite split, and its composite cell has a unique second quotient for each (q,r,s) |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | no faster deterministic closure than the available second-LPF descent inside Phi-LPF |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | verification package, not a second-LPF rough quotient gate |

本轮继续选择行/列 Phi-LPF，因为上一层已经把 residual 压成 `q,r,alpha` 的唯一 rough quotient 图。最快可闭合的真子门是把 `alpha` 分成素数商与第二 LPF 合成商。

## 2. 第二 LPF 分裂正规形

```text
two_cells=alpha prime OR alpha=s*beta with s=LPF(alpha)>=r, beta>=s, LPF(beta)>=s.
unique_beta_candidate=For fixed (q,r,s), beta=floor(kP/(q*r*s))+1 is the only possible second quotient because P/(q*r*s)<2/(r*s)<=2/49<1.
edge_decomposition=Residual edges split exactly into semiprime-alpha edges and second-LPF rough-quotient quadruples (q,r,s,beta).
phase=Both cells keep phase e(-hD/q), with D=q*r*alpha-kP or D=q*r*s*beta-kP.
not_enough=The remaining hard point is phase saving or signed separation across the two-cell iterated rough quotient graph.
```

这一步继续下钻而不循环：`alpha` 的合成部分被强制写成 `s*beta`，且固定 `(q,r,s)` 时二级商区间长度 `<1`。剩余困难转为两个相位单元的 signed/oscillatory 控制。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
actual_total_edges_R30=299977
predicted_total_edges_R30=299977
semiprime_alpha_total_edges=274812
second_lpf_total_edges=25165
predicted_second_quadruple_total=25165
split_totals_on_edges={'semiprime_alpha_prime': 274812, 'second_lpf_descent_cell': 25165}
lpf_r_bucket_totals={'7': 96700, '11': 52080, '13': 44104, '17': 34414, '19': 29723, '23': 22368, '29': 11815, '31': 6916, '37': 1559, '41': 262, '43': 36}
second_rs_bucket_totals={'7,7': 15091, '7,11': 6978, '7,13': 1882, '11,11': 1181, '11,13': 33}
max_beta_interval_points=1
beta_interval_unique_for_each_qrs=true
predicted_edges_equal_actual_edges=true
two_cell_partition_exhaustive=true
second_quadruples_equal_second_edges=true
all_predicted_displacements_in_1_to_Pminus1=true
all_alpha_formulas_verified=true
all_beta_formulas_verified=true
all_second_lpf_descent_valid=true
bad_beta_interval_total=0
bad_alpha_formula_total=0
bad_beta_formula_total=0
bad_second_lpf_total=0
bad_displacement_total=0
missing_edge_total=0
extra_edge_total=0
```

有限审计只验证实现和账本一致性；全局闭合来自 `P/(q*r*s)<1` 与最小素因子递降。

代表行：

| P | k | actual_edge_count_R30 | semiprime_alpha_edge_count | second_lpf_edge_count | r_bucket_counter | rs_bucket_counter | semiprime_samples | second_lpf_samples |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 1 | 1 | 0 | 11:1 |  | q=71,r=11,alpha=13,m=143,d=53 | empty |
| 257 | 256 | 3 | 3 | 0 | 11:1, 13:1, 19:1 |  | q=151,r=19,alpha=23,m=437,d=195; q=193,r=11,alpha=31,m=341,d=21; q=137,r=13,alpha=37,m=481,d=105 | empty |
| 971 | 936 | 23 | 21 | 2 | 11:4, 13:2, 17:6, 19:1, 23:2, 37:1, 41:1, 7:6 | 11,11:1, 7,13:1 | q=673,r=7,alpha=193,m=1351,d=367; q=677,r=17,alpha=79,m=1343,d=355; q=919,r=23,alpha=43,m=989,d=35; q=523,r=37,alpha=47,m=1739,d=641; q=491,r=17,alpha=109,m=1853,d=967 | q=683,r=11,s=11,beta=11,m=1331,d=217; q=769,r=7,s=13,beta=13,m=1183,d=871 |
| 1009 | 1008 | 9 | 8 | 1 | 11:1, 13:2, 17:1, 23:1, 31:1, 37:1, 41:1, 7:1 | 11,11:1 | q=991,r=13,alpha=79,m=1027,d=685; q=941,r=23,alpha=47,m=1081,d=149; q=743,r=37,alpha=37,m=1369,d=95; q=617,r=17,alpha=97,m=1649,d=361; q=761,r=7,alpha=191,m=1337,d=385 | q=647,r=11,s=11,beta=13,m=1573,d=659 |

## 4. 外部前沿匹配

| source | source_url | verified_status | useful_part | closes_this_gate | reason_not_direct |
| --- | --- | --- | --- | --- | --- |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | https://arxiv.org/abs/2511.07550 | power-saving estimates for general bilinear Kloosterman forms modulo arbitrary q | possible target only after completing the iterated rough quotient graph to bilinear Kloosterman sums | false | does not handle the fixed-row alpha-prime/second-LPF split directly |
| Pascadi 2025 arXiv:2511.08445 | https://arxiv.org/abs/2511.08445 | non-abelian amplification for Type-II Kloosterman sums with composite moduli | possible completion technology for a later Type-II organisation | false | not a pointwise estimate for this prime-q iterated quotient graph |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | https://arxiv.org/abs/2411.12113 | Kloosterman sums parametrised by square-free and smooth integers; Cambridge journal version first online in 2025 | comparison source for arithmetic-function-twisted Kloosterman sums after a bridge | false | alpha-prime and second-LPF rough quotient cells are not their completed parameter family |
| Dong--Robles--Zeindler 2026 arXiv:2601.00292 | https://arxiv.org/abs/2601.00292 | withdrawn on arXiv v2 after a missing factor was reported | near-miss diagnostic only | false | withdrawn papers cannot be used as an admissible external theorem |

这些外部 Kloosterman/Type-II 结果仍只是后续 completion 的候选工具；本层闭合的是内部第二 LPF 分裂和唯一 beta 正规形。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RoughQuotientPrimeOrSecondLPFPartition | true | true | The r-rough quotient alpha is either prime or has second least prime factor s>=r. | none |
| FixedPrimeQRSecondLPFQuotientSingleton | true | true | For fixed q,r,s, the beta interval has length <1 and contains at most one integer. | none |
| ResidualAsSemiprimeAlphaOrSecondRoughQuotientGraph | true | true | Residual edges split exactly into semiprime-alpha edges and second-LPF rough quotient quadruples. | none |
| PrimeQIteratedRoughQuotientTwoCellPhaseSaving | false | false | Prove cancellation or signed separation over semiprime-alpha and second-LPF rough quotient cells. | two-cell iterated rough quotient phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the iterated quotient graph to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQIteratedRoughQuotientTwoCellPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
rough_quotient_second_lpf_split_closed=true
iterated_rough_quotient_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
