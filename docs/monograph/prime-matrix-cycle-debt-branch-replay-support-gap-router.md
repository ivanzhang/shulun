# Prime Matrix cycle-debt branch replay support-gap router

**状态：** `local_moving_slot_replay_excluded_far_replay_routed_to_columncrt_pdec`

K13 branch-exclusive 与 K14 coupled entry-branch 的本地 moving-slot 复现被关闭：同一阻断因子包若在周期坐标中平移复现，非零位移必须至少为其 CRT lcm。K13 branch-exclusive 的 lcm 约 10^36.678，已远超 73 宽度支撑；K14 branch+entry+postwall 的 lcm 约 10^85.024，远超 78 宽度实际支撑与 117 个审计槽。因此本地支撑运动不能复现这些终端载荷；剩余只能是远程 ColumnCRT/PDEC 复现，或被登记为孤立有限原子，而不是新的自由逃逸路线。

```text
row_column_unconditional_closed=false
previous_hardpoint=K13BranchExclusiveCRTLoadExclusionOrK14CoupledEntryBranchCRTWallExclusion
period_p=5680
near_shift_limit_cycles=16
k13_branch_exclusive_width=73
k14_branch_arrival_union_width=78
k14_coupled_audit_slot_count_all_postwall=117
smallest_log10_margin_over_support_width=30.737
smallest_log10_margin_over_audit_slots=30.737
all_blocks_coprime_to_period=true
all_nonzero_replay_moduli_exceed_support_width=true
all_nonzero_replay_moduli_exceed_audit_slots=true
local_moving_slot_replay_excluded_for_registered_blocks=true
far_replay_still_requires_columncrt_pdec=true
next_direct_attack_target=BranchReplayColumnCRTPDECExclusionOrIsolatedTerminalAtomAbsorption
```

## 1. replay lemma

设本地周期为 `M=5680`。若一个已登记阻断包 `B` 在周期坐标中平移 `T` 个周期后仍由同一素因子包复现，则对每个 `q in B` 有

```text
n_q + T*M == 0 (mod q),  且  n_q == 0 (mod q).
```

因全部 `q` 与 `M` 互素，得到 `T == 0 (mod q)`。合并后 `T == 0 (mod lcm(B))`。所以最小非零复现周期就是 `lcm(B)`。

## 2. replay blocks

| block | support width | audit slots | factors | log10 replay modulus | margin over support | margin over audit |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `k13_branch_exclusive` | 73 | 73 | 22 | 36.678 | 34.814 | 34.814 |
| `k14_branch_exclusive` | 70 | 70 | 20 | 32.582 | 30.737 | 30.737 |
| `k14_branch_plus_entry` | 78 | 78 | 28 | 72.064 | 70.172 | 70.172 |
| `k14_branch_plus_entry_plus_assigned` | 78 | 107 | 30 | 76.351 | 74.459 | 74.321 |
| `k14_branch_plus_entry_plus_postwall` | 78 | 117 | 34 | 85.024 | 83.132 | 82.956 |
| `both_branches_plus_k14_entry_postwall` | 151 | 190 | 41 | 99.349 | 97.170 | 97.070 |

## 3. 判定

- K13 分支的最小复现模数已经比 `73` 宽度支撑大约 `10^34.814` 倍。
- K14 `branch+entry+postwall` 的最小复现模数比 `78` 宽度实际支撑大约 `10^83.132` 倍，也远超 `117` 个审计槽。
- 因此高因子吸收槽不能通过本地 moving-slot 支撑运动复现；一旦移动，就必须换成新的阻断包并回流 `ColumnCRT/PDEC/SAE`。
- 这仍不是全局行/列命题闭合；它关闭本地复现解释，并把远程复现登记为明确的 ColumnCRT/PDEC 接口。
- 下一主攻点：`BranchReplayColumnCRTPDECExclusionOrIsolatedTerminalAtomAbsorption`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
| `data/prime-matrix-cycle-debt-coupled-branch-entry-wall-ledger.json` | `afb79d743dda71833cb0dd36a922b5e7ba43bc563f9076e1ff61a5067a6fcef4` |
| `data/prime-matrix-cycle-debt-terminal-switch-arrival-wall-ledger.json` | `53823ea60fb8f2553523e1aae71f1ccf72d2d682985b5152d3b545ba4c659a6e` |
