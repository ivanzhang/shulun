# Prime Matrix strict cold-filtered 产品除数支撑路由器

**状态：** `cold_filtered_support_domain_closed_prime_power_order_removed_raw_tau_and_sparsification_open`

`ColdFilteredDivisorSupportP018Envelope` 的支撑域已经压实：产品纤维商化后，素数幂有序级联不再产生 Fibonacci 型支撑爆炸，只剩同一产品除数状态。但全体除数函数在有限边界仍远超 P^0.18，不能用粗 tau(h_0) 关闭。因此当前最窄剩余是二选一：要么给出显式除数尾界加有限边界证书，要么证明 cold/nonpersistent/no-return 条件会把实际产品支撑稀疏化；局部集中失败已能登记为热除数密度/PDEC/SAE，分散失败则需要原始支撑 Rankin 账本。

```text
cold_filtered_support_domain_closed=true
prime_power_ordered_cascade_removed_for_support=true
raw_tau_p018_closure_rejected=true
cold_structural_failure_routes_registered=true
cold_filtered_divisor_support_p018_envelope_proved=false
active_prefix_level_packing_exponent_table_proved=false
row_column_unconditional_closed=false
```

## 1. 粗 tau 阻塞

| P or n | witness | tau | P^0.18 | passes | ratio |
| ---: | ---: | ---: | ---: | --- | ---: |
| 100000 | 83160 | 128 | 7.943282 | `false` | 16.114245 |
| 83160 | 83160 | 128 | 7.683951 | `false` | 16.658096 |
| 110880 | 110880 | 144 | 8.09233 | `false` | 17.794628 |
| 720720 | 720720 | 240 | 11.334386 | `false` | 21.174505 |
| 1081080 | 1081080 | 256 | 12.192546 | `false` | 20.996435 |

## 2. 素数幂支撑商化

| prime | max exp at P=100000 | ordered growth before quotient | support after quotient | P^0.18 | passes |
| ---: | ---: | --- | ---: | ---: | --- |
| 2 | 16 | exponential/Fibonacci depending on allowed blocks | 17 | 7.943282 | `false` |
| 3 | 10 | exponential/Fibonacci depending on allowed blocks | 11 | 7.943282 | `false` |
| 5 | 7 | exponential/Fibonacci depending on allowed blocks | 8 | 7.943282 | `false` |
| 7 | 5 | exponential/Fibonacci depending on allowed blocks | 6 | 7.943282 | `true` |
| 2 | all P>=75184381 | not relevant after product quotient | floor(log_2 P)+1 <= P^0.18 | threshold identity | `true` |

## 3. 剩余二分

