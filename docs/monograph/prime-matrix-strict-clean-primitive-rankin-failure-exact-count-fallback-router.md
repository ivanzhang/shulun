# Prime Matrix strict clean primitive Rankin 失败精确计数 fallback 路由器

**状态：** `clean_primitive_rankin_failure_reduced_to_exact_count_fallback_table`

clean primitive 残项中必须先区分 Rankin 上界失败和实际支撑失败：`rankin_bound>P^0.18` 只说明该 Rankin 证书太松；若实际块计数仍不超过 `P^0.18`，该行应判为 `exact_count_pass`，不能生成回流包。当前诊断失败行全部属于这种情形。因此 `CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass` 被压缩为 `ExactPrimitiveBlockCountP018FallbackTable` 或逐块 sigma 表；全体 actual fallback 表仍未完成。

```text
rankin_failure_not_equivalent_to_support_failure_closed=true
exact_count_fallback_schema_closed=true
diagnostic_rankin_fail_rows_exact_count_pass=true
exact_primitive_block_count_p018_fallback_table_proved=false
row_column_unconditional_closed=false
```

## 1. 判定细化

| verdict | condition | effect |
| --- | --- | --- |
| `rankin_pass` | there exists sigma with rankin_bound<=P^0.18 | 直接由 Rankin 证书支付该块。 |
| `exact_count_pass` | rankin_bound>P^0.18 but exact block count<=P^0.18 | Rankin 失败只是上界松弛，不生成 return packet。 |
| `named_return` | exact block count>P^0.18 and one of the five packet triggers fires | 进入 PrimitiveProductRankinFailureReturnPacketLedger 的命名回流包。 |
| `clean_exact_overbudget` | exact block count>P^0.18 and no named trigger fires | 这才是真正 clean primitive 残项，进入精确计数表或推出矛盾。 |
| `payload_missing` | actual source_tuple/block/divisor list is absent | 不能判定，转入 ExactPrimitiveBlockCountP018FallbackTable。 |

## 2. fallback 表字段

| field | role |
| --- | --- |
| `source_tuple_hash` | 绑定早期零行反例 formal unit，防止诊断样本冒充 actual row。 |
| `block_id` | 绑定 dyadic 产品块 `(Y,2Y]` 和 no-return/cold guard。 |
| `divisor_count_exact_or_certified_cap` | 给出精确块计数，或给出可复核上界证书。 |
| `rankin_certificate_hash` | 保留原 Rankin 失败证书，说明 fallback 是处理上界松弛。 |
| `packet_trigger_vector` | 若精确计数仍超预算，登记五类回流触发是否发生。 |
| `refined_verdict` | `rankin_pass`、`exact_count_pass`、`named_return` 或 `clean_exact_overbudget`。 |

## 3. 诊断样本校验

| sample_row_id | Y | h0 | rankin_ratio | exact_count | floor(P^0.18) | refined_verdict |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| sample-1 | 16 | 2310 | 3.935239 | 3 | 7 | `exact_count_pass` |
| sample-2 | 64 | 2310 | 3.982899 | 5 | 7 | `exact_count_pass` |
| sample-3 | 64 | 4320 | 6.167526 | 6 | 7 | `exact_count_pass` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `CleanPrimitiveResidualTargetImported` | `true` | `true` | 上一层已把无名失败残项压成 clean primitive Rankin 失败。 | CleanPrimitiveDispersionRankinFailureExclusionOrSigmaPass |
| `RankinFailureNotSupportFailureSeparated` | `true` | `true` | Rankin 上界失败只说明证书松弛，不等价于实际块计数超预算。 | verdict refinement |
| `ExactCountFallbackSchemaClosed` | `true` | `true` | actual clean primitive 行必须先提交精确计数或可复核计数上界。 | ExactPrimitiveBlockCountP018FallbackTable |
| `DiagnosticRankinFailRowsExactCountPass` | `true` | `true` | 当前诊断样本的 Rankin 失败行全部由 exact_count_pass 消解，不需要回流包。 | diagnostic only |
| `GlobalExactPrimitiveBlockCountP018FallbackTableProved` | `false` | `false` | 尚未给出全体 actual clean primitive 块的精确计数 fallback 表。 | ExactPrimitiveBlockCountP018FallbackTable |
| `CleanPrimitiveDispersionRankinFailureExcludedOrSigmaPass` | `false` | `false` | 本步只删除 Rankin 失败=支撑失败 的错误等价；全局 clean exact overbudget 仍未排除。 | ExactPrimitiveBlockCountP018FallbackTable OR PerBlockRankinSigmaSelectionTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到排除早期零行反例链的终端矛盾。 | ExactPrimitiveBlockCountP018FallbackTable AND CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption AND SparseHistoryDemandExceedsNonpersistentSupplyBudget AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步最窄点

- 主攻：`ExactPrimitiveBlockCountP018FallbackTable`。
- 目标：对 actual clean primitive 块给出精确计数或可复核计数上界；只有 exact count 超预算且五类回流均不触发时，才是真正 clean residual。
- 边界：本步不把诊断 exact pass 升级为全体证明，不声明行/列命题无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/primitive-product-rankin-p018-sample-table.json` | `6ee83fd827a289762f17da0e458cc1fb7fcfbe64b862d7b1fef635133f06e551` |
| `data/primitive-product-rankin-weight-sample-ledger.json` | `79d8bcd52bc3ab367484ed2666f5dbfcae80ee87b53681d41d2df50132e2e3b1` |
| `docs/monograph/prime-matrix-strict-no-return-actual-dyadic-block-enumerator-router.json` | `3e4a65761bb62c0fff3f6614aedffd25ae31dda55b75295520a2eae1e3ce29ad` |
| `docs/monograph/prime-matrix-strict-primitive-product-rankin-failure-return-packet-router.json` | `f9732754d5a511c6da9dc3d382bf20ed9866c868a98f43450bfec50b6252cff7` |
| `docs/monograph/prime-matrix-strict-primitive-product-rankin-p018-table-router.json` | `01ac5c80037d76d59f0d127041d9105c694a553da6cb5f6466928b73c67985f6` |
| `experiments/prime_matrix_strict_clean_primitive_rankin_failure_exact_count_fallback_router.py` | `9eacf48ea35ffbbe6e51c396983c8d225c63bd68680a2be664b9d622b763ea73` |
