# Prime Matrix strict 原始产品 Rankin manifest/权重表路由器

**状态：** `primitive_product_rankin_manifest_schema_closed_concrete_data_weight_table_open`

`PrimitiveProductRankinEmbeddingManifestAndWeightTable` 的 schema 层已闭合：manifest 必须锁定 source tuple、dyadic 产品块、cold/no-return 守卫、primitive rank profile、Rankin 权重、`P^0.18` 预算行和失败回流行。但当前还没有具体 source/block 数据、权重比较表和失败回流映射；因此 Rankin 门仍未闭合，最新最窄点是生成目标专用 concrete embedding data ledger。

```text
primitive_product_rankin_embedding_manifest_schema_closed=true
concrete_primitive_product_rankin_embedding_data_ledger_proved=false
primitive_product_rankin_weight_p018_comparison_proved=false
primitive_product_rankin_embedding_manifest_and_weight_table_proved=false
primitive_product_support_rankin_ledger_proved=false
row_column_unconditional_closed=false
```

## 1. Embedding Schema

| name | definition | purpose |
| --- | --- | --- |
| source_tuple | (formal_unit_id, h0, parameter_id, counterexample_branch_id) | 固定同一反例链和同参数账本。 |
| support_block | (Y,2Y] with d\|h0 and d cold-admissible | 锁定一个 dyadic 产品块，禁止跨块拼接预算。 |
| primitive_projection | d -> squarefree/local primitive profile after removing registered common kernels | 把分散支撑写成逐素数 rank 贡献，而不是全局 tau(d)。 |
| local_rank_weight | rho_l(d), w_l(rho_l), and product/Euler aggregate | 提供 Rankin 权重的可复算局部因子。 |
| cold_no_return_guard | not hot-density, not common-kernel return, not named PDEC/SAE/ColumnCRT | 确保 manifest 只覆盖 primitive dispersion branch。 |
| budget_row | rankin_sum(block) <= allowed_P018(block) | 直接对接 P^0.18 支撑预算。 |
| return_row | failed rows point to hot-density/common-kernel/PDEC/SAE/constant-gap packet | 保证失败行不形成第四出口。 |

## 2. 仍缺数据

| missing | why needed | next |
| --- | --- | --- |
| concrete_source_tuple_inventory | 需要列出当前 cold 产品块来自哪些 formal unit 与参数行。 | ConcretePrimitiveProductRankinEmbeddingDataLedger |
| primitive_projection_rule_hash | 必须可复算地移除共同核并生成 primitive rank profile。 | ConcretePrimitiveProductRankinEmbeddingDataLedger |
| rankin_weight_formula | 需要明确局部 rank 权和 Euler/Rankin 聚合常数。 | PrimitiveProductRankinWeightP018Comparison |
| P018_allowed_budget_table | 每个 dyadic 块必须有同参数允许预算，而不是总量口头估计。 | PrimitiveProductRankinWeightP018Comparison |
| failure_return_packet_map | 未通过 Rankin 的行必须指向热窗口、共同核或 PDEC/SAE 回流包。 | PrimitiveProductRankinFailureReturnPacketLedger |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PrimitiveProductManifestTargetImported` | `true` | `true` | 上一层已确认 Rankin 验收 schema 可复用，但目标产品 manifest 缺失。 | PrimitiveProductRankinEmbeddingManifestAndWeightTable |
| `OldManifestScopeMismatchGuardClosed` | `true` | `true` | 明确禁止把旧 colored corridor manifest 直接套入当前 cold 产品块。 | guard closed |
| `PrimitiveProductRankinEmbeddingManifestSchemaClosed` | `true` | `true` | 目标 manifest 字段、预算行和失败回流行已经定义为可审查 schema。 | PrimitiveProductRankinEmbeddingManifestSchema |
| `ConcretePrimitiveProductRankinEmbeddingDataLedgerProved` | `false` | `false` | 尚未生成当前 formal unit / dyadic block / primitive rank profile 的具体数据清单。 | ConcretePrimitiveProductRankinEmbeddingDataLedger |
| `PrimitiveProductRankinWeightP018ComparisonProved` | `false` | `false` | 尚未给出 Rankin 权重总和与 P^0.18 预算的逐块比较。 | PrimitiveProductRankinWeightP018Comparison |
| `PrimitiveProductRankinFailureReturnPacketLedgerClosed` | `false` | `false` | 尚未为目标产品 Rankin 失败行生成回流包。 | PrimitiveProductRankinFailureReturnPacketLedger |
| `PrimitiveProductRankinEmbeddingManifestAndWeightTableProved` | `false` | `false` | schema 已闭合，具体数据、权重比较和失败回流仍未完成。 | ConcretePrimitiveProductRankinEmbeddingDataLedger AND PrimitiveProductRankinWeightP018Comparison AND PrimitiveProductRankinFailureReturnPacketLedger |
| `PrimitiveProductSupportRankinLedgerProved` | `false` | `false` | 目标 manifest/权重表未完成，故原始产品 Rankin 门仍未闭合。 | PrimitiveProductSupportRankinLedger |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未形成排除早期零行反例链的终端矛盾。 | ConcretePrimitiveProductRankinEmbeddingDataLedger AND PrimitiveProductRankinWeightP018Comparison AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`ConcretePrimitiveProductRankinEmbeddingDataLedger`。
- 同步：`PrimitiveProductRankinWeightP018Comparison` 与 `PrimitiveProductRankinFailureReturnPacketLedger`。
- 边界：本步只闭合 schema，不提供具体 Rankin pass 证明。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-batch-rankin-pass-return-router.json` | `c7ba9f5f98a7264b55c3ca6eb01d057cc93f64f39531350bde862cae35abd1a0` |
| `docs/monograph/prime-matrix-full-rankin-ledger-inventory-router.json` | `914416c71595e19675adf90d35301cd1f8648a17e67f9676211ab8a2f2f6187b` |
| `docs/monograph/prime-matrix-strict-cold-product-support-sparsification-router.json` | `1dc6e98d6eb37c2571d0c3bdff385f66069b8812c6c1a9c8b97860b37cfc6f95` |
| `docs/monograph/prime-matrix-strict-primitive-product-support-rankin-router.json` | `7243686f554a798d739ea6cec2a7ae2019a3b0f8a5854d65cb18f408afb4edee` |
| `experiments/prime_matrix_strict_primitive_product_rankin_manifest_router.py` | `a39eb31b2596296ebb1d6288f085f10c637bc971d787dd2d81107454619dacc3` |
