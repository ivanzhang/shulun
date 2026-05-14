# Prime Matrix square-phase low-alpha z=61 高壳负 profile 比例路由

**状态：** `z61_high_shell_exit_reciprocal_ratio_equals_negative_profile_ratio_open`

高壳两个 `--++` 格中的出口/互反信用比并非新的自由比例，而是同一正来源 `200003` 向两个负 profile 端点输送信用时的目标负质量比：`|L_10007|/|L_36739|`。因此上一层比例带硬点被压成两个负 profile 质量比的稳定性问题；仍需证明该负 profile 比例带不变量，或登记 NegativeRatio-PDEC。

```text
cell_count=2
max_ratio_identity_error=0.000000
max_share_identity_error=0.000000
high_shell_negative_profile_ratio_identity_closed=true
min_negative_profile_ratio=0.729821
max_negative_profile_ratio=0.793991
negative_profile_ratio_spread=0.064170
negative_ratio_band_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 精确同一性

在同一正来源 `200003` 下，规范运输信用对目标负端点成比例，故每个高壳格满足：

```text
credit(200003->10007) / credit(200003->36739) = |L_10007| / |L_36739|
```

| omega | profile `[10007,36739,83561,200003]` | exit/reciprocal | negative ratio | error | pos 200003/83561 |
| ---: | --- | ---: | ---: | ---: | ---: |
| 3 | `[-0.750899, -1.028881, 3.102292, 3.490612]` | 0.729821 | 0.729821 | -0.000000 | 1.125172 |
| 4 | `[-1.576550, -1.985602, 7.257244, 2.455029]` | 0.793991 | 0.793991 | -0.000000 | 0.338287 |

## 2. 证明边界

- 已闭合：高壳出口/互反比例到账本负 profile 质量比的精确同一性。
- 未闭合：两个负 profile 质量比的全局稳定下界/上界，或 NegativeRatio-PDEC 排斥。
- 下一目标：`HighShellNegativeProfileRatioBandInvariantOrNegativeRatioPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-cell-ratio-router.json` | `51631a0ab4eb902d4ac4c2c167048e8553d803a14de6c9ca9f6d854726a0a748` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-profile-sign-pattern-router.json` | `f37d1d58c9c03c95badb956c102919ebd6a69db811139157393a1123f0a52d1b` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_high_shell_negative_ratio_router.py` | `c605db4e817f25b8dbdb6147253a27fd399a325a272a053a79bb1519c20a022d` |
