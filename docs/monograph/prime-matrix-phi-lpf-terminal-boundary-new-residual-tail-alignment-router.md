# Prime Matrix Phi-LPF terminal boundary new-residual tail alignment 证书

**状态：** `new_residual_tail_alignment_partial_closed_bulk_source_open`
**核验日期：** `2026-05-25`

本证书核对 new-side boundary residual 是否可由 terminal tail survivor 精确支付。

```text
previous_residual_flow_side_decomposition_closed=true
previous_old_residual_return_alignment_closed=true
new_residual_event_count=42
tail_survivor_count=7
new_residual_tail_matched_event_count=6
new_residual_tail_alignment_partial_closed=true
new_residual_unmatched_after_tail_event_count=36
tail_survivor_unmatched_count=1
all_new_residual_return_alignment_closed=false
row_column_unconditional_closed=false
```

## 1. totals

| quantity | value |
| --- | --- |
| `new_residual_tail_matched_mass` | 1.580044997219 (124249416037/78636631397) |
| `new_residual_unmatched_after_tail_mass` | 11.684494473663 (48967251418543203254061941388483988569929566712414232303496831012/4190789043455521398233821685192850236361315067355978489004650201) |
| `tail_survivor_mass_total` | 2.411795172567 (87431161523472/36251487074017) |
| `tail_survivor_unmatched_mass` | 0.831750175347 (179065/215287) |

## 2. matched tail returns

| atom | new run | q | direction | residual | tail q-range | matched |
| --- | ---: | ---: | --- | --- | --- | --- |
| `left:2842:extra_shell:m719` | 9 | 701 | `positive->negative` | 0.356428699921 (136715/383569) | 701->709 | `true` |
| `left:2842:extra_shell:m751` | 8 | 673 | `positive->negative` | 0.462466987687 (177388/383569) | 673->709 | `true` |
| `left:2842:selected_terminal:m757` | 10 | 701 | `positive->negative` | 0.038532832424 (14780/383569) | 701->709 | `true` |
| `left:2842:selected_terminal:m761` | 13 | 701 | `negative->positive` | 0.032752907560 (12563/383569) | 701->709 | `true` |
| `right:1887:extra_shell:m479` | 4 | 461 | `positive->negative` | 0.088823635574 (18210/205013) | 461->467 | `true` |
| `right:1887:selected_terminal:m769` | 4 | 461 | `positive->negative` | 0.601039934053 (123221/205013) | 461->467 | `true` |

## 3. unmatched new residual by atom

| atom | events | mass |
| --- | ---: | --- |
| `left:2842:extra_shell:m719` | 8 | 2.990917633112 (75475078540795845436016/25234756619581092595811) |
| `left:2842:extra_shell:m751` | 7 | 1.831497793709 (33875380764978493728312/18495998674605510903967) |
| `left:2842:selected_terminal:m757` | 7 | 2.767331803736 (37281575438673519020539585/13472029406932386192433901) |
| `left:2842:selected_terminal:m761` | 6 | 2.562975537742 (67149610682817077385409/26199864061905050395049) |
| `right:1887:extra_shell:m479` | 3 | 0.961331165462 (39920962962/41526754147) |
| `right:1887:selected_terminal:m769` | 3 | 0.339701674541 (14106707922/41526754147) |
| `right:1887:selected_terminal:m773` | 2 | 0.230738865361 (47346/205193) |

## 4. unmatched tail survivor

| atom | run | q-range | mass |
| --- | ---: | --- | --- |
| `right:1887:selected_terminal:m773` | 4 | 461->467 | 0.831750175347 (179065/215287) |

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `NewResidualTerminalTailAlignmentPartial` | `true` | `true` | six new-side residuals match terminal tail survivors exactly. | `finite terminal-tail return ledger` |
| `AllNewResidualReturnAlignment` | `false` | `false` | 36 new-side residual events remain unmatched after tail returns. | `BoundaryBulkNewResidualSourceLawOrPDEC` |
| `RightSelectedTerminalTailOverhang` | `false` | `false` | one right selected-terminal tail survivor is not a new-side residual return. | `RightSelectedTerminalTailOverhangPDEC` |
| `GroupOrbitExpansionEntry` | `false` | `false` | no admissible group orbit or expander family has been constructed for the 36 bulk residuals. | `AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite partial return alignment, not a global parity-breaking theorem. | `PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |

## 6. 最新开放口

```text
BoundaryBulkNewResidualSourceLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json` | `4f2f4be70956f3ab1da6e3fd1cd790630014cc1213eb83a1d0111e61cdca5641` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json` | `4023c41551ce51476161cd01fce05b5de460b37c42c870000d0a1c853544ef88` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json` | `5f855cce874423998dc3046cbf66f7a3930b939520d1103766f0f0bae77a65e3` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_new_residual_tail_alignment_router.py` | `2a32909f19f43c2401797e9b31873b467e9d780fb39910870e762a67e68e309a` |

行/列命题仍未无条件闭合。
