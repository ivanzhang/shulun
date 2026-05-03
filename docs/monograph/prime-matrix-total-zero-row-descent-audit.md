# 任意 q 零行总下降审计

**状态：** `finite_total_zero_row_descent_audit_not_global_proof`

本文把 aligned 分支、seam 分支、末行 `q^2` 端点穿孔、CRT 周期性和尾镜像统一到同一条件下降模型中，检验：若高阶 `q×q` 方阵内任意非第一行是零行，是否会强制某个小阶 `h×h` 方阵内也出现零行。

## 参数

- `max_p`: `500`。
- `row_stride`: `1`。
- `max_levels`: `None`。
- `q_rows`: `2..q; row 1 omitted because it is not a candidate zero row`。

## 摘要

- 检查 q 行数：`21936`。
- 初始分支计数：`{'aligned_p_row_contained': 597, 'seam_window': 21339}`。
- 出现条件强制零行数：`21936`。
- 小阶方阵头部/尾镜像命中数：`21936`。
- 未闭合行数：`0`。
- 命中比例：`1.0`。
- 最大首次命中下降层数：`91`。
- 最小命中素数：`3`。
- 末行端点穿孔行数：`93`。
- 命中模式计数：`{'direct_head_phase': 29065, 'tail_mirror_phase': 13357}`。
- 命中素数分布摘录：`{3: 6, 5: 283, 7: 4751, 11: 1144, 13: 104, 17: 8, 19: 13, 23: 25, 29: 20, 31: 27, 37: 24, 41: 25, 43: 40, 47: 48, 53: 52, 59: 41, 61: 55, 67: 49, 71: 53, 73: 68, '...': '完整分布见 JSON'}`。

## 命中样本

| p | q | q-row | initial | terminal puncture | hit h | hit profiles |
|---:|---:|---:|---|---|---:|---|
| 5 | 7 | 2 | `seam_window` | `[]` | 3 | `[{'row': 4, 'h': 3, 'period_rows': 2, 'phase': 2, 'mirror_phase': 1, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}]` |
| 5 | 7 | 3 | `aligned_p_row_contained` | `[]` | 5 | `[{'row': 4, 'h': 5, 'period_rows': 6, 'phase': 4, 'mirror_phase': 3, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 3}]` |
| 5 | 7 | 4 | `seam_window` | `[]` | 3 | `[{'row': 8, 'h': 3, 'period_rows': 2, 'phase': 2, 'mirror_phase': 1, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}]` |
| 5 | 7 | 5 | `aligned_p_row_contained` | `[]` | 5 | `[{'row': 7, 'h': 5, 'period_rows': 6, 'phase': 1, 'mirror_phase': 6, 'direct_head_hit': True, 'mirror_head_hit': False, 'head_or_tail_hit': True, 'tail_distance': 6}]` |
| 5 | 7 | 6 | `aligned_p_row_contained` | `[]` | 5 | `[{'row': 8, 'h': 5, 'period_rows': 6, 'phase': 2, 'mirror_phase': 5, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 5}]` |
| 5 | 7 | 7 | `seam_window` | `[49]` | 3 | `[{'row': 15, 'h': 3, 'period_rows': 2, 'phase': 1, 'mirror_phase': 2, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 2}, {'row': 16, 'h': 3, 'period_rows': 2, 'phase': 2, 'mirror_phase': 1, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}]` |
| 7 | 11 | 2 | `aligned_p_row_contained` | `[]` | 7 | `[{'row': 3, 'h': 7, 'period_rows': 30, 'phase': 3, 'mirror_phase': 28, 'direct_head_hit': True, 'mirror_head_hit': False, 'head_or_tail_hit': True, 'tail_distance': 28}]` |
| 7 | 11 | 3 | `seam_window` | `[]` | 5 | `[{'row': 6, 'h': 5, 'period_rows': 6, 'phase': 6, 'mirror_phase': 1, 'direct_head_hit': False, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}]` |
| 7 | 11 | 4 | `aligned_p_row_contained` | `[]` | 7 | `[{'row': 6, 'h': 7, 'period_rows': 30, 'phase': 6, 'mirror_phase': 25, 'direct_head_hit': True, 'mirror_head_hit': False, 'head_or_tail_hit': True, 'tail_distance': 25}]` |
| 7 | 11 | 5 | `seam_window` | `[]` | 5 | `[{'row': 11, 'h': 5, 'period_rows': 6, 'phase': 5, 'mirror_phase': 2, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 2}]` |
| 7 | 11 | 6 | `aligned_p_row_contained` | `[]` | 5 | `[{'row': 12, 'h': 5, 'period_rows': 6, 'phase': 6, 'mirror_phase': 1, 'direct_head_hit': False, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}, {'row': 13, 'h': 5, 'period_rows': 6, 'phase': 1, 'mirror_phase': 6, 'direct_head_hit': True, 'mirror_head_hit': False, 'head_or_tail_hit': True, 'tail_distance': 6}]` |
| 7 | 11 | 7 | `aligned_p_row_contained` | `[]` | 5 | `[{'row': 15, 'h': 5, 'period_rows': 6, 'phase': 3, 'mirror_phase': 4, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 4}]` |

## 未闭合样本

| p | q | q-row | initial | terminal puncture | first forced | last level |
|---:|---:|---:|---|---|---|---|

## 审稿解释

统一模型使用三个严格输入：

1. 相邻壳层单点性：`q^2` 内旧 `p`-筛唯一合数幸存者是 `q^2`；
2. 剥层复活恒等式：降到 `h<=p` 后复活点为 `P^-(n)∈(h,p]` 的点，另加末行 `q^2`；
3. CRT 头尾镜像：强制 `h` 零行行相位 `rho` 或镜像相位 `N_h-rho+1` 落入 `1..h` 时，得到 `h×h` 方阵内条件零行。

因此若归纳已知所有小阶 `Row(h)`，任何命中记录都排斥对应高阶 q 零行。

本账本支持用户的总路线：在测试域内，不管初始是 aligned 还是 seam，也不管是否末行带 `q^2` 穿孔，全部假想高阶零行都被压到某个小阶方阵零行。

但全局论文仍需证明 `TotalDescent-TM`：上述命中机制对所有素数和所有行相位成立；或者证明非命中相位集合必触发 `SAE/PDEC/ColumnCRT`。有限账本不能替代这个全局不等式。
