# Prime Matrix B=3 Backlund 独立 Jensen 圆盘零点计数路由器

**状态：** `backlund_independent_jensen_disk_zero_count_reduced_open`

独立 Jensen 圆盘零点计数尚未闭合。本步闭合 Jensen 公式形式层，剩余是独立圆周上界、圆心下界和 C16 常数聚合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
backlund_independent_jensen_reduced=true
backlund_independent_jensen_self_contained_proved=false
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
BacklundIndependentJensenDiskZeroCountLedger
  =>
(BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantLedger AND BacklundIndependentJensenCenterLowerAnchorLedger AND BacklundIndependentJensenZeroCountC16AggregationLedger)
```

## 2. Jensen 公式

```text
N(r) log(R/r) <= (1/2pi) int_0^{2pi} log|xi(z0+R e^{i theta})| dtheta - log|xi(z0)|
```

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| IndependentJensenGateActive | `true` | `false` | 上一层唯一内部最窄点是独立 Jensen 圆盘零点计数。 | BacklundIndependentJensenDiskZeroCountLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| XiEntireAndNoCircularAvailable | `true` | `true` | xi 整函数增长与非循环纪律已可用。 | 无形式输入剩余。 |
| JensenDiskFormulaClosed | `true` | `true` | Jensen 公式把圆盘内零点数控制为圆周 log\|xi\| 上界减圆心 log\|xi\| 下界。 | BacklundJensenDiskFormulaClosed |
| IndependentBoundaryMajorantMissing | `false` | `false` | 仍需独立圆周上界，不能从待证 Backlund/RVM 取零点计数。 | BacklundIndependentXiDiskBoundaryMajorantLedger |
| IndependentCenterLowerAnchorMissing | `false` | `false` | 仍需圆心处 xi 不过小的显式下界，避免 Jensen 只给上界不计数。 | BacklundIndependentJensenCenterLowerAnchorLedger |
| JensenC16AggregationMissing | `false` | `false` | 仍需把圆周上界和圆心下界合并成局部零点计数常数 C_N=16。 | BacklundIndependentJensenZeroCountC16AggregationLedger |
| IndependentJensenReduced | `true` | `false` | 旧独立 Jensen 原子已压成 Jensen 公式、圆周上界、圆心下界、C16 聚合四包。 | (BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantLedger AND BacklundIndependentJensenCenterLowerAnchorLedger AND BacklundIndependentJensenZeroCountC16AggregationLedger) |
| ZeroDistanceDownstreamStillOpen | `false` | `false` | Jensen 计数完成后仍需近零分离、倒距离常数聚合和窗口尺度。 | BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger AND BacklundVariationWindowScaleLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantLedger AND BacklundIndependentJensenCenterLowerAnchorLedger AND BacklundIndependentJensenZeroCountC16AggregationLedger) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `BacklundIndependentXiDiskBoundaryMajorantLedger`；随后是 `BacklundIndependentJensenCenterLowerAnchorLedger`、`BacklundIndependentJensenZeroCountC16AggregationLedger`。
