# Prime Matrix square-phase low-alpha z=61 carry-layer projection

**状态：** `z61_signed_crt_support_reduced_to_carry_layer_projection_open`

带 carry 的符号支撑可进一步按最小代表层 `c` 分解。当前 formal unit 的 32 个符号向量只落在 8 个 carry 层：`-9,-8,-7,-6,5,6,7,8`。所有 `37/71/2627` 目标投影命中都集中在 `carry=6` 的单个符号字 `--++-`，对应 `r=26951`。因此最新硬点是全局 carry-layer 目标纤维界，或登记 CarryProjection-PDEC。

```text
carry_layer_projection_group_count=1
all_carry_layer_projections_closed=true
carry_layer_target_fiber_global_bound_proved=false
row_column_unconditional_closed=false
```

## 1. Carry 分层摘要

| M | carry values | selected carry | selected sign | q4/q2 target hits | combined hits | closed |
| ---: | --- | ---: | --- | ---: | ---: | --- |
| 57684 | `[-9, -8, -7, -6, 5, 6, 7, 8]` | 6 | `--++-` | 1 | 1 | true |

## 2. Carry 层表

| carry | sign count | S min | S max | target hits | combined hits |
| ---: | ---: | ---: | ---: | --- | --- |
| -9 | 1 | -465433 | -465433 | `[]` | `[]` |
| -8 | 4 | -440353 | -411511 | `[]` | `[]` |
| -7 | 7 | -401897 | -353561 | `[]` | `[]` |
| -6 | 4 | -338095 | -299639 | `[]` | `[]` |
| 5 | 4 | 299639 | 338095 | `[]` | `[]` |
| 6 | 7 | 353561 | 401897 | `['--++-:26951']` | `['--++-:26951']` |
| 7 | 4 | 411511 | 440353 | `[]` | `[]` |
| 8 | 1 | 465433 | 465433 | `[]` | `[]` |

## 3. 自足小引理

对符号和 `S(sigma)` 定义最小代表 carry `c(sigma)` 为唯一整数，使

```text
0 <= S(sigma)-c(sigma)M < M.
```

则目标投影条件不是单独的 `S(sigma) mod ell` 条件，而是分层条件

```text
S(sigma)-cM in target classes mod ell.
```

所以每个 carry 层可以独立审计目标纤维。当前证书显示除 `c=6` 外所有层目标纤维为空，而 `c=6` 层也只有 `--++-` 一个目标命中。

## 4. 证明边界

- 已闭合：当前 z=61 formal unit 的 carry 分层目标纤维唯一命中 `--++- / r=26951`。
- 未闭合：全局 carry-layer 目标纤维容量界，或 CarryProjection-PDEC 排斥。
- 下一目标：`CarryLayerTargetFiberGlobalBoundOrCarryProjectionPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-projection-support-router.json` | `6f3e6110974e79d39e0a67c305741d1d06b4b21d1c8a1a4910ebaab92e52f9df` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_carry_layer_projection_router.py` | `5061aab64b4818eda451f76b8f1b33fceb9eb7c2f0c8dc7a06f9838cecaceef6` |
