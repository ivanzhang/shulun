# Prime Matrix strict RKS2/RKS3 标量塌缩 residue 矩阵证书

**状态：** `scalar_collapse_reduced_to_pure_quadratic_legendre_wronskian_nonzero`

本轮把三奇点标量塌缩剩余进一步算术化。设四个投影残基为 `a,b,c,delta`，其中 `delta=-(a+b+c)`。三处 lambda 奇点的标量塌缩对应 `a+c=0`、`b+c=0`、`c+delta=0` 三条线性同余。前两条给出 `a=b=-c`，代回 `delta` 得 `delta=c`，第三条给出 `2c=0`。在四可见支路中 `c` 非零，故唯一可能是 `d` 为偶数且 `a=b=c=delta=d/2`，即纯二次 Legendre 型。因此所有非二次残基标量塌缩通道被排除；当前唯一内部自足剩余压缩为 `PureQuadraticLegendreScalarCollapseExclusionLemma`：必须在不调用外部 Hasse/Deligne/Katz 的前提下，用 Legendre 二次特化的 Picard-Fuchs 或 Hasse-Wronskian 计算证明两维局部解不全局成比例。未完成该 Wronskian 非零原子前，pivot determinant、Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。

```text
three_singularity_residue_scalar_equation_matrix_closed=true
nonquadratic_residue_scalar_collapse_excluded=true
pure_quadratic_legendre_only_surviving_scalar_channel=true
pure_quadratic_legendre_scalar_collapse_excluded=false
rank_two_pivot_nonzero_determinant_proved=false
row_column_unconditional_closed=false
```

## 1. residue 标量矩阵

| field | value |
| --- | --- |
| `projective_residues` | a,b,c,delta with delta=-(a+b+c) modulo d |
| `normal_form` | x^a*(1-x)^b*(1-lambda*x)^c has infinity residue delta |
| `lambda_infinity_edge` | a+c == 0 mod d |
| `lambda_one_edge` | b+c == 0 mod d |
| `lambda_zero_edge` | c+delta == 0 mod d |
| `visibility` | a,b,c,delta are nonzero in the exact four-visible rank-two channel |

## 2. 符号推导

| field | value |
| --- | --- |
| `from_lambda_infinity` | a == -c |
| `from_lambda_one` | b == -c |
| `infinity_residue` | delta=-(a+b+c)==c after substituting a=b=-c |
| `from_lambda_zero` | c+delta==2c==0 |
| `visible_consequence` | c is nonzero of order two, so d is even and a=b=c=delta=d/2 |
| `closed_nonquadratic_case` | if the residue pattern is not pure quadratic, the all-three scalar collapse equations cannot hold |

## 3. 已接入防火墙

| field | value |
| --- | --- |
| `low_support` | support size <3 is already a PGL2 one-coordinate degeneration, not a rank-two scalar channel |
| `exact_three` | exactly three visible branches are Jacobi/Gauss and already closed |
| `four_branch_pairing` | four visible residues either have a Jacobi pair or reduce to pure quadratic Legendre |
| `legendre_status` | Legendre is not an independent gate, but its internal Wronskian nonzero proof is still needed here |

## 4. 唯一剩余 Legendre 原子

| field | value |
| --- | --- |
| `new_atom` | PureQuadraticLegendreScalarCollapseExclusionLemma |
| `new_subatom` | LegendrePicardFuchsHasseWronskianNonzeroLemma |
| `statement` | for the pure quadratic pattern a=b=c=delta=d/2, the Legendre rank-two local system is not globally scalar and has a nonzero Hasse-Wronskian pivot seed |
| `equivalent_curve_form` | E_lambda: y^2=x(1-x)(1-lambda*x), lambda not in {0,1} |
| `needed_internal_input` | derive the Picard-Fuchs/Hasse derivative relation and prove its two local solutions are not proportional |
| `why_this_is_narrower` | all non-quadratic residue scalar-collapse channels are now excluded by three linear congruences |
| `must_not_use` | external Hasse, Deligne, Katz irreducibility, or a finite point-count audit as a proof |

## 5. 禁止捷径

| field | value |
| --- | --- |
| `finite_audit` | the residue enumeration checks the congruence algebra only; it is not the proof of the Legendre Wronskian |
| `legendre_subsumed_means_closed` | previous subsumption removed Legendre as a separate trace gate, but did not prove this internal Wronskian |
| `generic_lambda` | lambda values with j=0 or j=1728 are smooth and still must be covered |
| `external_hasse` | the elliptic Hasse bound would close an external route, not this author-side pivot determinant route |

## 6. 有限一致性审计

