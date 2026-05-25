# Prime Matrix Phi-LPF terminal boundary split ratio obstruction 证书

**状态：** `boundary_split_ratio_spectrum_closed_ratio_source_key_law_open`
**核验日期：** `2026-05-25`

本证书把 q-boundary synthetic split 分支压成相邻 run 质量比率谱。

```text
previous_source_key_obstruction_partition_closed=true
q_boundary_synthetic_split_event_count=47
boundary_adjacency_closed=true
whole_equal_pair_event_count=0
synthetic_split_event_count=47
old_consumed_new_residual_event_count=42
old_residual_new_consumed_event_count=5
negative_to_positive_event_count=24
positive_to_negative_event_count=23
boundary_ratio_spectrum_closed=true
boundary_synthetic_split_ratio_source_key_law_proved=false
row_column_unconditional_closed=false
```

## 1. ratio totals

| quantity | value |
| --- | --- |
| `ratio_min` | 0.013003592969 (415829/31978008) |
| `ratio_max` | 0.967151620496 (169997634/175771441) |
| `boundary_chunk_mass_total` | 14.631796550631 (11300120486994743871953452237691197733518695954935357389819382388044553919/772298907238916261289587790898356540320031771197428129590077001137691901) |
| `boundary_residual_gap_mass_total` | 13.480078809654 (18704725831274706221411647651674960542383244116881133974210171827029401/1387582824655253501519413061432408291809940502746766545644906695501703) |
| `boundary_residual_gap_mass_max` | 0.861355534983 (280062/325141) |

## 2. atom ratio summary

| atom | role | events | chunk mass | residual mass | ratio min | ratio max | old consumed | new consumed |
| --- | --- | ---: | --- | --- | --- | --- | ---: | ---: |
| `left:2842:extra_shell:m719` | `extra_shell` | 9 | 3.478975075583 (26739673357718428729175749722/7686077875461867926109901813) | 3.347346333033 (32399870152060550712283521969/9679270361816100105882629459) | 0.417452248922 (27101/64920) | 0.626887958537 (7689466/12266093) | 9 | 0 |
| `left:2842:extra_shell:m751` | `extra_shell` | 8 | 1.951365193439 (36492733961628521825208/18701129898353446329889) | 2.293964781395 (55604956035864843393004/24239672939547702829783) | 0.014690904907 (129215/8795578) | 0.967151620496 (169997634/175771441) | 8 | 0 |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 9 | 3.433026065167 (15024302909640266450183994759071/4376402224871392586998345173751) | 2.872877465098 (27440774191849321709934734164/9551668849515061810435635809) | 0.119395026649 (50381/421969) | 0.846169045837 (120260426/142123405) | 8 | 1 |
| `left:2842:selected_terminal:m761` | `selected_terminal` | 10 | 3.827051185252 (3571582840913344148351018622169456424527/933246687338919490296248231194601552083) | 2.726259016822 (27397419102758177057923755853/10049455658360858274978549881) | 0.013003592969 (415829/31978008) | 0.959283315282 (280764/292681) | 7 | 3 |
| `right:1887:extra_shell:m479` | `extra_shell` | 4 | 1.170451009968 (49047901777/41905130039) | 1.050154801037 (46390993056/44175385391) | 0.309657742695 (11472907/37050283) | 0.861629155039 (8712352/10111487) | 4 | 0 |
| `right:1887:selected_terminal:m769` | `selected_terminal` | 4 | 0.430216234104 (18028267235/41905130039) | 0.940741608594 (41557623113/44175385391) | 0.230421946827 (28020/121603) | 0.630959553820 (9079219/14389542) | 4 | 0 |
| `right:1887:selected_terminal:m773` | `selected_terminal` | 3 | 0.340711787118 (14277571745/41905130039) | 0.248734803675 (10329149040/41526754147) | 0.036432661143 (757249/20784894) | 0.938358108461 (11174263/11908314) | 2 | 1 |

## 3. smallest ratio events

