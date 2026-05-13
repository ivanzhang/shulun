# Prime Matrix strict 活动前缀产品纤维重数路由器

**状态：** `product_fiber_multiplicity_compressed_to_canonical_product_support_and_named_return_open`

`ActivePrefixProductFiberMultiplicityOrNamedReturnLedger` 的裸计数形态不能成立：同一产品 `d=2^a` 的有序分解数已经在边界样本中远超 `P^0.18`，所以不能把产品纤维重数当成可直接求和的冷容量。本步关闭的是无名 overcount：product-window 端点外向缩放只依赖总乘积，同产品内的顺序/括号冗余必须商化为规范产品类；若内部顺序改变了相位、标签、窗口或 cold guard，差异就不是自由容量，而是固定历史、PDEC/SAE、ColumnCRT、热核心或标签回流。因此产品纤维不再是独立裸硬点；真正剩余转为 `ColdNonpersistentProductSupportSparsificationLemma`：证明通过 cold/nonpersistent guard 的规范产品类本身足够稀疏，并并行排斥命名回流。

```text
product_fiber_target_imported=true
raw_product_fiber_overcount_certified=true
product_endpoint_quotient_closed=true
row_free_and_sparse_no_silent_collapse_imported=true
duplicate_complete_key_routes_to_named_return=true
product_fiber_multiplicity_independent_hardpoint_removed=true
active_prefix_product_fiber_multiplicity_or_named_return_ledger_proved=false
row_column_unconditional_closed=false
```

## 1. 裸纤维阻塞

| P | a=floor(log2 P) | all ordered | one/two step | P^0.18 | all over | one/two over |
| ---: | ---: | ---: | ---: | ---: | --- | --- |
| 100000 | 16 | 32768 | 1597 | 7.943282 | `true` | `true` |
| 1000000 | 19 | 262144 | 6765 | 12.022644 | `true` | `true` |
| 10000000 | 23 | 4194304 | 46368 | 18.197009 | `true` | `true` |
| 1000000000 | 29 | 268435456 | 832040 | 41.686938 | `true` | `true` |

## 2. 端点交换样本

| left | right | a | b | left seq | left once | right seq | right once | commutes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1000 | 1234 | 2 | 8 | 62 | 62 | 78 | 78 | `true` |
| 1000 | 1234 | 3 | 5 | 66 | 66 | 83 | 83 | `true` |
| 98765 | 100001 | 6 | 10 | 1646 | 1646 | 1667 | 1667 | `true` |

## 3. 商化字典

| piece | formula | status | meaning |
| --- | --- | --- | --- |
| `raw product fiber` | A_j(d)={U in A_j: D(U)=d} | `closed_definition` | 裸纤维按同一产品除数 d 分组；它仍含有有序分解和内部标签冗余。 |
| `canonical endpoint quotient` | I_U=I(d) after outward product-window scaling, unless a boundary phase defect is registered | `closed_or_named_return` | 端点生成器满足外向缩放结合律；若旧记号或边界字段不服从，则进入相位缺陷回流。 |
| `row-free type quotient` | A_j(d)=disjoint union_kappa A_j(d,kappa) | `closed_reduction` | 同产品内继续按 row-free type、标签骨架、窗口相位和 cold guard 商化。 |
| `duplicate complete key` | \|A_j(d,kappa)\|>1 with complete key preserved -> fixed history / PDEC / ColumnCRT | `named_return_registered` | 完整 key 下的重复不能作为多个免费冷前缀；它就是固定历史或持久相位复现。 |
| `many distinct kappa` | #kappa large -> row-free/sparse anti-collapse budget or named return | `budget_route_open` | 若不是完整 key 重复，而是大量不同类型，则负载没有消失，回到 cold-filtered 产品支撑。 |

## 4. 路线拆分

