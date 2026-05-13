# Prime Matrix strict 冷支撑深度伸缩/对数吸收路由器

**状态：** `depth_telescoping_reduced_to_per_level_support_exponent_open`

`ColdSupportDepthTelescopingContractionOrLogAbsorptionTable` 可关闭两个基础环节：实际历史深度至多 `floor(log_2 P)+1`，且在 `P>=100000` 时该对数因子可由 `P^(1/4)` 显式吸收。但现有兄弟收费/父支撑投影账本没有给出统一严格收缩 `S_{j+1}<=qS_j(q<1)`；因此不能把全深度支撑直接压成根势能。剩余变成清晰的同参数指数条件：若每层冷支撑 `S_level<=P^beta` 且 `T_PDEC<=P^tau`，需要 `beta+tau+1/4<0.43`。最新最窄点是 `SameParameterPerLevelColdSupportExponentTable`。

```text
depth_telescoping_target_imported=true
depth_cap_log_p_closed=true
explicit_log_quarter_absorption_closed=true
strict_contraction_not_available_certified=true
log_absorption_criterion_closed=true
same_parameter_per_level_cold_support_exponent_table_proved=false
cold_support_depth_telescoping_contraction_or_log_absorption_table_proved=false
row_column_unconditional_closed=false
```

## 1. 伸缩公式

| name | formula | status | meaning |
| --- | --- | --- | --- |
| `strict_depth_cap` | depth(W)<=floor(log_2 h_0)<=floor(log_2 P) | `closed` | 每一步乘子至少为 2，因此历史深度至多对数级。 |
| `explicit_log_absorption` | floor(log_2 P)+1 <= P^(1/4) for P>=100000 | `closed` | 对数深度可转成一个显式 P^0.25 预算损耗。 |
| `single_layer_to_all_depths` | Sigma_support <= (floor(log_2 P)+1) * max_level S_level + named returns | `closed_as_reduction` | 若无严格收缩，最保守的全深度代价是一个对数因子。 |
| `weighted_log_absorption_criterion` | if S_level<=P^beta and T_PDEC<=P^tau and beta+tau+1/4<alpha, then weighted support < P^alpha | `closed_criterion` | 最终只需每层支撑指数和 PDEC 权重留出 alpha-1/4 的余量。 |
| `strict_contraction` | S_{j+1} <= q S_j with q<1 | `not_proved` | 现有兄弟投影账本只有非扩张/收费，不含统一 q<1 收缩。 |

## 2. 对数吸收核验

| P | depth cap | P^1/4 | absorbed | margin |
| ---: | ---: | ---: | --- | ---: |
| 100000 | 17 | 17.782794 | `true` | 0.782794 |
| 300000 | 19 | 23.403473 | `true` | 4.403473 |
| 1000000 | 20 | 31.622777 | `true` | 11.622777 |
| 10000000 | 24 | 56.234133 | `true` | 32.234133 |
| 1000000000 | 30 | 177.827941 | `true` | 147.827941 |

## 3. 指数预算

| beta support | tau T_PDEC | log epsilon | total | below alpha | margin |
| ---: | ---: | ---: | ---: | --- | ---: |
| 0.1 | 0.05 | 0.25 | 0.4 | `true` | 0.03 |
| 0.12 | 0.05 | 0.25 | 0.42 | `true` | 0.01 |
| 0.15 | 0.03 | 0.25 | 0.43 | `false` | 0.0 |
| 0.18 | 0.0 | 0.25 | 0.43 | `false` | 0.0 |
| 0.2 | 0.0 | 0.25 | 0.45 | `false` | -0.02 |

## 4. 无严格收缩见证

| level | S_level | S_next | nonexpansion valid | strict contraction needed | witness fails strict contraction |
| ---: | ---: | ---: | --- | --- | --- |
| 1 | 1 | 1 | `true` | <1 | `true` |
| 2 | 1 | 1 | `true` | <1 | `true` |
| 3 | 1 | 1 | `true` | <1 | `true` |
| 4 | 1 | 1 | `true` | <1 | `true` |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `DepthTelescopingTargetImported` | `true` | `true` | 上一层已把加权支撑测度的最窄剩余压成跨层深度伸缩。 | ColdSupportDepthTelescopingContractionOrLogAbsorptionTable |
| `DepthCapLogPClosed` | `true` | `true` | 历史深度至多 floor(log_2 P)+1。 | ColdSupportDepthTelescopingContractionOrLogAbsorptionTable |
| `ExplicitLogQuarterAbsorptionClosed` | `true` | `true` | 在 P>=100000 下，对数深度可被 P^1/4 吸收。 | SameParameterPerLevelColdSupportExponentTable AND SameParameterPDECThresholdNumericTable |
| `StrictContractionNotAvailableCertified` | `true` | `true` | 现有单层 sibling envelope 不含统一 q<1 收缩，不能直接 telescope 成根势能。 | SameParameterPerLevelColdSupportExponentTable |
| `LogAbsorptionCriterionClosed` | `true` | `true` | 若每层支撑指数 beta 和 T_PDEC 指数 tau 满足 beta+tau+1/4<0.43，则深度因子可吸收。 | SameParameterPerLevelColdSupportExponentTable AND SameParameterPDECThresholdNumericTable |
| `PerLevelColdSupportExponentTableProved` | `false` | `false` | 尚未证明每层实际冷支撑有 beta<0.18-tau 的同参数指数界。 | SameParameterPerLevelColdSupportExponentTable |
| `ColdSupportDepthTelescopingTableProved` | `false` | `false` | 对数吸收判据已闭合，但缺每层支撑指数和 T_PDEC 权重表。 | SameParameterPerLevelColdSupportExponentTable AND SameParameterPDECThresholdNumericTable |
| `CoreHistoryWeightedSupportMeasureTableProved` | `false` | `false` | 深度伸缩、T_PDEC 权重和有限 runner 未全部闭合。 | ColdSupportDepthTelescopingContractionOrLogAbsorptionTable AND SameParameterPDECThresholdNumericTable AND FiniteColdHistorySummationRunnerOrAnalyticEnvelope |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 仍未得到早期零行反例链的最终矛盾。 | SameParameterPerLevelColdSupportExponentTable AND SameParameterPDECThresholdNumericTable AND SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow AND IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 6. 下一步最窄点

- 主攻：`SameParameterPerLevelColdSupportExponentTable`。
- 并行：`SameParameterPDECThresholdNumericTable`、`SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow`、`FiniteColdHistorySummationRunnerOrAnalyticEnvelope`。
- 边界：本步关闭深度 cap 与显式对数吸收判据；未证明每层支撑指数，因此不闭合最终命题。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json` | `5be154f20bb3ff27a7c356dc2fc1d9b2a963be039e3c4f94ec2d941a7e47f721` |
| `docs/monograph/prime-matrix-strict-core-history-weighted-support-measure-router.json` | `2dd7639bfbaa615273487219d874098fb83b09636ad217369bb1b71df21bdf8b` |
| `docs/monograph/prime-matrix-strict-same-parameter-core-threshold-summation-router.json` | `1cc2717fe5d08bdea447f23044a214316ff2f4dd1f13426922f016ce20beba74` |
| `docs/monograph/prime-matrix-strict-same-parameter-prefix-window-spec-router.json` | `d80bb554768007ffae5c7b1823173e7c985d85af69f458046ca8aa84f81fcc0b` |
| `experiments/prime_matrix_strict_cold_support_depth_telescoping_router.py` | `23a6c788da6c8bbfbb1d4e146c09cce1d6d272e4405ffc5479cf8b5aca9db2b3` |
