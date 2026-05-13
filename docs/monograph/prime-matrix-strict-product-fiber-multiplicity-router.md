# Prime Matrix strict 产品纤维重数/命名回流账本路由器

**状态：** `product_fiber_free_support_multiplicity_quotiented_named_drift_registered_divisor_envelope_open`

`ActivePrefixProductFiberMultiplicityOrNamedReturnLedger` 的支撑版已闭合：同一 formal unit 下同一产品 d 的顺序/形式前缀差异只给出同一个规范端点和同一个冷核心阈值键；同 key 多重命中是负载，不是新支撑；异 key、标签漂移或相位漂移必须登记为 PDEC/SAE/ColumnCRT/热核心/固定历史回流。因此产品纤维不能再作为免费支撑膨胀源。但这还没有证明最终活动前缀打包指数，因为商掉纤维后仍需控制真实 cold-filtered 产品除数支撑，并把同 key 负载、collar 总和与 T_PDEC 权重接入统一预算。

```text
product_fiber_canonical_endpoint_quotient_closed=true
same_product_permutation_new_support_excluded=true
same_product_same_key_multiplicity_routed_to_load=true
product_fiber_label_phase_drift_registered=true
active_prefix_product_fiber_multiplicity_or_named_return_ledger_closed_for_support=true
cold_filtered_divisor_support_p018_envelope_proved=false
active_prefix_level_packing_exponent_table_proved=false
row_column_unconditional_closed=false
```

## 1. 纤维分支

| case | condition | effect | route | status | meaning |
| --- | --- | --- | --- | --- | --- |
| same_product_same_canonical_key | D(U1)=D(U2)=d, same formal unit, same row-free/cold-core key | I_{U1}=I_{U2}, C_core(U1)=C_core(U2) | ProductFiberCanonicalEndpointQuotientLedger | closed_support_quotient | 乘法顺序或形式前缀差异不产生新的冷支撑窗口，只保留一个规范产品支撑。 |
| same_product_same_key_multiple_labels | same d and same key, but multiple prefix labels hit the same support | multiplicity becomes Load(d,key), not additional support | SameProductSameKeyMultiplicityToLoadOrNamedReturn | closed_routing_budget_numeric_open | 多重命中按负载守恒进入冷容量/统一预算；不能静默消失，也不能重复算作新支撑。 |
| same_product_label_or_phase_drift | same d, but row-free key, phase key, endpoint key, or formal unit changes | drift is a registered defect | ProductFiberLabelPhaseDriftNamedReturnLedger | registered_named_return | 若为了区分同产品前缀必须改变标签或相位，则它不是免费冷支撑，而是 PDEC/SAE/ColumnCRT/热核心/固定历史出口。 |
| same_product_hot_or_persistent_overload | Load(d,key) exceeds the registered cold capacity threshold | hot core, fixed history, or PDEC recurrence | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion | registered_not_excluded | 同产品纤维过载不能留在非持久冷支撑；但本步不排斥这些命名出口。 |
| different_product_support | d ranges over actual cold products dividing h_0 | support is counted by cold-filtered divisor products | ColdFilteredDivisorSupportP018Envelope | open | 产品纤维已商掉后，剩余主量是哪些产品除数真正冷且非持久可用。 |

## 2. 支撑商化恒等式

