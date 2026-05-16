# Prime Matrix AffineTwin endpoint-release moving-family persistence pressure audit

**状态：** `current_sweep_moving_family_persistence_routed_global_open`

本审计继续下钻 moving-slot 的族级持久复现出口：若反例链不靠单个槽位，而靠 moving family 反复续命，则每个候选 `q` 必须同时通过 source 物化、双侧压力乘积、阈值穿越和 fill 到达/重置二分。

```text
candidate_q_values=[31, 43, 103]
source_gate_pass_q_values=[31]
source_gate_fail_q_values=[43, 103]
source_gate_blocked_formal_pairs=28
candidate_product_mass_upper_sum=0.023577117628562343
one_sided_pressure_q_values=[43, 103]
all_minimal_routes_require_fill_increment=true
total_min_extra_fill_required_if_all_candidates_cross=11
anonymous_moving_family_persistence_closed_current_sweep=true
```

## 1. family persistence rows

| q | route | source | blocked | one-sided pressure | paired slack | min fill | fill mass | phase defect |
| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | --- |
| 31 | `RealizedGraphCap+FillArrivalOrReset` | `ExactSourceMaterialized` | 0 | false | 0.839822 | 1 | 0.032258 | `exact_source_materialized, dp_delta=0` |
| 43 | `SameGapWrongSource-MaterializationGate+FillArrivalOrReset` | `SameGapWrongSource-MaterializationGate` | 16 | true | 0.854793 | 3 | 0.069767 | `wrong_source_signature, dp_delta=-39` |
| 103 | `NoGapSource-MaterializationGate+FillArrivalOrReset` | `NoGapSource-MaterializationGate` | 12 | true | 0.986158 | 7 | 0.067961 | `gap_source_absent` |

## 2. 显式矛盾读数

- `q=31` 是唯一已物化 source，但已被固定 graph cap 管住；若要从安全阈值穿越，仍需新增 fill residue 或进入 reset/ColumnCRT。
- `q=43` 有同 gap source，但实际签名是 `plus->minus` 且 `p_delay=74`，而 AffineTwin 期望 `minus->plus` 且 `p_delay=113`；相位差 `-39`，16 个 formal pairs 全部被 source gate 阻断。
- `q=103` 没有 gap source，12 个 formal pairs 全部被 source gate 阻断。
- `q=43,103` 虽有 generator 单侧压力，但 paired pressure product 仍低于 1；缺口由 fill 侧瓶颈控制。若要越过阈值，所有最小路线都要求 fill 增量。
- 若三个候选全都尝试阈值穿越，至少需要新增 fill residue 总数 `11`，对应 Rankin 质量 `0.169986671425`；重复则触发 reset/ColumnCRT-PDEC。

## 3. 结论边界

当前 sweep 的 moving-family 持久复现不能作为匿名容量来源：未物化候选先被 source gate 阻断；已物化候选受 graph cap 和 fill-arrival 二分约束；单侧 generator 压力没有与 fill 侧同步形成 paired overload。

这仍不是全局无条件证明。下一层全局剩余是证明 fill-side residue arrival 不能持久补齐这些阈值缺口，或把失败登记为 `FillResidueArrivalBound`、`HighDensityEpochPair-PDEC/ColumnCRT`、`PressureProduct-PDEC`、`SourceRematerialization-PDEC/SAE`。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json` | `3a12613953c6eb9a61f7865f232f4aabf9fa56048ea7047aada4d957b58ba15a` |
| `data/prime-matrix-affine-twin-source-materialization-gate-ledger.json` | `aaaee80eaba6130fa016758509513449beff23eaefa41fcc79a174e183c5e385` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json` | `8323447f703d339a1ff63e35f0dcaff4d697b295ea79241f67c23d2ecd5c00d3` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json` | `3260f7bb9020052ca7362859c608c3ed7508238ae927c79a4a42712ba09a41a2` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier-ledger.json` | `af447a26eec5e39236b523897a32afba579de755c400d642fe6ae18e3a27ac71` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json` | `fa2485f12eee15af77f301d61a720a4d349ce27c4d9b82e3640f58700c143c03` |
