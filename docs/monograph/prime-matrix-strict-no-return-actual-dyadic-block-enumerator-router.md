# Prime Matrix strict no-return actual dyadic 产品块枚举器路由器

**状态：** `no_return_actual_dyadic_block_enumerator_closed_weight_table_return_global_open`

`ActualDyadicColdProductBlockEnumeratorForH0` 在 no-return 分支可关闭为唯一 dyadic 分割规则：给定 `h0^car` 后，每个候选产品 `d|h0^car` 落入唯一块 `(2^j,2^{j+1}]`，候选集再由 cold/no-return guard 过滤，并以 `block_id` 稳定哈希。这样“缺 Y 列表”不再是独立源头硬点；真正剩余变成对所有枚举块提交 Rankin/P^0.18 权重表和失败回流包。全局 source-defect/valuation-overflow return 分支仍未排斥或吸收，所以行/列命题仍未无条件闭合。

```text
actual_dyadic_cold_product_block_enumerator_for_no_return_h0_closed=true
actual_dyadic_cold_product_block_enumerator_global_proved=false
actual_cold_product_block_parameter_ledger_present=false
primitive_product_rankin_p018_inequality_table_present=false
carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved=false
row_column_unconditional_closed=false
```

## 1. 枚举规则

| component | rule | status |
| --- | --- | --- |
| dyadic partition | B_j=(2^j,2^{j+1}], 0<=j<=floor(log_2 h0^car) | closed_rule |
| unit product | d=1 is the empty-prefix unit and is not counted as a productive dyadic product block | closed_boundary |
| candidate set | Cand_j={d:d\|h0^car, d in B_j, d passes cold/no-return guard} | closed_rule |
| empty block | Cand_j=empty may be omitted with empty-block hash; it carries no Rankin mass | closed_rule |
| block id | block_id=H(source_tuple_hash,h0_hash,cold_key,j,2^j,2^{j+1}) | closed_rule |
| no cross-block merge | each d belongs to exactly one dyadic B_j | closed_rule |
| return filter | source-defect/overflow/hot/common-kernel candidates leave no-return and enter named return frontier | registered_global_open |

## 2. 样本核验

- sample h0: `840`
- sample_partition_valid: `true`

| Y | interval | candidate_count | candidate_divisors |
| --- | --- | --- | --- |
| `1` | `(1,2]` | `1` | `[2]` |
| `2` | `(2,4]` | `2` | `[3, 4]` |
| `4` | `(4,8]` | `4` | `[5, 6, 7, 8]` |
| `8` | `(8,16]` | `4` | `[10, 12, 14, 15]` |
| `16` | `(16,32]` | `5` | `[20, 21, 24, 28, 30]` |
| `32` | `(32,64]` | `5` | `[35, 40, 42, 56, 60]` |
| `64` | `(64,128]` | `4` | `[70, 84, 105, 120]` |
| `128` | `(128,256]` | `3` | `[140, 168, 210]` |
| `256` | `(256,512]` | `2` | `[280, 420]` |
| `512` | `(512,1024]` | `1` | `[840]` |

## 3. 剩余原子

| remaining | meaning |
| --- | --- |
| `ColdProductBlockCandidateCountOrSymbolicBound` | 每块候选集已定义，但仍需证明候选数或 Rankin 权重低于预算。 |
| `PerBlockRegisteredCommonKernelLedger` | 每个实际块必须登记共同核/primitive 投影，防止重复计数。 |
| `PrimitiveProductRankinP018InequalityTable` | 需要对所有枚举块给出 Rankin 权重与 P^0.18 预算比较。 |
| `PrimitiveProductRankinFailureReturnPacketLedger` | 权重失败块必须带命名回流包，不能静默删除。 |
| `CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption` | 全局 return 分支仍需非持久预算吸收或持久终端排斥。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EnumeratorTargetImported` | `true` | `true` | 上一层 no-return h0 回接后，下一点是实际 dyadic 产品块枚举器。 | ActualDyadicColdProductBlockEnumeratorForH0 |
| `NoReturnH0DomainImported` | `true` | `true` | no-return 分支已有 h0^car、D(U)\|h0^car 和整数残频。 | NoReturnActualProductDivisorDomainH0EmitterForFormalUnit |
| `ColdProductCandidateGeneratorImported` | `true` | `true` | 候选集定义为 d\|h0 且通过 cold/no-return guard 的产品支撑。 | ColdProductCandidateSetGeneratorRule |
| `ActualDyadicEnumeratorRuleClosed` | `true` | `true` | 给定 h0^car 后，dyadic 块和 block_id 有唯一可复算规则。 | ActualDyadicColdProductBlockEnumeratorForH0 |
| `PrimitiveProjectionAndRankinFormulaImported` | `true` | `true` | 候选 d 到 primitive profile 的投影规则与局部 Rankin 公式已可复用。 | PrimitiveProductProjectionRuleExecutableHash AND PrimitiveProductRankinWeightP018Comparison |
| `ActualColdProductBlockParameterLedgerPresent` | `false` | `false` | 枚举规则闭合但尚未给出全体实际块的权重 pass/return 表。 | PrimitiveProductRankinP018InequalityTable AND PrimitiveProductRankinFailureReturnPacketLedger |
| `GlobalActualDyadicEnumeratorProved` | `false` | `false` | 全局枚举仍受 source-defect/overflow return 分支限制。 | CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的最终矛盾。 | PrimitiveProductRankinP018InequalityTable AND CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步

- 主攻：`PrimitiveProductRankinP018InequalityTable`。
- 并行保留：
  - `PrimitiveProductRankinFailureReturnPacketLedger`
  - `PerBlockRegisteredCommonKernelLedger`
  - `ColdProductBlockCandidateCountOrSymbolicBound`
  - `CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption`
  - `SparseHistoryDemandExceedsNonpersistentSupplyBudget`
  - `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`
  - `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json` | `a2d4e9a4d5d5f8d377571fc39d9c94e1ddb97d2afae30ef9e4c9e18296677307` |
| `docs/monograph/prime-matrix-strict-cold-product-block-inventory-router.json` | `a9630947c1df0d152a5f1e9f111863792c4022494f509f6ae966b0f7957d6b1b` |
| `docs/monograph/prime-matrix-strict-cold-product-candidate-count-router.json` | `664b98a29a37db7ba354f28adf9d20842bfdac7505c8803fd5cd2d9038b06175` |
| `docs/monograph/prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.json` | `635120578c17b2e7d697814ee4da41449b6381ed8b3717ad611f235620b89051` |
| `docs/monograph/prime-matrix-strict-primitive-product-projection-rule-router.json` | `4c85ccfac092bb1ef772079cbf6adaa4c1f64f7b485b8d3ed2a71e2ea67422f9` |
| `docs/monograph/prime-matrix-strict-primitive-product-rankin-p018-table-router.json` | `01ac5c80037d76d59f0d127041d9105c694a553da6cb5f6466928b73c67985f6` |
| `docs/monograph/prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json` | `2b1fa788ac82421045fe246cf635e7c945c68d6dee6b67a5e418c134120e940f` |
| `experiments/prime_matrix_strict_no_return_actual_dyadic_block_enumerator_router.py` | `57f5a0ee02cc73bc7a96973cad9c6827c73800c25a9b573157809f6441203653` |
