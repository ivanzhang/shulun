# Prime Matrix strict RKS2/RKS3 Legendre Wronskian 闭合证书

**状态：** `pure_quadratic_legendre_scalar_collapse_closed_by_picard_fuchs_wronskian`

本轮闭合纯二次 Legendre 标量塌缩。对 `E_lambda: y^2=x(1-x)(1-lambda*x)`，内部微分计算给出 Picard-Fuchs 方程 `lambda(1-lambda)F''+(1-2lambda)F'-F/4=0`。其 Wronskian 满足 `W'=-(1-2lambda)/(lambda(1-lambda))*W`，故 `W=C/(lambda(1-lambda))`。在 `lambda=0` 的 Frobenius 基中存在一个全纯周期和一个对数伴随解，所以 `C!=0`；清除 `lambda(1-lambda)` 后得到非零 Hasse-Wronskian 种子，奇点只在 `0,1,infinity`。这排除了上一轮剩下的纯二次 Legendre 全局标量塌缩；结合非二次 residue 塌缩已排除，rank-two 标量塌缩通道为空，固定 rank-two pivot determinant 非零支路闭合。但全局阶无关 Kummer selector、Stepanov-Kummer 非零秩、Kummer 迹界和行/列命题仍需后续粘合，本证书不声明行/列命题作者侧无条件闭合。

```text
legendre_picard_fuchs_equation_derived=true
legendre_picard_fuchs_hasse_wronskian_nonzero_proved=true
pure_quadratic_legendre_scalar_collapse_excluded=true
rank_two_scalar_monodromy_collapse_excluded=true
rank_two_pivot_nonzero_determinant_proved=true
elementary_stepanov_pivot_internalized=true
order_free_signature_selector_internalized=false
row_column_unconditional_closed=false
```

## 1. Picard-Fuchs 推导

| field | value |
| --- | --- |
| `family` | E_lambda: y^2=x*(1-x)*(1-lambda*x), lambda not in {0,1} |
| `period_form` | omega=dx/y |
| `normalized_period` | F(lambda)=2F1(1/2,1/2;1;lambda) |
| `differential_equation` | lambda*(1-lambda)*F'' + (1-2*lambda)*F' - F/4 = 0 |
| `internal_inputs` | differentiate omega under the integral sign and reduce dx/y powers modulo d(x/y) |
| `bad_characteristics` | only characteristic 2 is excluded; the quadratic-character branch is over odd primes |

## 2. Wronskian 闭合

| field | value |
| --- | --- |
| `standard_form` | F'' + P(lambda)*F' + Q(lambda)*F=0 |
| `P(lambda)` | (1-2*lambda)/(lambda*(1-lambda)) |
| `wronskian_equation` | W'=-P(lambda)*W |
| `explicit_solution` | W=C/(lambda*(1-lambda)) |
| `nonzero_constant` | the Frobenius basis at lambda=0 has one holomorphic period and one logarithmic companion, so C!=0 |
| `hasse_wronskian` | after clearing lambda*(1-lambda), the seed is the nonzero constant C; modulo odd p it remains nonzero |

## 3. 标量塌缩排除

| field | value |
| --- | --- |
| `previous_residue_reduction` | all non-quadratic scalar-collapse residue patterns are already excluded |
| `surviving_pattern` | a=b=c=delta=d/2, the pure quadratic Legendre pattern |
| `contradiction` | a globally scalar rank-two block would have zero Wronskian, but Picard-Fuchs gives W=C/(lambda*(1-lambda)) with C!=0 |
| `scope` | all smooth lambda, including j=0 and j=1728; only lambda=0,1,infinity are singular and already firewalled |
| `consequence` | the scalar-collapse channel is empty, so the fixed rank-two pivot determinant is nonzero |

## 4. 下游边界

| field | value |
| --- | --- |
| `closed_now` | pure quadratic Legendre scalar collapse, rank-two scalar collapse, and pivot determinant nonzero |
| `imported_ledgers` | degree/multiplicity and Hasse-jet condition ledgers from the prior Stepanov pivot certificate |
| `next_frontier` | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `why_not_row_column_closed` | the global order-free selector/rank-surjectivity and Burgess-to-row-column promotion gates are still separate |
| `no_external_blackbox` | this step uses the explicit Picard-Fuchs/Wronskian calculation, not Deligne/Katz/Hasse as a black box |

