# RPZ 短候选端点相位账本

**状态：** `rpz_short_candidate_endpoint_phase_ledger`

## 总结

- 短候选样本记录数：`3`。
- 相位族数：`3`。
- 实际样本有 selector 数：`3`。
- 实际样本无 selector 数：`0`。
- 存在 all-rejected 相位的族数：`3`。

## 关键相位细化

短候选情形下，`u mod h` 只决定网格包含；是否命中 `A_h` 取决于候选行号 `m mod P(h)`。
因此 selector 相位必须细化为：

```text
u mod h*P(h)。
```

## 短候选实际样本

| top P | top row | h | length | u mod h | u mod hP | candidates | packets | selector | all-rejected family phases |
|---:|---:|---:|---:|---:|---:|---|---|---|---:|
| 17 | 1211 | 7 | 13 | 1 | 1464 | `[2940]` | `[{'row': 2940, 'phase_mod_primorial': 0, 'accepted': True, 'first_failure_key': None}]` | `True` | 588 |
| 23 | 59 | 11 | 19 | 7 | 1338 | `[123]` | `[{'row': 123, 'phase_mod_primorial': 123, 'accepted': True, 'first_failure_key': None}]` | `True` | 11880 |
| 29 | 5210 | 13 | 25 | 2 | 151062 | `[11622]` | `[{'row': 11622, 'phase_mod_primorial': 11622, 'accepted': True, 'first_failure_key': None}]` | `True` | 344760 |

## 相位族统计

| h | length | period hP(h) | candidate count histogram | selector counts | all-rejected counts | first-failure rows |
|---:|---:|---:|---|---|---|---|
| 7 | 13 | 1470 | `{'1': 1470}` | `{'1': 882}` | `{'1': 588}` | `[{'first_failure_key': [7, 5, 3, 2], 'count': 294}, {'first_failure_key': [7, 5, 4, 4], 'count': 294}]` |
| 11 | 19 | 25410 | `{'0': 4620, '1': 20790}` | `{'1': 8910}` | `{'1': 11880}` | `[{'first_failure_key': [7, 5, 3, 2], 'count': 2970}, {'first_failure_key': [7, 5, 4, 4], 'count': 2970}, {'first_failure_key': [11, 7, 5, 5], 'count': 2970}, {'first_failure_key': [11, 7, 6, 3], 'count': 2970}]` |
| 13 | 25 | 390390 | `{'1': 390390}` | `{'1': 45630}` | `{'1': 344760}` | `[{'first_failure_key': [7, 5, 3, 2], 'count': 15210}, {'first_failure_key': [7, 5, 4, 4], 'count': 15210}, {'first_failure_key': [11, 7, 5, 5], 'count': 15210}, {'first_failure_key': [11, 7, 6, 3], 'count': 15210}, {'first_failure_key': [13, 11, 3, 5], 'count': 35490}, {'first_failure_key': [13, 11, 4, 10], 'count': 35490}, {'first_failure_key': [13, 11, 5, 4], 'count': 35490}, {'first_failure_key': [13, 11, 6, 9], 'count': 35490}, {'first_failure_key': [13, 11, 7, 3], 'count': 35490}, {'first_failure_key': [13, 11, 8, 8], 'count': 35490}, {'first_failure_key': [13, 11, 9, 2], 'count': 35490}, {'first_failure_key': [13, 11, 10, 7], 'count': 35490}]` |

## 审稿结论

当前三个短候选样本都命中 accepted selector；但对应的完整相位族中仍存在 all-rejected 相位。
因此下一硬点不是证明任意短候选相位都安全，而是证明正式 BCB 构造的 `u mod hP(h)` 避开这些 all-rejected 相位。
若不能排除，则这些 all-rejected 相位已经带有 first-failure seam 键，可进入 seam/PDEC/ColumnCRT 出口账本。
