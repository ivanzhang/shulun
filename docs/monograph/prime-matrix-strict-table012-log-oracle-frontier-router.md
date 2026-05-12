# Prime Matrix strict table_012 log-oracle 前沿证书

**状态：** `table012_log_oracle_reduced_to_logl_abs_error_or_mpfr_interval_rescan`

table_012 log-oracle 硬点进一步收缩：完整归档和误差预算传递已导入，Kahan 累计与 RHS 舍入在 long double 模型下可被绝对 1.0 保护项吸收。真正未闭合的单点是 runner 实际 `std::log(long double)` 对所有整数输入到 8e11 是否有绝对误差 <= 1e-12 的形式化证书；或者改走 MPFR 区间 log 全量重扫。

```text
full_archive_and_budget_imported=true
kahan_compensated_positive_log_summation_error_budget_closed=true
std_logl_abs_error_1e_minus_12_closed=false
certified_mpfr_interval_rescan_archive_closed=false
certified_log_summation_interval_arithmetic_closed=false
row_column_unconditional_closed=false
```

## 1. 数值预算

| field | value |
| --- | --- |
| `unit_roundoff` | `5.42101086242752217003726400434970855713E-20` |
| `max_prime_count` | `30341383527` |
| `theta_at_8e11_archive` | `799999133776.0847430825` |
| `max_log_8e11` | `27.40787756461433845311947976597366505302` |
| `runner_max_numeric_error_bound` | `1.030341383527000000000` |
| `runner_min_guard_margin` | `55.07003791407393599` |
| `log_oracle_budget_if_abs_error_1e_minus_12` | `0.030341383527` |
| `kahan_compensated_budget_bound` | `1.734721597653105533904051144850450743138951417854502301191029251835722326691549352678004382206693664E-7` |
| `rhs_auxiliary_rounding_budget` | `0.000001` |
| `non_log_budget_total` | `0.000001173472159765310553390405114485045074313895141785450230119102925183572232669154935267800438220669366` |
| `unused_absolute_guard_after_non_log_budget` | `0.9999988265278402346894466095948855149549256861048582145497698808970748164277673308450647321995617793` |

## 2. 本机模型

| field | value |
| --- | --- |
| `mpfr_available` | `True` |
| `ldbl_mant_dig` | `64` |
| `ldbl_epsilon` | `1.084202172485504434007452800869941711426e-19` |
| `log_max` | `27.40787756461433845311947976597366505302` |

## 3. 判定表

| gate | closed | meaning | remaining |
| --- | --- | --- | --- |
| `LogOracleOutwardIntervalImplementationOrFormalUlpCertificate` | `false` | 上一层已证明只需给 log 输入提供外向包含；本层继续拆分该原子。 | StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11 OR CertifiedMPFRIntervalThetaExtremalRescanArchive |
| `KahanCompensatedPositiveLogSummationErrorBudgetLedger` | `true` | 在 IEEE 64-bit mantissa long double 模型下，Kahan 正项累计误差预算远小于绝对 1.0 保护项。 | closed under IEEE rounded-addition model |
| `RHSLogAndDivisionLongDoubleRoundingBudgetLedger` | `true` | RHS 中有限个 log/div/mul/add 的 long double 舍入可由绝对 1.0 保护项吸收。 | closed as budget allocation; exact log enclosure still open |
| `StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11` | `false` | 需证明 runner 实际调用的 std::log(long double) 对所有整数输入 2..8e11 的绝对误差 <= 1e-12。 | libm algorithm proof, exhaustive certified ulp certificate, or replacement oracle |
| `CertifiedMPFRIntervalThetaExtremalRescanArchive` | `false` | 替代路线：用 MPFR/区间 log 重新生成完整 theta 极值归档并登记 hash。 | computationally heavy full rescan |
| `CertifiedLogSummationIntervalArithmeticForThetaLedger` | `false` | 只有 logl 误差证书或 MPFR 区间重扫二选一闭合后，table_012 自足 theta 证书才闭合。 | StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11 OR CertifiedMPFRIntervalThetaExtremalRescanArchive |

## 4. 下一最窄点

```text
StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11
```

