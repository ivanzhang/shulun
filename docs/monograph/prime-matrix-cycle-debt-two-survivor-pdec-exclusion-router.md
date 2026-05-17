# Prime Matrix cycle-debt two-survivor PDEC exclusion router

**状态：** `two_survivor_terminal_switch_pressure_registered`

Two-survivor 终端分叉不能只靠共同 anchor 或共同 delta 吸收。唯一共同实际边 13->67 只承载宽度 15，剩余 26 个 target 仍有宽度 86 必须重路由。每个终端分支至少有 70 宽度落在 branch-exclusive delta 上，相关 CRT lcm 至少约 10^32.582。若从 K13 切到 K14，K14 还必须调用 8 个在 K13 时容量为 0 的新 source，承载 29 宽度，其 arrival 因子 lcm 约 10^20.205。因此剩余已压成 terminal switch-arrival ColumnCRT/PDEC，或 branch-exclusive CRT-load 排斥，而不是局部相位微调。

```text
row_column_unconditional_closed=false
previous_hardpoint=TwoSurvivorTerminalCRTBifurcationPDECExclusion
period_p=5680
common_pair_count=1
common_pair_width=15
forced_rematched_target_count=26
forced_rematched_target_width=86
minimum_branch_exclusive_delta_width=70
minimum_branch_exclusive_delta_lcm_log10=32.582
k14_only_assigned_width=29
k14_only_capacity_at_k13=0
k14_only_capacity_at_k14=39
k14_arrival_lcm_log10=20.205
k13_same_support_capacity_deficit_at_k14=8
common_source_changed_count=18
next_direct_attack_target=TerminalSwitchArrivalColumnCRTPDECOrBranchExclusiveCRTLoadExclusion
```

## 1. switch pressure

| item | value |
| --- | ---: |
| common actual edge width | 15 |
| forced rematched target width | 86 |
| K13 branch-exclusive delta width | 73 |
| K14 branch-exclusive delta width | 70 |
| K14 fresh-arrival assigned width | 29 |
| K14 fresh-arrival capacity gain | 39 |
| common source changed count | 18 |

## 2. width by delta

| branch | width by delta |
| --- | --- |
| `k13` | `{0: 4, 8: 11, 22: 20, 39: 17, 54: 18, 55: 9, 58: 10, 59: 8, 66: 4}` |
| `k14` | `{2: 6, 4: 15, 16: 19, 28: 16, 48: 4, 54: 23, 58: 8, 70: 10}` |

## 3. factor blocks

| block | width | factors | log10 lcm |
| --- | ---: | ---: | ---: |
| `k13_branch_exclusive_deltas` | 73 | 22 | 36.678 |
| `k14_branch_exclusive_deltas` | 70 | 20 | 32.582 |
| `k13_common_delta_nonanchor` | 13 | 8 | 10.248 |
| `k14_common_delta_nonanchor` | 16 | 9 | 13.562 |
| `k13_common_anchor` | 15 | 11 | 15.515 |
| `k14_common_anchor` | 15 | 11 | 16.731 |
| `k13_departing_sources` | 8 | 4 | 4.004 |
| `k14_arriving_sources` | 29 | 13 | 20.205 |

## 4. 判定

- 共同实际边只有 `13->67`，它无法承载除 target `67` 以外的 `86` 宽度需求。
- 共同 delta `54,58` 的非 anchor 容量很小；每个分支仍至少有 `70` 宽度必须落在 branch-exclusive delta。
- K14 的 8 个新增 source 在 K13 时容量全为 `0`，到 K14 才出现 `39` 容量并承载 `29` 宽度。
- 因此 terminal bifurcation 的下一硬点是 arrival ColumnCRT/PDEC 或 branch-exclusive CRT-load 排斥。
- 下一主攻点：`TerminalSwitchArrivalColumnCRTPDECOrBranchExclusiveCRTLoadExclusion`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
| `data/prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json` | `48c044e9957e2e14cb3f160b7c5fa6bd818fff5f55341fab9417753de39b6d49` |
| `data/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json` | `8af1f444ef07b546648e0a298ed439419bf8a8a6ed38280754b76a309bc2cc63` |
| `data/prime-matrix-cycle-debt-two-survivor-terminal-crt-bifurcation-ledger.json` | `689ba530e42f37f1f964cf714de61aa0b25a928ad4ce486e59e1f60adc3f0d5a` |
