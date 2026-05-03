# TotalDescent-TM 鸽巢余量审计

**状态：** `finite_total_descent_pigeonhole_margin_audit_not_global_proof`

本文把当前最窄硬点改写为一个显式计数不等式：候选头部/尾镜像 `h` 行数必须严格大于被复活点打断的候选行数。

## 参数

- `max_p`: `2000`。
- `row_stride`: `25`。
- `max_levels`: `None`。
- `min_h`: `3`。

## 摘要

- 检查 q 行数：`11583`。
- 初始分支计数：`{'aligned_p_row_contained': 95, 'seam_window': 11488}`。
- 鸽巢闭合数：`11583`。
- 鸽巢失败数：`0`。
- 闭合比例：`1.0`。
- 最小最佳余量：`1`。
- 最大最佳余量：`249`。
- 末行端点穿孔行数：`301`。
- 最优 h 分布摘录：`{3: 11583}`。

## 最紧样本

| p | q | q-row | initial | terminal | h | candidates | blocked rows | margin |
|---:|---:|---:|---|---|---:|---:|---:|---:|
| 5 | 7 | 2 | `seam_window` | `[]` | 3 | 1 | 0 | 1 |
| 7 | 11 | 11 | `aligned_p_row_contained` | `[121]` | 3 | 3 | 2 | 1 |
| 5 | 7 | 7 | `seam_window` | `[49]` | 3 | 2 | 0 | 2 |
| 31 | 37 | 37 | `aligned_p_row_contained` | `[1369]` | 3 | 12 | 10 | 2 |
| 7 | 11 | 2 | `aligned_p_row_contained` | `[]` | 3 | 3 | 0 | 3 |
| 11 | 13 | 2 | `seam_window` | `[]` | 3 | 3 | 0 | 3 |
| 11 | 13 | 13 | `seam_window` | `[169]` | 3 | 4 | 1 | 3 |
| 13 | 17 | 17 | `aligned_p_row_contained` | `[289]` | 3 | 5 | 2 | 3 |
| 17 | 19 | 2 | `seam_window` | `[]` | 3 | 5 | 2 | 3 |
| 19 | 23 | 23 | `seam_window` | `[529]` | 3 | 7 | 4 | 3 |
| 43 | 47 | 47 | `seam_window` | `[2209]` | 3 | 15 | 12 | 3 |
| 13 | 17 | 2 | `seam_window` | `[]` | 3 | 5 | 1 | 4 |
| 17 | 19 | 19 | `seam_window` | `[361]` | 3 | 6 | 2 | 4 |
| 23 | 29 | 27 | `aligned_p_row_contained` | `[]` | 3 | 9 | 5 | 4 |
| 29 | 31 | 31 | `seam_window` | `[961]` | 3 | 10 | 6 | 4 |
| 37 | 41 | 41 | `seam_window` | `[1681]` | 3 | 13 | 9 | 4 |

## 审稿引理

设 `C_h(I)` 为完整包含在 `I` 中且满足 `rho<=h` 或 `N_h-rho+1<=h` 的 `h` 对齐行集合。设 `B_h(I)` 为其中含有复活点或端点穿孔的行集合。若

\[
|C_h(I)|>|B_h(I)|,
\]

则存在一条候选 `h` 行没有被任何复活点打断。由于 `I` 在旧 `p`-筛下为零，该行在 `h`-筛下为零；再由头部/尾镜像条件落入 `h×h` 方阵。

因此 `TotalDescent-TM` 的当前最窄可审查形式是证明：对任意相邻 `p<q` 与任意 `2<=s<=q`，存在 `h<=p` 使上述严格不等式成立；或证明所有失败相位触发 `SAE/PDEC/ColumnCRT`。
