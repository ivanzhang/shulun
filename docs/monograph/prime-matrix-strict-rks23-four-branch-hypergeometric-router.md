# Prime Matrix strict RKS2/RKS3 四分支超几何前沿证书

**状态：** `four_branch_crossratio_reduced_to_rank_two_hypergeometric_trace_atom`

本轮没有证明完整四分支 pivot，但把四可见分支交比硬点进一步压成 rank-two 迹界原子。四个投影可见分支经 PGL2 可固定为 `0,1,∞,lambda`，函数化为 `c*x^a*(1-x)^b*(1-lambda*x)^c*h(x)^d`，所有位置自由度只剩一个交比 `lambda`。残基层面闭合了一个有限二分：若存在一对残基乘积非平凡，则可抽出 Jacobi 核 `J(A,B)`，把四分支和写成 `J(A,B)*H_lambda(A,B;C)`；若所有配对都平凡，则唯一例外是四个同一二次残基的 Legendre 交比核。于是当前真正剩余不再是自由的 d 阶梯 selector，而是 `RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma`：自足证明归一化二阶交比迹 `H_lambda` 以及纯二次 Legendre 核在所有特殊和一般 `lambda` 下统一有界，或给出等价的 order-free Stepanov pivot 块。未完成该 rank-two 输入前，Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。

```text
previous_four_visible_target_active=true
four_branch_pgl2_crossratio_normal_form_closed=true
four_branch_residue_pair_selector_closed=true
jacobi_kernel_extraction_closed=true
rank_two_crossratio_trace_bound_internalized=false
order_free_signature_selector_internalized=false
row_column_unconditional_closed=false
```

## 1. 四分支交比正规形

| field | value |
| --- | --- |
| `support` | exactly four projective visible branches after previous low-support and exact-three closures |
| `pgl2_normalization` | send three visible branches to 0, 1, infinity; the fourth is the cross-ratio parameter lambda not in {0,1} |
| `normal_form` | f(x)=c*x^a*(1-x)^b*(1-lambda*x)^c*h(x)^d |
| `visibility_conditions` | a,b,c,a+b+c are all nonzero modulo d, with infinity residue -(a+b+c) |
| `free_parameter` | all branch-position dependence is compressed into one cross-ratio lambda |

## 2. 残基配对二分

| field | value |
| --- | --- |
| `statement` | among four visible residues, either some pair has nontrivial product, or all pair products are trivial |
| `nontrivial_pair_case` | choose that pair as a Jacobi sqrt(p) kernel after a PGL2 relabeling |
| `exception` | if every pair product is trivial, then all four residues are the same order-two residue; this is the pure quadratic Legendre core |
| `why_order_free` | the dichotomy uses only four residues and does not depend on d, P, or branch positions |
| `closed_here` | the finite residue dichotomy is closed; the trace bound for the remaining rank-two core is not |

## 3. Jacobi 核抽取

| field | value |
| --- | --- |
| `sum` | S_lambda(A,B,C)=sum_x A(x)B(1-x)C(1-lambda*x) |
| `kernel` | when AB is nontrivial, J(A,B)=sum_x A(x)B(1-x) has size sqrt(p) |
| `normalized_trace` | H_lambda(A,B;C)=S_lambda(A,B,C)/J(A,B) |
| `remaining_bound` | prove \|H_lambda(A,B;C)\|<=C_m uniformly, including special cross-ratio collisions |
| `quadratic_core` | if every pair product is trivial, the remaining sum is the Legendre elliptic trace sum chi(x(1-x)(1-lambda*x)) |

## 4. 当前 rank-two 原子

| field | value |
| --- | --- |
| `old_atom` | FourVisibleBranchCrossRatioJetPivotLemma |
| `new_atom` | RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma |
| `rank_two_meaning` | the four-branch cross-ratio problem is now a normalized rank-two trace problem, not a free d-ladder rank problem |
| `required_trace_output` | uniform O_m(sqrt(p)) for S_lambda, or equivalently O_m(1) for normalized H_lambda |
| `required_pivot_output` | translate the same rank-two bound into an order-free pivot block with Hasse-jet loss O_m(TN) |
| `why_not_closed` | the corpus still lacks a self-contained proof of the rank-two cross-ratio trace bound in all special and generic lambda cases |

