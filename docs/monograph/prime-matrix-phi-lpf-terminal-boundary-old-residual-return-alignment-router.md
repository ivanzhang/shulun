# Prime Matrix Phi-LPF terminal boundary old-residual return alignment 证书

**状态：** `old_residual_return_alignment_closed_new_source_open`
**核验日期：** `2026-05-25`

本证书核对 old-side boundary residual 是否逐项等于 nonboundary/internal return。

```text
previous_residual_flow_side_decomposition_closed=true
previous_source_key_obstruction_partition_closed=true
old_residual_event_count=5
nonboundary_record_jump_event_count=4
internal_survivor_return_count=1
old_residual_equals_nonboundary_plus_internal_obstruction=true
old_residual_return_alignment_closed=true
new_residual_return_alignment_closed=false
row_column_unconditional_closed=false
```

## 1. totals

| quantity | value |
| --- | --- |
| `old_residual_total` | 0.215539338772 (4672783399294642/21679492133206013) |
| `nonboundary_record_jump_mass_total` | 0.197543400458 (21161487092/107123229847) |
| `internal_survivor_mass_total` | 0.017995938314 (3642/202379) |
| `nonboundary_plus_internal_obstruction_mass` | 0.215539338772 (4672783399294642/21679492133206013) |
| `matched_old_residual_return_mass` | 0.215539338772 (4672783399294642/21679492133206013) |
| `unmatched_old_residual_return_mass` | 0.000000000000 (0/1) |
| `new_residual_mass_total_still_open` | 13.264539470882 (41926303295575689754715570945220742196966577484713147368977982770741/3160780921765953306422353215107991553097814357054137917186575616177) |

## 2. return alignment rows

| atom | old run | q | direction | old residual | return type | return endpoint | matched |
| --- | ---: | ---: | --- | --- | --- | --- | --- |
| `left:2842:selected_terminal:m757` | 1 | 569 | `positive->negative` | 0.067012828938 (20701/308911) | `nonboundary_record_jump` | `old_q_end=569, new_q_start=577` | `true` |
| `left:2842:selected_terminal:m761` | 0 | 563 | `negative->positive` | 0.075506206368 (23243/307829) | `nonboundary_record_jump` | `old_q_end=563, new_q_start=593` | `true` |
| `left:2842:selected_terminal:m761` | 2 | 571 | `negative->positive` | 0.007352739611 (2414/328313) | `nonboundary_record_jump` | `old_q_end=571, new_q_start=593` | `true` |
| `left:2842:selected_terminal:m761` | 5 | 599 | `positive->negative` | 0.047671625541 (15500/325141) | `nonboundary_record_jump` | `old_q_end=599, new_q_start=607` | `true` |
| `right:1887:selected_terminal:m773` | 2 | 457 | `negative->positive` | 0.017995938314 (3642/202379) | `internal_survivor` | `q_start=449, q_end=457` | `true` |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `OldResidualReturnAlignmentClosed` | `true` | `true` | the five old-side boundary residuals match four nonboundary jumps plus one internal survivor exactly. | `finite old-side return ledger` |
| `BoundaryResidualTransportToNonBoundaryInternalReturnsOldSide` | `true` | `true` | old-side residual transport is fully accounted for in the finite source-key partition. | `old-side transport closed only` |
| `BoundaryDominantNewResidualSource` | `false` | `false` | new-side residual mass remains dominant and has no return alignment in this certificate. | `BoundaryDominantNewResidualSourceLawOrPDEC` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite old-side return alignment, not a global parity-breaking theorem. | `PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |

## 4. 最新开放口

```text
BoundaryDominantNewResidualSourceLawOrPDEC AND BoundaryNewResidualReturnOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json` | `4023c41551ce51476161cd01fce05b5de460b37c42c870000d0a1c853544ef88` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json` | `5f855cce874423998dc3046cbf66f7a3930b939520d1103766f0f0bae77a65e3` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_old_residual_return_alignment_router.py` | `0c04f928b27408820b0722704b7926b009d56107dee6bb8d877ebff6d52d39c1` |

行/列命题仍未无条件闭合。
