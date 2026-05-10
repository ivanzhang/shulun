# Prime Matrix strict RKS23 Fano 次数与普通线证书

**状态：** `fano_ruling_curve_degree_and_ordinary_line_bound_closed_remaining_directrix_and_cayley_salmon`

当前唯一内部自足线继续下钻并关闭 Fano 原子的一半：ruling Fano 曲线次数界与普通线 O(d) 相交界。用 generic Schubert divisor，也就是与一条 generic line 相交的直线条件，计算 Fano 曲线次数；每条满足该条件的 ruling line 给出 generic line 与曲面 S 的一个交点，所以次数至多 d。因此任何普通 contained line 的 Schubert divisor 与 ruling curve 交数至多 d，普通线贡献闭合。剩余只在异常 directrix 型线界和 Cayley-Salmon flecnode 判据；row_column_unconditional_closed 仍保持 false。

```text
fano_ruling_curve_degree_bound_closed=true
ordinary_ruled_line_od_intersection_bound_closed=true
exceptional_directrix_line_bound_closed=false
cayley_salmon_flecnode_criterion_closed=false
row_column_unconditional_closed=false
```

## 1. Fano 次数证明

| field | value |
| --- | --- |
| `surface` | irreducible singly ruled surface S in P^3 of degree d, excluding plane/quadric cases already handled |
| `ruling_curve` | let C be the one-dimensional ruling component of F_1(S) in G(1,3) |
| `degree_measure` | degree of C is intersection with a generic Schubert divisor Sigma_m of lines meeting a generic line m |
| `generic_line_argument` | for generic m not contained in S, each ruling line meeting m gives an intersection point in m cap S |
| `bound` | \|m cap S\|<=d by Bezout, hence deg(C)<=d |
| `scope` | this proves the ordinary-line degree input; it does not bound exceptional lines whose Schubert divisor contains C |

## 2. 普通线转移

| field | value |
| --- | --- |
| `ordinary_line` | a contained line ell is ordinary if C is not contained in Sigma_ell |
| `schubert_intersection` | ruling lines meeting ell are C cap Sigma_ell |
| `degree_bound` | \|C cap Sigma_ell\|<=deg(C)<=d, up to harmless multiplicity conventions |
| `result` | ordinary contained lines meet O(d) ruling lines |
| `downstream` | the prior component accounting already absorbs ordinary O(d) contributions into O(\|L\|^(1/2)\|M\|) |

## 3. 剩余 directrix 异常线

| field | value |
| --- | --- |
| `exceptional_line` | ell is exceptional if C is contained in Sigma_ell, equivalently ell meets every ruling line |
| `needed_bound` | there are O(1), classically at most two, such directrix-type exceptional lines outside plane/quadric cases |
| `why_still_open` | this requires a separate directrix/Grassmannian incidence argument; it is not implied by deg(C)<=d alone |
| `remaining_atom` | SelfContainedExceptionalDirectrixLineBoundForSinglyRuledSurface |

## 4. 剩余源头原子

| atom | closed | why_remaining |
| --- | --- | --- |
| `SelfContainedExceptionalDirectrixLineBoundForSinglyRuledSurface` | `false` | must prove only O(1) lines have Schubert divisors containing the ruling Fano curve |
| `SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic` | `false` | must prove Flec(F) vanishing identically on the surface forces ruledness |

## 5. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousFanoFrontierReady` | `true` | `true` | 上一证书已把 ruled 几何压成 Fano 曲线次数/异常线界。 | SelfContainedFanoCurveDegreeAndExceptionalLineBoundForSinglyRuledSurface |
| `GenericSchubertDegreeArgumentClosed` | `true` | `true` | 用 generic line 的 Schubert divisor 计算 Fano ruling 曲线次数。 | SelfContainedFanoRulingCurveDegreeBoundForSinglyRuledSurface |
| `FanoRulingCurveDegreeBoundClosed` | `true` | `true` | 由 generic line 与 S 的 Bezout 交数得到 deg(C)<=d。 | SelfContainedFanoRulingCurveDegreeBoundForSinglyRuledSurface |
| `OrdinaryRuledLineOdIntersectionBoundClosed` | `true` | `true` | 若 C 不含于 Sigma_ell，则 ell 只与 O(d) 条 ruling 线相交。 | SelfContainedOrdinaryRuledLineOdIntersectionBound |
| `OrdinaryContributionLedgerClosed` | `true` | `true` | 普通线 O(d) 贡献与前序 ruled component 账本严格对接。 | ordinary contribution closed |
| `ExceptionalDirectrixLineBoundClosed` | `false` | `false` | 仍需证明 Schubert divisor 包含 C 的 directrix 型异常线只有 O(1)。 | SelfContainedExceptionalDirectrixLineBoundForSinglyRuledSurface |
| `FanoCurveDegreeAndExceptionalLineBoundClosed` | `false` | `false` | Fano 次数界已闭合，但异常线界未闭合。 | SelfContainedFanoCurveDegreeAndExceptionalLineBoundForSinglyRuledSurface |
| `RuledSurfaceRulingGeometryClosed` | `false` | `false` | ruled 几何仍等待异常 directrix 界。 | SelfContainedRuledSurfaceRulingAndExceptionalLineGeometry |
| `CayleySalmonFlecnodeCriterionClosed` | `false` | `false` | Cayley-Salmon 判据仍未作者侧内联。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `SelfContainedFlecnodeCayleySalmonPackClosed` | `false` | `false` | 结构包现在剩 directrix 异常线界和 Cayley-Salmon 判据。 | SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack |
| `SinglyRuledExceptionalLineTheoremClosed` | `false` | `false` | singly-ruled 分支仍等待异常 directrix 界。 | SelfContainedSinglyRuledSurfaceExceptionalLineTheorem |
| `NonRuledLineIntersectionTheoremClosed` | `false` | `false` | non-ruled 分支等待 Cayley-Salmon 判据。 | SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem |
| `RuledAndNonRuledComponentLineCountClosed` | `false` | `false` | 两个源头原子未内联前，ruled/non-ruled 总包仍未闭合。 | SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack |
| `SelfContainedKollarRuledSurfacePackageClosed` | `false` | `false` | Kollár/Guth-Katz 曲面结构包仍未作者侧自足闭合。 | SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack |
| `SelfContainedBipartiteLineIntersectionBoundClosed` | `false` | `false` | 二分线交点界仍依赖曲面结构包。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `SelfContainedPointPlaneIncidenceProofClosed` | `false` | `false` | 点-平面 incidence 仍依赖二分线交点界。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | RNRS/Rudnev 输入仍未作者侧自足闭合。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合 Fano 次数界和普通线界；未宣称行/列命题无条件闭合。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 6. 下一真正自足目标

```text
SelfContainedCayleySalmonAndFanoRuledSurfaceStructurePack
SelfContainedExceptionalDirectrixLineBoundForSinglyRuledSurface + SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic
```
