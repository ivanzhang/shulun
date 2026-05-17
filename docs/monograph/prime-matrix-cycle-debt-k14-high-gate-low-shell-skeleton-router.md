# Prime Matrix cycle-debt K14 high-gate low-shell skeleton router

**状态：** `k14_high_gate_drift_compressed_to_full_debt_eight_lane_crt_load`

K=14 high-gate drift 不是新的未登记自由族。K=14 的 tight shell 只有 2 个 high-core 匹配；选择最优 core 后，剩余低层用整数规划补齐，low shell 单独最少 6 个 delta，相对 core 只需新增 2,48,58,70 四条 lane。于是 K=14 全 101 宽度被压成 8-lane CRT 载荷，全局 lcm 约 10^48.508，超过本地周期 5680。K14 moving 分支回到 full-debt CRT-load PDEC。

```text
row_column_unconditional_closed=false
previous_hardpoint=K13GateProfileNoNearReplayPDECOrK14HighGateDriftSAE
period_p=5680
k14_zero_slack_layers=[7, 8, 13, 15]
k14_high_gate_core_alternative_count=2
k14_best_core_deltas=[4, 16, 28, 54]
k14_low_shell_minimum_delta_count=6
k14_low_shell_new_delta_count_over_core=4
k14_low_shell_new_deltas_over_core=[2, 48, 58, 70]
k14_full_delta_count_after_low_shell=8
k14_full_deltas_after_low_shell=[2, 4, 16, 28, 48, 54, 58, 70]
k14_full_total_required_width=101
k14_full_global_lcm_log10=48.508
k14_full_lcm_exceeds_period=true
k14_full_used_tail_slots=28
k14_tail_lcm_log10=17.956
next_direct_attack_target=K13FixedGateProfilePDECOrK14FullDebtEightLaneCRTLoadPDEC
```

## 1. K14 core alternatives

| candidate | core deltas | low min deltas | new over core | full deltas | log10 full lcm | tail slots |
| ---: | --- | ---: | --- | --- | ---: | ---: |
| 1 | `[4, 16, 28, 54]` | 6 | `[2, 48, 58, 70]` | `[2, 4, 16, 28, 48, 54, 58, 70]` | 48.508 | 28 |
| 2 | `[4, 16, 54, 57, 58]` | 6 | `[36, 39, 60, 70]` | `[4, 16, 36, 39, 54, 57, 58, 60, 70]` | 48.381 | 25 |

## 2. best full K14 lane load

| delta | edges | width | tail slots | blocker factors | log10 lane lcm |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 3 | 6 | 1 | 4 | 4.888 |
| 4 | 2 | 15 | 3 | 11 | 14.877 |
| 16 | 3 | 19 | 6 | 9 | 13.085 |
| 28 | 4 | 16 | 7 | 10 | 12.800 |
| 48 | 3 | 4 | 6 | 3 | 2.364 |
| 54 | 4 | 23 | 3 | 14 | 22.059 |
| 58 | 3 | 8 | 0 | 5 | 5.977 |
| 70 | 5 | 10 | 2 | 6 | 8.285 |

## 3. 判定

- K14 高门漂移只留下两个 high-core 匹配，不是未命名的自由移动族。
- 最优 high-core 的低层补齐只需新增四条 lane：`2,48,58,70`。
- K14 全部 `101` 需求宽度被压成 `8` lane CRT 载荷，全局 lcm 约 `10^48.508`。
- 因此 K14 moving 分支回到 full-debt CRT-load PDEC；剩余还包括固定 K13 gate-profile PDEC。
- 下一主攻点：`K13FixedGateProfilePDECOrK14FullDebtEightLaneCRTLoadPDEC`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
| `data/prime-matrix-cycle-debt-shell-phase-graph-ledger.json` | `b575245854e1f1a72d715a468d40fd484bbb3b4f27f1a90728923966785d412f` |
| `data/prime-matrix-cycle-debt-k13-tail-gate-drift-ledger.json` | `eb05e53effefd940c094aaf1be6e07996773e331aa39e5edab878d3fdf6fcc8b` |
