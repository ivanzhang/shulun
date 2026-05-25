# Prime Matrix Phi-LPF terminal adjacent-run Jordan cancellation source obstruction 证书

**状态：** `formal_jordan_cancellation_closed_source_preserving_pairing_open`
**核验日期：** `2026-05-25`

本证书寻找统一相邻抵消律。结论是：形式律已找到，它就是相位路径
`A(q)/q` 的 signed telescoping/Jordan 分解；actual 证明仍缺源保持 pairing。

```text
terminal_phase_path_count=7
terminal_transition_count_total=126
terminal_run_count_total=59
sign_matches_Awrap_all_transitions=true
maximal_run_reconstruction_closed=true
signed_telescoping_identity_closed=true
formal_jordan_cancellation_law_closed=true
cancellation_event_count=51
complete_whole_run_pair_event_count=0
synthetic_split_cancellation_event_count=51
survivor_fragment_count_total=8
internal_survivor_fragment_count=1
tail_only_survivor_law_proved=false
source_preserving_adjacent_run_pairing_constructed=false
row_column_unconditional_closed=false
```

## 1. atom 形式律

| atom | role | P | m | transitions | runs | sign=Awrap | telescope | Jordan | survivor |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| `left:2842:extra_shell:m719` | `extra_shell` | 739 | 719 | 27 | 10 | `true` | `true` | `true` | 0.356428699921 (136715/383569) `negative` |
| `left:2842:extra_shell:m751` | `extra_shell` | 739 | 751 | 27 | 9 | `true` | `true` | `true` | 0.462466987687 (177388/383569) `negative` |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 739 | 757 | 27 | 11 | `true` | `true` | `true` | 0.038532832424 (14780/383569) `negative` |
| `left:2842:selected_terminal:m761` | `selected_terminal` | 739 | 761 | 27 | 14 | `true` | `true` | `true` | 0.032752907560 (12563/383569) `positive` |
| `right:1887:extra_shell:m479` | `extra_shell` | 607 | 479 | 6 | 5 | `true` | `true` | `true` | 0.088823635574 (18210/205013) `negative` |
| `right:1887:selected_terminal:m769` | `selected_terminal` | 607 | 769 | 6 | 5 | `true` | `true` | `true` | 0.601039934053 (123221/205013) `negative` |
| `right:1887:selected_terminal:m773` | `selected_terminal` | 607 | 773 | 6 | 5 | `true` | `true` | `true` | 0.849746113661 (174209/205013) `negative` |

## 2. 源保持障碍

抵消不是完整 run 对完整 run 的自然 involution，而需要切分质量块。样本：

| atom | old run | new run | old dir | new dir | chunk | old consumed | new consumed |
| --- | ---: | ---: | --- | --- | --- | --- | --- |
| `left:2842:extra_shell:m719` | 0 | 1 | `positive` | `negative` | 0.488057442471 (148654/304583) | `true` | `false` |
| `left:2842:extra_shell:m719` | 1 | 2 | `negative` | `positive` | 0.290482703059 (89419/307829) | `true` | `false` |
| `left:2842:extra_shell:m719` | 2 | 3 | `positive` | `negative` | 0.346733130332 (110111/317567) | `true` | `false` |
| `left:2842:extra_shell:m719` | 3 | 4 | `negative` | `positive` | 0.483455173286 (156668/324059) | `true` | `false` |
| `left:2842:extra_shell:m719` | 4 | 5 | `positive` | `negative` | 0.409009552657 (139624/341371) | `true` | `false` |
| `left:2842:extra_shell:m719` | 5 | 6 | `negative` | `positive` | 0.262116436598 (90897/346781) | `true` | `false` |
| `left:2842:extra_shell:m719` | 6 | 7 | `positive` | `negative` | 0.365779178470 (130803/357601) | `true` | `false` |
| `left:2842:extra_shell:m719` | 7 | 8 | `negative` | `positive` | 0.373465021300 (135976/364093) | `true` | `false` |
| `left:2842:extra_shell:m719` | 8 | 9 | `positive` | `negative` | 0.459876437411 (174404/379241) | `true` | `false` |
| `left:2842:extra_shell:m751` | 0 | 1 | `negative` | `positive` | 0.119867399730 (35472/295927) | `true` | `false` |
| `left:2842:extra_shell:m751` | 1 | 2 | `positive` | `negative` | 0.012842764081 (3870/301337) | `true` | `false` |
| `left:2842:extra_shell:m751` | 2 | 3 | `negative` | `positive` | 0.861355534983 (280062/325141) | `true` | `false` |

内部 survivor fragment：

| atom | run | dir | q interval | mass |
| --- | ---: | --- | --- | --- |
| `right:1887:selected_terminal:m773` | 2 | `negative` | `[449,457]` | 0.017995938314 (3642/202379) |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `AwrapSignLawClosed` | `true` | `true` | 所有 transition 的符号由 A(q)/q 是否 wrap 精确决定。 | `formal phase-path sign law` |
| `SignedTelescopingClosed` | `true` | `true` | 每个 atom 的 signed_delta 总和等于末端相位减初端相位。 | `one-dimensional phase telescoping` |
| `FormalJordanCancellationClosed` | `true` | `true` | total variation 被分解为 cancelled chunks 与 survivor，这是形式 Jordan 恒等式。 | `formal cancellation law only` |
| `WholeRunInvolutionClosesCancellation` | `false` | `false` | 抵消事件需要切分 run 质量，不是完整 run 对完整 run 的自然 involution。 | `SourcePreservingAdjacentRunPairingOrInternalSurvivorPDEC` |
| `TailOnlySurvivorLaw` | `false` | `false` | 存在内部 survivor fragment，不能只用右端尾段 survivor 律闭合。 | `InternalSurvivorPDECOrSourcePreservingPairing` |
| `SourcePreservingPairingConstructed` | `false` | `false` | 尚未把形式抵消块绑定到 pre-Cauchy source/orientation/local-factor 键。 | `SourcePreservingAdjacentRunPairingOrInternalSurvivorPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步找到统一形式抵消律，但未生成 actual signed payload 定理。 | `SourcePreservingAdjacentRunPairingOrInternalSurvivorPDEC AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |

## 4. 外部前沿适配

| input | source | current use |
| --- | --- | --- |
| Fouvry-Kowalski-Michel-Sawin, Bilinear forms with trace functions | https://arxiv.org/abs/2511.09459 | only after adjacent-run chunks become a trace-function bilinear family |
| Milićević-Qin-Wu, Bilinear forms with Kloosterman sums | https://arxiv.org/abs/2511.07550 | only after moving Beatty phases are completed to a bilinear Kloosterman family |
| Pascadi, On the exponents of distribution of primes and smooth numbers | https://arxiv.org/abs/2505.00653 | only after the pointwise row/column load is turned into well-factorable AP averages |
| Wright, Trilinear Kloosterman fractions I | https://arxiv.org/abs/2604.25177 | only after terminal payload becomes a trilinear convolution with equidistributed beta sequence |

## 5. 最新开放口

```text
SourcePreservingAdjacentRunPairingOrInternalSurvivorPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json` | `e05dc6c48cd18aaa25cef5abe9aa5dc346d5b07db0827c8443dcefe536111615` |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json` | `ec3616097527b1bf9d426727572ea66b66e15f92ca243d44221f5973437d8613` |
| `experiments/prime_matrix_phi_lpf_terminal_adjacent_run_jordan_cancellation_source_obstruction_router.py` | `20b2672e45b8127691a8b7bd76461a08b38adaae83ca356e3ad6c0993104ef86` |

行/列命题仍未无条件闭合。
