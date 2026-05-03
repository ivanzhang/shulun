# TotalDescent-TM 鸽巢余量审计

**状态：** `finite_total_descent_pigeonhole_margin_audit_not_global_proof`

本文把当前最窄硬点改写为一个显式计数不等式：候选头部/尾镜像 `h` 行数必须严格大于被复活点打断的候选行数。

## 参数

- `max_p`: `500`。
- `row_stride`: `1`。
- `max_levels`: `None`。
- `min_h`: `3`。

## 摘要

- 检查 q 行数：`21936`。
- 初始分支计数：`{'aligned_p_row_contained': 597, 'seam_window': 21339}`。
- 鸽巢闭合数：`21936`。
- 鸽巢失败数：`0`。
- 闭合比例：`1.0`。
- 最小最佳余量：`1`。
- 最大最佳余量：`72`。
- 末行端点穿孔行数：`93`。
- 最优 h 分布摘录：`{3: 21935, 5: 1}`。

## 最紧样本

| p | q | q-row | initial | terminal | h | candidates | blocked rows | margin |
|---:|---:|---:|---|---|---:|---:|---:|---:|
| 5 | 7 | 2 | `seam_window` | `[]` | 3 | 1 | 0 | 1 |
| 5 | 7 | 5 | `aligned_p_row_contained` | `[]` | 5 | 1 | 0 | 1 |
| 5 | 7 | 4 | `seam_window` | `[]` | 3 | 2 | 1 | 1 |
| 7 | 11 | 9 | `aligned_p_row_contained` | `[]` | 3 | 3 | 2 | 1 |
| 7 | 11 | 11 | `aligned_p_row_contained` | `[121]` | 3 | 3 | 2 | 1 |
| 11 | 13 | 10 | `seam_window` | `[]` | 3 | 4 | 3 | 1 |
| 13 | 17 | 13 | `aligned_p_row_contained` | `[]` | 3 | 5 | 4 | 1 |
| 17 | 19 | 16 | `seam_window` | `[]` | 3 | 6 | 5 | 1 |
| 5 | 7 | 3 | `aligned_p_row_contained` | `[]` | 3 | 2 | 0 | 2 |
| 5 | 7 | 6 | `aligned_p_row_contained` | `[]` | 3 | 2 | 0 | 2 |
| 5 | 7 | 7 | `seam_window` | `[49]` | 3 | 2 | 0 | 2 |
| 7 | 11 | 3 | `seam_window` | `[]` | 3 | 3 | 1 | 2 |
| 7 | 11 | 4 | `aligned_p_row_contained` | `[]` | 3 | 3 | 1 | 2 |
| 7 | 11 | 5 | `seam_window` | `[]` | 3 | 3 | 1 | 2 |
| 7 | 11 | 6 | `aligned_p_row_contained` | `[]` | 3 | 3 | 1 | 2 |
| 7 | 11 | 8 | `aligned_p_row_contained` | `[]` | 3 | 3 | 1 | 2 |

## 审稿引理

设 `C_h(I)` 为完整包含在 `I` 中且满足 `rho<=h` 或 `N_h-rho+1<=h` 的 `h` 对齐行集合。设 `B_h(I)` 为其中含有复活点或端点穿孔的行集合。若

\[
|C_h(I)|>|B_h(I)|,
\]

则存在一条候选 `h` 行没有被任何复活点打断。由于 `I` 在旧 `p`-筛下为零，该行在 `h`-筛下为零；再由头部/尾镜像条件落入 `h×h` 方阵。

因此 `TotalDescent-TM` 的当前最窄可审查形式是证明：对任意相邻 `p<q` 与任意 `2<=s<=q`，存在 `h<=p` 使上述严格不等式成立；或证明所有失败相位触发 `SAE/PDEC/ColumnCRT`。
