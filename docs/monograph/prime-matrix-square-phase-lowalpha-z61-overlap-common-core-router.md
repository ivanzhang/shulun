# Prime Matrix square-phase low-alpha z=61 overlap common-core 路由

**状态：** `z61_single_double_hit_overlap_reduced_to_two_three_common_core_open`

唯一 double-hit overlap 已压成 `C=4807=11*19*23` 的 `2C/3C` common-core 原子：`9614=2C`、`14421=3C`、`b=28842=6C=lcm(2C,3C)`。在目标格中，`b` 只命中这两个模数；其贡献正是两个目标 bucket kernel 权重之和。下一步最窄硬点是证明这种 `2/3` common-core 原子不能持续超过允许容量，或把它登记为 CommonCore-PDEC。

```text
b_value=28842
common_core=4807
prefixes=[2, 3]
b_equals_lcm_of_hit_moduli=true
target_dividing_moduli_exactly_hit_moduli=true
kernel_edge_decomposition_closed=true
two_three_common_core_identity_closed=true
row_column_unconditional_closed=false
```

## 1. Common-Core 原子

| object | value | factorization |
| --- | ---: | --- |
| `C` | 4807 | `[11, 19, 23]` |
| `2C` | 9614 | `[2, 11, 19, 23]` |
| `3C` | 14421 | `[3, 11, 19, 23]` |
| `b` | 28842 | `[2, 3, 11, 19, 23]` |

## 2. 目标 bucket 边分解

| m | prefix | edge count | kernel | edge sum | identity error |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 9614 | 2 | 4 | 0.390406 | 0.390406 | -0.000000 |
| 14421 | 3 | 2 | 0.165021 | 0.165021 | 0.000000 |

## 3. 证明边界

- 已闭合：唯一 overlap 到 `2C/3C` common-core 原子的精确等价与边权分解。
- 未闭合：`2/3` common-core overlap 原子的全局容量界，或 CommonCore-PDEC 排斥。
- 下一目标：`TwoThreeCommonCoreOverlapAtomBoundOrCommonCorePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-hit-overlap-flip-router.json` | `ee5c1ebcec70df322e5c6df2c862ce7c43a7c6b0978df815cd8ae456920b31b5` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_overlap_common_core_router.py` | `9b8e4a5f967ab7b90b3105d7de475fe14a38dc15004ec9baa1d1b93b43d072b0` |
