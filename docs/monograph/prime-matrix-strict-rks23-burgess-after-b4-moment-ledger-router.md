# Prime Matrix strict RKS2/RKS3 B4 后 Burgess 放大矩账本证书

**状态：** `burgess_pointwise_internalized_after_b4_moment_ledger_rks23_threshold_closed`

B4 闭合后，经典 Burgess 的剩余已不再是黑箱。本证书把 Pólya-Vinogradov/归纳启动、ab 移位平均、Hölder 三账本、Vinogradov 重数计数、B4 完全 2r 矩输入、以及 `A,B,r` 参数优化接成一条作者侧内部链，得到素模非主角色在 `|I|>=P^(1/4+epsilon_B)` 区间上的固定幂节省。结合已闭合薄包吸收，RKS23 四区间角色矩阈值门闭合。审稿边界仍保持清楚：这还不是行/列最终命题无条件闭合，下一步必须审查 RKS23 角色矩到行/列推广门是否已经全部登记。

```text
burgess_after_b4_target_active=true
b4_weil_complete_rational_sum_kernel_closed_author_side=true
self_contained_classical_burgess_proof_internalized=true
burgess_pointwise_input_internalized=true
thin_dyadic_packet_mass_absorption_proved=true
rks23_character_moment_closed_author_side_self_contained=true
row_column_unconditional_closed=false
```

## 1. 定理接口

| field | value |
| --- | --- |
| `modulus` | prime P |
| `character` | nonprincipal multiplicative character chi mod P |
| `interval` | any consecutive interval I, with a wrapping interval split into at most two intervals |
| `burgess_form` | \|sum_{n in I} chi(n)\| <= C_r \|I\|^(1-1/r) P^((r+1)/(4r^2)) (log P)^(1/r) |
| `large_interval_saving` | if \|I\|>=P^(1/4+epsilon_B), choose r with 1/(4r)<epsilon_B and obtain \|S_I\|<=\|I\| P^(-delta_B) for large P |
| `constant_discipline` | C_r and the lower threshold P_0(r) depend only on r, hence only on fixed epsilon_B |

## 2. 证明账本

| field | value |
| --- | --- |
| `B0_pv_induction_shell` | finite Fourier completion gives Polya-Vinogradov \|S\|<<P^(1/2)log P; trivial bound handles very short N; the middle range is handled by induction on N |
| `B1_interval_translation` | for H=AB<N, average S(M+ab,N) over 1<=a<=A,1<=b<=B; endpoint discrepancies are shorter sums and are absorbed by the induction majorant E(H) |
| `B2_vinogradov_shift_amplification` | after multiplying by a inverse mod P, the averaged sum becomes H^(-1) sum_x nu(x) sum_{b<=B} chi(x+b) |
| `B3_holder_and_vinogradov_count` | Holder gives V<=V1^(1-1/r)V2^(1/(2r))W^(1/(2r)); V1=AN and the standard congruence count gives V2<=C AN(AN/P+log^2 P) |
| `B4_complete_moment_import` | the previous selector-to-Kummer certificate supplies W<=C_r(B^r P+B^(2r)P^(1/2)) |
| `B5_parameter_choice` | take B about r P^(1/(2r)) and A about N/(C_r P^(1/(2r))); then H=AB is a fixed fraction of N and V/H has Burgess exponent (r+1)/(4r^2) |
| `B6_dyadic_uniformity` | all endpoint splits, dyadic labels and fixed packet choices add only constants or P^o(1), absorbed into a smaller delta_B for P>=P_0(epsilon_B) |

## 3. 矩公式

| field | value |
| --- | --- |
| `V_definition` | V=sum_x nu(x) \|sum_{1<=b<=B} chi(x+b)\| |
| `holder` | V<=V1^(1-1/r) V2^(1/(2r)) W^(1/(2r)) |
| `V1` | V1=sum_x nu(x)=AN |
| `V2` | V2=sum_x nu(x)^2<=C AN(AN/P+log^2 P) |
| `W` | W=sum_x \|sum_{1<=b<=B} chi(x+b)\|^(2r)<=C_r(B^r P+B^(2r)P^(1/2)) |
| `optimized_bound` | \|S(M,N)\|<=C_r N^(1-1/r) P^((r+1)/(4r^2))(log P)^(1/r) |

