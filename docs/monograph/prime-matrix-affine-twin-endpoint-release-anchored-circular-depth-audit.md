# Prime Matrix AffineTwin endpoint-release anchored circular-depth audit

**状态：** `current_sweep_anchored_circular_depth_structured_global_open`

本审计继续下钻 circular-aperture：上一层只计算支撑窗口覆盖圆弧所需的单侧扩张；若唯一 actual packet 仍作为圆弧锚点保留，则 generator 与 shifted-fill 两个左端点必须同时到达圆弧起点，形成更强的双端点释放账本。

```text
actual_anchor_pair=19:8
minimal_circular_alignment_arc=[3029, 3586]
shifted_actual_anchor_representative=3586
actual_anchor_is_circular_arc_end=true
support_width=20
required_common_left_depth_to_cover_arc=557
current_generator_left_depth=18
current_fill_left_depth=28
generator_left_increment_required=539
fill_left_increment_required=529
anchored_endpoint_release_total_required=1068
one_sided_circular_support_extension=539
hidden_second_endpoint_release=529
endpoint_release_to_support_width_ratio=53.4
q_from_generator_depth_formula=1109
q_from_fill_depth_formula=560
q_candidate_gap=549
same_orientation_common_q_absent=true
same_orientation_anchored_depth_absorption_closed_current_sweep=true
```

## 1. anchored depth row

| anchor | arc start | arc end | required D | gen inc | fill inc | total release | q from gen | q from fill | q gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `19:8` | 3029 | 3586 | 557 | 539 | 529 | 1068 | 1109 | 560 | 549 |

## 2. 新显式矛盾点

圆周最小弧为 `[3029,3586]`，唯一 actual packet `19:8` 平移后正好位于右端点 `3586`。因此若反例链要保持这个 actual 锚点并吸收全部 formal pair，就必须把左深度从当前 pair support 的 `18` 推到 `557`。

单侧 circular-aperture 只看交支撑左扩，得到 `539`；但真实链要让 generator phase 与 shifted-fill phase 同时覆盖圆弧起点，所以还要支付 fill 左端点额外 `529`。总端点释放为 `1068`，是 support width `20` 的 `53.4` 倍。

同向 AffineTwin moving key 也不能吸收该锚定深度：lower-side 深度公式给出 `q=2D-5=1109` 与 `q=D+3=560`，两侧相差 `549`，且 fill 侧候选为偶数，不能成为同一个奇素数 AffineTwin key。

## 3. 结论边界

- 本步关闭当前 sweep 的 same-orientation anchored circular-depth absorption。
- 本步不关闭全局行/列命题；剩余是排斥 `AnchoredCircularDepth-PDEC`，或证明持久 actual-anchored 圆弧复现进入 `ColumnCRT/PDEC`、`SAE`、方向改变 key 或 moving-family multiplicity 出口。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-circular-aperture-ledger.json` | `724d4a76ddb964eab913e216f5ca717e92451124c7980af1fc37e4d97d447982` |
| `data/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json` | `69b806c23fb4f5515cbcf1cc184229db85a44b885469676905fcd83056be0bd5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
