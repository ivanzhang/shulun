# Prime Matrix strict actual emitter incidence 熵/纤维拆分路由器

**状态：** `strict_actual_emitter_bounded_incidence_reduced_to_source_entropy_and_fixed_pair_fiber_bound_open`

`ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem` 被拆成两个不可混淆的账本：`ActualEmitterSourceDomainEntropyLedger` 与 `ExactUVMapFixedPairPolylogFiberBoundLedger`。这仍是同一源熵目标内部的 incidence 证明，不是换命题。当前语料尚未证明这两个账本，行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
actual_emitter_incidence_entropy_router_closed=true
bounded_multiplicity_split_pinned=true
actual_emitter_source_domain_entropy_proved=false
exact_uv_map_fixed_pair_polylog_fiber_bound_proved=false
actual_emitter_exact_uv_bounded_multiplicity_incidence_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 拆分

拆分前：

```text
ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem
```

拆分后：

```text
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```

拆分合同：

```text
To prove bounded multiplicity for the actual emitter, prove both: (1) the pre-Cauchy emitted source domain has log-power absolute entropy/support, and (2) after branch/sign/local-factor refinement, each fixed exact (u,v) pair has only polylog many primitive preimages.
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ActualEmitterIncidenceTargetActive` | `true` | `false` | 上一层已把 exact-UV map rank 压成 actual emitter 的有界重数 incidence。 | ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem |
| `BoundedMultiplicitySplitPinned` | `true` | `false` | 有界重数 incidence 等价于源域足够大且每个 fixed pair 的原像纤维足够小。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `PaymentSkeletonDoesNotGiveSourceDomainEntropy` | `true` | `true` | payment count identity 只统计下游需求，不证明 pre-Cauchy emitted primitive summand 域的 absolute entropy。 | ActualEmitterSourceDomainEntropyLedger。 |
| `DisintegrationDictionaryDoesNotGiveFiberBound` | `true` | `true` | 即使 signed 字典存在，还必须另证 fixed `(u,v)` 下 branch/sign/local-factor 原像数受控。 | ExactUVMapFixedPairPolylogFiberBoundLedger。 |
| `BranchBudgetNotEnoughForEntropy` | `false` | `true` | branch key 复杂度预算尚未证明；即便证明 polylog key 数，也只给 fixed-pair 纤维上界的一部分，不给 image entropy。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `NaiveFactorSupportCountermodelImported` | `true` | `true` | 旧 factor-support 反模型显示内部 atom 可在一个 moving pair 内展开；不能用 residue-flat 代替源域 entropy。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `WeightComparabilityImported` | `true` | `true` | 单 summand 权重和容量损失已登记，所以本步只处理 counting/entropy，不再处理权重偷换。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |
| `CurrentCorpusIncidenceEntropyBasisProved` | `false` | `false` | 当前语料尚未证明源域 entropy 和 fixed-pair polylog fiber bound 的合取。 | ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger |

## 3. 结构结论

有界重数 incidence 不是一个单字段性质。源域总支撑不足时，即使 fixed-pair 纤维小也无用；fixed-pair 纤维可很大时，即使 payment count 大也可能全部坍缩到一个 `(u,v)`。因此下一步必须同时证明 source-domain entropy 与 fixed-pair polylog fiber bound。

## 4. 下一主攻点

```text
ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger
```
