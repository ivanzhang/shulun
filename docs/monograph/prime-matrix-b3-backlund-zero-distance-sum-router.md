# Prime Matrix B=3 Backlund 独立局部零点倒距离和路由器

**状态：** `backlund_independent_local_zero_distance_sum_reduced_open`

独立局部零点倒距离和尚未闭合。本步闭合了 dyadic 求和形式层，但真正硬点是独立 Jensen 圆盘零点计数；它必须不依赖 Backlund/RVM。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
backlund_independent_local_zero_distance_sum_reduced=true
backlund_independent_local_zero_distance_sum_self_contained_proved=false
C_zero_count_target=16.000000000000
C_distance_target=64.000000000000
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
BacklundIndependentLocalZeroDistanceSumLedger
  =>
(BacklundIndependentJensenDiskZeroCountLedger AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger)
```

## 2. dyadic 预算压力

| inner radius | shell count | zero-count constant | distance-sum candidate |
| ---: | ---: | ---: | ---: |
| `1.000000000000` | `1.000000000000` | `16.000000000000` | `64.000000000000` |
| `0.500000000000` | `2.000000000000` | `16.000000000000` | `96.000000000000` |
| `0.250000000000` | `3.000000000000` | `16.000000000000` | `128.000000000000` |
| `0.125000000000` | `4.000000000000` | `16.000000000000` | `160.000000000000` |
| `0.062500000000` | `5.000000000000` | `16.000000000000` | `192.000000000000` |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| ZeroDistanceSumGateActive | `true` | `false` | 上一层唯一内部最窄点是独立局部零点倒距离和。 | BacklundIndependentLocalZeroDistanceSumLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| HadamardNoCircularXiInputsAvailable | `true` | `true` | Hadamard 变差公式、非循环纪律和 xi 整函数增长输入均已可用。 | 无形式输入剩余。 |
| IndependentJensenDiskZeroCountMissing | `false` | `false` | 仍需独立 Jensen 圆盘零点计数；不得调用 RVM/Backlund 导出的局部零点计数。 | BacklundIndependentJensenDiskZeroCountLedger |
| ZeroDistanceDyadicSummationClosed | `true` | `true` | 一旦每个 dyadic 环的零点数有 O(log(T+3)) 上界，倒距离和由 dyadic 环求和转为常数聚合。 | BacklundZeroDistanceDyadicSummationClosed |
| NearZeroIndentSeparationMissing | `false` | `false` | 离中心过近的零点不能直接进倒距离和，必须切给凹口/端点成本账本。 | BacklundNearZeroIndentSeparationLedger |
| ZeroDistanceConstantAggregationMissing | `false` | `false` | 仍需把 Jensen 计数常数、dyadic 层数和近零截断合并为局部变差可用常数。 | BacklundZeroDistanceSumConstantAggregationLedger |
| IndependentLocalZeroDistanceSumReduced | `true` | `false` | 旧零点倒距离和原子已压成独立 Jensen 计数、dyadic 求和、近零分离、常数聚合四包。 | (BacklundIndependentJensenDiskZeroCountLedger AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) |
| WindowIndentSlackStillDownstream | `false` | `false` | 之后还需窗口尺度、凹口成本和 C_S=8 余量验收。 | BacklundVariationWindowScaleLedger AND BacklundZeroProximityIndentationCostLedger AND BacklundCS8SlackAfterBridgeLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND (BacklundIndependentJensenDiskZeroCountLedger AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `BacklundIndependentJensenDiskZeroCountLedger`；随后是 `BacklundNearZeroIndentSeparationLedger`、`BacklundZeroDistanceSumConstantAggregationLedger`。
