# Prime Matrix AffineTwin endpoint-release carrier-arrival pressure-product audit

**状态：** `current_sweep_carrier_arrival_pressure_product_routed_global_open`

本审计检查 carrier-arrival packet 若被物化，是否仍只是普通新残基到达，还是已经越过 `sqrt((q-2)q)` 压力乘积门。

```text
generator_modulus=29
fill_modulus=31
modulus_product=899
sqrt_floor=29
base_counts=(3, 4)
base_side_product=12
carrier_required_new_generator_residues=[10, 16, 17, 18, 20]
carrier_required_new_fill_residues=[5, 6, 7, 30]
full_counts_after_carrier_arrival=(8, 8)
full_side_product_after_carrier_arrival=64
full_square_excess_over_modulus_product=3197
minimal_crossing_target_atom_count=2
minimal_crossing_side_product=30
minimal_crossing_square_excess_over_modulus_product=1
carrier_arrival_pressure_product_routed_current_sweep=true
```

## 1. target atoms

| target | p | new generator | new fill | new side | arrival count | carrier events |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `10:30` | 2678 | 10 | 30 | 2 | 3 | 9 |
| `16:5` | 2684 | 16 | 5 | 2 | 2 | 5 |
| `17:6` | 2685 | 17 | 6 | 2 | 2 | 7 |
| `18:7` | 2686 | 18 | 7 | 2 | 1 | 2 |
| `20:9` | 2688 | 20 | - | 1 | 1 | 4 |

## 2. minimal crossing atoms

| targets | side counts | product | square excess | carrier events |
| --- | --- | ---: | ---: | ---: |
| `10:30,16:5` | `(5,6)` | 30 | 1 | 14 |
| `10:30,17:6` | `(5,6)` | 30 | 1 | 16 |
| `10:30,18:7` | `(5,6)` | 30 | 1 | 11 |
| `16:5,17:6` | `(5,6)` | 30 | 1 | 12 |
| `16:5,18:7` | `(5,6)` | 30 | 1 | 7 |
| `17:6,18:7` | `(5,6)` | 30 | 1 | 9 |

## 3. 显式矛盾点

当前基础侧残基数为 `(3,4)`，乘积 `12`，安全低于 `sqrt(29*31)`。若物化 carrier-arrival 使用到的全部新残基，侧残基数变成 `(8,8)`，乘积 `64`，满足 `64^2-29*31=3197>0`。

更窄的是，任意两个双侧 target atoms 已把侧残基数推到 `(5,6)`，乘积 `30`，并且 `30^2-29*31=1`。也就是说，最小 crossing 只超过平方根门一个单位，是当前局部反例链与真实链之间的精确压力断点。

因此 carrier-arrival packet 不能继续作为普通 arrival 义务保留：若这些 target 原子被真实物化，立即进入 `SuperSqrt/PressureProduct-PDEC`；若 PDEC 被排斥，则当前 carrier-arrival packet 不能复现。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-routing-ledger.json` | `56b25e4803fe188a597db807650eba7c16a912589afedd0867c4e0749964b3a5` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-slot-phase-lock-ledger.json` | `a8048685a2c6449b42ed5d2190aa47e75b20abf36a18e18c4d1ddb223cba033f` |
