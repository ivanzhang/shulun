# Prime Matrix strict RKS2/RKS3 selector 到 Kummer 迹界闭合证书

**状态：** `global_selector_rank_and_kummer_trace_closed_after_rank_two_pivot_sync`

本轮把 rank-two pivot 输出同步回全局阶无关 Kummer selector。投影可见支撑小于三由 PGL2 退化防火墙关闭；精确三分支由 Gauss/Jacobi 恒等式关闭；四分支及以上由交比归一、Jacobi 核抽取和上一轮已闭合的 rank-two Stepanov pivot determinant 关闭。三支路覆盖所有投影可见支撑情形，且 Hasse-jet 损耗账本保持 `O_m(TN)`，所以 `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` 闭合。接入 Stepanov 非零秩、重数-次数、值类放大和参数账本后，秩一 Kummer 迹界、阶无关 Weil 有理函数角色和界、以及 Burgess B4 完全和内核同步闭合。当前新的内部自足剩余转为完整经典 Burgess 点态证明组件：放大、2r 矩能量、区间归一和常数统一。行/列命题仍未作者侧无条件闭合。

```text
rank_two_pivot_output_to_global_kummer_selector_synchronized=true
order_free_signature_selector_internalized=true
stepanov_kummer_auxiliary_rank_surjectivity_proved=true
stepanov_auxiliary_polynomial_rank_bound_proved=true
self_contained_kummer_trace_bound_internalized=true
self_contained_weil_bound_internalized=true
b4_weil_complete_rational_sum_kernel_closed_author_side=true
burgess_pointwise_input_internalized=false
row_column_unconditional_closed=false
```

## 1. selector 同步接口

| field | value |
| --- | --- |
| `old_atom` | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `old_subatom` | RankTwoPivotOutputToGlobalKummerSelectorSynchronization |
| `support_partition` | projective visible support is split into <=2, exact 3, and >=4/cross-ratio rank-two regions |
| `rank_two_pivot_input` | closed by the Legendre Wronskian closure certificate after scalar-collapse exclusion |
| `jet_loss` | imported from the HasseJetBookkeepingClosed certificate; losses are O_m(TN) |
| `constant_discipline` | all constants depend only on fixed branch bound m, not on d, P, chi, or branch positions |

## 2. 分支覆盖表

| selector_region | certificate | closure_mechanism | output |
| --- | --- | --- | --- |
| projective visible support size 0, 1, or 2 | order-free selector router | d-th-power exclusion, degree-zero contradiction, or PGL2 one-coordinate complete character sum | no rank-two pivot needed |
| exactly three projective visible branches | three-branch Jacobi router | PGL2 normal form 0,1,infinity and internal Gauss/Jacobi identity | sqrt(p) trace branch and selector branch closed |
| four or more visible branches after cross-ratio reduction | four-branch, rank-two pivot, Legendre Wronskian closure | Jacobi kernel extraction plus rank-two Stepanov pivot determinant nonzero | order-free rank-two pivot block with O_m Hasse-jet loss |

## 3. 下游闭合链

| field | value |
| --- | --- |
| `selector_to_rank` | selector plus Hasse-jet bookkeeping closes Stepanov-Kummer auxiliary rank surjectivity |
| `rank_to_stepanov` | rank surjectivity plus value-class, degree/multiplicity, and parameter ledgers closes Stepanov bound |
| `stepanov_to_kummer_trace` | Stepanov bound gives SelfContainedRankOneKummerSheafRHTraceBound |
| `kummer_trace_to_weil` | rank-one Kummer conductor ledger and trace formula give order-free Weil bound |
| `weil_to_b4` | Burgess complete rational-sum kernel B4 closes once the order-free Weil bound is internalized |

## 4. 新剩余 Burgess 组件

