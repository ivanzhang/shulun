# Prime Matrix strict primitive emitter multiplicity/rank 直攻路由器

**状态：** `strict_emitter_multiplicity_reduced_to_exact_uv_map_rank_no_collapse_open`

`PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem` 被进一步压到映射秩层：payment skeleton、alpha/delta 解积分字典、branch 预算和反向来源函子都不能证明 exact `(u,v)` map 没有大原像纤维。最新最窄点是 `PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem`。该秩/无坍缩定理尚未证明，行/列命题仍未无条件闭合。

```text
same_theorem_target_preserved=true
no_theorem_switch=true
emitter_multiplicity_rank_attack_closed=true
payment_skeleton_not_enough=true
alpha_delta_dictionary_not_rank_proof=true
branch_budget_not_map_rank=true
pre_cauchy_emitter_exact_uv_map_rank_proved=false
new_actual_source_entropy_theorem_proved=false
row_column_unconditional_closed=false
```

## 1. 压缩

压缩前：

```text
PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem
```

压缩后：

```text
PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem
```

映射秩合同：

```text
For the actual pre-Cauchy primitive emitter in one formal unit, prove that the map from emitted primitive summands (including branch key, sign/local factor and source parameters) to exact (u,v) has maximum fiber at most |Domain|/L^K, or equivalently that the exact (u,v) image support has log-power rank/entropy.
```

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EmitterMultiplicityTargetActive` | `true` | `false` | 上一层已把绝对 fiber 质量分散压成 primitive emitter 原像 multiplicity 分散。 | PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem |
| `PaymentSkeletonNotEnough` | `true` | `true` | payment skeleton、first-cover map 和 count identity 只给下游计数骨架，不给 exact `(u,v)` map 的原像秩。 | PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem |
| `AlphaDeltaDictionaryStillObjectNotRank` | `true` | `true` | signed 解积分字典若存在，只给 source 对象和逐纤维字段；还必须证明这些字段不会坍缩到少数 `(u,v)`。 | PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem |
| `BranchBudgetNotMapRank` | `true` | `true` | branch key 与几何变差预算控制复杂度和总变差，但不自动给 exact `(u,v)` 映射秩下界。 | PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem |
| `ReverseFunctorNoRankRecovery` | `true` | `true` | 从推前 payment 图不能恢复 pre-Cauchy 原像，也不能恢复 exact `(u,v)` map 的最大纤维界。 | PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem |
| `MultiplicityEquivalentToMapRank` | `true` | `false` | 在单 summand 权重已登记后，multiplicity 分散等价于证明 exact `(u,v)` map 的最大 fiber 小，或 image 支撑足够大。 | PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem |
| `NoFiberCollapseConditionPinned` | `true` | `false` | 必须排除大量 branch/source summands 具有不同内部 key 但同一个 exact `(u,v)` 的坍缩模型。 | NoExactUVFiberCollapseForActualEmitter。 |
| `PreCauchyEmitterExactUVMapRankCurrentCorpusProved` | `false` | `false` | 当前语料尚未证明 actual pre-Cauchy emitter 的 exact `(u,v)` 映射秩/无坍缩定理。 | PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem |

## 3. 结构结论

multiplicity 分散的底层不是 payment count，也不是 alpha/delta 字典存在性，而是 exact `(u,v)` 映射的秩/无坍缩性质。branch key 复杂度小只说明可审计，不说明不同 branch 不会落入同一个 pair；必须直接证明 no-fiber-collapse。

## 4. 下一主攻点

```text
PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem
```
