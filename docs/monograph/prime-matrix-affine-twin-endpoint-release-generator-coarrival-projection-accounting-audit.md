# Prime Matrix AffineTwin endpoint-release generator-coarrival projection-accounting audit

**状态：** `current_sweep_generator_coarrival_projection_accounting_closed_global_open`

本审计继续压缩 `GeneratorCoarrivalBound`：当 realized `q=31` 的 fill arrival 被迫携带 generator 共到达时，形式侧乘积可以越过平方根门，但投影到 actual 支撑图像仍远低于平方根门。

```text
realized_q_values=[31]
source_blocked_q_values=[43, 103]
sqrt_floor=29
actual_anchor_pair=19:8
base_formal_product_count=12
base_projection_hit_count=1
fill_arrival_subset_count=30
fill_only_subset_count=0
formal_super_sqrt_subset_count=22
actual_overload_subset_count=0
minimal_coarrival_formal_product_count=30
minimal_coarrival_projection_hit_count=3
minimal_coarrival_actual_sqrt_slack=26
full_formal_product_count=64
full_projection_hit_count=6
full_actual_sqrt_slack=23
generator_coarrival_projection_accounting_closed_current_sweep=true
```

## 1. 共到达原子

| pair | target p | g residue | f residue | new g | new f | carrier events |
| --- | ---: | ---: | ---: | --- | --- | ---: |
| `10:30` | 2678 | 10 | 30 | true | true | 9 |
| `16:5` | 2684 | 16 | 5 | true | true | 5 |
| `17:6` | 2685 | 17 | 6 | true | true | 7 |
| `18:7` | 2686 | 18 | 7 | true | true | 2 |
| `20:9` | 2688 | 20 | 9 | true | false | 4 |

## 2. 最小 crossing 的 actual 投影

| targets | new g | new f | formal product | actual hits | deficit | sqrt slack | hits |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `10:30,16:5` | 2 | 2 | 30 | 3 | 27 | 26 | `10:30,16:5,19:8` |
| `10:30,17:6` | 2 | 2 | 30 | 3 | 27 | 26 | `10:30,17:6,19:8` |
| `10:30,18:7` | 2 | 2 | 30 | 3 | 27 | 26 | `10:30,18:7,19:8` |
| `16:5,17:6` | 2 | 2 | 30 | 3 | 27 | 26 | `16:5,17:6,19:8` |
| `16:5,18:7` | 2 | 2 | 30 | 3 | 27 | 26 | `16:5,18:7,19:8` |
| `17:6,18:7` | 2 | 2 | 30 | 3 | 27 | 26 | `17:6,18:7,19:8` |

## 3. 显式矛盾读数

- `fill_arrival_subset_count=30` 中没有 fill-only 子集；每个 fill arrival 都伴随 generator coarrival。
- 形式上越过平方根门的 `22` 个子集，actual overload 数为 `0`。
- 最小 crossing 的形式乘积为 `30`，但 actual hits 只有 `3`，投影缺口 `27`。
- 全部 carrier packet 形式乘积为 `64`，actual hits 只有 `6`，仍有 sqrt slack `23`。

## 4. 结论边界

当前 sweep 中 generator coarrival 不能把 fill-arrival 分支变成 actual overload；它只把形式账本推高，然后被 support graph projection 收紧。

这仍不是全局无条件证明。最新剩余是把该投影账本升格为族级 `GeneratorCoarrivalFamilyBound`，或把失败形态登记为 `ProductAccountingTighteningGlobal`、`SourceRematerialization-PDEC/SAE`、`ColumnCRT/PDEC` 与 moving-family persistence 出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-ledger.json` | `1e08c9fd3d4c27ec13e43200c3fa5745664ff6036cf6ffae69cd361830079efb` |
| `data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-ledger.json` | `f7e3bf6df22c1d9022cd75d547f2297d474950d5d2ef3491abea242c048e9eeb` |
| `data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json` | `209cc18174894b44e5eb153e0601602460f730a98e83e968e7e7d6dbf7ebe3b5` |
| `data/prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json` | `51c3143a936264617d47fff2643948dc806b44fabe3bcbf8380508634fd3b966` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
| `data/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json` | `29dbb00110b05ea2a63df6fece2f60c4bcfe8844268529e4b06730d5dc0da2d6` |
