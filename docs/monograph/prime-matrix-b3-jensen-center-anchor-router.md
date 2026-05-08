# Prime Matrix B=3 Backlund 独立 Jensen 圆心下界 anchor 路由器

**状态：** `backlund_independent_jensen_center_anchor_reduced_gamma_cancellation_open`

独立 Jensen 圆心下界 anchor 尚未闭合。本步确认关键障碍：不能用正的 xi 圆周上界直接扣圆心下界，必须先建立圆心选择和 Gamma 主项在 Jensen 平均中的有符号相消。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
backlund_independent_jensen_center_anchor_reduced=true
backlund_independent_jensen_center_anchor_self_contained_proved=false
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
BacklundIndependentJensenCenterLowerAnchorLedger
  =>
(BacklundJensenRightEdgeCenterChoiceConventionLedger AND BacklundJensenGammaMainCancellationInMeanLedger AND BacklundJensenRightEdgeEulerProductLowerBoundLedger AND BacklundJensenLowHeightCenterAnchorFiniteLedger AND BacklundJensenCenterLowerAnchorConstantAggregationLedger)
```

## 2. 当前障碍

xi 含有 Gamma 因子。若圆心在固定高度 `T`，`log|Gamma|` 的主衰减约为 `-pi*T/4`。Jensen 中正确做法是让圆周平均与圆心的 Gamma 主项有符号相消；只用 `log^+|xi|` 圆周上界会把这项变成线性假成本。

| T | log(T+3) | pi*T/4 | (pi*T/4)/log(T+3) |
| ---: | ---: | ---: | ---: |
| 10 | `2.564949357462` | `7.853981633974` | `3.062041599818` |
| 100 | `4.634728988230` | `78.539816339745` | `16.945935035081` |
| 10000 | `9.210640326985` | `7853.981633974483` | `852.707450855943` |
| 1e+06 | `13.815513557960` | `785398.163397448254` | `56849.002398824552` |

因此下一步不能直接用 `C_xi_boundary`；必须先闭合圆心选择与 Gamma 均值相消。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| JensenCenterAnchorGateActive | `true` | `false` | 上一层唯一内部最窄点是独立 Jensen 圆心下界 anchor。 | BacklundIndependentJensenCenterLowerAnchorLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| BoundaryJensenGammaEulerInputsAvailable | `true` | `true` | Jensen 公式、独立圆周上界、Gamma/digamma 和右边 Euler 输入均已可用。 | 无形式输入剩余。 |
| PositiveMajorantAloneInsufficient | `true` | `true` | 若只用 log^+ 圆周上界再减圆心下界，xi 的 Gamma 主衰减会制造约 pi*T/4 的线性假成本。 | BacklundJensenGammaMainCancellationInMeanLedger |
| CenterChoiceConventionMissing | `false` | `false` | 必须固定 Jensen 圆心与半径，使圆盘覆盖目标窗口且圆心落在可控非零锚线上。 | BacklundJensenRightEdgeCenterChoiceConventionLedger |
| GammaMeanCancellationMissing | `false` | `false` | 必须在 Jensen 平均中保留 Gamma/初等因子的有符号调和相消，不能只取 log^+ 上界。 | BacklundJensenGammaMainCancellationInMeanLedger |
| RightEdgeEulerLowerBoundMissing | `false` | `false` | 若圆心选在 sigma>1，需要 Euler product 给出 zeta 圆心下界。 | BacklundJensenRightEdgeEulerProductLowerBoundLedger |
| LowHeightCenterAnchorStillFinite | `false` | `false` | 低高度圆心还需有限非零 anchor 或 compact lower-bound 账本。 | BacklundJensenLowHeightCenterAnchorFiniteLedger |
| CenterAnchorConstantAggregationMissing | `false` | `false` | 最后要把圆心选择、Gamma 相消、Euler 下界和低高度 anchor 聚成 O(log(T+3)) 下界。 | BacklundJensenCenterLowerAnchorConstantAggregationLedger |
| IndependentJensenCenterAnchorReduced | `true` | `false` | 旧圆心 anchor 原子已压成圆心选择、Gamma 均值相消、右边 Euler 下界、低高度 anchor、常数聚合五包。 | (BacklundJensenRightEdgeCenterChoiceConventionLedger AND BacklundJensenGammaMainCancellationInMeanLedger AND BacklundJensenRightEdgeEulerProductLowerBoundLedger AND BacklundJensenLowHeightCenterAnchorFiniteLedger AND BacklundJensenCenterLowerAnchorConstantAggregationLedger) |
| JensenC16StillDownstream | `false` | `false` | anchor 完成后仍需把圆周上界和圆心下界压入局部零点计数 C_N=16。 | BacklundIndependentJensenZeroCountC16AggregationLedger AND BacklundNearZeroIndentSeparationLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND (BacklundJensenRightEdgeCenterChoiceConventionLedger AND BacklundJensenGammaMainCancellationInMeanLedger AND BacklundJensenRightEdgeEulerProductLowerBoundLedger AND BacklundJensenLowHeightCenterAnchorFiniteLedger AND BacklundJensenCenterLowerAnchorConstantAggregationLedger) AND BacklundIndependentJensenZeroCountC16AggregationLedger) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `BacklundJensenRightEdgeCenterChoiceConventionLedger`；随后是 `BacklundJensenGammaMainCancellationInMeanLedger`。
