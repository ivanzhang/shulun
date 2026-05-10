# Prime Matrix strict RKS2/RKS3 Stepanov 秩签名前沿证书

**状态：** `stepanov_nonzero_rank_reduced_to_order_free_branch_signature_selector`

Stepanov-Kummer 非零秩输入继续缩窄。现在的硬点不再是笼统的辅助多项式存在性，而是一个阶无关的分支签名选择问题：必须在只允许常数依赖分支数 `m<=2r`、不允许依赖角色阶 `d` 的条件下，构造足够多的辅助函数签名，并证明 Hasse-jet 插值条件只造成 `O_m(TN)` 的秩损耗。本步闭合了三件事：把秩问题重定位到分支估值签名，排除使用整条 Kummer 曲线 `y^0,...,y^{d-1}` 全梯子的 d 依赖伪证明，并固定 Hasse-jet 条件的记账接口。唯一剩余变为 `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma`。未证明该签名选择引理前，Stepanov、Kummer 迹界、Weil 界、B4 和行/列命题仍不能作者侧无条件闭合。

```text
stepanov_rank_surjectivity_target_active=true
rank_gap_relocalized_to_branch_signatures=true
full_kummer_d_ladder_firewall_closed=true
branch_signature_normal_form_closed=true
hasse_jet_bookkeeping_closed=true
order_free_signature_selector_internalized=false
stepanov_kummer_auxiliary_rank_surjectivity_proved=false
row_column_unconditional_closed=false
```

## 1. 归一化秩问题

| field | value |
| --- | --- |
| `input` | branch divisor B={a_1,...,a_m}, signed exponents e_a, character order d, f not a d-th power |
| `auxiliary_space_goal` | construct a bounded-pole auxiliary space with dimension growing like c_m*D and rank loss O_m(T*N) |
| `forbidden_dimension_source` | do not use the full y^d=f(x) monomial ladder; it has d-dependent dimension/genus |
| `allowed_dimension_source` | use branch valuation signatures and Hasse derivatives whose constants depend only on m |
| `surjectivity_goal` | after imposing Hasse-jet vanishing conditions, a nonzero function remains on the Kummer eigenspace |

## 2. 分支签名正规形

| field | value |
| --- | --- |
| `valuation_signature` | sigma(g)=(ord_{a_1}(g),...,ord_{a_m}(g)) modulo local Kummer equivalence |
| `collision_rule` | two auxiliary monomials can collapse only if their signature difference is invisible at every branch place |
| `nonpower_anchor` | because f is not a d-th power, at least one branch coordinate carries a nonzero residue signature |
| `order_free_requirement` | the chosen signature family must have size and separation bounded below in terms of m, not d |
| `local_derivatives` | Hasse derivatives change local signatures by controlled bounded amounts, so jet conditions consume O_m(T) signatures per point |

## 3. 已闭合归约

| field | value |
| --- | --- |
| `rank_gap_relocalized` | the old nonzero-rank gate is now a finite branch-signature selector plus Hasse-jet independence problem |
| `d_ladder_firewall` | any proof using O(d) independent y-powers is rejected because it breaks Burgess uniformity |
| `jet_bookkeeping` | multiplicity T at N points consumes a predictable number of Hasse-jet linear conditions once a selector exists |
| `degree_bookkeeping_imported` | previous Stepanov degree/multiplicity contradiction applies after selector rank is available |

## 4. 当前真缺口

| field | value |
| --- | --- |
| `precise_atom` | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `selector_statement` | for every non-dth-power f with m branch places, find an order-free family of auxiliary signatures with rank >= c_m*D after all Kummer relations |
| `jet_statement` | the Hasse-jet evaluation matrix on that family has rank loss bounded by C_m*T*N |
| `why_not_closed_here` | the corpus still lacks a proof that such a selector exists uniformly for all exponent residue patterns e_a mod d |
| `if_proved` | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity closes, then the Kummer trace and Burgess B4 chain can continue |

## 5. 签名参数表

| r | branch_bound_m | signature_vector_length | rank_constant_may_depend_on | rank_constant_must_not_depend_on | next_selector_size |
| --- | --- | --- | --- | --- | --- |
| `5` | `10` | `10` | `m<=10` | `d,P,chi,branch_positions` | positive c_m*D after Hasse-jet losses |
| `9` | `18` | `18` | `m<=18` | `d,P,chi,branch_positions` | positive c_m*D after Hasse-jet losses |
| `17` | `34` | `34` | `m<=34` | `d,P,chi,branch_positions` | positive c_m*D after Hasse-jet losses |
| `26` | `52` | `52` | `m<=52` | `d,P,chi,branch_positions` | positive c_m*D after Hasse-jet losses |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `StepanovRankSurjectivityTargetActive` | `true` | `true` | 上一证书已把唯一剩余压成 Stepanov-Kummer 辅助空间非零秩。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `RankGapRelocalizedToBranchSignatures` | `true` | `true` | 非零秩问题已重定位为分支估值签名选择与 Hasse-jet 独立性。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `FullKummerDLadderFirewallClosed` | `true` | `true` | 已排除用 `y^0,...,y^{d-1}` 全梯子制造维数的 d 依赖路线。 | review firewall |
| `BranchSignatureNormalFormClosed` | `true` | `true` | 辅助函数的可区分性可由分支估值签名记录，碰撞只来自全分支不可见差。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `HasseJetBookkeepingClosed` | `true` | `true` | 一旦有阶无关签名族，Hasse-jet 条件的秩损耗可按 `O_m(TN)` 记账。 | BoundedBranchSignatureHasseJetIndependenceLemma |
| `OrderFreeKummerSignatureSelectorAndHasseJetRankLemma` | `false` | `false` | 仍需证明所有 exponent residue pattern 下都存在足够大的阶无关签名选择族。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity` | `false` | `false` | Stepanov-Kummer 非零秩等待签名选择与 Hasse-jet 秩引理。 | OrderFreeKummerSignatureSelectorAndHasseJetRankLemma |
| `StepanovAuxiliaryPolynomialRankBoundForKummerSums` | `false` | `false` | Stepanov 完整证明仍未作者侧闭合。 | StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity |
| `SelfContainedRankOneKummerSheafRHTraceBound` | `false` | `false` | 秩一 Kummer 迹界仍等待 Stepanov rank gate。 | StepanovAuxiliaryPolynomialRankBoundForKummerSums |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只把非零秩问题压成签名选择原子，不声明行/列命题无条件闭合。 | SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals |

## 7. 下一最窄目标

```text
OrderFreeKummerSignatureSelectorAndHasseJetRankLemma
```

审稿边界：本证书没有证明阶无关签名选择引理；
它只关闭秩问题的正规形、防 d 依赖误用和 Hasse-jet 记账接口。
