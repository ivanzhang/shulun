# Prime Matrix square-phase off-band prefix gap shadow selector modulus barrier router

**状态：** `selector_one_step_modulus_barrier_open_global`

本步把 Q=15 窗口错位的端点距离不等式进一步压缩为一跳模数屏障。当前 49 个错位原子全部满足：覆盖词进程在 phase 窗口内只有一个代表、该代表不是 actual P 的 mod 15 残基，且 word_modulus M 大于 phase_width W。于是沿同一覆盖词进程要到达 actual 残基至少平移一个 M，而一个 M 已超过整个窗口宽度，故命中点必在窗口外。当前最小 M-W 为 45，最小 M/W 为 1.974359。全局剩余变成证明 formal-unit 族中非结构冲突覆盖词均满足 M>W，或把 M<=W 的重叠族送入 PDEC。

```text
record_count=11
barrier_atom_count=49
one_step_barrier_closed_count=49
one_step_barrier_failure_count=0
min_modulus_minus_width=45
min_modulus_to_width_ratio=1.974359
row_column_unconditional_closed=false
```

## 1. 一跳屏障

若覆盖词进程在 phase 窗口内只有一个代表 `v`，且 `v mod 15` 不是 actual `P mod 15`，则下一个 actual 残基命中必须沿同一进程平移非零个 `M`。当 `M>W` 时，任意一跳已超过整个窗口宽度，因此 actual 残基命中不可能仍在窗口内。

## 2. 前沿记录

| idx | P | side | atoms | closed | failures | min M-W | min M/W |
| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 733 | `plus` | 3 | 3 | 0 | 553 | 70.125000 |
| 1 | 523 | `plus` | 1 | 1 | 0 | 4293 | 45.718750 |
| 2 | 691 | `minus` | 11 | 11 | 0 | 114 | 1.974359 |
| 3 | 683 | `plus` | 1 | 1 | 0 | 7121 | 42.401163 |
| 4 | 733 | `plus` | 2 | 2 | 0 | 7193 | 72.930000 |
| 5 | 673 | `minus` | 2 | 2 | 0 | 245 | 9.750000 |
| 6 | 733 | `plus` | 3 | 3 | 0 | 553 | 70.125000 |
| 7 | 313 | `plus` | 4 | 4 | 0 | 45 | 2.406250 |
| 8 | 1129 | `plus` | 9 | 9 | 0 | 159 | 3.208333 |
| 9 | 691 | `minus` | 11 | 11 | 0 | 114 | 1.974359 |
| 10 | 673 | `minus` | 2 | 2 | 0 | 245 | 9.750000 |

## 3. 最紧屏障原子

| P | side | labels | M | W | M-W | M/W | nearest distance |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 313 | `plus` | `[7, 11]` | 77 | 32 | 45 | 2.406250 | 53 |
| 313 | `plus` | `[11, 7]` | 77 | 32 | 45 | 2.406250 | 293 |
| 313 | `plus` | `[17, 7]` | 119 | 32 | 87 | 3.718750 | 713 |
| 313 | `plus` | `[11, 13]` | 143 | 32 | 111 | 4.468750 | 128 |
| 691 | `minus` | `[7, 3, 11]` | 231 | 117 | 114 | 1.974359 | 426 |
| 691 | `minus` | `[7, 3, 11]` | 231 | 117 | 114 | 1.974359 | 426 |
| 1129 | `plus` | `[3, 7, 11, 3]` | 231 | 72 | 159 | 3.208333 | 455 |
| 1129 | `plus` | `[3, 11, 7, 3]` | 231 | 72 | 159 | 3.208333 | 215 |
| 1129 | `plus` | `[3, 13, 7, 3]` | 273 | 72 | 201 | 3.791667 | 239 |
| 673 | `minus` | `[7, 3, 13]` | 273 | 28 | 245 | 9.750000 | 523 |
| 673 | `minus` | `[7, 3, 13]` | 273 | 28 | 245 | 9.750000 | 523 |
| 691 | `minus` | `[7, 3, 19]` | 399 | 117 | 282 | 3.410256 | 298 |

## 4. 命题行

| name | status | statement |
| --- | --- | --- |
| `one_step_modulus_barrier` | `closed_on_current_frontier` | For all current window-miss atoms, word_modulus exceeds phase width and the word has a single window representative. |
| `endpoint_distance_implied_by_modulus_barrier` | `closed` | The endpoint distance inequality follows from the one-step modulus barrier and actual mod-15 residue absence. |
| `global_modulus_dominates_phase_width` | `open` | A global proof must show every non-structural formal-unit cover word has modulus larger than its fixed phase window width. |
| `small_modulus_overlap_pdec` | `open` | If word_modulus is not larger than the window width, the possible actual-residue overlap must be certified by PDEC/ColumnCRT. |

## 5. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `FiniteOneStepBarrierClosed` | `true` | `true` | 当前全部窗口错位原子都由 M>W 的一跳模数屏障解释。 | closed on current finite frontier |
| `EndpointInequalityReducedToModulusWidth` | `true` | `true` | 端点距离守门项已化为 word_modulus 与 phase_width 的比较。 | closed |
| `GlobalModulusWidthDominanceProved` | `false` | `false` | 尚未证明任意 formal-unit 非结构冲突覆盖词都满足 M>W。 | CoverWordModulusDominatesPhaseWidthOrSmallModulusOverlapPDEC |
| `SmallModulusOverlapPDECExcluded` | `false` | `false` | 若 M<=W，则需对可能重叠给出 PDEC/ColumnCRT 排斥。 | CoverWordModulusDominatesPhaseWidthOrSmallModulusOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步关闭当前端点距离计算层，但全局行/列命题仍未无条件闭合。 | CoverWordModulusDominatesPhaseWidthOrSmallModulusOverlapPDEC |

## 6. 下一步

- 主攻：`CoverWordModulusDominatesPhaseWidthOrSmallModulusOverlapPDEC`。
- 直接证明目标：从 fixed band/k phase 宽度公式与 cover-word 标签乘积下界推出 `M>W`。
- 若存在 `M<=W`，则把对应 actual-residue overlap 登记为 small-modulus overlap `PDEC/ColumnCRT`。
- 当前仍未证明全局行/列无条件闭合。

## 7. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_barrier_router.py` | `1ca7e61999663032eecab0d856aa1543020323ba27d2910fbf06afc8a35e4eb9` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_window_miss_router.py` | `a8ef692843613d2a3b840606f8bb3f3959da6e822d4c8dac2aac95a1837abe78` |
| `data/square-phase-offband-prefix-gap-shadow-selector-window-miss-ledger.json` | `ae5a517480d202fd4c2e1480ab47dca31ba3b2fe9252599fa46db2009c443cfe` |
| `data/square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-ledger.json` | `f28ab6070f5e6e8b1f6bce16c9855098fd6a95e4b24b79c5b1716d4223626fc1` |