## 4. 指数表

| epsilon_B | chosen_r | condition | delta_B | positive |
| --- | --- | --- | --- | --- |
| `1/16` | `5` | `1/(4r)=1/20<epsilon_B` | `1/400` | `true` |
| `1/32` | `9` | `1/(4r)=1/36<epsilon_B` | `1/2592` | `true` |
| `1/64` | `17` | `1/(4r)=1/68<epsilon_B` | `1/18496` | `true` |
| `1/100` | `26` | `1/(4r)=1/104<epsilon_B` | `1/67600` | `true` |

## 5. 下游合并

| field | value |
| --- | --- |
| `large_packet` | Burgess pointwise saving now supplies the large side branch of the four-interval character moment |
| `thin_packet` | thin dyadic packet absorption was already closed by the registered endpoint side Cauchy floor certificate |
| `rks23_character_moment` | large plus thin branches close the RKS23 threshold dichotomy gate author-side |
| `not_row_column_yet` | the later promotion from RKS23 character moment to row/column theorem remains a separate audit gate |

## 6. 禁止捷径

| field | value |
| --- | --- |
| `no_external_burgess_black_box` | the certificate does not count classical Burgess as an imported theorem; it registers the internal proof ledger after B4 |
| `no_b4_reopen` | the complete rational-sum kernel remains imported from the selector-to-Kummer closure and is not re-proved here |
| `no_row_column_jump` | closing Burgess/RKS23 character moment is not identical to closing every row/column promotion gate |
| `no_empirical_input` | no finite runner or absence-of-counterexample audit is used as a proof input |

## 7. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BurgessAfterB4TargetActive` | `true` | `true` | 上一证书已闭合 B4，并把唯一 Burgess 剩余指向 B4 后放大矩账本。 | BurgessAmplificationMomentLedgerAfterB4KernelClosure |
| `B4_weil_complete_rational_sum_kernel` | `true` | `true` | 完全有理函数角色和内核已由 selector/Kummer/Stepanov 链闭合。 | imported closed |
| `PolyaVinogradovAndInductionShellClosed` | `true` | `true` | Pólya-Vinogradov 启动门、平凡短区间门和中区间归纳外壳已登记。 | closed |
| `BurgessVinogradovShiftAveragingClosed` | `true` | `true` | ab 移位平均和乘法反演把原区间和转成带权短移位和。 | closed |
| `HolderVinogradovMultiplicityCountClosed` | `true` | `true` | Hölder 与 `V1,V2,W` 三账本、以及 `V2` 的 Vinogradov 同余计数已闭合。 | closed |
| `CompleteMomentWBoundImportedAfterB4` | `true` | `true` | B4 给出 `W<=C_r(B^rP+B^(2r)P^(1/2))`。 | closed |
| `BurgessParameterOptimizationClosed` | `true` | `true` | 选择 `B~rP^(1/(2r))`, `A~N/(C_rP^(1/(2r)))` 得到经典 Burgess 指数。 | closed |
| `DyadicIntervalUniformConstantsClosed` | `true` | `true` | 环绕区间拆分、dyadic 包和多对数损耗均可由固定 `epsilon_B` 的 `delta_B` 吸收。 | closed |
| `SelfContainedClassicalBurgessProofWithUniformDyadicIntervalConstants` | `true` | `true` | 经典 Burgess 点态证明组件在 B4 后作者侧闭合。 | closed |
| `SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals` | `true` | `true` | 素模非主乘法角色在 `P^(1/4+epsilon_B)` 以上区间的点态幂节省闭合。 | closed |
| `BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment` | `true` | `true` | 大包 Burgess 与已闭合薄包吸收合并，RKS23 四区间角色矩阈值门闭合。 | closed |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本轮关闭 Burgess/RKS23 角色矩输入，但不自动关闭后续行/列推广与最终命题门。 | RKS23CharacterMomentToRowColumnPromotionGateAudit |

## 8. 下一最窄目标

```text
RKS23CharacterMomentToRowColumnPromotionGateAudit
```

审稿边界：本证书关闭 Burgess 点态和 RKS23 角色矩阈值门；
它仍不声明行/列命题作者侧无条件闭合。
