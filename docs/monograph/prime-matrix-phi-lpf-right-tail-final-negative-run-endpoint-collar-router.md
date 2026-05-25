# Prime Matrix Phi-LPF right-tail final negative-run endpoint-collar 证书

**状态：** `final_negative_run_endpoint_collar_reduction_closed_payment_law_open`
**核验日期：** `2026-05-25`

本证书把上一层唯一 final negative tail 继续压成两步 endpoint-collar wrap debt。

```text
atom_key=right:1887:selected_terminal:m773
q_path=[461, 463, 467]
A_path=[417, 87, 34]
D_path=[44, 376, 433]
q_gap_path=[2, 4]
carry_path=[2, 5]
two_edge_sum_matches_variation_and_tail=true
endpoint_telescoping_closed=true
middle_phase_cancels=true
endpoint_collar_debt_formula_closed=true
double_awrap_same_lift_word_closed=true
right_tail_final_negative_run_endpoint_collar_reduction_closed=true
terminal_double_awrap_endpoint_collar_payment_law_proved=false
row_column_unconditional_closed=false
```

## 1. exact endpoint identities

| quantity | value |
| --- | --- |
| `final_tail_mass` | 0.831750175347 (179065/215287) |
| `transition_signed_delta_sum` | -0.831750175347 (-179065/215287) |
| `endpoint_drop_signed` | -0.831750175347 (-179065/215287) |
| `left_collar_start_D_over_q` | 0.095444685466 (44/461) |
| `right_collar_end_A_over_q` | 0.072805139186 (34/467) |
| `endpoint_collar_formula_tail` | 0.831750175347 (179065/215287) |

核心恒等式：

```text
179065/215287 = 417/461 - 34/467 = 1 - 44/461 - 34/467
```

## 2. two-edge turn word

| edge | signed delta | word |
| ---: | --- | --- |
| 0 | -0.716650346931 (-152964/213443) | `negative_Awrap1_Dwrap0_L1to1_gap2_carry2` |
| 1 | -0.115099828416 (-24887/216221) | `negative_Awrap1_Dwrap0_L1to1_gap4_carry5` |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `FinalRunTwoEdgeTurnWordIdentified` | `true` | `true` | the remaining tail is exactly the q=461->463->467 two-edge terminal run. | finite turn-word ledger |
| `DoubleAwrapSameLiftEndpointCollar` | `true` | `true` | both final edges are negative Awrap=1, Dwrap=0, L1->L1 transitions. | finite phase-turn ledger |
| `EndpointTelescopingIdentity` | `true` | `true` | the middle phase A=87/q=463 cancels, leaving only endpoint collar data. | finite rational identity |
| `EndpointCollarDebtFormula` | `true` | `true` | tail mass equals 1 - D_start/q_start - A_end/q_end. | finite endpoint-collar identity |
| `TerminalDoubleAwrapEndpointCollarPaymentLaw` | `false` | `false` | a uniform law must pay or exclude this terminal double-Awrap collar debt. | TerminalDoubleAwrapEndpointCollarPaymentOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite collar reduction, not a global parity-breaking theorem. | BridgeRootQSpinePivotEnclosureLawOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving |

## 4. 最新开放口

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC AND TerminalDoubleAwrapEndpointCollarPaymentOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 5. 外部前沿含义

- trace/Kloosterman/Type-II：两步 collar 太局部，必须先聚合成 admissible moving-denominator family。
- finite-group orbit：当前只是确定性 collar orbit segment，还没有 spectral-gap orbit family。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-normal-form-audit.json` | `45e13789a89eca78b31950a4fa13b50e4712160e2ff835fb8a33be28c8fff931` |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json` | `e05dc6c48cd18aaa25cef5abe9aa5dc346d5b07db0827c8443dcefe536111615` |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-right-tail-overhang-excess-decomposition-router.json` | `508b72f5bee9144dc953ea64dbb14ebb2d4be39e32ce93fa4dafeb23fb977a7a` |
| `experiments/prime_matrix_phi_lpf_right_tail_final_negative_run_endpoint_collar_router.py` | `021ceac2c4c524240e6580f6efa7dc705f2cbc28547b0a2a5448249bc7bc5db9` |

行/列命题仍未无条件闭合。