| order | visible_scalar_solutions | sample_solutions | all_solutions_pure_quadratic |
| --- | --- | --- | --- |
| `2` | `1` | `[[1, 1, 1, 1]]` | `true` |
| `3` | `0` | `[]` | `true` |
| `4` | `1` | `[[2, 2, 2, 2]]` | `true` |
| `5` | `0` | `[]` | `true` |
| `6` | `1` | `[[3, 3, 3, 3]]` | `true` |
| `7` | `0` | `[]` | `true` |
| `8` | `1` | `[[4, 4, 4, 4]]` | `true` |
| `9` | `0` | `[]` | `true` |
| `10` | `1` | `[[5, 5, 5, 5]]` | `true` |
| `11` | `0` | `[]` | `true` |
| `12` | `1` | `[[6, 6, 6, 6]]` | `true` |
| `14` | `1` | `[[7, 7, 7, 7]]` | `true` |
| `16` | `1` | `[[8, 8, 8, 8]]` | `true` |
| `18` | `1` | `[[9, 9, 9, 9]]` | `true` |
| `20` | `1` | `[[10, 10, 10, 10]]` | `true` |
| `22` | `1` | `[[11, 11, 11, 11]]` | `true` |
| `24` | `1` | `[[12, 12, 12, 12]]` | `true` |
| `26` | `1` | `[[13, 13, 13, 13]]` | `true` |
| `28` | `1` | `[[14, 14, 14, 14]]` | `true` |
| `30` | `1` | `[[15, 15, 15, 15]]` | `true` |
| `32` | `1` | `[[16, 16, 16, 16]]` | `true` |
| `34` | `1` | `[[17, 17, 17, 17]]` | `true` |
| `36` | `1` | `[[18, 18, 18, 18]]` | `true` |
| `38` | `1` | `[[19, 19, 19, 19]]` | `true` |
| `40` | `1` | `[[20, 20, 20, 20]]` | `true` |
| `42` | `1` | `[[21, 21, 21, 21]]` | `true` |
| `44` | `1` | `[[22, 22, 22, 22]]` | `true` |
| `46` | `1` | `[[23, 23, 23, 23]]` | `true` |
| `48` | `1` | `[[24, 24, 24, 24]]` | `true` |
| `50` | `1` | `[[25, 25, 25, 25]]` | `true` |
| `52` | `1` | `[[26, 26, 26, 26]]` | `true` |
| `54` | `1` | `[[27, 27, 27, 27]]` | `true` |
| `56` | `1` | `[[28, 28, 28, 28]]` | `true` |
| `58` | `1` | `[[29, 29, 29, 29]]` | `true` |
| `60` | `1` | `[[30, 30, 30, 30]]` | `true` |
| `62` | `1` | `[[31, 31, 31, 31]]` | `true` |
| `64` | `1` | `[[32, 32, 32, 32]]` | `true` |
| `66` | `1` | `[[33, 33, 33, 33]]` | `true` |
| `68` | `1` | `[[34, 34, 34, 34]]` | `true` |
| `70` | `1` | `[[35, 35, 35, 35]]` | `true` |
| `72` | `1` | `[[36, 36, 36, 36]]` | `true` |
| `74` | `1` | `[[37, 37, 37, 37]]` | `true` |
| `76` | `1` | `[[38, 38, 38, 38]]` | `true` |
| `78` | `1` | `[[39, 39, 39, 39]]` | `true` |
| `80` | `1` | `[[40, 40, 40, 40]]` | `true` |

## 7. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousScalarCollapseTargetActive` | `true` | `true` | 上一证书已把唯一内部剩余压成三奇点 residue signature 标量塌缩排除。 | RankTwoScalarMonodromyCollapseExclusionLemma |
| `ThreeSingularityResidueScalarEquationMatrix` | `true` | `true` | 三处局部标量塌缩已写成 a+c、b+c、c+delta 三条线性同余。 | PureQuadraticLegendreScalarCollapseExclusionLemma |
| `LowSupportAndExactThreeFirewallImported` | `true` | `true` | 低支撑、exact-three、四分支配对与 Legendre 并入证书已作为防火墙接入。 | PureQuadraticLegendreScalarCollapseExclusionLemma |
| `NonQuadraticResidueScalarCollapseExcluded` | `true` | `true` | 三条标量同余强制 a=b=c=delta=d/2，因此所有非二次残基塌缩被排除。 | PureQuadraticLegendreScalarCollapseExclusionLemma |
| `PureQuadraticLegendreOnlySurvivingScalarChannel` | `true` | `true` | 唯一还能通过三条标量同余的模式是纯二次 Legendre 型。 | PureQuadraticLegendreScalarCollapseExclusionLemma |
| `PureQuadraticLegendreScalarCollapseExclusionLemma` | `false` | `false` | 仍需内部证明 Legendre 二次特化的 Picard-Fuchs/Hasse-Wronskian 非零。 | LegendrePicardFuchsHasseWronskianNonzeroLemma |
| `RankTwoScalarMonodromyCollapseExclusionLemma` | `false` | `false` | rank-two 标量塌缩排除等待纯二次 Legendre Wronskian 原子。 | PureQuadraticLegendreScalarCollapseExclusionLemma |
| `RankTwoPivotNonzeroDeterminant` | `false` | `false` | pivot 行列式非零等待标量塌缩排除。 | RankTwoScalarMonodromyCollapseExclusionLemma |
| `RankTwoElementaryStepanovPivotNonzeroDeterminantLemma` | `false` | `false` | 初等 rank-two Stepanov pivot 仍等待 determinant atom。 | RankTwoPivotNonzeroDeterminant |
| `ElementaryStepanovPivotForRankTwoTraceLemma` | `false` | `false` | rank-two trace 的内部 Stepanov pivot 尚未闭合。 | RankTwoPivotNonzeroDeterminant |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 完整阶无关 selector 仍等待 pivot 非零证明与下游粘合。 | RankTwoPivotNonzeroDeterminant |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩仍未闭合。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整内部证明仍未闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待内部 pivot/selector 链条闭合或外部路线被接受。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只排除非二次标量塌缩，不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 8. 下一最窄目标

```text
PureQuadraticLegendreScalarCollapseExclusionLemma
LegendrePicardFuchsHasseWronskianNonzeroLemma
```

审稿边界：本证书只排除非二次 residue 标量塌缩；
没有证明纯二次 Legendre Wronskian 非零，也没有声明 pivot、Stepanov、Kummer 迹界或行/列命题作者侧无条件闭合。
