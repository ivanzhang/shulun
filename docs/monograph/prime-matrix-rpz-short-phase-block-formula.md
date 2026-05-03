# RPZ 短候选端点禁区块公式账本

**状态：** `rpz_short_candidate_endpoint_forbidden_block_formula`

## 总结

- 短候选族数：`3`。
- 块公式匹配枚举的族数：`3`。
- 实际短候选记录数：`3`。
- 实际候选行 accepted 数：`3`。

## 块公式

若 `length<2h`，每个端点 `u` 最多包含一个完整 `h` 行。行号 `m` 的完整行区间为

```text
[(m-1)h+1, mh]。
```

长度为 `length` 的核心起点 `u` 包含该行当且仅当

```text
mh-length+1 <= u <= (m-1)h+1。
```

因此每个 rejected 行相位给出一个端点禁区块，块长为 `length-h+1`。

## 族公式核验

| h | length | P(h) | period hP(h) | block width | accepted phases | rejected phases | no-candidate | selector | all-rejected | formula match |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 7 | 13 | 210 | 1470 | 7 | 126 | 84 | 0 | 882 | 588 | `True` |
| 11 | 19 | 2310 | 25410 | 9 | 990 | 1320 | 4620 | 8910 | 11880 | `True` |
| 13 | 25 | 30030 | 390390 | 13 | 3510 | 26520 | 0 | 45630 | 344760 | `True` |

## 实际端点余量

| top P | top row | h | length | u mod hP | candidate | phase | accepted run | row margin | endpoint block offset | distance to all-rejected |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 17 | 1211 | 7 | 13 | 1464 | 2940 | 0 | 2 | 1 | `6/0` | 7 |
| 23 | 59 | 11 | 19 | 1338 | 123 | 123 | 1 | 1 | `3/5` | 6 |
| 29 | 5210 | 13 | 25 | 151062 | 11622 | 11622 | 1 | 1 | `0/12` | 1 |

## 审稿结论

短候选分支已经从大规模端点枚举压缩为一阶块公式：rejected 行相位乘以端点块宽。
当前实际端点均在 accepted 行相位块内，且到 all-rejected 端点集合的循环距离为正。
但这仍不是全局闭合；下一步必须从正式 BCB 构造推出 candidate row phase 属于 `A_h`，否则仍需调用 seam/PDEC/ColumnCRT 出口证书。
