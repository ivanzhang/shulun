# Prime Matrix square-phase low-alpha z=61 branch decision ledger

**状态：** `z61_terminal_sign_forcing_reduced_to_branch_decision_ledger_open`

当前 z=61 signed-sum 唯一路径可整理为 5 步分支决策账本。所选路径为 peel 坐标 `++---`，对应原 CRT 符号 `--++-`。所有兄弟分支均已分类为 interval-empty 或 residue-empty，末端空剩余和唯一命中确认没有隐藏第二路径。因此最新硬点是把这种分支决策模式提升为全局界，或登记 BranchDecision-PDEC。

```text
branch_decision_group_count=1
all_rejected_branches_closed=true
selected_path_unique=true
global_branch_decision_pattern_bound_proved=false
row_column_unconditional_closed=false
```

## 1. 决策摘要

| peel coefficients | selected peel sign | selected original sign | rejected statuses | closed |
| --- | --- | --- | --- | --- |
| `[382536, 36708, 14421, 19228, 12540]` | `++---` | `--++-` | `['interval_empty', 'residue_empty', 'residue_empty', 'interval_empty', 'residue_empty']` | true |

## 2. 分支账本

| step | coeff | selected | prefix | selected hits | rejected statuses |
| ---: | ---: | --- | --- | ---: | --- |
| 1 | 382536 | `+` | `+` | 1 | `['interval_empty']` |
| 2 | 36708 | `+` | `++` | 1 | `['residue_empty']` |
| 3 | 14421 | `-` | `++-` | 1 | `['residue_empty']` |
| 4 | 19228 | `-` | `++--` | 1 | `['interval_empty']` |
| 5 | 12540 | `-` | `++---` | 1 | `['residue_empty']` |

## 3. 被拒分支细节

| step | coeff | rejected sign | status | interval | rest abs | gap | interval candidates | hits |
| ---: | ---: | --- | --- | --- | ---: | --- | ---: | ---: |
| 1 | 382536 | `-` | `interval_empty` | `[728640,786324)` | 82897 | 645743 | 0 | 0 |
| 2 | 36708 | `-` | `residue_empty` | `[276,57960)` | 46189 |  | 4 | 0 |
| 3 | 14421 | `+` | `residue_empty` | `[-87561,-29877)` | 31768 |  | 1 | 0 |
| 4 | 19228 | `+` | `interval_empty` | `[-77947,-20263)` | 12540 | 7723 | 0 | 0 |
| 5 | 12540 | `+` | `residue_empty` | `[-52031,5653)` | 0 |  | 1 | 0 |

## 4. 自足小引理

每个剥离节点只需验收两个事实之一：

```text
interval-empty:  [L-epsilon*A,H-epsilon*A) 与 [-R,R] 不交；
residue-empty:   区间候选存在，但没有候选落入平移后的目标同余类。
```

若所有非选中兄弟分支满足上述二者之一，而选中路径末端只有一个空剩余命中，则该 formal unit 的 signed-sum 纤维是单点。

## 5. 证明边界

- 已闭合：当前 z=61 formal unit 的所有非选中分支均被区间空或同余空排除，选中路径唯一。
- 未闭合：把该分支决策模式提升为全局 bound，或排斥 BranchDecision-PDEC。
- 下一目标：`GlobalBranchDecisionPatternBoundOrBranchDecisionPDEC`。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json` | `bd408eb36e3b1a42cb0b24c07eff5dcbbc55684c54633cc1cb2ee90eb8952756` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json` | `000bb6e26dec4b78c4215118876df470f40659f120db560c9bee5cf6a80fd0c7` |
| `docs/monograph/prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.json` | `fe82db8bed8550d35f4778fde4f6f1dbd590e45035dc0aa9e3d97e385f0cd179` |
| `experiments/prime_matrix_square_phase_lowalpha_z61_branch_decision_ledger_router.py` | `0deff05cb90bbc7b63e638c8a27dcc9117ec0949a9e49678181e8121f42a728e` |
