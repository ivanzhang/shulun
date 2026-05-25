# Prime Matrix Phi-LPF terminal boundary bridge-root q-spine microtemplate 证书

**状态：** `bridge_root_qspine_microtemplate_closed_source_law_open`
**核验日期：** `2026-05-25`

本证书把两个 bridge-root debt 压成共享 q-spine 微模板。

```text
previous_carry_break_source_packet_reduction_closed=true
bridge_root_packet_count=2
all_bridge_roots_share_ad_singleton_template=true
unit_to_bridge_pivot_alignment_closed=true
shared_pivot_q=607
m_gap_between_bridge_packets=4
root_micro_q_shift=30
bridge_to_unit_q_gaps=[30, 24]
bridge_root_qspine_microtemplate_closed=true
bridge_root_qspine_source_law_proved=false
row_column_unconditional_closed=false
```

## 1. q-spine summary

| field | value |
| --- | --- |
| `q_spine_node_count` | `3` |
| `q_spine_nodes` | `[577, 607, 631]` |
| `shared_pivot_q` | `607` |
| `unit_to_bridge_pivot_alignment_closed` | `True` |
| `m_gap_between_bridge_packets` | `4` |
| `root_micro_q_shift` | `30` |
| `same_P` | `True` |
| `same_packet_index` | `True` |
| `same_packet_side` | `True` |
| `same_role` | `True` |
| `bridge_to_unit_q_gaps` | `[30, 24]` |

## 2. bridge-root microtemplates

| packet | atom | P | bridge q | unit q | pre bridge run | bridge old run | following run | unit run | bridge debt |
| ---: | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `left:2842:selected_terminal:m757` | 739 | 577 | 607 | r2 negative q569->571 A1/D0 c2..2 | r3 positive q571->577 A0/D1 c7..7 | r4 negative q577->607 A5/D0 c2..10 | r5 positive q607->617 A0/D1 c5..6 | 0.020343948936 (2063273071/101419497143) |
| 2 | `left:2842:selected_terminal:m761` | 739 | 607 | 631 | r6 negative q599->601 A1/D0 c2..2 | r7 positive q601->607 A0/D1 c7..7 | r8 negative q607->631 A4/D0 c2..12 | r9 positive q631->641 A0/D1 c11..11 | 0.189486602027 (23891548917/126085689761) |

## 3. mass ledger

| mass | value |
| --- | --- |
| bridge-root debt still open | 0.209830550963 (4650291309275317106/22162126954053594199) |
| unit old-return echo mass | 0.114684454479 (21291801/185655511) |

## 4. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BridgeRootADSingletonMicrotemplateLedger` | `true` | `true` | both bridge roots are preceded by the same negative A-singleton and positive D-singleton run pair. | finite bridge-root microtemplate ledger |
| `BridgeRootQSpinePivotLedger` | `true` | `true` | the first packet unit root q equals the second packet bridge root q. | shared q=607 pivot ledger |
| `BridgeRootQSpineSourceLaw` | `false` | `false` | the shared AD-singleton q-spine still needs a uniform source law or named PDEC. | BridgeRootADSingletonQSpineSourceLawOrPDEC |
| `RightTailOverhangPDEC` | `false` | `false` | the single right selected-terminal tail overhang is unchanged. | RightSelectedTerminalTailOverhangPDEC |
| `ExternalTraceOrGroupEntry` | `false` | `false` | trace/Kloosterman/Type-II or group-expansion inputs still need a signed averaged family built from the q-spine. | AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite q-spine microtemplate reduction, not a global parity-breaking theorem. | BridgeRootADSingletonQSpineSourceLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving |

## 5. 最新开放口

```text
BridgeRootADSingletonQSpineSourceLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-carry-break-source-packet-router.json` | `e352152ebee0b366126014257df6013cd054e827004ff882dc67e943dde1ea4c` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_microtemplate_router.py` | `9f17b8544cfd719f8a1d3f0f117c18cede1c78b18d530117124a6ae7019da375` |

行/列命题仍未无条件闭合。