| branch | condition | closed part | remaining | meaning |
| --- | --- | --- | --- | --- |
| pure_divisor_tail | use only # {d:d\|h_0} | product-fiber order multiplicity already quotiented | ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate | 需要显式除数函数尾界和有限边界证书；P=100000 附近粗界失败。 |
| cold_structural_sparsification | d must be cold, nonpersistent, and no named return | divisor compatibility, parent-window geometry, prefix structural dichotomy | ColdProductSupportSparsificationBeyondTauLedger | 必须证明真实冷产品远少于全体除数，而不是继续数 tau(h_0)。 |
| short_window_density_failure | too many products concentrate in a multiplicative window | reciprocal/count threshold produces hot density certificate | ShortWindowHotDivisorDensityPDECorSAEReturnExclusion | 集中失败会变成热频率除数窗口；仍需排斥 PDEC/SAE/ColumnCRT 出口。 |
| spread_primitive_rank | products avoid local concentration but use many independent primitive factors | free common-kernel return cycle excluded | PrimitiveProductSupportRankinLedger | 分散失败应由逐素数/Rankin 原始支撑账本吸收；该验收仍独立开放。 |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `ColdFilteredSupportTargetImported` | `true` | `true` | 上一层已商掉同产品纤维的免费支撑重数，剩余是 distinct cold products。 | ColdFilteredDivisorSupportP018Envelope |
| `ColdFilteredSupportDomainClosed` | `true` | `true` | 可计支撑已限制为 D\|h_0、父扩张窗口内、且未进入命名回流的 cold products。 | ColdProductSupportSparsificationBeyondTauLedger |
| `PrimePowerOrderedCascadeRemovedForSupport` | `true` | `true` | 产品商化后，素数幂有序历史爆炸只剩指数状态数；Fibonacci/order 爆炸不再是支撑爆炸。 | finite boundary for small P remains separate |
| `RawTauP018ClosureRejected` | `true` | `true` | P=100000 附近 tau(h_0) 仍可远大于 P^0.18；不能只用全体除数函数闭合。 | ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate |
| `ColdStructuralFailureRoutesRegistered` | `true` | `false` | 冷产品若局部集中或共同核回流，已有热窗口/PDEC/SAE/共同核下降路由；但这些出口未排斥。 | ShortWindowHotDivisorDensityPDECorSAEReturnExclusion AND PrimitiveProductSupportRankinLedger |
| `ColdFilteredDivisorSupportP018EnvelopeProved` | `false` | `false` | 尚未证明全体实际 cold products 的支撑数小于 P^0.18；需纯除数尾证书或冷结构稀疏化证书。 | ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate OR ColdProductSupportSparsificationBeyondTauLedger |
| `ActivePrefixLevelPackingExponentTableProved` | `false` | `false` | 产品支撑 envelope 未闭合，且还需 collar 总和与 T_PDEC 权重。 | ColdFilteredDivisorSupportP018Envelope AND SameParameterSiblingCollarWidthFiniteSumTable AND SameParameterPDECThresholdNumericTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链终端矛盾。 | ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate OR ColdProductSupportSparsificationBeyondTauLedger; plus UnifiedTerminalBudgetStrictInequality AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步最窄点

- 主攻：`ColdProductSupportSparsificationBeyondTauLedger`。
- 备选纯除数路线：`ExplicitDivisorSupportP018TailWithFiniteBoundaryCertificate`。
- 并行验收：`UnifiedTerminalBudgetStrictInequality`、`SameParameterSiblingCollarWidthFiniteSumTable`、`SameParameterPDECThresholdNumericTable`、`DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。
- 边界：本步不声明 cold-filtered 支撑 envelope 已证明。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-active-prefix-level-packing-router.json` | `c5ee2755b1acbab1168ec9f2dc5638d915ce1122c5068be73352077ddd6f3188` |
| `docs/monograph/prime-matrix-strict-cold-history-prefix-branching-attack-router.json` | `ec7b96227c0b8752620609589fb1367d7483f2c46db66c705a13e68523002e86` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-divisor-compatible-tree-packing-attack-router.json` | `dbc983163e64456b63a6be5e99375fabb7ddaf8aa17490fd9fdf42d664c6e129` |
| `docs/monograph/prime-matrix-strict-effective-cold-history-pruning-router.json` | `72d7aeeb5a09864efcb9cd729d4d5331b1adfb780ec33b3a1ae29dfe6e67431b` |
| `docs/monograph/prime-matrix-strict-parent-support-numeric-envelope-router.json` | `c6fe6dcdc47b377c9a55915560031ec8b37d528f6d9980eedbce671a2ee8d653` |
| `docs/monograph/prime-matrix-strict-product-fiber-multiplicity-router.json` | `207253ea5e911247addc82f0e59edfdf1d034a6591d762a9928b493792500d4a` |
| `docs/monograph/prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.json` | `9eef33defabab6ff2bddfd3627b5034984171d98db34e55d04cecee3b4d15f56` |
| `docs/monograph/prime-matrix-strict-windowed-reciprocal-divisor-density-router.json` | `1a367725b5a64d16447823d3bd619ac9955dd634eba4f31ad09326be20ccf57c` |
| `experiments/prime_matrix_strict_cold_filtered_divisor_support_router.py` | `c838cfb5a9b73be62f85950fcfe8e6fbbd508f9518815076d438a1ef4bd868f3` |
