# Prime Matrix AffineTwin endpoint-release carrier-arrival routing audit

**状态：** `current_sweep_carrier_arrival_routed_global_open`

本审计把 near-jump carrier 的 target 侧近邻事件逐个路由到 unused-target arrival 账本，检查是否存在未登记的匿名 target 侧承载通道。

```text
carrier_q_values=[61, 65, 96, 111, 154, 293, 297, 355, 386]
carrier_event_count=27
unique_arrival_atom_count_used_by_carriers=9
target_pair_histogram={'10:30': 9, '16:5': 5, '17:6': 7, '18:7': 2, '20:9': 4}
carrier_event_new_side_residue_requirement_total=50
carrier_event_new_side_residue_histogram={1: 4, 2: 23}
required_new_generator_residues=[10, 16, 17, 18, 20]
required_new_fill_residues=[5, 6, 7, 30]
exact_zero_phase_event_count=1
missing_unused_target_arrival_match_count=0
all_carrier_events_match_closed_unused_target_arrival=true
all_carrier_targets_not_supported_actual_current_sweep=true
carrier_arrival_routed_current_sweep=true
```

## 1. carrier-arrival rows

| q | route | scale | jump | delta | source | target | new side | matched | target actual |
| ---: | --- | --- | ---: | ---: | --- | --- | ---: | --- | --- |
| 61 | `PrimeButNotTwinAffine` | `q_minus_2=59` | 59 | 0 | `19:12` | `20:9` | 1 | true | false |
| 61 | `PrimeButNotTwinAffine` | `q=61` | 60 | -1 | `15:8` | `17:6` | 2 | true | false |
| 61 | `PrimeButNotTwinAffine` | `q_minus_2=59` | 60 | 1 | `15:8` | `17:6` | 2 | true | false |
| 61 | `PrimeButNotTwinAffine` | `q=61` | 59 | -2 | `19:12` | `20:9` | 1 | true | false |
| 65 | `CompositeQ` | `q_minus_2=63` | 60 | -3 | `15:8` | `17:6` | 2 | true | false |
| 65 | `CompositeQ` | `q_minus_2=63` | 59 | -4 | `19:12` | `20:9` | 1 | true | false |
| 65 | `CompositeQ` | `q=65` | 60 | -5 | `15:8` | `17:6` | 2 | true | false |
| 65 | `CompositeQ` | `q=65` | 59 | -6 | `19:12` | `20:9` | 1 | true | false |
| 96 | `CompositeQ` | `q_minus_2=94` | 90 | -4 | `13:8` | `16:5` | 2 | true | false |
| 96 | `CompositeQ` | `q=96` | 90 | -6 | `13:8` | `16:5` | 2 | true | false |
| 111 | `CompositeQ` | `q_minus_2=109` | 90 | -19 | `13:8` | `16:5` | 2 | true | false |
| 154 | `CompositeQ` | `q_minus_2=152` | 150 | -2 | `13:12` | `18:7` | 2 | true | false |
| 154 | `CompositeQ` | `q=154` | 150 | -4 | `13:12` | `18:7` | 2 | true | false |
| 293 | `PrimeButNotTwinAffine` | `q_minus_2=291` | 281 | -10 | `19:28` | `10:30` | 2 | true | false |
| 293 | `PrimeButNotTwinAffine` | `q=293` | 281 | -12 | `19:28` | `10:30` | 2 | true | false |
| 297 | `CompositeQ` | `q_minus_2=295` | 281 | -14 | `19:28` | `10:30` | 2 | true | false |
| 297 | `CompositeQ` | `q=297` | 281 | -16 | `19:28` | `10:30` | 2 | true | false |
| 355 | `CompositeQ` | `q_minus_2=353` | 345 | -8 | `13:9` | `16:5` | 2 | true | false |
| 355 | `CompositeQ` | `q_minus_2=353` | 343 | -10 | `15:28` | `10:30` | 2 | true | false |
| 355 | `CompositeQ` | `q=355` | 345 | -10 | `13:9` | `16:5` | 2 | true | false |
| 355 | `CompositeQ` | `q=355` | 343 | -12 | `15:28` | `10:30` | 2 | true | false |
| 355 | `CompositeQ` | `q=355` | 374 | 19 | `13:28` | `10:30` | 2 | true | false |
| 355 | `CompositeQ` | `q=355` | 375 | 20 | `15:9` | `17:6` | 2 | true | false |
| 386 | `CompositeQ` | `q_minus_2=384` | 375 | -9 | `15:9` | `17:6` | 2 | true | false |
| 386 | `CompositeQ` | `q_minus_2=384` | 374 | -10 | `13:28` | `10:30` | 2 | true | false |
| 386 | `CompositeQ` | `q=386` | 375 | -11 | `15:9` | `17:6` | 2 | true | false |
| 386 | `CompositeQ` | `q=386` | 374 | -12 | `13:28` | `10:30` | 2 | true | false |

## 2. 显式矛盾点

27 个 carrier target 侧近邻事件全部匹配到已登记的 9 个 unused-target arrival 原子，缺失匹配数为 `0`。这些 target pair 全部不在当前形式积，也不被当前 actual support 支持。

唯一 exact zero phase 事件是 `q=61, q-2=59, jump=59`，但它仍对应 `19:12 -> 20:9`，需要新增 generator residue `20`，且 source gate 已在 `61/59` phase-fracture 中失败。因此“相位正好贴住 target jump”仍不能生成真实链 actual load。

carrier 侧总共出现 `50` 次事件级新侧残基需求，压缩为 generator residues `[10,16,17,18,20]` 与 fill residues `[5,6,7,30]`。所以 target 侧若要复现，只能进入全局新残基到达率控制或命名 `PDEC/SAE/ColumnCRT` 出口。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json` | `979b19f46c602de6e5e43d5e4f48231b62a7fae2495470e8ee25c741a71dbe5e` |
| `data/prime-matrix-affine-twin-endpoint-release-nearjump-carrier-exhaustion-ledger.json` | `97d043220b3d7157851434c75a83a7210b814e68db7f029d599fdec90609ebee` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
