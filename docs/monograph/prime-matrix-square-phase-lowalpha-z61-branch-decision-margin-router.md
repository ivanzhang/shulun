# Prime Matrix square-phase low-alpha z=61 branch decision margin

**状态：** `z61_branch_decision_ledger_reduced_to_positive_margin_stability_open`

分支决策账本可升级为正余量账本：每个 interval-empty 分支有显式区间间隙，每个 residue-empty 分支有到目标余类集合的正环距离。当前 formal unit 的最小被拒分支余量为 55，最小选中分支非命中余量也为 55；两个 interval-empty 分支间隙分别为 645743 与 7723。于是本地唯一路径在小扰动下稳定。全局剩余变成证明这些正余量模式在一般 formal unit 中保持，或把余量塌缩登记为 Margin-PDEC。

```text
branch_decision_margin_group_count=1
all_steps_have_positive_rejected_margins=true
minimum_rejected_branch_margin=55
minimum_selected_nonhit_residue_margin=55
global_branch_decision_margin_stability_proved=false
row_column_unconditional_closed=false
```

## 1. 余量摘要

| step | coeff | selected | prefix | rejected min margin | selected nonhit margin | closed |
| ---: | ---: | --- | --- | ---: | ---: | --- |
| 1 | 382536 | `+` | `+` | 645743 | 55 | true |
| 2 | 36708 | `+` | `++` | 162 | 55 | true |
| 3 | 14421 | `-` | `++-` | 55 | 364 | true |
| 4 | 19228 | `-` | `++--` | 7723 | 364 | true |
| 5 | 12540 | `-` | `++---` | 364 | None | true |

## 2. 分支余量

| step | sign | selected | status | mode | interval gap | interval candidates | hits | margin | stability radius |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | `+` | true | `survives` | `selected_unique_hit` |  | 7 | 1 | 55 | 27 |
| 1 | `-` | false | `interval_empty` | `interval_gap` | 645743 | 0 | 0 | 645743 | 322871 |
| 2 | `+` | true | `survives` | `selected_unique_hit` |  | 3 | 1 | 55 | 27 |
| 2 | `-` | false | `residue_empty` | `residue_gap` |  | 4 | 0 | 162 | 80 |
| 3 | `+` | false | `residue_empty` | `residue_gap` |  | 1 | 0 | 55 | 27 |
| 3 | `-` | true | `survives` | `selected_unique_hit` |  | 2 | 1 | 364 | 181 |
| 4 | `+` | false | `interval_empty` | `interval_gap` | 7723 | 0 | 0 | 7723 | 3861 |
| 4 | `-` | true | `survives` | `selected_unique_hit` |  | 2 | 1 | 364 | 181 |
| 5 | `+` | false | `residue_empty` | `residue_gap` |  | 1 | 0 | 364 | 181 |
| 5 | `-` | true | `survives` | `selected_unique_hit` |  | 1 | 1 |  |  |

## 3. 最近同余距离

| step | sign | candidate | sum mod 2627 | nearest target | distance |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | `+` | `++--` | 972 | 1027 | 55 |
| 1 | `+` | `+--+` | 2464 | 2100 | 364 |
| 1 | `+` | `-+++` | 1600 | 1879 | 279 |
| 1 | `+` | `-++-` | 163 | 325 | 162 |
| 1 | `+` | `-+-+` | 2549 | 325 | 403 |
| 1 | `+` | `--++` | 1655 | 1879 | 224 |
| 2 | `+` | `+--` | 1042 | 1097 | 55 |
| 2 | `+` | `--+` | 2534 | 2170 | 364 |
| 2 | `-` | `+++` | 1530 | 1809 | 279 |
| 2 | `-` | `++-` | 93 | 255 | 162 |
| 2 | `-` | `+-+` | 2479 | 255 | 403 |
| 2 | `-` | `-++` | 1585 | 1809 | 224 |
| 3 | `+` | `--` | 2383 | 2438 | 55 |
| 3 | `-` | `-+` | 1193 | 829 | 364 |
| 4 | `-` | `+` | 2032 | 1668 | 364 |
| 5 | `+` | `` | 0 | 2263 | 364 |

## 4. 自足小引理

分支排除有两个可验收余量：

```text
interval margin = dist([L,H), [-R,R]);
residue margin  = min circular distance from interval candidates to target residues.
```

若 interval margin 为正，则足够小的区间端点扰动不会产生候选。若 residue margin 为正，则足够小的余类扰动不会把非命中候选推入目标集。因此正余量账本是 BranchDecision 模式全局化的精确输入基。

## 5. 证明边界

- 已闭合：当前 z=61 formal unit 的所有被拒分支都有正余量；选中分支的非命中候选也有正余量。
- 未闭合：全局证明这些余量不塌缩，或把余量塌缩登记为 Margin-PDEC。
- 下一目标：`BranchDecisionMarginStabilityGlobalBoundOrMarginPDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-branch-decision-ledger-router.json` | `727ffcb802fd6a005bb546bd7708d1fafafe332f96a703cfcfb65753714d8d28` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_branch_decision_margin_router.py` | `5fb0f4d46812217c50931507b3872b1698b1593a3b3a51e1c7e968a81f620547` |
