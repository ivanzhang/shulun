# Prime Matrix AffineTwin endpoint-release phase-scale bridge exhaustion audit

**状态：** `current_sweep_phase_scale_bridge_exhausted_global_open`

本审计把全部 moving-q 候选、当前可用 gap source、unused-target CRT 跳跃放入同一个相位尺度账本，检查是否存在比 `61/59` 更强的桥接通道。

```text
support_width=20
moving_q_candidate_count=19
moving_q_values=[61, 65, 96, 111, 119, 123, 154, 181, 235, 293, 297, 355, 386, 575, 699, 761, 1375, 1499, 1747]
available_gap_source_values=[31, 43, 59]
unused_target_jump_values=[59, 60, 90, 150, 281, 343, 345, 374, 375]
exact_q_gap_bridge_q_values=[]
exact_q_unused_jump_bridge_q_values=[]
exact_qminus2_gap_and_unused_bridge_q_values=[61]
viable_exact_scale_bridge_q_values=[]
strongest_exact_offset_bridge_atom={'q': 61, 'route': 'ExactQMinus2ScaleFractured', 'q_minus_2': 59, 'exact_gap_q_minus_2_count': 1, 'exact_unused_jump_q_minus_2_count': 1, 'moving_route': 'PrimeButNotTwinAffine', 'failed_invariants': ['expected_p_delay_integral', 'gap_source_absent', 'q_mod4_eq3']}
all_exact_or_offset_scale_bridges_fractured_current_sweep=true
```

## 1. q bridge rows

| q | route | moving route | exact gap q | exact gap q-2 | exact jump q | exact jump q-2 | nearest gap to q | nearest jump to q | failed invariants |
| ---: | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| 61 | `ExactQMinus2ScaleFractured` | `PrimeButNotTwinAffine` | 0 | 1 | 0 | 1 | `{'value': 59, 'signed_delta': -2, 'abs_delta': 2}` | `{'value': 60, 'signed_delta': -1, 'abs_delta': 1}` | `expected_p_delay_integral,gap_source_absent,q_mod4_eq3` |
| 65 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -6, 'abs_delta': 6}` | `{'value': 60, 'signed_delta': -5, 'abs_delta': 5}` | `gap_source_absent,q_composite` |
| 96 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -37, 'abs_delta': 37}` | `{'value': 90, 'signed_delta': -6, 'abs_delta': 6}` | `gap_source_absent,q_composite` |
| 111 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -52, 'abs_delta': 52}` | `{'value': 90, 'signed_delta': -21, 'abs_delta': 21}` | `gap_source_absent,q_composite` |
| 119 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -60, 'abs_delta': 60}` | `{'value': 90, 'signed_delta': -29, 'abs_delta': 29}` | `gap_source_absent,q_composite` |
| 123 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -64, 'abs_delta': 64}` | `{'value': 150, 'signed_delta': 27, 'abs_delta': 27}` | `gap_source_absent,q_composite` |
| 154 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -95, 'abs_delta': 95}` | `{'value': 150, 'signed_delta': -4, 'abs_delta': 4}` | `gap_source_absent,q_composite` |
| 181 | `NoExactScaleBridge` | `PrimeButNotTwinAffine` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -122, 'abs_delta': 122}` | `{'value': 150, 'signed_delta': -31, 'abs_delta': 31}` | `expected_p_delay_integral,gap_source_absent,q_mod4_eq3` |
| 235 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -176, 'abs_delta': 176}` | `{'value': 281, 'signed_delta': 46, 'abs_delta': 46}` | `gap_source_absent,q_composite` |
| 293 | `NoExactScaleBridge` | `PrimeButNotTwinAffine` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -234, 'abs_delta': 234}` | `{'value': 281, 'signed_delta': -12, 'abs_delta': 12}` | `expected_p_delay_integral,gap_source_absent,q_minus_2_is_prime,q_mod4_eq3` |
| 297 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -238, 'abs_delta': 238}` | `{'value': 281, 'signed_delta': -16, 'abs_delta': 16}` | `gap_source_absent,q_composite` |
| 355 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -296, 'abs_delta': 296}` | `{'value': 345, 'signed_delta': -10, 'abs_delta': 10}` | `gap_source_absent,q_composite` |
| 386 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -327, 'abs_delta': 327}` | `{'value': 375, 'signed_delta': -11, 'abs_delta': 11}` | `gap_source_absent,q_composite` |
| 575 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -516, 'abs_delta': 516}` | `{'value': 375, 'signed_delta': -200, 'abs_delta': 200}` | `gap_source_absent,q_composite` |
| 699 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -640, 'abs_delta': 640}` | `{'value': 375, 'signed_delta': -324, 'abs_delta': 324}` | `gap_source_absent,q_composite` |
| 761 | `NoExactScaleBridge` | `PrimeButNotTwinAffine` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -702, 'abs_delta': 702}` | `{'value': 375, 'signed_delta': -386, 'abs_delta': 386}` | `expected_p_delay_integral,gap_source_absent,q_minus_2_is_prime,q_mod4_eq3` |
| 1375 | `NoExactScaleBridge` | `CompositeQ` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -1316, 'abs_delta': 1316}` | `{'value': 375, 'signed_delta': -1000, 'abs_delta': 1000}` | `gap_source_absent,q_composite` |
| 1499 | `NoExactScaleBridge` | `PrimeButNotTwinAffine` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -1440, 'abs_delta': 1440}` | `{'value': 375, 'signed_delta': -1124, 'abs_delta': 1124}` | `gap_source_absent,q_minus_2_is_prime` |
| 1747 | `NoExactScaleBridge` | `PrimeButNotTwinAffine` | 0 | 0 | 0 | 0 | `{'value': 59, 'signed_delta': -1688, 'abs_delta': 1688}` | `{'value': 375, 'signed_delta': -1372, 'abs_delta': 1372}` | `gap_source_absent,q_minus_2_is_prime` |

## 2. 显式矛盾点

没有任何 moving-q 与可用 gap source 精确相等，也没有任何 moving-q 与 unused-target CRT 跳跃精确相等。唯一同时命中 gap source 与 unused jump 的精确 offset 是 `q=61` 的 `q-2=59`。

这个唯一 offset 桥已经被上一层 `61/59` phase-fracture 关闭：`q=61` 不通过 AffineTwin 同向 prime/source gate；gap `59` source 的角色是 `generator=61, fill=59, sides=minus->minus`，不是 `q=61` 期望的 `generator=59, fill=61, sides=minus->plus`；unused-target 的 `59` 跳跃仍需要新增侧残基。

因此当前 sweep 中反例链不能把 moving-key、已有 source、unused-target arrival 三者接成同一条 actual 相位桥。若全局族中这类桥持续复现，必须升级为 `PhaseScaleBridgeGlobalNoGo` 的族证明；否则失败形态应登记为 source-rematerialization、unused-target、ColumnCRT/PDEC 或 moving-family 出口。

## 3. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json` | `2422c8aa6737da977b23027242f682ada1bcaa60bb71cd0dc1fdecfd4b6e2e93` |
| `data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json` | `b7d9016b2e43da9d390efdde3012739d24305e4843ed29efc8c295d16dc52fd6` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
| `data/prime-matrix-affine-twin-endpoint-release-near-miss-61-59-phase-fracture-ledger.json` | `25a249feac48f337d8def74e0f8a59adc2d10c459f67493ebd295dc39b8f15d1` |
