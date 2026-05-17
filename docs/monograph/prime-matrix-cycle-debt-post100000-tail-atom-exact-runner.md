# Prime Matrix cycle-debt post-100000 tail atom exact runner

**状态：** `post100000_tail_atoms_exactly_verified_registered_finite_branch_closed`

31 个 post-100000 tail atoms 已逐个精确审计：23 个合数槽的记录因子全部整除且均为最小因子；8 个 post-wall first prime 均经试除验证为真素数；每个 arrival row 的 first prime 之前槽位均为已证合数。因此 post-100000 finite atom runner 对当前登记原子闭合，有限原子分支从最新前沿移除；剩余集中为持久 branch replay ColumnCRT/PDEC 排斥。

```text
row_column_unconditional_closed=false
previous_hardpoint=BranchReplayColumnCRTPDECExclusionOrPost100000TailAtomRunner
tail_atom_count=31
tail_atom_p_range=[101087,134047]
kind_counts={'assigned_slot': 15, 'postwall_first_prime': 8, 'tail_slot': 8}
all_composite_atoms_divisible_by_recorded_factor=true
all_composite_recorded_factors_are_smallest=true
all_postwall_first_primes_verified=true
all_preprime_slots_composite_in_arrival_rows=true
finite_atom_branch_closed_for_registered_atoms=true
next_direct_attack_target=BranchReplayColumnCRTPDECExclusion
```

## 1. row summaries

| source -> target | capacity K13 | capacity K14 | first-prime position | first prime | post-100000 atoms | pre-prime composite |
| --- | ---: | ---: | ---: | ---: | ---: | :---: |
| `6->8` | 0 | 4 | 4 | 115807 | 3 | true |
| `23->25` | 0 | 2 | 2 | 103967 | 1 | true |
| `29->57` | 0 | 6 | 6 | 124847 | 5 | true |
| `47->24` | 0 | 4 | 4 | 113647 | 3 | true |
| `54->41` | 0 | 5 | 5 | 118127 | 4 | true |
| `60->43` | 0 | 5 | 5 | 121967 | 4 | true |
| `63->20` | 0 | 6 | 6 | 123887 | 5 | true |
| `70->15` | 0 | 7 | 7 | 134047 | 6 | true |

## 2. tail atom verification

| kind | count |
| --- | ---: |
| `assigned_slot` | 15 |
| `postwall_first_prime` | 8 |
| `tail_slot` | 8 |

## 3. 判定

- `23` 个 post-100000 合数槽全部由记录小因子精确验证，且记录因子均为最小因子。
- `8` 个 post-wall first prime 全部经独立素性检查确认。
- 每个 arrival row 的 first prime 之前 post-wall 槽全为已证合数，因此 first-prime 边界解释闭合。
- 本步只关闭当前登记有限原子分支，不排斥全局持久 ColumnCRT/PDEC。
- 下一主攻点：`BranchReplayColumnCRTPDECExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-finite-atom-boundary-bridge-ledger.json` | `cd66994982b1f9753d854abf69d472e50ddd2ab61f661fb266fff12cbb1dd444` |
| `data/prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json` | `53823ea60fb8f2553523e1aae71f1ccf72d2d682985b5152d3b545ba4c659a6e` |
