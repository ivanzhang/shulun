# Prime Matrix strict 同参数每层冷支撑指数表路由器

**状态：** `per_level_support_exponent_reduced_to_active_prefix_packing_open`

`SameParameterPerLevelColdSupportExponentTable` 继续下钻后，真正困难集中在同层活动前缀打包。对数深度已经消耗 `P^(1/4)`，`alpha=0.43` 只剩 `0.18` 的指数预算给每层冷支撑和 `T_PDEC` 权重；因此需要 `beta+tau<0.18`。现有材料能把单父兄弟收费分解为父投影支撑、collar debit 和命名回流，但不能阻止同层活动父前缀数本身达到 `P^0.2` 这类超预算规模。最新最窄点是 `ActivePrefixLevelPackingExponentTable`。

```text
per_level_support_target_imported=true
residual_exponent_budget_computed=true
per_level_charge_decomposition_closed=true
trivial_active_prefix_bound_rejected=true
collar_route_imported=true
same_parameter_per_level_cold_support_exponent_table_proved=false
row_column_unconditional_closed=false
```

## 1. 每层支撑分解

| piece | formula | status | meaning |
| --- | --- | --- | --- |
| `active prefix set` | A_j={U: depth(U)=j, U remains cold and nonpersistent} | `closed_definition` | 每层支撑必须先按活动父前缀集合打包。 |
| `base projected support` | B_j=sum_{U in A_j} \|pi(F_U)\| | `geometry_closed_numeric_open` | 同父兄弟支撑投影到父扩张窗口，但跨父前缀求和仍需打包。 |
| `collar debit` | C_j=sum_{U in A_j} C_col(U) | `cap_closed_sum_open` | 单 collar cap 已闭合，跨层/同层总和仍需有限和或 LCM 压缩。 |
| `overlap and persistence` | E_j=sum_U E_overlap(U)+E_persistent(U) | `named_return_registered` | 重复收费或持久历史不留在非持久冷支撑，进入命名回流。 |
| `per-level exponent target` | S_j=B_j+C_j <= P^beta with beta+tau<0.18 | `open` | 这是深度对数吸收后剩下的真正指数表。 |

## 2. 活动前缀阻塞

| gamma active prefixes | unit support | tau T_PDEC | required gamma+tau < | passes | margin |
| ---: | ---: | ---: | ---: | --- | ---: |
| 0.1 | 1 | 0.0 | 0.18 | `true` | 0.08 |
| 0.1 | 1 | 0.05 | 0.18 | `true` | 0.03 |
| 0.18 | 1 | 0.0 | 0.18 | `false` | 0.0 |
| 0.18 | 1 | 0.05 | 0.18 | `false` | -0.05 |
| 0.2 | 1 | 0.0 | 0.18 | `false` | -0.02 |
| 0.2 | 1 | 0.05 | 0.18 | `false` | -0.07 |
| 0.3 | 1 | 0.0 | 0.18 | `false` | -0.12 |
| 0.3 | 1 | 0.05 | 0.18 | `false` | -0.17 |

## 3. 路线拆分

| route | task | status |
| --- | --- | --- |
| `ActivePrefixLevelPackingExponentTable` | 证明同层活动父前缀的投影支撑不会以超过 P^(0.18-tau) 的指数增长。 | `open` |
| `SameParameterSiblingCollarWidthFiniteSumTable` | 证明 collar 宽度总和可直接有限求和吸收；否则沿 LCM/共同核回流。 | `open_or_routed` |
| `LowMultiplierCommonKernelColumnCRTOrPDECRoute` | 若活动前缀密集来自低乘子共同核，必须进入有界小商 SAE/PDEC 或固定历史。 | `registered_not_final_excluded` |
| `SameParameterPDECThresholdNumericTable` | 给出同参数持久阈值指数 tau；tau 越大，每层支撑可用指数越小。 | `open` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PerLevelSupportTargetImported` | `true` | `true` | 深度伸缩已把剩余压成每层冷支撑指数表。 | SameParameterPerLevelColdSupportExponentTable |
| `ResidualExponentBudgetComputed` | `true` | `true` | 对数因子 P^1/4 已扣除，alpha=0.43 剩余指数预算为 0.18。 | SameParameterPerLevelColdSupportExponentTable AND SameParameterPDECThresholdNumericTable |
| `PerLevelChargeDecompositionClosed` | `true` | `true` | 每层支撑可分解为活动前缀投影支撑、collar debit 与命名回流。 | ActivePrefixLevelPackingExponentTable AND SameParameterSiblingCollarWidthFiniteSumTable |
| `TrivialActivePrefixBoundRejected` | `true` | `true` | 若同层活动前缀数达到 P^0.2，即使每个只贡献 1 也超过剩余预算。 | ActivePrefixLevelPackingExponentTable |
| `CollarRouteImported` | `true` | `true` | collar 单项 cap 与宽度 LCM/共同核压缩已可调用，但直接同层有限总和仍未给出。 | SameParameterSiblingCollarWidthFiniteSumTable OR SiblingCollarWidthLCMKernelCompressionLedger |
| `SameParameterPerLevelColdSupportExponentTableProved` | `false` | `false` | 尚未证明活动前缀打包指数和 collar 同层总和满足 beta+tau<0.18。 | ActivePrefixLevelPackingExponentTable AND SameParameterSiblingCollarWidthFiniteSumTable AND SameParameterPDECThresholdNumericTable |
| `DepthTelescopingTableProved` | `false` | `false` | 每层指数表未闭合，因此深度伸缩无法升级为全深度加权支撑界。 | SameParameterPerLevelColdSupportExponentTable AND SameParameterPDECThresholdNumericTable |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的最终矛盾。 | ActivePrefixLevelPackingExponentTable AND SameParameterPDECThresholdNumericTable AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 5. 下一步最窄点

- 主攻：`ActivePrefixLevelPackingExponentTable`。
- 并行：`SameParameterSiblingCollarWidthFiniteSumTable`、`SameParameterPDECThresholdNumericTable`、`SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow`。
- 边界：本步关闭每层支撑的结构分解和指数预算门槛；未证明活动前缀打包指数。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-support-depth-telescoping-router.json` | `b68feb863ab061597333a2ef25c80e660e84db7d9a1bc352b94b3d1ba6e12570` |
| `docs/monograph/prime-matrix-strict-core-history-weighted-support-measure-router.json` | `2dd7639bfbaa615273487219d874098fb83b09636ad217369bb1b71df21bdf8b` |
| `docs/monograph/prime-matrix-strict-parent-support-numeric-envelope-router.json` | `c6fe6dcdc47b377c9a55915560031ec8b37d528f6d9980eedbce671a2ee8d653` |
| `docs/monograph/prime-matrix-strict-sibling-collar-cap-table-router.json` | `04affb2be59db89256bbc83cb022d0808a473268dff3de85d9f2230214a06b42` |
| `docs/monograph/prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json` | `973a1c986598cb27dd132354715b336eae7938103c89d09da451123f2ade08de` |
| `docs/monograph/prime-matrix-strict-sibling-numeric-envelope-attack-router.json` | `52bd322127d85f72df347da33b5ccc71b6ef2c023539db38244793e6d8d3448c` |
| `experiments/prime_matrix_strict_same_parameter_per_level_support_exponent_router.py` | `4797e6c686e221d4b5c69191d0ba84a6ae94813ebcecb5021dca285d32e70b21` |
