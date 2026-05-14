# Prime Matrix inverse alignment 残洞 atom 权重压缩路由器

**状态：** `residual_atom_weight_compression_imported_strict_margin_open`

`ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger` 不应再被当作新的 raw 删除命题。上一层的整数缺口 `floor(|R_{x,z}|-M#)+1` 只说明：若把残洞已分配 atom 继续按单位权留在 raw supply 中，必然无法低于 M#。但主线早已把这些 atom 通过容量乘子归一化为 `M#=sum 1/mu_tau` 的加权义务；无法进入该weighted ledger 的部分必须登记为命名回流。因此残洞 atom 权重压缩作为独立硬点已移除，真正剩余回到同参数严格余量 `M#-E_registered>U_np`。

```text
msharp_weighted_source_imported=true
no_loss_or_named_return_imported=true
same_parameter_sparse_demand_cold_supply_normal_form_imported=true
residual_atom_weight_compression_closed_as_measure_change=true
same_parameter_sparse_demand_cold_supply_strict_margin_proved=false
row_column_unconditional_closed=false
```

## 1. 换尺审计表

| P | X(P) | z | assigned units | M# | raw-M# | integer gap | formula ok |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `168` | `3` | `4` | `2.666666666667` | `1.333333333333` | `2` | `true` |
| `17` | `1210` | `3` | `5` | `3.166666666667` | `1.833333333333` | `2` | `true` |
| `19` | `3658` | `3` | `6` | `2.666666666667` | `3.333333333333` | `4` | `true` |
| `23` | `58` | `3` | `7` | `3.566666666667` | `3.433333333333` | `4` | `true` |
| `29` | `5209` | `4` | `9` | `3.233333333333` | `5.766666666667` | `6` | `true` |
| `31` | `60794` | `4` | `10` | `4.0` | `6.0` | `7` | `true` |
| `37` | `73916` | `4` | `12` | `4.595238095238` | `7.404761904762` | `8` | `true` |
| `41` | `170880` | `4` | `13` | `5.041666666667` | `7.958333333333` | `8` | `true` |
| `43` | `162932` | `5` | `11` | `4.916666666667` | `6.083333333333` | `7` | `true` |

## 2. 命题接口

| name | status | statement |
| --- | --- | --- |
| `residual_atom_unit_gap_identified` | `closed` | after direct suffix deletion, the remaining raw unit count is \|R_xz\|, while the budget demand is M#. |
| `capacity_multiplier_weight_normalization` | `closed_by_imported_Msharp_ledger` | each assigned residual atom contributes 1/mu_tau to M#, not one raw supply unit. |
| `integer_residual_deletion_gap` | `closed_as_wrong_measure_artifact` | floor(\|R_xz\|-M#)+1 is the extra deletion required only if assigned atoms are incorrectly kept at unit weight. |
| `named_return_boundary` | `closed_as_no_loss_or_named_return` | mass not entering the weighted sparse terminal ledger must be registered as PDEC/SAE/ColumnCRT/hot/fixed/quotient return. |
| `same_parameter_strict_margin` | `open` | the true remaining inequality is M# - E_registered > U_np under the same parameter ledger. |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DeletionMapImported` | `true` | `true` | 上一层已把 raw suffix 删除量拆成直接后缀冗余与残洞已分配 atom。 | ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger |
| `MsharpWeightedSourceImported` | `true` | `true` | prefix 残洞到 M# 的容量乘子归一化已经在主线账本闭合。 | SameParameterSparseDemandColdSupplyStrictMarginCertificate |
| `NoLossOrNamedReturnImported` | `true` | `true` | 不能进入 weighted sparse terminal ledger 的质量只能命名回流，不能作为免费冷供给。 | SameParameterSparseDemandColdSupplyStrictMarginCertificate |
| `ResidualCompressionIndependentHardpointRemoved` | `true` | `true` | 残洞 atom 的“额外删除量”是 raw 单位尺误差；正确预算已使用 M# reciprocal 权重。 | SameParameterSparseDemandColdSupplyStrictMarginCertificate |
| `SameParameterStrictMarginProved` | `false` | `false` | 尚未证明 M# 扣除命名回流后严格大于非持久 cold supply。 | SameParameterSparseDemandColdSupplyStrictMarginCertificate |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 同参数严格余量、热/固定出口、持久 moving atom 和 DStructure/Rankin 仍未全部闭合。 | SameParameterSparseDemandColdSupplyStrictMarginCertificate AND TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一步

- 主攻：`SameParameterSparseDemandColdSupplyStrictMarginCertificate`。
- 具体任务：在同一 `x,z,M#` 参数下给出 `M#-E_registered>U_np`，或者证明失败必进入热核心、固定历史、PDEC/SAE、持久 moving atom 或 DStructure/Rankin 验收门。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-inverse-alignment-latest-frontier-sync-router.json` | `ff08e13fd2dbbd7dbbdaf7a1648fc8f339cd2e52eec84a5ba3a0df7873c05d9c` |
| `docs/monograph/prime-matrix-inverse-alignment-overlap-slack-deletion-map-router.json` | `aab2d0b36efaea80ba1bc26cac797fef5785f35ea82610f11b752d097ed7f965` |
| `docs/monograph/prime-matrix-inverse-alignment-prefix-demand-bridge-router.json` | `369bf801b153a8cb792ef4a0971d5156020eb6604c2cdd31808d81cd4770c70a` |
| `docs/monograph/prime-matrix-strict-forced-obligation-lower-bound-router.json` | `0ed72910957c08af8ef93e950899e431fb6600b2b9efe685120c2d95fbb63b8b` |
| `docs/monograph/prime-matrix-strict-sparse-budget-after-unified-sync-router.json` | `70ca92ae2e350fdeba4eb1d386a9c31835da97f91a7252e3d0fee445a0e79f08` |
| `docs/monograph/prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json` | `3fabe3f3825c980842551045d9ca8714df0b3bb6fd1b92e39ba5e7e70daea1af` |
| `experiments/prime_matrix_inverse_alignment_residual_atom_weight_compression_router.py` | `a0a106b9fea78e06aa02caf8a7c91cc581b7d633194d4eb8317115ae5ab68ca2` |
