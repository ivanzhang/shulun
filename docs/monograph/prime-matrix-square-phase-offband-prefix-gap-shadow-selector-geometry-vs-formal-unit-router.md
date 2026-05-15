# Prime Matrix square-phase off-band prefix gap shadow selector geometry vs formal-unit router

**状态：** `selector_residue_avoidance_requires_prime_pressure_open_global`

本步检验 residue avoidance 是否可由固定 band/k 几何单独推出。答案是否定的：在奇整数 P<=5000 的纯几何扫描中，同 ordered shape 命中 8942 次，其中目标 rho 命中 715 次；但实际 formal-unit 同 shape 命中 14 次，rho 命中为 0。因此不能用固定几何常数闭合，必须使用 tail prime count、half-grid survivors 与 selector 链条形成的素数压力约束。

```text
max_p=5000
template_count=7
geometry_shape_hit_count=8942
geometry_rho_hit_count=715
formal_unit_shape_hit_count=14
formal_unit_rho_hit_count=0
templates_requiring_prime_pressure_count=7
row_column_unconditional_closed=false
```

## 1. Geometry vs Formal Unit

| template | side | g | rho | geometry hits | geometry rho hits | examples | formal shape hits | formal rho hits |
| ---: | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 0 | `minus` | 15 | 2 | 1228 | 93 | `[77, 107, 167, 197, 257, 287, 347, 407]` | 1 | 0 |
| 1 | `minus` | 15 | 7 | 1228 | 86 | `[67, 157, 217, 277, 337, 427, 487, 517]` | 1 | 0 |
| 2 | `plus` | 15 | 7 | 605 | 47 | `[157, 217, 337, 427, 517, 577, 697, 817]` | 3 | 0 |
| 3 | `plus` | 15 | 7 | 605 | 47 | `[157, 217, 337, 427, 517, 577, 697, 817]` | 3 | 0 |
| 4 | `plus` | 3 | 2 | 330 | 112 | `[173, 191, 227, 305, 311, 317, 443, 449]` | 2 | 0 |
| 5 | `minus` | 15 | 2 | 2473 | 165 | `[77, 107, 137, 167, 197, 227, 257, 287]` | 2 | 0 |
| 6 | `minus` | 15 | 7 | 2473 | 165 | `[67, 97, 127, 157, 187, 217, 247, 277]` | 2 | 0 |

## 2. 命题行

| name | status | statement |
| --- | --- | --- |
| `pure_geometry_not_enough` | `closed_on_current_sweep` | The same band/k ordered shapes have many integer P with the template residue, so geometry alone cannot explain selector residue avoidance. |
| `formal_unit_prime_pressure_needed` | `closed_on_current_sweep` | The observed residue avoidance appears only after imposing the formal-unit prime-pressure gates H,T and the actual selector chain. |
| `prime_pressure_residue_avoidance_theorem` | `open` | A global proof must derive residue avoidance from the infinite prime-pressure constraints, or route overlaps to PDEC/ColumnCRT. |

## 3. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `GeometryOnlyRouteRejected` | `true` | `true` | 纯 band/k 几何同 shape 中存在大量目标 rho 命中，不能作为闭合证明。 | rejected |
| `PrimePressureRouteNecessary` | `true` | `true` | 当前每个模板都需要 formal-unit 素数压力约束解释 residue 避让。 | PrimePressureResidueAvoidanceTheoremOrFullShapeOverlapPDEC |
| `GlobalPrimePressureResidueAvoidanceProved` | `false` | `false` | 仍需证明素数尾段压力门强制避开模板 rho。 | PrimePressureResidueAvoidanceTheoremOrFullShapeOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只排除了纯几何捷径，不关闭全局行/列命题。 | PrimePressureResidueAvoidanceTheoremOrFullShapeOverlapPDEC |

## 4. 下一步

- 主攻：`PrimePressureResidueAvoidanceTheoremOrFullShapeOverlapPDEC`。
- 不能把 residue avoidance 降成固定 band/k 几何命题；几何层存在大量 rho 命中。
- 必须证明素数压力门 `2T-H`、ordered selector 与 residue rho 不可同时成立，或登记 full-shape overlap PDEC/ColumnCRT。
- 当前仍未证明全局行/列无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_geometry_vs_formal_unit_router.py` | `053368853b91afd756c3f35bec1851daeac12eeea8f6c9d7f8338b78b76798dc` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_formal_unit_residue_sweep_router.py` | `db28e17236cf5313264bc2d88075ed5b3dc87cde92318b3bb38a43a53f36e8db` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py` | `6fac77056cdc883354f2d7c8ffe2e2331928cfaadb9e849960fbde9b36d23c65` |
| `data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json` | `c01101b66f6cdfbff4a7895ac71b81af50423460b957518ecdea7d775bfcddf5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-ledger.json` | `20994de52f79184fef55f0a7c51eba3c9d84267ea06b3f3491a0f292ca774036` |
| `data/square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-ledger.json` | `bcde34967b9e597318feb0290623130d1a9127ed3c033ba1a8fba5f6400540ae` |
