# Prime Matrix 旧筛 CRT 零行位置审计

**状态：** `experimental_zero_row_position_audit_not_a_proof`

本文审计旧 `p`-筛在 `p` 对齐延续行中的首个零行，并同步检查 `q×q` 中每个 `q` 行是否仍有旧筛幸存者。

## 参数

- `max_p`: `2000`
- `row_factor`: `200`
- `block_rows`: `5000`
- `full_period_max_p`: `23`
- `aligned_max_p`: `200`

## 总结

- 检查奇素数个数：`302`。
- 找到 `p` 对齐零行的个数：`5`。
- 首个 `p` 对齐零行落入 `ceil(q^2/p)` 覆盖内的个数：`0`。
- `q×q` 内旧筛 `q` 行失败个数：`0`。
- 已找到零行中的最小 `row/ceil(q^2/p)`：`1.5945945945945945`。

## 关键样本

| p | q | ceil(q²/p) | scan | first p-zero row | relation | min q-row survivors | q-row failure |
| ---: | ---: | ---: | --- | ---: | --- | ---: | --- |
| 3 | 5 | 9 | full_crt_row_period | None | not_found_within_scan_bound | 1 | False |
| 5 | 7 | 10 | full_crt_row_period | None | not_found_within_scan_bound | 1 | False |
| 7 | 11 | 18 | full_crt_row_period | None | not_found_within_scan_bound | 1 | False |
| 11 | 13 | 16 | full_crt_row_period | None | not_found_within_scan_bound | 1 | False |
| 13 | 17 | 23 | full_crt_row_period | 169 | after_q_square_p_row_cover | 1 | False |
| 17 | 19 | 22 | full_crt_row_period | 1211 | after_q_square_p_row_cover | 1 | False |
| 19 | 23 | 28 | full_crt_row_period | 3659 | after_q_square_p_row_cover | 1 | False |
| 23 | 29 | 37 | full_crt_row_period | 59 | after_q_square_p_row_cover | 1 | False |
| 29 | 31 | 34 | bounded_after_next_square | 5210 | after_q_square_p_row_cover | 1 | False |
| 31 | 37 | 45 | bounded_after_next_square | None | not_found_within_scan_bound | 1 | False |
| 37 | 41 | 46 | bounded_after_next_square | None | not_found_within_scan_bound | 1 | False |
| 41 | 43 | 46 | bounded_after_next_square | None | not_found_within_scan_bound | 1 | False |
| 43 | 47 | 52 | bounded_after_next_square | None | not_found_within_scan_bound | 1 | False |
| 47 | 53 | 60 | bounded_after_next_square | None | not_found_within_scan_bound | 1 | False |
| 53 | 59 | 66 | bounded_after_next_square | None | not_found_within_scan_bound | 1 | False |

## 审稿解释

实验支持两个分开的事实：

1. 对已找到的 `p` 对齐零行，首个位置均在 `ceil(q^2/p)` 之后；这支持“旧筛零行不会侵入下一素数平方壳层”的递推直觉。
2. 更直接相关的检查是 `q×q` 内每个 `q` 行的旧筛幸存者数；本次参数内没有出现失败。

但这仍不是证明。原因是 `p` 对齐行非空不能自动推出任意 `q` 行非空；`q` 行会跨越 `p` 行边界。因此正式引理必须直接证明 `q` 行旧筛幸存者非空，或证明所有可能的跨边界空窗会触发 `PDEC-or-SAE`。
