# Prime Matrix AffineTwin endpoint-release carrier-arrival projection-deficit audit

**状态：** `current_sweep_carrier_arrival_projection_deficit_closed_global_open`

本审计把 carrier-arrival 的形式侧乘积投影回真实共同支撑窗口，检查 `SuperSqrt` crossing 是否真是 actual overload。

```text
sqrt_floor=29
target_window_pair_count=20
minimal_crossing_formal_product_count=30
minimal_crossing_projection_hit_count=3
minimal_crossing_projection_deficit_count=27
minimal_crossing_actual_sqrt_slack=26
full_formal_product_count=64
full_projection_hit_count=6
full_projection_deficit_count=58
full_actual_sqrt_slack=23
carrier_arrival_projection_deficit_closed_current_sweep=true
```

## 1. minimal crossing projection rows

| targets | formal product | projection hits | deficit | actual sqrt slack | hits |
| --- | ---: | ---: | ---: | ---: | --- |
| `10:30,16:5` | 30 | 3 | 27 | 26 | `10:30,16:5,19:8` |
| `10:30,17:6` | 30 | 3 | 27 | 26 | `10:30,17:6,19:8` |
| `10:30,18:7` | 30 | 3 | 27 | 26 | `10:30,18:7,19:8` |
| `16:5,17:6` | 30 | 3 | 27 | 26 | `16:5,17:6,19:8` |
| `16:5,18:7` | 30 | 3 | 27 | 26 | `16:5,18:7,19:8` |
| `17:6,18:7` | 30 | 3 | 27 | 26 | `17:6,18:7,19:8` |

## 2. full packet projection

```text
formal_product_count=64
projection_hit_count=6
projection_deficit_count=58
actual_sqrt_slack=23
projection_hits=['10:30', '16:5', '17:6', '18:7', '19:8', '20:9']
```

## 3. 显式矛盾点

最小 crossing 的形式侧乘积是 `30`，只比 `sqrt_floor=29` 高一格；但投影到真实共同支撑窗口后只有 `3` 个 actual hits：实际锚点 `19:8` 加上两个被选 target atoms。因此 actual 侧仍有 `26` 个平方根余量。

完整 carrier packet 的形式侧乘积为 `64`，但真实窗口投影只有 `6` 个 hits，即实际锚点加五个 target atoms，投影缺口为 `58`。所以当前 `SuperSqrt` 不是 actual overload，而是形式侧乘积把大量不落窗的笛卡尔积误计为负载。

这把当前 PDEC 排斥继续压窄为：全局证明必须使用 actual projection count，而不是裸侧乘积；若未来某族真的让投影 hits 超过平方根门，则它已经是命名 `ProjectionCollision/SupportEscape-PDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-pressure-product-ledger.json` | `f7e3bf6df22c1d9022cd75d547f2297d474950d5d2ef3491abea242c048e9eeb` |
| `data/prime-matrix-affine-twin-window-edge-collision-ledger.json` | `344885dd9ed7914d65f259e2b63626a2837703893cbf23623e034b34c6cfe334` |
