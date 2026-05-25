# Prime Matrix Phi-LPF terminal signed payload measure absorption frontier 证书

**状态：** `terminal_signed_payload_measure_schema_closed_strong_absorption_open`
**核验日期：** `2026-05-25`

本证书把 terminal/extra phase-turn 数据统一写成有限 signed payload measure
`mu(q,m,packet)`，并检查 selected terminal 余量能否吸收 extra 变差。

```text
terminal_signed_payload_measure_schema_closed=true
mu_transition_count=126
selected_net_excess_beats_extra_net_excess=true
selected_net_excess_beats_extra_total_variation=false
monotone_run_total_to_net_compression_proved=false
extra_total_variation_absorption_proved=false
admissible_averaged_trace_family_created=false
trace_or_kloosterman_completion_ready=false
selected_terminal_fixed_numerator_kloosterman_ready=false
row_column_unconditional_closed=false
phi_lpf_parity_barrier_globally_broken=false
```

## 1. 吸收余量

```text
selected_negative_excess=1.456565972578 (114539441491/78636631397)
extra_negative_excess=0.907719323182 (71379989829/78636631397)
extra_total_variation=14.109301881162 (27768758142307772418840319934041830802744822617132968593977647725/1968117088725958506051611620121066252424277248250429833368124847)
net_excess_absorption_margin=0.548846649396 (43159451662/78636631397)
strong_total_variation_absorption_margin=-12.652735908584 (-24902065760820990456035480299500630131988359582829950635383120884/1968117088725958506051611620121066252424277248250429833368124847)
selected_excess_to_extra_total_ratio=0.103234446668 (2866692381486781962804839634541200670756463034303017958594526841/27768758142307772418840319934041830802744822617132968593977647725)
selected_excess_to_extra_negative_excess_ratio=1.604643566991 (114539441491/71379989829)
```

结论：净超额吸收有正余量，但强总变差吸收仍为负余量。

## 2. atom readiness