## 5. 禁止捷径

| field | value |
| --- | --- |
| `pointcount_only` | the earlier point-count identity does not by itself prove the Wronskian nonzero; the Picard-Fuchs equation is used here |
| `finite_audit` | Hasse polynomial samples are consistency checks only |
| `external_hasse` | elliptic Hasse-Weil is not counted as this internal proof |
| `generic_lambda` | special smooth automorphism points are included because W has poles only at 0,1,infinity |

## 6. Wronskian 恒等式机检

| field | value |
| --- | --- |
| `equation` | lambda*(1-lambda)*y'' + (1-2*lambda)*y' - y/4 = 0 |
| `standard_form_P` | (1-2*lambda)/(lambda*(1-lambda)) |
| `candidate_wronskian` | 1/(lambda*(1-lambda)) |
| `cleared_denominator` | lambda^2*(1-lambda)^2 |
| `left_numerator_W_prime` | 2*lambda-1 |
| `right_numerator_minus_PW` | 2*lambda-1 |
| `identity_verified` | True |

## 7. Hasse 多项式有限审计

| prime | degree_m | constant | leading | derivative_nonzero | hasse_polynomial_nonzero |
| --- | --- | --- | --- | --- | --- |
| `3` | `1` | `1` | `1` | `true` | `true` |
| `5` | `2` | `1` | `1` | `true` | `true` |
| `7` | `3` | `1` | `1` | `true` | `true` |
| `11` | `5` | `1` | `1` | `true` | `true` |
| `13` | `6` | `1` | `1` | `true` | `true` |
| `17` | `8` | `1` | `1` | `true` | `true` |
| `19` | `9` | `1` | `1` | `true` | `true` |
| `23` | `11` | `1` | `1` | `true` | `true` |
| `29` | `14` | `1` | `1` | `true` | `true` |
| `31` | `15` | `1` | `1` | `true` | `true` |

## 8. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousPureQuadraticLegendreTargetActive` | `true` | `true` | 上一证书已把唯一内部剩余压成纯二次 Legendre Wronskian 非零。 | PureQuadraticLegendreScalarCollapseExclusionLemma |
| `LegendrePicardFuchsEquationDerived` | `true` | `true` | Legendre 族周期满足显式 Picard-Fuchs 方程。 | LegendrePicardFuchsHasseWronskianNonzeroLemma |
| `LegendrePicardFuchsHasseWronskianNonzeroLemma` | `true` | `true` | Wronskian 为 C/(lambda*(1-lambda)) 且 C 非零，故两维局部解不全局成比例。 | closed |
| `PureQuadraticLegendreScalarCollapseExclusionLemma` | `true` | `true` | 纯二次 Legendre 标量塌缩被 Picard-Fuchs Wronskian 排除。 | closed |
| `RankTwoScalarMonodromyCollapseExclusionLemma` | `true` | `true` | 非二次 residue 塌缩已排除，纯二次支路本步关闭，因此 rank-two 标量塌缩为空。 | closed |
| `RankTwoPivotNonzeroDeterminant` | `true` | `true` | 由上一正规形：无标量塌缩则固定 rank-two pivot 行列式非零。 | closed |
| `RankTwoElementaryStepanovPivotNonzeroDeterminantLemma` | `true` | `true` | 结合已关闭的次数/重数和 Hasse-jet 账本，rank-two 初等 pivot 支路闭合。 | closed |
| `ElementaryStepanovPivotForRankTwoTraceLemma` | `true` | `true` | rank-two trace 的初等 Stepanov pivot 已由 determinant 非零支路闭合。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 下一步需要把已得 rank-two pivot 输出同步到全局阶无关 Kummer selector/jet-rank 门。 | RankTwoPivotOutputToGlobalKummerSelectorSynchronization |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩仍等待完整 selector。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | 全局 Stepanov 证明仍未全部作者侧闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待 selector/rank-surjectivity 全局粘合。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步关闭 pivot determinant 支路，但不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 9. 下一最窄目标

```text
OrderFreeKummerSignatureSelectorAndHasseJetRankLemma
RankTwoPivotOutputToGlobalKummerSelectorSynchronization
```

审稿边界：本证书闭合纯二次 Legendre Wronskian 与 rank-two pivot determinant 支路；
但全局 selector、Stepanov-Kummer rank、Kummer 迹界和行/列命题仍未作者侧无条件闭合。