| atom | old/new run | boundary q | ratio | residual | consumed pattern |
| --- | --- | ---: | --- | --- | --- |
| `left:2842:selected_terminal:m761` | 7->8 | 607 | 0.013003592969 (415829/31978008) | 0.822670087625 (311982/379231) | `old=true, new=false` |
| `left:2842:extra_shell:m751` | 1->2 | 557 | 0.014690904907 (129215/8795578) | 0.861355534983 (280062/325141) | `old=true, new=false` |
| `right:1887:selected_terminal:m773` | 1->2 | 449 | 0.036432661143 (757249/20784894) | 0.222332434467 (44605/200623) | `old=true, new=false` |
| `left:2842:extra_shell:m751` | 5->6 | 617 | 0.061958571682 (990839/15991960) | 0.747881018230 (267443/357601) | `old=true, new=false` |
| `left:2842:selected_terminal:m761` | 9->10 | 641 | 0.073951746279 (15203/205580) | 0.613765062178 (219483/357601) | `old=true, new=false` |
| `left:2842:extra_shell:m751` | 7->8 | 673 | 0.102422776312 (6811363/66502425) | 0.462466987687 (177388/383569) | `old=true, new=false` |
| `left:2842:selected_terminal:m757` | 3->4 | 577 | 0.119395026649 (50381/421969) | 0.780387597123 (270480/346597) | `old=true, new=false` |
| `left:2842:selected_terminal:m761` | 11->12 | 673 | 0.120319514127 (9113/75740) | 0.771657072943 (292644/379241) | `old=true, new=false` |
| `right:1887:selected_terminal:m769` | 3->4 | 461 | 0.230421946827 (28020/121603) | 0.601039934053 (123221/205013) | `old=true, new=false` |
| `right:1887:selected_terminal:m769` | 2->3 | 457 | 0.246750581899 (5452247/22096187) | 0.179959383138 (36420/202379) | `old=true, new=false` |
| `left:2842:selected_terminal:m757` | 5->6 | 617 | 0.249817210926 (30409/121725) | 0.624934647899 (218744/350027) | `old=true, new=false` |
| `left:2842:selected_terminal:m757` | 7->8 | 653 | 0.251881376046 (17709639/70309442) | 0.646423116328 (241653/373831) | `old=true, new=false` |

## 4. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BoundaryAdjacencyClosed` | `true` | `true` | all 47 events are adjacent q-boundary events with run_distance=1. | `formal deterministic boundary ledger` |
| `BoundaryRatioSpectrumClosed` | `true` | `true` | each boundary split has an exact old/new mass ratio and residual side. | `finite ratio spectrum` |
| `BoundaryEqualWholeRunInvolution` | `false` | `false` | no boundary event has equal old/new run masses. | `BoundaryAdjacentRunMassRatioLawOrPDEC` |
| `BoundaryResidualFlowSourceKeyConservation` | `false` | `false` | 42 events leave a new-run residual and 5 leave an old-run residual; this needs source-key conservation. | `BoundaryResidualFlowSourceKeyConservationOrPDEC` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | the boundary ratio spectrum is finite evidence, not a global parity-breaking theorem. | `PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |

## 5. 最新开放口

```text
BoundaryAdjacentRunMassRatioLawOrPDEC AND BoundaryResidualFlowSourceKeyConservationOrPDEC AND NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC AND InternalPrefixRecordSurvivorPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-source-key-obstruction-partition-router.json` | `5f855cce874423998dc3046cbf66f7a3930b939520d1103766f0f0bae77a65e3` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_split_ratio_obstruction_router.py` | `cb26bc126ef132c7b357ca944946772fbe169e951d997ba56edbfcd70ae6219b` |
| `experiments/prime_matrix_phi_lpf_terminal_prefix_record_source_key_obstruction_router.py` | `72125d4034079273695d40955e9d3e65835c7ea341a7abdbf943cd47179e5834` |

行/列命题仍未无条件闭合。
