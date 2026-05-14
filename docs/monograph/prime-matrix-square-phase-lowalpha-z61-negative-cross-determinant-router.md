# Prime Matrix square-phase low-alpha z=61 负 profile 交叉行列式

**状态：** `z61_negative_profile_ratio_band_reduced_to_two_by_two_cross_determinant_open`

两个高壳负 profile 比例带已等价改写为一个 2x2 交叉行列式界：`ratio_spread=(a4*b3-a3*b4)/(b3*b4)`，其中 `a=|L_10007|`、`b=|L_36739|`。样本中 `a` 的 omega 升阶尺度只比 `b` 的尺度高约 8.79%，因此下一步最窄硬点是证明该交叉行列式/尺度失配有全局上界，或把持续失配登记为 Determinant-PDEC。

```text
low_omega=3
high_omega=4
low_negative_ratio=0.729821
high_negative_ratio=0.793991
ratio_spread=0.064170
cross_determinant=0.131097
normalized_cross_determinant=0.064170
determinant_identity_error=-0.000000
exit_abs_scale_high_over_low=2.099550
reciprocal_abs_scale_high_over_low=1.929865
relative_scale_gap=0.087926
negative_cross_determinant_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 等价式

令 `a_i=|L_10007(omega=i)|`，`b_i=|L_36739(omega=i)|`。两个比例的带宽满足：

```text
a_4/b_4 - a_3/b_3 = (a_4*b_3 - a_3*b_4)/(b_3*b_4)
```

因此证明比例带宽小，等价于证明 `a` 相对 `b` 的升阶尺度没有产生大交叉行列式。

## 2. 证明边界

- 已闭合：比例带到账本 2x2 交叉行列式的精确等价。
- 未闭合：交叉行列式全局上界，或 Determinant-PDEC 排斥。
- 下一目标：`NegativeProfileTwoOmegaCrossDeterminantBoundOrDeterminantPDEC`。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-high-shell-negative-ratio-router.json` | `d625ffbf82381273b31a2bd7629b69f929c4f30e81ce237ab3bdd0a225af18b1` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_negative_cross_determinant_router.py` | `2e3a9c4ed826d35ec256087cc9cee47ae5632d6b2ac34af1ae6677e59b1623e0` |
