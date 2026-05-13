# Prime Matrix strict primitive product Rankin P^0.18 表路由器

## 结论

`PrimitiveProductRankinP018InequalityTable` 的表结构和判定规则已闭合：每行必须给出 `source_tuple_hash,P,h0,Y,common_kernel,sigma,rankin_bound,p018_budget`，并按 `rankin_bound<=p018_budget` 判定 pass，否则必须附回流包。但当前只有 schema 与诊断样表，没有全体实际 cold 产品块参数行；且诊断样表中已有失败行，说明失败回流包不能省略。最新最窄点转为 `ActualColdProductBlockParameterLedgerForP018Table`。

```text
status=p018_table_schema_closed_actual_block_rows_and_failure_returns_open
hardpoint_before=PrimitiveProductRankinP018InequalityTable
hardpoint_after=ActualColdProductBlockParameterLedgerForP018Table AND PrimitiveProductRankinFailureReturnPacketLedger
next_direct_attack_target=ActualColdProductBlockParameterLedgerForP018Table
p018_table_schema_closed=true
primitive_product_rankin_p018_inequality_table_present=false
row_column_unconditional_closed=false
```

## 表字段

| 字段 | 作用 |
|---|---|
| `source_tuple_hash` | 绑定实际 early-zero 反例链 formal unit。 |
| `P` | 给出当前周期基准和 P^0.18 预算。 |
| `h0` | 给出产品除数域和局部 Euler product。 |
| `registered_common_kernel` | 删除已回流共同核素因子。 |
| `Y` | 指定 dyadic 产品块 (Y,2Y]。 |
| `sigma` | 给出该块 Rankin 权重参数。 |
| `rankin_bound` | 计算 min(Y^{-s}Z_+(s),(2Y)^sZ_-(s))。 |
| `p018_budget` | 计算 P^0.18 或同参数剩余预算。 |
| `verdict` | pass 或 return_required。 |
| `return_packet` | 失败时指向热窗口、共同核、PDEC/SAE、固定历史或 ColumnCRT。 |

## 判定规则

| 规则 | 条件 | 效果 |
|---|---|---|
| `rankin_pass` | rankin_bound <= p018_budget | 该块支撑进入 P^0.18 预算。 |
| `rankin_fail_return` | rankin_bound > p018_budget | 该块不能留在 primitive dispersion，必须有 return_packet。 |
| `missing_actual_row` | 缺 source_tuple_hash/P/h0/Y/sigma | 表不存在，不能宣称权重比较闭合。 |
| `sample_row` | 来自诊断样本而非全体实际块 | 只用于检验计算规则，不升级为证明。 |

## 阻断点

| 阻断 | 含义 | 下一步 |
|---|---|---|
| `actual_block_rows_missing` | 已有产品块 schema，但没有全体实际 source_tuple/P/h0/Y 行。 | `ActualColdProductBlockParameterLedgerForP018Table` |
| `sample_fail_rows_need_return` | 诊断样表中有 3 个失败行；这说明失败回流包是必要字段。 | `PrimitiveProductRankinFailureReturnPacketLedger` |
| `budget_is_rowwise_not_global_constant` | P^0.18 比较依赖每行 h0、Y、共同核和 sigma，不能用单个固定常数替代。 | `ActualColdProductBlockParameterLedgerForP018Table` |
| `old_inventory_schema_not_actual_table` | cold 产品块清单当前只闭合 schema 与候选生成规则，尚未给出实际参数表。 | `ActualColdProductBlockParameterLedgerForP018Table` |

## 判定表

| Gate | Closed | Proved | Meaning | Remaining |
|---|---:|---:|---|---|
| `PrimitiveProductRankinP018TableTargetImported` | `true` | `true` | 上一层已闭合局部 Rankin 权重公式，当前目标是逐块 P^0.18 表。 | `PrimitiveProductRankinP018InequalityTable` |
| `P018TableSchemaClosed` | `true` | `true` | 表字段和 pass/return 判定规则已闭合。 | `schema closed` |
| `DiagnosticP018SampleTableExecutable` | `true` | `true` | 诊断样表可生成；它只检验判定规则，不代表全体实际块。 | `diagnostic only` |
| `DiagnosticP018SampleAllRowsPass` | `true` | `false` | 诊断样本是否全部通过；失败行说明必须有 return_packet。 | `PrimitiveProductRankinFailureReturnPacketLedger` |
| `ActualColdProductBlockParameterLedgerPresent` | `false` | `false` | 尚未列出全体实际 source tuple / P / h0 / Y / common-kernel 参数行。 | `ActualColdProductBlockParameterLedgerForP018Table` |
| `PrimitiveProductRankinFailureReturnPacketLedgerClosed` | `false` | `false` | 尚未为所有 P^0.18 失败行给出目标专用回流包。 | `PrimitiveProductRankinFailureReturnPacketLedger` |
| `PrimitiveProductRankinP018InequalityTablePresent` | `false` | `false` | 只有 schema 与诊断样表，缺全体实际行和失败回流，因此完整表不存在。 | `ActualColdProductBlockParameterLedgerForP018Table AND PrimitiveProductRankinFailureReturnPacketLedger` |
| `PrimitiveProductRankinWeightP018ComparisonProved` | `false` | `false` | P^0.18 表未闭合，Rankin 权重比较仍未闭合。 | `PrimitiveProductRankinWeightP018Comparison` |
| `ColdProductBlockCandidateCountOrSymbolicBoundProved` | `false` | `false` | 权重比较未闭合，cold 产品候选计数/符号界仍未闭合。 | `ColdProductBlockCandidateCountOrSymbolicBound` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | `ActualColdProductBlockParameterLedgerForP018Table AND PrimitiveProductRankinFailureReturnPacketLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 样表

- 路径：`data/primitive-product-rankin-p018-sample-table.json`
- 用途：只检验 P^0.18 表判定规则，不作为全体实际块证明。

## 依赖哈希

| 文件 | SHA256 |
|---|---|
| `experiments/prime_matrix_strict_primitive_product_rankin_p018_table_router.py` | `f79d3de3342a94bb82913d6a24a7e79783091d9eaaa572a955a323cbdcbb0e12` |
| `data/primitive-product-rankin-p018-sample-table.json` | `6ee83fd827a289762f17da0e458cc1fb7fcfbe64b862d7b1fef635133f06e551` |
| `docs/monograph/prime-matrix-strict-primitive-product-rankin-weight-comparison-router.json` | `2b1fa788ac82421045fe246cf635e7c945c68d6dee6b67a5e418c134120e940f` |
| `docs/monograph/prime-matrix-strict-cold-product-block-inventory-router.json` | `a9630947c1df0d152a5f1e9f111863792c4022494f509f6ae966b0f7957d6b1b` |
| `data/primitive-product-rankin-weight-sample-ledger.json` | `79d8bcd52bc3ab367484ed2666f5dbfcae80ee87b53681d41d2df50132e2e3b1` |
