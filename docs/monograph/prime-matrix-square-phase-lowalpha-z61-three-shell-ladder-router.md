# Prime Matrix square-phase low-alpha z=61 三壳层阶梯

**状态：** `z61_unique_cover_reduced_to_three_shell_ladder_open`

唯一五格覆盖可重写为三壳层阶梯：`(2D,4D]`、`(4D,8D]`、`(8D,16D]`。低中两壳给出 base credit，但仍不足；高壳 `--++` 包正好补足缺口。因此下一步可证明三壳层阶梯支撑不变量，或登记 Shell-PDEC。

```text
unbalanced_residual_needed_ratio=0.037200
base_shell_credit_ratio=0.027481
deficit_after_base_shells_ratio=0.009719
high_shell_credit_ratio=0.011029
high_shell_covers_base_deficit=true
three_shell_ladder_covers_need=true
three_shell_ladder_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 壳层阶梯

| shell | credit | share/need | cumulative | deficit after cumulative | cells |
| --- | ---: | ---: | ---: | ---: | ---: |
| `(2D,4D]` | 0.018748 | 0.503996 | 0.018748 | 0.018451 | 2 |
| `(4D,8D]` | 0.008732 | 0.234743 | 0.027481 | 0.009719 | 1 |
| `(8D,16D]` | 0.011029 | 0.296470 | 0.038509 | 0.000000 | 2 |

## 2. 壳内 pair

| shell | pair | credit | share/shell |
| --- | --- | ---: | ---: |
| `(2D,4D]` | `36739->200003` | 0.011492 | 0.612947 |
| `(2D,4D]` | `200003->36739` | 0.007257 | 0.387053 |
| `(4D,8D]` | `36739->200003` | 0.008732 | 1.000000 |
| `(8D,16D]` | `200003->36739` | 0.006264 | 0.567991 |
| `(8D,16D]` | `200003->10007` | 0.004764 | 0.432009 |

## 3. 证明边界

- 已闭合：唯一五格覆盖到三壳层阶梯的分解账本。
- 未闭合：证明低中壳 base 与高壳补项的阶梯支撑不变量，或登记 Shell-PDEC。
- 下一目标：`ThreeShellLadderSupportInvariantOrShellPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.json` | `a2d7e3fe1691bc189ae503661c6ea63f7ca97c746734711b69841ef24cc82d22` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-two-arm-internal-structure-router.json` | `f378c02abbb5e220763fc819472c93fd7e537f34edb39c4e349267ede55146bd` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_three_shell_ladder_router.py` | `ec14b112b775fb2474f260b0eda53c640caf83ffa925696b22e824d5298cf7a4` |
