# RPZ Seam/PDEC/ColumnCRT 出口压力账本

**状态：** `rpz_seam_exit_pressure_ledger_not_exclusion`

## 总结

- 已吸收 rejected phases：`27924`。
- seam 行数：`12`。
- seam 支持总量：`1752`。
- 下层标签已杀死端点：`1348`。
- unit endpoint 相位：`404`。
- unit endpoint 占比：`0.230594`。
- ColumnCRT 位移类数：`10`。
- 最大聚合位移负载：`96`。
- unit endpoint 是否全为固定非零位移：`True`。

## 按相邻下降聚合

| p | r | seam rows | support | killed endpoint | unit endpoint | max unit/row | displacement classes |
|---:|---:|---:|---:|---:|---:|---:|---|
| 7 | 5 | 2 | 12 | 8 | 4 | 2 | `[1, 2]` |
| 11 | 7 | 2 | 60 | 44 | 16 | 8 | `[5, 7]` |
| 13 | 11 | 8 | 1680 | 1296 | 384 | 48 | `[1, 3, 4, 5, 10, 11]` |

## 按 ColumnCRT 位移类聚合

| label | d mod label | seam rows | unit load | support | source rows [p,r,delta,rho] |
|---:|---:|---:|---:|---:|---|
| 7 | 1 | 1 | 2 | 6 | `[[7, 5, 3, 2]]` |
| 7 | 2 | 1 | 2 | 6 | `[[7, 5, 4, 4]]` |
| 11 | 5 | 1 | 8 | 30 | `[[11, 7, 5, 5]]` |
| 11 | 7 | 1 | 8 | 30 | `[[11, 7, 6, 3]]` |
| 13 | 1 | 1 | 48 | 210 | `[[13, 11, 9, 2]]` |
| 13 | 3 | 1 | 48 | 210 | `[[13, 11, 6, 9]]` |
| 13 | 4 | 2 | 96 | 420 | `[[13, 11, 4, 10], [13, 11, 8, 8]]` |
| 13 | 5 | 1 | 48 | 210 | `[[13, 11, 10, 7]]` |
| 13 | 10 | 1 | 48 | 210 | `[[13, 11, 5, 4]]` |
| 13 | 11 | 2 | 96 | 420 | `[[13, 11, 3, 5], [13, 11, 7, 3]]` |

## 审稿结论

rejected set 已经不是大规模未命名对象：它被压缩为 `12` 条 first-grid-fail seam 行。
其中非 unit 端点全部由下层小素数标签吸收，真正仍需处理的是 `404` 个 unit endpoint 相位。
这些 unit endpoint 又全部进入固定非零 ColumnCRT 位移类，聚合后只有 `10` 个 `(label,d)` 类。

因此下一步硬点不能写成“继续调阈值”或“继续检查 rejected phase”。有效目标只剩三类：

1. 证明 formal-family 起始相位避开这 `12` 条 seam 行；
2. 对这 `12` 条单余类 PDEC 支持行给出同口径 `U_CRT<L_PDEC`；
3. 对聚合后的 `10` 个固定非零 ColumnCRT 位移类证明独立 `ColumnCRTDefect` 排斥。

本账本仍不是闭合证明；它把最后出口从逐相位问题压缩为可逐行审稿的有限窄接口。
