# Prime Matrix strict RKS2/RKS3 rank-two Stepanov pivot 前沿证书

**状态：** `rank_two_internal_route_reduced_to_stepanov_pivot_determinant_nonvanishing`

本轮没有证明 rank-two 平方根迹界，但把作者侧内部路线从“RH 内部化或 Stepanov pivot”二选一继续压窄为一个明确的初等 Stepanov pivot 行列式原子。外部 Deligne/Katz 路线仍保持可接受则闭合；但完全自足路线现在锁定为：在 `U=P^1-{0,1,infinity}` 上构造固定秩二辅助块，使用有界 Hasse-jet 派生字母表，通过次数-重数矛盾推出 `sqrt(p)` 级抵消。次数账本与 jet 条件账本已经收束为 `O_m` 常数，不依赖角色阶 `d`，也不使用 `y^0,...,y^{d-1}` 维数来源。唯一真正剩余变成 `RankTwoElementaryStepanovPivotNonzeroDeterminantLemma`：证明这个固定 rank-two 辅助块的 pivot 行列式不恒为零，并覆盖所有光滑 lambda，包括 `j=0` 与 `j=1728`。未完成该行列式非零原子前，Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。

```text
internal_route_locked_to_elementary_stepanov_pivot=true
rank_two_stepanov_degree_multiplicity_ledger_closed=true
rank_two_hasse_jet_condition_ledger_closed=true
rank_two_pivot_nonzero_determinant_proved=false
elementary_stepanov_pivot_internalized=false
row_column_unconditional_closed=false
```

## 1. 内部路线锁定

| field | value |
| --- | --- |
| `old_two_way_atom` | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `rh_internalization` | proving rank-two lisse sheaf RH internally is essentially a full Weil/Deligne theorem route |
| `chosen_internal_route` | elementary Stepanov pivot on the rank-two trace function |
| `external_route_status` | Deligne/Katz remains a valid external closure if accepted |
| `why_lock` | to continue the self-contained author-side line without repeatedly toggling between external RH and internal pivot |

## 2. pivot 空间

| field | value |
| --- | --- |
| `trace_function` | T(lambda)=sum_x A(x)B(1-x)C(1-lambda*x) on U=P^1-{0,1,infinity} |
| `auxiliary_family` | bounded-degree functions in lambda and controlled logarithmic/Hasse derivatives along the three singular directions |
| `rank_two_constraint` | use only a fixed two-dimensional local solution space; do not introduce a d-length Kummer ladder |
| `vanishing_goal` | force high multiplicity at all lambda with large trace while keeping total divisor degree smaller than total forced zeros |
| `nonzero_goal` | prove the auxiliary determinant/pivot block is not identically zero |

## 3. 次数-重数账本

| field | value |
| --- | --- |
| `closed_part` | once a nonzero pivot exists, standard Stepanov degree-vs-multiplicity contradiction gives sqrt(p)-scale cancellation |
| `degree_growth` | degree grows as O_m(D) under the fixed rank-two derivative alphabet |
| `condition_count` | Hasse-jet vanishing consumes O_m(TN) linear conditions |
| `order_free` | all constants depend only on the fixed branch bound m and not on d |
| `remaining_dependency` | the only unproved input is determinant nonvanishing for the pivot block |

## 4. 行列式原子

| field | value |
| --- | --- |
| `new_atom` | RankTwoElementaryStepanovPivotNonzeroDeterminantLemma |
| `statement` | there exists a bounded rank-two Stepanov auxiliary block whose Hasse-jet evaluation determinant is not identically zero on U |
| `must_cover` | all smooth lambda, including j=0 and j=1728, and all nontrivial character triples already admitted by the sheaf contract |
| `must_avoid` | generic-position assumptions and any y^0,...,y^{d-1} dimension source |
| `if_proved` | rank-two trace bound internalizes, then the order-free selector and downstream Stepanov/Burgess chain can continue |
| `why_not_closed` | the corpus still lacks the determinant nonvanishing proof for the fixed rank-two derivative alphabet |

