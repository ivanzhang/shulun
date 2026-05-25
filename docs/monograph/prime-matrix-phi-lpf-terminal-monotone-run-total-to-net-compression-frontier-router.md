# Prime Matrix Phi-LPF terminal monotone-run total-to-net compression frontier 证书

**状态：** `finite_run_decomposition_closed_uniform_compression_open`
**核验日期：** `2026-05-25`

本证书继续上一层 signed payload absorption，逐 run 检查 total variation 能否压成 net。
结论是：有限相消分解可闭合，但全局 run-cancellation 定理仍未证明。

```text
previous_terminal_signed_payload_schema_closed=true
terminal_monotone_run_ledger_closed=true
terminal_run_count_total=59
selected_terminal_run_count=35
extra_shell_run_count=24
strict_run_local_compression_count=0
atom_adjacent_cancellation_decomposition_closed=true
finite_absorption_would_close_after_uniform_cancellation_law=true
monotone_run_total_to_net_compression_proved=false
uniform_run_cancellation_family_created=false
extra_total_variation_absorption_proved=false
trace_or_kloosterman_completion_ready=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

## 1. 压缩读数

```text
selected_negative_excess=1.456565972578 (114539441491/78636631397)
extra_total_variation=14.109301881162 (27768758142307772418840319934041830802744822617132968593977647725/1968117088725958506051611620121066252424277248250429833368124847)
extra_atom_local_survivor_total=0.907719323182 (71379989829/78636631397)
extra_total_to_atom_survivor_compression_ratio=0.064334814779 (1786497911721324096105724649360006725755550062258369319434886479/27768758142307772418840319934041830802744822617132968593977647725)
extra_total_to_atom_survivor_variation_removed=13.201582557980 (178751334270449465685158589411147418426733863214127453038/13540144409611167359882043326758564235011339562652178391)
selected_negative_excess_minus_extra_atom_survivor=0.548846649396 (43159451662/78636631397)
```

解释：若存在 uniform adjacent-run cancellation law，extra 的强总变差会被压到
atom-local survivor，有限账本中 selected negative excess 足以支付它。
但每个 monotone run 内部压缩比恒为 1，所需相消来自 run 间配对，不是局部事实。

## 2. role 汇总

| role | runs | transitions | +runs | -runs | total variation | signed net | abs net | total-to-net ratio | local ratio range |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| `extra_shell` | 24 | 60 | 11 | 13 | 14.109301881162 (27768758142307772418840319934041830802744822617132968593977647725/1968117088725958506051611620121066252424277248250429833368124847) | -0.907719323182 (-71379989829/78636631397) | 0.907719323182 (71379989829/78636631397) | 0.064334814779 (1786497911721324096105724649360006725755550062258369319434886479/27768758142307772418840319934041830802744822617132968593977647725) | `1.000000000000..1.000000000000` |
| `selected_terminal` | 35 | 66 | 16 | 19 | 17.979169131897 (18409482351943445293965578391556725137299870717352700685388218401134317/1023933988099770462723506583596845526698662565115878981568636879953733) | -1.456565972578 (-114539441491/78636631397) | 1.456565972578 (114539441491/78636631397) | 0.081014087019 (1491427405231834885050080915564173458276584564377359022242522311030899/18409482351943445293965578391556725137299870717352700685388218401134317) | `1.000000000000..1.000000000000` |

## 3. atom cancellation 分解

| atom | role | P | m | runs | total variation | cancelled removed | survivor | survivor direction | ratio | identity |
| --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- |
| `left:2842:extra_shell:m719` | `extra_shell` | 739 | 719 | 10 | 7.314378851086 (39859189791196246306766250492791/5449429213702464359611920385417) | 6.957950151165 (53479346715436857458351499444/7686077875461867926109901813) | 0.356428699921 (136715/383569) | `negative` | 0.048729865813 (1942332969951514368795037386995/39859189791196246306766250492791) | `true` |
| `left:2842:extra_shell:m751` | `extra_shell` | 739 | 751 | 9 | 4.365197374565 (31312318976264902113512764636/7173173693981533055309193841) | 3.902730386878 (72985467923257043650416/18701129898353446329889) | 0.462466987687 (177388/383569) | `negative` | 0.105944118445 (829339007602280284391587483/7828079744066225528378191159) | `true` |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 739 | 757 | 11 | 7.038610620634 (21839887946724610150799587828243196/3102869177433817344181826728189459) | 7.000077788210 (56626905742323524278083537864/8089468068154145262473835811) | 0.038532832424 (14780/383569) | `negative` | 0.005474494115 (29890584511829566744840823321645/5459971986681152537699896957060799) | `true` |
| `left:2842:selected_terminal:m761` | `selected_terminal` | 739 | 761 | 14 | 7.947916421105 (5258912969911360856935706921220147347487585/661671901323293918620039995916972500426847) | 7.915163513545 (7386800128761728341043269080273958363924/933246687338919490296248231194601552083) | 0.032752907560 (12563/383569) | `positive` | 0.004120942625 (29325681487544605055519815028296167071/7116255710299541078397438323707912513515) | `true` |
| `right:1887:extra_shell:m479` | `extra_shell` | 607 | 479 | 5 | 2.429725655511 (20874007392026392/8591096424685507) | 2.340902019937 (98095803554/41905130039) | 0.088823635574 (18210/205013) | `negative` | 0.036557063705 (381546209005095/10437003696013196) | `true` |
| `right:1887:selected_terminal:m769` | `selected_terminal` | 607 | 769 | 5 | 1.461472402260 (12555650329833729/8591096424685507) | 0.860432468207 (36056534470/41905130039) | 0.601039934053 (123221/205013) | `negative` | 0.411256437770 (8506741397917/20684761663647) | `true` |
| `right:1887:selected_terminal:m773` | `selected_terminal` | 607 | 773 | 5 | 1.531169687897 (13154426431279521/8591096424685507) | 0.681423574236 (28555143490/41905130039) | 0.849746113661 (174209/205013) | `negative` | 0.554965344715 (12026772321193/21671213231103) | `true` |

## 4. 最大 run 热点

| atom | role | run | dir | len | q | gap | wraps | carry | variation |
| --- | --- | ---: | --- | ---: | --- | --- | --- | --- | --- |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 5 | `positive` | 2 | `[607,617]` | `[4,6]` | `A0/D1` | `[5,6]` | 0.921483289232 (345113/374519) |
| `left:2842:extra_shell:m719` | `extra_shell` | 4 | `positive` | 6 | `[599,631]` | `[2,12]` | `A0/D5` | `[2,11]` | 0.892464725943 (337324/377969) |
| `left:2842:extra_shell:m751` | `extra_shell` | 3 | `positive` | 1 | `[601,607]` | `[6,6]` | `A0/D0` | `[6,6]` | 0.890610651660 (324901/364807) |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 4 | `negative` | 5 | `[577,607]` | `[2,10]` | `A5/D0` | `[2,10]` | 0.886194855513 (310380/350239) |
| `left:2842:selected_terminal:m761` | `selected_terminal` | 12 | `negative` | 4 | `[673,701]` | `[4,10]` | `A4/D0` | `[4,10]` | 0.877201535484 (413840/471773) |
| `left:2842:extra_shell:m751` | `extra_shell` | 2 | `negative` | 8 | `[557,601]` | `[2,10]` | `A8/D0` | `[2,10]` | 0.874198299065 (292644/334757) |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 8 | `negative` | 6 | `[653,691]` | `[2,12]` | `A6/D1` | `[2,12]` | 0.864064996687 (389886/451223) |
| `left:2842:selected_terminal:m761` | `selected_terminal` | 0 | `negative` | 3 | `[541,563]` | `[6,10]` | `A3/D0` | `[6,10]` | 0.854046351898 (260128/304583) |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 7 | `positive` | 1 | `[647,653]` | `[6,6]` | `A0/D0` | `[6,6]` | 0.842576528257 (355981/422491) |
| `left:2842:selected_terminal:m761` | `selected_terminal` | 8 | `negative` | 4 | `[607,631]` | `[2,12]` | `A4/D0` | `[2,12]` | 0.833508695436 (319248/383017) |
| `left:2842:extra_shell:m719` | `extra_shell` | 8 | `positive` | 4 | `[673,701]` | `[4,10]` | `A0/D4` | `[4,10]` | 0.833341458710 (393148/471773) |
| `left:2842:selected_terminal:m757` | `selected_terminal` | 6 | `negative` | 5 | `[617,647]` | `[2,12]` | `A5/D0` | `[2,12]` | 0.833043168946 (332550/399199) |

## 5. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalSignedPayloadImported` | `true` | `true` | 上一层 mu(q,m,packet) signed payload measure 已导入。 | `finite signed payload imported` |
| `MonotoneRunRowsClosed` | `true` | `true` | 59 个 monotone run 的 signed_delta、variation、wrap、carry、q-window 字段已全部抽取。 | `finite run ledger closed` |
| `RunLocalTotalToNetCompression` | `false` | `false` | 每个 monotone run 内 variation=abs(signed_delta)，局部压缩比恒为 1；run 内没有相消。 | `UniformAdjacentRunCancellationFamilyOrPDEC` |
| `AtomAdjacentCancellationDecompositionClosed` | `true` | `true` | 每个 atom 可有限分解为 adjacent opposite-run cancelled chunks 加 atom-local survivor。 | `finite decomposition only` |
| `ExtraTotalToAtomSurvivorIfCancellationLaw` | `true` | `false` | 若能全局证明 adjacent-run cancellation law，则 extra total variation 将压到 atom survivor。 | `UniformAdjacentRunCancellationFamilyOrPDEC OR AtomLocalSurvivorPaymentOrPDEC` |
| `SelectedBeatsExtraAtomSurvivorFiniteCheck` | `true` | `true` | 有限账本中 selected negative excess 已大于 extra atom-local survivor。 | `finite numerical check; not a global theorem` |
| `UniformRunCancellationLawProved` | `false` | `false` | 尚无可审稿的 uniform family/trace/Type-II 定理把 run cancellation 推广到所有反例链。 | `UniformAdjacentRunCancellationFamilyOrPDEC AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |
| `NamedLocalSurvivorReturnRegistered` | `true` | `false` | 若 cancellation law 失败，剩余必须登记为 PDEC/SAE/LocalSurvivor，不能保留匿名。 | `ExtraTotalVariationAbsorptionOrLocalSurvivor OR AtomLocalSurvivorPaymentOrPDEC` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步闭合有限 run 分解和真正缺口位置，没有证明三命题无条件闭合。 | `MonotoneRunTotalToNetCompressionOrPDEC AND ExtraTotalVariationAbsorptionOrLocalSurvivor AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |

