# Prime Matrix strict RKS23 二分线交点界吸收证书

**状态：** `bipartite_line_intersection_bound_closed_remaining_point_plane_absorption`

本步把已闭合的 Cayley-Salmon/Kollár 曲面结构包吸收到二分 Guth-Katz 线交点界。初等插值曲面层、离面 Bézout、平面/二次退化收费此前已经闭合；现在 ruled/non-ruled 分量也由已闭合曲面包覆盖，因此二分线交点界闭合。点-平面 incidence 与 RNRS/行列命题仍需后续回接。

```text
self_contained_bipartite_line_intersection_bound_closed=true
self_contained_point_plane_incidence_proof_closed=false
self_contained_rnrs_rudnev_proof_closed=false
row_column_unconditional_closed=false
```

## 1. 目标线交点界

| field | value |
| --- | --- |
| `input` | two finite line families L,M in F^3 with \|L\|<=\|M\| and \|L\|=O(p^2) in characteristic p |
| `degeneracy` | no quadric contains simultaneously s lines of L and t lines of M |
| `output` | I(L,M)=O(\|L\|^(1/2)\|M\| + t\|L\| + s\|M\|) |
| `surface_choice` | interpolate a degree D=O(\|L\|^(1/2)) surface containing every line in L |
| `degree_condition` | the imported c0 cutoff guarantees component degrees below characteristic in the positive-characteristic branch |

## 2. 吸收账本

| field | value |
| --- | --- |
| `off_surface_M_lines` | each M-line not contained in the interpolating surface contributes at most D points by Bezout |
| `plane_quadric_components` | charged by the stated s,t quadric degeneracy ledger |
| `singly_ruled_components` | ordinary contained lines meet O(d_i) peers; exceptional directrix lines are O(1) and already charged |
| `non_ruled_components` | Cayley-Salmon now gives Flec(F_i) nonzero; Bezout yields O(d_i^3) internal line-intersection scale |
| `component_degree_sum` | sum d_i<=D and the closed component ledger absorbs O(sum d_i^3) into the same target scale under the previous certificate's accounting |
| `result` | all contributions match the bipartite Guth-Katz/Kollar target bound |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousBipartiteFrontierReady` | `true` | `true` | de Zeeuw 归约、初等曲面层和 Cayley-Salmon/Kollar 曲面包均已就绪。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `PositiveCharacteristicCutoffImported` | `true` | `true` | 正特征 degree<p 截断已从前序证书导入。 | degree<p cutoff |
| `InterpolationSurfaceLayerImported` | `true` | `true` | 低次数插值曲面构造已闭合并导入。 | interpolation layer |
| `OffSurfaceBezoutImported` | `true` | `true` | 不含于插值曲面的 M 直线由 Bézout 计数控制。 | off-surface Bezout |
| `PlaneQuadricDegeneracyImported` | `true` | `true` | 平面/二次曲面退化分量已由 quadric s,t 假设收费。 | plane/quadric degeneracy |
| `RuledSurfacePackageImported` | `true` | `true` | singly-ruled 与 non-ruled 曲面结构包已由 Cayley-Salmon 闭合证书导入。 | closed Kollar surface package |
| `ComponentSummationClosed` | `true` | `true` | 各分量贡献按前序账本求和后落入目标二分线交点界。 | component summation |
| `SelfContainedBipartiteLineIntersectionBoundClosed` | `true` | `true` | 二分 Guth-Katz/Kollar 线交点界在作者侧吸收闭合。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `SelfContainedPointPlaneIncidenceProofClosed` | `false` | `false` | 点-平面 incidence 还需把 de Zeeuw 字典与本线交点界做最终回接证书。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | RNRS/Rudnev 输入仍等待点-平面 incidence 回接。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合二分线交点界；未宣称行/列命题无条件闭合。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 4. 下一真正自足目标

```text
SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof
Absorb closed bipartite line-intersection bound into de Zeeuw point-plane incidence reduction
```
