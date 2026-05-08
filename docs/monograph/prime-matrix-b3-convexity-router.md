# Prime Matrix B=3 临界带凸性上界路由器

**状态：** `critical_strip_convexity_reduced_open`

临界带凸性账本尚未闭合。本步闭合了三线/PL 形式原理并确认右边界输入可用；真正剩余回到左边函数方程预算和 C=2 常数优化。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
critical_strip_convexity_reduced=true
critical_strip_convexity_self_contained_proved=false
C_convexity_target=2.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
CriticalStripConvexityLogZetaBoundNumericalLedger
  =>
(CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentLedger AND CriticalStripConvexityC2ConstantOptimizationLedger)
```

## 2. 三线结构

对 `F=(s-1)zeta(s)` 使用三线定理，而不是直接对有极点的 `zeta` 使用。若左右边界都给出 `log|F|<=2L`，则竖带内部也给出同一 `2L` 目标；但左边界和低高度常数尚未核算，所以本层仍是 open。

| T | L | eta | strip width | right target | left target | interior target |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | `1.609437912434` | `0.621334934560` | `2.242669869119` | `3.218875824868` | `3.218875824868` | `3.218875824868` |
| 10 | `2.564949357462` | `0.389871245251` | `1.779742490503` | `5.129898714923` | `5.129898714923` | `5.129898714923` |
| 100 | `4.634728988230` | `0.215762346092` | `1.431524692184` | `9.269457976459` | `9.269457976459` | `9.269457976459` |
| 10000 | `9.210640326985` | `0.108570084652` | `1.217140169304` | `18.421280653970` | `18.421280653970` | `18.421280653970` |
| 1e+06 | `13.815513557960` | `0.072382397933` | `1.144764795866` | `27.631027115920` | `27.631027115920` | `27.631027115920` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| CriticalStripConvexityGateActive | `true` | `false` | 上一层唯一内部最窄点是临界带 log\|zeta\|/log\|F\| 的显式凸性上界。 | CriticalStripConvexityLogZetaBoundNumericalLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| AnalyticEntireFAndPoleBudgetAvailable | `true` | `true` | 用 F=(s-1)zeta(s) 避开 s=1 极点；去极点水平预算已在上一层闭合。 | 无 pole obstruction。 |
| PhragmenLindelofThreeLinesClosed | `true` | `true` | 对整函数 F 在有限竖带内应用三线定理：log sup 在 sigma 方向由两侧边界对数凸控制。 | CriticalStripPhragmenLindelofThreeLinesClosed |
| RightBoundaryInputAvailable | `true` | `true` | 右边界 sigma=1+1/L 已有 Euler product 点态预算。 | ZetaRightEdgeEulerProductArgumentClosedCright2 |
| LeftBoundaryFunctionalEquationMissing | `false` | `false` | 仍需用函数方程和 Gamma/Stirling 预算给左边界 F 的 O(log(T+3)) 上界。 | FunctionalEquationLeftEdgeArgumentLedger |
| ConvexityC2ConstantOptimizationMissing | `false` | `false` | 即使左右边界都有 O(L)，仍需核算最小高度、eta=1/L、去极点项后是否能保住 C=2 目标。 | CriticalStripConvexityC2ConstantOptimizationLedger |
| CriticalStripConvexityReduced | `true` | `false` | 旧凸性原子已压成三线形式原理、右边界已证输入、左边界函数方程和常数优化。 | (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentLedger AND CriticalStripConvexityC2ConstantOptimizationLedger) |
| HorizontalAggregationStillDownstream | `false` | `false` | 凸性常数完成后，还需回到水平边聚合，再进入 Backlund 总常数。 | HorizontalVariationConstantAggregationLedger AND BacklundArgumentConstantAggregationLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentLedger AND CriticalStripConvexityC2ConstantOptimizationLedger) AND HorizontalVariationConstantAggregationLedger) AND FunctionalEquationLeftEdgeArgumentLedger AND BacklundArgumentConstantAggregationLedger) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `FunctionalEquationLeftEdgeArgumentLedger`；随后是 `CriticalStripConvexityC2ConstantOptimizationLedger`、`HorizontalVariationConstantAggregationLedger`、`BacklundArgumentConstantAggregationLedger`。
