# Prime Matrix strict 原始产品支撑 Rankin 路由器

**状态：** `primitive_product_rankin_schema_reusable_target_manifest_weight_table_open`

`PrimitiveProductSupportRankinLedger` 不能由旧 full Rankin 子账本直接关闭。可复用的是 Rankin 验收 schema 与 pass-or-return 纪律；不可复用的是旧 formal colored corridor manifest，因为当前对象是 cold 产品 dyadic 块。故最新剩余被压成目标专用三件套：当前产品支撑到 Rankin 行的 embedding manifest、Rankin 权重对 `P^0.18` 的比较表、以及失败行回流包。

```text
existing_rankin_verifier_schema_reusable=true
existing_colored_corridor_manifest_covers_current_products=false
target_primitive_product_manifest_present=false
primitive_product_rankin_weight_p018_comparison_proved=false
primitive_product_support_rankin_ledger_proved=false
row_column_unconditional_closed=false
```

## 1. Rankin 复用边界

| component | reuse | status | meaning |
| --- | --- | --- | --- |
| verifier_schema | yes | closed | 单证书、批量 manifest、pass-or-return 字段可复用。 |
| existing_colored_corridor_manifest | no_direct_import | scope_mismatch | 旧 manifest 覆盖 formal colored corridors，不自动覆盖当前 cold 产品 dyadic 块。 |
| failure_return_discipline | yes | closed_schema_open_exclusion | 失败行必须回流 PDEC/SAE/常数缺口；但回流排斥仍在下游。 |
| independent_promotion_acceptance | no_author_side_upgrade | referee_open | DStructure/Tail-log4/finite Rankin 晋级仍需独立验收。 |

## 2. 目标 manifest schema

| field | role | required |
| --- | --- | --- |
| formal_unit_id | 锁定同一 h_0、同一反例链 source tuple。 | yes |
| dyadic_product_block | 记录 Y<d<=2Y 的过载块。 | yes |
| cold_key | 绑定 cold/nonpersistent/no-return 过滤条件和规范窗口键。 | yes |
| primitive_rank_profile | 逐素数记录 primitive factor/rank 贡献，避免全局 tau 因子偷渡。 | yes |
| rankin_weight | 给出每行 Rankin 权重和总和。 | yes |
| allowed_P018_budget | 同参数比较目标，必须小于 P^0.18 的剩余支撑预算。 | yes |
| verdict_or_return | 每行要么 pass，要么回流热窗口、共同核、PDEC/SAE 或常数缺口。 | yes |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PrimitiveRankinTargetImported` | `true` | `true` | 上一层已把分散 cold 产品支撑压成原始 Rankin/Euler 账本。 | PrimitiveProductSupportRankinLedger |
| `ExistingRankinVerifierSchemaReusable` | `true` | `true` | 现有 Rankin 子账本提供可复用的单证书、批量 manifest 和 pass-or-return schema。 | schema closed |
| `ExistingColoredCorridorManifestCoversCurrentProducts` | `false` | `false` | 旧 concrete manifest 覆盖 formal colored corridors；当前 cold 产品 dyadic 块尚无嵌入映射，不能直接导入为已 pass。 | PrimitiveProductRankinEmbeddingManifestAndWeightTable |
| `TargetPrimitiveProductManifestPresent` | `false` | `false` | 尚未列出当前 formal unit / dyadic block / cold key / primitive rank profile 的目标专用 manifest。 | PrimitiveProductRankinEmbeddingManifestAndWeightTable |
| `PrimitiveProductRankinWeightP018ComparisonProved` | `false` | `false` | 尚未证明目标 manifest 的 Rankin 权重总和低于 P^0.18 支撑预算。 | PrimitiveProductRankinWeightP018Comparison |
| `PrimitiveProductRankinFailureReturnClosed` | `false` | `false` | 若目标 Rankin 行失败，尚未给出目标专用回流包。 | PrimitiveProductRankinFailureReturnPacketLedger |
| `PrimitiveProductSupportRankinLedgerProved` | `false` | `false` | Rankin 验收格式可复用，但当前产品支撑缺目标专用 manifest、权重比较和失败回流。 | PrimitiveProductRankinEmbeddingManifestAndWeightTable AND PrimitiveProductRankinWeightP018Comparison AND PrimitiveProductRankinFailureReturnPacketLedger |
| `ColdProductSupportSparsificationBeyondTauLedgerProved` | `false` | `false` | 原始分散支撑 Rankin 未闭合，故 cold 稀疏化仍未闭合。 | PrimitiveProductSupportRankinLedger AND ShortWindowHotDivisorDensityPDECorSAEReturnExclusion AND CommonKernelReturnCycleDescentOrPDECLedger |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链终端矛盾。 | PrimitiveProductRankinEmbeddingManifestAndWeightTable AND UnifiedTerminalBudgetStrictInequality AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`PrimitiveProductRankinEmbeddingManifestAndWeightTable`。
- 同步：`PrimitiveProductRankinWeightP018Comparison` 与 `PrimitiveProductRankinFailureReturnPacketLedger`。
- 边界：本步不把旧 Rankin manifest 直接套到当前产品支撑。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-batch-rankin-pass-return-router.json` | `c7ba9f5f98a7264b55c3ca6eb01d057cc93f64f39531350bde862cae35abd1a0` |
| `docs/monograph/prime-matrix-concrete-rankin-manifest-data-router.json` | `7e4fd3e653f18ab92f358a8f7f4dfe3db3c058c987109bdcf1795f3d374d961e` |
| `docs/monograph/prime-matrix-dstructure-rankin-promotion-acceptance-router.json` | `6a25a769df2b107f8a5a31e1374395d99717c4d0dd8188c969111477a648de7a` |
| `docs/monograph/prime-matrix-full-rankin-ledger-inventory-router.json` | `914416c71595e19675adf90d35301cd1f8648a17e67f9676211ab8a2f2f6187b` |
| `docs/monograph/prime-matrix-per-color-rankin-certificate-file-router.json` | `96396434ac61259eceff783f0b18da5523c1bd920e0e1661c2cc1471dcd631fe` |
| `docs/monograph/prime-matrix-strict-cold-product-support-sparsification-router.json` | `1dc6e98d6eb37c2571d0c3bdff385f66069b8812c6c1a9c8b97860b37cfc6f95` |
| `experiments/prime_matrix_strict_primitive_product_support_rankin_router.py` | `810e7e4dcc6abebb149811f9f46a01289dbf658e4e10a3b92ab2e22793e2b722` |