| object | formula | role | status |
| --- | --- | --- | --- |
| raw_prefix_count | \|A_j\|=sum_{d\|h_0}\|A_j(d)\| | load_identity | not_a_support_bound |
| canonical_support | S_j=supp{(d,key): U in A_j, D(U)=d, no named drift} | support_identity | closed_definition |
| same_fiber_quotient | many U with same (d,key) -> one support point plus Load(d,key) | fiber_multiplier_removed_from_support | closed |
| remaining_support_goal | \|S_j\| <= # cold-filtered products + registered key classes | next_envelope | open_numeric_envelope |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ProductFiberTargetImported` | `true` | `true` | 上一层已把活动前缀打包压到产品投影与产品纤维重数。 | ActivePrefixProductFiberMultiplicityOrNamedReturnLedger |
| `CanonicalEndpointQuotientInputsClosed` | `true` | `true` | 同产品的规范端点、旧窗口记号和冷核心注册键已经对齐；顺序差异不改变支撑窗口。 | ProductFiberCanonicalEndpointQuotientLedger |
| `SameProductPermutationNewSupportExcluded` | `true` | `true` | 同一 formal unit 下同一产品 d 的有序分解不会生成多个冷支撑点，只生成同一规范产品支撑。 | closed for support quotient |
| `SameProductSameKeyMultiplicityRoutedToLoad` | `true` | `true` | 同一产品同一 key 的多重前缀按负载守恒进入冷容量或统一预算，不再作为自由支撑膨胀因子。 | SameProductSameKeyMultiplicityToLoadOrNamedReturn |
| `ProductFiberLabelPhaseDriftRegistered` | `true` | `false` | 同产品但标签、相位或 formal-unit 键漂移时，必须进入命名回流桶；本步只完成登记，不排斥该桶。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ActivePrefixProductFiberMultiplicityOrNamedReturnLedgerClosedForSupport` | `true` | `true` | 产品纤维内的免费重数支撑爆炸被排除：同 key 商化为一个支撑，异 key/漂移进入命名回流。 | ColdFilteredDivisorSupportP018Envelope AND UnifiedTerminalBudgetStrictInequality |
| `ProductFiberMultiplicityNumericAbsorptionProved` | `false` | `false` | 同 key 的负载守恒已路由，但尚未在同参数最终预算中完成数值吸收。 | UnifiedTerminalBudgetStrictInequality AND SameParameterPDECThresholdNumericTable |
| `ColdFilteredDivisorSupportP018EnvelopeProved` | `false` | `false` | 商掉产品纤维后，仍需证明真实冷产品支撑满足 P^0.18 级 envelope；粗 tau(h_0) 已失败。 | DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope AND ColdNonpersistentProductSupportSparsificationLemma |
| `ActivePrefixLevelPackingExponentTableProved` | `false` | `false` | 本步关闭产品纤维免费膨胀，不关闭 cold-filtered 产品支撑、collar 总和和 T_PDEC 权重。 | ColdFilteredDivisorSupportP018Envelope AND SameParameterSiblingCollarWidthFiniteSumTable AND SameParameterPDECThresholdNumericTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的最终矛盾；不能声明行/列命题无条件闭合。 | ColdFilteredDivisorSupportP018Envelope AND UnifiedTerminalBudgetStrictInequality AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步最窄点

- 主攻：`ColdFilteredDivisorSupportP018Envelope`。
- 同步：`UnifiedTerminalBudgetStrictInequality`、`SameParameterSiblingCollarWidthFiniteSumTable`、`SameParameterPDECThresholdNumericTable`。
- 边界：本步只排除产品纤维免费支撑膨胀；不声明行/列命题无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/product-window-endpoint-generator-sample-ledger.json` | `7a8cd5b0992165d1967c2f9d025d276b1b72250c780fa445d03b47c428575a2b` |
| `docs/monograph/prime-matrix-strict-active-prefix-level-packing-router.json` | `c5ee2755b1acbab1168ec9f2dc5638d915ce1122c5068be73352077ddd6f3188` |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-function-table-router.json` | `17d7ee987e51872094edd8c3dc0210b6b87d4751d04864d5d66a162770f3cffc` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json` | `2c0a5401dc9e7f7158cd30e758f88f5a07f68460712f611452ff609ae3b7ddbb` |
| `docs/monograph/prime-matrix-strict-legacy-product-window-equivalence-router.json` | `d713760f063f00117cf6564c911523cf43033f612fb2d51e62a37425156f769e` |
| `docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json` | `818c17bd920eb69eaa05f2cca96099ad4637c8ab960afd843ec6a53872d392d3` |
| `docs/monograph/prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json` | `94229062234848b5e5e20ffaf940e7d4447b8ec957a0b3e8b2bf85d3e55a1a3f` |
| `docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.json` | `a1061abb510efd9743123d49a9e85775f9b27985a51957ab1b976ae3399e1a42` |
| `docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.json` | `f480a9407780a2cc2a9f8e6fc742d6f2db1fa6875fe3de58f687f585abef12e6` |
| `experiments/prime_matrix_strict_product_fiber_multiplicity_router.py` | `d6ccf2fff3a609444a0df49024c14901f9b225c4efed1366285077fc5dfa441a` |
