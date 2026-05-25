# Prime Matrix Phi-LPF terminal sibling q-spine gap-drift 证书

**状态：** `terminal_sibling_qspine_gap_drift_closed_payment_law_open`
**核验日期：** `2026-05-25`

本证书把 terminal integer balance 改写为 q-spine gap-drift 正规形。

```text
q_spine_for_balance=[439, 461, 467]
q_gaps_from_prefix=[22, 28]
primitive_gap_vector=[11, 14]
offset_cancels_from_gap_drift=true
gap_drift_identity_closed=true
primitive_gap_drift_identity_closed=true
lpf_factor_peeling_closed=true
terminal_sibling_qspine_gap_drift_closed=true
terminal_sibling_qspine_gap_drift_payment_law_proved=false
row_column_unconditional_closed=false
```

## 1. gap-drift identities

```text
(295-203-60-18)*439 = 22*203 + 28*60
6146 = 6146
7*439 = 11*203 + 14*60
3073 = 3073
439 = 11*29 + 2*60
439 = 439
```

## 2. coefficients

| quantity | value |
| --- | ---: |
| `target_final_tail` | 295 |
| `paid_sibling_tail` | 203 |
| `middle_kernel` | 60 |
| `endpoint_offset` | 18 |
| `drift_defect` | 14 |
| `primitive_defect` | 7 |
| `paid_sibling_tail_after_lpf_peel` | 29 |
| `primitive_right_gap_after_lpf_peel` | 2 |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `IntegerBalanceImported` | `true` | `true` | 上一层 terminal integer balance 已有限闭合，支付律仍未证明。 | finite integer-balance ledger |
| `OffsetCancellationInGapDrift` | `true` | `true` | endpoint offset 与 target 共用 q_mid*q_right 分母，清分母后只贡献 q_prefix 项并可并入 defect。 | finite offset ledger |
| `GapDriftIdentity` | `true` | `true` | integer balance 等价于 drift defect 支付 q-prefix 到两个 q-spine gap 的漂移。 | finite gap-drift identity |
| `PrimitiveGapDriftIdentity` | `true` | `true` | 除以 q-spine gap 公因子 2 后得到 primitive drift law。 | finite primitive gap ledger |
| `LPFThresholdSevenPeel` | `true` | `true` | primitive defect 是 7，且 paid coefficient 与 right primitive gap 可剥离同一 LPF-threshold 因子。 | finite 7-factor ledger |
| `TerminalSiblingQSpinePrimitiveGapDriftPaymentLaw` | `false` | `false` | 仍需 uniform law 支付或排除该 primitive gap-drift，而不能只在 m773 有限点成立。 | TerminalSiblingQSpinePrimitiveGapDriftPaymentOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 这是 finite gap-drift reduction，不是全局奇偶性突破定理。 | BridgeRootQSpinePivotEnclosureLawOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving |

## 4. 最新开放口

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC AND TerminalSiblingQSpinePrimitiveGapDriftPaymentOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance-router.json` | `77390867227503670dafeb9f99fb12f4cef8102e4cfa3d4adefe1ad08f12d536` |
| `experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_gap_drift_router.py` | `88a4312bf0831c910381f7a2d702100a35bba5f150539581318564dfcebd56dc` |

行/列命题仍未无条件闭合。