## 5. 禁止捷径

| field | value |
| --- | --- |
| `rh_as_internal` | do not count external Deligne/Katz as author-side internal proof |
| `dimension_by_d` | do not create auxiliary rank by using d Kummer powers |
| `generic_lambda` | the determinant must not vanish identically even at special smooth automorphism points |
| `numerical_pivot` | finite determinant audits may guide but cannot replace symbolic nonvanishing |

## 6. pivot 预算表

| branch_bound_m | rank_bound | singularities_on_lambda_line | allowed_constant_dependency | forbidden_dependency | pivot_unknown |
| --- | --- | --- | --- | --- | --- |
| `4` | `2` | `3` | `O_4(1)` | d, p, character order, branch positions | nonzero determinant only |
| `6` | `2` | `3` | `O_6(1)` | d, p, character order, branch positions | nonzero determinant only |
| `8` | `2` | `3` | `O_8(1)` | d, p, character order, branch positions | nonzero determinant only |
| `10` | `2` | `3` | `O_10(1)` | d, p, character order, branch positions | nonzero determinant only |

## 7. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousRankTwoRHOrPivotTargetActive` | `true` | `true` | 上一证书已把唯一剩余压成 rank-two RH 内部化或等价 Stepanov pivot。 | RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma |
| `InternalRouteLockedToElementaryStepanovPivot` | `true` | `true` | 作者侧自足主攻路线锁定为初等 Stepanov pivot，不再在内部证明中来回切换 RH 黑箱。 | RankTwoElementaryStepanovPivotNonzeroDeterminantLemma |
| `RankTwoStepanovDegreeMultiplicityLedger` | `true` | `true` | 非零 pivot 一旦存在，次数-重数矛盾账本已可按 O_m 常数运行。 | RankTwoElementaryStepanovPivotNonzeroDeterminantLemma |
| `RankTwoHasseJetConditionLedger` | `true` | `true` | Hasse-jet 条件消耗保持 O_m(TN)，不依赖角色阶 d。 | RankTwoElementaryStepanovPivotNonzeroDeterminantLemma |
| `RankTwoPivotNonzeroDeterminant` | `false` | `false` | 唯一未证的是固定 rank-two 派生字母表的 pivot 行列式非零。 | RankTwoElementaryStepanovPivotNonzeroDeterminantLemma |
| `RankTwoLisseSheafRHTraceBoundInternalizationOrElementaryStepanovPivotLemma` | `false` | `false` | 旧二选一原子已压成具体的 Stepanov pivot 行列式非零原子。 | RankTwoElementaryStepanovPivotNonzeroDeterminantLemma |
| `RankTwoElementaryStepanovPivotNonzeroDeterminantLemma` | `false` | `false` | 仍需证明秩二 Stepanov 辅助块存在非零行列式。 | RankTwoPivotDeterminantNonvanishing |
| `BoundedBranchSignatureHasseJetIndependenceLemma` | `false` | `false` | 全局 Hasse-jet 独立性等待 rank-two pivot 行列式非零。 | RankTwoElementaryStepanovPivotNonzeroDeterminantLemma |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 完整阶无关 selector 等待 rank-two pivot 非零证明。 | RankTwoElementaryStepanovPivotNonzeroDeterminantLemma |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩仍等待完整 selector。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整内部证明仍未闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待 rank-two pivot 作者侧闭合或外部接受。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只压窄内部原子，不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 8. 下一最窄目标

```text
RankTwoElementaryStepanovPivotNonzeroDeterminantLemma
```

审稿边界：本证书锁定内部 Stepanov pivot 路线并关闭次数/jet 账本，
但没有证明 pivot 行列式非零；
因此不声明 Kummer 迹界、Burgess B4 或行/列命题作者侧无条件闭合。
