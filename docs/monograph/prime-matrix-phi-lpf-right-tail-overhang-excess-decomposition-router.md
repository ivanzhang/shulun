# Prime Matrix Phi-LPF right-tail overhang excess decomposition 证书

**状态：** `right_tail_overhang_excess_decomposition_closed_final_payment_law_open`
**核验日期：** `2026-05-25`

本证书把唯一 right-tail overhang 压成 m773 selected-terminal 负变差超额的剩余部分。

```text
atom_key=right:1887:selected_terminal:m773
negative_excess_equals_internal_plus_tail=true
tail_overhang_equals_excess_after_internal_return=true
internal_survivor_old_return_paid=true
final_run_tail_matches=true
right_tail_overhang_excess_decomposition_closed=true
right_tail_final_negative_run_payment_law_proved=false
row_column_unconditional_closed=false
```

## 1. exact decomposition

| quantity | value |
| --- | --- |
| `negative_variation_excess` | 0.849746113661 (174209/205013) |
| `internal_survivor_mass` | 0.017995938314 (3642/202379) |
| `tail_overhang_mass` | 0.831750175347 (179065/215287) |
| `residual_after_internal_return` | 0.831750175347 (179065/215287) |

## 2. final run

| run | direction | q-range | length | A-wrap | D-wrap | carry | signed delta |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- |
| 4 | `negative` | 461->467 | 2 | 2 | 0 | 2->5 | -0.831750175347 (-179065/215287) |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `M773NegativeExcessDecomposition` | `true` | `true` | m773 selected-terminal negative excess equals internal survivor return plus final tail overhang. | finite excess decomposition ledger |
| `InternalSurvivorAlreadyPaid` | `true` | `true` | the internal survivor part is already matched by old-residual return alignment. | none for internal survivor payment |
| `FinalNegativeRunTailIdentification` | `true` | `true` | the unmatched tail is exactly the final negative run q=461->467 of m773. | finite final-run identification |
| `RightTailFinalNegativeRunPaymentLaw` | `false` | `false` | a uniform law must pay or exclude such final negative tail excess. | RightSelectedTerminalFinalNegativeRunExcessPaymentOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite decomposition, not a global parity-breaking theorem. | BridgeRootQSpinePivotEnclosureLawOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving |

## 4. 最新开放口

```text
BridgeRootQSpinePivotEnclosureLawOrPDEC AND RightSelectedTerminalFinalNegativeRunExcessPaymentOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json` | `23ca4dfcd8fe7771e24bb62c0e0a4bc8aa0fbb57b5406690c9175bec78eb5440` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bulk-carry-chain-normal-form-router.json` | `e2482fea4f855b9e66c2c8d16f5d6ae7f020a83a8b0d16cbb29f02562f72539e` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json` | `4f2f4be70956f3ab1da6e3fd1cd790630014cc1213eb83a1d0111e61cdca5641` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json` | `5f855cce874423998dc3046cbf66f7a3930b939520d1103766f0f0bae77a65e3` |
| `experiments/prime_matrix_phi_lpf_right_tail_overhang_excess_decomposition_router.py` | `5c6217ae4f420d760885939ff9ada68b12d3924490edc6b44f991661202fbcf6` |

行/列命题仍未无条件闭合。
