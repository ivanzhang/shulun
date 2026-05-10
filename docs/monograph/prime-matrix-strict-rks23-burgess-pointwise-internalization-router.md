# Prime Matrix strict RKS2/RKS3 Burgess 点态输入内部化边界证书

**状态：** `burgess_pointwise_input_strictly_matched_to_classical_burgess_internalization_frontier`

当前唯一内部自足线的真正剩余已精确压缩为经典 Burgess 点态角色和证明的内部化。所需大包输入与素模经典 Burgess 定理严格匹配：对任意非主角色和长度 `H>=P^(1/4+epsilon_B)` 的区间，Burgess 形式经 `1/(4r)<epsilon_B` 的参数选择给出 `|S|<=H P^(-delta_B)`。因此若接受经典 Burgess 作为外部已证定理，RKS23 大包与已闭合薄包可合并闭合；若要求作者侧完全自足，剩余不再是含糊的角色矩黑箱，而是 Burgess 放大、2r 矩能量账本、Weil 完全有理函数角色和界，以及区间/常数统一性的内部证明包。行/列命题仍未在作者侧无条件闭合。

```text
burgess_pointwise_target_active=true
thin_dyadic_packet_mass_absorption_proved=true
needed_input_matches_classical_burgess_prime_modulus=true
burgess_exponent_optimization_ledger_closed=true
external_classical_burgess_would_close_rks23_large_branch=true
burgess_pointwise_input_internalized=false
rks23_character_moment_closed_author_side_self_contained=false
row_column_unconditional_closed=false
```

## 1. 所需输入

| field | value |
| --- | --- |
| `modulus` | prime P |
| `character` | nonprincipal multiplicative character chi mod P; for prime P it is primitive |
| `interval` | any consecutive interval I in a dyadic packet; a wrapping interval splits into at most two ordinary intervals |
| `length_condition` | \|I\|>=P^(1/4+epsilon_B) |
| `required_bound` | \|sum_{n in I} chi(n)\| <= \|I\| P^(-delta_B) |
| `uniformity` | epsilon_B fixed; constants may depend on epsilon_B but not on P, chi, or the dyadic packet |

## 2. 经典 Burgess 对接

| field | value |
| --- | --- |
| `standard_form` | \|S_I(chi)\| <= C_r H^(1-1/r) P^((r+1)/(4r^2)) up to harmless log/P^o(1) loss |
| `choice_of_r` | choose integer r with 1/(4r)<epsilon_B |
| `saving_exponent` | if H>=P^(1/4+epsilon_B), then \|S\|/H <= C_r P^{-(epsilon_B-1/(4r))/r+o(1)} |
| `delta_choice` | after absorbing C_r and polylog losses for large P, take any delta_B < (epsilon_B-1/(4r))/r |
| `dyadic_packet_match` | packet intervals are ordinary intervals after at most a two-piece split, so the same bound applies |
| `large_branch_consequence` | four large sides give the character-moment saving already registered by the Burgess-threshold router |

## 3. 参数账本

| epsilon_B | chosen_r | delta_B | positive |
| --- | --- | --- | --- |
| `1/16` | `5` | `1/400` | `true` |
| `1/32` | `9` | `1/2592` | `true` |
| `1/64` | `17` | `1/18496` | `true` |
| `1/100` | `26` | `1/67600` | `true` |

## 4. 完全自足剩余

| atom | status |
| --- | --- |
| `B1_interval_completion_and_translation` | elementary normalization; must be written with endpoint/wrap constants |
| `B2_vinogradov_shift_amplification` | needs a self-contained lemma with A,B,r parameters and no hidden range loss |
| `B3_amplified_moment_energy_ledger` | needs the exact 2r-th moment expansion and collision-count bound |
| `B4_weil_complete_rational_sum_kernel` | needs the complete character-sum bound for non-perfect-power rational functions |
| `B5_parameter_optimization_and_dyadic_uniformity` | the exponent algebra is closed here; constants still depend on B2-B4 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BurgessPointwiseTargetActive` | `true` | `true` | 薄包分支已闭合，最新全局剩余确认为大包 Burgess 点态角色和输入。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |
| `NeededInputMatchesClassicalBurgessPrimeModulus` | `true` | `true` | 所需输入正是素模非主角色在长度 `P^(1/4+epsilon_B)` 以上区间的经典 Burgess 点态节省。 | classical Burgess theorem |
| `BurgessExponentOptimizationLedgerClosed` | `true` | `true` | 由经典 Burgess 形式选择 `1/(4r)<epsilon_B` 可得到固定正的 `delta_B`。 | closed algebra |
| `ExternalClassicalBurgessWouldCloseRKS23LargeBranch` | `true` | `true` | 若接受经典 Burgess 定理作为外部已证定理，则大包分支与已闭合薄包分支合并后闭合 RKS23 角色矩门。 | external theorem acceptance |
| `BurgessProofComponentsInternalized` | `false` | `false` | 仓库内尚未把 Burgess 的放大、矩估计与 Weil 完全和证明逐项写成自足证明。 | SelfContainedClassicalBurgessProofWithUniformDyadicIntervalConstants |
| `SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals` | `false` | `false` | 作者侧完全自足闭合仍需完成经典 Burgess 证明组件账本。 | BurgessAmplificationMomentWeilLedgerForLargeDyadicIntervals |
| `BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment` | `false` | `false` | 薄包已闭合；无外部 Burgess 或内部 Burgess 证明前，作者侧不声明该门无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只完成 Burgess 输入的严格匹配和内部化边界压缩，不声明行/列命题无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 6. 下一最窄攻击顺序

```text
B4_weil_complete_rational_sum_kernel
B2_vinogradov_shift_amplification
B3_amplified_moment_energy_ledger
B1_interval_completion_and_translation
B5_parameter_optimization_and_dyadic_uniformity
```

审稿边界：本证书闭合的是 Burgess 输入与经典定理形式的匹配和指数账本；
它不把经典 Burgess 证明本身登记为仓库内部自足证明。
