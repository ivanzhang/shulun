# Prime Matrix Phi-LPF terminal boundary bulk carry-chain normal form 证书

**状态：** `bulk_new_residual_carry_chain_normal_form_closed_uniform_source_open`
**核验日期：** `2026-05-25`

本证书把未支付的 bulk new residual 压缩为 atomwise carry-chain normal form。

```text
previous_new_residual_tail_alignment_partial_closed=true
new_residual_event_count=42
bulk_unmatched_new_residual_event_count=36
atom_count=7
carry_segment_count=11
carry_transition_count=31
carry_break_count=4
tail_closed_segment_count=6
open_segment_count=5
all_carry_transitions_exact=true
all_tail_matched_events_are_segment_terminal=true
bulk_carry_chain_normal_form_closed=true
row_column_unconditional_closed=false
```

## 1. carry segments

| id | atom | events | carry | q-range | run-range | bulk | tail closed | terminal residual |
| ---: | --- | ---: | ---: | --- | --- | ---: | --- | --- |
| 1 | `left:2842:extra_shell:m719` | 9 | 8 | 563->701 | 1->9 | 8 | `true` | 0.356428699921 (136715/383569) |
| 2 | `left:2842:extra_shell:m751` | 8 | 7 | 547->673 | 1->8 | 7 | `true` | 0.462466987687 (177388/383569) |
| 3 | `left:2842:selected_terminal:m757` | 1 | 0 | 563->563 | 1->1 | 1 | `false` | 0.126151207326 (38833/307829) |
| 4 | `left:2842:selected_terminal:m757` | 1 | 0 | 577->577 | 4->4 | 1 | `false` | 0.780387597123 (270480/346597) |
| 5 | `left:2842:selected_terminal:m757` | 6 | 5 | 607->701 | 5->10 | 5 | `true` | 0.038532832424 (14780/383569) |
| 6 | `left:2842:selected_terminal:m761` | 1 | 0 | 593->593 | 5->5 | 1 | `false` | 0.200325209838 (69237/345623) |
| 7 | `left:2842:selected_terminal:m761` | 1 | 0 | 607->607 | 8->8 | 1 | `false` | 0.822670087625 (311982/379231) |
| 8 | `left:2842:selected_terminal:m761` | 5 | 4 | 631->701 | 9->13 | 4 | `true` | 0.032752907560 (12563/383569) |
| 9 | `right:1887:extra_shell:m479` | 4 | 3 | 443->461 | 1->4 | 3 | `true` | 0.088823635574 (18210/205013) |
| 10 | `right:1887:selected_terminal:m769` | 4 | 3 | 443->461 | 1->4 | 3 | `true` | 0.601039934053 (123221/205013) |
| 11 | `right:1887:selected_terminal:m773` | 2 | 1 | 443->449 | 1->2 | 2 | `false` | 0.222332434467 (44605/200623) |

## 2. carry breaks

| atom | prev run/q | root run/q | run gap | q gap | previous residual | root old mass | delta |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| `left:2842:selected_terminal:m757` | 1/563 | 4/577 | 3 | 14 | 0.126151207326 (38833/307829) | 0.105807258390 (34860/329467) | -0.020343948936 (-2063273071/101419497143) |
| `left:2842:selected_terminal:m757` | 4/577 | 5/607 | 1 | 30 | 0.780387597123 (270480/346597) | 0.713374768185 (234263/328387) | -0.067012828938 (-20701/308911) |
| `left:2842:selected_terminal:m761` | 5/593 | 8/607 | 3 | 14 | 0.200325209838 (69237/345623) | 0.010838607812 (3954/364807) | -0.189486602027 (-23891548917/126085689761) |
| `left:2842:selected_terminal:m761` | 8/607 | 9/631 | 1 | 24 | 0.822670087625 (311982/379231) | 0.774998462084 (264562/341371) | -0.047671625541 (-15500/325141) |

## 3. tail overhang carried forward

| atom | run | q-range | mass |
| --- | ---: | --- | --- |
| `right:1887:selected_terminal:m773` | 4 | 461->467 | 0.831750175347 (179065/215287) |

## 4. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BulkCarryChainNormalForm` | `true` | `true` | 42 new-side residual events are partitioned into 11 atomwise carry segments with 31 exact carry transitions. | `finite carry-chain ledger` |
| `BulkResidualIndependentEventReduction` | `true` | `true` | the 36 unmatched bulk events are no longer independent scatter; they are segment roots/interiors in the carry normal form. | `BoundaryBulkCarrySegmentRootSourceLawOrPDEC` |
| `CarrySegmentRootSourceLaw` | `false` | `false` | the 11 segment roots and 4 carry breaks still need a uniform source law or named PDEC. | `BoundaryBulkCarrySegmentRootSourceLawOrPDEC` |
| `RightTailOverhangPDEC` | `false` | `false` | the single unmatched right selected-terminal tail survivor is carried forward. | `RightSelectedTerminalTailOverhangPDEC` |
| `ExternalTraceOrGroupEntry` | `false` | `false` | frontier trace/Kloosterman/Type-II or group-expansion inputs still require an admissible family built from these segments. | `AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite normal form, not a global parity-breaking theorem. | `PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving` |

## 5. 最新开放口

```text
BoundaryBulkCarrySegmentRootSourceLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-new-residual-tail-alignment-router.json` | `a6abbc588de0905e4f96855b5bfe7f0594d2f46351732cf3bc3c9a34048c508f` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-old-residual-return-alignment-router.json` | `4f2f4be70956f3ab1da6e3fd1cd790630014cc1213eb83a1d0111e61cdca5641` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-residual-flow-obstruction-router.json` | `4023c41551ce51476161cd01fce05b5de460b37c42c870000d0a1c853544ef88` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_bulk_carry_chain_normal_form_router.py` | `20f5be201ef341e33b6e12768f12015f5eab6b4592ed2c4485ce0c53a7603e12` |

行/列命题仍未无条件闭合。
