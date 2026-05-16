# Prime Matrix AffineTwin moving-key depth formula audit

**状态：** `current_sweep_same_orientation_moving_key_depth_formula_closed_global_open`

本审计继续下钻 `MovingPrimitiveKey`：即使允许 `q` 移动，只要保持同一 AffineTwin 深度公式和同侧吸收，support-motion 所需共同深度也不能由 generator/fill 两侧给出同一个 `q`。

```text
moving_key_depth_formula_candidate_count=11
support_motion_side_histogram={'above': 3, 'below': 8}
min_lower_q_candidate_gap=50
max_lower_q_candidate_gap=375
min_above_fill_right_depth_residual=341
max_above_fill_right_depth_residual=434
same_orientation_moving_key_depth_absorption_closed_current_sweep=true
```

## 1. moving-q formula 表

| pair | side | depth D | q from g | q from f | q gap | right residual | obstruction |
| --- | --- | ---: | ---: | --- | --- | --- | --- |
| `13:8` | `below` | 93 | 181 | 96 | 85 | - | `lower_depth_q_mismatch` |
| `13:9` | `above` | 342 | 1375 | - | - | 341 | `fill_right_depth_fixed_one` |
| `13:12` | `below` | 151 | 297 | 154 | 143 | - | `lower_depth_q_mismatch` |
| `13:28` | `below` | 383 | 761 | 386 | 375 | - | `lower_depth_q_mismatch` |
| `15:8` | `below` | 62 | 119 | 65 | 54 | - | `lower_depth_q_mismatch` |
| `15:9` | `above` | 373 | 1499 | - | - | 372 | `fill_right_depth_fixed_one` |
| `15:12` | `below` | 120 | 235 | 123 | 112 | - | `lower_depth_q_mismatch` |
| `15:28` | `below` | 352 | 699 | 355 | 344 | - | `lower_depth_q_mismatch` |
| `19:9` | `above` | 435 | 1747 | - | - | 434 | `fill_right_depth_fixed_one` |
| `19:12` | `below` | 58 | 111 | 61 | 50 | - | `lower_depth_q_mismatch` |
| `19:28` | `below` | 290 | 575 | 293 | 282 | - | `lower_depth_q_mismatch` |

## 2. 当前读数

- lower-side 同侧吸收要求 `(q+5)/2=D` 且 `q-3=D`，即 `q=2D-5` 与 `q=D+3` 必须相等；这只在 `D=8` 时可能。
- above-side 同侧吸收要求 `(q-7)/4=D` 且 `1=D`，而当前 above depths 远大于 `1`。
- 当前最窄公式阻塞 atom 是 `19:12`，side `below`，`D=58`，阻塞类型 `lower_depth_q_mismatch`。
- 因此当前支撑运动不能由同向 AffineTwin moving key 的深度公式吸收。

## 3. 结论边界

- 本步关闭当前 sweep 的 same-orientation moving-key depth absorption。
- 本步不证明所有 moving primitive key 全局不复现；剩余是方向改变、source 重物化或 key 迁移的非持久性证明，或路由到 `OrientationChangingPrimitiveKey-PDEC/SAE`、`SourceRematerialization-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json` | `7c63e2c3bd443a430ef7f633d1359f88c65ead388b69f34a0e0f9d72ccb32ef4` |
| `data/prime-matrix-affine-twin-support-motion-depth-ledger.json` | `0e2786c4a32ee35a38c027a4cadfe59cda82e09b51939d935fb476762c9700c7` |
