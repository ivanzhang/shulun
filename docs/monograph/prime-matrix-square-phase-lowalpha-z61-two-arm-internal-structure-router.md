# Prime Matrix square-phase low-alpha z=61 双臂内部结构

**状态：** `z61_two_arm_cover_split_into_single_target_and_exit_arm_open`

双臂覆盖内部结构进一步分裂：`36739` 臂是单靶向臂，全部指向 `200003`；`200003` 臂是互反加出口臂，主要指向 `36739`，另有出口指向 `10007`。因此下一步可证明单靶向臂与出口臂的组合不变量，或登记 ArmStructure-PDEC。

```text
arm_count=2
single_target_arm_count=1
exit_arm_count=1
single_target_plus_exit_arm_schema_materialized=true
single_target_arm_and_exit_arm_invariant_proved=false
row_column_unconditional_closed=false
```

## 1. 臂画像

| positive P | credit | targets | pairs | single target | has exit |
| ---: | ---: | ---: | ---: | --- | --- |
| 36739 | 0.020224 | 1 | 1 | true | false |
| 200003 | 0.018285 | 2 | 2 | false | true |

## 2. pair / target 明细

| positive P | kind | key | credit | share of arm |
| ---: | --- | --- | ---: | ---: |
| 36739 | pair | `36739->200003` | 0.020224 | 1.000000 |
| 36739 | target | `200003` | 0.020224 | 1.000000 |
| 200003 | pair | `200003->36739` | 0.013521 | 0.739437 |
| 200003 | pair | `200003->10007` | 0.004764 | 0.260563 |
| 200003 | target | `36739` | 0.013521 | 0.739437 |
| 200003 | target | `10007` | 0.004764 | 0.260563 |

## 3. 证明边界

- 已闭合：双臂覆盖的内部 pair/target 结构账本。
- 未闭合：证明单靶向臂与出口臂组合不变量，或登记 ArmStructure-PDEC。
- 下一目标：`SingleTargetArmAndReciprocalExitArmInvariantOrArmStructurePDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-unique-cover-two-arm-balance-router.json` | `cdb93b7dd20cedec769bda292c7aa21758c72da81554168a7fde3038ffc67a60` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_two_arm_internal_structure_router.py` | `341798441a841b347f74877aad48780f97990cf205403ce824c2c9f9ced49f70` |
