# RPZ-BCB 候选下层行相位身份账本

**状态：** `rpz_bcb_candidate_lower_row_phase_identity`

## 总结

- BCB 记录数：`5`。
- 核心区间公式匹配数：`5`。
- 候选行公式匹配数：`5`。
- 候选行总数：`6`。
- accepted 候选行数：`6`。
- 有 selector 的记录数：`5`。

## 精确身份

BCB 核心区间为

```text
L=(R-1)P+1+s_min+T,
U=RP+s_max-T。
```

完整包含的 `h` 对齐候选行满足

```text
m_min=floor((L+h-2)/h)+1,
m_max=floor(U/h)。
```

若 `P=Qh+d`，则相位只依赖 `R mod hP(h)`：

```text
m_min=(R-1)Q+floor(((R-1)d+s_min+T+h-1)/h)+1,
m_max=RQ+floor((Rd+s_max-T)/h)。
```

## 当前样本

| top P | top row | h | shifts | R mod hP(h) | candidate rows | phases | accepted | selector | identity match |
|---:|---:|---:|---|---:|---|---|---|---|---|
| 13 | 169 | 5 | `[-1, 3]` | 19 | `[439]` | `[19]` | `[True]` | `True` | `True` |
| 17 | 1211 | 7 | `[-1, 3]` | 1211 | `[2940]` | `[0]` | `[True]` | `True` | `True` |
| 19 | 3659 | 7 | `[-3, 1]` | 719 | `[9930, 9931]` | `[60, 61]` | `[True, True]` | `True` | `True` |
| 23 | 59 | 11 | `[-1, 3]` | 59 | `[123]` | `[123]` | `[True]` | `True` | `True` |
| 29 | 5210 | 13 | `[-4, 0]` | 5210 | `[11622]` | `[11622]` | `[True]` | `True` | `True` |

## 审稿结论

候选下层行不再是程序扫描对象，而是 BCB 参数给出的显式 floor 身份。
当前样本中该身份逐项匹配 `contained_half_rows`，且 `6/6` 个候选行相位都属于 `A_h`。
剩余全局硬点是证明正式 BCB 反例的 `R mod hP(h)` 必诱导 accepted 候选相位；若诱导 rejected 相位，则回流到已命名 first-failure 出口。
