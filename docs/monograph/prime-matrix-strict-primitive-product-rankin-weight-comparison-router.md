# Prime Matrix strict primitive product Rankin 权重比较路由器

## 结论

`PrimitiveProductRankinWeightP018Comparison` 的公式层已经推进：对任意 dyadic 产品块 `(Y,2Y]` 与任意 `s>0`，候选数满足 `N_B<=min(Y^{-s}Z_+(s),(2Y)^sZ_-(s))`，其中 `Z_±` 是允许 primitive 因子域上的有限 Euler product。这个结论自足且可复算。但要推出 `P^0.18` 仍必须给出全部实际块的 `P,h0,Y,s` 预算表，并为失败块登记回流包；因此完整权重比较尚未闭合。

```text
status=primitive_rankin_local_weight_formula_closed_p018_table_open
hardpoint_before=PrimitiveProductRankinWeightP018Comparison
hardpoint_after=PrimitiveProductRankinP018InequalityTable AND PrimitiveProductRankinFailureReturnPacketLedger
next_direct_attack_target=PrimitiveProductRankinP018InequalityTable
primitive_product_local_rankin_weight_formula_closed=true
primitive_product_rankin_weight_p018_comparison_proved=false
row_column_unconditional_closed=false
```

## 已闭合公式

| 名称 | 公式 | 状态 |
|---|---|---|
| `left_tail_rankin` | 1_{d>Y} <= (d/Y)^s, so N_B <= Y^{-s} sum_{d\|h0,allowed} d^s | `closed` |
| `right_tail_rankin` | 1_{d<=2Y} <= (2Y/d)^s, so N_B <= (2Y)^s sum_{d\|h0,allowed} d^{-s} | `closed` |
| `euler_factorization` | sum_{d\|h0,allowed} d^{±s}=prod_{p^a\|\|h0,allowed}(1+p^{±s}+...+p^{±as}) | `closed` |
| `two_sided_dyadic_bound` | N_B <= min(Y^{-s}Z_+(s),(2Y)^s Z_-(s)) for every s>0 | `closed` |
| `p018_comparison_condition` | need min_s min(Y^{-s}Z_+(s),(2Y)^s Z_-(s)) <= P^0.18 for each actual block | `open_requires_table` |

## 剩余阻断

| 阻断 | 含义 | 下一步 |
|---|---|---|
| `profile_hash_not_budget` | 投影 hash 只锁定局部素因子 profile，不给出实际 P、h0、Y 与剩余预算。 | `PrimitiveProductRankinP018InequalityTable` |
| `sigma_not_universal` | 不同 dyadic 块的最优 s 可变；固定常数 s 不能替代逐块表。 | `PrimitiveProductRankinP018InequalityTable` |
| `failed_weight_row_needs_return` | 若某块 Rankin 上界超过 P^0.18，必须回流热窗口/共同核/PDEC/SAE/固定历史。 | `PrimitiveProductRankinFailureReturnPacketLedger` |
| `sample_pass_not_proof` | 样本账本只验证公式可执行性；即使通过也不能代表全部 formal unit 与产品块。 | `PrimitiveProductRankinP018InequalityTable` |
| `sample_boundary_pressure` | 当前诊断样本已有若干块的粗 Rankin 网格上界超过 P^0.18，说明公式层不能单独闭合。 | `PrimitiveProductRankinP018InequalityTable AND PrimitiveProductRankinFailureReturnPacketLedger` |

## 判定表

| Gate | Closed | Proved | Meaning | Remaining |
|---|---:|---:|---|---|
| `PrimitiveProductRankinWeightTargetImported` | `true` | `true` | 上一层已闭合 d 到 primitive profile 的可执行投影规则。 | `PrimitiveProductRankinWeightP018Comparison` |
| `PrimitiveProductLocalRankinWeightFormulaClosed` | `true` | `true` | 双侧 dyadic Rankin 指示函数与局部 Euler product 权重公式已自足闭合。 | `PrimitiveProductLocalRankinWeightFormula` |
| `PrimitiveProductEulerProfileSumBoundClosed` | `true` | `true` | 允许 primitive 因子域上的 sum d^{±s} 已分解为有限 Euler product。 | `PrimitiveProductEulerProfileSumBound` |
| `DiagnosticSampleLedgerExecutable` | `true` | `true` | 样本账本可执行；该项只校验公式管线，不作为全体产品块证明。 | `diagnostic only` |
| `DiagnosticSampleAllRowsPassGridP018` | `true` | `false` | 诊断样本是否全部通过 P^0.18 网格比较；失败表示需要更细预算表或回流包。 | `PrimitiveProductRankinP018InequalityTable AND PrimitiveProductRankinFailureReturnPacketLedger` |
| `PrimitiveProductRankinP018InequalityTablePresent` | `false` | `false` | 尚未列出全部实际 formal unit / dyadic block 的 P、h0、Y、s 与剩余预算比较。 | `PrimitiveProductRankinP018InequalityTable` |
| `PrimitiveProductRankinFailureReturnPacketLedgerClosed` | `false` | `false` | 尚未为 P^0.18 比较失败块生成热窗口/共同核/PDEC/SAE 回流包。 | `PrimitiveProductRankinFailureReturnPacketLedger` |
| `PrimitiveProductRankinWeightP018ComparisonProved` | `false` | `false` | 公式层已闭合，但缺全体实际块的不等式表和失败回流处理。 | `PrimitiveProductRankinP018InequalityTable AND PrimitiveProductRankinFailureReturnPacketLedger` |
| `ColdProductBlockCandidateCountOrSymbolicBoundProved` | `false` | `false` | Rankin 权重比较未闭合，因此 cold 产品候选计数符号界仍未闭合。 | `ColdProductBlockCandidateCountOrSymbolicBound` |
| `PrimitiveProductSupportRankinLedgerProved` | `false` | `false` | 权重比较和失败回流未完成，原始产品支撑 Rankin 门仍未闭合。 | `PrimitiveProductSupportRankinLedger` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链与真实结构链的终端矛盾。 | `PrimitiveProductRankinP018InequalityTable AND PrimitiveProductRankinFailureReturnPacketLedger AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` |

## 样本账本

- 路径：`data/primitive-product-rankin-weight-sample-ledger.json`
- 用途：只校验公式和计算管线，不作为全体产品块证明。

## 依赖哈希

| 文件 | SHA256 |
|---|---|
| `experiments/prime_matrix_strict_primitive_product_rankin_weight_comparison_router.py` | `4aa6909c583ee11f3b3c5fd12733ec1dc3950e565839da879dc1498d8faf2af6` |
| `data/primitive-product-rankin-weight-sample-ledger.json` | `79d8bcd52bc3ab367484ed2666f5dbfcae80ee87b53681d41d2df50132e2e3b1` |
| `docs/monograph/prime-matrix-strict-primitive-product-projection-rule-router.json` | `4c85ccfac092bb1ef772079cbf6adaa4c1f64f7b485b8d3ed2a71e2ea67422f9` |
| `docs/monograph/prime-matrix-strict-cold-product-candidate-count-router.json` | `664b98a29a37db7ba354f28adf9d20842bfdac7505c8803fd5cd2d9038b06175` |
| `docs/monograph/prime-matrix-strict-primitive-product-rankin-manifest-router.json` | `394a44df31ee2a99dcdf53921e1c42af5943255233e2a49051affd1da12b3e9b` |
| `data/primitive-product-projection-sample-ledger.json` | `3aa57b90781b1cbfb8a04a23fe3c22d29db27744e23c34938def21314fe0774b` |
