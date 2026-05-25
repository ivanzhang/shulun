# Prime Matrix Phi-LPF terminal boundary bridge-root q-spine Beatty margin 证书

**状态：** `bridge_root_qspine_beatty_margin_closed_uniform_source_law_open`
**核验日期：** `2026-05-25`

本证书把 bridge-root q-spine 源律继续压成 Beatty 整数分子 margin。

```text
previous_qspine_microtemplate_closed=true
micro_transition_count=4
packet_count=2
beatty_numerator_identity_closed=true
A_singleton_negative_pure_P_multiple_closed=true
D_singleton_positive_margin_closed=true
bridge_root_qspine_beatty_margin_closed=true
bridge_root_uniform_beatty_margin_source_law_proved=false
row_column_unconditional_closed=false
```

核心恒等式：

```text
phase_delta_num = lift_step*q*q_next + P*(s*q-a*g), m=P+r, a=floor(qr/P), s=floor((D+gr)/P)
```

## 1. micro transition rows

| role | transition | r | a | s | B=sq-ag | lift step | numerator | formula ok |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `A_singleton_pre_bridge` | m757 q569->571 g2 | 18 | 13 | 0 | -26 | 0 | -19214 | `true` |
| `D_singleton_bridge_old` | m757 q571->577 g6 | 18 | 13 | 1 | 493 | -1 | 34860 | `true` |
| `A_singleton_pre_bridge` | m761 q599->601 g2 | 22 | 17 | 0 | -34 | 0 | -25126 | `true` |
| `D_singleton_bridge_old` | m761 q601->607 g6 | 22 | 17 | 1 | 499 | -1 | 3954 | `true` |

## 2. packet margin rows

| packet | atom | r | A transition | A numerator | D transition | D positive margin | packet closed |
| ---: | --- | ---: | --- | ---: | --- | ---: | --- |
| 1 | `left:2842:selected_terminal:m757` | 18 | m757:q569->571 | -19214 | m757:q571->577 | 34860 | `true` |
| 2 | `left:2842:selected_terminal:m761` | 22 | m761:q599->601 | -25126 | m761:q601->607 | 3954 | `true` |

## 3. two-packet delta summary

| field | value |
| --- | --- |
| `packet_count` | `2` |
| `two_packet_delta_closed` | `True` |
| `r_gap` | `4` |
| `m_gap` | `4` |
| `A_beatty_a_gap` | `4` |
| `D_beatty_a_gap` | `4` |
| `A_B_gap` | `-8` |
| `D_B_gap` | `6` |
| `D_positive_margin_drop` | `30906` |
| `first_D_positive_margin` | `34860` |
| `second_D_positive_margin` | `3954` |

## 4. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `BridgeRootQSpineMicrotemplateImported` | `true` | `true` | the two bridge roots already form one selected-terminal q-spine. | none for import |
| `BeattyNumeratorIdentity` | `true` | `true` | each micro transition satisfies phase_delta_num = lift_step*q*q' + P*(s*q-a*g). | finite numerator factorization |
| `ASingletonPurePMultiple` | `true` | `true` | the A-singleton pre-bridge steps have lift_step=0, s=0, and negative P-multiple numerator. | finite A-side margin ledger |
| `DSingletonPositiveBeattyMargin` | `true` | `true` | the D-singleton bridge-old steps have lift_step=-1, s=1, and positive numerator margin. | finite D-side margin ledger |
| `BridgeRootUniformBeattyMarginSourceLaw` | `false` | `false` | a uniform law must force the same margin pattern outside the finite q=607 spine. | BridgeRootADSingletonBeattyMarginSourceLawOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite Beatty margin factorization, not a global parity-breaking theorem. | BridgeRootADSingletonBeattyMarginSourceLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving |

## 5. 最新开放口

```text
BridgeRootADSingletonBeattyMarginSourceLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-dominant-sign-word-repeated-step-packet-enclosure-terminal-phase-turn-word-audit.json` | `e05dc6c48cd18aaa25cef5abe9aa5dc346d5b07db0827c8443dcefe536111615` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json` | `0b04b0f60f1c95e20bfbde8eb6ab7485a46e6d1f798b58b40e9cc3d09e6c2fa8` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_beatty_margin_router.py` | `d1237564778bb18702194f04aeea0777e43e31fb9e0e118067c96d265f2b6ae9` |

行/列命题仍未无条件闭合。
