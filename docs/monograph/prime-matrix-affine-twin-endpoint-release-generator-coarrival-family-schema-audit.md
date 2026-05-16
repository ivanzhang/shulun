# Prime Matrix AffineTwin endpoint-release generator-coarrival family schema audit

**状态：** `current_sweep_generator_coarrival_family_schema_routed_global_open`

本审计把上一轮 `q=31` 的 coarrival 子集枚举提升为族级门控格式：固定 AffineTwin 支撑图像内，actual load 只按图像容量计；若要 actual overload，必须破坏固定图像假设并进入命名出口。

```text
candidate_q_values=[31, 43, 103]
fixed_graph_family_symbolic_bound_proved=true
q_ge_13_symbolic_margin_at_13=88
formal_super_sqrt_subset_count=22
actual_overload_subset_count=0
full_formal_product_count=64
full_projection_hit_count=6
moving_slot_support_escape_routed_current_sweep=true
source_materialization_gate_closed_current_sweep=true
fixed_residue_columncrt_compression_closed_current_sweep=true
generator_coarrival_family_schema_closed_current_sweep=true
```

## 1. 固定图像族级不等式

固定 AffineTwin 槽的支撑宽度为 `W=(q+9)/2`。对 `q>=13`，

```text
W^2 <= q(q-2)  <=>  3q^2-26q-81 >= 0.
```

`q=13` 时右侧为正，且导数 `6q-26` 在 `q>=13` 为正，所以该不等式对所有 `q>=13` 成立。

| q | W | sqrt_floor | W^2 | q(q-2)-W^2 | margin | pass |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | 20 | 29 | 400 | 499 | 1996 | true |
| 43 | 26 | 41 | 676 | 1087 | 4348 | true |
| 103 | 56 | 101 | 3136 | 7267 | 29068 | true |

## 2. 出口路由

| gate | status | evidence | route if fails |
| --- | --- | --- | --- |
| `InsideFixedSupportGraphProjection` | `closed_current_sweep` | formal_super_sqrt_subset_count=22, actual_overload_subset_count=0, full packet 64 -> 6 actual hits | `ProductAccountingTighteningGlobal or ProjectionCollision-PDEC` |
| `FixedAffineTwinGraphFamilyBound` | `closed_current_sweep` | For q>=13, W=(q+9)/2 and W^2<=q(q-2) follows from 3q^2-26q-81>=0; current candidate q values all pass | `MovingSlotSupportEscape-PDEC/SAE` |
| `MovingSlotSupportEscape` | `closed_current_sweep` | support_motion_candidate_count=11; narrowest release=70 against support width=20; exact_rematerialized_q_values=[] | `MovingSlotFamilyPersistenceNoGo or SourceRematerialization-PDEC/SAE` |
| `SourceMaterializationGate` | `closed_current_sweep` | source_gate_pass_q_values=[31]; source_gate_fail_q_values=[43, 103]; blocked formal pairs=28 | `SameGapWrongSource-PDEC/SAE or NoGapSource-PDEC/SAE` |
| `FixedResidueColumnCRTCompression` | `closed_current_sweep` | actual anchor 19:8 compresses 12 cuts to P == 889 mod 899 | `ColumnCRT/PDEC` |
| `MovingFamilyPersistencePressure` | `closed_current_sweep` | realized_q_values=[31]; source_gate_blocked_formal_pairs=28; total_min_extra_fill_required=11 | `HighDensityEpochPair-PDEC/ColumnCRT or moving-family SAE` |

## 3. 显式矛盾读数

- 反例链需要把 generator/fill 共到达后的侧残基笛卡尔积当作容量来源。
- 真实链在固定 AffineTwin 支撑内只允许函数图像容量 `W`，而 `W<=sqrt(q(q-2))`。
- 当前 sweep 的 `22` 个形式超平方根子集全部投影到平方根门以下；完整 packet 为 `64 -> 6 hits`。
- 若未来全局族中出现 actual overload，它必须破坏固定函数图像，转入 support motion、source rematerialization、ColumnCRT/PDEC 或 moving-family persistence。

## 4. 结论边界

当前 sweep 的 generator-coarrival family schema 已路由闭合，但这仍不是行/列命题的全局无条件证明。全局剩余是把该 schema 推广到所有持久 AffineTwin family，并排斥或吸收每个命名出口。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-projection-accounting-ledger.json` | `ca993a7c75824e43cb29331a89426f48026a3cbc5226b9055481438dbdb26689` |
| `data/prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json` | `51c3143a936264617d47fff2643948dc806b44fabe3bcbf8380508634fd3b966` |
| `data/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json` | `3a12613953c6eb9a61f7865f232f4aabf9fa56048ea7047aada4d957b58ba15a` |
| `data/prime-matrix-affine-twin-source-materialization-gate-ledger.json` | `aaaee80eaba6130fa016758509513449beff23eaefa41fcc79a174e183c5e385` |
| `data/prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-ledger.json` | `2a5fc9d2433400377968f31a99049ba8d3ba6d39ad2188126c75ae24edafdc45` |
| `data/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json` | `29dbb00110b05ea2a63df6fece2f60c4bcfe8844268529e4b06730d5dc0da2d6` |
