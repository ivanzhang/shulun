# Prime Matrix B=3 近零点缩进分离路由器

**状态：** `near_zero_indent_separation_external_closed_indent_cost_open`

近零点分离在外部 Backlund/Jensen 分支中已闭合为固定 eta=1/16 的记账规则：eta 外的零点进入有限 dyadic 倒距离常数聚合，eta 内的零点不估掉而转入凹口成本账本。因此本步关闭的是分区和无循环纪律，不关闭后续凹口成本。

```text
counterexample_assumption_only=true
empirical_absence_not_used=true
hypothetical_chain_only=true
near_zero_indent_separation_external_closed=true
near_zero_indent_separation_self_contained_closed=false
eta=0.062500000000
outer_radius=4.000000000000
dyadic_shells_from_outer_to_eta=6
row_column_unconditional_closed=false
```

## 1. 外部条件链替换

```text
BacklundNearZeroIndentSeparationLedger
  =>
BacklundNearZeroIndentSeparationClosedEta1Over16
```

该替换只说明近零点的归属，不支付凹口成本。

## 2. 分区表

| zone | condition | eta/value | handled by | effect |
| --- | --- | ---: | --- | --- |
| near-zero core | \|s-rho\| < eta | `0.062500000000` | BacklundZeroProximityIndentationCostLedger | 不进入倒距离 dyadic 求和，等待凹口成本账本支付。 |
| safe dyadic annuli | eta <= \|s-rho\| <= 4 | `0.062500000000` | BacklundZeroDistanceSumConstantAggregationLedger | 固定有限层 dyadic 环；每层调用 Jensen C16 计数。 |
| outside disk | \|s-rho\| > 4 | `0.062500000000` | Hadamard remainder / outer tail | 不属于局部 Jensen 圆盘倒距离硬点。 |
| available zero count | N(D)<=C_N log(T+3) | `16.000000000000` | external Jensen C16 aggregation | 外部分支已关闭；自足分支仍等低高度零点账本。 |

## 3. 判定表

| gate | closed | proved | meaning | remaining |
| --- | --- | --- | --- | --- |
| NearZeroIndentSeparationGateActive | `true` | `false` | 外部 Backlund/Jensen 分支当前最窄点是把过近零点从倒距离和中剥离。 | BacklundNearZeroIndentSeparationLedger |
| CounterexampleBranchGuardPreserved | `true` | `true` | 本步仍只处理假设链条内的解析记账，不使用真实零行缺席。 | 保持 row_column_unconditional_closed=false。 |
| JensenC16ZeroCountAvailableExternally | `true` | `false` | 外部分支已有 Jensen C16 局部零点计数；它只给数量，不处理路径贴近零点的奇性。 | BacklundIndependentJensenZeroCountC16AggregationExternalClosed |
| FixedEtaIndentConventionClosed | `true` | `true` | 固定 eta=1/16；\|s-rho\|<eta 的零点统一交给凹口成本，不进入倒距离主和。 | BacklundNearZeroIndentSeparationClosedEta1Over16 |
| SafeDyadicAnnuliRemainFinite | `true` | `true` | eta 到外半径 4 之间只有固定 6 层 dyadic 环，因此不会引入额外 log log 或可变层数。 | BacklundZeroDistanceSumConstantAggregationLedger |
| NearZerosAssignedToIndentCostLedger | `true` | `true` | 近零点没有被丢弃；它们被保留为零点邻近凹口成本账本的输入。 | BacklundZeroProximityIndentationCostLedger |
| NearZeroIndentSeparationClosed | `true` | `true` | 近零/远零分区完成：远零点可做 dyadic 倒距离常数聚合，近零点转入凹口成本。 | BacklundNearZeroIndentSeparationClosedEta1Over16 |
| ZeroDistanceConstantAggregationNext | `false` | `false` | 近零分离后，下一步要合并 dyadic 层数、Jensen C16 常数和 eta 截断常数。 | BacklundZeroDistanceSumConstantAggregationLedger |
| IndentCostStillDownstream | `false` | `false` | 凹口成本本身还未支付；它是后续尖峰排斥闭合的独立账本。 | BacklundZeroProximityIndentationCostLedger |

## 4. 最新输入基

