# Prime Matrix AffineTwin endpoint-release fill-arrival projection gate audit

**状态：** `current_sweep_fill_arrival_projection_routed_global_open`

本审计继续压缩 `FillResidueArrivalBound`：fill 到达本身不是 actual overload。已物化 `q=31` 不能走 fill-only 路线，必须 generator 共到达；未物化 `q=43,103` 虽形式上可 fill-only，但先被 source gate 阻断。

```text
candidate_q_values=[31, 43, 103]
realized_q_values=[31]
source_blocked_q_values=[43, 103]
source_blocked_formal_pairs=28
all_realized_fill_arrivals_require_generator_coarrival=true
minimal_crossing_formal_product_count=30
minimal_crossing_projection_hit_count=3
minimal_crossing_actual_sqrt_slack=26
anonymous_fill_arrival_actual_overload_closed_current_sweep=true
```

## 1. fill arrival projection rows

| q | route | source | fill-only | min fill | min generator | blocked pairs | obstruction |
| ---: | --- | --- | --- | ---: | ---: | ---: | --- |
| 31 | `RealizedNoFillOnlyGraphProjection` | `ExactSourceMaterialized` | false | 1 | 2 | 0 | fill arrival alone cannot cross; needs at least 2 generator residues and then projects below sqrt gate |
| 43 | `SourceGateBlockedBeforeFillProjection:SameGapWrongSource-MaterializationGate` | `SameGapWrongSource-MaterializationGate` | true | 3 | 0 | 16 | formal fill-only threshold is source-unmaterialized; actual packet blocked by SameGapWrongSource-MaterializationGate |
| 103 | `SourceGateBlockedBeforeFillProjection:NoGapSource-MaterializationGate` | `NoGapSource-MaterializationGate` | true | 7 | 0 | 12 | formal fill-only threshold is source-unmaterialized; actual packet blocked by NoGapSource-MaterializationGate |

## 2. 显式矛盾读数

- `q=31` 是唯一已物化候选，但 `minimal_route_can_be_fill_only=false`；任何阈值穿越至少还要新增 2 个 generator residue。
- unused-target 账本给出的新 fill residues 为 `[5, 6, 7, 30]`，但全部 target 同时需要新 generator residue，并且 CRT jump 都超过 support width。
- 即使把共到达形式乘积推到最小 crossing `30`，actual projection 也只有 `3` 个 hit，仍有 sqrt slack `26`。
- `q=43,103` 的 fill-only 形式路线不能进入真实链，因为 source gate 已先阻断：一个 wrong-source，一个 no-source。

## 3. 结论边界

当前 sweep 内不存在匿名 fill-arrival actual overload：realized 分支必须 generator 共到达并回到 graph projection；non-realized 分支先败于 source materialization。

这仍不是全局无条件证明。下一层剩余被压成 `GeneratorCoarrivalBound`、`ProductAccountingTighteningGlobal`、`SourceRematerialization-PDEC/SAE` 与 `ColumnCRT/PDEC` 的族级排斥或控制。

## 4. 依赖哈希

| file | sha256 |
| --- | --- |
| `data/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json` | `29dbb00110b05ea2a63df6fece2f60c4bcfe8844268529e4b06730d5dc0da2d6` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier-ledger.json` | `af447a26eec5e39236b523897a32afba579de755c400d642fe6ae18e3a27ac71` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json` | `fa2485f12eee15af77f301d61a720a4d349ce27c4d9b82e3640f58700c143c03` |
| `data/prime-matrix-affine-twin-source-materialization-gate-ledger.json` | `aaaee80eaba6130fa016758509513449beff23eaefa41fcc79a174e183c5e385` |
| `data/prime-matrix-affine-twin-unused-target-arrival-ledger.json` | `cc69729e33a77e2389eb185ee4e5fb959e4fe3087549bb31f6cba497f0b0caa3` |
| `data/prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json` | `209cc18174894b44e5eb153e0601602460f730a98e83e968e7e7d6dbf7ebe3b5` |
| `data/prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json` | `51c3143a936264617d47fff2643948dc806b44fabe3bcbf8380508634fd3b966` |
