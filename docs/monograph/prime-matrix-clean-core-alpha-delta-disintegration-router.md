# Prime Matrix clean-core alpha/delta 解积分字典路由器

**状态：** `alpha_delta_lift_reduced_to_registered_signed_disintegration_dictionary_open`

alpha/delta lift 被进一步压成 signed 解积分字典。已有模型给出基底映射和 canonical 模板，但当前材料尚未给出 noncanonical clean-core 的实际字典，所以行/列无条件命题仍未闭合。

```text
alpha_delta_disintegration_boundary_closed=true
payment_base_map_closed=true
lift_equivalent_to_signed_disintegration_dictionary=true
canonical_decision_tree_template_scoped=true
registered_alpha_delta_disintegration_dictionary_proved=false
exact_alpha_delta_lift_proved=false
row_column_unconditional_closed=false
```

## 1. 解积分律

ExactAlphaDeltaLiftForRegisteredPaymentFiberSkeletonAndReturn 的本质不是新的数值估计，而是 signed 源测度相对于 first-cover payment map 的解积分问题。payment skeleton 提供基底映射；pre-Cauchy 来源账本给出必要字段；路径分割说明 polylog branch key 如何转化为支撑保留；canonical RIW/Buchstab 决策树只提供作用域内模板。因此最新自足原子是 RegisteredAlphaDeltaDisintegrationDictionaryAndReturn：提交 actual noncanonical signed alpha/delta 源测度、逐纤维字典、推前恒等式、总变差/支撑预算、sign-refinement 和失败回流。

```text
signed alpha/delta primitive source measure nu
  -- first-cover payment map Phi --> payment skeleton Gamma;

Exact lift <=> registered signed disintegration dictionary of nu over Phi.
```

## 2. 汇总

- `alpha_delta_disintegration_boundary_closed=true`。
- `registered_alpha_delta_disintegration_dictionary_proved=false`。
- `latest_internal_subinput=RegisteredAlphaDeltaDisintegrationDictionaryAndReturn`。
- `row_column_unconditional_closed=false`。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PriorAlphaDeltaLiftPinned | `true` | `false` | 上一层已把最窄自足剩余压成 payment skeleton 到 signed alpha/delta primitive 系数的提升。 | 把 lift 拆成测度解积分字典字段。 |
| PaymentBaseMapClosed | `true` | `true` | completion-hole 域、first-cover map 和 payment count identity 已给出解积分的基底映射。 | 基底映射不生成 signed 源测度。 |
| LiftEquivalentToSignedDisintegrationDictionary | `true` | `true` | Exact alpha/delta lift 与 signed primitive 源测度在 payment map 上的逐纤维解积分字典等价。 | 等价不证明 actual noncanonical 字典存在。 |
| PreCauchyLedgerShowsNecessaryFields | `true` | `true` | pre-Cauchy 来源律原子化已说明字段必须包含 formal unit、branch key、u/v map、sign 和 local factor。 | 当前材料未提交 noncanonical clean-core 的实际字段表。 |
| PathPartitionShowsBudgetUse | `true` | `true` | 路径分割路由已说明 polylog branch schema 足以转化为 selector 支撑保留。 | 仍需 actual noncanonical 字典给出这些 branch key。 |
| CanonicalDecisionTreeTemplateScoped | `true` | `true` | canonical RIW/Buchstab 决策树展示了解积分字典的结构模板。 | 模板只在 canonical 分支内有效，不能导入 noncanonical clean-core。 |
| GenericOrUnregisteredDictionaryBlocked | `true` | `true` | generic WFD 和未登记来源不能作为字典；它们已被外部化或命名回流。 | 保留分支必须给 actual noncanonical registered dictionary。 |
| RegisteredAlphaDeltaDisintegrationDictionaryCurrentCorpusProved | `false` | `false` | 当前材料尚未给出 actual noncanonical clean-core 的 signed alpha/delta 解积分字典。 | 证明 RegisteredAlphaDeltaDisintegrationDictionaryAndReturn。 |
| DStructureRankinStillIndependent | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 4. 字典字段

| field | requirement |
| --- | --- |
| `signed_source_measure` | 在 Cauchy/dispersion 前给出 actual noncanonical alpha/delta signed primitive 源测度。 |
| `payment_base_map` | 给出 primitive summand 到 completion-hole/first-cover payment atom 的确定性映射。 |
| `fiber_dictionary` | 对每个正质量 payment atom 列出其 signed preimage summand、branch key、u/v map、sign 和 local factor。 |
| `pushforward_identity` | 证明字典沿 payment_base_map 推前后等于目标 alpha/delta payment-side 系数。 |
| `variation_and_support_budget` | 证明总变差、绝对支撑和 branch key 数在注册的 polylog/K6 预算内。 |
| `sign_refinement` | 同一完整 key 内 local factor 非零；若有相反号，必须先细分到 sign-refined key。 |
| `failure_return` | 无源测度、非同一 formal unit、推前不等式失败、超预算或抵消必须命名回流。 |

## 5. 等价方向

| direction | content |
| --- | --- |
| `lift_to_dictionary` | 若 ExactAlphaDeltaLift 已证明，则按 first-cover payment atom 分组 signed summand，得到解积分字典。 |
| `dictionary_to_lift` | 若字典含 signed 源测度、纤维表和推前恒等式，则逐纤维求和直接给出 ExactAlphaDeltaLift。 |
| `canonical_template_scoped` | RIW/Buchstab 决策树给出了 canonical 分支上的字典模板，但作用域不能跨到 noncanonical clean-core。 |

## 6. 最新输入基

条件输入基：

```text
(RegisteredAlphaDeltaDisintegrationDictionaryAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
RegisteredAlphaDeltaDisintegrationDictionaryAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 当前结论

本步没有证明 signed 字典。它把 alpha/delta lift 的终端硬点改写成一个可审稿的解积分字典：
先给 actual signed 源测度，再沿 first-cover payment map 逐纤维列出 signed summand 和推前恒等式。
canonical 决策树只提供模板，不能跨分支导入 noncanonical clean-core。