canonical 自足链条输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND BacklundIndependentJensenCenterLowerAnchorClosedSymbolic AND (BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7 AND (BacklundJensenLowHeightDiskImaginaryRangeClosedT14 AND (BacklundXiZetaNontrivialZeroEquivalenceClosed AND CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger) AND BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14) AND BacklundJensenRadiusOptimizationOrCNRelaxationLedger)) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationLedger AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

conditional/external Backlund 输入基：

```text
NoFurtherCanonicalSourceTerminalPromotionGap AND ((((B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND (B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND (B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND (SmoothChebyshevExplicitFormulaAppendixClosed AND PrimePowerThetaPsiTransferLedgerClosed AND ((GaussianPoissonThetaIdentityClosed AND ThetaMellinZetaContinuationFunctionalEquationClosed AND XiEntireOrderOneGrowthClosed AND HadamardFactorizationLogDerivativeClosed) AND EulerProductLogDerivativePositiveRealPartClosed AND DeLaValleePoussinTrigonometricKernelIdentityClosed AND DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants AND ((GammaDigammaStirlingUniformNumericalClosedCgamma24 AND ((ArgumentPrincipleXiRectangleCountingClosed AND GammaMainTermLocalDifferenceNumericalClosedCmain4 AND (BacklundLittlewoodRectangleArgumentClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND (HorizontalZeroIndentationConventionClosed AND HorizontalPoleRemovalBudgetClosed AND (CriticalStripPhragmenLindelofThreeLinesClosed AND ZetaRightEdgeEulerProductArgumentClosedCright2 AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND CriticalStripConvexityClosedC2) AND HorizontalVariationConstantClosedC8) AND FunctionalEquationLeftEdgeArgumentClosedCleft4 AND (BacklundBoundaryConstantSumClosedC16 AND (BacklundArgumentBranchNormalizationClosed AND BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability AND (BacklundSpikeNoRVMCircularityDisciplineClosed AND (BacklundHadamardLogDerivativeVariationFormulaClosed AND ((BacklundJensenDiskFormulaClosed AND BacklundIndependentXiDiskBoundaryMajorantClosedSymbolic AND BacklundIndependentJensenCenterLowerAnchorClosedSymbolic AND (BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7 AND (BacklundJensenLowHeightDiskImaginaryRangeClosedT14 AND (BacklundXiZetaNontrivialZeroEquivalenceClosed AND ClassicalFirstZetaZeroHeightGT14ExternalAccepted AND BacklundXiNoNontrivialZeroBelow14ExternalClosed) AND BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14) AND BacklundJensenRadiusOptimizationNotNeededC16ClosedR4)) AND BacklundZeroDistanceDyadicSummationClosed AND BacklundNearZeroIndentSeparationClosedEta1Over16 AND BacklundZeroDistanceSumConstantAggregationLedger) AND BacklundVariationWindowScaleLedger) AND BacklundZeroProximityIndentationCostLedger)) AND BacklundCS8SlackAfterBridgeLedger)) AND EndpointZeroAvoidanceMultiplicityConventionLedger AND RVMToCN16LocalInequalityLedger) AND XiBoundaryLogMajorantNumericalLedger AND JensenDiskLowerAnchorNumericalLedger AND LocalZeroCountCNConventionLedger) AND HadamardPartialFractionRemainderNumericalLedger AND CLogAggregationAndRangeConventionLedger) AND ZeroRepulsionParameterNumericalOptimizationLedger AND ZeroFreeRegionToExplicitPNTContourConstantLedger AND ThetaEnvelopeTargetAt20000NumericalBudgetLedger) AND FiniteLowHeightZeroCheckLedger) AND ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion AND FiniteThetaEnvelopeBridgeBelowAnalyticThreshold) AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000))) AND (B3RosserFaceDictionaryClosedAlpha043 AND B3Anchor20000BoundaryVariationBudgetClosedAlpha043)) OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043)) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance
```

## 5. 下一步

完全自足路线仍先攻 `CriticalLineNoZeroOn0To14FiniteLedger`；外部 Backlund/Jensen 分支下一步转为 `BacklundZeroDistanceSumConstantAggregationLedger`。
