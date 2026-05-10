# Prime Matrix strict RKS2/RKS3 统一 rank-two sheaf 合同证书

**状态：** `unified_smooth_rank_two_trace_reduced_to_rank_two_sheaf_rh_or_stepanov_pivot`

本轮没有把作者侧自足 rank-two 迹界证明完结，但完成了最终形态的 sheaf 合同和外部匹配。统一 smooth rank-two 迹函数 `T(lambda)=sum_x A(x)B(1-x)C(1-lambda*x)` 已经被压成 `P^1_lambda-{0,1,infinity}` 上的秩二 lisse hypergeometric/Kummer convolution trace；秩、奇点数和导子只依赖固定分支数，不依赖角色阶 `d`，也不使用整条 `y^d=f(x)` 曲线。因此若接受 Deligne RH for curves 与 Katz hypergeometric sheaf 构造作为外部黑箱，当前 rank-two 输入可以严格对接闭合；但作者侧完全自足路线仍只剩一个原子：`RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma`，即内部证明秩二 lisse sheaf 平方根迹界，或构造等价的初等 Stepanov pivot 块。未完成该内部原子前，Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。

```text
unified_rank_two_sheaf_contract_closed=true
order_free_conductor_ledger_closed=true
external_deligne_katz_match_ready=true
rank_two_rh_trace_bound_internalized=false
elementary_stepanov_pivot_internalized=false
row_column_unconditional_closed=false
```

## 1. sheaf 合同

| field | value |
| --- | --- |
| `trace_function` | T(lambda)=sum_x A(x)B(1-x)C(1-lambda*x), lambda in P^1-{0,1,infinity} |
| `sheaf_object` | rank-two hypergeometric/Kummer convolution local system on the lambda-line |
| `lisse_domain` | U=P^1_lambda minus {0,1,infinity} |
| `singularities` | only 0,1,infinity after previous collision firewall |
| `rank` | 2 |
| `weight` | 1 before normalization, weight 0 after dividing by the Jacobi sqrt(p) kernel |
| `legendre_subcase` | quadratic Legendre core is included as the quadratic specialization |

## 2. 导子账本

| field | value |
| --- | --- |
| `rank_bound` | rank <= 2 |
| `singular_point_count` | at most 3 on the lambda-line |
| `local_monodromy_source` | multiplicative characters A,B,C and their product at infinity |
| `conductor_dependency` | depends only on the number of branch points, not on character order d |
| `forbidden_dependency` | no y^0,...,y^{d-1} Kummer ladder and no genus O(d) argument |

## 3. 路线选项

| field | value |
| --- | --- |
| `external_route` | Deligne RH for curves plus Katz hypergeometric sheaf construction gives \|T(lambda)\| <= C*sqrt(p) |
| `external_status` | matched and available if external black-box lemmas are accepted |
| `internal_route` | prove the same rank-two trace bound by an elementary Stepanov pivot on the lambda-line |
| `internal_status` | not yet proved in the corpus |
| `why_this_is_final_shape` | all earlier support, lambda, Legendre, and d-dependence gates have been eliminated |

## 4. 唯一内部原子

| field | value |
| --- | --- |
| `old_atom` | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `new_atom` | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `single_required_input` | self-contained square-root cancellation for rank-two lisse trace functions on P^1-{0,1,infinity} |
| `equivalent_pivot_input` | construct an elementary order-free Stepanov pivot block for the same rank-two trace |
| `if_external_accepted` | Burgess/Weil/B4 chain may proceed through the matched Deligne-Katz input |
| `if_self_contained_required` | this rank-two RH/Stepanov atom remains the sole internal hard point |

## 5. 禁止捷径

| field | value |
| --- | --- |
| `finite_audit` | bounded numerical samples do not prove the trace theorem |
| `external_as_internal` | Deligne/Katz may close an external route, but it is not an author-side self-contained proof |
| `full_kummer_curve` | returning to y^d=f(x) would reintroduce d-dependent genus and is forbidden |
| `generic_lambda` | the sheaf contract includes all smooth lambda, including j=0 and j=1728 special points |

## 6. 迹函数数值审计

| prime | order | exponents_a_b_c | smooth_lambda_count | max_abs_trace_over_sqrt_p | max_lambda | mean_abs_trace_over_sqrt_p | audit_only_not_proof |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `29` | `7` | `[1, 2, 3]` | `27` | `1.808777384271` | `13` | `0.803302696993` | `True` |
| `31` | `5` | `[1, 1, 2]` | `29` | `1.824506079915` | `2` | `0.812209083734` | `True` |
| `41` | `8` | `[1, 3, 2]` | `39` | `1.76817231105` | `12` | `0.811688812763` | `True` |
| `61` | `10` | `[1, 3, 4]` | `59` | `1.879807172183` | `28` | `0.84276852834` | `True` |

## 7. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousUnifiedSmoothRankTwoTargetActive` | `true` | `true` | 上一证书已把唯一剩余压成统一 smooth rank-two 迹界或 pivot。 | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `UnifiedSmoothRankTwoSheafContractAndConductorLedger` | `true` | `true` | 统一 smooth rank-two 迹函数已匹配为 lambda 线上秩二 lisse sheaf 合同。 | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `OrderFreeConductorLedgerClosed` | `true` | `true` | 秩、奇点数、导子依赖只随分支数有界，不依赖角色阶 d。 | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `DeligneKatzRankTwoTraceExternalMatch` | `true` | `true` | 若接受 Deligne/Katz 外部定理，rank-two 迹界接口已严格匹配。 | external route closed if accepted |
| `UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma` | `false` | `false` | 旧表述已收束为秩二 sheaf RH 或等价 Stepanov pivot 原子。 | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `RankTwoLisseSheafRHTraceBoundInternalizationLemma` | `false` | `false` | 作者侧自足路线仍需内部证明秩二 lisse sheaf 平方根迹界。 | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `ElementaryStepanovPivotForRankTwoTraceLemma` | `false` | `false` | 等价内部路线是直接构造秩二 Stepanov pivot 块。 | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma` | `false` | `false` | 唯一真正剩余：秩二 RH 迹界内部化或等价初等 Stepanov pivot。 | RankTwoRHOrElementaryPivot |
| `BoundedBranchSignatureHasseJetIndependenceLemma` | `false` | `false` | Hasse-jet 秩下界等待 rank-two pivot/RH 输入。 | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 完整阶无关 selector 等待 rank-two 输入作者侧闭合。 | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩仍等待完整 selector。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整内部证明仍未闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待 rank-two 输入作者侧闭合或外部接受。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只完成 sheaf 合同和外部匹配，不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 8. 下一最窄目标

```text
RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma
```

审稿边界：本证书完成 rank-two sheaf 合同、导子账本和外部 Deligne/Katz 匹配，
但没有给出作者侧自足 RH/Stepanov 证明；
因此不声明 Kummer 迹界、Burgess B4 或行/列命题作者侧无条件闭合。