| field | value |
| --- | --- |
| `next_target` | SelfContainedClassicalBurgessProofWithUniformDyadicIntervalConstants |
| `next_subatom` | BurgessAmplificationMomentLedgerAfterB4KernelClosure |
| `already_closed_here` | B4 complete rational-sum kernel, the former Weil/Kummer terminal input |
| `still_needed` | classical Burgess interval proof components B1/B2/B3/B5 and dyadic uniform constants |
| `why_not_row_column_closed` | RKS23 Burgess pointwise input and later row/column promotion gates remain distinct certificates |
| `external_note` | accepting classical Burgess would close this next target externally, but this certificate stays author-side internal |

## 5. 禁止捷径

| field | value |
| --- | --- |
| `row_column_jump` | closing B4/Kummer trace is not the same as closing all Burgess pointwise and row/column promotion gates |
| `d_ladder` | the proof still rejects any dimension source using y^0,...,y^{d-1} |
| `external_burgess` | classical Burgess may be accepted externally, but is not counted as author-side internal closure here |
| `finite_audit` | no finite numerical audit is used as proof of selector or Kummer trace closure |

## 6. 既有 Burgess 前沿状态

| field | value |
| --- | --- |
| `burgess_pointwise_target_active` | True |
| `burgess_pointwise_input_internalized` | False |
| `next_direct_attack_target` | SelfContainedClassicalBurgessProofWithUniformDyadicIntervalConstants |
| `next_atomic_attack_target` | BurgessAmplificationMomentWeilLedgerForLargeDyadicIntervals |

## 7. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousPivotOutputTargetActive` | `true` | `true` | 上一证书已闭合 rank-two pivot determinant，并把剩余指向全局 selector 同步。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `LowVisibleSupportPGL2SelectorBranchClosed` | `true` | `true` | 投影可见支撑小于三的支路已由 PGL2 退化/非幂防火墙关闭。 | closed |
| `ExactThreeVisibleJacobiSelectorBranchClosed` | `true` | `true` | 精确三可见分支由内部 Gauss/Jacobi 恒等式关闭。 | closed |
| `FourVisibleCrossRatioRankTwoPivotBranchClosed` | `true` | `true` | 四分支及以上经交比归一和 rank-two pivot 输出关闭。 | closed |
| `RankTwoPivotOutputToGlobalKummerSelectorSynchronization` | `true` | `true` | 三个支路覆盖全部投影可见支撑情形，rank-two pivot 已同步回全局 selector。 | closed |
| `BoundedBranchSignatureHasseJetIndependenceLemma` | `true` | `true` | Hasse-jet 秩损耗账本已固定为 O_m(TN)。 | closed |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `true` | `true` | 阶无关 Kummer selector 与 Hasse-jet 秩引理闭合。 | closed |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `true` | `true` | selector 与 jet 账本推出 Stepanov-Kummer 辅助空间非零秩。 | closed |
| `StepanovMultiplicityDegreeContradictionLedger` | `true` | `true` | 重数-次数矛盾账本已从 Stepanov 前沿证书接入。 | closed |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `true` | `true` | 非零秩、值类接口、重数-次数和参数账本合并后闭合 Stepanov 证明。 | closed |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `true` | `true` | 秩一 Kummer 迹界由内部 Stepanov 证明闭合。 | closed |
| `SelfContainedWeilBoundForMultiplicativeCharacterRationalFunctions` | `true` | `true` | 导子账本与迹公式接入后，乘法角色有理函数 Weil 界作者侧闭合。 | closed |
| `B4_weil_complete_rational_sum_kernel` | `true` | `true` | Burgess 完全有理函数角色和内核 B4 闭合。 | closed |
| `SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals` | `false` | `false` | 完整 Burgess 点态证明仍需放大、矩账本、区间与常数统一组件。 | SelfContainedClassicalBurgessProofWithUniformDyadicIntervalConstants |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合 Kummer/Weil/B4 终端输入，但不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 8. 下一最窄目标

```text
SelfContainedClassicalBurgessProofWithUniformDyadicIntervalConstants
BurgessAmplificationMomentLedgerAfterB4KernelClosure
```

审稿边界：本证书闭合 selector、Stepanov-Kummer rank、Kummer 迹界、Weil/B4 终端输入；
但完整 Burgess 点态证明和行/列命题仍未作者侧无条件闭合。