| packet | role | P | m | q_count | transitions | runs | max_run | A_full_distinct | fixed_Kloosterman | numerator | net | total variation |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| left:2842 | extra_shell | 739 | 719 | 28 | 27 | 10 | 6 | `true` | `false` | `full_distinct_moving_beatty_numerator` | -0.356428699921 (-136715/383569) | 7.314378851086 (39859189791196246306766250492791/5449429213702464359611920385417) |
| left:2842 | extra_shell | 739 | 751 | 28 | 27 | 9 | 8 | `false` | `false` | `moving_beatty_numerator_with_collision` | -0.462466987687 (-177388/383569) | 4.365197374565 (31312318976264902113512764636/7173173693981533055309193841) |
| left:2842 | selected_terminal | 739 | 757 | 28 | 27 | 11 | 6 | `true` | `false` | `full_distinct_moving_beatty_numerator` | -0.038532832424 (-14780/383569) | 7.038610620634 (21839887946724610150799587828243196/3102869177433817344181826728189459) |
| left:2842 | selected_terminal | 739 | 761 | 28 | 27 | 14 | 5 | `true` | `false` | `full_distinct_moving_beatty_numerator` | 0.032752907560 (12563/383569) | 7.947916421105 (5258912969911360856935706921220147347487585/661671901323293918620039995916972500426847) |
| right:1887 | extra_shell | 607 | 479 | 7 | 6 | 5 | 2 | `true` | `false` | `full_distinct_moving_beatty_numerator` | -0.088823635574 (-18210/205013) | 2.429725655511 (20874007392026392/8591096424685507) |
| right:1887 | selected_terminal | 607 | 769 | 7 | 6 | 5 | 2 | `true` | `false` | `full_distinct_moving_beatty_numerator` | -0.601039934053 (-123221/205013) | 1.461472402260 (12555650329833729/8591096424685507) |
| right:1887 | selected_terminal | 607 | 773 | 7 | 6 | 5 | 2 | `true` | `false` | `full_distinct_moving_beatty_numerator` | -0.849746113661 (-174209/205013) | 1.531169687897 (13154426431279521/8591096424685507) |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `TerminalVariationBudgetImported` | `true` | `true` | terminal phase variation budget 已给出 selected 与 extra 的精确正/负变差。 | `finite variation ledger imported` |
| `MuPayloadMeasureSchemaClosed` | `true` | `true` | 七个 terminal/extra fixed-m line atoms 已统一写成 mu(q,m,packet) transition measure。 | `closed finite signed payload measure schema` |
| `SelectedNetExcessBeatsExtraNetExcess` | `true` | `true` | selected terminal 负净超额大于 extra 负净超额；这是净账本层面的真实余量。 | `net-level margin only` |
| `SelectedNetExcessBeatsExtraTotalVariation` | `false` | `false` | selected 负净超额远小于 extra 总变差，不能直接支付强吸收。 | `ExtraTotalVariationAbsorptionOrLocalSurvivor` |
| `SelectedFixedNumeratorKloostermanReady` | `false` | `false` | selected terminal atoms 全是 moving Beatty numerator；直接 fixed-numerator Kloosterman 输入不可用。 | `SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving` |
| `ParityShadowShortcutRejected` | `true` | `true` | factor-word parity shadow 不能替代本层所需 signed payload 或 orientation law。 | `PrimitiveOrientationLocalFactorProductLawBeforePushforward OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows` |
| `TraceKloostermanFamilyReady` | `false` | `false` | mu 目前是有限 transition measure，还没有外部 trace/Kloosterman/Type-II 可求和族。 | `AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |
| `MonotoneRunTotalToNetCompressionProved` | `false` | `false` | 要把 strong absorption 失败变成可用相消，必须证明 run 级 total-to-net 压缩或命名回流。 | `MonotoneRunTotalToNetCompressionOrPDEC` |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只关闭 payload measure schema 与吸收余量账本，没有闭合三命题。 | `MonotoneRunTotalToNetCompressionOrPDEC AND ExtraTotalVariationAbsorptionOrLocalSurvivor AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily` |

## 4. 外部前沿适配

| input | usable after | current gap |
| --- | --- | --- |
| FKMS trace/bilinear and DI/BFI/Kuznetsov dispersion | mu is promoted from a finite transition measure to an averaged trace family | only two P packets and seven fixed-m atoms are present |
| Milicevic-Qin-Wu arbitrary-modulus Kloosterman and Wright unbalanced fractions | moving Beatty numerator A(q)/q is completed into a summable reciprocal family | selected atoms are moving-numerator, not fixed-numerator Kloosterman sums |
| Pascadi composite Type-II | terminal line atoms are enlarged to a genuine two-dimensional Type-II rectangle | current object is a one-dimensional prime-q prefix transition measure |

## 5. 最新开放口

```text
MonotoneRunTotalToNetCompressionOrPDEC AND ExtraTotalVariationAbsorptionOrLocalSurvivor AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

保留基底：

```text
PrimeQSupportSetReciprocalPhaseSavingBeyondParity AND (PrimitiveOrientationLocalFactorProductLawBeforePushforward OR BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows) AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_phi_lpf_terminal_signed_payload_measure_absorption_frontier_router.py` | `b81cd996a8d9157dc27095ea7547f95944b5a77288413d55b2339e29bc8a3c1b` |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-variation-budget-audit.json` | `284aadf7447ca0c0c9bc5d8af87a9ba3ff62826b35185de2b495d5175d7087eb` |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json` | `e05dc6c48cd18aaa25cef5abe9aa5dc346d5b07db0827c8443dcefe536111615` |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-normal-form-audit.json` | `45e13789a89eca78b31950a4fa13b50e4712160e2ff835fb8a33be28c8fff931` |
| `docs/monograph/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-router.json` | `ab900d720941352fc10d61aed2361314cd534bde8857294368ead900015784ef` |

行/列命题仍未无条件闭合。
