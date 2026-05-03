# RPZ-BCB Accepted Top-Row Residue Preimage 账本

**状态：** `rpz_bcb_accepted_top_row_residue_preimage`

## 总结

- 参数族数：`5`。
- 实际样本落入 selector preimage 的族数：`5`。
- 仍存在 bad residue 的族数：`4`。

## 逐族 preimage 统计

| top P | h | shifts | period hP | status counts | candidate histogram | max bad run | max selector run | actual R mod hP | actual status | dist to bad |
|---:|---:|---|---:|---|---|---:|---:|---:|---|---:|
| 13 | 5 | `[-1, 3]` | 150 | `{'selector': 150}` | `{'1': 150}` | 0 | 150 | 19 | `selector` | None |
| 17 | 7 | `[-1, 3]` | 1470 | `{'all_rejected': 588, 'selector': 882}` | `{'1': 1470}` | 8 | 15 | 1211 | `selector` | 7 |
| 19 | 7 | `[-3, 1]` | 1470 | `{'all_rejected': 420, 'selector': 1050}` | `{'1': 1050, '2': 420}` | 2 | 7 | 719 | `selector` | 3 |
| 23 | 11 | `[-1, 3]` | 25410 | `{'all_rejected': 11880, 'no_candidate': 4620, 'selector': 8910}` | `{'0': 4620, '1': 20790}` | 7 | 3 | 59 | `selector` | 2 |
| 29 | 13 | `[-4, 0]` | 390390 | `{'all_rejected': 344760, 'selector': 45630}` | `{'1': 390390}` | 34 | 1 | 5210 | `selector` | 1 |

## all-rejected 出口键

| top P | h | first-failure keys |
|---:|---:|---|
| 13 | 5 | `[]` |
| 17 | 7 | `[{'first_failure_key': [7, 5, 3, 2], 'count': 294}, {'first_failure_key': [7, 5, 4, 4], 'count': 294}]` |
| 19 | 7 | `[{'first_failure_key': [7, 5, 3, 2], 'count': 378}, {'first_failure_key': [7, 5, 4, 4], 'count': 378}]` |
| 23 | 11 | `[{'first_failure_key': [7, 5, 3, 2], 'count': 2970}, {'first_failure_key': [7, 5, 4, 4], 'count': 2970}, {'first_failure_key': [11, 7, 5, 5], 'count': 2970}, {'first_failure_key': [11, 7, 6, 3], 'count': 2970}]` |
| 29 | 13 | `[{'first_failure_key': [7, 5, 3, 2], 'count': 15210}, {'first_failure_key': [7, 5, 4, 4], 'count': 15210}, {'first_failure_key': [11, 7, 5, 5], 'count': 15210}, {'first_failure_key': [11, 7, 6, 3], 'count': 15210}, {'first_failure_key': [13, 11, 3, 5], 'count': 35490}, {'first_failure_key': [13, 11, 4, 10], 'count': 35490}, {'first_failure_key': [13, 11, 5, 4], 'count': 35490}, {'first_failure_key': [13, 11, 6, 9], 'count': 35490}, {'first_failure_key': [13, 11, 7, 3], 'count': 35490}, {'first_failure_key': [13, 11, 8, 8], 'count': 35490}, {'first_failure_key': [13, 11, 9, 2], 'count': 35490}, {'first_failure_key': [13, 11, 10, 7], 'count': 35490}]` |

## 审稿结论

当前实际 top row residue 全部落入 selector preimage，但每个参数族仍有 bad residue。
因此全局证明不能由 preimage 枚举替代；下一义务是证明 formal BCB 反例的 `R mod hP(h)` 避开 bad residue。
若落入 all-rejected residue，则该 residue 已携带 first-failure seam/PDEC/ColumnCRT 出口键；若落入 no-candidate residue，则回到 BCB grid/endpoint 出口。
