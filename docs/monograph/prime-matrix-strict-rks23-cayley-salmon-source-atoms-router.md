# Prime Matrix strict RKS23 Cayley-Salmon 源头原子证书

**状态：** `cayley_salmon_reduced_to_monge_prolongation_and_line_germ_closure`

当前唯一内部自足线继续下钻 Cayley-Salmon flecnode 判据。本步闭合的是入口层：Flec(F) 在曲面上恒零时，三阶接触方向的 incidence variety 有支配曲面的代数分支。这还不是 ruledness；真正剩余被压成 Monge 延拓和线芽代数闭包两个源头原子。因此 row_column_unconditional_closed 仍保持 false。

```text
dominating_third_order_contact_branch_closed=true
monge_prolongation_closed=false
algebraic_line_germ_closure_closed=false
cayley_salmon_flecnode_criterion_closed=false
row_column_unconditional_closed=false
```

## 1. Cayley-Salmon 入口归约

| field | value |
| --- | --- |
| `input` | F irreducible, squarefree, deg(F)=d<char(k); Flec(F) vanishes on Z(F) |
| `generic_locus` | remove singular locus, coordinate hyperplane failures, and vertical direction charts; this does not change ruledness |
| `contact_incidence` | inside smooth points x of Z(F), impose first, second, and third Hasse directional contact equations in projective direction v |
| `dominant_branch` | because Flec(F)\|Z(F)=0, every generic x has at least one admissible v; an irreducible component of the incidence variety dominates Z(F) |
| `closed_part` | this gives an algebraic branch of third-order contact directions over a dense open subset |
| `remaining_part` | must prove this branch is not merely osculating, but integrates/prolongs to actual projective lines contained in the surface |

## 2. 本步已闭合子原子

| atom | closed | role |
| --- | --- | --- |
| `SelfContainedFlecnodeZeroDominatingThirdOrderContactBranch` | `true` | Flec(F)\|Z(F)=0 gives a dominating algebraic third-order contact direction branch |
| `SelfContainedSmoothGenericLocusAndDegreeLessThanCharacteristicJetTransfer` | `true` | the degree<p cutoff lets Hasse directional derivatives serve as the needed jet equations on the generic smooth locus |

## 3. 剩余两个源头原子

| atom | closed | role | hard_point |
| --- | --- | --- | --- |
| `SelfContainedMongeProlongationFiniteOrderContactToLineForFlecnodeSurfaces` | `false` | derive from the third-order contact branch the Monge characteristic equations whose integral curves have constant projective direction | third-order contact at each point is local finite-jet information; contained lines require a propagation theorem along the branch |
| `SelfContainedAlgebraicLineGermClosureCoveringSurface` | `false` | turn the local line germs produced by Monge prolongation into a Zariski one-parameter family of projective lines covering the surface | exclude isolated or chart-dependent formal germs and show the family survives after closure and exceptional-set removal |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousCayleySalmonFrontierReady` | `true` | `true` | 上一证书已把唯一剩余压成 Cayley-Salmon flecnode 判据。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `DegreeLessThanCharacteristicImported` | `true` | `true` | degree<p 截断已作为 Hasse/jet 传递前提导入。 | degree<p imported |
| `SmoothGenericLocusReductionClosed` | `true` | `true` | 去掉奇异点和有限个坏 chart 后，ruledness 的稠密开集判定不变。 | generic smooth locus |
| `ContactIncidenceDefinedClosed` | `true` | `true` | 三阶接触方向的代数 incidence variety 已由 flecnode 构造给出。 | third-order contact incidence |
| `DominatingThirdOrderContactBranchClosed` | `true` | `true` | Flec(F) 在曲面上恒零推出存在支配曲面的三阶接触方向分支。 | SelfContainedFlecnodeZeroDominatingThirdOrderContactBranch |
| `HasseToJetTransferClosed` | `true` | `true` | degree<p 下 Hasse 方向导数与所需三阶 jet 条件一致。 | Hasse jet transfer |
| `CayleySalmonSourceAtomsIdentified` | `true` | `true` | Cayley-Salmon 终端剩余已压成 Monge 延拓与线芽代数闭包两个源头原子。 | SelfContainedMongeProlongationFiniteOrderContactToLineForFlecnodeSurfaces + SelfContainedAlgebraicLineGermClosureCoveringSurface |
| `MongeProlongationClosed` | `false` | `false` | 尚需证明三阶接触方向分支沿自身传播并产生真实直线。 | SelfContainedMongeProlongationFiniteOrderContactToLineForFlecnodeSurfaces |
| `AlgebraicLineGermClosureClosed` | `false` | `false` | 尚需证明局部线芽闭包为覆盖曲面的代数直线族。 | SelfContainedAlgebraicLineGermClosureCoveringSurface |
| `CayleySalmonFlecnodeCriterionClosed` | `false` | `false` | 两个源头原子未闭合前，不能声称 Cayley-Salmon 作者侧自足闭合。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `NonRuledLineIntersectionTheoremClosed` | `false` | `false` | non-ruled O(d^3) 分支仍等待 Cayley-Salmon 判据。 | SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem |
| `SelfContainedBipartiteLineIntersectionBoundClosed` | `false` | `false` | 二分线交点界仍依赖 non-ruled 分支。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `SelfContainedPointPlaneIncidenceProofClosed` | `false` | `false` | 点-平面 incidence 仍依赖二分线交点界。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | RNRS/Rudnev 输入仍未作者侧自足闭合。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合 Cayley-Salmon 的接触分支入口；未宣称行/列命题无条件闭合。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 5. 下一真正自足目标

```text
SelfContainedMongeProlongationFiniteOrderContactToLineForFlecnodeSurfaces
SelfContainedMongeProlongationFiniteOrderContactToLineForFlecnodeSurfaces + SelfContainedAlgebraicLineGermClosureCoveringSurface
```
