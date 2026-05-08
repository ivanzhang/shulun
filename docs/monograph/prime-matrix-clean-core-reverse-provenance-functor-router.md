# Prime Matrix clean-core 反向来源函子路由器

**状态：** `reverse_provenance_functor_boundary_closed_registered_fiber_emitter_open`

从已有支付图、投影塔和横向商模型得到的有效突破是边界重写：不能从 Gamma 反推 actual noncanonical primitive constructor；但当前公式剩余可等价压成一个更可审查的已登记 pre-pushforward 纤维分解 emitter。当前材料尚未证明该 emitter，因此行/列无条件命题仍未闭合。

```text
reverse_provenance_functor_boundary_closed=true
payment_pushforward_functoriality_available=true
pushforward_reverse_uniqueness_rejected=true
finite_projection_recovers_gamma_not_source=true
constructor_formula_equivalent_to_registered_fiber_emitter=true
registered_primitive_prepushforward_fiber_emitter_proved=false
actual_noncanonical_primitive_constructor_formula_proved=false
row_column_unconditional_closed=false
```

## 1. 反向函子律

支付图 Gamma、有限投影、弧限制和横向商都是 pre-Cauchy 来源测度的正向推前或有限因子。这些结构能证明来源兼容性和未登记出口纪律，却不能反向唯一恢复 primitive summand。在已闭合的回流纪律下，ActualNoncanonicalPrimitiveSourceConstructorFormulaAndReturn 等价于给出同一 formal unit 内的 RegisteredPrimitivePrePushforwardFiberEmitterAndReturn：它必须在推前前逐纤维列出 primitive summand、系数恒等式、branch key、u/v map、符号和 local factor；无法登记或超预算者必须回流。

```text
pre-Cauchy primitive source measure
  --deterministic payment pushforward--> Gamma
  --finite projections / arc restrictions / transverse quotients--> downstream factors;

Gamma and its finite factors do not determine the primitive source;
a valid reverse route must supply:
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn.
```

## 2. 汇总

- `reverse_provenance_functor_boundary_closed=true`。
- `registered_primitive_prepushforward_fiber_emitter_proved=false`。
- `actual_noncanonical_primitive_constructor_formula_proved=false`。
- `row_column_unconditional_closed=false`。
- `latest_internal_subinput=RegisteredPrimitivePrePushforwardFiberEmitterAndReturn`。
- `latest_external_subinput=CDependentResidueWeightSpectralCancellationInput`。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| PriorConstructorFormulaPinned | `true` | `false` | 上一层已把完全自足源侧剩余固定为 actual noncanonical primitive constructor formula。 | 判断已有支付图/投影塔模型能否反向恢复该公式。 |
| PaymentPushforwardFunctorialityAvailable | `true` | `true` | actual payment graph、有限投影、弧限制和横向商均为同一来源上的推前/因子操作。 | 这些是正向函子，不自动提供反向来源。 |
| ReversePushforwardUniquenessRejected | `true` | `true` | 推前映射通常不可逆；多个 pre-Cauchy primitive 源或不同纤维分配可给出同一 Gamma。 | 不能把 downstream payment atom 当作 primitive source formula。 |
| FiniteProjectionOnlyReconstructsGamma | `true` | `true` | 有限投影塔最多恢复真实支付图 Gamma 的投影极限，不恢复被推前前的 summand emitter。 | 需要额外的 pre-pushforward 纤维分解数据。 |
| CanonicalReverseImportBlocked | `true` | `true` | canonical 来源分支的 RIW/Buchstab 构造器已闭合但作用域固定，不能反向导入 noncanonical clean-core。 | noncanonical clean-core 必须给自己的已登记纤维 emitter 或回流。 |
| UnregisteredFiberReturnAbsorbed | `true` | `true` | 若某支付纤维没有同一 formal unit 的来源登记，它不再是 clean-core 终端，而回到已命名出口。 | 保留的 clean-core 情形必须提交已登记纤维分解。 |
| ConstructorFormulaEquivalentToRegisteredFiberEmitter | `true` | `true` | 公式与已登记 pre-pushforward 纤维分解在闭合的回流纪律下等价：公式可分组为纤维，纤维 emitter 可求和为公式。 | 等价不证明该 emitter 存在。 |
| DownstreamModelsCloseCompatibilityFields | `true` | `true` | 支付图、投影塔、横向商和来源分类防火墙已关闭 formal-unit 兼容与未登记出口问题。 | 仍需真正的 pre-pushforward summand 生成规则。 |
| RegisteredPrimitivePrePushforwardFiberEmitterCurrentCorpusProved | `false` | `false` | 当前材料尚未给出 actual noncanonical clean-core 的已登记 primitive 纤维分解 emitter。 | 证明 RegisteredPrimitivePrePushforwardFiberEmitterAndReturn。 |
| DStructureRankinStillIndependent | `true` | `false` | DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。 | 源侧完成后仍需独立验收。 |

## 4. 纤维 emitter 字段

| field | requirement |
| --- | --- |
| `pre_pushforward_domain` | 在 Cauchy/dispersion 前给出 primitive summand 的定义域，而不是从 Gamma 事后命名。 |
| `fiber_emitter` | 对每个正质量 clean-core payment atom，输出有限/polylog 个 primitive preimage summand。 |
| `coefficient_identity` | 证明这些 preimage summand 的 alpha/delta、符号与 local factor 推前后等于 actual payment 质量。 |
| `branch_schema` | 每个 summand 带 branch key、u/v map、phase/sign/local factor，且 key 数为 log^O(1)。 |
| `formal_unit_registration` | preimage、payment、capacity、support 与 return ledger 使用同一个 actual formal unit。 |
| `failure_return` | 空纤维、非唯一口径、超预算、thin block 或未登记来源必须给出命名 return tag。 |

## 5. 等价方向

| direction | content |
| --- | --- |
| `constructor_formula_to_fiber_emitter` | 若 actual noncanonical primitive constructor formula 已给出，则按 payment signature 分组其 emitted summand，即得到已登记 pre-pushforward 纤维分解。 |
| `fiber_emitter_to_constructor_formula` | 若已登记纤维分解 emitter 给出所有字段，则把 emitter 的输出在 Cauchy/dispersion 前求和，即得到 actual noncanonical primitive constructor formula；失败情形由 return tag 吸收。 |
| `pushforward_graph_to_formula_no_go` | 仅知道 Gamma 或任意有限投影不能反推唯一 pre-Cauchy 来源；不同 primitive 源测度可有同一推前。 |

## 6. 最新输入基

条件输入基：

```text
(RegisteredPrimitivePrePushforwardFiberEmitterAndReturn OR CDependentResidueWeightSpectralCancellationInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

完全自足输入基：

```text
RegisteredPrimitivePrePushforwardFiberEmitterAndReturn AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 7. 当前结论

本步没有证明新的 emitter，也没有声明行/列无条件命题闭合。它把“直接写公式”的剩余改写成更可审查的反向来源问题：
若能给出已登记的 pre-pushforward 纤维分解 emitter，则 actual noncanonical primitive constructor formula 随之闭合；
若不能给出，则该对象不能留在 clean-core 终端，而必须按未登记来源、口径冲突、thin block 或外部谱输入回流。
