# Prime Matrix AffineTwin endpoint-release cut-anchor sweep audit

**状态：** `current_sweep_cut_anchor_sweep_closed_global_open`

本审计把 anchored parity no-go 从单个最优圆弧扩展到全部圆周切口：对每个相邻 CRT 类之间的 cut，保留唯一 actual packet，把它平移进对应 lifted arc，并同时计算 left/right 共同深度和双端点释放量。

```text
cut_count=12
combined_crt_modulus=899
support_width=20
actual_anchor_pair=19:8
actual_anchor_position_histogram={'arc_end': 1, 'arc_interior': 10, 'arc_start': 1}
minimal_circular_arc_matches_previous_audit=true
min_arc_cut=19:8->13:9
min_arc_width=558
min_release_cut=19:8->13:9
min_total_endpoint_release_required=1068
min_release_to_support_width_ratio=53.4
max_total_endpoint_release_required=1737
left_common_depth_solution=8
right_common_depth_solution=1
min_positive_left_depth=58
min_left_gap_from_common_depth_solution=50
min_positive_right_depth=342
min_right_gap_from_common_depth_solution=341
all_endpoint_releases_exceed_support_width=true
all_actual_retained_cuts_same_orientation_closed=true
cut_anchor_sweep_closed_current_sweep=true
```

## 1. 全切口账本

| cut | open gap | arc width | actual pos | left D | right D | release | reasons |
| --- | ---: | ---: | --- | ---: | ---: | ---: | --- |
| `13:9->15:9` | 30 | 869 | `arc_interior` | 526 | 342 | 1683 | `left:D!=8,right:D!=1` |
| `15:9->19:9` | 61 | 838 | `arc_interior` | 464 | 373 | 1621 | `left:D!=8,right:D!=1` |
| `19:9->13:28` | 80 | 819 | `arc_interior` | 383 | 435 | 1583 | `left:D!=8+parity,right:D!=1` |
| `13:28->15:28` | 30 | 869 | `arc_interior` | 352 | 516 | 1683 | `left:D!=8,right:D!=1` |
| `15:28->19:28` | 61 | 838 | `arc_interior` | 290 | 547 | 1621 | `left:D!=8,right:D!=1` |
| `19:28->13:12` | 138 | 761 | `arc_interior` | 151 | 609 | 1467 | `left:D!=8+parity,right:D!=1` |
| `13:12->15:12` | 30 | 869 | `arc_interior` | 120 | 748 | 1683 | `left:D!=8,right:D!=1` |
| `15:12->13:8` | 26 | 873 | `arc_interior` | 93 | 779 | 1691 | `left:D!=8+parity,right:D!=1` |
| `13:8->15:8` | 30 | 869 | `arc_interior` | 62 | 806 | 1683 | `left:D!=8,right:D!=1` |
| `15:8->19:12` | 3 | 896 | `arc_interior` | 58 | 837 | 1737 | `left:D!=8,right:D!=1` |
| `19:12->19:8` | 57 | 842 | `arc_start` | 0 | 841 | 1675 | `right:D!=1` |
| `19:8->13:9` | 341 | 558 | `arc_end` | 557 | 0 | 1068 | `left:D!=8+parity` |

## 2. 容量与相位矛盾点

容量侧：所有 `12` 个切口的双端点释放量都超过 support width `20`。最小释放仍是 `1068`，发生在 cut `19:8->13:9`，为 support width 的 `53.4` 倍；最大释放为 `1737`。

相位侧：left lower-side 同向吸收仍只能在 `D=8,q=11` 处合一；本 sweep 的正 left depth 最小也为 `58`，距离共同解仍有 `50`。right above-side 同向吸收被 fill right depth 固定为 `D=1`；本 sweep 的正 right depth 最小为 `342`，距离固定解 `341`。

两个 endpoint cut 也没有逃逸：actual 位于右端的最优 cut 给出 left `D=557`，落入 anchored parity no-go；actual 位于左端的 cut 给出 right `D=841`，被 `D=1` fixed-fill 条件排斥。其余十个 interior cut 更强，因为它们同时要求左右两侧释放。

## 3. 结论边界

- 本步关闭当前 sweep 的 actual-retained same-orientation cut-anchor absorption。
- 本步仍不宣称全局行/列命题无条件闭合；剩余是把 cut-anchor no-go 升格为全局族定理，或处理方向改变 key、`ColumnCRT/PDEC`、`SAE`、moving-family multiplicity 出口。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-bidirectional-skew-hull-ledger.json` | `69b806c23fb4f5515cbcf1cc184229db85a44b885469676905fcd83056be0bd5` |
| `data/prime-matrix-affine-twin-endpoint-release-circular-aperture-ledger.json` | `724d4a76ddb964eab913e216f5ca717e92451124c7980af1fc37e4d97d447982` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
| `data/prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-ledger.json` | `cb28955dde483d9f9381c4f0239c924c6515c47069c111e037aa1b19b7449b87` |
