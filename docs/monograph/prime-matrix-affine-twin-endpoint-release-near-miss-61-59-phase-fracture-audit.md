# Prime Matrix AffineTwin endpoint-release 61/59 near-miss phase-fracture audit

**状态：** `current_sweep_near_miss_61_59_phase_fracture_closed_global_open`

本审计对准 actual-anchor replacement 后的最窄近失配：formal 替换最窄 atom `19:12` 要求 moving-key 候选 `61/111`，而 unused-target 最窄跳跃与最近可用 gap source 都出现整数 `59`。审计目标是判定这个 `61/59` 近邻是否能桥接反例链与真实链。

```text
combined_crt_modulus=899
support_width=20
actual_anchor_pair=19:8
actual_crt_residue=889
formal_min_pair=19:12
formal_min_abs_crt_jump=58
formal_min_required_common_side_depth=58
formal_min_endpoint_release=70
moving_narrowest_candidate_q_values=[61, 111]
q61_route=PrimeButNotTwinAffine
q61_failed_invariants=['expected_p_delay_integral', 'gap_source_absent', 'q_mod4_eq3']
q111_route=CompositeQ
q111_failed_invariants=['gap_source_absent', 'q_composite']
q59_is_moving_candidate=false
unused_min_target_pair=20:9
unused_min_abs_crt_jump=59
unused_min_new_side_residue_count=1
near_miss_61_59_phase_fracture_closed_current_sweep=true
```

## 1. bridge rows

| atom | role | source/pair | scale | phase status | blocking invariant |
| --- | --- | --- | ---: | --- | --- |
| `formal_replacement_minimum` | existing formal pair would replace actual anchor | `19:12` | 58 | `jump_exceeds_support_and_requires_endpoint_release` | `abs_crt_jump=58 > support_width=20; endpoint_release=70` |
| `moving_key_fill_candidate` | fill-depth formula candidate for the same formal atom | `q=61` | 61 | `PrimeButNotTwinAffine` | `expected_p_delay_integral,gap_source_absent,q_mod4_eq3` |
| `moving_key_generator_candidate` | generator-depth formula candidate for the same formal atom | `q=111` | 111 | `CompositeQ` | `gap_source_absent,q_composite` |
| `nearest_available_gap_source` | nearest source to q=61 in the current source ledger | `gap=59` | 59 | `wrong_gap_role_for_q61` | `gap=59 source has generator=61, fill=59, sides=minus->minus` |
| `unused_target_minimum` | unused target replacement from the same formal atom | `19:12->20:9` | 59 | `new_side_residue_required` | `jump=59 > support_width=20; new_generator_residue=20` |

## 2. 相位裂缝

`q=61` 是最强 near miss：`61` 与 `59` 都为素数，且最近可用 gap source 确实是 `59`，signed delta 为 `-2`。但 AffineTwin 同向源要求的是 `gap=61, generator=59, fill=61, sides=minus->plus`，并且 `p_delay=(11q-21)/4` 必须为整数。

当前 gap `59` source 的实际签名是 `gap=59, generator=61, fill=59, sides=minus->minus, p_delay=70`。它和 `q=61` 的期望签名 `{'gap_ell': 61, 'generator_ell': 59, 'fill_ell': 61, 'generator_side': 'minus', 'fill_side': 'plus', 'expected_p_delay': None}` 不同：gap、fill、方向和 delay 均不能匹配。因此 `59` 只是最近相邻源，不是 `q=61` 的重物化源。

同时，unused-target 最窄跳跃也是 `59`，但它的对象是 `19:12->20:9` 的新侧残基到达，仍有 `59>20`，并且至少新增 `1` 个侧残基。这与 moving-key `q=61` 的源门控不是同一相位义务。

## 3. 结论边界

- 本步关闭当前 sweep 中 `61/59` 近失配作为隐藏桥接通道的解释。
- 本步没有证明全局行/列命题；剩余是把 `NearMiss6159GlobalFamilyNoGo` 升格为族定理，或继续排斥 source-rematerialization、unused-target arrival、ColumnCRT/PDEC 与 moving-family 出口。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-actual-anchor-replacement-ledger.json` | `2422c8aa6737da977b23027242f682ada1bcaa60bb71cd0dc1fdecfd4b6e2e93` |
| `data/prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json` | `b7d9016b2e43da9d390efdde3012739d24305e4843ed29efc8c295d16dc52fd6` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-gap-fill-pair-ledger.json` | `abfda31e733d7c1e274ded997056cf5e55d39d555a72f4f8ca35ac689c62ae1e` |
