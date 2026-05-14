# Prime Matrix square-phase low-alpha z=61 核心出口最小覆盖

**状态：** `z61_core_exit_support_has_unique_five_cell_minimal_cover_open`

核心出口的 6 个支撑格中，覆盖 `unbalanced<=8` residual 的最小子集大小为 5，且最小覆盖唯一，正是上一层选中的五格。任意删除其中一格都会失去覆盖。因此下一步不能再靠选择策略压缩，只能证明这五格联合不变量，或登记 MinimalCover-PDEC。

```text
unbalanced_residual_needed_ratio=0.037200
candidate_cell_count=6
minimal_cover_size=5
minimal_cover_count=1
minimal_cover_unique=true
minimal_cover_matches_selected_cover=true
minimal_cover_credit_ratio=0.038509
minimal_cover_surplus_ratio=0.001310
all_minimal_cells_indispensable=true
unique_five_cell_joint_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 最小覆盖

| omega | shell | signs | credit | pairs |
| ---: | --- | --- | ---: | --- |
| 3 | `(2D,4D]` | `-++-` | 0.011492 | `36739->200003:0.011492` |
| 5 | `(4D,8D]` | `-+--` | 0.008732 | `36739->200003:0.008732` |
| 5 | `(2D,4D]` | `+-++` | 0.007257 | `200003->36739:0.007257` |
| 3 | `(8D,16D]` | `--++` | 0.005640 | `200003->10007:0.002379, 200003->36739:0.003260` |
| 4 | `(8D,16D]` | `--++` | 0.005389 | `200003->10007:0.002385, 200003->36739:0.003004` |

## 2. 删除测试

| removed cell | removed credit | remaining credit | remaining deficit | still covers |
| --- | ---: | ---: | ---: | --- |
| `omega=3|shell=(2D,4D]|sign=-++-` | 0.011492 | 0.027018 | 0.010182 | false |
| `omega=5|shell=(4D,8D]|sign=-+--` | 0.008732 | 0.029777 | 0.007423 | false |
| `omega=5|shell=(2D,4D]|sign=+-++` | 0.007257 | 0.031253 | 0.005947 | false |
| `omega=3|shell=(8D,16D]|sign=--++` | 0.005640 | 0.032870 | 0.004330 | false |
| `omega=4|shell=(8D,16D]|sign=--++` | 0.005389 | 0.033120 | 0.004079 | false |

## 3. 省略格

| cell | credit |
| --- | ---: |
| `omega=4|shell=(4D,8D]|sign=--++` | 0.000870 |

## 4. 证明边界

- 已闭合：6 个候选格的最小覆盖枚举。
- 未闭合：证明唯一五格联合支撑下界，或登记 MinimalCover-PDEC。
- 下一目标：`UniqueFiveCellJointInvariantOrMinimalCoverPDEC`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-cell-support-router.json` | `0912930626796d5c415b381e8bd837ffb4dca6d5380e77c6b816cd3377120336` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-odd-core-even-booster-router.json` | `aaa05a0e860dbcba1477a501924859af0896d4043c7912283803831f99c2bb71` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_core_exit_minimal_cover_router.py` | `0d6786d9d8463e7ef4cf6e425e605526758e0faffe2891a84568901747dc93f8` |
