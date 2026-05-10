# Prime Matrix strict RKS2/RKS3 Kummer sheaf-Weil 归约证书

**状态：** `rational_character_sum_reduced_to_order_free_rank_one_kummer_trace_bound`

Weil 输入的真正自足剩余继续缩窄。Burgess 完全和中的有理函数 `f=prod(x-a)^{e_a}` 不是 `d` 次幂时，目标不是整条 `y^d=f(x)` 曲线的属数界，因为那会带入角色阶 `d`；正确对象是秩一 Kummer sheaf `L_{chi(f)}` 或等价的 Stepanov 辅助多项式证明。其导子只由分支点数控制，在 2r 矩中 `cond<=2r+2`，所以一旦有秩一 Kummer RH/Stepanov 迹界，就得到阶无关的 `O_r(P^(1/2))`，从而关闭 B4。作者侧完全自足仍未完成；下一唯一硬点是 `SelfContainedRankOneKummerSheafRHTraceBound`，等价初等路线是 `StepanovAuxiliaryPolynomialRankBoundForKummerSums`。行/列命题仍未无条件闭合。

```text
weil_bound_target_active=true
rational_function_to_kummer_sheaf_reduction_closed=true
whole_kummer_curve_genus_hazard_closed=true
order_free_conductor_ledger_closed=true
external_kummer_sheaf_rh_would_close_weil_bound=true
self_contained_kummer_trace_bound_internalized=false
self_contained_weil_bound_internalized=false
row_column_unconditional_closed=false
```

## 1. 目标和

| field | value |
| --- | --- |
| `field` | F_P with P prime |
| `character` | nonprincipal multiplicative character chi of order d |
| `function` | f(x)=prod_a (x-a)^{e_a} from the Burgess complete kernel after collecting signed multiplicities |
| `nonpower_condition` | some e_a is not divisible by d, equivalently f is not a d-th power in F_P(x) |
| `branch_places` | B={a in P^1: ord_a(f) not congruent to 0 mod d} |
| `burgess_kernel_size` | for the 2r-th Burgess moment, \|B\|<=2r; infinity is unramified because numerator and denominator have equal degree |
| `needed_bound` | \|sum_x chi(f(x))\| <= C_r P^(1/2) with C_r independent of d and P |

## 2. 防误用边界

| field | value |
| --- | --- |
| `tempting_route` | use the smooth projective model of y^d=f(x) and Hasse-Weil for the whole curve |
| `problem` | the genus of the whole d-cover can grow like d*\|B\|, so the bound may carry a factor depending on d |
| `why_bad_for_burgess` | d can be as large as P-1, but Burgess needs a constant depending only on fixed r |
| `correct_route` | work on the chi-eigenspace/rank-one Kummer sheaf, or use Stepanov directly, so the conductor is O(\|B\|) |
| `firewall` | no future certificate may claim B4 closed from a whole-curve genus bound unless the d-dependence is removed |

## 3. 阶无关接口

| field | value |
| --- | --- |
| `rank` | 1 |
| `open_curve` | U=P^1 \ B |
| `sheaf` | L_{chi(f)} is the pullback of the Kummer sheaf by f |
| `nontriviality` | nonpower_condition makes the sheaf geometrically nonconstant |
| `conductor` | cond(L_{chi(f)}) <= \|B\|+2 <= 2r+2 in the Burgess kernel |
| `cohomology_shape` | H_c^0 and H_c^2 vanish for a geometrically nonconstant rank-one sheaf on U |
| `trace_formula` | sum_{x in U(F_P)} chi(f(x)) = -Tr(Frob_P \| H_c^1(U_bar,L_{chi(f)})) |
| `rh_trace_input` | all Frobenius eigenvalues on H_c^1 have absolute value P^(1/2) |
| `consequence` | \|sum chi(f(x))\| <= dim H_c^1 * P^(1/2) <= O_r(P^(1/2)) |

## 4. 导子表

| r | max_branch_places_m | rank_one_conductor_bound | trace_bound_shape | depends_on_character_order_d |
| --- | --- | --- | --- | --- |
| `5` | `10` | `12` | `O(12*P^(1/2))` | `false` |
| `9` | `18` | `20` | `O(20*P^(1/2))` | `false` |
| `17` | `34` | `36` | `O(36*P^(1/2))` | `false` |
| `26` | `52` | `54` | `O(54*P^(1/2))` | `false` |

## 5. Stepanov 入口

| field | value |
| --- | --- |
| `goal` | prove the same O_r(P^(1/2)) bound without importing l-adic language |
| `auxiliary_polynomial` | construct a low-degree polynomial in x and the Kummer values whose many zeros force the desired estimate |
| `rank_condition` | monomials modulo the Kummer relation must remain independent up to the selected degree window |
| `multiplicity_ledger` | zeros at the large value set are counted with controlled multiplicity and bounded by total degree |
| `current_gap` | the auxiliary polynomial rank/surjectivity lemma is not yet written in the corpus |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `WeilBoundTargetActive` | `true` | `true` | 上一证书已把 B4 唯一剩余压成乘法角色有理函数 Weil 平方根界。 | SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions |
| `RationalFunctionToKummerSheafReductionClosed` | `true` | `true` | Burgess 内核的非幂有理函数和已归约为秩一 Kummer sheaf 的迹和。 | rank-one Kummer sheaf |
| `WholeKummerCurveGenusHazardClosed` | `true` | `true` | 已排除整条 `y^d=f(x)` 曲线 Hasse-Weil 直接闭合的 d 依赖误用。 | review firewall |
| `OrderFreeConductorLedgerClosed` | `true` | `true` | 导子只由分支点数控制，Burgess 2r 矩中 `cond<=2r+2`，与角色阶 d 无关。 | conductor ledger |
| `TraceFormulaInterfaceClosed` | `true` | `true` | 迹公式接口已固定：目标和等于 `H_c^1` 上 Frobenius 迹。 | SelfContainedRankOneKummerSheafRHTraceBound |
| `ExternalKummerSheafRHWouldCloseWeilBound` | `true` | `true` | 若接受秩一 Kummer sheaf 的 RH/Weil 迹界，则得到所需 `O_r(P^(1/2))`。 | external sheaf RH or classical Stepanov-Weil |
| `SelfContainedKummerTraceBoundInternalized` | `false` | `false` | 仓库内尚未给出该 RH/Stepanov 迹界的完整内部证明。 | SelfContainedRankOneKummerSheafRHTraceBound |
| `SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions` | `false` | `false` | 作者侧完全自足版仍需证明秩一 Kummer sheaf RH 迹界或等价 Stepanov 引理。 | SelfContainedRankOneKummerSheafRHTraceBound |
| `B4_weil_complete_rational_sum_kernel` | `false` | `false` | B4 作者侧闭合等待 Kummer 迹界内部化；接受外部 Weil/Stepanov 时可关闭。 | SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合 Weil 输入的正确阶无关归约，不声明行/列命题无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 7. 下一最窄目标

```text
SelfContainedRankOneKummerSheafRHTraceBound
StepanovAuxiliaryPolynomialRankBoundForKummerSums
```

审稿边界：本证书关闭的是有理函数角色和到阶无关 Kummer 迹界的归约，
并排除整曲线属数带来的 d 依赖误用；它尚未证明 Kummer RH/Stepanov 迹界本身。
