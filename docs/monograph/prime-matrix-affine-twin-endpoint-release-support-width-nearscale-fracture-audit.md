# Prime Matrix AffineTwin endpoint-release support-width near-scale fracture audit

**状态：** `current_sweep_support_width_nearscale_fractured_global_open`

本审计继续下钻 `PhaseScaleBridgeGlobalNoGo`：exact/offset 桥已空后，检查是否存在落在 support width 内的近似尺度桥可以偷渡。

```text
support_width=20
moving_q_candidate_count=19
support_width_near_source_q_values=[61, 65]
support_width_near_unused_jump_q_values=[61, 65, 96, 111, 154, 293, 297, 355, 386]
support_width_near_source_and_jump_q_values=[61, 65]
viable_support_width_nearscale_bridge_q_values=[]
near_source_and_jump_moving_route_histogram={'CompositeQ': 1, 'PrimeButNotTwinAffine': 1}
all_support_width_nearscale_bridges_fractured_current_sweep=true
```

## 1. q near-scale rows

| q | route | moving route | near source events | near jump events | common scale kinds | failed invariants |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 61 | `NearSourceAndJumpButGateFractured` | `PrimeButNotTwinAffine` | 4 | 4 | `['q', 'q_minus_2']` | `expected_p_delay_integral,gap_source_absent,q_mod4_eq3` |
| 65 | `NearSourceAndJumpButGateFractured` | `CompositeQ` | 3 | 4 | `['q', 'q_minus_2']` | `gap_source_absent,q_composite` |
| 96 | `NearJumpOnly` | `CompositeQ` | 0 | 2 | `[]` | `gap_source_absent,q_composite` |
| 111 | `NearJumpOnly` | `CompositeQ` | 0 | 1 | `[]` | `gap_source_absent,q_composite` |
| 154 | `NearJumpOnly` | `CompositeQ` | 0 | 2 | `[]` | `gap_source_absent,q_composite` |
| 293 | `NearJumpOnly` | `PrimeButNotTwinAffine` | 0 | 2 | `[]` | `expected_p_delay_integral,gap_source_absent,q_minus_2_is_prime,q_mod4_eq3` |
| 297 | `NearJumpOnly` | `CompositeQ` | 0 | 2 | `[]` | `gap_source_absent,q_composite` |
| 355 | `NearJumpOnly` | `CompositeQ` | 0 | 6 | `[]` | `gap_source_absent,q_composite` |
| 386 | `NearJumpOnly` | `CompositeQ` | 0 | 4 | `[]` | `gap_source_absent,q_composite` |

## 2. 显式矛盾点

在 support width `20` 内同时靠近 source 与 unused jump 的 moving-q 只有 `61` 和 `65`。其中 `61` 是 `PrimeButNotTwinAffine`，仍失败于 delay 整数性、`q mod 4=3` 与 gap `61` source 缺席；`65` 是合数。其余 near-jump 候选没有 near-source，不能形成相位桥。

因此即使把 exact equality 放宽到 support-width 邻域，当前 sweep 也没有可承载 actual load 的桥。近似数值距离不能替代 CRT/source 签名：非零尺度差必须改变 moving key、source 或 unused target，因而回到 source-rematerialization、unused-target arrival、ColumnCRT/PDEC 或 moving-family 出口。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json` | `2422c8aa6737da977b23027242f682ada1bcaa60bb71cd0dc1fdecfd4b6e2e93` |
| `data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json` | `b7d9016b2e43da9d390efdde3012739d24305e4843ed29efc8c295d16dc52fd6` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/prime-matrix-affine-twin-endpoint-release-phase-scale-bridge-exhaustion-ledger.json` | `07c46be7e85eb5e4fd1ecdccea3ae78bc78687664be46db43c16f1bbc722f98f` |
