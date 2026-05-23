# Prime Matrix Phi-LPF complete rough factor tree closure 审计

**状态：** `complete_rough_factor_tree_closed_leaf_phase_saving_open`
**核验日期：** `2026-05-23`

## 1. 三命题选择

| claim | frontier | frontier_before | fastest_subgate | chosen | reason |
| --- | --- | --- | --- | --- | --- |
| Prime Matrix row/column Phi-LPF |  | PrimeQIteratedRoughQuotientTwoCellPhaseSaving / AND CompletionToExternalKloostermanOrVaughanTypeII | CompleteRoughFactorTreeAndPrefixSingletons | true | the two-cell iterated quotient graph still has deterministic LPF recursion; all fixed-prefix suffixes are singleton intervals |
| two-point sieve / prime-pair line | BMD=>TLI without hidden denominator/parity gap |  |  | false | no faster deterministic closure than exhausting the current Phi-LPF LPF recursion |
| RH contradiction-field line | IndependentRefereeAcceptanceOfAllRHControlledExits |  |  | false | not a same-object LPF recursion gate |

本轮继续选择行/列 Phi-LPF，因为上一层二级 LPF 分裂仍留下 deterministic LPF recursion。最快可闭合子门是把 residual cofactor 完整写成粗素因子叶子树。

## 2. 完整粗因子树正规形

```text
normal_form=Every R30 residual edge has a unique complete rough prime factor chain m=p1*...*pt with 7<=p1<=...<=pt.
prefix_singleton=For each proper prefix G_j=p1*...*pj, the suffix A_j=m/G_j is the unique integer floor(kP/(q*G_j))+1.
interval_reason=P/(q*G_j)<2/G_j<=2/7<1, and the bound only improves with depth.
phase=Each leaf keeps D=q*m-kP and phase e(-hD/q); no deterministic LPF split remains.
not_enough=The remaining hard point is signed phase saving over the complete rough-factor leaves or an exact completion to external Kloosterman/Vaughan Type-II form.
```

这一步耗尽了“继续按 LPF 分裂”的确定性收益：任何再分裂只是在同一完整叶子链上揭示更深前缀。真正剩余不再是因子正规形，而是叶子相位节省或外部 completion。

## 3. 全量有限审计

```text
max_prime=1009
k_range=1<=k<P in this implementation audit
row_count=76954
active_residual_row_count=52697
actual_total_edges_R30=299977
predicted_complete_leaf_total=299977
max_factor_depth_observed=3
depth_totals={'2': 274812, '3': 25165}
first_factor_totals={'7': 96700, '11': 52080, '13': 44104, '17': 34414, '19': 29723, '23': 22368, '29': 11815, '31': 6916, '37': 1559, '41': 262, '43': 36}
leaf_signature_top20={'7*109': 3204, '13*59': 3182, '19*41': 3178, '19*37': 3173, '7*107': 3173, '11*71': 3169, '7*103': 3165, '7*97': 3162, '23*31': 3161, '11*67': 3160, '13*53': 3159, '17*41': 3157, '17*43': 3151, '7*101': 3148, '7*113': 3145, '13*61': 3139, '23*29': 3134, '17*47': 3133, '11*73': 3115, '7*7*17': 3114}
max_prefix_interval_points=1
prefix_interval_unique_for_every_prefix=true
predicted_complete_leaves_equal_actual_edges=true
complete_factorization_valid=true
all_prefix_formulas_verified=true
all_predicted_displacements_in_1_to_Pminus1=true
bad_prefix_formula_total=0
bad_prefix_interval_total=0
bad_displacement_total=0
bad_factorization_total=0
missing_edge_total=0
extra_edge_total=0
```

有限审计只验证实现和账本一致性；全局闭合来自唯一分解、最小素因子递降和 `P/(q*G_j)<1`。

代表行：

