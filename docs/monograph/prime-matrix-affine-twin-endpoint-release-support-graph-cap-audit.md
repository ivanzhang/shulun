# Prime Matrix AffineTwin endpoint-release support-graph cap audit

**状态：** `current_sweep_support_graph_cap_closed_global_moving_open`

本审计把共同支撑窗口识别为单值 residue 图像，说明 actual projection 由图像容量控制，而不是由两侧残基笛卡尔积控制。

```text
q=31
support_width=20
sqrt_floor=29
target_window_pair_count=20
generator_functional_graph=true
fill_functional_graph=true
affine_offsets_mod_fill=[20]
support_graph_cap=20
support_graph_cap_slack_to_sqrt_floor=9
modulus_product_minus_support_width_square=499
q_ge_13_symbolic_margin=1996
support_graph_cap_closed_current_sweep=true
```

## 1. support graph rows

| target p | generator residue | fill residue | pair |
| ---: | ---: | ---: | --- |
| 2669 | 1 | 21 | `1:21` |
| 2670 | 2 | 22 | `2:22` |
| 2671 | 3 | 23 | `3:23` |
| 2672 | 4 | 24 | `4:24` |
| 2673 | 5 | 25 | `5:25` |
| 2674 | 6 | 26 | `6:26` |
| 2675 | 7 | 27 | `7:27` |
| 2676 | 8 | 28 | `8:28` |
| 2677 | 9 | 29 | `9:29` |
| 2678 | 10 | 30 | `10:30` |
| 2679 | 11 | 0 | `11:0` |
| 2680 | 12 | 1 | `12:1` |
| 2681 | 13 | 2 | `13:2` |
| 2682 | 14 | 3 | `14:3` |
| 2683 | 15 | 4 | `15:4` |
| 2684 | 16 | 5 | `16:5` |
| 2685 | 17 | 6 | `17:6` |
| 2686 | 18 | 7 | `18:7` |
| 2687 | 19 | 8 | `19:8` |
| 2688 | 20 | 9 | `20:9` |

## 2. projection cap rows

| targets | projection hits | graph slack | sqrt slack | hits |
| --- | ---: | ---: | ---: | --- |
| `10:30,16:5` | 3 | 17 | 26 | `10:30,16:5,19:8` |
| `10:30,17:6` | 3 | 17 | 26 | `10:30,17:6,19:8` |
| `10:30,18:7` | 3 | 17 | 26 | `10:30,18:7,19:8` |
| `16:5,17:6` | 3 | 17 | 26 | `16:5,17:6,19:8` |
| `16:5,18:7` | 3 | 17 | 26 | `16:5,18:7,19:8` |
| `17:6,18:7` | 3 | 17 | 26 | `17:6,18:7,19:8` |

## 3. 显式矛盾点

共同支撑窗口的 20 个 target pairs 是一条双向函数图像：每个 generator residue 只对应一个 fill residue，反向也单值。因此 actual projection hits 至多是图像大小 `20`，不是形式侧乘积 `A_g*A_f`。

当前 `sqrt_floor=floor(sqrt(29*31))=29`，所以固定 AffineTwin 支撑图像本身还有 `9` 个平方根余量。最小 crossing 的 actual hits 为 `3`，完整 carrier packet 的 actual hits 为 `6`，都远低于图像上界和平方根门。

一般 AffineTwin 固定槽满足 `W=(q+9)/2`；对 `q>=13`，`W^2<=q(q-2)` 等价于 `3q^2-26q-81>=0`。当前 `q=31` 的 margin 为正。因此若没有 moving-slot support escape，ProductAccounting 已收紧到 actual graph projection。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json` | `209cc18174894b44e5eb153e0601602460f730a98e83e968e7e7d6dbf7ebe3b5` |
| `data/prime-matrix-affine-twin-window-edge-collision-ledger.json` | `344885dd9ed7914d65f259e2b63626a2837703893cbf23623e034b34c6cfe334` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
