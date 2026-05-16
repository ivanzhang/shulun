# Prime Matrix AffineTwin endpoint-release anchored parity no-go audit

**状态：** `current_sweep_anchored_parity_nogo_structured_global_open`

本审计把 anchored circular-depth 的 moving-key 失败从数值不等式升级为同向 lower-side 的奇偶/方程 no-go：共同深度 `D` 若要由同一个 AffineTwin key 吸收，必须同时满足 `q=2D-5` 与 `q=D+3`。

```text
actual_anchor_pair=19:8
minimal_circular_alignment_arc=[3029, 3586]
minimal_circular_alignment_arc_width=558
support_width=20
required_common_left_depth=557
required_depth_parity=odd
q_from_generator_depth_formula=1109
q_from_fill_depth_formula=560
q_from_fill_is_even=true
q_from_fill_is_prime=false
common_depth_solution=8
common_q_solution=11
required_depth_gap_from_common_solution=549
same_orientation_common_q_absent_by_equality=true
same_orientation_common_q_absent_by_parity=true
anchored_parity_nogo_closed_current_sweep=true
```

## 1. parity no-go row

| anchor | D | q_g=2D-5 | q_f=D+3 | common D | D gap | parity no-go |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `19:8` | 557 | 1109 | 560 | 8 | 549 | `true` |

## 2. 显式矛盾点

同向 lower-side AffineTwin 深度公式为：

```text
generator left depth D = (q+5)/2  =>  q_g=2D-5
fill left depth D = q-3          =>  q_f=D+3
```

若同一个 `q` 同时解释两侧，则 `2D-5=D+3`，唯一解为 `D=8`、`q=11`。但 actual-anchored 圆弧强制 `D=557`，距离唯一解相差 `549`。更强地，`D=557` 是奇数，所以 `q_f=D+3=560` 为大于 `2` 的偶数，不可能是奇素数 AffineTwin key。

## 3. 结论边界

- 本步关闭当前 sweep 的 same-orientation anchored parity absorption。
- 本步不关闭全局行/列命题；剩余是把这个 parity no-go 升格为全局族定理，或处理方向改变 key、ColumnCRT/PDEC、SAE、moving-family multiplicity 出口。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-ledger.json` | `d84ec936ad7080345ee101ddf038988928baa4b113686e9f7ef04a24ead4a89c` |
