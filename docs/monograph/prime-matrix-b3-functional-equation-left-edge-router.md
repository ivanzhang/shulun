# Prime Matrix B=3 函数方程左边界预算闭合证书

**状态：** `functional_equation_left_edge_closed_cleft4`

函数方程左边界预算已用 C_left=4 自足闭合。该闭合足以给左边界 O(log(T+3)) 输入，但还不足以证明凸性目标 C=2；下一步必须做 C=2 常数优化或明确改写水平边常数。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
functional_equation_left_edge_closed=true
C_chi=2.000000000000
C_left=4.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
FunctionalEquationLeftEdgeArgumentLedger
  =>
FunctionalEquationLeftEdgeArgumentClosedCleft4
```

## 2. 核心不等式

```text
s=-eta+it, eta=1/L, L=log(T+3), t>=1: zeta(s)=chi(s)zeta(1-s), log|chi(s)|<=2L, log|zeta(1-s)|<=L, log|s-1|<=L, hence log|F(s)|<=4L.
```

这里的 `chi` 预算来自函数方程中的 Gamma 比值。低于 `t=1` 的端点/低高度问题不在本账本中硬吞，后续仍由端点 convention 统一处理。

## 3. chi/Gamma 比值预算审计

| T | L | eta | chi envelope | 2L budget | chi margin | right zeta L | pole L | left F 4L |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | `1.609437912434` | `0.621334934560` | `3.191013317337` | `3.218875824868` | `0.027862507531` | `1.609437912434` | `1.609437912434` | `6.437751649736` |
| 10 | `2.564949357462` | `0.389871245251` | `3.668769039851` | `5.129898714923` | `1.461129675072` | `2.564949357462` | `2.564949357462` | `10.259797429846` |
| 100 | `4.634728988230` | `0.215762346092` | `4.703658855235` | `9.269457976459` | `4.565799121225` | `4.634728988230` | `4.634728988230` | `18.538915952919` |
| 10000 | `9.210640326985` | `0.108570084652` | `6.991614524612` | `18.421280653970` | `11.429666129358` | `9.210640326985` | `9.210640326985` | `36.842561307941` |
| 1e+06 | `13.815513557960` | `0.072382397933` | `9.294051140100` | `27.631027115920` | `18.336975975820` | `13.815513557960` | `13.815513557960` | `55.262054231839` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| FunctionalEquationLeftEdgeGateActive | `true` | `false` | 上一层唯一内部最窄点是函数方程左边界预算。 | FunctionalEquationLeftEdgeArgumentLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ZetaFunctionalEquationAvailable | `true` | `true` | zeta 函数方程已在 theta-Mellin 层闭合。 | 无函数方程形式剩余。 |
| RightEdgeEulerInputAvailable | `true` | `true` | 左边界 s=-eta+it 经 1-s 映到右边界 1+eta-it，Euler product 预算可复用。 | 无右边界剩余。 |
| ChiGammaRatioEnvelopeClosed | `true` | `true` | Gamma 比值给 \|chi(-eta+it)\|<=4(t+3)^(1/2+eta)，在 eta=1/L、T>=2 下由 2L 支付。 | ChiGammaRatioEnvelopeClosedCchi2 |
| LeftEdgePoleAndZetaBudgetClosed | `true` | `true` | log\|F\|<=log\|s-1\|+log\|chi(s)\|+log\|zeta(1-s)\| <= L+2L+L=4L。 | FunctionalEquationLeftEdgeArgumentClosedCleft4 |
| FunctionalEquationLeftEdgeArgumentLedger | `true` | `true` | 左边界函数方程预算闭合为 C_left=4；这不是 C=2 凸性目标的最优闭合。 | FunctionalEquationLeftEdgeArgumentClosedCleft4 |
| ConvexityC2OptimizationStillNext | `false` | `false` | 下一步需要判断 C_left=4 是否可压到凸性目标 C=2，或调整后续水平边常数。 | CriticalStripConvexityC2ConstantOptimizationLedger |
| HorizontalAndBacklundAggregationStillDownstream | `false` | `false` | 随后还需水平边聚合与 Backlund 总常数聚合。 | HorizontalVariationConstantAggregationLedger AND BacklundArgumentConstantAggregationLedger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityC2ConstantOptimizationLedger) AND HorizontalVariationConstantAggregationLedger) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND BacklundArgumentConstantAggregationLedger) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

唯一内部最窄点更新为 `CriticalStripConvexityC2ConstantOptimizationLedger`；随后是 `HorizontalVariationConstantAggregationLedger`、`BacklundArgumentConstantAggregationLedger`。
