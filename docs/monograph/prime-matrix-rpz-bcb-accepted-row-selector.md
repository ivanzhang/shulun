# RPZ BCB Accepted Lower-Row 选择器账本

**状态：** `rpz_bcb_accepted_row_selector_current_samples`

## 总结

- BCB-Core 记录数：`5`。
- 存在 accepted selector 的记录数：`5`。
- 候选完整下层行总数：`6`。
- accepted 候选行总数：`6`。
- rejected 候选行总数：`0`。
- 是否每条记录都有 selector：`True`。

## 精确选择器形式

对 BCB 核心区间 `J=[u,v]` 与半宽素数 `h`，完整下层候选行集合为

```text
C_h(J)={m: u <= (m-1)h+1 and mh <= v}。
```

目标从“任意起始行都安全”收窄为更弱且足够的选择器命题：

```text
C_h(J) ∩ A_h != empty。
```

若相交，则选择其中一条 accepted lower zero-row 下降；若不相交，则所有候选行回流到 seam/PDEC/ColumnCRT 出口。

## 当前样本选择器表

| top P | top row | h | core interval | candidate rows | accepted rows | rejected rows | selected |
|---:|---:|---:|---|---|---|---|---:|
| 13 | 169 | 5 | `[2188, 2196]` | `[439]` | `[439]` | `[]` | 439 |
| 17 | 1211 | 7 | `[20574, 20586]` | `[2940]` | `[2940]` | `[]` | 2940 |
| 19 | 3659 | 7 | `[69504, 69518]` | `[9930, 9931]` | `[9930, 9931]` | `[]` | 9930 |
| 23 | 59 | 11 | `[1338, 1356]` | `[123]` | `[123]` | `[]` | 123 |
| 29 | 5210 | 13 | `[151062, 151086]` | `[11622]` | `[11622]` | `[]` | 11622 |

## 审稿结论

当前 `5/5` 条 BCB-Core 样本均满足 `C_h(J)∩A_h` 非空；所有 `6` 条候选完整下层行也都 accepted。
这比上一账本更接近正式证明所需对象：不必证明每个可能下层行都安全，只需证明存在一个 accepted selector。

仍未闭合的是全局选择器存在定理。下一硬点应证明正式 BCB-Core 的端点相位和长度强制 `C_h(J)` 命中 `A_h`；否则全拒绝候选行必须进入已材料化 seam/PDEC/ColumnCRT 出口。
