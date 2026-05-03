# Seam 尾镜像下降审计

**状态：** `finite_seam_tail_mirror_descent_audit_not_global_proof`

本文审计用户提出的加强路径：seam 降阶后得到的强制零行即使不直接落入小阶方阵，也可能在该小阶 CRT 周期尾边界；由零行镜像刚性，尾边界零行会映回头部方阵，从而得到小阶方阵零行。

## 参数

- `max_p`: `500`。
- `row_stride`: `1`。
- `max_levels`: `None`。

## 摘要

- 检查 seam 窗口数：`21339`。
- 出现条件强制零行数：`21339`。
- 周期头部或尾镜像命中数：`21339`。
- 未命中数：`0`。
- 命中比例：`1.0`。
- 最大首次命中下降层数：`91`。
- 最小命中素数：`3`。
- 命中模式计数：`{'direct_head_phase': 28279, 'tail_mirror_phase': 12984}`。
- 命中素数分布摘录：`{3: 4, 5: 249, 7: 4622, 11: 1112, 13: 99, 17: 7, 19: 10, 23: 21, 29: 19, 31: 22, 37: 21, 41: 24, 43: 37, 47: 43, 53: 47, 59: 40, 61: 50, 67: 46, 71: 52, 73: 63, '...': '完整分布见 JSON'}`。

## 命中样本

| p | q | q-row | seam guards | h | hit profiles |
|---:|---:|---:|---|---:|---|
| 5 | 7 | 2 | `[2, 1]` | 3 | `[{'row': 4, 'h': 3, 'period_rows': 2, 'phase': 2, 'mirror_phase': 1, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}]` |
| 5 | 7 | 4 | `[1, 2]` | 3 | `[{'row': 8, 'h': 3, 'period_rows': 2, 'phase': 2, 'mirror_phase': 1, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}]` |
| 5 | 7 | 7 | `[2, 1]` | 3 | `[{'row': 15, 'h': 3, 'period_rows': 2, 'phase': 1, 'mirror_phase': 2, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 2}, {'row': 16, 'h': 3, 'period_rows': 2, 'phase': 2, 'mirror_phase': 1, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}]` |
| 7 | 11 | 3 | `[1, 2]` | 5 | `[{'row': 6, 'h': 5, 'period_rows': 6, 'phase': 6, 'mirror_phase': 1, 'direct_head_hit': False, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}]` |
| 7 | 11 | 5 | `[2, 1]` | 5 | `[{'row': 11, 'h': 5, 'period_rows': 6, 'phase': 5, 'mirror_phase': 2, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 2}]` |
| 7 | 11 | 10 | `[1, 2]` | 5 | `[{'row': 21, 'h': 5, 'period_rows': 6, 'phase': 3, 'mirror_phase': 4, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 4}, {'row': 22, 'h': 5, 'period_rows': 6, 'phase': 4, 'mirror_phase': 3, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 3}]` |
| 11 | 13 | 2 | `[2, 7]` | 7 | `[{'row': 3, 'h': 7, 'period_rows': 30, 'phase': 3, 'mirror_phase': 28, 'direct_head_hit': True, 'mirror_head_hit': False, 'head_or_tail_hit': True, 'tail_distance': 28}]` |
| 11 | 13 | 3 | `[4, 5]` | 7 | `[{'row': 5, 'h': 7, 'period_rows': 30, 'phase': 5, 'mirror_phase': 26, 'direct_head_hit': True, 'mirror_head_hit': False, 'head_or_tail_hit': True, 'tail_distance': 26}]` |
| 11 | 13 | 4 | `[6, 3]` | 7 | `[{'row': 7, 'h': 7, 'period_rows': 30, 'phase': 7, 'mirror_phase': 24, 'direct_head_hit': True, 'mirror_head_hit': False, 'head_or_tail_hit': True, 'tail_distance': 24}]` |
| 11 | 13 | 5 | `[8, 1]` | 5 | `[{'row': 12, 'h': 5, 'period_rows': 6, 'phase': 6, 'mirror_phase': 1, 'direct_head_hit': False, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}, {'row': 13, 'h': 5, 'period_rows': 6, 'phase': 1, 'mirror_phase': 6, 'direct_head_hit': True, 'mirror_head_hit': False, 'head_or_tail_hit': True, 'tail_distance': 6}]` |
| 11 | 13 | 7 | `[1, 8]` | 5 | `[{'row': 17, 'h': 5, 'period_rows': 6, 'phase': 5, 'mirror_phase': 2, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 2}, {'row': 18, 'h': 5, 'period_rows': 6, 'phase': 6, 'mirror_phase': 1, 'direct_head_hit': False, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 1}]` |
| 11 | 13 | 8 | `[3, 6]` | 5 | `[{'row': 20, 'h': 5, 'period_rows': 6, 'phase': 2, 'mirror_phase': 5, 'direct_head_hit': True, 'mirror_head_hit': True, 'head_or_tail_hit': True, 'tail_distance': 5}]` |

## 未命中样本

| p | q | q-row | seam guards | first forced | last level |
|---:|---:|---:|---|---|---|

## 审稿解释

对 `h`-筛，令 `M_h=prod_{ell<=h}ell`、`N_h=M_h/h`。若第 `R` 条 `h` 对齐行是零行，则其行相位

```text
rho=((R-1) mod N_h)+1
```

也是零行相位。非平凡列的取负映射给出镜像相位 `rho*=N_h-rho+1`。若 `rho<=h`，则周期直接落入 `h×h` 方阵；若 `rho*<=h`，则尾边界零行经 CRT 镜像落入 `h×h` 方阵。

因此用户提出的路径是有效的严格接口：

```text
seam zero window
=> 多层下降产生条件 h-zero-row
=> 若 h-row phase 或 mirror phase <= h
=> 小阶 h×h 方阵条件零行
=> 与已知 Row(h) 或边界非零证书冲突。
```

但必须保留两个审稿边界：第一，该 h-zero-row 仍是在上层 seam 零窗假设下的条件结论；第二，若相位与镜像相位都不落入头部方阵，则仍需继续用 `SMD-Global Inequality` 或 `SAE/PDEC/ColumnCRT` 排除。
