# Prime Matrix Phi-LPF terminal prefix-record source-key obstruction 证书

**状态：** `prefix_record_reflection_closed_source_key_lift_open`
**核验日期：** `2026-05-25`

本证书把形式 Jordan 抵消推进为 prefix-record/reflection 账本，并检查它是否已经
给出 source-preserving pairing。结论：形式反射闭合，source-key lift 仍未闭合。

```text
previous_formal_jordan_cancellation_law_closed=true
terminal_atom_count=7
terminal_run_count_total=59
prefix_record_reflection_schema_closed=true
cancellation_event_count=51
whole_run_pair_event_count=0
synthetic_split_event_count=51
q_boundary_pair_event_count=47
non_q_boundary_pair_event_count=4
survivor_fragment_count_total=8
internal_survivor_fragment_count=1
tail_only_survivor_law_proved=false
prefix_record_source_key_lift_constructed=false
row_column_unconditional_closed=false
```

## 1. atom prefix 摘要

| atom | role | P | m | runs | net | prefix min | prefix max | events | non-boundary | survivors | internal |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| `left:2842:extra_shell:m719` | `extra_shell` | 739 | 719 | 10 | -0.356428699921 (-136715/383569) | -0.483455173286 (-156668/324059) @ `3` | 0.488057442471 (148654/304583) @ `0` | 9 | 0 | 1 | 0 |
| `left:2842:extra_shell:m751` | `extra_shell` | 739 | 751 | 9 | -0.462466987687 (-177388/383569) | -0.861355534983 (-280062/325141) @ `2` | 0.052772231271 (19214/364093) @ `7` | 8 | 0 | 1 | 0 |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 739 | 757 | 11 | -0.038532832424 (-14780/383569) | -0.713374768185 (-234263/328387) @ `4` | 0.217641880359 (76887/353273) @ `7` | 10 | 1 | 1 | 0 |
| `left:2842:selected_terminal:m761` | `selected_terminal` | 739 | 761 | 14 | 0.032752907560 (12563/383569) | -0.854046351898 (-260128/304583) @ `0` | 0.117466263859 (38066/324059) @ `5` | 13 | 3 | 1 | 0 |
| `right:1887:extra_shell:m479` | `extra_shell` | 607 | 479 | 5 | -0.088823635574 (-18210/205013) | -0.248097177293 (-49774/200623) @ `2` | 0.553100865208 (111936/202379) @ `3` | 4 | 0 | 1 | 0 |
| `right:1887:selected_terminal:m769` | `selected_terminal` | 607 | 769 | 5 | -0.601039934053 (-123221/205013) | -0.601039934053 (-123221/205013) @ `4` | 0.179959383138 (36420/202379) @ `3` | 4 | 0 | 1 | 0 |
| `right:1887:selected_terminal:m773` | `selected_terminal` | 607 | 773 | 5 | -0.849746113661 (-174209/205013) | -0.849746113661 (-174209/205013) @ `4` | 0.008406430894 (1657/197111) @ `1` | 3 | 0 | 2 | 1 |

## 2. 非边界 pairing 事件

| atom | old run | new run | old q_end | new q_start | run distance | chunk |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `left:2842:selected_terminal:m757` | 1 | 4 | 569 | 577 | 3 | 0.067012828938 (20701/308911) |
| `left:2842:selected_terminal:m761` | 2 | 5 | 571 | 593 | 3 | 0.007352739611 (2414/328313) |
| `left:2842:selected_terminal:m761` | 0 | 5 | 563 | 593 | 5 | 0.075506206368 (23243/307829) |
| `left:2842:selected_terminal:m761` | 5 | 8 | 599 | 607 | 3 | 0.047671625541 (15500/325141) |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PrefixRecordReflectionSchemaClosed` | `true` | `true` | 相邻抵消可写成前缀极值/反射式有限分解。 | `formal deterministic ledger` |
| `WholeRunPairingSchemaClosed` | `false` | `false` | 没有任何完整 run-to-run 抵消事件；全部需要切分质量。 | `PrefixRecordSourceKeyLiftOrPDEC` |
| `QBoundaryOnlyPairingSchemaClosed` | `false` | `false` | 存在非 q-boundary pairing，不能仅靠相邻边界局部律闭合。 | `NonBoundaryPrefixRecordSourceKeyLiftOrPDEC` |
| `TailOnlySurvivorLawProved` | `false` | `false` | 存在内部 survivor，不能只用尾段 survivor 律闭合。 | `InternalPrefixRecordSurvivorPDEC` |
| `SourceKeyLiftConstructed` | `false` | `false` | 尚未把 prefix-record 反射块提升到 pre-Cauchy/source/orientation 键。 | `PrefixRecordSourceKeyLiftOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步闭合前缀反射账本，没有证明三命题无条件闭合。 | `SourcePreservingAdjacentRunPairingOrInternalSurvivorPDEC AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |

## 4. 最新开放口

```text
PrefixRecordSourceKeyLiftOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json` | `e05dc6c48cd18aaa25cef5abe9aa5dc346d5b07db0827c8443dcefe536111615` |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-adjacent-run-jordan-cancellation-source-obstruction-router.json` | `0c18e61b945499886d3f0d3720f0fd5a119a2d264dbb714be71236504fe121c7` |
| `experiments/prime_matrix_phi_lpf_terminal_prefix_record_source_key_obstruction_router.py` | `72125d4034079273695d40955e9d3e65835c7ea341a7abdbf943cd47179e5834` |

行/列命题仍未无条件闭合。
