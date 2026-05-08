# Prime Matrix 独立 pre-Cauchy 算术来源恒等式分类路由器

**状态：** `independent_precauchy_identity_taxonomy_closed_actual_spread_open`

本步穷尽 IndependentPreCauchyArithmeticSourceIdentity 的合法来源类：canonical 来源只在 canonical 分支内闭合，generic WFD 来源被 moving-delta/防火墙阻断，APSourceLift 被对象账本拒绝，外部谱定理不能作为完全自足 pre-Cauchy source identity。剩余不再是新恒等式黑箱，而是 actual noncanonical moving-block spread/NC-BLK 数学输入；精确外部谱匹配仍留在条件分支。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
identity_taxonomy_closed=true
canonical_source_identity_blocked=true
generic_wfd_identity_rejected=true
ap_source_lift_rejected=true
external_spectral_self_contained_identity_proved=false
actual_moving_block_spread_proved=false
precisely_matched_external_spectral_accepted=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
terminal_gap_before_router=IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn
terminal_gap_after_router=ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
```

## 1. 分类律

```text
independent pre-Cauchy source identity
  in {canonical, generic_wfd, AP/external, actual_noncanonical}
canonical       -> scoped out of noncanonical clean-core
generic_wfd     -> rejected
AP/external     -> not self-contained source identity
actual_noncanonical -> moving-block spread / NC-BLK core
```

## 2. 替换律

```text
IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn
  =>
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn
```

该替换把独立来源恒等式黑箱并入已知终局二选一数学核心。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `IndependentPreCauchyIdentityGateActive` | `true` | `false` | 最新最窄点要求独立于早期零行覆盖图的 pre-Cauchy 算术来源恒等式。 | `分类它的所有合法来源类。` |
| `NoHiddenFourthRouteImported` | `true` | `true` | noncanonical full-S 补集合同已声明没有第四条可自足偷渡路线。 | `候选恒等式必须落入 canonical、generic、external/AP 或 actual-source 类。` |
| `CanonicalSourceIdentityBlockedForNoncanonical` | `true` | `true` | canonical RIW/Buchstab 来源只在 canonical 分支内闭合。 | `不能导入 noncanonical clean-core。` |
| `GenericWFDIdentityRejected` | `true` | `true` | generic WFD/source 模板已被 moving-delta 和来源防火墙阻断。 | `不能作为 pre-Cauchy source identity。` |
| `APSourceLiftRejected` | `true` | `true` | AP-source lift 是 source-level reclassification；non-AP clean-core 不能静默升级为 AP 源。 | `若走 AP/DI-BFI 必须新增 full-S theorem 或新 source identity。` |
| `ExternalSpectralNotSelfContainedSourceIdentity` | `true` | `true` | DI/BFI/Kuznetsov 处理 completion 后系数平均，不能生成 pre-Cauchy summand emitter。 | `它只能作为精确外部谱输入分支。` |
| `RemainingActualSourceCoreIdentified` | `true` | `true` | 所有伪来源恒等式删除后，自足数学核心与 moving-block spread/NC-BLK 汇合；外部谱只保留在条件分支。 | `ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn` |
| `IndependentPreCauchyIdentityTaxonomyClosed` | `true` | `true` | 独立来源恒等式的合法类别已穷尽；它不能成为新隐藏终端。 | `剩余是 actual moving-block spread/NC-BLK；精确外部谱输入保留在条件分支。` |
| `ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn` | `false` | `false` | 当前材料尚未证明 actual noncanonical moving-block spread/NC-BLK。 | `ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn` |
| `ExplicitModelGapAndFiniteDPRCLedger` | `true` | `false` | 模型余量/有限 DPRC 账本仍在输入基中，未由本步处理。 | `ExplicitModelGapAndFiniteDPRCLedger。` |
| `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` | `false` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | `DStructureRankinPromotionPackage。` |

## 4. 最新输入基

条件输入基：

```text
((ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn AND ExplicitModelGapAndFiniteDPRCLedger) OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn AND ExplicitModelGapAndFiniteDPRCLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

下一步最窄目标为 `ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn`：在假设早期零行反例分支中证明 actual same-(u,v) moving block 不能集中到足以支付零行；若改走外部条件分支，则必须精确匹配并接受 CDependent residue spectral input；否则给出命名 PDEC/SAE/ColumnCRT/CleanKLS 回流证书。
