# Prime Matrix strict primitive product actual block replay 前沿路由器

**状态：** `primitive_product_rankin_synced_to_actual_block_replay_open`

`PrimitiveProductSupportRankinLedger` 的当前缺口已经不是投影规则或 Rankin 公式：primitive 投影规则已可执行，Rankin 权重公式已闭合，Rankin 失败也已通过 exact-count fallback 与 hot-return 二分同步。真正未闭合的是 actual 产品块 replay：当前语料没有`source_tuple_hash/P/h0/Y/registered_common_kernel` 参数行，不能把诊断样本升级为全体证明。因此下一最窄点是 `ActualColdProductBlockReplayLedgerOrHotReturnPacketTable`。

```text
cold_product_block_inventory_schema_closed=true
primitive_product_projection_rule_executable_hash_closed=true
rankin_formula_and_exact_fallback_synced=true
actual_cold_product_block_parameter_ledger_present=false
primitive_product_support_rankin_ledger_proved=false
row_column_unconditional_closed=false
```

## 1. actual 参数扫描

| scan | found | hit count | required fields |
| --- | --- | ---: | --- |
| `actual_cold_product_block_parameter_ledger_scan` | `false` | `0` | source_tuple_hash, P, h0, Y, registered_common_kernel |

## 2. 接口状态

| name | status | statement |
| --- | --- | --- |
| `block_inventory_schema` | `closed` | block_id, source tuple, cold key, dyadic interval, candidate rule, and return filter are defined. |
| `primitive_projection_rule` | `closed` | candidate d is projected to an order-free primitive rank profile after common-kernel filtering. |
| `rankin_weight_formula` | `closed_formula_only` | two-sided dyadic Rankin/Euler weight bounds are available but need actual P,h0,Y rows. |
| `exact_count_hot_return_dichotomy` | `closed_logic_only` | if exact block count exceeds P^0.18, the block is a hot-return packet; otherwise it is exact_count_pass. |
| `actual_block_replay_ledger` | `open` | no actual source_tuple/P/h0/Y/common-kernel replay ledger is present in the current corpus. |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ColdProductBlockInventorySchemaClosed` | `true` | `true` | 产品块字段和候选集合生成规则已经定义。 | ActualColdProductBlockReplayLedgerOrHotReturnPacketTable |
| `PrimitiveProjectionExecutableClosed` | `true` | `true` | 候选 d 到 primitive rank profile 的投影规则已经闭合。 | PrimitiveProductRankinWeightP018Comparison |
| `RankinFormulaAndExactFallbackSynced` | `true` | `true` | Rankin 上界失败不再等同支撑失败；可用 exact-count fallback 或 hot-return 二分处理。 | ActualColdProductBlockReplayLedgerOrHotReturnPacketTable |
| `ActualBlockParameterLedgerPresent` | `false` | `false` | 当前语料没有 actual source_tuple/P/h0/Y/common-kernel 参数行，不能把样本升级为全体证明。 | ActualColdProductBlockReplayLedgerOrHotReturnPacketTable |
| `PrimitiveProductSupportRankinLedgerProved` | `false` | `false` | 公式、投影和二分已同步，但缺 actual replay 表，因此原始产品支撑 Rankin 门仍未闭合。 | ActualColdProductBlockReplayLedgerOrHotReturnPacketTable AND FiniteColdProductBlockCandidateRunnerHash |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | actual replay、非持久预算反超、持久 moving atom 和 DStructure/Rankin 仍未全部闭合。 | ActualColdProductBlockReplayLedgerOrHotReturnPacketTable AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步

- 主攻：`ActualColdProductBlockReplayLedgerOrHotReturnPacketTable`。
- 具体任务：对每个 actual source tuple 生成 dyadic 产品块清单、候选 d 集合、exact count 或 Rankin bound；若 exact count 超过 `P^0.18`，同步生成 hot-return packet，而不是留下 clean residual。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/actual-cold-product-block-parameter-scan.json` | `0053d61213e6cfeff176dc50fe3ff71bc2e44427bf6c1f22bb71459e3abf02b6` |
| `data/primitive-product-projection-sample-ledger.json` | `3aa57b90781b1cbfb8a04a23fe3c22d29db27744e23c34938def21314fe0774b` |
| `data/primitive-product-rankin-p018-sample-table.json` | `6ee83fd827a289762f17da0e458cc1fb7fcfbe64b862d7b1fef635133f06e551` |
| `data/primitive-product-rankin-weight-sample-ledger.json` | `79d8bcd52bc3ab367484ed2666f5dbfcae80ee87b53681d41d2df50132e2e3b1` |
| `docs/monograph/prime-matrix-strict-clean-primitive-rankin-failure-exact-count-fallback-router.json` | `0d36d83349f2e522b623cb21c0b644a720de17b13a9a8777b017e4be6d8f039d` |
| `docs/monograph/prime-matrix-strict-cold-product-block-inventory-router.json` | `a9630947c1df0d152a5f1e9f111863792c4022494f509f6ae966b0f7957d6b1b` |
| `docs/monograph/prime-matrix-strict-cold-product-candidate-count-router.json` | `664b98a29a37db7ba354f28adf9d20842bfdac7505c8803fd5cd2d9038b06175` |
| `docs/monograph/prime-matrix-strict-exact-primitive-block-count-hot-return-dichotomy-router.json` | `4162412458fa176a590493f6d2e9bfec6c72169a893e81716c5b6d496ffece1e` |
| `docs/monograph/prime-matrix-strict-primitive-product-projection-rule-router.json` | `4c85ccfac092bb1ef772079cbf6adaa4c1f64f7b485b8d3ed2a71e2ea67422f9` |
| `docs/monograph/prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json` | `2b1fa788ac82421045fe246cf635e7c945c68d6dee6b67a5e418c134120e940f` |
| `docs/monograph/prime-matrix-strict-terminal-hot-core-return-frontier-router.json` | `bb4818efdb6673899bc0e2eb86174244ef0f80568301c8ca34a57dc380bda909` |
| `experiments/prime_matrix_strict_primitive_product_actual_block_replay_frontier_router.py` | `13e62a4432a0b3056d88e0c7fd28019032449105db3836b6ecd2f5ccb2bc7ed1` |
