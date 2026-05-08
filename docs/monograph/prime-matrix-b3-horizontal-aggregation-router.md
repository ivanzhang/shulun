# Prime Matrix B=3 水平边常数聚合闭合证书

**状态：** `horizontal_variation_constant_closed_c8`

水平边常数聚合已闭合为 C_horizontal=8。关键是用三线凸性给出的端点平均积分，而不是用临界带点态最大值粗乘宽度。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
horizontal_variation_constant_closed=true
C_horizontal=8.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
HorizontalVariationConstantAggregationLedger
  =>
HorizontalVariationConstantClosedC8
```

## 2. 核心不等式

```text
w=1+2/L, B_left=0.5L+log(T+2)+log(1+L), B_right=log(T+1)+log(1+L): two horizontal sides <= w*(B_left+B_right) < 8L for T>=2. For L>=2, this follows from w<=2 and log(1+L)/L<=log(3)/2. For 2<=T<=e^2-3, a finite grid plus |d margin/dT|<=10 closes the compact interval.
```

紧区间有限网格证书：

```text
compact_start=2.000000000000
compact_end=4.389056098931
grid_step=0.001000000000
derivative_bound=10.000000000000
grid_points=2392.000000000000
grid_min_margin=1.195913464862
grid_min_point=2.000000000000
certified_compact_margin=1.185913464862
```

尾区间解析证书：

```text
tail_start_T=4.389056098931
tail_start_L=2.000000000000
ratio_bound_for_two_horizontal_over_L=7.197224577336
tail_margin_factor=0.802775422664
```

## 3. 预算表

| T | L | width | B_left | B_right | two horizontal | 8L | margin | ratio |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | `1.609437912434` | `2.242669869119` | `3.150148156258` | `2.057747127589` | `11.679589834611` | `12.875503299473` | `1.195913464862` | `7.256937185571` |
| 3 | `1.791759469228` | `2.116221253102` | `3.531989678247` | `2.412966392319` | `12.580842385293` | `14.334075753824` | `1.753233368532` | `7.021501826198` |
| 5 | `2.079441541680` | `1.961796693926` | `4.110379182804` | `2.916507732137` | `13.785323518324` | `16.635532333439` | `2.850208815115` | `6.629339292312` |
| 10 | `2.564949357462` | `1.779742490503` | `5.038531176803` | `3.669045121083` | `15.497243526642` | `20.519594859692` | `5.022351333051` | `6.041929631694` |
| 100 | `4.634728988230` | `1.431524692184` | `8.671286359365` | `6.344069568807` | `21.494852773103` | `37.077831905837` | `15.582979132734` | `4.637779863222` |
| 10000 | `9.210640326985` | `1.217140169304` | `16.139290861351` | `11.533870712856` | `33.682116563608` | `73.685122615881` | `40.003006052274` | `3.656870246570` |
| 1e+06 | `13.815513557960` | `1.144764795866` | `23.418944182096` | `16.511186403117` | `45.710607788279` | `110.524108463678` | `64.813500675400` | `3.308643402687` |

## 4. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| HorizontalAggregationGateActive | `true` | `false` | 上一层唯一内部最窄点是水平边常数聚合。 | HorizontalVariationConstantAggregationLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| ConvexityAndHorizontalConventionsAvailable | `true` | `true` | C=2 凸性、水平边避零缩进和去极点预算均已闭合。 | 无输入剩余。 |
| EndpointAverageConvexityIntegralClosed | `true` | `true` | 由三线凸性，单条水平边积分不超过宽度乘左右端点上界平均。 | EndpointAverageConvexityIntegralClosed |
| TwoHorizontalScalarMarginClosed | `true` | `true` | 上下两条水平边合计 w(B_left+B_right) 小于 8L；低区间由有限网格+导数界支付，尾区间由 L>=2 的解析不等式支付。 | compact_margin=1.185913464862, tail_factor=0.802775422664 |
| HorizontalVariationConstantAggregationLedger | `true` | `true` | 水平边变化常数聚合闭合为 C_horizontal=8。 | HorizontalVariationConstantClosedC8 |
| BacklundAggregationStillNext | `false` | `false` | 下一步需要把 Littlewood、右边界、水平边、左边界等输入聚合为 Backlund/arg zeta 总常数。 | BacklundArgumentConstantAggregationLedger |

## 5. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND BacklundArgumentConstantAggregationLedger) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 6. 下一步

唯一内部最窄点更新为 `BacklundArgumentConstantAggregationLedger`。
