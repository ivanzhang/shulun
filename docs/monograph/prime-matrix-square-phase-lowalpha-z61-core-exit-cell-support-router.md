# Prime Matrix square-phase low-alpha z=61 核心出口格支撑

**状态：** `z61_unbalanced_core_exit_reduced_to_five_support_cells_open`

互反核心加出口的 pair 信用可按格支撑合并。总共有 6 个支撑格；去掉最小的 `omega=4,(4D,8D],--++` 后，剩余 5 个格仍覆盖 `unbalanced<=8` 残量。下一步只需证明这 5 个格支撑的不变量，或登记 CellExit-PDEC。

```text
unbalanced_residual_needed_ratio=0.037200
core_plus_exit_credit_ratio=0.039379
all_core_exit_cell_count=6
cover_cell_count=5
cover_credit_ratio=0.038509
cover_surplus_ratio=0.001310
sample_five_cells_cover_unbalanced_residual=true
cell_support_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 覆盖格

| omega | shell | signs | credit | cumulative | pairs | profile vector |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 3 | `(2D,4D]` | `-++-` | 0.011492 | 0.011492 | `36739->200003:0.011492` | `10007:-2.193242, 36739:2.714492, 83561:6.893740, 200003:-6.796502` |
| 5 | `(4D,8D]` | `-+--` | 0.008732 | 0.020224 | `36739->200003:0.008732` | `10007:-0.184853, 36739:1.985946, 83561:-1.267369, 200003:-4.021515` |
| 5 | `(2D,4D]` | `+-++` | 0.007257 | 0.027481 | `200003->36739:0.007257` | `10007:0.226569, 36739:-2.537867, 83561:1.807935, 200003:1.861220` |
| 3 | `(8D,16D]` | `--++` | 0.005640 | 0.033120 | `200003->10007:0.002379, 200003->36739:0.003260` | `10007:-0.750899, 36739:-1.028881, 83561:3.102292, 200003:3.490612` |
| 4 | `(8D,16D]` | `--++` | 0.005389 | 0.038509 | `200003->10007:0.002385, 200003->36739:0.003004` | `10007:-1.576550, 36739:-1.985602, 83561:7.257244, 200003:2.455029` |

## 2. 省略格

| omega | shell | signs | credit | pairs |
| ---: | --- | --- | ---: | --- |
| 4 | `(4D,8D]` | `--++` | 0.000870 | `200003->10007:0.000426, 200003->36739:0.000443` |

## 3. cover 分组

| group | value | credit |
| --- | --- | ---: |
| sign word | `-++-` | 0.011492 |
| sign word | `--++` | 0.011029 |
| sign word | `-+--` | 0.008732 |
| sign word | `+-++` | 0.007257 |
| omega | `3` | 0.017131 |
| omega | `5` | 0.015989 |
| omega | `4` | 0.005389 |

## 4. 证明边界

- 已闭合：核心出口 pair 信用到 5 个覆盖格的压缩账本。
- 未闭合：证明这 5 个格的支撑不变量，或登记 CellExit-PDEC。
- 下一目标：`FiveCoreExitCellSupportInvariantOrCellExitPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-nonprincipal-secondary-extractor-router.json` | `130e8563d7e67db0a68c9312fc628f9f68415094d5e4c12f5116aec144aa1bae` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-unbalanced-reciprocal-core-exit-router.json` | `ae39bd2ffb9128a0ff92f838531db59bbf8d62a4e2d99bb3873c4e4481199163` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_core_exit_cell_support_router.py` | `52725de9908e733eee0949d3c5aa19436c308925cf9c16ac4c7c94fc8a3b9486` |
