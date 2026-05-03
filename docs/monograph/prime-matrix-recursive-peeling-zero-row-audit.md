# 零行递归剥离审计

**状态：** `recursive_peeling_audit_supports_punctured_windows_not_automatic_zero_rows`

## 参数

- `source`: `docs/monograph/prime-matrix-zero-row-crt-audit.json`
- `source_max_p`: `2000`
- `max_levels`: `6`

## 总结

- 已知首个对齐零行记录数：`5`。
- 一步剥离后仍完全零的记录数：`2`。
- 一步剥离后包含完整下层对齐零行的记录数：`1`。
- 剥离剖面中出现连续对齐零行对的记录数：`0`。

## 逐例剖面

| p | row | interval | next | one-step zero | contains aligned zero | consecutive pair | first peeled level | survivors | contained zero rows |
|---:|---:|---|---:|---|---|---|---:|---:|---|
| 13 | 169 | `[2185, 2197]` | 17 | `false` | `false` | `false` | 11 | 1 | `[]` |
| 17 | 1211 | `[20571, 20587]` | 19 | `true` | `false` | `false` | 13 | 0 | `[]` |
| 19 | 3659 | `[69503, 69521]` | 23 | `false` | `false` | `false` | 17 | 1 | `[]` |
| 23 | 59 | `[1335, 1357]` | 29 | `false` | `false` | `false` | 19 | 1 | `[]` |
| 29 | 5210 | `[151062, 151090]` | 31 | `true` | `true` | `false` | 23 | 0 | `[6569]` |

## 审稿解释

若一个区间在 `p`-筛下为零，剥去顶层素数 `p` 后，重新出现的幸存者只能来自该区间内的 `p` 的倍数，并且其商避开更小筛素数。故递归对象不是零行，而是带少数复活点的 punctured zero window。

本审计显示：已知样本中，一步剥离后完全仍零的情况存在，但多数情况会产生复活点；更关键的是，没有样本在剥离剖面中自动产生连续下层对齐零行。因此“递归剥离自动推出连续零行”不能作为无条件证明出口。

可保留的硬点是：若能证明这些复活点不能被后续缝合窗口稳定吸收，或证明吸收必造成 `PDEC/TailAnchor/ColumnCRT` 缺陷，则递归剥离可以成为主链条的有效压力项。
