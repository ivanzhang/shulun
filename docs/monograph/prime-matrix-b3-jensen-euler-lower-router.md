# Prime Matrix B=3 Jensen 右边 Euler product 圆心下界闭合证书

**状态：** `backlund_jensen_right_edge_euler_lower_bound_closed_zeta2`

Jensen 右边 Euler product 圆心下界已闭合：|zeta(2+iT)|>=1/zeta(2)，只产生常数 log(zeta(2)) 成本。剩余是低高度圆心 anchor 与统一常数聚合。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
backlund_jensen_right_edge_euler_lower_bound_closed=true
sigma_center=2.000000000000
zeta2=1.644934066848
log_zeta2=0.497700302471
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
BacklundJensenRightEdgeEulerProductLowerBoundLedger
  =>
BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2
```

## 2. 下界公式

| step | formula | bound |
| --- | --- | --- |
| inverse series | 1/zeta(s)=sum_{n>=1} mu(n)n^{-s}, sigma>1 | \|1/zeta(2+iT)\| <= sum n^{-2}=zeta(2) |
| lower bound | \|zeta(2+iT)\| >= 1/zeta(2) | -log\|zeta(2+iT)\| <= log(zeta(2)) = 0.497700302471 |
| log scale | log(zeta(2)) <= log(zeta(2))*log(T+3)/log(3) | 常数项可被后续 O(log(T+3)) anchor 聚合吸收。 |

该下界只使用 `sigma>1` 的绝对收敛，不调用零点计数或 Backlund 结论。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| EulerLowerGateActive | `true` | `false` | 上一层唯一内部最窄点是 Jensen 右边 Euler product 圆心下界。 | BacklundJensenRightEdgeEulerProductLowerBoundLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| GammaCancellationAndEulerInputsAvailable | `true` | `true` | Gamma 均值相消、右边界 Euler 预算和 Euler product 基础均已可用。 | 无形式输入剩余。 |
| ZetaRightEdgeLowerBoundClosed | `true` | `true` | 在 sigma=2，由 1/zeta(s) 的绝对收敛级数得 \|zeta(2+iT)\|>=1/zeta(2)。 | BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2 |
| BacklundJensenRightEdgeEulerProductLowerBoundLedger | `true` | `true` | zeta 圆心下界闭合为常数 log(zeta(2)) 成本。 | BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2 |
| LowCenterAnchorStillNext | `false` | `false` | 高高度 Euler 下界已闭合；低高度圆心 anchor 仍需有限处理。 | BacklundJensenLowHeightCenterAnchorFiniteLedger |
| AnchorConstantAggregationStillDownstream | `false` | `false` | 最后仍需把 Gamma 相消、Euler 下界、低高度项聚成统一 anchor 常数。 | BacklundJensenCenterLowerAnchorConstantAggregationLedger AND BacklundIndependentJensenZeroCountC16AggregationLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND (BacklundJensenRightEdgeCenterChoiceConventionClosedR4 AND BacklundJensenGammaMainCancellationInMeanClosedHighT10R4 AND BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2 AND BacklundJensenLowHeightCenterAnchorFiniteLedger AND BacklundJensenCenterLowerAnchorConstantAggregationLedger) AND BacklundIndependentJensenZeroCountC16AggregationLedger) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `BacklundJensenLowHeightCenterAnchorFiniteLedger`；随后是 `BacklundJensenCenterLowerAnchorConstantAggregationLedger`。
