# Prime Matrix strict 回流后同参数稀疏余量同步路由器

**状态：** `same_parameter_sparse_margin_after_return_cycle_reduced_to_cold_numeric_open`

`SameParameterSparseDemandColdSupplyStrictMarginCertificate` 已吸收共同核回流后的新事实：非持久共同核不能免费循环，非持久命名回流也不能另开 E_named 扣除，只能进入同参数 U_np。因此在纯非持久侧，严格余量的内部剩余等价压成 `ColdSupplySameParameterNumericEnvelope`：证明同一参数账本下 `U_np<=sum_W(T_PDEC(W)-1)C_core(W)` 的数值上界足够小。热核心、固定历史和持久命名回流仍是并行命名出口；本步不证明最终正余量。

```text
unified_after_return_cycle_target_imported=true
no_free_return_cycle_imported=true
old_same_parameter_margin_reduction_imported=true
nonpersistent_lane_no_hidden_deduction_closed=true
same_parameter_sparse_margin_after_return_cycle_reduced=true
cold_supply_same_parameter_numeric_envelope_proved=false
same_parameter_sparse_demand_cold_supply_strict_margin_proved=false
row_column_unconditional_closed=false
```

## 1. 字段

| field | formula | status |
| --- | --- | --- |
| demand | M#_{x,z} or D_prefix under the same z,D,lambda ledger | available under current standard/external lower-sieve contract |
| nonpersistent returns | absorbed into U_np, not a separate E_named deduction | schema closed after no-free-return-cycle |
| cold supply | U_np <= sum_W (T_PDEC(W)-1) C_core(W) | formula closed; numeric envelope open |
| strict margin | M#_{x,z} > U_np in the pure nonpersistent lane | equivalent to ColdSupplySameParameterNumericEnvelope plus numeric dominance |

## 2. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `UnifiedAfterReturnCycleTargetImported` | `true` | `true` | 最新统一预算同步已把非持久侧主攻点指向同参数稀疏余量。 | SameParameterSparseDemandColdSupplyStrictMarginCertificate |
| `NoFreeReturnCycleImported` | `true` | `true` | 非持久共同核回流不能再作为免费循环吞掉余量。 | CommonKernelReturnCycleDescentOrPDECLedger |
| `OldSameParameterMarginReductionImported` | `true` | `true` | 旧同参数余量证书已经把内部缺口压到冷供给数值包。 | ColdSupplySameParameterNumericEnvelope |
| `NonpersistentLaneNoHiddenDeductionClosed` | `true` | `true` | 非持久命名回流只能进入 U_np 预算；不能另开 E_named 或共同核循环。 | ColdSupplySameParameterNumericEnvelope |
| `SameParameterSparseMarginAfterReturnCycleReduced` | `true` | `true` | 回流后的非持久内部余量已等价压到冷供给数值包。 | ColdSupplySameParameterNumericEnvelope |
| `ColdSupplySameParameterNumericEnvelopeProved` | `false` | `false` | 仍缺 C_core/T_PDEC/有效剪枝给出的同参数数值上界。 | ColdSupplySameParameterNumericEnvelope |
| `SameParameterSparseDemandColdSupplyStrictMarginProved` | `false` | `false` | 结构等价闭合，但数值反超尚未证明。 | ColdSupplySameParameterNumericEnvelope |
| `PersistentNamedReturnStillParallel` | `false` | `false` | 持久命名回流不属于非持久余量包，仍需单独排斥。 | NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的终端矛盾。 | ColdSupplySameParameterNumericEnvelope AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 3. 下一步最窄点

- 主攻：`ColdSupplySameParameterNumericEnvelope`。
- 含义：给出同参数 C_core/T_PDEC/有效剪枝数值包，使非持久冷供给小于需求。
- 边界：持久命名出口仍并行开放，不能由非持久余量包吸收。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json` | `7c34a1965c8ddc44a43cafb902ae668fb7ed21db3fc6f73cb42716be37c213be` |
| `docs/monograph/prime-matrix-strict-cold-core-threshold-budget-gap-router.json` | `dc5db9c8aa57f3b8c29354615714c6c124f8b8326b288d3b8c7cccec57db62cf` |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json` | `86ba2fbc9abd9d917a940525fde0a9db0dd4e70ee94f745a56382fee896d8255` |
| `docs/monograph/prime-matrix-strict-common-kernel-return-cycle-descent-router.json` | `133a5b59827c92d7e6e3b2cefcadf6f8c67b5b999fa6a1b5e7cbda57b8d4e671` |
| `docs/monograph/prime-matrix-strict-named-return-same-parameter-deduction-router.json` | `2eee9f35708971c2d184bcc194c94c6be162a4f928834f628380ed747a45e1df` |
| `docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-attack-router.json` | `b5d97d9049f35ae7649c8d27932977e68c162e97373651f96fe4d97c90619447` |
| `docs/monograph/prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json` | `0b1f76cce75b61929c79f82036782b10d6c1755b84840de0e666224ad5ae7922` |
| `experiments/prime_matrix_strict_same_parameter_sparse_margin_after_return_cycle_router.py` | `a42c058a08989055593dee608507f83a64cbdc4b8fd68958da72e7c6167554e7` |
