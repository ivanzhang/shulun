# Prime Matrix strict RKS23 flecnode 多项式构造证书

**状态：** `flecnode_polynomial_construction_closed_remaining_cayley_salmon_and_ruled_geometry`

当前唯一内部自足线继续下钻并关闭一个真实结构原子：flecnode 多项式的构造与次数界。用一、二、三阶 Hasse 方向导数写出三阶接触条件，再对 projective 方向变量消元，得到 Flec(F)；安全次数界 deg Flec(F)<=11d 已足以支撑后续 Bezout。任何包含于 F=0 的直线都会落入 flecnode locus。但 Cayley-Salmon 判据和 singly-ruled 的 ruling/异常线几何仍未内联，所以 row_column_unconditional_closed 仍保持 false。

```text
flecnode_polynomial_construction_closed=true
cayley_salmon_flecnode_criterion_closed=false
ruled_surface_ruling_geometry_closed=false
row_column_unconditional_closed=false
```

## 1. 接触条件

| field | value |
| --- | --- |
| `surface` | let F(x,y,z) be a squarefree irreducible polynomial of degree d defining a component |
| `direction` | use a projective direction v=(u:v:w) |
| `first_contact` | D_v F=0 |
| `second_contact` | D_v^2 F=0 using Hasse derivatives in positive characteristic |
| `third_contact` | D_v^3 F=0 using Hasse derivatives, valid under the imported degree<p cutoff |
| `flecnode_condition` | a point is flecnodal if the three homogeneous equations in v have a nonzero projective solution |

## 2. 消元与次数界

| field | value |
| --- | --- |
| `method` | take the multihomogeneous resultant in the projective direction variables |
| `result` | obtain a polynomial Flec(F)(x,y,z) vanishing at every flecnodal point of F=0 |
| `coefficient_degrees` | the three contact equations have direction degrees 1,2,3 and x-degrees d-1,d-2,d-3 |
| `safe_degree_bound` | deg Flec(F)<=11d is enough for all downstream Bezout estimates |
| `classical_sharpening` | the classical Salmon flecnode polynomial has degree 11d-24; the internal chain only needs O(d) |

## 3. 包含线进入 flecnode locus

| field | value |
| --- | --- |
| `statement` | if an affine/projective line ell is contained in Z(F), then every nonsingular point of ell is flecnodal |
| `reason` | restricting F to ell gives the zero univariate polynomial, so the first three Hasse directional derivatives along ell vanish |
| `consequence` | every contained line lies in Z(F) cap Z(Flec(F)) outside harmless singular/exceptional points |
| `downstream_use` | if Flec(F) is not identically zero on F, Bezout with deg Flec(F)=O(d) gives the O(d^3) non-ruled line-intersection scale after the remaining Cayley-Salmon criterion |

## 4. 剩余原子

| atom | closed | why_remaining |
| --- | --- | --- |
| `SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic` | `false` | must prove Flec(F) vanishing identically on Z(F) forces the surface component to be ruled |
| `SelfContainedRuledSurfaceRulingAndExceptionalLineGeometry` | `false` | must prove the ruling-family and exceptional-line geometry for singly ruled components |

## 5. 外部校准锚点

| name | url | used_for |
| --- | --- | --- |
| Guth-Katz flecnode degree statement | https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p02-p.pdf | classical degree 11d-24 calibration; internal certificate uses the weaker safe O(d) bound |
| Katz flecnode exposition | https://arxiv.org/abs/1404.3412 | Cayley-Salmon/flecnode context and separation of construction from ruledness criterion |

## 6. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousFlecnodeFrontierReady` | `true` | `true` | 上一证书已把唯一剩余压成 flecnode/Cayley-Salmon 结构包三个原子。 | SelfContainedFlecnodeCayleySalmonRuledSurfaceStructurePack |
| `HasseDerivativeContactSetupClosed` | `true` | `true` | 一、二、三阶接触条件用 Hasse 方向导数统一处理，兼容正特征 degree<p 截断。 | directional contact equations closed |
| `ProjectiveDirectionEliminationClosed` | `true` | `true` | 通过方向变量的多重齐次消元得到 flecnode 多项式。 | resultant construction closed |
| `FlecnodeDegreeBoundClosed` | `true` | `true` | 得到 deg Flec(F)<=11d 的安全次数界，足够支撑后续 Bezout 账本。 | SelfContainedFlecnodePolynomialConstructionAndDegreeBound |
| `ContainedLineImpliesFlecnodeLocusClosed` | `true` | `true` | 整条直线包含于曲面时，沿该直线的一至三阶方向导数恒为零。 | contained line -> flecnode locus closed |
| `FlecnodePolynomialConstructionClosed` | `true` | `true` | flecnode 多项式的构造、次数界和包含线进入 flecnode locus 的部分已自足闭合。 | SelfContainedFlecnodePolynomialConstructionAndDegreeBound |
| `CayleySalmonFlecnodeCriterionClosed` | `false` | `false` | 尚未作者侧证明 Flec(F) 在曲面上恒零推出 ruled。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `RuledSurfaceRulingGeometryClosed` | `false` | `false` | 尚未作者侧证明 singly-ruled 曲面的 ruling 与异常线几何。 | SelfContainedRuledSurfaceRulingAndExceptionalLineGeometry |
| `SelfContainedFlecnodeCayleySalmonPackClosed` | `false` | `false` | 结构包还剩 Cayley-Salmon 判据和 ruled 几何，不能关闭总包。 | SelfContainedCayleySalmonCriterionAndRuledSurfaceRulingGeometry |
| `SinglyRuledExceptionalLineTheoremClosed` | `false` | `false` | 仍等待 ruled-surface 几何包。 | SelfContainedSinglyRuledSurfaceExceptionalLineTheorem |
| `NonRuledLineIntersectionTheoremClosed` | `false` | `false` | flecnode 构造已闭合，但仍等待 Cayley-Salmon 判据。 | SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem |
| `RuledAndNonRuledComponentLineCountClosed` | `false` | `false` | 两个剩余结构定理未内联前，ruled/non-ruled 总包仍未闭合。 | SelfContainedCayleySalmonCriterionAndRuledSurfaceRulingGeometry |
| `SelfContainedKollarRuledSurfacePackageClosed` | `false` | `false` | Kollár/Guth-Katz 曲面结构包仍未作者侧自足闭合。 | SelfContainedCayleySalmonCriterionAndRuledSurfaceRulingGeometry |
| `SelfContainedBipartiteLineIntersectionBoundClosed` | `false` | `false` | 二分线交点界仍依赖曲面结构包。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `SelfContainedPointPlaneIncidenceProofClosed` | `false` | `false` | 点-平面 incidence 仍依赖二分线交点界。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | RNRS/Rudnev 输入仍未作者侧自足闭合。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合 flecnode 多项式构造原子；未宣称行/列命题无条件闭合。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 7. 下一真正自足目标

```text
SelfContainedCayleySalmonCriterionAndRuledSurfaceRulingGeometry
SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic + SelfContainedRuledSurfaceRulingAndExceptionalLineGeometry
```