## 5. 禁止捷径

| field | value |
| --- | --- |
| `generic_lambda` | lambda cannot be assumed generic; lambda values with extra automorphisms must be included |
| `jacobi_only` | Jacobi closes the extracted kernel, not the normalized cross-ratio trace H_lambda |
| `elliptic_known_bound` | the pure quadratic Legendre case may be recognized as elliptic, but an internal trace proof is still required |
| `d_ladder` | using y^0,...,y^{d-1} remains forbidden because it reintroduces d-dependent constants |

## 6. 交比迹数值审计

| prime | order | lambda | residues_a_b_c_inf | pair_type | abs_sum_over_sqrt_p | abs_jacobi_ab | abs_sum_over_abs_jacobi_ab |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `4` | `3` | `[1, 1, 1, 1]` | has_nontrivial_pair_product | `0.0` | `4.123105625618` | `0.0` |
| `29` | `7` | `5` | `[1, 2, 3, 1]` | has_nontrivial_pair_product | `0.507421206116` | `5.385164807135` | `0.507421206116` |
| `31` | `5` | `3` | `[1, 1, 2, 1]` | has_nontrivial_pair_product | `1.04534896477` | `5.56776436283` | `1.04534896477` |
| `41` | `8` | `6` | `[1, 3, 2, 2]` | has_nontrivial_pair_product | `1.727004111506` | `6.403124237433` | `1.727004111506` |
| `43` | `2` | `7` | `[1, 1, 1, 1]` | pure_quadratic_all_pair_products_trivial | `1.219988562661` | `1.0` | `None` |

## 7. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousFourVisibleTargetActive` | `true` | `true` | 上一证书已把唯一剩余压到四可见分支交比 pivot。 | FourVisibleBranchCrossRatioJetPivotLemma |
| `FourBranchPGL2CrossRatioNormalFormClosed` | `true` | `true` | 四个投影可见分支已归一为 0、1、∞ 与一个交比参数 lambda。 | closed |
| `FourBranchResiduePairSelectorOrQuadraticCoreLemma` | `true` | `true` | 四个残基要么有非平凡 Jacobi 配对，要么落入纯二次 Legendre 核。 | RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma |
| `JacobiKernelExtractionForFourBranchCrossRatio` | `true` | `true` | 非平凡配对支路可抽出 sqrt(p) Jacobi 核，剩余为归一化二阶交比迹。 | RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma |
| `PureQuadraticLegendreCoreIsolated` | `true` | `true` | 所有配对平凡的例外被唯一定位为四个二次残基的 Legendre 交比核。 | RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma |
| `FourVisibleBranchCrossRatioJetPivotLemma` | `false` | `false` | 四分支 pivot 已正规化并抽核，但 rank-two 交比迹界仍未内部证明。 | RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma |
| `RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma` | `false` | `false` | 仍需自足证明归一化二阶超几何/Legendre 交比迹的统一有界性。 | RankTwoTraceBoundOrStepanovPivotBlock |
| `BoundedBranchSignatureHasseJetIndependenceLemma` | `false` | `false` | Hasse-jet 秩下界仍等待 rank-two 交比 pivot 块。 | RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 完整阶无关 selector 仍等待 rank-two 交比迹界或等价 pivot 证明。 | RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩仍等待完整 selector。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整内部证明仍未闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待 rank-two 交比输入内部化。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只关闭四分支正规形与 Jacobi 抽核，不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 8. 下一最窄目标

```text
RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma
```

审稿边界：本证书关闭四分支 PGL2 正规形、残基配对二分和 Jacobi 核抽取，
但没有证明 rank-two 交比迹界或完整 Stepanov selector；
因此不声明 Kummer 迹界、Burgess B4 或行/列命题作者侧无条件闭合。
