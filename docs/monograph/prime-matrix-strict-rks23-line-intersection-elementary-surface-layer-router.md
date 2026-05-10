# Prime Matrix strict RKS23 线交点初等曲面层证书

**状态：** `bipartite_line_intersection_elementary_surface_layer_closed_remaining_ruled_surface_package`

当前唯一内部自足线继续推进：二分线交点界中的初等曲面层已经闭合。具体闭合了三项：用多项式维数计数构造穿过 L 中全部直线的低次数曲面；用一元 Bézout 控制不含于该曲面的 M 直线；用 quadric 退化假设处理平面/二次曲面分量。真正剩余因此缩为 ruled/non-ruled 曲面分量的 Kollár 型线计数与正特征次数截断。在该包内联前，row_column_unconditional_closed 仍必须保持 false。

```text
elementary_surface_layer_closed=true
ruled_and_nonruled_component_line_count_closed=false
self_contained_bipartite_line_intersection_bound_closed=false
row_column_unconditional_closed=false
```

## 1. 插值曲面

| field | value |
| --- | --- |
| `input` | n=\|L\| affine lines in F^3 |
| `degree_choice` | choose D=C*ceil(sqrt(n)) with C large enough |
| `unknowns` | dimension of polynomials of degree <=D in three variables is binomial(D+3,3) |
| `constraints_per_line` | vanishing on one line imposes at most D+1 linear conditions after restricting to a univariate polynomial |
| `dimension_count` | binomial(D+3,3)>n(D+1) for an absolute C, so a nonzero polynomial vanishing on all L exists |
| `output` | there is a surface S={F=0} of degree O(\|L\|^(1/2)) containing all lines of L |

## 2. 非包含线 Bézout 计数

| field | value |
| --- | --- |
| `input` | a line m in M not contained in S={F=0} |
| `restriction` | F restricted to m is a nonzero univariate polynomial of degree <=D |
| `intersection_bound` | m meets S in at most D points, counted without multiplicity for incidence purposes |
| `sum` | all such M-lines contribute O(D\|M\|)=O(\|L\|^(1/2)\|M\|) |

## 3. 平面/二次曲面退化分量

| field | value |
| --- | --- |
| `component_types` | plane or quadric irreducible/reducible components of the interpolating surface |
| `degeneracy_hypothesis` | no quadric contains s lines of L and t lines of M |
| `plane_handling` | a plane is contained in a reducible quadric after adjoining another plane, so the same s,t exclusion applies |
| `charge` | each such component contains fewer than s L-lines or fewer than t M-lines; charge at most s\|M_i\| or t\|L_i\| |
| `sum` | summing over components gives O(t\|L\|+s\|M\|) |

## 4. 剩余 ruled 包

| field | value |
| --- | --- |
| `singly_ruled` | need a self-contained proof that only O(1) exceptional lines per singly ruled component can meet infinitely many component lines, while all other lines meet O(deg S_i) lines |
| `non_ruled` | need a self-contained proof that a non-ruled component of degree d has O(d^3) line-line intersection points among contained lines |
| `positive_characteristic_cutoff` | need the degree<characteristic condition, tied to \|L\|=O(p^2), for the non-ruled line-count theorem |
| `why_not_closed` | these are algebraic-geometry structure theorems, not consequences of the elementary interpolation/Bézout layer alone |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousLineIntersectionFrontierReady` | `true` | `true` | 上一证书已把真正剩余固定为二分 Guth-Katz/Kollár 线交点证明包。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `InterpolationSurfaceThroughAllLinesClosed` | `true` | `true` | 用三变量多项式维数计数构造次数 O(\|L\|^1/2) 的曲面穿过 L 中全部直线。 | InterpolationSurfaceThroughAllLinesOfL |
| `OffSurfaceBezoutIntersectionCountClosed` | `true` | `true` | 不含于曲面的 M 直线每条至多贡献 deg(S) 个交点，总贡献 O(\|L\|^1/2\|M\|)。 | OffSurfaceBezoutIntersectionCount |
| `PlaneAndQuadricDegenerateComponentAccountClosed` | `true` | `true` | 平面/二次曲面分量由 quadric 退化假设收费到 t\|L\|+s\|M\|。 | PlaneAndQuadricDegenerateComponentAccount |
| `ElementarySurfaceLayerClosed` | `true` | `true` | 线交点证明中的初等插值曲面层已经闭合。 | elementary layer closed |
| `RuledAndNonRuledComponentLineCountClosed` | `false` | `false` | 单 ruled 与非 ruled 分量的线计数仍需 Kollár/Guth-Katz 型代数几何包。 | SelfContainedRuledAndNonRuledSurfaceLineCountingWithPositiveCharacteristicCutoff |
| `SelfContainedKollarRuledSurfacePackageClosed` | `false` | `false` | Kollár ruled-surface 与正特征次数截断尚未完整内联。 | SelfContainedRuledAndNonRuledSurfaceLineCountingWithPositiveCharacteristicCutoff |
| `SelfContainedBipartiteLineIntersectionBoundClosed` | `false` | `false` | 二分线交点界还差 ruled/non-ruled 分量计数，不能算闭合。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `SelfContainedPointPlaneIncidenceProofClosed` | `false` | `false` | 点-平面 incidence 依赖二分线交点界，故仍未闭合。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | RNRS/Rudnev 输入仍未作者侧自足闭合。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合初等曲面层；未宣称行/列命题无条件闭合。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 6. 下一真正自足目标

```text
SelfContainedRuledAndNonRuledSurfaceLineCountingWithPositiveCharacteristicCutoff
SelfContainedKollarRuledSurfaceExceptionalLineAndNonRuledLineIntersectionTheorems
```
