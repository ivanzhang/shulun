# Prime Matrix Phi-LPF terminal double-Awrap sibling q-spine kernel 证书

**状态：** `terminal_double_awrap_sibling_qspine_kernel_closed_payment_law_open`
**核验日期：** `2026-05-25`

本证书把 m773 terminal double-Awrap endpoint collar 与已支付 sibling m769 对齐。

```text
sibling_atom_key=right:1887:selected_terminal:m769
target_atom_key=right:1887:selected_terminal:m773
q_path=[461, 463, 467]
same_q_path=true
same_turn_words=true
same_gap_carry=true
paid_sibling_tail_closed=true
sibling_gap_is_ten_internal_units=true
endpoint_offset_is_three_endpoint_units=true
target_kernel_identity_closed=true
p_scaled_kernel_identity_closed=true
terminal_double_awrap_sibling_qspine_kernel_closed=true
terminal_double_awrap_sibling_qspine_kernel_payment_law_proved=false
row_column_unconditional_closed=false
```

## 1. q-spine kernel identity

```text
179065/215287
= 123221/205013 + 36420/202379 + 10926/215287
= 607*(203/(439*467) + 60/(439*461) + 18/(461*467))
295/(461*467) = 203/(439*467) + 60/(439*461) + 18/(461*467)
```

## 2. exact masses

| quantity | value | P-scaled coefficient |
| --- | --- | ---: |
| `target_final_tail_mass` | 0.831750175347 (179065/215287) | 295 |
| `sibling_final_collar_mass` | 0.780999317191 (168139/215287) | 277 |
| `paid_sibling_tail_mass` | 0.601039934053 (123221/205013) | 203 |
| `sibling_final_minus_paid` | 0.179959383138 (36420/202379) | 60 |
| `sibling_endpoint_offset` | 0.050750858157 (10926/215287) | 18 |
| `target_internal_survivor_unit` | 0.017995938314 (3642/202379) | 6 |
| `endpoint_unit_same_numerator` | 0.016916952719 (3642/215287) | 6 |

## 3. shared terminal words

| atom | A path | D path | words |
| --- | --- | --- | --- |
| `right:1887:selected_terminal:m769` | `[440, 118, 81]` | `[21, 345, 386]` | `['negative_Awrap1_Dwrap0_L1to1_gap2_carry2', 'negative_Awrap1_Dwrap0_L1to1_gap4_carry5']` |
| `right:1887:selected_terminal:m773` | `[417, 87, 34]` | `[44, 376, 433]` | `['negative_Awrap1_Dwrap0_L1to1_gap2_carry2', 'negative_Awrap1_Dwrap0_L1to1_gap4_carry5']` |

## 4. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SiblingDoubleAwrapSignatureMatched` | `true` | `true` | m769 and m773 share q-path, gap/carry path, and terminal double-Awrap turn words. | finite turn-word ledger |
| `PaidSiblingTailImported` | `true` | `true` | m769 terminal tail is already paid by new-residual tail alignment. | finite tail-alignment ledger |
| `InternalUnitScalingIdentity` | `true` | `true` | m769 final collar minus paid tail equals ten copies of the m773 internal survivor unit. | finite rational identity |
| `EndpointOffsetUnitIdentity` | `true` | `true` | m773 minus m769 final collar equals three copies of the same numerator over the final endpoint denominator. | finite rational identity |
| `PScaledQSpineKernelIdentity` | `true` | `true` | the target final tail is a P-scaled three-denominator q-spine kernel. | finite q-spine kernel ledger |
| `SiblingQSpineKernelPaymentLaw` | `false` | `false` | a uniform law must pay or exclude this P-scaled sibling q-spine kernel. | TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite sibling-kernel reduction, not a global parity-breaking theorem. | BridgeRootQSpinePivotEnclosureLawOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving |

## 5. 最新开放口

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC AND TerminalDoubleAwrapSiblingQSpineKernelPaymentOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json` | `e05dc6c48cd18aaa25cef5abe9aa5dc346d5b07db0827c8443dcefe536111615` |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-right-tail-final-negative-run-endpoint-collar-router.json` | `e730a16464c742772ec61fc6afe1ba38dbb1c7bf2b1dedd0ec578c7f9861f194` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json` | `a6abbc588de0905e4f96855b5bfe7f0594d2f46351732cf3bc3c9a34048c508f` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json` | `5f855cce874423998dc3046cbf66f7a3930b939520d1103766f0f0bae77a65e3` |
| `experiments/prime_matrix_phi_lpf_terminal_double_awrap_sibling_qspine_kernel_router.py` | `ba56a16f8f53f8727b1aaffc59611f5c6938ef35bdadcfc9cb81bf32d3b8ee59` |

行/列命题仍未无条件闭合。
