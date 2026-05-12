# Prime Matrix strict table_012 x87 指令精度前沿证书

**状态：** `x87_accuracy_reduced_to_y_equals_ln2_applicability_or_mpfr_rescan`

x87 精度硬点进一步压缩：如果能证明 glibc 的 y=ln2 型 FYL2X/FYL2XP1 调用有 1.5 ulp 级误差，1e-12 预算有约 3.84e5 倍余量，table_012 log oracle 即可闭合。但现阶段不能把常见的 y=1 精度陈述直接套到 y=ln2；剩余原子是该适用性证明，或改走 MPFR 外向 log 全量重扫。

```text
glibc_logl_source_binding_imported=true
x87_1p5ulp_budget_would_close_log_oracle=true
fyl2x_y_equals_ln2_accuracy_applicability_closed=false
x87_instruction_accuracy_closed=false
std_logl_abs_error_1e_minus_12_closed=false
row_column_unconditional_closed=false
```

## 1. 预算

| field | value |
| --- | --- |
| `ln_x_upper_bound_used` | `32` |
| `extended_precision_significand_bits` | `64` |
| `ulp_bound_for_ln_x_less_than_32` | `1.73472347597680709441192448139190673828125E-18` |
| `one_point_five_ulp_bound` | `2.602085213965210641617886722087860107421875E-18` |
| `required_log_abs_error_bound` | `1E-12` |
| `slack_factor_vs_1p5ulp` | `384307.1682022823253333333333333333333333333333333333333333333333333333333333333333333333333333333333` |

## 2. CPU 环境

| field | value |
| --- | --- |
| `Architecture` | `x86_64` |
| `Vendor ID` | `GenuineIntel` |
| `Model name` | `Intel(R) Xeon(R) Gold 6152 CPU @ 2.10GHz` |
| `CPU family` | `6` |
| `Model` | `85` |
| `Stepping` | `4` |

## 3. 判定表

| gate | closed | meaning | remaining |
| --- | --- | --- | --- |
| `X87FYL2X_FYL2XP1InstructionAccuracyLedger` | `false` | 若 glibc 使用的 FYL2X/FYL2XP1 在 y=ln2 乘子下有 <=1.5 ulp 误差，则 log oracle 预算立即闭合。 | FYL2X_FYL2XP1_YEqualsLn2AccuracyApplicabilityLedger |
| `X87OnePointFiveUlpWouldBeSufficient` | `true` | 在 ln(x)<32 范围，1.5 ulp 约 2.60e-18，比 1e-12 小约 3.84e5 倍。 | closed |
| `FYL2X_FYL2XP1_YEqualsLn2AccuracyApplicabilityLedger` | `false` | 必须证明 Intel/AMD FYL2X/FYL2XP1 的精度保证适用于 glibc 的 y=ln2 调用，而不只是 y=1 的特殊陈述。 | architectural/manual proof or formally sampled microcode certificate |
| `CertifiedMPFRIntervalThetaExtremalRescanArchive` | `false` | 绕开硬件指令精度：用 MPFR 外向 log 全量重扫完整 theta 归档。 | heavy full rescan |
| `StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11` | `false` | 当前仍不能把有限点审计和 y=1 手册语句合成全域 logl 误差证明。 | FYL2X_FYL2XP1_YEqualsLn2AccuracyApplicabilityLedger OR CertifiedMPFRIntervalThetaExtremalRescanArchive |

## 4. 下一最窄点

```text
FYL2X_FYL2XP1_YEqualsLn2AccuracyApplicabilityLedger
```

