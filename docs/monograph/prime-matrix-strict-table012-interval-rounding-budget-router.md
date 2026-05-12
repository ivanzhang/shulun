# Prime Matrix strict table_012 区间误差预算证书

**状态：** `table012_interval_budget_reduced_to_log_oracle_outward_certificate`

table_012 完整归档后的下一层已收缩：34 行极值搜索和 hash 已闭合，误差预算传递也足以吸收所有行，最薄行仍有正保护余量。严格自足版现在只剩 log(p)/log(x) 外向区间 oracle 或等价 ulp 证书；在补齐该原子前，不能声称 theta 表自足闭合，更不能声称行/列命题无条件闭合。

```text
full_table012_theta_extremal_archive_run_hash_closed=true
table012_directed_rounding_and_interval_propagation_closed=true
certified_log_summation_interval_arithmetic_closed=false
independent_theta_extremal_archive_closed=false
theta_less_than_identity_to_8e11_self_contained_closed=false
row_column_unconditional_closed=false
```

## 1. 预算结论

| field | value |
| --- | --- |
| `archive_sha256` | `2d1e955a6fa533c4e68bf9d786617d4d090dc91b52e224447eebaff849ddc1a3` |
| `row_count` | `34` |
| `segment_count` | `700` |
| `min_margin_after_guard` | `55.07003791407393599` |
| `min_margin_label` | `3E+08` |
| `min_margin_max_x` | `380767693` |
| `max_numeric_error_bound` | `1.030341383527000000000` |
| `next_direct_attack_target` | `LogOracleOutwardIntervalImplementationOrFormalUlpCertificate` |

## 2. 传递定理

设 `R_b(x)=x+b*x/log(x)`。每个 table_012 行中 `b<0` 且 `R_b'(x)>0`，而 `theta(x)` 只在素数跳点后增加。因此每行只需检查左端点和素数跳点。归档给出这些点上的最大数值缺陷 `D_i`；若真实缺陷被包含在`D_i + numeric_error_bound_i` 之下，则 `D_i+numeric_error_bound_i<0` 直接推出整行 `theta(x)<=R_b(x)<x`。

本证书已经逐行复核 `D_i+numeric_error_bound_i<0`；唯一未闭合的是`numeric_error_bound_i` 对所有 `log(p)`、`log(x)` 和累计求和舍入的外向包含证明。

## 3. 判定表

| gate | closed | meaning | remaining |
| --- | --- | --- | --- |
| `FullTable012ThetaExtremalArchiveRunAndHashLedger` | `true` | 完整 34 行极值归档与 hash 已由上一证书登记。 | closed |
| `ThetaStepFunctionPrimeJumpReduction` | `true` | R_b(x)=x+b*x/log(x) 在每个 table_012 区间单调递增，theta 只在素数跳点后上升。 | closed |
| `UniformDefectErrorBudgetDominatesAllRows` | `true` | 每行 max_defect + numeric_error_bound < 0；最小保护余量仍约 55。 | closed |
| `Table012DirectedRoundingAndIntervalPropagationLedger` | `true` | 误差预算传递层已闭合为一个明确 log-oracle 输入；不再需要重跑 34 行极值搜索。 | LogOracleOutwardIntervalImplementationOrFormalUlpCertificate |
| `CertifiedLogSummationIntervalArithmeticForThetaLedger` | `false` | 仍需给 log(p)、log(x) 与累计 theta 求和一个真正外向区间实现或形式化 ulp 证明。 | LogOracleOutwardIntervalImplementationOrFormalUlpCertificate |
| `IndependentThetaExtremalArchiveForTable012IntervalsLedger` | `false` | 独立归档已完成运行/hash和误差预算传递；最后缺 log-oracle 外向包含。 | CertifiedLogSummationIntervalArithmeticForThetaLedger |
| `RowColumnUnconditionalClosed` | `false` | 本证书仍只是 table_012 低段自足输入推进，不产生早期零行反例链终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 最薄行附近

| index | label | max_x | max_kind | numeric_error_bound | margin_after_guard |
| ---: | --- | ---: | --- | ---: | ---: |
| `2` | `3E+08` | `380767693` | `prime_jump` | `1.000021336326000000` | `55.07003791407393599` |
| `0` | `1E+08` | `179845447` | `prime_jump` | `1.000011078937000000` | `75.34810237764390431` |
| `3` | `4E+08` | `497589787` | `prime_jump` | `1.000026355867000000` | `89.39187124023171544` |
| `1` | `2E+08` | `263237879` | `prime_jump` | `1.000016252325000000` | `104.9930489381183034` |
| `4` | `5E+08` | `597294499` | `prime_jump` | `1.000031324703000000` | `157.4046001536597167` |
| `7` | `8E+08` | `843484583` | `prime_jump` | `1.000046009215000000` | `244.9914976685369062` |
| `11` | `3E+09` | `3745619057` | `prime_jump` | `1.000189961812000000` | `246.6450372897623971` |
| `5` | `6E+08` | `604520611` | `prime_jump` | `1.000036252931000000` | `251.6695630043621573` |

## 5. 下一最窄点

```text
LogOracleOutwardIntervalImplementationOrFormalUlpCertificate
```