| route | status | task |
| --- | --- | --- |
| `CanonicalProductClassSupportP018OrColdSparsificationLedger` | `open` | 对规范产品类而非有序分解求支撑；证明 cold/nonpersistent 过滤后其数量满足 P^(0.18-tau) 级预算。 |
| `ColdNonpersistentProductSupportSparsificationLemma` | `open` | 证明大多数 d\|h_0 无法同时通过 cold guard、非持久 guard 与同层活动 guard。 |
| `NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion` | `registered_not_excluded` | 排斥或预算吸收完整 key 重复、标签丢失、边界相位漂移、固定历史和热核心回流。 |
| `DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope` | `parallel_open` | 给出规范产品支撑的有限边界或解析 envelope；不能再使用裸 tau(h_0) 粗界。 |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ProductFiberTargetImported` | `true` | `true` | 上一层已把活动前缀层打包的首要剩余指向同产品纤维重数。 | ActivePrefixProductFiberMultiplicityOrNamedReturnLedger |
| `RawProductFiberOvercountCertified` | `true` | `true` | 裸有序分解纤维在 dyadic 样本中远超 P^0.18，不能作为容量上界。 | ActivePrefixProductFiberMultiplicityOrNamedReturnLedger |
| `ProductEndpointQuotientClosed` | `true` | `true` | product-window 外向缩放端点只依赖总乘积；端点顺序冗余可商化。 | CanonicalProductClassSupportP018OrColdSparsificationLedger |
| `DuplicateCompleteKeyRoutesToNamedReturn` | `true` | `false` | 同产品、同完整 key 的重复是固定历史/PDEC/ColumnCRT/热核心回流，不是免费冷容量。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ProductFiberMultiplicityIndependentHardpointRemoved` | `true` | `true` | 产品纤维重数不再作为独立裸计数；已压成规范产品支撑、cold 过滤和命名回流排斥。 | CanonicalProductClassSupportP018OrColdSparsificationLedger AND ColdNonpersistentProductSupportSparsificationLemma AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ActivePrefixProductFiberMultiplicityLedgerProved` | `false` | `false` | 路由和商化闭合，但命名回流排斥与 cold-filtered 产品支撑数值界未闭合。 | CanonicalProductClassSupportP018OrColdSparsificationLedger AND ColdNonpersistentProductSupportSparsificationLemma AND NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion |
| `ActivePrefixLevelPackingExponentTableProved` | `false` | `false` | 仍需规范产品支撑 envelope、collar 总和和同参数 T_PDEC 权重。 | CanonicalProductClassSupportP018OrColdSparsificationLedger AND ColdNonpersistentProductSupportSparsificationLemma AND SameParameterPDECThresholdNumericTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的最终矛盾。 | CanonicalProductClassSupportP018OrColdSparsificationLedger AND ColdNonpersistentProductSupportSparsificationLemma AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一步

- 主攻：`ColdNonpersistentProductSupportSparsificationLemma`。
- 边界：本步删除的是裸产品纤维重数作为独立免费容量的可能性；没有排斥全部命名回流，也没有闭合最终行/列命题。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-active-prefix-level-packing-router.json` | `c5ee2755b1acbab1168ec9f2dc5638d915ce1122c5068be73352077ddd6f3188` |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json` | `c93a11c1f9f9a11728fb454eb16ead7a4cc308bdfcf2647af6dcb20d6f405602` |
| `docs/monograph/prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json` | `defb123fedb4526b578e6dc01d989c696788e013fcd9db77f4b0f609186c52ea` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json` | `2c0a5401dc9e7f7158cd30e758f88f5a07f68460712f611452ff609ae3b7ddbb` |
| `docs/monograph/prime-matrix-strict-legacy-product-window-equivalence-router.json` | `d713760f063f00117cf6564c911523cf43033f612fb2d51e62a37425156f769e` |
| `docs/monograph/prime-matrix-strict-named-return-after-rowfree-sync-router.json` | `818c17bd920eb69eaa05f2cca96099ad4637c8ab960afd843ec6a53872d392d3` |
| `docs/monograph/prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json` | `94229062234848b5e5e20ffaf940e7d4447b8ec957a0b3e8b2bf85d3e55a1a3f` |
| `docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.json` | `a1061abb510efd9743123d49a9e85775f9b27985a51957ab1b976ae3399e1a42` |
| `docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.json` | `f480a9407780a2cc2a9f8e6fc742d6f2db1fa6875fe3de58f687f585abef12e6` |
| `experiments/prime_matrix_strict_active_prefix_product_fiber_multiplicity_router.py` | `4bf1ea0cedd0df3a66f8926eb1abad6f3d45e443177b041cedb9fd0333c2df42` |
