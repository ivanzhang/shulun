# Prime Matrix strict 活动前缀层打包指数路由器

**状态：** `active_prefix_packing_reduced_to_product_fiber_and_divisor_envelope_open`

`ActivePrefixLevelPackingExponentTable` 已被压成产品投影问题。每个活动前缀 `U` 给出 `D(U)|h_0`，同层活动数满足 `|A_j|=sum_{d|h_0}|A_j(d)|`。因此必须同时控制产品除数支撑和同一产品纤维重数。粗除数函数界不能关闭本目标：在 `P=100000` 边界内，`tau(83160)=128`，而 `P^0.18≈7.94`，远远超预算。所以最新最窄点不是继续调常数，而是 `ActivePrefixProductFiberMultiplicityOrNamedReturnLedger`：证明同一产品下多前缀若过大，必进入固定历史、PDEC/SAE、ColumnCRT、热核心或标签回流；并配合 cold-filtered 产品支撑 envelope。

```text
active_packing_target_imported=true
product_projection_closed=true
packing_identity_closed=true
raw_divisor_p018_bound_rejected_at_boundary=true
no_silent_collapse_imported_for_fibers=true
active_prefix_level_packing_exponent_table_proved=false
row_column_unconditional_closed=false
```

## 1. 产品投影

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `product_projection` | Phi(U)=D(U)=prod_i g_i, with D(U)\|h_0 | `closed_interface` | 每个活动前缀投影到同一 formal unit 的一个产品除数。 |
| `level_product_fiber` | A_j(d)={U in A_j: D(U)=d} | `closed_definition` | 同层活动前缀数分解为产品支撑数与每个产品纤维重数。 |
| `packing_identity` | \|A_j\|=sum_{d\|h_0} \|A_j(d)\| | `closed_identity` | 活动前缀打包必须同时控制产品支撑和纤维重数。 |
| `fiber_named_return_gate` | large \|A_j(d)\| -> same product/type recurrence -> named PDEC/SAE/ColumnCRT/hot return | `registered_not_proved` | 同一产品下多前缀若不可区分，不能作为自由冷支撑；但全局排斥未完成。 |

## 2. 粗除数界阻塞

| limit/P | witness n | tau | P^0.18 | raw bound passes | ratio |
| ---: | ---: | ---: | ---: | --- | ---: |
| 100000 | 83160 | 128 | 7.943282 | `false` | 16.114245 |
| 83160 | 83160 | 128 | 7.683951 | `false` | 16.658096 |
| 110880 | 110880 | 144 | 8.09233 | `false` | 17.794628 |
| 720720 | 720720 | 240 | 11.334386 | `false` | 21.174505 |
| 1081080 | 1081080 | 256 | 12.192546 | `false` | 20.996435 |

## 3. 路线拆分

| route | task | status |
| --- | --- | --- |
| `ActivePrefixProductFiberMultiplicityOrNamedReturnLedger` | 证明同一产品 d 的活动前缀纤维若过大，必形成固定历史、PDEC/SAE、ColumnCRT、热核心或 row-free 标签回流。 | `open` |
| `DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope` | 给出产品除数支撑的 P^0.18 级有限/解析 envelope；粗 tau(h_0) 界在 P=100000 边界失败。 | `open` |
| `ColdNonpersistentProductSupportSparsificationLemma` | 利用 cold/nonpersistent 条件删去大多数产品除数，而不是对所有 d\|h_0 求和。 | `open` |
| `SameParameterSiblingCollarWidthFiniteSumTable` | 活动前缀数一旦可控，还需同步控制同层 collar debit 总和。 | `parallel_open` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ActivePackingTargetImported` | `true` | `true` | 上一层已把每层冷支撑指数表压成活动前缀层打包。 | ActivePrefixLevelPackingExponentTable |
| `ProductProjectionClosed` | `true` | `true` | 每个活动前缀投影到产品除数 D(U)\|h_0。 | ActivePrefixLevelPackingExponentTable |
| `PackingIdentityClosed` | `true` | `true` | \|A_j\|=sum_{d\|h_0}\|A_j(d)\|，必须同时控制除数支撑和产品纤维。 | ActivePrefixProductFiberMultiplicityOrNamedReturnLedger AND DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope |
| `RawDivisorP018BoundRejectedAtBoundary` | `true` | `true` | P=100000 附近 tau(h_0) 可远大于 P^0.18，不能只靠 D(U)\|h_0。 | DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope OR ColdNonpersistentProductSupportSparsificationLemma |
| `NoSilentCollapseImportedForFibers` | `true` | `true` | 标签塌缩不会让义务消失；同产品多前缀必须进入负载、冷供给或命名回流。 | ActivePrefixProductFiberMultiplicityOrNamedReturnLedger |
| `ActivePrefixLevelPackingExponentTableProved` | `false` | `false` | 尚未证明产品纤维重数和 cold-filtered 除数支撑满足 P^(0.18-tau) 指数界。 | ActivePrefixProductFiberMultiplicityOrNamedReturnLedger AND DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope AND ColdNonpersistentProductSupportSparsificationLemma |
| `SameParameterPerLevelColdSupportExponentTableProved` | `false` | `false` | 活动前缀打包、collar 总和和 T_PDEC 权重仍未全部闭合。 | ActivePrefixLevelPackingExponentTable AND SameParameterSiblingCollarWidthFiniteSumTable AND SameParameterPDECThresholdNumericTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的最终矛盾。 | ActivePrefixProductFiberMultiplicityOrNamedReturnLedger AND DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步最窄点

- 主攻：`ActivePrefixProductFiberMultiplicityOrNamedReturnLedger`。
- 并行：`DivisorSupportP018FiniteBoundaryOrAnalyticEnvelope`、`ColdNonpersistentProductSupportSparsificationLemma`、`SameParameterSiblingCollarWidthFiniteSumTable`、`SameParameterPDECThresholdNumericTable`。
- 边界：本步关闭产品投影和粗除数界阻塞审查；未证明活动前缀打包指数。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-formal-unit-sparse-history-multiplicity-router.json` | `2c0a5401dc9e7f7158cd30e758f88f5a07f68460712f611452ff609ae3b7ddbb` |
| `docs/monograph/prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json` | `94229062234848b5e5e20ffaf940e7d4447b8ec957a0b3e8b2bf85d3e55a1a3f` |
| `docs/monograph/prime-matrix-strict-row-free-type-anticollapse-sync-router.json` | `f480a9407780a2cc2a9f8e6fc742d6f2db1fa6875fe3de58f687f585abef12e6` |
| `docs/monograph/prime-matrix-strict-same-parameter-per-level-support-exponent-router.json` | `5ebdc22eb78889400955a3bb60261e6757c64bb64a27c14600f7eb9d329c606e` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-history-router.json` | `6cbb750d3888d20ef1c7267231ddfb8490b1efc92b0edda308ec96f1d40905b2` |
| `experiments/prime_matrix_strict_active_prefix_level_packing_router.py` | `f40ab581ce559296d67518ff8108236b8556ece86b719dfad3d5b55bed46f030` |
