# Prime Matrix square-phase low-alpha 第一锚区间路由

**状态：** `lowalpha_first_anchor_intervalized_prime_composite_split_open`

第一锚分解已进一步区间化：每个 low-alpha 命中唯一写成 `P^2+k=q*a*n`，其中 `a=P^-(m)>z`，`n=m/a` 落入长度约 `P/(qa)` 的短区间。`n=1` 正是素互补因子，回到 RFP/Selberg 分布线；`n>1` 时 `n` 自动为 `a`-rough，因子深度严格下降。

```text
first_anchor_interval_formula_closed=true
residual_lower_depth_identity_closed=true
anchor_primality_checked=true
prime_anchor_return_to_rfp_closed=true
composite_anchor_load_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 全局分裂

| total hits | prime anchor | composite anchor | prime share | composite share |
| ---: | ---: | ---: | ---: | ---: |
| 21504 | 9044 | 12460 | 0.420573 | 0.579427 |

## 2. 最坏 low-alpha 块

| P | block | hits | prime | composite | active pairs | active density | top pair | top pair hits | top bucket |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| 200003 | `(31,62]` | 4540 | 1456 | 3084 | 3131 | 0.236680 | `37:37` | 24 | `A24:(16777216z,33554432z]` |

## 3. 每个 P 的总结

| P | low blocks | total hits | prime | composite | worst block | worst top pair |
| ---: | ---: | ---: | ---: | ---: | --- | --- |
| 10007 | 2 | 412 | 200 | 212 | `(31,62]` | `37:83` |
| 36739 | 3 | 2040 | 915 | 1125 | `(31,62]` | `37:43` |
| 83561 | 4 | 5659 | 2551 | 3108 | `(31,62]` | `37:41` |
| 200003 | 4 | 13393 | 5378 | 8015 | `(31,62]` | `37:37` |

## 4. 证明边界

- 已闭合：第一锚短区间公式、anchor 素性、residual `a`-rough 降深。
- 素互补分支：`n=1` 已严格回流 `PrimeAnchorRFPOrSelbergDistributionLedger`。
- 复合分支：剩余为 `CompositeFirstAnchorIntervalLoadBoundOrPDEC`，失败必须表现为第一锚 PDEC。
- 递归分支：`n>1` 时继续进入 `ResidualLowerDepthBuchstabCofactorLoadBoundOrPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-cofactor-depth-regime-router.json` | `c79c5f204c4b9690ec75a2238198f0af6af82746c4583e64483fe8f6c737d3a0` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-buchstab-anchor-decomposition.json` | `8075bf13712f96e2ff3d13a5f6cf317dbdd2362c2a1a19a40659d4b5521dc41f` |
| `experiments/prime_matrix_square_phase_lowalpha_first_anchor_interval_router.py` | `6fcc60e8d5546df7310f7be4db5aade7656a81aceca85ca96499ef6826b828c3` |
