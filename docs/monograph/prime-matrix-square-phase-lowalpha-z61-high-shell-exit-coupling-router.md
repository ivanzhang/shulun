# Prime Matrix square-phase low-alpha z=61 高壳互反出口耦合

**状态：** `z61_high_shell_booster_split_to_reciprocal_exit_coupling_open`

高壳补项 `(8D,16D]` 全部来自 `200003` 正向来源，并分成互反项 `200003->36739` 与出口项 `200003->10007`。低中壳加高壳互反项仍不足；高壳出口项正好补齐该缺口。下一步应证明高壳互反/出口耦合不变量，或登记 HighShell-PDEC。

```text
unbalanced_residual_needed_ratio=0.037200
base_shell_credit_ratio=0.027481
high_shell_reciprocal_credit_ratio=0.006264
high_shell_exit_credit_ratio=0.004764
exit_over_reciprocal_ratio=0.760593
deficit_after_base_plus_reciprocal_ratio=0.003455
exit_covers_reciprocal_deficit=true
base_plus_high_shell_surplus_ratio=0.001310
high_shell_exit_coupling_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 高壳 pair

| pair | credit | share/high shell | cells |
| --- | ---: | ---: | --- |
| `200003->36739` | 0.006264 | 0.567991 | `omega=3:0.003260, omega=4:0.003004` |
| `200003->10007` | 0.004764 | 0.432009 | `omega=3:0.002379, omega=4:0.002385` |

## 2. 证明边界

- 已闭合：高壳补项拆成互反项与出口项的账本。
- 未闭合：证明高壳互反/出口耦合下界，或登记 HighShell-PDEC。
- 下一目标：`HighShellReciprocalExitCouplingInvariantOrHighShellPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-three-shell-ladder-router.json` | `a0d8ebb013edca4206f1b044e7753e5513086e949cc7755c77ce5450d8ad9c70` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_high_shell_exit_coupling_router.py` | `410c9632c321c7ae0f78d28af387938bf8c5e90a83277e06b0477dfd50f152d9` |
