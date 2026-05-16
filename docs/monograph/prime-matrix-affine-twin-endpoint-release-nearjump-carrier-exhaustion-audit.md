# Prime Matrix AffineTwin endpoint-release near-jump carrier exhaustion audit

**状态：** `current_sweep_nearjump_carrier_exhausted_global_open`

本审计把 support-width 内所有 near-jump 候选统一分解为 near-source gate fracture 与 orphan source deficit 两类，检查 target 侧近邻是否还有匿名承载通道。

```text
support_width=20
nearjump_carrier_q_values=[61, 65, 96, 111, 154, 293, 297, 355, 386]
near_source_gate_fractured_q_values=[61, 65]
orphan_source_deficit_q_values=[96, 111, 154, 293, 297, 355, 386]
source_status_histogram={'near_source_gate_fractured': 2, 'orphan_source_deficit': 7}
moving_route_histogram={'CompositeQ': 7, 'PrimeButNotTwinAffine': 2}
min_near_jump_abs_delta=0
min_orphan_source_gap_abs_delta=35
min_orphan_source_gap_abs_delta_minus_support_width=15
all_carrier_jump_events_need_new_side_residue=true
nearjump_carrier_exhausted_current_sweep=true
```

## 1. carrier rows

| q | carrier route | source status | moving route | nearest jump | jump delta | source deficit | failed invariants |
| ---: | --- | --- | --- | ---: | ---: | ---: | --- |
| 61 | `NearSourceAndJumpButGateFractured` | `near_source_gate_fractured` | `PrimeButNotTwinAffine` | 59 | 0 | - | `expected_p_delay_integral,gap_source_absent,q_mod4_eq3` |
| 65 | `NearSourceAndJumpButGateFractured` | `near_source_gate_fractured` | `CompositeQ` | 60 | -3 | - | `gap_source_absent,q_composite` |
| 96 | `NearJumpOnly` | `orphan_source_deficit` | `CompositeQ` | 90 | -4 | 15 | `gap_source_absent,q_composite` |
| 111 | `NearJumpOnly` | `orphan_source_deficit` | `CompositeQ` | 90 | -19 | 30 | `gap_source_absent,q_composite` |
| 154 | `NearJumpOnly` | `orphan_source_deficit` | `CompositeQ` | 150 | -2 | 73 | `gap_source_absent,q_composite` |
| 293 | `NearJumpOnly` | `orphan_source_deficit` | `PrimeButNotTwinAffine` | 281 | -10 | 212 | `expected_p_delay_integral,gap_source_absent,q_minus_2_is_prime,q_mod4_eq3` |
| 297 | `NearJumpOnly` | `orphan_source_deficit` | `CompositeQ` | 281 | -14 | 216 | `gap_source_absent,q_composite` |
| 355 | `NearJumpOnly` | `orphan_source_deficit` | `CompositeQ` | 345 | -8 | 274 | `gap_source_absent,q_composite` |
| 386 | `NearJumpOnly` | `orphan_source_deficit` | `CompositeQ` | 375 | -9 | 305 | `gap_source_absent,q_composite` |

## 2. 显式矛盾点

near-jump carrier 全部分成两类：`61,65` 同时 near source 与 near jump，但前者不是同向 AffineTwin source，后者是合数；其余七个 q 是 orphan source deficit，到 source 侧至少还差 `35>20`。

更强的是，所有 carrier 的 target 侧 near-jump 事件都需要新增侧残基。因此反例链无法只凭 target 侧近邻承载 actual load；一旦补 source 或补 target，就回到 source-rematerialization、unused-target arrival 或 moving-family 出口。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json` | `2422c8aa6737da977b23027242f682ada1bcaa60bb71cd0dc1fdecfd4b6e2e93` |
| `data/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json` | `979b19f46c602de6e5e43d5e4f48231b62a7fae2495470e8ee25c741a71dbe5e` |
| `data/prime-matrix-affine-twin-endpoint-release-orphan-nearjump-source-deficit-ledger.json` | `fb281989e4409d649eb8162c3155152ec56f226bcdfc66e4dc16e454fc67bffa` |
