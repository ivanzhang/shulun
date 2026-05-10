# Prime Matrix strict RKS2/RKS3 Burgess-Weil 内核对角证书

**状态：** `burgess_weil_kernel_shape_and_power_diagonal_ledger_closed_weil_bound_remains`

Burgess 内部化的首个最窄原子已继续压缩：完整和内核、非幂判据、以及幂型异常对角的 `O_r(A^r)` 计数都可在仓库内部自足写清。因此 B4 不再是一个模糊黑箱；它只剩一个标准但深的点：对非 `d` 次幂有理函数的乘法角色完全和证明 Weil 平方根界。若接受该 Weil 界作为外部已证定理，则 Burgess 的完整和矩估计 `V<=C_r(A^rP+A^(2r)P^(1/2))` 闭合；若坚持作者侧完全自足，下一唯一硬点就是把有限域有理函数角色和 Weil 界本身内部化。行/列命题仍未在作者侧无条件闭合。

```text
b4_weil_kernel_attack_active=true
burgess_complete_kernel_shape_closed=true
dth_power_criterion_closed=true
exceptional_power_tuple_dimension_bound_closed=true
conditional_complete_moment_bound_closed_if_weil=true
external_weil_bound_would_close_b4=true
self_contained_weil_bound_internalized=false
b4_weil_complete_rational_sum_kernel_closed_author_side=false
row_column_unconditional_closed=false
```

## 1. 完整和内核

| field | value |
| --- | --- |
| `character_order` | d=ord(chi)>=2 because chi is nonprincipal |
| `tuple_variables` | u=(u_1,...,u_r), v=(v_1,...,v_r) from the amplifier shift set |
| `complete_kernel` | K_chi(u,v)=sum_x chi(prod_i (x+u_i)/prod_j (x+v_j)), omitting denominator zeros |
| `signed_multiplicity` | e_a=#{i:u_i=a}-#{j:v_j=a} |
| `d_power_criterion` | the rational function is a d-th power in F_P(x) iff d divides e_a for every a |
| `nonpower_case` | if some e_a is not divisible by d, the kernel is a genuine nonpower rational character sum |

## 2. 异常对角账本

| field | value |
| --- | --- |
| `exceptional_condition` | d divides every signed multiplicity e_a |
| `dimension_reason` | every distinct value used by an exceptional tuple occupies at least two of the 2r signed slots |
| `free_value_bound` | number of distinct values <= r |
| `tuple_count` | for any shift interval of length A, exceptional tuples are O_r(A^r) |
| `exceptional_contribution` | their complete sums are bounded trivially by P, giving O_r(A^r P) |
| `nonexceptional_contribution_if_weil` | Weil gives O_r(P^(1/2)) per tuple, hence O_r(A^(2r) P^(1/2)) |

## 3. 条件矩估计

| field | value |
| --- | --- |
| `moment` | V=sum_x \|sum_{a in A} chi(x+a)\|^(2r) |
| `expansion` | V=sum_{u,v} K_chi(u,v) |
| `bound_if_weil_available` | V <= C_r (A^r P + A^(2r) P^(1/2)) |
| `role_in_burgess` | this is the complete-sum moment input needed before Vinogradov shifting and parameter optimization |
| `not_yet_unconditional_author_side` | the square-root nonpower estimate still rests on the finite-field Weil bound unless proved internally |

## 4. 异常维度表

| r | positions | free_values_bound | exceptional_tuple_bound | bell_digits |
| --- | --- | --- | --- | --- |
| `5` | `10` | `5` | `Bell(10)*A^5` | `6` |
| `9` | `18` | `9` | `Bell(18)*A^9` | `12` |
| `17` | `34` | `17` | `Bell(34)*A^17` | `29` |
| `26` | `52` | `26` | `Bell(52)*A^26` | `50` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `B4WeilKernelAttackActive` | `true` | `true` | 上一证书给出的首个内部化原子正是 Burgess 完全有理函数角色和内核。 | B4_weil_complete_rational_sum_kernel |
| `BurgessCompleteKernelShapeClosed` | `true` | `true` | 2r 矩展开后的完整和已精确化为 `K_chi(u,v)`。 | kernel formula |
| `DthPowerCriterionClosed` | `true` | `true` | `prod(x+u_i)/prod(x+v_j)` 为 `d` 次幂当且仅当所有签名重数 `e_a` 被 `d` 整除。 | finite algebra ledger |
| `ExceptionalPowerTupleDimensionBoundClosed` | `true` | `true` | 幂型异常元组至多有 `r` 个自由值，因此数量为 `O_r(A^r)`。 | diagonal ledger |
| `ConditionalCompleteMomentBoundClosedIfWeil` | `true` | `true` | 一旦非幂内核有 Weil 平方根界，即得 `V<=C_r(A^rP+A^(2r)P^(1/2))`。 | SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions |
| `ExternalWeilBoundWouldCloseB4` | `true` | `true` | 若接受有限域有理函数乘法角色和 Weil 界作为外部已证定理，则 B4 完整闭合。 | external Weil theorem |
| `SelfContainedWeilBoundInternalized` | `false` | `false` | 仓库内尚未把该 Weil 界本身的曲线/RH 证明写成自足证明。 | SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions |
| `B4_weil_complete_rational_sum_kernel` | `false` | `false` | 作者侧完全自足闭合还差非幂有理函数角色和的 Weil 平方根界。 | SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions |
| `BurgessProofComponentsInternalized` | `false` | `false` | B4 尚未作者侧自足闭合，后续 B2/B3/B1 也仍需逐项登记。 | BurgessAmplificationMomentWeilLedgerForLargeDyadicIntervals |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合的是 Burgess-Weil 内核代数和异常对角账本，不声明行/列命题无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 6. 下一最窄目标

```text
SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions
```

审稿边界：本证书没有把 Weil 界本身登记为作者侧自足证明；
它只关闭 Burgess 完全和内核的代数分类、异常对角计数和条件矩估计接口。
