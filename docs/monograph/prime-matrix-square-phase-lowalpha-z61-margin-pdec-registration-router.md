# Prime Matrix square-phase low-alpha z=61 Margin-PDEC registration

**状态：** `z61_branch_margin_reduced_to_margin_pdec_atoms_open`

正余量账本的失败可完全物化为 Margin-PDEC 原子：interval-empty 分支若失败，就是区间端点撞入剩余 signed-sum 盒；residue-empty 分支若失败，就是某个候选余类撞上目标余类。当前 formal unit 共登记 18 个塌缩原子，其中 2 个区间塌缩、16 个同余塌缩；最小余量为 55。下一步只剩证明全局不发生这些余量塌缩，或排斥相应 Margin-PDEC。

```text
margin_pdec_registration_closed=true
margin_atom_count=18
interval_margin_atom_count=2
residue_margin_atom_count=16
minimum_registered_margin=55
global_no_margin_collapse_proved=false
row_column_unconditional_closed=false
```

## 1. 最近塌缩原子

| type | step | sign | selected | candidate | target | offset | margin |
| --- | ---: | --- | --- | --- | ---: | ---: | ---: |
| `ResidueMarginCollapse` | 1 | `+` | true | `++--` | 1027 | -55 | 55 |
| `ResidueMarginCollapse` | 2 | `+` | true | `+--` | 1097 | -55 | 55 |
| `ResidueMarginCollapse` | 3 | `+` | false | `--` | 2438 | -55 | 55 |

## 2. 全部塌缩原子

| type | step | coeff | sign | status | candidate | sum mod | target | offset | margin |
| --- | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| `ResidueMarginCollapse` | 1 | 382536 | `+` | `survives` | `++--` | 972 | 1027 | -55 | 55 |
| `ResidueMarginCollapse` | 1 | 382536 | `+` | `survives` | `+--+` | 2464 | 2100 | 364 | 364 |
| `ResidueMarginCollapse` | 1 | 382536 | `+` | `survives` | `-+++` | 1600 | 1879 | -279 | 279 |
| `ResidueMarginCollapse` | 1 | 382536 | `+` | `survives` | `-++-` | 163 | 325 | -162 | 162 |
| `ResidueMarginCollapse` | 1 | 382536 | `+` | `survives` | `-+-+` | 2549 | 325 | -403 | 403 |
| `ResidueMarginCollapse` | 1 | 382536 | `+` | `survives` | `--++` | 1655 | 1879 | -224 | 224 |
| `IntervalMarginCollapse` | 1 | 382536 | `-` | `` | `` |  |  |  | 645743 |
| `ResidueMarginCollapse` | 2 | 36708 | `+` | `survives` | `+--` | 1042 | 1097 | -55 | 55 |
| `ResidueMarginCollapse` | 2 | 36708 | `+` | `survives` | `--+` | 2534 | 2170 | 364 | 364 |
| `ResidueMarginCollapse` | 2 | 36708 | `-` | `residue_empty` | `+++` | 1530 | 1809 | -279 | 279 |
| `ResidueMarginCollapse` | 2 | 36708 | `-` | `residue_empty` | `++-` | 93 | 255 | -162 | 162 |
| `ResidueMarginCollapse` | 2 | 36708 | `-` | `residue_empty` | `+-+` | 2479 | 255 | -403 | 403 |
| `ResidueMarginCollapse` | 2 | 36708 | `-` | `residue_empty` | `-++` | 1585 | 1809 | -224 | 224 |
| `ResidueMarginCollapse` | 3 | 14421 | `+` | `residue_empty` | `--` | 2383 | 2438 | -55 | 55 |
| `ResidueMarginCollapse` | 3 | 14421 | `-` | `survives` | `-+` | 1193 | 829 | 364 | 364 |
| `IntervalMarginCollapse` | 4 | 19228 | `+` | `` | `` |  |  |  | 7723 |
| `ResidueMarginCollapse` | 4 | 19228 | `-` | `survives` | `+` | 2032 | 1668 | 364 | 364 |
| `ResidueMarginCollapse` | 5 | 12540 | `+` | `residue_empty` | `` | 0 | 2263 | 364 | 364 |

## 3. 自足小引理

BranchDecision 的全局失败只可能来自两种塌缩：

```text
IntervalMarginCollapse: interval_gap 从正数降到 <=0；
ResidueMarginCollapse: candidate_sum_mod 与目标余类发生碰撞。
```

所以只要全局证明所有登记原子不塌缩，当前分支决策模式即可稳定；若任一塌缩发生，它本身就是显式 Margin-PDEC 证书对象。

## 4. 证明边界

- 已闭合：当前 z=61 formal unit 的余量失败对象已全部登记为具体原子。
- 未闭合：全局排斥这些 Margin-PDEC，或证明正余量模式全局保持。
- 下一目标：`GlobalNoMarginCollapseOrMarginPDECExclusion`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-margin-router.json` | `b0657f1f734480164be0235a26ccf8ddb8c49e9ad4c3af257b3ed0de0e1640ae` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_margin_pdec_registration_router.py` | `ce0daf2f4db3bc03371f59c4cbafb739b41c8419264e71ef8f4c15cb4002ad03` |
