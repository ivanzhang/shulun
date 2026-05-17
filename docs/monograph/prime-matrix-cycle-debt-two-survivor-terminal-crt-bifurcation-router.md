# Prime Matrix cycle-debt two-survivor terminal CRT bifurcation router

**状态：** `two_survivor_terminal_crt_bifurcation_named`

K13 与 K14 两个 survivor 已不再是可互相吸收的同一支撑运动。两者覆盖同一 27 个需求 target，但 source 支撑只重合 19 行，实际 source-target 边只重合 1 条。delta lane 只共同保留 54 与 58，其余 13 条 lane 位于对称差中。两分支阻断素因子联合 lcm 约为 10^57.156，tail 因子联合 lcm 约为 10^24.632，均远超本地周期 5680。因此剩余不再是未命名 SAE，而是两 survivor 终端 CRT 分叉 PDEC 的排斥问题。

```text
row_column_unconditional_closed=false
previous_hardpoint=K13FixedGateProfilePDECOrK14FullDebtEightLaneCRTLoadPDEC
period_p=5680
survivor_shifts=[13, 14]
k13_delta_count=9
k14_delta_count=8
common_deltas=[54, 58]
delta_union_count=15
delta_symmetric_difference_count=13
source_intersection_count=19
source_symmetric_difference_count=16
target_intersection_count=27
pair_intersection_count=1
pair_intersection=[{'source_residue': 13, 'target_residue': 67}]
k13_lcm_log10=42.095
k14_lcm_log10=48.508
union_factor_count=32
union_lcm_log10=57.156
tail_union_lcm_log10=24.632
k13_tail_slots=18
k14_tail_slots=28
k14_tail_slot_increase_over_k13=10
next_direct_attack_target=TwoSurvivorTerminalCRTBifurcationPDECExclusion
```

## 1. branch load comparison

| branch | deltas | edges | width | tail slots | factors | log10 lcm |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `k13` | 9 | 27 | 101 | 18 | 25 | 42.095 |
| `k14` | 8 | 27 | 101 | 28 | 28 | 48.508 |

## 2. lane comparison

| item | value |
| --- | --- |
| common deltas | `[54, 58]` |
| delta union | `[0, 2, 4, 8, 16, 22, 28, 39, 48, 54, 55, 58, 59, 66, 70]` |
| delta symmetric difference | `[0, 2, 4, 8, 16, 22, 28, 39, 48, 55, 59, 66, 70]` |
| source symmetric difference | `[2, 6, 17, 23, 25, 29, 41, 42, 47, 49, 54, 57, 60, 62, 63, 70]` |

## 3. branch lanes

### k13

| delta | edges | width | tail slots | factors | log10 lane lcm |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 2 | 4 | 2 | 4 | 4.800 |
| 8 | 4 | 11 | 0 | 6 | 7.853 |
| 22 | 4 | 20 | 2 | 11 | 15.565 |
| 39 | 4 | 17 | 9 | 11 | 17.244 |
| 54 | 2 | 18 | 0 | 12 | 17.502 |
| 55 | 2 | 9 | 0 | 6 | 6.627 |
| 58 | 2 | 10 | 2 | 7 | 8.262 |
| 59 | 4 | 8 | 2 | 6 | 6.766 |
| 66 | 3 | 4 | 1 | 4 | 3.798 |

### k14

| delta | edges | width | tail slots | factors | log10 lane lcm |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 3 | 6 | 1 | 4 | 4.888 |
| 4 | 2 | 15 | 3 | 11 | 14.877 |
| 16 | 3 | 19 | 6 | 9 | 13.085 |
| 28 | 4 | 16 | 7 | 10 | 12.800 |
| 48 | 3 | 4 | 6 | 3 | 2.364 |
| 54 | 4 | 23 | 3 | 14 | 22.059 |
| 58 | 3 | 8 | 0 | 5 | 5.977 |
| 70 | 5 | 10 | 2 | 6 | 8.285 |

## 4. 判定

- K13 与 K14 覆盖同一 target 需求集合，但实际匹配边只重合 `13->67` 一条。
- lane 交集只有 `54,58`，13 条 lane 位于对称差，不能解释为单一相位的小扰动。
- 两分支联合 CRT lcm 约 `10^57.156`；tail 因子联合 lcm 约 `10^24.632`。
- 因此剩余压成 two-survivor terminal CRT bifurcation PDEC 排斥问题。
- 下一主攻点：`TwoSurvivorTerminalCRTBifurcationPDECExclusion`。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
| `data/prime-matrix-cycle-debt-low-shell-delta-skeleton-ledger.json` | `48c044e9957e2e14cb3f160b7c5fa6bd818fff5f55341fab9417753de39b6d49` |
| `data/prime-matrix-cycle-debt-k13-full-debt-nine-lane-tail-ledger.json` | `2cc8e902d04fdc3cca2c892030ddcb5d75786f207521c11b5bb43d3c23da8b9d` |
| `data/prime-matrix-cycle-debt-k13-tail-gate-drift-ledger.json` | `eb05e53effefd940c094aaf1be6e07996773e331aa39e5edab878d3fdf6fcc8b` |
| `data/prime-matrix-cycle-debt-k14-high-gate-low-shell-skeleton-ledger.json` | `8af1f444ef07b546648e0a298ed439419bf8a8a6ed38280754b76a309bc2cc63` |
