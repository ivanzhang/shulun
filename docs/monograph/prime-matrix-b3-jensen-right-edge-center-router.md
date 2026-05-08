# Prime Matrix B=3 Jensen 右边圆心选择 convention 闭合证书

**状态：** `backlund_jensen_right_edge_center_choice_closed_r4`

Jensen 右边圆心选择 convention 已闭合：取 z0=2+iT、外半径 R=4，目标局部零点窗口落在内半径 sqrt(5) 中。这只固定几何和非零圆心线，不闭合 Gamma 相消或数值 C_N。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
backlund_jensen_right_edge_center_choice_closed=true
sigma_center=2.000000000000
outer_radius=4.000000000000
target_radius=2.236067977500
jensen_log_ratio=0.581575404903
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
BacklundJensenRightEdgeCenterChoiceConventionLedger
  =>
BacklundJensenRightEdgeCenterChoiceConventionClosedR4
```

## 2. 圆盘几何

| item | value | meaning |
| --- | --- | --- |
| center | z0(T) = 2 + iT | 圆心放在 sigma=2 的 Euler product 非零线上。 |
| target strip | 0 <= beta <= 1, \|gamma-T\| <= 1 | 需要计数的局部非平凡零点窗口。 |
| target radius | sqrt((2-0)^2+1^2) = 2.236067977500 | 目标窗口完全包含在半径 r 的内圆盘。 |
| outer radius | R = 4.000000000000 | 固定外圆半径，给 Jensen 留出正的 log(R/r)。 |
| Jensen denominator | log(R/r) = 0.581575404903 | 该量为正，后续常数聚合可除以它。 |

圆心线 `sigma=2` 的非零性只用于 convention 合法性；定量下界仍在后续 Euler/Gamma anchor 中处理。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| RightEdgeCenterChoiceGateActive | `true` | `false` | 上一层唯一内部最窄点是 Jensen 右边圆心选择 convention。 | BacklundJensenRightEdgeCenterChoiceConventionLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| JensenBoundaryEulerInputsAvailable | `true` | `true` | Jensen 公式、独立圆周上界和 sigma=2 的 Euler product 输入均已可用。 | 无形式输入剩余。 |
| TargetWindowContainedInInnerDisk | `true` | `true` | 对任意 0<=beta<=1 且 \|gamma-T\|<=1 的零点，距 2+iT 至多 sqrt(5)<4。 | 无几何覆盖剩余。 |
| RightEdgeCenterNonzeroConvention | `true` | `true` | 圆心在 sigma=2，zeta 由 Euler product 非零，Gamma 与初等因子在该线上也非零。 | 定量下界仍由 Euler/Gamma anchor 支付。 |
| BacklundJensenRightEdgeCenterChoiceConventionLedger | `true` | `true` | Jensen 右边圆心选择 convention 闭合为 z0=2+iT、R=4、r=sqrt(5)。 | BacklundJensenRightEdgeCenterChoiceConventionClosedR4 |
| GammaCancellationStillNext | `false` | `false` | 圆心已固定后，下一步必须证明 Gamma 主项在 Jensen 平均中相消到 O(log(T+3))。 | BacklundJensenGammaMainCancellationInMeanLedger |
| EulerLowConstantStillDownstream | `false` | `false` | 还需右边 Euler 下界、低高度 anchor 与常数聚合。 | BacklundJensenRightEdgeEulerProductLowerBoundLedger AND BacklundJensenLowHeightCenterAnchorFiniteLedger AND BacklundJensenCenterLowerAnchorConstantAggregationLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND (BacklundJensenRightEdgeCenterChoiceConventionClosedR4 AND BacklundJensenGammaMainCancellationInMeanLedger AND BacklundJensenRightEdgeEulerProductLowerBoundLedger AND BacklundJensenLowHeightCenterAnchorFiniteLedger AND BacklundJensenCenterLowerAnchorConstantAggregationLedger) AND BacklundIndependentJensenZeroCountC16AggregationLedger) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `BacklundJensenGammaMainCancellationInMeanLedger`；随后是 `BacklundJensenRightEdgeEulerProductLowerBoundLedger`。
