# Prime Matrix Phi-LPF terminal source-key obstruction partition 证书

**状态：** `source_key_obstruction_partition_closed_three_actual_gates_open`
**核验日期：** `2026-05-25`

本证书把 `PrefixRecordSourceKeyLiftOrPDEC` 拆成三类实际缺口：
q-boundary synthetic split、non-boundary record jump、internal survivor。

```text
previous_prefix_record_reflection_schema_closed=true
source_key_obstruction_partition_closed=true
cancellation_event_count=51
whole_run_pair_event_count=0
synthetic_split_event_count=51
q_boundary_synthetic_split_event_count=47
nonboundary_record_jump_event_count=4
nonboundary_record_jump_atom_count=2
old_consumed_new_residual_event_count=46
old_residual_new_consumed_event_count=5
survivor_fragment_count_total=8
tail_survivor_fragment_count=7
internal_survivor_fragment_count=1
finite_margin_after_nonboundary_internal_payment_positive=true
row_column_unconditional_closed=false
```

## 1. event partition

| atom | partition | events | mass | max distance | old consumed | new consumed |
| --- | --- | ---: | --- | ---: | ---: | ---: |
| `left:2842:extra_shell:m719` | `q_boundary_synthetic_split` | 9 | 3.478975075583 (26739673357718428729175749722/7686077875461867926109901813) | 1 | 9 | 0 |
| `left:2842:extra_shell:m751` | `q_boundary_synthetic_split` | 8 | 1.951365193439 (36492733961628521825208/18701129898353446329889) | 1 | 8 | 0 |
| `left:2842:selected_terminal:m757` | `nonboundary_record_jump` | 1 | 0.067012828938 (20701/308911) | 3 | 1 | 0 |
| `left:2842:selected_terminal:m757` | `q_boundary_synthetic_split` | 9 | 3.433026065167 (15024302909640266450183994759071/4376402224871392586998345173751) | 1 | 8 | 1 |
| `left:2842:selected_terminal:m761` | `nonboundary_record_jump` | 3 | 0.130530571520 (45265/346777) | 5 | 3 | 0 |
| `left:2842:selected_terminal:m761` | `q_boundary_synthetic_split` | 10 | 3.827051185252 (3571582840913344148351018622169456424527/933246687338919490296248231194601552083) | 1 | 7 | 3 |
| `right:1887:extra_shell:m479` | `q_boundary_synthetic_split` | 4 | 1.170451009968 (49047901777/41905130039) | 1 | 4 | 0 |
| `right:1887:selected_terminal:m769` | `q_boundary_synthetic_split` | 4 | 0.430216234104 (18028267235/41905130039) | 1 | 4 | 0 |
| `right:1887:selected_terminal:m773` | `q_boundary_synthetic_split` | 3 | 0.340711787118 (14277571745/41905130039) | 1 | 2 | 1 |

## 2. non-boundary record jumps

| atom | old run | new run | old q_end | new q_start | distance | chunk |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `left:2842:selected_terminal:m757` | 1 | 4 | 569 | 577 | 3 | 0.067012828938 (20701/308911) |
| `left:2842:selected_terminal:m761` | 2 | 5 | 571 | 593 | 3 | 0.007352739611 (2414/328313) |
| `left:2842:selected_terminal:m761` | 0 | 5 | 563 | 593 | 5 | 0.075506206368 (23243/307829) |
| `left:2842:selected_terminal:m761` | 5 | 8 | 599 | 607 | 3 | 0.047671625541 (15500/325141) |

## 3. survivor partition

| atom | run | q interval | type | mass |
| --- | ---: | --- | --- | --- |
| `left:2842:extra_shell:m719` | 9 | [701,709] | `tail_survivor` | 0.356428699921 (136715/383569) |
| `left:2842:extra_shell:m751` | 8 | [673,709] | `tail_survivor` | 0.462466987687 (177388/383569) |
| `left:2842:selected_terminal:m757` | 10 | [701,709] | `tail_survivor` | 0.038532832424 (14780/383569) |
| `left:2842:selected_terminal:m761` | 13 | [701,709] | `tail_survivor` | 0.032752907560 (12563/383569) |
| `right:1887:extra_shell:m479` | 4 | [461,467] | `tail_survivor` | 0.088823635574 (18210/205013) |
| `right:1887:selected_terminal:m769` | 4 | [461,467] | `tail_survivor` | 0.601039934053 (123221/205013) |
| `right:1887:selected_terminal:m773` | 2 | [449,457] | `internal_survivor` | 0.017995938314 (3642/202379) |
| `right:1887:selected_terminal:m773` | 4 | [461,467] | `tail_survivor` | 0.831750175347 (179065/215287) |

## 4. finite scalar check

| quantity | value |
| --- | --- |
| nonboundary plus internal obstruction mass | 0.215539338772 (4672783399294642/21679492133206013) |
| selected finite margin after that subtraction | 0.333307310624 (2392528166482640981268/7178144883780910522339) |

该标量余量不是证明；它只说明有限样本中非边界 jump 与内部 survivor 的质量本身
不是最大的数值障碍。真正缺口仍是 source-key lift 与 orientation/local-factor law。

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `SourceKeyObstructionPartitionClosed` | `true` | `true` | prefix-record source-key failure is split into boundary splits, non-boundary jumps, and internal survivor. | `formal deterministic partition` |
| `BoundarySyntheticSplitRatioSourceKeyLaw` | `false` | `false` | 47 q-boundary cancellations still split masses and need a pre-pushforward source ratio law. | `BoundarySyntheticSplitRatioSourceKeyLawOrPDEC` |
| `NonBoundaryPrefixRecordJumpSourceKeyLift` | `false` | `false` | 4 cancellations jump across q-boundaries and cannot be certified by adjacent q-locality. | `NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC` |
| `InternalPrefixRecordSurvivorPDEC` | `false` | `false` | 1 selected-terminal survivor is internal rather than tail-only. | `InternalPrefixRecordSurvivorPDEC` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | the partition is finite evidence, not a global Phi-LPF parity-breaking theorem. | `PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |

## 6. 最新开放口

```text
BoundarySyntheticSplitRatioSourceKeyLawOrPDEC AND NonBoundaryPrefixRecordJumpSourceKeyLiftOrPDEC AND InternalPrefixRecordSurvivorPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json` | `ec3616097527b1bf9d426727572ea66b66e15f92ca243d44221f5973437d8613` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-prefix-record-source-key-obstruction-router.json` | `567dde4948ec2f22e3b4babeccea9e3e667e3ba4261192deddd97e87285f2b3e` |
| `experiments/prime_matrix_phi_lpf_terminal_prefix_record_source_key_obstruction_router.py` | `72125d4034079273695d40955e9d3e65835c7ea341a7abdbf943cd47179e5834` |
| `experiments/prime_matrix_phi_lpf_terminal_source_key_obstruction_partition_router.py` | `a6e67251f057343472d4791ecec76c366ba8c298482cdb76e37153232244792c` |

行/列命题仍未无条件闭合。
