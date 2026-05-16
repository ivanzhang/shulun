# Prime Matrix AffineTwin endpoint-release orphan near-jump source-deficit audit

**状态：** `current_sweep_orphan_nearjump_source_deficit_closed_global_open`

本审计继续下钻 support-width near-scale fracture 后的剩余：只靠近 unused-target jump、却不靠近 source 的 orphan near-jump 是否能补成真实相位桥。

```text
support_width=20
available_gap_source_values=[31, 43, 59]
orphan_nearjump_q_values=[96, 111, 154, 293, 297, 355, 386]
orphan_nearjump_moving_route_histogram={'CompositeQ': 6, 'PrimeButNotTwinAffine': 1}
min_source_gap_abs_delta=35
min_source_gap_abs_delta_minus_support_width=15
min_source_gap_deficit_q=96
all_orphan_nearjump_source_gaps_exceed_support_width=true
all_orphan_nearjump_events_need_new_side_residue=true
orphan_nearjump_source_deficit_closed_current_sweep=true
```

## 1. orphan rows

| q | moving route | nearest jump | jump delta | nearest source scale | source gap | source deficit | failed invariants |
| ---: | --- | ---: | ---: | --- | ---: | ---: | --- |
| 96 | `CompositeQ` | 90 | -4 | `q_minus_2` | 59 | 15 | `gap_source_absent,q_composite` |
| 111 | `CompositeQ` | 90 | -19 | `q_minus_2` | 59 | 30 | `gap_source_absent,q_composite` |
| 154 | `CompositeQ` | 150 | -2 | `q_minus_2` | 59 | 73 | `gap_source_absent,q_composite` |
| 293 | `PrimeButNotTwinAffine` | 281 | -10 | `q_minus_2` | 59 | 212 | `expected_p_delay_integral,gap_source_absent,q_minus_2_is_prime,q_mod4_eq3` |
| 297 | `CompositeQ` | 281 | -14 | `q_minus_2` | 59 | 216 | `gap_source_absent,q_composite` |
| 355 | `CompositeQ` | 345 | -8 | `q_minus_2` | 59 | 274 | `gap_source_absent,q_composite` |
| 386 | `CompositeQ` | 375 | -9 | `q_minus_2` | 59 | 305 | `gap_source_absent,q_composite` |

## 2. 显式矛盾点

这些 orphan 候选虽然在 unused-target jump 侧落入 support width `20`，但到最近 source scale 的距离最小也是 `35`，比 support width 还多 `15`。最窄例是 `q=96`。

同时所有 orphan near-jump 的 unused-target 事件都需要新增侧残基，且 moving source 均未物化；候选本身也全部失败于合数或 AffineTwin prime/source gate。因此“近 target”不能替代“近 source”，也不能承载 actual load。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json` | `2422c8aa6737da977b23027242f682ada1bcaa60bb71cd0dc1fdecfd4b6e2e93` |
| `data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json` | `b7d9016b2e43da9d390efdde3012739d24305e4843ed29efc8c295d16dc52fd6` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/prime-matrix-affine-twin-endpoint-release-support-width-nearscale-fracture-ledger.json` | `979b19f46c602de6e5e43d5e4f48231b62a7fae2495470e8ee25c741a71dbe5e` |
