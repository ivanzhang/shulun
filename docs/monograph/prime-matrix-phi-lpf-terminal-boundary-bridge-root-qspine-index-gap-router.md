# Prime Matrix Phi-LPF terminal boundary bridge-root q-spine index-gap 证书

**状态：** `bridge_root_qspine_index_gap_reduction_closed_uniform_index_order_law_open`
**核验日期：** `2026-05-25`

本证书把 moving endpoint barrier 顺序继续压成 q-spine 索引间隔。

```text
previous_moving_endpoint_barrier_reduction_closed=true
q_spine_nodes=[577, 607, 631]
q_spine_gap_vector=[30, 24]
q_spine_index_gap_row_count=2
endpoint_slack_equals_qspine_gap_sum_closed=true
finite_qspine_index_order_closed=true
qspine_index_gaps=[2, 0]
min_qspine_index_gap=0
zero_index_contact_count=1
bridge_root_qspine_index_gap_reduction_closed=true
bridge_root_uniform_qspine_index_order_law_proved=false
row_column_unconditional_closed=false
```

核心恒等式：

```text
endpoint_slack equals the q-spine adjacent-gap sum from bridge index to moving-barrier index
```

## 1. index-gap rows

| transition | bridge index | barrier index | index gap | q-gap sum | slack | bridge role | barrier role |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| m757 q571->577 | 0 | 2 | 2 | 54 | 54 | `left_bridge_root` | `right_terminal_node` |
| m761 q601->607 | 1 | 1 | 0 | 0 | 0 | `shared_pivot` | `shared_pivot` |

## 2. two-packet index shift summary

| field | value |
| --- | --- |
| `packet_count` | `2` |
| `two_packet_index_shift_closed` | `True` |
| `bridge_index_shift` | `1` |
| `barrier_index_shift` | `-1` |
| `index_gap_drop` | `2` |
| `index_gap_drop_equals_bridge_minus_barrier_index_shift` | `True` |
| `slack_drop` | `54` |
| `slack_drop_equals_first_full_spine_gap_sum` | `True` |
| `zero_contact_transition` | `m761 q601->607` |

## 3. 门控表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `MovingEndpointBarrierImported` | `true` | `true` | the moving endpoint barrier reduction is imported. | none for import |
| `SlackAsQSpineGapSum` | `true` | `true` | endpoint slack equals the adjacent q-spine gap sum. | finite q-spine gap ledger |
| `FiniteQSpineIndexOrder` | `true` | `true` | in the audited rows bridge index does not exceed barrier index. | finite index-order ledger |
| `UniformQSpineIndexBarrierOrderLaw` | `false` | `false` | a uniform law must force nonnegative q-spine index gap. | BridgeRootQSpineIndexBarrierOrderLawOrPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | this is a finite q-spine index-gap reduction, not a global parity-breaking theorem. | BridgeRootQSpineIndexBarrierOrderLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving |

## 4. 最新开放口

```text
BridgeRootQSpineIndexBarrierOrderLawOrPDEC AND RightSelectedTerminalTailOverhangPDEC AND BoundaryAdjacentRunMassRatioLawOrPDEC AND PrimitiveOrientationLocalFactorProductLawBeforePushforward AND SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily
```

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-moving-endpoint-barrier-router.json` | `ff0d6491895b8757792b01f81897775cd0fa6c2892a611f57d0121ef8e700aba` |
| `docs/monograph/prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-microtemplate-router.json` | `0b04b0f60f1c95e20bfbde8eb6ab7485a46e6d1f798b58b40e9cc3d09e6c2fa8` |
| `experiments/prime_matrix_phi_lpf_terminal_boundary_bridge_root_qspine_index_gap_router.py` | `9f8195c46b435762bcdac0f25663030a890994fa4cae64aff0fb412f03ba4a5f` |

行/列命题仍未无条件闭合。
