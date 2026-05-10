# Prime Matrix strict RKS2/RKS3 Stepanov-Kummer 迹界前沿证书

**状态：** `rank_one_kummer_trace_bound_reduced_to_stepanov_auxiliary_rank_surjectivity`

秩一 Kummer 迹界的初等内部化路线继续缩窄为 Stepanov 辅助多项式的秩/非零问题。本步已经把目标标准化为分支数 `m<=2r` 的阶无关平方根界，并把 Stepanov 路线拆成六包：值类放大、辅助空间、插值条件、秩非零、重数-次数矛盾、参数优化。其中值类接口、重数-次数账本和常数不依赖角色阶 `d` 的纪律已经固定。唯一真正剩余不再是笼统 Weil/RH，而是 `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity`：必须证明所选辅助函数空间在 Kummer 关系与导数条件下仍有足够非零秩。未证明该秩引理前，作者侧不能声明 Kummer 迹界、Weil 界、B4 或行/列命题无条件闭合。

```text
kummer_trace_target_active=true
stepanov_problem_normalization_closed=true
stepanov_package_decomposition_closed=true
stepanov_multiplicity_degree_ledger_closed=true
stepanov_auxiliary_rank_surjectivity_internalized=false
self_contained_kummer_trace_bound_internalized=false
self_contained_weil_bound_internalized=false
row_column_unconditional_closed=false
```

## 1. 标准化目标

| field | value |
| --- | --- |
| `input` | P prime, nonprincipal chi, f in F_P(x), f not a d-th power for d=ord(chi) |
| `branch_count` | m=\|{places where ord_a(f) not congruent to 0 mod d}\| <= 2r |
| `target` | \|sum_x chi(f(x))\| <= C_m P^(1/2) |
| `constant_discipline` | C_m may depend on fixed m but not on d, P, chi, or the root positions |
| `already_closed` | Burgess kernel formula, d-th-power criterion, exceptional diagonal, Kummer conductor ledger |

## 2. Stepanov 六包

| package | role |
| --- | --- |
| `S1_value_class_amplification` | large character-sum bias forces one coset/value class of the Kummer torsor to contain P/d + Omega(P^(1/2)) excess after a standard Fourier inversion |
| `S2_auxiliary_space` | choose an auxiliary function space on P^1 with poles only at the branch divisor B and bounded order depending on m |
| `S3_interpolation_conditions` | impose vanishing to multiplicity T at every point in the overlarge value class |
| `S4_nonzero_rank_surjectivity` | prove the interpolation map has a nonzero kernel element not identically zero on the Kummer eigenspace |
| `S5_degree_multiplicity_contradiction` | a nonzero auxiliary function cannot have more forced zeros than its pole degree permits |
| `S6_parameter_optimization` | choose degree and multiplicity parameters so the contradiction starts at excess > C_m P^(1/2) |

## 3. 当前真缺口

| field | value |
| --- | --- |
| `precise_gap` | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `why_it_is_the_real_gap` | dimension counting alone is not enough; the chosen auxiliary functions must remain nonzero after Kummer/eigenspace relations and derivative conditions |
| `forbidden_shortcut` | do not count all monomials on y^d=f(x) with d-dependent dimension; this reintroduces the forbidden character-order dependence |
| `needed_statement` | for every non-dth-power f with m branch places, there is a Stepanov auxiliary space of dimension > imposed conditions and rank loss O_m(1) |
| `output_if_proved` | SelfContainedRankOneKummerSheafRHTraceBound=true |

## 4. 重数-次数账本

| field | value |
| --- | --- |
| `pole_budget` | auxiliary functions have pole divisor degree O_m(D) |
| `zero_budget` | multipity T at N selected points forces at least T*N zeros |
| `contradiction_condition` | T*N > O_m(D) |
| `parameter_shape` | take D,T on the P^(1/2) scale after the rank lemma supplies a nonzero auxiliary function |
| `closed_here` | only the bookkeeping shape is fixed; the nonzero rank lemma is still the bottleneck |

## 5. 参数表

| r | branch_bound_m | target_constant_shape | rank_space_must_depend_on | forbidden_dependence | compatible_with_burgess |
| --- | --- | --- | --- | --- | --- |
| `5` | `10` | `C(10)` | `m only` | `character_order_d` | `true` |
| `9` | `18` | `C(18)` | `m only` | `character_order_d` | `true` |
| `17` | `34` | `C(34)` | `m only` | `character_order_d` | `true` |
| `26` | `52` | `C(52)` | `m only` | `character_order_d` | `true` |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `KummerTraceTargetActive` | `true` | `true` | 上一证书已把唯一剩余压成秩一 Kummer RH/Stepanov 迹界。 | SelfContainedRankOneKummerSheafRHTraceBound |
| `StepanovProblemNormalizationClosed` | `true` | `true` | 目标已标准化为分支数 `m<=2r`、常数只依赖 m 的乘法角色和平方根界。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `StepanovPackageDecompositionClosed` | `true` | `true` | Stepanov 路线已拆成值类放大、辅助空间、插值条件、秩非零、重数-次数和参数优化六包。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `ValueClassAmplificationInterfaceClosed` | `true` | `true` | 若角色和超过 `C_m P^(1/2)`，可转成某个 Kummer 值类的过量点集。 | standard finite Fourier inversion |
| `StepanovMultiplicityDegreeContradictionLedger` | `true` | `true` | 一旦存在非零辅助函数，重数-次数矛盾账本给出平方根级阈值。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `StepanovParameterShapeClosed` | `true` | `true` | 参数只允许依赖分支数 m，已排除角色阶 d 进入常数。 | parameter ledger |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | 仍需证明辅助函数空间在 Kummer 关系和导数条件下有足够非零秩。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整证明等待秩/非零引理。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界作者侧仍未完全内部化。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions` | `false` | `false` | 有理函数 Weil 界等待 Kummer/Stepanov 迹界内部化。 | SelfContainedRankOneKummerSheafRHTraceBound |
| `B4_weil_complete_rational_sum_kernel` | `false` | `false` | B4 仍等待 Weil/Kummer/Stepanov 终端输入；接受外部定理时可关闭。 | SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只关闭 Stepanov 路线的精确拆包和参数边界，不声明行/列命题无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 7. 下一最窄目标

```text
StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity
```

审稿边界：本证书没有证明 Stepanov 秩/非零引理；
它只把 Kummer 迹界的初等路线压缩到这个单一秩输入，并固定常数不得依赖角色阶 d。
