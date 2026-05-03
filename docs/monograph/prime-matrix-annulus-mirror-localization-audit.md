# 环带零行与 CRT 镜像落点审计

**状态：** `annulus_mirror_does_not_force_smaller_matrix_zero_row`

## 总结

- 相邻素数对数量：`9`。
- `p^2` 内未被 `Row(p)` 排除的 q 缝合行数：`97`。
- 穿过或落入 `(p^2,q^2)` 环带的 q 行数：`60`。
- 环带行的 CRT 零镜像行号落入更小方阵早期行次数：`45`。
- 上述落点实际成为更小方阵零行次数：`0`。

## 关键区分

1. `Row(p)` 只排除完整 `p` 对齐零行；它不排除 `p^2` 内跨两条 p 行的 q 缝合零窗。
2. 保持小素数零同余覆盖的镜像是 `n -> -n mod M_p`。在固定 q 行宽下，行号变为 `r -> M_p-r+1`，这是 CRT 周期尾部，不是早期小方阵。
3. `n -> q^2-n` 的确把环带映到早期小区间，但覆盖条件变成 `q^2 mod ell` 的非零类；它是终端镜像非零类问题，不是零行问题。

## 样本表

| p | q | core seam rows | annulus rows | row-number hits | actual zero hits | first annulus row record |
|---:|---:|---:|---:|---:|---|
| 5 | 7 | 1 | 4 | 3 | 0 | `{'row': 4, 'type': 'seam_window', 'interval': (22, 27), 'relation': 'crosses_p_square_boundary', 'crt_tail_distance': 3, 'terminal_reflection_interval': [22, 27], 'row_number_hits': 1, 'actual_zero_hits': 0}` |
| 7 | 11 | 1 | 7 | 5 | 0 | `{'row': 5, 'type': 'seam_window', 'interval': (45, 54), 'relation': 'crosses_p_square_boundary', 'crt_tail_distance': 4, 'terminal_reflection_interval': [67, 76], 'row_number_hits': 2, 'actual_zero_hits': 0}` |
| 11 | 13 | 7 | 4 | 3 | 0 | `{'row': 10, 'type': 'seam_window', 'interval': (118, 129), 'relation': 'crosses_p_square_boundary', 'crt_tail_distance': 9, 'terminal_reflection_interval': [40, 51], 'row_number_hits': 1, 'actual_zero_hits': 0}` |
| 13 | 17 | 6 | 7 | 5 | 0 | `{'row': 11, 'type': 'seam_window', 'interval': (171, 186), 'relation': 'wholly_annulus', 'crt_tail_distance': 10, 'terminal_reflection_interval': [103, 118], 'row_number_hits': 2, 'actual_zero_hits': 0}` |
| 17 | 19 | 13 | 4 | 3 | 0 | `{'row': 16, 'type': 'seam_window', 'interval': (286, 303), 'relation': 'crosses_p_square_boundary', 'crt_tail_distance': 15, 'terminal_reflection_interval': [58, 75], 'row_number_hits': 1, 'actual_zero_hits': 0}` |
| 19 | 23 | 11 | 8 | 6 | 0 | `{'row': 16, 'type': 'seam_window', 'interval': (346, 367), 'relation': 'crosses_p_square_boundary', 'crt_tail_distance': 15, 'terminal_reflection_interval': [162, 183], 'row_number_hits': 1, 'actual_zero_hits': 0}` |
| 23 | 29 | 13 | 11 | 9 | 0 | `{'row': 19, 'type': 'seam_window', 'interval': (523, 550), 'relation': 'crosses_p_square_boundary', 'crt_tail_distance': 18, 'terminal_reflection_interval': [291, 318], 'row_number_hits': 1, 'actual_zero_hits': 0}` |
| 29 | 31 | 25 | 4 | 3 | 0 | `{'row': 28, 'type': 'seam_window', 'interval': (838, 867), 'relation': 'crosses_p_square_boundary', 'crt_tail_distance': 27, 'terminal_reflection_interval': [94, 123], 'row_number_hits': 2, 'actual_zero_hits': 0}` |
| 31 | 37 | 20 | 11 | 8 | 0 | `{'row': 27, 'type': 'seam_window', 'interval': (963, 998), 'relation': 'wholly_annulus', 'crt_tail_distance': 26, 'terminal_reflection_interval': [371, 406], 'row_number_hits': 2, 'actual_zero_hits': 0}` |

## 可保留方向

这条想法的有效部分应改写为：

```text
q 方阵零行
=> direct 完整 p 行支 或 seam 缝合支
=> direct 支由 Row(p) 排除
=> seam/terminal 支转入 q^2-n 非零类终端镜像块
=> PDEC / SAE / 端点 CRT 缺陷。
```

不能写成“环带零行经镜像成为更小素数方阵零行”。
