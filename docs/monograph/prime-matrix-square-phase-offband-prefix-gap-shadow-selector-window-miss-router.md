# Prime Matrix square-phase off-band prefix gap shadow selector window miss router

**状态：** `selector_window_miss_endpoint_margin_open`

本步把 49 个 Q=15 窗口错位词全部正规化为端点距离原子：先把覆盖词进程与 actual P mod 15 合并成一个 CRT 命中进程，再检查该命中进程到 fixed phase 窗口的最近点。当前前沿没有命中点落入窗口，最近距离最小为 53，最小距离/窗口宽度比为 1.656250。因此剩余不再是素数供给问题，而是端点距离不等式的全局提升，或失败时的 persistent overlap PDEC。

```text
record_count=11
window_miss_atom_count=49
left_miss_count=21
right_miss_count=28
q15_hit_inside_window_count=0
min_nearest_hit_distance=53
min_distance_to_width_ratio=1.656250
row_column_unconditional_closed=false
```

## 1. 端点距离正规形

对每个窗口错位覆盖词，合并 `word CRT` 与 `P mod 15` 得到唯一命中进程。若该进程在 fixed phase 窗口内无点，则当前错位由最近命中点在左侧或右侧的端点距离解释。

## 2. 前沿记录

| idx | P | side | atoms | left | right | inside hits | min distance | min ratio |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 733 | `plus` | 3 | 1 | 2 | 0 | 1121 | 140.125000 |
| 1 | 523 | `plus` | 1 | 0 | 1 | 0 | 4312 | 44.916667 |
| 2 | 691 | `minus` | 11 | 6 | 5 | 0 | 298 | 2.547009 |
| 3 | 683 | `plus` | 1 | 0 | 1 | 0 | 7219 | 41.970930 |
| 4 | 733 | `plus` | 2 | 1 | 1 | 0 | 14514 | 145.140000 |
| 5 | 673 | `minus` | 2 | 0 | 2 | 0 | 523 | 18.678571 |
| 6 | 733 | `plus` | 3 | 1 | 2 | 0 | 1121 | 140.125000 |
| 7 | 313 | `plus` | 4 | 0 | 4 | 0 | 53 | 1.656250 |
| 8 | 1129 | `plus` | 9 | 6 | 3 | 0 | 215 | 2.986111 |
| 9 | 691 | `minus` | 11 | 6 | 5 | 0 | 298 | 2.547009 |
| 10 | 673 | `minus` | 2 | 0 | 2 | 0 | 523 | 18.678571 |

## 3. 最紧原子

| P | side | labels | hit side | hit distance | width | ratio | window values |
| ---: | --- | --- | --- | ---: | ---: | ---: | --- |
| 313 | `plus` | `[7, 11]` | `right` | 53 | 32 | 1.656250 | `[296]` |
| 313 | `plus` | `[11, 13]` | `right` | 128 | 32 | 4.000000 | `[305]` |
| 1129 | `plus` | `[3, 11, 7, 3]` | `left` | 215 | 72 | 2.986111 | `[1105]` |
| 1129 | `plus` | `[3, 13, 7, 3]` | `right` | 239 | 72 | 3.319444 | `[1126]` |
| 313 | `plus` | `[11, 7]` | `right` | 293 | 32 | 9.156250 | `[305]` |
| 691 | `minus` | `[7, 3, 19]` | `left` | 298 | 117 | 2.547009 | `[745]` |
| 691 | `minus` | `[7, 3, 19]` | `left` | 298 | 117 | 2.547009 | `[745]` |
| 1129 | `plus` | `[3, 19, 7, 3]` | `right` | 344 | 72 | 4.777778 | `[1105]` |
| 691 | `minus` | `[7, 3, 11]` | `right` | 426 | 117 | 3.641026 | `[724]` |
| 691 | `minus` | `[7, 3, 11]` | `right` | 426 | 117 | 3.641026 | `[724]` |
| 1129 | `plus` | `[3, 7, 11, 3]` | `left` | 455 | 72 | 6.319444 | `[1096]` |
| 673 | `minus` | `[7, 3, 13]` | `right` | 523 | 28 | 18.678571 | `[652]` |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `finite_window_miss_endpoint_margin` | `closed_on_current_frontier` | Every non-structural Q=15 hit progression has its nearest actual-residue hit outside the fixed phase window. |
| `window_miss_is_endpoint_inequality` | `closed` | The remaining Q=15 lift is an endpoint distance inequality for a combined CRT progression, not a new primality assertion. |
| `global_endpoint_margin_inequality` | `open` | A global proof must show the combined Q=15 hit progression always misses the formal-unit phase window. |
| `persistent_overlap_pdec` | `open` | If the endpoint inequality fails, the overlap becomes an explicit PDEC/ColumnCRT input. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteEndpointMarginPositive` | `true` | `true` | 当前窗口错位原子的 Q=15 命中进程全部错开 phase 窗口。 | closed on current finite frontier |
| `EndpointInequalityNormalFormClosed` | `true` | `true` | 窗口错位已正规化为 nearest-hit 距离不等式。 | closed |
| `GlobalEndpointMarginProved` | `false` | `false` | 尚未证明任意 formal unit 中该距离恒正。 | LowWheel15WindowMissEndpointInequalityOrPersistentOverlapPDEC |
| `PersistentOverlapPDECExcluded` | `false` | `false` | 若距离不等式失败，则需要 PDEC/ColumnCRT 排斥重叠族。 | LowWheel15WindowMissEndpointInequalityOrPersistentOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只把剩余转成端点距离守门项，不关闭全局行/列命题。 | LowWheel15WindowMissEndpointInequalityOrPersistentOverlapPDEC |

## 6. 下一步

- 主攻：`LowWheel15WindowMissEndpointInequalityOrPersistentOverlapPDEC`。
- 直接证明目标：把 nearest-hit 距离写成 fixed band/k 参数的不等式，证明它在 formal-unit 族中恒为正。
- 若距离可以为零或负，则对应重叠直接进入 persistent overlap `PDEC/ColumnCRT`。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_window_miss_router.py` | `a8ef692843613d2a3b840606f8bb3f3959da6e822d4c8dac2aac95a1837abe78` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_lowwheel_lift_router.py` | `2b16c31c7a682a0a0122634256522cbc6802789d54ae2ef1c50ced26b94db72c` |
| `data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json` | `366bda520b7fbd1a8ad5e8a602af1ffb19daf9b447569fd5110a6f1f4bac8609` |
| `data/square-phase-offband-prefix-gap-shadow-selector-lowwheel-lift-ledger.json` | `494a9f0e6d8d0bb31b97efee740e1e206ee45b789d86f1c92a2c33f076b119a7` |
| `data/square-phase-offband-prefix-gap-shadow-selector-window-miss-ledger.json` | `ae5a517480d202fd4c2e1480ab47dca31ba3b2fe9252599fa46db2009c443cfe` |
