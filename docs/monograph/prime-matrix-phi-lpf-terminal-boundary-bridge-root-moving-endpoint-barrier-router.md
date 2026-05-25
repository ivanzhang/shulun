# Prime Matrix Phi-LPF terminal boundary bridge-root moving endpoint barrier 证书

**状态：** `bridge_root_moving_endpoint_barrier_reduction_closed_uniform_order_law_open`
**核验日期：** `2026-05-25`

本证书把 endpoint slack 非负门继续压成 moving endpoint barrier 顺序。

```text
previous_endpoint_slack_reduction_closed=true
D_singleton_barrier_row_count=2
endpoint_slack_equals_barrier_distance_closed=true
all_barriers_lie_on_qspine=true
all_bridge_roots_lie_on_qspine=true
finite_bridge_root_barrier_order_closed=true
zero_barrier_contact_count=1
bridge_root_moving_endpoint_barrier_reduction_closed=true
bridge_root_uniform_barrier_order_law_proved=false
row_column_unconditional_closed=false
```

核心恒等式：

```text
D-singleton endpoint_slack = (P-g*r)-q_bridge, where q_bridge=q_next
```

q-spine nodes: `[577, 607, 631]`

## 1. barrier rows

| transition | r | bridge q | barrier q=P-gr | slack | barrier on spine | contact |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| m757 q571->577 | 18 | 577 | 631 | 54 | `true` | `false` |
| m761 q601->607 | 22 | 607 | 607 | 0 | `true` | `true` |

## 2. two-packet shift summary

| field | value |
| --- | --- |
| `packet_count` | `2` |
| `two_packet_shift_closed` | `True` |
| `m_gap` | `4` |
| `r_gap` | `4` |
| `common_D_gap_g` | `6` |
| `bridge_shift` | `30` |
| `barrier_shift` | `-24` |
| `barrier_slope_times_r_gap` | `-24` |
| `slack_drop` | `54` |
| `slack_drop_equals_bridge_shift_minus_barrier_shift` | `True` |
| `first_barrier` | `631` |
| `second_barrier` | `607` |
| `zero_contact_transition` | `m761 q601->607` |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `EndpointSlackImported` | `true` | `true` | the endpoint slack reduction is imported. | none for import |
| `SlackAsBarrierDistance` | `true` | `true` | D-singleton endpoint slack equals (P-g*r)-bridge_root_q. | finite barrier-distance identity |
| `BarrierNodesOnQSpine` | `true` | `true` | both bridge roots and both moving barriers are q-spine nodes. | finite q-spine barrier ledger |
| `FiniteBridgeRootBarrierOrder` | `true` | `true` | in the audited rows bridge_root_q <= moving_endpoint_barrier_q. | finite barrier order ledger |
| `UniformMovingEndpointBarrierOrderLaw` | `false` | `false` | a uniform law must force bridge roots not to pass the moving endpoint barrier. | BridgeRootMovingEndpointBarrierOrderLawOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite moving-barrier reduction, not a global parity-breaking theorem. | BridgeRootMovingEndpointBarrierOrderLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving |

## 4. 最新开放口

```text
BridgeRootMovingEndpointBarrierOrderLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-endpoint-slack-router.json` | `e9b3b5c48e6a1ca9b7142f5e98c1afb740b24bcf2dcdf8466d63c590ab8d8ef7` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json` | `0b04b0f60f1c95e20bfbde8eb6ab7485a46e6d1f798b58b40e9cc3d09e6c2fa8` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_moving_endpoint_barrier_router.py` | `ad042212291f8f5156c95620d9ae8a26b6f882eac25a949f383232bc02bd3b4f` |

行/列命题仍未无条件闭合。
