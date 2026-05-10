# Prime Matrix strict RKS23 非锥 directrix 界证书

**状态：** `noncone_directrix_and_singly_ruled_branch_closed_remaining_only_cayley_salmon`

当前唯一内部自足线继续突破并关闭 ruled/directrix 源头原子。相交 directrix 线会迫使平面或公共顶点锥面分支，均已在前序账本中处理；在剩余非锥分支中 directrix 必 pairwise skew。若存在三条 skew directrix，所有 ruling line 都是三条 skew 线的公共横截线，因而填满唯一 smooth quadric，迫使当前不可约曲面为已分离的二次曲面。故非锥 directrix 至多两条。至此 singly-ruled 分支闭合，唯一内部自足剩余压成 Cayley-Salmon flecnode 判据；row_column_unconditional_closed 仍保持 false。

```text
noncone_directrix_line_bound_closed=true
exceptional_directrix_line_bound_closed=true
singly_ruled_exceptional_line_theorem_closed=true
cayley_salmon_flecnode_criterion_closed=false
row_column_unconditional_closed=false
```

## 1. 相交 directrix 分支

| field | value |
| --- | --- |
| `claim` | two distinct non-cone directrix lines cannot intersect outside already closed degeneracies |
| `reason` | if directrices ell1 and ell2 meet at O, any ruling line meeting both either lies in the plane span(ell1,ell2) or passes through O |
| `plane_exit` | infinitely many ruling lines in the span plane force a plane component, already separated |
| `cone_exit` | otherwise the ruling family has common vertex O, the cone/star branch already closed |
| `consequence` | in the remaining non-cone non-plane branch, directrix lines are pairwise skew |

## 2. 三条 skew directrix 分支

| field | value |
| --- | --- |
| `claim` | three pairwise skew directrix lines force the excluded quadric case |
| `transversal_fact` | common transversals to three skew lines in P^3 form one ruling of a unique smooth quadric |
| `ruling_effect` | every ruling line of S meets all three directrices, so the ruling Fano curve lies in that transversal ruling |
| `surface_effect` | an infinite ruling family fills the quadric; irreducibility forces S to equal that quadric |
| `consequence` | after quadrics are separated, at most two non-cone directrix lines remain |

## 3. 闭合转移

| field | value |
| --- | --- |
| `ordinary_lines` | ordinary line O(d) bound was closed in the Fano degree certificate |
| `cone_exceptional` | common-vertex cone/star exceptional branch was closed in the directrix-cone dichotomy certificate |
| `noncone_exceptional` | this certificate proves at most two non-cone directrix lines |
| `ruled_branch_result` | singly-ruled exceptional-line theorem is now closed for the line-intersection contribution ledger |

## 4. 剩余源头原子

| atom | closed | why_remaining |
| --- | --- | --- |
| `SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic` | `false` | must prove Flec(F) vanishing identically on the surface forces ruledness |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousNonConeDirectrixFrontierReady` | `true` | `true` | 上一证书已关闭锥面分支，只剩非锥 directrix 界与 Cayley-Salmon。 | SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack |
| `IntersectingDirectricesReducedToClosedDegeneracies` | `true` | `true` | 相交 directrix 线迫使平面分支或公共顶点锥面分支，均已闭合。 | intersecting directrix branch closed |
| `SkewThreeDirectricesForceQuadricClosed` | `true` | `true` | 三条 pairwise skew directrix 线强迫 ruling 落在唯一 quadric 上，回到已分离的二次曲面分支。 | three skew directrices -> quadric |
| `NonConeDirectrixLineBoundClosed` | `true` | `true` | 非锥、非平面、非二次曲面分支中 directrix 异常线至多两条。 | SelfContainedNonConeFanoDirectrixLineBoundForSinglyRuledSurface |
| `ExceptionalDirectrixLineBoundClosed` | `true` | `true` | 锥面分支和非锥 directrix 分支均已闭合。 | SelfContainedExceptionalDirectrixLineBoundForSinglyRuledSurface |
| `FanoCurveDegreeAndExceptionalLineBoundClosed` | `true` | `true` | Fano 次数界、普通线界、异常 directrix 界均已闭合。 | SelfContainedFanoCurveDegreeAndExceptionalLineBoundForSinglyRuledSurface |
| `RuledSurfaceRulingGeometryClosed` | `true` | `true` | singly-ruled 分支所需 ruling/异常线几何已闭合。 | SelfContainedRuledSurfaceRulingAndExceptionalLineGeometry |
| `SinglyRuledExceptionalLineTheoremClosed` | `true` | `true` | singly-ruled 分支的线交点贡献闭合。 | SelfContainedSinglyRuledSurfaceExceptionalLineTheorem |
| `CayleySalmonFlecnodeCriterionClosed` | `false` | `false` | Cayley-Salmon 判据仍未作者侧内联。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `SelfContainedFlecnodeCayleySalmonPackClosed` | `false` | `false` | 结构包现在唯一剩余是 Cayley-Salmon flecnode 判据。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `NonRuledLineIntersectionTheoremClosed` | `false` | `false` | non-ruled 分支仍等待 Cayley-Salmon 判据。 | SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem |
| `RuledAndNonRuledComponentLineCountClosed` | `false` | `false` | ruled 分支已闭合，但 non-ruled 分支仍差 Cayley-Salmon。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `SelfContainedKollarRuledSurfacePackageClosed` | `false` | `false` | Kollár/Guth-Katz 曲面结构包只剩 Cayley-Salmon 原子。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `SelfContainedBipartiteLineIntersectionBoundClosed` | `false` | `false` | 二分线交点界仍依赖最后 Cayley-Salmon 原子。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `SelfContainedPointPlaneIncidenceProofClosed` | `false` | `false` | 点-平面 incidence 仍依赖二分线交点界。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | RNRS/Rudnev 输入仍未作者侧自足闭合。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步闭合 ruled/directrix 分支；未宣称行/列命题无条件闭合。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 6. 下一真正自足目标

```text
SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic
SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic
```
