# Prime Matrix square-phase low-alpha z=61 唯一覆盖双臂平衡

**状态：** `z61_unique_five_cell_cover_reduced_to_two_positive_source_arms_open`

唯一五格覆盖可按正向来源 P 压成两个平衡臂：`36739` 臂与 `200003` 臂。两臂都不能单独覆盖 residual，但贡献规模接近，合起来覆盖需求。下一步应证明这种双臂平衡是结构强制，或登记 Arm-PDEC。

```text
unbalanced_residual_needed_ratio=0.037200
unique_five_cell_cover_credit_ratio=0.038509
arm_count=2
two_arm_total_covers_need=true
each_arm_individually_insufficient=true
arm_credit_ratio_max_over_min=1.106038
arm_balance_materialized=true
two_arm_balance_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 双臂

| positive P | credit | share/need | share/cover | deficit if alone |
| ---: | ---: | ---: | ---: | ---: |
| 36739 | 0.020224 | 0.543665 | 0.525175 | 0.016975 |
| 200003 | 0.018285 | 0.491543 | 0.474825 | 0.018914 |

## 2. 臂内单元

| positive P | omega | shell | signs | pair | credit |
| ---: | ---: | --- | --- | --- | ---: |
| 36739 | 3 | `(2D,4D]` | `-++-` | `36739->200003` | 0.011492 |
| 36739 | 5 | `(4D,8D]` | `-+--` | `36739->200003` | 0.008732 |
| 200003 | 5 | `(2D,4D]` | `+-++` | `200003->36739` | 0.007257 |
| 200003 | 3 | `(8D,16D]` | `--++` | `200003->36739` | 0.003260 |
| 200003 | 4 | `(8D,16D]` | `--++` | `200003->36739` | 0.003004 |
| 200003 | 4 | `(8D,16D]` | `--++` | `200003->10007` | 0.002385 |
| 200003 | 3 | `(8D,16D]` | `--++` | `200003->10007` | 0.002379 |

## 3. 证明边界

- 已闭合：唯一五格覆盖到两个正向来源臂的分解账本。
- 未闭合：证明双臂平衡不变量，或登记 Arm-PDEC。
- 下一目标：`TwoArmPositiveSourceBalanceInvariantOrArmPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-core-exit-minimal-cover-router.json` | `a2d7e3fe1691bc189ae503661c6ea63f7ca97c746734711b69841ef24cc82d22` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_unique_cover_two_arm_balance_router.py` | `0b9fdbeb2ceaee6f5b5fe2506a8a4efb34bfd08a8e794a50d47ce0e51d6d354a` |
