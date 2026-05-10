# Prime Matrix strict RKS23 Monge 简单根分支证书

**状态：** `monge_simple_root_branch_closed_remaining_parabolic_hessian_and_line_germ_closure`

当前主攻点继续保持 Cayley-Salmon 内部自足线，不换命题。本步把 Monge 延拓写成显式局部方程，并闭合简单根/非抛物分支：由 0=L3+2(Xu)A 与 A!=0 推出方向场沿自身不变，从而生成真实直线芽。剩余压缩为 A=0 的 Hessian 退化 developable 分支，以及后续线芽代数闭包。

```text
monge_simple_branch_closed=true
parabolic_hessian_developable_branch_closed=false
monge_prolongation_closed=false
algebraic_line_germ_closure_closed=false
cayley_salmon_flecnode_criterion_closed=false
row_column_unconditional_closed=false
```

## 1. 局部正规形

| field | value |
| --- | --- |
| `chart` | at a smooth generic point write the surface as z=f(x,y) |
| `direction` | normalize a tangent projective direction as X=partial_x+u partial_y+(f_x+u f_y) partial_z |
| `line_test` | the candidate line is s -> (x+s, y+u s, z+s(f_x+u f_y)) |
| `second_contact` | L2=f_xx+2u f_xy+u^2 f_yy=0 |
| `third_contact` | L3=f_xxx+3u f_xxy+3u^2 f_xyy+u^3 f_yyy=0 |
| `simple_root_factor` | A=f_xy+u f_yy=(1/2) partial_u L2 |

## 2. Monge 简单根恒等式

| field | value |
| --- | --- |
| `branch_equation` | L2(x,y,u(x,y))=0 on the dominating contact branch |
| `differentiate_along_X` | (partial_x+u partial_y)L2 + (X u) partial_u L2 = 0 |
| `expanded_identity` | 0=L3+2(X u)A |
| `simple_root_case` | if A!=0 and L3=0, then X u=0 |
| `straightness` | X(f_x+u f_y)=L2+(X u)f_y=0, so the full projective direction is constant along X-integral curves |
| `consequence` | each simple-root integral curve is a straight projective line germ contained in the surface |

## 3. 退化分支

| field | value |
| --- | --- |
| `condition` | A=f_xy+u f_yy=0 together with L2=0 |
| `equivalent_shape` | the second fundamental form has a repeated/asymptotic direction; in graph form this is the parabolic Hessian branch |
| `why_not_closed_here` | the identity 0=L3+2(Xu)A loses the factor that forces Xu=0 |
| `next_needed_fact` | prove the Hessian-degenerate branch is developable and hence ruled, or reduce it to already closed plane/cone/tangent-developable cases |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| `PreviousMongeFrontierReady` | `true` | `true` | 上一证书已把 Cayley-Salmon 的真正剩余压成 Monge 延拓与线芽闭包。 | SelfContainedMongeProlongationFiniteOrderContactToLineForFlecnodeSurfaces |
| `DegreeLessThanCharacteristicImported` | `true` | `true` | degree<p 截断允许使用三阶 Hasse/jet 接触方程。 | degree<p imported |
| `GraphChartNormalFormClosed` | `true` | `true` | 在光滑一般点把曲面写成 z=f(x,y)，并规范化切向方向。 | graph chart normal form |
| `ContactEquationNormalFormClosed` | `true` | `true` | 二阶与三阶接触方程化为 L2=0、L3=0。 | L2/L3 contact equations |
| `SimpleRootMongeIdentityClosed` | `true` | `true` | 沿切向方向微分 L2 得到 0=L3+2(Xu)A。 | Monge identity |
| `NonParabolicStraightLineIntegralClosed` | `true` | `true` | A!=0 时由 L3=0 推出 Xu=0，从而切向 projective direction 沿积分曲线恒定。 | SelfContainedMongeSimpleRootBranchFiniteOrderContactToLine |
| `MongeSimpleRootBranchClosed` | `true` | `true` | Monge 延拓的简单根/非抛物分支已产生真实直线芽。 | SelfContainedMongeSimpleRootBranchFiniteOrderContactToLine |
| `ParabolicHessianDevelopableBranchClosed` | `false` | `false` | A=0 时强制 Xu 的因子消失，剩余为 Hessian 退化 developable 分支。 | SelfContainedParabolicHessianDevelopableBranchToRuledness |
| `MongeProlongationClosed` | `false` | `false` | 简单根分支已闭合；整个 Monge 延拓仍等待抛物/Hessian 退化分支。 | SelfContainedParabolicHessianDevelopableBranchToRuledness |
| `AlgebraicLineGermClosureClosed` | `false` | `false` | 即使产生线芽，仍需后续证明其 Zariski 闭包覆盖曲面。 | SelfContainedAlgebraicLineGermClosureCoveringSurface |
| `CayleySalmonFlecnodeCriterionClosed` | `false` | `false` | Monge 退化分支和线芽闭包未闭合前，Cayley-Salmon 仍未作者侧自足闭合。 | SelfContainedCayleySalmonFlecnodeCriterionInDegreeLessThanCharacteristic |
| `NonRuledLineIntersectionTheoremClosed` | `false` | `false` | non-ruled O(d^3) 分支仍等待 Cayley-Salmon 判据。 | SelfContainedNonRuledSurfaceLineIntersectionO_d3_Theorem |
| `SelfContainedBipartiteLineIntersectionBoundClosed` | `false` | `false` | 二分线交点界仍依赖 non-ruled 分支。 | SelfContainedBipartiteGuthKatzLineIntersectionBoundWithKollarRuledSurfacePackage |
| `SelfContainedPointPlaneIncidenceProofClosed` | `false` | `false` | 点-平面 incidence 仍依赖二分线交点界。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling` | `false` | `false` | RNRS/Rudnev 输入仍未作者侧自足闭合。 | SelfContainedRudnevPointPlaneIncidencePolynomialMethodProof |
| `RowColumnUnconditionalClosed` | `false` | `false` | 本步只闭合 Monge 简单根分支；未宣称行/列命题无条件闭合。 | SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling |

## 5. 下一真正自足目标

```text
SelfContainedParabolicHessianDevelopableBranchToRuledness
SelfContainedParabolicHessianDevelopableBranchToRuledness + SelfContainedAlgebraicLineGermClosureCoveringSurface
```
