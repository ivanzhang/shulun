# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin threshold route classifier

**状态：** `affine_twin_threshold_crossing_routes_classified_global_open`

本步把整数阈值穿越缺口继续拆成最小补齐路线。当前所有最小穿越路线都需要 fill 侧新增 residue；`q=31` 是 mixed coaccumulation-only，`q=43,103` 允许 fill-catchup 或 mixed 两种最小补齐，且没有 generator-only 最小路线。最大 fill catch-up 倍率上界为 9.000000，最小 fill 延迟/所需新增 fill 为 80.000000。因此最新硬点从总阈值穿越压成：排斥 fill 侧持久追赶或 mixed 双侧同步补齐。

```text
candidate_q_values=[31, 43, 103]
route_class_histogram={'MixedCoaccumulationOnly': 1, 'FillCatchUpOrMixed': 2}
all_minimal_routes_require_fill_increment=true
fill_only_route_q_values=[]
mixed_only_route_q_values=[31]
max_fill_catchup_multiplier_upper=9.000000000000
min_fill_delay_per_required_fill_increment=80.000000000000
row_column_unconditional_closed=false
```

## 1. 路线分类

| q | route | min extra | fill extra min | gen extra min | fill multiplier | delay/fill | PDEC |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 31 | `MixedCoaccumulationOnly` | 4 | 1 | 2 | 1.500000 | 80.000000 | `AffineTwin-MixedCoaccumulationOnly-ThresholdCrossing-PDEC` |
| 43 | `FillCatchUpOrMixed` | 4 | 3 | 0 | 3.000000 | 536.666667 | `AffineTwin-FillCatchUpOrMixed-ThresholdCrossing-PDEC` |
| 103 | `FillCatchUpOrMixed` | 8 | 7 | 0 | 9.000000 | 153.428571 | `AffineTwin-FillCatchUpOrMixed-ThresholdCrossing-PDEC` |

## 2. 结论

- 最小穿越路线没有 generator-only 情形。
- `q=31` 必须双侧共同补齐；`q=43,103` 存在 fill-only 追赶路线，也允许少量 mixed 路线，但都必须新增 fill 侧 residue。
- 因此下一步只需攻 fill-catchup 与 mixed-coaccumulation 两类持久 PDEC。

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `minimal_threshold_crossing_routes_classified` | `closed_current_sweep` | Every current q has an explicit minimal crossing route; all minimal routes require fill-side residue growth. |
| `fill_catchup_and_mixed_routes_split` | `closed_routing` | Threshold crossing splits into FillCatchUp-only, MixedCoaccumulation-only, or composite route classes with named PDEC labels. |
| `global_fill_catchup_or_mixed_exclusion` | `open` | A self-contained proof must exclude persistent fill-side catch-up or mixed coaccumulation, or close the named PDEC/ColumnCRT families. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `MinimalRoutesClassified` | `true` | `true` | 阈值穿越的最小补齐路线已逐 q 分类。 | closed |
| `AllMinimalRoutesRequireFillIncrement` | `true` | `false` | 当前所有最小穿越路线都必须增加 fill 侧 residue。 | finite evidence only |
| `RoutePDECsNamed` | `true` | `true` | fill-only 与 mixed 补齐失败形态已命名为具体 PDEC。 | exclusion still separate |
| `GlobalFillCatchupExcluded` | `false` | `false` | 仍需全局证明 fill 侧不能持久追赶到阈值，或排斥对应 PDEC。 | AffineTwinFillCatchUpOrMixedCoaccumulationPDECExclusion |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成阈值穿越路线分类，不关闭全局行/列命题。 | AffineTwinFillCatchUpOrMixedCoaccumulationPDECExclusion |

## 5. 下一步

- 主攻：`AffineTwinFillCatchUpOrMixedCoaccumulationPDECExclusion`。
- fill-catchup 线：证明 fill 侧晚激活后无法补足最小新增 residue。
- mixed 线：证明双侧同时新增到最小见证会触发固定双模 ColumnCRT/PDEC。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_threshold_route_classifier.py` | `9e67ac8c3accdda041bde7e1b2c678ef3bd5f234a3ad29d6f7530195a69ba817` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-ledger.json` | `4585a4af4e66518873bf3edf31e8b868db6baeaf6d7d9466ad3abafbd8283e0e` |
| `data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier-ledger.json` | `af447a26eec5e39236b523897a32afba579de755c400d642fe6ae18e3a27ac71` |
