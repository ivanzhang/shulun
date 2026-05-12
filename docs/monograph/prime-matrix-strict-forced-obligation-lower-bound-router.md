# Prime Matrix strict 边界帽 forced obligation 下界路由器

**状态：** `forced_obligation_lower_bound_reduced_to_residual_mass_and_no_quotient_collapse_open`

`BoundaryCapForcedFormalUnitObligationLowerBound` 继续下钻后，必须区分两种量。早期零行与 CLB/no-loss 账本已经给出残洞到加权 obligation 的注入：残洞不会被删除，重复和复用也只能作为 quotient/reuse/weighted return 保留。但类型压缩需要的是可和 row-free type alphabet 比较的有效不同实例数。当前还缺边界残洞质量下界，以及防止 quotient/reuse 把大量残洞塌缩成少数类型的 anti-collapse 证明。行/列命题仍未无条件闭合。

```text
clb_residual_to_weighted_obligation_injection_closed=true
no_loss_weighted_accounting_imported=true
boundary_residual_mass_lower_bound_proved=false
no_quotient_collapse_below_type_threshold_proved=false
effective_distinct_type_instance_lower_bound_proved=false
boundary_cap_forced_obligation_lower_bound_proved=false
direct_unconditional_contradiction_found=false
row_column_unconditional_closed=false
```

## 1. 下界拆分

拆分前：

```text
BoundaryCapForcedFormalUnitObligationLowerBound
```

拆分后：

```text
BoundaryResidualMassLowerBoundForTypeCompression AND NoQuotientCollapseBelowTypeThreshold
```

## 2. 质量转移律

| law | formula | status |
| --- | --- | --- |
| `residual_hole_forcing` | EarlyZeroRowWithinP => each c in R_x has at least one covering label obligation. | `conditional_closed_as_weighted_injection` |
| `no_loss_partition` | O(w)=SourceRecords disjoint_union NamedReturnRecords, Lost(O)=empty. | `closed` |
| `weighted_reuse_not_erasure` | duplicate coordinates become quotient/reuse/weighted returns, not deleted obligations. | `closed` |
| `unweighted_instance_gap` | weighted mass lower bound does not imply enough distinct row-free type instances without anti-collapse. | `open` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ForcedLowerBoundInputActive` | `true` | `false` | 上一层把类型压缩的第一缺口定为边界帽 forced obligation 下界。 | BoundaryCapForcedFormalUnitObligationLowerBound |
| `CLBResidualEqualityImported` | `true` | `true` | 早期零行假设下 CLB 把残洞集合压成必须被补洞支付的对象。 | 需要把残洞数量转成类型压缩可用的有效实例数。 |
| `NoLossWeightedObligationImported` | `true` | `true` | 覆盖义务不会丢失；普通来源、命名回流、quotient/reuse 均保留在 O(w) 中。 | 这给加权质量守恒，不给未加权不同类型数量。 |
| `CarryCollarRigidityImported` | `true` | `true` | 残洞支付必须满足 carry-shell 与 anchor-collar 短纤维刚性。 | 刚性可限制类型，但具体计数尚未证明。 |
| `WeightedResidualHoleInjectionClosed` | `true` | `true` | 每个残洞至少贡献一个加权 obligation；重复或复用只能作为加权/quotient return 保留。 | CLBResidualHoleToWeightedObligationInjection |
| `BoundaryResidualMassLowerBoundCurrentCorpusProved` | `false` | `false` | 尚未给出足以压过 row-free type alphabet 的边界残洞质量下界。 | BoundaryResidualMassLowerBoundForTypeCompression |
| `NoQuotientCollapseCurrentCorpusProved` | `false` | `false` | 尚未证明 quotient/reuse/weighted returns 不能把大量残洞压成太少的不同 type instances。 | NoQuotientCollapseBelowTypeThreshold |
| `EffectiveDistinctTypeInstanceLowerBoundCurrentCorpusProved` | `false` | `false` | 类型压缩需要的是有效不同实例数，而不仅是加权质量；当前该下界未证。 | EffectiveDistinctTypeInstanceLowerBound |
| `BoundaryCapForcedFormalUnitObligationLowerBoundCurrentCorpusProved` | `false` | `false` | 已闭合残洞到加权义务的注入，但未闭合残洞质量和抗商化塌缩，所以 forced lower bound 仍未完成。 | BoundaryResidualMassLowerBoundForTypeCompression AND NoQuotientCollapseBelowTypeThreshold |

## 4. 下一主攻点

```text
BoundaryResidualMassLowerBoundForTypeCompression
```

并行硬点：

```text
NoQuotientCollapseBelowTypeThreshold
```