## 6. 外部前沿适配

| input | date | usable after | current gap | url |
| --- | --- | --- | --- | --- |
| Fouvry-Kowalski-Michel-Sawin, arXiv:2511.09459v3 | `2026-03-11` | terminal runs are promoted to a bilinear trace-function family with monodromy data | the present object is a finite run ledger, not an ell-adic trace family | https://arxiv.org/abs/2511.09459 |
| Milicevic-Qin-Wu, arXiv:2511.07550v1 | `2025-11-10` | moving Beatty numerator is completed into a genuine bilinear Kloosterman sum modulo q | no admissible two-variable Kloosterman family has been constructed from the prime-q prefix | https://arxiv.org/abs/2511.07550 |
| Pascadi, arXiv:2505.00653v2 | `2025-06-29` | Prime Matrix weights become triply-well-factorable AP averages | row/column positivity is pointwise at P^2 scale, not an averaged distribution statement | https://arxiv.org/abs/2505.00653 |
| Wright, arXiv:2604.25177v1 | `2026-04-28` | terminal payload is upgraded to a trilinear Kloosterman-fraction convolution | current signed payload is one-dimensional and finite, with no equidistributed beta sequence | https://arxiv.org/abs/2604.25177 |

## 7. 最新开放口

```text
UniformAdjacentRunCancellationFamilyOrPDEC AND AtomLocalSurvivorPaymentOrPDEC AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 8. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json` | `e05dc6c48cd18aaa25cef5abe9aa5dc346d5b07db0827c8443dcefe536111615` |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-signed-payload-measure-absorption-frontier-router.json` | `dbed64083b897a4055f665ef636aa284b0c9cc3bf2e1201730c3d8396555543c` |
| `experiments/prime_matrix_phi_lpf_terminal_monotone_run_total_to_net_compression_frontier_router.py` | `3d92ba4b08e39f8b4d7de6b9067d0e0e9070e0c7a1ce8b1febf68b8e56a39dc7` |

行/列命题仍未无条件闭合。
