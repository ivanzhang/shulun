# Prime Matrix strict RKS2/RKS3 三分支 Jacobi 前沿证书

**状态：** `exact_three_visible_branch_closed_by_internal_jacobi_gauss`

本轮没有闭合完整阶无关 selector，但关闭了当前最窄线中的精确三可见分支支路。若投影可见支撑正好为三，经 PGL2 可归一到 0、1、∞，函数写成 `c*x^a*(1-x)^b*h(x)^d`，其中 `a,b,a+b` 均非零模 `d`。于是主和是 Jacobi 和 `J(chi^a,chi^b)`；用内部 Gauss/Jacobi 恒等式 `J(A,B)=G(A)G(B)/G(AB)` 与 `|G(Psi)|=sqrt(p)` 得到 `sqrt(p)` 界，不可见奇点只贡献 `O_m(1)`。该证明只用角色正交，不用整条 Kummer 曲线的 d 阶梯。因此真正剩余从三可见分支 pivot 缩为四可见分支交比 pivot：必须利用第四分支的交比自由度，构造常数只依赖 `m` 的 pivot 块并证明 Hasse-jet 秩下界。未完成四分支 pivot 前，Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。

```text
previous_three_visible_target_active=true
exact_three_visible_pgl2_normal_form_closed=true
internal_gauss_jacobi_identity_closed=true
exact_three_visible_branch_trace_bound_closed=true
selector_scope_restricted_to_four_visible_branches=true
order_free_signature_selector_internalized=false
row_column_unconditional_closed=false
```

## 1. 精确三分支正规形

| field | value |
| --- | --- |
| `visible_support` | exactly three projective visible places |
| `pgl2_normalization` | send the three visible places to 0, 1, infinity |
| `residue_condition` | f is represented by c*x^a*(1-x)^b*h(x)^d with a,b,a+b nonzero modulo d |
| `invisible_places` | zeros and poles of h only delete O_m(1) affine points and do not affect the conductor constant |
| `order_free_feature` | the reduction depends on support size 3, not on the character order d |

## 2. 内部 Gauss/Jacobi 恒等式

| field | value |
| --- | --- |
| `characters` | A=chi^a, B=chi^b, with A, B, and AB all nontrivial |
| `jacobi_sum` | J(A,B)=sum_x A(x)B(1-x) |
| `gauss_relation` | J(A,B)=G(A)G(B)/G(AB) |
| `gauss_magnitude` | \|G(Psi)\|=sqrt(p) for every nontrivial multiplicative character Psi |
| `consequence` | \|J(A,B)\|=sqrt(p), plus O_m(1) deleted invisible/singular points |
| `self_contained_inputs` | multiplicative/additive character orthogonality and one-line Gauss norm calculation |

## 3. 链条影响

| field | value |
| --- | --- |
| `closed_case` | exactly three projective visible branches no longer needs the Stepanov selector gate |
| `old_frontier_split` | ThreeVisibleBranchOrderFreeJetPivotLemma = exact-three Jacobi branch + four-or-more visible branch pivot branch |
| `new_frontier` | FourVisibleBranchCrossRatioJetPivotLemma |
| `new_required_output` | after fixing 0,1,infinity, use at least one remaining cross-ratio branch to build an order-free pivot block and prove Hasse-jet rank loss O_m(TN) |
| `not_claimed` | the four-or-more branch pivot and full selector are not proved here |

## 4. 禁止捷径

| field | value |
| --- | --- |
| `jacobi_overextension` | Jacobi/Gauss closes only exact three visible branches; it does not bound arbitrary four-branch rational character sums |
| `generic_cross_ratio` | the four-branch proof must include special cross-ratio collisions and cannot assume generic branch positions |
| `d_ladder` | the y^0,...,y^{d-1} ladder remains forbidden because it makes constants depend on d |
| `audit` | finite Jacobi audits are consistency checks only; the proof object is the Gauss/Jacobi identity |

## 5. Jacobi 恒等式数值审计

| prime | order | checked_nontrivial_pairs | sqrt_prime | max_abs_jacobi | max_abs_error | identity_shape_verified |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `4` | `6` | `4.123105625618` | `4.123105625618` | `8.882e-16` | `True` |
| `29` | `7` | `30` | `5.385164807135` | `5.385164807135` | `1.776e-15` | `True` |
| `31` | `5` | `12` | `5.56776436283` | `5.56776436283` | `2.665e-15` | `True` |
| `41` | `8` | `42` | `6.403124237433` | `6.403124237433` | `2.665e-15` | `True` |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousThreeVisibleTargetActive` | `true` | `true` | 上一证书已把 selector 硬点压到至少三处投影可见分支。 | ThreeVisibleBranchOrderFreeJetPivotLemma |
| `ExactThreeVisiblePGL2NormalFormClosed` | `true` | `true` | 精确三可见分支可由 PGL2 固定到 0、1、∞，残基化为 Jacobi 型。 | ExactThreeVisibleBranchJacobiGaussClosure |
| `InternalGaussJacobiIdentityClosed` | `true` | `true` | 用角色正交和 Gauss 和范数给出 \|J(A,B)\|=sqrt(p)，常数不依赖 d。 | ExactThreeVisibleBranchJacobiGaussClosure |
| `ExactThreeVisibleBranchJacobiGaussClosure` | `true` | `true` | 精确三可见分支 trace 支路闭合，只留下 O_m(1) 奇点删项。 | closed |
| `SelectorScopeRestrictedToFourVisibleBranches` | `true` | `true` | 剩余 selector 问题已进一步缩窄到至少四处投影可见分支。 | FourVisibleBranchCrossRatioJetPivotLemma |
| `ThreeVisibleBranchOrderFreeJetPivotLemma` | `false` | `false` | 原三分支及以上表述已拆分；exact-three 已闭合，但 four-or-more pivot 仍未证明。 | FourVisibleBranchCrossRatioJetPivotLemma |
| `FourVisibleBranchCrossRatioJetPivotLemma` | `false` | `false` | 仍需利用第四分支交比构造阶无关 pivot 块并证明 Hasse-jet 秩下界。 | CrossRatioPivotBlockIndependenceLemma |
| `BoundedBranchSignatureHasseJetIndependenceLemma` | `false` | `false` | Hasse-jet 记账接口仍等待四分支 pivot 块实际秩下界。 | FourVisibleBranchCrossRatioJetPivotLemma |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 完整阶无关 selector 仍等待四分支交比 pivot 引理。 | FourVisibleBranchCrossRatioJetPivotLemma |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩仍等待完整 selector。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整内部证明仍未闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待四分支 selector/Stepanov rank gate。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只关闭 exact-three 退化支路，不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 7. 下一最窄目标

```text
FourVisibleBranchCrossRatioJetPivotLemma
```

审稿边界：本证书关闭 exact-three Jacobi 支路，
但没有证明四可见分支交比 pivot 或完整 Stepanov selector；
因此不声明 Kummer 迹界、Burgess B4 或行/列命题作者侧无条件闭合。
