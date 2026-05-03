# RPZ-BCB 核心低筛连续覆盖长度障碍

**状态：** `rpz_bcb_no_tailanchor_core_run_obstruction`

## 总结

- h 层数：`4`。
- BCB 记录数：`5`。
- 被低筛覆盖长度障碍排斥的记录数：`5`。
- 最小障碍余量：`4`。

## 低筛最大连续覆盖长度

| h | P(h) | max covered run | example start | example end |
|---:|---:|---:|---:|---:|
| 5 | 30 | 5 | 2 | 6 |
| 7 | 210 | 9 | 2 | 10 |
| 11 | 2310 | 13 | 114 | 126 |
| 13 | 30030 | 21 | 9440 | 9460 |

## BCB 核心长度对比

| top P | top row | h | core interval | core length | max covered run | margin | obstructed |
|---:|---:|---:|---|---:|---:|---:|---|
| 13 | 169 | 5 | `[2188, 2196]` | 9 | 5 | 4 | `True` |
| 17 | 1211 | 7 | `[20574, 20586]` | 13 | 9 | 4 | `True` |
| 19 | 3659 | 7 | `[69504, 69518]` | 15 | 9 | 6 | `True` |
| 23 | 59 | 11 | `[1338, 1356]` | 19 | 13 | 6 | `True` |
| 29 | 5210 | 13 | `[151062, 151086]` | 25 | 21 | 4 | `True` |

## 审稿结论

在 no-TailAnchor 分支中，BCB-Core 要求 `J_T0` 是 `h`-筛零区间；这不是端点相位问题，而是低筛连续覆盖长度问题。
当前五条 BCB 样本的核心长度全部严格超过对应 `h` 层的最大连续低筛覆盖长度，所以这些参数族的 no-TailAnchor BCB 核心不相容。
该账本把当前最小硬点从 accepted preimage 进一步上移为 Jacobsthal 型上界：全局证明若能给出 `max_run_h < |J_T0|`，则 BCB no-TailAnchor 分支直接关闭；否则剩余仍需进入 endpoint/first-failure/PDEC/ColumnCRT 出口。
