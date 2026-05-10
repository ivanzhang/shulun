# Prime Matrix strict RKS2/RKS3 阶无关签名选择器前沿证书

**状态：** `order_free_selector_reduced_to_three_visible_branch_jet_pivot`

阶无关 Kummer 签名选择器没有整体闭合，但本轮把唯一内部自足剩余继续压窄：先把分支残基放到投影直线 P^1 上，证明可见支撑小于三的退化情形不需要 Stepanov selector。支撑为零是 d 次幂而被排除；投影支撑为一与除子次数零矛盾；投影支撑为二可经 PGL2 变成 `c*phi(x)^e*h(x)^d`，仿射完整和退化为 `F_p^*` 上的非平凡角色和删去至多 `O_m(1)` 个坐标值，因而只有 `O_m(1)` 边界项，常数不依赖角色阶 `d`。因此真正剩余从笼统的 `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` 缩成 `ThreeVisibleBranchOrderFreeJetPivotLemma`：只需处理至少三处投影可见分支的非退化残基图，构造阶无关 pivot 族并证明 Hasse-jet 秩下界。未完成该三分支 pivot 引理前，Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。

```text
previous_selector_target_active=true
projective_residue_support_normal_form_closed=true
projective_low_visible_support_exact_pgl2_closure_proved=true
selector_scope_restricted_to_three_visible_branches=true
order_free_signature_selector_internalized=false
stepanov_kummer_auxiliary_rank_surjectivity_proved=false
row_column_unconditional_closed=false
```

## 1. 投影支撑正规形

| field | value |
| --- | --- |
| `support_definition` | work on P^1 and include infinity; visible support S={v: ord_v(f) not congruent 0 mod d} |
| `degree_zero_constraint` | sum_v ord_v(f)=0, hence a non-dth-power residue pattern cannot have exactly one projective visible branch |
| `d_power_quotient` | multiplying f by a d-th power changes no character value and removes invisible branch coordinates |
| `constant_factor` | a nonzero constant only multiplies the complete character sum by chi(c), so it is irrelevant to the rank gate |
| `scope_gain` | the selector problem only needs projective visible support size at least three |

## 2. 低支撑精确闭合

| field | value |
| --- | --- |
| `support_size_0` | all residues vanish; this is a d-th power case and is excluded by the Kummer nonpower hypothesis |
| `support_size_1` | impossible on P^1 because the divisor degree is zero modulo d |
| `support_size_2` | after a PGL2 change sending the two visible branches to 0 and infinity, f=c*phi(x)^e*h(x)^d with e not congruent 0 mod d |
| `complete_sum` | on the regular affine locus the sum is a full nontrivial F_p^* character sum with at most O_m(1) PGL2 coordinate values deleted, hence O_m(1) |
| `order_free_status` | this closes the degenerate selector cases without using the y^0,...,y^{d-1} ladder and with constants independent of d |

## 3. 非退化剩余

| field | value |
| --- | --- |
| `old_atom` | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `new_atom` | ThreeVisibleBranchOrderFreeJetPivotLemma |
| `projective_support_condition` | \|S\|>=3 |
| `required_selector_output` | construct a bounded-pole pivot family of size >= c_m*D after Kummer relations, with c_m independent of d,P,chi and branch positions |
| `required_jet_output` | prove the Hasse-jet evaluation matrix on that pivot family loses at most C_m*T*N rank |
| `why_this_is_narrower` | all zero-, one-, and two-visible-branch residue patterns are now exact PGL2 degeneracies; only genuine three-branch interaction remains |
| `why_not_closed` | the corpus still lacks a uniform proof that three visible branch residues force an order-free pivot block for every residue pattern and every branch configuration |

## 4. 禁止捷径

| field | value |
| --- | --- |
| `support_count_only` | support size >=3 is necessary for the hard case but does not itself prove Hasse-jet rank independence |
| `generic_position` | the proof must allow collisions and special cross-ratios; it cannot assume branch positions are generic |
| `full_d_ladder` | using O(d) Kummer powers would reintroduce d-dependent genus/dimension and is still rejected |
| `finite_audit` | the finite PGL2 audit records the exact low-support map shape only; it is not used as empirical proof of the three-branch gate |

## 5. PGL2 低支撑覆盖审计

| prime | map | domain_size | image_size | missing_values | is_bijection_to_Fp_without_1 | max_fiber_size |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | (x-a)/(x-b), a=1, b=2 | `16` | `16` | `[]` | `True` | `1` |
| `29` | (x-a)/(x-b), a=1, b=2 | `28` | `28` | `[]` | `True` | `1` |
| `41` | (x-a)/(x-b), a=1, b=2 | `40` | `40` | `[]` | `True` | `1` |
| `53` | (x-a)/(x-b), a=1, b=2 | `52` | `52` | `[]` | `True` | `1` |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousSelectorTargetActive` | `true` | `true` | 上一证书的唯一剩余确认为阶无关 Kummer 签名选择器与 Hasse-jet 秩问题。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `ProjectiveResidueSupportNormalFormClosed` | `true` | `true` | 把有限分支残基提升到 P^1，并用 d 次幂商掉不可见坐标。 | closed |
| `ProjectiveLowVisibleSupportExactPGL2Closure` | `true` | `true` | 投影可见支撑小于三的退化情形由 PGL2 单坐标精确求和关闭。 | closed |
| `SelectorScopeRestrictedToThreeVisibleBranches` | `true` | `true` | 全局 selector 原子已缩窄为三可见分支以上的非退化 jet 枢轴问题。 | ThreeVisibleBranchOrderFreeJetPivotLemma |
| `ThreeVisibleBranchOrderFreeJetPivotLemma` | `false` | `false` | 仍需给出三可见分支下的阶无关 pivot 族和 Hasse-jet 独立性证明。 | ProjectiveResidueSupportExpansionOrJetPivotLemma |
| `BoundedBranchSignatureHasseJetIndependenceLemma` | `false` | `false` | Hasse-jet 记账接口已固定，但非退化 pivot 块的实际秩下界仍未证明。 | ProjectiveResidueSupportExpansionOrJetPivotLemma |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 低支撑退化已关闭，但完整阶无关 selector 还等待三分支 pivot 引理。 | ThreeVisibleBranchOrderFreeJetPivotLemma |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩仍等待完整 selector。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整内部证明仍未闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待 Stepanov rank gate。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只缩窄内部自足线，不声明行/列命题作者侧无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 7. 下一最窄目标

```text
ThreeVisibleBranchOrderFreeJetPivotLemma
```

审稿边界：本证书只闭合投影低支撑退化情形，
没有证明三可见分支的阶无关 pivot 引理；
因此不声明 Stepanov、Kummer 迹界或行/列命题作者侧无条件闭合。
