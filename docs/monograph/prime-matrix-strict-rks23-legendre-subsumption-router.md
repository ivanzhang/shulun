# Prime Matrix strict RKS2/RKS3 Legendre 并入证书

**状态：** `legendre_quadratic_core_subsumed_into_unified_smooth_rank_two_gate`

本轮没有证明统一 smooth rank-two 迹界，但消去了一个重复守门项：纯二次 Legendre 核不再作为独立缺口。对 `lambda notin {0,1}`，令 `L_lambda=sum_x chi(x(1-x)(1-lambda*x))`，光滑曲线 `E_lambda: y^2=x(1-x)(1-lambda*x)` 满足精确点数恒等式 `#E_lambda(F_p)=p+1+L_lambda`，因此 `a_p(lambda)=-L_lambda`。这说明 Legendre 核只是统一 smooth rank-two 交比迹界的二次特化；它不应再作为独立的第三个开放输入反复出现。当前唯一真正剩余压成 `UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma`：在光滑交比域 `lambda notin {0,1,infinity}` 上，自足证明统一 rank-two 迹界，或构造等价 order-free Stepanov pivot。未完成该统一输入前，Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。

```text
previous_smooth_rank_two_target_active=true
legendre_exact_pointcount_identity_closed=true
legendre_core_independent_gate_eliminated=true
unified_smooth_rank_two_trace_bound_internalized=false
order_free_signature_selector_internalized=false
row_column_unconditional_closed=false
```

## 1. 精确点数恒等式

| field | value |
| --- | --- |
| `quadratic_sum` | L_lambda=sum_x chi(x(1-x)(1-lambda*x)) |
| `curve` | E_lambda: y^2=x(1-x)(1-lambda*x), with lambda not in {0,1} |
| `point_count` | #E_lambda(F_p)=p+1+L_lambda |
| `trace_identity` | a_p(lambda)=p+1-#E_lambda(F_p)=-L_lambda |
| `meaning` | bounding the Legendre core is exactly the smooth elliptic trace subcase of the rank-two input |

## 2. 并入关系

| field | value |
| --- | --- |
| `old_split` | SmoothLegendreQuadraticCoreTraceInput + SmoothRankTwoHypergeometricTraceInput |
| `new_unified_gate` | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `legendre_role` | quadratic-character specialization of the same smooth cross-ratio trace problem |
| `not_independent` | Legendre no longer remains as a separate gate; it is carried by the unified smooth rank-two trace/pivot lemma |
| `not_claimed` | the Hasse/Stepanov trace bound itself is not proved in this certificate |

## 3. 统一剩余输入

| field | value |
| --- | --- |
| `trace_form` | prove \|sum_x A(x)B(1-x)C(1-lambda*x)\| <= C_m*sqrt(p) on the smooth lambda domain |
| `normalized_form` | equivalently prove the normalized rank-two trace H_lambda is O_m(1) |
| `pivot_form` | or construct an order-free Stepanov pivot block whose Hasse-jet losses are O_m(TN) |
| `domain` | lambda not in {0,1,infinity}, including j=0 and j=1728 smooth points |
| `constant_rule` | constants may depend on the fixed branch bound m, but not on d, p, chi, or branch positions |

## 4. 禁止捷径

| field | value |
| --- | --- |
| `separate_legendre_gate` | do not keep asking for Legendre as an independent third gate; it is a subcase of the unified smooth rank-two input |
| `pointcount_as_hasse` | the exact point-count identity is not a proof of the Hasse bound |
| `external_hasse_label` | labeling the curve elliptic is not enough for a self-contained route unless the trace bound is proved or accepted as an external lemma |
| `whole_kummer_curve` | the forbidden d-dependent Kummer curve route remains excluded |

## 5. 点数恒等式审计

| prime | lambda | smooth_lambda | legendre_sum | point_count | trace_p_plus_1_minus_points | identity_trace_equals_negative_sum | abs_sum_over_sqrt_p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `3` | `True` | `6` | `24` | `-6` | `True` | `1.455213750218` |
| `29` | `5` | `True` | `2` | `32` | `-2` | `True` | `0.371390676354` |
| `31` | `3` | `True` | `4` | `36` | `-4` | `True` | `0.718421208107` |
| `41` | `6` | `True` | `-2` | `40` | `2` | `True` | `0.312347523777` |
| `43` | `7` | `True` | `-8` | `36` | `8` | `True` | `1.219988562661` |
| `53` | `11` | `True` | `-6` | `48` | `6` | `True` | `0.824163383692` |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousSmoothRankTwoTargetActive` | `true` | `true` | 上一证书已把唯一剩余压到光滑 rank-two 交比域。 | SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma |
| `LegendreCoreExactEllipticPointCountIdentity` | `true` | `true` | 纯二次 Legendre 和与光滑椭圆曲线点数满足精确恒等式。 | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `LegendreCoreSubsumedIntoUnifiedRankTwoGate` | `true` | `true` | Legendre 核不再作为独立守门项，而是统一 smooth rank-two 输入的二次特化。 | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `SmoothLegendreQuadraticCoreTraceInput` | `true` | `true` | 该项作为独立缺口已消去；实际界仍由统一 rank-two 输入承担。 | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `SmoothRankTwoHypergeometricTraceInput` | `false` | `false` | 非二次与二次特化统一后，仍需证明 smooth rank-two 交比迹界。 | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma` | `false` | `false` | 旧的 smooth rank-two 表述已去掉独立 Legendre 分支，但统一迹界未证。 | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma` | `false` | `false` | 仍需自足证明统一 smooth rank-two 迹界，或给出等价 Stepanov pivot。 | UnifiedSmoothRankTwoTraceBoundOrPivot |
| `BoundedBranchSignatureHasseJetIndependenceLemma` | `false` | `false` | Hasse-jet 秩下界仍等待统一 smooth rank-two pivot 块。 | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 完整阶无关 selector 仍等待统一 smooth rank-two 输入。 | UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩仍等待完整 selector。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整内部证明仍未闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待统一 smooth rank-two 输入内部化。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只消去独立 Legendre 分支，不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 7. 下一最窄目标

```text
UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma
```

审稿边界：本证书只证明 Legendre 核的精确点数恒等式并消去独立分支，
没有证明统一 smooth rank-two 迹界或完整 Stepanov selector；
因此不声明 Kummer 迹界、Burgess B4 或行/列命题作者侧无条件闭合。
