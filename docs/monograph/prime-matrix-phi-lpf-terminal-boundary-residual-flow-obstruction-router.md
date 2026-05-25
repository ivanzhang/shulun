# Prime Matrix Phi-LPF terminal boundary residual-flow obstruction 证书

**状态：** `boundary_residual_flow_side_ledger_closed_local_conservation_refuted`
**核验日期：** `2026-05-25`

本证书检验 q-boundary synthetic split 是否能在边界内部形成 residual-flow 守恒。

```text
previous_boundary_ratio_spectrum_closed=true
q_boundary_synthetic_split_event_count=47
residual_flow_side_decomposition_closed=true
new_residual_side_event_count=42
old_residual_side_event_count=5
finite_boundary_local_opposite_side_cancellation_refuted=true
boundary_residual_flow_source_key_conservation_proved=false
row_column_unconditional_closed=false
```

## 1. residual totals

| quantity | value |
| --- | --- |
| `new_residual_mass_total` | 13.264539470882 (41926303295575689754715570945220742196966577484713147368977982770741/3160780921765953306422353215107991553097814357054137917186575616177) |
| `old_residual_mass_total` | 0.215539338772 (4672783399294642/21679492133206013) |
| `net_new_minus_old_residual_mass` | 13.049000132111 (54957153409114568024198549894917703765637866355953735626792659191/4211598808546086562597811196363849161858214943368430057167809509) |
| `atomwise_opposite_side_matched_mass` | 0.215539338772 (4672783399294642/21679492133206013) |
| `atomwise_unmatched_residual_mass` | 13.049000132111 (54957153409114568024198549894917703765637866355953735626792659191/4211598808546086562597811196363849161858214943368430057167809509) |
| `negative_to_positive_residual_mass_total` | 3.932134974227 (271832180664183870221045826677760843366027418986798/69130938395016822099452973148919227136792312500447) |
| `positive_to_negative_residual_mass_total` | 9.547943835427 (842081351966928692835468859567942722547075232616837/88195046648942059920997564570529412060602526622489) |
| `direction_signed_residual_mass_negpos_minus_posneg` | -5.615808861200 (-20616505380989542068374002861508114591349180568320726581429112813/3671155107046486620647230490946104817617160409310727984688973687) |

## 2. atom residual-flow summary

| atom | role | events | sequence | flips | new count | old count | net new-old |
| --- | --- | ---: | --- | ---: | ---: | ---: | --- |
| `left:2842:extra_shell:m719` | `extra_shell` | 9 | `NNNNNNNNN` | 0 | 9 | 0 | 3.347346333033 (32399870152060550712283521969/9679270361816100105882629459) |
| `left:2842:extra_shell:m751` | `extra_shell` | 8 | `NNNNNNNN` | 0 | 8 | 0 | 2.293964781395 (55604956035864843393004/24239672939547702829783) |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 9 | `NONNNNNNN` | 2 | 8 | 1 | 2.738851807222 (84686545608552246572466/30920455566538782401519) |
| `left:2842:selected_terminal:m761` | `selected_terminal` | 10 | `OONONNNNNN` | 3 | 7 | 3 | 2.465197873782 (71440426330627972298019/28979591086954608509153) |
| `right:1887:extra_shell:m479` | `extra_shell` | 4 | `NNNN` | 0 | 4 | 0 | 1.050154801037 (46390993056/44175385391) |
| `right:1887:selected_terminal:m769` | `selected_terminal` | 4 | `NNNN` | 0 | 4 | 0 | 0.940741608594 (41557623113/44175385391) |
| `right:1887:selected_terminal:m773` | `selected_terminal` | 3 | `NNO` | 1 | 2 | 1 | 0.212742927047 (8834523228/41526754147) |

## 3. quadrant residual-flow summary

| residual side | direction pair | events | mass |
| --- | --- | ---: | --- |
| `new` | `negative->positive` | 21 | 3.831280089934 (264859987871297303508715302188929026757093095351577/69130938395016822099452973148919227136792312500447) |
| `new` | `positive->negative` | 21 | 9.433259380948 (831966751154270935531577374944465196440988627210638/88195046648942059920997564570529412060602526622489) |
| `old` | `negative->positive` | 3 | 0.100854884293 (6371408629/63174021503) |
| `old` | `positive->negative` | 2 | 0.114684454479 (21291801/185655511) |

## 4. old-side residual exceptions

| atom | q | old/new run | direction | residual | ratio |
| --- | ---: | --- | --- | --- | --- |
| `left:2842:selected_terminal:m761` | 563 | 0->1 | `negative->positive` | 0.075506206368 (23243/307829) | 0.911590037004 (12266093/13455712) |
| `left:2842:selected_terminal:m757` | 569 | 1->2 | `positive->negative` | 0.067012828938 (20701/308911) | 0.468789634613 (10394774/22173643) |
| `left:2842:selected_terminal:m761` | 599 | 5->6 | `positive->negative` | 0.047671625541 (15500/325141) | 0.594167516914 (6796583/11438833) |
| `right:1887:selected_terminal:m773` | 457 | 2->3 | `negative->positive` | 0.017995938314 (3642/202379) | 0.919058420977 (18898511/20562905) |
| `left:2842:selected_terminal:m761` | 571 | 2->3 | `negative->positive` | 0.007352739611 (2414/328313) | 0.898980981607 (6133251/6822448) |

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BoundaryResidualSideLedgerClosed` | `true` | `true` | all 47 adjacent boundary events have exact old/new residual side and mass. | `finite residual-flow side ledger` |
| `FiniteBoundaryLocalOppositeSideCancellation` | `false` | `false` | new-side and old-side residual masses are not equal even after atomwise matching. | `BoundaryDominantNewResidualSourceLawOrPDEC` |
| `BoundaryDirectionEventBalance` | `true` | `true` | direction counts are 24 versus 23, but residual mass by direction is still unbalanced. | `BoundaryAdjacentRunMassRatioLawOrPDEC` |
| `BoundaryResidualTransportOutsideBoundary` | `false` | `false` | the leftover new-side source must be transported to non-boundary/internal returns or paid by PDEC. | `BoundaryResidualTransportToNonBoundaryInternalReturnsOrPDEC` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite obstruction certificate, not a global parity-breaking theorem. | `PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |

## 6. 最新开放口

```text
BoundaryDominantNewResidualSourceLawOrPDEC AND BoundaryResidualTransportToNonBoundaryInternalReturnsOrPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND BoundaryResidualFlowSourceKeyConservationOrPDEC AND NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC AND InternalPrefixRecordSurvivorPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-split-ratio-obstruction-router.json` | `531aa4dbe2be427b1a131cfc43693df97c4ff8948cd1c48c7c7a2a3e97d5266a` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_residual_flow_obstruction_router.py` | `e82b3100d316f7e1d83ffda0136a0b4941640c11778281d6c1121ef414f168ed` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_split_ratio_obstruction_router.py` | `cb26bc126ef132c7b357ca944946772fbe169e951d997ba56edbfcd70ae6219b` |

行/列命题仍未无条件闭合。
