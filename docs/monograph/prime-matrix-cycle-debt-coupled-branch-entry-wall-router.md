# Prime Matrix cycle-debt coupled branch entry-wall router

**状态：** `k13_k14_branch_entry_wall_coupling_registered`

Eight-prime entry-wall 与 branch-exclusive 不是两个可任意择一的松散出口。若终端走 K14，70 宽度 branch-exclusive 载荷与 29 宽度 fresh-arrival 载荷有 21 宽度重叠，但二者联合仍强制 78 宽度 actual load；K14 branch+entry 的 lcm 约 10^72.064，branch+entry+assigned post-wall 的 lcm 约 10^76.351，branch+entry+全部 post-wall 的 lcm 约 10^85.024。若终端走 K13，则剩余是 K13 branch-exclusive CRT-load，宽度 73，lcm 约 10^36.678。因此最新剩余从泛化的 entry-wall/branch-exclusive 并列出口，压成 K13 branch-exclusive PDEC 或 K14 coupled entry-branch CRT wall。

```text
row_column_unconditional_closed=false
previous_hardpoint=EightPrimeEntryWallPostWallCRTExclusionOrBranchExclusiveCRTLoadExclusion
k13_branch_exclusive_width=73
k13_branch_exclusive_lcm_log10=36.678
k14_branch_exclusive_width=70
k14_arrival_assigned_width=29
k14_arrival_branch_overlap_width=21
k14_branch_arrival_union_width=78
k14_branch_plus_entry_lcm_log10=72.064
k14_branch_plus_entry_plus_assigned_lcm_log10=76.351
k14_branch_plus_entry_plus_postwall_lcm_log10=85.024
both_branches_plus_k14_entry_postwall_lcm_log10=99.349
entry_wall_disjoint_from_branch_and_postwall=true
all_coupled_lcms_coprime_to_period=true
next_direct_attack_target=K13BranchExclusiveCRTLoadExclusionOrK14CoupledEntryBranchCRTWallExclusion
```

## 1. coupled CRT blocks

| block | factors | log10 lcm | gcd with period |
| --- | ---: | ---: | ---: |
| `k13_branch_exclusive` | 22 | 36.678 | 1 |
| `k14_branch_exclusive` | 20 | 32.582 | 1 |
| `all_branch_exclusive` | 27 | 46.907 | 1 |
| `k14_branch_plus_entry` | 28 | 72.064 | 1 |
| `k14_branch_plus_entry_plus_assigned` | 30 | 76.351 | 1 |
| `k14_branch_plus_entry_plus_postwall` | 34 | 85.024 | 1 |
| `both_branches_plus_k14_entry_postwall` | 41 | 99.349 | 1 |

## 2. overlap diagnostics

| item | value |
| --- | --- |
| K14 branch/postassigned common factors | `[3, 7, 11, 13, 23, 29, 31, 43, 79, 139, 283]` |
| K14 branch-only factors | `[17, 19, 53, 67, 83, 97, 127, 173, 227]` |
| postassigned-only factors | `[61, 317]` |

## 3. 判定

- K14 终端分支同时携带 branch-exclusive 载荷与 entry-wall/post-wall 载荷；不是两个无关出口。
- arrival 与 branch-exclusive 有 `21` 宽度重叠，但联合仍强制 `78` 宽度 actual load。
- K14 耦合载荷的最大审计 lcm 约 `10^85.024`；若把 K13/K14 branch-exclusive 全部合并则约 `10^99.349`。
- 因此最新剩余压成 K13 branch-exclusive 排斥，或 K14 coupled entry-branch CRT wall 排斥。
- 下一主攻点：`K13BranchExclusiveCRTLoadExclusionOrK14CoupledEntryBranchCRTWallExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-ledger.json` | `61a7cfac22f419f2a7efb585493897f3ba41e84ceb6fbc1416bdb377bd2da709` |
| `data/prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json` | `53823ea60fb8f2553523e1aae71f1ccf72d2d682985b5152d3b545ba4c659a6e` |
