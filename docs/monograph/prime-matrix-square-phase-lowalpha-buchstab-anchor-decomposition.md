# Prime Matrix square-phase low-alpha Buchstab 第一锚分解

**状态：** `lowalpha_buchstab_cofactor_load_reduced_to_first_anchor_layers_open`

low-alpha Buchstab cofactor 负载已按第一锚 `a=P^-(m)>z` 精确分解。每个命中互补因子 `m` 唯一进入某个 anchor dyadic 层，并留下更低深度残余 `m/a`。若某层负载异常重，就进入 first-anchor PDEC；否则剩余问题下降为更低深度的 Buchstab 负载。

```text
first_anchor_decomposition_checked=true
identity_failure_count=0
invalid_anchor_count=0
first_anchor_load_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 最坏 low-alpha 块

| P | block | alpha | hits | top anchor bucket | top count | residual depths | max residual depth |
| ---: | --- | ---: | ---: | --- | ---: | --- | ---: |
| 200003 | `(31,62]` | 0.281334 | 4540 | `A24:(16777216z,33554432z]` | 1187 | `{'1': 2198, '2': 792, '0': 1456, '3': 94}` | 3 |

## 2. 每个 P 的 low-alpha 总结

| P | low blocks | total hits | worst block | worst hits | top bucket | residual depths |
| ---: | ---: | ---: | --- | ---: | --- | --- |
| 10007 | 2 | 412 | `(31,62]` | 232 | `A16:(65536z,131072z]` | `{'1': 103, '2': 22, '0': 107}` |
| 36739 | 3 | 2040 | `(31,62]` | 831 | `A19:(524288z,1048576z]` | `{'1': 414, '0': 306, '2': 109, '3': 2}` |
| 83561 | 4 | 5659 | `(31,62]` | 1892 | `A22:(4194304z,8388608z]` | `{'2': 284, '1': 947, '0': 650, '3': 11}` |
| 200003 | 4 | 13393 | `(31,62]` | 4540 | `A24:(16777216z,33554432z]` | `{'1': 2198, '2': 792, '0': 1456, '3': 94}` |

## 3. 证明边界

- 已闭合：每个 low-alpha cofactor 命中唯一分解为第一锚层加 residual lower-depth cofactor。
- 未闭合：`LowAlphaFirstAnchorCofactorLoadBoundOrAnchorPDEC`，即第一锚层负载上界或其 PDEC 排斥。
- 并行：`ResidualLowerDepthBuchstabCofactorLoadBoundOrPDEC`，即 residual 深度下降后的递归负载账本。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-cofactor-depth-regime-router.json` | `c79c5f204c4b9690ec75a2238198f0af6af82746c4583e64483fe8f6c737d3a0` |
| `docs/monograph/prime-matrix-square-phase-dyadic-first-moment-cofactor-duality.json` | `071d009e1b6c5271a6957acabc4002f13b7be7e324a10e53bb804a6ddd1285de` |
| `experiments/prime_matrix_square_phase_lowalpha_buchstab_anchor_decomposition.py` | `3a9726c4e2269579aa63559cf2a8f461698162f2c1fe0843c7d6516541f0db89` |
