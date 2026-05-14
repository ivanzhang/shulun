# Prime Matrix square-phase low-alpha z=61 高壳格比例带

**状态：** `z61_high_shell_exit_reciprocal_split_has_two_cell_ratio_band_open`

高壳出口项与互反项在两个 `--++` 高壳格中成对出现。两个格的出口/互反比例接近，形成窄比例带；因此下一步可证明两个高壳格的比例带不变量，或登记 Ratio-PDEC。

```text
cell_count=2
all_cells_are_high_shell_double_positive_template=true
min_exit_over_reciprocal_ratio=0.729821
max_exit_over_reciprocal_ratio=0.793991
exit_over_reciprocal_ratio_spread=0.064170
sample_ratio_band_width_below_point_10=true
aggregate_exit_over_reciprocal_ratio=0.760593
two_high_shell_ratio_band_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 高壳格

| omega | shell | signs | reciprocal | exit | exit/reciprocal | exit share |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 3 | `(8D,16D]` | `--++` | 0.003260 | 0.002379 | 0.729821 | 0.421905 |
| 4 | `(8D,16D]` | `--++` | 0.003004 | 0.002385 | 0.793991 | 0.442584 |

## 2. 证明边界

- 已闭合：高壳互反/出口项到两个高壳格比例带的账本。
- 未闭合：证明比例带不变量，或登记 Ratio-PDEC。
- 下一目标：`TwoHighShellCellExitReciprocalRatioBandInvariantOrRatioPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-exit-coupling-router.json` | `5cd55bc39d9c1f93a63b9ac45e15d5fb2f11b446125bd7533a3b68d0d8faa5a2` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_high_shell_cell_ratio_router.py` | `328af8decc3dfee730fb7ed8697bb495a7c8d0706f7557b811f3f9386107059c` |
