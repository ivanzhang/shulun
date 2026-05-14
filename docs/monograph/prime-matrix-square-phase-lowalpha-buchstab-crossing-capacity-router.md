# Prime Matrix square-phase low-alpha Buchstab crossing 容量路由

**状态：** `lowalpha_buchstab_crossing_unit_capacity_reduction_open`

low-alpha Buchstab 命中沿 `q` 加互补因子素因子前缀继续展开，每条路径唯一存在第一次跨过 `P` 的前缀 `D_-<=P<D_+`。固定精确 crossing 前缀 `D_+` 后，剩余 cofactor 区间长度小于一，所以局部多重容量已经消失；若仍有反例负载，只能来自 crossing 前缀集合的全局分布过密或 PDEC。

```text
crossing_prefix_exists_and_brackets_p=true
post_crossing_unit_capacity_checked=true
exact_crossing_key_collision_free=true
crossing_distribution_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 总体账本

| total hits | prime anchor | composite anchor | crossing failures | unit failures | key collisions |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 21504 | 9044 | 12460 | 0 | 0 | 0 |

## 2. 最坏 low-alpha 块

| P | block | hits | composite | max post-cross capacity | top key | max key multiplicity | depth counts | top crossing bucket |
| ---: | --- | ---: | ---: | ---: | --- | ---: | --- | --- |
| 200003 | `(31,62]` | 4540 | 3084 | 1 | `37:13567` | 1 | `{'1': 2005, '2': 2416, '3': 119}` | `C17:(131072P,262144P]` |

## 3. 每个 P 的总结

| P | low blocks | total hits | prime | composite | worst block | worst depth counts |
| ---: | ---: | ---: | ---: | ---: | --- | --- |
| 10007 | 2 | 412 | 200 | 212 | `(31,62]` | `{'1': 163, '2': 69}` |
| 36739 | 3 | 2040 | 915 | 1125 | `(31,62]` | `{'1': 437, '2': 394}` |
| 83561 | 4 | 5659 | 2551 | 3108 | `(31,62]` | `{'2': 965, '1': 923, '3': 4}` |
| 200003 | 4 | 13393 | 5378 | 8015 | `(31,62]` | `{'1': 2005, '2': 2416, '3': 119}` |

## 4. 证明边界

- 已闭合：每条 Buchstab 因子路径存在唯一 crossing edge `D_-<=P<D_+`。
- 已闭合：crossing 后的剩余整数区间容量至多一；精确 crossing key 无重复命中。
- 未闭合：`CrossingPrefixDistributionBoundOrPDEC`，即 crossing 前缀集合的全局分布上界或 PDEC 排斥。
- 并行保留：`PrimeAnchorRFPOrSelbergDistributionLedger`，处理 `m` 本身为素数的 prime-anchor 分支。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-anchor-decomposition.json` | `8075bf13712f96e2ff3d13a5f6cf317dbdd2362c2a1a19a40659d4b5521dc41f` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-first-anchor-interval-router.json` | `c137e604c7b0d9a24ec7a9c15d77aecf2753760fdc7554398202948aed341bc7` |
| `experiments/prime_matrix_square_phase_lowalpha_buchstab_crossing_capacity_router.py` | `7f8243beaeaa8c4255fbdbca73cefd13ae35f6223877f7c6a151952fbe874225` |
