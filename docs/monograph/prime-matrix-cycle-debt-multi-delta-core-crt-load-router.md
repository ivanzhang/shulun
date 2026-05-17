# Prime Matrix cycle-debt multi-delta core CRT load router

**状态：** `multi_delta_core_carries_large_transverse_crt_load`

把 multi-delta support SAE 的核心匹配展开成实际合数槽和阻断素因子。K=14 的最小多相位核心唯一，4 个 delta lane 的全局 CRT lcm 约为 10^31.716；K=13 的可枚举刚性核心只有 2 个最小 delta 方案，7 个 delta lane 的全局 CRT lcm 约为 10^36.165。这些核心载荷都远超本地周期，不是轻量相位碎裂；剩余只能是 multi-delta core CRT-load PDEC，或回到 K=13 低层大 shell 的 full-residue SAE。

```text
row_column_unconditional_closed=false
previous_hardpoint=NonAffineShellPhaseFragmentPDECOrMultiDeltaSupportSAE
period_p=5680
k13_enumerated_core_matching_count=96
k13_minimum_delta_count=7
k13_minimum_delta_matching_count=2
k13_best_min_delta_global_lcm_log10=36.165
k14_enumerated_core_matching_count=2
k14_minimum_delta_count=4
k14_minimum_delta_matching_count=1
k14_best_min_delta_global_lcm_log10=31.716
all_min_delta_lcms_exceed_period=true
next_direct_attack_target=MultiDeltaCoreCRTLoadPDECOrLowShellFullResidueSAE
```

## 1. survivor core load

| K | core matchings | min delta | min-delta matchings | best log10 lcm | excluded shells |
| ---: | ---: | ---: | ---: | ---: | --- |
| 13 | 96 | 7 | 2 | 36.165 | `['1..3']` |
| 14 | 2 | 4 | 1 | 31.716 | `[]` |

## 2. best lane loads

| K | delta | edges | width | blocker factors | log10 lane lcm |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 8 | 1 | 5 | 4 | 4.621 |
| 13 | 22 | 2 | 17 | 10 | 13.739 |
| 13 | 39 | 2 | 14 | 10 | 15.295 |
| 13 | 54 | 1 | 15 | 11 | 15.515 |
| 13 | 55 | 1 | 7 | 5 | 5.513 |
| 13 | 58 | 1 | 9 | 7 | 8.262 |
| 13 | 59 | 1 | 4 | 4 | 4.095 |
| 14 | 4 | 1 | 13 | 9 | 12.184 |
| 14 | 16 | 2 | 16 | 8 | 11.166 |
| 14 | 28 | 1 | 8 | 6 | 6.491 |
| 14 | 54 | 1 | 15 | 11 | 16.731 |

## 3. 判定

- 每个 edge load 使用目标 demand width 展开 source 行从 shift 开始的实际合数槽。
- `K=14` 的最小多相位核心唯一；4 个 delta lane 已足以产生约 `10^31.716` 的横向 CRT 载荷。
- `K=13` 的可枚举刚性核心只有 2 个最小 delta 方案；7 个 delta lane 的最小全局 lcm 约 `10^36.165`。
- `K=13` 的低层 `1..3` shell 尚未作为闭合证明使用；它是下一步 full-residue SAE/PDEC 的接口。
- 下一主攻点：`MultiDeltaCoreCRTLoadPDECOrLowShellFullResidueSAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-cycle-debt-shell-phase-graph-ledger.json` | `b575245854e1f1a72d715a468d40fd484bbb3b4f27f1a90728923966785d412f` |
| `data/prime-matrix-cycle-debt-support-row-replacement-hall-ledger.json` | `a7b03048e67a16e4ab08f7a6fb7b8d757da9eb24b9ed598d61c01ae351799335` |
