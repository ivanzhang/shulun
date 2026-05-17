# Prime Matrix cycle-debt finite atom boundary bridge router

**状态：** `finite_atoms_split_between_dynamic_bridge_and_post100000_tail_runner`

有限原子基例检查不能被旧 P<=5000 直接验证误吸收。cycle-debt cover pressure 的 155 个 P 坐标全落在已关闭的 3001<=P<100000 动态有限桥中；但 terminal arrival/post-wall 的 55 个坐标中有 31 个已经进入 P>=100000 尾段，最大到 134047。因此有限原子出口被拆成：前缀原子由动态有限桥吸收，尾段原子必须进入 post-100000 runner、tail lower-sieve 或 ColumnCRT/PDEC，而不能宣称全局闭合。

```text
row_column_unconditional_closed=false
previous_hardpoint=BranchReplayColumnCRTPDECExclusionOrFiniteAtomBaseCheck
direct_grid_verified_max_p=5000
dynamic_finite_bridge_range=[3001,99991]
dynamic_finite_bridge_closed=true
tail_start_p=100000
cover_pressure_atom_count=155
cover_pressure_all_atoms_in_dynamic_finite_bridge=true
arrival_wall_atom_count=55
arrival_wall_tail_atom_count=31
total_post100000_tail_atom_count=31
tail_atom_p_range=[101087,134047]
finite_atom_base_check_fully_closed=false
next_direct_attack_target=BranchReplayColumnCRTPDECExclusionOrPost100000TailAtomRunner
```

## 1. boundary counts

| packet | atoms | P min | P max | class counts |
| --- | ---: | ---: | ---: | --- |
| `cover_pressure` | 155 | 10207 | 98047 | `{'dynamic_finite_bridge_3001_99991': 155}` |
| `arrival_wall` | 55 | 84047 | 134047 | `{'dynamic_finite_bridge_3001_99991': 24, 'post100000_tail_atom': 31}` |
| `total` | 210 | 10207 | 134047 | `{'dynamic_finite_bridge_3001_99991': 179, 'post100000_tail_atom': 31}` |

## 2. post-100000 tail atom kinds

| kind | count |
| --- | ---: |
| `assigned_slot` | 15 |
| `postwall_first_prime` | 8 |
| `tail_slot` | 8 |

## 3. 判定

- `P<=5000` 的直接方阵验证不能覆盖当前 finite atom 出口。
- `3001<=P<100000` 的动态有限桥吸收了 cover-pressure 包中的全部 `155` 个坐标。
- terminal arrival/post-wall 仍有 `31` 个 `P>=100000` 尾段坐标，最大 `134047`。
- 因此有限原子基例检查被拆成前缀已吸收与尾段 runner/ColumnCRT 两部分，不能标记为全局闭合。
- 下一主攻点：`BranchReplayColumnCRTPDECExclusionOrPost100000TailAtomRunner`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-branch-replay-global-dichotomy-ledger.json` | `b25a9e5083355f5495156d61b9cf924af55843966d0efe0b7492075cdd811bc4` |
| `data/prime-matrix-cycle-debt-crt-cover-pressure-ledger.json` | `e2731895ab36398581674261c359b074ef71dba80c47601be4992723de15ddd8` |
| `data/prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json` | `53823ea60fb8f2553523e1aae71f1ccf72d2d682985b5152d3b545ba4c659a6e` |
| `docs/monograph/prime-matrix-dynamic-skeleton-lower-factorization-router.json` | `2c46448ba6bd4969f962984ad095d47199a787ef4906d5d2297ac5c252fefa8d` |
