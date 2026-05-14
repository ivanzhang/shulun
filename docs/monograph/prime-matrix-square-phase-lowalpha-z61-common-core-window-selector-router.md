# Prime Matrix square-phase low-alpha z=61 common-core 窗口选择器

**状态：** `z61_two_three_common_core_overlap_reduced_to_ratio_window_selector_open`

`2C/3C` common-core overlap 的目标权重完全由 bucket 比例窗口选择决定：把 `C=11*19*23` 二分后，只保留使 `max(d,e)/min(d,e)` 落在 `(4,8]` 的分割。样本中被选中的无序分割只有 `prefix=2` 的两个分割和 `prefix=3` 的一个分割；其有向对称权重和精确等于 overlap 权重。下一步应证明这类窗口分割容量受控，或登记 Window-PDEC。

```text
selector_row_count=8
selected_oriented_edge_count=6
selected_unordered_split_count=3
selected_weight=0.555427
selector_weight_identity_error=0.000000
ratio_window_selector_identity_closed=true
row_column_unconditional_closed=false
```

## 1. 入选有向边

| prefix | core split | d | e | ratio | weight |
| ---: | --- | ---: | ---: | ---: | ---: |
| 2 | `[19, 253]` | 38 | 253 | 6.657895 | 0.188377 |
| 2 | `[23, 209]` | 46 | 209 | 4.543478 | 0.202029 |
| 3 | `[19, 253]` | 57 | 253 | 4.438596 | 0.165021 |

## 2. 候选 bucket 计数

| bucket | oriented candidates |
| --- | ---: |
| `far>8` | 7 |
| `mid<=4` | 1 |
| `unbalanced<=8` | 3 |

## 3. 证明边界

- 已闭合：`2C/3C` common-core 权重到 ratio-window 选择器的精确等价。
- 未闭合：窗口分割容量全局界，或 Window-PDEC 排斥。
- 下一目标：`CommonCoreRatioWindowPartitionBoundOrWindowPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json` | `4784443770637bbe4832130b0d33a9d72035071ad39e497e65ff67571c5d16d1` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_common_core_window_selector_router.py` | `b17a30042d33830667ba97f1c0058c4e99b18ecceb1b4e95585963129e1b7cb5` |
