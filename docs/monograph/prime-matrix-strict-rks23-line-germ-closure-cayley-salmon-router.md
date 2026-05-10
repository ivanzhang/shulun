# Prime Matrix strict RKS23 线芽闭包与 Cayley-Salmon 证书

**状态：** `line_germ_closure_and_cayley_salmon_closed_remaining_incidence_absorption`

本步闭合 Cayley-Salmon 的最后源头原子。Monge 延拓已经给出一般点线芽；线芽代数性使整条 projective line 包含于曲面，再通过 Grassmannian incidence 的维数二分法得到覆盖曲面的代数直线族。因此 Cayley-Salmon flecnode 判据闭合；但二分线交点界、点-平面 incidence 与行/列命题仍需后续吸收审计。

```text
algebraic_line_germ_closure_closed=true
cayley_salmon_flecnode_criterion_closed=true
non_ruled_line_intersection_theorem_closed=true
self_contained_kollar_ruled_surface_package_closed=true
self_contained_bipartite_line_intersection_bound_closed=false
row_column_unconditional_closed=false
```

## 1. 线芽闭包证明

| field | value |
| --- | --- |
| `line_germ_extension` | if a projective line germ lies in Z(F), then F restricted to the full line vanishes as a univariate polynomial |
| `incidence_variety` | I={(x,ell): x in ell and ell subset Z(F)} is algebraic because line containment is finitely many coefficient equations |
| `dominance` | Monge prolongation gives a line through each generic smooth point, so the projection I -> Z(F) is dominant |
| `grassmannian_image` | let Gamma be the Zariski closure of the image of I in G(1,3) |
| `zero_dim_case` | dim Gamma=0 cannot dominate an irreducible surface by finitely many lines |
| `one_dim_case` | dim Gamma=1 is exactly a one-parameter line family covering a dense open subset |
| `two_dim_case` | if dim Gamma>=2, a generic point has a positive-dimensional pencil of contained lines; this forces the tangent plane section to have a plane component, hence the irreducible surface is a plane |
| `conclusion` | in every case the irreducible component is ruled |

## 2. Cayley-Salmon 转移

| field | value |
| --- | --- |
| `input` | F irreducible squarefree, deg(F)<char(k), and Flec(F) vanishes on Z(F) |
| `monge` | previous certificate turns the flecnode condition into genuine line germs through generic points |
| `closure` | this certificate globalizes those germs through Grassmannian incidence |
| `result` | Z(F) is ruled; hence the Cayley-Salmon flecnode criterion is closed in the degree<p regime |
| `nonruled_exit` | therefore in the non-ruled case Flec(F) is not identically zero on F, so Bezout with deg Flec(F)<=11d gives the O(d^3) line-intersection scale |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousLineGermFrontierReady` | `true` | `true` | 上一证书已闭合 Monge 延拓，唯一 Cayley-Salmon 剩余是线芽闭包。 | SelfContainedAlgebraicLineGermClosureCoveringSurface |
| `LineGermExtendsToProjectiveLineClosed` | `true` | `true` | 代数曲面中的线芽使 F 在线上有无穷零点，故整条 projective line 包含于曲面。 | line germ -> full line |
| `GrassmannianIncidenceClosed` | `true` | `true` | 直线包含条件是 Grassmannian 上有限个多项式系数方程。 | algebraic incidence |
| `DominantProjectionClosed` | `true` | `true` | Monge 延拓给出一般点上线，因此 incidence 到曲面的投影支配。 | dominant incidence projection |
| `GrassmannianDimensionDichotomyClosed` | `true` | `true` | Grassmannian 线族像维数为 1 则 ruled；维数至少 2 则一般点有线笔，迫使平面分支。 | dimension dichotomy |
| `AlgebraicLineGermClosureClosed` | `true` | `true` | 一般点线芽已闭包为覆盖曲面的代数直线族。 | SelfContainedAlgebraicLineGermClosureCoveringSurface |
| `CayleySalmonFlecnodeCriterionClosed` | `true` | `true` | Flec(F) 在曲面上恒零推出曲面 ruled 的 Cayley-Salmon 判据已闭合。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `NonRuledLineIntersectionTheoremClosed` | `true` | `true` | non-ruled 情形 Flec(F) 不恒零，Bezout 给出 O(d^3) 线交点控制。 | SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem |
| `RuledAndNonRuledComponentLineCountClosed` | `true` | `true` | ruled 分支此前已闭合，non-ruled 分支现由 Cayley-Salmon 闭合。 | SelfContainedKollarRuledSurfacePackage |
| `SelfContainedKollarRuledSurfacePackageClosed` | `true` | `true` | 曲面结构包在作者侧已闭合；后续 incidence/RNRS 仍需独立吸收审计。 | SelfContainedKollarRuledSurfacePackage |
| `SelfContainedBipartiteLineIntersectionBoundClosed` | `false` | `false` | 曲面结构包已就绪，但二分线交点界仍需单独吸收证书对接。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `SelfContainedPointPlaneIncidenceProofClosed` | `false` | `false` | 点-平面 incidence 仍需在吸收证书中从二分线交点界回接。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | RNRS/Rudnev 输入仍未在本证书中宣称闭合。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合 Cayley-Salmon 曲面结构源头；未宣称行/列命题无条件闭合。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 4. 下一真正自足目标

```text
SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage
Absorb closed Cayley-Salmon/Kollar surface package into bipartite line-intersection bound
```
