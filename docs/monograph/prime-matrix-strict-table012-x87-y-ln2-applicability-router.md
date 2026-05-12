# Prime Matrix strict table_012 x87 y=ln2 适用性闭合证书

**状态：** `x87_y_ln2_applicability_closed_log_oracle_closed_under_intel_sdm`

x87 y=ln2 适用性原子已在 Intel SDM 口径下闭合：手册覆盖 FYL2X/FYL2XP1 的 y!=1 round-to-nearest 误差，并给出 1.35 ulps；当前 glibc logl 使用 fldln2 与 x87 fyl2x/fyl2xp1，当前 FPU 控制字也是 round-to-nearest/extended precision。1.35 ulps 在 ln(x)<32 范围内比 1e-12 小约 4.27e5 倍。因此 table_012 的 log-oracle 与独立 theta 归档在 Intel SDM 硬件规范作为可信计算基的意义下闭合。行/列总命题仍未因此闭合，下一数学目标回到 DStructure/反例链终端矛盾。

```text
manual_y_not_equal_1_statement_closed=true
x87_round_to_nearest_extended_precision_closed=true
fyl2x_y_equals_ln2_accuracy_applicability_closed=true
std_logl_abs_error_1e_minus_12_closed=true
certified_log_summation_interval_arithmetic_closed=true
theta_less_than_identity_to_8e11_self_contained_closed=true
row_column_unconditional_closed=false
```

## 1. 误差预算

| field | value |
| --- | --- |
| `ln_x_upper_bound_used` | `32` |
| `ulp_bound_for_ln_x_less_than_32` | `1.73472347597680709441192448139190673828125E-18` |
| `one_point_three_five_ulp_bound` | `2.3418766925686895774560980498790740966796875E-18` |
| `required_log_abs_error_bound` | `1E-12` |
| `slack_factor_vs_1p35ulp` | `427007.9646692025837037037037037037037037037037037037037037037037037037037037037037037037037037037037` |

## 2. 证据

| field | value |
| --- | --- |
| `manual_pdf_sha256` | `54415a6ff0f1453ed8636d97bc43215b334524984c9d6bf4ea10e0ac8817a038` |
| `manual_hit_line_1_based` | `18782` |
| `excerpt_sha256` | `697b53944b19859637e621995382cddf6468b93dffa290383a69c9d81f23a82f` |
| `x87_control_word_hex` | `0x37f` |
| `round_to_nearest` | `true` |
| `extended_precision` | `true` |
| `cpu` | `Intel(R) Xeon(R) Gold 6152 CPU @ 2.10GHz` |

## 3. 判定表

| gate | closed | meaning | remaining |
| --- | --- | --- | --- |
| `FYL2X_FYL2XP1_YEqualsLn2AccuracyApplicabilityLedger` | `true` | Intel SDM 明确给出 FYL2X/FYL2XP1 在 y!=1、round-to-nearest 下的 1.35 ulps 上界；glibc 使用 y=ln2，当前 x87 控制字为 round-to-nearest。 | closed |
| `X87FYL2X_FYL2XP1InstructionAccuracyLedger` | `true` | 1.35 ulps 在 ln(x)<32 范围内远小于 1e-12，因此 x87 指令误差预算闭合。 | closed |
| `StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11` | `true` | std::logl 通过 glibc e_logl.S 的 x87 路径得到 <=1e-12 绝对误差证书。 | closed |
| `CertifiedLogSummationIntervalArithmeticForThetaLedger` | `true` | 结合前序 Kahan/RHS 预算和完整 theta 归档，严格 log 求和区间输入闭合。 | closed |
| `IndependentThetaExtremalArchiveForTable012IntervalsLedger` | `true` | 完整 34 行归档、hash、误差预算和 log oracle 已同时闭合。 | closed |
| `ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger` | `true` | table_012 低段 theta<x 到 8e11 的独立自足计算输入闭合；这是计算输入闭合，不是行/列总命题闭合。 | closed under Intel SDM x87 trusted-computing-base |
| `RowColumnUnconditionalClosed` | `false` | 本证书只关闭 table_012 低段 theta 输入，不产生早期零行反例链终端矛盾。 | DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance |

## 4. 下一目标

```text
DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