| P | k | actual_edge_count_R30 | predicted_leaf_edge_count | max_depth | depth_counter | first_factor_counter | samples |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 101 | 100 | 1 | 1 | 2 | 2:1 | 11:1 | q=71,m=143,D=53,factors=11*13,prefixes=depth=1,G=11,next_or_suffix=13,candidate=13 |
| 257 | 256 | 3 | 3 | 2 | 2:3 | 11:1, 13:1, 19:1 | q=151,m=437,D=195,factors=19*23,prefixes=depth=1,G=19,next_or_suffix=23,candidate=23 \| q=193,m=341,D=21,factors=11*31,prefixes=depth=1,G=11,next_or_suffix=31,candidate=31 \| q=137,m=481,D=105,factors=13*37,prefixes=depth=1,G=13,next_or_suffix=37,candidate=37 |
| 971 | 936 | 23 | 23 | 3 | 2:21, 3:2 | 11:4, 13:2, 17:6, 19:1, 23:2, 37:1, 41:1, 7:6 | q=673,m=1351,D=367,factors=7*193,prefixes=depth=1,G=7,next_or_suffix=193,candidate=193 \| q=677,m=1343,D=355,factors=17*79,prefixes=depth=1,G=17,next_or_suffix=79,candidate=79 \| q=919,m=989,D=35,factors=23*43,prefixes=depth=1,G=23,next_or_suffix=43,candidate=43 \| q=523,m=1739,D=641,factors=37*47,prefixes=depth=1,G=37,next_or_suffix=47,candidate=47 \| q=683,m=1331,D=217,factors=11*11*11,prefixes=depth=1,G=11,next_or_suffix=121,candidate=121;depth=2,G=121,next_or_suffix=11,candidate=11 \| q=491,m=1853,D=967,factors=17*109,prefixes=depth=1,G=17,next_or_suffix=109,candidate=109 |
| 1009 | 1008 | 9 | 9 | 3 | 2:8, 3:1 | 11:1, 13:2, 17:1, 23:1, 31:1, 37:1, 41:1, 7:1 | q=991,m=1027,D=685,factors=13*79,prefixes=depth=1,G=13,next_or_suffix=79,candidate=79 \| q=941,m=1081,D=149,factors=23*47,prefixes=depth=1,G=23,next_or_suffix=47,candidate=47 \| q=743,m=1369,D=95,factors=37*37,prefixes=depth=1,G=37,next_or_suffix=37,candidate=37 \| q=617,m=1649,D=361,factors=17*97,prefixes=depth=1,G=17,next_or_suffix=97,candidate=97 \| q=761,m=1337,D=385,factors=7*191,prefixes=depth=1,G=7,next_or_suffix=191,candidate=191 \| q=887,m=1147,D=317,factors=31*37,prefixes=depth=1,G=31,next_or_suffix=37,candidate=37 |

## 4. 外部前沿匹配

| source | source_url | verified_status | useful_part | closes_this_gate | reason_not_direct |
| --- | --- | --- | --- | --- | --- |
| Milićević--Qin--Wu 2025 arXiv:2511.07550 | https://arxiv.org/abs/2511.07550 | power-saving estimates for general bilinear Kloosterman forms modulo arbitrary q | candidate target after completing complete rough-factor leaves to a genuine bilinear Kloosterman family | false | does not supply the missing completion from q, factor-chain leaves, and floor suffixes to standard Kloosterman sums |
| Pascadi 2025 arXiv:2511.08445 | https://arxiv.org/abs/2511.08445 | Type-II Kloosterman sums with composite moduli via non-abelian amplification | candidate technology if the leaf tree is reorganised into composite-modulus Type-II sums | false | near-prime/prime-q fixed-row leaf phases are not yet its input family |
| Shao--Shparlinski--Wijaya 2024/2025 arXiv:2411.12113 | https://arxiv.org/abs/2411.12113 | Kloosterman sums over square-free and smooth integer parameters | possible comparison after replacing LPF leaves by completed smooth/square-free parameter sums | false | the complete rough-factor tree remains a pointwise floor-suffix graph |
| Ford--Maynard 2024 arXiv:2407.14368 | https://arxiv.org/abs/2407.14368 | prime-producing sieve framework requiring object-specific Type-I/II inputs | conceptual guide for what a successful source package must prove | false | the required Type-II estimates for these exact leaves are not produced automatically |

这些外部结果仍是后续 completion 的候选工具；本层闭合的是内部完整 LPF 叶子树，不是外部相位节省。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CompleteRoughFactorTreeNormalForm | true | true | Every residual cofactor is written as one nondecreasing rough-prime leaf chain. | none |
| EveryPrefixRoughQuotientSingleton | true | true | For every fixed prime-q and proper factor prefix, the remaining suffix interval has length <1. | none |
| DeterministicLPFDescentExhausted | true | true | Further LPF splitting only reveals later leaves of the same complete factor tree. | none |
| PrimeQCompleteRoughFactorTreeLeafPhaseSaving | false | false | Prove signed cancellation/separation over the complete rough-factor leaves. | complete leaf phase theorem |
| CompletionToExternalKloostermanOrVaughanTypeII | false | false | Convert the leaf tree to a DI/DFI/BC/FM-compatible estimate without losing pointwise P,k. | completion/dispersion identity |

## 6. 最新最窄口

```text
PrimeQCompleteRoughFactorTreeLeafPhaseSaving
AND CompletionToExternalKloostermanOrVaughanTypeII
```

状态边界：

```text
complete_rough_factor_tree_closed=true
deterministic_lpf_descent_exhausted=true
complete_leaf_phase_saving_closed=false
phi_lpf_parity_barrier_globally_broken=false
row_column_unconditional_closed=false
external_lemma_version_unconditional_closed=false
internal_self_contained_closed=false
```
