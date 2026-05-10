# Prime Matrix strict RKS23 directrix-锥面二分证书

**状态：** `cone_vertex_exceptional_branch_closed_remaining_noncone_directrix_and_cayley_salmon`

当前唯一内部自足线继续下钻并修正 directrix 异常线口径：Schubert divisor 包含 Fano ruling 曲线时，锥面/公共顶点星形分支可能产生一族异常生成线，但这些线的互交贡献塌缩为单个顶点，在线交点计数中已可吸收。因此异常线剩余被正确压成非锥 directrix 数量界，而不是错误地全局宣称异常线至多两条。剩余源头原子仍是非锥 directrix 界与 Cayley-Salmon flecnode 判据；row_column_unconditional_closed 仍保持 false。

```text
cone_vertex_star_contribution_closed=true
noncone_directrix_line_bound_closed=false
cayley_salmon_flecnode_criterion_closed=false
row_column_unconditional_closed=false
```

## 1. 修正后的异常模型

| field | value |
| --- | --- |
| `old_risk` | Schubert divisor contains the ruling Fano curve does not always mean only finitely many exceptional lines |
| `cone_countercase` | for a cone, every generator meets every other generator at the vertex, so many generators satisfy the Schubert containment condition |
| `correct_measure` | the line-intersection theorem counts distinct intersection points, not pairs of lines |
| `repair` | split exceptional behavior into cone vertex-star collapse and non-cone directrix lines |

## 2. 锥面公共顶点分支

| field | value |
| --- | --- |
| `case` | all or a one-parameter subfamily of ruling lines share a common vertex point O |
| `intersection_points` | all mutual intersections created by that star contribute the single point O |
| `contribution` | one point per irreducible component is O(number of components), already absorbed by the existing component/degree ledger |
| `closed_scope` | the cone/star branch no longer needs an O(1) exceptional-line count |

## 3. 非锥 directrix 分支

| field | value |
| --- | --- |
| `case` | the ruling family is not a common-vertex star |
| `directrix_line` | a line ell with C contained in Sigma_ell meets every ruling line without all intersections collapsing to one vertex |
| `needed_bound` | only O(1), classically at most two, such directrix lines exist outside plane/quadric/common-vertex cases |
| `remaining_atom` | SelfContainedNonConeFanoDirectrixLineBoundForSinglyRuledSurface |

## 4. 剩余源头原子

| atom | closed | why_remaining |
| --- | --- | --- |
| `SelfContainedNonConeFanoDirectrixLineBoundForSinglyRuledSurface` | `false` | must prove the non-cone Fano curve admits only O(1) Schubert-contained directrix lines |
| `SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic` | `false` | must prove Flec(F) vanishing identically on the surface forces ruledness |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousDirectrixFrontierReady` | `true` | `true` | 上一证书已关闭 Fano 次数界和普通线界，只剩异常 directrix 与 Cayley-Salmon。 | SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack |
| `SchubertExceptionalDefinitionRefined` | `true` | `true` | 修正异常线定义：Schubert 包含须分离锥面公共顶点塌缩。 | exceptional definition refined |
| `ConeVertexStarBranchIdentified` | `true` | `true` | 识别出锥面/公共顶点分支中可有一族 Schubert-异常生成线。 | SelfContainedConeVertexStarExceptionalCollapseContribution |
| `ConeVertexStarContributionClosed` | `true` | `true` | 锥面星形分支贡献的是单个交点而非大量不同交点，已由交点计数账本吸收。 | SelfContainedConeVertexStarExceptionalCollapseContribution |
| `NonConeDirectrixReductionClosed` | `true` | `true` | 异常线界的真正剩余被压到非锥 directrix 线数量界。 | SelfContainedNonConeFanoDirectrixLineBoundForSinglyRuledSurface |
| `OverstrongTwoDirectrixClaimQuarantined` | `true` | `true` | 隔离早先过强的“异常线至多两条”口径；它只适用于非锥 directrix 分支。 | safety correction closed |
| `NonConeDirectrixLineBoundClosed` | `false` | `false` | 尚未作者侧证明非锥 ruling Fano 曲线只有 O(1) 条 directrix 线。 | SelfContainedNonConeFanoDirectrixLineBoundForSinglyRuledSurface |
| `ExceptionalDirectrixLineBoundClosed` | `false` | `false` | 锥面分支已闭合，但非锥 directrix 数量界未闭合。 | SelfContainedExceptionalDirectrixLineBoundForSinglyRuledSurface |
| `FanoCurveDegreeAndExceptionalLineBoundClosed` | `false` | `false` | Fano 次数界和普通线界已闭合，异常 directrix 总界仍差非锥原子。 | SelfContainedFanoCurveDegreeAndExceptionalLineBoundForSinglyRuledSurface |
| `RuledSurfaceRulingGeometryClosed` | `false` | `false` | ruled 几何仍等待非锥 directrix 原子。 | SelfContainedRuledSurfaceRulingAndExceptionalLineGeometry |
| `CayleySalmonFlecnodeCriterionClosed` | `false` | `false` | Cayley-Salmon 判据仍未作者侧内联。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `SelfContainedFlecnodeCayleySalmonPackClosed` | `false` | `false` | 结构包现在剩非锥 directrix 界和 Cayley-Salmon 判据。 | SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack |
| `SinglyRuledExceptionalLineTheoremClosed` | `false` | `false` | singly-ruled 分支等待非锥 directrix 界。 | SelfContainedSinglyRuledSurfaceExceptionalLineTheorem |
| `NonRuledLineIntersectionTheoremClosed` | `false` | `false` | non-ruled 分支等待 Cayley-Salmon 判据。 | SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem |
| `RuledAndNonRuledComponentLineCountClosed` | `false` | `false` | 两个源头原子未内联前，ruled/non-ruled 总包仍未闭合。 | SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack |
| `SelfContainedKollarRuledSurfacePackageClosed` | `false` | `false` | Kollár/Guth-Katz 曲面结构包仍未作者侧自足闭合。 | SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack |
| `SelfContainedBipartiteLineIntersectionBoundClosed` | `false` | `false` | 二分线交点界仍依赖曲面结构包。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `SelfContainedPointPlaneIncidenceProofClosed` | `false` | `false` | 点-平面 incidence 仍依赖二分线交点界。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | RNRS/Rudnev 输入仍未作者侧自足闭合。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步修正并压缩 directrix 异常线分支；未宣称行/列命题无条件闭合。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 6. 下一真正自足目标

```text
SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack
SelfContainedNonConeFanoDirectrixLineBoundForSinglyRuledSurface + SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic
```
