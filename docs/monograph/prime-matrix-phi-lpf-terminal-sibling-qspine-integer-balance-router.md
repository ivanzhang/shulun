# Prime Matrix Phi-LPF terminal sibling q-spine integer-balance 证书

**状态：** `terminal_sibling_qspine_integer_balance_closed_payment_law_open`
**核验日期：** `2026-05-25`

本证书把上一层 P-scaled q-spine 三分母 kernel 继续压成一个整数守恒。

```text
q_spine_for_balance=[439, 461, 467]
q_path_from_double_awrap=[461, 463, 467]
denominators_closed=true
normalized_identity_closed=true
integer_balance_closed=true
endpoint_coefficients_closed=true
endpoint_offset_formula_closed=true
terminal_sibling_qspine_integer_balance_closed=true
terminal_sibling_qspine_integer_balance_payment_law_proved=false
row_column_unconditional_closed=false
```

## 1. integer balance

```text
295/(461*467) = 203/(439*467) + 60/(439*461) + 18/(461*467)
295*439 = 203*461 + 60*467 + 18*439
129505 = 129505
```

## 2. exact kernel masses

| quantity | value | coefficient |
| --- | --- | ---: |
| `target_final_tail_mass` | 0.831750175347 (179065/215287) | 295 |
| `sibling_final_collar_mass` | 0.780999317191 (168139/215287) | 277 |
| `paid_sibling_tail_mass` | 0.601039934053 (123221/205013) | 203 |
| `middle_kernel_mass` | 0.179959383138 (36420/202379) | 60 |
| `endpoint_offset_mass` | 0.050750858157 (10926/215287) | 18 |

## 3. endpoint coefficients

```text
coeff=(q_mid*q_right - D_start*q_right - A_end*q_mid)/607
m769: (461*467 - 21*467 - 81*461)/607 = 277
m773: (461*467 - 44*467 - 34*461)/607 = 295
offset: ((21-44)*467 + (81-34)*461)/607 = 18
```

## 4. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SiblingQSpineKernelImported` | `true` | `true` | 上一层 P-scaled sibling q-spine kernel 已有限闭合，支付律仍未证明。 | finite sibling-kernel ledger |
| `QSpineDenominatorAlignment` | `true` | `true` | 三个分母精确落在 right-side q-spine [439,461,467] 的三条二点边上。 | finite denominator ledger |
| `IntegerBalanceIdentity` | `true` | `true` | 三分母 kernel 等价于整数守恒 295*439=203*461+60*467+18*439。 | finite integer identity |
| `EndpointCoefficientFormula` | `true` | `true` | m769 与 m773 的 endpoint collar 系数服从同一 D_start/A_end 公式。 | finite endpoint coefficient ledger |
| `EndpointOffsetFormula` | `true` | `true` | m773 相对 m769 的 offset 系数 18 来自两个 endpoint 数据的差分公式。 | finite endpoint difference ledger |
| `TerminalSiblingQSpineIntegerBalancePaymentLaw` | `false` | `false` | 仍需一个 uniform law 支付或排除该整数 balance，而不能只在 m773 有限点成立。 | TerminalSiblingQSpineIntegerBalancePaymentOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 这是 finite integer-balance reduction，不是全局奇偶性突破定理。 | BridgeRootQSpinePivotEnclosureLawOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving |

## 5. 最新开放口

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC AND TerminalSiblingQSpineIntegerBalancePaymentOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json` | `8ee3a54cdd7ed21521fee953ef6d2f3433235a0e6a7a81b4055f89e31e1603da` |
| `experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_integer_balance_router.py` | `bbb50a10be014d88e783698d173edc282f2b650cd486981a410a3da91557f464` |

行/列命题仍未无条件闭合。
