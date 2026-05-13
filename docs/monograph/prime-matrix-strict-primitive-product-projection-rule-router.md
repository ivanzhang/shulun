# Prime Matrix strict primitive product projection rule 路由器

**状态：** `primitive_product_projection_rule_executable_closed_weight_comparison_open`

`PrimitiveProductProjectionRuleExecutableHash` 已闭合：候选产品 `d` 先通过 `d|h0` 守卫，再剔除已登记共同核重叠；留在 primitive dispersion 分支的产品被唯一分解为排序的局部素因子/指数 profile，并生成稳定 hash。该规则删除了有序历史和共同核歧义。但这还没有证明 Rankin 权重总和小于 `P^0.18`，最新最窄点转为 `PrimitiveProductRankinWeightP018Comparison`。

```text
primitive_rank_profile_canonicalization_closed=true
primitive_product_projection_rule_executable_hash_closed=true
primitive_product_rankin_weight_p018_comparison_proved=false
cold_product_block_candidate_count_or_symbolic_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 投影规则

| step | definition | effect |
| --- | --- | --- |
| divisibility_guard | reject d if d does not divide h0 | not a candidate product for this formal unit |
| common_kernel_guard | reject d if gcd(d, registered_common_kernel)>1 | candidate returns to common-kernel/PDEC ledger, not primitive dispersion |
| prime_factor_projection | factor d and sort primes increasingly | order-free local rank profile |
| valuation_state | record (prime, product_exp, h0_exp, rank_unit=1) | Rankin/Euler weights can be applied per local prime factor |
| profile_hash | sha256 of canonical sorted JSON profile | stable manifest row key |

## 2. 样本账本

- path: `data/primitive-product-projection-sample-ledger.json`
- sha256: `3aa57b90781b1cbfb8a04a23fe3c22d29db27744e23c34938def21314fe0774b`

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PrimitiveProjectionTargetImported` | `true` | `true` | 上一层已把候选计数的解析路线压到 primitive 投影规则。 | PrimitiveProductProjectionRuleExecutableHash |
| `CommonKernelReturnGuardImported` | `true` | `true` | 共同核重叠不能留在 primitive dispersion 分支，必须回流。 | CommonKernelCandidateReturnFilter |
| `PrimitiveRankProfileCanonicalizationClosed` | `true` | `true` | 候选 d 被确定性分解为排序局部素因子/指数 profile，并给出稳定 hash。 | PrimitiveProductRankProfileCanonicalization |
| `PrimitiveProductProjectionRuleExecutableHashClosed` | `true` | `true` | 投影规则已由本脚本和样本账本物化为可执行哈希对象。 | PrimitiveProductRankinWeightP018Comparison |
| `PrimitiveProductRankinWeightP018ComparisonProved` | `false` | `false` | 投影规则已闭合，但尚未证明 Rankin 权重总和低于 P^0.18。 | PrimitiveProductRankinWeightP018Comparison |
| `ColdProductBlockCandidateCountOrSymbolicBoundProved` | `false` | `false` | 缺权重比较或 finite runner，因此候选计数符号界仍未闭合。 | PrimitiveProductRankinWeightP018Comparison OR FiniteColdProductBlockCandidateRunnerHash |
| `ConcretePrimitiveProductRankinEmbeddingDataLedgerProved` | `false` | `false` | 投影规则闭合但 concrete 产品块权重数据仍未完成。 | PrimitiveProductRankinWeightP018Comparison |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链终端矛盾。 | PrimitiveProductRankinWeightP018Comparison AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`PrimitiveProductRankinWeightP018Comparison`。
- 边界：本步只闭合投影规则，不证明权重比较。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/primitive-product-projection-sample-ledger.json` | `3aa57b90781b1cbfb8a04a23fe3c22d29db27744e23c34938def21314fe0774b` |
| `docs/monograph/prime-matrix-strict-cold-product-block-inventory-router.json` | `a9630947c1df0d152a5f1e9f111863792c4022494f509f6ae966b0f7957d6b1b` |
| `docs/monograph/prime-matrix-strict-cold-product-candidate-count-router.json` | `664b98a29a37db7ba354f28adf9d20842bfdac7505c8803fd5cd2d9038b06175` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `experiments/prime_matrix_strict_primitive_product_projection_rule_router.py` | `ee1e8a38b1ccb5592627fa05f462bea69874cc4cbad0c5407a57c2eb0d9bfdbf` |
