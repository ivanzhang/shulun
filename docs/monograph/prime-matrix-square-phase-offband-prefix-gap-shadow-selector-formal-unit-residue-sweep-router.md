# Prime Matrix square-phase off-band prefix gap shadow selector formal-unit residue sweep router

**状态：** `selector_formal_unit_residue_avoidance_closed_on_sweep_open_global`

本步在 `P<=5000` 的实际 formal-unit 记录中扫描 small-modulus matching templates。候选级模板 7 个，同 full-shape 命中总数 14，但目标 rho residue 命中数为 0。因此当前扫描范围内 actual selector residue 与局部 matching template residue 完全分离；全局剩余是把该 residue avoidance 证明为符号定理。

```text
max_p=5000
prime_count=668
candidate_level_template_count=7
formal_unit_shape_hit_count=14
formal_unit_rho_hit_count=0
templates_with_rho_hits=0
row_column_unconditional_closed=false
```

## 1. Residue Sweep

| template | side | g | rho | shape P values | residues | rho hits |
| ---: | --- | ---: | ---: | --- | --- | --- |
| 0 | `minus` | 15 | 2 | `[691]` | `[1]` | `[]` |
| 1 | `minus` | 15 | 7 | `[691]` | `[1]` | `[]` |
| 2 | `plus` | 15 | 7 | `[421, 523, 683]` | `[1, 13, 8]` | `[]` |
| 3 | `plus` | 15 | 7 | `[421, 523, 683]` | `[1, 13, 8]` | `[]` |
| 4 | `plus` | 3 | 2 | `[313, 1129]` | `[1, 1]` | `[]` |
| 5 | `minus` | 15 | 2 | `[673, 691]` | `[13, 1]` | `[]` |
| 6 | `minus` | 15 | 7 | `[673, 691]` | `[13, 1]` | `[]` |

## 2. 命题行

| name | status | statement |
| --- | --- | --- |
| `finite_formal_unit_residue_sweep` | `closed_on_current_sweep` | For every candidate-level template, all actual formal units in the sweep with the same full shape avoid the template residue. |
| `local_phase_residue_not_actual_selector_residue` | `closed_on_current_sweep` | The residue classes that have local phase matching primes do not occur as actual P residues on the same full shape in the sweep. |
| `symbolic_formal_unit_residue_avoidance` | `open` | A global proof must derive this residue avoidance from the shape formulas, not from a finite sweep. |

## 3. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `CurrentFormalUnitResidueSweepClosed` | `true` | `true` | 当前扫描范围内，同 shape actual formal unit 全部避开模板 residue。 | closed on current finite sweep |
| `FullShapeOverlapPDECNeededOnSweep` | `true` | `true` | 当前扫描范围没有 full-shape residue overlap PDEC 实例。 | closed on current finite sweep |
| `GlobalSymbolicResidueAvoidanceProved` | `false` | `false` | 仍需将有限 residue 分离提升为 formal-unit 族定理。 | SymbolicFormalUnitShapeResidueAvoidanceOrFullShapeOverlapPDEC |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成当前扫描范围的 actual selector residue 审计，不关闭全局行/列命题。 | SymbolicFormalUnitShapeResidueAvoidanceOrFullShapeOverlapPDEC |

## 4. 下一步

- 主攻：`SymbolicFormalUnitShapeResidueAvoidanceOrFullShapeOverlapPDEC`。
- 把有限 sweep 中的 residue avoidance 转写成 shape 参数不等式或 CRT residue identity。
- 若出现同 shape 且同 rho 的 formal unit，则登记 full-shape overlap PDEC/ColumnCRT。
- 当前仍未证明全局行/列无条件闭合。

## 5. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_formal_unit_residue_sweep_router.py` | `db28e17236cf5313264bc2d88075ed5b3dc87cde92318b3bb38a43a53f36e8db` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_source_guard_router.py` | `5383c437edb961ee7bfaf1fca30900ff45821eff1844dc568d3f5fae209b56a1` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py` | `6fac77056cdc883354f2d7c8ffe2e2331928cfaadb9e849960fbde9b36d23c65` |
| `data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json` | `c01101b66f6cdfbff4a7895ac71b81af50423460b957518ecdea7d775bfcddf5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-formal-unit-residue-sweep-ledger.json` | `20994de52f79184fef55f0a7c51eba3c9d84267ea06b3f3491a0f292ca774036` |
