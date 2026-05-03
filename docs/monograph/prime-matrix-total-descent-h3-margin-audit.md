# 固定 h=3 的 TotalDescent-TM 余量审计

**状态：** `finite_h3_total_descent_margin_audit_not_global_proof`

本文专攻当前最窄硬点的更强版本：固定使用 `h=3`，不再任选下降层。由于 `N_3=2`，完整 3 对齐行自动满足 CRT 头部/尾镜像命中；更强的是，完整 3 行的唯一六轮候选一旦不是 `[5,p]` 复活点，就直接成为旧 `p`-筛零窗的幸存点矛盾。

## 参数

- `max_p`: `5000`。
- `row_stride`: `1`。
- `max_n`: `25030009`。
- `max_h3_row`: `8343337`。

## 摘要

- 检查 q 行数：`1552462`。
- 初始分支计数：`{'aligned_p_row_contained': 5671, 'seam_window': 1546791}`。
- `h=3` 闭合数：`1552462`。
- `h=3` 失败数：`0`。
- 闭合比例：`1.0`。
- 最小余量：`1`。
- 最大余量：`561`。
- 末行 `q^2` 行数：`667`。

## 最紧样本

| p | q | q-row | initial | h3 rows | candidates | blocked | margin | terminal |
|---:|---:|---:|---|---|---:|---:|---:|---|
| 5 | 7 | 2 | `seam_window` | `[4, 4]` | 1 | 0 | 1 | `False` |
| 5 | 7 | 5 | `aligned_p_row_contained` | `[11, 11]` | 1 | 0 | 1 | `False` |
| 5 | 7 | 4 | `seam_window` | `[8, 9]` | 2 | 1 | 1 | `False` |
| 7 | 11 | 9 | `aligned_p_row_contained` | `[31, 33]` | 3 | 2 | 1 | `False` |
| 7 | 11 | 11 | `aligned_p_row_contained` | `[38, 40]` | 3 | 2 | 1 | `True` |
| 11 | 13 | 10 | `seam_window` | `[40, 43]` | 4 | 3 | 1 | `False` |
| 13 | 17 | 13 | `aligned_p_row_contained` | `[69, 73]` | 5 | 4 | 1 | `False` |
| 17 | 19 | 16 | `seam_window` | `[96, 101]` | 6 | 5 | 1 | `False` |
| 5 | 7 | 3 | `aligned_p_row_contained` | `[6, 7]` | 2 | 0 | 2 | `False` |
| 5 | 7 | 6 | `aligned_p_row_contained` | `[13, 14]` | 2 | 0 | 2 | `False` |
| 5 | 7 | 7 | `seam_window` | `[15, 16]` | 2 | 0 | 2 | `True` |
| 7 | 11 | 3 | `seam_window` | `[9, 11]` | 3 | 1 | 2 | `False` |
| 7 | 11 | 4 | `aligned_p_row_contained` | `[12, 14]` | 3 | 1 | 2 | `False` |
| 7 | 11 | 5 | `seam_window` | `[16, 18]` | 3 | 1 | 2 | `False` |
| 7 | 11 | 6 | `aligned_p_row_contained` | `[20, 22]` | 3 | 1 | 2 | `False` |
| 7 | 11 | 8 | `aligned_p_row_contained` | `[27, 29]` | 3 | 1 | 2 | `False` |
| 11 | 13 | 5 | `seam_window` | `[19, 21]` | 3 | 1 | 2 | `False` |
| 11 | 13 | 8 | `seam_window` | `[32, 34]` | 3 | 1 | 2 | `False` |
| 11 | 13 | 11 | `aligned_p_row_contained` | `[45, 47]` | 3 | 1 | 2 | `False` |
| 11 | 13 | 12 | `aligned_p_row_contained` | `[49, 52]` | 4 | 2 | 2 | `False` |

## 严格化目标

固定 `h=3` 时，每条完整 3 对齐行只有一个避开 `2,3` 的候选数。若该候选数的最小素因子在 `[5,p]`，该行被复活点打断；否则该候选是 `p`-rough 点。由于候选数大于 `1` 且避开 `2,3`，在旧 `p`-筛零窗假设下它已经给出直接幸存点矛盾；等价地，它会强制出不可能的 `3`-筛零行。

因此最窄硬点可写成显式 6-轮不等式：任意相邻 `p<q` 与任意 `2<=s<=q`，令 `I=[(s-1)q+1,sq]`，完整 3 行的数量严格大于其中候选数最小素因子落在 `[5,p]` 的数量。

有限账本显示该不等式在测试域内余量恒正。若要成为正式证明，需要给出全局覆盖上界；若上界失败，则失败意味着 `I` 中 6-轮候选数被 `[5,p]` 素因子精确覆盖，应触发 `SAE/PDEC/ColumnCRT`。
