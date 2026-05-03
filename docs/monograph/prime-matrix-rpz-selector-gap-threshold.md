# RPZ Selector Gap 阈值账本

**状态：** `rpz_selector_gap_threshold_current_layers`

## 总结

- h 层数：`4`。
- 已枚举 h 层数：`4`。
- BCB 样本记录数：`5`。
- 仅由长度强制 selector 的记录数：`2`。
- 仍需端点相位的记录数：`3`。

## Accepted Set 间隙阈值

| h | P(h) | accepted | rejected | max rejected run | length threshold |
|---:|---:|---:|---:|---:|---:|
| 5 | 30 | 30 | 0 | 0 | 1 |
| 7 | 210 | 126 | 84 | 1 | 2 |
| 11 | 2310 | 990 | 1320 | 5 | 6 |
| 13 | 30030 | 3510 | 26520 | 15 | 16 |

## BCB 样本长度分支

| top P | top row | h | candidate count | threshold | length alone | candidate rows |
|---:|---:|---:|---:|---:|---|---|
| 13 | 169 | 5 | 1 | 1 | `True` | `[439]` |
| 17 | 1211 | 7 | 1 | 2 | `False` | `[2940]` |
| 19 | 3659 | 7 | 2 | 2 | `True` | `[9930, 9931]` |
| 23 | 59 | 11 | 1 | 6 | `False` | `[123]` |
| 29 | 5210 | 13 | 1 | 16 | `False` | `[11622]` |

## 审稿结论

selector 存在定理自然分成两支：

1. **长度分支**：若 `|C_h(J)| >= max_rejected_run(A_h)+1`，则自动命中 `A_h`。
2. **短候选相位分支**：若候选行数低于该阈值，必须用端点相位精确证明命中 `A_h`，否则进入 seam/PDEC/ColumnCRT。

当前样本中 `2/5` 条记录由长度自动保证，`3/5` 条记录仍依赖端点相位。所以下一步不能只扩大核心长度估计；还必须证明短候选端点相位避开 rejected gaps。
