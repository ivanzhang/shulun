# RPZ First-Grid-Fail Seam 标准形证书

**状态：** `rpz_first_grid_fail_seam_normal_form_certificate`

## 标准形

设 `g=p-r`，`delta=-(a-1)g mod r`。首个 `grid_fail` 当且仅当 `g<delta<r`。此时 `p` 行跨相邻两条 `r` 行：

```text
left cap length  = delta；
right cap length = r+g-delta；
left missing     = r-delta；
right missing    = delta-g；
missing mass     = r-g。
```

该 seam 内的 `r`-筛幸存者至多为右端点 `ap`。

## 总结

- 转换数：`5`。
- 含 grid_fail 的转换数：`3`。
- seam 相位行数：`12`。
- 完整 `Q` 中 grid_fail 相位基数：`1752`。
- 与源账本计数不一致数：`0`。

## 转换表

| p | r | Q | gap | fail deltas | fail residues mod r | source fail count | count ok |
|---:|---:|---:|---:|---|---|---:|---|
| 3 | 2 | 2 | 1 | `[]` | `[]` | 0 | yes |
| 5 | 3 | 6 | 2 | `[]` | `[]` | 0 | yes |
| 7 | 5 | 30 | 2 | `[3, 4]` | `[2, 4]` | 12 | yes |
| 11 | 7 | 210 | 4 | `[5, 6]` | `[5, 3]` | 60 | yes |
| 13 | 11 | 2310 | 2 | `[3, 4, 5, 6, 7, 8, 9, 10]` | `[5, 10, 4, 9, 3, 8, 2, 7]` | 1680 | yes |

## 证书意义

first-grid-fail seam 不是任意坏窗。它具有固定双帽结构、固定缺口守恒 `r-g`，且最多只有右端点 `ap` 一个 `r`-rough 幸存者。持久出现时，相位 `delta` 和行号余类 `a mod r` 被固定，适合进入 `PDEC`；若右端点幸存者携带稳定列位移或吸收标签，则进入 `ColumnCRT`。

本证书只完成标准形抽取，不排除这些 seam 相位。下一步需要提交 `PDEC/ColumnCRT` 排斥证书，或证明正式反例族不能命中这些 seam 相位。
