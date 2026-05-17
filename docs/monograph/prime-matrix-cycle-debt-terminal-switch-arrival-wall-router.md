# Prime Matrix cycle-debt terminal switch arrival wall router

**状态：** `terminal_switch_arrival_entry_wall_and_postwall_crt_registered`

K14 fresh-arrival 不是平滑打开的匿名容量。8 个 K14-only source 在 K13 时容量全为 0，并且全部在 K13 入口处撞到 window_position=0 的真实素数墙；入口素数墙的 lcm 约为 10^39.482。越过该墙后，K14 才得到 39 个 post-wall 容量槽，其中 29 槽被实际分配；assigned post-wall 因子 lcm 约为 10^20.205，entry+assigned 联合 lcm 约为 10^59.687，entry+全部 post-wall 联合 lcm 约为 10^68.361，且与本地周期 5680 互素。因此 terminal switch-arrival 不是局部微调，而是八素数入口墙加 post-wall CRT-load 的持久排斥问题；并行仍保留 branch-exclusive CRT-load 排斥义务。

```text
row_column_unconditional_closed=false
previous_hardpoint=TerminalSwitchArrivalColumnCRTPDECOrBranchExclusiveCRTLoadExclusion
arrival_source_count=8
all_arrival_sources_zero_capacity_at_k13=true
all_entry_wall_cycles_equal_13=true
all_entry_wall_positions_zero_at_k13=true
entry_wall_lcm_log10=39.482
postwall_capacity_total=39
postwall_assigned_width_total=29
postwall_tail_slot_total=10
postwall_assigned_lcm_log10=20.205
entry_plus_assigned_lcm_log10=59.687
entry_plus_postwall_lcm_log10=68.361
entry_plus_postwall_coprime_to_period=true
arrival_width_by_delta={2: 5, 16: 7, 28: 7, 48: 2, 54: 3, 58: 5}
next_direct_attack_target=EightPrimeEntryWallPostWallCRTExclusionOrBranchExclusiveCRTLoadExclusion
```

## 1. arrival rows

| source | target | delta | width | cap K13 | cap K14 | entry prime | next prime |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 6 | 8 | 2 | 4 | 0 | 4 | 87407 | 115807 |
| 23 | 25 | 2 | 1 | 0 | 2 | 86927 | 103967 |
| 29 | 57 | 28 | 1 | 0 | 6 | 85087 | 124847 |
| 47 | 24 | 48 | 2 | 0 | 4 | 85247 | 113647 |
| 54 | 41 | 58 | 5 | 0 | 5 | 84047 | 118127 |
| 60 | 43 | 54 | 3 | 0 | 5 | 87887 | 121967 |
| 63 | 20 | 28 | 6 | 0 | 6 | 84127 | 123887 |
| 70 | 15 | 16 | 7 | 0 | 7 | 88607 | 134047 |

## 2. CRT factor summaries

| block | slots | factors | log10 lcm | gcd with period |
| --- | ---: | ---: | ---: | ---: |
| `entry_wall` | 8 | 8 | 39.482 | 1 |
| `postwall_assigned` | 29 | 13 | 20.205 | 1 |
| `postwall_tail` | 10 | 6 | 9.995 | 1 |
| `postwall_all` | 39 | 17 | 28.879 | 1 |
| `entry_plus_assigned` | 37 | 21 | 59.687 | 1 |
| `entry_plus_postwall` | 47 | 25 | 68.361 | 1 |

## 3. 判定

- K14-only source 在 K13 全部为 `0` 容量，且全部由同一 `K=13` 入口素数墙切断。
- K14 的 `39` 个 post-wall 容量槽中有 `29` 个被实际分配，剩余 tail 为 `10`。
- 入口素数墙与 post-wall 因子均和本地周期 `5680` 互素，联合 lcm 约 `10^68.361`。
- 因此 switch-arrival 分支已压成八素数入口墙 + post-wall CRT-load 排斥；branch-exclusive CRT-load 仍为并行义务。
- 下一主攻点：`EightPrimeEntryWallPostWallCRTExclusionOrBranchExclusiveCRTLoadExclusion`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
| `data/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json` | `8af1f444ef07b546648e0a298ed439419bf8a8a6ed38280754b76a309bc2cc63` |
| `data/prime-matrix-cycle-debt-two-survivor-pdec-exclusion-ledger.json` | `61a7cfac22f419f2a7efb585493897f3ba41e84ceb6fbc1416bdb377bd2da709` |
