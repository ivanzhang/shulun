# Prime Matrix square-phase off-band prefix gap shadow selector rho-hit obstruction router

**状态：** `selector_geometry_rho_hits_classified_open_global`

本步把几何层 715 个目标 rho 命中全部分类。其中合数 P 命中 371 个，素数 P 命中 344 个；当前 full-shape overlap 为 0。素数 rho 命中没有进入 overlap，而是落入 witness-pressure mismatch 或 ordered-shape mismatch。

```text
max_p=5000
geometry_rho_hit_count=715
composite_rho_hit_count=371
prime_rho_hit_count=344
full_shape_overlap_count=0
matches_geometry_rho_total=true
row_column_unconditional_closed=false
```

## 1. Obstruction Counts

| obstruction | count |
| --- | ---: |
| `CompositeP` | 371 |
| `WitnessPressureMismatch` | 344 |

## 2. Template Records

| template | side | g | rho | geometry rho | composite | prime | overlap | prime examples |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 0 | `minus` | 15 | 2 | 93 | 50 | 43 | 0 | `[107, 167, 197, 257, 347, 587, 617, 677]` |
| 1 | `minus` | 15 | 7 | 86 | 42 | 44 | 0 | `[67, 157, 277, 337, 487, 577, 607, 727]` |
| 2 | `plus` | 15 | 7 | 47 | 22 | 25 | 0 | `[157, 337, 577, 937, 1087, 1327, 1447, 1627]` |
| 3 | `plus` | 15 | 7 | 47 | 22 | 25 | 0 | `[157, 337, 577, 937, 1087, 1327, 1447, 1627]` |
| 4 | `plus` | 3 | 2 | 112 | 70 | 42 | 0 | `[173, 191, 227, 311, 317, 443, 449, 653]` |
| 5 | `minus` | 15 | 2 | 165 | 82 | 83 | 0 | `[107, 137, 167, 197, 227, 257, 317, 347]` |
| 6 | `minus` | 15 | 7 | 165 | 83 | 82 | 0 | `[67, 97, 127, 157, 277, 307, 337, 367]` |

## 3. 命题行

| name | status | statement |
| --- | --- | --- |
| `geometry_rho_hits_classified` | `closed_on_current_sweep` | Every geometry-level rho hit is classified as composite P, witness-pressure mismatch, ordered-shape mismatch, or full-shape overlap. |
| `current_prime_rho_hits_do_not_overlap_full_shape` | `closed_on_current_sweep` | No prime rho hit in the sweep reaches full-shape overlap; prime hits fail pressure or ordered-shape gates. |
| `global_prime_rho_hit_obstruction` | `open` | A global proof must exclude prime rho hits by pressure/shape mismatch, or route full-shape overlaps to PDEC. |

## 4. 决策表

| gate | closed | proved | meaning | remaining |
| --- | ---: | ---: | --- | --- |
| `RhoHitObstructionClassificationClosed` | `true` | `true` | 几何 rho 命中已分为合数 P、压力不匹配、shape 不匹配或 overlap。 | closed on current finite sweep |
| `CurrentFullShapeOverlapAbsent` | `true` | `true` | 当前扫描无 full-shape overlap PDEC 实例。 | closed on current finite sweep |
| `GlobalPrimeRhoHitObstructionProved` | `false` | `false` | 仍需证明所有素数 rho 命中都必压力不匹配或 shape 不匹配。 | PrimeRhoHitWitnessPressureMismatchOrOrderedShapeMismatchTheorem |
| `RowColumnUnconditionalClosureReached` | `false` | `false` | 本步只完成 rho 命中有限分类，不关闭全局行/列命题。 | PrimeRhoHitWitnessPressureMismatchOrOrderedShapeMismatchTheorem |

## 5. 下一步

- 主攻：`PrimeRhoHitWitnessPressureMismatchOrOrderedShapeMismatchTheorem`。
- 合数 P 出口已与素数 formal unit 分离；真正剩余是素数 rho 命中为何必压力不匹配或 shape 不匹配。
- 若出现 `FullShapeOverlapPDEC`，立即登记 ColumnCRT/PDEC 证书对象。
- 当前仍未证明全局行/列无条件闭合。

## 6. 依赖哈希

| file | sha256 |
| --- | --- |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_rho_hit_obstruction_router.py` | `f0c6e92421aa66727d36b60042796ef73cadb07e7a08b378fde9c8cba2eb81cd` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_geometry_vs_formal_unit_router.py` | `053368853b91afd756c3f35bec1851daeac12eeea8f6c9d7f8338b78b76798dc` |
| `experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_router.py` | `6fac77056cdc883354f2d7c8ffe2e2331928cfaadb9e849960fbde9b36d23c65` |
| `data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json` | `c01101b66f6cdfbff4a7895ac71b81af50423460b957518ecdea7d775bfcddf5` |
| `data/square-phase-offband-prefix-gap-shadow-selector-geometry-vs-formal-unit-ledger.json` | `bcde34967b9e597318feb0290623130d1a9127ed3c033ba1a8fba5f6400540ae` |
| `data/square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-ledger.json` | `31606c41cf9268aa4adf031683d22757bac054b17103da646d7eff0898717f8f` |
