# Prime Matrix square-phase low-alpha z=61 positive lift projection gate bridge

**状态：** `z61_positive_lift_factor_gates_reduced_to_root_projection_gate_open`

MissingLift 的素因子提升门可继续降为一级 CRT 根支撑上的小模投影筛：q4=37 投影根为 `15,16`，q2=71 移位投影根为 `42,50`，但在当前 32 个一级根支撑中，两门与合并门都只命中 `r=26951`。因此剩余从提升容量界进一步压成根支撑投影容量界，或 MissingLift-PDEC。

```text
single_span_locked=true
q4_projection_gate_unique=true
q2_projection_gate_unique=true
combined_projection_gate_unique=true
positive_lift_projection_gate_bridge_closed_for_sample=true
row_column_unconditional_closed=false
```

## 1. Affine selector

| M | delta | selected r | h values | q4 pass | q2 pass | combined pass |
| ---: | ---: | ---: | --- | --- | --- | --- |
| 57684 | 527 | 26951 | `[3]` | `[26951]` | `[26951]` | `[26951]` |

## 2. Projection gate

| gate | root solutions | pass roots | unrealized | unique |
| --- | --- | --- | --- | --- |
| q4=37 | `[15, 16]` | `[26951]` | `[16]` | true |
| q2=71 | `[42, 50]` | `[26951]` | `[50]` | true |

## 3. Combined projection

| combined classes | pass roots | unique |
| --- | --- | --- |
| `[681, 1754, 1533, 2606]` | `[26951]` | true |

## 4. 证明边界

- 已闭合：当前 MissingLift factor gate 与 root projection gate 严格同一对象。
- 未闭合：全局根支撑投影容量界，或 MissingLift-PDEC 排斥。
- 下一目标：`RootProjectionGateGlobalBoundOrMissingLiftPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-affine-lift-selector-router.json` | `2ac894c685b6e8b035c7d02751db47f25ba5cfe238cd4bec7fc7efef5f9cb7dd` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-factor-gate-bridge-router.json` | `72589dcf151e37a2602f41b121da0f9576841e343d6fb4faf257b7d7274512b1` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-root-projection-gate-router.json` | `4ec06861847a756a7e7b58fdd536bf6518b4c6ca26c0ab19a7378f32befe17a3` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_projection_gate_bridge_router.py` | `fefac9051b17c40d9f1b09fe5474a196ad64950283e937a898633a6ddf882430` |
