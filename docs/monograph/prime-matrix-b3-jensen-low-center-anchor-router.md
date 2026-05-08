# Prime Matrix B=3 Jensen 低高度圆心 anchor 闭合证书

**状态：** `backlund_jensen_low_height_center_anchor_compact_nonzero_closed`

Jensen 低高度圆心 anchor 已以紧致非零下界闭合。这给出正的符号常数 m_xi_center_low；数值大小仍由下一步 anchor 常数聚合支付。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
backlund_jensen_low_center_anchor_closed=true
sigma_center=2.000000000000
low_height_ceiling=10.000000000000
low_log_floor=1.098612288668
row_column_unconditional_closed=false
```

## 1. 自足替换

```text
BacklundJensenLowHeightCenterAnchorFiniteLedger
  =>
BacklundJensenLowHeightCenterAnchorCompactNonzeroClosed
```

## 2. 低高度紧致下界

```text
m_xi_center_low := inf_{|T|<=10} |xi(2+iT)| > 0
A_center_low := -log(m_xi_center_low) < infinity
```

| component | fact | role |
| --- | --- | --- |
| center line | z0(T)=2+iT, \|T\|<=10 is compact | 圆心参数集是紧集。 |
| zeta factor | \|zeta(2+iT)\|>=1/zeta(2) | 低高度也沿用右边 Euler 下界，且无零。 |
| Gamma factor | Gamma(1+iT/2) has no zero or pole on \|T\|<=10 | 连续非零，紧集上最小模为正。 |
| elementary factor | s(s-1) and pi^{-s/2} are nonzero on s=2+iT | 连续非零，紧集上最小模为正。 |
| low anchor | m_xi_center_low := inf_{\|T\|<=10} \|xi(2+iT)\| > 0 | 低高度圆心下界闭合为有限正常数。 |

这里不调用低高度零点表；圆心固定在 `sigma=2`，非零性来自绝对收敛 Euler product 和 Gamma 无零。

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| LowCenterAnchorGateActive | `true` | `false` | 上一层唯一内部最窄点是 Jensen 低高度圆心 anchor。 | BacklundJensenLowHeightCenterAnchorFiniteLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条的解析输入，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| CenterEulerXiInputsAvailable | `true` | `true` | 右边圆心 convention、Euler 下界和 xi 基础输入均已可用。 | 无形式输入剩余。 |
| LowCenterCompactNonzeroClosed | `true` | `true` | 在 \|T\|<=10 的紧圆心线上，xi(2+iT) 由非零连续因子相乘，故最小模为正。 | BacklundJensenLowHeightCenterAnchorCompactNonzeroClosed |
| BacklundJensenLowHeightCenterAnchorFiniteLedger | `true` | `true` | 低高度圆心 anchor 已闭合为正的紧致下界常数 m_xi_center_low。 | BacklundJensenLowHeightCenterAnchorCompactNonzeroClosed |
| AnchorConstantAggregationStillNext | `false` | `false` | 下一步需把高高度相消、Euler 常数和低高度 anchor 聚合为统一 O(log(T+3)) 下界。 | BacklundJensenCenterLowerAnchorConstantAggregationLedger |
| JensenC16StillDownstream | `false` | `false` | anchor 聚合后仍需 Jensen C_N=16 数值聚合。 | BacklundIndependentJensenZeroCountC16AggregationLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND (BacklundJensenRightEdgeCenterChoiceConventionClosedR4 AND BacklundJensenGammaMainCancellationInMeanClosedHighT10R4 AND BacklundJensenRightEdgeEulerProductLowerBoundClosedZeta2 AND BacklundJensenLowHeightCenterAnchorCompactNonzeroClosed AND BacklundJensenCenterLowerAnchorConstantAggregationLedger) AND BacklundIndependentJensenZeroCountC16AggregationLedger) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

唯一内部最窄点更新为 `BacklundJensenCenterLowerAnchorConstantAggregationLedger`；随后是 `BacklundIndependentJensenZeroCountC16AggregationLedger`。
