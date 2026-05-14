# Prime Matrix square-phase low-alpha z=61 负行列式 actual/expected 分裂

**状态：** `z61_negative_cross_determinant_split_to_actual_expected_hit_scale_open`

负 profile 交叉行列式的纯模型项完全抵消，剩余只由实际命中和模型均值之间的升阶尺度漂移决定。样本中公共模型尺度为 `mu4/mu3≈2.049869`；`10007` 的实际命中尺度低于模型约 8.72%，`36739` 的实际命中尺度高于模型约 1.53%。因此下一步最窄硬点是证明这种相反尺度漂移受控，或把持续漂移登记为 HitSupport-PDEC。

```text
model_scale_high_over_low=2.049869
exit_actual_scale_high_over_low=1.871028
reciprocal_actual_scale_high_over_low=2.081312
exit_actual_scale_drift_from_model=-0.087245
reciprocal_actual_scale_drift_from_model=0.015339
cross_determinant=0.131097
actual_expected_split_error=0.000000
actual_expected_split_identity_closed=true
row_column_unconditional_closed=false
```

## 1. 四个 profile

| p | omega | value count | actual | expected | deficit | nonzero share | actual/expected |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10007 | 3 | 777 | 0.208600 | 0.959498 | 0.750899 | 0.001287 | 0.217405 |
| 10007 | 4 | 777 | 0.390296 | 1.966845 | 1.576550 | 0.002574 | 0.198437 |
| 36739 | 3 | 4013 | 3.926674 | 4.955555 | 1.028881 | 0.004984 | 0.792378 |
| 36739 | 4 | 4013 | 8.172635 | 10.158237 | 1.985602 | 0.007725 | 0.804533 |

## 2. 行列式三项分裂

纯模型项在交叉行列式中抵消，只剩两个 actual-vs-model 项和一个 actual 交叉修正项。

| component | value | normalized | share of determinant |
| --- | ---: | ---: | ---: |
| `reciprocal_actual_against_common_model` | 0.118469 | 0.057989 | 0.903675 |
| `exit_actual_against_common_model` | 0.184873 | 0.090493 | 1.410201 |
| `actual_cross_correction` | -0.172245 | -0.084312 | -1.313876 |

## 3. 证明边界

- 已闭合：交叉行列式到 actual/expected 命中尺度漂移的精确分裂。
- 未闭合：实际命中尺度漂移的全局上界，或 HitSupport-PDEC 排斥。
- 下一目标：`ActualHitScaleDriftBoundOrHitSupportPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-negative-cross-determinant-router.json` | `1a2d3c66cfd86f2eb0e6f5af785d285471f1d9383b347046fecfb665aa879ec9` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_negative_determinant_actual_expected_router.py` | `be0974dff3e258efbcb6dc330d6f227c8339460988989f78919a2b754ff169a7` |
