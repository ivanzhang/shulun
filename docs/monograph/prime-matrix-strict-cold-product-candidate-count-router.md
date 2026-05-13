# Prime Matrix strict cold 产品候选计数/符号界路由器

**状态：** `candidate_window_count_identity_closed_symbolic_bound_needs_projection_or_runner`

`ColdProductBlockCandidateCountOrSymbolicBound` 的可用恒等式已压实：候选数至多为同一 dyadic 窗口中的除数数，且 cold/no-return guard 只能删候选。但把它粗化为全局 `tau(h0)` 会回到已失败路线；真正可闭合的路只剩两条：给出 `d -> primitive rank profile` 的可执行投影并完成 Rankin 权重比较，或提供有限 runner/hash。最新最窄点因此转为 `PrimitiveProductProjectionRuleExecutableHash`。

```text
window_divisor_count_envelope_closed=true
raw_tau_closure_rejected_for_candidate_count=true
candidate_excess_return_route_registered=true
primitive_symbolic_envelope_schema_closed=true
cold_product_block_candidate_count_or_symbolic_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 候选封套

| name | formula | status | meaning |
| --- | --- | --- | --- |
| raw_window_count | #Cand(B) <= N_{h0}(Y,2Y] | closed_identity | 候选产品必须是 h0 在该 dyadic 窗口内的除数。 |
| cold_filter | Cand(B) = raw_window_count minus hot/common/named-return candidates | closed_definition | cold/no-return 条件只删候选，不增加候选。 |
| excess_to_return | too many candidates before primitive projection -> hot density or common-kernel return | registered_not_excluded | 过量候选不是免费支撑，必须登记为热窗口或共同核回流。 |
| primitive_symbolic_envelope | #Cand(B) <= RankinWeight(primitive profiles) + Return(B) | schema_open_projection | 真正可和封套需要 primitive 投影规则和权重比较。 |

## 2. 未闭合原因

| obstruction | reason | required |
| --- | --- | --- |
| raw_tau_reuse | N_{h0}(Y,2Y] 的粗全局求和会退回 tau(h0)，该路线已在 P=100000 边界失败。 | PrimitiveProductProjectionRuleExecutableHash OR FiniteColdProductBlockCandidateRunnerHash |
| cold_filter_not_quantified | cold/no-return guard 定义了删选集合，但没有给出删选后数量的数值界。 | CandidateExcessHotDensityOrCommonKernelReturnLedger |
| rankin_without_projection | 没有 d -> primitive rank profile，Rankin 权不能作用到当前候选集合。 | PrimitiveProductProjectionRuleExecutableHash |
| finite_runner_missing | 没有当前 source tuple / block 的可复算枚举输出和 hash。 | FiniteColdProductBlockCandidateRunnerHash |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CandidateCountTargetImported` | `true` | `true` | 上一层已定义 cold 产品块候选集合，当前需给出计数或符号界。 | ColdProductBlockCandidateCountOrSymbolicBound |
| `WindowDivisorCountEnvelopeClosed` | `true` | `true` | 候选数被同一窗口内的 h0 除数数 N_{h0}(Y,2Y] 控制。 | WindowDivisorCountEnvelopeForColdProductBlock |
| `RawTauClosureRejectedForCandidateCount` | `true` | `true` | 不能把窗口除数数再粗化为全局 tau(h0) 并宣称闭合。 | PrimitiveProductProjectionRuleExecutableHash OR FiniteColdProductBlockCandidateRunnerHash |
| `CandidateExcessReturnRouteRegistered` | `true` | `false` | 若候选块过量且不进入 primitive 分散支撑，则必须回流热窗口或共同核；回流排斥未闭合。 | CandidateExcessHotDensityOrCommonKernelReturnLedger |
| `PrimitiveSymbolicEnvelopeSchemaClosed` | `true` | `false` | 候选计数可写成 primitive Rankin 权重加回流项，但投影规则和权重比较仍缺。 | PrimitiveProductProjectionRuleExecutableHash AND PrimitiveProductRankinWeightP018Comparison |
| `ColdProductBlockCandidateCountOrSymbolicBoundProved` | `false` | `false` | 窗口计数恒等式闭合，但没有可用数值界；必须走 primitive 投影/Rankin 或有限 runner。 | (PrimitiveProductProjectionRuleExecutableHash AND PrimitiveProductRankinWeightP018Comparison) OR FiniteColdProductBlockCandidateRunnerHash |
| `ColdProductDyadicBlockInventoryLedgerProved` | `false` | `false` | 候选计数/符号界未闭合，产品块 inventory 仍未闭合。 | ColdProductDyadicBlockInventoryLedger |
| `ConcretePrimitiveProductRankinEmbeddingDataLedgerProved` | `false` | `false` | 产品块候选界未闭合，concrete Rankin data 仍未闭合。 | ConcretePrimitiveProductRankinEmbeddingDataLedger |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链终端矛盾。 | PrimitiveProductProjectionRuleExecutableHash AND PrimitiveProductRankinWeightP018Comparison AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`PrimitiveProductProjectionRuleExecutableHash`。
- 同步：`PrimitiveProductRankinWeightP018Comparison`。
- 备选：`FiniteColdProductBlockCandidateRunnerHash`。
- 边界：本步只关闭窗口计数恒等式，不证明候选数足够小。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-filtered-divisor-support-router.json` | `c37398e74be3f912c6d753868ae8a973f7c61df6aa9fe834e420fd0a893ed7b7` |
| `docs/monograph/prime-matrix-strict-cold-product-block-inventory-router.json` | `a9630947c1df0d152a5f1e9f111863792c4022494f509f6ae966b0f7957d6b1b` |
| `docs/monograph/prime-matrix-strict-cold-product-support-sparsification-router.json` | `1dc6e98d6eb37c2571d0c3bdff385f66069b8812c6c1a9c8b97860b37cfc6f95` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-windowed-reciprocal-divisor-density-router.json` | `1a367725b5a64d16447823d3bd619ac9955dd634eba4f31ad09326be20ccf57c` |
| `experiments/prime_matrix_strict_cold_product_candidate_count_router.py` | `6f9e970707938c9217bb55f86c92967b17c3249e36393b32b3aa0c26fbcd5d9a` |
