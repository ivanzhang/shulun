# Prime Matrix strict RKS2/RKS3 rank-two 奇异边界证书

**状态：** `rank_two_trace_restricted_to_smooth_crossratio_domain`

本轮没有证明 rank-two 交比迹界，但把其中的 lambda 边界完全剥离。四分支归一化后的交比参数只需考虑 `lambda notin {0,1,infinity}`：`lambda=0,1,∞` 都是分支碰撞，支撑降到至多三处，已由低支撑和 exact-three Jacobi 支路关闭。对纯二次 Legendre 核 `y^2=x(1-x)(1-lambda*x)`，判别式为 `lambda^2(1-lambda)^2`；因此 `lambda notin {0,1}` 时曲线光滑。`j=0`、`j=1728` 只表示额外自同构，不是新奇异边界，不能再作为未处理特殊情形。所以唯一剩余从含糊的“所有特殊和一般 lambda”压成 `SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma`：在光滑交比域上自足证明 rank-two 迹界，或构造等价的 order-free Stepanov pivot 块。未完成该光滑 rank-two 输入前，Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。

```text
previous_rank_two_target_active=true
crossratio_singular_lambda_firewall_closed=true
special_automorphism_lambda_smoothness_firewall_closed=true
rank_two_crossratio_trace_bound_internalized=false
order_free_signature_selector_internalized=false
row_column_unconditional_closed=false
```

## 1. 奇异 lambda 防火墙

| field | value |
| --- | --- |
| `crossratio_domain` | lambda belongs to P^1 minus {0,1,infinity} after PGL2 normalization |
| `lambda_0` | the fourth branch collides with 0; support drops to at most three and is already closed by low-support/Jacobi routers |
| `lambda_1` | the fourth branch collides with 1; support drops to at most three and is already closed |
| `lambda_infinity` | after relabeling, infinity collision is the same support-drop case |
| `consequence` | rank-two trace input only needs smooth lambda not in {0,1,infinity} |

## 2. 光滑性证书

| field | value |
| --- | --- |
| `legendre_core` | y^2=x(1-x)(1-lambda*x) |
| `discriminant` | Delta(lambda)=lambda^2*(1-lambda)^2 up to a nonzero square factor |
| `smooth_condition` | Delta(lambda)!=0, exactly lambda not in {0,1,infinity} |
| `j_invariant` | j(lambda)=256*(1-lambda+lambda^2)^3/(lambda^2*(1-lambda)^2) |
| `special_automorphism_points` | j=0 and j=1728 are smooth when lambda not in {0,1}; they do not create new singular gates |

## 3. rank-two 剩余范围

| field | value |
| --- | --- |
| `old_atom` | RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma |
| `new_atom` | SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma |
| `closed_boundary` | all branch-collision lambda values are routed back to already closed <=3 visible-branch cases |
| `remaining_legendre` | prove the smooth Legendre quadratic core trace bound for every lambda not in {0,1} |
| `remaining_hypergeometric` | prove the smooth rank-two hypergeometric trace bound for every lambda not in {0,1} |
| `remaining_equivalent_pivot` | or construct an order-free Stepanov pivot block on the same smooth lambda domain |

## 4. 禁止捷径

| field | value |
| --- | --- |
| `special_j_as_exception` | j=0 and j=1728 may increase automorphisms but are not singular and cannot be left as separate unclosed cases |
| `lambda_zero_one` | lambda=0 or 1 must not be counted inside rank-two; they are support-drop cases already closed upstream |
| `finite_audit` | the audit confirms the symbolic discriminant pattern but is not used as proof of the trace bound |
| `hasse_weil_whole_kummer` | do not return to the full y^d=f(x) curve; the remaining input is rank-two and order-free |

## 5. lambda 奇异性审计

| prime | singular_lambdas | smooth_count | expected_smooth_count | j_zero_smooth_lambdas | j_1728_smooth_lambdas | all_special_points_smooth |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `[0, 1]` | `15` | `15` | `[]` | `[2, 9, 16]` | `True` |
| `29` | `[0, 1]` | `27` | `27` | `[]` | `[2, 15, 28]` | `True` |
| `31` | `[0, 1]` | `29` | `29` | `[6, 26]` | `[2, 16, 30]` | `True` |
| `41` | `[0, 1]` | `39` | `39` | `[]` | `[2, 21, 40]` | `True` |
| `43` | `[0, 1]` | `41` | `41` | `[7, 37]` | `[2, 22, 42]` | `True` |
| `53` | `[0, 1]` | `51` | `51` | `[]` | `[2, 27, 52]` | `True` |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousRankTwoTargetActive` | `true` | `true` | 上一证书已把唯一剩余压成 rank-two 交比迹界内部化。 | RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma |
| `CrossRatioSingularLambdaReductionFirewall` | `true` | `true` | lambda=0,1,∞ 都是分支碰撞，回到已闭合的低支撑/三分支支路。 | closed |
| `SpecialAutomorphismLambdaSmoothnessFirewall` | `true` | `true` | j=0 与 j=1728 只是光滑特殊自同构点，不再作为独立未闭合边界。 | closed |
| `RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma` | `false` | `false` | rank-two 输入已去掉奇异 lambda 边界，但光滑迹界本身仍未内部证明。 | SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma |
| `SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma` | `false` | `false` | 仍需在光滑 lambda 域证明 rank-two 交比迹界，或给出等价 Stepanov pivot。 | SmoothRankTwoTraceBoundOrPivot |
| `SmoothLegendreQuadraticCoreTraceInput` | `false` | `false` | 纯二次 Legendre 核仍需要光滑椭圆迹界的自足证明。 | SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma |
| `SmoothRankTwoHypergeometricTraceInput` | `false` | `false` | 非二次归一化超几何核仍需要 rank-two 迹界的自足证明。 | SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma |
| `BoundedBranchSignatureHasseJetIndependenceLemma` | `false` | `false` | Hasse-jet 秩下界仍等待光滑 rank-two pivot 块。 | SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 完整阶无关 selector 仍等待光滑 rank-two 输入。 | SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩仍等待完整 selector。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整内部证明仍未闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待光滑 rank-two 输入内部化。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只剥离奇异 lambda 边界，不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 7. 下一最窄目标

```text
SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma
```

审稿边界：本证书只剥离奇异 lambda 与特殊自同构伪边界，
没有证明光滑 rank-two 迹界或完整 Stepanov selector；
因此不声明 Kummer 迹界、Burgess B4 或行/列命题作者侧无条件闭合。
